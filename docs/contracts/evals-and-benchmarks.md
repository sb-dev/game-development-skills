# Game Development Evals and Benchmarks Contract

**Version:** 1.0  
**Defined by:** [Stage 14](../research-logs/2026-09-13-stage-14-evals-and-benchmarks.md)  
**Case designs:** [BC01–BC20](../research-logs/2026-09-13-stage-14-case-designs.md)  
**Inputs:** [Evidence/tuning](evaluation-and-tuning.md), [execution/install](execution-and-installation.md), [skills/commands](skills-and-commands.md), [packs](extension-packs-and-authoring.md), [fifteen examples](progressive-examples.md).

This contract designs evaluation. No benchmark, player session, game build or installed skill is reported as executed here. The domain benchmark judges game-production capability; an optional orchestrator may judge routing/composition separately without duplicating domain quality evaluation.

## 1. Evidence, oracle and result rules

Separate repository validity, command conformance, mechanical correctness, balance, player experience, spatial/content quality, accessibility, performance, preservation, pack usefulness and installed use. The ten layers below organise the work; no overall numeric score can conceal a material failure. A correct build can feel bad; promising play can still violate a deterministic rule.

Before running a case, identify the claim/operation, input and expected-behaviour revisions, accepted authority/constraints, smallest adequate fixture, observation route, contrary outcome, required evidence and pass boundary. Choose the relevant representation before cost optimisation. Use an existing project runner or ordinary browser/engine test facility; no common game engine, universal artefact schema or custom test platform is needed.

An oracle comes from the accepted game rule, delivered-content agreement, declared project budget, verified reference case or explicit human question. It must be independent of the result being assessed. Do not copy an implementation's current output as its own expected answer, change a tolerance after a failure, or use the same defective calculation for both observation and expectation. Label analytical models, privileged fixture setup, scheduled network impairments and deliberate faults. Actual input claims need real input into the running game; assertions need authoritative runtime state, not only a displayed label or external duplicate model.

Retain skill/pack/model/tool versions when relevant, exact effective prompt, project/build/configuration, target, seeds/policies, starting state, input/assistance, timestamps/measurement endpoints, actual commands, outputs, errors, timeouts, exclusions and limitations. For comparisons preserve each arm and deviations. Sensitive participant identity is unnecessary for most game questions; use relevant context and only the needed consented observations.

Use `PASS`, `FAIL`, `BLOCKED`, `NOT RUN` and justified `NOT APPLICABLE` for individual technical gates. `NOT APPLICABLE` requires an absent feature/claim, not missing access to a required feature. Human/quality findings remain observed support, observed barrier/contrary evidence or inconclusive within the stated scope; do not convert silence into a pass. An evaluation task can complete with a negative finding while the game/readiness claim remains failed. Mandatory blocked/not-run evidence cannot count as completed production.

## 2. Repository and deterministic validation

| Check | Smallest adequate validation / failure signal |
|---|---|
| Skill self-containment | Inspect each installed unit's required resources and runtime instructions; no required source checkout, sibling skill, creator, books or central docs |
| Required references | Resolve actual local paths/case-sensitive names after selective copy installation; remove one required resource in a disposable fixture and require a clear failure |
| Command contracts | Exercise natural requests and named operations against Stage 11 outputs/authority; design-only stays design-only, independent evaluation does not silently mutate, production works without evaluator |
| Artefact schemas where present | Validate against an actually declared project schema and negative fixture; do not invent a mandatory schema merely to satisfy this row |
| Asset / scene references | Check source/import/runtime references, dependency inclusion, units and version; actual game use still needs runtime evidence |
| Invalid state transitions | Assert accepted preconditions/effects in the game or adequate model; runtime equivalence is separately required |
| Input bindings | Verify intended actions from actual declared input and unavailable-input handling; binding names alone cannot pass |
| Build failures | Run the actual target build, inspect output/errors and fresh readiness; exit code alone does not prove play |
| Test fixtures | Ensure required cases have runnable setups/oracles and current inputs; a missing, empty or skipped required case fails completeness |
| Invalid packs | Validate local profile identity/revision/selection, required operational fields, authority and source/evidence states; metadata validity does not prove useful behaviour |
| Installation integrity | Record installed source/resource hashes/versions and CLI result; separate structural package checks from external playable use |

Use cheap static checks first where they can expose the defect. Command/skill behavioural cases judge actual actions and artefacts, not whether the answer recites instruction keywords. Include wrong tool/context, unavailable capability, stale output and scope near-misses. Source-only success is never the installation gate.

## 3. Mechanical correctness

| Concern | Required oracle / case family |
|---|---|
| Specified rules | Normal, invalid and boundary inputs with accepted state/effect assertions; BC02/04/05 and actual example cases |
| Reachable win / failure | Witness both declared outcomes in the actual game, preserving legal actions/information; record omitted branches; E01–E15 as applicable |
| Restart / checkpoint | Restore the declared state, pending/held-input policy and outcomes, repeatedly; checkpoint and full restart can retain different state; BC02/18 |
| Save / load | Valid relationship reconstruction, version/corrupt/interrupted data and declared recovery; no silent hybrid state; BC15 |
| Cooldowns / resource changes | Just-before/at/after eligibility and consumption once; non-negative or other invariants only where the game declares them; BC04/05 and pack boundaries |
| Collision / interaction | Runtime geometry, transforms, range/occupancy and action/cue agreement with actual input; BC06 and E02/03/07–09 |
| Known soft locks | Keep every discovered reproduction, expected exit/recovery and repaired result; do not infer global absence from finite passing cases; BC13–16 |
| Required content reachable | Validate dependencies after placement/import and under actual actions, costs and state; a graph or privileged teleport cannot establish playable reachability; BC06/13/15 |

Exact discrete predicates use exact equality. Floating/time tolerances must come from declared simulation step, numeric precision or measurement resolution, recorded before evaluating results. A tolerance cannot hide a different legal action, extra reward, stale session or unreachable required route. Test controlled boundary timing and real input binding separately when precise scheduling is unavailable through the player path.

## 4. Systemic and simulation evaluation

| Concern | Method and evidence limit |
|---|---|
| Strategy diversity | Define materially distinct legal policies with available knowledge, starting scenarios and opponents; report viable alternatives and omitted play, not just differently named scripts |
| Dominant strategies | Seek counter-strategies and relevant scenarios, trace the cause of advantage; finite policy coverage cannot prove universal dominance |
| Economy stability | Trace sources/sinks/conversions, bounds and feedback over a justified horizon; compare assumptions with runtime before retuning; BC04 |
| Progression curves | Record required actions/resources/attempts and state dependencies, including stalled/unfinished cases and optional routes |
| AI interaction | Inspect perception/knowledge, target selection, action execution, path blockage and fallback; BC14; a planned path is not movement proof |
| Procedural reachability | Retain seed/configuration and validate final placement with permitted actions/resources; BC13; construction success is insufficient |
| Seed reproducibility | Same declared generator/runtime/configuration produces its promised repeatable artefacts; compare actual outputs and note nondeterministic layers rather than assuming seed implies everything |
| Content utilisation | Denominator is exposed/eligible content or sessions as appropriate; distinguish never reached, never offered and failed collection |
| Pacing distributions | Define time/actions/attempts and cohort/exposure, report spread and incomplete runs; model pacing and human pacing remain different evidence |

Use all relevant failed/unfinished runs and explain exclusions. Stage 13's E10 fixed seeds 1–20, E11 three scenarios/policies and E12 adverse message schedules are predeclared bounded suites. They do not establish broad genre or hardware coverage. A strategy exploiting withheld state invalidates a player-policy inference. An aggregate improvement does not repair invalid telemetry, mixed cohorts or a violated invariant; BC08 checks this explicitly.

## 5. Player-experience evaluation

Keep all thirteen candidate dimensions inspectable and select those relevant to the actual claim. Evidence can support a bounded account or expose uncertainty, not certify universal quality.

| Dimension | Observable question / required distinction |
|---|---|
| Responsiveness | Which input-to-state/cue events occurred, with what endpoint/clock? Actual human response/feel needs people; component timing is not full input-to-display latency |
| Control clarity | Can relevant players discover and execute the intended action without the claimed level of help? Record remaps/input demands and assistance |
| Feedback quality | Does the actual cue correspond to state and help the relevant task? Event correctness and perception are separate |
| Readability | Can required object/state/direction information be recognised in the actual view/context? A clean screenshot alone is insufficient |
| Player agency | What meaningful alternatives do players perceive and attempt, and what consequences follow? Counting buttons is not agency |
| Challenge legibility | What can the player know before committing, including intentional uncertainty? Failure frequency alone does not show a legible challenge |
| Fairness | Record situated participant accounts and the relevant rule/information/role conditions; equal outcomes or identical rules do not prove perceived fairness |
| Pacing | Observe exposure, interruptions, action/wait periods and participant accounts; no universal ideal tempo |
| Mastery curve | Follow relevant repeated exposure and a declared performance/transfer criterion, retaining unfinished cases; one successful run is not mastery |
| Flow | Ask/observe within the chosen method and play context; do not infer a psychological state from a telemetry streak |
| Game feel | Connect actual control, spatial and feedback behaviour to real situated player accounts; correct physics/constants alone cannot pass |
| Satisfaction | Retain participant accounts with context/variation; completion, session length or a reviewer adjective is not satisfaction evidence |
| Comprehension | Use neutral first-use tasks or the specified exposed context, record help and distinguish action from explanation; coached success cannot be labelled unaided |

Human protocol: name the question/participant suitability, use a runnable adequate build, give a neutral task, observe without unrecorded coaching, record interventions/failures/withdrawal, then collect the relevant account. Separate observation, quotation/account and evaluator inference. Reusing experienced participants for an unfamiliar-first-use claim is invalid. Sample size follows the claim; a small situated session does not establish population prevalence or causality. L2 and selected L3/L5 example prompts explicitly require actual human evidence; record a real access blocker if absent.

## 6. Levels and encounters

| Concern | Evaluation in the relevant playable context |
|---|---|
| Navigation | Actual movement/path execution and usable information with declared actor/camera constraints |
| Critical-path readability | Mechanical required path plus human discovery/understanding where claimed; BC07 |
| Choice quality | Available alternatives, costs, consequences and participant interpretation, not branch count |
| Encounter pacing | Spawn/action/recovery sequence and relevant timed/turn/human observations |
| Spawn fairness | Visibility, arrival, legal response opportunity, overlaps and role/state conditions; no blanket safe distance |
| Cover / traversal utility | Actual attack/range/collision/movement rules, not architectural appearance; compare required/optional routes |
| Camera safety | Occlusion, clipping, required information and controllability during actual motion; comfort needs relevant people/device evidence |
| Checkpoint placement | Restored state, retry demand and intended recovery cost; exact technical restore differs from whether players find placement appropriate |
| Dead space | Identify function, navigation/information and pacing context before labelling inactivity waste; proposed deletion must preserve intent |
| Content reachability | Final placement/state/cost prerequisites and permitted actor path, not only adjacency/connectivity |

BC06/07/11/13/18 and E07–15 provide bounded contexts. Keep source delivery, import/placement, gameplay rule and evidence failures distinct. Use unassisted play only when that is the actual claim; editor flight or known-route scripts do not establish discovery.

## 7. Accessibility

Start from critical tasks and relevant needs: start/configure, perceive state, choose/action, sustain/sequence input, receive outcome, pause/recover and restart. Inspect the applicable keyboard/pointer/other declared inputs, remapping/alternatives, simultaneous/held/rapid demands, timing, UI navigation/focus, text/readability, non-colour distinctions, non-audio cues, caption/volume controls where relevant, camera/motion demands and settings persistence. Test the whole task and state transitions, not a menu alone.

Automated DOM/reference checks can find some barriers, but do not certify a rendered playfield or the whole game. Use actual task execution and relevant participants/devices for claims requiring them. A canvas state label cannot replace usable game interaction. A turn-based game still needs focus/information checks; deliberate difficulty cannot excuse stale input or missing critical meaning. Record which overlapping needs/settings were exercised and what remains untested. BC09/19 and each example's input/cue requirements supply cases; PP-A05/07/08 and TT-A04/07/10 specialise them without removing core obligations.

## 8. Performance and representative budgets

| Dimension | Measurement boundary and required context |
|---|---|
| Frame time | Distinguish frame-work duration, scheduling interval and presented frames; record samples, stalls, workload and capture overhead |
| CPU / GPU cost | Use suitable actual runtime tools, identify thread/phase/device and workload; a JavaScript duration cannot certify GPU cost |
| Memory | Name heap/process/GPU measure and growth/peak interval; unavailable memory tooling is unknown, not zero |
| Allocation spikes | Correlate recorded allocation/collection and observed stalls using adequate tooling; do not assign cause solely from temporal coincidence |
| Load time | Define start/end and cold/warm/cache conditions, asset readiness and errors; process launch is not a ready game |
| Streaming stalls | Exercise actual boundary/content transitions and retain relevant long intervals and state/cue effects |
| Input latency | Name hardware/input/engine/display endpoints and clock/resolution; component traces or headless events cannot stand in for full perceptual delay |
| Network latency / replication cost | Identify round trip versus one way, schedule/workload, authority, bytes/messages/backlog and convergence; synthetic delay is not public-network measurement |

Use suitable built candidates and representative workload, not engine-editor profiling alone. Stage 13's budgets remain project targets: E07/08/10/13/14 frame-interval p95 ≤33.3 ms, E09/15 ≤50 ms at 1280×720 over 60 seconds after loading; record intervals >100 ms separately. E10 generates each retained small seed below 500 ms. E11 update-step p95 ≤50 ms at 256 cargo objects, also measuring 64-object and render/interaction conditions. E12 requires declared shared outcome convergence within 2 seconds after delivery settles under its controlled schedules and retains a 60-second workload record.

These thresholds are deliberately modest acceptance targets for bounded examples, **not sourced perceptual laws, measured baselines or platform-wide support**. The frame targets correspond to approximately 30/20 scheduling opportunities per second; they cannot certify displayed frame rate or input feel. At implementation pin environment, workload, clocks, sample collection and capture overhead before evaluating. Use the exact promised budget; do not relax it after observing failure. A materially different target/requirement needs an explicit design revision with history, not silent waiver.

For percentile reports, sort finite observed samples and use nearest-rank `ceil(p × n)` for p95, stating n, duration, excluded loading/warm-up interval and relevant maximum/stalls. Preserve raw samples; no convenient outlier deletion. Exact controls/setup should match comparisons. Repeat only when variance, changed workload or a remaining risk makes one capture inadequate; report uncertainty. None of these measurements implies physical-device, release or experience evidence beyond its endpoint. BC17 tests tail/endpoint misinterpretation.

## 9. Preservation and repair

| Required preservation | Acceptance behaviour |
|---|---|
| Approved mechanics survive unrelated content refinement | Compare actual rule values/semantics and affected routes; source/import repair cannot silently retune movement; BC06 |
| Accepted control feel survives level changes | Preserve accepted controller and relevant measured/human evidence conditions; technical equivalence alone does not establish a new feel claim; BC11 |
| Local balance fixes preserve unrelated systems | Trace cost/flow cause, change within authority, rerun affected strategies/invariants and stable neighbours; BC04/08 |
| Level repair preserves unaffected rooms/encounters | Retain identities/content and actual regression paths; whole-level regeneration needs a demonstrated causal reason/authority; BC06/13 |
| Pack activation respects locked decisions | Apply stronger instructions, preserve intentional no-buffer/strict commitment/hidden information and still reject true faults; PP-A08, TT-A10 |

Retain baseline, defective state, reproduction, expected result, diagnosis/alternatives, responsible change, authority and repaired/affected reruns. Judge whether the cause is supported, scope is sufficient and stable decisions survive; a small line count alone is not success. A diagnosed but unfixed defect stays open. Independent game-evaluate recommends the change unless production mutation is authorised.

The regression loop is **escaped defect → diagnosis of responsible unit → smallest reproducible fixture → eval/benchmark case → fix → retained regression protection**. Run the new fixture against the faulty and repaired states so an always-green checker cannot pass unnoticed. Rerun affected neighbours and installation if resource boundaries changed. Do not rerun unrelated full games for every local defect, but do not use a cheap unit test to claim absent integration/human/target proof.

## 10. Extension Pack behaviour and comparison

The completed P5 profiles define acceptance **before implementation**: [PP-A01–12](../research-logs/2026-09-13-stage-12-precision-platformer-p5.md) and [TT-A01–13](../research-logs/2026-09-13-stage-12-tactical-turn-based-p5.md). Keep all twenty-five cases and their conditions; implementation may add reproductions without deleting inconvenient tests.

| Required behaviour | Primary cases / oracle |
|---|---|
| Activate when requested | PP-A01 / TT-A01: relevant operational decisions and effects from the requested profile |
| Stay inactive when absent | Same cases: competent core task with no implicit profile activation |
| Meaningful specialised behaviour | PP-A02–07/09–10 and TT-A02–09/11–12: actual movement/space or action/phase reasoning and outputs |
| Explicit project precedence | PP-A08 / TT-A10: stronger concrete project decisions preserved |
| Approved-decision precedence | Same cases plus repair: locked values/intent survive pack defaults |
| Pack-aware criteria without hiding defects | Distinguish intentional difficulty/commitment/uncertainty from stale input, illegal action, bad cues or reset faults |
| Negative / incompatibility | PP-A12 / TT-A13: unsupported/conflicting scope handled without invented support |
| Targeted refinement | PP-A04/08–09 and TT-A09–11: correct-layer change and affected regression, no unrelated regeneration |
| Domain boundary discipline | PP-A01/12, TT-A01/13 and creator review: no art/network/engine takeover or unneeded pack |

Every implemented pack must execute four distinct obligations: **its exact-prompt primary showcase; a distinct additional reuse brief/fixture; behavioural and precedence cases; and fair core-only versus core-plus-pack production**. Precision uses Copper Steps plus Low Ceiling Traverse; Tactical uses Relay Hold plus Two Couriers. The fifteen primary examples do not replace these gates. Source/behaviour/test provenance and limitations travel with the evaluation, not as installed research dependencies.

For the primary comparison use the exact same substantive P5 prompt and inputs in matched fresh contexts with competent core guidance, equal task requirements, comparable tools/allowed resources and recorded revisions/settings. The intentional difference is profile activation and its packaged guidance. Retain effective contexts and context contamination/deviation; if fresh isolation cannot be achieved, the limitation prevents a strong comparative claim. Do not credit a name mention, extra text or a richer packed brief.

Use at least one fully executed matched pair plus the distinct reuse and behavioural evidence. A single favourable pair alone is insufficient for readiness or general superiority. Repeat when stochastic variation, ambiguous effect or a claimed consistency benefit requires it; predeclare the repeat policy and retain every run. A core-plus-ordinary-instructions arm can determine whether useful packaging remains beyond a one-off brief. If value is indistinguishable, record inconclusive/unproven status, refine a real recurring weakness and rerun affected cases; never weaken core to manufacture a difference.

Judge concrete decisions, playable correctness, qualified specialist effect, defect detection, causal repair, preserved work, effort/context cost when measured and human/target limits separately. Pack readiness requires useful intended effect with acceptable regressions, actual reuse/behaviour and clean installed use. Research complete, directory implemented and prompt present remain different states; readiness does not promote repository maturity.

## 11. Clean consumer installation

Use the normal Skills CLI and the Stage 9 contract; record actual CLI/source revision, options and installed paths. Pin tested dependencies rather than assuming development packages exist. The eventual concrete commands must be verified against the installed CLI, not copied as already-successful output.

| Install scenario | Required actual use / failure detection |
|---|---|
| Production only | Clean external project installs only game-development, builds/plays/evaluates/repairs a bounded result using its local instructions; no evaluator, creator, pack or source checkout dependency |
| Evaluation only | Only game-evaluate inspects an explicitly supplied independent game with native records, executes relevant checks and diagnoses without unrequested source changes |
| Creator only | Only game-extension-pack-creator uses explicitly supplied adequate prerequisite evidence to author/review a bounded increment and reject unsupported overrides/readiness; no hidden sibling references |
| Production + selected pack | Bundled profile resolves locally, selection is explicit, specialist task and precedence/non-use work without creator/books/research/another pack |
| Evaluation + selected pack | Local pack criteria apply to a supplied game and distinguish intent from genuine faults without production-skill dependency |
| Combined advertised installation / negative fixture | Normal combined install works without shadowing incompatible revisions; missing required local resource or wrong revision produces an explicit failure instead of reading the source repository |

A consumer directory alone is not isolation. Use selective copy installation, inspect resolved paths and required closure, and run from outside the source repository without implicit source-root search or environment-only dependencies. Explicit user-supplied game/evidence is legitimate input; an undeclared sibling/root path is not. Preserve the exact installed resources and commands in the proof. Structural file checks and actual consumer production/evaluation are separate gates; source-repository validation cannot replace either.

## 12. Suite ownership and efficient execution

Implement cheap repository/contract checks with ordinary scripts only where needed, keeping fixtures/evidence inside the owning repository or example. Use the game/runtime's native tests for behaviour and existing browser/engine facilities for input, state, capture and profiling. Scenario-specific hooks belong to their game; no shared global state graph or universal scene format is required.

Run static/discovery checks after relevant packaging changes; smallest rule/fixture plus affected integration on gameplay changes; the applicable example/pack cases when guidance or content assumptions change; and clean selective installation whenever a required resource/interface changes or an installed-use claim is made. Full curriculum and release gates remain mandatory at their owning stages. Do not skip a required gate for speed, invent a result, or repeat unrelated expensive suites without a concrete risk.

Stage 18 may scaffold these locations and implement appropriate structural checks. Stage 19 proves one core vertical; Stage 20 executes the fifteen examples and pack evidence; Stage 21 validates clean installation scope. Results always identify what actually ran. Evals feed refinements back to their responsible skill/command/profile instead of adding architecture merely because a test is inconvenient.
