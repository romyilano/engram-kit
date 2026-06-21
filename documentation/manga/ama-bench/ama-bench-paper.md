# AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications

**Authors:** Yujie Zhao, Boqin Yuan, Junbo Huang, Haocheng Yuan, Zhongming Yu, Haozhou Xu, Lanxiang Hu, Abhilash Shankarampeta, Zimeng Huang, Wentao Ni, Yuandong Tian, Jishen Zhao
**arXiv:** 2602.22769v4
**Project:** https://ama-bench.github.io/

> This file holds the source abstract (verbatim) plus a plain-English summary so the
> `manga-pdf-generator` skill can append the source to the rendered manga PDF.

## Abstract (verbatim)

Large Language Models (LLMs) are increasingly used as autonomous agents in complex,
long-horizon applications, where effective memory is critical for sustained
performance. Yet existing memory benchmarks are largely dialogue-centric, while real
agent memory consists of continuous agent-environment interaction trajectories
composed of states, actions, observations, and tool outputs. To address this, we
introduce AMA-Bench (Agent Memory with Any length), a benchmark for evaluating
long-horizon memory in realistic agentic settings. It combines (i) real-world agent
trajectories from representative applications with expert-curated QA, and (ii)
synthetic trajectories that scale to arbitrary horizons with rule-based QA. Our study
shows that existing memory systems underperform because they fail to capture causal
and objective information and rely heavily on lossy similarity-based retrieval. We
further propose AMA-Agent, a memory system based on causality-graph construction and
tool-augmented retrieval. AMA-Agent achieves 57.22% accuracy on AMA-Bench,
outperforming the strongest baseline by 11.16%. Resources are available at:
https://ama-bench.github.io/.

## Plain-English summary

**The problem.** LLMs are now used as autonomous agents on long, multi-step tasks,
where **memory** is what sustains performance. But most memory benchmarks test
**dialogue** (conversation, chit-chat), whereas real agent memory is a **trajectory**:
a continuous record of **states, actions, observations, and tool outputs**. Those are
machine-generated (JSON, ASCII tables, code), **causally** linked (each action changes
the environment, which constrains later observations), and **objective** (dense facts,
no fluff). Dialogue benchmarks miss all three properties.

**The benchmark.** **AMA-Bench** ("Agent Memory with Any length") has two
complementary subsets:

- a **real-world subset** — expert-annotated, sanity-checked QA drawn from six agent
  domains: **Web, open-world QA, Text2SQL, software engineering, gaming, and embodied
  AI**; and
- a **synthetic subset** — automatically generated, rule-based QA in programmatic
  environments that **scales to arbitrary horizon lengths** while preserving the
  agent-environment interaction pattern.

It probes four question categories: **Temporal Information, State Dependency, Memory
Updating, and Memory Summarization.**

**The findings.**

- Agent memory is hard even for frontier models — **GPT-5.2 reaches only ~72.26%**.
- Existing agent-memory techniques often *beat* long-context baselines on
  dialogue-centric benchmarks but **fall short** on long-horizon agentic tasks.
- The bottleneck is **suboptimal memory-system design**, not base-model capability.
- **Lossy compression** and **similarity-based retrieval** fail because they discard
  or miss the **causal and objective** information the tasks need.

**Their system.** **AMA-Agent** builds a **causality graph** (actions → state
transitions → observations) and uses **tool-augmented retrieval**, reaching **57.22%**
accuracy — **+11.16%** over the strongest baseline.

## Why it pairs with ENGRAM

ENGRAM is a challenge for memory systems in evolving workspaces: ingest dated states
in order, write whatever memory you want, and answer **without hindsight** —
distinguishing **current / stale / superseded / uncertain** facts and citing evidence.
AMA-Bench is the evaluation-side mirror of that challenge: *how do you measure whether
agent memory is any good?* The companion book in this repo, ALMA (`../alma/`), is the
design-side mirror: *how is a good memory design even found?*
