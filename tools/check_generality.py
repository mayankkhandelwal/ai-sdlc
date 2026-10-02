"""Block test-document terms in agent, skill and prompt files (rule R1).

Collects every term from eval/**/banned-terms.txt and from the hold-out set
outside the repo (HOLDOUT_DIR), and searches the product's
instruction files for them. Exits 1 if any term is found, so the pre-commit
hook can stop the commit.

Usage: python tools/check_generality.py [extra paths...]
"""
import json
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCAN_DIRS = ["plugin", "agents", "skills", "prompts"]
SCAN_EXT = {".md", ".txt", ".json", ".yaml", ".yml", ".py", ".ts", ".js"}
ALLOW_FILE = ROOT / "tools" / "generality-allow.txt"
MIN_LEN = 4


def holdout_dir():
    """The hold-out set lives outside the repo (rule R2); same lookup as tools/guard_holdout.py."""
    if os.environ.get("HOLDOUT_DIR"):
        return pathlib.Path(os.environ["HOLDOUT_DIR"])
    try:
        cfg = json.loads((ROOT / "tools" / "paths.json").read_text(encoding="utf-8"))
        if cfg.get("holdout_dir"):
            return pathlib.Path(cfg["holdout_dir"])
    except (OSError, ValueError):
        pass
    return ROOT.parent / ("AI_SDLC" + "_hold" + "out")


def load_terms():
    """Return {term: is_holdout}. Hold-out terms are never printed (rule R2)."""
    terms = {}
    sources = [(f, False) for f in (ROOT / "eval").rglob("banned-terms.txt")]
    if holdout_dir().is_dir():
        sources += [(f, True) for f in holdout_dir().rglob("banned-terms.txt")]
    for f, hidden in sources:
        for line in f.read_text(encoding="utf-8").splitlines():
            t = line.strip().lower()
            if len(t) >= MIN_LEN and not t.startswith("#"):
                terms[t] = terms.get(t, False) or hidden
    allow = set()
    if ALLOW_FILE.exists():
        for line in ALLOW_FILE.read_text(encoding="utf-8").splitlines():
            t = line.split("#", 1)[0].strip().lower()
            if t:
                allow.add(t)
    return {t: h for t, h in sorted(terms.items()) if t not in allow}


def files_to_scan(extra):
    paths = [ROOT / d for d in SCAN_DIRS] + [pathlib.Path(p) for p in extra]
    for p in paths:
        if p.is_file():
            yield p
        elif p.is_dir():
            for f in p.rglob("*"):
                if f.is_file() and f.suffix.lower() in SCAN_EXT:
                    yield f


def main():
    terms = load_terms()
    if not terms:
        print("check_generality: no banned terms found (eval/**/banned-terms.txt)")
        return 0
    patterns = [(t, h, re.compile(r"(?<![\w-])" + re.escape(t) + r"(?![\w-])", re.IGNORECASE))
                for t, h in terms.items()]
    hits = []
    scanned = 0
    for f in files_to_scan(sys.argv[1:]):
        scanned += 1
        text = f.read_text(encoding="utf-8", errors="replace")
        for n, line in enumerate(text.splitlines(), 1):
            for term, hidden, pat in patterns:
                if pat.search(line):
                    shown = "<hold-out term>" if hidden else term
                    hits.append((f.relative_to(ROOT) if f.is_relative_to(ROOT) else f, n, shown))
    if hits:
        print("check_generality: test-document terms found in product files (rule R1):")
        for path, n, term in hits:
            print(f"  {path}:{n}  '{term}'")
        print("Fix the general cause, use a neutral example, or add a truly generic word to tools/generality-allow.txt with a reason.")
        return 1
    print(f"check_generality: ok ({scanned} files, {len(terms)} terms)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
