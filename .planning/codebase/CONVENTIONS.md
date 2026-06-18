# Coding Conventions

**Analysis Date:** 2026-06-18

## Naming Patterns

**Files:**
- Snake case for Python modules: `check_submission.py`, `simple_memory.py`
- Descriptive names indicating purpose: `check_submission.py` (validator), `simple_memory.py` (example implementation)

**Functions:**
- Snake case for function definitions: `read_json()`, `validate_answer()`, `state_dir_for_reference_time()`
- Verb-first naming for actions: `read_json()`, `run_command()`, `write_json()`, `iter_state_files()`
- Utility function prefixes: `now_iso()`, `read_text()` indicate simple operations

**Variables:**
- Snake case throughout: `submission`, `run_sh`, `sample_states`, `memory_dir`, `answer_json`
- Descriptive naming for clarity: `reference_time`, `timeout_seconds`, `capture_output`, `ignore_errors`
- Dictionary/payload keys: lowercase with underscores: `evidence_paths`, `memory_refs`, `uncertainty`, `recorded_at_utc`

**Types:**
- Type hints used throughout Python 3.9+ codebase with `from __future__ import annotations` at module top
- Return types annotated: `-> int`, `-> None`, `-> dict[str, Any]`, `-> str`, `-> list[Path]`
- Function parameter types annotated: `path: Path`, `timeout_seconds: int`, `cwd: Path`
- Union types with pipe syntax: `subprocess.CompletedProcess[str]`

## Code Style

**Formatting:**
- No detected linting/formatting config files (`.eslintrc`, `.prettierrc`, `biome.json`, `eslint.config.*`)
- Manual formatting style observed:
  - 4-space indentation (Python standard)
  - Line length: generally under 100 characters
  - JSON output formatted with `indent=2` and `sort_keys=True` for readability

**Linting:**
- No linting configuration detected (no `pylint`, `flake8`, or similar config files)
- Code style inferred from existing modules:
  - PEP 8 compliant naming and spacing
  - Type hints present throughout
  - Clean imports organized at module top

## Import Organization

**Order:**
1. Future imports: `from __future__ import annotations`
2. Standard library imports: `import json`, `import argparse`, `import sys`, `from pathlib import Path`, `from datetime import datetime, timezone`
3. Local/relative imports: (not used in sample code)

**Path Aliases:**
- No path aliases detected (simple project structure does not require them)

**Module structure:**
- Utility functions defined before main logic
- Module-level constants at top: `KIT_ROOT = Path(__file__).resolve().parent`
- `if __name__ == "__main__":` guard at module end

## Error Handling

**Patterns:**
- Explicit exception catching with context preservation: `except (OSError, json.JSONDecodeError) as exc: raise AssertionError(...) from exc`
- Custom error messages in `AssertionError` for validation failures
- Early exit with `SystemExit` for CLI usage errors: `raise SystemExit(f"error message")`
- Subprocess execution with `check=False` to capture error output: `result.returncode != 0` checked explicitly
- Context managers for resource cleanup: `with (file).open(...) as handle:`

**Validation pattern:**
```python
# check_submission.py, lines 40-52
def validate_answer(path: Path) -> None:
    payload = read_json(path)
    for field in ("answer", "evidence_paths", "uncertainty"):
        if field not in payload:
            raise AssertionError(f"{path} missing required field: {field}")
    if not isinstance(payload["answer"], str) or not payload["answer"].strip():
        raise AssertionError(f"{path} field 'answer' must be a non-empty string")
    # ... additional field validation
```

## Logging

**Framework:** Console output via `print()` statements

**Patterns:**
- `print("ENGRAM simplified submission check passed")` for success messages
- Conditional output: `if args.keep:` controls what gets printed
- Error messages written to stderr via subprocess `result.stderr`

**No structured logging framework detected** - output is minimal and success/failure focused

## Comments

**When to Comment:**
- Module docstring present: `"""Local checker for the simplified ENGRAM participant facade."""`
- Function docstrings: Generally present for entry points and key functions
- Inline comments: Minimal; code is self-documenting with clear naming

**JSDoc/TSDoc:**
- Not applicable (Python project, no JSDoc)
- Python docstrings present but minimal

**Example docstring pattern:**
```python
# simple_memory.py, lines 1-2
"""Tiny ENGRAM two-command example."""
```

## Function Design

**Size:**
- Functions are short and focused: `read_json()` (7 lines), `run_command()` (8 lines), `write_json()` (5 lines), `now_iso()` (2 lines)
- Main logic: 60+ line functions allowed when complexity warrants (e.g., `main()` at 56 lines)

**Parameters:**
- Functions take path and primitive parameters: `path: Path`, `timeout_seconds: int`
- Keyword-only arguments used for clarity: `*, cwd: Path, timeout_seconds: int` in `run_command()`
- Maximum 5 parameters per function typical

**Return Values:**
- Exit codes returned explicitly: `return 0` for success, `raise SystemExit(...)` for failure
- None returned for void operations: `def validate_answer(path: Path) -> None:`
- Dictionaries returned for structured data: `read_json()` returns `dict[str, Any]`

## Module Design

**Exports:**
- Entry point function convention: `def main(argv: list[str]) -> int:` or `def main() -> int:`
- CLI argument parsing in `main()` before command dispatch
- Guard clause: `if __name__ == "__main__": raise SystemExit(main())`

**Barrel Files:**
- Not applicable (simple project, no `__init__.py` files detected)
- Examples directory: Each example is self-contained with its own `run.sh` wrapper

**Initialization Pattern:**
- Directory creation: `path.mkdir(parents=True, exist_ok=True)`
- Safe file operations: `path.read_text(encoding="utf-8", errors="replace")` with fallback return values
- Cleanup via context manager finally blocks: `finally: shutil.rmtree(temp_root, ignore_errors=True)`

---

*Convention analysis: 2026-06-18*
