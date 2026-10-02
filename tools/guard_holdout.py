"""Claude Code PreToolUse hook: keep the hold-out set unseen (rule R2).

The hold-out set lives OUTSIDE this repo. Its folder is given by the HOLDOUT_DIR
environment variable, else by tools/paths.json (see eval/README.md).
This hook blocks obvious and accidental tool calls that point at that folder:
- Read, Edit, Write, NotebookEdit: by file or notebook path
- Grep, Glob, Bash, PowerShell, and any other tool: anywhere in the call's input
The only exception is one plain call of the scoring script, which prints summary
scores only: `python tools/eval_score.py <args>` with no chaining, pipes,
redirects or substitution.

Paths are compared after normalising case, slashes, quotes and "./" segments.
Exit code 2 blocks the call and shows the reason.

Also blocked: any mention of the HOLDOUT_DIR variable in a command, Grep/Glob
rooted at a parent of the hold-out folder, and recursive shell commands that
reach a parent folder ("..").

This guard stops accidental and obvious access; it is not a security boundary.
Known limits (docs/rules.md, R2): a hook only sees the text of a call, so code
or commands that walk parent folders without naming the hold-out, or that build
its name from pieces, can still list and read it. The folder being outside the
repo, and the rule every chat follows, are the main protection. If a call can't
be parsed or checked, it is blocked (fail closed).
"""
import json
import os
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_NAME = "AI_SDLC" + "_hold" + "out"


def configured_holdout():
    """HOLDOUT_DIR env var, else tools/paths.json, else a sibling folder of the repo."""
    if os.environ.get("HOLDOUT_DIR"):
        return os.environ["HOLDOUT_DIR"]
    try:
        cfg = json.loads((REPO / "tools" / "paths.json").read_text(encoding="utf-8"))
        if cfg.get("holdout_dir"):
            return cfg["holdout_dir"]
    except (OSError, ValueError):
        pass
    return str(REPO.parent / DEFAULT_NAME)


HOLDOUT_DIR = configured_holdout()
PATH_FIELDS = ("file_path", "notebook_path")
ENV_NAME = re.compile(r"holdout_dir", re.IGNORECASE)        # $HOLDOUT_DIR, $env:HOLDOUT_DIR, %HOLDOUT_DIR%
RECURSIVE = re.compile(r"(\s-[a-z]*r[a-z]*\b|\s--recursive\b|\brg\b|\bfind\b|-recurse\b|\btar\b|\bzip\b|\brobocopy\b|\bxcopy\b|\bdir\s+/s\b)",
                       re.IGNORECASE)
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


PARENT = norm(pathlib.Path(HOLDOUT_DIR).resolve().parent).rstrip("/")


def mentions_holdout(text):
    return TARGET_NAME in norm(text) or bool(ENV_NAME.search(str(text)))


def searches_parent(path, cwd):
    """True if a search rooted at `path` would include the hold-out folder (an ancestor of it)."""
    if not path:
        return False
    full = norm(pathlib.Path(cwd or ".", str(path)).resolve()).rstrip("/")
    return full == PARENT or (PARENT + "/").startswith(full + "/")


def blocked(tool, tool_input, cwd):
    if tool in ("Read", "Edit", "Write", "NotebookEdit"):
        return any(mentions_holdout(tool_input.get(f, "")) for f in PATH_FIELDS)
    if tool in ("Grep", "Glob"):
        return mentions_holdout(json.dumps(tool_input)) or searches_parent(tool_input.get("path"), cwd)
    if tool in ("Bash", "PowerShell"):
        cmd = str(tool_input.get("command", ""))
        if RECURSIVE.search(cmd) and (".." in cmd or PARENT in norm(cmd)):
            return True
        if not mentions_holdout(cmd):
            return False
        in_repo = cwd is not None and norm(pathlib.Path(cwd).resolve()).rstrip("/") == norm(REPO).rstrip("/")
        return not (in_repo and SCORER.match(norm(cmd)) and not UNSAFE.search(cmd) and not ENV_NAME.search(cmd))
    return mentions_holdout(json.dumps(tool_input))


def main():
    try:
        data = json.loads(sys.stdin.read())
        if blocked(data.get("tool_name", ""), data.get("tool_input", {}) or {}, data.get("cwd")):
            print(MESSAGE, file=sys.stderr)
            return 2
        return 0
    except Exception:  # fail closed (rule R9): if the call can't be checked, it doesn't run
        print("Blocked: the hold-out guard could not check this call (rule R9: fail closed).", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
