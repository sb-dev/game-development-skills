# Bootstrap Research and Execution Tooling

**Status:** Family-candidate prototype  
**Revised:** 17 September 2026  
**Branch:** `feat/bootstrap-3`

## Operator model

The normal entry point is:

```text
/bootstrap
```

The user should not repeat stage numbers, research instructions, or supplied-book paths on each run.

## Local supplied-book convention

Put user-supplied book PDFs under:

```text
books/
```

Subdirectories are allowed; `/bootstrap` scans `books/**/*.pdf`.

Lifecycle:

```text
local PDF discovered
→ treat as user-supplied source
→ capture bibliographic/access metadata
→ apply corpus-selection and permission rules from the bootstrap
→ directly examine selected books when the extraction stage arrives
→ persist reading coverage and findings
```

The actual PDFs remain local working material and are gitignored. Durable logs record only repository-relative identifiers such as `books/<file>.pdf`, bibliographic metadata, access state, selection decisions, reading coverage and findings. Never persist absolute machine paths.

Do not upload supplied PDFs to Firecrawl or another external service without explicit user approval. Native/local reading is the default.

If more PDFs are supplied than the foundational corpus allows, follow the governing bootstrap's approval rules before excluding, replacing or demoting any supplied source. If a new PDF appears after corpus selection is already accepted, do not silently reopen the corpus; treat it as supplementary unless the process or user explicitly reopens selection.

## Skills

```text
/bootstrap
    ↓
bootstrap-stage-execution
    ├── bootstrap-research
    └── direct-source-extraction
```

`bootstrap-research` uses Claude Code `WebSearch` / `WebFetch` first and escalates to Firecrawl only for a concrete retrieval problem. `direct-source-extraction` owns local source inventory, meaningful reading, source-location traceability and reconciliation.

## Game-development research boundary

Use professional practice, primary design literature, official engine/platform documentation and actual game evidence as appropriate. Automated tests, simulations and telemetry can establish mechanical or behavioural evidence but must not silently substitute for human play evidence when the claim is experiential.

## Retrieval boundary

```text
WebSearch before Firecrawl search
WebFetch before Firecrawl scrape
local Read before external document parsing
```

Large Firecrawl outputs belong under `.firecrawl/`, which is gitignored. `books/` is also gitignored.

## Separation of responsibility

```text
HOW bootstrap research/execution works
→ reusable Claude skills

WHAT counts as game-development evidence and what each stage must produce
→ governing game-development bootstrap specification

WHAT this branch may execute
→ bootstrap execution contract

WHAT source files are locally available
→ books/**/*.pdf at runtime
```
