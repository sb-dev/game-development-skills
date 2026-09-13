# Execution and Installation Contract

**Version:** 1.0  
**Defined by:** [Stage 9 decisions and verification](../research-logs/2026-09-13-stage-09-execution-layer-and-engine-integration.md)  
**Inputs:** the accepted thesis, behaviour, prototype, integration and evaluation contracts.

## 1. Selected architecture

Skills direct game-development work through the consumer's existing coding agent, editor and runtime tools. They describe the intended operation, accepted constraints and required evidence. The engine or runtime implements that operation in its own terms. Existing test, capture and measurement tools return observations which the skill interprets against the game contract.

The first proof path is a **bounded local browser game**, using ordinary project-owned HTML/JavaScript, browser rendering/input, and Playwright for browser execution and evidence capture. Use semantic HTML for controls, instructions and status; Canvas may render the playfield when appropriate. This chooses a cheap execution path, not the game's thesis, mechanics, example catalogue or a new shared game engine. Do not build a cross-engine scene system, physics engine, UI toolkit or test runner for this proof. A later question that needs established engine facilities should use the appropriate engine.

Godot native CLI/scripts are the next documented engine-specific reference path. Unity native Editor/testing and CLI/Pipeline, Unreal's layered editor/runtime facilities, and Roblox Studio's built-in MCP remain distinct optional paths. Their documented capabilities are not installed support. The core has no mandatory engine, MCP server, cloud AI provider, second coding agent, hosted telemetry service, Extension Pack or Pactwright dependency.

All engine-neutral semantics come from accepted production needs: intent, constraints, decisions/revisions, action/rule expectations, content handoffs, evidence conditions, findings and repair scope. This is a common way to explain work, not an API that pretends all engines have identical entities, scenes, input, time or physics.

## 2. Provider and engine boundaries

| Execution responsibility | Concrete owner | Skill supplies / checks |
|---|---|---|
| Code generation | Consumer's developer or existing coding agent | Behaviour semantics, permitted changes, review and runtime acceptance |
| Engine editor manipulation | Selected native Editor API or justified bridge | Explicit project/instance, intended edit, preserved data and observed result |
| Scene creation | Selected engine's own scene/content representation; ordinary game data for the browser proof | Composition, placement and gameplay relationships; no invented universal scene format |
| Asset generation | Appropriate specialist or existing generation tool | Handoff requirements, rights constraints already supplied by the project and integration acceptance |
| Build execution | Existing engine export/build tools or project packaging command | Target, source/configuration identity, output and failure checks |
| Input simulation | Engine runtime input/test facility or Playwright | Declared input route, action sequence and timing; direct state mutation is not an input test |
| Runtime state inspection | Project hooks, native debugger/tests or explicit runtime API | Authoritative values needed by the current assertion, session and observation time |
| Profiling | Existing target-runtime profiler/measurement tools | Workload, target/build, relevant measurement and limit on inference |
| Capture | Existing engine/browser screenshot, video or trace facilities | Required moments, run identity and visual/behavioural question |
| Telemetry | Project event log or an explicitly selected SDK/service | Event meaning, collection verification, revisions/cohorts and denominators |
| Platform deployment | Existing export and chosen platform delivery tools | Identified candidate, destination, existing authority and separate installation/play checks |

An execution provider returns what actually happened, including failure, timeout or partial completion. Generated prose, a success exit code or a tool's advertised capability is not by itself the required gameplay evidence. Read the concrete outputs and compare them with the requested operation.

## 3. Adapter placement

| Location | Decision |
|---|---|
| Core SKILL.md | Keep the production workflow, acceptance and tool-selection rules here. Do not embed a large engine manual or require a provider. |
| A skill's own `references/` | Put concise engine-specific operation guidance here when the skill needs it. Include native context, prerequisites, invocation shape, expected evidence and limits. Load only the relevant reference. |
| A skill's own `scripts/` | Add only a reusable, demonstrated helper that cannot reasonably be a direct existing command. Bundle its complete dependency contract; it must run after selective installation. None is required by this architecture decision. |
| An example or consumer game | Keep scene paths, rule adapters, game-state snapshots, input drivers and test fixtures here. These belong to that game, not to all installed skills. |
| Separate package | Do not create one now. An existing engine plugin remains separately installed. A new shared integration package needs demonstrated repeated use and an independent installation/versioning benefit. |

Avoid references from an installed skill into repository-root docs, sibling skill folders, research logs or source-only examples for required runtime instructions. Each independently installable skill includes its essential guidance and referenced resources. Short common principles may be repeated deliberately; this is preferable to an undeclared runtime dependency. Repository validation checks the installed resource closure. Detailed historical research remains outside the install payload.

## 4. Minimum inspection surface

The required surface is defined by the current proof. It is a checklist for choosing actual tools, not eight mandatory API endpoints or a new capability registry.

| Observation/action | Required when | Evidence boundary |
|---|---|---|
| Identify project, source/build and execution tool/version | Every executed proof | A responding process must be the intended project/runtime. Record the selected path explicitly. |
| Inspect editable objects/data and dependencies | Editing/importing/repairing that content | Read the relevant engine-native object or project data before editing; not an obligatory global graph scan. |
| Start, observe readiness, reset and stop the session | A playable/runtime proof | A fresh declared start/reset state and bounded termination; readiness is more than process launch. |
| Apply actions through the route under test | Input, control or gameplay sequence claims | Distinguish native input, scripted action API and direct fixture setup. Test input binding through actual input when claimed. |
| Observe authoritative rule/state results | Mechanical or interaction claims | Read the relevant state plus invariants/outcomes; a displayed label alone can be stale or wrong. |
| Observe player-facing feedback | Feedback/integration/playable claims | Check the appropriate visible, audible or other cue; state success does not establish perception. |
| Retrieve errors, logs and requested evidence | Every executed proof | Retain errors and partial results; missing evidence is not success. Tie outputs to the current run. |
| Collect target measurements/captures | Performance, visual or other claims that need them | Name enabled measures, target and capture timing; headless/editor evidence cannot certify unobserved hardware or human experience. |

For the browser proof, Playwright runs the same page a player uses. A small game-owned read-only state snapshot can make rule assertions possible through `page.evaluate`; it must identify the game state and not substitute the test runner's own model. Fixture setup is explicit and separate. At least the claimed control path is exercised through real browser input. Capture and state assertions must agree on the same run. Do not expose a general remote command server merely to inspect one local game.

For Godot, project tests/scripts observe nodes and rule state; native input events and import/export commands remain Godot-specific. For Unity, Editor objects, PlayMode tests and a target Player are different contexts. Unreal editor Python cannot stand in for gameplay runtime execution. Roblox tools must state the Studio instance and Edit/Client/Server context. No adapter may erase those distinctions.

## 5. Detect and choose available tooling

1. Read the consumer's current instructions, accepted execution decision, project manifests and commands. An existing project's engine takes precedence over the first-proof default.
2. Identify only plausible tools from explicit configuration, project evidence and available executables/integrations. Examples of useful project signals are `project.godot`, Unity's project-version/package files, a `.uproject`, a configured Studio project, or a web package/entry page. A filename alone does not prove a working installation.
3. Perform bounded read-only probes: resolve the configured executable, inspect version/help, locate the project and required modules, or query the explicitly targeted bridge. Do not start a second editor against a locked project or inspect unrelated projects.
4. Record the result beside the proof: tool/version, project/target, operations needed, access context and status **verified for this operation**, **detected but unverified**, **unavailable**, or **unknown**. A tool appearing on PATH is only detected. A successful read does not prove write, build or runtime access.
5. Prefer an adequate native operation already available. Add a thin bridge only for a demonstrated missing access operation. For a new bounded browser proof, select the documented browser route and its normal dependencies; do not force it on an existing engine project.
6. If the required operation is unavailable, report the exact prerequisite or failure and the claim it blocks. Install ordinary declared dependencies under existing authority when permitted. Do not silently replace the proof with documentation or a different engine. A material cost/lock-in or unresolved choice outside existing authority needs the project's owner.

An invocation identifies the working directory/project, concrete operation and arguments, target/build, input fixture/seed when relevant, expected output, bounded timeout and permitted change scope. Results retain exit/status, output paths, actual observations and limitations. This can be a short section in the project's existing evidence record; no new universal transport or schema is required.

On failure, preserve diagnostics; distinguish unavailable tool, wrong project/context, invalid operation, failed game assertion and invalid evidence collection. Stop or clean up only the process/resources owned by that invocation. Never interpret an old capture, stale build or previous success file as the current result. Re-run the failed operation and affected checks after a bounded repair.

## 6. Benchmark engine-specific behaviour

Each claimed path needs an executed, versioned example tied to production questions. Reusing the same acceptance meaning is useful; identical commands, frame timing or numeric performance across engines are not promised.

At minimum, the path's proof exercises its declared start/action/outcome/reset sequence, reads actual runtime state, captures required feedback, detects one relevant fault, applies a scoped repair and repeats affected checks while preserving accepted behaviour. Import, scene editing, profiling, networking or delivery claims add their own concrete cases only when claimed. Negative cases include the relevant missing tool, wrong context, failed operation and missing/stale evidence conditions.

Record skill revision and selected skills, engine/provider/runtime versions, project/build identity, fixture and target conditions, exact commands, outputs, expected versus observed results and limitations. Separate baseline, faulty candidate and repaired result. A simulated or stubbed bridge tests orchestration only and cannot qualify the actual engine path. A new engine/version/path earns its own evidence rather than inheriting another engine's pass.

Performance comparisons hold workload and target conditions stable and report measurement boundaries. Experience and accessibility questions retain the accepted human-evidence rules. Do not average a mechanical pass with a material accessibility or installation failure. Later benchmark design refines case coverage; this contract fixes the engine/provider boundary it must respect.

## 7. Clean and selective installation

The unit installed by the Agent Skills CLI is the selected skill and its own required resources. It does not install an engine or clone the consumer's game. Core use remains standalone without research books, sibling families, optional packs or Pactwright.

Use the standard Skills CLI's named selection, target-agent and copy options when verifying isolation. The command shape is `npx skills add <repository-or-pinned-skill-source> --skill <selected-name> --agent <target-agent> --copy --yes`. Resolve names and pin the tested CLI/source revision in the actual installation record. This is an installation design, not a claim that an unimplemented skill can be installed now.

The clean-consumer check must:

1. Create an external project without the source repository or preinstalled sibling skills available as an implicit dependency.
2. Install only the chosen core skill(s) through the normal CLI. Record source commit, CLI version, agent target and actual install paths; do not assume all agents use the same directory.
3. Check that SKILL.md and every required relative reference/script/asset resolve inside the installed unit. Copy mode helps expose source-linked assumptions; also check ordinary installation behaviour where advertised.
4. Install the declared execution prerequisites separately using their existing package/engine workflows. A preinstalled development dependency cannot be the only documented route.
5. Follow only installed instructions and the consumer's brief to create, run, evaluate and repair the required playable result. Repository examples may be explicit optional inputs, never undisclosed runtime dependencies.
6. Save commands, actual outputs, installed-resource checks and remaining limitations with the consumer proof. Re-run after relevant packaging/resource changes.

Required resources use paths relative to the installed skill, and commands use an explicit consumer project directory. Secrets remain supplied by the consumer's normal tooling rather than bundled in skills. Examples and benchmark tooling have their own declared dependencies and must not require this workspace's absolute paths or runtime-owned packages.

## 8. Scope and authority

This contract authorises the minimal architecture within the existing bootstrap scope. It does not claim that any skill, engine integration, benchmark or clean installation has run. The local browser first proof adds no paid platform or substantial engine lock-in. Consumer commitments, accepted game decisions and publishing retain their existing authority. Broader execution support is qualified only by its own evidence.
