# Novel 1: Rejected by the Alpha (the Wren Ashveil story)

Paranormal romance / shifter fantasy with a political-thriller spine. 350 chapters,
6 arcs, 10 outline batches. Target 1,000 to 1,500 words per chapter.

## Files

| Path | What it is | Changes how often |
| --- | --- | --- |
| `bible.md` | Premise, story fundamentals, character bible, world bible, plot architecture, commercial optimization, platform hooks | Rarely |
| `outline.md` | All 350 chapters, purpose / key events / character development / cliffhanger | Per batch revision |
| `chapters/` | Finalized chapter prose, one file per chapter | Per chapter |
| `ledger.md` | Story-State Ledger: per-chapter deltas, plus Master Ledger Updates at checkpoints | Every chapter |

The governing process lives in `../../sop/novel_sop.md` (Parts A through F). The
per-chapter system prompt and Context Stack are assembled from Part C each time;
there is no separate stored copy, deliberately, so there is only one source.

`cast.json` maps every POV-capable character to `she` or `he`. The automated POV
check reads it, so a new POV character must be added there before that character
can hold a chapter.

Before committing anything here, run `python3 ../../scripts/check.py .` from this
folder, or `python3 scripts/check.py novels/rejected-by-the-alpha` from the repo
root. See `../../WORKFLOW.md` for the Google Docs review loop.

## Current state

Chapters 1 through 20 have prose drafts. Treat them as drafts requiring continued editorial review, not as universally final or platform-ready. Chapter 20's Master Ledger Update is the current continuity checkpoint; the earlier checkpoint followed Chapter 6. Current word counts should be regenerated from the live files with `scripts/check.py`, not copied from this README.

Chapter-level POV fields are in `outline.md`. Chapters 1-25 have provisional POV assignments. Chapters 26-350 have provisional POV proposals that must be confirmed during batch planning. The current proposals do not yet meet the bible's 65% Wren / 35% Kieran target.

## Canonical numbering

Arc 1 opens: 1 "The Binding Moon", 2 "Alpha of Duskmoor", 3 "Rejected", 4 "The Brand".

An earlier six-chapter numbering (in which "Rejected" was Chapter 5) was superseded
when Chapters 1 through 6 were compressed to 1 through 4. That numbering is gone from
the repository. If it resurfaces in an old paste, `outline.md` wins.

## POV header rule

No header on single-POV chapters. Once dual POV starts, every chapter carries a
`[Name]'s POV` header. That is why Chapter 1 has none and Chapters 2 onward do.

## Outstanding

- Run `python3 scripts/check.py --repo` before every hand-off. A passing mechanical check is necessary, not sufficient, for publication readiness.
- Verify current official platform terms, especially AI-assisted content, before choosing a submission target.
- Decide whether “A Second Wolf” refers to a literal second wolf or a metaphor for Wren's unmediated connection. The current prose says it is not a pulse and describes a wellspring, so the title/terminology needs intentional handling.
- Two displaced chapters from the 1 through 6 compression still need final placement.
- Three allied pack threads (Hollow Ridge / Rurik Voss, Fenmoor / Maeve Renn,
  Stonevale / Torvin Sedge) and the backstory integrations (Kessa Vane at Ch. 198,
  Tamsin exile history at Ch. 16) are patched into the outline but not yet drafted.
