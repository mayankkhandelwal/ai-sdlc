"""Claude Code PreToolUse hook: keep the hold-out set unseen (rule R2).

The hold-out set lives OUTSIDE this repo. Its folder is given by the HOLDOUT_DIR
environment variable (default: a sibling folder of the repo; see eval/README.md).
This hook blocks any tool call that points at that folder:
- Read, Edit, Write, NotebookEdit: by file or notebook path
- Grep, Glob, Bash, PowerShell, and any other tool: anywhere in the call's input
The only exception is one plain call of the scoring script, which prints summary
scores only: `python tools/eval_score.py <args>` with no chaining, pipes,
redirects or substitution.

Paths are compared after normalising case, slashes, quotes and "./" segments.
Exit code 2 blocks the call and shows the reason.

Known limits (documented in docs/rules.md, R2): a hook only sees the text of a
call. Code that builds the folder name from pieces, or that searches the whole
disk, is not caught. The folder being outside the repo is the main protection.
"""
import json
import os
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_NAME = "AI_SDLC" + "_hold" + "out"
HOLDOUT_DIR = os.environ.get("HOLDOUT_DIR") or str(REPO.parent / DEFAULT_NAME)
PATH_FIELDS = ("file_path", "notebook_path")
SCORER = re.compile(r"^\s*python3?\s+(\./)?tools/eval_score\.py(\s+[\w.=:/,-]+)*\s*$")
UNSAFE = re.compile(r"[;&|`<>\n\r]|\$\(|\$\{")
MESSAGE = ("Blocked by rule R2: the hold-out set must stay unseen. "
           "Only `python tools/eval_score.py` may read it (summary scores only).")


def norm(text):
    t = str(text).lower().replace("\\\\", "/").replace("\\", "/")
    t = t.replace('"', "").replace("'", "")
    t = re.sub(r"/(\./)+", "/", t)
    t = re.sub(r"/{2,}", "/", t)
    return t


TARGET_NAME = norm(pathlib.Path(HOLDOUT_DIR).name)


def mentions_holdout(text):
    return TARGET_NAME in norm(text)


def blocked(tool, tool_input):
    if tool in ("Read", "Edit", "Write", "NotebookEdit"):
        return any(mentions_holdout(tool_input.get(f, "")) for f in PATH_FIELDS)
    if tool in ("Bash", "PowerShell"):
        cmd = str(tool_input.get("command", ""))
        if not mentions_holdout(cmd):
            return False
        return not (SCORER.match(norm(cmd)) and not UNSAFE.search(cmd))
    return mentions_holdout(json.dumps(tool_input))


def main():
    raw = sys.stdin.read()
    try:
        data = json.loads(raw)
    except ValueError:
        if mentions_holdout(raw):
            print(MESSAGE, file=sys.stderr)
            return 2
        return 0
    if blocked(data.get("tool_name", ""), data.get("tool_input", {}) or {}):
        print(MESSAGE, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
