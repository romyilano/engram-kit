# Technology Stack

**Analysis Date:** 2026-06-18

## Languages

**Primary:**
- Python 3 (3.9.6+) - Core evaluation framework and example implementation

**Secondary:**
- Bash - Shell scripting for entry points and test runners

## Runtime

**Environment:**
- Python 3.9+ (system Python)

**Package Manager:**
- pip (standard Python packaging)
- Lockfile: Not present - no `requirements.txt` or `pyproject.toml` file

## Frameworks

**Testing:**
- No external test framework - uses Python standard library (`unittest` style validation)
- `subprocess` module for test execution
- `tempfile` for test isolation

**Build/Dev:**
- Bash shell scripts (`run.sh`) as entry points

## Key Dependencies

**Critical:**
- Python standard library only:
  - `json` - JSON parsing and generation (`check_submission.py`, `simple_memory.py`)
  - `argparse` - CLI argument parsing (`check_submission.py`)
  - `subprocess` - Running participant submissions (`check_submission.py`)
  - `pathlib` - File path handling (`check_submission.py`, `simple_memory.py`)
  - `tempfile` - Temporary test directories (`check_submission.py`)
  - `shutil` - Directory cleanup (`check_submission.py`)
  - `datetime` - Timestamp and ISO date handling (`simple_memory.py`, `check_submission.py`)

**Infrastructure:**
- None - this is a standalone evaluation kit with no external dependencies

## Configuration

**Environment:**
- No environment variables required
- Configuration passed via command-line arguments to `run.sh` interface

**Build:**
- No build process required
- Direct Python execution via bash wrapper scripts

## Platform Requirements

**Development:**
- Python 3.9 or later
- Bash shell
- Unix-like environment (Linux, macOS)

**Production:**
- Python 3.9 or later
- Bash shell
- Read/write access to `STATE_DIR` and `MEMORY_DIR` paths
- Typical single-machine execution (no distributed requirements)

## Notable Characteristics

**Zero External Dependencies:**
The evaluation kit is intentionally designed with zero external package dependencies. All functionality uses only Python standard library modules. This ensures:
- Simple deployment and execution
- No version conflicts or compatibility issues
- Straightforward participant submission verification

**Entry Point Pattern:**
All execution flows through `run.sh` bash wrappers that invoke Python scripts with specific command signatures:
```bash
./run.sh update STATE_DIR MEMORY_DIR
./run.sh answer STATE_DIR MEMORY_DIR QUESTION_JSON ANSWER_JSON
```

---

*Stack analysis: 2026-06-18*
