**Purpose & context**

ZenithCite is building a serialized web novel business centered on AI-assisted production of romance fiction (primarily werewolf/paranormal/shifter fantasy) for mobile-first platforms including GoodNovel, Dreame, LetterLux, MoboReader, SevenCat/TapRead, and others. The dual goal is: (1) producing a specific 350-chapter novel ("Rejected by the Alpha" / the Wren Ashveil story) to commercial publication, and (2) developing a reusable, transferable SOP system that someone with no AI knowledge could use to produce commercially viable web novels independently.

ZenithCite's editorial standard is ruthlessly functional: every element must directly improve output quality or it gets cut. Documentation is written for execution, not explanation.

**Current state**

Active novel project is in early chapter production. Chapters 1–4 have been drafted, audited, and finalized:

- **Chapter 1**: Cold-open flash-forward (present tense) + past-tense main narrative. Wren's hidden secondary pulse ignites a public mate bond at the Rite. Established the "binding thread" mechanic. Ledger delta logged.
- **Chapter 2**: Kieran POV. Bond ignition suppressed by King Aldric and Oracle Yseult. Political conspiracy introduced. Ledger delta logged.
- **Chapter 3**: Wren POV. "Rejected." Expanded to mid-range word count (1,239 words). Ledger delta logged.
- **Chapter 4**: "The Brand." 1,168 words, all mechanical checks clean. POV header deferred per bible rule (headers begin only when dual POV starts). Ledger delta logged.

The production SOP (Parts A–F) exists as a refined markdown document covering: seed development, story blueprint, chapter drafting, chapter editing, book cover generation, and platform submission.

**On the horizon**

- Chapters 5–6 outlined and ready for drafting (outlines supplied in Chapter 4 session).
- Ongoing ledger management: per-chapter delta outputs, full master ledger rewrite at batch-end checkpoints or after major plot events (deaths, reveals).
- Continued POV rotation tracking (Kieran/Wren balance).
- Placeholder chapters from the Chapter 1 restructure (two chapters displaced when Chapters 1–6 compressed to 1–4) still need final placement.
- Three allied pack threads (Hollow Ridge/Rurik Voss, Fenmoor/Maeve Renn, Stonevale/Torvin Sedge) and backstory integrations (Kessa Vane at Ch. 198, Tamsin exile history at Ch. 16) are patched into the outline but not yet drafted.

**Key learnings & principles**

- **Word count is a hard requirement, not a guideline.** Target is 1,000–1,500 words per chapter. Must be verified programmatically before delivery, not estimated.
- **Outline fidelity over improvisation.** If an outline is missing, request it; never invent plot.
- **Flag, don't silently fix.** Surface issues explicitly so ZenithCite can make the call.
- **Decisive on style when no preference is stated.** When ZenithCite expresses no preference, Claude resolves it using the bible's own rules.
- **Continuity errors caught and corrected mid-project set precedent for rigor.** Examples: Cassian placed in a scene before his rejoining chapter (Ch. 177 → 213), batch hand-off re-covering ground, sequencing contradictions within a draft chapter.
- **The em dash ban is a hard constraint with zero exceptions** -- the character must not appear anywhere: in prose, in SOP prompt blocks, or in any generated output. Replace with periods, commas, colons, semicolons, or restructured sentences.
- **Overused constructions become tics, not craft.** Patterns that repeat (e.g., "[statement], like [abstract gloss]") must be identified and eliminated in audit.
- **Additions must develop existing beats, not pad.** When expanding word count, deepen sensory detail and extend reaction beats; do not add filler.

**Approach & patterns**

**Production sequence (per chapter):**
1. Draft against the chapter outline
2. Run structured line-edit audit (checklist: banned words, em/en dash sweep, AI-tell patterns, paragraph length, show-don't-tell, ledger continuity, POV discipline, outline fidelity, cliffhanger type, voice consistency)
3. Implement audit findings
4. Apply any ZenithCite-directed corrections
5. Deliver final with ledger delta appended

**Hard formatting and style rules:**
- No em dashes or en dashes anywhere in prose or SOP content
- Paragraph cap: 3 sentences maximum (mobile-first)
- Banned word list enforced (includes: "smirked," "chuckled," "pivotal," "intricate," and near-miss substitutes)
- No direct emotion naming (show-don't-tell)
- Terminology must follow established canon ("lines" not "tier" for murmur-spread; "platform" not "dais")
- All prompts in SOP formatted in monospace code blocks

**Continuity system:**
- Ledger delta (2–5 bullets) generated every chapter
- Full master ledger rewrite triggered at batch-end checkpoints or immediately after major plot events

**Feedback style:** ZenithCite's corrections are direct and line-specific -- they identify the exact phrase, note the problem, and sometimes flag when an adjacent line partially resolves it. Claude should match this precision in responses.

**SOP documentation philosophy:** KISS principle. Split every stage into User Input vs. Prompt. Strip explanatory "why" text unless it materially changes behavior. LLM gathers evidence autonomously rather than relying on manually sourced material.

**Tools & resources**

- Claude with file creation and bash tooling (word count verification, banned word scans, dash audits, paragraph length checks)
- SOP markdown document (Parts A–F) as the governing production reference
- Story bible, character ledger, world bible, and master continuity ledger for the Wren Ashveil novel
- Chapter-by-chapter outline (all 350 chapters developed, with patch instructions for gap fills)
- Target platforms: GoodNovel, Dreame, LetterLux, MoboReader, SevenCat/TapRead, NovelSnack, MegaNovel, StaryWriting