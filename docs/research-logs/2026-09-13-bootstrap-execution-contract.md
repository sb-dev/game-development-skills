# Game Development Skills — Bootstrap Execution Contract

Execute the bootstrap specification exactly as written:

https://github.com/sb-dev/game-development-skills/blob/main/docs/research-logs/2026-09-07-game-development-skills-new-project-bootstrap-process.md

**Repository:** `sb-dev/game-development-skills`  
**Working branch:** `feat/bootstrap`  
**Starting commit:** `a4fec4cc2b3623571481fc088abf74af7ec0a291`  
**Accepted completed work:** Stages 1, 1A, 1B and 2  
**Next stage:** Stage 3 — Define Player Experience and Game Thesis Model  
**Authorised remaining stages:** 3–23, in order

The bootstrap specification is the authority. This execution contract only controls how it is executed; it does not replace, simplify or reinterpret the bootstrap.

## Core rule

Treat **one stage at a time as the only task you have been asked to do**.

For every stage:

```text
READ THE STAGE IN THE BOOTSTRAP
→ extract every requirement and exit criterion
→ read accepted prior-stage inputs
→ complete all required research / design / implementation
→ create every required output
→ verify the actual repository against the stage requirements
→ repair every failure
→ commit only that stage
→ verify the remote commit
→ only then start the next stage
```

Do not batch stages. Do not optimise for reaching Stage 23.

## Exact requirements are exact

Never replace a required output with a representative or partial version.

Examples:

- `5 levels × 3 examples` means exactly 15 complete primary examples.
- `six canonical specs` means six complete specification files.
- required Extension Pack research means completing the specified P1–P5 work, not listing candidate packs.
- Stage 20 requires the specified P6–P7 implementation, demonstration, evaluation and installation/catalogue proof.
- `execute`, `test`, `validate` or `prove` means actually run the required work and record the result; describing what should happen is not enough.

Do not claim a stage complete because a research log or implementation plan exists.

## Before each stage

Re-read the relevant stage in the bootstrap and make a short acceptance checklist covering:

- required inputs and prerequisites;
- required research / activities;
- required deliverables and exact counts;
- required verification or execution;
- research-log output;
- exit criteria.

State the stage and its completion requirements before substantive work.

Use accepted repository outputs as context, not conversation memory.

Stages 1, 1A, 1B and 2 are accepted prior work. Do not rewrite them while executing later stages. If a later stage reveals a genuine defect that requires changing accepted earlier work, stop and ask me first.

## Verification gate

Before declaring a stage complete, re-read the original stage specification and verify the **actual outputs**, not your summary of them.

Record a conformance table:

| Requirement | Evidence / output | Verification | Result |
|---|---|---|---|
| ... | ... | ... | PASS / FAIL / BLOCKED |

A stage can be completed only when every mandatory requirement is `PASS`.

If a requirement fails, repair it and verify again.

Do not weaken a requirement, validator, benchmark or exit criterion to make the stage pass.

Do not invent research, source access, playtest evidence, player behaviour, benchmark runs, generated assets, test results, installation results or performance data. Synthetic fixtures must remain explicitly synthetic.

## Questions and blockers

If **any question requires my input**, stop the entire process and ask me.

This includes:

- ambiguous or conflicting requirements;
- missing required source material;
- a user-owned creative or technical decision;
- a proposed substitution, deferral or scope reduction;
- unavailable tooling needed to satisfy a mandatory requirement;
- permission to change accepted prior-stage work.

Do not answer on my behalf and do not continue to another stage while waiting.

## Commit gate

After all current-stage requirements pass:

1. persist the required research log and outputs;
2. persist the verification evidence;
3. commit only the current stage to `feat/bootstrap`;
4. verify the remote branch points to that commit and the intended files exist;
5. report the stage, verification result and full commit SHA.

Only then start the next authorised stage.

## Final gate

After Stage 23, perform a final audit against the complete bootstrap specification and its global acceptance requirements.

Do not claim the bootstrap complete, raise/mark a PR ready, publish, merge or promote maturity while any mandatory requirement is incomplete or unverified.

# Most important instruction

**COMPLETE EACH STAGE AS IF IT WERE THE ONLY TASK I ASKED YOU TO DO. THE BOOTSTRAP SPECIFICATION IS MORE IMPORTANT THAN THIS EXECUTION PROMPT.**
