# 04 — Testing and Benchmark Specification

**Status:** Canonical evaluation design; runtime/installed benchmark evidence pending  
**Version / date:** 1.0 / 2026-09-13  
**Inputs:** [workflows](02-game-development-skills-workflows-and-artifacts-spec.md), [repository contracts](03-game-development-skills-repository-and-contracts-spec.md), [pack contract](05-game-development-customisation-packs-spec.md) and [catalogue](06-game-development-extension-pack-catalogue.md).  
**Provenance:** Accepted Stage 14 evaluation and case designs, with the complete Stage 13 curriculum.

This specification owns evaluation methods, benchmark cases, progressive coverage, regression and release-evidence gates. It consolidates the full accepted design below. No playable result, participant session, runtime benchmark, installed use or quality pass is established by writing this specification. The domain benchmark owns game-production quality; optional orchestrators may separately evaluate routing without duplicating it.

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

The completed P5 profiles define acceptance **before implementation**: [PP-A01–12](06-game-development-extension-pack-catalogue.md#2-precision-platformer) and [TT-A01–13](06-game-development-extension-pack-catalogue.md#3-tactical-turn-based). Keep all twenty-five cases and their conditions; implementation may add reproductions without deleting inconvenient tests.

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

## 13. Core benchmark case contracts

BC01–BC16 preserve their source-derived question identities; BC17–BC20 add performance, checkpoint, navigation/focus and execution-context cases. These twenty families are predefined and not executed. Their setups, expected evidence and smallest repair boundaries are normative; concrete game fixtures/commands must implement them at the owning proof stage.


### BC01 — Intent and incentive tension

**Setup/task:** Supply an accepted tense-risk thesis and a bounded score/resource model in which passive waiting earns ongoing reward without the declared cost/pressure. Ask define-game-thesis/model-system to assess the discrepancy; E04/E06 are later playable contexts.

**Oracle/evidence:** Identify the precise rule/intent relationship and demonstrate the permitted passive trajectory under stated horizon/assumptions. Do not claim that any waiting is inherently bad, that a title establishes tension, or that scripted outcomes establish player feeling. A narrow qualitative intent review can complete with an unresolved human question; an actual rule claim needs its model/runtime evidence.

**Repair/preserve:** Recommend a causal change only if the accepted intent/rule contract calls for it, within existing authority. Preserve unrelated movement/resources and relevant alternatives. Inventing player frustration or adding arbitrary punishment to force an aesthetic preference fails.

### BC02 — Reset leaves a gate unlocked

**Setup/task:** Use E01's valid crate/plate/gate room, then a retained variant with old gate-open state surviving restart. Request validate-gameplay/repair-gameplay from normal play and two successive restarts.

**Oracle/evidence:** The gate's actual collision/passability and visible state agree with the restored plate rule and initial positions. Retain actual input, authoritative state, outcome and reset observations; changing only the displayed label fails. Exercise normal and blocked push, plate entry/exit and required gate crossing alongside the failed reset.

**Repair/preserve:** Correct the reset/derived-state boundary and preserve board, push eligibility, controls and valid gate behaviour. Removing the gate or auto-completing the puzzle is a failure even if the old test no longer finds it.

### BC03 — Inadequate representation for control timing

**Setup/task:** Supply paper rules and an attractive static frame as proposed proof of responsive continuous control. Ask build-playable-proof to establish the needed question, using E02 as the small execution context.

**Oracle/evidence:** Reject the unsupported timing inference, identify input/state/feedback variables and produce the smallest runnable interaction when execution is requested. Record actual input endpoints and runtime observation; a written experiment plan or direct call to the movement function cannot close player-input proof. Human feel remains a separate question.

**Repair/preserve:** Increase only the fidelity needed to expose the issue, preserving approved rules. Rebuilding a polished complete game, inventing latency measurements or calling the paper model adequate fails the capability case.

### BC04 — Coupled upgrade creates resources

**Setup/task:** E06 or a small same-runtime economy fixture has a declared non-negative cost invariant but repeated discounts cross below zero. Supply initial resources and two legal policies before testing.

**Oracle/evidence:** Trace the exact source/sink/cost sequence, reveal the resource-creating purchase, and distinguish local cost validity from overall human balance. Retain boundary costs, actual accepted/rejected transactions and policy outcomes. A copied implementation formula cannot be the independent expected calculation.

**Repair/preserve:** Repair the responsible cost rule within the accepted contract; preserve upgrade effect, demand, order and unrelated stock. Rerun both policies and affected invariants. Lowering the goal or broadly nerfing rewards to conceal the exploit fails.

### BC05 — State-boundary input lost or repeated

**Setup/task:** Supply a timed action with declared legal states, expiry and single-consumption semantics; normal-average response looks acceptable but near-transition input is lost or reused. Use E02 or the explicit PP-A03 60 ms/100 ms-before-landing cases under Copper Steps's 80 ms buffer.

**Oracle/evidence:** Evaluate before/at/after eligibility, expired and consumed input, held versus fresh action and reset. Preserve controlled-time setup separately from real input-binding evidence. Report exact events and permitted tolerance from simulation/measurement resolution, not an invented perceptual standard.

**Repair/preserve:** Correct ordering/eligibility/consumption or binding at the supported cause. Do not add a universal buffer, alter accepted movement or accept a good mean while the boundary remains wrong. Intentional no-buffer projects use their own oracle.

### BC06 — Content handoff defects have different owners

**Setup/task:** Use four bounded variants tied to actual delivered/integrated assets: environment source dimensions correct but import scale wrong; valid animation marker converted with the wrong time basis; valid narrative once-only intent bound twice; valid audio cue routed to the wrong event/mix state. E07/E09/E14/E15 provide appropriate later contexts.

**Oracle/evidence:** For each variant compare source revision/properties, agreement, import/binding and actual runtime use. Check traversal/collision, action event timing, narrative state/continuity or audible cue meaning respectively. A static name lookup or the earlier synthetic Stage 6 predicate is insufficient for runtime/modality acceptance.

**Repair/preserve:** Fix integration when delivered content is valid; a contrary variant whose actual source violates the agreement must return to its producer. Preserve accepted art/story/motion, controller, unrelated rooms and cue roles. Rewriting valid specialist content or changing gameplay to hide a bad binding fails.

### BC07 — Mechanically reachable danger is unreadable

**Setup/task:** A new player's required approach exposes a hazard or target only after commitment; a known-route bot succeeds. Supply the accepted information policy and player-view geometry, using E05/E07/E09.

**Oracle/evidence:** Distinguish legal reachability, visible cue availability and actual first-use comprehension. Inspect runtime view/approach; use a relevant unfamiliar participant for a claimed comprehension result, with neutral task and recorded help. Deliberately hidden information is evaluated against its contract rather than automatically revealed.

**Repair/preserve:** Target cue/framing/occlusion or the actual faulty relationship, preserve movement and intended uncertainty, then rerun mechanical/visibility and relevant human checks. Claiming bot completion proves discovery or changing physics before diagnosing information fails.

### BC08 — Invalid collection and mixed assistance

**Setup/task:** Provide a clearly labelled synthetic evidence fixture with duplicate events across two restart sessions and results combining coached and uncoached attempts. Ask evaluate-balance/evaluate-player-experience to interpret it before tuning; E04/E11 later supply actual collection contexts.

**Oracle/evidence:** Recover or flag session/attempt/event identity, defined eligible denominators, exposure and assistance. Keep invalid rows and uncertainty. Report distinct cohort/context results and reject an unsupported unaided or causal-success conclusion. More arithmetic on invalid collection is not a pass; synthetic records are not real participants.

**Repair/preserve:** Fix logging/reconstruction or test setup first and recollect the necessary actual evidence. Preserve accepted game values until a valid design finding supports change. A single favourable aggregate cannot close the case.

### BC09 — Hue and short sound carry the only critical state

**Setup/task:** A required action/outcome is distinguishable only by hue plus a brief sound, with no persistent readable alternative. Evaluate the full task under declared colour-independent and sound-off conditions.

**Oracle/evidence:** Identify the actual task information missing, not merely a generic warning. Inspect/use equivalent text/shape/status alternatives and state transitions in the running game; human/device claims require the appropriate actual conditions. An unrelated menu label or automated DOM score cannot certify a canvas task.

**Repair/preserve:** Correct the responsible cue/interaction without changing accepted rules or treating accessibility as an optional pack. Rerun normal and alternative task paths with recorded focus/input conditions. Do not claim universal accessibility from this one case.

### BC10 — A polished corner is used to justify wider commitment

**Setup/task:** Supply one attractive integrated room with unperformed later-level/build/save work, then request evaluation of a larger production commitment. Use E07–09's declared slice scope.

**Oracle/evidence:** Identify which gameplay and production responsibilities were actually demonstrated, important omitted combinations, integration/review costs and unresolved evidence. Present a concrete bounded next proof/decision under existing authority. Do not claim the finished corner proves the entire content pipeline or invent delivery estimates as measurements.

**Repair/preserve:** Retain accepted assets and working interaction. Add the necessary representative integration proof instead of regenerating the corner or approving broad scope from visual appeal. Do not ask again for authority already present.

### BC11 — Late controller change breaks accepted routes

**Setup/task:** E13 retains an accepted controller/route baseline; a disclosed lower-jump variant makes one required route fail. Request diagnosis and correction preserving accepted movement and unaffected levels.

**Oracle/evidence:** Reproduce with actual input and inspect changed controller, route geometry and contact evidence. Identify affected required/optional routes and retain baseline/fault observations. An animation or successful privileged teleport is not a route witness.

**Repair/preserve:** Restore the accepted dependency or make the specifically authorised coordinated correction; never silently change the oracle or rebuild all levels. Rerun failed and unaffected paths, outcomes and reset. Equivalent constants support technical preservation, not an invented new human-feel result.

### BC12 — Source/editor works, packaged candidate fails

**Setup/task:** A local build omits a required asset or uses an absolute source path; a fresh consumer/package run fails. Use E13/E15 or the installed core vertical, preserving the source-working baseline.

**Oracle/evidence:** Identify actual built candidate, source/config/dependency versions, fresh run context and failed asset/behaviour. Run build plus complete candidate input/outcome/reset with errors and captures. A successful compile, development server or files-present check cannot pass packaged play or skill installation.

**Repair/preserve:** Correct packaging/reference/dependency at its owning layer, preserve game rules/assets and rerun fresh candidate and affected installed resource checks. Copying the entire source repository into the consumer or omitting the failing feature fails isolation.

### BC13 — Generated floor is connected but progression is impossible

**Setup/task:** E10's fixed seeds/configuration include a post-placement key-behind-gate or resource-insufficient required path. Retain final placement and a known-valid baseline seed set.

**Oracle/evidence:** Evaluate actual actions, dependencies, costs and information after all placement. A graph-only path or seed value cannot certify play. Retain failing seed, expected condition, witness/counterexample and actual same-runtime versus model scope; check repeatability only where promised.

**Repair/preserve:** Correct construction/placement dependency and rerun the retained failure and all affected fixed seeds/accepted runs. Do not discard bad seeds, unlock the gate unconditionally or retune unrelated movement/combat. Human generated-content quality stays separate.

### BC14 — Removed target stalls an active agent

**Setup/task:** An actor in a still-active encounter approaches a selected target; that target becomes invalid/removed and repeated reselection stalls useful action. Use a bounded native AI/navigation fixture informed by E05, with explicit permitted knowledge and fallback policy.

**Oracle/evidence:** Preserve perception/selection/movement observations before and after invalidation. The actor follows its declared fallback without attacking absent state or obtaining forbidden information. A valid returned path alone cannot pass if movement/action remains stalled.

**Repair/preserve:** Correct invalidation, commitment or fallback at the actual cause and rerun normal selection, blocked movement, removal and other accepted actions. Disabling the actor or granting omniscience fails. If the game's outcome legitimately ends the encounter, do not demand continued action after termination.

### BC15 — Saved dependencies and interrupted writes

**Setup/task:** E11/E14/E15 save an acquired key/facility without reconstructing a dependent object; a second variant interrupts persistence. Supply valid, invalid, incompatible and interrupted states with an accepted recovery policy.

**Oracle/evidence:** Actual load/reload yields a complete valid checkpoint or the explicitly reported permitted clean start, never a silent mixed state. Distinguish serialization, write/recovery, schema and runtime reconstruction. Preserve bad data and logs; no cloud or crash-safety guarantee follows from a local simulation.

**Repair/preserve:** Repair the responsible boundary, preserve valid previous saves under the compatibility contract and accepted progression/rules. Rerun valid/invalid/interrupted states, affected required paths and restart. Silently discarding all progress or weakening the dependency is not a pass unless that exact recovery was already authorised.

### BC16 — Duplicate multiplayer reward across reconnect

**Setup/task:** E12 uses two actual clients and a local authoritative server. Duplicate a request, delay/drop an application message and reconnect during resolution under the predefined schedules.

**Oracle/evidence:** The same accepted outcome earns one reward; a genuinely new outcome remains valid. After delivery settles, declared shared state converges within two seconds, with transient differences assessed against the architecture. Preserve both client inputs/observations and server traces. One-runtime cursors or simulated state tables cannot establish multi-peer execution.

**Repair/preserve:** Correct authoritative request/outcome/session handling, retain valid recovery and player-role rules, rerun adverse and normal two-room paths. Label scheduled delivery separately from real network measurements and retain human coordination questions/evidence where required.

### BC17 — Good mean hides budget failure and wrong endpoints

**Setup/task:** Supply a labelled synthetic 20-sample frame-interval fixture: seventeen 10 ms samples and three 120 ms samples, with a 33.3 ms p95 budget. A proposed report uses the mean and claims input-to-display/GPU performance. Follow with an actual target/workload capture at the owning stage.

**Oracle/evidence:** The analytical mean is 26.5 ms but nearest-rank p95 is 120 ms, with three intervals above 100 ms. The report must reject the p95 pass and unsupported endpoint claims, retain raw samples and exclusions and state actual capture limits. This designed arithmetic is not an executed profiling result.

**Repair/preserve:** Diagnose with adequate runtime instrumentation before changing the game; repair the relevant work/allocation/streaming or collection issue without lowering workload or budget silently. Rerun the affected representative capture with stable conditions and preserve correctness. Treat missing tooling as unknown, not zero cost.

### BC18 — Checkpoint differs from full restart

**Setup/task:** A bounded E07/E13-style room fixture declares checkpoint-retained progress but restores player position/contact/temporary hazards on retry; full restart clears progress too. Faulty retry retains queued input or mixes the two restore policies.

**Oracle/evidence:** Assert the exact retained/restored fields, legal next action, once-only outcome and fresh/held input semantics at repeated deaths, checkpoint reload and full restart. Observe actual input and state. Do not make checkpoint semantics mandatory in games that do not promise them; this dedicated fixture does.

**Repair/preserve:** Correct the relevant restore/session boundary, preserve accepted recovery cost, checkpoint placement, controller and unaffected room progress. Adding checkpoints everywhere or clearing all persistent progress to hide the defect fails.

### BC19 — Focus disappears after an actor/action is removed

**Setup/task:** A tactical or dense-management interface removes the selected action/actor and opens outcome/restart UI. Pointer automation still succeeds, but the keyboard path has no usable focus or return route; use E08/E11 and TT-A07.

**Oracle/evidence:** Exercise keyboard selection, proposal/cancel/commit, removal, phase/outcome and restart with visible focus and declared information alternatives. Report actual control/state transitions and which needs were tested. A logical DOM tab order alone cannot prove the whole task remains possible.

**Repair/preserve:** Restore meaningful focus/navigation/state announcement at the responsible UI transition, preserving accepted tactics and valid pointer/keyboard actions. Replacing the whole interface or adding an unrelated shortcut without fixing the required path fails. Human usability/device scope remains explicit.

### BC20 — Wrong context or stale evidence appears successful

**Setup/task:** Give an execution result from the wrong project/session, an old capture after a failed launch, or an unavailable required operation. Ask the skill to verify the current candidate. Tool-response fixtures are explicitly synthetic until an actual runtime case is executed.

**Oracle/evidence:** Check project/build/session and observation identity, readiness, errors and requested output. Reject a stale success or correct file from another context, preserve diagnostics and state the exact missing/current operation. Do not mutate the unrelated project or claim unavailable execution happened.

**Repair/preserve:** Select/restart only the intended owned context and rerun the failed operation plus affected case under existing authority. No general scanning/cleanup of other projects or new provider framework. A valid eventual run does not erase the failed/stale record.


## 14. Skill routing and fixture publication


These eight probes extend Stage 11's documented synthetic walkthroughs into future actual skill-use cases. They remain **not run** as installed-agent benchmarks. A probe passes by observed task scope/output/action, not by repeating a command name. The contract and curriculum map all fourteen operations to production contexts; these probes target discovery, authority and near-misses.

| Probe | Input / expected behaviour | Failure |
|---|---|---|
| SR01 | Short thesis request → game-development produces the bounded design with explicit uncertainties | Unrequested engine/game build or invented achieved player response |
| SR02 | Build and repair a bounded reset fault with production skill only → actual playable result and essential checks | Hidden evaluator/creator/pack or source-checkout dependency |
| SR03 | Independently supplied game review with evaluator only → actual relevant evidence and recommendation | Required proprietary folder layout or unrequested game-source mutation |
| SR04 | Correct doorway delivery imported at half scale → compare source/import/runtime and fix/recommend the right owner | Retune the controller or blame valid source without evidence |
| SR05 | Screenshot offered as proof controls feel good → bound visual evidence and require actual control/human evidence for the claim | Invent measurements or participants |
| SR06 | Tuning request beyond a locked range → recognise any explicit new authority; otherwise prepare the concrete change/impact and seek only missing decision | Silent material change or needless repeat permission where already authorised |
| SR07 | Reusable specialisation request → existing creator checks core/pack/project alternatives, adequate research and proof state | Label-only pack, automatic book replacement or fabricated readiness |
| SR08 | General code-architecture review without a gameplay criterion → use existing engineering responsibility | Unnecessary game-specific pipeline or domain takeover |



Keep each actual fixture small and game-native, with source/config revision, expected result, exact setup/input and runnable command. Preserve baseline/fault/repair identities and relevant raw evidence. Prefer a local rule or interface reproduction over a whole campaign when it faithfully retains the failure; actual integration/human/target gates still require their appropriate scope. Record deliberate injection and evaluator familiarity, and use fresh contexts for independent diagnosis claims when available.

The owning proof stages must turn these designs into real cases and inspect their outputs. Required fixtures cannot be empty files, unconditional success scripts or checks that merely match instruction text. Retain unsuccessful and blocked outcomes. When an escaped defect adds a new case, preserve its original conditions and rerun the responsible regression and affected neighbours after repair. No universal case runner, world schema or giant cross-game state model is required.

## 15. Progressive examples and public capability coverage

### 15.1. Curriculum and proof boundary

The primary curriculum is exactly **five levels × three examples = fifteen examples**, selected from thirty candidates. Level describes the production responsibility under test, not code size, artistic finish or a mandatory order for every consumer task. Each trio complements the other two. Pack showcases and independent reuse fixtures remain additional evidence; they do not replace or inflate this count.

| Level / meaning | Primary examples | Combined proof |
|---|---|---|
| 1 — one mechanic | E01 Latch Room; E02 Rebound Lab; E03 Depth Dock | Rule/state and reset; continuous input/contact and basic tuning; actual 3D manipulation and depth information. Each includes feedback, small automated checks and local repair |
| 2 — repeatable loop | E04 Spark Run; E05 Quiet Parcel; E06 Reservoir Shift | Motor/score risk, stealth information/AI and discrete resource incentives. Each includes goal, challenge, reward/failure, retry, pacing/basic balance and actual human playtest |
| 3 — coherent vertical slice | E07 Beacon Walk; E08 Switchyard Tactics; E09 Orbit Courier | Traversal/content, tactical encounter/progression and 3D camera/physics. Each integrates representative content, UI/audio/visual handoffs, workload budget and broader evaluation |
| 4 — scale, systems and repair | E10 Seeded Vault; E11 Canal Works; E12 Twin Signal | Generated progression/placement, interacting simulation/persistence and actual multi-peer authority/recovery, with multiple content units, load evidence and stable-system preservation |
| 5 — full thesis | E13 Signal Orchard; E14 Harbor Accord; E15 Lantern Atlas | Small complete precision game, tactical narrative campaign and coherent 3D world. Together exercise both packs and core-only production, broad cross-domain integration and actual release-candidate validation |

### 15.2. Complete prompt and output locations

The linked files contain three **standalone, copyable prompts** each. Copy the entire relevant fenced prompt into an installed-skill consumer. No prompt requires another example's artefacts or earlier prompt text. Each requests original content and records any selected ordinary runtime dependencies. These are generation tasks with explicit proof and failure handling, not claims of existing game outputs.

| Examples | Complete prompts | Future output / evidence location |
|---|---|---|
| E01–E03 | [Level 1](research-logs/stage-13-prompts/level-1.md) | `examples/level-1/<example-id>/` |
| E04–E06 | [Level 2](research-logs/stage-13-prompts/level-2.md) | `examples/level-2/<example-id>/` |
| E07–E09 | [Level 3](research-logs/stage-13-prompts/level-3.md) | `examples/level-3/<example-id>/` |
| E10–E12 | [Level 4](research-logs/stage-13-prompts/level-4.md) | `examples/level-4/<example-id>/` |
| E13–E15 | [Level 5](research-logs/stage-13-prompts/level-5.md) | `examples/level-5/<example-id>/` |

At the implementation stage each primary example gets its own README containing the **exact generation prompt actually used**, premise, prerequisites/run commands, selected skills/packs and revisions, expected behaviour, generated artefacts, actual execution provenance, evaluation and limitations. Keep the planned prompt and any authorised deviation visible. Preserve actual playable output, source/data/assets, required local test drivers, baseline/fault/repair evidence and status. A link to a prompt without output is not a demonstrated example.

### 15.3. Required gates at each level

| Level | Gate for each primary example | Additional combined coverage |
|---|---|---|
| 1 | Bounded playable interaction with actual input/state/feedback, stated rule values, one basic tuning comparison, small automated normal/invalid/reset checks and smallest responsible repair | Temporal/physics and discrete semantics plus a genuine 3D depth case; the first core vertical may select one of these |
| 2 | Complete goal/challenge/outcome/retry loop, pacing and basic balance analysis, automated technical checks and an actual question-led human session | Distinct score, information and resource pressures; human actions/accounts separate from scripts and expert inference |
| 3 | Representative composed slice, level/encounter progression, actual delivered/integrated UI/audio/visual content, target/workload budget and broader rule/experience/access/performance review | 2D/3D, physical/tactical control and source/import/runtime fault ownership |
| 4 | Multiple content units, interacting systems/strategies, procedural or systemic content, complex balance questions, representative load and regression-protected repair | Procedural post-placement validity, simulation trajectories/persistence and real two-peer session recovery |
| 5 | Coherent thesis, mechanics/systems/space, integrated content, actual playtesting, balance/performance/access review and identified local release-candidate validation | Both selected packs, a core-only world, all four required content handoff disciplines and a bounded creator revision/evidence review |

Human requirements cannot be satisfied by fabricated participants, LLM roles, bot telemetry or author intuition. Use relevant actual participants with neutral tasks and recorded familiarity/assistance. A small session supports only its situated observations. If required participants or another necessary execution capability are unavailable, the affected example/proof remains blocked with the precise need; do not silently remove that gate. These gates were designed at Stage 13 and require actual execution at Stage 20.

### 15.4. Whole-set coverage matrix

This is a coverage map, not a measured support catalogue. Each cell names the relevant planned proof. Hardware and broad platform claims require actual representative evidence.

| Bootstrap dimension | Deliberate examples and limits |
|---|---|
| 2D vs 3D | 2D E01/02/04–08/10–14; actual 3D scene/camera E03/E09/E15. A flat projection pretending to be 3D cannot pass those examples |
| Real-time vs turn-based | Continuous E02/04/05/07/09/13/15; discrete E01/03/06/08/11/14; E10 mixes exploration with discrete resource decisions; E12 multi-peer real-time input with discrete authoritative outcomes |
| Precision vs systemic | Precision/contact E02/07/13; resource/strategy/phase interaction E06/08/10–12/14; information/space E01/03/05/09/15 |
| Authored vs procedural content | Authored rooms/encounters across L1–3 and L5; E10 seeded generation after placement; E11 systemic flow/demand. No procedural-quality guarantee from a seed or assembly check |
| Physics dependence | E02 collision/deflection, E07/13 movement/contact, E09 steering/inertia; E01/06/08/11/14 intentionally rule-based |
| AI dependence | E05 perception/patrol/recovery, E08 opponents, E10 encounters, E11 agents and E14 encounter decisions. E01–03 do not require AI |
| Single-player vs multiplayer | Most are single-player; E12 actually uses two browser clients and one authoritative local server. Production service operation, matchmaking and internet-scale fairness are outside this bounded proof |
| Short-session vs progression-heavy | L1/2 bounded attempts/loops; E08/10/11/13–15 multi-content progression with declared retained state |
| Level-based vs world-based | E07/08/10/13/14 explicit sequences; E11 connected systemic scenarios; E15 three connected zones with persistent world-state relationships |
| Platform / input differences | All can use ordinary browser delivery; keyboard E01/04/05/07/12/13, pointer plus keyboard alternatives E01/03/06/08/11/14/15, multi-client E12 and 3D camera E09/15. Browser touch events may be inspected where relevant but do not establish real mobile, gamepad, console or XR support; those remain explicit gaps |
| Core skills | game-development and independent game-evaluate across the set; game-extension-pack-creator bounded profile/evidence revision in E14. No sibling family is an undeclared runtime prerequisite |
| Commands | Complete operation mapping in section 15.5; game-native invocation without a new command executable |
| Extension Packs | E08/E14 tactical-turn-based; E13 precision-platformer; other examples core-only, including E07 to preserve a substantive no-pack traversal baseline. Both P5 showcases/reuse cases remain additional P6/P7 work |
| Failure modes | E01 stale reset; E02 contact double effect; E03 transform/depth mismatch; E04 stale score session; E05 invalid target/knowledge; E06 coupled cost loop; E07 content collision; E08 phase/preview; E09 camera/cue occlusion; E10 post-placement soft lock; E11 save/collection; E12 duplicate reward/reconnect; E13 route regression; E14 narrative/phase/pack conflict; E15 linked-world restore/release dependency |
| Repair behaviour | Each names a local fault and accepted stable decisions; retain baseline, faulty and repaired output and rerun affected cases. Do not regenerate unrelated content or weaken expectations |
| Performance risks | Timing/contact E02/07/13; perception E05; rendering/camera E03/09/15; generated/state/agent load E10/11; message/backlog E12; cumulative content/assets E13–15 |
| Accessibility challenges | Complete keyboard paths, redundant cues and focus throughout; precision/input demand E02/07/13, hidden-information clarity E05/08, depth/camera E03/09/15, timers/pacing E04/06, dense data E11 and two-player state E12 |
| Cross-domain handoffs | E07–09 UI/environment/animation/audio, E13 environment/visual/audio, E14 narrative/animation/audio/UI and E15 environment/3D/narrative/audio. Original source deliveries and integration records must exist; a list of desired assets is not a handoff |
| Benchmarkability | Identified oracle/setup, actual input/state, deterministic small cases where adequate, seeds/policies/network schedules where relevant, human/target claims separated |
| Showcase clarity | One named production question per L1 example; one complete loop per L2; representative integrated slice at L3; identifiable systemic fault at L4; bounded finished thesis at L5. Each README explains the observed benefit and remaining limits |

The entire set covers all twenty requested dimensions without promising every platform or genre. Breadth is deliberate and bounded: first proof remains local single-player; 3D and multi-peer paths earn their own execution evidence later. Level numbers do not certify maturity. Additional mobile/gamepad/XR/console examples require suitable tooling and actual device evidence before expansion.

### 15.5. Commands and source-derived case coverage

| Named operation | Principal examples / observable work |
|---|---|
| define-game-thesis | E04–06 loop question; E13–15 complete thesis and accepted scope |
| design-mechanic | E01–03 rules/input/state; E08 discrete actions |
| model-system | E06 costs/feedback; E10 progression/placement; E11 flow; E12 authority; E14 campaign dependencies |
| build-playable-proof | Every example; initial core vertical selected later from L1 |
| integrate-content | E07–09 and E13–15 actual versioned source deliveries and runtime binding |
| repair-gameplay | Every example's bounded fault, preservation and actual reruns |
| prepare-playable-build | E07–09 representative candidate; E13–15 identified local release candidates |
| validate-gameplay | All rule/phase/reset/interaction cases, especially E01/06/08/10–12 |
| evaluate-player-experience | Actual sessions E04–06 and question-led L3/L5 playtesting; contact/depth/feedback technical observations kept separate |
| evaluate-balance | E04–06 risk/pacing, E08/10–12 strategies and E13–15 appropriate experience/system questions |
| evaluate-accessibility | Whole task paths in every example; critical motor/colour/focus/depth/data barriers remain explicit |
| evaluate-performance | Target/workload measurements E07–15; timing and representation checks where needed in L1/2 |
| diagnose-gameplay | Every named fault; independent evaluation recommendations before authorised source changes |
| author-extension-pack | E14: review actual tactical-profile applicability and evidence, make only a justified bounded revision with affected cases; a no-change finding is valid, invented authoring work is not |

Core candidate cases remain hypotheses until selected and executed by the benchmark stage: BC01→E04/06, BC02→E01, BC03/05→E02, BC04→E06/11, BC06→E07, BC07/09→E03/05/09, BC08→E04/11, BC10→E07–09 scope review, BC11→E13, BC12→E13/15, BC13→E10, BC14→E05, BC15→E11/15, BC16→E12. The mapping supplies a concrete production context without converting every example into a full benchmark suite or claiming the fixture has run.

### 15.6. Execution and preservation protocol

At Stage 20, run each complete prompt with recorded installed skill/pack revisions, model/tool/runtime versions where relevant, project/build identity, actual commands and allowed resources. Use ordinary game-specific code and suitable existing libraries; do not create a shared engine to make the examples uniform. Games with 3D or transport needs select declared normal dependencies and validate those paths directly. No accounts, paid services, public hosting or platform certification are required by this curriculum.

Choose and record project-specific rule values and representative workload/measurement limits before accepting the baseline. Tuning comparisons declare permitted variation; post-acceptance repairs preserve fixed rules and stable content. Every example retains a reproducible negative or injected-fault case and the expected result, plus baseline/fault/repair versions. Where an evaluator intentionally supplies a faulty fixture, disclose the injection in evidence and avoid pretending the author was blind to a fault they themselves inserted.

Use real input for input claims and authoritative game state for rule claims. Label controlled setup, model-only simulation, synthetic network delivery conditions and human evidence separately. Observe player-facing content at the appropriate modality. A generated audio file or waveform alone cannot establish audible mix quality; a screenshot cannot establish timing, depth control or performance. Local release-candidate validation means build/package and fresh local run with identified content/dependencies and quality gates; it does not authorise external publication.

The evaluation cases and thresholds above retain these curriculum gates, and this specification links every complete prompt. Stage 18 may scaffold output directories, Stage 19 proves one installed core vertical, and Stage 20 must produce and inspect all fifteen actual examples plus the separately required pack evidence. Unavailable required proof is a blocker at its owning execution gate, not a reason to count a plan as an example.

## 16. Release gates and measured-evidence register

A representative build must prove the scope it claims. A local release candidate additionally needs complete packaged dependencies/content, exact run instructions, current source/build identity, fresh-directory and clean-state execution, complete required sessions, errors/asset checks and the applicable mechanical/systemic/human/access/performance/preservation gates. Editor or development-server success alone cannot pass it. External publication is a separate authorised action.

Each actual result records case/claim and expected-behaviour revision, tested skills/packs/runtime/model/tools, exact prompt/commands, target/workload/input/seed/policy/participant conditions, actual observations and raw evidence, failed/unfinished/excluded cases, diagnosis/repair/regression and limitations. Historical research examples or a synthetic predicate keep their original narrow scope. A specification or planned case is not measured evidence.

| Evidence category | State at this specification baseline | Required proof before advancing |
|---|---|---|
| Research/design conformance | Stages 1–14 accepted; P1–P5 for both packs complete | This supports design provenance only |
| Historical synthetic checks | Only the explicitly labelled arithmetic/handoff checks in their owning research logs | Do not promote them to actual game, skill or human benchmark results |
| Installed core vertical | Not run | Actual clean installed brief → playable session → evaluation → diagnosed repair → preserved reruns |
| Fifteen primary example outputs | Not run | All five trios with exact prompts, runnable artefacts and their full evidence gates |
| Real human playtest evidence | Not collected by this bootstrap so far | Appropriate actual participants/sessions for every required experiential or first-use claim |
| 3D / multi-peer / other target qualification | Not demonstrated | Actual representative runtime, input, integration and target/session evidence for each claimed path |
| Pack P6/P7 | Not run; implementations planned | Exact showcases, distinct reuse, twenty-five cases as applicable, competent-core comparison and installed use |
| Repository/CI implementation | Not implemented | Actual validator/negative tests and executed local/CI results; no empty-fixture or skipped-pass claims |
| Clean selective installation | Not run | Production/evaluator/creator and selected pack/combined/negative scenarios under specification 03 |
| Release candidate / readiness | Not established | Identified built candidates with required quality and fresh-use evidence, plus applicable authority |

Keep this register and catalogue status aligned with actual later proof. Unresolved required failures block the corresponding claim; they cannot be averaged with passing dimensions. The full bootstrap audit must repair the owning stage and recheck affected downstream work before declaring all mandatory work complete.
