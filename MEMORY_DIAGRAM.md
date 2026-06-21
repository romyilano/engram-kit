# How Context Engineering frames Memory

Source: Context Engineering (Manning MEAP v1, Boni Garcia) — Ch. 1 taxonomy and
section 1.5.4 Memory. Memory gets its own chapter (Ch. 5) and is one of six
context sources.

---

## 1. Where memory sits in the stack

Context engineering picks the smallest set of high-signal tokens that still lets
the model behave as intended. Memory is one input among six; a context manager
curates all six into the finite context window.

```mermaid
flowchart TB
    I[Instructions]
    K[External knowledge]
    T[Tools]
    M[Memory ch5]
    S[State ch5]
    U[User prompt]

    I --> MGMT
    K --> MGMT
    T --> MGMT
    M --> MGMT
    S --> MGMT
    U --> MGMT

    MGMT[Context management: select write compress isolate]
    MGMT --> WIN[LLM context window: finite tokens]
    WIN --> ORCH[Context orchestration: agentic reasoning]

    style M fill:#ffe2b8,stroke:#d98a00,stroke-width:2px
    style S fill:#fff4d6,stroke:#d9b800
```

Why memory exists: LLMs are stateless, so each API call is independent. Memory is
the technique that turns a series of stateless exchanges into a continuous,
stateful conversation.

---

## 2. The memory taxonomy itself (section 1.5.4)

```mermaid
flowchart TB
    MEM[Memory]
    MEM --> PAR[Parametric: baked into model weights]
    MEM --> NONPAR[Non-parametric: external, updatable at runtime]

    NONPAR --> ST[Short-term: conversational context in the window]
    NONPAR --> LT[Long-term: persists across sessions]

    LT --> EP[Episodic: past interactions]
    LT --> SEM[Semantic: stable facts and attributes]
    LT --> PRO[Procedural: routines and action patterns]

    EP --> EPS[stored as logs plus vector embeddings]
    SEM --> SEMS[stored as key-value or knowledge graphs]
    PRO --> PROS[stored as workflow defs or templates]

    style MEM fill:#ffe2b8,stroke:#d98a00,stroke-width:2px
    style LT fill:#fff4d6,stroke:#d9b800
```

At runtime, relevant fragments are retrieved from these external stores and
injected into the context window. The model stays stateless; the system appears
to remember.

---

## 3. The write / retrieve loop and how engram-kit maps onto it

Memory is two operations: write (persist what is worth keeping) and retrieve
(surface the relevant slice into context). This kit's two commands are exactly
those operations.

```mermaid
flowchart LR
    EVENT[New work: STATE_DIR snapshot] --> UPDATE[run.sh update]
    UPDATE --> STORE[Long-term memory: MEMORY_DIR]

    Q[Question JSON] --> RET[run.sh answer: retrieve memory]
    STORE --> RET
    RET --> LLM[LLM with injected context]
    LLM --> A[Answer JSON]

    style STORE fill:#ffe2b8,stroke:#d98a00,stroke-width:2px
```

| Book concept (1.5.4)       | engram-kit equivalent                          |
|----------------------------|------------------------------------------------|
| Write to long-term memory  | run.sh update STATE_DIR MEMORY_DIR             |
| Retrieve and inject        | run.sh answer with QUESTION_JSON ANSWER_JSON   |
| External store             | MEMORY_DIR                                      |
| Episodic source            | dated sample_states snapshots plus git log      |
| Evaluation harness         | check_submission.py and scoring                 |

---

Tip: GitHub, VS Code, and most Markdown viewers render the Mermaid blocks above
inline. For slides, paste a block into https://mermaid.live to export SVG or PNG.
