# Contributing to HumanCopywrite

Thanks for your interest in improving this skill. It is a small,
documentation-heavy project, so contributing is mostly about clear writing
and good judgment rather than large code changes.

## Ways to help

- **Sharpen the guidance.** Better examples, clearer rules, or a sharper
  before/after pair in `references/`.
- **Catch new AI tells.** If you spot a recurring machine-written pattern that
  isn't covered, propose an entry for `references/ai-tells.md`. Include a
  before/after and explain *why* it reads as machine-written.
- **Improve the scanner.** Reduce false positives or add a high-signal pattern
  to `scripts/copy_scan.py`. Keep it heuristic and dependency-free.
- **Add test prompts.** New trigger / no-trigger cases or evaluation samples in
  `tests/test-prompts.md`.

## Principles to preserve

These are the reasons the skill exists. Please don't regress them:

1. **Never fabricate.** No invented numbers, names, testimonials, results, or
   claims. Missing proof becomes a visible placeholder, and the user's own
   specifics are kept and flagged for verification, not deleted.
2. **Don't flatten voice.** A provided sample or brand voice always wins over
   the skill's default taste.
3. **Keep `SKILL.md` lean.** It is the active instruction layer. Deep material
   belongs in `references/`, consulted on demand.
4. **Diagnose on clusters, not isolated words.** One formal word or dash is not
   proof of AI writing.
5. **Stay in scope.** This is for reader-facing marketing and long-form copy,
   not code, data, changelogs, legal terms, or casual chat.

## Development

The scanner targets Python 3.8+ and uses only the standard library.

```bash
make check     # run all automated checks (skill structure + scanner)
make build     # package dist/human-copywrite.skill
make clean     # remove build artifacts
```

You can also run the checks directly:

```bash
python tests/run_checks.py
```

## Pull requests

1. Keep changes focused; one concern per PR.
2. If you change skill behavior, update `tests/test-prompts.md` and the
   `CHANGELOG.md` under `[Unreleased]`.
3. Make sure `make check` passes.
4. Describe the *reader-facing* effect of your change, not just the diff.

By contributing, you agree that your contributions are licensed under the
project's [Apache License 2.0](LICENSE).
