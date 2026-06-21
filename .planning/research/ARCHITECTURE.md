# Architecture Research — Explainer Structure & Visual Language

**Domain:** Technical explainer manga (narrated diagram-style, non-plot) teaching ENGRAM + a history of AI memory
**Researched:** 2026-06-18
**Confidence:** MEDIUM (structure/pedagogy/visual-language reasoning is HIGH and grounded in the repo + established explainer-comic craft; the AI-memory history timeline is MEDIUM and flagged for a fact-check pass — web research tools were unavailable in this run)

> "Architecture" here = the **narrative skeleton + visual design language** of the comic, not software components. The downstream consumer is the roadmap, which turns each page below into a GSD spike (one ChatGPT image prompt per page).

---

## Standard Architecture

### The Explainer Arc (the "system overview")

A non-expert needs understanding to **accrue**, not arrive. The proven shape for technical explainers is a one-directional staircase: each rung only assumes the rungs below it. ENGRAM maps cleanly onto a 7-beat arc.

```
┌──────────────────────────────────────────────────────────────────────┐
│  ACT I — WHY CARE          (emotional + intuitive buy-in)             │
│  ┌─────────┐   ┌─────────┐                                            │
│  │  HOOK   │ → │INTUITION│   "memory is hard" → "here's the picture"  │
│  └─────────┘   └─────────┘                                            │
├──────────────────────────────────────────────────────────────────────┤
│  ACT II — HOW IT WORKS     (the machine, made physical)              │
│  ┌─────────┐   ┌─────────┐   ┌─────────┐                              │
│  │MECHANICS│ → │  RULES  │ → │ HOW-TO  │  the 2 commands → the laws   │
│  └─────────┘   └─────────┘   └─────────┘     → how to compete         │
├──────────────────────────────────────────────────────────────────────┤
│  ACT III — ZOOM OUT        (place it in the world + lock it in)      │
│  ┌─────────┐   ┌─────────┐                                            │
│  │ HISTORY │ → │  RECAP  │   2020→now lineage → "the idea in 1 panel" │
│  └─────────┘   └─────────┘                                            │
└──────────────────────────────────────────────────────────────────────┘
        │            │            │            │            │
   Engy alone   Engy + room   Engy + sensei  sensei leads  Engy waves
```

**Why this order (dependency chain):**

1. **Hook before intuition** — a reader who does not yet feel the problem will not invest in the metaphor.
2. **Intuition before mechanics** — the two commands (`update`/`answer`) only make sense once "a memory that ingests states over time" is already a picture in the reader's head.
3. **Mechanics before rules** — "no future states / no answer keys / cite evidence" are *constraints on a thing*; you must know the thing first.
4. **Rules before how-to** — what a participant builds is shaped by the rules, so the rules gate the build page.
5. **How-to before history** — history is the "victory lap"; it rewards a reader who now understands the mechanics by showing them where this idea came from. Putting history early would front-load jargon (RAG, vector DBs) onto a reader with no scaffold.
6. **Recap last** — the single-panel restatement is only powerful as a *callback* to motifs already established.

### Component Responsibilities (the recurring cast = your "components")

| Component | Responsibility | Typical Implementation |
|-----------|----------------|------------------------|
| **Engy** (mascot) | Embodies the *memory system under test*. Her glowing-notebook chest **is** `MEMORY_DIR`. She reacts, struggles, succeeds — the reader feels the mechanics through her. | Round librarian-robot, 4–5 fixed visual tokens (see Mascot section). Appears on ~every page. |
| **Narrator-sensei** | Explains, points, frames the "rule in one panel." Voice of authority; never the subject of the lesson. | Calm older figure with a pointer/scroll. Appears when a *rule or definition* is stated. |
| **The Workspace Room** (`STATE_DIR`) | The dated, bounded world Engy reads each tick. Physicalizes "a full state, not a diff." | A room/shelf with a date placard; re-dressed each state. |
| **The Letter / Quest** (`QUESTION`) | The question arriving. Gives the reader something to root for. | A sealed envelope or quest scroll Engy receives. |
| **The Verdict Card** (`ANSWER`) | Engy's written answer with evidence tags. Closes each mini-loop. | An index card with answer + clipped citation tags + an "uncertainty" sticky note. |

---

## Recommended Page Structure (the page-by-page skeleton)

**Target: 18 pages** (meets the 15+ requirement with 3 pages of headroom the roadmap can cut to 15 if needed — cut candidates marked `[CUT-OK]`). One *idea* per page. Each page is multi-panel but carries a single takeaway.

```
PAGE 01  COVER / HOOK
PAGE 02  THE PROBLEM (intuition: why memory is hard)
PAGE 03  MEET ENGY (the memory system, made physical)        ← motif setup
PAGE 04  THE WORKSPACE ROOM (STATE_DIR explained)            ← motif setup
PAGE 05  TIME MOVES FORWARD (the tick / sequence of states)
PAGE 06  COMMAND ONE: UPDATE
PAGE 07  COMMAND TWO: ANSWER
PAGE 08  THE TWO COMMANDS TOGETHER (the contract, one panel)  ← payload page
PAGE 09  RULE — NO FUTURE STATES (locked door to tomorrow)
PAGE 10  RULE — NO ANSWER KEYS (no peeking / sealed vault)
PAGE 11  RULE — CITE YOUR EVIDENCE (citation tags)
PAGE 12  RULE — CURRENT vs STALE vs SUPERSEDED vs UNCERTAIN   ← hardest idea
PAGE 13  HOW TO COMPETE (the submission folder + run.sh)
PAGE 14  THE CHECKER (check_submission.py proves the handshake)  [CUT-OK]
PAGE 15  HISTORY I — 2020–2022 (RAG & vector memory)         ← victory lap
PAGE 16  HISTORY II — 2023–2024 (long context + agent memory)
PAGE 17  HISTORY III — 2025→now (where ENGRAM sits)          [CUT-OK]
PAGE 18  RECAP — THE WHOLE IDEA IN ONE PANEL                 ← callback payoff
```

### Page-by-page detail

| # | Page | Single takeaway | Key panels / beats | Cast | Motifs introduced/recalled |
|---|------|-----------------|--------------------|------|----------------------------|
| 01 | **Cover / Hook** | "This is about a robot who must remember." | Title; Engy mid-stride hugging her glowing notebook; soft-color splash. | Engy | NOTEBOOK-CHEST |
| 02 | **The Problem** | A worker who forgets yesterday can't answer today. | Before/after: Engy *without* a notebook stares blankly at a question; thought-bubble of yesterday fading. | Engy | FADING-MEMORY (stale grey) |
| 03 | **Meet Engy** | The memory system is Engy; her notebook is its memory. | Label-callout pointing to the glowing chest = `MEMORY_DIR`; she can write in it. | Engy + sensei | NOTEBOOK-CHEST = MEMORY_DIR |
| 04 | **The Workspace Room** | Each day she's handed a full room to read — not a diff. | Engy steps into a dated room: shelves, files, a manifest clipboard, a git-log scroll. Placard: `2026-04-09`. | Engy | ROOM = STATE_DIR; DATE-PLACARD; MANIFEST-CLIPBOARD |
| 05 | **Time Moves Forward** | States arrive in order; the room changes each tick. | A film-strip / calendar of rooms left→right; today is lit, future rooms are dark. | Engy | TIMELINE-STRIP; DARK-FUTURE |
| 06 | **Command One: `update`** | She reads the room and writes into her notebook. | Engy reads room → glowing arrow into notebook; small `update STATE_DIR MEMORY_DIR` ribbon. | Engy | UPDATE-ARROW (room→notebook) |
| 07 | **Command Two: `answer`** | A letter arrives; she answers from room + notebook. | Envelope (question) → Engy consults room AND notebook → writes a verdict card. | Engy | LETTER = QUESTION; VERDICT-CARD = ANSWER |
| 08 | **The Two Commands Together** ★ | The whole contract on one page. | Two-panel diptych: left = UPDATE loop, right = ANSWER loop; the command ribbons beneath. "Just these two." | Engy + sensei | UPDATE-ARROW + LETTER/VERDICT recalled |
| 09 | **Rule: No Future States** | You can never read tomorrow. | A locked door labelled "TOMORROW"; Engy's hand stopped; key not given. | Engy + sensei | LOCKED-DOOR-TO-TOMORROW |
| 10 | **Rule: No Answer Keys** | No rubrics, no reference answers, no peeking. | A sealed vault marked "JUDGE" behind glass; Engy can't open it; sensei wags finger. | Engy + sensei | SEALED-JUDGE-VAULT |
| 11 | **Rule: Cite Your Evidence** | Every answer must point at the file that proves it. | Verdict card with string/tags running back to specific files on the shelf (`evidence_paths`). | Engy | CITATION-TAGS (string-to-file) |
| 12 | **Rule: Current vs Stale vs Superseded vs Uncertain** ★ | Not all info is equally true; label it. | 4-quadrant panel: ✅ current (bright), 🌫️ stale (greyed), ✗ superseded (crossed-out & replaced), ❓ uncertain (sticky-note). | Engy + sensei | COLOR-STATE-CODING |
| 13 | **How to Compete** | You build a folder with a `run.sh` speaking the two commands. | A submission folder opened like a lunchbox: `README.md`, `run.sh`, `src/`; run.sh as a "mouth" speaking update/answer. | Engy | SUBMISSION-BOX |
| 14 | **The Checker** `[CUT-OK]` | `check_submission.py` only proves the handshake, not the score. | A friendly gate-guard stamps "speaks the interface ✓" but holds up a "not a score" sign. | sensei | HANDSHAKE-STAMP |
| 15 | **History I (2020–2022)** | Before agent memory: RAG + vector stores. | Sensei unrolls a timeline scroll; mini-Engy ancestors: a "retrieval librarian" fetching documents into a prompt. | sensei + Engy | TIMELINE-SCROLL |
| 16 | **History II (2023–2024)** | Long context + explicit agent memory (MemGPT/Letta). | Scroll continues: a giant context "window" pane; a robot with an external memory ledger paging things in/out. | sensei + Engy | recalls NOTEBOOK-CHEST |
| 17 | **History III (2025→now)** `[CUT-OK]` | ENGRAM tests memory *over time, without hindsight*. | Scroll arrives at "today"; Engy steps onto the timeline; the locked-door motif reappears as the new frontier. | Engy + sensei | recalls LOCKED-DOOR |
| 18 | **Recap — One Panel** ★ | The whole idea, callable from memory. | Single hero panel: dated rooms streaming in → Engy (notebook glowing) → verdict card with citation tags → locked future door. One caption line. | Engy | ALL motifs recalled |

★ = "payload" page; if anything is cut, these three (08, 12, 18) plus 03–07 must survive — they are the Core Value defined in PROJECT.md.

### Structure rationale

- **Pages 03–07 are the spine.** They establish every reusable motif *before* any rule depends on it. The roadmap should treat these as a single non-splittable phase.
- **Rules (09–12) are parallel-safe** once the spine exists — they share no dependencies on each other and can be prompt-authored in any order. Page 12 is the hardest concept and should get extra prompt-iteration budget.
- **History (15–17) depends only on the sensei + timeline-scroll motif**, not on the rules. It can be authored independently and even in parallel with the rules — but **content-wise it must be fact-checked** (see Anti-Patterns / Pitfalls flag).
- **Recap (18) depends on everything** — it must be authored last because it is a callback collage of established motifs.

---

## The Visual Design Language (the reusable motif system)

This is the single most reused asset. Because each page is a *fresh ChatGPT generation*, every motif below must be (a) describable in one short clause and (b) restated in every prompt that uses it. Drift between pages is the #1 quality risk (per PROJECT.md constraints).

### Master motif table — concept → consistent depiction

| ENGRAM concept | Visual motif | One-clause prompt phrasing (reusable) | Notes |
|----------------|--------------|----------------------------------------|-------|
| `MEMORY_DIR` (persistent memory) | **Engy's glowing notebook chest** | "a softly glowing open notebook set into the robot's chest" | The anchor motif. Glow = memory is alive/active. |
| `STATE_DIR` (one dated state) | **A dated workspace room / shelf** | "a cozy archive room with a date placard on the wall reading <DATE>" | Always a *full* room, never a fragment — reinforces "not a diff." |
| Sequence of states / ticks | **A left-to-right strip of rooms (or calendar/film-strip)** | "a horizontal film-strip of dated rooms, earlier rooms on the left, today lit, future rooms dark" | Direction = time. |
| `manifest.tsv` | **A clipboard inventory** | "a clipboard listing files with little checkmarks" | The file inventory Engy carries. |
| `git_log.txt` | **A hanging scroll of commit notes** | "a short hanging scroll of dated note-cards (history, treated as clues not truth)" | Visually tentative (clues, not oracle). |
| `QUESTION` (`question.json`) | **A sealed letter / quest envelope** | "a sealed envelope with a question mark wax seal, delivered to Engy" | Arrival = a quest begins. |
| `ANSWER` (`answer.json`) | **A written verdict / index card** | "an index card where Engy writes her answer" | Closes the loop. |
| `evidence_paths` (citations) | **Strings/tags from the card back to specific shelf files** | "thin strings tying the answer card to the exact files on the shelf that prove it" | Makes "cite evidence" literal. |
| `uncertainty` field | **A small sticky-note on the verdict card** | "a small yellow sticky-note clipped to the card noting what's still unclear" | Honesty is visible, not hidden. |
| `update` command | **An arrow from room → notebook** | "a glowing arrow flowing from the room into Engy's notebook chest" | Reading-into-memory. |
| `answer` command | **Notebook + room → verdict card** | "two glowing arrows, from room and from notebook, meeting at the answer card" | Both surfaces feed the answer. |
| **No future states** | **A locked door labelled TOMORROW** | "a heavy locked door marked 'TOMORROW', no key, Engy's hand stopped before it" | The headline rule motif. |
| **No answer keys / private eval** | **A sealed JUDGE vault behind glass** | "a sealed vault marked 'JUDGE' behind frosted glass, unreachable" | Distinct from the door (door = time; vault = secrecy). |
| **Current info** | **Bright, full-color, ✅** | "rendered bright and crisp with a green check" | |
| **Stale info** | **Greyed / desaturated, faded edges, 🌫️** | "drawn faded and grey, edges dissolving" | The fading-memory look from page 02. |
| **Superseded / rejected info** | **Crossed-out and visibly replaced, ✗→new** | "an old card crossed out with a red X, a new card placed over it" | Replacement, not just deletion. |
| **Uncertain info** | **A wobbly question-mark sticky, ❓** | "a wobbly yellow note with a question mark" | Ties to the `uncertainty` field. |
| `run.sh` / submission folder | **An open lunchbox-style folder; run.sh as a speaking mouth** | "an open folder like a lunchbox holding README, run.sh, and src; run.sh shaped like a small mouth saying 'update / answer'" | The two commands literally come out of run.sh. |
| `check_submission.py` | **A gate-guard who stamps "speaks the interface"** | "a friendly gate-guard stamping a passport 'SPEAKS THE INTERFACE', holding a sign 'not a score'" | Encodes the README caveat. |

### Color-state coding (use everywhere, not just page 12)

A single palette rule the prompt-writer reuses on **every** page that shows information:

```
CURRENT      → bright, saturated, sharp outline      (✅)
STALE        → desaturated grey, soft/dissolving edge (🌫️)
SUPERSEDED   → red strike-through, replacement on top (✗→)
UNCERTAIN    → yellow sticky, wobbly outline          (❓)
```

This is the comic's "syntax highlighting." Once the reader learns it on page 12, it pays off silently on every later page (especially recap).

### Style block (pin once, restate every prompt)

Per PROJECT.md, a fixed style block must be re-stated in *every* page prompt to fight cross-generation drift:

> "Soft-color manga / light watercolor anime style. Gentle pastel palette (warm cream paper, soft teal + peach accents). Clean rounded line art, friendly and approachable, picture-book-meets-manga. Multi-panel explainer page layout with clear reading order, generous white space, hand-lettered-style captions. No harsh shadows, no photorealism."

The roadmap should store this block + the mascot block as a **shared header** that every spike's prompt copies verbatim.

---

## Mascot Design — built for cross-generation consistency

The hard constraint: a *fresh ChatGPT session must redraw Engy recognizably from text alone*. The defense is **few, high-contrast, nameable tokens**. Complexity is the enemy of consistency.

### Engy — the 5-token spec

Keep Engy to exactly five fixed, easy-to-name visual tokens. Five is the sweet spot: enough to be a character, few enough that a text model reproduces them.

| # | Token | Fixed description | Why it survives regeneration |
|---|-------|-------------------|------------------------------|
| 1 | **Body shape** | "small round white librarian-robot, egg/rounded body" | Simple silhouettes regenerate; limbs/joints don't. |
| 2 | **Notebook chest** | "a softly glowing open notebook set into her chest" | The plot-critical token (= `MEMORY_DIR`); always named first. |
| 3 | **Eyes** | "two large round friendly black dot-eyes on a screen-face" | Dot-eyes are near-impossible to draw wrong. |
| 4 | **One accent color** | "a single soft-teal scarf/collar" | One accent color is far more stable than a full outfit. |
| 5 | **One prop** | "a tiny pencil tucked behind her, or held" | A single prop reads as "the same character." |

**Reusable mascot prompt block (copy verbatim into every page):**

> "ENGY is a small, round, white librarian-robot with a softly glowing open notebook set into her chest (this notebook is her memory), two large friendly round black dot-eyes on a simple screen-face, a single soft-teal scarf, and a tiny pencil. Keep her simple, rounded, and consistent."

### Narrator-sensei — the 3-token spec

The sensei appears less often and mainly *frames* — so keep him even simpler than Engy to avoid stealing visual weight.

| # | Token | Fixed description |
|---|-------|-------------------|
| 1 | **Silhouette** | "a calm older robot-sage, taller and rectangular (contrast with Engy's round shape)" |
| 2 | **Prop** | "holding a long pointer or an unrolling scroll" |
| 3 | **Accent** | "a single deep-indigo robe/sash (contrasts Engy's teal)" |

> Shape + color contrast (round/teal vs tall/indigo) lets the reader tell them apart instantly even when the line art drifts slightly between generations.

### Consistency tactics for the prompt-writer

1. **Name tokens explicitly, every time.** "round white robot, glowing notebook chest, teal scarf, dot-eyes" — never rely on the model remembering a prior page.
2. **Lead with the silhouette, then the chest.** The two load-bearing tokens go first in the prompt so they don't get dropped if the model truncates.
3. **Fix the palette in words** (cream/teal/peach), not just "soft colors."
4. **Avoid anything ChatGPT renders inconsistently:** exact text on signs (keep labels short, ≤2 words), precise finger counts, complex backgrounds, small faces in crowds.
5. **One Engy per panel cluster, large.** Crowds of tiny Engys drift; one big Engy stays on-model.
6. **Reuse a "pose vocabulary"** — reading, writing, reaching-and-stopped, waving — so poses repeat rather than invent.

---

## Pedagogical Patterns (what makes explainer comics work)

| Pattern | What it is | Where it lands in this comic |
|---------|-----------|------------------------------|
| **One idea per page** | Each page has exactly one takeaway; resist cramming. | Enforced by the page table — every row has a single "takeaway." |
| **Recurring visual metaphor** | A single physical anchor the reader returns to. | The glowing notebook = memory. Established p03, recalled everywhere. |
| **The rule in one panel** | Each rule gets a single, iconic, memorable panel. | Pages 09–12: locked door, sealed vault, citation strings, 4-quadrant. |
| **Before / after** | Show the world without the concept, then with it. | Page 02 (Engy with no notebook fails) → page 03 (notebook fixes it). |
| **Callbacks** | Re-use an earlier motif later to reward attention. | Recap (p18) is pure callback; history (p16) recalls the notebook. |
| **Physicalize the abstract** | Turn data structures into objects. | STATE_DIR=room, QUESTION=letter, evidence=strings, commands=arrows. |
| **Progressive disclosure** | Never use a term before it's been shown. | Strict bottom-up order; jargon (RAG, vector DB) only after p14. |
| **Same syntax, repeated** | A consistent "visual grammar" (the color-state code). | Learned p12, silently reused after. |
| **A character to root for** | Emotional investment carries dry mechanics. | Engy struggles (p02), learns, succeeds — reader follows her. |

---

## Data Flow (how a reader's understanding moves)

```
HOOK (feel the problem)
   ↓
INTUITION (the notebook metaphor)            ← anchor motif planted
   ↓
MECHANICS (room → update → notebook → answer → card)
   ↓
RULES (constraints on the mechanics)         ← each = one iconic panel
   ↓
HOW-TO (the submission folder)
   ↓
HISTORY (place ENGRAM in the lineage)        ← victory lap, fact-checked
   ↓
RECAP (one panel = all motifs recalled)      ← callback payoff
```

**Key dependency flows:**

1. **Motif-setup flow:** p03–p07 must precede every rule and the recap. They are the comic's "type definitions."
2. **Rule flow:** p09–p12 each depend on the mechanics page (p08) but not on each other → parallel-authorable.
3. **History flow:** p15–p17 depend only on the sensei/timeline motif → independently authorable, but content-gated on a fact-check.
4. **Recap flow:** p18 depends on *all* motifs → authored last.

---

## Scaling Considerations (cutting 18 → 15, or growing past 18)

| Target length | Adjustment |
|---------------|------------|
| **Hard 15 pages** | Cut `[CUT-OK]` pages 14 + 17, and merge 15+16 history into one page. Keeps all ★ payload + all rules. |
| **18 pages (recommended)** | As specced. Comfortable one-idea-per-page pacing. |
| **20+ pages** | Split page 12 (the 4-state distinction) into two pages, and give each rule a "before/after" pair. Don't pad history. |

**Scaling priorities (what to protect when cutting):**

1. **First to protect:** the spine (p03–p08) and the recap (p18) — these *are* the Core Value.
2. **Second:** the four rule pages (09–12), especially the current/stale/superseded/uncertain page.
3. **First to cut:** the checker page (14) and the "where it sits now" history page (17).

---

## Anti-Patterns

### Anti-Pattern 1: Front-loading the history
**What people do:** Open with "the history of AI memory" to seem authoritative.
**Why it's wrong:** Dumps jargon (RAG, vector DB, long context) on a reader with no scaffold; they bounce before reaching ENGRAM.
**Do this instead:** History is the *victory lap* (p15–17), readable only after the mechanics click.

### Anti-Pattern 2: A complex, detailed mascot
**What people do:** Give Engy an elaborate outfit, many accessories, expressive hands, a detailed face.
**Why it's wrong:** Every extra token is a thing a fresh ChatGPT generation will draw differently → the character "drifts" page to page, breaking the one consistency the project most needs.
**Do this instead:** Lock Engy to 5 nameable tokens; lead prompts with silhouette + notebook.

### Anti-Pattern 3: Two ideas on one page
**What people do:** Combine `update` and `answer` mechanics *and* the no-hindsight rule on one busy page to "save space."
**Why it's wrong:** The reader can't tell which idea the page is "about"; retention collapses.
**Do this instead:** One takeaway per page (the page table enforces this); use the diptych page 08 only to *summarize* two already-taught commands.

### Anti-Pattern 4: Long text on signs / in panels
**What people do:** Write full sentences, file paths, or JSON on in-image signage.
**Why it's wrong:** ChatGPT image generation garbles long/exact text, and it re-renders differently each page.
**Do this instead:** Keep in-image labels ≤2 words (`TOMORROW`, `JUDGE`, `2026-04-09`); put real explanation in the page's caption text, not inside the art.

### Anti-Pattern 5: Blurring `STATE_DIR` evidence and `MEMORY_DIR` memory
**What people do:** Draw the answer's evidence and Engy's memory as the same thing.
**Why it's wrong:** The kit explicitly separates workspace evidence (`evidence_paths` → STATE_DIR) from self-memory (`memory_refs` → MEMORY_DIR); conflating them teaches the concept wrong.
**Do this instead:** Citation strings (p11) run to *shelf files in the room*; memory always lives in the *notebook*. Two surfaces, two colors of string.

---

## Integration Points

### Downstream consumers

| Consumer | What it reads from here | Notes |
|----------|-------------------------|-------|
| **Roadmap (phase/page structure)** | The 18-row page table + dependency flows | Each page → one GSD spike → one ChatGPT prompt. Spine = one phase; rules = parallel phase; history = parallel+gated; recap = final phase. |
| **Prompt-writer (per spike)** | The motif table + style block + mascot block | Copies the style + mascot blocks verbatim into every prompt; pulls per-page motifs from the page table. |
| **FEATURES.md research** | Which concepts are "table stakes" to depict | The ★ payload pages map to Core Value. |
| **PITFALLS.md research** | Anti-patterns above | Especially mascot drift + garbled in-image text. |

### Internal boundaries / phase ordering for the roadmap

| Boundary | Ordering | Notes |
|----------|----------|-------|
| Style/mascot block ↔ all pages | **First** | Must be locked before any page prompt is authored. |
| Spine (p03–08) ↔ rules/history | Spine **before** both | Motifs are dependencies. |
| Rules (09–12) ↔ each other | **Parallel** | No inter-dependencies. |
| History (15–17) ↔ rules | **Parallel** but content-gated | Needs a fact-check pass (see flag). |
| Recap (18) ↔ everything | **Last** | Callback collage. |

---

## Research Flags (for the roadmap)

- **History pages (15–17) need a fact-check pass.** Web research tools were unavailable in this run, so the 2020→present AI-memory timeline below is from model knowledge (cutoff Jan 2026), **MEDIUM confidence**. The roadmap should schedule a verification step against primary sources before those prompts are rendered. Anchor points to verify: RAG (Lewis et al., 2020); vector-DB era (FAISS/Pinecone/Chroma, ~2021–2023); long-context models (2023–2024); explicit agent memory (MemGPT → Letta, 2023–2024); memory frameworks maturing 2024–2025. Treat names/dates as *to-confirm*, not authoritative.
- **Page 12 (4-state distinction) is the hardest single idea** — flag for extra prompt-iteration budget and possibly a 2-page split.

---

## Sources

- ENGRAM repo (authoritative, HIGH confidence): `CONTRACT.md`, `STATE_FORMAT.md`, `QUESTION_FORMAT.md`, `SUBMISSION_FORMAT.md`, `README.md`, `.planning/PROJECT.md`.
- Explainer-comic pedagogy & visual-language reasoning: established educational-comic craft (one-idea-per-page, recurring metaphor, before/after, rule-in-one-panel) — applied analysis, HIGH confidence for structure.
- AI-memory history timeline: model knowledge (cutoff Jan 2026), MEDIUM confidence — **flagged for fact-check** (web tools unavailable this run).

---
*Architecture research for: ENGRAM explainer manga — narrative structure & visual design language*
*Researched: 2026-06-18*
