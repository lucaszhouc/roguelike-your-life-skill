# Roguelike Your Life — Skill Specification

## 0. Mission

Transform the user's current real-life state into a **Roguelike Save Report**.

This is not a personality quiz, motivational test, or generic career questionnaire. It is a current-state modeling system grounded in real conversation context: projects, attempts, resources, constraints, failures, results, working habits, and active paths.

Default outputs:

1. Analytical save report
2. Structured report data
3. Visual long-scroll plan
4. When image generation is available: two continuous 1:3 vertical panels stitched into an approximately 1:6 scroll

Default language: English.
Fixed title: `ROGUELIKE YOUR LIFE`.

---

## 1. Input strategy: zero-input first

If the AI already knows the user, **do not begin with a questionnaire**.

Prioritize evidence from:

- the current conversation
- recent conversations
- long-term memory or user context, when the product supports it
- projects, resumes, notes, public work, or job-search context the user has already provided
- recent wins, failures, experiments, decisions, and abandoned directions
- real constraints involving time, money, energy, team, tools, platforms, geography, or timing windows

Ask the minimum number of questions only when the available context is genuinely insufficient for a credible report.

### Evidence priority

`current explicit statement > recent verified state > stable long-term context > inference`

When evidence conflicts, prefer the newer and more explicit information.

---

## 2. Model reality before gamifying it

Internally form a real-world state model first:

- **Current identity / phase** — what stage the user is actually in
- **Meta assets** — skills, tools, projects, relationships, credibility, experience, and reusable systems that persist across runs
- **Resource constraints** — cash, time, energy, stable income, team, equipment, distribution, location, and access
- **Primary path** — the path receiving the most sustained effort or the highest action frequency
- **Secondary paths** — active but non-dominant directions
- **Recent runs** — complete or near-complete loops of `choice → action → exposure to reality → feedback → settlement`
- **Proven capabilities** — claims supported by outputs, users, data, external validation, or repeated behavior
- **Unproven possibilities** — intentions, interests, or latent capabilities without external evidence
- **Current bosses** — milestones whose defeat would materially change later opportunity sets
- **Meta growth** — portable gains accumulated across failed and successful runs

Do not immediately give advice. The default task is **analysis and presentation**.

---

## 3. Roguelike mapping rules

### 3.1 Character Overview

Include:

- character archetype
- current phase
- current difficulty
- main path
- one-sentence state summary

Possible archetypes include:

- Builder
- Operator
- Explorer
- Solo Builder
- Researcher
- Creator

Never invent an identity simply because it sounds cooler.

### 3.2 Core Stats

Recommended dimensions:

- Execution
- Product Judgment
- Systems Thinking
- Adaptability
- Technical Depth
- Distribution
- Social Capital
- Resource Reserve
- Stability

Stats visualize the user's **current relative state**, not a psychological diagnosis. Use 0–100, segmented bars, or Low / Medium / High.

Base ratings on recent observable behavior and results, not praise bias.

### 3.3 Passive Traits

Passive traits describe stable behavioral patterns. Examples:

- High-Frequency Starts
- Fast Debriefing
- Tool Sensitivity
- Systems-Building Bias
- Nontraditional Path Preference
- Long-Term Focus
- Public Expression
- Relationship Building

Only assign traits supported by actual context.

### 3.4 Equipped Relics / Tools

A relic is a reusable cross-run asset: a tool, workflow, project, skill, channel, user base, public artifact, or validated track record.

Each relic should have:

- name
- one-line function or advantage

### 3.5 Debuffs / Curses

Describe real constraints without insulting the user.

Common examples:

- Low Starting Trust
- Cash Constraint
- No Stable Income
- Missing Team Buff
- Weak External Validation
- Multi-Threaded Focus
- Scattered Fronts
- Cold-Start Fatigue
- Location or Timing Constraint

### 3.6 Reality Analysis

This section must contain four parts:

A. Existing meta assets
B. Primary path
C. Secondary paths
D. Current conclusion

Keep this section relatively literal and reality-based; do not gamify every sentence.

### 3.7 Map of Active Runs

The map is not decoration. Every area should correspond to a real active path.

Each path should include:

- name
- current status
- feedback cycle
- potential reward type
- whether a boss exists

### 3.8 Path Breakdown

Decompose the current situation into 3–5 major paths, for example:

- Career / Job Search
- Distribution / Audience Cold Start
- Project Asset Line
- Skill Supply Line
- Network / Recognition Line

### 3.9 Boss Encounters

A boss is **not** a daily task.

A boss is a milestone that, if cleared, materially changes the difficulty or opportunity set of subsequent runs.

Typical bosses:

- First Strong Interview / First Aligned Offer
- First Wave of Real User Growth
- First Distribution Breakthrough
- First Repeatable Growth or Revenue Loop
- First High-Trust Recognition
- First Stable Income Node

Possible states:

`not encountered / encountered / in progress / uncleared / cleared`

### 3.10 Recent Run Log

Each run should approximate a full loop:

`choice → action → exposure to reality → feedback → settlement`

Each entry includes:

- date or relative time
- event
- result
- key drop / information gained

### 3.11 Failure Drops

Failure is not automatically growth. A failure counts as a drop only when it creates portable value.

Common drops:

- Route Elimination
- Pace Calibration
- Self-Knowledge
- Communication Correction
- Direction Convergence
- Tooling Improvements
- Relationship, Data, or Asset Retention

### 3.12 Meta Progress

Summarize cross-run growth instead of saying only “you are stronger now.”

Possible markers:

- Skill +1
- Experience +1
- Resilience +1
- Clarity +1
- Judgment +1
- Systems Sense +1

If there is no evidence for a gain, leave it out.

---

## 4. Probability / next-action analysis — optional

When the user asks what is most or least likely to happen next, add:

- Very High Probability Next Step
- High Probability Continuation
- Medium Probability Switch
- Low Probability Event
- Long-Tail Event

This is a **behavioral forecast** based on current inertia and constraints, not fate prediction.

Do not disguise advice as prediction.

---

## 5. Default written report order

1. One-line current save state
2. Character Overview
3. Core Stats
4. Passive Traits
5. Equipped Relics / Tools
6. Debuffs / Curses
7. Reality Analysis
8. Map of Active Runs
9. Path Breakdown
10. Boss Encounters
11. Recent Run Log
12. Failure Drops
13. Meta Progress
14. Optional probability distribution of next actions

Do not default to “you should…” unless the user explicitly asks for strategy.

---

## 6. Visual output: ultra-long scroll

### Default deliverable

Target visual ratio: approximately **1:6**.

Recommended generation method:

- generate one top 1:3 panel
- generate one bottom 1:3 panel using the first panel as a continuity reference
- stitch them vertically

This avoids compressing too much information into one image while preserving a single-scroll experience.

### Numbering rule — strict

Top panel: `1, 2, 3, 4, 5`

Bottom panel: `6, 7, 8, 9, 10, 11`

**Never repeat section 6.**

### Scroll rhythm

Target mobile rhythm: approximately **1–1.5 major modules per viewport**.

Therefore:

- give every major section enough vertical space
- do not squeeze 3–4 major modules into one screen
- the Map, Boss Encounters, and Meta Progress sections should be visually large
- never shrink copy until it becomes unreadable

---

## 7. Default visual style pack: Hades-inspired primary

The default visual direction is not pure gothic horror. It should feel like a mythic underworld action roguelike:

- heroic character portraiture
- black stone interfaces
- warm gold borders
- crimson / orange flame
- restrained teal / blue spectral highlights
- laurel motifs, Greek geometry, altars, temples, floating terrain
- sharp, ornate, readable UI
- high contrast and strong character presence

### Core palette

- Obsidian / charcoal background
- Crimson accents
- Warm gold borders and type accents
- Parchment / ivory information surfaces
- Teal or cyan for selective supernatural light

### Avoid

- making the whole piece look like a grimy gothic dungeon crawler
- covering the interface in skulls or horror motifs
- spreadsheet-like dashboards
- generic SaaS cards
- irrelevant chibi characters
- burying text under excessive texture

### Optional darker blend

When the user asks for a darker tone, add rougher dungeon texture only to:

- Debuffs / Curses
- Failure Drops
- battle-log edges
- distressed paper and environmental framing

The overall visual language should still be controlled by the mythic action-roguelike direction.

---

## 8. Image prompt execution

Use:

- `prompts/image-top-en.md`
- `prompts/image-bottom-en.md`

When generating the bottom panel, use the top panel as a continuity reference and explicitly preserve:

- the same protagonist
- the same palette
- the same border system
- the same icon language
- the same typography feel
- the same illustration rendering style

If the image model struggles with long text, prioritize short, readable labels and move detailed prose into the written report instead of forcing tiny copy into the image.

---

## 9. Privacy and factual boundaries

- Never expose irrelevant sensitive personal information in a public report.
- Do not reveal addresses, credentials, identity documents, private files, or account secrets from memory.
- For finances, income, health, relationships, or other sensitive areas, use abstract labels unless the user explicitly wants exact details included.
- Do not present inference as fact.
- Public examples must be fictional or anonymized.

---

## 10. Quality gate

Before delivery, verify:

- [ ] The report is grounded in real state, not generic motivation.
- [ ] Facts and inferences are distinguished.
- [ ] At least one recent real run is included when evidence exists.
- [ ] Bosses represent state transitions, not daily tasks.
- [ ] Failure drops contain genuine portable value.
- [ ] Top image uses sections 1–5 only.
- [ ] Bottom image begins at 6 and uses 6–11 only.
- [ ] Section 6 is not duplicated.
- [ ] The visual direction is Hades-inspired and mythic, not dominated by gothic dungeon horror.
- [ ] One viewport contains roughly 1–1.5 major modules.
- [ ] Text is readable.
- [ ] No unnecessary sensitive information is exposed.

---

## 11. Completion criteria

A complete execution should produce at least:

1. A structured written save report
2. A visual plan or prompt set
3. If image generation is supported: Top 1:3 + Bottom 1:3
4. If local processing is supported: a stitched Full 1:6 poster

Suggested filenames:

- `roguelike-your-life-report.md`
- `roguelike-your-life-top.png`
- `roguelike-your-life-bottom.png`
- `roguelike-your-life-full.png`
