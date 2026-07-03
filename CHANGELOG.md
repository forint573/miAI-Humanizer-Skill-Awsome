# Changelog

All notable changes to The Sonnopus Humanizer are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.0.1] - 2026-07-03

The Sonnet 5 and Opus 4.8 calibration release. These models follow
instructions literally, do not generalize a rule beyond its stated scope, and
apply a conservative instruction exactly as conservatively as written, which
turns vague taste ("don't over-edit," "act on clusters") into silent
under-editing. This release converts every judgment call the skill used to
imply into a definition it states, following Anthropic's published prompting
guidance for both models: concrete bars over qualitative terms, coverage
before filtering, explicit scope on every instruction, positive examples,
defined output shape, and named triggers for loading references and tools.

### Added
- `SKILL.md`: an edit bar with three levels. Always-fix items (process bleed,
  wrapper, unsupported specifics, certainty inflation, dashes, scaffold,
  buzzword blocklist) get fixed on a single instance anywhere in the piece.
  Cluster-fix items (AI vocabulary, -ing tails, rule of three, and the other
  style tells) change only at a numeric threshold: two catalog tells in one
  paragraph, or three within any 150-word span. Leave-alone items are named
  too, so the over-editing guard is now as concrete as the under-editing one.
- `SKILL.md`: a two-pass cleanup workflow. Coverage pass first (sweep the
  entire piece, mark every candidate, no filtering, no stopping early), bar
  pass second (the bar decides what changes, not first impressions).
- `SKILL.md`: an output contract. The reply is the deliverable starting at
  line one, then at most a six-line labeled editorial note (Changed / Verify /
  Placeholders / Flagged / Register), with a worked example, plus length
  rules that calibrate output to the format instead of to effort.
- `SKILL.md`: explicit whole-deliverable scope on every rule: headlines,
  subheads, bullets, CTAs, button and link microcopy, captions, alt text, and
  footers, stated once globally and repeated on the rules that need it most
  (sentence test, dash default, voice matching, harm check).
- `SKILL.md`: a reasoning-depth section. Substance and integrity work is
  named as multi-step reasoning to do before writing; mechanical cleanup is
  named as direct work that needs no deep pass. Matches adaptive-thinking
  steering guidance for both models.
- `SKILL.md`: named load triggers for every reference file and a word-count
  threshold for the scanner, because Opus 4.8 favors reasoning over tool
  calls unless told when and why to reach for them.
- `references/ai-tells.md`: every one of the 33 catalog items now carries a
  bar tag (always / cluster / context) with the tag's rationale where it is
  not obvious, plus the two overrides: a voice sample can protect style items
  but never process, fact, or integrity items, and fact safety outranks every
  tag.
- `references/voice-calibration.md`: a propose-voice-directions move. For
  voice-sensitive work with no sample, offer two or three directions as
  rewritten opening lines and build only the chosen one; when immediate
  output was requested, use the grounded default and name it in the editorial
  note. Plus an explicit warning that the model's own default voice must not
  become the brand's, and whole-deliverable scope for voice matching.
- `tests/test-prompts.md`: an under-editing trap (isolated always-bar items
  must be fixed even in an excellent draft), an output-contract check, a
  voice-directions sample, and a rewritten over-editing trap that resolves
  by the bar instead of by feel.
- `tests/run_checks.py`: structural checks for the v3 calibration (output
  contract, edit bar, cluster threshold, reference triggers, whole-deliverable
  scope, bar tags on all catalog items, propose-directions move).
- Root README: a "Tuned for Claude Sonnet 5 and Opus 4.8" section explaining
  the calibration and the operator settings that matter (effort levels,
  adaptive thinking on Opus 4.8, Sonnet 5 tokenizer headroom for long
  outputs, one well-specified turn).

### Changed
- `references/substance.md`: drafting now names its think-before-writing
  step; cleanup now judges every section, not only the visibly weak ones.
- `references/integrity.md`: the harm check states its scope: every claim in
  every section, headlines and CTAs included.
- `references/process-bleed.md`: the sentence test states its scope and
  sweep-to-the-end requirement.
- `references/qa-scorecard.md`: category 9 became "Output hygiene and
  contract" and scores the reply shape; category 2 checks cleanliness across
  every element.
- Both READMEs reframed around the calibration; the badge now says which
  models the skill is tuned for.

### Kept
- Every 2.0 layer as the foundation: the substance tests, the integrity
  rules, fact safety, voice preservation, the dash default, the seven leaks,
  and the template-not-final-copy positioning. The calibration changes how
  reliably those rules fire on the current models, not what they say.

## [2.0.0] - 2026-06-13

The intelligence and integrity release. Version 1.0 made copy clean: no AI
tells, no process bleed, no invented facts, no flattened voice. This release
adds two things the first half made necessary. First, the substance to make
copy worth reading, not just clean. Second, the safety layer the substance
demands: a humanizer is a persuasion amplifier, and the better it works, the
more it can harm when the claims are not sound. So the same release that adds
persuasive force adds the firewall. Persuasion never outruns evidence,
load-bearing caveats survive every edit, and the skill humanizes honest copy
but refuses to manufacture proof, scarcity, urgency, or a real person's words.
The value always comes from the true material. Nothing is invented to add it.

This release also states the skill's honest scope plainly across the files: it
turns a quick sketch into a consumable template that a human finishes into final
prose, not publish-ready copy, and it chains with the Hungarian translation
skill for interpretive, native Hungarian rather than a literal calque.

### Added
- `references/substance.md`: the intelligence layer. Defines the "clean nothing"
  failure and the moves that catch it (the swap test, the negation test, earning
  a claim by showing the mechanism, the so-what ladder, the real question), the
  keep-the-tension rule, the cliché-to-truth move, mode-specific guidance, a
  voice guard, and worked examples, all under one hard boundary: insight is
  compression of true material, never invention. Earning a claim by showing why
  it is true, rather than asserting it, is the move that turns persuasion into
  something the reader actually learns.
- `references/integrity.md`: the do-more-good-than-harm layer the scanner
  always referenced but the skill never spelled out. Persuasion never outruns
  evidence, load-bearing caveats (safety, legal, financial, uncertainty)
  survive every edit, authenticity is never manufactured (no fabricated
  reviews, social proof, scarcity, urgency, or putting words in a real person's
  mouth), the substance moves are bounded by all of it, and humanizing is named
  as the wrong tool for disguising authorship where disclosure is expected.
- `SKILL.md`: a "Make it worth reading" section carrying the four core substance
  tests and the insight-not-invention rule, a "Do more good than harm" section
  carrying the integrity rules, a reframed mission that names the subtractive
  and additive jobs as co-equal and binds both to the harm rule, a substance
  pass and a harm check in the workflows, and clean-nothing plus harm lines in
  the pre-ship checklist.
- `references/qa-scorecard.md`: new "Substance (worth reading)" and "Integrity
  (do more good than harm)" categories, so the new dimensions are scored, not
  just described. A 0 in Truthfulness, Substance, or Integrity caps the result
  whatever the total.
- `references/ai-tells.md`: a capstone entry, "Clean nothing (the de-slop
  trap)," and a framing note that cutting a tell is only half the job.
- `scripts/copy_scan.py`: an `empty_claim` detector for phrases that fail the
  negation test, a `risky_claim` detector for high-liability claims (guarantees,
  absolutes, medical, financial, or regulated, #1 or world's-best), and a
  `manufactured_pressure` detector for fabricated scarcity, urgency, and social
  proof. Heuristic, like the rest of the scanner.
- `references/translation-handoff.md`: how to chain with
  `translating-english-to-hungarian`. Humanize in English first, translate last
  and interpretively, pass the formal or informal register (`ön` or `te`) with
  the voice, keep placeholders untranslated, carry the integrity rules across
  the language line, and let Hungarian typography win in the Hungarian output.
- `tests/`: a clean-nothing sample, an overclaim and manufactured-pressure
  sample, trigger prompts for substance and integrity work, plus automated
  checks for the new reference files and the empty-claim, risky-claim, and
  manufactured-pressure detectors.

### Changed
- The skill description now names the additive job (says something worth
  reading: specific, defensible, non-obvious, not clean but empty) alongside the
  humanizing job, without weakening the existing triggers.
- The scorecard is now ten categories out of twenty, with rescaled thresholds
  and Integrity as a gating category. "Substance preservation" was renamed
  "Meaning preservation" to free the word "substance" for the new value category.
- Root and skill READMEs reframed around two failures, two tests, and the
  do-more-good-than-harm standard.
- Positioning made explicit across the files: the skill turns quick sketches
  into consumable templates that humans finish into final prose, not
  publish-ready copy. Finalization mode, the workflows, and both READMEs now
  say so.

### Kept
- Every 1.0 guardrail: fact safety, voice preservation, the lightest effective
  edit, the dash default, and the process-bleed test. The new layer never
  overrides them. When substance is missing, the skill flags a placeholder
  instead of inventing it.

## [1.0.0] - 2026-06-05

First public release.

### Added
- `SKILL.md` — the active instruction layer: scope, modes, the one sentence
  test, the seven process-bleed leaks, human-prose rules, dash default, fact
  safety, voice safety, the workflow, and the pre-ship checklist.
- `references/process-bleed.md` — expanded leak examples and fast-scan phrases.
- `references/ai-tells.md` — diagnostic catalog of generic AI prose patterns,
  meant to be applied to clusters rather than isolated words.
- `references/qa-scorecard.md` — an 8-category, 0–2 scorecard for judging
  whether finished copy is production-ready.
- `references/voice-calibration.md` — quick guide for matching a provided
  writing sample or brand voice.
- `scripts/copy_scan.py` — optional heuristic scanner that flags process
  bleed, assistant wrapper text, hype clusters, vague authority, and dashes.
- `tests/test-prompts.md` — trigger / no-trigger prompts and evaluation
  samples for checking behavior after install.
- `install.sh` — one-command installer (user or project scope, curl-pipeable)
  so the skill drops into a Claude skills folder in a single step.
- README with a `TL;DR`, one-line install, a before/after example, an FAQ, and
  the skill's own rules applied to its copy (no em or en dashes, no hype
  clusters, no process bleed, no invented facts).
- Repository scaffolding: Apache-2.0 LICENSE, NOTICE, CONTRIBUTING,
  CODE_OF_CONDUCT, build script, automated checks, and CI.

[3.0.1]: https://github.com/forint573/miAI-Humanizer-Skill-Awesome/releases/tag/v3.0.1
[2.0.0]: https://github.com/forint573/miAI-Humanizer-Skill-Awesome/releases/tag/v2.0.0
[1.0.0]: https://github.com/forint573/miAI-Humanizer-Skill-Awesome/releases/tag/v1.0.0
