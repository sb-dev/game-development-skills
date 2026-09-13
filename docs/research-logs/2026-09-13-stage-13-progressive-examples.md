# Stage 13: progressive example discovery and selection

**Date:** 2026-09-13  
**Branch:** `feat/bootstrap-2`  
**Outputs:** [Progressive Examples Contract](../contracts/progressive-examples.md) and five level prompt files linked there.  
**Status boundary:** Selection and complete prompt/design work only. No selected example has been generated, played, benchmarked or installed during this stage.

## 1. Inputs and acceptance

Read the complete original [bootstrap section 18](2026-09-07-game-development-skills-new-project-bootstrap-process.md#18-stage-13---design-progressive-examples). Reviewed the accepted charter's game/platform/quality boundaries; Stage 2 P01–P16 responsibilities, BC01–BC16 questions and evidence limits; the prototype/commitment, content/handoff and evaluation contracts; Stage 9 execution/install scope; Stage 11 skill/command boundaries; and completed Stage 12 pack profiles/authoring contract. The immediately preceding accepted checkpoint is `2e2d2016944013461e6b048e21932c5d959be2fe`.

Acceptance: derive each level's required capabilities, generate a larger pool, score against explicit coverage, remove substantially overlapping behaviour, select exactly three per level, inspect the entire fifteen-example set across all twenty coverage dimensions, and provide every complete copyable generation prompt. Level meanings remain hypotheses to test through actual implementation/evaluation. Stage 13 designs the curriculum; it cannot replace Stage 20's fifteen actual outputs with prompt files.

## 2. Candidate generation and scoring method

Generated **six candidates at each of five levels: thirty candidates**. This is deliberate design exploration using the accepted capability model, not an empirical survey or popularity ranking. Seed grammars were considered alongside alternatives and selected only for their contribution. No new source reading or measured quality result is implied by a candidate name.

Scores indicate **0 absent, 1 secondary/partial, 2 primary/adequate planned coverage** against the named column. They are ordinal design judgements supported by each premise and intended proof; they are not measured percentages, weighted quality or success predictions. A trio must meet its common level gate and cover complementary specialist columns. Do not sum away a missing gate. Where two candidates cover similar behaviour, prefer the clearer bounded proof and use the other only if actual execution exposes a gap.

### Level 1 — derive and compare one-mechanic proof

Common gate **G**: rules, actual input/state/feedback, basic tuning, small automated tests and smallest-scope repair. Distinct columns: **R** discrete rule/reset semantics; **T** continuous response/contact; **D** real 3D depth/transform/input.

| Candidate | G | R | T | D | Decision / coverage reason |
|---|---:|---:|---:|---:|---|
| L1-C1 Latch Room | 2 | 2 | 0 | 0 | **Select E01.** One crate/plate/gate dependency exposes legal/invalid/reset semantics in a complete small interaction |
| L1-C2 Rebound Lab | 2 | 1 | 2 | 0 | **Select E02.** Continuous input, time/contact, measurable tuning and repeated-contact failure complement discrete state |
| L1-C3 Depth Dock | 2 | 1 | 1 | 2 | **Select E03.** Genuine 3D transform/collision and depth cues add a new representation and repair boundary |
| L1-C4 Precision jump/dash sandbox | 2 | 1 | 2 | 0 | Defer at this level: strong seed, but response/contact overlaps E02 and platformer depth is explicitly represented later and in pack proof |
| L1-C5 Top-down dodge/attack arena | 1 | 1 | 2 | 0 | Move its coupled action/pressure ideas to later work; multiple combat mechanics weaken the single-mechanic question here |
| L1-C6 Multi-crate spatial puzzle | 2 | 2 | 0 | 0 | Remove overlap with E01; search complexity adds less curriculum breadth than the 3D case |

The selected trio covers all common requirements in each prompt plus the three distinct columns. A jump seed is not rejected as illegitimate; it loses this slot because of whole-set repetition and a more focused alternate contact proof.

### Level 2 — derive and compare complete-loop proof

Common gate **G**: goal, challenge, reward/failure, restart/retry, pacing and basic balance. **H** actual question-led human playtest; distinct columns **S** motor/score risk, **I** AI/information pressure, **E** coupled economy/opportunity.

| Candidate | G | H | S | I | E | Decision / coverage reason |
|---|---:|---:|---:|---:|---:|---|
| L2-C1 Spark Run | 2 | 2 | 2 | 0 | 1 | **Select E04.** Banking versus carrying creates score risk and exposes passive-strategy/session-log defects |
| L2-C2 Quiet Parcel | 2 | 2 | 0 | 2 | 0 | **Select E05.** Perception, guard knowledge and extraction add an information/AI loop and cue-comprehension question |
| L2-C3 Reservoir Shift | 2 | 2 | 0 | 0 | 2 | **Select E06.** Discrete gather/repair/upgrade decisions expose coupled costs, survival pressure and human consequence understanding |
| L2-C4 Unbounded idle factory | 1 | 1 | 0 | 0 | 2 | Defer: lacks a convincing bounded goal/outcome/retry proof as proposed; no end condition must be invented merely to claim completion |
| L2-C5 Duel score arena | 2 | 2 | 2 | 1 | 0 | Remove overlap: combines combat/opponent burden with the motor/score question covered more clearly by E04 |
| L2-C6 Timed maze escape | 2 | 2 | 1 | 1 | 0 | Remove overlap: route/time pressure contributes less distinct system coverage than E05's perception and E06's economy |

The three bootstrap loop seeds survive only after comparison; they address different decisions rather than three reskinned score loops. Every selected prompt requires actual human evidence at execution, not just a test plan.

### Level 3 — derive and compare representative slices

Common gate **G**: composed systems, content/level/encounter structure, progression, actual UI/audio/visual handoffs, performance budget and broader evaluation. Distinct columns **P** 2D traversal/content replacement, **T** tactical phase/progression, **D** 3D steering/camera/spatial integration.

| Candidate | G | P | T | D | Decision / coverage reason |
|---|---:|---:|---:|---:|---|
| L3-C1 Beacon Walk | 2 | 2 | 0 | 0 | **Select E07.** Three-room core-only traversal and source/import/runtime repair establish a substantive no-pack integration case |
| L3-C2 Switchyard Tactics | 2 | 0 | 2 | 0 | **Select E08.** Three tactical shunting encounters test the selected pack outside its defensive showcase and integrate phase/decision cues |
| L3-C3 Orbit Courier | 2 | 1 | 0 | 2 | **Select E09.** Extends the racing/time-trial seed toward 3D delivery, inertia/camera and approach visibility, with a complete route |
| L3-C4 Flat lap time-trial | 2 | 1 | 0 | 0 | Remove overlap: valid seed but provides less representation/camera breadth than E09 and repeats continuous-route evidence |
| L3-C5 Polished combat corner | 1 | 1 | 0 | 0 | Reject as proposed: attractive isolated presentation cannot establish representative progression or production integration breadth |
| L3-C6 Dialogue-only vignette | 1 | 0 | 0 | 0 | Defer as a game slice here: narrative craft without sufficient gameplay/system composition does not satisfy this level; narrative integration is covered in L5 |

E07's core-only selection prevents pack activation from being a hidden prerequisite for all traversal production. E08 reuses the tactical grammar without reusing the pack showcase premise. E09 earns the 3D extension through its own later execution evidence.

### Level 4 — derive and compare systemic scale/repair

Common gate **G**: multiple content units, interacting strategies/systems, procedural or systemic content, complex balance, regression, representative load and preservation. Distinct columns **R** generated progression/placement, **S** simulation/flow/persistence, **N** actual multiple peers/session recovery.

| Candidate | G | R | S | N | Decision / coverage reason |
|---|---:|---:|---:|---:|---|
| L4-C1 Seeded Vault | 2 | 2 | 1 | 0 | **Select E10.** Three-room runs over twenty retained seeds test integrated placement, resources and smallest generator repair |
| L4-C2 Canal Works | 2 | 0 | 2 | 0 | **Select E11.** Three connected flow scenarios, interacting policies, saved dependencies and 64/256-object workloads add systemic and recovery depth |
| L4-C3 Twin Signal | 2 | 0 | 1 | 2 | **Select E12.** Two rooms/two actual clients, authority and adverse delivery test a responsibility absent from single-runtime examples |
| L4-C4 One hundred authored rooms | 1 | 0 | 0 | 0 | Reject as proposed: content count alone does not demonstrate interacting systems or useful scale/repair behaviour |
| L4-C5 Loot-only roguelite | 1 | 1 | 1 | 0 | Remove overlap: random reward tables add less than E10's post-placement progression and resource dependency failures |
| L4-C6 Massive online world | 1 | 1 | 2 | 2 | Defer: broad label and operational burden lack a bounded adequate proof; E12 isolates the actual multi-peer need without claiming service scale |

Selection covers procedural generation, simulation and networked recovery separately. It does not collapse all three into one untestably large game. Dedicated later actual execution remains mandatory for the selected broader paths.

### Level 5 — derive and compare full-thesis production

Common gate **G**: coherent thesis, mechanics, systems, space, content, actual playtesting, balance, performance, access, local release validation and cross-domain composition. Distinct columns **P** full precision-pack production, **T** tactical/narrative campaign and creator review, **W** core-only 3D connected-world production. Pack coverage is also assessed across the trio.

| Candidate | G | P | T | W | Decision / coverage reason |
|---|---:|---:|---:|---:|---|
| L5-C1 Signal Orchard | 2 | 2 | 0 | 0 | **Select E13.** Finished three-level precision game tests the movement/space thesis, finish, play and local release together |
| L5-C2 Harbor Accord | 2 | 0 | 2 | 0 | **Select E14.** Three-mission tactical campaign adds narrative consequences, saved progress and bounded creator evidence review |
| L5-C3 Lantern Atlas | 2 | 0 | 0 | 2 | **Select E15.** Connected 3D world with persistent interactions integrates multiple disciplines while preserving a competent core-only path |
| L5-C4 Second polished platformer | 2 | 2 | 0 | 0 | Remove overlap: another controller/level premise adds less than campaign/world and no-pack coverage |
| L5-C5 Long procedural campaign | 1 | 0 | 1 | 1 | Defer as proposed: scope and content volume obscure completion and repeat E10; a future bounded campaign could be worthwhile |
| L5-C6 High-detail asset gallery | 0 | 0 | 0 | 1 | Reject as game proof: content-rich presentation without gameplay outcomes, systems and playtesting cannot deliver the thesis |

The three selected targets instantiate the bootstrap's complete-game, campaign/world and cross-domain slice directions, with concrete production and failure questions. “Polished” is not scored independently from whole-session behaviour or missing quality gates.

## 3. Whole-set review and prompt inventory

The [contract's twenty-row matrix](../contracts/progressive-examples.md#4-whole-set-coverage-matrix) assesses every requested dimension: 2D/3D, time/decision structure, precision/systemic, authored/procedural, physics, AI, player count, session/progression, level/world, platform/input, skills, commands, packs, faults, repair, performance, access, handoffs, benchmarkability and showcase clarity. It maps all fourteen selected operations and all sixteen source-derived candidate case contexts without claiming benchmark execution.

| Level | Exact count | Complete prompt file | Distinct selected outputs |
|---|---:|---|---|
| 1 | 3 | [level-1.md](stage-13-prompts/level-1.md) | E01 Latch Room, E02 Rebound Lab, E03 Depth Dock |
| 2 | 3 | [level-2.md](stage-13-prompts/level-2.md) | E04 Spark Run, E05 Quiet Parcel, E06 Reservoir Shift |
| 3 | 3 | [level-3.md](stage-13-prompts/level-3.md) | E07 Beacon Walk, E08 Switchyard Tactics, E09 Orbit Courier |
| 4 | 3 | [level-4.md](stage-13-prompts/level-4.md) | E10 Seeded Vault, E11 Canal Works, E12 Twin Signal |
| 5 | 3 | [level-5.md](stage-13-prompts/level-5.md) | E13 Signal Orchard, E14 Harbor Accord, E15 Lantern Atlas |

Each prompt stands alone: named installed skill(s)/pack selection, premise/scope, rules and project decisions to establish, meaningful playable output, input/feedback, actual proof requirements, negative/fault/repair and preserved work, local run/delivery instructions and honest evidence limits. It does not say “repeat the prior example” or count a plan as execution. The generation author is free to make ordinary bounded project choices and must record/verify them; this stage does not invent measured parameter quality.

Repeated traversal/tactical work has a deliberate progression: isolated behaviour at L1, loop coupling at L2, content/progression integration at L3 and full-thesis/delivery at L5. E10/E11/E12 have distinct failure ownership and are not additional platformer variants. Three genuine 3D tasks, a dedicated multi-peer task, procedural/stateful content, two researched packs and substantive core-only work prevent a one-genre curriculum.

Remaining breadth limits are explicit: browser delivery is the common accessible path; real mobile/gamepad, console, XR, internet-scale services and general performance across hardware are not proved. Input alternatives, camera and multi-client tests add meaningful variation without pretending to test absent devices. Adjacent content disciplines have actual source/delivery/integration work in the prompts; their family skills are not assumed installed. Human/modality/target requirements remain required where stated and can become genuine blockers during execution. None blocks designing these complete examples now.

## 4. Downstream evidence obligations

Stage 14 selects benchmark cases and develops defensible evaluation without removing curriculum gates. Stage 15 specification 04 consolidates the curriculum. Scaffold may create output paths, but Stage 19 must actually prove one installed core vertical and Stage 20 must produce all fifteen runnable examples plus the separate pack P6/P7 evidence. Each example's eventual README embeds the exact used prompt and records generated output, revisions/tools/commands, actual results, failures, corrections and limitations.

Examples are public product and regression surfaces. Meaningful escaped defects become the smallest adequate reproducible fixtures. Retain invalid evidence and unsuccessful runs rather than adjusting the oracle or hiding a failed seed. Do not install a generic engine, content platform or network service to homogenise otherwise independent examples. An actual larger-scope deficiency can justify a bounded later design change with preserved history; it cannot justify claiming a planned output is complete.

## 5. Conformance verification

Re-read original bootstrap section 18 and inspected the actual candidate tables, curriculum contract and all fifteen full prompts. Counted six candidates and three selections per level, five prompt files and fifteen standalone fenced prompts. Checked local links and that every level's required proof appears in its selected prompts. Review is design conformance, not executed game validation.

| Requirement | Evidence | Verification | Result |
|---|---|---|---|
| Read required accepted inputs and derive level capabilities | Sections 1–2; contract section 3 | Charter/capability/quality/pack boundaries retained; all five levels have explicit common gates | PASS |
| Larger candidate pool per level; no automatic seeds | Section 2 | Six candidates per level, thirty total; seed retention/adaptation/deferral reasons explicit | PASS |
| Score against coverage and remove overlapping behaviour | Five candidate matrices | Ordinal 0/1/2 scores with meaning and rationale; common gate cannot be averaged away | PASS |
| Exactly five levels × three primary examples | Section 3 and contract section 1 | Fifteen unique E01–E15 identities, three per level; pack showcase/reuse excluded from count | PASS |
| L1 rules/input/state/feedback/tuning/tests/repair | Level 1 prompts | Three different bounded mechanic proofs each include actual small tests, tuning and preserved local repair | PASS |
| L2 goal/challenge/reward/failure/retry/pacing/balance/human | Level 2 prompts | Three full-loop tasks require actual human sessions and distinguish their evidence from scripts | PASS |
| L3 composed slice/content/progression/handoffs/budget/evaluation | Level 3 prompts | Three representative slices, actual source delivery/integration, numeric project budgets and broader evidence | PASS |
| L4 scale/systemic content/balance/regression/load/stable repair | Level 4 prompts | Three-room seeds, three flow scenarios and two-room multi-peer work with fixed adverse cases and preservation | PASS |
| L5 full-thesis and broad cross-domain/pack/release coverage | Level 5 prompts | Three bounded complete productions, actual quality gates, both selected packs and core-only world, local candidate validation | PASS |
| Complete copyable generation prompt for every primary example | Five level files | Fifteen independent full prompts; scope, output, actual proof, fault/repair and run/evidence requirements present | PASS |
| Entire set inspected across all requested dimensions | Contract sections 4–5 | Twenty explicit dimension rows, all three skills/fourteen commands, failure contexts and platform limits | PASS |
| Deliberate curriculum rather than fifteen variants | Sections 2–3 and contract | Discrete/continuous/3D, AI/economy, content, generation/simulation/network and full-thesis responsibilities differentiated | PASS |

**Stage 13: COMPLETE as progressive-example design.** After committing and remotely verifying this stage, continue directly to Stage 14. All fifteen actual example outputs remain unperformed; remaining blockers for this design stage: none.
