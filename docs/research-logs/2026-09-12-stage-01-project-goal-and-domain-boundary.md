# Stage 1 — Project Goal and Domain Boundary

**Project:** `game-development-skills`  
**Bootstrap stage:** 1 — Define Project Goal and Domain Boundary  
**Status:** Complete  
**Date:** 12 September 2026

## 1. Stage purpose

This stage defines what `game-development-skills` owns before book selection, broader professional research, engine/tool research or skill architecture begins.

The project is a Production Skills repository for reusable expertise that turns a game premise into **playable, integrated and evaluable gameplay**. It does not stop at abstract game design, and it does not expand into a general-purpose game-engine framework or software-engineering repository.

The core boundary is:

> `game-development-skills` owns reusable production intelligence for designing gameplay, proving it cheaply, integrating it into a playable runtime, evaluating observed behaviour, and directing the smallest sufficient gameplay correction.

The repository therefore owns **game design plus playable integration**. General implementation engineering, specialist asset production and consuming-project governance remain adjacent responsibilities.

## 2. Canonical inputs reviewed

This charter is grounded in the current repository bootstrap and Production Skills family contracts:

- [`2026-09-07-game-development-skills-new-project-bootstrap-process.md`](2026-09-07-game-development-skills-new-project-bootstrap-process.md)
- [`production-skills/docs/bootstrap/README.md`](https://github.com/sb-dev/production-skills/blob/main/docs/bootstrap/README.md)
- [`01-production-skills-family-system.md`](https://github.com/sb-dev/production-skills/blob/main/docs/specs/01-production-skills-family-system.md)
- [`02-production-skills-project-contract.md`](https://github.com/sb-dev/production-skills/blob/main/docs/specs/02-production-skills-project-contract.md)
- [`03-production-skills-evaluation-and-extension-packs.md`](https://github.com/sb-dev/production-skills/blob/main/docs/specs/03-production-skills-evaluation-and-extension-packs.md)
- [`04-cross-domain-orchestration-and-integration.md`](https://github.com/sb-dev/production-skills/blob/main/docs/specs/04-cross-domain-orchestration-and-integration.md)

No Stage 1A book selection, Stage 1B source extraction, Stage 2 professional-practice challenge research, engine selection or proposed skill decomposition is performed here.

## 3. Project goal

The mature project should make game-development production behaviour installable and reusable across consuming projects.

A successful installation should be able to help a consuming project move through a game-development reasoning loop such as:

```text
player / product intent
→ game thesis
→ verbs, rules and mechanics
→ cheapest adequate playable proof
→ observed play behaviour
→ human and measurable evidence
→ deliberate commitment
→ systems / content integration
→ representative playable slice
→ evaluation and diagnosis
→ smallest sufficient correction
→ target-platform validation
→ playable delivery
```

This is a production responsibility, not a mandatory universal workflow schema. Different games may need different artefacts, fidelity steps and iteration loops.

The project should encode the reasoning required to decide **what needs to be playable, what evidence is sufficient, what should be preserved, what should change, and which adjacent discipline or execution tool owns the concrete operation**.

## 4. Target game-development outcomes

`game-development-skills` should ultimately support the following outcomes:

1. turn an initial game premise, player need or product constraint into a testable gameplay thesis;
2. define core verbs, rules, mechanics, state transitions, systems and loops precisely enough to implement and evaluate;
3. select the cheapest representation capable of answering the current gameplay question;
4. produce or direct a playable prototype before expensive production is committed where playability is material to the decision;
5. connect intended player experience to implemented rules and observed runtime behaviour;
6. integrate gameplay-relevant outputs from narrative, UI/UX, art, animation, audio, music, environment and engineering disciplines into a playable whole;
7. plan and interpret playtests, telemetry, simulations and deterministic checks without confusing automated evidence with human experiential judgement;
8. diagnose failures at the responsible gameplay layer and correct the smallest sufficient unit while preserving approved work;
9. establish game-specific performance, accessibility, control, feedback and runtime acceptance requirements;
10. validate representative behaviour on the target platform or an adequately representative build path before release-quality claims are made;
11. produce reproducible evidence explaining what was tested, what was observed, what was changed and what remains uncertain.

## 5. Intended users

The primary users are people or agents responsible for getting gameplay from intent to a validated playable state, including:

- solo developers and small teams that need disciplined game-design and integration guidance;
- game designers working directly with engine/editor or coding execution layers;
- gameplay engineers who need explicit design intent and acceptance criteria rather than only implementation tasks;
- technical designers bridging rules, content, scripting and runtime behaviour;
- multidisciplinary teams composing several Production Skills families;
- AI coding/editor agents that need domain production direction rather than unconstrained implementation freedom;
- consuming-project orchestrators that need an installable game-development capability while retaining project governance themselves.

The repository is not restricted to professional game studios, but its reusable guidance should be strong enough to support professional production behaviour rather than only tutorial-scale exercises.

## 6. Supported project scales

The production model should scale across three useful bands:

### 6.1 Bounded prototypes and experiments

Examples include an isolated movement controller, combat arena, economy simulation, puzzle rule set, procedural-generation proof or network interaction test.

The purpose is to answer one material uncertainty cheaply and quickly.

### 6.2 Small complete games and representative vertical slices

The project should support an end-to-end playable path that combines mechanics, feedback, content, state, evaluation and target-runtime concerns.

This is the primary proof surface for the core production model because it demonstrates integration rather than isolated design advice.

### 6.3 Gameplay subsystems inside larger productions

The same production intelligence should remain useful inside larger games for bounded gameplay responsibilities such as combat, traversal, progression, encounters, economy or world interaction.

The project does **not** become a complete studio operating system for AAA-scale staffing, asset scheduling, portfolio management or organisation-wide production governance. Large productions consume Game Development Skills for gameplay responsibilities while project/programme management remains elsewhere.

## 7. Supported game forms

The long-term domain boundary includes reusable gameplay production across:

- 2D and 3D games;
- real-time and turn-based interaction;
- authored and procedural content;
- deterministic and simulation-heavy systems;
- single-player and multiplayer gameplay;
- controller, keyboard/mouse and touch-driven interaction;
- mobile, desktop, web and console targets;
- games that integrate narrative, audiovisual and world-production pipelines without owning those specialist pipelines.

This does not mean every class must be proven by the first implementation vertical.

The following classes should be deferred until the core production model has evidence and their specialist requirements are researched directly:

- XR / spatial-computing interaction;
- massively persistent or MMO-scale networking and operations;
- large live-service economies and continuous content operations;
- user-generated-content platforms with complex creator/runtime safety constraints;
- specialised physical installations, location-based entertainment and unusual hardware;
- regulated real-money or gambling-like systems.

These may later become supported core scenarios, specialised execution paths or Extension Packs if evidence justifies them. They must not distort the initial core model.

## 8. Engine expectations

The core production intelligence should be **engine-agnostic but engine-aware**.

The repository should own reusable reasoning such as:

```text
what uncertainty exists
→ what must become playable
→ what runtime behaviour is required
→ what evidence must be observed
→ what acceptance criteria apply
```

Concrete execution may later use engine-specific adapters, provider skills, editor agents, CLIs, APIs, scripts or direct coding operations.

This stage makes no engine selection and defines no adapter architecture. Those decisions belong to later tool and execution-layer stages.

The boundary rules are:

- no engine should define the game-development workflow merely because it is popular or well tooled;
- the core should not become a lowest-common-denominator abstraction that hides meaningful engine/runtime constraints;
- engine-specific behaviour may be expressed at execution boundaries when a consuming project requires it;
- reusable game-development knowledge should remain portable when the concrete engine changes;
- engine documentation and editor automation are execution knowledge, not substitutes for game-development production intelligence.

## 9. Platform expectations

Platform constraints are part of game-development reasoning because they affect input, feedback, readability, performance budgets, memory pressure, load behaviour and interaction design.

The project should therefore:

- capture the intended target platforms early enough to influence gameplay decisions;
- distinguish editor behaviour from representative runtime behaviour;
- define gameplay-facing performance and latency budgets where relevant;
- require representative target-path validation before platform-quality claims;
- preserve platform-specific constraints as project inputs rather than silently assuming desktop development conditions.

The project does not own general platform build engineering, store submission, signing, deployment infrastructure, legal compliance or console certification operations. It may define gameplay-facing acceptance criteria that those processes must satisfy.

## 10. Multiplayer expectations

Multiplayer is inside the game-development boundary when networking changes the game rules or player experience.

Game Development owns reusable reasoning about matters such as:

- authority and ownership as they affect game rules;
- synchronisation-critical gameplay state;
- fairness and exploit-sensitive mechanics;
- latency tolerance from the player's perspective;
- prediction, rollback or reconciliation requirements when they materially affect game feel;
- disconnect, reconnect, join/leave and failure states as gameplay states;
- cooperative or competitive interaction rules;
- multiplayer playtest questions and observed behaviour.

General networking implementation, distributed-system architecture, backend infrastructure, service reliability, security engineering and non-game-specific protocol work belong primarily to Software Engineering or infrastructure responsibilities.

The first end-to-end core proof does not need to be networked. Networked scenarios should be added only when the core single-runtime production model is stable enough that networking introduces useful additional evidence rather than avoidable complexity.

## 11. Game-design responsibilities

`game-development-skills` owns reusable production expertise for:

- game thesis, player fantasy and intended experience;
- player verbs and action vocabulary;
- mechanics and rules;
- gameplay state and state transitions;
- loops, systems and system interactions;
- progression and unlock structures where gameplay-relevant;
- encounter structure and gameplay pacing;
- level/world gameplay requirements and affordances;
- economy and resource rules where they are game systems;
- controls and gameplay feedback requirements;
- game-feel targets and response characteristics;
- difficulty, tuning and balance reasoning;
- gameplay accessibility requirements;
- prototype hypotheses and proof strategy;
- playtest questions, observation and diagnosis;
- emergence, dominant strategies, exploits, soft locks and unintended dynamics;
- gameplay-specific release acceptance.

It does not own final narrative writing, visual-art production, animation production, music composition, sound-design production, cinematography or general interface-design practice.

## 12. Gameplay implementation responsibilities

The project owns **game-specific implementation intent, integration decisions and acceptance criteria**, not general software engineering.

Game Development may direct an engine, editor tool or coding agent to create or modify gameplay-specific implementation when that is the concrete operation required to realise an approved mechanic or playable proof.

Examples inside the boundary include:

- expressing a rule as runtime state and transitions;
- wiring player input to an approved gameplay action;
- integrating an encounter's triggers and win/fail conditions;
- connecting gameplay events to feedback hooks;
- implementing a bounded prototype needed to answer a design question;
- configuring gameplay data or tuning parameters;
- composing gameplay systems inside a representative scene or build;
- instrumenting game-specific telemetry needed for evaluation.

Software Engineering owns general concerns such as:

- application and service architecture unrelated to game-design semantics;
- generic code organisation and refactoring;
- dependency management;
- build systems and CI/CD;
- general test engineering infrastructure;
- observability platforms;
- security engineering;
- persistence and backend architecture;
- generic networking infrastructure;
- deployment and cloud operations;
- non-game-specific performance implementation;
- maintainability concerns that apply regardless of the game's production model.

Where both domains are required, Game Development defines the gameplay behaviour and acceptance target; Software Engineering owns the general implementation quality needed to realise it safely and maintainably.

## 13. Content integration responsibilities

Game Development is responsible for making specialist content function as gameplay without taking over specialist content creation.

It may:

- specify gameplay-facing requirements for an asset or content package;
- define runtime hooks, states, events, collision/interaction needs and gameplay metadata;
- integrate supplied assets into mechanics, encounters, levels and feedback loops;
- validate an asset in context rather than accepting it solely because the source discipline considers it complete;
- request targeted revisions when integrated gameplay evidence shows a domain-specific problem;
- preserve approved specialist work when the defect is actually owned by another gameplay layer.

It must not silently regenerate specialist assets merely because it can access a generative provider. When the defect belongs to the producing discipline, the correct response is a bounded handoff back to that discipline with evidence and acceptance criteria.

## 14. Cross-domain handoffs

The project participates in cross-domain composition through explicit producer/consumer contracts rather than a universal asset schema.

Representative boundaries are:

| Adjacent discipline | Provides to Game Development | Game Development owns after handoff | Game Development may return |
| --- | --- | --- | --- |
| Narrative Production | character/world intent, narrative constraints, dialogue/story assets | gameplay consequences, runtime use, interaction logic | gameplay conflicts, affordance requirements, evidence from play |
| UI/UX Design | interface/interaction design, information hierarchy, flows, accessibility guidance | gameplay-facing integration and runtime state coupling | gameplay states, data/feedback needs, usability evidence |
| Character / 2D / 3D / Environment Production | runtime-suitable visual assets and production constraints | gameplay placement, affordances, collision/interaction requirements, in-game validation | technical/gameplay constraints, contextual failure evidence |
| Animation | animation assets, state intent and transition capabilities | gameplay timing, state integration, interruptibility requirements | gameplay timing constraints, missing states, observed integration defects |
| Audio / Sound Production | sound assets and audio behaviour proposals | gameplay event hooks, priority requirements, contextual validation | feedback/readability needs, event timing evidence |
| Music Production | music assets, stems and musical production intent | gameplay-driven triggering/integration requirements | state/transition needs and contextual evaluation evidence |
| Deep Research | external evidence relevant to a game-design question | interpretation within gameplay production | bounded research questions and evidence gaps |
| Software Engineering | maintainable implementation, infrastructure and technical systems | gameplay semantics and acceptance | game-specific contracts, budgets, failing scenarios and acceptance tests |
| QA / Evaluation | independent integrated test evidence where available | game-design diagnosis and gameplay correction decisions | reproducible gameplay defects, expected behaviour and regression needs |

Project-specific handoff instances remain in the consuming project. Only reusable handoff knowledge belongs here.

## 15. Quality definition

Game quality must remain multidimensional. The project must not collapse game correctness, game feel and player experience into one score.

A gameplay outcome is credible only when the applicable quality dimensions are visible separately:

### 15.1 Rule and state correctness

- implemented rules match approved intent;
- state transitions are valid;
- required states are reachable;
- invalid states, soft locks and corrupt progression are controlled;
- deterministic invariants hold where expected.

### 15.2 Interaction quality

- controls are responsive enough for the intended interaction;
- feedback communicates important state changes;
- timing and input behaviour support the intended mechanic;
- gameplay remains readable under representative conditions.

### 15.3 Player-experience evidence

- human play evidence is used for experiential claims such as fun, fairness, clarity, tension, satisfaction or emotional effect;
- automated agents and simulations may reveal defects or coverage gaps but are not authoritative substitutes for human experience.

### 15.4 Systems and balance quality

- interacting systems do not create obviously broken dominant strategies, runaway economies or dead content;
- tuning supports the intended challenge/progression envelope;
- important emergent behaviours are observed rather than dismissed as noise.

### 15.5 Accessibility and inclusion

Applicable control, timing, readability, colour, captioning, feedback redundancy, cognitive-load and motor-demand concerns are treated as core quality dimensions rather than optional polish.

### 15.6 Runtime and platform quality

- representative performance, memory, loading and latency behaviour is acceptable for the target path;
- editor success is not treated as shipping evidence.

### 15.7 Integration and preservation quality

- approved upstream decisions and specialist assets are preserved unless evidence requires reopening them;
- defects are corrected at the smallest responsible layer;
- cross-domain changes are traceable to an observed need.

### 15.8 Reproducibility

- material evaluations identify the build/context, relevant inputs, expected behaviour and observed result sufficiently for later regression work.

## 16. Human approval points

Automation can accelerate exploration and verification, but material commitment remains explicit.

Human approval is required before the workflow substantially increases cost or intentionally changes an accepted player-facing decision.

Core approval points are:

1. **Game thesis / intended experience** — confirm the player promise and important constraints before treating downstream work as authoritative.
2. **Core mechanic or loop commitment** — select which playable proof is worth carrying forward when alternatives materially differ.
3. **Fidelity escalation** — approve moving from cheap prototypes/greyboxes/placeholders into substantially more expensive content or implementation.
4. **Material system or content expansion** — approve scaling an interaction pattern when the evidence base is still bounded.
5. **Reopening locked gameplay decisions** — explicitly authorise changes to accepted mechanics, controls, progression, level constraints or other persistent decisions.
6. **Experiential acceptance** — human evidence remains authoritative when declaring player-facing qualities such as fun, fairness, clarity or emotional effectiveness acceptable.
7. **Release trade-offs** — intentional acceptance of known gameplay, accessibility or performance limitations requires an accountable human decision in the consuming project.

The exact organisational approver belongs to the consuming project; the reusable skill set only preserves the need for the decision and its evidence.

## 17. Persistent and locked decisions

Approved work should constrain later production until explicitly reopened.

Potentially persistent decisions include:

- game thesis and intended player experience;
- target audience and platform constraints;
- accepted core verbs and mechanics;
- control mappings and interaction contracts;
- important rule/state invariants;
- progression or economy rules;
- accepted encounter/level constraints;
- approved tuning values where they have become production contracts;
- accessibility requirements;
- gameplay-facing performance budgets;
- accepted specialist assets and their integration contracts;
- explicit rejected alternatives when revisiting them would waste work without new evidence.

A later evaluation failure must first identify which layer owns the problem. It must not silently discard a valid locked decision simply because regeneration is cheaper for the execution tool.

Precedence is:

```text
explicit current project instruction
→ approved / locked project decisions
→ applicable specialised guidance
→ core Game Development defaults
```

The storage mechanism for project-specific locks belongs to the consuming project or its Project Intelligence system, not to the reusable Production Skills repository.

## 18. Smallest meaningful end-to-end playable outcome

The minimum end-to-end proof for this project is **a bounded playable vertical slice**, not a design document and not a polished full game.

It should contain enough of the intended game to prove the complete reasoning loop:

- a defined player objective or interaction purpose;
- at least one controllable or meaningfully interactive player verb;
- explicit rules and state transitions;
- a coherent short gameplay loop or encounter;
- observable feedback for important state changes;
- a success/failure, progression or otherwise meaningful state outcome;
- placeholder or supplied content integrated where needed;
- basic accessibility and control considerations appropriate to the slice;
- representative execution in an actual runtime rather than only prose or diagrams;
- recorded evaluation evidence;
- at least one demonstrated diagnosis/correction cycle when the first implementation exposes a material problem.

The slice need not use final art, final audio, final narrative or final optimisation. Its purpose is to prove that the installed production intelligence can carry gameplay from intent through executable behaviour and evidence-driven correction.

## 19. Definition of a successful installed skill set

At maturity, installing `game-development-skills` into a clean consuming project should provide enough reusable production intelligence to:

1. understand the game-development objective and constraints;
2. establish a defensible gameplay thesis without inventing unrelated project requirements;
3. model the mechanics, systems and states that need to exist;
4. choose the cheapest adequate proof for the current uncertainty;
5. direct an available engine/editor/coding execution layer to realise the required playable behaviour;
6. integrate outputs from adjacent production domains without duplicating their specialist pipelines;
7. evaluate structural behaviour automatically where appropriate and player experience with human evidence where required;
8. preserve approved decisions and diagnose failures before changing them;
9. direct the smallest sufficient correction;
10. validate representative target behaviour;
11. leave behind reproducible artefacts/evidence sufficient for later regression and continuation.

Success is therefore **playable, evidenced and repairable behaviour**, not merely generation of design documentation or source code.

## 20. Non-goals

`game-development-skills` is not intended to become:

- a general software-engineering handbook;
- a universal game engine or engine abstraction runtime;
- a replacement for engine documentation, editor tooling or coding agents;
- a provider/model registry;
- a generic project-management or studio-management system;
- a replacement for Pactwright or consuming-project lifecycle governance;
- a narrative-writing, concept-art, 2D/3D asset, animation, music, sound-design or cinematic-production pipeline;
- a generic UI/UX design repository;
- a cloud/backend/network-infrastructure framework;
- a storefront submission, console certification or deployment system;
- a legal, ratings, licensing, monetisation or business-strategy authority;
- a guarantee that automated playtesting can determine whether a game is fun;
- a repository of project-specific lore, tuning decisions or implementation history;
- a core bloated with every genre, platform or specialist workflow before those specialisations have evidence.

## 21. Boundary decisions

The Stage 1 questions are resolved as follows.

### Does the project own game design only, or game design plus playable integration?

**Decision:** game design plus playable integration.

A reusable game-development production system is incomplete if it cannot carry an approved mechanic into an actual runtime and evaluate the resulting behaviour.

### Where does game-specific engineering end and general software engineering begin?

**Decision:** Game Development owns gameplay semantics, game-specific implementation intent, runtime integration and acceptance criteria. Software Engineering owns general code/system architecture, infrastructure, maintainability and engineering practices that remain relevant independent of the game's design.

### Does the project support engine-agnostic production intelligence with engine-specific execution adapters?

**Decision:** yes in principle. The core reasoning is engine-agnostic; concrete execution may be engine-specific. The adapter/tool architecture is intentionally deferred to later stages.

### What game classes are legitimate targets at maturity?

**Decision:** mainstream 2D/3D, real-time/turn-based, authored/procedural, single-player/multiplayer games across mobile, desktop, web and console are legitimate long-term targets. Specialised XR, massive persistent online, UGC-platform, unusual hardware and regulated game classes require later direct evidence before being treated as core coverage.

### Which classes are deferred until the core has evidence?

**Decision:** XR, MMO-scale persistence, large live-service operations, complex UGC platforms, unusual physical installations and regulated real-money systems are deferred.

### What is the smallest meaningful playable outcome?

**Decision:** a bounded playable vertical slice that demonstrates at least one meaningful interaction loop, runtime state/rules, feedback, an observable outcome, evaluation evidence and a correction cycle.

### What decisions require human approval before substantially more expensive work begins?

**Decision:** game-thesis acceptance, selection/commitment of material mechanics or loops, major fidelity escalation, substantial production expansion, reopening accepted player-facing decisions and experiential/release trade-offs.

## 22. Stage 1 exit gate

Stage 1 passes because this charter now provides:

- a clear project goal;
- explicit owned game-development outcomes;
- intended users;
- supported project scales and game forms;
- engine, platform and multiplayer expectations;
- explicit game-design and gameplay-implementation responsibilities;
- content-integration responsibilities;
- a multidimensional quality definition;
- human approval points;
- persistent/locked decision rules;
- explicit cross-domain handoffs;
- non-goals;
- a defensible boundary against Software Engineering and specialist Production Skills;
- a concrete definition of the smallest end-to-end playable proof;
- a clear definition of what a successful installed skill set should produce.

No Stage 1A corpus selection or later-stage architecture work is claimed by this document.

**Stage 1 status: COMPLETE.**
