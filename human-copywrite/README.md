# HumanCopywrite

A Claude Agent Skill for drafting, finalizing, and humanizing reader-facing marketing and long-form copy, and for making sure that copy actually says something worth reading. Its main job is to turn a quick sketch into a consumable template that a human finishes into final prose.

It stops two failures. The first: the finished deliverable starts narrating the hidden production process behind it, mentioning the chat, outline, roadmap, prior draft, internal decision, or scaffold instead of speaking to the reader about the product, offer, proof, objection, and next step. The second: the copy comes out clean but empty, grammatically perfect and saying nothing only this writer could say. Removing the first failure without fixing the second just produces tidy nothing.

And it does both behind a firewall, because a humanizer is a persuasion amplifier: every edit that makes copy clearer and more human also makes it more convincing, which is harm if the claims are not sound. So the skill never makes a claim more believable than it is true.

## What this version optimizes

Version 4 runs on Claude Sonnet 5, Claude Opus 4.8, and Claude Fable 5. The package is built around these choices:

- A lean `SKILL.md`, so the active instruction layer stays light in context. Anthropic's own guidance for its strongest current models is that over-prescriptive prompts and skills reduce output quality, so the instruction layer states goals and hard bars instead of enumerating micro-steps. The deep catalogs live in `references/` and load on named triggers.
- A concrete edit bar in place of qualitative taste. Every tell is tagged always-fix, cluster-fix (two tells in a paragraph, or three per 150 words), or context. On models that follow a conservative instruction exactly, "don't over-edit" quietly becomes under-editing; a bar keeps both failure modes out.
- Coverage before filtering. Cleanup sweeps the whole piece and marks every candidate first; the bar decides what changes second.
- Fact safety that respects the user's material. Specifics the model would have to invent become visible placeholders. Specifics already in the user's draft are kept and flagged under `Verify` in the editorial note, never silently deleted. High-liability claims and pressure tactics (guarantees, income results, scarcity, deadlines) are weakened or marked inline regardless of origin.
- An output contract: deliverable first, at most a six-line labeled editorial note after, with named exceptions for proposing voice directions and for file-based agent workflows.
- An integrity layer, so persuasion never outruns evidence, real caveats survive, and proof, scarcity, urgency, and a real person's words are never faked.
- Voice preservation with a propose-directions move, so the model's own default voice never becomes the brand's.
- Translation-ready: the English template hands off cleanly to `translating-english-to-hungarian`.
- An optional heuristic scanner for long deliverables, gated on script-execution availability.

## Core principles

Every sentence should pass this test:

> Would this sentence make sense to a reader who never saw the project, chat, plan, outline, prompt, or drafting process?

If not, it is process bleed. Cut it or rewrite it around the reader, product, offer, proof, objection, or next step.

And every sentence that survives should pass a second test:

> Could this exact sentence appear on a competitor's page, or about a different product?

If yes, it is clean nothing. Replace it with the specific, true thing only this writer could say, taken from the real material.

Both tests sit under one standard:

> Would a reader who trusts this copy because it is clear and human be safe in trusting it?

If an edit made the copy more convincing without making it more true, the answer is no. See `references/integrity.md`.

## Installation

Upload the package where custom Claude skills are supported. The archive keeps the skill folder at the root.

## Testing

Use `tests/test-prompts.md`. The most important checks:

1. It triggers for landing pages, e-books, reports, product copy, and humanizing requests.
2. It does not trigger for code, raw data, legal terms, changelogs, or casual chat.
3. It never invents facts; missing proof becomes a visible placeholder.
4. It keeps specifics from the user's own draft and flags load-bearing ones under `Verify`, instead of deleting them into placeholders.
5. It removes process bleed without deleting real meaning.
6. It preserves a provided voice sample rather than forcing a generic style.
7. It turns clean-but-empty copy into specific, defensible points instead of swapping hype words for plainer ones.
8. It never makes a claim more certain than the source, strips a needed caveat, or manufactures reviews, scarcity, or urgency, and it weakens or marks guarantees and pressure tactics inline.
9. It fixes an isolated always-bar item (one dash, one "as discussed") even in an otherwise excellent draft, and leaves a lone cluster-bar tell in human prose alone.
10. Its reply starts with the deliverable and ends with at most a six-line labeled editorial note.
11. With `translating-english-to-hungarian`, it humanizes in English first, passes the register, and leaves placeholders intact.

## Optional scanner

When script execution is available:

```bash
python scripts/copy_scan.py draft.txt
```

The script flags likely process bleed, wrapper text, dash usage, vague authority, hype clusters, empty claims that fail the negation test, high-liability claims, and manufactured pressure. It is intentionally heuristic: treat its output as warnings, not verdicts.
