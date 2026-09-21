# Drafting workflow: git and Google Docs

The loop is: draft in git, review in Docs, approve, import back to git.
Git is the source of truth. Google Docs is the review surface.

## Google Drive layout

```
AI Novel Workspace/                        1lzW3g9wHfKu2iHXF2MuFKwBnp4cBdoaD
  Novel 1 - Rejected by the Alpha/         1gv1IjYCdpfvTvlGgxf3jd63xSCenbZM7
    Ch 005 - The Long Walk
    Ch 006 - Left for the Wolves
    ...
```

One Doc per chapter, titled `Ch NNN - Title`.

### Why one doc per chapter, and not tabs

The original plan was a single doc with one tab per chapter. That is not
possible here: tabs are a Google Docs API feature, and the available connector
is the Drive API, which creates single-tab documents only.

More importantly, the connector can create a doc and read it back, but it
cannot write into an existing doc. One doc per chapter turns that limitation
into a safety property: the assistant can never overwrite edits made in Docs,
because it never writes to a doc that already exists. A rolling multi-chapter
doc would require regenerating the whole doc on every addition, which risks
destroying in-progress edits.

If real tabs matter more than portability, Claude's own Docs connector supports
them. It is tied to the Claude account, so chapters stored there may become
inaccessible if that subscription lapses. Google Docs was chosen for
portability instead.

## The loop

### 1. Draft (assistant)

Assemble the Context Stack from SOP Part C, draft the chapter, then:

```
python3 scripts/check.py novels/<slug>/chapters/chNN-slug.md
```

Fix everything blocking before going further.

### 2. Publish for review (assistant)

Create a Doc in the novel's Drive folder, titled `Ch NNN - Title`, containing
the chapter text.

**Publish only once the chapter has converged.** Because the connector cannot
write into an existing doc, every revision means trashing the old doc and
creating a new one, which changes the URL and leaves dead links behind. So
finish the gates, do a full read-through, and settle any craft notes first.
Chapters 5 and 6 were published three times over before this rule existed.

**Give the author the folder link, not the per-chapter link**, as the stable
entry point. The folder always lists the current docs, so it survives
republishing:

    https://drive.google.com/drive/folders/1gv1IjYCdpfvTvlGgxf3jd63xSCenbZM7

Per-chapter links are fine for pointing at one specific chapter, but they go
stale the moment that chapter is revised.

### 3. Review (author)

Edit directly in the Doc, or leave comments. Both survive: the assistant reads
the doc back with comments included.

**Turn off Docs autocorrect before editing.** Tools > Preferences, then uncheck
"Use smart quotes" and remove any substitution that produces a dash. Docs
otherwise converts `--` into an em dash and straight quotes into curly ones,
which silently violates house style. The import step repairs and reports this
either way, but it is cheaper not to introduce it.

### 4. Approve (author)

Say so explicitly. Nothing is committed without it.

### 5. Import and commit (assistant)

```
# read the doc back, save the raw text, then:
python3 scripts/from_docs.py raw.txt novels/<slug>/chapters/chNN-slug.md \
    --title "The Long Walk" --num 5 --pov Wren
python3 scripts/check.py novels/<slug>/chapters/chNN-slug.md
```

`from_docs.py` repairs Docs artifacts and reports every change it made. Read
that report. An em dash it replaced with a comma may deserve a better fix.

Then append the Ledger Delta to `ledger.md`, run `check.py` across the whole
novel, commit, and push.

### 6. Merge

Drafting happens on `draft/<novel>-chNNN`. Once the chapters are approved and
committed, merge into `main`.

## What check.py enforces

Blocking: chapter number matches filename and heading, POV header correctness
(by possessive interiority, not mention count), no dashes, word count in range,
no banned words, paragraphs of 3 sentences or fewer, a ledger delta present for
every drafted chapter.

Advisory: near-miss substitutes for banned words, runs of clipped one-word
fragments, overuse of "it wasn't X, it was Y".

What it cannot judge, and still needs the Part D audit: continuity against the
ledger, outline fidelity, whether the cliffhanger lands on the specified type,
and voice consistency against the previous chapter.
