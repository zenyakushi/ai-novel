# ai-novel

Working repository for the ZenithCite AI-assisted web novel production system.

## Layout

| Path | What it is |
| --- | --- |
| `sop/novel_sop.md` | The governing production SOP, Parts A through F: seed, blueprint, chapter drafting, chapter editing, cover generation, platform submission. Canonical. |
| `sop/platform-submission-reference.md` | Long-form platform research behind Part F. Reference only; Part F is what you execute. |
| `novel-1/` | Novel 1, "Rejected by the Alpha" (the Wren Ashveil story). Bible, 350-chapter outline, chapter prose, ledger. See its own README. |
| `context/project_memory.md` | Carried-over project state, standing rules, production sequence, feedback conventions. |

One source per thing. The SOP is not duplicated inside the novel; the novel's
bible is not duplicated inside the outline. When something is superseded it gets
deleted, not kept alongside.

## Standing hard rules

- No em dashes or en dashes anywhere, in prose or in SOP text. Double hyphens used
  the same way count as violations.
- Paragraphs cap at 3 sentences.
- Word count is verified programmatically, never estimated. Target 1,000 to 1,500
  words per chapter (1,700 to 1,900 for MoboReader).
- Every chapter ends on a cliffhanger.
- Every chapter outputs a Ledger Delta.
- Never invent detail that is not in the outline or bible. Flag instead.

## Per-chapter production sequence

1. Draft against the chapter outline, with the full Context Stack attached (SOP Part C).
2. Run the structured line-edit audit (SOP Part D).
3. Implement audit findings.
4. Apply any directed corrections.
5. Deliver final, append the Ledger Delta to `novel-1/ledger.md`.
