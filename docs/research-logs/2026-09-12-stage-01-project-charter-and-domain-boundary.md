# Stage 1 - Project Charter and Domain Boundary

**Date:** 12 September 2026  
**Version:** 1.0  
**Status:** Stage 1 complete; scope baseline for subsequent research  
**Bootstrap:** [Version 1.1, Stage 1](2026-09-07-game-development-skills-new-project-bootstrap-process.md#6-stage-1---define-project-goal-and-domain-boundary)

## 1. Project charter

`game-development-skills` will provide installable, reusable production expertise for turning player intent into designed, playable, evaluated and progressively refined gameplay. It owns **game design plus playable integration**, including the decisions and acceptance criteria that connect mechanics, runtime behaviour and observed player experience.

Its primary users are game designers, gameplay developers and technical designers working alone or in small teams, with coding agents and engine tools as execution collaborators. Larger teams may use it for bounded gameplay responsibilities within their existing production process.

A successful installed skill set must guide a clean consumer project from a brief through a meaningful playable result, evaluation, diagnosis and a targeted correction, preserving accepted work and recording reproducible evidence. Documentation alone does not satisfy that outcome.

Production reasoning must remain independent of one engine, provider or agent. Concrete execution can use engine-specific capabilities. Begin proof with a bounded local single-player game; broader forms remain legitimate targets subject to demonstrated coverage. No engine or skill decomposition is selected here.

The repository owns reusable game-development expertise. Consumer projects own their games, requirements, assets, source code, decisions and delivery authority. General software engineering and specialist content production retain their own boundaries. Installed core skills must work without Extension Packs, the central Production Skills repository or Pactwright.

## 2. Owned outcomes and responsibilities

| Responsibility | Game Development owns | Required outcome in the consuming project |
|---|---|---|
| Player intent and game design | Intended experience, player fantasy, core verbs, meaningful choices, rules, constraints and design hypotheses | An explicit game thesis connected to observable gameplay questions |
| Mechanics and systems | State transitions, progression, interactions, encounter behaviour, balance assumptions and unintended strategies | Implementable rules and acceptance criteria, including interaction failures and edge cases |
| Playable production | Choice of the cheapest adequate proof, scope of implementation, controls, feedback and integration sequence | A runnable game or bounded gameplay slice that exposes the current uncertainty |
| Game-specific implementation | Behavioural requirements for controllers, cameras, combat, gameplay AI, simulations and other applicable systems; domain configuration and tuning | Engine/code changes whose observed gameplay can be checked against those requirements |
| Levels, worlds and content integration | Traversal, affordances, collision intent, encounters, pacing, gameplay placement and runtime use of supplied content | A playable composition with traceable handoffs and integration checks |
| Evaluation and repair | Gameplay correctness, playtest questions, telemetry interpretation, balancing, accessibility, performance trade-offs and diagnosis | Evidence-linked findings, the smallest sufficient correction and checks that accepted behaviour survives |
| Playable delivery | Gameplay readiness criteria, limitations and repeatable build/run evidence | A versioned playable result with the information needed to reproduce and assess it |

This boundary includes directing concrete implementation and checking its result. It must not end at a design document or an instruction to another discipline to make the game playable. An engine, coding agent or developer may perform the operation; Game Development remains responsible for specifying and judging the gameplay outcome.

Reuse lies in methods for framing uncertainty, designing rules, testing interactions, integrating content and diagnosing failures. A particular game's fiction, tuning values, level layout or progression is consumer-project knowledge, not a reusable core rule.

## 3. Users, project scale and coverage expectations

### 3.1 Project scale

The initial proof should be manageable by one developer or a small team: an isolated mechanic, repeatable loop or short playable slice. This limits the first validation workload, not the mature domain boundary or quality standard.

At maturity, the same expertise should apply to larger games through bounded systems, levels, encounters and integration milestones. Whole-studio scheduling, staffing, portfolio management and an autonomous guarantee of large-game delivery are outside this repository. A large project must supply its integration authority and constraints.

### 3.2 Game forms and platforms

All entries below are scope decisions. **No engine, platform or game class is implemented or verified by this charter.** A path becomes supported only through appropriate executed examples, evaluation and consumer-installation evidence.

| Class | Position in the domain | Evidence required before a support claim |
|---|---|---|
| Bounded local single-player games | First end-to-end proof target; one execution and platform path selected later | Installed skills produce, evaluate, repair and reproduce a complete bounded play session |
| 2D and 3D games | Both legitimate targets; the first proof need not demonstrate both | Representative interaction, camera, collision, spatial-readability and content-integration checks for each claimed path |
| Desktop and browser delivery | Legitimate accessible proof candidates; neither mandated now | Real runnable builds with declared runtime, input and performance conditions |
| Mobile games | Legitimate target; defer a mobile support claim until device evidence exists | Touch/input suitability, interruption and resume behaviour, screen readability, and performance on a declared device path |
| Procedural games and content | Legitimate target after the bounded core proof | Reproducible seeds where applicable, constraint and reachability checks, problematic-seed coverage and human review of generated play |
| Simulation-heavy and emergent games | Legitimate target after the bounded core proof, including interacting physical and social systems | Rule invariants, interaction and stability tests, long-run behaviour where relevant, exploit analysis and bounded experiential findings |
| Local multiplayer | Legitimate target after the single-player proof | Multiple-player input/state separation, shared or split presentation, session lifecycle and appropriate human play evidence |
| Networked co-operative or competitive games | Legitimate target; defer network implementation support until dedicated evidence exists | Authority and synchronisation behaviour, latency/loss tests, joining/leaving/reconnection and gameplay fairness findings under declared conditions |
| Console games | Legitimate target; defer platform support until authorised tooling and representative execution are available | Target builds, device/input evidence and applicable platform review; gameplay tests do not imply certification |
| XR games | Legitimate target; defer support until representative hardware and suitable evaluation are available | Tracking/input, spatial interaction, comfort and accessibility evidence under declared conditions |

Genres do not define the repository's architecture. Real-time, turn-based, puzzle, action, strategy, narrative-led and open-ended play may all use the owned responsibilities. Their specialised methods and any Extension Pack classification require later research.

Multiplayer is neither a mandatory core dependency nor permanently excluded. Game Development owns its player-facing rules and acceptance questions. General networking, service operation and security engineering remain engineering responsibilities.

Simulation behaviour is evaluated against the game's stated model. A plausible simulation or an emergent in-game finding is not proof of real-world validity; scientific claims require external domain evidence and review.

### 3.3 Engine expectations

Support engine-independent production reasoning with **engine-specific execution paths or adapters where justified**. Engine independence does not promise automatic portability or identical features across engines.

Use existing engines, editor capabilities and deterministic tools for execution. An adapter may be a documented tool contract or thin integration; this charter does not require a universal adapter API, custom engine or common runtime. Tool research and execution-path selection belong to Stages 8 and 9.

Each demonstrated path must identify its prerequisites, tool/engine revision, target runtime, limitations and how to reproduce its evidence. Installing skills is separate from installing an engine or obtaining platform access.

## 4. Engineering and cross-domain boundaries

### 4.1 Game-specific engineering versus general engineering

Use the decision's acceptance criterion to identify its owner:

| Decision | Gameplay ownership | Engineering / execution ownership |
|---|---|---|
| Jump, dash or movement controller | Movement envelope, responsiveness, collision intent, timing tolerance and tuning acceptance | Code architecture, input plumbing, implementation, unit tests and profiling mechanisms |
| Gameplay AI or simulation | Perception/action rules, state consequences, fairness, interaction constraints and scenario acceptance | Data structures, concurrency, numerical implementation and use of engine facilities |
| Performance problem | Player-visible budget, representative workload, acceptable fidelity trade-off and preserved gameplay | Measurement tooling, memory/CPU/GPU diagnosis and implementation optimisation |
| Networked combat | Authority requirements as experienced in play, latency tolerance and fairness scenarios | Replication mechanisms, transport, backend architecture, security and operations |

The same person or agent can carry both responsibilities. Installing the Software Engineering family is not a prerequisite for core game production. General engineering can be supplied by the consumer's existing developers, agents and tools; responsibility for its quality remains explicit.

For example, a missed jump first requires determining whether the rule, timing, feedback, collision setup, input handling or frame-time behaviour caused it. Route the correction to that owner instead of rewriting the game or changing an accepted jump specification to conceal an implementation fault.

### 4.2 Specialist handoffs

These are discipline boundaries, not claims that every adjacent family is already implemented or must be installed.

| Adjacent discipline | Specialist contribution | Game Development specifies and accepts |
|---|---|---|
| Software Engineering | General architecture, implementation quality, refactoring, infrastructure, CI and runtime engineering | Gameplay behaviour, target workload, integration conditions and game-specific acceptance |
| UI/UX Design | Interface research, information architecture, menus, navigation and interaction design | In-play information, control/feedback needs, state transitions, timing and readability in actual play |
| Narrative Production | Fiction, characters, dialogue, story structure and narrative intent | Branching conditions, triggers, interactive consequences and integration without silently rewriting approved story content |
| World/Environment Production | Environmental and spatial design, authored world composition and blockout contributions | Traversable routes, gameplay scale, sightlines, encounter positions and greybox playability |
| 2D, 3D and visual character production | Visual assets and their specialist craft validation | Runtime scale, pivots, collision requirements, attachment points, budgets, state variants and gameplay readability |
| Animation / Character Performance | Rigging, motion and performance production | Required states, transition and event timing, movement/root-motion expectations and feedback during play |
| Music and Audio Production | Composition, music production, sound design and audio assets | Triggers, looping/transitions, priority, timing and audio feedback requirements, including redundant non-audio cues |
| Video Production | Cinematics, rendered sequences and trailers | Playback, skip/interruption, state continuity and return-to-play requirements |
| Deep Research | External source investigation, market/player evidence and specialist scientific research | Research questions and application of findings to game decisions, with uncertainty preserved |
| QA/Evaluation | Independent test design, execution and assessment of the assembled product | Game-domain quality criteria and diagnosed gameplay findings; QA evidence complements the domain benchmark |
| Legal and Business/Advertising disciplines | Rights, legal/platform advice, commercial strategy and promotion | Relevant constraints supplied to production; Game Development does not certify legal clearance or own launch marketing |

A handoff identifies the producer, consumer, artefact/version, intended use, required runtime properties, constraints, acceptance evidence and authority over changes. Use a documented project-native agreement; no universal asset schema is introduced.

The producer retains specialist craft authority. Game Development accepts gameplay integration, and the consumer's owner resolves conflicts affecting approved work. If art obscures a traversable route, for example, record the gameplay failure and request the responsible asset/layout correction instead of silently replacing the approved environment.

Placeholder content is sufficient when it answers the current gameplay question. Final art, music or narrative production must not be required merely to prove a rule.

## 5. Quality definition

Quality means that the game meets its declared rules and constraints, supports its intended players and experience, and can be reproduced and improved without destroying accepted work. Keep the following findings distinct; one score cannot hide a material failure.

| Dimension | Required evidence and limit |
|---|---|
| Mechanical correctness | Rule/state checks, reachable outcomes, restart integrity and interaction edge cases; a build compiling is insufficient |
| Systems and balance | Scenario tests, simulations or telemetry for dominant strategies, exploits, soft locks, pacing and progression; scope claims to the tested conditions |
| Player experience and game feel | Human play observations against explicit questions about comprehension, agency, challenge, fairness or satisfaction; agents and scripted runs provide supporting evidence |
| Accessibility | Applicable input alternatives/remapping, timing and motor demands, readability, colour independence, redundant feedback, captions and pause/speed behaviour; document gaps and test with relevant players where required |
| Content integration | Collision, scale, timing, state continuity, readability and asset/version consistency in actual play |
| Target performance | Declared frame-time, memory, load-time and input-latency budgets where applicable, tested on representative builds/hardware; editor-only evidence remains labelled |
| Preservation and repair | Traceable diagnosis, bounded change and regression evidence for both the repaired defect and unaffected accepted behaviour |
| Reproducibility and installation | Discoverable selected skills in a clean consumer project, explicit prerequisites, recorded revisions/configuration, runnable output and repeatable evaluation |

Baseline accessibility belongs to core production quality. Specialist packs may deepen a target but cannot remove that responsibility. Human evidence supports bounded experiential findings; it does not establish that all players will find a game fun. Thresholds, participant criteria and benchmark methods are designed in later stages, not invented here as measured results.

## 6. Human decisions, cost and preservation

The consumer's designated owner controls creative and product commitments. Existing explicit approval within a defined scope remains valid; routine reversible implementation and checks within that scope need no repeated confirmation.

| Commitment | Human decision required before proceeding beyond existing authority |
|---|---|
| Select a materially different game thesis or target audience | Accept the intended experience, scope, constraints and rejected alternatives |
| Move from competing playable candidates to expensive production | Review the available play/evaluation evidence and approve the selected direction and fidelity increase |
| Adopt an engine/platform or specialist multiplayer/XR path with substantial cost or lock-in | Approve the researched trade-offs, prerequisites and resource envelope |
| Expand content volume, external spend or delivery scope | Approve the additional commitment and the evidence supporting it |
| Change an accepted mechanic, tuned range, layout, story integration or quality constraint | Explicitly reopen the affected decision and accept its downstream impact |
| Waive a material release-quality issue or publish a playable release | Accept the recorded exception or authorise publication within the consumer's release process |

Before each new commitment, present a concrete candidate, evidence, remaining uncertainty, expected cost and consequences. Prefer written rules or a small simulation for rule questions, a controller sandbox for movement, and a greybox for spatial play. Increase fidelity only when the current question requires it.

Persist approved decisions in the consumer project with their identity/revision, scope, rationale, evidence, approver, constraints and affected artefacts. Important retained decisions include the thesis, target controls/platform, accepted mechanics, tuning values or permitted ranges, layouts, content interfaces and quality budgets.

Approved ranges allow tuning within those ranges. A later failure creates a finding; it does not automatically unlock every upstream decision. Reopening records the reason, impacted work, new approval and replacement evidence while preserving history. Explicit project instructions and approved decisions take precedence over packs and core defaults; conflicts must be surfaced before destructive changes.

## 7. Smallest meaningful installed outcome

The minimum end-to-end proof is one bounded playable session with a player-controlled verb, a meaningful goal or choice, an interacting rule, observable feedback, an outcome and restart/reset behaviour. It must expose a real design question and permit a targeted correction.

An illustrative shape is a placeholder room in which the player chooses a route around a hazard to reach a goal, then wins or fails and can retry. This demonstrates the required scope; it does not select the later benchmark, genre, engine or example catalogue.

The eventual installed workflow must produce:

1. A brief naming intended players/experience, the rule question, constraints and acceptance conditions.
2. Editable source/project content and a runnable build or documented runtime path, using cheap assets where adequate.
3. The implemented rules, input/feedback behaviour and relevant accepted decisions.
4. Actual mechanical and interaction checks, plus scoped human play evidence for any experiential claim.
5. A recorded finding, root-cause diagnosis, targeted correction and repeat evaluation demonstrating the correction and preservation of accepted work.
6. Reproduction instructions and provenance: skill revision, relevant tool/runtime versions, configuration, seed where applicable, evidence locations and known limitations.

Perform this from a clean consumer project with the selected core skills, declared execution prerequisites and no undocumented dependence on this repository's research logs, books or sibling families. If execution or required human evidence is unavailable, record that limitation instead of claiming the playable proof passed.

This is a capability proof rather than a commercial release. Mature acceptance still requires the later bootstrap's broader examples, Extension Packs, benchmarks and installation gates. Nothing in this Stage 1 record claims that proof has run.

## 8. Non-goals and alternatives resolved

| Alternative | Decision and rationale |
|---|---|
| Game-design advice ending at documentation | Rejected: it cannot satisfy the required playable, evaluated outcome |
| Owning all code and specialist asset pipelines | Rejected: it duplicates adjacent expertise; own game-specific decisions and integrated acceptance instead |
| One mandatory engine or coding agent | Rejected as the domain boundary: execution choices must follow research and remain replaceable at the production-reasoning level |
| Building a universal engine/adaptor runtime before proof | Rejected: a demonstrated path must justify any integration machinery |
| Supporting every platform, genre or team scale immediately | Deferred: legitimate scope is wider than demonstrated support; add evidence before expanding claims |
| Owning each consumer's game, roadmap or project graph centrally | Rejected: product state and delivery governance remain with that consumer and its optional orchestrator |
| Autonomous proof of fun, commercial success, scientific validity or platform certification | Rejected: each requires its appropriate external evidence or authority |

No core skill list, engine selection, Extension Pack catalogue, universal artefact schema, production scaffold or dependency on Pactwright is created in Stage 1.

## 9. Evidence basis and next-stage handoff

This is a normative scope decision derived from the governing documents, not a professional-practice literature review. It establishes what subsequent research must cover and challenge. Research may refine the baseline through explicit revisions with reasons; it must not silently narrow the domain to match a convenient book or tool.

Sources reviewed on 12 September 2026:

| Source | Revision reviewed | Contribution |
|---|---|---|
| [Game Development bootstrap](https://github.com/sb-dev/game-development-skills/blob/a4b1c2bf2d5188ecf8837da3447eb0d1184e93fe/docs/research-logs/2026-09-07-game-development-skills-new-project-bootstrap-process.md) | v1.1; main commit `a4b1c2b` | Stage 1 requirements, game-specific principles and Stage 1A/1B/2 ordering |
| [Family bootstrap guide](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/bootstrap/README.md) and [new-project process](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/bootstrap/new-project-process.md) | v1.1 / v1.4 | Durable stage outputs, standalone execution and boundary-first progression |
| [Family system](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/specs/01-production-skills-family-system.md) and [project contract](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/specs/02-production-skills-project-contract.md) | v1.0 / v1.3 | Domain ownership, self-contained installation and evidence-based maturity |
| [Evaluation and Extension Packs](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/specs/03-production-skills-evaluation-and-extension-packs.md) and [cross-domain integration](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/specs/04-cross-domain-orchestration-and-integration.md) | v1.2 / v1.1 | Separate quality dimensions, approval precedence, handoffs and consumer ownership |
| [Domain research process](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/bootstrap/domain-research-process.md) and [five-book decision](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/research-logs/2026-09-10-five-book-bootstrap-research-foundation.md) | v1.0 / v1.0 | Seed scope, corpus permissions, access/reading distinction and research qualification |

The **next stage is Stage 1A**. Use this charter to derive the knowledge-coverage map through bounded reconnaissance, compare a broader book pool, select exactly five complementary books and record access needs and selection decisions. No books were supplied with this Stage 1 request and none have been selected or examined here. Review any newly supplied material before selection; supplied-book removal, replacement or demotion requires explicit permission.

Stage 1B then directly examines and reconciles the corpus. Stage 2 challenges and extends the resulting model. Preserve these separate gates. Engine choice, specialised support, detailed workflow/artefact contracts, skill decomposition and measured quality thresholds remain work for their designated later stages.

## 10. Stage 1 completion check

| Required item | Evidence in this record |
|---|---|
| Short charter, target outcomes and intended users | Sections 1-2 |
| Project scales and game forms | Sections 3.1-3.2 |
| Engine, platform and multiplayer expectations | Sections 3.2-3.3 |
| Design plus playable integration decision | Sections 1-2 and 7 |
| Game-specific versus general implementation boundary | Section 4.1 |
| Content integration and explicit adjacent disciplines | Sections 2 and 4.2 |
| Quality definition | Section 5 |
| Human approval and expensive commitment points | Section 6 |
| Persistent/locked decisions and reopening | Section 6 |
| Legitimate mature targets and deferred classes | Section 3.2 |
| Smallest meaningful installed result | Section 7 |
| Non-goals and boundary rationale | Section 8 |
| Canonical inputs, evidence limits and next dependency | Section 9 |

**Exit decision:** Stage 1's charter and defensible domain boundary are complete. This completes a design stage only; it does not establish researched, implemented, benchmarked or installable game-development capabilities and does not promote repository maturity.

---

**Version:** 1.0 | **Stage:** 1 | **Updated:** 12 September 2026
