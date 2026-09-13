# Precision Platformer: P1 specialisation and core baseline

**Date:** 2026-09-13  
**Pack:** `precision-platformer`  
**Phase:** P1 within Stage 12  
**Inputs:** [catalogue curation](2026-09-13-stage-12-catalogue-curation.md), [core skill/command contract](../contracts/skills-and-commands.md), [execution contract](../contracts/execution-and-installation.md), and the accepted [behaviour](../contracts/gameplay-behaviour.md), [prototype](../contracts/prototype-and-commitment.md), [integration](../contracts/content-and-handoffs.md) and [evaluation](../contracts/evaluation-and-tuning.md) contracts.

P1 acceptance is a bounded reusable specialisation with all eleven bootstrap definition areas resolved: use/non-use, reusable need, baseline, insufficiency of ordinary instructions, expected behaviour, relevant skills, constraints/defaults, preserved work, adjacent boundaries and provisional evaluation. This phase specifies a need and comparison baseline; it does not select books, complete extraction or claim production results.

## 1. Specialisation brief

| Required area | Decision |
|---|---|
| Intended use / non-use | Local, continuous-control platforming where repeated movement/jump execution through spatial challenges is central. Initially qualify bounded 2D run/jump play. Do not activate merely for side-view graphics, an occasional jump, turn-based tactics, autonomous simulation or a request for platformer art. Wall movement, dashes or other verbs require their own declared rules; they are not automatically added. |
| Reusable production need | Relate a measured movement envelope and input/contact behaviour to traversable geometry, information and retry structure; recheck those relationships after tuning or content replacement. |
| Core revision / baseline | Core design `10101f5e01661d6622964e2c0a030be7c7c1ad05`; core specified, not implemented/measured. Use the actual platforming need in section 2, with the same rules and resources in eventual core-only and packed runs. |
| Why core + ordinary project instructions is insufficient | Core already asks for controls, state, geometry and evidence. Repeating a game brief does not package a reusable procedure for deriving movement/landing cases, checking boundary input/contact, arranging demand progression and diagnosing controller-versus-layout failures. This is a reusable-depth hypothesis, not a claim that core is incapable of making one platformer. P7 must reject or qualify it if fair core/project-instruction comparisons show no useful benefit. |
| Expected specialised behaviour | Establish movement/control measurements before scaling a layout; derive legal routes and demanding boundary cases from them; compare feedback and input opportunities; test retry integrity; diagnose the smallest controller, contact, layout or cue correction while preserving accepted movement. |
| Relevant core skills | game-development: design-mechanic, model-system, build-playable-proof, integrate-content, repair-gameplay and prepare-playable-build. game-evaluate: mechanical, controls/feel/flow, access, performance and diagnosis operations as needed. Creator authors the optional pack; it is not a gameplay dependency. |
| Hard constraints | Preserve explicit/accepted movement, timing and layout decisions; state units and tested runtime; maintain declared collision/contact and outcome/reset rules; identify actual versus proposed evidence. Numeric movement targets and optional verbs are supplied by the game. Baseline accessibility remains core. |
| Soft defaults | Begin with a small controller/route sandbox and placeholder geometry; keep retries focused on the disputed movement sequence; prefer clear action/outcome feedback. Consider input buffering or edge tolerance as explicit design options to investigate, not mandatory features or universal timing constants. |
| What must remain stable | Accepted verb semantics, permitted parameter ranges, reachable required routes, goal/failure/reset, input alternatives and evidence provenance. A geometry change must not silently force retuning the controller; a controller change must not silently invalidate accepted geometry. |
| Adjacent-domain boundaries | Engineering implements the controller/native physics and tools. Environment/art produces agreed geometry/visuals; animation and audio own craft. The pack specifies gameplay envelopes, cues and integration checks without creating a new physics engine, commissioning final assets or copying a named game's style. |
| Provisional evaluation questions | Can the produced movement/geometry evidence reveal a boundary input or landing defect? Is the diagnosis at the correct layer? Does a scoped repair retain accepted routes and reset? Does a distinct room/verb configuration still benefit? Are automated results kept separate from human claims about precision, frustration or feel? |

## 2. Honest core baseline

The comparison need is a small original local platforming session with player-controlled horizontal movement and jumping, spatially demanding but declared legal routes, visible hazards/goal, a failure/outcome and restart. It must expose a meaningful movement or control question and preserve any supplied movement values and accepted route. Include practical input/feedback and accessibility constraints; the core run is not deprived of those requirements.

The baseline uses the selected browser proof path or another explicitly accepted native path, identical across comparison arms. Relevant project instructions, source/game assets, starting state, time/resource limits and evaluation criteria must match. Only pack activation and its packaged guidance should differ in the primary comparison. An additional core-plus-ordinary-project-instructions comparison may test whether packaging contributes beyond a longer brief. Do not design a weak generic core prompt to favour the pack.

The core contracts already require a playable interaction, actual technical checks, relevant human/target evidence, authority and small repair. Those are not claimed as pack inventions. The expected delta is the specialised workflow connecting **movement response → executable envelope → spatial demand and information → attempted traversal → controller/layout/cue diagnosis**. Its usefulness is not yet measured.

## 3. Boundaries of the proposed grammar

Movement measurements may include speed/acceleration or an equivalent response model, jump rise/fall and held/released behaviour when relevant, contact/landing conditions and the resulting traversable distances/heights. The pack must let the game choose its model and target; it cannot impose a particular engine integrator, universal jump equation or fixed player reaction threshold.

Spatial challenge concerns repeated player-controlled execution and information. A reachable destination under a privileged script is insufficient to claim human readability or an appropriate challenge. Input forgiveness, recovery cost and optional assists are design choices whose implications require evidence; neither harshness nor forgiveness defines quality by itself. P3/P4 must assess these provisional methods before they become operational guidance.

The pack does not add score-attack economies, procedural generation, metaprogression, networked play, mandatory gamepad controls or a mobile target by default. Those require their own project need and appropriate core/specialist evidence. A targeted correction should not regenerate an entire level or replace approved art if a smaller binding, contact or cue change is responsible.

## 4. Reuse and qualification decision

No existing pack is available to reuse. A reusable platforming method would be irrelevant to many tactical, narrative or non-spatial games, so it should not be embedded as a default in every core production request. Two independent briefs can exercise the same method with different geometry, movement relationships and failure causes; the exact showcase and additional fixture will be specified in P5 after research.

The specialisation provisionally meets the family qualification dimensions: repeated cross-project need, expected material production change, irrelevant detail if forced into core, a feasible bounded demonstration and a falsifiable comparison. P1 acceptance qualifies the **research direction**. It is not proof that a pack improves outcomes, installs correctly or is ready to use.

## 5. Verification and handoff

Re-read the original P1 requirements and catalogue decision, then reviewed the actual brief against the specified core. All eleven definition areas are explicit. The baseline retains the full production need, while conditional features and empirical claims remain bounded.

| Requirement | Evidence | Verification | Result |
|---|---|---|---|
| Bounded use, reusable need and relevant skills | Section 1 | Continuous platforming production grammar distinguished from viewpoint, asset style and general core work | PASS |
| Exact honest core baseline | Section 2 | Core commit and specified status recorded; equal substantive requirements and comparison conditions required | PASS |
| Explain specialised delta and core/project alternatives | Sections 2 and 4 | Reusable movement-to-layout procedure identified; no claim of measured core insufficiency | PASS |
| Define constraints, defaults and preserved work | Sections 1 and 3 | Hard accepted constraints separated from optional tolerance/recovery heuristics and project numbers | PASS |
| Respect adjacent boundaries and define evaluation questions | Sections 1, 3 and 4 | Native engineering/craft ownership retained; failure/repair, reuse and human-evidence questions falsifiable | PASS |

**P1: COMPLETE.** Research direction qualified; P2 selection, P3 extraction, P4 challenge and P5 profile are not yet complete. Implementation planned; evaluation not run; readiness not ready. Overall Stage 12 remains in progress. Next: the separately recorded five-book selection after this checkpoint is committed and remotely verified.
