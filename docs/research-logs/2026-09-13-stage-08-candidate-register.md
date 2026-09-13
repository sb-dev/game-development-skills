# Stage 8 — Execution candidate register

Research snapshot: **2026-09-13**. This register contains **22 candidates**, each with the bootstrap's **14 fields**. Sources and examined locations are in the [source evidence](2026-09-13-stage-08-source-evidence.md); operation coverage and delegation decisions are in the [landscape](2026-09-13-stage-08-execution-capability-landscape.md).

Classifications are research dispositions: **USE** an existing operation when that execution path is selected; **ADAPT** a small project binding around an existing tool; **REFERENCE** informs design without becoming a dependency; **REJECT** excludes a candidate from a new integration. They do not select an engine, install anything, authorise publishing, or claim a successful execution. Maturity assessments concern the examined documentation and repository state, not measured reliability. Scripted operations can still depend on timing, engine state, seeds and external services; “scripted” does not promise deterministic simulation.

## C01 — Game-design Agent Skills

| Field | Record |
|---|---|
| Capability | Design critique and arithmetic balance investigation. |
| Source | [Yuki001/game-dev-skills](https://github.com/Yuki001/game-dev-skills); examined design-review and balance-analysis skills. |
| Licence | Unresolved: repository metadata has no licence; no root licence or licence declaration in the examined skills. Do not copy them into this project. |
| Maturity | Published instruction collection; no independent execution evaluation examined. |
| Engine / platform | Largely engine independent; relies on its host agent. |
| Installation | Repository skill folders consumed by a compatible agent; reference only here. |
| Production role | Review a design or identify a balance experiment. |
| Deterministic vs generative | Generative review; optional scripted arithmetic. |
| Editor / runtime access | None supplied intrinsically. |
| Composability | Skill instructions can request host tools. |
| Quality suitability | Useful distinctions between facts, assumptions and proposed checks. |
| Maintenance | Repository pushed 2026-08-25; not archived. |
| Classification | **REFERENCE** — conceptual comparison only. |
| Gaps | Cannot establish player response; temporary-script deletion guidance does not satisfy this bootstrap's durable evidence requirement. |

## C02 — Space Engineers gameplay-programming skill

| Field | Record |
|---|---|
| Capability | Prepare and compile Space Engineers programmable-block scripts. |
| Source | [CometWorks/skills](https://github.com/CometWorks/skills), `skills/se-dev-script/SKILL.md`. |
| Licence | MIT according to repository metadata. |
| Maturity | Narrow published workflow; game API reference identifies version 1.208.015. |
| Engine / platform | Space Engineers 1; Windows preparation and Linux development tooling. |
| Installation | Skills CLI or manual skill placement; separate preparation, uv, .NET and API indexing prerequisites. |
| Production role | Implement and check game-specific code. |
| Deterministic vs generative | Generative code; scripted build and inspection. |
| Editor / runtime access | Build output and prepared API information; game loading remains separate. |
| Composability | Agent skill plus shell tools. |
| Quality suitability | Concrete example of engine-specific instructions and a build gate. |
| Maintenance | Repository pushed 2026-09-13; not archived. |
| Classification | **REFERENCE** — coupling is outside the initial project scope. |
| Gaps | Compilation does not enforce the game's complete runtime whitelist; not a general gameplay implementation skill. |

## C03 — Engine-independent coding agent

| Field | Record |
|---|---|
| Capability | Edit repository code, inspect diffs and invoke existing lint/test commands. |
| Source | [Aider](https://github.com/Aider-AI/aider). |
| Licence | Apache-2.0; model services have separate terms. |
| Maturity | Documented repository-oriented workflow; no comparative benchmark performed here. |
| Engine / platform | Language and repository tooling rather than one engine. |
| Installation | Python `aider-install` workflow; configure a supported provider or local model. |
| Production role | Engineering implementation and repair. |
| Deterministic vs generative | Generative edits; external scripted checks. |
| Editor / runtime access | Files and invoked processes; no intrinsic game-editor state. |
| Composability | CLI, Git and project commands. |
| Quality suitability | Existing coding agents can perform this role without a new game-specific coding runtime. |
| Maintenance | Repository pushed 2026-05-22; not archived. |
| Classification | **USE** — delegate engineering to an existing compatible agent; Aider is an examined option, not a mandatory second agent. |
| Gaps | Game intent, engine bindings, execution assertions and evidence interpretation remain project responsibilities. |

## C04 — Godot native execution and inspection

| Field | Record |
|---|---|
| Capability | Import, run, export, debug, capture movies, inject input and query navigation. |
| Source | [Godot](https://github.com/godotengine/godot); official CLI, Input and NavigationAgent documentation in the source log. |
| Licence | MIT engine; dependencies and imported assets retain their own licences. |
| Maturity | Latest release API returned 4.7.2-stable; no binary exercised here. |
| Engine / platform | Godot; available exports depend on platform templates and SDKs. |
| Installation | Official editor binary; matching export templates and project presets. |
| Production role | Project execution, content integration and technical evidence collection. |
| Deterministic vs generative | Scripted; simulation reproducibility needs a controlled fixture. |
| Editor / runtime access | Editor/import commands, project scripts, runtime Input and navigation APIs. |
| Composability | CLI and GDScript/C# project bindings. |
| Quality suitability | Broad native operations with a small project harness. |
| Maintenance | Repository pushed 2026-09-13; release published 2026-08-18. |
| Classification | **USE** — delegate native operations if Godot is selected. |
| Gaps | Headless mode cannot prove perception; movie capture uses fixed timing; navigation needs project movement; `--test` tests the engine, not project gameplay. |

## C05 — Godot MCP bridge

| Field | Record |
|---|---|
| Capability | Launch projects, retrieve debug output and perform specified scene operations. |
| Source | [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp). |
| Licence | MIT according to repository metadata. |
| Maturity | Documented community bridge; compatibility and failure recovery untested here. |
| Engine / platform | Godot; UID helpers require 4.4 or later. |
| Installation | Node.js 18+, installed Godot, npm MCP package and configured executable path. |
| Production role | Agent access to engine operations. |
| Deterministic vs generative | Scripted tools; calling agent may generate arguments/code. |
| Editor / runtime access | Process output and documented create/add/save scene operations through bundled scripts. |
| Composability | MCP server wrapping Godot operations. |
| Quality suitability | Potential convenience where native CLI calls become repetitive. |
| Maintenance | Repository pushed 2026-04-16; not archived. |
| Classification | **ADAPT** — only a demonstrated missing access operation warrants a binding. |
| Gaps | Examined tool list does not establish continuous live-state inspection or a complete input/replay interface; no reason to make MCP compulsory. |

## C06 — Unity native Editor, tests and Profiler

| Field | Record |
|---|---|
| Capability | Batch Editor scripts, project tests and performance collection. |
| Source | Unity 6.0 command-line and Profiler manuals; Test Framework 1.4 manual. |
| Licence | Unity Editor/provider terms; package-specific terms also apply. No engine-source redistribution proposed. |
| Maturity | Versioned native documentation; project/platform behaviour still requires execution. |
| Engine / platform | Unity Editor plus installed target-platform modules. |
| Installation | Licensed Editor and modules; project Test Framework package. |
| Production role | Build/import automation, EditMode/PlayMode checks and performance diagnosis. |
| Deterministic vs generative | Scripted operations and measurements. |
| Editor / runtime access | Editor methods; test contexts; Profiler sources include Editor and target Player. |
| Composability | Batch CLI, C# and NUnit-based testing. |
| Quality suitability | Prefer native mechanisms for reproducible engineering checks. |
| Maintenance | Unity 6.0 and package 1.4 documentation examined on 2026-09-13. |
| Classification | **USE** — conditional on Unity selection. |
| Gaps | Batch project cannot also be open in another Editor instance; Editor timings do not establish target-device performance; gameplay assertions must be supplied. |

## C07 — Unity Assistant and AI Gateway

| Field | Record |
|---|---|
| Capability | Editor-grounded generative assistance and external-agent model access. |
| Source | Unity's May 2026 AI announcement and Assistant 2.19 Gateway documentation. |
| Licence | Unity AI/provider terms; Gateway eligibility and agent/provider requirements are separate. |
| Maturity | Open-beta announcement; examined package 2.19.0-pre.2 is prerelease. |
| Engine / platform | Unity 6+; linked organisation/project for documented service access. |
| Installation | Assistant package; Gateway requires eligible subscription, assigned seat and matching organisation. |
| Production role | Interactive authoring assistance. |
| Deterministic vs generative | Generative planning, code and editor changes. |
| Editor / runtime access | Assistant can use Editor context; Gateway alone is not a gameplay-state inspector. |
| Composability | In-editor assistant and supported external agents. |
| Quality suitability | Useful optional interaction layer; generated changes need native verification. |
| Maintenance | Gateway documentation generated 2026-09-01. |
| Classification | **REFERENCE** — service dependency is unnecessary for the initial local proof. |
| Gaps | No measured quality improvement here; beta/service dependencies; old Assistant MCP instructions are superseded separately in C22. |

## C08 — Community Unity MCP

| Field | Record |
|---|---|
| Capability | Expose scene, asset, script, test, build and profiling operations to agents. |
| Source | [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp); examined default-branch README. |
| Licence | MIT bridge; Unity and dependencies have separate terms. |
| Maturity | README documents v10.0.0; default branch is `beta`. Advertised breadth is not independently benchmarked. |
| Engine / platform | README advertises Unity 2021.3 LTS through 6.x. |
| Installation | Versioned UPM package plus Python 3.10+ / uv server and MCP client configuration. |
| Production role | Editor automation from an external agent. |
| Deterministic vs generative | Tool operations scripted; caller-generated changes require checks. |
| Editor / runtime access | Editor plugin tools; exact runtime evidence depends on invoked tool/context. |
| Composability | UPM plugin and MCP transport. |
| Quality suitability | Candidate bridge when required operations exceed the chosen native interface. |
| Maintenance | Repository pushed 2026-09-05; v10.0.0 dated 2026-06-30. |
| Classification | **ADAPT** — pin and prove the specific binding before relying on it. |
| Gaps | Additional bridge/server lifecycle; advertised tools do not prove project outcomes. Unity's in-editor MCP deprecation does not deprecate this repository. |

## C09 — Unreal native automation and runtime facilities

| Field | Record |
|---|---|
| Capability | Script editor work; execute functional/screenshot tests; orchestrate sessions; replay and emulate networks. |
| Source | Epic's Python, Automation Test Framework, Gauntlet, Replay and Network Emulation documentation. |
| Licence | Unreal Engine EULA and applicable third-party terms; use installed tools rather than redistribute engine source. |
| Maturity | Native documentation displayed Unreal 5.8; Python plugin labelled experimental. |
| Engine / platform | Unreal; target builds and SDKs are platform-specific. |
| Installation | Engine, required plugins and platform tooling; project tests and session configuration. |
| Production role | Content automation, runtime regression and technical diagnosis. |
| Deterministic vs generative | Scripted; network scenarios and replay state are explicitly configured. |
| Editor / runtime access | Python is editor-only; functional tests, replay and game sessions provide separate runtime paths. |
| Composability | Python/commandlets, C++/Blueprint tests and Gauntlet process orchestration. |
| Quality suitability | Existing layered facilities cover distinct proof types. |
| Maintenance | Current primary documentation examined 2026-09-13. |
| Classification | **USE** — conditional on Unreal selection. |
| Gaps | Gauntlet does not invent assertions; replay requires replicated data and compatibility handling; emulation is not evidence of real network populations. |

## C10 — Roblox Studio built-in MCP

| Field | Record |
|---|---|
| Capability | Inspect/edit the data model, run Luau, playtest, capture screens and simulate input. |
| Source | Roblox's current Studio MCP and accelerated-workflows documentation. |
| Licence | Roblox Studio/provider terms; no open-source licence established for the built-in implementation. |
| Maturity | Current provider-documented integration replacing the archived standalone server. |
| Engine / platform | Roblox Studio; documented Windows/macOS setup. |
| Installation | Installed Studio and a configured compatible MCP client. |
| Production role | Authoring and bounded playtest automation. |
| Deterministic vs generative | Scripted tools plus optional generative services/agent decisions. |
| Editor / runtime access | Data-model inspection, explicit Edit/Client/Server Luau context, play state and input. |
| Composability | Built-in stdio MCP; target Studio instance explicitly. |
| Quality suitability | Broad native access for a Roblox-specific workflow. |
| Maintenance | Live provider documentation examined 2026-09-13. |
| Classification | **USE** — conditional on Roblox selection. |
| Gaps | No headless Linux Studio or publish/install proof established; screen/input access does not establish player enjoyment. |

## C11 — Archived Roblox standalone MCP server

| Field | Record |
|---|---|
| Capability | Legacy Studio script execution, console capture and play control. |
| Source | [Roblox/studio-rust-mcp-server](https://github.com/Roblox/studio-rust-mcp-server). |
| Licence | MIT according to repository metadata. |
| Maturity | Archived; README explicitly ends development and recommends built-in Studio MCP. |
| Engine / platform | Roblox Studio with a separate plugin/server. |
| Installation | Historical Windows/macOS binaries or Cargo build and plugin setup. |
| Production role | Legacy external-agent bridge. |
| Deterministic vs generative | Scripted bridge; generative caller possible. |
| Editor / runtime access | Documented script and play-mode operations through the plugin. |
| Composability | Rust server, stdio and Studio communication. |
| Quality suitability | Explains older integrations; weak basis for new work. |
| Maintenance | Archived; last push 2026-04-03. |
| Classification | **REJECT** — use the current native candidate C10 for new integration research. |
| Gaps | No ongoing development; installation and tool semantics differ from current built-in MCP. |

## C12 — ML-Agents for automated policies

| Field | Record |
|---|---|
| Capability | Train and run agents in instrumented game environments. |
| Source | [Unity-Technologies/ml-agents](https://github.com/Unity-Technologies/ml-agents), `Readme.md` and `LICENSE.md`. |
| Licence | Apache-2.0 in the actual licence file; repository API reported NOASSERTION. |
| Maturity | README release table: Release 23, Unity package 4.0.0, Python 1.1.0; development branch is not a stable pin. |
| Engine / platform | Unity environments; Python/PyTorch training dependencies. |
| Installation | Matching released Unity and Python packages, then project observations/actions/rewards and training setup. |
| Production role | Behaviour experiments and automated scenario exploration. |
| Deterministic vs generative | Learned policies and stochastic training; explicit seeds/configuration matter. |
| Editor / runtime access | Project-supplied environment observations and action channels. |
| Composability | Unity package, Python API and training processes. |
| Quality suitability | Useful when a learned policy answers a defined question. |
| Maintenance | Repository pushed 2026-09-02; examined release dated 2025-08-28. |
| Classification | **ADAPT** — bind an explicit scenario, policy and oracle. |
| Gaps | Reward optimisation is not enjoyment; policy blind spots and training cost; no ready-made proof of arbitrary gameplay coverage. |

## C13 — GameAnalytics telemetry SDK

| Field | Record |
|---|---|
| Capability | Collect sessions, progression, resource and custom events for backend analysis. |
| Source | [GameAnalytics Unity SDK](https://github.com/GameAnalytics/GA-SDK-UNITY) and provider implementation-planning documentation. |
| Licence | MIT SDK; hosted service and account use have separate terms. |
| Maturity | Documented SDK and service workflow; ingestion and metrics untested here. |
| Engine / platform | Examined candidate is Unity-specific; other SDKs require their own integration. |
| Installation | UPM/OpenUPM or Unity package; configure the game's service keys and events. |
| Production role | Instrumentation and quantitative observation. |
| Deterministic vs generative | Programmed event collection and backend aggregation. |
| Editor / runtime access | Runtime events explicitly emitted by the integration. |
| Composability | SDK API and provider dashboards; not a universal game-state interface. |
| Quality suitability | Candidate for an established need for hosted telemetry. |
| Maintenance | Repository pushed 2026-09-07; provider documentation examined 2026-09-13. |
| Classification | **REFERENCE** — local proof does not yet require a hosted dependency. |
| Gaps | Missing events, version/cohort mixing and denominator mistakes still require Stage 7 checks; service collection cannot infer causal player experience. |

## C14 — Playwright browser execution

| Field | Record |
|---|---|
| Capability | Automate browser input and assertions; collect screenshots, video and traces. |
| Source | [microsoft/playwright](https://github.com/microsoft/playwright). |
| Licence | Apache-2.0; bundled browser/dependency terms remain separate. |
| Maturity | Established documented test runner; no browser-game benchmark performed here. |
| Engine / platform | Browser games and web interfaces; not native game windows. |
| Installation | Project Playwright package plus matching browser binaries/dependencies. |
| Production role | Browser-based functional checks and evidence capture. |
| Deterministic vs generative | Scripted tests; model-driven MCP use is a distinct caller layer. |
| Editor / runtime access | DOM, browser input, network and exposed application hooks. |
| Composability | Test runner, library, CLI and MCP options. |
| Quality suitability | Existing runner for a web execution path. |
| Maintenance | Repository pushed 2026-09-11; not archived. |
| Classification | **USE** — if the selected proof runs in a browser. |
| Gaps | DOM locators do not reveal a canvas game's internal state; project hooks and meaningful assertions remain necessary. |

## C15 — axe-core accessibility checks

| Field | Record |
|---|---|
| Capability | Detect supported accessibility violations in rendered web interfaces. |
| Source | [dequelabs/axe-core](https://github.com/dequelabs/axe-core). |
| Licence | MPL-2.0; retain applicable notices and review modified-file obligations if distributing modifications. |
| Maturity | Documented rules and integration examples; incomplete findings require review. |
| Engine / platform | HTML/web UI, including browser-based menus; not arbitrary native game rendering. |
| Installation | Project npm dependency and `axe.run` integration in the test context. |
| Production role | One part of accessibility verification. |
| Deterministic vs generative | Rule-based analysis of the examined UI state. |
| Editor / runtime access | Rendered page structure; only states exercised by the test. |
| Composability | JavaScript API and existing browser test runners. |
| Quality suitability | Useful automated signal alongside human and device-specific review. |
| Maintenance | Repository pushed 2026-09-11; not archived. |
| Classification | **ADAPT** — exercise relevant states and map findings to repair owners. |
| Gaps | Cannot certify all accessibility, gamepad use, audio comprehension or canvas gameplay; do not generalise a provider coverage percentage. |

## C16 — SteamPipe platform build delivery

| Field | Record |
|---|---|
| Capability | Package/upload depot content and identify platform builds and manifests. |
| Source | [Steamworks: Uploading to Steam](https://partner.steamgames.com/doc/sdk/uploading). |
| Licence | Steamworks SDK/partner terms and account permissions; no SDK source reuse proposed. |
| Maturity | Documented production delivery workflow; no upload performed here. |
| Engine / platform | Engine-independent built content; Windows/Linux/macOS builder variants. |
| Installation | Steamworks SDK ContentBuilder tools, SteamCMD, app/depot configuration and authorised builder account. |
| Production role | Platform packaging, delivery and installation verification. |
| Deterministic vs generative | Scripted file mappings; external service creates build/manifest identities. |
| Editor / runtime access | Build files and delivery logs; no gameplay state. |
| Composability | SteamCMD and app/depot VDF scripts. |
| Quality suitability | Delegate a chosen Steam delivery workflow to its existing tools. |
| Maintenance | Live Valve documentation examined 2026-09-13. |
| Classification | **USE** — only if Steam delivery is in scope and authorised. |
| Gaps | Upload/build identity does not prove installed play or release approval; platform access remains a prerequisite. |

## C17 — itch.io butler

| Field | Record |
|---|---|
| Capability | Send build content to an itch.io project channel. |
| Source | [itchio/butler](https://github.com/itchio/butler) and the official installation manual. |
| Licence | MIT project; distributed third-party components have additional licence files. |
| Maturity | Documented stable and development binary channels; no delivery tested here. |
| Engine / platform | Built game directories; platform-specific host binaries. |
| Installation | Download an identified official binary, extract, add to PATH, verify version and authenticate for uploads. |
| Production role | Build delivery and update distribution. |
| Deterministic vs generative | Scripted content transfer; service-side state changes. |
| Editor / runtime access | Files and upload status; no editor/gameplay access. |
| Composability | CLI called by an existing build process. |
| Quality suitability | Small existing delivery tool when itch.io is selected. |
| Maintenance | Repository pushed 2026-09-12; not archived. |
| Classification | **USE** — conditional on chosen delivery target and authority. |
| Gaps | Successful push is not a clean install, playable proof or permission to publish; avoid floating binary versions in proof records. |

## C18 — LimboAI behaviour trees and state machines

| Field | Record |
|---|---|
| Capability | Author and run behaviour trees and hierarchical state machines with debugging support. |
| Source | [limbonaut/limboai](https://github.com/limbonaut/limboai). |
| Licence | MIT according to repository metadata. |
| Maturity | Documented Godot/version compatibility matrix; extension and module paths differ. |
| Engine / platform | Godot 4; choose the matching release and binary platform. |
| Installation | Compatible GDExtension addon or engine module; extension avoids a custom engine build. |
| Production role | Implement and inspect project AI behaviour. |
| Deterministic vs generative | Authored tasks/transitions; randomness depends on project tasks. |
| Editor / runtime access | Behaviour-tree editor, BTPlayer, blackboard and runtime debugger; HSM uses a code API. |
| Composability | GDScript tasks and Godot resources/nodes. |
| Quality suitability | Existing authoring/runtime tooling when a plain script becomes inadequate. |
| Maintenance | Repository pushed 2026-09-04; compatibility table includes Godot 4.7 module builds. |
| Classification | **ADAPT** — write game tasks and observations, not a new behaviour-tree runtime. |
| Gaps | Behaviour architecture does not establish readable/fair opponents; no HSM GUI advertised; wrong release/binary can break integration. |

## C19 — WaveFunctionCollapse generation

| Field | Record |
|---|---|
| Capability | Generate patterns/tiles under local adjacency constraints. |
| Source | [mxgmn/WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse); README and actual `LICENSE`. |
| Licence | MIT code; licence explicitly excludes image samples and tiles from the licensed software. |
| Maturity | Published reference implementation; no project-level benchmark performed. |
| Engine / platform | Engine-independent C#/.NET console implementation. |
| Installation | Build/run the project with .NET; configure inputs such as `samples.xml`. |
| Production role | Generate candidate content for further validation. |
| Deterministic vs generative | Constraint-based generation with random choices; contradictions can fail a run. |
| Editor / runtime access | Input/output artefacts; engine integration is separate. |
| Composability | Console process or a separately evaluated compatible port. |
| Quality suitability | Useful technique to compare when local pattern constraints matter. |
| Maintenance | Repository pushed 2026-03-22; not archived. |
| Classification | **REFERENCE** — no procedural-generation need has been established for the first proof. |
| Gaps | Local consistency does not guarantee global reachability, pacing or playability; example-image rights are not granted by the code licence. |

## C20 — GUT project tests

| Field | Record |
|---|---|
| Capability | Run Godot project script tests with assertions, doubles and reports. |
| Source | [bitwes/Gut](https://github.com/bitwes/Gut), README and `addons/gut/LICENSE.md`. |
| Licence | MIT in the actual licence file; repository API licence was null. |
| Maturity | README maps GUT 9.7.1 to Godot 4.7.x; `main` describes a different compatibility line. |
| Engine / platform | Godot/GDScript; pin a compatible release rather than assuming latest/main fits. |
| Installation | Place `addons/gut`, enable the plugin and restart; select the matching release or Asset Library package. |
| Production role | Rule regressions and project-level technical checks. |
| Deterministic vs generative | Scripted tests; fixtures control game state. |
| Editor / runtime access | Project tests execute against Godot scripts/nodes; CLI and editor running paths. |
| Composability | Test addon, CLI and JUnit XML output. |
| Quality suitability | Candidate existing runner for Godot gameplay checks. |
| Maintenance | Repository pushed 2026-08-18; compatibility guidance inspected. |
| Classification | **USE** — if Godot is selected and this runner adds needed value. |
| Gaps | Assertions/scenarios remain project-owned; passing script tests cannot establish feel or target-device performance. |

## C21 — Unity CLI and Pipeline package

| Field | Record |
|---|---|
| Capability | Manage Editor installations and execute commands/code against a running Editor. |
| Source | Unity CLI overview/use/replacement guide and Unity Pipeline package documentation. |
| Licence | Provider-distributed tools; CLI requires no Unity AI subscription. Editor and package terms remain separate. |
| Maturity | Official documentation explicitly calls CLI experimental. |
| Engine / platform | CLI host support documented for Windows, macOS and Linux; Editor control requires Unity 6.0 LTS+. |
| Installation | Hub or standalone CLI; documented authentication/setup and `unity pipeline install` for Editor control. |
| Production role | Native external-agent execution interface. |
| Deterministic vs generative | Scripted CLI operations; agent-authored code remains generative. |
| Editor / runtime access | Pipeline local HTTP API to the running Editor; target project/instance explicitly. |
| Composability | CLI, structured output, `unity command`, `unity eval`, and a separate `unity mcp` option. |
| Quality suitability | Current native candidate to evaluate before another Unity bridge. |
| Maintenance | Use guide updated 2026-09-11; examined 2026-09-13. |
| Classification | **ADAPT** — experimental interface needs a pinned, bounded operation proof. |
| Gaps | Not an installed proof; Editor access alone is not runtime assertions; Assistant versions below 2.13 have a documented conflict. |

## C22 — Deprecated Unity Assistant in-editor MCP server

| Field | Record |
|---|---|
| Capability | Legacy external-agent connection to Assistant's in-editor tools. |
| Source | Assistant 2.19 MCP getting-started page and Unity CLI replacement guide. |
| Licence | Unity Assistant/provider terms; no open-source reuse licence established. |
| Maturity | Explicitly deprecated in current provider documentation. |
| Engine / platform | Unity 6+ with the relevant Assistant package and relay. |
| Installation | Historical Assistant/relay setup; current guide points to CLI/Pipeline instead. |
| Production role | Legacy editor-agent bridge. |
| Deterministic vs generative | Tool transport; caller may generate actions. |
| Editor / runtime access | Assistant editor tool access, not a general standalone game runtime. |
| Composability | Former in-editor MCP route. |
| Quality suitability | Retain only as migration context for older research. |
| Maintenance | Deprecation visible in 2.19.0-pre.2 documentation generated 2026-09-01. |
| Classification | **REJECT** — do not choose this deprecated path for new work. |
| Gaps | This deprecation does not include `unity mcp` in the new CLI or third-party servers such as C08. |
