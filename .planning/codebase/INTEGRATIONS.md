# External Integrations

**Analysis Date:** 2026-06-18

## APIs & External Services

**None**
- This is a standalone evaluation kit with no external API integrations
- Participants may use external services (LLMs, databases, vector stores) in their own submissions, but the kit itself has no dependencies

## Data Storage

**Databases:**
- None required by the kit
- Participants may implement SQLite, vector indexes, or other storage in their `MEMORY_DIR`

**File Storage:**
- Local filesystem only
- `STATE_DIR`: Read-only workspace state snapshots
- `MEMORY_DIR`: Participant-managed persistent memory directory (read/write)

**Caching:**
- None - stateless evaluation framework

## Authentication & Identity

**Auth Provider:**
- Not applicable - local evaluation kit

**Implementation:**
- No authentication required for kit operation
- Participants handle their own auth for external services (LLM API keys, database credentials, etc.)

## Monitoring & Observability

**Error Tracking:**
- None integrated - errors reported via exit codes and stderr

**Logs:**
- Standard output/error streams from participant `run.sh` execution
- Exit codes used to signal success (0) or failure (non-zero)

## CI/CD & Deployment

**Hosting:**
- Local execution only
- No cloud platform required

**CI Pipeline:**
- None - kit is distributed as standalone files
- Participants run `check_submission.py` locally to validate their submission

## Environment Configuration

**Required env vars:**
- None - all configuration via command-line arguments

**Secrets location:**
- Participants manage their own secrets (if using external APIs)
- Kit itself has no secrets

## Webhooks & Callbacks

**Incoming:**
- None - kit does not receive external callbacks

**Outgoing:**
- None - kit does not initiate external calls

## Participant Integration Points

While the kit itself has no external integrations, participants may integrate:

**Common Patterns Observed in Examples:**
- `simple_memory.py` (`examples/simple_memory/`) uses only standard library
- Local memory stored as `.jsonl` files in `MEMORY_DIR`
- No API calls or external service requirements

**Recommended Participant Integrations:**
Per `CONTRACT.md`, participants may use:
- Vector databases (Supermemory, Cognee)
- Graph stores
- LLM APIs for embeddings/retrieval
- SQLite for structured memory
- Custom agent backends

All participant integrations must be documented in their submission README and must work offline with `STATE_DIR` and `MEMORY_DIR` only.

## Boundary Rules

**Kit Constraints on Participant Integration:**
- Participants only receive states released so far (no future data)
- No access to private evaluation data, judge packets, or answer keys
- No access to other candidates' memory or submissions
- `MEMORY_DIR` is the only durable benchmark-visible memory
- Any external service, model API, cache, or daemon must be documented in submission README

---

*Integration audit: 2026-06-18*
