# Pairing with the Hungarian translation skill

This skill produces English copy. When the output needs to be Hungarian, it pairs with `translating-english-to-hungarian`, which turns English into idiomatic, native Hungarian rather than a word-for-word calque. The two are meant to chain, with a human finishing the result.

## What this skill is, in the chain

This skill is a template maker, not a final-copy machine. It turns a quick sketch or half-built draft into a consumable template: clean, specific, honestly sourced, voiced, with visible placeholders where proof is missing. A human finishes that template into final prose. When the target is Hungarian, the translation skill sits between the template and the human.

The chain: sketch (English) to consumable template (this skill, English) to native Hungarian (the translation skill) to final prose (a human).

## Order of operations

Do the humanizing in English, then translate. Run this skill first: strip process bleed, add substance, apply the integrity rules, leave visible placeholders. Hand the finished English template to the translation skill last. Substance and integrity decisions are easier to get right in the source language, and the translator's job is then narrow: render settled meaning as native Hungarian.

## Interpret, do not transliterate

The translated copy must carry the meaning, tone, and intent, not the English word order or idioms. The translation skill already works this way: it corrects topic and focus order, definite and indefinite conjugation, dropped pronouns, case suffixes in place of prepositions, and false cognates. Keep it that way. The goal is what a Hungarian writer would have written, not English wearing Hungarian words.

To make copy that translates well interpretively:

- Avoid English-only wordplay, puns, and rhyme in load-bearing lines. If a line depends on a pun, flag it so a person can find a Hungarian equivalent instead of a literal rendering that loses the point.
- Prefer plain, concrete constructions over idioms with no Hungarian counterpart.
- Keep close to one idea per sentence. Interpretive translation is cleaner when the source is not overloaded.

## Carry the voice across, including register

This skill preserves the user's voice. Hungarian forces a choice English did not: formal `ön` or informal `te`. The translation skill defaults to `ön`, so pass the register with the template, because register is part of the voice.

- Casual, founder-led, or peer-to-peer English: note that the Hungarian should use `te`.
- Formal, institutional, or enterprise English: `ön`, the default.

State the intended register in an editorial note outside the copy, so the interpretive translation matches the tone instead of flattening it to the default.

## Placeholders survive translation

The template's placeholders (`[ADD VERIFIED METRIC]`, `[CONFIRM THIS DEADLINE]`) are instructions to the human, not copy. They pass through translation untouched, exactly like code, URLs, and brand names. Do not translate the bracketed token. The human fills them in during finishing, in the target language. A placeholder that survives into the Hungarian template is working as intended.

## Integrity travels with the meaning

The integrity rules do not stop at the language boundary. In the Hungarian output:

- No claim is more certain or proven than the English template supported. Interpretive does not mean stronger.
- Every safety, legal, or financial caveat in the English survives in the Hungarian. Translation never drops a qualification for flow.
- No proof, scarcity, or urgency appears that was not in the source.

If the Hungarian reads more convincing than the English it came from, that is the same inflation the integrity layer forbids, now in a second language.

## Who owns which conventions

- This skill's typographic defaults (no em dashes, English-style quotation marks) apply to English output.
- In the Hungarian output, the translation skill's localization wins: Hungarian quotation marks („…"), decimal comma, dates like `2026. június 13.`. Do not impose English punctuation on Hungarian copy.

## On the other skill

`translating-english-to-hungarian` already returns Hungarian only, with no commentary, and leaves code, URLs, and brand names untouched. This skill does not require any change to it; the template translates cleanly as is. For full symmetry, that skill could add one line to its pass-through list (placeholder tokens in square brackets stay untranslated) and accept the register note above. Those are optional refinements on its side, not prerequisites.
