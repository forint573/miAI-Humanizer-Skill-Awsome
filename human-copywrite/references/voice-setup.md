# Project voice setup: MY_OWN_VOICE.md

This flow turns the skill into a copywriter for one specific project. It runs a short interview once, writes the answers to `MY_OWN_VOICE.md` in the project root, and every later copy task in that project loads the file automatically.

## When to run it

- The user invokes the skill with a setup argument: `/human-copywrite setup` (or `setup-voice`).
- The user asks in their own words: "set up my voice," "set up the brand voice for this project," "make the copywriter sound like us."
- Offer it (once, briefly) when a voice-sensitive piece is requested in a project that has no MY_OWN_VOICE.md and no sample; if the user wants immediate output instead, proceed with the grounded default.

## The interview

Ask everything in one batched message, not one question at a time. Skip any question the context already answers (an existing site, a README, prior copy in the repo) and instead show what you inferred for confirmation. Six questions, none padded:

1. Voice: paste one to three short samples that sound like you or the brand (an email you liked, an old page, a post). Links or files work too.
2. Reader: in one line, who arrives, and what do they want or fear?
3. Product: one plain sentence on what it is, plus the mechanism that makes it work.
4. Proof: what can you claim today with a source? Metrics, named customers, certifications. Only what is verified; this list is what the copy may state as fact.
5. Posture: dry expert, warm founder, institutional, playful, or describe it. Plus any words or moves the brand never uses.
6. Practical: US or UK spelling; roughly how technical the reader is; any caveat or legal line that must survive every edit; if output will ever be Hungarian, `te` or `ön`.

Then write the file with the template below, show it, and say it can be edited by hand any time or refreshed by rerunning setup.

## The template

Write `MY_OWN_VOICE.md` at the project root exactly in this shape, filling only what the user gave; leave a section out rather than padding it:

```markdown
# MY_OWN_VOICE for <project name>

## Voice samples
> <sample 1>

> <sample 2>

## Reader
<one line: who arrives, what they want or fear>

## Product truth
<one plain sentence>
Mechanism: <the how that makes it believable>

## Verified proof
- <claim> (source: <where this is verified>)

## Posture and register
<posture description; spelling; technicality; te/ön if relevant>

## Never say
- <banned word or move>

## Always keep
- <caveat or legal line that survives every edit>
```

## How the file is used

Before any copy task, check the project root (then `.claude/`) for `MY_OWN_VOICE.md` and read it if present. Then:

- Voice samples count as the provided writing sample: they win over the skill's default taste and can protect cluster-bar style items they demonstrably use.
- Reader and Product truth pre-fill the source sheet for website prose.
- Verified proof entries are sourced facts: the copy may state them without placeholders, and the editorial note does not need to re-flag them.
- Never say entries are always-fix bans, same weight as the buzzword blocklist.
- Always keep entries are load-bearing caveats: they survive every edit, in every voice.

Precedence stays the same as everywhere else in this skill: MY_OWN_VOICE.md overrides default taste and cluster-bar style items, and never overrides the integrity layer. A voice file cannot authorize an invented metric, a stripped safety caveat, or manufactured urgency.

If the file exists but is stale or contradicts what the user now says, follow the user, and offer to update the file.
