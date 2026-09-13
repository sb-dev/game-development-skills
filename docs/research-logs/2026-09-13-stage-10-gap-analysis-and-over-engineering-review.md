# Stage 10: Gap analysis and over-engineering review

**Date:** 2026-09-13  
**Branch:** `feat/bootstrap-2`  
**Governing stage:** [Bootstrap Stage 10](2026-09-07-game-development-skills-new-project-bootstrap-process.md#15-stage-10---gap-analysis-and-over-engineering-review)

## 1. Inputs, method and acceptance

This review compares the required game-development workflow against the existing capabilities examined in [Stage 8](2026-09-13-stage-08-execution-capability-landscape.md) and its [candidate register](2026-09-13-stage-08-candidate-register.md), using the selected [Stage 9 execution architecture](../contracts/execution-and-installation.md). The [charter](2026-09-12-stage-01-project-charter-and-domain-boundary.md), [Stage 2 responsibilities P01–P16 and research gaps G01–G10](2026-09-13-stage-02-professional-practice-and-capability-model.md), and accepted [thesis](../contracts/game-thesis.md), [behaviour](../contracts/gameplay-behaviour.md), [prototype](../contracts/prototype-and-commitment.md), [integration](../contracts/content-and-handoffs.md) and [evaluation](../contracts/evaluation-and-tuning.md) contracts define the demand side.

The acceptance checklist is: compare the complete owned workflow; classify covered/partially covered/missing capability; explicitly examine all **16 named gap areas** and all **13 over-engineering flags**; justify native production intelligence only where existing capabilities are insufficient; record deferred architecture with a concrete reconsideration trigger; inspect this actual record against the complete original stage and commit it with the progress index. This is an analytical review, not an implementation or benchmark stage.

Classification describes the **scoped operation available from the examined external capabilities**, not implemented support in this repository:

- **covered:** an existing mechanism performs the stated operation; consume it with its prerequisites and project inputs.
- **partially covered:** mechanisms or useful instructions exist, but a required game-specific decision, binding, interpretation or preservation responsibility remains.
- **missing:** the examined candidates do not supply the required reusable production responsibility. This is a bounded finding about this research set, not a claim that no product anywhere can do it.

A documented core contract is a design input, not an installed skill. An external tool being classified covered does not claim we have run it. A gap in our implementation is not sufficient reason to rebuild an existing tool.

## 2. Required workflow versus existing execution

| Required production step | Available capability | Remaining production intelligence | Stage 2 coverage |
|---|---|---|---|
| Frame the intended play and question | C01 design critique; C03 can edit a brief | Relate audience, verbs, constraints, hypotheses and contrary observations; retain decision status | P01, P07 |
| Define rules, systems and appropriate proof | C01 arithmetic/review; C03 implementation; native runtime options | Specify state/actions/outcomes; choose adequate fidelity; inspect coupled incentives and omissions before committing | P02–P04, P10 |
| Build and integrate a bounded playable session | C03 coding; C04/C06/C09/C10/C14/C21 execution | Supply control/feedback intent, composition, content agreements, invariants and reset; inspect actual integrated play | P02, P05–P07 |
| Evaluate and diagnose | Native tests, input/capture, C12 policies, C13 telemetry, C15 web checks, profilers | Define assertions and meaningful cases, validate collection, distinguish human experience from proxies, diagnose the responsible layer | P04, P05, P08, P09, P11 |
| Correct and preserve accepted play | C03 diffs/repair; native reruns and version control | Bound the correction, preserve accepted revisions/ranges, compare effects and keep/revert on evidence | P10, P11 |
| Validate and deliver a playable candidate | Native builds; C16/C17 distribution; standard Skills CLI | Scope target and quality claims; verify independent skill consumption, identified build and installed play; retain release authority | P09, P12 |
| Extend only where the game requires it | C18 behaviour tools; C19 generation; native navigation/replay/network/storage facilities | Define agent knowledge/fallback, generation constraints, persistence/recovery or network authority and obtain corresponding evidence | P13–P16 |

P15 persistence is conditional on a game promising retained progress; it is not implied by restart. P16 networked sessions are not required by the local first proof. Their absence from that proof must remain a limitation rather than narrowing the domain charter. Specialist responsibilities stay subject to the later catalogue and evidence gates.

## 3. All 16 required gap areas

Row IDs S10-01–S10-16 are local to this review; Stage 2 G01–G10 keep their original meanings. Candidate identifiers refer to the Stage 8 register; standard installation refers to Stage 9's directly examined Skills CLI. The final column identifies concrete work and its closure evidence, not a new skill per row.

| # | Focus area | Classification | Existing coverage and relevant limit | Necessary native responsibility / closure evidence |
|---|---|---|---|---|
| S10-01 | player-experience to mechanic traceability | partially covered | C01 reviews intent and design; coding tools can store text. Neither establishes a selected revision linked to actual play evidence. | Connect intended choice/experience to behaviour and observation, retaining assumptions. Close through a consumer brief → rule → run/finding trace with unsupported experience claims kept open. |
| S10-02 | prototype selection | missing | Execution tools offer representations; no examined candidate supplies the accepted adequacy-before-cost decision with omissions and commitment limits. | Choose the least costly adequate proof for the named uncertainty. Show why rejected representations cannot answer it, then test the selected representation's actual behaviour. |
| S10-03 | system-interaction reasoning | partially covered | C01 arithmetic, C12 policies and C19 constraints expose subsets of behaviour; local correctness does not define the relevant combined scenario. | Trace shared state, feedback, resources and strategy assumptions; reproduce a coupled failure and repair its responsible relationship. |
| S10-04 | playtest diagnosis | partially covered | Native test/capture tools collect failures; C01 can critique. Neither makes a raw symptom's causal interpretation authoritative. | Compare expected/actual and collection integrity; separate rule, implementation, feedback, content and method defects; verify targeted repair. |
| S10-05 | game-feel evaluation | partially covered | Native input, capture and profiling observe events and timings; C01 provides advice. No tool establishes sensation or satisfaction. | Preserve device/control/feedback context; measure relevant events and obtain appropriately scoped human evidence when feel is claimed. |
| S10-06 | balance diagnosis | partially covered | C01 arithmetic and C12/C13 scenario/event facilities can expose trends. Optimisation or popularity does not establish fair or viable play. | Define units, strategies, cohorts and denominators; identify the controlling interaction, test alternatives and retain human/causal limitations. |
| S10-07 | level-flow evaluation | partially covered | Native scene, navigation and collision tools inspect geometry or routes. They do not establish discovery, pacing or integrated traversal. | Relate task/progression to actual movement, viewpoint, placement and cues; check routes after integration and appropriate first-use questions. |
| S10-08 | approved-decision preservation | missing | Version control preserves file history; the examined tools do not supply the charter's gameplay decision/reopen semantics. | Identify accepted thesis, rule/range/layout and affected consumers; distinguish an implementation fix from a material design change; demonstrate preservation in repair evidence. |
| S10-09 | small-scope repair | partially covered | C03 performs bounded code edits; native tests rerun. A small diff can still violate a large accepted dependency. | Locate the smallest sufficient responsible unit, retain authority and inspect downstream effects; require fault/repair and unaffected-case evidence. |
| S10-10 | cross-domain integration | partially covered | Native imports/editor tools and specialised content production provide artefacts and bindings. Import success does not determine gameplay suitability or correction ownership. | Apply producer-delivery/integration/correction agreements; check source, import and runtime separately, including timing and perceptual conditions. |
| S10-11 | engine-state inspection | covered | C04/C06/C09/C10/C14/C21 expose native scripts, test contexts or page/Editor access for declared paths. Project hooks and explicit context are still required. | Consume existing access, select the relevant authoritative values and correlate run identity. Do not write a new generic inspector; prove each claimed binding in its actual runtime. |
| S10-12 | automated mechanical playtesting | partially covered | Native runners, C14 and C20 execute assertions; C12 can supply policies. They do not choose complete game acceptance oracles. | Define initial state, actions, invariants, adverse cases, reset and policy limits; execute actual game tests rather than a duplicated model alone. |
| S10-13 | human evidence handling | missing | The examined execution candidates do not provide the accepted workflow for participant context, interventions, observations, accounts and scoped inference. | Embed the Stage 7 method in production guidance; record real evidence when required and explicitly distinguish it from expert/agent inference. Never fabricate participants to close the gap. |
| S10-14 | performance-budget validation | partially covered | Existing profilers measure chosen workloads; browser/native capture can expose spikes. They do not set appropriate gameplay budgets or certify untested hardware. | State target/workload, measurement endpoints and trade-offs; measure the actual path and preserve play while correcting the responsible cost. |
| S10-15 | accessibility | partially covered | C15 finds supported web violations; C14 exercises UI states. Input, timing, sensory, cognitive and native gameplay needs extend beyond that mechanism. | Make relevant access requirements core, trace critical tasks, provide alternatives, evaluate barriers and retain required human/device evidence limits. |
| S10-16 | installation | covered | Standard Skills CLI supplies named/selective installation and agent placement; existing package/engine tools supply prerequisites. It does not author correct self-contained skill resources. | Use existing installers; validate each skill's resource closure and perform clean external consumption. No custom installer, engine bundler or hidden source checkout. |

Totals: **covered 2; partially covered 11; missing 3**. Covered rows have explicit scope: native state access and installation mechanics. The remaining project inputs and execution checks are still required; they do not justify replacing those mechanisms.

## 4. Native intelligence justified by the gaps

The native work is the reusable reasoning and decision guidance across these gaps: frame an experience hypothesis and implementable rules; select an adequate proof; integrate controls/content into play; design and interpret evidence; diagnose and correct the responsible unit while preserving accepted work. The repeated accepted contracts show why these responsibilities belong together in game development. They do not establish a count of skills.

The next design stage must organise those responsibilities around distinct user tasks, inputs, outputs and repair/evaluation boundaries. It should not expose sixteen skills just because this table has sixteen rows, mirror the five books, or create one wrapper skill per engine/tool. Baseline accessibility and honest human-evidence handling apply across the workflow rather than becoming optional add-ons.

Do not encode general code generation, scene serialization, asset creation, platform packaging, test scheduling or metric transport as native expertise when existing engineering or specialist tools already perform them. Domain guidance may select and judge the operation. A concise engine reference or concrete game test can fill a binding gap without becoming a new product framework.

The browser-first architecture remains adequate for the initial bounded session and its mechanical evidence. It does not settle the example catalogue, claim human playtest success, prove all engine integrations or remove the charter's later target/quality obligations. Missing future execution evidence stays attached to its required stage.

## 5. All 13 over-engineering flags

No examined gap currently justifies building any of these general systems. “Deferred” means excluded from current bootstrap implementation unless a specific demonstrated failure makes a narrower solution necessary; it does not create a future promise to build the universal form.

| # | Architecture flag | Current disposition and smaller existing solution | Evidence needed to reconsider |
|---|---|---|---|
| O01 | custom game engine | Deferred; use browser/native engines and ordinary project game code | A required behaviour cannot be implemented adequately in available engines, with measured constraints and a bounded implementation case. A local game update loop is not a shared engine. |
| O02 | universal gameplay DSL | Deferred; use implementable behaviour examples and native code/data | Repeated independently implemented rules require a shared notation that demonstrably reduces error without hiding engine semantics. |
| O03 | universal entity-component system | Deferred; use each engine's native composition or simple project objects | Real projects demonstrate an unmet composition need after evaluating existing implementations; mere conceptual entity/state vocabulary is insufficient. |
| O04 | cross-engine runtime abstraction layer | Deferred; use explicit native operations and meaning-preserving production records | At least two real executed paths require substantially the same reusable operation and can retain material context through a narrow boundary. |
| O05 | custom scene editor | Deferred; use native editors or edit the bounded game's data | A demonstrated authoring task cannot be handled adequately by existing tools; compare an extension before a new editor. |
| O06 | universal asset pipeline | Deferred; use discipline handoffs and native importers | Repeated concrete conversion/integration failures remain after correct native configuration; justify a specific converter, not a universal pipeline. |
| O07 | general-purpose autonomous playtester | Deferred; use scoped scripted tests or an existing policy package | Defined exploration failures require more than scenario tests; compare policy coverage, cost and blind spots without experiential overclaims. |
| O08 | universal simulation platform | Deferred; use a bounded model or selected engine simulation | Independent models demonstrate a repeatable unmet execution need beyond existing libraries/engines. No such result exists here. |
| O09 | custom telemetry backend | Deferred; use local evidence files or a selected existing service | Actual collection volume/queries/constraints cannot be met by those options; measure the problem before building infrastructure. |
| O10 | universal behaviour-tree system | Deferred; use plain game logic or C18/native AI facilities | Existing systems fail a concrete required behaviour and a narrow extension cannot address it. |
| O11 | central provider router | Deferred; use the consumer's agent and explicit selected execution path | Multiple operational integrations produce a demonstrated coordination problem not solved by existing tooling; preserve provider-specific evidence. |
| O12 | universal game artefact graph | Deferred; use project-native records and resolvable references, with optional existing orchestration | Actual cross-record inconsistency justifies a specific automated validation/integration; do not invent manual graph maintenance or duplicate an orchestrator. |
| O13 | universal benchmark score | Deferred; retain separate mechanical, behavioural, semantic, performance, access and installation results | A narrowly defined decision needs an explicitly justified aggregate that cannot hide mandatory failures. It still cannot become a universal quality score. |

## 6. Follow-up candidates with bounded triggers

| Candidate | Smallest useful scope | Trigger and stop condition |
|---|---|---|
| Reusable game-state capture helper | An identified native operation shared by actual examples | Consider only after duplicate executed bindings show a maintenance defect; stop at the native helper boundary. |
| Seed/scenario generation aid | Inputs for a particular generator or policy | Consider when recorded failures expose uncovered cases; keep failed seeds and project acceptance outside the generator. |
| Decision-reference validator | Check exact accepted revision links/ranges in existing records | Consider when a real repair violates a retained decision; validate existing artefacts automatically rather than introducing a graph platform. |
| Additional engine operation reference | One materially different native operation | Add when an example needs it and can execute a supporting proof; do not promote unsupported engine breadth. |

These ideas do not block the core vertical and are not dependencies for it. Ordinary required gameplay tests and resource checks remain justified work; the restriction concerns building general infrastructure before evidence.

## 7. Conformance verification

Re-read the complete original Stage 10 and inspected the actual workflow comparison, classifications, native-intelligence justification and deferred-architecture rows. A Python comparison matched the exact ordered names of all 16 focus areas and all 13 flags against the specification, counted the 2/11/3 classification distribution and resolved 11 relative links/anchors: **PASS**. Review-local IDs use S10-01–S10-16 to avoid changing the meaning of Stage 2's retained gap IDs.

| Requirement | Evidence | Verification | Result |
|---|---|---|---|
| Compare the required workflow with available capabilities | Section 2; accepted P01–P16 and Stage 8/9 inputs | Seven workflow rows cover intent through delivery and conditional specialisation, with execution owners and remaining decisions | PASS |
| Classify covered, partially covered and missing work | Sections 1 and 3 | Definitions distinguish documented external mechanisms from this repository's unimplemented support; totals 2/11/3 | PASS |
| Examine all named gap areas | Section 3, S10-01–S10-16 | Exact ordered comparison with all 16 original names; each row identifies remaining work and closure evidence | PASS |
| Review all over-engineering flags | Section 5, O01–O13 | Exact ordered comparison with all 13 names; each has an existing smaller solution and reconsideration trigger | PASS |
| Justify native skills only for unsolved production intelligence | Section 4 | Reasoning, interpretation, integration acceptance and preservation retained; tooling wrappers and source-shaped decomposition rejected | PASS |
| Identify deferred architecture without blocking the vertical | Sections 5–6 | All 13 systems excluded absent proof; four narrow follow-up candidates have triggers rather than dependency status | PASS |
| Persist and inspect substantive output | This record | Full original-section review, actual content inspection, counts and 11 link/anchor checks pass | PASS |

**Stage 10: COMPLETE.** The native-intelligence justification and explicit deferred-architecture exit criterion pass. Remaining Stage 10 blockers: none. No implementation, benchmark or human result is claimed. Commit scope is this record and the progress index; remote verification precedes Stage 11.
