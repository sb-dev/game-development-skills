# Stage 11: Core skills and commands

**Date:** 2026-09-13  
**Branch:** `feat/bootstrap-2`  
**Governing stage:** [Bootstrap Stage 11](2026-09-07-game-development-skills-new-project-bootstrap-process.md#16-stage-11---design-core-skills-and-commands)  
**Output:** [Core Skills and Commands Contract](../contracts/skills-and-commands.md)

## 1. Accepted inputs and checklist

Read the complete Stage 11, [Stage 10 gap/over-engineering review](2026-09-13-stage-10-gap-analysis-and-over-engineering-review.md), [Stage 9 execution/installation contract](../contracts/execution-and-installation.md) and accepted production/evidence contracts referenced by those records. Their responsibilities and evidence requirements determine the split; skill count and professional job titles do not.

Acceptance: compare hypotheses A, B and C; derive the smallest coherent installable set; give each unit a responsibility and independent use/install boundary; give every selected command concrete inputs, outputs and composition/diagnosis/reuse/benchmark value; account for the example command candidates without inheriting them as mandatory names; record reasoning, verify actual design and commit the stage. No actual SKILL.md installation or runtime test is required by this design stage.

The available skill-creator guidance was read in full and applied to precise discovery, progressive disclosure, self-contained resources and behaviour-based validation. It adds no new permission requirement or dependency to this repository. Domain semantics come from the accepted project research, not from that authoring aid.

## 2. Architectural comparison

| Hypothesis | Task/isolation fit | Evaluation and installation consequences | Decision |
|---|---|---|---|
| A: `game-development`, `game-evaluate`, `game-extension-pack-creator` | Production keeps design, adequate proof, integration and repair together. Evaluation serves independent existing-game review. Pack authoring changes reusable behaviour rather than one game. | Production must bundle essential checking rules; evaluation and creator must carry their own needed resources. Three independent units have different output/authority boundaries. | **Selected.** Satisfies the observed responsibilities without extra mandatory handoffs. |
| B: separate `game-design` from playable `game-development` | Design-only work is legitimate, but is already a bounded production mode. No accepted example yet demonstrates an isolation need requiring another skill. | Adds discovery overlap and duplicate thesis/rule/authority guidance; production still needs enough design reasoning to diagnose implemented failures. | **Not selected now.** Reconsider only after actual standalone design use demonstrates a material context or evaluation advantage. |
| C: add `game-balance`, `game-level-design`, `game-playtest` | These are real specialised tasks but share current records, evidence rules and repair loops. Role labels do not show distinct installation requirements. | Separate units would duplicate accepted evidence and integration rules before any isolation benefit is demonstrated. | **Deferred.** Keep explicit commands/lenses; add a unit only after a concrete production/evaluation problem warrants it. |

The selected set has **3 installable skills** and **14 named operations**: 7 production, 6 evaluation and 1 pack-authoring entry point. This count follows the comparison; it is not a target imposed on future evidence. The core contract explicitly preserves design-only requests, standalone evaluation, production without the evaluator installed, and ordinary use without a creator or pack.

## 3. Disposition of all example command candidates

The bootstrap presents these as examples. Each candidate's useful behaviour is retained; merging addresses common input/output and proof boundaries rather than deleting capability. The 23 original names are reviewed below; newly selected names are designed operations, not aliases for already implemented commands.

| Original candidate | Selected operation | Reason and preserved distinction |
|---|---|---|
| define-game-thesis | define-game-thesis | Independent short thesis and experience-hypothesis record |
| design-mechanic | design-mechanic | Local rule/state semantics differ from runtime construction |
| model-system | model-system | Interaction and resource/strategy model with adverse cases |
| define-core-loop | model-system | Core loop is a composition relationship; preserve its named question without duplicating the record |
| prototype-mechanic | build-playable-proof | Includes adequate proof of a mechanic or bounded integrated loop; actual play remains required |
| greybox-level | integrate-content | Spatial composition lens preserves movement, routes, viewpoint and traversal checks |
| design-encounter | integrate-content | Encounter lens preserves information, agent/system composition and recovery requirements |
| integrate-content | integrate-content | Source/import/runtime and handoff correction boundaries remain explicit |
| tune-parameters | repair-gameplay | Tuning is an authorised hypothesis/change/rerun inside the accepted range, not a separate unobserved numerical edit |
| prepare-representative-build | prepare-playable-build | Representative target/purpose and required checks remain explicit |
| produce-release-build | prepare-playable-build | Release context adds its real quality/delivery/authority gates; no publication inferred from command invocation |
| validate-rules | validate-gameplay | Rules lens produces concrete expected-versus-actual assertions |
| test-state-transitions | validate-gameplay | Transition lens includes invalid/boundary/interruption/reset cases |
| check-reachability | validate-gameplay | Reachability lens includes actual content/dependency conditions and declared action privileges |
| evaluate-controls | evaluate-player-experience | Controls lens separates measured binding/response from human usability/feel |
| evaluate-feedback | evaluate-player-experience | Feedback lens checks state/cue relationship and appropriate perceptual evidence |
| evaluate-level-flow | evaluate-player-experience | Flow lens checks relevant traversal/discovery/pacing conditions; graph connectivity alone remains insufficient |
| evaluate-balance | evaluate-balance | Separate strategy, model/cohort and denominator analysis |
| evaluate-game-feel | evaluate-player-experience | Feel lens explicitly requires scoped human evidence for experiential claims |
| evaluate-accessibility | evaluate-accessibility | Core critical-task and input/presentation assessment; no automated completeness claim |
| evaluate-performance | evaluate-performance | Separate target, workload and measurement boundaries |
| diagnose-system-interaction | diagnose-gameplay | System-interaction cause remains a named diagnosis scope among rule/integration/evidence causes |
| recommend-smallest-repair | diagnose-gameplay | Recommendation includes responsible unit and preservation checks; source mutation remains production work |

`author-extension-pack` is the fourteenth selected operation and has its own responsibility boundary in the contract. Its detailed pack workflow and catalogue are deliberately left to their owning next stage, not replaced with an invented generic process here.

## 4. Responsibility coverage and evaluation obligations

| Stage 10 gap cluster | Production responsibility | Evaluation responsibility | Required future proof |
|---|---|---|---|
| S10-01/02: traceability and adequate prototype | Thesis/rule/system decisions and build-playable-proof | Check that the represented behaviour answers the claim | An actual brief-to-play trace with meaningful contrary evidence |
| S10-03/06/07: interactions, balance and flow | Composition, integration and bounded repair | Mechanical/strategy/experience lenses with distinct evidence | Coupled fault, diagnosis, repair and affected-case preservation |
| S10-04/05/12/13: diagnosis, feel and evidence | Essential evaluation embedded in production | Independent claim/method selection, collection checks and diagnosis | Mechanical execution plus real human evidence when claimed; no proxy substitution |
| S10-08/09/10: preservation, small repair and handoffs | Respect accepted scope/ranges and source/integration ownership | Explain responsible cause, proposed change and impacted consumers | Wrong-layer changes rejected; required correction closes its actual defect |
| S10-11/14/15/16: native access, target/access quality and installation | Select actual execution context and produce self-contained resources/build | Use existing native mechanisms and distinguish target/access limits | Engine/path evidence and clean isolated install per claimed unit |

Creator coverage concerns the separate first-class specialisation/authoring requirement. It cannot make missing core access or evidence responsibilities optional. Native skills consume the existing mechanisms identified as covered, rather than creating an inspector, installer or test framework.

### Existing benchmark questions that shaped command boundaries

The unexecuted [BC01–BC13 candidates](2026-09-13-stage-01b-five-book-extraction-and-reconciliation.md) and [BC14–BC16 additions](2026-09-13-stage-02-professional-practice-and-capability-model.md) were examined as evaluation-design inputs. This mapping preserves their question and pass boundary; it does not claim a final benchmark fixture or a run. The later benchmark stage must make the cases executable.

| Selected operation | Evaluation question that justifies its boundary |
|---|---|
| define-game-thesis | BC01: can it expose intent/incentive conflict without claiming achieved tension? |
| design-mechanic | BC02/BC05: can it state reset and boundary semantics precisely enough to detect an implementation fault? |
| model-system | BC04/BC13: can it explain reinforcing incentives or post-placement constraints beyond local validity? |
| build-playable-proof | BC03: does it reject inadequate paper-only evidence for a timing claim and produce the necessary runnable interaction? |
| integrate-content | BC06/BC07: can it preserve traversal and information through content/encounter integration without hiding a source defect? |
| repair-gameplay | BC11/BC02: does the correction restore the defect while preserving the accepted route/rule and authority? |
| prepare-playable-build | BC10/BC12: can it distinguish demonstrated scope and an actual self-contained build from an editor-only corner or compile pass? |
| validate-gameplay | BC02/BC13–BC16: do declared reset, reachability, agent, persistent-state or network invariants hold in the relevant real path? Conditional features are not imposed on every game. |
| evaluate-player-experience | BC05/BC07/BC08: are response events, comprehension, assistance and actual human accounts kept distinct? |
| evaluate-balance | BC04/BC08: are strategy assumptions, session boundaries and metric interpretation valid before tuning? |
| evaluate-accessibility | BC09: does the assessment identify a critical task's hue/sound-only barrier and demand equivalent usable information? |
| evaluate-performance | Stage 2 P12/G03 and Stage 10 S10-14: does the result identify target/workload and problematic intervals, rather than certify performance from an Editor average? |
| diagnose-gameplay | BC06/BC11/BC15: can it distinguish source/import, out-of-range design change and restoration/write failure and propose the correct repair owner? |
| author-extension-pack | Bootstrap specialisation gate: can authoring reject a cosmetic label-only pack or unsupported override/readiness claim against an exact core baseline? Concrete pack cases require the next stage's research. |

These questions explain why mechanical, experience, balance, access and performance evaluations retain separate proof boundaries even where individual candidate names are merged into lenses.

## 5. Design walkthroughs

These are synthetic request-routing and responsibility reviews, not usage benchmarks or installed-agent tests.

| Request | Expected route and boundary | Review result |
|---|---|---|
| “Write a short thesis for this game idea.” | game-development / define-game-thesis; stop at the requested design output | PASS |
| “Build this bounded prototype and fix its reset bug.” | game-development / build-playable-proof then repair-gameplay; embedded checks make evaluator installation optional | PASS |
| “Evaluate this independently developed game.” | game-evaluate using supplied expectations/build; no required game-development folder layout | PASS |
| “This imported doorway is half the agreed width.” | Integration/diagnosis isolates import versus source error; do not alter accepted movement to conceal it | PASS |
| “The screenshot looks fine; say the controls feel good.” | Experience/control lens distinguishes capture from human evidence; unsupported feel claim stays unverified | PASS |
| “Tune this parameter beyond its accepted range.” | Prepare a concrete changed-decision proposal under existing authority rules before material mutation | PASS |
| “Create a reusable specialist workflow.” | Pack creator authoring scope; does not rewrite a consumer game's settings or claim source/evaluation completion early | PASS |
| “Review the app's general code architecture.” | Existing engineering capability; no game-specific acceptance criterion requires these skills | PASS |

## 6. Verification

Re-read the complete original Stage 11 after drafting and inspected the actual contract and this record. Python counted **3** skill responsibility records, **14** unique operations (**7 + 6 + 1**), **23** original candidate dispositions and **8** labelled synthetic routing reviews; every disposition target resolves to a selected operation. Relative links/anchors resolve. Manual review checked that merged lenses retain distinct evidence requirements and that independent installation has no sibling-skill dependency. This is design verification, not an executed skill benchmark.

| Requirement | Evidence | Verification | Result |
|---|---|---|---|
| Derive the smallest coherent installable set | Hypothesis comparison; contract sections 1–2 | Three distinct responsibility/output boundaries; design-only work remains possible without an extra unit | PASS |
| Compare A, B and C | Section 2 | All three examined for task, isolation, evaluation, duplication and installation consequences | PASS |
| Define every skill's coherent responsibility | Contract sections 1–2 | Three units each have discovery scope, inputs, outputs, mutation boundary, required resources and independent evaluation question | PASS |
| Justify every selected command | Contract sections 3–6; benchmark-question mapping | Fourteen operations each have a bounded task/result and composition, diagnosis, reuse or evaluation value | PASS |
| Derive command surface from workflow and evaluation design | Sections 3–4 | All 23 original examples dispositioned; accepted BC01–BC16 questions and coverage gaps inform boundaries | PASS |
| Preserve standalone and selective use | Contract sections 1–2 and 7; routing reviews | Production includes essential checks; evaluator accepts external games; creator is optional; required resources stay within each unit | PASS |
| Keep execution and empirical limits explicit | Contract; sections 4–5 | Existing tools execute; eight reviews are labelled synthetic; no skill installation, participant or runtime result claimed | PASS |
| Persist and inspect actual output | Contract and this log | Original-section comparison, field/count/target checks and relative-link/anchor validation pass | PASS |

**Stage 11: COMPLETE.** Every installable responsibility and selected command meets the design exit criterion. Remaining Stage 11 blockers: none. Commit scope is the skill/command contract, this research record and the progress index. Remote verification precedes Stage 12.
