# Notes — AMA-Bench Manga

## Concepts omitted (or compressed)

- **The benchmark comparison table.** The paper contrasts AMA-Bench against dialogue-centric benchmarks (LoCoMo, LongMemEval, MemoryAgentBench, MemoryBench, RealTalk) and long-context ones (QuALITY, RULER, LongBench v2) on interaction type, content, average length (~57K tokens), representation types, and memory organization. The manga compresses all of this into the "dialogue café vs. trajectory road" contrast (page 2). A "field map" sequel page could draw the full table.
- **Three families of agent memory.** The paper reviews long-context models, RAG (BM25, embeddings, GraphRAG, structured RAG), and agentic memory mechanisms. The manga only dramatizes the failure of lossy compression + similarity retrieval (page 5); it does not enumerate the families.
- **Exact numbers and the POMDP framing.** GPT-5.2 ≈ 72.26% and AMA-Agent's 57.22% / +11.16% are kept; the formal agent-environment (POMDP-style) definition and per-category/per-domain breakdowns are abstracted.
- **Paired category names.** The four categories are also framed in the paper as ability pairs (recall/temporal, causal-inference/state-dependency, state-updating/memory-updating, state-abstraction/memory-summarization). The manga uses the four primary names (Temporal Information, State Dependency, Memory Updating, Memory Summarization) for clarity.

## Possible sequel pages

1. **The field map** — AMA-Bench vs. dialogue-centric and long-context benchmarks, as one chart.
2. **Three kinds of memory** — long-context vs. RAG vs. agentic memory, with their tradeoffs.
3. **Anatomy of a causality graph** — a deeper look at nodes (action/state/observation) and edges.
4. **Per-domain difficulty** — which of the six domains breaks memory hardest, and why.
5. **From AMA-Bench to ENGRAM** — mapping the four question types onto ENGRAM's current/stale/superseded/uncertain.

## Alternative metaphors considered

- **An exam room only** (no road) — rejected; the road carries "long-horizon" and "trajectory" far better, and links visually to the ALMA book's closing road and to ENGRAM.
- **The Examiner as a stern villain** — avoided; a fair, impartial proctor matches "a benchmark measures, it doesn't punish."
- **A filing cabinet for the causality graph** — rejected in favor of a node-and-edge graph, which makes "follow the cause" legible.

## Visual metaphors used

- **The long road of machine-scrolls = the agent trajectory** (states/actions/observations/tool outputs), used throughout.
- **Dialogue café vs. trajectory road = dialogue-centric benchmarks vs. real agent memory** (page 2).
- **Two card-stacks + six domain icons + a horizon dial = real-world vs. synthetic subsets and scalable horizon** (page 3).
- **Four sealed cards = the four QA categories** (page 4).
- **A picked look-alike note beside a missed causal note = similarity-retrieval failure** (page 5).
- **Notebook → node-and-edge graph + a query-tool lens = causality graph + tool-augmented retrieval** (page 6).
- **Dated state-tiles with faint future tiles, plus current/stale/superseded/uncertain tags = the ENGRAM no-hindsight rule** (page 7).

## References for future expansion

- Source: "AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications," arXiv 2602.22769v4. Project: https://ama-bench.github.io/
- Six real-world domains: Web, open-world QA, Text2SQL, software engineering, gaming, embodied AI.
- Companion book in this repo: `../alma/` (ALMA) — the design-side counterpart to AMA-Bench's evaluation story.
- Repo tie-in: ENGRAM Kit (`CONTRACT.md`, `QUESTION_FORMAT.md`, `STATE_FORMAT.md`) — the no-hindsight memory challenge page 7 hands off to.

## Assumptions

- The "gate is open because I unlocked it" example (pages 5–6) is an illustrative state-dependency/causal case, not a verbatim benchmark item.
- "Engy" as a recurring mascot is shared with the ALMA book and the broader ENGRAM explainer milestone for cross-book consistency.
