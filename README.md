<div align="center">

# HumanCopywrite ✸☽

(agent built stuff)

**A human copywriter for Claude. It writes and de-slops marketing and website copy: no AI tells, no chat history leaking into the page, your facts kept and flagged, your voice preserved, and a real point worth reading.**

[![CI](https://github.com/forint573/human-copywrite/actions/workflows/ci.yml/badge.svg)](https://github.com/forint573/human-copywrite/actions/workflows/ci.yml)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Claude Skill](https://img.shields.io/badge/Claude-Skill-d97757.svg)](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
[![Tuned for Sonnet 5, Opus 4.8 & Fable 5](https://img.shields.io/badge/Tuned_for-Sonnet_5_·_Opus_4.8_·_Fable_5-8a63d2.svg)](#models)

</div>

## Install

```bash
git clone https://github.com/forint573/human-copywrite.git && \
  cp -r human-copywrite/human-copywrite ~/.claude/skills/
```

Or `curl -fsSL https://raw.githubusercontent.com/forint573/human-copywrite/main/install.sh | bash`, or grab the packaged `.skill` from [Releases](https://github.com/forint573/human-copywrite/releases) (`make build` builds it).

## Use

Claude reaches for the skill on its own when you say things like:

- "Humanize this landing page and make it sound less like AI."
- "Now write the homepage copy for what we built in this session."
- "Draft a sales page for this offer using only the proof in the brief."
- "This copy is clean but it says nothing. Make it specific without inventing anything."
- "Set up my voice for this project." (or `/human-copywrite setup`)

It stays out of the way for code, data, changelogs, legal terms, and casual chat.

## What it does

| Before | After |
| --- | --- |
| *"Based on our discussion, we built Relay to solve this. We started with delivery inspection, then added retry timelines, and finally wired up Slack alerts."* | *"Your webhook failed at 3 a.m. and the customer noticed first. Relay shows every delivery attempt, the exact payload, and why it failed, and pings your Slack the moment an endpoint starts erroring. `[ADD PRICING]`"* |
| *"We're committed to excellence and deliver world-class solutions that help businesses succeed."* | *"Your reps stop copying leads between four tabs. The CRM writes call notes back to the deal on its own, so follow-up happens the same day instead of next week."* |

The first row is the failure most humanizers miss: asked for site copy at the end of a working session, AI narrates the session. This skill treats the chat as source material, never as the manuscript, and writes from the product facts in the reader's order. The second row is the other half: clean-but-empty copy replaced with a claim only this product could make.

## What's specific about it

- **The transcript rule.** Chat history never ships as copy. Site prose is written from a source sheet (reader, problem, product, mechanism, proof, objection, next step) extracted from the session, ordered by the reader's questions, not the build timeline.
- **An edit bar, not a mood.** Every AI tell in a 30+ item catalog is tagged always-fix, cluster-fix (two tells in a paragraph, or three per 150 words), or context, so the same draft comes back the same way every time and good human writing is left alone.
- **A substance layer.** Copy that passes every style check but says nothing a competitor couldn't also say is treated as a failure. The swap test, the negation test, and the so-what ladder force a real point, drawn only from your material.
- **An integrity firewall.** Persuasion never outruns evidence: no invented proof, no stripped safety caveats, no manufactured scarcity or urgency, and it is not an AI-detector bypass.
- **Fact safety that respects your material.** Missing specifics become visible placeholders like `[ADD VERIFIED METRIC]`; specifics already in your draft stay and get flagged under `Verify` instead of deleted. Guarantees and countdowns get intervened on inline.
- **Per-project voice** via `MY_OWN_VOICE.md` (below).
- **A fixed reply shape.** Deliverable first, then at most a six-line labeled editorial note (Changed / Verify / Placeholders / Flagged / Register).
- **An optional heuristic scanner** (`scripts/copy_scan.py`) for long drafts, plus a handoff to [`translating-english-to-hungarian`](https://github.com/forint573/ENG-HUN-Translation-skill) for native Hungarian output.

## Make it write like you: MY_OWN_VOICE.md

Run `/human-copywrite setup` (or say "set up my voice for this project"). The skill asks six questions in one message: writing samples, who your reader is, the product in one sentence plus its mechanism, the proof you can actually claim, your posture and banned words, and practical details like spelling and required caveats. It writes the answers to `MY_OWN_VOICE.md` in your project root.

From then on, every copy task in that project loads the file automatically: your samples set the voice, your verified proof can be stated as fact without placeholders, your banned words become always-fix, and your legal caveats survive every edit. Edit the file by hand any time, or rerun setup. It can override the skill's taste, never its integrity rules.

## Models

Calibrated for Claude Sonnet 5, Opus 4.8, and Fable 5: hard bars and defined output shapes for literal instruction-followers, a light goal-stated layer for Fable 5 (which does worse under over-prescriptive skills, per Anthropic's own guidance). Run at effort `high` (`xhigh` for heavy rescue rewrites). Sonnet 5 thinks adaptively by default; on Opus 4.8 set `thinking: {type: "adaptive"}`; on Fable 5 omit the thinking parameter entirely. Earlier Claude models run it fine.

## What's inside

```text
human-copywrite/
├── SKILL.md                      # the active instruction layer
├── references/                   # loaded on named triggers
│   ├── process-bleed.md          #   the eight leaks, incl. the transcript transplant
│   ├── website-copy.md           #   source sheet, page patterns, hero/proof/FAQ craft
│   ├── substance.md              #   how to say something worth reading
│   ├── integrity.md              #   do more good than harm
│   ├── ai-tells.md               #   the tell catalog with edit-bar tags
│   ├── voice-setup.md            #   the MY_OWN_VOICE.md interview and template
│   ├── voice-calibration.md      #   matching a provided sample
│   ├── qa-scorecard.md           #   0 to 2 readiness score
│   └── translation-handoff.md    #   Hungarian chain
├── scripts/copy_scan.py          # optional heuristic scanner
└── tests/test-prompts.md         # trigger checks and evaluation samples
```

The output is a template a human finishes, not publish-without-review copy. This README follows the skill's own rules; the *Before* cells above break them on purpose.

## Contributing and license

PRs welcome: see [CONTRIBUTING.md](CONTRIBUTING.md); keep `make check` green. Apache 2.0, see [LICENSE](LICENSE) and [NOTICE](NOTICE). Full version history in [CHANGELOG.md](CHANGELOG.md).

> "Claude", "Sonnet", "Opus", and "Fable" are model names from Anthropic. This is an independent community skill, not affiliated with or endorsed by Anthropic.
