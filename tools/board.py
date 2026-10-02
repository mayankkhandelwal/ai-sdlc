"""Show the plan's state: what is ready, doing, in review, blocked or waiting for a person.

Reads plans/tasks/*.md (Status and Depends on lines). Also warns about tasks in
review without an audit file and done tasks with an empty Proof section.

Usage: python tools/board.py            summary + ready list
       python tools/board.py E-07       one epic in detail
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TASKS = ROOT / "plans" / "tasks"
AUDITS = ROOT / "plans" / "audits"
FIELD = re.compile(r"^- \*\*(\w[\w ]*):\*\* (.*)$")


def load():
    tasks = {}
    for f in sorted(TASKS.glob("T-*.md")):
        text = f.read_text(encoding="utf-8")
        fields = {}
        for line in text.splitlines():
            m = FIELD.match(line)
            if m:
                fields[m.group(1).lower()] = m.group(2).strip()
        tid = f.name.split("-", 2)
        tid = f"{tid[0]}-{tid[1]}"
        title = text.splitlines()[0].split("·", 1)[-1].strip()
        deps = [d.strip() for d in fields.get("depends on", "—").split(",") if d.strip() not in ("—", "")]
        proof = text.split("## Proof", 1)[-1].split("## ", 1)[0].strip()
        tasks[tid] = {
            "file": f, "title": title, "status": fields.get("status", "todo"),
            "role": fields.get("role", ""), "owner": fields.get("owner", ""),
            "epic": tid.split(".")[0].replace("T-", "E-"), "deps": deps,
            "proof_empty": proof.startswith("_") or not proof,
        }
    return tasks


PASS = re.compile(r"Result:?\**\s*:?\s*PASS", re.IGNORECASE)
SATISFIED = ("done", "skipped")


def passed_audit(tid):
    """True if any audit file for this task records Result: PASS."""
    for f in AUDITS.glob(f"{tid}*.md"):
        if PASS.search(f.read_text(encoding="utf-8")):
            return True
    return False


def find_cycles(tasks):
    state, stack, cycles = {}, [], []

    def visit(tid):
        state[tid] = "visiting"
        stack.append(tid)
        for d in tasks[tid]["deps"]:
            if d not in tasks:
                continue
            if state.get(d) == "visiting":
                cycles.append(stack[stack.index(d):] + [d])
            elif d not in state:
                visit(d)
        stack.pop()
        state[tid] = "done"

    for tid in tasks:
        if tid not in state:
            visit(tid)
    return cycles


def main():
    tasks = load()
    only = sys.argv[1] if len(sys.argv) > 1 else None
    by_status = {}
    for tid, t in tasks.items():
        by_status.setdefault(t["status"], []).append(tid)

    if only:
        print(f"{only}")
        for tid, t in tasks.items():
            if t["epic"] == only:
                print(f"  {tid:8} {t['status']:11} {t['role']:8} {t['title']}  (deps: {', '.join(t['deps']) or '—'})")
        return 0

    total = len(tasks)
    print(f"Tasks: {total}  " + "  ".join(f"{s}: {len(v)}" for s, v in sorted(by_status.items())))
    for label in ("doing", "review", "blocked", "needs-human"):
        if by_status.get(label):
            print(f"\n{label.upper()}")
            for tid in by_status[label]:
                print(f"  {tid:8} {tasks[tid]['owner']:14} {tasks[tid]['title']}")

    ready = [tid for tid, t in tasks.items() if t["status"] == "todo"
             and all(tasks.get(d, {}).get("status") in SATISFIED for d in t["deps"])]
    print("\nREADY TO START")
    for tid in ready:
        t = tasks[tid]
        print(f"  {tid:8} {t['role']:8} {t['owner']:14} {t['title']}")

    warnings = []
    for tid, t in tasks.items():
        audited = passed_audit(tid)
        if t["status"] == "review" and not audited:
            warnings.append(f"{tid} is in review and has no passed audit yet")
        if t["status"] == "done" and t["role"] not in ("Human", "Auditor") and not audited:
            warnings.append(f"{tid} is done without a passed audit")
        if t["status"] == "done" and t["proof_empty"] and t["role"] != "Human":
            warnings.append(f"{tid} is done but its Proof section is empty")
        for d in t["deps"]:
            if d not in tasks:
                warnings.append(f"{tid} depends on unknown task {d}")
    for cycle in find_cycles(tasks):
        warnings.append("dependency cycle: " + " -> ".join(cycle))
    if warnings:
        print("\nWARNINGS")
        for w in warnings:
            print(f"  {w}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
