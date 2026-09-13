# Game Development Skills

**Turn a game brief into playable, evaluated gameplay.**

Game Development Skills gives coding agents a production workflow for designing mechanics, building playable proofs, integrating content, evaluating what happens and repairing the responsible part while preserving accepted work.

**Current status:** Design baseline on `feat/bootstrap-2`. Six canonical specifications, fifteen example briefs and two researched Extension Pack profiles are complete. Installable skills, playable example outputs and measured benchmark results are still to be implemented and demonstrated. [Bootstrap progress](docs/research-logs/README.md) records the verified stages.

## What you can produce

The specified workflow covers a single mechanic, a complete play loop, a representative level or encounter, interacting systems and a small finished game. It connects thesis and rules to controls, state, feedback, progression, content, playtesting, balance, accessibility and target performance.

Start with the production problem you have: develop a brief, prototype a disputed mechanic, integrate a delivered asset, investigate a failing encounter or prepare a playable build. Independent evaluation accepts an existing game made with other tools. The planned curriculum includes 2D, genuine 3D and local multi-peer browser work; those paths gain support only through their own actual proof.

## Playability, fidelity and decision control

Choose the least costly representation that can answer the current question. A rule table may settle a rule; control timing needs a running controller; player comprehension needs actual people. Prove a bounded playable result before expanding content or committing to expensive fidelity.

Accepted mechanics, controls, story intent and content remain stable through unrelated repairs. Work within existing approval and tuning bounds proceeds without another permission request. A new material change needs its concrete candidate, evidence, impact and any genuinely missing decision. A planned or approved experience is not an observed experience.

## Installation

The installation interface is designed below; **this design checkpoint does not yet contain operational skills or a verified installation**. The implementation stages will replace this status with the exact tested source and commands.

```sh
npx skills add https://github.com/sb-dev/game-development-skills/tree/feat/bootstrap-2 --skill game-development --agent codex --copy --yes
```

Install `game-evaluate` independently for evaluation, or `game-extension-pack-creator` for authoring reusable specialisations. Production includes essential evaluation and repair and does not require either optional skill. Select only the skills needed; normal engine/library/browser prerequisites are separate from skill installation. See the [installation contract](docs/03-game-development-skills-repository-and-contracts-spec.md#6-installation-and-dependencies).

## Quick start — Latch Room

The first planned proof is one small keyboard-playable room. Push a crate onto a plate, cross the gate and reach the exit; then verify that restart restores the real game state. It exercises actual input, visible consequences, a bounded tuning choice and a diagnosed repair.

**Execution status: not run yet.** After the production skill is implemented and installed, use this complete Level 1 prompt in a fresh consumer project. It asks for runnable source, local launch instructions, real browser checks and a player-view capture. A design document alone cannot finish it.

```text
Create Latch Room in a fresh local consumer project using the installed game-development skill, with no Extension Pack selected. Make a small original keyboard-playable browser room in which the player pushes one crate onto a pressure plate to open a gate and reach an exit. Use a bounded grid, a safe starting position and simple original shapes/text. Choose and record a compact solvable layout whose exit really requires the gate; do not make a decorative gate the player can bypass.

Movement is one cardinal grid step per fresh action. A crate moves only when the next cell is free and in bounds; wall, occupied and out-of-bounds pushes change nothing. The gate is open exactly while the crate occupies the plate, and its collision/passability and visible state must agree. Restart restores all initial positions, plate/gate state and outcome. Explain the rules on screen, identify player/crate/plate/gate without colour alone, and make start/restart and the complete interaction keyboard operable with visible focus. Offer pointer buttons as an additional route without replacing the keyboard proof.

Implement and run the actual game through its normal browser input. Preserve a compact rule/state record, an authoritative read-only state observation for tests and observed checks for normal push, blocked push, plate enter/leave, gate crossing, win and two restarts. Do a bounded basic tuning comparison of two feedback durations chosen and recorded before testing; observe cue overlap/clarity mechanically and treat human readability as untested unless someone actually participates. Select a duration within that declared range and record the reason.

After accepting the working baseline, create a disposable fault variant in which gate state survives restart. Retain the baseline and faulty version. Reproduce the fault, diagnose the responsible state/reset boundary, and repair it while preserving the accepted board, push rules and input paths. Run the failing case and unaffected push/win cases again. Label deliberate fault injection and do not claim blind diagnosis.

Provide runnable source, exact dependency and local run commands, the complete prompt, baseline/fault/repair identities, actual test output and a player-view capture. Distinguish real input from privileged fixture setup and do not invent tests, people or device support. Keep the implementation game-specific; no shared engine, service, account or external publication.
```

The generated game must supply exact dependency and launch commands in its own README. Open its local URL, use the on-screen keyboard instructions and complete the gate/exit task. The example evidence must retain the working, deliberately faulty and repaired versions. No account, paid service or external publication is required. Its actual output and tested launch command will be linked here after the installed proof.

## Learn by producing

These are **fifteen designed examples, not fifteen completed games**. Each linked prompt is complete and independent. Actual source, captures, run instructions and observed results will accompany each implemented example. Pack showcases and reuse fixtures are additional evidence, not extra members of the five trios.

### Level 1 — Prove one mechanic

| Example / complete prompt | Production question |
|---|---|
| [Latch Room](docs/research-logs/stage-13-prompts/level-1.md) | Crate/plate/gate state, real input, feedback and reset repair |
| [Rebound Lab](docs/research-logs/stage-13-prompts/level-1.md) | Continuous deflector control, contact response, timing and a repeated-hit fault |
| [Depth Dock](docs/research-logs/stage-13-prompts/level-1.md) | Actual 3D movement, depth information and visual/logical transform agreement |

### Level 2 — Complete a repeatable loop

| Example / complete prompt | Production question |
|---|---|
| [Spark Run](docs/research-logs/stage-13-prompts/level-2.md) | Collect/carry/bank risk, pacing and valid attempt evidence |
| [Quiet Parcel](docs/research-logs/stage-13-prompts/level-2.md) | Stealth, opponent knowledge, detection/recovery and target loss |
| [Reservoir Shift](docs/research-logs/stage-13-prompts/level-2.md) | Limited resources, interacting costs and contrasting policies |

Each needs a complete goal/challenge/outcome/retry loop, basic balance work and an actual question-led human playtest.

### Level 3 — Integrate a coherent slice

| Example / complete prompt | Production question |
|---|---|
| [Beacon Walk](docs/research-logs/stage-13-prompts/level-3.md) | Three traversal rooms, content replacement and a collision/import fault |
| [Switchyard Tactics](docs/research-logs/stage-13-prompts/level-3.md) | Tactical actions, encounter progression and stale previews |
| [Orbit Courier](docs/research-logs/stage-13-prompts/level-3.md) | 3D steering/inertia, camera information and integrated delivery cues |

Add actual UI, visual, environment, animation and audio deliveries, an observed target workload and broader quality evidence.

### Level 4 — Scale systems and preserve them through repair

| Example / complete prompt | Production question |
|---|---|
| [Seeded Vault](docs/research-logs/stage-13-prompts/level-4.md) | Generated progression that remains reachable after final placement |
| [Canal Works](docs/research-logs/stage-13-prompts/level-4.md) | Flow, congestion, strategy comparison and dependent-state restoration |
| [Twin Signal](docs/research-logs/stage-13-prompts/level-4.md) | Two real browser clients, shared authority and duplicate/reconnect recovery |

Retain multiple content units, adverse cases, measured load and regression evidence. Simulated message schedules must be labelled; human cooperation requires actual people.

### Level 5 — Realise a small complete thesis

| Example / complete prompt | Production question |
|---|---|
| [Signal Orchard](docs/research-logs/stage-13-prompts/level-5.md) | A complete precision-platforming game with preserved routes and ending |
| [Harbor Accord](docs/research-logs/stage-13-prompts/level-5.md) | A tactical narrative campaign, persistent consequences and a bounded pack review |
| [Lantern Atlas](docs/research-logs/stage-13-prompts/level-5.md) | A coherent 3D world, linked state, exploration and packaged dependencies |

Complete actual playtesting, balance, access and performance review, then validate the identified release candidate from a fresh local directory. A release candidate does not require public hosting.

## Project structure grows with the game

Keep one mechanic in a small consumer project with a brief/rules record, source, local run instructions and evidence. Add scene/content and handoff records when things interact; add progression, save/network and load fixtures only when those behaviours exist. A larger game needs stable identities and affected-case regression, not a universal folder tree.

Use the project's native representation. Separate source deliveries from imported/runtime state so the correct owner can repair a defect. Preserve baseline, fault and repair identities without copying every artefact into global approval folders. [Workflows and artefacts](docs/02-game-development-skills-workflows-and-artifacts-spec.md) define the required meaning, not a mandatory GDD or shared engine.

## Core skills

| Designed skill | Owned outcome |
|---|---|
| `game-development` | Design, build, integrate, evaluate and repair requested playable gameplay; prepare the appropriate build |
| `game-evaluate` | Independently evaluate gameplay, balance, experience, accessibility and performance; diagnose the responsible repair without unrequested game changes |
| `game-extension-pack-creator` | Research, implement or revise a reusable specialisation with evidence, fair core comparison and truthful readiness |

The [fourteen operation contracts](docs/03-game-development-skills-repository-and-contracts-spec.md#3-command-contract) are named workflows that also accept natural-language requests, not a new shell CLI.

## Extension Packs

Packs are optional gameplay guidance. Explicit project instructions and accepted game decisions take precedence over pack defaults. No selection means core behaviour.

| Researched profile | Intended difference | Current proof state |
|---|---|---|
| [Precision Platformer](docs/06-game-development-extension-pack-catalogue.md#2-precision-platformer) | Relate measured movement and action boundaries to spatial demands, information and responsible repair | P1–P5 complete; implementation planned; evaluation/install not run; not ready |
| [Tactical Turn-based](docs/06-game-development-extension-pack-catalogue.md#3-tactical-turn-based) | Relate information and legal opportunities to commitment, ordered resolution and encounter decisions | P1–P5 complete; implementation planned; evaluation/install not run; not ready |

When implemented, the consuming skill carries its own optional profiles. A project can explicitly select `Game Development packs: precision-platformer (PP-01)`. No creator, other pack, source books or research checkout is needed to apply local guidance. The [authoring contract](docs/05-game-development-customisation-packs-spec.md) requires exact showcases, distinct reuse, behavioural tests, fair comparison and clean installed use before readiness.

## Execution paths

The skills decide the gameplay work and acceptance; the existing coding agent and native tools execute it. The first proof path is ordinary local HTML/JavaScript with semantic controls, optional Canvas and actual browser input through Playwright. Godot is the next documented native reference; Unity, Unreal and Roblox retain separate optional tool/context requirements. None is claimed installed or demonstrated by research alone.

3D libraries, multiplayer transports and other dependencies belong to the relevant game and must be declared and run. No mandatory provider, MCP, telemetry service, Pactwright runtime or shared engine is required. [Execution architecture](docs/01-game-development-skills-system-spec.md#6-execution-architecture) defines detection, project identity, observation and failure handling.

## Playtesting, evaluation and benchmarks

Keep rule correctness, systemic behaviour, actual human experience, access, performance and preservation separately visible. Scripts test exercised rules; telemetry needs valid collection; a screenshot cannot prove feel; a mean frame time can hide stalls. Retain failures and repair the responsible rule, state, cue, integration or evidence boundary.

[Testing and benchmarks](docs/04-testing-and-benchmark-spec.md) specifies ten layers, twenty core case families, eight routing probes and the pack/install gates. The [case designs](docs/research-logs/2026-09-13-stage-14-case-designs.md) contain setups, independent oracles and repair boundaries. **Runtime benchmarks and human sessions have not yet been executed.** Actual run records will be linked as they are produced.

## Documentation

| Specification | Purpose |
|---|---|
| [01 — System](docs/01-game-development-skills-system-spec.md) | Mission, scope, skills, execution, integration and acceptance |
| [02 — Workflows and artefacts](docs/02-game-development-skills-workflows-and-artifacts-spec.md) | Thesis, behaviour, composition, content, evidence and repair |
| [03 — Repository and contracts](docs/03-game-development-skills-repository-and-contracts-spec.md) | Operations, self-containment, dependencies, install and CI |
| [04 — Testing and benchmark](docs/04-testing-and-benchmark-spec.md) | Cases, curriculum, proof methods and release gates |
| [05 — Customisation and Extension Packs](docs/05-game-development-customisation-packs-spec.md) | Qualification, research, authoring, selection and readiness |
| [06 — Extension Pack catalogue](docs/06-game-development-extension-pack-catalogue.md) | Actual researched profiles, exact prompts, reuse and evidence status |

The [research index](docs/research-logs/README.md) links source evidence, accepted decisions, the [bootstrap process](docs/research-logs/2026-09-07-game-development-skills-new-project-bootstrap-process.md) and its [execution contract](docs/research-logs/2026-09-13-bootstrap-execution-contract.md).

## Project boundary

Game Development owns playable meaning and integration. Narrative, environment/3D, animation, audio and visual specialists own their source craft; engineering owns general implementation quality. A handoff states the intended use, delivered properties, binding and actual gameplay acceptance. General studio management, commercial guarantees, platform certification and an all-purpose engine are outside this project.

## Contributing

Keep changes bounded to the responsible skill, rule, fixture or specification. Preserve source provenance and accepted decisions, add the smallest meaningful regression for an escaped defect and report actual evidence limits. Follow the current [repository and validation contract](docs/03-game-development-skills-repository-and-contracts-spec.md). The scaffold stage will add the contributor runbook and executable local checks.

## Licence

The scaffold will add MIT for original repository-authored code and guidance. That planned licence does not relicense supplied books, third-party source material or assets; those are excluded or retain their own terms. No private source PDFs are distributed here.
