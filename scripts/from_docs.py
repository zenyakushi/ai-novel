#!/usr/bin/env python3
"""Normalize chapter text pulled back out of Google Docs.

Google Docs changes text on the way through, and two of its habits break house
style silently:

  * autocorrect turns "--" and sometimes " - " into an em dash, which is banned
  * smart quotes replace straight quotes and apostrophes

The Drive read also escapes markdown characters and collapses blank lines.
This script undoes all of that and REPORTS what it touched, so a Docs round trip
can never quietly reintroduce a dash.

    python3 scripts/from_docs.py raw_from_docs.txt \
        novels/rejected-by-the-alpha/chapters/ch05-the-long-walk.md \
        --title "The Long Walk" --num 5 --pov Wren
"""
import argparse, re, sys

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("dest")
    ap.add_argument("--title", required=True)
    ap.add_argument("--num", required=True, type=int)
    ap.add_argument("--pov", default=None)
    a = ap.parse_args()

    t = open(a.src).read()
    report = []

    def count(pat):
        return len(re.findall(pat, t))

    # 1. dashes introduced by Docs autocorrect -> flagged, then repaired
    for sym, name in (("\u2014","em dash"), ("\u2013","en dash")):
        n = t.count(sym)
        if n:
            report.append(f"{n} {name}(s) found and replaced with a comma; REVIEW these")
            t = t.replace(f" {sym} ", ", ").replace(sym, ", ")
    n_dbl = count(r"\s--\s")
    if n_dbl:
        report.append(f"{n_dbl} double hyphen(s) replaced with a comma")
        t = re.sub(r"\s--\s", ", ", t)

    # 2. smart quotes -> straight, to match the existing chapter files
    for bad, good in (("\u201c",'"'), ("\u201d",'"'), ("\u2018","'"), ("\u2019","'")):
        if bad in t:
            report.append(f"{t.count(bad)} smart quote(s) {bad!r} normalized to {good!r}")
            t = t.replace(bad, good)

    # 3. undo the Drive read's markdown escaping
    t = re.sub(r"\\([\[\]*_`#])", r"\1", t)

    # 4. strip any heading/POV line the doc carried, we re-add them canonically
    lines = [l.rstrip() for l in t.split("\n")]
    lines = [l for l in lines
             if not re.match(r"^#?\s*Chapter \d+", l) and not re.match(r"^\[?\w+'s POV\]?$", l)]

    # 5. one line per paragraph, blank line between
    paras = [l.strip() for l in lines if l.strip()]

    head = f"# Chapter {a.num}: {a.title}\n"
    if a.pov:
        head += f"\n\\[{a.pov}'s POV\\]\n"
    open(a.dest, "w").write(head + "\n" + "\n\n".join(paras) + "\n")

    words = len(re.findall(r"[A-Za-z0-9']+", "\n".join(paras)))
    print(f"wrote {a.dest}: {len(paras)} paragraphs, {words} words")
    if report:
        print("\nDocs round trip altered the text:")
        for r in report:
            print(f"  ! {r}")
    else:
        print("no Docs artifacts found")
    print("\nNow run: python3 scripts/check.py " + a.dest)

if __name__ == "__main__":
    sys.exit(main())
