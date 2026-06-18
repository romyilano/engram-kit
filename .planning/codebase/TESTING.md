# Testing

> Mapped: 2026-06-18

## Summary

There is **no unit-test framework** in this repo — no `pytest`, `unittest`,
test directory, or CI config. Validation is done by a single **integration-style
contract checker**, `check_submission.py`, which replays real fixtures against a
participant submission and asserts the output shape.

This is appropriate for the kit's purpose: it ships a *contract* and proves that
a candidate submission *speaks the interface*, not that a particular memory
implementation is correct. The README is explicit: "Passing `check_submission.py`
only proves that your package speaks the interface. It is not benchmark evidence"
(`README.md:68`).

## How "Tests" Run

```bash
# From engram-kit/
python3 check_submission.py --submission examples/simple_memory
```

Flags (`check_submission.py:64`):

- `--submission` (required) — folder containing `run.sh`.
- `--timeout-seconds` (default `60`) — per-subprocess timeout.
- `--keep` — keep the temp run dir and print `temp_dir` / `answer_json` paths
  for inspection.

Expected success output: `ENGRAM simplified submission check passed`.

## What the Checker Validates

The checker is the de-facto test harness (`check_submission.py:84`–`123`):

1. **Update replay** — runs `run.sh update STATE_DIR MEMORY_DIR` for every
   directory in `sample_states/`, in chronological (sorted) order. Any non-zero
   exit fails with the last 2000 chars of stderr.
2. **Answer run** — takes the first question from `sample_questions.json`,
   resolves its `reference_time` to a state dir, and runs
   `run.sh answer STATE_DIR MEMORY_DIR question.json answer.json`.
3. **Schema validation** (`validate_answer`, line 40):
   - `answer`, `evidence_paths`, `uncertainty` must be present.
   - `answer` must be a non-empty string.
   - `evidence_paths` must be a list.
   - `uncertainty` must be a string.
   - `memory_refs`, if present, must be a list.

## Test Fixtures

- **State fixtures** — `sample_states/2026-04-08/` … `2026-04-19/`: real
  first-two-week daily ENGRAM states. These act as the replay corpus. The
  checker discovers them dynamically via `iterdir()` + sort, so adding a new
  dated directory automatically extends coverage.
- **Question fixtures** — `sample_questions.json` (`questions` array). Only the
  **first** question is exercised by the checker today (`questions[0]`,
  `check_submission.py:102`).

## Execution Model

- **Real subprocess execution** via `subprocess.run` with `capture_output=True`,
  `text=True`, and a hard `timeout` (`run_command`, line 29). No mocking — the
  participant program runs for real in a temp directory.
- **Isolation** — each check runs in a fresh `tempfile.mkdtemp` root
  (`engram-kit-check-…`) holding `memory/`, `question.json`, `answer.json`.
  Cleaned up in a `finally` block unless `--keep` (line 121).
- **Working directory** — subprocesses run with `cwd=submission` so relative
  paths in `run.sh` resolve against the submission folder.

## Mocking & Coverage

- **Mocking**: none. The design favors real end-to-end execution over mocks.
- **Coverage measurement**: none configured.
- **Assertion style**: plain `AssertionError` / `SystemExit` with descriptive
  messages; no assertion library.

## Gaps (see CONCERNS.md)

- Only one question is validated, not the full `sample_questions.json` set.
- Answer validation is structural only — no semantic check of `evidence_paths`
  (e.g. that they exist in the state) or memory consistency across ticks.
- No timeout-boundary or failure-path tests for the checker itself.
- No machine-readable (JSON/exit-code-rich) output for CI integration.

## Adding Tests

To extend validation, the natural seams are:
- Loop over all `questions` instead of `questions[0]` in `main`.
- Strengthen `validate_answer` to verify `evidence_paths` resolve inside the
  resolved `STATE_DIR`.
- Add a lightweight `pytest` suite around `read_json`, `validate_answer`, and
  `state_dir_for_reference_time` (all pure, easily unit-testable).
