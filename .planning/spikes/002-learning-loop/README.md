---
spike: 002
name: learning-loop
type: standard
validates: "Given a scene about a paper concept, when the player hits a comprehension checkpoint (Examiner quiz with in-character corrective feedback + retry), then the interaction reinforces the idea better than passive reading — the reason a learning VN beats the flipbook."
verdict: VALIDATED
related: [001, 003]
tags: [vn, pedagogy, quiz, learning]
---

# Spike 002: Learning Loop

## What This Validates

This is the spike that decides whether the whole idea is worth building. The flipbook already
shows panels + captions. **When** a player hits a comprehension checkpoint — the *Examiner*
(AMA-Bench personified) asks a question, a wrong answer triggers in-character corrective feedback
and a retry, a right answer lights up Engy's notebook and advances — **then** the player has to
*apply* the concept, not just read it. That retrieval-plus-feedback loop is the pedagogical reason
a VN beats a passive flipbook.

## Research

No new external libraries (builds on the Spike 001 vanilla engine). The pedagogy is grounded in
two well-established findings, applied here deliberately:

- **Retrieval practice (the testing effect):** being asked to recall/apply a concept produces
  stronger retention than re-reading it.
- **Corrective feedback:** a wrong answer that explains *why* it's wrong (and is immediately
  retryable) turns an error into a learning event instead of a dead end.

Content is drawn from real AMA-Bench material — the "memory is a causal trajectory, not a
conversation" thesis and the four question categories (temporal, state-dependency,
memory-updating, summarization) from the character sheet and `page-NN.md` files. The **Examiner**
character already exists in the cast specifically to "administer the benchmark and reveal where
memory breaks" — so the quiz-master role is brand-native, not bolted on.

## How to Run

```bash
open .planning/spikes/002-learning-loop/index.html
```

Read the two setup lines, then answer the Examiner's checkpoint. **Deliberately pick a wrong
answer first** to see the corrective feedback + retry, then pick the right one to see the notebook
light up and the mastery dot fill. Two checkpoints; the end card shows your learning stats.
Top-right **export** includes a `learning` summary in the JSON.

## What to Expect

- Two AMA-Bench checkpoints administered by the **Examiner** (amber name plate, distinct from the
  green character plates).
- Wrong answer → that option greys/ambers out, an amber "Examiner ✗" feedback box explains the
  misconception, and you can still pick another option (no penalty, just learning).
- Right answer → green "Examiner ✓" confirmation, a recall-green flash, the background warms, and a
  mastery dot fills in the HUD.
- End card with **checkpoints passed / first-try correct / total attempts** — the signal that
  separates "recognized" from "mastered".

## Observability

Forensic log records every `checkpoint-shown`, each `answer` (✓/✗ with try number and whether it
was a first-try correct), `line`, `end`, `replay`. Wrong answers are tagged `bad` in the on-screen
log. **Export** embeds a `learning` block: `{checkpoints, passed, firstTryCorrect, totalAttempts}`
— the exact telemetry a real build would use to measure whether a scene is teaching.

## Investigation Trail

1. **Framing the checkpoint as a character, not a popup.** First instinct was a generic quiz modal.
   Rejected — it would break the VN fiction. Used the existing **Examiner** persona so the question
   *is* the story beat. The amber name-plate (the brand's `--stale` token, reserved for
   stale/superseded info) doubles as the "you're being tested" signal.
2. **Wrong answers must not end the scene.** Early version advanced on any click. That punishes
   exploration and kills the learning value. Reworked so an unanswered/incorrect checkpoint *blocks*
   advance — you stay until you get it right — but each wrong attempt yields specific corrective
   feedback keyed to that misconception (not a generic "try again").
3. **Distractors had to be plausible-wrong, not silly.** For the memory-updating question, the
   tempting wrong answer is *temporal* ("before… last changed" sounds like time-ordering). The
   feedback explicitly disambiguates the two AMA-Bench categories — so even a wrong click teaches
   the distinction. That's the moment passive reading can't reproduce.
4. **Measuring learning.** Added first-try-correct vs. total-attempts tracking. Simulated a
   q1-right / q2-wrong-then-right run headlessly: `passed 2/2, firstTryCorrect 1/2, totalAttempts 3`
   — confirming the metric distinguishes "knew it" from "figured it out after feedback", which is
   the data a real build needs to tune difficulty.

## Results

**Verdict: VALIDATED** (loop logic + stat tracking verified headlessly; the felt pedagogical
punch is a human playtest — open the file and miss one on purpose).

- The comprehension checkpoint is a small extension of the Spike 001 engine — a `{quiz}` node
  slotted where 001 had a flavor `{choice}` node. **The learning loop is cheap once the VN exists.**
- The Examiner persona makes the quiz diegetic: it reads as a story confrontation, not a pop quiz,
  which is exactly what a *narrative* learning game needs.
- Corrective feedback keyed to each distractor means **wrong answers teach** — the single biggest
  edge over the flipbook, which can only show the right answer.
- First-try-correct vs. attempts is a usable mastery signal and exports cleanly for telemetry.
- **Carries forward:** the real build should author 1–2 checkpoints per paper concept, always
  diegetic (Examiner / Sensei), always with per-distractor feedback. **Open question for the real
  build:** how many checkpoints per page before it feels like a test instead of a story — a tuning
  question, not a feasibility one.
