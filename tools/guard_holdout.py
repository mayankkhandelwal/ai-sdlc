"""Claude Code PreToolUse hook: keep the hold-out set unseen (rule R2).

Blocks tools that would open or list the hold-out folder:
- Read, Edit, Write: when file_path points into it
- Grep, Glob: when path or pattern points into it
- Bash: when the command names it, except a single scoring-script call, a single
  git command that doesn't print file content (add, status, mv, rm, log --oneline),
  or a git commit whose only mention is inside its -m message. Chained commands,
  pipes and redirects are never treated as safe.

Text that only mentions the folder (docs, commit messages) is allowed.
Exit code 2 blocks the call and shows the reason.
"""
import json
import re
import sys

HOLDOUT = re.compile(r"eval[\\/]+hold" + r"out", re.IGNORECASE)
SAFE_BASH = re.compile(
    r"^\s*(python3?\s+\S*tools[\\/]+eval_score\.py\b"
    r"|git\s+(add|status|mv|rm|log\s+--oneline)\b)")
# Any of these means more than one command, a pipe or a redirect: never "safe".
CHAINING = re.compile(r"[;&|`<>\n]|\$\(")
MESSAGE = ("Blocked by rule R2: the hold-out set must stay unseen. "
           "Only tools/eval_score.py may read it (summary scores only).")


def git_commit_message_only(cmd):
    """A single `git commit -m "..."` whose only mention of the folder is inside the message."""
    m = re.match(r'^\s*git\s+commit\b(.*)$', cmd, re.DOTALL)
    if not m:
        return False
    outside = re.sub(r'(-m|--message)\s+("([^"\\]|\\.)*"|\'[^\']*\')', "", m.group(1))
    return not HOLDOUT.search(outside) and not CHAINING.search(outside)


def touches_holdout(tool, tool_input):
    if tool in ("Read", "Edit", "Write", "NotebookEdit"):
        return bool(HOLDOUT.search(str(tool_input.get("file_path", ""))))
    if tool in ("Grep", "Glob"):
        return any(HOLDOUT.search(str(tool_input.get(k, ""))) for k in ("path", "pattern", "glob"))
    if tool in ("Bash", "PowerShell"):
        cmd = str(tool_input.get("command", ""))
        if not HOLDOUT.search(cmd):
            return False
        if git_commit_message_only(cmd):
            return False
        return not (SAFE_BASH.search(cmd) and not CHAINING.search(cmd))
    return False


def main():
    raw = sys.stdin.read()
    try:
        data = json.loads(raw)
    except ValueError:
        # Can't tell what the call does: block only if it seems to involve the hold-out.
        if HOLDOUT.search(raw):
            print(MESSAGE, file=sys.stderr)
            return 2
        return 0
    if touches_holdout(data.get("tool_name", ""), data.get("tool_input", {}) or {}):
        print(MESSAGE, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
