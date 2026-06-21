# Character Sheet — AMA-Bench Manga

Characters must remain **visually and tonally consistent across every page**. Restate the **bolded** visual traits inside each page prompt — the image model has no memory between generations. Engy and Sensei are shared with the ALMA book; keep them identical.

---

## Engy

- **Name:** Engy
- **Role:** The agent being tested — the one whose memory the benchmark probes.
- **Age:** "New model" — reads young and earnest.
- **Appearance:** **A small, rounded librarian-robot with a soft matte-cream chassis, one big friendly camera-lens eye that glows a faint recall-green, short stubby arms, and an open NOTEBOOK embedded in its chest — that notebook is its MEMORY. The pages flutter and glow recall-green when Engy recalls correctly, and go blank/grey when memory fails.**
- **Distinguishing features:** **Carries a small satchel for the machine-generated scrolls it picks up along the road (states, actions, observations, tool outputs).**
- **Personality:** Curious, eager, a little forgetful; takes the test in good faith.
- **Purpose:** Makes "agent memory under test" physical and watchable.

## Sensei

- **Name:** Sensei
- **Role:** Teacher / narrator. Frames each concept; never lectures.
- **Age:** Middle-aged.
- **Appearance:** **A calm human archivist: round glasses, a soft cardigan over a high-collar shirt, neat greying hair, carries a slim wooden pointer.**
- **Distinguishing features:** **Always holding the slim wooden pointer, used to indicate diagrams drawn in the air or on a board.**
- **Personality:** Warm, patient, precise. Teaches by demonstration.
- **Purpose:** The reader's guide; explains what the benchmark is really measuring.

## The Examiner

- **Name:** The Examiner (the benchmark, personified)
- **Role:** Administers AMA-Bench — asks the questions and scores the answers fairly.
- **Age:** Indeterminate; reads as a kind but rigorous proctor.
- **Appearance:** **A poised proctor figure holding a fan of question-cards. Each card is stamped with one of four category seals: TEMPORAL, STATE-DEPENDENCY, MEMORY-UPDATING, SUMMARIZATION. Neat, impartial, soft-toned robes; a small balance-scale emblem at the collar.**
- **Distinguishing features:** **The fan of four-sealed cards; a quiet scoreboard slate that shows accuracy percentages.**
- **Personality:** Fair, exacting, unmoved by excuses. Tests, does not punish.
- **Purpose:** Embodies the benchmark and its four question types; reveals where memory breaks.

## The Long Road / Trajectory

- **Name:** The Long Road (the agent's trajectory)
- **Role:** The journey whose record IS the thing memory must hold.
- **Appearance:** **A long winding road Engy walks, strung with machine-generated scrolls dropped and collected along the way: little JSON tags, small ASCII tables, code snippets — each a state, action, observation, or tool output, linked nose-to-tail like a causal chain (each scroll's edge plugging into the next).**
- **Distinguishing features:** **The scrolls are objective and terse (no chit-chat); a faint causal thread of recall-green light links each scroll to the ones it caused.**
- **Personality:** N/A — environment/motif.
- **Purpose:** Shows that real agent memory is a causal, machine-generated *trajectory*, not a conversation.
