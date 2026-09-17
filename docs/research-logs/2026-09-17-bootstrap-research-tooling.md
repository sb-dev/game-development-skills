# Bootstrap Research and Execution Tooling

**Status:** Family-candidate prototype  
**Date:** 17 September 2026  
**Branch:** `feat/bootstrap-3`

## Purpose

This branch adds the shared bootstrap operator model used across Production Skills projects without duplicating game-development methodology outside the governing bootstrap.

## Operator surface

The normal command is:

```text
/bootstrap
```

It reconstructs progress from repository state, resumes at the next incomplete stage, and continues through the remaining bootstrap until completion or a genuine user decision is required.

The user should not need to restate stage numbers, ranges, or the execution procedure on each run.

## Internal support skills

```text
.claude/skills/
├── bootstrap/
├── bootstrap-stage-execution/
├── bootstrap-research/
└── direct-source-extraction/
```

Only `/bootstrap` is the normal operator entry point. The other three skills are internal support capabilities.

### `bootstrap-stage-execution`

Owns the reusable stage loop: read requirements, execute, persist, verify, repair, commit, push, and return control to `/bootstrap`.

### `bootstrap-research`

Owns reusable research mechanics. Claude Code `WebSearch`/`WebFetch` remain the default path. Firecrawl is an escalation layer for richer search/extraction, site mapping/crawling, dynamic interaction, document parsing, and developer/tooling source retrieval.

Game-specific evidence rules remain in the governing bootstrap, including the distinction between mechanical/automated evidence and experiential human-play evidence.

### `direct-source-extraction`

Owns direct reading, source coverage, traceable extraction, reconciliation, and copyright-safe persistence for the Seed → Five → Challenge stages and Extension Pack research.

## Firecrawl policy

Use native Claude web tools first. Do not run `firecrawl setup defaults` and do not add a generic deep-research workflow that competes with the project bootstrap.

Large Firecrawl retrieval artefacts belong under `.firecrawl/`, which is ignored by Git.

## Source of truth

```text
HOW execution/research works
→ shared skills

WHAT game-development evidence counts
→ governing bootstrap specification

WHAT each stage must produce
→ governing bootstrap specification

WHAT branch/run is active
→ bootstrap execution contract under docs/research-logs/
```

No `.claude/bootstrap/` configuration layer is used.

## Branch rule

This feature branch is based directly on `main`. It must not inherit accepted stage state from earlier feature branches. `/bootstrap` reconstructs progress from `feat/bootstrap-3` only.
