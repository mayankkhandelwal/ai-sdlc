"""Block test-document terms in agent, skill and prompt files (rule R1).

Collects every term from eval/**/banned-terms.txt and searches the product's
instruction files for them. Exits 1 if any term is found, so the pre-commit
hook can stop the commit.

Usage: python tools/check_generality.py [extra paths...]
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCAN_DIRS = ["plugin", "agents", "skills", "prompts"]
SCAN_EXT = {".md", ".txt", ".json", ".yaml", ".yml", ".py", ".ts", ".js"}
ALLOW_FILE = ROOT / "tools" / "generality-allow.txt"
MIN_LEN = 4


def load_terms():
    terms = set()
    for f in (ROOT / "eval").rglob("banned-terms.txt"):
        for line in f.read_text(encoding="utf-8").splitlines():
            t = line.strip().lower()
            if len(t) >= MIN_LEN and not t.startswith("#"):
                terms.add(t)
    allow = set()
    if ALLOW_FILE.exists():
        for line in ALLOW_FILE.read_text(encoding="utf-8").splitlines():
            t = line.split("#", 1)[0].strip().lower()
            if t:
                allow.add(t)
    return sorted(terms - allow)


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
    patterns = [(t, re.compile(r"(?<![\w-])" + re.escape(t) + r"(?![\w-])", re.IGNORECASE)) for t in terms]
    hits = []
    scanned = 0
    for f in files_to_scan(sys.argv[1:]):
        scanned += 1
        text = f.read_text(encoding="utf-8", errors="replace")
        for n, line in enumerate(text.splitlines(), 1):
            for term, pat in patterns:
                if pat.search(line):
                    hits.append((f.relative_to(ROOT) if f.is_relative_to(ROOT) else f, n, term))
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
