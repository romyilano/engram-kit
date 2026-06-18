# Architecture

> Mapped: 2026-06-18

## Overview

ENGRAM Kit is the **public participant facade** for the ENGRAM memory-system
challenge. It is not an application with running services — it is a
**contract + fixtures + reference checker** that defines a two-command interface
participants implement, and a local validator that proves a submission speaks
that interface.

The architecture is deliberately thin. The "system" being specified lives in
*participant* submissions; this kit only defines the boundary and ships a trivial
reference implementation plus a checker.

```text
                 ENGRAM (private runtime)
                         │
                         │ calls in chronological order
                         ▼
        ┌──────────────────────────────────┐
        │   ./run.sh update STATE_DIR MEM   │   ← participant program
        │   ./run.sh answer STATE_DIR MEM   │     (the thing being built)
        │            QUESTION ANSWER        │
        └──────────────────────────────────┘
                         ▲
                         │ simulated locally by
                         │
        ┌──────────────────────────────────┐
        │        check_submission.py        │   ← reference checker
        │   replays sample_states/ +        │
        │   sample_questions.json           │
        └──────────────────────────────────┘
```

## Architectural Pattern

**Contract-driven / fixture-replay.** There is no framework, server, or
long-lived process. The design centers on a stable CLI contract documented in
`CONTRACT.md` and enforced by `check_submission.py:64` (`main`).

Two phases define the entire data lifecycle:

1. **Update phase** — `./run.sh update STATE_DIR MEMORY_DIR`
   Program ingests a dated bounded workspace state and writes whatever it wants
   into its persistent `MEMORY_DIR`.
2. **Answer phase** — `./run.sh answer STATE_DIR MEMORY_DIR QUESTION_JSON ANSWER_JSON`
   Program reads current state + accumulated memory + a question, and writes a
   structured answer JSON.

## Layers

The checker (`check_submission.py`) is organized into small, single-purpose
functions rather than classes:

| Layer | Responsibility | Location |
|-------|----------------|----------|
| Command dispatch | Parse CLI args, orchestrate phases | `check_submission.py:64` (`main`) |
| Subprocess execution | Run participant `run.sh` with timeout | `check_submission.py:29` (`run_command`) |
| State resolution | Map a question's `reference_time` → state dir | `check_submission.py:55` (`state_dir_for_reference_time`) |
| Input parsing | Safe JSON loading with assertions | `check_submission.py:19` (`read_json`) |
| Output validation | Enforce answer JSON schema | `check_submission.py:40` (`validate_answer`) |

The reference participant program (`examples/simple_memory/simple_memory.py`)
mirrors the same two-phase shape: `update()` (line 35) and `answer()` (line 49),
dispatched by `main()` (line 90).

## Data Flow

**Checker replay flow** (`check_submission.py:84`–`123`):

1. Create a temp working root (`tempfile.mkdtemp`) with `memory/`, `answer.json`,
   `question.json`.
2. Discover and sort sample states: `sorted((KIT_ROOT / "sample_states").iterdir())`.
3. **For each state in chronological order**, invoke `run.sh update STATE_DIR MEMORY_DIR`.
   Non-zero exit aborts with the captured stderr tail.
4. Load the first sample question, resolve its `reference_time` to a state dir.
5. Invoke `run.sh answer STATE_DIR MEMORY_DIR question.json answer.json`.
6. Validate the produced `answer.json` shape.
7. Clean up the temp dir (unless `--keep`).

**Memory persistence flow** (reference impl): `MEMORY_DIR` is the only durable,
benchmark-visible surface (`CONTRACT.md:51`). The simple example appends one
JSON record per update to `memory/memory.jsonl` (`simple_memory.py:44`).

## Key Abstractions

- **STATE_DIR** — a *full bounded workspace state* for one date (not a diff).
  Contains `files/`, `manifest.tsv`, `git_log.txt`, `changes.txt`,
  `state_meta.json`, `README.md`. Defined in `STATE_FORMAT.md`.
- **MEMORY_DIR** — participant-owned persistent storage. Format is entirely up
  to the participant (SQLite, vectors, Markdown, JSONL, graph stores).
- **Question / Answer JSON** — `QUESTION_FORMAT.md`. Answer requires `answer`,
  `evidence_paths`, `uncertainty`; optional `memory_refs`.
- **Evidence vs. memory separation** — evidence paths point into `STATE_DIR`;
  memory refs point into `MEMORY_DIR`. The contract explicitly forbids blurring
  the two (`QUESTION_FORMAT.md:47`).

## Entry Points

- `check_submission.py` — `python3 check_submission.py --submission <folder>`.
  The `if __name__ == "__main__"` guard calls `SystemExit(main())`.
- `examples/simple_memory/run.sh` — the canonical participant entrypoint shape;
  a thin bash wrapper that execs `simple_memory.py "$@"`.

## Constraints (Boundary Rules)

From `CONTRACT.md:44`–`53`, the architecture enforces a strict *no-hindsight*
boundary:

- Only released states are visible; no future states.
- No private evaluation data, judge packets, answer keys, rubrics, or reference sets.
- No access to other candidates' memory.
- `MEMORY_DIR` is the only durable benchmark-visible memory.
- External services/APIs/daemons must be declared in the submission README.

## Anti-Patterns to Avoid (per contract intent)

- Treating `manifest.tsv` or `git_log.txt` as an answer oracle — they are
  *evidence*, not truth (`STATE_FORMAT.md:42`, `:54`).
- Answering with hindsight from states later than the question's `reference_time`.
- Storing answers in evidence paths or workspace files in `memory_refs`.

## Error Handling Strategy

- Parsing failures raise `AssertionError` with the offending path
  (`read_json`, `validate_answer`).
- Subprocess failures surface exit code + last 2000 chars of stderr
  (`check_submission.py:99`, `:111`).
- Reference-time parse failure falls back to a date slice, then to the latest
  state (`state_dir_for_reference_time`) — a *silent* fallback (see CONCERNS.md).
