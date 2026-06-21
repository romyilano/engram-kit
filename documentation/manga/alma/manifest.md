# Manifest — ALMA Manga

**Title:** *The Notebook That Redesigns Itself* — an ALMA explainer
**Source:** "Learning to Continually Learn via Meta-learning Agentic Memory Designs" (ALMA)
**Authors:** Yiming Xiong, Shengran Hu, Jeff Clune (UBC · Vector Institute · CIFAR)
**Source URL / id:** arXiv 2602.07755v1 · code: https://github.com/zksha/alma
**Topic slug:** `alma` (panel image prefix: `alma`)
**Audience:** Motivated newcomer to AI / agent memory. Assumes curiosity, not expertise.
**Depth:** Conceptual — the *why* and the *loop*, not the implementation details.

## Style preset — Soft-color / watercolor (locked)

```
Style:
Soft-color educational manga.
Light watercolor / gentle anime palette — warm cream paper, soft ink linework, muted pastel washes.
One restrained accent: recall-green (#00e0a4), used only for memory, recall, and "it worked" moments.
Clean confident linework, generous negative space, friendly but precise.
Calm, contemplative, explanatory tone — diagrams integrated naturally into the scene.
Not gritty. Not neon. Not chibi. Not glossy 3D. Not photorealistic.
```

## Core concepts (dependency order)

1. Foundation models are **stateless** → no memory, no continual learning.
2. **Memory modules** let agents store and reuse past experience.
3. Human-crafted memory designs are **fixed** → they don't adapt to diverse, non-stationary tasks.
4. ALMA **meta-learns the memory design** via a Meta Agent (the open-ended loop).
5. The search space is **executable code** — schemas + retrieval + update mechanisms.
6. The **archive** of designs + evaluation logs guides future search.
7. **Results** across four domains: learned designs beat human-crafted, more cost-efficient.
8. **Big picture** — a step toward self-improving, continually-learning AI (safely); ties to ENGRAM.

## Page table

| #  | Concept | Narrative purpose | Visual metaphor | Status |
|----|---------|-------------------|-----------------|--------|
| 01 | Statelessness | Problem: no memory ⇒ re-solve from scratch | Engy's notebook wipes blank each task | prompt-ready |
| 02 | Memory modules | The common fix: store & reuse experience | The chest-notebook fills with notes | prompt-ready |
| 03 | Fixed designs | Limitation: hand-drawn memory can't adapt | A rigid hand-drawn box that breaks on a new task | prompt-ready |
| 04 | The Meta Agent loop | Core idea: meta-learn the design | Sample → Reflect → Plan → Build → Verify → Evaluate → Archive | prompt-ready |
| 05 | Code as search space | Designs are code: schema + retrieval + update | Meta Agent writes Engy a new notebook in code | prompt-ready |
| 06 | The archive | Sample designs + logs to seed new ideas | A glowing wall of drawer-cards with gauges | prompt-ready |
| 07 | Results | Learned designs win across four worlds, cheaper | Four little worlds; Engy thrives with tailored memory | prompt-ready |
| 08 | Big picture | Self-improving memory, safely; ENGRAM tie-in | Engy + Sensei look ahead at a road of dated states | prompt-ready |

**Total pages:** 8. Panel art lives in `panels/alma_pageNN.png` (placeholders until generated).
