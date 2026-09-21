# ai-novel

Production system for AI-assisted serialized web novels, plus the novels made
with it.

**New here, human or model? Read [HANDOFF.md](HANDOFF.md) first.**

## Layout

| Path | What it is |
| --- | --- |
| `HANDOFF.md` | Cold-start guide. How to pick this up with no prior context. |
| `WORKFLOW.md` | The git and Google Docs review loop. |
| `sop/novel_sop.md` | Governing process, Parts A through F. Canonical. |
| `sop/platform-submission-reference.md` | Long-form platform research behind Part F. |
| `scripts/check.py` | Mechanical gate. Run before every commit. |
| `scripts/from_docs.py` | Normalizes text pulled back from Google Docs. |
| `novels/<slug>/` | One folder per novel. See each novel's own README. |

Novels are folders, not branches. Drafting happens on short-lived
`draft/<novel>-chNNN` branches that merge into `main` once approved.

## Quick start

```
python3 scripts/check.py novels/rejected-by-the-alpha
```

Exit 0 means the novel currently satisfies every mechanical rule.

## Starting a new novel

1. `mkdir -p novels/<slug>/chapters`
2. Work SOP Part A (seed) and Part B (blueprint) to produce `bible.md` and
   `outline.md`.
3. Create `cast.json` mapping every POV-capable character to `she` or `he`,
   so the POV check can run.
4. Create an empty `ledger.md` with a `## Chapter 1 delta` heading to come.
5. Draft per `WORKFLOW.md`.

The SOP is shared. Improving it improves every novel, which is the whole reason
novels are folders rather than branches.

## Standing hard rules

- No em dashes, en dashes, or double hyphens used as dashes, anywhere.
- Paragraphs cap at 3 sentences.
- 1,000 to 1,500 words per chapter, verified programmatically, never estimated.
- Every chapter ends on a cliffhanger.
- Every chapter produces a Ledger Delta.
- Never invent detail absent from the outline or bible. Flag it instead.

Verify the dash rule across every tracked file with:

```
python3 scripts/check.py --repo
```

It exits 0 when the repository is clean, and names the file and line otherwise.
