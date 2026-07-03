# The Sonnopus Humanizer

A Claude Agent Skill for drafting, finalizing, and humanizing reader-facing marketing and long-form copy, and for making sure that copy actually says something worth reading. Its main job is to turn a quick sketch into a consumable template that a human finishes into final prose.

It stops two failures. The first: the finished deliverable starts narrating the hidden production process behind it, mentioning the chat, outline, roadmap, prior draft, internal decision, or scaffold instead of speaking to the reader about the product, offer, proof, objection, and next step. The second: the copy comes out clean but empty, grammatically perfect and saying nothing only this writer could say. Removing the first failure without fixing the second just produces tidy nothing.

And it does both behind a firewall, because a humanizer is a persuasion amplifier: every edit that makes copy clearer and more human also makes it more convincing, which is harm if the claims are not sound. So the skill never makes a claim more believable than it is true.

## What this version optimizes

Version 3 is calibrated for Claude Sonnet 5 and Claude Opus 4.8, which follow instructions literally, apply stated bars faithfully, and do not silently generalize a rule beyond its stated scope. The package is built around these choices:

- Short invocation metadata, so the model can trigger the skill reliably.
- Lean `SKILL.md`, so the active instruction layer is clear for both Sonnet and Opus.
- A concrete edit bar in place of qualitative taste. Every tell in the catalog is tagged always-fix, cluster-fix, or context, and a cluster is defined numerically. On models that respect a conservative instruction exactly, "don't over-edit" quietly becomes under-editing; an explicit bar keeps both failure modes out.
- Coverage before filtering. Cleanup sweeps the whole piece and marks every candidate first; the bar decides what changes second. The model never skips a finding because it guessed the finding was below the bar.
- Explicit scope on every rule: the whole deliverable, headings, CTAs, captions, and microcopy included, so no rule silently applies to body text only.
- An output contract, so the reply shape is fixed: deliverable first, a labeled editorial note after it only when needed, and length calibrated to the format rather than to effort.
- Explicit load triggers for every reference file and the scanner, so a model that favors reasoning over tool calls still reaches for the deeper catalogs at the right moments.
- Deeper references, so the model inspects examples and diagnostics only when useful.
- Strong fact safety, so the skill never invents metrics, testimonials, proof, awards, or claims.
- A substance layer, so de-slopping adds a specific, defensible point instead of leaving clean nothing, always drawn from the true material and never invented.
- An integrity layer, so the persuasion it adds never outruns the evidence, real caveats survive, and proof, scarcity, urgency, and a real person's words are never faked.
- Voice preservation with a propose-directions move, so it improves copy without flattening it into one house style, and never lets the model's own default voice become the brand's.
- Translation-ready, so the English template hands off cleanly to `translating-english-to-hungarian` for interpretive, native Hungarian instead of a literal calque.
- Optional scanner, so long deliverables can be checked for leftover process bleed, wrapper text, empty claims, high-liability claims, and manufactured pressure.

## Core principles

Every sentence should pass this test:

> Would this sentence make sense to a reader who never saw the project, chat, plan, outline, prompt, or drafting process?

If not, it is process bleed. Cut it or rewrite it around the reader, product, offer, proof, objection, or next step.

And every sentence that survives should pass a second test:

> Could this exact sentence appear on a competitor's page, or about a different product?

If yes, it is clean nothing. Replace it with the specific, true thing only this writer could say, taken from the real material. The skill removes what should not be there and supplies what should, without ever inventing a fact to do it.

Both tests sit under one standard:

> Would a reader who trusts this copy because it is clear and human be safe in trusting it?

If an edit made the copy more convincing without making it more true, the answer is no. Persuasion never outruns evidence, real caveats stay, and authenticity is never manufactured. See `references/integrity.md`.

## Installation

Upload the package where custom Claude skills are supported. The archive keeps the skill folder at the root.

## Testing

Use `tests/test-prompts.md`. The most important checks:

1. It triggers for landing pages, e-books, reports, product copy, and humanizing requests.
2. It does not trigger for code, raw data, legal terms, changelogs, or casual chat.
3. It replaces missing proof with visible placeholders instead of inventing facts.
4. It removes process bleed without deleting real meaning.
5. It preserves a provided voice sample rather than forcing a generic style.
6. It turns clean-but-empty copy into specific, defensible points instead of swapping hype words for plainer ones.
7. It never makes a claim more certain than the source, strips a needed caveat, or manufactures reviews, scarcity, or urgency.
8. It fixes an isolated always-bar item (one dash, one "as discussed," one unsupported figure) even in an otherwise excellent draft, and leaves a lone cluster-bar tell in human prose alone.
9. Its reply starts with the deliverable and ends with at most a six-line labeled editorial note. No preamble, no commentary around the copy.
10. With `translating-english-to-hungarian`, it humanizes in English first, passes the register, and leaves placeholders intact for native Hungarian.

## Optional scanner

Run:

```bash
python scripts/copy_scan.py draft.txt
```

The script flags likely process bleed, wrapper text, dash usage, vague authority, hype clusters, empty claims that fail the negation test, high-liability claims that need verification, and manufactured pressure such as fake scarcity or urgency. It is intentionally heuristic. Treat its output as warnings, not verdicts.
