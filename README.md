# ENGRAM Kit

ENGRAM is a small challenge for memory systems in evolving workspaces.

Your program receives dated workspace states in chronological order. It may
write anything it wants into its own memory directory. When ENGRAM asks a
question, your program answers from the current state plus that memory.

The contract is two commands:

```bash
./run.sh update STATE_DIR MEMORY_DIR
./run.sh answer STATE_DIR MEMORY_DIR QUESTION_JSON ANSWER_JSON
```

This kit is the public participant facade. It does not contain private
evaluation data, judge packets, answer keys, rubrics, QEMU details, dashboard
internals, atlas/tracks artifacts, or provider credentials.

Public repo:

```text
https://github.com/saxenauts/engram-kit
```

Direct zip download:

```text
https://github.com/saxenauts/engram-kit/releases/download/v0.1-real-first-two-weeks/engram-kit.zip
```

Discord / submission channel:

```text
https://discord.gg/8F2g6VDD
```

## Files

```text
CHECKLIST.md              readiness checklist before sharing
CONTRACT.md               the two-command interface
STATE_FORMAT.md           what STATE_DIR contains
QUESTION_FORMAT.md        question and answer JSON
SUBMISSION_FORMAT.md      required submission folder shape
PRESENTATION_PLACEMENT.md where this belongs in the deck
sample_states/            real first-two-week daily ENGRAM states
sample_questions.json     candidate-visible first-two-week questions
examples/simple_memory/   minimal working submission
check_submission.py       local contract checker
```

## Quick Start

Check the included example:

```bash
python3 check_submission.py --submission examples/simple_memory
```

Then build your own submission folder with a `run.sh` that supports:

```bash
./run.sh update STATE_DIR MEMORY_DIR
./run.sh answer STATE_DIR MEMORY_DIR QUESTION_JSON ANSWER_JSON
```

Passing `check_submission.py` only proves that your package speaks the interface.
It is not benchmark evidence and it does not predict private-eval score.

## What To Build

Build any memory system you want: a graph, vector index, Markdown memory,
SQLite store, local agent loop, wrapped open-source backend, or custom pipeline.

ENGRAM only requires that your system can:

- read dated workspace states;
- maintain persistent memory under `MEMORY_DIR`;
- answer from current state plus prior memory;
- cite evidence paths;
- handle stale, current, superseded, and uncertain information;
- run without manual intervention through the two-command interface.

## Explorations & Spikes (internal)

An internal site of experiential spikes exploring a **visual-novel learning game** built
around the ENGRAM papers (ALMA & AMA-Bench). Each spike is a runnable, zero-dependency demo
plus a writeup. Open the hub, or jump straight to a demo:

**▶ [Explorations hub](.planning/spikes/index.html)** — links every spike's demo + writeup

| # | Spike | Verdict | Demo | Writeup |
|---|-------|---------|------|---------|
| 001 | VN engine feel — panels + typewriter + branching, zero build | ✓ VALIDATED | [play](.planning/spikes/001-vn-engine-feel/index.html) | [read](.planning/spikes/001-vn-engine-feel/README.html) |
| 002 | Learning loop — Examiner comprehension checkpoints | ✓ VALIDATED | [play](.planning/spikes/002-learning-loop/index.html) | [read](.planning/spikes/002-learning-loop/README.html) |
| 003 | Dialogue pipeline — auto-extract a VN script from the manga | ✓ VALIDATED | [play](.planning/spikes/003-dialogue-pipeline/play.html) | [read](.planning/spikes/003-dialogue-pipeline/README.html) |

Also: [Manifest](.planning/spikes/MANIFEST.html) · [Conventions](.planning/spikes/CONVENTIONS.html).
Regenerate the site after editing any spike with `node .planning/spikes/build-site.js`.

> The demos open directly via `file://` (no server). The HTML pages are generated from the
> spike markdown and committed for convenience.
