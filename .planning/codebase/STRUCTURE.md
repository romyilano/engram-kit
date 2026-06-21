# Directory Structure

> Mapped: 2026-06-18

## Top-Level Layout

```text
engram-kit/
  README.md                  entry doc: challenge overview + quick start
  CONTRACT.md                the two-command interface (source of truth)
  STATE_FORMAT.md            what a STATE_DIR contains
  QUESTION_FORMAT.md         question + answer JSON schema
  SUBMISSION_FORMAT.md       required participant folder shape
  CHECKLIST.md               operator readiness checklist
  PRESENTATION_PLACEMENT.md  where this fits in the event deck
  STATE_FORMAT.md
  check_submission.py        local contract checker (the only real "code")
  sample_questions.json      candidate-visible sample questions
  examples/
    simple_memory/           minimal reference submission
      README.md
      run.sh                 bash entrypoint → simple_memory.py
      simple_memory.py       two-phase reference implementation
  sample_states/             real first-two-week daily ENGRAM states (fixtures)
    2026-04-08/ … 2026-04-19/
```

## Key Locations

| What | Where |
|------|-------|
| Interface contract | `CONTRACT.md` |
| Reference checker | `check_submission.py` |
| Reference submission | `examples/simple_memory/` |
| Sample state fixtures | `sample_states/<YYYY-MM-DD>/` |
| Sample questions | `sample_questions.json` |
| Format specs (docs) | `*_FORMAT.md` at repo root |

## State Fixture Layout

Each `sample_states/<date>/` directory is a full bounded workspace snapshot
(`STATE_FORMAT.md`):

```text
sample_states/2026-04-09/
  README.md          short state note (date, reference time, caveats)
  state_meta.json    machine-readable summary (state_id, date, path counts)
  manifest.tsv       tab-separated file inventory (path/size/sha256/status/…)
  git_log.txt        bounded commit history visible at this state
  changes.txt        human-readable change summary since previous state
  files/             the actual workspace files visible at this state
    research/n1-memory-lab/*.md
```

Dates observed: `2026-04-08` through `2026-04-19` (daily cadence,
`cadence_id: "daily"` in `state_meta.json`). Each later state generally adds
files under `files/research/n1-memory-lab/`.

## Naming Conventions

- **Docs**: `UPPER_SNAKE_CASE.md` at repo root (e.g. `STATE_FORMAT.md`,
  `SUBMISSION_FORMAT.md`). README is the conventional `README.md`.
- **State dirs**: ISO date `YYYY-MM-DD`, sorted lexicographically (which equals
  chronological order — the checker relies on this, `check_submission.py:76`).
- **State IDs**: `daily_<date>` (e.g. `daily_2026-04-08`).
- **Python**: `snake_case` modules and functions; lowercase script names
  (`check_submission.py`, `simple_memory.py`).
- **Memory artifacts** (reference impl): `memory.jsonl` under `MEMORY_DIR`.

## Where Things Go

- **New format rules** → a root-level `*_FORMAT.md` doc.
- **New sample state** → a new `sample_states/<date>/` directory following the
  fixture layout above; the checker auto-discovers it (no registration needed).
- **New sample question** → append to the `questions` array in
  `sample_questions.json`.
- **Reference/example code** → `examples/<name>/` with its own `run.sh`.
- **Checker logic** → `check_submission.py` (single-file, stdlib only).

## Notable Non-Source Files

- `.idea/` — JetBrains IDE project metadata (committed; not part of the kit
  contract).
- `.claude/settings.local.json` — local Claude Code settings.
- `.planning/` — GSD planning artifacts (this codebase map).
