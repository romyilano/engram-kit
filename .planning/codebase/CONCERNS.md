# Concerns

> Mapped: 2026-06-18

Scope note: this is a small, intentionally-thin participant kit, not a
production service. "Concerns" here are mostly about checker robustness,
validation depth, and event-readiness — not large-scale architecture risk.

## High Priority

### 1. Silent fallback in reference-time → state resolution
`check_submission.py:55` (`state_dir_for_reference_time`):
- On a `ValueError` parsing `reference_time`, it falls back to `reference_time[:10]`.
- If the resulting `state_dir` does not exist, it **silently** returns the
  *latest* state (`sample_states[-1]`).
This can mask a malformed question or a missing state by quietly answering
against the wrong (latest) state — a hindsight-leak risk given ENGRAM's
no-future-state contract. Recommend logging/raising when no matching state dir
is found.

### 2. Checker validates only one question
`check_submission.py:102` uses `questions[0]` only. `sample_questions.json` may
contain multiple candidate questions, but the contract check exercises just the
first. A submission could pass while failing on other questions. Recommend
looping over all questions.

### 3. Structural-only answer validation
`validate_answer` (`check_submission.py:40`) checks types/presence but not:
- whether `evidence_paths` actually exist inside the resolved `STATE_DIR`;
- whether `memory_refs` point into `MEMORY_DIR`;
- any memory consistency across update→answer cycles.
A submission can emit well-formed but evidence-free answers and still pass.

### 4. Event-readiness items still open (CHECKLIST.md)
`CHECKLIST.md:38`–`43` ("Still Needed Before The Event") has unchecked items:
- QR code / short URL for the presentation.
- Public resource limits undecided (timeout, disk, RAM, network/model mode).
- Submission delivery mechanism undecided (PRs vs zip vs form).
- Whether the public checker runs in CI undecided.
These are operational blockers, not code bugs, but they gate the live event.

## Medium Priority

### 5. `shutil.rmtree(..., ignore_errors=True)` masks cleanup failures
`check_submission.py:123`: cleanup of the temp dir swallows all errors. Fine for
hygiene, but a failing cleanup (e.g. a daemon holding a file) is invisible.

### 6. Reference example does full file enumeration on every answer
`examples/simple_memory/simple_memory.py:53` re-reads every state file on each
`answer` call (`iter_state_files` + `read_text`). It is explicitly a keyword toy
(`uncertainty` field says so), but as a starting template it models an
unscalable pattern. Acceptable for an example; worth a comment warning so
participants don't copy the approach into a real system.

### 7. No machine-readable checker output
The checker prints human strings (`ENGRAM simplified submission check passed`)
and signals via exit code only. There is no JSON result for CI/dashboard
ingestion — directly tied to the open CHECKLIST item on CI.

### 8. Reference impl keyword heuristics don't generalize
`simple_memory.py:58`–`73` branches on the literal substrings `"backend"` and
`"direction"` with hardcoded canned answers. This is intentional (it's a
minimal example), but it is dead-end logic that won't transfer.

## Low Priority / Notes

### 9. Implicit Python version requirement
`check_submission.py` and `simple_memory.py` use `from __future__ import
annotations` plus PEP 604-style `list[str]` / `dict[str, Any]` annotations,
implying **Python 3.9+** (cleanly 3.10+). This is not documented in README or
SUBMISSION_FORMAT.md. Participants on older interpreters could hit surprises.

### 10. No declared resource sandboxing in the checker
The checker enforces a subprocess `timeout` (`run_command`) but no memory, disk,
or network limits. The contract asks participants to *declare* external services
(`CONTRACT.md:52`), but the local checker does not enforce or detect them.

### 11. `.idea/` committed to the repo
JetBrains project files (`.idea/workspace.xml`, etc.) are tracked. Harmless but
noise for a public participant-facing kit; consider gitignoring.

## What's Healthy

- Single-file, stdlib-only checker — easy to audit, no dependency risk.
- Clear separation of evidence (state) vs memory surfaces in the contract.
- Strong, explicit boundary rules against hindsight and private-data leakage
  (`CONTRACT.md` boundary section).
- Fixtures are real first-two-week states, giving an authentic replay corpus.
- Error messages on subprocess failure include captured stderr tail — good for
  participant debugging.
