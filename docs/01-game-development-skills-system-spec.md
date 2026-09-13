# 01 — Game Development Skills System Specification

**Status:** Canonical design; implementation and installed proof pending  
**Version / date:** 1.0 / 2026-09-13  
**Design baseline:** Stages 1–14 through `074630827117357299c473ed04cd526fb0fdd3a2` on `feat/bootstrap-2`  
**Companion specifications:** [workflows](02-game-development-skills-workflows-and-artifacts-spec.md), [repository](03-game-development-skills-repository-and-contracts-spec.md), [evaluation](04-testing-and-benchmark-spec.md), [pack contract](05-game-development-customisation-packs-spec.md), [catalogue](06-game-development-extension-pack-catalogue.md).

These six specifications consolidate accepted domain decisions. The bootstrap still governs stage execution and acceptance. Historical contracts/research retain their evidence and revision meanings; creating canonical files does not establish implementation, quality, installation or maturity.

## 1. Mission and users

`game-development-skills` provides independently installable Agent Skills for turning player/product intent into designed, playable, evaluated and progressively refined gameplay. It owns game design **and playable integration**, including the reasoning that connects rules, runtime behaviour, player evidence and targeted correction. It does not merely produce a design document or route every decision to an engine.

Primary users are designers, gameplay developers and technical designers working alone or in small teams with an existing developer/coding agent and runtime tools. Larger teams use the same expertise for bounded systems, levels, encounters and integration milestones. The consumer owns its game, source/content, requirements, decisions and delivery authority; this repository owns reusable production guidance and domain evaluation.

An installed core skill must guide a clean consumer from a substantive brief or existing game through the requested production/evaluation scope, including an actual playable result when requested, a reproducible failure/diagnosis, the smallest sufficient authorised correction and preserved accepted work. Design-only and independent-review tasks remain valid bounded uses.

## 2. Domain scope and non-goals

The domain owns intended play, verbs, rules, mechanics, systems/loops, state/progression, controls/feedback requirements, game-feel questions, encounter/spatial gameplay, greybox and content integration, balance/tuning, evidence/diagnosis, baseline accessibility, gameplay performance budgets and playable delivery acceptance. It includes game-specific AI/navigation, persistent-state recovery and networked-session semantics when the game requires them.

| Game form / path | Qualification rule |
|---|---|
| Bounded local single-player | First end-to-end proof; actual installed production, input, outcome/reset, diagnosis and repair required |
| 2D and 3D | Both legitimate; each claimed path needs representative movement/input, collision, camera/information and content proof |
| Browser and desktop | Legitimate delivery paths; identify actual build/runtime, prerequisites, inputs and target evidence |
| Procedural / systemic / simulation-heavy | Require retained seeds/configuration, final-placement constraints, interactions/strategies and representative load; game simulation is not real-world validation |
| Local or networked multiplayer | Require actual distinct inputs/peers, authority/session/recovery, impaired-delivery conditions and appropriate human evidence; not a first-proof dependency |
| Mobile / gamepad / console / XR | No support claim until actual applicable tooling, devices, interaction, access, performance and platform evidence exist |

The Stage 13 curriculum plans genuine 3D and local multi-peer browser work after the first proof. That plan does not establish support today. Engine independence means portable production reasoning with distinct concrete execution, not identical engine semantics or automatic project conversion.

Non-goals include whole-studio scheduling/staffing, commercial or psychological guarantees, legal/platform certification, launch marketing, an autonomous guarantee of a large game, a new engine, universal gameplay language/ECS, scene editor, asset pipeline, autonomous playtester, simulation platform, telemetry backend, behaviour-tree framework, provider router, global artefact graph or universal quality score. A local game loop, project fixture or thin native binding is not automatically such a shared system; its scope must remain demonstrated and bounded.

## 3. Evidence-qualified foundation

The core corpus retains the supplied editions: Fullerton's *Game Design Workshop* fifth edition (2024), Adams/Dormans's *Game Mechanics* (2012), Swink's *Game Feel* first edition (2008 publication/2009 copyright), Totten's *An Architectural Approach to Level Design* second edition (2019), and Lemarchand's *A Playful Production Process* (2021). Stage 1B records identities, reading scope and thirty-five direct-source findings; Stage 2 separately challenges them and adds missing professional responsibilities. Membership is distinct from accepting every claim.

These sources inform capabilities, not a book-shaped skill architecture. Their claims include context-dependent methods and heuristics, not universal fun/balance/perception laws. Source availability is separate from examination; descriptions, model memory and citations cannot replace direct or adequately reviewed source evidence. Supplied-book removal/replacement/demotion needs applicable explicit authority; empty corpus slots can be filled under existing authoring scope. Private books/paths and substantial copied text are not public repository artefacts.

The sixteen retained responsibilities are experience hypotheses; actionable mechanics; adequate proof; systems/balance; controls/feedback; spatial/content integration; learnable encounters; evidence design/interpretation; accessibility; coherent scope/commitment; diagnosis/repair/preservation; playable readiness; procedural/emergent constraints; AI/navigation; persistence/recovery; and networked sessions. These are responsibilities, not sixteen installable skills. Detailed findings and source limitations remain in the [research index](research-logs/README.md).

## 4. Governing production principles

1. Start from the discipline and accepted project need. Tools execute; production guidance chooses the work and its acceptance.
2. Connect intended experience → rules/mechanics → runtime dynamics → observed behaviour/accounts → decision. An aspiration or accepted design is not an achieved experience.
3. Choose the least costly **adequate** representation. Preserve the variables needed to reveal a contrary result before optimising cost.
4. Prove a bounded playable vertical before architectural or content scale. Generated documentation, a successful compile or a polished corner is insufficient.
5. Evaluate local rules, interactions, strategies and edge cases. Correct components can compose into soft locks, exploits, inaccessible tasks or poor pacing.
6. Keep human play authoritative for experiential claims. Scripts, bots, telemetry and measurements support their own bounded questions.
7. Make accessibility a core quality responsibility. Optional packs may deepen it but cannot make basic access/information optional.
8. Preserve approved work and decision authority. Routine reversible work and tuning within granted bounds proceed; do not ask again for existing approval.
9. Diagnose the responsible relationship and make the smallest sufficient correction. Small diff size is not causal sufficiency; coordinated repairs are allowed when necessary and authorised.
10. Test the appropriate build/target and actual input path. Editor convenience, a state setter or a screenshot cannot supply omitted runtime/human/device evidence.
11. Keep standalone and selective installation real. No core consumer requires another family, creator, optional pack, source research or Pactwright.
12. Share later, after independent production evidence. At least two domains must demonstrate substantially the same need before a family abstraction is promoted.

## 5. Core skills and responsibilities

| Skill | Entry and owned outcome | Independence / authority |
|---|---|---|
| `game-development` | Design, build, integrate or refine playable gameplay from a brief/existing game; produce the requested thesis/rule/model, runnable proof, integrated change or build plus actual evidence and correction | Contains essential evaluation/repair guidance itself. Works without evaluator/creator/pack. Design-only remains design-only; production mutations follow accepted authority |
| `game-evaluate` | Independently evaluate rules, balance, player experience, access or performance and diagnose the responsible repair; produce actual scoped evidence, findings, limits and recommendation | Accepts project-native artefacts from other producers. Does not silently edit accepted gameplay just to make it pass; no production-skill dependency |
| `game-extension-pack-creator` | Research, author or revise a reusable game-development specialisation, implement/test it when in scope and maintain truthful readiness evidence | Owns `author-extension-pack`; not required to consume a pack. Reuses adequate prerequisites rather than restarting unrelated research |

There are **fourteen named operations**, not a new shell CLI: seven production (`define-game-thesis`, `design-mechanic`, `model-system`, `build-playable-proof`, `integrate-content`, `repair-gameplay`, `prepare-playable-build`), six evaluation (`validate-gameplay`, `evaluate-player-experience`, `evaluate-balance`, `evaluate-accessibility`, `evaluate-performance`, `diagnose-gameplay`) and `author-extension-pack`. Natural-language requests can invoke the same bounded operations. Specification 03 fixes their contracts.

The three-skill choice follows distinct output, mutation and independent-installation responsibilities. Separate design, balance, level-design and playtest skills remain unjustified until actual isolation/context/evaluation evidence requires them. Engine wrappers and provider agents are not additional core skills.

## 6. Execution architecture

Use the consumer's existing developer/coding agent and chosen native runtime/editor tools. The **first proof path is a bounded local browser game** using ordinary project-owned HTML/JavaScript, semantic controls/instructions/status, optional Canvas playfield and Playwright for actual browser input/state/capture. A small read-only game-state observation can support assertions; direct setup is labelled and cannot stand in for player input. No shared game engine is introduced.

Godot native commands/scripts are the next documented reference path; Unity, Unreal and Roblox retain separate optional context/tool contracts. Tool research classifies mechanisms, not installed support. Additional 3D or transport needs use appropriate existing libraries/tools and game-specific code with their own executed proof. No mandatory MCP, paid provider, second coding agent, hosted telemetry or execution router is required.

| Operation | Concrete owner | Domain instruction / acceptance |
|---|---|---|
| Code/editor/scene creation | Existing coding agent and native engine/project representation | Rule/state/composition intent, allowed mutation and actual runtime result |
| Asset generation | Relevant specialist/existing tool | Delivery properties, game meaning, source identity and integration checks |
| Build and delivery | Existing project/engine/package and platform tools | Target/source identity, complete dependencies, actual built play and authority |
| Input/state inspection | Native runtime tests/debugger or browser input/read-only observation | Correct project/session, actual input route, authoritative state and expected effect |
| Profiling/capture | Existing target/browser/engine facilities | Representative workload, measurement endpoints, meaningful view/modality and limits |
| Telemetry | Local project events or an explicitly selected existing service | Event/session meaning, collection validity, denominators and supported inference |

Detection sequence: read project instructions/manifests; identify plausible configured tools; make bounded read-only availability/version/context probes; record `verified for this operation`, `detected but unverified`, `unavailable` or `unknown`; choose an adequate native operation; install ordinary declared dependencies under existing authority where permitted; report an exact missing capability if it blocks required proof. A responding tool or filename does not establish correct project/context or build/run access.

Every execution identifies the project/build/tool, input/configuration, requested operation, expected output and bounded lifecycle. Inspect readiness, actual state and player-facing feedback, errors and outputs. On failure preserve diagnostics, distinguish unavailable/wrong context/invalid operation/game failure/invalid evidence, and rerun the corrected operation and affected checks. Stop only invocation-owned processes; stale captures or another project's success cannot close the current task.

## 7. Prototype, fidelity and commitment policy

Name the uncertainty and decision; identify required variables and evidence kind; compare representations and reject inadequate ones; compare effort, dependencies, integration/review, spend and reversibility among adequate options; execute the selected proof; retain result/limitations and decide keep, repair, reject, investigate or propose a larger commitment.

Rule uncertainty may use a table; economy a bounded calculation/simulation; movement a controller sandbox; combat an arena; camera a moving spatial scene; AI an inspectable encounter; flow a greybox; progression a dependency model plus integrated paths; procedural play a reproducible generator after placement; network semantics real peers under declared schedules; performance a representative target workload; comprehension actual relevant people with adequate cues. A cheaper representation cannot omit the disputed behaviour.

Fidelity covers rules, input/timing, feedback, space/content, system combinations, production workflow and target runtime independently. Written rules, simulation, mechanic toy, placeholder prototype, greybox, encounter, vertical slice, integrated content, target build and release candidate are useful contexts, not ten compulsory milestones. Retain useful prototype code or replace it according to evidence, not a blanket throwaway rule.

Review material commitments to thesis, mechanic, control, loop, representative content, slice, content volume and release candidate only as relevant. Existing approval persists. Before a new material decision supply concrete candidate/revisions, evidence and contrary findings, unresolved questions, cost/resource scope, affected accepted work and alternatives. The owner accepts/rejects/requests evidence; acceptance does not convert untested claims into proof. Out-of-range changes reopen only the affected decision and its consumers. Publication is a distinct authorised action.

## 8. Player evidence and quality policy

Mechanical correctness concerns specified state/rules and reachable outcomes. Balance concerns incentives, strategies, resources and progression under declared conditions. Experience concerns what relevant people perceive, understand and feel. Accessibility, content integration, performance, preservation and reproducibility remain separately inspectable quality dimensions. No opaque score can hide one failing dimension.

Automated tests, headless models, bots, telemetry, replay, expert review, human comprehension sessions, human experiential sessions and platform profiling have different proof scopes. Record actual inputs/observations, policies/knowledge, participant familiarity and assistance, build/cohort/session boundaries and limitations. Verify collection before interpreting it. Completion is not comprehension; a before/after improvement is not automatically causal; one expert is not an unfamiliar-player cohort; a seed is not global determinism.

Human experiential or first-use claims need appropriate actual participants. Missing people/device/modality evidence stays unperformed/blocked at its required gate. Baseline access includes relevant remapping/input alternatives, motor/timing demands, readable non-colour information, non-audio cues/captions where applicable, navigation/focus, pause/settings and complete task transitions. Technical checks do not certify all access needs or human satisfaction. Specification 04 owns methods, cases and actual-evidence gates.

## 9. Cross-domain integration

The producer owns specialist content/craft; Game Development defines gameplay use, integrates it and accepts resulting play. Engineering owns general implementation quality. One agent/person can perform several roles but must preserve the boundary and evidence.

| Handoff | Producer delivery | Gameplay integration / correction |
|---|---|---|
| Narrative → story/character intent | Accepted content/branches, variables, trigger and continuity expectations | Bind once/repeat/interrupt/save/reset semantics; repair wrong bindings without rewriting valid story intent |
| Environment/3D → playable space | Identified assets, units/axes/pivots, geometry/collision, sockets and dependencies | Import/place and test actual traversal, camera, contact, navigation and workload; distinguish source defect from integration scale/configuration |
| Animation → action/state | Compatible clips/rigs, timing/markers, transitions and movement contribution | Bind states/hit windows, interruption and single movement ownership; distinguish bad marker source from time conversion/playback fault |
| Music/audio → feedback | Identified cues/stems, loop/transition, mix/state and delivery properties | Route events/priorities, inspect actual audibility/meaning and alternatives; preserve valid craft while correcting integration |

UI/UX, visual/character art, video, research, legal/business and QA retain their specialist responsibilities. Gameplay supplies applicable requirements and acceptance, not a duplicate craft pipeline. A delivered asset is not yet integrated; an imported asset is not yet accepted gameplay. Use project-native versioned agreements, not a universal cross-domain asset graph.

## 10. Build order and current state

Research/design stages establish the domain, tools, skills, packs, examples and evaluation before broad implementation. Stage 15 creates these specifications; Stage 16 designs the public README; Stage 17 reviews other domains; Stage 18 scaffolds the repository; Stage 19 implements and proves one installed core vertical; Stage 20 expands to all fifteen primary examples and selected packs' P6/P7; Stage 21 validates repository/clean installation; Stage 22 handles optional Pactwright/maturity registration; Stage 23 reviews shared abstractions; final audit checks every original requirement.

Each stage is a substantive task with original criteria, accepted inputs, actual outputs, conformance verification, stage-scoped commit and remote verification before dependent work. A clean stage or context boundary is a checkpoint, not a reason to stop already authorised work. Genuine required missing input/capability/authority is reported precisely; no requirements are weakened to claim completion.

At this specification baseline, Stages 1–14 research/design are complete. Three skills are specified, fifteen examples designed, two packs have separate P1–P5 research and twenty core benchmark families plus eight routing probes are designed. **No operational skill/pack, playable example, human session, runtime benchmark, installed-use proof or readiness/maturity promotion is established by these files.**

## 11. System acceptance

Completion requires all original bootstrap outputs and exits, including six complete specifications; a coherent self-contained three-skill implementation; actual installed brief-to-play/evaluate/repair core proof; exactly five levels × three actual primary examples with exact prompts and evidence; implemented selected packs with exact showcases, distinct reuse, behavioural/precedence and fair core comparisons; appropriate human/access/target evidence; local validation and clean selective external installation; accurate public status; optional orchestration without runtime coupling; and evidence-backed maturity/shared-abstraction decisions.

An evaluation can finish with a negative finding, but an unresolved required production/quality/install gate remains failed or blocked. A pack may stay unproven if useful effect is absent; do not label it ready to force a catalogue claim. No merge, public release, PR readiness or maturity promotion follows merely from writing these specifications. Preserve real failures and repair the owning responsibility, then recheck affected downstream work.
