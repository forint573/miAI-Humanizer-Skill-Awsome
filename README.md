<div align="center">

# HumanCopywrite ✸☽

(agent built stuff)

**Humanize AI-written marketing and long-form copy in Claude. It removes AI tells and process bleed, keeps your facts and your voice, and pushes past clean-but-empty writing to the specific, true point worth reading.**

[![CI](https://github.com/forint573/human-copywrite/actions/workflows/ci.yml/badge.svg)](https://github.com/forint573/human-copywrite/actions/workflows/ci.yml)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Claude Skill](https://img.shields.io/badge/Claude-Skill-d97757.svg)](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
[![Tuned for Sonnet 5, Opus 4.8 & Fable 5](https://img.shields.io/badge/Tuned_for-Sonnet_5_·_Opus_4.8_·_Fable_5-8a63d2.svg)](#tuned-for-claude-sonnet-5-opus-48-and-fable-5)

</div>

---

## TL;DR

HumanCopywrite drafts and de-slops marketing and long-form copy: landing pages, e-books, reports, case studies, sales pages, product copy, and founder notes. Its main job is to turn a quick sketch into a consumable template, clean, specific, voiced, and honestly sourced, that a human finishes into final prose. It keeps the writing about the reader and the product, it refuses to invent facts, and it preserves a real voice instead of flattening it into house style. It also does the part most humanizers skip: it makes the copy say something. Clean but empty is a failure here, not a finish line.

It is built for copywriters, marketers, and founders who draft with AI and want copy that does not read like AI. It is not an AI-detector bypass. It makes weak copy read like a person actually wrote it, and worth the reader's time once they did.

Version 4 runs on Claude Sonnet 5, Claude Opus 4.8, and Claude Fable 5: a concrete edit bar instead of taste, a fixed output shape, fact safety that flags your claims instead of deleting them, and a deliberately light instruction layer, because Anthropic's strongest current models do best with clear goals and hard rules, not micro-scripts. The details are in [Tuned for Claude Sonnet 5, Opus 4.8, and Fable 5](#tuned-for-claude-sonnet-5-opus-48-and-fable-5).

Install it in one line, then ask Claude to humanize your copy.

```bash
git clone https://github.com/forint573/human-copywrite.git && \
  cp -r human-copywrite/human-copywrite ~/.claude/skills/
```

Then open Claude and say *"humanize this landing page"* or *"finalize this draft and strip the planning notes."* That is the whole setup.

---

## What it is

HumanCopywrite is an [Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) for marketing and long-form copy. It fixes two failures at once.

The first is process bleed: the finished piece starts narrating the hidden work behind it. The copy points at the chat, the outline, the roadmap, an earlier draft, or a leftover scaffold instead of speaking to the reader about the product, the offer, the proof, the objection, and the next step.

The second is clean nothing: the copy comes out tidy and de-slopped and still says nothing only this writer could say. Most humanizers stop at the first failure and ship the second. This one treats both as failures. The standard it holds copy to is not "reads like a human wrote it" but "a sharp human would be glad they wrote it, and a busy reader is glad they read it."

It also avoids the two ways humanizing usually backfires:

- It never invents numbers, names, testimonials, results, awards, or claims. Missing proof becomes a visible placeholder, not a fabrication. And it never deletes *your* real numbers either: specifics already in your draft stay in the copy and get flagged for verification instead.
- It never flattens good human writing into one generic voice. A provided writing sample beats the skill's default taste every time.

## The two tests

Every sentence in the output should pass two questions. The first catches process bleed:

> Would this sentence make sense to a reader who never saw the project, chat, plan, outline, prompt, or drafting process?

If not, cut it, or rewrite it around the reader, product, offer, proof, objection, or next step.

The second catches clean nothing:

> Could this exact sentence appear on a competitor's page, or about a different product?

If yes, it carries no information. Replace it with the specific, true thing only this writer could say, drawn from the real material.

## See it in action

The first row carries two problems at once: it narrates the chat and the plan, and it leans on vague authority. The second row is clean but empty. The right cells are what the skill returns.

| Before | After |
| --- | --- |
| *"Based on our discussion, this guide starts with the problem, then moves into the framework we landed on. Our platform cuts onboarding time by 73% and is trusted by leading enterprises."* | *"Onboarding breaks down in three predictable places. Here is where, and how to fix each one. Our platform cuts onboarding time by 73%. `[ADD NAMED CUSTOMER]`"* |
| *"We're committed to excellence and deliver world-class solutions that help businesses succeed."* | *"Your reps stop copying leads between four tabs. The CRM writes call notes back to the deal on its own, so follow-up happens the same day instead of next week. `[CONFIRM SUPPORTED INTEGRATIONS]`"* |

In the first row, the chat reference and the roadmap narration are gone and the copy opens on the reader's problem. The 73% is your material, so it stays in the copy, and the editorial note after the deliverable flags it: *"Verify: the 73% is from your draft; confirm it before publishing."* The vague "leading enterprises" carries no name, so it becomes a placeholder for a real one. The second row shows the other half of the job: the committed-to-excellence line passes every grammar check and still says nothing, so the skill replaces it with the specific mechanism a competitor could not claim, and flags the one detail it cannot verify.

## A humanizer is a persuasion amplifier

Here is the uncomfortable part, and the reason this skill is built the way it is. Every edit it makes, clearer, more human, more specific, more confident, also makes the copy more persuasive. Persuasion is value when it is pointed at something true. It is harm when it is pointed at something false, because a polished, human, mechanism-backed claim gets trusted in a way that obvious AI slop never does. The better a humanizer works, the more damage it can do to copy that is not honest.

So this skill ships the firewall that the persuasion demands. Three rules, in `references/integrity.md`:

- **Persuasion never outruns evidence.** The skill may make a claim clearer. It may not make it more certain, more proven, or more universal than your source supports. It watches the quiet escalations, like "may reduce" drifting to "eliminates," that read like style edits and quietly change the truth.
- **Load-bearing caveats survive every edit.** It cuts empty hedging, never a real safety, legal, or financial qualification. Removing one of those to add punch hides risk, so it stays.
- **Authenticity is never manufactured.** The skill humanizes your real copy. It will not invent reviews, testimonials, social proof, scarcity, or urgency, and it will not put words in a real person's mouth. Missing proof becomes a placeholder, exactly like a missing metric. Guarantees, income claims, and countdowns that are already in your draft get weakened or marked for confirmation inline, because those should never ship unverified.

This is also why it is not an AI-detector bypass. The goal is honest writing that reads well, not deception that reads human. The standard the whole skill answers to: a reader who trusts this copy because it is clear and human should be safe in trusting it.

## Sketch in, template out

This skill is most useful as a force multiplier for a human writer, not a replacement for one. You give it a quick sketch or a half-built draft. It returns a consumable template: the process bleed stripped, the structure sound, the claims specific and within the evidence, the voice intact, and visible placeholders wherever real proof is missing. A person then finishes that template into final prose, filling the placeholders, confirming the flagged claims, and making the last calls.

That is the honest scope. The skill does the mechanical and structural work, fast. It does not replace the human judgment that turns a strong template into something worth publishing, and it is not meant to.

### Use it with the Hungarian translation skill

If your final copy needs to be Hungarian, chain this with [`translating-english-to-hungarian`](https://github.com/forint573/ENG-HUN-Translation-skill), which renders English as idiomatic, native Hungarian instead of a literal calque.

Humanize in English first, then translate. The chain is sketch, to a consumable English template here, to native Hungarian there, to final prose by a human. The handoff carries the voice (including the formal `ön` or informal `te` register), leaves placeholders untranslated for the human to fill, and keeps the integrity rules across the language line, so the Hungarian never reads more certain than the English or drops a caveat for flow. The details are in `references/translation-handoff.md`.

## Tuned for Claude Sonnet 5, Opus 4.8, and Fable 5

Anthropic's current models changed how instructions behave, in two directions at once. Sonnet 5 and Opus 4.8 follow prompts literally: they do not silently generalize a rule beyond its stated scope, and when you tell them to be conservative, they are exactly that conservative, which turns vague taste ("don't nitpick") into silent under-editing. Claude Fable 5, the Mythos-class tier above Opus, adds the opposite lesson: Anthropic's own migration guidance says prompts and skills written for prior models are often *too prescriptive* for it and reduce output quality, so the fix is stating goals and constraints, not enumerating steps.

Version 4 is built for both pressures:

- **A concrete edit bar replaces qualitative taste.** Every tell in the catalog is tagged: always-fix (a single em dash, one "as we discussed" gets fixed anywhere it appears), cluster-fix (style tells change only when two land in one paragraph or three in 150 words), or context. "Don't over-edit" is a definition, not a mood, so the same draft comes back the same way every time. Definitions like this are not over-prescription; they are the spec, and all three models need them.
- **A light instruction layer.** `SKILL.md` states the goals, the bars, and the hard integrity rules once, without restating them section after section, and without micro-scripting the obvious. The deep catalogs live in `references/` behind named load triggers, and the full tell catalog loads only for pieces long enough to need it. Less context per run, and better output on Fable 5, which does its best work from a clear spec rather than a step list.
- **Fact safety that respects your material.** Specifics the model would have to invent become visible placeholders. Specifics already in your draft stay in the copy and get flagged under `Verify` in the editorial note, because deleting your real numbers "to be safe" is its own kind of harm. Guarantees, income claims, scarcity, and deadlines are the exception: those get weakened or marked inline no matter where they came from.
- **Coverage first, filtering second.** Cleanup sweeps the entire piece and marks every candidate without judging, then the bar decides what changes. A conservative instruction can never quietly turn into skipped findings.
- **A fixed output shape with named exceptions.** The reply starts with the deliverable's first line and ends with, at most, a six-line labeled editorial note (Changed / Verify / Placeholders / Flagged / Register). Proposing voice directions before drafting, and file-based deliverables in agent workflows, are the two stated exceptions, so the contract never fights the context it runs in.
- **Voice directions instead of a house style.** Left to their defaults, these models settle into one consistent voice, and generic "sound more human" prompts just swap it for a different fixed voice. For voice-sensitive work with no sample, the skill proposes two or three concrete directions as rewritten opening lines and builds only the one you pick.

Running it, a few settings matter:

- **Effort.** `high` (the default on all three models) is right for normal drafting and cleanup. Raise to `xhigh` for substance-heavy rescue rewrites of long pieces. At `low`, these models scope tightly to the letter of the request, which fights the skill's coverage pass.
- **Thinking.** Sonnet 5 runs adaptive thinking by default; leave it on. On Opus 4.8, thinking is off unless you set `thinking: {type: "adaptive"}`; set it for anything past mechanical cleanup, since the substance and integrity passes are exactly the multi-step reasoning it helps. On Fable 5, thinking is always on and needs no setting; omit the `thinking` parameter entirely (an explicit "disabled" config is rejected).
- **Token headroom.** Sonnet 5's tokenizer produces roughly 30% more tokens for the same text than Sonnet 4.6, and thinking shares the `max_tokens` budget on all three models. For e-book chapters and long reports, raise `max_tokens` or the output truncates mid-template. Fable 5 and Opus 4.8 share a tokenizer, so counts carry over between those two.
- **One well-specified turn.** All three models do their best work when the task, voice, facts, and constraints arrive upfront rather than drip-fed across turns. Put the brief, the writing sample, and the proof in the first message.

Earlier Sonnet and Opus models still run the skill fine; they just benefit less from the calibration.

## Install

Three ways, fastest first.

**1. One line, Claude Code.** Installs a personal skill that is available in every project:

```bash
git clone https://github.com/forint573/human-copywrite.git && \
  cp -r human-copywrite/human-copywrite ~/.claude/skills/
```

For a project skill that travels with one repo, copy the folder into that repo's `.claude/skills/` instead.

**2. Installer script.** From a clone, run `./install.sh` for user scope, or `SCOPE=project ./install.sh` to install into the current repo. To install without cloning first:

```bash
curl -fsSL https://raw.githubusercontent.com/forint573/human-copywrite/main/install.sh | bash
```

**3. Packaged `.skill` file.** Download it from the [Releases](https://github.com/forint573/human-copywrite/releases) page, or build it yourself:

```bash
make build   # writes dist/human-copywrite.skill
```

Upload that file anywhere custom Claude skills are accepted. The archive keeps the skill folder at its root.

## Use it

Once installed, Claude reaches for the skill on its own when you ask for things like:

- "Humanize this landing page and make it sound less like AI."
- "Finalize the homepage copy from the outline. Remove planning notes and make it paste-ready."
- "Draft a sales page for this offer using only the proof in the brief."
- "Clean up this e-book chapter. Keep the arguments, but lose the self-announcing intros."
- "This copy is clean but it says nothing. Make it specific and sharp without inventing anything."

It stays out of the way for code, raw data, tables, changelogs, release notes, legal terms, technical reference docs, and casual chat. There, factual structure matters more than this posture.

## Optional scanner

For long drafts, a heuristic scanner flags leftover process bleed, wrapper text, hype clusters, empty claims, high-liability claims, manufactured pressure, vague authority, and em or en dashes:

```bash
python human-copywrite/scripts/copy_scan.py draft.txt
# or
cat draft.txt | python human-copywrite/scripts/copy_scan.py
```

It produces false positives on purpose. Treat each result as a reason to look, not a verdict. Human judgment always wins.

> This README was written with the skill's own rules: no em dashes, no hype clusters, no process bleed, no invented facts, nothing that fails the swap test. The only places the rules are broken on purpose are the *Before* cells above, which exist to show the patterns the skill removes.

## What's inside

```text
human-copywrite/
├── SKILL.md                      # the active instruction layer
├── README.md                     # the skill's own package notes
├── references/
│   ├── process-bleed.md          # the seven leaks, examples, fast-scan phrases
│   ├── substance.md              # the intelligence layer: how to say something worth reading
│   ├── integrity.md              # the safety layer: do more good than harm
│   ├── ai-tells.md               # tell catalog, every item tagged with its edit-bar level
│   ├── qa-scorecard.md           # 10-category, 0 to 2 readiness score
│   ├── voice-calibration.md      # matching a sample or brand voice
│   └── translation-handoff.md    # chaining with the Hungarian translation skill
├── scripts/
│   └── copy_scan.py              # optional heuristic scanner
└── tests/
    └── test-prompts.md           # trigger / no-trigger checks and samples
```

## Design notes

- **Lean active layer.** `SKILL.md` holds only what the model needs in context to act: the goals, the bars, and the hard rules, stated once. The deeper catalogs live in `references/` and load on named triggers, which keeps the instruction layer clear on every model and follows Anthropic's guidance that its strongest models do worse under over-prescriptive prompts.
- **Clean is not the finish line.** De-slopping removes what should not be there. `substance.md` supplies what should: the specific, defensible point only this writer could make. The skill treats clean-but-empty copy as a failure and draws the substance from your material, never from an invented fact.
- **Persuasion comes with a firewall.** A humanizer makes copy more convincing, so `integrity.md` makes sure it never gets more convincing than it is true. Persuasion never outruns evidence, real caveats stay, and authenticity is never faked.
- **A bar, not a mood.** `ai-tells.md` names why something reads as machine written, and every item carries an edit-bar tag: always-fix, cluster-fix (two tells in a paragraph, or three per 150 words), or context. One formal word is still not proof of AI writing, and the judgment is a definition the model applies the same way every run.
- **Your facts are yours.** The skill never invents a specific, and it never deletes one of yours either. Missing proof becomes a placeholder; your existing claims stay and get flagged for verification. Only guarantees and pressure tactics get intervened on inline, because those cause real harm when they ship unverified.
- **A fixed reply shape.** Deliverable first, labeled editorial note after it only when needed. The copy never arrives buried in commentary.
- **Lightest effective edit.** Drafting, finalization, and cleanup are separate modes. The skill picks the smallest one that solves the task instead of rewriting good prose for its own sake, and the bar defines what "smallest" means.

## FAQ

**Who is this for?**
Copywriters, marketers, founders, and anyone who drafts marketing or long-form copy with AI and wants it to read like a person wrote it.

**Does it bypass AI detectors?**
No. This is not an AI-detection bypass tool. It improves real copy: it removes AI tells and process bleed, flags unverified claims, and keeps your voice. The goal is honest, publishable writing, not gaming a detector.

**Which models does it work with?**
It is written for Claude and calibrated for Claude Sonnet 5, Claude Opus 4.8, and Claude Fable 5: the concrete bars that literal instruction-followers need, and the light, goal-stated instruction layer that Fable 5 does its best work under. Earlier Sonnet and Opus models run it fine and simply benefit less from the calibration. It works anywhere Claude reads skills, including Claude Code, the desktop and web apps, and any setup that accepts custom skills.

**What changed in version 4?**
The skill was renamed to HumanCopywrite, and the instruction layer went on a diet: roughly a third smaller, with duplicate rule statements removed and the full tell catalog loading only for pieces long enough to need it. Fact safety now distinguishes origins: specifics the model would have to invent become placeholders, while specifics from your own draft stay in the copy and get flagged under `Verify` instead of being deleted. Title Case headings stopped being treated as an automatic AI tell. The output contract gained its two honest exceptions (voice directions, file-based workflows), and the scanner instruction is gated on script execution being available. See [CHANGELOG.md](CHANGELOG.md) for the full list.

**Will it invent facts to fill a gap?**
No. Missing proof becomes a visible placeholder such as `[ADD VERIFIED METRIC]`, never a fabricated number, name, or testimonial.

**Will it delete the real numbers already in my copy?**
No. Specifics in your draft are your material: they stay in the copy, and load-bearing ones are listed under `Verify` in the editorial note so you confirm them before publishing. Only unsettled markers (TODOs, scaffold notes), drafts you flag as unverified, and high-liability claims like guarantees or countdowns get intervened on inline.

**Does it just remove AI words, or does it actually improve the writing?**
Both, and the second part is the point. Removing tells leaves a gap, and a gap filled with a cleaner version of nothing is still nothing. The skill fills it with a specific, defensible claim drawn from your material, the kind a competitor could not also make. If the substance genuinely is not there, it flags the gap instead of inventing one.

**Can it be used to make false claims more convincing, or to fake reviews and urgency?**
No, and preventing that is the job of the integrity layer. The skill makes a claim more persuasive only when the evidence is already there. It never raises certainty past the source, never strips a safety or legal caveat to add punch, and never manufactures reviews, social proof, scarcity, or urgency. See `references/integrity.md`.

**Does it produce final, ready-to-publish copy?**
No, and it is not trying to. It produces a consumable template: clean, specific, voiced, and honestly sourced, with visible placeholders where proof is missing and flagged claims where proof needs confirming. A human finishes it into final prose.

**Can I use it with the Hungarian translation skill?**
Yes. Chain it with [`translating-english-to-hungarian`](https://github.com/forint573/ENG-HUN-Translation-skill). Humanize in English first, then translate, so the Hungarian comes out idiomatic and native rather than a literal calque. See `references/translation-handoff.md`.

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md). Changes to behavior should keep [`tests/test-prompts.md`](human-copywrite/tests/test-prompts.md) honest and pass the automated checks (`make check`).

## License

Apache License 2.0. Copyright 2026 Virág Làzár Csaba ✸☽. See [LICENSE](LICENSE) and [NOTICE](NOTICE).

> "Claude", "Sonnet", "Opus", and "Fable" are model names from Anthropic. This is an independent community skill. It is not affiliated with or endorsed by Anthropic.
