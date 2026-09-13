# Stage 8 — AI skills, engines and execution capability landscape

**Date:** 2026-09-13  
**Stage:** 8, research AI skills, engines and tools  
**Branch:** `feat/bootstrap-2`  
**Specification:** [Bootstrap v1.1, Stage 8](2026-09-07-game-development-skills-new-project-bootstrap-process.md#13-stage-8---research-ai-skills-engines-and-tools)  
**Execution rule:** [Bootstrap execution contract](2026-09-13-bootstrap-execution-contract.md)

Existing tools provide credible documented paths for engine execution, inspection, testing, capture, generation and delivery. The domain project should delegate those operations and retain responsibility for game intent, behaviour semantics, project bindings, evidence questions, interpretation and scoped repair. This stage researches those paths; it does not select an engine or claim an installed capability proof.

## 1. Accepted inputs and stage acceptance

The accepted [charter](2026-09-12-stage-01-project-charter-and-domain-boundary.md) supplies the domain boundary, initial bounded local/single-player scope, engineering handoff and material commitment authority. The [Stage 2 capability model](2026-09-13-stage-02-professional-practice-and-capability-model.md) and [source evidence](2026-09-13-stage-02-source-evidence.md) supply professional responsibilities, gaps and initial engine leads. The five-book findings remain accepted through [Stage 1B](2026-09-13-stage-01b-five-book-extraction-and-reconciliation.md); this stage does not replace or demote a book.

The accepted contracts supply the questions that execution must answer:

| Accepted input | Consequence for this research |
|---|---|
| [Game thesis](../contracts/game-thesis.md) | A tool cannot choose the player's intended experience or convert an aspiration into an observation. |
| [Behaviour and systems](../contracts/gameplay-behaviour.md) | Code/test tools consume explicit rule/state definitions; interaction failures need the responsible dependency identified. |
| [Prototype and commitment](../contracts/prototype-and-commitment.md) | Choose a representation adequate for the question before comparing its cost; more tooling does not justify a larger commitment. |
| [Content and handoffs](../contracts/content-and-handoffs.md) | Importing an artefact does not establish its runtime binding, timing, collision, audibility or player-facing meaning. |
| [Evaluation and tuning](../contracts/evaluation-and-tuning.md) | Scripted, bot, human, telemetry and profiler evidence support different claims; preserve collection validity and tested conditions. |

Acceptance checklist used for this stage:

1. Read the complete original Stage 8 and the accepted domain/evidence inputs.
2. Research every one of its **27 named capability areas**, including instructional skills, native tools, runtime access, evaluation and delivery.
3. Record all **14 required fields for every candidate**, with current primary sources, consumption/prerequisite boundaries, maintenance and USE/ADAPT/REFERENCE/REJECT disposition. Stage 8 prescribes no candidate count; this examination produced **22**.
4. State which concrete operations existing tools should perform and which game-development responsibilities remain owned here.
5. Persist the landscape, candidate register, examined-source evidence and conformance review. Stage 8 requires research and repository verification, not installation or a runtime benchmark.
6. Inspect the actual outputs against the original section, repair failures, then commit only Stage 8 and the progress index; verify the remote commit and intended files.

## 2. Research result and dispositions

The [candidate register](2026-09-13-stage-08-candidate-register.md) contains **308 populated fields: 22 × 14**. Its classifications are **9 USE, 6 ADAPT, 5 REFERENCE and 2 REJECT**. Every disposition is conditional on the documented coupling and prerequisites. “USE” means the operation belongs with an existing tool when that path is chosen; it does not make all nine tools dependencies. “ADAPT” permits a small required binding, not a universal engine abstraction.

The [source evidence](2026-09-13-stage-08-source-evidence.md) records examined locations, versions/dates, reading limits and 15 repository metadata snapshots. Licence uncertainty is explicit: C01 remains a reference without copied instructions; C12, C19 and C20 required actual licence-file inspection after inconclusive API labels. C19's code licence excludes its example images/tiles. Provider tools are considered for consumption under their terms, not for source redistribution.

Two current findings refine the initial leads without changing historical accepted records:

- Roblox's standalone Rust MCP repository is archived and directs new integrations to built-in Studio MCP. C10 is the current conditional execution candidate; C11 is rejected for new integration. [Archived repository](https://github.com/Roblox/studio-rust-mcp-server), [current Studio MCP](https://create.roblox.com/docs/studio/mcp).
- Unity now deprecates the **Assistant in-editor MCP server** and documents an experimental CLI/Pipeline route. That deprecation does not include the CLI's `unity mcp` or third-party MCP servers. C21 therefore needs a bounded compatibility proof; C22 is rejected for new work. The CLI does not require a Unity AI subscription; Editor licensing remains separate. [Unity replacement guide](https://docs.unity.com/en-us/unity-cli/replace-mcp-server-unity-cli).

No engine ranking is inferred from stars, marketing demonstrations or operation counts. An engine's suitability for the selected project and the availability of its actual runtime remain decisions and evidence to establish in the owning later stage.

## 3. All 27 required search areas

Candidate IDs resolve to the register. A topic is researched when its primary-source-backed operation and relevant limitation are recorded; a row does not claim that operation ran in this repository.

| # | Required search area | Examined candidates | Existing operation to delegate | Domain/project obligation or uncovered limit |
|---|---|---|---|---|
| 01 | game-design Agent Skills | C01 | Host-agent design review instructions, as reference only | Preserve project authority, evidence and durable findings; no imported skill licence assumed. |
| 02 | gameplay programming skills | C02, C03 | Game-specific coding guidance and repository implementation | Supply exact semantics and runtime checks; one game's API guidance is not general engine expertise. |
| 03 | Unity skills / MCP / editor agents | C06, C07, C08, C21, C22 | Native Editor commands and optional agent bridges | Compare required access against current interfaces; separate beta, experimental and deprecated routes. |
| 04 | Unreal skills / editor automation / Python / commandlets | C09 | Editor Python/commandlets and native automation | Keep editor-only Python distinct from runtime tests; supply the intended level/context. |
| 05 | Godot skills / editor automation | C04, C05, C20 | Native CLI/scripts, optional MCP and project tests | Bind the project to a compatible installed version; a bridge is optional. |
| 06 | Roblox Studio AI / MCP | C10, C11 | Built-in data-model, Luau and playtest tools | Identify Studio instance and execution context; exclude archived bridge from a new path. |
| 07 | engine-agnostic coding agents | C03 | Code edits, Git diffs and invoking project tools | Own behaviour acceptance and interpret engine evidence; no second coding runtime required. |
| 08 | game-engine CLIs | C04, C06, C09, C21 | Import, script execution and build/run entry points | Record executable/version, arguments, logs, exit status and actual output identity. |
| 09 | scene / object graph inspection | C08, C10, C21 | Inspect scene/data-model objects via documented editor tools or Editor code | Map engine objects to game entities; editor state may differ from live state. |
| 10 | asset import automation | C04, C06, C09 | Invoke native import/editor scripting | Supply scale, origin, event, collision and dependency expectations from the handoff contract. |
| 11 | headless builds | C04, C06 | Native export or batch build methods | Matching templates/modules, explicit build settings and actual distributable checks are still required. |
| 12 | headless play | C04, C14 | Run the project without an interactive display; automate browser execution | Headless success cannot establish motion feel, sound or device input usability. |
| 13 | input simulation | C04, C09, C10, C14 | Runtime input events, automation driver or browser/Studio input tools | State the path exercised; Godot Input.parse_input_event reaches game input callbacks, not OS window switching. |
| 14 | replay systems | C09 | Native replication-based recording/playback | Identify recorded state, build/version and compatible serialization; a replay is not video or universal deterministic re-execution. |
| 15 | functional tests | C06, C09, C14, C20 | Existing project/level/browser test runners | Supply meaningful initial state, action, oracle and reset; Godot engine self-tests do not test the game. |
| 16 | screenshot / video capture | C04, C09, C10, C14 | Movie, screenshot comparison, Studio capture or browser video | Tie captures to runs and claims; fixed-rate capture is not a real-time performance measurement. |
| 17 | state inspection | C08, C09, C10, C18, C21 | Runtime/test hooks, explicit execution contexts and AI debugging | Inspect authoritative game state, not merely a visible cue or unrelated Editor object. |
| 18 | profilers | C04, C06, C08 | Native profiling or a bridge to it | Preserve target/workload and enabled measurements; target-player timings differ from Editor timings. |
| 19 | telemetry tools | C13 | SDK event transport and backend collection | Specify events, verify collection, retain revision/cohort/denominator; a local trace may be sufficient initially. |
| 20 | procedural-generation tools | C19 | Existing constraint-based candidate generation | Validate global reachability and play after placement; sample rights and random/failed cases remain explicit. |
| 21 | AI / behaviour-tree tools | C18, C12 | Existing authored behaviour runtime or learned policy tooling | Supply tasks, observations, actions and decision criteria; neither architecture implies good opponents. |
| 22 | navigation tools | C04 | Native path query, following assistance and avoidance | Project code moves the actor; navigation, physics collision and avoidance are distinct. |
| 23 | physics-debug tools | C04 | Native collision/debug visualisation | Check actual shapes, transforms and motion against rules; a debug drawing is only supporting evidence. |
| 24 | network simulation | C09 | Native lag/loss/order/duplication/jitter emulation | Define authority and recovery scenarios; synthetic settings do not represent observed players/networks. |
| 25 | automated playtesting agents | C12, C10, C14, C09 | Learned policies or scripted action sequences through existing runners | Declare policy, scenario coverage and oracle; agent success cannot establish human understanding or enjoyment. |
| 26 | accessibility validation | C15, C14 | Web-rule checks in exercised UI states | Add relevant human/device and gameplay checks; native, audio and canvas coverage is not established by axe. |
| 27 | store / platform build tooling | C16, C17, C04, C06 | Export/package with engine tools and deliver through platform tools | Preserve build identity and prove clean installation/play separately; publication keeps existing authority rules. |

## 4. Delegation boundaries

| Production responsibility | Existing execution owner | What game-development-skills should supply | Evidence to require when executed |
|---|---|---|---|
| Implement or repair game behaviour | Existing engineering agent and selected engine's language/toolchain | Accepted rule/state contract, smallest repair scope and affected consumers | Diff, build identity and relevant passing/failing runtime cases |
| Create/import/bind content | Engine importer and Editor API; asset production remains with its discipline | The delivery/integration/correction agreement and concrete bindings | Import outputs plus integrated behaviour checks |
| Build, run and inspect | Native CLI/Editor/runtime APIs; optional proven bridge | Project paths, target settings, expected state and bounded commands | Actual logs, exit/results, version and state observations |
| Execute technical scenarios | Existing test runner, input/replay facilities and optional policy package | Starting state, actions, invariants, adverse cases, seed/timing and reset requirements | Actual case results and coverage limits; preserve failures |
| Capture and measure | Existing capture, profiler and telemetry tools | Claim, target/workload, event/metric definitions and validity checks | Run-linked captures/traces and collection verification |
| Interpret experience and tune | Domain evaluator with relevant human input; tools supply observations | Separate mechanical correctness, strategy behaviour, comprehension, feel and balance claims | Stage 7 observation → diagnosis → smallest change → rerun → comparison → retain/revert record |
| Generate content or agent behaviour | Existing generator/AI runtime when needed | Constraints, project tasks, permitted variation and post-generation checks | Identified generated artefact/policy and validated scenarios |
| Distribute an identified build | Existing engine export and chosen platform tooling | Target, package/build identity, authorised destination and installation criteria | Delivery result plus a separate clean-install/play result |

Do not create an engine, generic scene graph, universal importer, coding agent, test runner, profiler, telemetry backend, behaviour-tree runtime, generator framework or store uploader merely to expose these capabilities. A necessary project harness can be ordinary code in the selected game; it must earn any later shared abstraction through actual reuse evidence.

Existing authority still covers routine reversible work. This research does not introduce a new permission checkpoint for every tool call. Material engine/platform cost or lock-in, changes to accepted game decisions and publication retain the charter's existing decision rules.

## 5. Gaps and limits retained for subsequent decisions

| Gap | Consequence for this bootstrap |
|---|---|
| Runtime availability and compatibility are unproved | No candidate can yet be called an installed capability. Select and execute the necessary path in the owning stage. |
| Documentation breadth is not failure recovery | A later proof must inspect missing process/project, invalid input, failed import/build and stale-result handling relevant to its operation. |
| Project state and test oracles are absent | Bind only the concrete rules, events and observations needed by the selected proof; tools cannot generate authoritative acceptance criteria. |
| Engine representations differ | Preserve meaning at the game contract level; do not promise equivalent runtime operations across all four engines. |
| Bot, telemetry and automated accessibility scope is limited | Keep human experience, relevant access needs and target conditions visible; do not mark them passed through proxy measurements. |
| Hosting, distribution and proprietary-platform access are conditional | Their absence does not block research; if required for an execution stage and unavailable, follow the contract's blocker rule. |
| Licensing and maturity differ by component | Reference-only and rejected candidates are not silently copied or installed; select a version and actual consumption route before implementation reliance. |

Stage 8 introduces no change to an accepted earlier contract. No custom integration, dependency installation, new engine commitment, telemetry collection or publication is included. Actual engine tests, playable proofs, benchmarks and installation results remain unperformed. The executed synthetic checks from Stages 4, 6 and 7 retain their original narrow scope and do not prove any candidate here.

## 6. Conformance verification

The complete original Stage 8 section was re-read and compared with the actual files after drafting. A Python inspection extracted the required topic list and field names from that section, compared the ordered 27-row matrix, and checked every candidate's field names and non-empty values. It also checked IDs, classification totals and 17 relative links/anchors across the three stage documents. Result: **PASS**. An initial parser incorrectly skipped the first field because the Markdown separator row used different spacing; the parser was corrected to exclude the header by name while retaining the exact 14-field requirement. No acceptance criterion was reduced.

Actual structural result:

```text
required search topics: 27; exact ordered comparison: PASS
candidates: C01–C22; missing/duplicate IDs: 0
required fields per candidate: 14; populated total: 308
classifications: USE 9; ADAPT 6; REFERENCE 5; REJECT 2
candidate references: resolved
relative links and anchors in stage documents: 17; failures: 0
```

Manual substance review inspected the capability, installation, licence, access, maturity, disposition and gap records against the examined sources. It specifically checked editor/runtime separation, project-test versus engine-test scope, native versus bridge responsibility, deprecation boundaries, source-code versus sample rights, and the absence of unsupported execution or experience claims.

| Requirement | Evidence | Verification | Result |
|---|---|---|---|
| Read the original stage and accepted inputs | Section 1; linked charter, Stage 2 and five accepted contracts | Complete Stage 8 re-read; operational decisions reviewed against those inputs | PASS |
| Research capabilities rather than brand names | Section 3 operation matrix; section 4 delegation agreements | Each row names an operation and project obligation, not a product ranking | PASS |
| Cover every prescribed search area | Section 3, rows 01–27 | Python compared all 27 names in order with the original specification | PASS |
| Record every candidate field | Candidate register C01–C22 | Exact 14 field names and populated values in all 22 records; 308 total | PASS |
| Establish current sources, licences, maturity and maintenance | Source evidence sections 2–3; register fields | Primary page/skill examination, 15 repository snapshots and actual licence files where API metadata was inconclusive; uncertainty retained | PASS |
| Distinguish behaviour class, access, coupling and consumption | All candidate records | Reviewed scripted/generative boundaries, Editor/runtime context and required installation inputs | PASS |
| State suitability, classification and gaps | Register dispositions and landscape section 5 | 9 USE / 6 ADAPT / 5 REFERENCE / 2 REJECT; each has a concrete reason or limiting condition | PASS |
| Make delegation to existing execution tools explicit | Section 4, eight responsibility rows | Reviewed tool-owned operations and domain-owned inputs/evidence; no replacement execution framework introduced | PASS |
| Preserve accepted decisions and evidence limits | Sections 1, 2 and 5; source evidence section 4 | Historical records remain unchanged; candidate selection is conditional; no installation, benchmark or gameplay result claimed | PASS |
| Persist research and verify actual outputs | Three Stage 8 documents and progress index | Inspected actual content, counts, references and link targets; progress record advances only to Stage 9 | PASS |

**Stage 8 result: COMPLETE as research.** All mandatory requirements and the capability-landscape/delegation exit criterion pass. Remaining Stage 8 blockers: none. Commit scope is these three research documents plus the progress index; remote commit/ref/tree verification follows the execution contract. Stage 9 has not been performed by this stage.
