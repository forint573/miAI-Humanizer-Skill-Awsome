# Website prose: write from the source, not the transcript

Use this when the task is website or page copy: homepage, landing page, product page, pricing, About, or any page written at the end of a working session ("now write the site copy for this").

## The failure this prevents: the transcript transplant

The most common way AI botches website copy is not bad style. It is wrong source material. Asked for a homepage at the end of a long build or planning session, the model narrates the session: what "we" built, in the order it was built, with the decisions and iterations still visible. The result is a diary wearing a homepage's clothes.

The tell is chronology. If the page's sections mirror the order things were built or discussed, rather than the order of the reader's questions, it is a transplant. Other symptoms: "we" meaning the chat participants instead of the company, feature names only the session used, and paragraphs that explain why a decision was made instead of what the product does for the reader.

Worked example. A session built "Relay," a webhook debugging tool: first delivery inspection, then retry timelines, then Slack alerts.

- Transplant (wrong): "Relay is a webhook debugging tool we built to solve this exact problem. We started with delivery inspection so you can see every payload, then added retry timelines, and finally wired up Slack alerts so the team gets notified."
- Written from the source (right): "Your webhook failed at 3 a.m. and the customer noticed first. Relay shows every delivery attempt, the exact payload, and why it failed, and pings your Slack the moment an endpoint starts erroring. `[ADD PRICING]`"

Same facts. The first is the session's story; the second is the reader's.

## The source sheet

The chat, the brief, the codebase, and the README are material to mine, never a manuscript to lightly edit. Before writing any page, fill this sheet from whatever context exists:

1. Reader: who arrives, and what they want or fear.
2. Problem: the moment that sends them looking.
3. Product: one plain sentence.
4. Mechanism: the how that makes the promise believable.
5. Proof: only what is verified or supplied; otherwise a placeholder.
6. Objection: the main reason they would not buy or sign up.
7. Next step: the one action the page asks for.

Write from the sheet. An empty slot becomes a visible placeholder, never a guess. Section order comes from the reader's questions (What is this? Will it work for me? Can I trust it? What now?), never from the session's timeline. If MY_OWN_VOICE.md exists in the project, its Reader, Product truth, and Verified proof sections pre-fill the sheet.

## Match the structure to reader awareness

Not every page starts from the same place. A reader who has never considered the problem needs a different shape than one comparing named competitors. Pick the frame from where the reader already stands, then fill it from the source sheet above; this changes pacing and order, never the truthfulness rules.

- Unaware (doesn't yet know they have the problem): Picture the situation, Promise the outcome, Proof it's real, Push toward the next step.
- Problem aware (feels the pain, has no solution in mind): Problem, Agitate the cost of leaving it unsolved, Solution.
- Solution aware (knows solutions exist, not this product): Before, After, Bridge, the mechanism that closes the gap.
- Product aware (knows this product, deciding whether to act): Attention, Interest, Desire, Action, compressed, since the case is mostly already made.

A PPPP page for an unaware reader still cannot invent a proof point it lacks; it just spends more of the page building the picture before it earns the right to ask for proof. When the brief does not say which stage the reader is at, default to the reader-questions order above (What is this? Will it work for me? Can I trust it? What now?), which reads correctly for the problem-aware or solution-aware reader, the most common case for a homepage.

## Page patterns

Hero: the headline carries the reader's value, not the product's category. The subhead names the mechanism. One CTA, one action.

- Category headline (weak): "The modern platform for webhook management."
- Value headline (strong): "Know why the webhook failed before the customer emails you."

Features: every feature ends in the reader's outcome. The test is the "so that" chain: feature, so that consequence.

- Feature only: "Automatic retry timelines."
- With the chain: "Automatic retry timelines, so you can see whether the fix worked without triggering the payment twice."

Proof: real numbers, named customers, or a placeholder. A proof section with vague authority ("trusted by leading teams") is worse than a placeholder, because it reads as filler.

FAQ: answer the real objection under each question, usually about risk, effort, or lock-in. "Is it secure?" is answered with the mechanism and the audit trail, not with "we take security seriously."

About: still for the reader. It answers "can I trust these people with this problem?" with the founders' actual stake in the problem, not a company diary.

Pricing: name who each tier is for, and say who it is not for. That one honest line does more for trust than any adjective.

## Skimmability

Readers scan. Front-load every section: the point in the first sentence, support after. One idea per section. Vary paragraph length like sentence length; three identical-weight paragraphs in a row read as generated. Headings must carry meaning on their own, because a scanning reader reads only them.
