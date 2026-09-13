# Stage 12: Extension Pack catalogue curation

**Date:** 2026-09-13  
**Branch:** `feat/bootstrap-2`  
**Scope:** catalogue curation only; the overall Stage 12 remains in progress until each selected pack completes P1–P5 and the authoring contract is complete.

## 1. Governing inputs and acceptance

Read [Bootstrap Stage 12](2026-09-07-game-development-skills-new-project-bootstrap-process.md#17-stage-12---design-extension-packs-and-pack-authoring), the canonical [Extension Pack process v1.0](https://github.com/sb-dev/production-skills/blob/main/docs/bootstrap/extension-pack-process.md), [family evaluation/pack contract v1.2](https://github.com/sb-dev/production-skills/blob/main/docs/specs/03-production-skills-evaluation-and-extension-packs.md), and [domain research process v1.0](https://github.com/sb-dev/production-skills/blob/main/docs/bootstrap/domain-research-process.md). All three canonical documents were directly read on 2026-09-13.

The domain inputs are the [charter](2026-09-12-stage-01-project-charter-and-domain-boundary.md), [Stage 10 classified needs](2026-09-13-stage-10-gap-analysis-and-over-engineering-review.md), [execution contract](../contracts/execution-and-installation.md), and [core skill/command contract](../contracts/skills-and-commands.md) at core-design commit `10101f5e01661d6622964e2c0a030be7c7c1ad05`. The core baseline is **specified, not implemented or measured**.

Curation acceptance: generate a broader candidate pool, classify each need, compare useful combined coverage, choose reusable complementary specialisations, identify core/project/adjacent alternatives, preserve existing state and clearly separate planned research from completed proof. This does not begin book extraction, implement a pack or claim comparative benefit. The canonical process's separate P-stage commits are checkpoints within the enclosing Stage 12.

## 2. Candidate pool and dispositions

The pool has **32 candidates**: all 23 examples in the domain bootstrap plus nine boundary/coverage probes. Candidates are production needs, not commitments to implement every label. No pack currently exists to reuse or migrate.

| ID | Candidate need | Classification | Disposition and rationale |
|---|---|---|---|
| CAT01 | precision-platformer | reusable specialised production behaviour | **Select for P1–P5.** Movement envelope, traversal geometry, input-window/recovery decisions and progressive execution challenges form a coherent repeated workflow. |
| CAT02 | arcade-score-attack | reusable specialised production behaviour | Planned; score opportunity, risk, anti-stall and repeat-session optimisation are distinct, but adding this now contributes less contrast than a discrete tactical workflow. |
| CAT03 | roguelite | reusable specialised production behaviour | Planned; run-reset versus retained progression and generated-route viability warrant separate evidence beyond a genre label. |
| CAT04 | tactical-turn-based | reusable specialised production behaviour | **Select for P1–P5.** Action economy, visible decision information, spatial legality and atomic turn/phase resolution differ materially from continuous motor execution. |
| CAT05 | survival-horror | reusable specialised production behaviour | Planned; resource pressure, information restriction and recovery could specialise behaviour; horror prose/art alone would not qualify. |
| CAT06 | stealth | reusable specialised production behaviour | Planned; perception, information, alert propagation and recovery need a specialised case set before selection. |
| CAT07 | fighting | reusable specialised production behaviour | Planned; adversarial move interaction, input/state timing and matchup evidence need dedicated depth and appropriate human/network scope. |
| CAT08 | racing | reusable specialised production behaviour | Planned; driving model, route/lap adjudication, assists and opponents require distinct evidence not provided by a platformer label. |
| CAT09 | rhythm | reusable specialised production behaviour | Planned; musical clock, judgement windows, calibration and accessible feedback introduce distinct timing/audio dependencies. |
| CAT10 | puzzle | insufficient distinction or evidence | Defer broad label; a concrete deduction, constraint-construction or spatial puzzle grammar may qualify later. |
| CAT11 | simulation / management | insufficient distinction or evidence | Defer broad label; specify a recurring model/decision grammar before creating a universal simulation pack. |
| CAT12 | 2d-side-view | one-project detail | Project execution/view constraint; perspective alone adds no independent production grammar. CAT01 may use it without owning all side-view games. |
| CAT13 | top-down / isometric | one-project detail | Project view/input/spatial representation unless further recurring behavioural differences are demonstrated. |
| CAT14 | first-person | existing core already covers it | Core camera, movement, feedback and access questions apply; a viewpoint alone does not establish a reusable specialisation. |
| CAT15 | third-person | existing core already covers it | Core viewpoint/occlusion/controller integration; a specialised camera/interaction grammar would need separate justification. |
| CAT16 | touch-first | existing core already covers it | Core must account for input constraints and access alternatives; hardware choice alone is not optional specialist quality. |
| CAT17 | gamepad-first | existing core already covers it | Core input mapping, configuration and task evaluation; do not duplicate it as a platform label. |
| CAT18 | local-multiplayer | broad game-development responsibility | Core-improvement candidate for multi-input/session boundaries when demonstrated; a more specific shared-play grammar could later qualify as a pack. |
| CAT19 | low-spec-mobile | one-project detail | Concrete target/workload/budget belongs to project instructions and core performance/access evaluation; no universal budget inherited. |
| CAT20 | deterministic-replay | broad game-development responsibility | Core execution/evidence capability when required; engine-specific implementation belongs to execution. A replay requirement alone is not a genre grammar. |
| CAT21 | short-session-arcade | insufficient distinction or evidence | Defer or merge with a qualified score-attack grammar; duration alone is a project constraint and overlaps CAT02. |
| CAT22 | high-density-simulation | one-project detail | Workload and performance target use core/native tooling until a distinct recurring simulation-production method is demonstrated. |
| CAT23 | networked-cooperative | reusable specialised production behaviour | Planned; coordinated player roles/recovery may qualify, with explicit separation from general networking, backend and security engineering. |
| CAT24 | baseline gameplay accessibility | existing core already covers it | Keep core; a pack cannot make inclusive input/information practice optional. |
| CAT25 | human playtest evidence handling | existing core already covers it | Keep core claim, participant/context, assistance and inference rules. |
| CAT26 | one level's jump height and layout | one-project detail | Consumer values and accepted geometry; not a reusable pack. |
| CAT27 | visual art style | adjacent-domain boundary | 2D/3D/environment/character production owns style and asset craft; gameplay accepts integration. |
| CAT28 | narrative genre or prose style | adjacent-domain boundary | Narrative Production owns it; gameplay branching/state requirements remain core or a qualified gameplay specialisation. |
| CAT29 | music genre | adjacent-domain boundary | Music Production owns composition/style; gameplay owns triggers and timing requirements. |
| CAT30 | cinematic language | adjacent-domain boundary | Video Production owns it; gameplay owns playback/interruption and return to play. |
| CAT31 | provider or model choice | one-project detail | Execution configuration; no demonstrated change to reusable gameplay grammar. |
| CAT32 | persistent-progress recovery | broad game-development responsibility | Core-improvement candidate under P15 when promised by the game; saved-state integrity is not a stylistic preference. |

The adjacent-domain classification is an explicit boundary exclusion under bootstrap section 17.2, not an additional Game Development pack category. “Planned” entries have no completed P1–P5, implementation, comparative evaluation or readiness claim.

## 3. Combined coverage and selected contribution

| Production dimension | precision-platformer | tactical-turn-based | Shared core that remains unchanged |
|---|---|---|---|
| Decision/time structure | Continuous movement and execution windows | Player-paced action selection and declared resolution phases | Explicit time basis, state transitions and constraints |
| Spatial play | Movement envelope, landings, hazards and retry routes | Legal movement, ranges, occupancy and encounter positions | Native geometry/data, integration ownership and reachability evidence |
| Resource/commitment grammar | Control commitment, failure/recovery cost and execution consistency | Action/opportunity costs, order, commitment and cancellation policy | Rules, accepted ranges, consequences and meaningful choices |
| Information | Readable action opportunities and feedback around attempted movement | Decision-relevant preview, legal/illegal actions and observable resolution | Redundant feedback, truthful state/cue mapping and access requirements |
| Progression and learning | Recombination of established movement demands | Recombination of actions, position and opponent information | Intended knowledge, encounter hypotheses and scoped human evidence |
| Characteristic failures | Landing/input boundary failure; layout broken by changed movement; excessive retry cost | Duplicate cost/action; stale preview; illegal occupancy; ambiguous turn resolution | Smallest sufficient repair, preserved decisions and actual reruns |
| Evidence | Movement/state/input traces plus actual traversal and relevant human experience | State/action traces, legality/adjudication cases and relevant decision/comprehension evidence | Separate correctness, experience, access and target claims |
| Feasible initial representation | Bounded 2D browser playfield | Bounded 2D browser grid/board | Declared runtime and normal dependencies; feasibility is a design assessment, not executed support |

The selected set has **two packs** because these directions cover materially different production and evaluation decisions while remaining compatible with the bounded core proof. They are not two perspectives on the same task. Their intentional overlap is core rule/evidence/integration discipline; specialised guidance must add the distinct decision process, not repeat that core.

Catalogue size is unrelated to the five-book rule. Other candidates remain available for later qualification; this selection does not exclude legitimate game forms from the charter or claim comprehensive specialist coverage. There is no existing approved pack identity, install interface or showcase to migrate.

## 4. Alternatives and research gates

A project may request either game form using core plus ordinary project instructions. That is the honest baseline, and it must include the substantive production need. The pack hypothesis is that packaging its specialised decision/evaluation procedure adds reusable depth or consistency across distinct briefs, with less repeated instruction and no unacceptable regressions. This hypothesis remains unmeasured.

For each selected pack, P1 must justify that difference against core at `10101f5e01661d6622964e2c0a030be7c7c1ad05`; P2 must compare a broader book pool and select five independent works; P3 must meaningfully examine the intended contributions or review adequate direct-source reuse; P4 must challenge specialised claims and gaps; P5 must define operational rules, negative cases, exact showcase prompt and distinct reuse fixture before implementation.

The five supplied books remain the approved **core** corpus. This curation does not assign or remove any book from a pack corpus. New pack selection must assess contributions independently and preserve source permission/access rules. Reusing evidence never makes books or other research logs installed runtime dependencies.

Core improvement is the answer when the need is general access, evidence integrity, persistence or basic native execution. Project instructions are the answer for one game's numeric values, layout or chosen provider. An adjacent discipline is the answer for art, prose, music or cinematography. A qualified optional pack is appropriate only for materially different reusable gameplay-production behaviour.

## 5. Current evidence status and verification

| Selected entry | Curation | P1 | P2 | P3 | P4 | P5 | Implementation | Evaluation | Readiness |
|---|---|---|---|---|---|---|---|---|---|
| precision-platformer | Selected for research | Planned | Planned | Planned | Planned | Planned | Planned | Not run | Not ready |
| tactical-turn-based | Selected for research | Planned | Planned | Planned | Planned | Planned | Planned | Not run | Not ready |

No selected entry is called researched, implemented or ready by this curation record. Separate phase logs will supersede the corresponding planned status without rewriting this historical checkpoint. The progress index tracks the current phase; the final Stage 12 synthesis will consolidate actual status.

| Requirement | Evidence | Verification | Result |
|---|---|---|---|
| Read canonical and accepted domain inputs | Section 1 | Complete canonical process/contract/research rules and relevant core boundary examined | PASS |
| Compare a broader candidate pool | Section 2 | 32 candidates include all 23 bootstrap examples plus nine boundary/coverage probes | PASS |
| Classify every need and consider alternatives | Sections 2 and 4 | Core, project, core-improvement, specialist, deferred and explicit adjacent-domain decisions recorded | PASS |
| Assess complementary coverage as a set | Section 3 | Two distinct continuous/discrete production grammars compared across eight dimensions | PASS |
| Preserve core independence and earlier decisions | Sections 3–4 | No core, book or existing pack change; no implicit package dependency | PASS |
| Distinguish planned research from proof | Section 5 | Both entries have P1–P5 planned and no implementation/evaluation/readiness claim | PASS |

**Catalogue curation: COMPLETE. Overall Stage 12: IN PROGRESS.** Per-pack work begins only after this checkpoint is committed and remotely verified.
