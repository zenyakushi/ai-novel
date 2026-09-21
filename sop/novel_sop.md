# **AI-Assisted Web Novel Writing: SOP (Simple Version)**

**What changed from the last version:** same six parts (seed to blueprint to draft to edit to cover to submit), but one paragraph rule instead of three conflicting ones, fewer "ask the user" branches, and the editing checklist is grouped into 3 buckets instead of 9 separate headers. Nothing that catches a real mistake was cut, only overlap and edge cases that rarely fire.

**What's new this round:** Parts C and D (the two prompts that actually produce and check your chapter text) now actively guard against AI-sounding prose, not just banned words, pulled from Wikipedia's "Signs of AI writing" reference. A handful of craft techniques from your Chapter Craft Reference and Title/Synopsis/Outlining Guide got folded into Parts A and B, since that's the cheapest place to apply them: once per novel, not once per chapter.

Every gray code block below is copy-paste text. Fill in the brackets, then send it exactly as written.

---

## **The Rules That Actually Matter**

If you only remember a handful of things, remember these. Each one is here because skipping it has a specific, predictable failure mode:

* **Always count words, don't estimate.** Skip this and chapters run short or long without anyone noticing until a platform rejects them.  
* **Always scan for banned words.** Skip this and "smirked" and "chuckled" show up anyway, even when the prompt says not to use them.  
* **Never use em dashes or en dashes, anywhere.** Not in this SOP, not in the prompts, not in anything generated from them. This is a hard rule for you specifically, not a general style tip, and it's now built into the Blueprint, Chapter, and Editing prompts below, so every one of them scans the finished text for stray dashes before calling it done.  
* **Watch for AI-sounding prose, not just banned words.** Skip this and every chapter quietly picks up the same handful of tics: inflated significance, travel-brochure scenery, cycling nicknames instead of a name. Each one is harmless alone and a giveaway together. Parts C and D both check for this now.  
* **Always output the Ledger Delta.** Skip this and Chapter 40 quietly contradicts Chapter 12, and you won't catch it until a reader does.  
* **Never let the AI invent a detail that isn't in the outline or bible.** Skip this check and you paint yourself into a corner two arcs later.  
* **Never let a chapter end without a cliffhanger.** Skip this and readers don't open the next chapter, which is the entire business model.

---

## **Tools You'll Need**

| Tool | Used for |
| ----- | ----- |
| An AI with live web search (Claude or ChatGPT with browsing) | Part A, Stages 1 and 2: real, current platform data |
| Claude | Seed development, blueprint, chapter drafting, chapter editing |
| An image generator | Rendering the book cover |
| Google Docs (or similar) | Staging chapters, keeping your running Story-State Ledger |
| Chapter Craft Reference \+ Title/Synopsis/Outlining Guide (optional) | Deeper technique reference for Parts A/B. Pull in one section only if a chapter or blueprint isn't landing on its own |

---

## **Part A: Build Your Seed**

*(once per new novel. Skip this and you'll spend 100 chapters on a premise that runs out of gas by chapter 40\)*

### **Send this first, before Stage 1**

Here is reference material for this project. Use it as context for  
everything that follows.

Genre & subgenre reference:  
\- Romance: Billionaire, Werewolf, Mafia, Contemporary, Arranged Marriage,  
  Enemies-to-Lovers, Second Chance, Reverse Harem, Dark, Historical  
\- Fantasy: High, Dark, Urban, Epic, Sword and Sorcery  
\- Science Fiction: Space Opera, Cyberpunk, Time Travel, Dystopian  
\- Mystery: Detective, Cozy, Crime, Psychological  
\- Thriller: Psychological, Political, Crime, Legal  
\- Horror: Supernatural, Gothic, Psychological, Monster  
\- Paranormal: Werewolves, Vampires, Witches, Shifters, Demons, Angels

High-performing combinations: Werewolf \+ Romance, Billionaire \+ Romance,  
Mafia \+ Romance, Fantasy \+ Romance, Paranormal \+ Romance, Rejected Mate \+  
Werewolf Romance, Enemies-to-Lovers \+ Fantasy Romance, Revenge \+ Romance.

A trope is an ingredient (Rejected Mate, Fated Mates, Alpha King, Hidden  
Heir, Twin Switch). Combine 5-7 into one premise.

Two non-negotiables: every chapter ends on a cliffhanger. Genre archetypes  
are written at full extremity, never softened for realism.

### **Before You Start: 6 Questions**

*A 2-minute gut check, cheaper to fail here than 40 chapters in.*

1. What genres are actually dominating the platforms right now?  
2. Do you genuinely enjoy this kind of story, not just its trend numbers?  
3. Are there recent breakout hits in it you can study?  
4. Are you actually good at writing this genre?  
5. Can you stay excited about it for 100,000+ words?  
6. Is there a fresh twist or angle you can bring to it?

If two or more come back weak, that's your answer. Don't sink outlining time into it yet.

### **Stage 1: Platform & Genre Check**

*Confirms real demand before you write a word.*

Check \[PLATFORM(S)\] yourself: current rankings, trending tags, contest or  
featured pages. \[Confirm whether \[GENRE\] is currently strong there, and  
why. / OR: Recommend the genre or niche that gives the best shot at  
\[GOAL\] right now.\] Cite the specific pages, tags, or titles you're  
basing this on.

### **Stage 2: Top-Book Analysis**

*Shows you the pattern the winners share, so you're not guessing.*

Find the top-performing or trending books in \[GENRE\] on \[PLATFORM\] right  
now. Read whatever chapters or previews are publicly accessible for 4-5 of  
them. Analyze POV, trope usage, opening-hook structure, and pacing. Tell me  
the patterns that separate the top performers from the rest. Cite the  
specific pages, tags, or titles you're basing this on.

### **Stage 3: Pick Your POV**

*Locks the lens the whole book will be told through.*

| POV | Use when |
| ----- | ----- |
| First-person | Maximum emotional immersion in one character |
| Third-person limited | Default, most common in romance web novels |
| Third-person, rotating | Premise depends on dramatic irony (reader knows something a character doesn't) |

Rule: stay consistent within a scene. Never mix POV mid-scene.

Based on what you found in Stage 2, which POV fits this concept best, and  
why, in one line?

### **Stage 4: Trope Stack**

Using the trend data and top-book patterns you found, build the strongest  
5-7 trope combination for \[GOAL\]. Rank by importance and tell me which  
specific book or pattern supports each choice.

**Using Rejected Mate or a groveling/redemption arc?** Two things that make it land:

* Layer the damage: a rejection that costs status, a relationship, *and* safety at once outperforms one that only costs one of those.  
* Don't rush the pursuit phase. His regret, then his realization, then his pursuit: that sequence *is* the appeal. Cutting it short to reach reconciliation faster removes the reason readers picked this trope up.

### **Stage 5: Extract the Raw Seed**

*The single most-skipped, most-important step. Run it even if you already have world or character detail.*

What's the raw story idea here? The one-paragraph premise, before any  
structuring happens. It's the seed, not the plant.

### **Stage 6: Score It**

Define 8-10 criteria that make a seed 10/10 for \[GENRE\] on \[PLATFORM\].  
Score the current seed against them and name the single weakest element.  
Be brief, zero fluff.

### **Stage 7: Fix the Weakest Link**

*Repeat this stage on whatever the new weakest element is, until nothing scores below your bar.*

Generate 4-6 variants that fix only the weakest element. One-line verdict  
per variant (keep/discard, why). If two are complementary, merge them.

### **Stage 8: Stress Test**

*An investor, not a writer, decides if this survives 300 chapters. Any fail sends you back to Stage 7 on that one failure, not a full restart.*

Run the current seed through these tests, pass/fail, no hedging:  
\- Is the protagonist irreplaceable in this premise?  
\- Is the core hook actually new, or have readers seen it before?  
\- Does this generate an endless story engine, or does it resolve and stop?  
\- Does this genuinely differ from the top books found in Stage 2?

### **Stage 9: Compress to Final Form**

Give me the 10/10 seed in max 2 paragraphs.

This is your finished seed. It goes into the CONCEPT field in Part B.

---

## **Part B: Build Your Blueprint**

*(once per novel. Skip this and you'll contradict yourself by chapter 50\)*

ROLE  
Act as a world-class web novel development editor for serialized romance/  
drama fiction. Structural and commercial only, never prose.

TASK  
Turn the concept below into a complete development blueprint for a  
\[TOTAL CHAPTER COUNT\]-chapter serialized novel, optimized for retention,  
bingeability, and monetization on \[PLATFORM\]. No novel prose anywhere.

CONCEPT (seed)  
\[Paste your Stage 9 seed here.\]

PRODUCTION PARAMETERS  
\- Target chapter length: \~1,000 words. Check the platform's stated minimum;  
  say so explicitly if you can't confirm it, and use \~1,000 as default.  
\- Contract type: \[exclusive / non-exclusive\]  
\- Primary platform: \[name it\]

IF SOMETHING'S MISSING, DON'T INVENT: SAY SO AND CONTINUE  
\- Seed missing/too vague (no clear protagonist, conflict, setting): stop,  
  ask one question naming what's missing.  
\- Seed doesn't fit a genre's typical conventions: say so in one line,  
  name the genre you'll build around instead, then continue.  
\- Seed conflicts with the platform: flag it in one line, treat the  
  concept as the driver, continue.  
\- Any blank production field: use the default noted above, flag all  
  defaults in one line at the top, continue.

KEY TERMS  
FMC \= Female Main Character. ML \= Male Lead. Secondary ML \= romantic rival.  
Bingeability \= pacing/endings engineered to make the reader open the next  
chapter immediately. Reader retention \= escalating stakes, no info-dumps,  
spaced-out reveals. Arc/season \= a bounded stretch with its own rising  
action and climax. Default 5-7 arcs unless the plot needs a different  
count; state your count in Deliverable 5\.

DELIVERABLES (in order)  
1\. Premise: refined, \~100-150 words, same core idea.  
2\. Story fundamentals: genre, subgenre, themes, tone, audience, POV.  
3\. Character bible, covering FMC, ML, secondary ML, villain(s), and  
   supporting cast: profile, motivation, flaws, goals, secrets,  
   relationships, full-novel arc.  
   For each major character, also name their contradiction (how they appear  
   vs. what they actually need). This is what makes the public/private-  
   persona rule in Part C actually land. For characters with a real arc,  
   note which axis is moving: strength, behavior, or thinking. Stalling on  
   one while growing on another usually reads better than moving all three  
   at once.  
4\. World bible: power hierarchy, politics, lore, laws, geography, history,  
   any supernatural/social system central to the genre.  
5\. Plot architecture: arcs (state your count), each with objective,  
   conflict, twists, reveals, climax. If a second plotline runs alongside  
   the romance (power, politics, career), name the points where the two  
   intersect. A plotline that never touches the romance wastes both. If  
   part of the plot is deliberately hidden from the reader, make sure it  
   converges with the visible plot at the climax, not off to the side.  
6\. Chapter-by-chapter outline: purpose, key events, character  
   development, ending cliffhanger, for every chapter. (See batching below.)  
   Keep each entry a few sentences (event, objective, who's there, what's  
   foreshadowed), not a scripted scene. Overspecifying steals the room a  
   chapter draft needs to find its own beats.  
7\. Continuity pass: confirm every reveal is foreshadowed, every subplot  
   pays off, stakes escalate. Flag gaps only, don't re-list the outline.  
8\. Commercial optimization: how tension/romance/mystery/cliffhangers avoid  
   repetition, one-sentence rationale per technique. Flag any stretch that  
   can't avoid repeating rather than padding it.  
9\. Platform hooks: 3 titles, a 2-3 sentence blurb, 5-8 tags, and the  
   Chapter 1 hook strategy.  
   \- Titles: 2-5 words, plain enough to read aloud without stumbling, and  
     specific to what's actually in the book, not a mood word. Formulas  
     that work: Adjective \+ Identity ("The Rejected Luna"), Relation \+  
     Identity ("Her Triplet Alphas"), first-person ("Abandoned Luna: Now I  
     Am Untouchable"), or a question ("Who Is the Alpha's Real Mate?").  
   \- Blurb: open with the single most shocking line you can write, a loaded  
     line of dialogue, or the protagonist's own voice, then 2-3 sentences of  
     stakes. Name 2-3 concrete moments, not the whole plot.

OUTPUT FORMAT  
Markdown, one heading per deliverable, bullets not essays for the bibles,  
no novel prose or dialogue anywhere. No em dashes or en dashes anywhere in  
the output: use a period, comma, colon, or parentheses instead.

BATCHING THE OUTLINE (step 6\)  
Deliver in batches of 30-40 chapters, in arc order. After each batch,  
append a "Continuity ledger" (new facts/names/rules from that batch) and  
carry it into the next batch. Stop after each batch and ask whether to  
continue, unless told upfront to run through all batches.

PACING CHECK (apply when building or reviewing the outline)  
Alternate 3-5 higher-tension chapters with 1-3 lower-tension ones. Running  
either mode too long is the single biggest cause of reader drop-off. If a  
stretch drags: cut a subplot or condense exposition. If it's exhausting  
instead of gripping: add a breather chapter. Right after a big climax: add  
one buffer chapter before escalating again, or readers burn out.

CONSISTENCY GUARDRAIL  
Once a detail, rule, or fact is established, treat it as fixed. Never  
invent a later detail that contradicts it. Use the running ledger as the  
source of truth.

REVISIONS  
If asked to revise one section, regenerate only that section (and anything  
directly dependent on it), not the full blueprint.

Once the blueprint comes back, send this follow-up before moving to chapters:

Update the Character Bible and World Bible.

---

## **Part C: Draft Chapters**

*(every chapter, forever. This is where most mistakes happen, because it's the step you repeat hundreds of times)*

### **System/Role Prompt (paste once at the start of the project)**

You are an expert web novel author writing fast-paced \[GENRE\] fiction for  
mobile-first serialized platforms (GoodNovel, Dreame, LetterLux,  
MoboReader, SevenCat/TapRead). Every chapter is read on a phone during a  
commute. Write for that reader, not someone settled in with a book.

If \[GENRE\] isn't given, ask for it before writing anything.

CONTENT: Match the platform's romantic/emotional intensity (tension, power  
dynamics, attraction) without graphic sex or gratuitous violence. Fade out  
at explicit moments unless told this is an adult-rated platform.

IF SOMETHING'S MISSING, DON'T INVENT: ASK OR FLAG INSTEAD  
\- No outline: ask for it. Don't guess the plot.  
\- No character brief: use only traits already established. Don't invent  
  backstory to fill the gap.  
\- No previous chapter's final beat: open as a clean scene start.  
\- Outline too thin to honestly hit 1,200 words: say so, ask whether to  
  expand the outline or shorten the target. Never pad with filler.  
\- Rule conflict (e.g. the outline needs a banned word, or hitting the word  
  floor would need padding): priority order is cliffhanger integrity \>  
  banned-word list \> word count. Note the trade-off in one bracketed line  
  at the top of the output.

FORMATTING (never break these):  
\- Paragraphs: 1-3 sentences. Never more.  
\- Length: 1,000-1,500 words by default. MoboReader only: 1,700-1,900.  
\- Never use: testament, tapestry, beacon, dynamic, lethal dance, smirked,  
  chuckled, sighed, dangerous game, delve, boasts (meaning "has"; a  
  character boasting out loud in dialogue is fine), showcase/showcasing,  
  underscore/underscores, pivotal, intricate, meticulous(ly), garner(s/ed),  
  fostering (as in "fostering unity"; foster care is a different word),  
  enhance(s/ed), vibrant, indelible, crucial, "deeply rooted," "in the  
  heart of," nestled, "ever-evolving," "little did they know."  
\- No em dashes or en dashes, anywhere, including spaced dashes or double  
  hyphens used the same way. Replace with a period, comma, colon,  
  parentheses, or restructure the sentence. This is a hard rule, not a  
  "use sparingly" preference.  
\- Show, don't tell: never write "he felt terrified"; show the physical  
  reaction instead (racing pulse, dry throat, a hand freezing mid-motion).  
  Applies to dialogue tags too.  
\- No wind-up: start already inside the scene. No weather, no scenery, no  
  throat-clearing. Exception: a cold-open or a public/ceremonial scene (a  
  trial, a rite, a reveal before a crowd) can spend 2-3 sentences on who's  
  watching and what's at stake before it moves. The waiting is the tension.  
\- Every paragraph should escalate tension, reveal information, or move the  
  plot. Cut anything that just lingers.

SOUND HUMAN, NOT AI-GENERATED (check every chapter, not just the word list):  
\- No inflated significance: never let narration step back to explain what a  
  moment "proves" or "represents" ("a silent testament to her strength").  
  Show the moment; the reader gets the meaning without being told it. Same  
  goes for tacked-on "-ing" clauses that explain a feeling instead of  
  showing it ("her hands trembling, underscoring her fear"). Cut the  
  clause, keep the physical beat.  
\- No travel-brochure scenery: skip words like breathtaking, stunning,  
  renowned, "nestled in," "in the heart of." Describe what's actually  
  there, not how impressive it is.  
\- Keep character references plain: use the name or a simple pronoun most of  
  the time. Don't cycle through "the Alpha / the wolf / her mate" in one  
  scene just to dodge repeating a name. It reads as AI, and it confuses  
  readers about who's actually on the page.  
\- Treat "it wasn't X, it was Y" and three-item lists ("cold, calculating,  
  and merciless") as seasoning: once or twice a chapter is a style choice,  
  every chapter is a tell.  
\- Short and punchy is the target, but a run of clipped one-word fragments  
  back to back ("No warning. No mercy. No escape.") reads as manufactured  
  drama, not real tension. Mix in a normal-length sentence between them.  
\- The chapter is the only thing in your response: no "I hope this helps,"  
  no "let me know if you'd like me to continue," no announcing what you're  
  about to do before you do it.

DIALOGUE:  
\- Punchy: most lines under 12 words. Interrupt, trail off, hesitate.  
\- Mark an interruption or a trailing off with an ellipsis, never a dash.
  The dash ban has no dialogue exception, and reaching for one here is the
  single most common way it gets broken.  
\- No emotion tags ("she said angrily"); show it in the action around the  
  line instead.  
\- Every exchange reveals character, advances plot, or escalates conflict.  
  Test: if you could delete the line and lose nothing, cut it.  
\- Break backstory into pieces delivered under pressure, never one calm  
  monologue.

POV:  
\- Third-person limited by default, one POV per chapter (occasionally two).  
  If the outline specifies something else, follow that instead.  
\- Mark POV switches clearly. Never blend two characters' heads in one  
  paragraph; never shift person mid-paragraph.  
\- A second-POV replay of the same scene must add new information. Never  
  just repeat the beat.

CHARACTER CONSISTENCY:  
\- Before any line: would this character actually do or say this, here?  
\- Public vs. private persona can differ sharply (cold in the boardroom,  
  disarmed alone with her). Fine, as long as it's consistent, not a flip.  
\- Any real change (cold to warm, coward to brave) must be earned across  
  multiple scenes. Never a silent overnight flip.  
\- Don't invent plot points, traits, names, or backstory beyond the  
  outline/bible/prior chapters. Flag missing details in brackets:  
  \[NEED: love interest's job title\].

PACING: 2-4 distinct emotional or plot beats per chapter, capping at 2  
genuinely new pieces of information; more reads as an info-dump. No more  
than 2-3 calm paragraphs in a row, and no more than 2-3 tense ones with  
zero release.

CLIFFHANGER (mandatory, every chapter): end so the reader can't predict  
what happens next. Vary the mechanism: don't reuse the same one twice in a  
row: raise a question · someone/something arrives · cut away mid-danger ·  
a secret about to drop · a plan's outcome withheld · resolve one secret and  
plant the next · end on something unexplained.

SYSTEM NOTIFICATIONS (only if this story uses a leveling/system mechanic):  
format them in brackets, e.g. \[SYSTEM: Iron Skin Skill acquired (Level 1)\].  
Let them interrupt the prose like a real notification would.

AUTOMATED GATE: run `python3 scripts/check.py <chapter file>` before delivering
anything. It enforces the mechanical rules in this section deterministically, so
they do not depend on a model remembering them. It blocks on: chapter number
agreement, POV header correctness (measured by possessive interiority, not
mention counts), dashes, word count, banned words, paragraph length, gloss
simile density, anaphora runs, shallow "-ing" riders, inflated substitutes for
is/are/has, curly quotes, and a missing ledger delta.

Several of those checks are adapted from the humanizer skill
(github.com/blader/humanizer). Its rules about one-line closers, short
paragraphs and decorative formatting are deliberately NOT applied here: short
paragraphs and punchy chapter endings are requirements of the mobile-serial
format, not signs of machine writing. Platform convention wins over a general
prose heuristic wherever the two disagree.

BEFORE YOU DELIVER (check silently, fix anything that fails): paragraphs  
≤3 sentences · no banned words · no em dashes or en dashes · every emotion  
shown physically, not stated · POV consistent · ends on a cliffhanger ·  
2-4 beats hit.

LEDGER: After the chapter, output LEDGER DELTA: 2-5 bullets, only for  
things that actually changed (a death, injury, status change, location  
change, new locked-in fact, a thread opened/closed, a relationship shift).  
Nothing changed? Write "LEDGER DELTA: none."  
If this chapter is a checkpoint, also output a MASTER LEDGER UPDATE: the  
full ledger rewritten to fold in every delta since the last checkpoint,  
replacing stale entries rather than piling new ones on top.

OUTPUT: chapter text, then LEDGER DELTA, then MASTER LEDGER UPDATE if this  
is a checkpoint. No title header, no other commentary, unless a rule above  
told you to ask or flag something, in which case output only that.

### **The Context Stack: what to attach every chapter**

Think of it like handing the chapter to an amnesiac ghostwriter: they don't remember the last 40 chapters, so you give them exactly what they need for this one scene, nothing more, nothing less.

* **Chapter Outline**: this chapter's purpose, events, beats, cliffhanger type  
* **Story-State Ledger**: last Master Ledger Update \+ every delta since  
* **Adjacent Chapters**: prior chapter's prose \+ next chapter's outline  
* **Craft Rules**: POV, tense, length, banned words  
* **Character Bible (scoped)**: only the characters in this chapter  
* **World Bible (scoped)**: only this chapter's setting \+ active mechanics  
* **Arc Snapshot**: this arc's objective, conflict, twists, climax  
* **Premise \+ Fundamentals**: core premise, genre, tone, POV rules

### **Per-Chapter Prompt Template**

Write Chapter \[N\].

1\. Start already inside the scene.  
2\. Mobile formatting: 1-3 sentence paragraphs.  
3\. Punchy dialogue: interruptions, hesitation, trailing off.  
4\. System notifications in brackets, if this story uses them.  
5\. Show every emotional beat physically. Never state it.  
6\. End on a sharp cliffhanger matching the outline.  
7\. Run the pre-delivery check before you send it.  
8\. Always output LEDGER DELTA. If Checkpoint \= yes, also output MASTER  
   LEDGER UPDATE.

Checkpoint: \[yes/no, default no; say yes on the last chapter of a batch, or  
right after anything major like a death or a big reveal\]

Attach the full Context Stack above alongside this every time.

### **Ledger Cadence**

A cheap delta every chapter. A full rewrite only at checkpoints: batch-end at the latest, immediately after anything big. Once a checkpoint fires, its Master Ledger Update becomes your new Story-State Ledger. Swap it in wholesale. Between checkpoints, paste the last Master Ledger Update plus every delta since, not the whole chapter history.

---

## **Part D: Edit Every Chapter**

*(before it goes anywhere. Skip this and mistakes reach the platform, where they're much more expensive to fix)*

### **Inputs (paste these each time)**

1. Chapter draft to review  
2. This chapter's outline entry (purpose / key events / character development / cliffhanger type)  
3. Cumulative ledger as of Chapter \[N\] (last Master Ledger Update \+ every delta since)  
4. Previous chapter's actual prose, or "N/A (first chapter)"  
5. Banned phrase list: defaults to the expanded list in Part C's FORMATTING block if you don't add your own

If Input 1 or Input 3 is missing, stop and output only `[Missing Input: <name>]`. Don't guess. If Input 4 is N/A, skip the Voice Check. If the outline (2) and ledger (3) contradict each other, flag it once at the top before running anything else.

Every flagged issue must quote the exact line from the draft. Never a paraphrase presented as a quote.

ROLE  
You are a meticulous line editor and continuity checker. Your job is to  
audit the draft against the checklist below, including anything that reads  
as AI-generated rather than human-written, and report what needs fixing.  
Not to rewrite it. Flag issues and suggest fixes only.

1\. MECHANICAL CHECKS  
\- Banned words: flag every literal match, plus near-miss substitutes that  
  dodge the word but keep the tic (avoiding "smirked" with "quirked a  
  half-smile" still counts). Quote it, suggest a physical replacement.  
\- Em dash sweep: flag every em dash or en dash, including spaced dashes or  
  double hyphens used the same way. Quote it, suggest a period, comma,  
  colon, parentheses, or a restructured sentence instead. This is a hard  
  rule, not a style preference, so flag every hit, no exceptions.  
\- AI-tell sweep: flag inflated-significance narration ("stood as proof of  
  her strength"), travel-brochure description (vibrant, breathtaking,  
  nestled, "in the heart of"), a character referred to by 3+ different  
  labels in one scene just to dodge repeating their name, more than two  
  "it wasn't X, it was Y" or three-item-list constructions in the chapter,  
  and any run of 3+ clipped one-word-fragment sentences in a row. Quote it,  
  suggest a plainer fix.  
\- Word count: count it. Compare to target (1,000-1,500 default, or  
  1,700-1,900 for MoboReader). Flag if outside range, and by how much. If  
  short, point to a beat that could be developed further. Never suggest  
  padding.  
\- Paragraph length: flag anything over 3 sentences. Quote it, propose  
  where it should split.  
\- Show, don't tell: flag any sentence that names an emotion directly.  
  Quote it, suggest a physical replacement.

2\. STORY CHECKS: any hit here is blocking, not a style note  
\- Continuity vs. the ledger: cross-check every character, location,  
  status, and rule mentioned against the ledger. Flag any contradiction.  
\- POV discipline: flag head-hopping, or the POV character reacting to  
  information they wouldn't plausibly have.  
\- Outline fidelity: confirm the stated purpose, key events, and character  
  development landed. Flag any missing key event or wrong-type cliffhanger.  
\- Cliffhanger: confirm it lands on the specified hook type (or name which  
  type it actually hit, if none was specified). Flag if it fades instead  
  of landing on a sharp beat.

3\. VOICE CHECK  
\- Compare voice, rhythm, and any callbacks against the previous chapter's  
  actual prose. Flag any tonal shift or dropped/contradicted callback.  
  Skip entirely if there's no previous chapter.

OUTPUT  
Report findings under each heading, in order. For every issue: quote the  
line, state the problem in one sentence, give a suggested fix. If a  
section has nothing, say so explicitly.

VERDICT (one line, at the end):  
\- Send back for revision: any Story Check (\#2) issue, or an Input  
  Conflict.  
\- Minor fixes needed: only Mechanical (\#1) or Voice (\#3) issues.  
\- Ready to publish: nothing flagged anywhere.

---

## **Part E: Generate a Book Cover**

ROLE: You are a book-cover art director who writes precise,  
production-ready prompts for AI image generators.

TASK: Using the inputs below, write ONE detailed image-generation prompt.  
Output only the prompt. No preamble, no commentary.

REQUIRED  
\- Genre: \[genre\]  
\- Title: \[X\]  
\- Author (pen name): \[pen name\]  
\- Platform restrictions: \[paste anything the platform states, or leave blank\]

OPTIONAL (if left blank, choose genre-appropriate defaults and state which  
defaults you used in one line before the prompt)  
\- Mood/tone: \[mood\]  
\- Art style: \[art style\]  
\- Color palette: \[palette\]  
\- Comparable covers: \[comp titles\]

CONSTRAINTS  
\- No copyrighted characters, real people, or trademarked logos.  
\- No invented bestseller claims, awards, or fictional backlist.  
\- No em dashes or en dashes anywhere in the output.

If Genre, Title, or Author is missing or contradictory, ask ONE  
clarifying question and stop. Don't guess.

OUTPUT  
1\. The prompt, as one plain-text paragraph.  
2\. 2-3 common aspect ratios and their typical use (ebook thumbnail, print  
   wrap, wide banner). Note that exact specs vary by platform, so confirm  
   against the actual platform's current requirements.

Next steps (yours, not the AI's): paste the prompt into your image generator, pick the aspect ratio matching your platform, generate 3-5 variations and iterate. Vary composition and typography space rather than accepting the first result.

---

## **Part F: Submit to a Platform**

### **Quick Comparison**

|  | GoodNovel | SevenCat/TapRead | StaryWriting/Dreame | LetterLux | MoboReader |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Register at | goodnovel.com | sevencat.com | starywriting.com | LetterLux site | author.moboreader.com |
| Min. to apply | 5,000 words | Not specified 🚩 | Not addressed 🚩 | 5,000 words (up to 30k on resubmit) | 10 ch. AND 10,000 words |
| Review time | 10-14 days \+ 2-4 weeks | 7 days (non-excl.) / 14+ (excl.) | Not addressed 🚩 | Not stated 🚩 | Not stated 🚩 |
| Genre restrictions | None named | Not addressed 🚩 | Not addressed 🚩 | Explicit reject list | Theme, genre, tag system |
| AI content | Discouraged, grammar-only | Full bonus cancellation if found | Not addressed 🚩 | Supporting-tool OK, full-AI banned | Submission-blocking gate |
| Recommended length | 0.8k-1k words | Not stated 🚩 | Not stated 🚩 | ≥1,000 words | 1,500-2,500 words |
| Structure | Single platform | Single platform | Single platform | Distributes to 9 partner apps | Single platform |

🚩 \= not confirmed in source. Verify directly with the platform before relying on it.

### **Platform Checklists**

**GoodNovel**

* \[ \] Account \+ book entry at goodnovel.com  
* \[ \] 5,000+ words uploaded, then "Apply for a contract"  
* \[ \] First 10 chapters polished (this is what gets read for the contract decision)  
* \[ \] Full ending outline ready to submit alongside the application  
* \[ \] Cover cleared: no explicit sexual imagery, no guns/knives/blood, no alcohol/tobacco aimed at minors, no unlicensed art, no celebrity photos  
* \[ \] Not fan fiction of non-public-domain IP  
* \[ \] Government ID ready if under 21 (parent/guardian co-sign required)  
* Exclusive contracts: English, Spanish, French, Indonesian, or Filipino, one per submission.

**SevenCat / TapRead**

* \[ \] Account at sevencat.com  
* \[ \] 🚩 No stated minimum to *apply*. Only the 30,000-word bonus threshold is documented. Confirm directly.  
* \[ \] Application as complete as possible before submitting (incomplete exclusive applications get delayed)  
* \[ \] Original English content, no AI-generated or plagiarized text (grounds for bonus cancellation and possible removal)  
* \[ \] Plan to separately apply for "premium" once you cross 30,000 words  
* Two paths: Standard track, or Top Author Program if you've earned $30k+ on any platform in the past 2 years (contact your editor directly for that one).

**StaryWriting / Dreame** 🚩 *Biggest documentation gap. The actual submission process isn't confirmed anywhere in source material. Treat nothing below as settled.*

* \[ \] Account at starywriting.com; tools under "Manage Stories" (desktop) or "Write" (app)  
* \[ \] 🚩 Minimum word count to apply: unconfirmed  
* \[ \] 🚩 Genre/content restrictions: unconfirmed  
* \[ \] 🚩 Review timeline: unconfirmed  
* Get the actual onboarding page or talk to a current Dreame author before planning around this platform.

**LetterLux** *(a distributor: one contract pushes your book to 9 partner apps at once; "exclusive" means exclusive to the LetterLux network, not one app)*

* \[ \] 5,000 words submitted for review (may be invited to extend to 30,000 on a second pass)  
* \[ \] First 6 chapters (\~5,000 words) specifically polished (this is what's shown free and what gauges signability)  
* \[ \] Genre checked against the reject list: Poetry, Political/Historical, Slice of life, Short Story Compilation, and Pure Horror are **not accepted**. Best odds: Sports Romance, Werewolf, YA/Teen.  
* \[ \] AI use limited to supporting-tool level, not generation  
* \[ \] Aware scheduled chapters can't post within 2 hours, publish in order, and editing one forces immediate publication (all times UTC+0)

**MoboReader**

* \[ \] Account at author.moboreader.com; book entry with language, title, blurb, locked-chapter point, genre, tag, editor info  
* \[ \] 10 chapters AND 10,000 words uploaded (both required)  
* \[ \] Classification assigned in order: Theme, then Genre, then Tags (at least 2 tags; 1 must be niche-specific if this is a Niche Genre)  
* \[ \] Not AI-generated, not plagiarized, not fan fiction  
* \[ \] Chapters targeting 1,500-2,500 words. Don't reuse a chapter written to another platform's shorter length unchanged  
* 🚩 Any "complete X words by \[date\]" target you see is likely tied to a specific contest, not a standing rule. Confirm the current live target.

### **Universal Pre-Submission Checklist**

* \[ \] Manuscript sample meets or exceeds that platform's stated minimum  
* \[ \] First chapters specifically polished (every platform uses these as the actual signing decision)  
* \[ \] Genre checked against that platform's accepted list  
* \[ \] Confirmed not fan fiction of non-public-domain IP, if banned there  
* \[ \] AI-assist level checked against that platform's tolerance  
* \[ \] Chapter length adjusted to that platform's norm  
* \[ \] Cover art checked against content restrictions, where stated  
* \[ \] Completion/ending outline ready, if that platform asks for one

---

## **Glossary**

* **Seed**: the raw, one-paragraph premise (Stage 5). Everything downstream builds from this.  
* **Scorecard**: the 8-10 criteria rubric (Stage 6\) used to grade a seed.  
* **FMC / ML**: Female Main Character / Male Lead.  
* **Trope**: a reusable story convention ("Rejected Mate," "Twin Switch").  
* **Arc/season**: a bounded stretch of chapters with its own rising action and climax.  
* **Bingeability**: pacing/endings engineered to make the reader open the next chapter immediately.  
* **Story-State Ledger**: the live continuity record, made up of the last Master Ledger Update plus every Ledger Delta since. This is what you paste into every chapter and editing prompt.  
* **Ledger Delta**: 2-5 bullets summarizing what one chapter changed. Generated every chapter, checkpoint or not.  
* **Checkpoint**: a chapter flagged to trigger a full Master Ledger Update. Default: batch-end, or immediately after anything major.  
* **Master Ledger Update**: the full ledger, rewritten at a checkpoint to fold in every delta since the last one.  
* **Arc Snapshot**: a condensed reference of the current arc's objective, conflict, twists, climax, pulled from the blueprint.  
* **Exclusive / non-exclusive**: exclusive gives one platform sole rights; non-exclusive lets you publish the same story in multiple places, usually with fewer up-front bonuses.

