# Manifest — AMA-Bench Manga

**Title:** *The Long Road Test* — an AMA-Bench explainer
**Source:** "AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications"
**Authors:** Yujie Zhao, Boqin Yuan, Junbo Huang, Haocheng Yuan, Zhongming Yu, Haozhou Xu, Lanxiang Hu, Abhilash Shankarampeta, Zimeng Huang, Wentao Ni, Yuandong Tian, Jishen Zhao
**Source URL / id:** arXiv 2602.22769v4 · project: https://ama-bench.github.io/
**Topic slug:** `ama-bench` (panel image prefix: `amabench`)
**Audience:** Motivated newcomer to AI / agent memory. Assumes curiosity, not expertise.
**Depth:** Conceptual — what the benchmark measures and why memory fails, not dataset internals.

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

1. LLM agents now run **long-horizon** tasks; memory keeps them coherent.
2. Real agent memory is a **trajectory** (states, actions, observations, tool outputs) — machine-generated, causal, objective — not dialogue/chit-chat.
3. AMA-Bench = a **real-world subset** (6 domains, expert QA) + a **synthetic subset** (rule-based QA, any horizon length).
4. Four **question categories**: Temporal Information, State Dependency, Memory Updating, Memory Summarization.
5. The **finding**: even frontier models struggle (GPT-5.2 ≈ 72%); lossy compression + similarity-only retrieval miss causal/objective info.
6. **AMA-Agent**: causality-graph construction + tool-augmented retrieval → 57.22% (+11.16% over the best baseline).
7. **Big picture**: memory-system *design* is the bottleneck, not model size; ties to ENGRAM.

## Page table

| #  | Concept | Narrative purpose | Visual metaphor | Status |
|----|---------|-------------------|-----------------|--------|
| 01 | Long horizon | Setup: agents on a long task need memory | Engy setting out on a long winding road | rendered |
| 02 | Trajectories vs chit-chat | Real memory is a causal machine trajectory | Chatty bubble-world vs. road of machine-scrolls | rendered |
| 03 | Two subsets | Real-world (6 domains) + scalable synthetic | The Examiner's two stacks of question-cards | rendered |
| 04 | Four question types | What the benchmark measures | Four sealed cards: Temporal/State/Update/Summary | rendered |
| 05 | Why memory breaks | Similarity-only recall misses causal/objective info | Engy grabs a look-alike note and fails | rendered |
| 06 | AMA-Agent | Causality graph + tool-augmented retrieval wins | Notebook upgrades into a linked cause-effect graph | rendered |
| 07 | Big picture | Design is the bottleneck; ENGRAM tie-in | The road becomes ENGRAM's dated-state road | rendered |

**Total pages:** 7. Panel art lives in `panels/amabench_pageNN.png`. All 7 pages rendered.
