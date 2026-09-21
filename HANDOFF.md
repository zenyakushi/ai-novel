# Handoff: read this first

This file exists so any assistant (Claude, ChatGPT, or otherwise) can pick this
project up cold, with no prior conversation, and continue without breaking
anything. Read it before touching a file.

## What this project is

A serialized web novel production system with two deliverables:

1. A specific 350-chapter novel, "Rejected by the Alpha" (the Wren Ashveil
   story), taken to commercial publication on mobile-first platforms
   (GoodNovel, Dreame, LetterLux, MoboReader, SevenCat/TapRead).
2. A reusable SOP that someone with no AI knowledge could follow to produce
   another commercially viable novel.

The owner is the author and the decision maker. The assistant drafts, audits,
and flags. The assistant does not make story decisions unilaterally.

## Repository map

```
sop/novel_sop.md                     Governing process, Parts A-F. Canonical.
sop/platform-submission-reference.md Long-form platform research behind Part F.
scripts/check.py                     Mechanical gate. Run before every commit.
scripts/from_docs.py                 Normalizes text pulled back from Google Docs.
novels/<slug>/bible.md               Premise, characters, world, plot architecture.
novels/<slug>/outline.md             All 350 chapters.
novels/<slug>/ledger.md              Continuity record. One delta per chapter.
novels/<slug>/cast.json              Character pronouns, used by the POV check.
novels/<slug>/chapters/chNN-slug.md  Finalized chapter prose.
novels/<slug>/project_memory.md      Carried-over state and conventions.
```

One source per thing. The SOP is never copied into a novel folder. A novel's
bible is never copied into its outline. Superseded material is deleted, not
kept alongside, because two divergent copies is the failure mode this project
has already hit twice.

## Branch model

`main` holds the system and every novel. Each new novel is a new folder under
`novels/`, not a new branch.

Drafting happens on a short-lived branch (`draft/<novel>-ch005-006`) that merges
into `main` once the author approves the chapters in Google Docs. Novel folders
never live on permanent branches, because a long-lived branch freezes its copy
of the SOP at fork date and the copies drift.

## The rules that are not negotiable

These are enforced by `scripts/check.py`. Do not rely on remembering them.

- No em dashes, en dashes, or double hyphens used as dashes. Anywhere: prose,
  outline, bible, SOP, commit messages. Use a period, comma, colon, or
  parentheses.
- Paragraphs are 1 to 3 sentences. Never more.
- 1,000 to 1,500 words per chapter (1,700 to 1,900 for MoboReader only).
  Count it programmatically. Never estimate.
- Every chapter ends on a cliffhanger, and the mechanism does not repeat twice
  in a row.
- Every chapter produces a Ledger Delta appended to `ledger.md`.
- Never invent a plot point, name, trait, or backstory that is not in the
  outline, bible, or prior chapters. Flag the gap instead: `[NEED: ...]`.
- Show, do not tell. Never name an emotion directly.
- POV: no header on single-POV chapters. Once dual POV starts, every chapter
  carries a `\[Name's POV\]` header.

## How to draft a chapter

1. Read `sop/novel_sop.md` Part C. Assemble the Context Stack it specifies:
   this chapter's outline entry, the ledger, the previous chapter's prose, the
   next chapter's outline, and the scoped character and world bible entries.
   Scoped means only the characters and settings in this chapter.
2. Draft the chapter.
3. Run `python3 scripts/check.py <path to the chapter>`. Fix everything
   blocking. Do not proceed while it fails.
4. Run the Part D editorial audit for the things a script cannot judge:
   continuity against the ledger, outline fidelity, cliffhanger type, and
   voice against the previous chapter.
5. Publish to Google Docs for the author's review (see WORKFLOW.md).
6. Only after the author approves: import, re-run `check.py`, append the ledger
   delta, commit, push.

Never skip step 3 or step 6's re-run. Google Docs autocorrect inserts em dashes
and smart quotes, so text coming back from Docs is not trusted until it passes
the gate again.

## Current state

Chapters 1 through 4 are drafted, audited, and final. Chapters 5 and 6 are
outlined and ready to draft. No Master Ledger Update has fired yet; the first
checkpoint is due at batch end or immediately after the next major event.

Run `python3 scripts/check.py novels/rejected-by-the-alpha` to confirm the
current state passes before starting anything.

## Traps that have already bitten this project

Do not rediscover these the hard way.

- A chapter shipped labeled `Chapter 3 / [Kieran's POV]` when it was Chapter 4
  in Wren's POV. Mention counts do not detect this, because a POV character
  often spends the chapter watching someone else. `check.py` now compares
  possessive interiority ("her chest" against "his chest") instead.
- Two chapter numberings coexisted after Chapters 1 through 6 were compressed
  to 1 through 4. The outline numbering is canonical.
- An older copy of the SOP lived inside the novel document and silently
  diverged from the real one. Never duplicate the SOP.
- The project memory file stated the em dash ban using a double hyphen as an em
  dash. The rule applies to the documents that state the rule.

## Platform reality check

Every target platform restricts AI-generated text, from "discouraged" to
"submission-blocking gate" (see `sop/platform-submission-reference.md`). This
system is an AI-assisted drafting pipeline aimed at those platforms. That
tension is real and unresolved, and it is the author's call, not the
assistant's. Do not quietly ignore it, and do not lecture about it either.
