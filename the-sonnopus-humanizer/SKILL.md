---
name: the-sonnopus-humanizer
description: "Write, finalize, and sharpen reader-facing marketing and long-form copy (landing pages, e-books, reports, case studies, sales and product copy, founder notes) so it reads like a specific human wrote it and actually says something worth reading: specific, defensible, and non-obvious, not clean but empty. Apply it to humanize, de-slop, make something sound less like AI, rewrite naturally, tighten, polish, clean up, sharpen, or add substance to a draft. It removes process bleed (roadmaps, outlines, internal decisions, scaffolding, and chat residue that leak from a long build session), preserves facts (never inventing numbers, names, or results, using visible placeholders instead), keeps a real voice rather than one house style, and pushes generic claims toward the specific, true, load-bearing point without ever making a claim more certain or proven than the source supports. Use it proactively when finalizing a deliverable. Not for code, data, changelogs, release notes, legal terms, or casual chat."
---

# The Sonnopus Humanizer

Use this skill to draft, finalize, or clean up reader-facing copy so it sounds like a specific human wrote it, says something worth reading, stays truthful, and never exposes the planning process that produced it.

Its highest-value use is turning a quick sketch or half-built draft into a consumable template: clean, specific, honestly sourced, voiced, with visible placeholders where proof is missing. A human then finishes that template into final prose. The skill does the mechanical and structural work so a person can do the judgment work. Treat the output as a strong draft for human finishing, not as publish-without-review copy.

The skill has two jobs, and clean copy only does the first one.

The first job is subtractive: keep the finished piece about the reader, the product, the offer, the proof, the objection, and the next step. Remove anything about the chat, outline, roadmap, internal decisions, drafts, prompts, files, or production process unless the user explicitly asked for a retrospective, changelog, or process document.

The second job is additive: make the copy worth the reader's time. Copy can pass every cleanliness check in this skill and still say nothing a reader could not have guessed before opening it. That is clean nothing, and it is a failure, not a pass. The standard is not "reads like a human wrote it." It is "a sharp human would be glad they wrote it, and a busy reader is glad they read it." The intelligence comes from the true material, never from inventing an impressive claim. This second job is `references/substance.md`.

Both jobs are bound by one rule that outranks them: do more good than harm. A humanizer makes copy more persuasive, so it must never make a claim more believable than it is true, strip a caveat the reader needs, or manufacture proof the source does not have. This rule is `references/integrity.md`.

## Scope

Use this for finished or near-finished copy: landing pages, websites, sales pages, e-books, reports, case studies, product copy, email copy, founder notes, brand copy, and editorial marketing copy.

Also use it when the user asks to humanize, finalize, polish, clean up, rewrite naturally, make less AI-sounding, de-slop, or turn planning work into a reader-facing deliverable.

Do not use it for code, raw data, tables, changelogs, release notes, legal terms, technical reference docs, or casual chat. In those cases, clarity and factual structure matter more than this copy posture.

Every rule in this skill applies to the entire deliverable: every sentence and every element, including headlines, subheadings, bullets, CTAs, button and link microcopy, captions, pull quotes, image alt text, and footers. Never apply a rule to the body paragraphs only, or to the first section only.

## Choose the mode

Drafting: write new copy from the brief. Do not invent facts the brief did not give you.

Finalization: turn a planned or half-built artifact into a clean, consumable template ready for human finishing. This is the highest-value use. Strip scaffolding, planning residue, assistant wrapper text, and outline language.

Cleanup: improve an existing draft. Preserve the meaning, claims, caveats, sections, and proportions unless the user asks for a deeper rewrite.

Use the lightest mode that solves the task. The edit bar below defines exactly what the lightest sufficient edit is; apply it in full, neither more nor less.

## The output contract

The reply contains, in this order, and nothing else:

1. The deliverable, starting at the first line of the reply. No preamble, no "here is the copy," no restated brief, no plan.
2. An editorial note after the deliverable, only when there is something the user must act on or decide.

The editorial note is at most six short lines, each labeled. Use only the labels you need:

- Changed: the one or two structural moves worth knowing about. Not a list of every edit.
- Verify: claims kept in the copy that still need a source before publishing.
- Placeholders: how many brackets were left, and where.
- Flagged: sections that remain clean nothing, and what real material would fix them.
- Register: `te` or `ön`, only when the copy is headed to Hungarian translation.

Example of a complete, well-formed note:

> Changed: opened on the reader's compliance risk instead of the feature list; merged the two overlapping proof sections.
> Verify: the "SOC 2 since 2023" line is from your brief; confirm it before publishing.
> Placeholders: 3, all in the proof section.

Length is calibrated to the deliverable, not to the effort spent:

- Cleanup keeps the output within roughly the input's length. Removing process bleed may shorten it; that is the job working. Do not grow the piece to demonstrate effort, and do not compress it below what the format needs.
- Drafting writes to the format's natural length: a hero section is a headline, a sentence or two, and a CTA, not four paragraphs. An e-book chapter is not a landing page.
- If the user names a length, hit it.

## The edit bar

Work in two passes. Coverage first: read the entire piece to the last line and mark every candidate issue as you go: process bleed, unsupported specifics, AI tells, empty sections, dashes, wrapper text. Do not filter while sweeping, do not skip a candidate because it seems minor, and do not stop early because you already found enough to act on. Then apply the bar below to decide what actually changes. The bar does the filtering, not your first impression.

Always fix, even a single instance anywhere in the piece:

- Process bleed of any kind (all seven leaks below), assistant wrapper, and signposting.
- Unsupported or invented specifics: numbers, names, quotes, results. Replace with a visible placeholder.
- Certainty inflated past the source, a dropped load-bearing caveat, manufactured proof, scarcity, or urgency.
- Em and en dashes (subject to the exceptions in the dash rule).
- Scaffold residue, self-praise, generic positive conclusions, and speculative gap-filling.
- Marketing buzzwords from the blocklist in `references/ai-tells.md`, in marketing copy, unless quoted or backed by a number.

Fix only when clustered. A cluster is two or more catalog tells inside one paragraph, or three or more within any 150-word span:

- Overused AI vocabulary, -ing analysis tails, copula avoidance, rule of three, negative parallelism, elegant variation, filler phrases, empty hedging, promotional tone, and the other patterns tagged `Bar: cluster` in `references/ai-tells.md`.

Leave alone, even when you notice it:

- A single cluster-bar tell in an otherwise specific, human paragraph.
- Anything a provided voice sample demonstrably does: its punctuation habits, formality, regional spelling, favorite constructions.
- The inside of quotation marks. Never edit a quote to satisfy a style rule.

A provided voice sample or brand style can override cluster-bar style items. It never overrides an always-bar item that exists for process, fact, or integrity reasons. Every item in `references/ai-tells.md` carries its bar tag.

## The sentence test

Apply this question to every sentence in the deliverable, headings and CTAs included:

> Would this sentence make sense to a reader who never saw the project, chat, plan, outline, prompt, or drafting process?

If not, it is process bleed. Cut it or rewrite it around the reader, product, offer, proof, objection, or next step.

The production journey is not the reader's journey. The reader arrives with uncertainty and needs a reason to understand, trust, choose, buy, reply, or act. That journey is the spine.

## Process bleed to remove

Look for these seven leaks:

1. Roadmap narration: describing the order the content was built or will be presented.
2. Artifact meta: saying "in this guide," "this section explores," or announcing the content instead of delivering it.
3. Conversation residue: "as discussed," "as requested," "based on our chat," or any wrapper meant for the requester.
4. Decision disclosure: "we decided," "we landed on," "we considered," or internal strategy talk.
5. Effort padding: "after extensive research," "carefully crafted," or effort used as a substitute for value.
6. Scaffold residue: phases, TODOs, placeholders, outline labels, bracket notes, or template headers left in the copy.
7. Self-praise: calling the piece comprehensive, definitive, carefully crafted, best-in-class, or similar.

Three of the most common, with the move (describe the thing, not the making):

- Roadmap. Before: "In this guide, we will start with the fundamentals, then move to advanced tactics." After: "Most teams get the fundamentals wrong in the same three places. Fix those first."
- Wrapper or conversation. Before: "Great question. Here is the landing-page copy you asked for. Let me know if you want changes." After: delete it and ship only the copy.
- Scaffold. Before: "Phase 1: Awareness. Phase 2: Consideration. [add stats later]." After: "A buyer arrives with one question: will this work for someone like me? [ADD REAL PROOF]"

For the full set and the fast scan phrases, use `references/process-bleed.md`.

## Make it worth reading

Removing the slop leaves a gap. Fill it with substance, not with a cleaner version of nothing. The value comes from the true material: the implication the source left unspoken, the connection between two given facts, the precise word for the vague feeling, the real question under the stated one. You never reach outside the material for an impressive claim. When the substance is genuinely missing, flag it with a placeholder and say so. Do not manufacture it.

Four tests catch clean nothing:

1. Swap test. Could this exact sentence appear in a competitor's copy or on a different product? If yes, it carries no information. Replace it with the specific true thing that is only true here: the mechanism, the number, the tradeoff, the named user.
2. Negation test. Would anyone claim the opposite? "Committed to quality" is empty because no one sells low quality. Make a claim a real competitor might refuse to make, then back it.
3. So-what ladder. Ask "so what?" of each fact until you reach the consequence the reader can act on or feel. Lead with that consequence, not the bare feature.
4. Real question. Answer the question under the stated one, usually about risk, status, or effort. "Is it secure?" often means "will I be blamed if this leaks?"

Earn the claim. Show the mechanism that makes a claim true so the reader can see why, instead of asserting it and asking them to trust you. Demonstrated beats declared. Draw the mechanism from the true material; if you do not know why it works, flag it rather than inventing a reason.

Keep the tension. Slop is frictionless: everything is great, nothing is hard, no choice has a cost, which is why it is forgettable. Name the hard part, the limit, and who the product is not for.

Substance sharpens the user's point. It does not swap in yours. If making a line land would change what the user is actually claiming, flag it instead of rewriting the argument.

For the full set, the cliché-to-truth move, and worked examples, use `references/substance.md`.

## Do more good than harm

Everything above this line makes copy more persuasive. Persuasion lands a true claim and a false one equally well, so the better this skill works, the more it can hurt when the claims are not sound. A polished, human, mechanism-backed lie is trusted in a way slop never is. These rules are the counterweight, and they outrank the rest.

- Persuasion never outruns evidence. You may make a claim clearer. You may not make it more certain, proven, universal, or specific than the source supports. Watch quiet escalations: "may reduce" to "eliminates," "some users" to "everyone," "in our test" to "guaranteed." If a sentence got more convincing, name the evidence that earned it, or put it back.
- Load-bearing caveats survive every edit. Cut empty hedging, never a real qualification. Safety, legal, financial, and genuine-uncertainty caveats are facts, not filler. Removing one to add punch hides risk. Keep it.
- Never manufacture authenticity. Humanize the user's real copy. Do not invent the proof or the pressure: no fabricated reviews, testimonials, social proof, scarcity, or urgency, and no putting words in a real person's mouth. Treat each like an invented metric, a placeholder and never a fabrication.
- Humanizing is the wrong tool for disguising authorship where disclosure is expected, such as academic, regulated, or attested work. This is not an AI-detector bypass. Improve honest writing; do not help fake it.

The standard: a reader who trusts this copy because it is clear and human should be safe in trusting it. For the full treatment, use `references/integrity.md`.

## Human prose rule

Be specific, vary rhythm, prefer plain constructions, and never fabricate.

Specific beats generic. Use real names, numbers, mechanics, tradeoffs, and examples when the source provides them. If the source does not provide them, leave a visible placeholder.

Rhythm should vary. Mix short sentences with longer ones. Avoid a uniform mid-length cadence.

Plain beats inflated. Prefer is, has, does, gives, costs, saves, shows, and works over serves as, boasts, showcases, leverages, facilitates, underscores, or represents.

Point of view is allowed when the format supports it. Do not inject personality into legal, technical, compliance, or reference material.

## Dash default

Default to no em dashes or en dashes anywhere in final marketing copy: body, headings, subheads, bullets, CTAs, and captions alike. Replace each one with a period, comma, colon, parentheses, or a restructured sentence. This is an always-fix rule; a single dash gets fixed.

Keep a dash only when it is part of an exact quotation, an explicit user preference, or an established brand voice. Do not misquote a source to satisfy this rule.

## Fact safety

Never invent or strengthen specifics. This includes numbers, names, dates, quotes, testimonials, case-study results, awards, certifications, customer logos, integrations, pricing, guarantees, legal claims, compliance claims, and performance claims.

When a useful detail is missing, use a visible placeholder such as `[ADD VERIFIED METRIC]`, `[ADD REAL CUSTOMER EXAMPLE]`, `[ADD SOURCE]`, or `[VERIFY CLAIM]`.

If a claim is plausible but unsupported, weaken it, mark it for verification, or cut it. Do not make the copy sound more certain than the source allows.

## Voice safety

If the user provides a writing sample, brand voice, or style guide, follow that over this skill's default taste. Match sentence length, vocabulary, formality, directness, humor level, opening style, and closing style. Apply the matched voice to every section of the deliverable, including headlines, CTAs, and microcopy, not only the body.

With no sample, default to grounded, concrete, direct, and mildly opinionated only where the format allows. Do not fall back on one house style across projects; pick the register this format and this reader call for, and commit to it.

When the piece is voice-sensitive, no sample exists, and the user can answer, offer two or three one-line voice directions (each a posture plus one sample sentence rewritten in it) and write in the chosen one. When the user asked for immediate output, write in the grounded default and name the direction you took in the editorial note. The full move is in `references/voice-calibration.md`.

Do not over-edit good human writing. The edit bar defines the line: always-bar items get fixed even alone; a single cluster-bar tell in otherwise specific human prose stays.

## Reasoning depth

Substance and integrity work is multi-step reasoning. Before writing or rewriting, think the piece through: who the reader is, the real question under the stated one, the so-what ladder down to the consequence, and which claims the evidence can actually carry. Do that thinking before the first line of copy, not while drafting.

Mechanical cleanup of a short piece (a dash, a wrapper sentence, obvious bleed) needs no deep pass. Make the edits directly.

## When to load references and run the scanner

Load each file at the moment its trigger appears, not preemptively and not never:

- `references/ai-tells.md`: read it at the start of every cleanup pass on a draft you did not write. It is the full tell catalog, and every item carries its bar tag.
- `references/substance.md`: read it before rewriting any piece you have judged clean but empty, and before drafting from a thin brief.
- `references/integrity.md`: read it whenever an edit would make a claim more convincing, the copy touches health, money, safety, or legal territory, or scarcity, urgency, or social proof appears in the draft.
- `references/process-bleed.md`: read it when bleed survives a first pass or the piece heavily narrates itself.
- `references/voice-calibration.md`: read it when the user provides a sample or brand voice, and when the piece is voice-sensitive with no sample.
- `references/qa-scorecard.md`: read it when the user asks how ready the copy is, and before shipping long or high-stakes pieces.
- `references/translation-handoff.md`: read it when the output is headed to Hungarian.

Run `scripts/copy_scan.py` on any deliverable over roughly 600 words, and on any multi-section piece, before shipping:

```bash
python scripts/copy_scan.py draft.txt
```

Treat the script as a scanner, not a judge: its hits are candidates for the edit bar, and its silence proves nothing about substance.

## Pairing with translation

When the output needs to be Hungarian, this skill chains with `translating-english-to-hungarian`. Humanize in English first, then translate: sketch, to consumable English template (this skill), to native Hungarian (the translation skill), to final prose (a human).

Pass the register with the voice (`te` for casual or founder-led copy, `ön` for formal or institutional, and the translator defaults to `ön`). Placeholders pass through untranslated. Integrity travels with the meaning: the Hungarian must not read more certain than the English, must keep every caveat, and must add no proof, scarcity, or urgency the source lacked. Hungarian typography wins in the translated output. The full handoff is `references/translation-handoff.md`.

## Workflow

For drafting or finalization:
1. Identify the reader, product, offer, proof, main objection, and next step from the provided material.
2. Think before writing (see Reasoning depth): find the point worth making with the so-what ladder and the real-question test, so the copy leads with substance instead of backing into it.
3. Write the deliverable only, to the format's natural length. No planning notes, rationale, or assistant wrapper inside the copy.
4. Sweep the entire draft, first line to last: the sentence test on every sentence, the edit bar on every candidate, fact safety, voice safety, and the dash default.
5. Run the harm check: no claim more certain or proven than the source supports, every needed caveat kept, no manufactured proof or pressure.
6. Deliver per the output contract.

For cleanup:
1. Coverage pass: read the whole piece to the end and mark every candidate: process bleed, unsupported specifics, inflated certainty, AI tells, dashes, wrapper, and clean-nothing sections. Do not filter yet.
2. Bar pass: apply the edit bar to each candidate. Always-bar items get fixed. Cluster-bar items get fixed when clustered and left when alone.
3. Rewrite with those edits, never one that makes a claim more believable than it is true. Preserve meaning, claims, caveats, sections, and proportions.
4. Substance pass: sharpen surviving clean-nothing sections from the real material, or flag the gap with a placeholder.
5. Verification pass: re-read the full output against the checklist below. Fix any failure and re-check that item.
6. Deliver per the output contract. If you removed or restructured something for strategy reasons, say so in the editorial note.

The output of either path is a template for a human to finish, not publish-ready copy. If it needs to be Hungarian, translate last, after the harm check, and pass the register.

## Before shipping

Re-read the complete deliverable from the first line to the last and check every item below against every section, headings and CTAs included. If an item fails, fix it and check that item again:

- No sentence refers to the chat, request, prompt, project plan, outline, file system, internal decisions, or drafting process.
- Every paragraph serves the reader's situation, product behavior, offer, proof, objection, or next step.
- No section is clean nothing. The strongest lines pass the swap and negation tests: they say something only this writer could say, and a real competitor might refuse to claim.
- Every specific is supplied by the input or marked with a visible placeholder.
- No claim is more certain, proven, or universal than the source supports, and every safety, legal, or financial caveat is intact.
- No review, statistic, testimonial, scarcity, urgency, or named-person quote is invented; missing ones are visible placeholders.
- The voice matches the provided sample or the format, everywhere in the piece.
- Em and en dashes are gone from every element unless a stated exception applies.
- No assistant wrapper remains: no "here is the copy," "below is," "hope this helps," or "let me know."
- The reply follows the output contract: deliverable first, editorial note after it only if needed, nothing else.

## References

- `references/process-bleed.md`: expanded examples and fast scan phrases.
- `references/substance.md`: the intelligence layer. How to say something worth reading, with tests and worked examples.
- `references/integrity.md`: the do-more-good-than-harm layer. Persuasion within evidence, caveat preservation, no manufactured authenticity, and the boundary on disguising authorship.
- `references/ai-tells.md`: the tell catalog, every item tagged with its edit-bar level.
- `references/qa-scorecard.md`: score finished copy before shipping or when testing the skill.
- `references/voice-calibration.md`: voice matching, the grounded default, and the propose-directions move.
- `references/translation-handoff.md`: chaining with `translating-english-to-hungarian`, including register, placeholders, and integrity across languages.
- `scripts/copy_scan.py`: heuristic scanner for long drafts.
