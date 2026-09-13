# Stage 6 — Levels, Content and Cross-Domain Handoffs

**Date:** 2026-09-13  
**Status:** Complete as an integration model with executed synthetic contract checks  
**Branch:** `feat/bootstrap-2`  
**Prerequisite:** accepted Stage 5 commit `7a30b85bfd52cbaf5f3a5269320859e1c2af61ab`  
**Output:** [Levels, content and gameplay handoffs](../contracts/content-and-handoffs.md)

## 1. Scope, acceptance and accepted inputs

The complete Stage 6 section of the [bootstrap specification](2026-09-07-game-development-skills-new-project-bootstrap-process.md#11-stage-6---model-levels-worlds-content-and-cross-domain-handoffs) was read before work. The acceptance checklist was: reconstruct the accepted spatial/content and ownership inputs; research all fourteen listed artefact concepts; specify delivery, integration and correction for all four handoff patterns; test those patterns; avoid an unsupported universal asset graph; persist the model, actual evidence and conformance before committing this stage alone.

Inputs inspected were the [charter](2026-09-12-stage-01-project-charter-and-domain-boundary.md), the [book findings](2026-09-13-stage-01b-book-findings.md), the [professional-practice model](2026-09-13-stage-02-professional-practice-and-capability-model.md) and relevant [source evidence](2026-09-13-stage-02-source-evidence.md), plus the accepted [thesis](../contracts/game-thesis.md), [behaviour](../contracts/gameplay-behaviour.md) and [prototype/commitment](../contracts/prototype-and-commitment.md) contracts. Earlier accepted outputs remain unchanged.

Totten's T1–T4 supply the spatial-task, information, greybox and measurement questions, with their accepted applicability limits. Swink S4 connects movement, camera and spatial context. Mechanics findings M5–M6 connect encounter composition and dependency checks. The Stage 2 responsibilities and R24 distinguish source delivery from import/customisation and resulting play. These are uses of the accepted, source-located extraction and reconciliation, not claims that the books were read again in full.

The charter's boundary remains controlling: adjacent disciplines retain specialist craft authority; Game Development owns gameplay intent and the integration into play; Engineering owns general software quality. Existing approval and reopening rules apply to changes in accepted intent, behaviour and substantial commitments. An integration failure alone does not authorise regenerating specialist work or changing an accepted controller.

## 2. Additional primary research

All three sources below were directly examined on 2026-09-13. Their implementation details motivate boundary questions; they do not select an execution engine or prove this repository has integrated assets.

| Source and examined scope | Finding used in this stage | Reading and inference limits |
|---|---|---|
| Epic Games, [Animation Notifies](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-notifies-in-unreal-engine), documentation displayed as Unreal Engine 5.8; overview, notify types, skeleton events, notify states and montage notify windows | An instantaneous event and an interval have different integration semantics. Record the animation/state binding, timing basis, attachment references and interruption behaviour. Source motion alone cannot establish the resulting action timing. | Read the documented mechanisms, not every linked page or video; no Unreal project, animation playback or editor/runtime comparison was executed. |
| Unity, [Audio Mixer](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioMixer.html), fixed Unity 6.0 manual; mixer groups/routing, snapshots, transitions and ducking | Supplied audio must be connected to runtime routing and state changes. A valid clip or state name does not establish that feedback remains audible when mixed with other signals. | No clips were auditioned and no mixer was executed. Platform support is conditional; this stage makes no Web or other target compatibility claim. |
| inkle, [Running Your Ink](https://github.com/inkle/ink/blob/master/Documentation/RunningYourInk.md), `master` as accessed; compiled story/runtime continuation, choices, state, variables, tags, external bindings and action/lookahead discussion | Story content and the game's interpretation of its tags, variables and events are separate responsibilities. A preview fallback is not evidence that the intended game binding exists. Side effects need the runtime's action/purity conventions rather than an assumption that every evaluation runs once. | The examined branch is moving, not a pinned SDK dependency. No Ink SDK was installed or executed; later tool selection must resolve actual version compatibility. |

The accepted Godot [import-configuration source R24](2026-09-13-stage-02-source-evidence.md#r24--source-assets-imports-and-retained-customisation) was also re-read in the repository's evidence register. It supports preserving the distinction among source assets, import settings and retained customisation. No new Godot execution or reimport result is claimed.

## 3. Model decisions and artefact coverage

The contract's fourteen-row artefact table gives each bootstrap concept minimum useful content, its consumer and an acceptance question. Level/encounter briefs connect player tasks and behaviours to conditions. Flow maps and critical paths expose alternatives and required dependencies. Spawn plans and greyboxes add temporal and playable spatial questions. Navigation, collision and reference contracts state consuming actors, units and meanings. Asset, animation, audio and narrative requirements state the properties to preserve across delivery. Performance budgets identify a target, workload and measurement; an unmeasured number is a target only.

These are concepts, not fourteen mandatory document types. They can live inside the accepted behaviour/composition or handoff records and inherit their lifecycle properties. This keeps uncertainty and correction local without losing ownership, evidence, approval or runtime expression. Non-spatial games record why geometry/navigation checks do not apply while retaining state, information and content obligations.

Each of the four handoff rows answers three different questions: what the producer must supply or disclose, what Game Development adds, and where correction belongs. Narrative intent remains with Narrative while gameplay trigger wiring belongs to integration. Source dimensions and imported dimensions are inspected separately. Animation markers and runtime playback conversion are distinct. Audio cues and runtime state routing are distinct. Agreements may allocate authoring work differently, but must name that allocation.

Rejected alternatives were a universal asset graph, a repository-wide tag vocabulary, automatic regeneration on any gameplay failure, and treating an editor preview or a resolved reference as integration acceptance. None is supported by this stage's evidence. Direct revision references and a compact project-native agreement are sufficient for the examined cases.

## 4. Executed handoff checks

The [fixture script](fixtures/stage-06-handoff-checks.py) was executed with Python 3.12.14 from the repository root:

```sh
python docs/research-logs/fixtures/stage-06-handoff-checks.py
```

The committed [actual result](fixtures/stage-06-handoff-results.json) records four patterns and twelve predicate evaluations: a baseline, an introduced defect, and a repair for each. All input values and deliveries are synthetic. The checks test requirements that can be represented as data/reference/arithmetic predicates; they are not an engine integration or an asset-quality validator.

| Pattern and fixed requirement | Introduced defect and actual diagnostic | Correction applied and owner | Observed sequence |
|---|---|---|---|
| Narrative: `door_open`, `met_guard` and once-only policy | Binding changed to unavailable `GateOpen`; `unknown_event_binding` | Restore the game binding; gameplay integration | ACCEPT → REJECT → ACCEPT |
| Environment/3D: 1.0 m actor width, 0.1 m clearance on each side, `traversable` tag | A delivered 1.3 m opening is imported at 0.5 scale, yielding 0.65 m versus the required 1.2 m; `insufficient_clearance` | Restore import scale to 1.0; gameplay/import integration | ACCEPT → REJECT → ACCEPT |
| Animation: `strike` inside 0.25–0.4 s at the fixture's playback rate, controller-owned movement | Delivered marker changed from 0.3 s to 0.6 s; `event_outside_window` | Correct the supplied marker; Animation producer | ACCEPT → REJECT → ACCEPT |
| Music/Audio: explore/alert states and a bound warning cue | Alert maps to absent `Danger` instead of delivered `Threat`; `unknown_mix_state` | Restore runtime mix mapping; gameplay/audio integration | ACCEPT → REJECT → ACCEPT |

Each repair changes only the faulty delivery or integration field. Assertions confirm that the required properties remain identical across all three variants and that no unrelated fixture data changes. The fixed expected diagnostic is checked, not just the presence of any error. Correction-owner labels are documented decisions under the agreement, not automated causal inference.

**Observed result:** `PASS`, four patterns, twelve evaluations, requirements preserved in every case. Runtime/perceptual validation is explicitly `false` in the results. These tests do not establish once-only runtime execution, collision response, animation blending, narrative quality, audible transitions, player comprehension or target performance. Those require the appropriate later execution and evaluation. Stage 6's required handoff-pattern tests are fulfilled at this model stage without claiming those later proofs.

## 5. Verification and handoff

After drafting, the full original Stage 6 section and actual contract were re-read. Verification inspected substantive coverage, counted fourteen artefact rows and four discipline handoffs, executed and inspected the twelve checks, and checked repository-relative links and anchors. The result file agrees with the executed output. Accepted earlier files are excluded from this stage's commit; the progress index is the only existing file updated.

| Requirement | Evidence | Verification | Result |
|---|---|---|---|
| Reconstruct accepted prerequisites and boundaries | §1 and linked accepted contracts/research | Checked specialist ownership, gameplay integration and existing authority against the charter | PASS |
| Research game-native artefacts | §§1–3 and contract §2 | Inspected primary research and accepted source-located findings; counted all fourteen listed concepts with consumers and acceptance questions | PASS |
| State what Game Development owns at integration boundaries | Contract §§1/3/5 | Traced delivered source, import/configuration, behaviour and resulting play as separate diagnostic locations | PASS |
| Define Narrative handoff | Contract §3 and narrative fixture | Checked intent/content delivery, gameplay state/trigger addition and conditional correction ownership; executed baseline/defect/repair | PASS |
| Define Environment/3D handoff | Contract §3 and environment fixture | Checked source properties, collision/traversal/encounter/camera/performance additions and producer versus integration repairs; executed clearance case | PASS |
| Define Animation handoff | Contract §3 and animation fixture | Checked motion/state/timing/movement delivery and additions; executed marker defect and producer repair | PASS |
| Define Music/Audio handoff | Contract §3 and audio fixture | Checked cues, runtime triggers, mix states and feedback ownership; executed unresolved-state case | PASS |
| Test all reusable handoff patterns | Script and recorded JSON, §4 | Four patterns × baseline/defect/repair = twelve evaluations; all expected outcomes and preservation assertions passed | PASS |
| Avoid premature universal cross-domain asset graph | Contract §§1/4; §3 alternatives | Inspected direct project-native references and scoped agreement; no universal graph or global schema introduced | PASS |
| Persist outputs, evidence and accurate status | Contract, script, results, this log and index | Inspected actual contents, local links/anchors and evidence limits; runtime/human proof remains unclaimed | PASS |

**Exit decision:** all mandatory Stage 6 requirements pass and no Stage 6 blocker remains. For each adjacent domain the model states the delivery obligation, gameplay addition and correction owner. After remote commit verification, the next stage is **Stage 7: playtesting, telemetry, tuning and balance**.
