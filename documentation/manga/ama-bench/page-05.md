Page 05

Purpose:
The finding — agent memory is hard even for frontier models (GPT-5.2 ≈ 72%), and existing lossy compression + similarity-based retrieval fail because they miss the causal and objective information the task needs.

Audience note:
Builds on page 4. "Similarity-based retrieval" = fetch the note that *looks* most like the question. Show why that can grab the wrong thing.

Panel Count:
6

Image Prompt:

Create a six-panel educational manga page.

Style:
Soft-color educational manga.
Light watercolor / gentle anime palette — warm cream paper, soft ink linework, muted pastel washes.
One restrained accent: recall-green (#00e0a4), used only for memory, recall, and "it worked" moments.
Clean confident linework, generous negative space, friendly but precise.
Calm, contemplative, explanatory tone — diagrams integrated naturally into the scene.
Not gritty. Not neon. Not chibi. Not glossy 3D. Not photorealistic.

Characters in this page:
- ENGY: a small, rounded librarian-robot with a soft matte-cream chassis, one big recall-green camera-lens eye, stubby arms, an open NOTEBOOK in its chest (its memory) — here the notebook uses a simple "find the most similar note" method.
- THE EXAMINER: a poised proctor figure holding sealed question-cards; a quiet scoreboard slate showing percentages.
- SENSEI: a calm middle-aged human archivist with round glasses, a soft cardigan, neat greying hair, holding a slim wooden pointer.

Setting:
The examination hall. A scoreboard slate is visible. Engy answers using a basic memory method.

Panel 1 (medium):
The Examiner poses a question that needs a *causal* fact ("because you unlocked the gate earlier..."). Engy starts to search its notebook. Dialogue space.

Panel 2 (close, the failure mechanism):
Engy's notebook grabs the note that simply LOOKS most similar to the question (same words) — but it's the wrong one; the truly relevant causal note sits ignored nearby, dim. Show two notes: a look-alike (picked) and the real one (missed).

Panel 3 (medium, lossy compression):
A second failure: the notebook had squashed many scrolls into a tiny summary and threw away the exact objective detail the question needed. The missing fact is a faded gap.

Panel 4 (close, the wrong answer):
Engy gives a confident but wrong answer; its eye flickers from green to grey. The Examiner marks it.

Panel 5 (the scoreboard):
Sensei's pointer at the scoreboard slate: even the strongest frontier model only scores about 72% — and many memory systems do worse on these long-horizon tasks than plain long-context baselines. Honest, sobering numbers.

Panel 6 (two-shot, the diagnosis):
Sensei explains the root cause: it's not that the model is weak — it's that the *memory method* loses the causal, objective information. Sets up page 6. Dialogue space.

Camera directions:
Make the "similar but wrong note" mechanic crystal clear in panel 2; use grey (not green) for the failure beats; reserve the scoreboard for panel 5; end on the diagnosis.

Lettering:
Leave room for English dialogue and captions.
- Panel 1 — Examiner: "Why is the gate open now?"
- Panel 2 — (caption) "Similarity search grabs the note that *looks* alike — and misses the one that actually *caused* it."
- Panel 3 — (caption) "Lossy compression had already thrown away the exact detail."
- Panel 4 — Engy: "Um... it was always open?" (wrong) — Examiner: "Incorrect."
- Panel 5 — Sensei: "Even the best models reach only ~72%. Many memory systems do *worse* than just keeping everything in context."
- Panel 6 — Sensei: "The model isn't the weak link. The *memory design* is — it loses the causal, objective facts."

Output:
A single finished manga page.
