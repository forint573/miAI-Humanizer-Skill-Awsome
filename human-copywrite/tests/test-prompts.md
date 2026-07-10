# Test prompts for HumanCopywrite

Use these after installation to check trigger behavior and output quality.

## Should trigger

1. Humanize this landing page copy and make it sound less like AI.

2. Finalize the homepage copy from the outline we built earlier. Remove planning notes and make it paste-ready.

3. Draft a sales page for this offer using only the proof in the brief.

4. Clean up this e-book chapter. Keep the same arguments, but remove the "in this chapter" style and make it read naturally.

5. Rewrite this email sequence in our founder voice. Do not invent metrics or testimonials.

6. This homepage copy is clean but it doesn't say anything. Make it sharper and more specific.

7. Tighten this health product copy, but do not overstate the claims or drop the safety caveats.

8. Turn this rough sketch into a clean, consumable template I can finish, and mark any placeholders.

9. Humanize this landing page in English first, then we will translate it to Hungarian.

10. Draft the about page. We have no brand voice yet, so give me a couple of voice options first.

## Should not trigger

1. Refactor this Python function.

2. Convert this CSV into a table.

3. Write release notes for version 2.1 from this changelog.

4. Summarize these legal terms plainly without changing the meaning.

5. Chat with me about whether this idea is good.

## Evaluation samples

### Process bleed sample

Input:

Based on our discussion, this guide starts by explaining the problem, then moves into the framework we decided on. After careful consideration, we landed on three pillars. In this section, we will explore the first pillar.

Expected behavior:

Remove the chat, plan, decision path, and section meta. Rewrite around the reader's problem and the framework's actual value.

### Proof-in-the-draft sample

Input (a cleanup request on the user's existing copy):

Our platform cuts onboarding time by 73% and is trusted by leading enterprises.

No source is provided beyond the draft itself.

Expected behavior:

The 73% is the user's own material: keep it as written and list it under `Verify` in the editorial note; do not delete it or swap it for a placeholder. "Leading enterprises" is an unnamed-authority claim: name the customers, weaken it, use a placeholder like `[ADD NAMED CUSTOMER]`, or cut it. If the user says the draft was AI-generated or its numbers are unverified, or asks for verified-only copy, the 73% becomes `[ADD VERIFIED METRIC]` instead. In no case does the number get stronger or more certain.

### Clean-nothing sample

Input:

We are committed to excellence and passionate about delivering value. Our innovative solutions help businesses succeed and exceed expectations every day.

Expected behavior:

Recognize clean nothing. Every line fails the negation test: no one advertises the opposite, so the lines carry no information. Do not just swap the hype words for plainer ones, since that produces a cleaner version of nothing. Ask for the real mechanism, number, tradeoff, or named user, and replace each empty claim with a specific, defensible point or a visible placeholder such as `[ADD THE REAL MECHANISM]`. Never invent the specifics to fill the gap.

### Overclaim and manufactured-pressure sample

Input:

Our course guarantees you will double your income in 30 days. Join 50,000 students who transformed their lives. Only 2 spots left, enroll before midnight.

No source backs the numbers, the guarantee, or the scarcity.

Expected behavior:

These are high-liability claims and pressure tactics, so keep-and-flag is not enough. Persuasion must not outrun evidence: weaken or mark the income guarantee inline (`[VERIFY CLAIM]` or a qualified rewrite), and mark the scarcity and deadline inline (`[CONFIRM ACTUAL SPOTS]`, `[CONFIRM REAL DEADLINE]`) or cut them. The "50,000 students" figure is proof: keep it under `Verify` or use `[ADD REAL ENROLLMENT COUNT]` if the user says it is unverified. Never fabricate the proof, the result, or the urgency, and never ship a guarantee or countdown as-is without verification.

### Voice preservation sample

Input includes a casual founder paragraph with short sentences, plain words, and a little skepticism.

Expected behavior:

Preserve that rhythm. Do not turn it into corporate brochure copy.

### Over-editing trap

Input contains one em dash, one formal transition, and otherwise specific human writing.

Expected behavior:

The edit bar makes this predictable. The dash is an always-fix item, so it goes (unless an exact quote, stated user preference, or brand voice protects it). The lone formal transition is a cluster-bar item standing alone in specific human prose, so it stays. Everything else is untouched. The output is not a rewrite; it is the same piece with one repair.

### Under-editing trap (isolated items far apart)

Input is a strong, specific, human-sounding draft that contains exactly one "as we discussed" clause, one em dash, and one unsourced "97% satisfaction" figure, each in a different paragraph, with no other tells anywhere.

Expected behavior:

Do not wave these through because they are isolated or the draft is otherwise good. The conversation residue is removed and the dash is replaced (both always-bar). The 97% is the user's own draft material: it stays in the copy and appears under `Verify` in the editorial note (placeholder only if the user flagged the draft as unverified). The rest of the draft stays as written. The coverage pass finds all three even though they sit far apart; none is skipped because the sweep stopped early.

### Output contract check

Any cleanup request.

Expected behavior:

The reply opens with the first line of the cleaned copy. No "Here is the revised version," no summary of the approach before the deliverable. If anything needs the user's attention, it appears after the copy as a labeled editorial note of at most six lines (Changed / Verify / Placeholders / Flagged / Register). A cleanup that needed no flags ends with the copy and nothing else.

### Voice directions sample

Input: "Draft our homepage hero. We don't have a voice guide yet." The user is present and asking interactively.

Expected behavior:

Offer two or three one-line voice directions, each a posture plus the opening line rewritten in that posture, and build only the chosen one. If the user instead asked for immediate output, write in the grounded default and name the direction taken in the editorial note.
