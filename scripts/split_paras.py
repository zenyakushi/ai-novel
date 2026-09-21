#!/usr/bin/env python3
"""Split paragraphs longer than the 3-sentence cap.

Breaks at the most natural seam available: before a line of dialogue starts,
otherwise after the last sentence that fits. Always review the result, since
where a paragraph breaks is a craft decision and this only proposes one.

    python3 scripts/split_paras.py <chapter.md> [--apply]
"""
import re, sys

MAX = 3
SPLIT = re.compile(r'(?<=[.!?])(?=\s)|(?<=[.!?]")(?=\s)')

def sentences(p):
    return [s.strip() for s in SPLIT.split(p) if s and s.strip()]

def chunk(sents):
    """Group into runs of <= MAX, preferring a break before dialogue."""
    out, cur = [], []
    for s in sents:
        starts_quote = s.lstrip().startswith('"')
        if cur and starts_quote and len(cur) >= 2:
            out.append(cur); cur = [s]
        elif len(cur) >= MAX:
            out.append(cur); cur = [s]
        else:
            cur.append(s)
    if cur:
        out.append(cur)
    # never leave a trailing single fragment if it can join the one before
    if len(out) > 1 and len(out[-1]) == 1 and len(out[-2]) < MAX:
        out[-2] += out.pop()
    # Never leave a group with unbalanced quotes: that orphans a closing quote
    # mark and breaks a single speech across two paragraphs.
    merged, i = [], 0
    while i < len(out):
        g = list(out[i])
        while " ".join(g).count('"') % 2 and i + 1 < len(out):
            i += 1
            g += out[i]
        merged.append(g)
        i += 1
    return merged
    return out

def main():
    path = sys.argv[1]
    apply = "--apply" in sys.argv
    lines = open(path, encoding="utf-8").read().split("\n")
    new, changed = [], 0
    for l in lines:
        s = l.strip()
        if (not s or s.startswith("#") or s.startswith("\\[")
                or (s.startswith("*") and s.endswith("*"))
                or len(sentences(s)) <= MAX):
            new.append(l); continue
        groups = chunk(sentences(s))
        changed += 1
        print(f"  split into {len(groups)}: {s[:70]}...")
        for g in groups:
            print(f"     | {' '.join(g)[:78]}")
        new.append("\n\n".join(" ".join(g) for g in groups))
    if apply and changed:
        open(path, "w", encoding="utf-8").write("\n".join(new))
        print(f"\napplied to {path}: {changed} paragraph(s) split")
    elif not changed:
        print("  nothing over the cap")
    else:
        print(f"\n{changed} paragraph(s) would be split; pass --apply to write")

if __name__ == "__main__":
    main()
