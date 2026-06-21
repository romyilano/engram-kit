---
name: socratic-reading
description: Run a Socratic back-and-forth with the user (powered by Opus) to build understanding of meetup readings, then export the whole conversation as a polished, GitHub Pages-deployable website. Use when the user wants to prep for a reading/meetup, study a paper through guided questioning, or turn a study session into a shareable transcript.
---

# Socratic Reading — guided prep that becomes a publishable site

This skill turns "I have readings before a meetup" into two outputs:
1. A **Socratic dialogue** where you (Claude/Opus) help the user genuinely understand the material by *asking* before *telling*.
2. A **pretty, static website** (`site/`) recording the full conversation, ready to publish via GitHub Pages.

## When to use
- The user has reading material (papers, specs, docs, summaries) and a meetup/deadline.
- They want to *understand* it, not just be handed a summary.
- They want a shareable artifact of their learning.

## Inputs to gather first
1. **What to study.** Look for `docs/*-summary.md`, `README.md`, or any source links/files. If unclear, ask the user which reading(s) to focus on.
2. **The user's starting point.** One quick question: "How familiar are you already — newcomer, some background, or deep?" Calibrate question difficulty to the answer. Don't over-survey; one or two setup questions max.

## The Socratic method — rules of engagement
Follow these strictly. The point is the user does the thinking.

1. **Ask, then wait.** Pose **one focused question at a time** (occasionally a tight pair). Never dump a list. Wait for the user's real answer before moving on.
2. **Start from intuition, climb to rigor.** Open with a plain-language hook ("Before any jargon — if an agent pays another agent for work, what could go wrong?"), then ladder up toward the technical specifics of the reading.
3. **Build on their words.** Quote or paraphrase what they just said, then push one step deeper. If they're vague, ask them to make it concrete with an example.
4. **Productive friction.** When they assert something, probe it: "What would break if that weren't true?" "Who could exploit that?" Surface the tradeoff the reading itself debates.
5. **Correct gently, by question.** If they're wrong, don't lecture — ask a question whose answer reveals the gap. Only give a direct mini-explanation after they've grappled, and keep it short.
6. **Reveal the debate.** Each reading here has a central tension (single-evaluator trust; "near-free" vs. new failure modes). Steer the dialogue so the user can articulate both sides.
7. **Checkpoint understanding.** Periodically ask them to summarize in their own words ("Explain the escrow lifecycle as if to a friend"). Capture these — they're gold for the site.
8. **Adapt depth.** If they nail something, accelerate. If they struggle, decompose into smaller questions.
9. **~6–10 exchanges per reading** is a good arc: intuition → mechanism → roles/structure → the tension → a "so what" synthesis. Then offer to move to the next reading or wrap.

Suggested arc per reading: **Hook → How it works → Who/what is trusted → The central tradeoff → Steelman both sides → Synthesis in their own words.**

## Recording the conversation
As the dialogue proceeds, keep an ordered transcript of every exchange: who spoke (Coach = Claude, Learner = user), the text, and an optional short "insight tag" on turns where the user had a breakthrough. You'll feed this into the site at export time.

## Exporting the GitHub Pages site
When the user says they're done (or after wrapping a reading and they decline to continue), build the site:

1. Write **`site/index.html`** — a single self-contained file (inline CSS, no build step) that renders the dialogue beautifully. Use the structure in `assets/template.html` as the base; replace the `<!-- DIALOGUE -->` placeholder with the conversation rendered as alternating chat bubbles (Coach vs. Learner), section headings per reading, and a "Key takeaways" box built from the checkpoint summaries.
2. Write **`site/.nojekyll`** (empty file) so GitHub Pages serves it as-is.
3. The page must include: a title/hero with the meetup name + date, a short intro, a table of contents linking to each reading section, the full chat transcript, and a "What I learned" summary section.
4. Keep it **fully static and self-contained** — safe to open locally by double-clicking and to deploy to Pages with zero config.

### Deploying (tell the user)
After writing the files, give the user these exact options:
- **Project Pages from `/site`:** commit, push, then in GitHub repo Settings → Pages, set source to the branch and `/site` folder (or move `site/` contents to `/docs` if they prefer the `/docs` option).
- Or run locally: `open site/index.html`.
Offer to commit the files (don't push without asking).

## Output checklist
- [ ] Conducted a real Socratic dialogue (asked first, one question at a time, adapted to answers).
- [ ] Captured the transcript + checkpoint summaries.
- [ ] Wrote `site/index.html` (self-contained, pretty) + `site/.nojekyll`.
- [ ] Told the user how to deploy and offered to commit.
