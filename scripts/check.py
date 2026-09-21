#!/usr/bin/env python3
"""Mechanical pre-delivery checks for chapter drafts.

Runs the SOP Part D mechanical checklist deterministically, so no model has to
remember it. Exits non-zero if any BLOCKING check fails.

    python3 scripts/check.py novels/rejected-by-the-alpha
    python3 scripts/check.py novels/rejected-by-the-alpha/chapters/ch05-the-long-walk.md
"""
import os, re, sys, glob

WORD_MIN, WORD_MAX = 1000, 1500          # MoboReader override: 1700-1900
BANNED = [
    r"testament", r"tapestry", r"beacon", r"lethal dance", r"smirked", r"chuckled",
    r"sighed", r"dangerous game", r"delve", r"showcas\w*", r"underscore\w*",
    r"pivotal", r"intricate", r"meticulous\w*", r"garner\w*", r"fostering",
    r"enhance\w*", r"vibrant", r"indelible", r"crucial", r"deeply rooted",
    r"in the heart of", r"nestled", r"ever-evolving", r"little did (they|she|he) know",
]
# near-miss substitutes that dodge the banned word but keep the tic
NEAR_MISS = [r"quirked a? ?half[- ]smile", r"lips twitched upward", r"huffed a laugh",
             r"let out a breath", r"a ghost of a smile"]

def sentences(p):
    return len(re.findall(r'[.!?]["”]?(?:\s|$)', p))

def words(t):
    return len(re.findall(r"[A-Za-z0-9']+", t))

def check_chapter(path, dual_pov_started):
    txt = open(path).read()
    body = "\n".join(l for l in txt.split("\n")
                     if not l.startswith("# Chapter") and not re.match(r"^\\\[.*POV\\\]", l))
    errs, warns = [], []
    name = os.path.basename(path)

    # --- filename / heading agreement -------------------------------------
    m_file = re.match(r"ch(\d+)-", name)
    m_head = re.search(r"^# Chapter (\d+):", txt, re.M)
    if not m_head:
        errs.append("no '# Chapter N: Title' heading")
    elif m_file and int(m_file.group(1)) != int(m_head.group(1)):
        errs.append(f"filename says ch{int(m_file.group(1))}, heading says Chapter {int(m_head.group(1))}")

    # --- POV header rule ---------------------------------------------------
    has_hdr = bool(re.search(r"^\\\[(\w+)'s POV\\\]", txt, re.M))
    if dual_pov_started and not has_hdr:
        errs.append("dual POV has started but this chapter has no POV header")
    if has_hdr:
        pov = re.search(r"^\\\[(\w+)'s POV\\\]", txt, re.M).group(1)
        # Third-person limited: the POV character's body and mind get possessive
        # interiority ("her chest", "his thoughts"); everyone else is observed from
        # outside. Mention counts do NOT work here, because a POV character often
        # spends the chapter watching someone else. This is the check that would
        # have caught Chapter 4 shipping as Kieran's POV over Wren's prose.
        INNER = r"(?:chest|pulse|throat|knees|stomach|skin|hands?|mind|thoughts?|breath|heart|eyes|ribs|spine|jaw)"
        cast = {}
        cj = os.path.join(os.path.dirname(os.path.dirname(path)), "cast.json")
        if os.path.exists(cj):
            import json
            cast = json.load(open(cj)).get("pronouns", {})
        pron = cast.get(pov)
        if pron is None:
            warns.append(f"{pov} is not in cast.json, so the POV check could not run")
        else:
            mine  = len(re.findall(rf"\b{'her' if pron=='she' else 'his'} {INNER}", body, re.I))
            other = len(re.findall(rf"\b{'his' if pron=='she' else 'her'} {INNER}", body, re.I))
            if mine == 0 and other == 0:
                warns.append("no possessive interiority found; POV could not be verified")
            elif other > mine:
                errs.append(f"POV header says {pov} ({pron}) but the interiority is "
                            f"{'his' if pron=='she' else 'her'}-dominant "
                            f"({'her' if pron=='she' else 'his'}+body={mine}, "
                            f"{'his' if pron=='she' else 'her'}+body={other}). "
                            f"Confirm whose head this chapter is in.")

    # --- dashes ------------------------------------------------------------
    # chr() keeps these characters out of this file, which the dash rule
    # also covers.
    for sym, label in ((chr(0x2014), "em dash"), (chr(0x2013), "en dash")):
        if sym in txt:
            errs.append(f"{txt.count(sym)} {label}(s)")
    if re.search(r"\s--\s|\w--\w", txt):
        errs.append("double hyphen used as a dash")

    # --- word count --------------------------------------------------------
    wc = words(body)
    if not (WORD_MIN <= wc <= WORD_MAX):
        errs.append(f"word count {wc} outside {WORD_MIN}-{WORD_MAX}")

    # --- banned words ------------------------------------------------------
    for pat in BANNED:
        for m in re.finditer(rf"\b{pat}\b", body, re.I):
            errs.append(f"banned word {m.group(0)!r}")
    for pat in NEAR_MISS:
        for m in re.finditer(pat, body, re.I):
            warns.append(f"near-miss substitute {m.group(0)!r}")

    # --- paragraph length --------------------------------------------------
    for i, p in enumerate(l for l in body.split("\n") if l.strip()):
        if sentences(p) > 3:
            errs.append(f"paragraph {i+1} has {sentences(p)} sentences (max 3): {p[:60]}...")

    # --- AI tells (advisory) ----------------------------------------------
    frag = re.findall(r"(?:(?:^|\. )[A-Z][a-z]*\.){3,}", body)
    if frag:
        warns.append(f"{len(frag)} run(s) of 3+ clipped one-word fragments")
    n_notx = len(re.findall(r"wasn't [^.]{1,40}, it was", body, re.I))
    if n_notx > 2:
        warns.append(f"{n_notx} \"it wasn't X, it was Y\" constructions (max 2)")

    # Gloss-simile tic: a concrete beat followed by an explanatory comparison
    # ("the way a person notices...", "more like sand than weather", "like a line
    # he had been handed"). Once or twice reads as voice. Seven times in 1,100
    # words, which is what Chapter 5 shipped with on its first pass, reads as a
    # tic. The project memory flags this pattern explicitly.
    # Dialogue is exempt: "It ends the way it always ends" is how a person
    # talks, not narration stepping back to explain itself.
    narration = re.sub(r'"[^"]*"', "", body)
    gloss = re.findall(r"the way [a-z]|, like [a-z]|more like [a-z ]{2,30} than|"
                       r"register [a-z ]{2,30} use when", narration, re.I)
    if len(gloss) > 2:
        errs.append(f"{len(gloss)} gloss-simile constructions (max 2): "
                    + "; ".join(repr(g.strip()) for g in gloss[:4]))
    elif len(gloss) == 2:
        warns.append("2 gloss-simile constructions, at the limit")

    # --- patterns adapted from the humanizer skill (github.com/blader/humanizer) ---
    # Only the ones that apply to serialized fiction. Its "one-line closers" and
    # "decorative formatting" rules are skipped deliberately: short paragraphs and
    # punchy chapter endings are required by the mobile-serial format, not tells.

    # Anaphora: three or more consecutive paragraphs opening the same way.
    paras = [x.strip() for x in body.split("\n") if x.strip()]
    opens = [" ".join(x.split()[:2]).strip('"').lower() for x in paras]
    run = 1
    for a, b in zip(opens, opens[1:]):
        run = run + 1 if (a == b and a) else 1
        if run >= 3:
            errs.append(f"{run} consecutive paragraphs opening with {a!r}")
            break

    # Shallow "-ing" riders that assert meaning instead of showing it.
    for m in re.finditer(r", (symboliz|reflect|showcas|underscor|highlight|emphasiz|"
                         r"signal|mark|cement|affirm)\w*ing\b[^.]{0,40}", body, re.I):
        errs.append(f"shallow -ing rider: {m.group(0).strip()!r}")

    # Avoiding is/are/has with inflated substitutes.
    for m in re.finditer(r"\b(serves as|stands as|acts as|boasts of|features a)\b", body, re.I):
        errs.append(f"inflated substitute for is/are/has: {m.group(0)!r}")

    # Stacked qualifiers.
    for m in re.finditer(r"\b(?:could|might|may) (?:potentially|possibly|perhaps)\b|"
                         r"\b(?:somewhat|rather|quite) \w+ly\b", body, re.I):
        warns.append(f"stacked qualifier: {m.group(0)!r}")

    # Curly quotes, which Google Docs inserts on edit.
    if any(c in txt for c in (chr(0x201c), chr(0x201d), chr(0x2018), chr(0x2019))):
        errs.append("curly quotes present; run scripts/from_docs.py to normalize")

    # The ", adjective and adjective" modifier tail. Ordinary English in ones and
    # twos, a signature in fours, so this warns rather than blocks.
    tails = re.findall(r", [a-z]+ and [a-z]+[,.]", body)
    if len(tails) > 3:
        warns.append(f"{len(tails)} ', adjective and adjective' tails: "
                     + "; ".join(repr(x.strip()) for x in tails[:4]))

    return wc, errs, warns


def check_repo():
    """Scan every tracked text file for banned dash characters."""
    import subprocess
    EM, EN = chr(0x2014), chr(0x2013)
    files = subprocess.run(["git", "ls-files"], capture_output=True, text=True).stdout.split()
    bad = 0
    for f in files:
        if not f.endswith((".md", ".py", ".json", ".txt", ".sh")):
            continue
        try:
            lines = open(f, encoding="utf-8").read().split("\n")
        except (UnicodeDecodeError, FileNotFoundError):
            continue
        for i, l in enumerate(lines, 1):
            hits = []
            if EM in l: hits.append("em dash")
            if EN in l: hits.append("en dash")
            if re.search(r"\s--\s", l): hits.append("double hyphen")
            if hits:
                print(f"[FAIL] {f}:{i}: {', '.join(hits)}")
                print(f"         {l.strip()[:100]}")
                bad += 1
    print(f"\n{'PASS' if bad==0 else 'FAIL'}: {bad} dash violation(s) across the repository")
    return 1 if bad else 0

def main(target):
    if os.path.isfile(target):
        novel, chapters = os.path.dirname(os.path.dirname(target)), [target]
    else:
        novel = target.rstrip("/")
        chapters = sorted(glob.glob(f"{novel}/chapters/ch*.md"))
    if not chapters:
        print(f"no chapters found under {target}"); return 1

    # dual POV is "started" from the first chapter that carries a POV header
    first_hdr = next((i for i, c in enumerate(sorted(glob.glob(f"{novel}/chapters/ch*.md")))
                      if re.search(r"^\\\[\w+'s POV\\\]", open(c).read(), re.M)), None)

    total_err = 0
    for c in chapters:
        idx = sorted(glob.glob(f"{novel}/chapters/ch*.md")).index(c)
        dual = first_hdr is not None and idx > first_hdr
        wc, errs, warns = check_chapter(c, dual)
        status = "FAIL" if errs else ("warn" if warns else "ok")
        print(f"[{status:>4}] {os.path.basename(c):<32} {wc:>5} words")
        for e in errs:   print(f"         BLOCKING: {e}")
        for w in warns:  print(f"         note:     {w}")
        total_err += len(errs)

    # --- ledger coverage ---------------------------------------------------
    lp = f"{novel}/ledger.md"
    if os.path.exists(lp):
        led = open(lp).read()
        for c in sorted(glob.glob(f"{novel}/chapters/ch*.md")):
            n = int(re.match(r"ch(\d+)-", os.path.basename(c)).group(1))
            if not re.search(rf"^## Chapter {n} delta", led, re.M):
                print(f"[FAIL] ledger.md missing a delta for Chapter {n}")
                total_err += 1
    else:
        print(f"[FAIL] no ledger.md at {lp}"); total_err += 1

    print(f"\n{'PASS' if total_err==0 else 'FAIL'}: {total_err} blocking issue(s)")
    return 1 if total_err else 0

if __name__ == "__main__":
    if "--repo" in sys.argv:
        sys.exit(check_repo())
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    sys.exit(main(args[0] if args else "novels/rejected-by-the-alpha"))
