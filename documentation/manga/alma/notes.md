# Notes — ALMA Manga

## Concepts omitted (or compressed)

- **AI-generating algorithms / "learning to learn" lineage.** The paper situates ALMA within Clune's three pillars (meta-learning architectures, meta-learning algorithms, automatic environment generation) and relates it to NAS, MAML, Meta-RL, POET, ADAS, AgentSquare. The manga folds all of this into "stop hand-drawing the box" (page 3) rather than naming the lineage. A sequel "family tree" page could draw it.
- **One-shot vs. continual evaluation.** A key distinction in the paper is that prior automated-design work evaluates only one-shot agentic performance, whereas ALMA explicitly optimizes for *continual* learning across a task sequence. The manga implies this via the repeated-task framing (pages 1–2) but does not dramatize the evaluation protocol.
- **Exact archive/sampling mechanics.** Figure 1's loop is faithfully rendered on page 4, but selection pressure, how a parent design is chosen, and stopping criteria are abstracted to "sample a promising card."
- **Specific quantitative results.** Page 7's chart is qualitative ("learned beats hand-crafted on every world; cheaper"). The real per-domain numbers (Table 1 / Figure 6) could anchor a data-appendix page.

## Possible sequel pages

1. **The family tree** — ALMA's place among NAS / MAML / Meta-RL / POET / ADAS.
2. **Anatomy of a discovered design** — open one winning card and read its schema + retrieval + update code.
3. **Cost curves** — a page on the efficiency result (learned designs cheaper than most baselines).
4. **Safety appendix** — unpacking "when developed and deployed safely" for self-improving systems.
5. **From ALMA to ENGRAM** — a crossover page mapping ALMA's learned memory onto an ENGRAM submission.

## Alternative metaphors considered

- **A chef rewriting recipes** instead of an architect redrawing blueprints — rejected because "design = code/schema" reads more naturally as architecture/engineering.
- **A gardener pruning** for the archive — charming but muddies the "scored, propagating designs" point; the glowing drawer-cards with gauges keep the evaluation explicit.
- **Personifying the Meta Agent as clearly human** — avoided; keeping it an architect-of-light preserves that it is an automated process, not a person.

## Visual metaphors used

- **Engy's chest-notebook = the agent's memory** (fills green when recalled, blank/grey when forgotten) — used throughout.
- **Hand-drawn chalkboard blueprint = human-crafted, fixed design** (page 3).
- **The Meta Agent's code-quill = designs expressed as executable code** (pages 4–5).
- **Schema / retrieval / update tri-diagram = the structure of a memory design** (page 5).
- **Wall of drawer-cards + success gauges = the archive of designs and evaluation logs** (page 6).
- **Four dioramas + comparison bar chart = the four domains and the results** (page 7).
- **A road of dated state-tiles, future tiles greyed = ENGRAM's no-hindsight rule** (page 8).

## References for future expansion

- Source: "Learning to Continually Learn via Meta-learning Agentic Memory Designs," arXiv 2602.07755v1. Code: https://github.com/zksha/alma
- Domains: ALFWorld, TextWorld, Baba Is AI, MiniHack.
- Companion book in this repo: `../ama-bench/` (AMA-Bench) — the evaluation-side counterpart to ALMA's design-side story.
- Repo tie-in: ENGRAM Kit (`CONTRACT.md`, `STATE_FORMAT.md`) — the no-hindsight memory challenge page 8 points to.

## Assumptions

- The "Success: 0.3 → 0.4" numbers on page 4 are illustrative of Figure 1's example logs, not headline results.
- "Engy" as a recurring mascot is shared with the AMA-Bench book and the broader ENGRAM explainer milestone for cross-book consistency.
