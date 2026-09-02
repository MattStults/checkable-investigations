#!/usr/bin/env python3
"""Cross-line leak scan: any word n-gram (n >= MIN_N) shared between a
translator-facing file and the README under test that occurs NOWHERE else in
the target record is a leak candidate. Tokenises across line breaks so
phrases straddling a README line wrap are caught.

Usage: leakscan.py FILE [FILE...] [--repo R] [--pin SHA] [--min-n 4]
Exit 1 if any candidate is found. Candidates are printed with the README
line and must be removed or reworded from the record's own vocabulary."""
import argparse, os, re, subprocess, sys

DEFAULT_REPO = os.path.expanduser("~/Documents/ai_safety_projects/semi-formal-document-analysis")
PIN = "48e66ce04a4d9f06771c42f89cb37b075583c5f6"
STOP = set("the a an of to in and or is are was were for on at by with as that this it its be not no".split())

def toks(s):
    return re.findall(r"[a-z0-9][a-z0-9'+./%-]*", s.lower())

def grams(tokens, n):
    return {" ".join(tokens[i:i + n]) for i in range(len(tokens) - n + 1)}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--repo", default=DEFAULT_REPO)
    ap.add_argument("--pin", default=PIN)
    ap.add_argument("--min-n", type=int, default=4)
    a = ap.parse_args()
    readme = subprocess.check_output(["git", "-C", a.repo, "show", f"{a.pin}:README.md"], text=True)
    rt = toks(readme)
    rg = set()
    for n in range(a.min_n, a.min_n + 5):
        rg |= grams(rt, n)
    # corpus: every tracked text file at the pin except README.md
    names = subprocess.check_output(["git", "-C", a.repo, "ls-tree", "-r", "--name-only", a.pin], text=True).split("\n")
    corpus = []
    for nme in names:
        if not nme or nme == "README.md" or nme.startswith(".claude/"):
            continue
        if not re.search(r"\.(md|py|json|jsonl|txt|yml|yaml|lp|sh|csv|html)$", nme) and "LICENSE" not in nme and "NOTICE" not in nme:
            continue
        try:
            corpus.append(subprocess.check_output(["git", "-C", a.repo, "show", f"{a.pin}:{nme}"], stderr=subprocess.DEVNULL).decode("utf-8", "replace"))
        except subprocess.CalledProcessError:
            pass
    ctext = " ".join(toks(" ".join(corpus)))
    found = []
    for f in a.files:
        ft = toks(open(f).read())
        cand = set()
        for n in range(a.min_n, a.min_n + 5):
            cand |= (grams(ft, n) & rg)
        # keep maximal phrases only, drop all-stopword grams
        cand = {c for c in cand if not set(c.split()) <= STOP}
        maximal = {c for c in cand if not any(c != o and c in o for o in cand)}
        for c in sorted(maximal):
            if c not in ctext:
                line = next((i + 1 for i, l in enumerate(readme.split("\n")) if c.split()[0] in toks(l) and c in " ".join(toks(" ".join(readme.split("\n")[i:i + 2])))), None)
                found.append((f, c, line))
    for f, c, line in found:
        print(f"LEAK  {os.path.basename(f)}  README~{line}  {c!r}")
    print(f"{len(found)} README-only phrase(s) of >= {a.min_n} words")
    sys.exit(1 if found else 0)

if __name__ == "__main__":
    main()
