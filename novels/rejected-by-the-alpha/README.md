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

Chapters 1 through 4 are drafted, audited, and final. All four sit inside the
1,000 to 1,500 word target:

| Chapter | Title | POV | Words |
| --- | --- | --- | --- |
| 1 | The Binding Moon | Wren (no header, single POV) | 1,169 |
| 2 | Alpha of Duskmoor | Kieran | 1,247 |
| 3 | Rejected | Wren | 1,239 |
| 4 | The Brand | Wren | 1,168 |

Chapters 5 and 6 are outlined and ready to draft. No Master Ledger Update has
fired yet; the first checkpoint is due at batch end or immediately after the next
major event, whichever lands first.

## Canonical numbering

Arc 1 opens: 1 "The Binding Moon", 2 "Alpha of Duskmoor", 3 "Rejected", 4 "The Brand".

An earlier six-chapter numbering (in which "Rejected" was Chapter 5) was superseded
when Chapters 1 through 6 were compressed to 1 through 4. That numbering is gone from
the repository. If it resurfaces in an old paste, `outline.md` wins.

## POV header rule

No header on single-POV chapters. Once dual POV starts, every chapter carries a
`[Name]'s POV` header. That is why Chapter 1 has none and Chapters 2 onward do.

## Outstanding

- Nothing dash-related. The whole repository is clean. Re-check with
  `python3 scripts/check.py --repo` before any batch hand-off.
- Two displaced chapters from the 1 through 6 compression still need final placement.
- Three allied pack threads (Hollow Ridge / Rurik Voss, Fenmoor / Maeve Renn,
  Stonevale / Torvin Sedge) and the backstory integrations (Kessa Vane at Ch. 198,
  Tamsin exile history at Ch. 16) are patched into the outline but not yet drafted.
