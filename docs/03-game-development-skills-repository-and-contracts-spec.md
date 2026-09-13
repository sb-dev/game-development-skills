# 03 — Repository and Contracts Specification

**Status:** Canonical design; scaffold/implementation/CI/install execution pending  
**Version / date:** 1.0 / 2026-09-13  
**Inputs:** [system](01-game-development-skills-system-spec.md), [workflows](02-game-development-skills-workflows-and-artifacts-spec.md), [evaluation](04-testing-and-benchmark-spec.md), [packs](05-game-development-customisation-packs-spec.md).

## 1. Repository structure and ownership

Commit directories only when their contents have an immediate specified purpose. Keep reusable skills distinct from consumer games, public examples, evaluation fixtures and historical research. Do not create empty engine/provider/pack folders for symmetry.

| Path | Purpose / contract |
|---|---|
| `README.md` | Public product entry, honest maturity, install/use, examples/packs and limitations; Stage 16 owns its design |
| `LICENSE` | Open-source licence for repository-authored material; original code and skill guidance use MIT at scaffold. Supplied books and third-party material are not relicensed or included by that choice |
| `CONTRIBUTING.md` | Local setup, scope/authority, checks, source/fixture/evidence requirements and contribution review |
| `CHANGELOG.md` | Material skill/profile/interface/evidence changes, preserving accepted identities and limitations |
| `docs/01-…` through `docs/06-…` | Six canonical specifications with distinct ownership; contract and catalogue remain separate |
| `docs/research-logs/` | Stage/source/candidate/decision evidence and original prompts/history; not an installed runtime dependency |
| `docs/contracts/` | Accepted earlier detailed design records, retained for traceability; canonical specifications govern consolidated implementation |
| `skills/game-development/` | Independently installable production skill with essential evaluation and local references |
| `skills/game-evaluate/` | Independently installable evaluator accepting external project-native games |
| `skills/game-extension-pack-creator/` | Independently installable domain authoring workflow and local research/proof rules |
| `examples/level-1/` through `examples/level-5/` | Exactly three primary examples per level when implemented, each with actual game output, exact prompt, commands and evidence |
| `examples/extension-packs/` | Actual pack showcases and distinct reuse outputs when implemented; additional to fifteen primary examples |
| `evals/` | Domain benchmark cases, actual run records and smallest behavioural fixtures; no universal quality score |
| `tests/` | Repository validator and other justified deterministic regression tests with meaningful negative cases |
| `tools/validate_repository.py` | Small standard-Python repository/installed-resource structural validator, justified by self-containment, metadata, references and count/status gates; not a gameplay engine or installer |
| `.github/workflows/validate.yml` | Actual local-check parity and bounded automated validation once implemented; heavier proof jobs remain separately identified |
| Optional `integrations/` | Add only concrete optional integration work, with no core runtime coupling; absent until justified |

Every implemented example includes source/data/assets or declared obtainable dependencies, exact used prompt, README/run instructions, test inputs/oracles, actual outputs/provenance and status. Preserve baseline/fault/repair and relevant raw evidence; large generated caches/install folders are not authored source. Include third-party notices for redistributed dependencies/assets as required by their actual source licences. Never commit private book files/paths, access credentials or substantial copied source text as ordinary research output.

Stage 18 creates the justified scaffold. Source libraries, runtime bindings and game tests are implemented at their owning proof stages; directory presence cannot imply those proofs passed.

## 2. SKILL.md contract

Each installable skill has a concise `SKILL.md` with valid frontmatter containing its exact stable `name` and a precise task-triggering `description`, then operational guidance. Describe when to use it and relevant near-misses. The metadata is for discovery, not a substitute for actual behaviour. Normal named operations and equivalent natural-language requests share the same contract; there is no custom shell command parser.

| Name | Discovery description / boundary |
|---|---|
| `game-development` | Design, build, integrate or refine playable gameplay from a brief or existing game. Use for game-specific production and targeted implementation changes. Design-only requests remain bounded |
| `game-evaluate` | Evaluate gameplay, balance, accessibility or performance evidence and diagnose the smallest responsible repair. Use for new or independently supplied existing games; no silent game changes |
| `game-extension-pack-creator` | Create or revise a researched game-development Extension Pack with explicit core overrides and comparative evaluation. Use for reusable specialisation, not one game's settings |

The body identifies input/current state, requested outcome, relevant authority/preserved work, workflow/routing, essential acceptance and evidence limits, local reference selection, failure handling and output expectations. Keep conditional detail in the skill's own references and load only what the task needs. Do not bury important authority or execution gates behind optional material or repeat whole source books/research logs.

Production includes the minimum evaluation/repair guidance needed to finish a requested game independently. Evaluation includes its own claim/method/collection/diagnosis and execution rules and accepts external project formats. Creator includes its own qualification, five-book permissions/access/reuse, profile, comparison, reuse/install and readiness rules. Optional agent UI metadata may be added when supported and validated, but must not change the skill's responsibility or become a hidden runtime requirement.

## 3. Command contract

Every operation identifies applicable input revisions, task/question, authority, preserved decisions and tools/context; produces the requested artefact/change/evidence; performs claim-appropriate verification; and reports output identity/paths, findings and limitations. Results distinguish completed requested scope, a negative finding/failure and a named required-input/capability/decision blocker. A skipped check, plan or package success cannot become gameplay proof.

### Production: seven operations

| Operation | Inputs / decision | Output and verification |
|---|---|---|
| `define-game-thesis` | Brief/constraints; connect players, verbs, intended experience, loop and evidence questions | Short identified thesis with assumptions, alternatives, authority and next disputed claim/contrary observation; no gameplay inferred |
| `design-mechanic` | Thesis/current behaviour and local rule question | Entities/state/trigger/effects/feedback/reset, normal/invalid/boundary cases, units/order/ranges and explicit unresolved semantics |
| `model-system` | Member behaviours/goals/resources and interaction question | Bounded composition/model with revisions, loops/progression, assumptions/adverse strategies; execute calculations/simulation when requested and label omissions |
| `build-playable-proof` | Question, game requirements and actual execution path | Least costly adequate runnable scope with actual input, consequence, feedback, outcome/reset and observed checks; human/target gaps remain visible |
| `integrate-content` | Composition/handoff requirements and actual delivery or greybox/encounter need | Integrated scene/game data, source/import/runtime identities and real relevant traversal/state/timing/cue checks with repair owner |
| `repair-gameplay` | Reproducible finding, accepted decisions and authorised bounds | Baseline/fault/correction, supported responsible change including approved tuning, affected reruns, preservation and keep/revert; no silent out-of-range revision |
| `prepare-playable-build` | Identified playable candidate, target and representative/delivery purpose | Built/package identity, actual build/run/quality evidence and reproduction instructions; release destination/authority explicit |

`integrate-content` uses relevant greybox, encounter, content-replacement, narrative/environment/animation/audio and import/runtime lenses. A non-spatial game need not acquire a level. `repair-gameplay` distinguishes value, rule, cue, composition and collection faults; a small diff is not enough. Representative and release builds share the operation with different evidence/authority gates.

### Evaluation: six operations

| Operation | Inputs / question | Output and verification |
|---|---|---|
| `validate-gameplay` | Declared behaviour/composition and runnable or explicitly modelled scope | Actual expected/observed rules, transitions/invariants, reachability, invalid/boundary/reset and interaction cases with setup and runtime/model limits |
| `evaluate-player-experience` | Specific controls, feedback, level-flow, comprehension or feel claim | Appropriate measured events and real participant evidence when required, observations/accounts versus interpretation, assistance/context and unmet evidence |
| `evaluate-balance` | Rules/resources, scenarios or telemetry and strategic question | Units/denominators/collection validity, flows/policies/cohorts/contrary cases and tuning hypotheses with human/causal limits |
| `evaluate-accessibility` | Critical tasks, intended inputs/presentation and relevant needs | Actual applicable task/setting findings, automated/human/device scope, smallest responsible recommendation and gaps |
| `evaluate-performance` | Target/build/workload and budget/question | Actual conditions/endpoints/overhead, raw samples/stalls/comparison and unsupported hardware/latency conclusions clearly excluded |
| `diagnose-gameplay` | Finding and accepted expectations | Supported cause or bounded alternatives, affected consumers, proposed smallest correction and preservation checks; no unrequested mutation |

Rule/transition/reachability and control/feedback/flow/feel remain distinct lenses even when entry points are merged. Combining command names does not combine proof standards. Engine-state reads, captures and test runners are mechanisms rather than extra domain commands.

### Authoring: one operation

`author-extension-pack` handles an identified new specialisation or bounded revision. Inputs are exact core/catalogue/profile revisions, requested research/implementation/evaluation scope, source material and consumer constraints. It reviews adequate prerequisites, justifies reusable difference against core/project/existing-pack alternatives, applies separate P1–P5 research and P6/P7 proof as needed, and produces the bounded pack increment with source → behaviour → test traceability and accurate research/implementation/evaluation/readiness state. A consumer parameter change is not pack authoring. Specification 05 owns the complete workflow; no competing generic authoring system or P-stage runtime commands are introduced.

The legacy bootstrap examples are preserved as lenses: define-core-loop→model-system; prototype-mechanic→build-playable-proof; greybox-level/design-encounter→integrate-content; tune-parameters→repair-gameplay; representative/release build→prepare-playable-build; validate-rules/state-transitions/reachability→validate-gameplay; controls/feedback/level-flow/game-feel→evaluate-player-experience; system-interaction diagnosis/smallest-repair recommendation→diagnose-gameplay. The selected stable interface remains fourteen operations, not twenty-three wrapper commands.

## 4. Local references and optional packs

Use a small reference set chosen for actual content. Production can place detailed decision/operation guidance in `references/production.md`; evaluation in `references/evaluation.md`; creator in `references/authoring.md`. Each consuming unit includes its own `references/browser-execution.md` when needed for the selected path, with the actual context, prerequisites, operation, expected output and limitations. Additional engine references are conditional and need their own evidence; no empty adapter folder is required.

Optional profiles are bundled independently in production/evaluation under `references/packs/`, with a local index and the two selected profile files when implemented. The index identifies scope/revision/status and file. Load only explicitly selected applicable profiles from that unit. Required runtime guidance cannot resolve through a sibling skill, another pack, creator, root docs/research, source books, a developer's absolute path or central family repository. Source citations may support provenance; consumers need not fetch them to apply the local method.

Repeating short necessary invariants across independently installed units is acceptable. Tailor routing to production versus evaluation, and verify common profile rules/revisions stay aligned. Do not bulk-copy research to avoid designing concise operational guidance. Profile identity and readiness are validated separately from local packaging.

## 5. Engine-specific references, scripts, tools and assets

Core guidance supplies engine-neutral purpose, constraints and evidence meaning. Native references preserve actual engine differences: browser page versus fixture setup; Godot nodes/scripts/import/export; Unity Editor versus PlayMode/Player; Unreal editor operations versus gameplay runtime; Roblox Studio instance and Edit/Client/Server. A tool's advertised operation does not establish local availability or correct context.

An invocation names explicit project/directory, tool/version/operation/arguments, input/configuration/target, expected output, timeout and allowed mutation. Record actual exit/result, readiness/state/feedback and evidence/errors. Required minimum observation depends on the task: project/build identity, relevant editable data, start/reset/stop, real input, authoritative state, player feedback, logs/errors and appropriate target capture. Do not create eight universal API endpoints just to mirror that checklist.

Put scenario paths, input drivers, read-only state hooks and game fixtures in their example/consumer. Put a script in a skill only after a demonstrated reusable operation justifies it beyond a direct existing command; bundle dependencies and run it after selective install. Initial core design requires no engine helper script. The repository validator is justified infrastructure for metadata/resource/structure integrity, not a gameplay runtime dependency. Ordinary required game tests remain game-owned.

An asset in a skill must have a concrete operational use, provenance and local dependency contract. Generated example content stays with its game, with source/delivery/integration identities. No private absolute paths, credentials, unsupported remote requirement or implicit runtime-owned package is permitted in install instructions. Use existing library/tool/package mechanisms for execution; do not build an installer, package registry or provider router.

## 6. Installation and dependencies

Use the standard Skills CLI with named/selective installation and the actual supported target agent. The design command shape is:

```sh
npx skills add <repository-or-pinned-skill-source> --skill <selected-name> --agent <target-agent> --copy --yes
```

Resolve and record concrete source/CLI revision, names, options and installed paths at execution; this template is not an installation success record. The selected agent may use a different directory layout—Codex's examined Skills CLI path is `.agents/skills`, not an assumed universal `.codex/skills`. Verify actual placement with the tested CLI. Normal skill installation is separate from engine/library/browser dependency installation.

For a clean proof create an external consumer with no implicit source/sibling skills; install only the selected unit in copy mode to expose symlink/source assumptions; inspect full required local closure and revision; install normal declared runtime prerequisites separately; use only installed operational guidance and explicit consumer inputs to build/play/evaluate/repair the requested task; retain actual commands/results and limitations. Also exercise ordinary advertised combined installation and missing-resource/wrong-revision failure behaviour.

Production-only, evaluation-only and creator-only are independent gates. Pack-use gates cover production/evaluation with explicit selected local profile and no creator/books/research/other-pack dependency. A consumer-supplied game or adequate source evidence is legitimate input; undisclosed root-relative context is not. Source validation and actual installed execution are separate results. Installing directories without using the skill cannot prove capability.

Keep execution dependencies local to the game/test package with explicit manifests/lockfiles or equivalent reproducible version records and run instructions. Browser binaries may have their own installation step. Do not rely on preinstalled development modules as the only documented route or claim an unavailable engine. Exact tool versions and build commands are recorded from actual proof, not invented in these design files.

## 7. CI and contributor validation

Implement the structural validator and its meaningful negative tests at scaffold. It must inspect actual SKILL metadata and local reference closure when skills exist, duplicate identities, required canonical files/counts, implemented example prompt/output/evidence state, pack profile/status consistency and referenced fixture presence. Planned records are not required to contain fabricated game outputs, but an implemented/ready claim must have its required evidence. Missing files or skipped required tests cannot be success. Validate only declared schemas; do not impose a new global artefact format.

CI runs local-check parity on relevant pull requests and branch pushes. Use ordinary GitHub Actions runners with recorded supported Python/Node and dependency versions selected/verified at implementation, read-only repository permissions and no required private services. Separate structural checks, game/fixture tests, browser/build smoke and heavier example/pack/install proof jobs. Each job executes actual commands, inspects results and retains useful logs/evidence on failure. Do not label a skipped expensive suite as passed or rebrand source checks as external installation.

Contributors run the same documented commands locally. Scope reruns to changed resources/gameplay and affected consumers, with full mandatory gates at their owning milestone/release. Changed required resources need clean selective installation; changed gameplay needs failed/affected cases; changed pack methods need the relevant comparison/reuse/preservation evidence. A public readiness/release claim requires its actual complete gates regardless of a narrow CI run.

Do not hide escaped defects by broad reruns without diagnosis. Retain the smallest reproduction, prove it detects the faulty version, repair and retain regression protection. CI and tooling are execution mechanisms; domain oracles/quality stay owned by specification 04.

## 8. Technical acceptance

The repository passes technical acceptance only when its actual committed structure has a purpose; all three intended skills have valid discovery and operational contracts; all fourteen operations are behaviourally exercised in appropriate scope; each independent install resolves required local resources and works without hidden siblings/root context; concrete execution paths identify tool/project/runtime and observe the real game; justified scripts and dependencies run through documented commands; examples and packs carry exact prompts, inspectable outputs and honest evidence; local/CI validation exposes meaningful negative cases; and clean consumer production/evaluation/repair passes separately from source checks.

No generated specification, scaffold folder, syntactically valid SKILL.md, successful installer exit or green metadata test establishes playable quality. Failure/blocked/unperformed evidence remains explicit. Preserve identities/interfaces and migration history when later verified needs change packaging; do not silently retire accepted work.
