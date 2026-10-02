"""Tests for tools/guard_holdout.py and tools/board.py.

Run: python -m unittest discover -s tools/tests
"""
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

TOOLS = pathlib.Path(__file__).resolve().parent.parent
H = "eval/" + "hold" + "out"  # built in pieces so this file never names the folder literally


def guard(tool, **tool_input):
    p = subprocess.run([sys.executable, str(TOOLS / "guard_holdout.py")],
                       input=json.dumps({"tool_name": tool, "tool_input": tool_input}),
                       capture_output=True, text=True)
    return p.returncode


class GuardHoldout(unittest.TestCase):
    def test_blocks_reading(self):
        self.assertEqual(guard("Read", file_path=f"D:/repo/{H}/a/document.md"), 2)
        self.assertEqual(guard("Bash", command=f"cat {H}/a/document.md"), 2)
        self.assertEqual(guard("Grep", pattern="x", path=H), 2)
        self.assertEqual(guard("Glob", pattern=f"{H}/**/*.md"), 2)

    def test_blocks_chaining_after_a_safe_command(self):
        self.assertEqual(guard("Bash", command=f"git status && cat {H}/a.md"), 2)
        self.assertEqual(guard("Bash", command=f"python tools/eval_score.py; cat {H}/a.md"), 2)
        self.assertEqual(guard("Bash", command=f"git log --oneline | cat {H}/a.md"), 2)
        self.assertEqual(guard("Bash", command=f"git commit -m 'x' && cat {H}/a.md"), 2)
        self.assertEqual(guard("Bash", command=f"git commit -F {H}/a.md"), 2)

    def test_allows_safe_and_unrelated(self):
        self.assertEqual(guard("Bash", command=f"python tools/eval_score.py --set {H}"), 0)
        self.assertEqual(guard("Bash", command=f"git commit -m 'Note about {H}'"), 0)
        self.assertEqual(guard("Bash", command=f"git add {H}"), 0)
        self.assertEqual(guard("Edit", file_path="docs/rules.md", new_string=f"mentions {H}"), 0)
        self.assertEqual(guard("Read", file_path="docs/rules.md"), 0)
        self.assertEqual(guard("Bash", command="ls eval/batch-1"), 0)


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
