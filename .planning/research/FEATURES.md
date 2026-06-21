# Feature Research — Content Coverage (Manga Explainer)

**Domain:** Educational manga that (A) explains the ENGRAM memory-system challenge from this repo and (B) recounts a factual history of memory in AI/agentic systems, 2020→present.
**Researched:** 2026-06-18
**Confidence:** Part A = HIGH (grounded line-by-line in repo source of truth). Part B = MEDIUM (drawn from model training knowledge through Jan 2026; live web/source verification was unavailable this run — see "Research Constraint & Verification Flags").

> **How to read this file.** "Features" here = **content beats**, each sized to roughly **one manga page**. Each beat lists what it must teach, why it matters, and a **Visualization Difficulty** rating so the prompt-writer can plan metaphors. Categories are **must-cover (core)**, **nice-to-have**, and **avoid / oversimplify-risk**.

---

## Research Constraint & Verification Flags

This run had **no access to live web search, WebFetch, or the gsd-tools research seam** (all denied/unavailable). Part A is fully verifiable against the repo files and is HIGH confidence. **Part B is reconstructed from training knowledge** and is internally consistent with well-known public history, but specific dates/paper attributions were **not re-verified against primary sources this session**. Each Part B claim carries a per-row confidence note. **Before these pages are rendered as fact in the manga, a human should spot-check the flagged dates and paper names** (one or two quick searches resolves all of them). Items most worth double-checking are marked **[VERIFY]**.

---

# PART A — ENGRAM Concepts to Teach (grounded in repo)

Every beat below is traceable to a repo file. The manga must match the kit **exactly** (commands, surfaces, rule wording). Source files: `CONTRACT.md`, `README.md`, `STATE_FORMAT.md`, `QUESTION_FORMAT.md`, `SUBMISSION_FORMAT.md`, `check_submission.py`, `examples/simple_memory/`.

## A. Must-Cover (Core) — one page each

| # | Page Beat | What it must teach (grounded) | Source | Visualization Difficulty |
|---|-----------|-------------------------------|--------|--------------------------|
| A1 | **The core idea** | ENGRAM is a small challenge for memory systems in *evolving workspaces*. A program receives **dated workspace states in chronological order**, keeps its own memory, and answers questions from **current state + that memory**. | `README.md:3-8`, `CONTRACT.md:55-65` | **MEDIUM** — "time-sequence of dated states feeding a memory" is the whole hook; metaphor needed (a stack of dated folders sliding past Engy day by day). |
| A2 | **Answering WITHOUT hindsight** | The system may **only see states released so far** — no future states. It must answer a question *as of* a reference time, not with knowledge it shouldn't have yet. This is the single hardest idea and the project's stated "must land" page. | `CONTRACT.md:46-48`, `PROJECT.md:11`, `QUESTION_FORMAT.md:8` | **HIGH** — "no hindsight" is abstract/temporal. Needs a strong metaphor (a blindfold over future folders; a calendar where tomorrow's pages are sealed). Flag for the prompt-writer. |
| A3 | **The two-command contract** | The whole interface is **two commands**: `./run.sh update STATE_DIR MEMORY_DIR` and `./run.sh answer STATE_DIR MEMORY_DIR QUESTION_JSON ANSWER_JSON`. Update = ingest a state into memory; Answer = read state + memory + question, write an answer. Both exit `0`/nonzero on fail. | `CONTRACT.md:5-8,14-42`, `README.md:9-15` | **LOW–MEDIUM** — two clearly labeled "buttons/levers" on Engy. Easy to draw as two distinct actions. |
| A4 | **The four surfaces** | Define the four arguments as physical things: **STATE_DIR** = current bounded workspace state (read-only input); **MEMORY_DIR** = the system's *own persistent writable memory* (the only durable benchmark-visible memory); **QUESTION_JSON** = the question file; **ANSWER_JSON** = the file the system must write. | `CONTRACT.md:10-12,51`, `ARCHITECTURE.md:89-95` | **MEDIUM** — four labeled objects. Mascot design already maps MEMORY_DIR → Engy's notebook chest; reuse that. STATE_DIR vs MEMORY_DIR distinction must be visually unmistakable. |
| A5 | **What's inside a STATE_DIR** | Each state is a **full bounded workspace state for one date, not just a diff**. Contains `files/`, `manifest.tsv`, `git_log.txt`, `changes.txt`, `state_meta.json`, `README.md`. `files/` = the visible workspace; `manifest.tsv` = file inventory (evidence, *not* an answer key); `changes.txt` = human summary since last state. | `STATE_FORMAT.md:1-66` | **MEDIUM** — drawable as the contents of one dated folder, fanned out and labeled. |
| A6 | **Update phase** | During `update`, the program reads STATE_DIR and writes whatever it wants under MEMORY_DIR — SQLite, vector indexes, Markdown notes, JSONL logs, graph stores, summaries. Exit 0 on success. (Reference example appends one JSON record per update to `memory.jsonl`.) | `CONTRACT.md:14-29`, `simple_memory.py:35-46` | **LOW–MEDIUM** — Engy reading today's folder and writing a note into the notebook. |
| A7 | **Answer phase + answer JSON shape** | During `answer`, read STATE_DIR + MEMORY_DIR + QUESTION_JSON, then **write ANSWER_JSON** with required fields: `answer` (string), `evidence_paths` (list), `uncertainty` (string); optional `memory_refs` (list). | `CONTRACT.md:31-42`, `QUESTION_FORMAT.md:24-49` | **MEDIUM** — show the answer "card" being filled out with labeled slots. |
| A8 | **Cite evidence — and don't blur the two surfaces** | Answers must **cite evidence**. `evidence_paths` point into the current **STATE_DIR** (workspace evidence); `memory_refs` point into the system's own **MEMORY_DIR** (self-created memory). The contract explicitly forbids blurring these two surfaces. `manifest.tsv`/`git_log.txt` are *evidence, not an oracle*. | `QUESTION_FORMAT.md:38-48`, `STATE_FORMAT.md:42,54`, `CONTRACT.md:62-64` | **MEDIUM–HIGH** — "two kinds of citations from two different sources" is subtle. Use color-coding (state = one color, memory = another). |
| A9 | **Current vs stale vs superseded vs uncertain** | The core skill ENGRAM measures: distinguish **current**, **stale**, **superseded/rejected**, and **uncertain** information across changing states. If the state doesn't support a confident answer, say so plainly ("Cannot determine from the released state") and fill `uncertainty`. | `CONTRACT.md:62-65`, `README.md:82`, `QUESTION_FORMAT.md:51-61` | **HIGH** — four overlapping info-states are abstract. Metaphor needed (sticky notes that fade=stale, get crossed-out=superseded, marked "?"=uncertain, glow=current). Flag for prompt-writer. |
| A10 | **How to compete: the submission** | Submit **one folder** with `README.md`, required `run.sh`, optional `requirements.txt`/`src/`. `run.sh` is the only required entrypoint; it accepts both commands, exits nonzero on failure, writes ANSWER_JSON, and **runs with no manual steps**. README must declare any model/network/daemon/DB/external service. | `SUBMISSION_FORMAT.md:1-46`, `CONTRACT.md:52-53` | **LOW** — a labeled folder; easy to draw. |
| A11 | **How validation works: check_submission.py** | The local checker **replays sample states in chronological order** calling `update`, then asks one sample question, resolves its `reference_time` to a state dir, calls `answer`, and **validates ANSWER_JSON shape**. Passing only proves you *speak the interface* — it is **not benchmark evidence** and does not predict private-eval score. | `check_submission.py:64-123`, `README.md:68`, `SUBMISSION_FORMAT.md:49-57` | **MEDIUM** — a conveyor of dated folders feeding Engy, then a checkmark on the answer card's *shape* (not its truth). The "passing ≠ scoring" caveat is important and easy to misdraw. |

## A. Nice-to-Have (Part A)

| Beat | What it adds | Source | Viz Difficulty |
|------|-------------|--------|----------------|
| **Boundary rules montage** | One page enumerating what you *don't* get: no future states, no private eval data, no judge packets/answer keys/rubrics/reference sets, no other candidates' memory; MEMORY_DIR is the only durable memory. | `CONTRACT.md:44-53` | MEDIUM — "locked doors" gallery. |
| **Backend-agnostic page** | ENGRAM is *not* testing a particular backend — graph, vector, Markdown, SQLite, agent loop, wrapped OSS, or custom pipeline all qualify. (Reference impl literally answers this.) | `README.md:72-83`, `simple_memory.py:58-66` | LOW — a shelf of interchangeable backend "cartridges". |
| **Failure-answer page** | Showing the honest "Cannot determine from the released state" answer as a *valid, good* answer, not a loss. Reinforces A9. | `QUESTION_FORMAT.md:51-61` | LOW–MEDIUM. |
| **Where to go (CTA)** | Public repo, zip download, Discord submission channel. | `README.md:20-36` | LOW — a signpost panel. |

## A. Avoid / Oversimplify-Risk (Part A)

| Risk | Why it's a trap | Guidance |
|------|-----------------|----------|
| **Implying check_submission.py = the benchmark/score** | The repo says passing the checker is *not* benchmark evidence and does not predict score. Drawing a "you passed → you win" panel is factually wrong. | Show the checker validating *shape only*; keep scoring off-page. |
| **Drawing STATE_DIR as editable by the system** | STATE_DIR is read input; **MEMORY_DIR** is the writable surface. Conflating them breaks the central mental model. | Make STATE read-only (e.g. sealed/stamped) and MEMORY the only place Engy writes. |
| **Treating manifest.tsv / git_log.txt as truth** | The repo explicitly calls them evidence, not an oracle; git subjects "are not guaranteed to be truth." | If shown, label them "evidence, not answer key." |
| **Inventing ENGRAM internals** | The kit is a *public facade*; it deliberately excludes private eval data, QEMU details, dashboard/atlas/tracks internals, rubrics. | Do not depict private scoring machinery — out of scope and not in source. |
| **Over-specifying memory format as "the right one"** | Backend is open by design. Picking one and presenting it as required misleads. | Keep memory format illustrative/plural. |
| **Showing a story/plot arc** | PROJECT scope = narrated explainer panels, not a character-driven plot. | Keep beats expository. |

---

# PART B — History of Memory in AI / Agentic Systems, 2020→present

**Verification posture:** dates and paper attributions below are from training knowledge (cutoff Jan 2026) and are widely documented in public sources, but were **not re-fetched this session**. Treat **[VERIFY]** rows as "human spot-check before printing." The *narrative shape* (why memory mattered more over time) is robust; exact months/version numbers are the parts most worth confirming.

## B. Must-Cover (Core) — the through-line that motivates ENGRAM

The spine of the history: **LLMs are stateless per call, so "memory" has been bolted on in escalating layers — retrieval, bigger context, then explicit persistent/agent memory — and ENGRAM is a benchmark for that last layer.** Each beat ≈ one page.

| # | Beat | What it teaches & rough date | Why it mattered | Confidence | Viz Difficulty |
|---|------|------------------------------|-----------------|-----------|----------------|
| B1 | **The stateless-LLM problem** | A language model, by itself, remembers nothing between calls — each prompt starts blank. Everything that follows is humanity bolting memory onto a forgetful engine. (Framing, not a dated event.) | Sets up *why memory is a field at all*; directly motivates ENGRAM. | HIGH (conceptual) | MEDIUM — "goldfish with a genius brain" metaphor. |
| B2 | **Retrieval-Augmented Generation (RAG)** | **2020** — RAG (Lewis et al., Facebook AI / "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks", arXiv 2005.11401) couples a retriever over an external document store with a generator, so the model pulls in outside knowledge at answer time instead of relying only on weights. | Established the dominant pattern: *don't memorize everything in weights — fetch relevant context on demand.* The conceptual ancestor of "look it up in memory." | MEDIUM **[VERIFY]** (2020, arXiv 2005.11401, Lewis et al.) | MEDIUM — librarian fetching a book, then speaking. |
| B3 | **Embeddings + vector databases** | **~2021–2023 mainstream wave** — text embeddings turn documents into vectors; **vector databases / indexes** (e.g. FAISS earlier; Pinecone, Weaviate, Chroma, Milvus; pgvector) store them for similarity search. This made RAG practical at scale. | Gave RAG its storage layer — "semantic memory you can search by meaning, not keywords." This is the literal substrate many ENGRAM submissions can use. | MEDIUM **[VERIFY]** (FAISS ~2017; the *product* wave of vector DBs surged 2022–2023 with the LLM boom) | MEDIUM — points of light in space, nearest-neighbor lookup. |
| B4 | **The ChatGPT inflection & RAG-everywhere** | **late 2022 → 2023** — ChatGPT's release drove mass adoption; "chat with your docs" RAG apps and frameworks (**LangChain**, then **LlamaIndex / GPT-Index**) exploded, standardizing retrieval pipelines. | Turned memory-via-retrieval from research into the default app architecture; created the tooling ENGRAM participants now reach for. | MEDIUM **[VERIFY]** (LangChain & LlamaIndex both emerged ~late 2022; ChatGPT Nov 2022) | LOW–MEDIUM — a toolbox suddenly everyone owns. |
| B5 | **Long-context windows grow** | **2023→2025** — context windows expanded fast: ~4K–8K (GPT-3.5 era) → 32K → **100K (Anthropic Claude, 2023)** → million-token contexts (Google **Gemini 1.5**, 2024) and large windows across frontier models. | Raised the question "*do we even need external memory if the window is huge?*" — answer: long context helps but is costly, lossy ("lost in the middle"), and non-persistent, so it complements rather than replaces memory. | MEDIUM **[VERIFY]** (Claude 100K = 2023; Gemini 1.5 1M = 2024; exact figures move fast) | MEDIUM — an expanding window/scroll; show it's *temporary*, not saved. |
| B6 | **External / persistent agent memory frameworks** | **2023→present** — explicit memory systems beyond retrieval: **MemGPT** (UC Berkeley, "LLM as Operating System," arXiv 2310.08560, Oct 2023; later the **Letta** project/company) introduced OS-style memory management — a small in-context "working memory" plus paged external memory the agent reads/writes itself. Companion ecosystem grew (e.g. **Cognee**, **Letta**, **Supermemory**, memory features in agent frameworks). | This is the layer ENGRAM directly measures: *systems that persist and manage their own memory over time.* The repo's own example even name-drops Letta/Cognee/Supermemory as strategies. | MEDIUM **[VERIFY]** (MemGPT arXiv 2310.08560, Oct 2023; Letta = its successor project) | HIGH — "memory as OS paging" is abstract; needs a desk (working memory) + filing cabinet (long-term) the agent shelves things into. |
| B7 | **Tool use & scratchpad/working memory** | **2022→present** — patterns like **ReAct** (reason+act, arXiv 2210.03629, 2022) and scratchpad/chain-of-thought gave agents a *transient* working memory: notes, tool outputs, and intermediate reasoning held during a task. Tool/function calling let agents offload state to external systems. | Distinguishes *short-lived working memory* (a task scratchpad) from *durable memory* (persists across tasks) — a distinction ENGRAM's update/answer split mirrors. | MEDIUM **[VERIFY]** (ReAct arXiv 2210.03629, 2022) | MEDIUM — a whiteboard wiped after each task vs. a notebook that's kept. |
| B8 | **Episodic vs semantic memory in agents** | **2023→present** — agent designs borrowed cognitive-science terms: **semantic memory** (facts/knowledge) vs **episodic memory** (specific past events/interactions, "what happened on which day"), sometimes plus procedural memory. Popularized by agent-simulation work (e.g. the **Generative Agents** "Stanford/Google smallville" paper, arXiv 2304.03442, 2023, with its memory stream + reflection + retrieval). | Gives the vocabulary for *time-aware* memory — exactly ENGRAM's territory, where "what was true on 2026-04-09" (episodic/temporal) matters. | MEDIUM **[VERIFY]** (Generative Agents arXiv 2304.03442, 2023) | MEDIUM–HIGH — two labeled memory shelves (facts vs dated events). |
| B9 | **The move to persistent agentic memory → why benchmarks like ENGRAM** | **2024→2025→present** — as agents run continuously over evolving workspaces, the open problem became *managing memory correctly over time*: keeping current info, retiring stale/superseded info, expressing uncertainty, and citing sources — not just retrieving more. Evaluation lagged capability, motivating dedicated **memory benchmarks**. ENGRAM sits here: it scores whether a system ingests changing states, preserves useful memory, distinguishes current/stale/rejected/uncertain, cites evidence, and answers without hindsight. | Closes the loop: the manga's history *arrives at* ENGRAM as the natural next step. | HIGH (framing) / MEDIUM on "benchmark landscape" specifics **[VERIFY]** | MEDIUM — timeline arrow landing on the Engy mascot. |

## B. Nice-to-Have (Part B)

| Beat | What it adds | Confidence | Viz Difficulty |
|------|-------------|-----------|----------------|
| **Pre-2020 ancestry (one panel)** | Memory networks / Neural Turing Machines / DNC (2014–2016), and RNN/LSTM "hidden state" memory — the deep-learning roots before transformers. | MEDIUM **[VERIFY]** (NTM 2014, DNC 2016, both DeepMind) | MEDIUM. |
| **GraphRAG / structured memory** | **2024** — Microsoft **GraphRAG** and knowledge-graph memory: organizing memory as entities+relations for better multi-hop and global questions. | LOW–MEDIUM **[VERIFY]** (Microsoft GraphRAG, 2024) | MEDIUM — a constellation/graph. |
| **Retrieval limitations panel** | "Lost in the middle" and retrieval-quality issues — why bigger context and naive RAG aren't a silver bullet. | MEDIUM **[VERIFY]** ("Lost in the Middle," Liu et al., 2023) | LOW. |
| **Hosted memory products** | Mem0, Zep, Supermemory, OpenAI/assistant "memory" features (2024–2025) — memory as a product, not just a paper. | LOW **[VERIFY]** (fast-moving commercial space) | LOW. |

## B. Avoid / Oversimplify-Risk (Part B)

| Risk | Why it's a trap | Guidance |
|------|-----------------|----------|
| **Precise dates/version numbers as gospel** | Context-window sizes and product launches move monthly; a wrong "X launched in month Y" is the most likely factual error in the whole manga. | Prefer "around 2023," "by 2024" phrasing on slides; only commit to a month after [VERIFY]. |
| **"Long context replaced RAG/memory"** | A common oversimplification; in reality they coexist and trade off (cost, recall, persistence). | Present long context as *complementary and non-persistent*, not a winner. |
| **"Embeddings = memory"** | Vectors are a *storage/retrieval substrate*; memory is the broader discipline of keeping/updating/retiring knowledge over time. | Keep B3 as "the storage layer," not "the answer." |
| **Anthropomorphizing episodic/semantic memory too literally** | The brain analogy is borrowed loosely; claiming agents have human-equivalent memory is misleading. | Use the terms as *labels for shelves*, with a "borrowed from cognitive science" caveat. |
| **Deep technical detail (attention math, ANN index internals, OS paging mechanics)** | Too deep for a non-expert explainer; kills the "click." | Stay at the metaphor level; one page per concept, no equations. |
| **Naming specific products as winners/endorsements** | Commercial landscape shifts and the repo is backend-agnostic. | Mention products as *examples of a pattern*, never as required or "best." |
| **Hallucinated paper titles/authors** | The biggest credibility risk for an explainer that cites history. | Only state author/arXiv-ID where [VERIFY] has confirmed it; otherwise describe the concept without false precision. |

---

## Content Dependencies (page ordering)

```
A1 core idea
   └─> A2 no-hindsight        (the payoff of A1; "must land")
A3 two commands
   └─> A4 four surfaces
          ├─> A5 inside STATE_DIR
          ├─> A6 update phase
          └─> A7 answer phase + answer JSON
                 └─> A8 cite evidence (state vs memory)
                        └─> A9 current/stale/superseded/uncertain   (peak difficulty)
A10 submission ──> A11 check_submission.py  (validation; "passing ≠ scoring")

History (Part B) is a SELF-CONTAINED arc that can sit BEFORE Part A
(as motivation) or AFTER (as context):
   B1 stateless ──> B2 RAG ──> B3 vectors ──> B4 ChatGPT/tooling
        ──> B5 long context ──> B6 persistent/agent memory (MemGPT/Letta)
        ──> B7 scratchpad vs durable ──> B8 episodic/semantic
        ──> B9 "why ENGRAM" (bridge into Part A)
```

**Recommended placement:** B1→B9 as the **opening arc** (sets up *why memory is hard*), landing B9 directly into A1. This makes ENGRAM feel inevitable rather than arbitrary. Alternatively, B can be a back-half "where this comes from" section if the author wants ENGRAM mechanics first.

## Page-Count Sanity Check (target 15+)

Core only: A1–A11 (11) + B1–B9 (9) = **20 pages**, already past the 15+ floor. With a title/cover page and the B9→A1 bridge, ~22. Nice-to-haves are the trimming buffer; **A2, A9, B6 are the non-negotiable "must land" pages** and should get the most care.

## Hardest-to-Visualize Beats (hand these to the prompt-writer first)

1. **A2 — answering without hindsight** (temporal/negative concept). Metaphor candidate: sealed future folders / a calendar with tomorrow blacked out.
2. **A9 — current vs stale vs superseded vs uncertain** (four overlapping info-states). Metaphor candidate: sticky notes that glow / fade / get crossed-out / wear a "?".
3. **B6 — OS-style paged agent memory (MemGPT/Letta)**. Metaphor candidate: desk (working memory) + filing cabinet (long-term) the robot shelves between.
4. **A8 — two citation surfaces (state vs memory)**. Metaphor candidate: strict color-coding, two-colored citation ribbons.
5. **B8 — episodic vs semantic shelves**. Metaphor candidate: a "facts" shelf vs a dated "diary" shelf.

## Sources

**Part A (HIGH — primary, in-repo):** `CONTRACT.md`, `README.md`, `STATE_FORMAT.md`, `QUESTION_FORMAT.md`, `SUBMISSION_FORMAT.md`, `check_submission.py`, `examples/simple_memory/simple_memory.py`, `.planning/codebase/ARCHITECTURE.md`, `.planning/PROJECT.md`.

**Part B (MEDIUM — model training knowledge, cutoff Jan 2026; NOT re-verified online this run):** Well-known public references behind each beat — RAG (Lewis et al. 2020, arXiv 2005.11401); ReAct (Yao et al. 2022, arXiv 2210.03629); Generative Agents (Park et al. 2023, arXiv 2304.03442); MemGPT (Packer et al. 2023, arXiv 2310.08560) and the Letta project; vector-DB ecosystem (FAISS, Pinecone, Weaviate, Chroma, Milvus, pgvector); LangChain / LlamaIndex; long-context milestones (Claude 100K 2023, Gemini 1.5 ~1M 2024); GraphRAG (Microsoft 2024); "Lost in the Middle" (Liu et al. 2023). **All arXiv IDs, authors, and dates above are marked [VERIFY] and should be confirmed with one search each before the history pages are treated as authoritative.**

---
*Content-coverage research for: ENGRAM manga explainer (Part A grounded in repo; Part B = AI-memory history 2020→present)*
*Researched: 2026-06-18*
