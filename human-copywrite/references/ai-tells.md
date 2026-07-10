# AI Tells: Diagnostic Catalog

A lookup for cleanup mode, and for naming *why* something reads as machine-written. This is a diagnostic reference; the edit bar in SKILL.md decides what actually changes.

Every item below carries a bar tag, so the decision is mechanical, not a mood:

- **Bar: always.** Fix every instance, even a single one anywhere in the piece, subject only to the exceptions stated in the item or in SKILL.md.
- **Bar: cluster.** Fix when part of a cluster; leave a lone instance in otherwise specific human prose. A cluster is two or more catalog tells inside one paragraph, or three or more within any 150-word span.
- **Bar: context.** Not a tell on its own. Act only on the condition named in the item.

Two overrides sit above the tags. A provided voice sample or brand style can override cluster-bar and context-bar items it demonstrably uses; it never overrides an always-bar item that exists for process, fact, or integrity reasons. And fact safety outranks everything: a specific inside any pattern is never invented or strengthened, whatever the tag says — a missing specific becomes a placeholder, and a kept one is flagged per SKILL.md's fact-safety rule.

Every fix here removes something, and removing is only half the job. A cut tell leaves a gap. A gap filled with a cleaner version of nothing is still nothing. When you cut, replace with the specific true thing, not sanitized emptiness. The diagnosis lives here; what to put in the gap lives in `references/substance.md`. Item 33 is the trap to watch for.

Patterns marked **(see SKILL.md)** are covered in the main body because they overlap with process bleed or the hard rule; they are listed here only for completeness.

## Contents
1. Significance, legacy, and "broader trends" inflation
2. Notability and media-coverage puffery
3. Present-participle ("-ing") analysis tails
4. Promotional / brochure language
5. Vague attributions and weasel words
6. "Challenges and Future Prospects" formula
7. Overused AI vocabulary
8. Copula avoidance (dodging is/are)
9. Negative parallelism and tailing negations
10. Rule of three
11. Elegant variation (synonym cycling)
12. False ranges ("from X to Y")
13. Passive voice and subjectless fragments
14. Em and en dashes (strong default, see SKILL.md)
15. Boldface overuse
16. Inline-header vertical lists
17. Title Case in headings
18. Decorative emoji
19. Curly quotation marks
20. Chat / correspondence artifacts (see SKILL.md)
21. Knowledge-cutoff disclaimers and speculative gap-filling
22. Sycophantic / servile tone
23. Filler phrases
24. Excessive hedging
25. Generic positive conclusions
26. Hyphenated word-pair overuse
27. Persuasive-authority tropes
28. Signposting and announcements
29. Fragmented headers
30. Diff-anchored writing (see SKILL.md)
31. Marketing buzzwords and clichés (quick blocklist)
32. Structural tells from social/marketing copy
33. Clean nothing (the de-slop trap)

---

### 1. Significance, legacy, and "broader trends" inflation
**Bar: cluster.** If the inflated significance is also an unsupported claim, fact safety makes it always.
LLMs puff up importance by claiming arbitrary things "represent" or "contribute to" a broader topic.
Watch: *stands/serves as, is a testament/reminder, plays a vital/pivotal/key role, underscores its significance, reflects broader, marks a turning point, evolving landscape, indelible mark, deeply rooted, setting the stage for.*
- Before: "Founded in 1989, it marked a pivotal moment in the evolution of regional statistics and reflected a broader movement toward decentralization."
- After: "Founded in 1989 to collect and publish regional statistics independently of the national office."

### 2. Notability and media-coverage puffery
**Bar: cluster.** An unsupported outlet list or follower count is always fixed via placeholder, per fact safety.
Listing outlets or follower counts to assert importance, usually without context.
- Before: "Her views have been cited in the Times, the BBC, and the FT. She maintains an active social media presence with over 500,000 followers."
- After: "In a 2024 Times interview, she argued AI rules should target outcomes, not methods."

### 3. Present-participle ("-ing") analysis tails
**Bar: cluster.**
Tacking an "-ing" clause onto a sentence to fake depth.
Watch: *highlighting…, ensuring…, reflecting…, symbolizing…, contributing to…, fostering…, showcasing….*
- Before: "The palette uses blue and gold, resonating with the region's beauty, symbolizing the coast, reflecting the community's deep connection to the land."
- After: "The palette uses blue and gold. The architect chose them to reference the local coast."

### 4. Promotional / brochure language
**Bar: cluster.**
Travel-brochure tone, common on "heritage" and "about us" copy.
Watch: *boasts, vibrant, rich (figurative), nestled, in the heart of, breathtaking, must-visit, stunning, renowned, groundbreaking, commitment to.*
- Before: "Nestled in the breathtaking hills, the town stands as a vibrant hub with a rich cultural heritage."
- After: "The town sits in the hills and is known for its weekly market and 18th-century church."

### 5. Vague attributions and weasel words
**Bar: always.** An unnamed authority is a factual-support problem, not a style choice: name the source, add a placeholder, weaken the claim, or cut it.
Opinions assigned to unnamed authorities.
Watch: *industry reports, observers have cited, experts argue, some critics say, several sources* (when none are named).
- Before: "Experts believe it plays a crucial role in the regional ecosystem."
- After: "It supports several endemic fish species, per a 2019 Academy of Sciences survey." (Or cut the claim.)

### 6. "Challenges and Future Prospects" formula
**Bar: always.** One instance is one whole formulaic section; fix it.
The formulaic "Despite its X, it faces challenges… Despite these challenges, it continues to thrive" section.
- Before: "Despite its prosperity, the area faces challenges typical of urban growth. Despite these, it continues to thrive."
- After: "Traffic worsened after 2015 when three IT parks opened. The city began a drainage project in 2022 to handle recurring floods."

### 7. Overused AI vocabulary
**Bar: cluster.**
These appear far more often in post-2023 text and tend to cluster.
Watch: *delve, leverage (verb), utilize, garner, underscore, showcase, harness, foster, cultivate, facilitate, navigate, unlock, empower, streamline, robust, seamless, holistic, tapestry, testament, landscape (abstract), realm, intricate, interplay, pivotal, crucial, vital, vibrant, enduring, comprehensive, multifaceted, nuanced, elevate, align with, whilst, albeit.*
Vague pluralizers (*various, numerous, multiple, diverse*) are a related tell: replace them with the actual count or the named items, not with another synonym.
- Before: "Additionally, pasta is an enduring testament to colonial influence, showcasing how dishes integrated into the culinary landscape."
- After: "Pasta, introduced under colonial rule, is still common, especially in the south."

### 8. Copula avoidance (dodging is/are)
**Bar: cluster.**
Substituting elaborate verbs for a simple "is."
Watch: *serves as, stands as, represents, marks, boasts, features, offers* where "is/has" would do.
- Before: "Gallery 825 serves as the exhibition space and boasts over 3,000 square feet."
- After: "Gallery 825 is the exhibition space. It has about 3,000 square feet across four rooms."

### 9. Negative parallelism and tailing negations
**Bar: cluster.**
"Not only… but also," "It's not just X, it's Y," and clipped negations tacked on the end ("no guessing," "no wasted motion").
- Before: "It's not just a song, it's a statement. The beat isn't only loud, it's relentless."
- After: "The heavy beat sets an aggressive tone."
- Before (tailing): "The options come from the selected item, no guessing."
- After: "The options come from the selected item, so the user doesn't have to guess."

### 10. Rule of three
**Bar: cluster.**
Forcing ideas into threes to sound complete.
- Before: "Expect innovation, inspiration, and industry insights across talks, panels, and networking."
- After: "Expect talks and panels, with time to network between sessions."

### 11. Elegant variation (synonym cycling)
**Bar: cluster.**
Cycling synonyms for the same noun across adjacent sentences.
- Before: "The protagonist faces challenges. The main character overcomes obstacles. The hero returns home."
- After: "The protagonist faces challenges but overcomes them and returns home."

### 12. False ranges ("from X to Y")
**Bar: always.** A range whose endpoints are not on a real scale is a false structure, not a style choice.
"From X to Y" where X and Y aren't on a real scale.
- Before: "From the singularity of the Big Bang to the dance of dark matter, from the birth of stars to the cosmic web."
- After: "The book covers the Big Bang, star formation, and current dark-matter theories."

### 13. Passive voice and subjectless fragments
**Bar: cluster.**
Hiding the actor or dropping the subject.
- Before: "No configuration file needed. The results are preserved automatically."
- After: "You don't need a config file. The system saves the results for you."

### 14. Em and en dashes (strong default, see SKILL.md)
**Bar: always.** Exceptions: exact quotation, explicit user preference, established brand voice.
No `—` or `–` in finished copy. Replace with a period, comma, colon, parentheses, or restructure. Catch spaced dashes and `--`. This is enforced in the main body; listed here for completeness.

### 15. Boldface overuse
**Bar: cluster.** Overuse is by definition a pattern; one bolded key term can stand.
Mechanically bolding phrases and acronym expansions.
- Before: "It blends **OKRs**, **KPIs**, and tools like the **Business Model Canvas**."
- After: "It blends OKRs, KPIs, and tools like the Business Model Canvas."

### 16. Inline-header vertical lists
**Bar: always.** The redundancy is objective: the header restates the sentence or the sentence restates the header.
Lists where each item is a bold header + colon + a sentence that restates it.
- Before: "- **Performance:** Performance is improved. - **Security:** Security is stronger."
- After: "The update speeds up load times and adds end-to-end encryption."

### 17. Title Case in headings
**Bar: context.** Title Case is a legitimate human convention in plenty of marketing copy, so it is not a tell on its own. Follow the provided brand style first; otherwise match the piece's dominant heading convention and fix only inconsistency (AI drafts often mix the two styles). When drafting fresh with no signal either way, default to sentence case.
- Before (mixed in one piece): "## Strategic Negotiations And Global Partnerships" alongside "## What buyers actually ask"
- After: pick the piece's dominant convention and apply it to every heading.

### 18. Decorative emoji
**Bar: always** in final marketing copy, unless the provided brand voice demonstrably uses them.
Emoji used as bullet markers or heading decoration.
- Before: "🚀 **Launch:** Ships in Q3. 💡 **Insight:** Users want simplicity."
- After: "Ships in Q3. Research showed users want simplicity."

### 19. Curly quotation marks
**Bar: context.** Most editors auto-curl, so this is not a tell alone. Act only when they cluster with other tells or clash with the surrounding copy's convention, and match that convention.

### 20. Chat / correspondence artifacts (see SKILL.md)
**Bar: always.** This is process bleed.
Chatbot wrapper pasted into content: *Great question!, Certainly!, You're absolutely right!, here is a…, I hope this helps, let me know if you'd like….* Covered in the main body.

### 21. Knowledge-cutoff disclaimers and speculative gap-filling
**Bar: always.** Both halves are factual risk: the disclaimer is residue, the speculation is invention.
Two tells: (a) leftover cutoff disclaimers; (b) when no source is found, a paragraph *about* not finding one, plus invented filler.
Watch: *as of [date], up to my last training update, while specific details are limited, based on available information, maintains a low profile, keeps personal details private, likely grew up…, it is believed that.*
- Before: "While details are scarce, it appears the company was founded sometime in the 1990s."
- After: "The company was founded in 1994, per its registration." (Or state plainly what isn't known, and cut the guess.)

### 22. Sycophantic / servile tone
**Bar: always.** In a deliverable this is wrapper residue, not style. Note: current Claude models produce little of it by default, so expect few genuine hits.
People-pleasing filler.
- Before: "Great question! You're absolutely right that this is complex. Excellent point."
- After: "The economic factors you raised are relevant here."

### 23. Filler phrases
**Bar: cluster.** A person writes "in order to" once; a machine writes it every time.
- "In order to achieve this goal" → "To do this"
- "Due to the fact that" → "Because"
- "At this point in time" → "Now"
- "Has the ability to" → "Can"
- "It is important to note that the data shows" → "The data shows"

### 24. Excessive hedging
**Bar: cluster.** Never cut a load-bearing caveat; `references/integrity.md` defines which hedges are facts.
Over-qualifying a plain statement.
- Before: "It could potentially possibly be argued that the policy might have some effect."
- After: "The policy may affect outcomes."

### 25. Generic positive conclusions
**Bar: always.** One vague upbeat ending is the whole ending; fix it.
Vague upbeat endings that say nothing.
- Before: "The future looks bright. Exciting times lie ahead on the journey to excellence."
- After: "The company plans to open two more locations next year."

### 26. Hyphenated word-pair overuse
**Bar: cluster** for density. The grammar half is always safe to apply: keep the hyphen when the compound is attributive (*a high-quality report*); drop it when it follows the noun (*the report is high quality*).
AI hyphenates uniformly, including in predicate position.
Watch: *data-driven, cross-functional, client-facing, real-time, long-term, end-to-end, high-quality.*

### 27. Persuasive-authority tropes
**Bar: cluster.**
Phrases that pretend to cut to a deeper truth before restating an ordinary point.
Watch: *the real question is, at its core, in reality, what really matters, fundamentally, the deeper issue, the heart of the matter.*
- Before: "The real question is whether teams can adapt. At its core, what matters is readiness."
- After: "The question is whether teams can adapt, which depends on whether the org will change its habits."

### 28. Signposting and announcements
**Bar: always.** Announcing content instead of delivering it is artifact meta, whatever the phrasing.
Watch: *let's dive in, let's explore, let's break this down, here's what you need to know, without further ado, here's a breakdown, below is….*
- Before: "Let's dive into how caching works. Here's what you need to know."
- After: "Next.js caches data at three layers: request memoization, the data cache, and the router cache."

### 29. Fragmented headers
**Bar: always.** The restating one-liner is objective redundancy; merge or cut it.
A heading followed by a one-line paragraph that just restates the heading.
- Before: "## Performance\n\nSpeed matters.\n\nWhen users hit a slow page, they leave."
- After: "## Performance\n\nWhen users hit a slow page, they leave."

### 30. Diff-anchored writing (see SKILL.md)
**Bar: always** outside changelogs and migration guides, which are out of scope anyway.
Prose written as if narrating a change rather than describing the thing. Covered in the main body under process bleed.

### 31. Marketing buzzwords and clichés (quick blocklist)
**Bar: always** in marketing copy, unless quoting research or backed by a number in the source.
Cut on sight:
*insights, the key to, unlock potential, leverage, optimize, maximize, unleash, driving impact, empower, world-class, cutting-edge, next-gen, game-changer, best-in-class, future-proof, scalable, disruptive, synergy, customer-centric, growth hacking, move the needle, low-hanging fruit, quick wins, win-win, thought leader, at scale (without numbers), paradigm shift, digital transformation, value-add, actionable insights, best practices (unless citing research).*

### 32. Structural tells from social/marketing copy
**Bar: always.** Each of these is a structure, so a single occurrence is the pattern in full.
High-signal structures that bleed into web and email copy. (Full LinkedIn-specific list is intentionally omitted, out of scope for e-books/reports/site copy.)
- **Stat-bomb opener:** 3+ short statistical fragments fired in a row. Weave stats into real sentences.
- **Label-colon framework:** packaging observations as named *Label: description* pairs to fake a methodology. Unless it's a real framework, write prose.
- **Contrast-based negation:** "It's not X. It's Y." Rewrite as a positive, declarative statement.
- **Triple rhetorical-question hook:** 2-3 rapid questions to manufacture intrigue. Open with the actual claim or a specific situation.
- **Punchy orphan closer:** ending on a standalone mic-drop fragment. Close with a real thought or fold it into the last paragraph.
- **Engagement-bait CTA:** "Agree? Thoughts? Drop a comment." Out of place in copy; cut it. If you want action, ask for the one action plainly.
- **Hype opener:** "This changes everything." / "X will never be the same." Start with the specific thing that happened.
- **Runway sentence:** a vague hype line before the actual detail. Cut the runway, start with the substance.
- **Product-tagline phrasing in prose:** compact feature-copy fragments ("Built for scale," "Hands-free until review") dropped mid-paragraph. Write them as sentences a person would say.
- **Fake-fascination opener:** "Interestingly," "What's fascinating is," "It's worth noting that" placed in front of an ordinary point to manufacture intrigue. Cut the opener and make the point directly.
- **Wonder-framing:** "there is a specific kind of magic that happens when," "a love letter to," "the energy in the room." Vague awe that names nothing concrete. Describe the actual experience instead.

### 33. Clean nothing (the de-slop trap)
**Bar: always.** This is a section-level failure: sharpen it from the real material or flag it with a placeholder. Never ship it as a pass.
The failure mode of this entire catalog. You can remove every tell above and still ship copy that is grammatically perfect and completely empty: no claim only this writer could make, no consequence the reader can act on, nothing a competitor could not also say. Clean is not the same as worth reading. Cutting a tell creates a gap; fill it with the specific true thing, never a sanitized blank, and never an invented one. Diagnosis here, the fix in `references/substance.md`.
- Before (slop): "We leverage cutting-edge solutions to drive results for our clients."
- After (clean nothing): "We use modern tools to get results for our clients." (every tell gone, still says nothing)
- After (substance): "Your reps stop copying leads between four tabs. The CRM writes call notes back to the deal on its own, so follow-up happens the same day instead of next week."
