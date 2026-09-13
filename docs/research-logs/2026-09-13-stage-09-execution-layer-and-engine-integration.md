# Stage 9: Execution layer and engine integration

**Date:** 2026-09-13  
**Branch:** `feat/bootstrap-2`  
**Governing stage:** [Bootstrap Stage 9](2026-09-07-game-development-skills-new-project-bootstrap-process.md#14-stage-9---choose-execution-layer-and-engine-integration-strategy)  
**Output:** [Execution and Installation Contract](../contracts/execution-and-installation.md)

## 1. Inputs and acceptance checklist

Read the complete Stage 9 and [execution contract](2026-09-13-bootstrap-execution-contract.md), the [charter](2026-09-12-stage-01-project-charter-and-domain-boundary.md), the [Stage 8 landscape](2026-09-13-stage-08-execution-capability-landscape.md), relevant [candidate records](2026-09-13-stage-08-candidate-register.md) and their [source evidence](2026-09-13-stage-08-source-evidence.md). The accepted [thesis](../contracts/game-thesis.md), [behaviour](../contracts/gameplay-behaviour.md), [prototype](../contracts/prototype-and-commitment.md), [integration](../contracts/content-and-handoffs.md) and [evaluation](../contracts/evaluation-and-tuning.md) contracts define the production meaning and evidence limits.

Stage acceptance is: separate production intelligence from all eleven named execution responsibilities; decide adapter placement, minimum inspection, tooling detection, engine-specific benchmarking and clean installation; justify a minimal architecture with explicit provider/engine boundaries; record research and verify the actual documents before a stage-only commit. No runtime benchmark or installation is required by Stage 9, and none is claimed here.

## 2. Decisions and alternatives

| Question | Selected decision | Alternative examined and reason |
|---|---|---|
| First bounded execution path | Local browser game; project-owned HTML/JavaScript, browser APIs and Playwright | Godot is the next native reference path; its import/scene tools are useful but unnecessary to establish the charter's first bounded loop. Unity/Unreal/Roblox add coupling/prerequisites without an established first-proof need. |
| Core versus execution | Skills own intent, constraints, evaluation and diagnosis; existing tools execute | A universal engine/coding-agent runtime duplicates Stage 8 capabilities and conceals real engine differences. |
| Adapter placement | Operation guidance in a skill's own references; concrete game bindings/tests in its example or consumer | Root-only references break selective installation; a separate package has no demonstrated independent reuse yet. |
| Minimum inspection | Eight conditional observations/actions tied to the claim | A mandatory complete scene graph, telemetry backend or debug protocol is unnecessary for a small rule proof. |
| Detection | Read project decisions; bounded probes; distinguish detected from verified operation access | Picking an engine solely because a binary exists or a plugin advertises a tool would conceal compatibility/context gaps. |
| Benchmark boundary | Versioned actual path, meaningful fault/repair and preserved behaviour | Mock passes and cross-engine score averages cannot establish native operation or target quality. |
| Installation | Standard selective Skills CLI installation; each skill carries required resources | Source checkout, sibling-skill or development-machine paths are hidden dependencies. |

The browser decision follows the charter's explicit desktop/browser candidate scope and Stage 8 C03/C14 delegation. It chooses a low-cost proof path, not a materially different thesis, paid platform or commercial commitment. Browser APIs execute rendering and input; the project writes ordinary game behaviour. No shared custom engine is proposed. Baseline access requirements remain core: semantic controls/status must accompany any Canvas playfield, and relevant human evidence remains necessary for experience claims.

## 3. Additional source examination and availability check

| Source | Actually examined | Decision supported / limitation |
|---|---|---|
| [Skills CLI README](https://github.com/vercel-labs/skills/blob/main/README.md) | Source formats, install/select/agent/copy options, project scope and agent path table on 2026-09-13 | Use the existing installer and discover actual output paths. Did not install this repository's future skills. |
| [Playwright installation](https://playwright.dev/docs/intro) | Installation, test execution, reports and current system-requirement body | Browser dependencies and test runner are separate from installed skills; pin actual versions during execution. |
| [Playwright page evaluation](https://playwright.dev/docs/evaluating) | Introduction, separate environments, argument passing and initialisation sections | A project-owned snapshot can be read in the real page context; the test process's own variables are not game state. |
| [MDN Canvas API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API) | API purpose and accessibility concerns | Browser rendering is adequate for a bounded 2D proof; Canvas pixels do not supply semantic object/accessibility information. |

An actual Python 3.12.14 executable-availability probe on 2026-09-13 found `node`, `npm`, `npx`, `python`, `git` and `ffmpeg` on PATH. It found no executable named `godot`, `godot4`, `Unity`, `unity` or `UnrealEditor`. This says only what those names resolved to in this workspace; it does not establish browser launch, engine absence everywhere, package availability or a clean-consumer install. No engine or package was installed in this stage. Architecture selection depends on adequacy and ordinary declared prerequisites, not on treating this probe as a support benchmark.

Stage 8's Unity Assistant MCP and Roblox bridge deprecations remain effective. The new architecture does not reinstate either rejected integration. The accepted research supports native operation guidance while leaving actual engine proof to its owning execution stage.

## 4. Architecture walkthroughs

These are **synthetic document reviews**, not runtime executions. They test whether the architecture gives an implementer a concrete decision without inventing access or evidence.

| Case | Challenge | Decision required by the contract | Review result |
|---|---|---|---|
| A1 | A browser test sees a win label but cannot inspect rule state | Read the game-owned state in the page and correlate with feedback; do not pass from the label alone | PASS |
| A2 | A Unity Editor responds while the requested target Player is absent | Record Editor access only; the target-runtime claim stays unverified and requires its actual path | PASS |
| A3 | Two Studio instances are open | Select the accepted project/instance and execution context before edits or play; ambiguity is not guessed away | PASS |
| A4 | A selected skill links to a root research log for essential instructions | Include the essential material in that skill's resource closure; validate the external copied installation | PASS |
| A5 | A native engine command fails but an old screenshot remains | Preserve the failure and reject stale evidence; rerun the corrected operation and capture | PASS |
| A6 | A project already uses Godot but the first example uses a browser | Honour the consumer's Godot decision, native project tools and matching proof; do not port it automatically | PASS |

## 5. Verification

Re-read the complete original Stage 9 after writing, then inspected the actual contract and research record. Python checked all 11 named execution boundaries, the eight architecture sections, six labelled document-review cases and 13 relative links/anchors: **PASS**. Manual review checked the five required decisions and the distinction between architecture, detected executables and executed support. No runtime/installation result was inferred from this verification.

| Requirement | Evidence | Verification | Result |
|---|---|---|---|
| Separate production intelligence from every named execution responsibility | Contract sections 1–2 | All 11 responsibilities have concrete execution owners and game-domain inputs/checks | PASS |
| Justify engine-neutral semantics without a common engine | Contract sections 1 and 4; accepted contracts | Shared semantics are production records; state, input and editor contexts remain native | PASS |
| Decide where adapters belong | Contract section 3 | Five placement decisions cover skills, references, helpers, examples/consumers and packages | PASS |
| Define minimum editor/runtime inspection | Contract section 4 | Eight conditional observations/actions; feedback, authoritative state and context remain distinct | PASS |
| Explain tooling detection and unavailable operations | Contract section 5; actual PATH probe in log section 3 | Read-only discovery, operation-specific status, target selection and bounded failures reviewed | PASS |
| Explain engine-specific benchmarking | Contract section 6 | Versioned actual operation, negative cases, repair and preservation; mocks cannot qualify an engine | PASS |
| Explain clean installation without hidden source dependencies | Contract section 7; examined Skills CLI documentation | Selective install, complete skill resource closure, separate prerequisites and external consumer proof specified | PASS |
| Produce a minimal architecture with explicit provider/engine boundaries | Contract; decision and alternative table | Browser first proof justified within charter; native alternatives retain their own evidence requirements | PASS |
| Persist and inspect actual stage outputs | Contract and this log | Original-section review, six synthetic walkthroughs, structural checks and 13 link/anchor checks pass | PASS |

**Stage 9: COMPLETE.** All mandatory architecture requirements and the exit criterion pass. Remaining Stage 9 blockers: none. The commit includes this record, the execution/installation contract and the progress index only. Remote ref, parent/tree, intended file hashes and preservation of earlier files are verified before starting Stage 10.
