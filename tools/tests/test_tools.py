"""Tests for tools/guard_holdout.py and tools/board.py.

Run: python -m unittest discover -s tools/tests
"""
import json
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

TOOLS = pathlib.Path(__file__).resolve().parent.parent
NAME = "AI_SDLC" + "_hold" + "out"          # built in pieces so this file never names the folder in one piece
PATHS = json.loads((TOOLS / "paths.json").read_text(encoding="utf-8"))
H = PATHS["holdout_dir"]                    # configured hold-out location
WORK = str(pathlib.Path(H).parent)          # its parent folder


def guard(tool, cwd=None, **tool_input):
    env = dict(os.environ)
    env.pop("HOLDOUT" + "_DIR", None)
    payload = {"tool_name": tool, "tool_input": tool_input}
    if cwd:
        payload["cwd"] = cwd
    p = subprocess.run([sys.executable, str(TOOLS / "guard_holdout.py")],
                       input=json.dumps(payload), capture_output=True, text=True, env=env)
    return p.returncode


class GuardHoldout(unittest.TestCase):
    def test_blocks_file_tools(self):
        self.assertEqual(guard("Read", file_path=f"{H}/a/document.md"), 2)
        self.assertEqual(guard("Read", file_path=f"D:\\AI-Job\\{NAME.lower()}\\a\\document.md"), 2)
        self.assertEqual(guard("Read", file_path=f"D:/AI-Job/./{NAME}/a.md"), 2)
        self.assertEqual(guard("Edit", file_path=f"{H}/a.md", old_string="x", new_string="y"), 2)
        self.assertEqual(guard("NotebookEdit", notebook_path=f"{H}/n.ipynb"), 2)

    def test_blocks_search_tools(self):
        self.assertEqual(guard("Grep", pattern="x", path=H), 2)
        self.assertEqual(guard("Grep", pattern="x", path="D:/AI-Job", glob=f"{NAME}/**"), 2)
        self.assertEqual(guard("Glob", pattern=f"{H}/**/*.md"), 2)

    def test_blocks_shell(self):
        for cmd in [f"cat {H}/a.md", f"git status && cat {H}/a.md",
                    f"python tools/eval_score.py; cat {H}/a.md", f"python tools/eval_score.py --set {H} | cat",
                    f"python tools/eval_score.py --set $(cat {H}/a.md)", f"python -c \"open('{H}/a.md').read()\"",
                    f"python other/tools/eval_score.py --set {H}", f"cd {H} && cat a.md",
                    f"Get-Content {H}/a.md"]:
            self.assertEqual(guard("Bash", command=cmd), 2, cmd)
        self.assertEqual(guard("PowerShell", command=f"Get-Content {H}\\a.md"), 2)
        env = "HOLDOUT" + "_DIR"
        self.assertEqual(guard("Bash", command=f'cat "${env}"/a/document.md'), 2)
        self.assertEqual(guard("PowerShell", command=f"Get-ChildItem $env:{env}"), 2)
        self.assertEqual(guard("Bash", command=f"python tools/eval_score.py --set ${env}"), 2)
        self.assertEqual(guard("Bash", command="grep -r secret .."), 2)
        self.assertEqual(guard("Bash", command="find .. -name '*.md'"), 2)

    def test_blocks_parent_searches(self):
        repo = str(TOOLS.parent)
        worktree = f"{WORK}/worktrees/t-02-2"
        self.assertEqual(guard("Grep", pattern="x", path="../..", cwd=worktree), 2)
        self.assertEqual(guard("Grep", pattern="x", path=WORK), 2)
        self.assertEqual(guard("Glob", pattern="*.md", path=WORK), 2)
        self.assertEqual(guard("Grep", pattern="x", path="eval", cwd=repo), 0)

    def test_paths_config_is_used(self):
        self.assertTrue(H.endswith(NAME))
        self.assertNotIn("AI-Job", H, "hold-out must not live in D:/AI-Job")
        self.assertNotIn("AI-Job", PATHS["worktrees_dir"], "worktrees must not live in D:/AI-Job")

    def test_fails_closed_on_bad_input(self):
        p = subprocess.run([sys.executable, str(TOOLS / "guard_holdout.py")], input="not json",
                           capture_output=True, text=True)
        self.assertEqual(p.returncode, 2)

    def test_fails_closed_on_hang(self):
        # stdin is never closed, so the guard waits forever; its timer must block the call
        p = subprocess.Popen([sys.executable, str(TOOLS / "guard_holdout.py")], stdin=subprocess.PIPE,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        try:
            self.assertEqual(p.wait(timeout=20), 2)
        finally:
            p.kill()
            p.stdin.close()

    def test_hook_command_fails_closed(self):
        settings = json.loads((TOOLS.parent / ".claude" / "settings.json").read_text(encoding="utf-8"))
        hooks = [h for entry in settings["hooks"]["PreToolUse"] for h in entry["hooks"]
                 if "guard_holdout.py" in h["command"]]
        self.assertEqual(len(hooks), 1)
        self.assertTrue(hooks[0]["command"].rstrip().endswith("|| exit 2"))
        src = (TOOLS / "guard_holdout.py").read_text(encoding="utf-8")
        timer = int(src.split("TIMER_SECONDS = ")[1].split()[0])
        self.assertLess(timer, hooks[0]["timeout"])

    def test_scorer_only_from_repo(self):
        self.assertEqual(guard("Bash", cwd=str(TOOLS.parent), command=f"python tools/eval_score.py --set {H}"), 0)
        self.assertEqual(guard("Bash", cwd=str(TOOLS.parent.parent), command=f"python tools/eval_score.py --set {H}"), 2)

    def test_allows_scorer_and_unrelated(self):
        self.assertEqual(guard("Bash", cwd=str(TOOLS.parent), command=f"python tools/eval_score.py --set {H} --runs 3"), 0)
        self.assertEqual(guard("Bash", command=f"python tools/eval_score.py --set {H}"), 2)  # no cwd: not allowed
        self.assertEqual(guard("Read", file_path="docs/rules.md"), 0)
        self.assertEqual(guard("Edit", file_path="docs/rules.md", old_string="a", new_string="b"), 0)
        self.assertEqual(guard("Bash", command="ls eval/batch-1"), 0)
        self.assertEqual(guard("Grep", pattern="x", path="eval"), 0)


def write_task(d, tid, status="todo", deps="—", role="Builder", proof="_x_"):
    (d / f"{tid}-x.md").write_text(
        f"# {tid} · t\n\n- **Role:** {role}\n- **Owner:** o\n- **Depends on:** {deps}\n- **Status:** {status}\n\n## Proof\n\n{proof}\n\n## Plan\n",
        encoding="utf-8")


class Board(unittest.TestCase):
    def run_board(self, setup, check):
        """Build a temporary plan, point board.py at it, and run check(board, tasks) inside."""
        sys.path.insert(0, str(TOOLS))
        import board
        with tempfile.TemporaryDirectory() as tmp:
            tasks = pathlib.Path(tmp) / "tasks"
            audits = pathlib.Path(tmp) / "audits"
            tasks.mkdir()
            audits.mkdir()
            setup(tasks, audits)
            board.TASKS, board.AUDITS = tasks, audits
            check(board, board.load())

    def test_ready_needs_done_or_skipped_deps(self):
        def setup(t, a):
            write_task(t, "T-01.1", "done", proof="ok")
            write_task(t, "T-01.2", "skipped")
            write_task(t, "T-01.3", "todo", "T-01.1, T-01.2")
            write_task(t, "T-01.4", "todo", "T-01.3")

        def check(board, tasks):
            ready = [k for k, v in tasks.items() if v["status"] == "todo"
                     and all(tasks[d]["status"] in board.SATISFIED for d in v["deps"])]
            self.assertEqual(ready, ["T-01.3"])
        self.run_board(setup, check)

    def test_only_pass_audits_count(self):
        def setup(t, a):
            (a / "T-02.1-audit-1-fail.md").write_text("- Result: FAIL\n", encoding="utf-8")
            (a / "T-02.2.md").write_text("- Result: PASS\n", encoding="utf-8")

        def check(board, tasks):
            self.assertFalse(board.passed_audit("T-02.1"))
            self.assertTrue(board.passed_audit("T-02.2"))
        self.run_board(setup, check)

    def test_finds_cycles(self):
        def setup(t, a):
            write_task(t, "T-03.1", deps="T-03.2")
            write_task(t, "T-03.2", deps="T-03.1")

        self.run_board(setup, lambda board, tasks: self.assertTrue(board.find_cycles(tasks)))


if __name__ == "__main__":
    unittest.main()
