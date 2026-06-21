# Learning to Continually Learn via Meta-learning Agentic Memory Designs

**Authors:** Yiming Xiong, Shengran Hu, Jeff Clune
**Affiliations:** University of British Columbia · Vector Institute · CIFAR
**arXiv:** 2602.07755v1
**Code:** https://github.com/zksha/alma

> This file holds the source abstract (verbatim) plus a plain-English summary so the
> `manga-pdf-generator` skill can append the source to the rendered manga PDF.

## Abstract (verbatim)

The statelessness of foundation models bottlenecks agentic systems' ability to
continually learn, a core capability for long-horizon reasoning and adaptation. To
address this limitation, agentic systems commonly incorporate memory modules to
retain and reuse past experience, aiming for continual learning during test time.
However, most existing memory designs are human-crafted and fixed, which limits
their ability to adapt to the diversity and non-stationarity of real-world tasks. In
this paper, we introduce ALMA (Automated meta-Learning of Memory designs for Agentic
systems), a framework that meta-learns memory designs to replace hand-engineered
memory designs, therefore minimizing human effort and enabling agentic systems to be
continual learners across diverse domains. Our approach employs a Meta Agent that
searches over memory designs expressed as executable code in an open-ended manner,
theoretically allowing the discovery of arbitrary memory designs, including database
schemas as well as their retrieval and update mechanisms. Extensive experiments
across four sequential decision-making domains demonstrate that the learned memory
designs enable more effective and efficient learning from experience than
state-of-the-art human-crafted memory designs on all benchmarks. When developed and
deployed safely, ALMA represents a step toward self-improving AI systems that learn
to be adaptive, continual learners. All code is open-sourced at
https://github.com/zksha/alma.

## Plain-English summary

**The problem.** A foundation model on its own is *stateless* — it doesn't carry
anything from one task to the next. That makes it hard for an agent to *continually
learn*, which is what long-horizon reasoning and adaptation require.

**The usual fix and its limit.** Agents add a *memory module* to store and reuse past
experience. But the **design** of that memory — what it stores, how it retrieves, how
it updates — is almost always **hand-crafted and fixed**. A fixed design can't adapt
to the diversity and non-stationarity of real tasks.

**ALMA's idea.** Instead of hand-designing memory, **meta-learn the design itself**. A
**Meta Agent** searches over memory designs that are written as **executable code**, so
in principle it can discover *any* design — including the database schema and the
retrieval and update mechanisms. The search is **open-ended**:

1. **Sample** a previously explored design from an **archive** (which stores every
   design together with its evaluation log).
2. **Reflect** on that design's code and its results.
3. **Ideate & Plan** a modification.
4. **Implement** the new design in code.
5. **Verify** the code's correctness.
6. **Evaluate** it by running an agentic system on real tasks (success rate,
   trajectories).
7. **Store** the new design and its log back in the archive — then sample again.

**Results.** Across four sequential decision-making domains — **ALFWorld, TextWorld,
Baba Is AI, and MiniHack** — the learned memory designs consistently **beat
state-of-the-art human-crafted memory baselines**, and are **more cost-efficient** than
most of them.

**The big picture.** ALMA is framed as a step toward **self-improving AI** that learns
to be an adaptive, continual learner — explicitly qualified, *"when developed and
deployed safely."*

## Why it pairs with ENGRAM

ENGRAM is a challenge for memory systems in evolving workspaces: ingest dated states
over time, write whatever memory you want, and answer questions **without hindsight**.
ALMA is the design-side mirror of that challenge — it asks *how a good memory design is
even found*. The companion book in this repo, AMA-Bench (`../ama-bench/`), is the
evaluation-side mirror: *how you measure whether agent memory is any good*.
