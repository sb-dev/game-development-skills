# 02 — Workflows and Artefacts Specification

**Status:** Canonical design  
**Version / date:** 1.0 / 2026-09-13  
**Authority:** Accepted Stages 3–7, consolidated without changing their decisions. [System](01-game-development-skills-system-spec.md), [command contracts](03-game-development-skills-repository-and-contracts-spec.md) and [evaluation](04-testing-and-benchmark-spec.md) define the surrounding boundaries.

## 1. Workflow and entry points

Start from the consumer's actual request and accepted state. A whole production can move through intent → thesis → mechanics/system → adequate proof → actual evidence → selection/commitment → integrated content → evaluation → causal repair → representative/release build. This is a dependency-aware workflow, not a compulsory sequence for every task. An existing game can enter at diagnosis, a design request can end with a design, and a narrow repair does not restart the thesis or adequate research.

| Work | Inputs and decision | Required output / completion |
|---|---|---|
| Frame play | Brief, intended players/context, constraints and alternatives; distinguish aspiration from rules | Compact thesis and contrary evidence questions, selected revision/status and next adequate proof |
| Define behaviour | Verbs, entities/resources/state, eligibility, effects, feedback and outcomes | Implementable normal/invalid/boundary/reset cases, timing/units and preserved decisions |
| Model composition | Member rules, loops, resources, progression, space and other actors | Bounded relationship model with assumptions, adverse strategies and executable consequences when claimed |
| Choose proof | Current uncertainty, claim/evidence kind, costs and essential variables | Least costly adequate representation, omissions, execution plan and actual results when requested |
| Build playable proof | Accepted rule/interaction scope and available native runtime | Actual input, consequential state, feedback, outcome/recovery and relevant observed checks |
| Integrate content | Accepted geometry/behaviour plus producer deliveries | Versioned source/import/runtime relationship, playable content, handoff acceptance and correct repair owner |
| Evaluate | Question, build/model, expected result, target/people/cases | Actual evidence and scoped interpretation; structural, mechanical, systemic, human, access and target results separate |
| Tune/repair | Reproduction, accepted constraints, cause/alternatives and authority | Smallest sufficient change, failing/affected-case reruns, preserved work and keep/revert decision |
| Prepare delivery | Identified candidate, dependencies, target and quality requirements | Built/package identity, actual fresh play, applicable quality evidence, reproduction instructions and remaining issues |

Use project-native files and records. A concept needs its own record only when it has an independent decision, consumer, validation or repair scope. Do not create a mandatory GDD, global graph, folder hierarchy or duplicate evidence database for a small task.

## 2. First-class records and lifecycle

The three core records are **thesis**, **behaviour definition**, and **system/encounter composition**. A file may contain multiple identified records. Findings, proof decisions, handoffs and run evidence can be linked sections or independent records when their use justifies it. Every record must preserve the applicable eleven properties below; a role can be carried by the same person/agent as another role.

| Property | Thesis | Behaviour | Composition |
|---|---|---|---|
| Creator | Designer/designated owner | Gameplay/technical designer and implementer | Systems/level/encounter designer and participating owners |
| Purpose | Intended play and bounded commitment | Local implementable interaction | Combined responsibility, dependencies and uncertainty |
| Consumers | Prototype, mechanics, content, evaluation | Runtime, content, systems, evaluator | Integration, encounter/balance, evaluation, delivery |
| Source evidence | Brief/research/constraints/findings | Exact thesis and relevant finding | Exact members, integration conditions and strategies |
| Preserved decisions | Direction/scope/constraints | Semantics, ranges, input/feedback/state | Dependencies, progression, placement/information |
| Status / confidence | Draft/accepted/rejected/superseded plus limits | Decision status separate from specified/implemented/verified | Decision status separate from modelled/integrated/evaluated |
| Approval behaviour | Existing accept/reopen authority | Routine authorised tuning proceeds; material semantics reopen | Accepted interactions/content changes use affected owner authority |
| Runtime expression | Constrains game; no required class | Identified code/data/controller/binding when implemented | Identified scene/configuration/wiring when integrated |
| Validation | Claim-appropriate thesis/evidence review | Rules, boundary/reset, input/feedback and relevant human question | Interactions/flows/progression/recovery and appropriate human play |
| Repair scope | Implicated premise/constraint | Rule/value/transition/binding/cue | Interaction/dependency/placement/schedule |
| Downstream impact | Affected prototypes/rules/content/evidence | Systems, cues, content, saves/network and tests | Encounters/progression/content/strategies/targets/builds |

Use stable identity and revision, active scope, status, authority and evidence limitations. Accepted, implemented and verified are distinct. Preserve rejected/superseded alternatives with reconstructable snapshot or immutable reference, rationale, evidence and authority; exclude them from active requirements. When a replacement is approved, change the active reference explicitly and review affected evidence rather than inheriting old passes automatically.

## 3. Game thesis

Keep the active thesis short enough to direct the next decision. It states what players should do, understand and experience, proposed play and evaluation conditions. Fiction, novelty, competition, saving and win/fail are not mandatory for every game. Open-ended play still needs entry, meaningful consequences and stop/resume intent.

```markdown
Identity / revision / active scope / decision status:
Owner / authority / source and alternative references:
Players and context: relevant prior knowledge, access/input needs and session shape;
label assumptions rather than claiming an established audience.
Intended play: role when useful, core verbs, meaningful choices/challenges,
learning/mastery intent and experience hypothesis; optional differentiator.
Loop and outcomes: situation → action → consequence → changed situation;
risk/reward, entry/end, success/failure or open-ended continuation, retry/reset.
Conditions and boundaries: viewpoint, platform/runtime/input/social mode,
access, non-goals and unresolved material constraints.
Evidence questions: claim → evidence kind → contrary result → next decision.
Next proof: essential behaviour/conditions, permitted omissions and authority.
Commitment: accepted constraints, authorised work/bounds and unresolved decisions.
```

Rule claims need rule/runtime evidence; observed player behaviour needs actual appropriately scoped observation; experience aspirations need actual human accounts/observations; external learning/real-world effects need suitable external evidence and study design. A threshold or sample plan may be proposed but is not measured. “Fun”, “immersive” or a feature list alone cannot select a useful proof.

Before wider content commitment, identify the accepted revision, audience/context, core activity/experience, material platform/input/view/social constraints, scope/access and evidence/quality obligations. A draft can guide already-authorised reversible exploration; it cannot silently replace an accepted baseline or approve expensive expansion.

## 4. Mechanics, rules, systems and loops

| Concept | Required distinction |
|---|---|
| Player verb | Intentional requested action, distinct from input binding and eligibility |
| Rule | Condition/transformation/constraint, distinct from its implementation |
| Mechanic | Operative rules/data/processes enabling interaction; may serve multiple purposes |
| Resource | Quantity with unit, owner/bounds and source/sink/transfer/conversion rules |
| Entity | Identifiable participant/object with relevant properties/lifetime; need not be visible or an engine class |
| State | Values/relationships governing next possibilities; authoritative, derived and durable state differ |
| Feedback | Player-available meaning of action/state/consequence; correct state can have an incorrect cue |
| System | Bounded interacting mechanics/resources/entities; boundary does not guarantee independent effects |
| Loop | Repeated player activity or reinforcing/stabilising feedback; identify which meaning applies |
| Progression | Changed access/capability/challenge/accomplishment, distinct from map connectivity and saved state |
| Win / failure | Outcome predicate/decision with continuation/reset; record absence when intentionally open-ended |
| Encounter | Bounded player/agent/system/information/content situation, possibly non-spatial |
| System interaction | Shared state/event/resource/time/information/space dependency where a combined defect may live |

A behaviour definition supplies its purpose/thesis, creator/consumers, decision/authority and actual evidence state; source/preserved constraints; entity lifetime and state/resource ownership/units/bounds; initial/derived/reset/persistent values and invariants; trigger/input mapping, preconditions, effects, invalid result and feedback; outcome/interruption/cancel/retry; time basis/order/ties, response/reference frame, accepted parameter ranges and randomness; concrete runtime expression; normal/invalid/boundary/reset tests and relevant human question; responsible repair and downstream consumers.

Use a trigger/prior-condition → allowed state/resource effect → feedback/unavailable-result table when helpful. A curve or equation may be clearer for continuous response. Two competing events need declared priority, order or simultaneous semantics. Fresh/held/repeated inputs, target loss and interruption need a result when material. A number cannot silently mean per frame, per second and per turn. Feedback specifies meaning before expensive assets. Randomness/reproduction and save/network ownership are explicit when applicable, never default universal dependencies.

A composition supplies exact member behaviour revisions and shared ownership, events/order, information, space/content and interfaces; the player activity loop; resource sources/sinks/conversions/feedback; prerequisites/access/progression and outcomes/reset; encounter conditions, strategy hypotheses and adverse combinations; runtime wiring or explicitly unimplemented model; model omissions/horizon/termination and invariant/interaction/human evidence questions; repair relationships and affected consumers. Describe a normal sequence and a plausible adverse combination. Check progression after actual placement and available-action costs, not just abstract connectivity.

Preserve these two reasoning chains without a mandatory global graph:

- Player goal → verb → rule → feedback → dynamic → actual playtest observation → tuning decision.
- Resource source → resource sink → progression pressure → strategy → economy result.

An observation stays unperformed until evidence exists. Scripts are declared policies, not assumed human strategies. Unexpected interaction is a finding to interpret; it is not automatically a defect to remove.

## 5. State, progression and recovery

Declare what resets on a local retry, checkpoint, session restart or full new game; what persists; who owns authoritative values; and how dependent objects are reconstructed. Outcome effects resolve as declared, including actor removal, empty phases, interrupts and stale inputs. A scene reload need not equal a valid game reset.

If persistence is promised, identify data/version/relationship invariants, write/recovery and compatibility policy. Preserve corrupt/interrupted inputs for diagnosis. Restore a complete valid checkpoint or the explicitly permitted reported recovery; do not silently combine incompatible state. If multiplayer is promised, declare authority, input/session/outcome identity, accepted prediction/reconciliation, join/leave/reconnect and adverse-delivery cases. Actual peers are needed for that proof; local single-runtime state cannot substitute.

For procedural progress retain seeds/configuration and final placement, validate required keys/gates/resources/actors and legal paths, keep failing cases and distinguish generator repeatability from full-runtime determinism. For AI, specify permitted knowledge, target eligibility, decision/execution, navigation, interruption and fallback. A path returned or an object saved is not proof of successful movement or restoration.

## 6. Prototype strategy and commitment

Name the question and decision; identify essential conditions and claim kind; compare adequate representations; choose the least costly considering creation/change, dependencies, integration, review, external spend and reversibility; execute when requested; retain observations/limits and a keep/repair/reject/investigate/commitment decision. Label estimated cost and unknowns rather than inventing measurements.

| Uncertainty | Adequate starting proof and limit |
|---|---|
| Rule | Written cases/state table; runtime still needed for implementation claim |
| Economy/probability | Bounded calculation/simulation with units, distributions, policies and horizon; not human balance |
| Movement | Controller/input/contact/view sandbox and representative spacing; constants alone insufficient |
| Combat timing | Small arena with actions/cues/hits and required movement |
| Camera | Moving camera/geometry/input conditions, not a static image |
| AI | Inspectable decision and executed movement/action under permitted knowledge |
| Level flow | Actual greybox traversal/information, not editor flight |
| Progression | Dependency/state sequences plus relevant integrated spatial/content effects |
| Procedural content | Retained cases and final-placement constraints plus appropriate play review |
| Network | Actual peers and declared delay/loss/recovery conditions |
| Performance | Representative workload and suitable target build/tool endpoints |
| Comprehension | Actual relevant humans and minimally adequate content/cues |

Fidelity choices span rules, input/timing, feedback, space/content, system combinations, workflow and target. Rule table, simulation, mechanic toy, placeholder game, greybox, representative encounter, vertical slice, integrated content, target build and release candidate are optional contexts, not ten compulsory phases. A late defect can return to a small model; early target constraints can require an early build. Keep or replace prototype implementation according to suitability/reuse cost.

The relevant commitment points are thesis, mechanic, control, loop, representative level/encounter, vertical slice, content scope and release candidate. Before material reliance record exact candidate/revisions, demonstrated/omitted evidence, constraints, cost/resource scope, downstream impact and alternatives. Use already granted authority for reversible work and approved-range tuning; seek only a genuinely missing decision. A new accepted commitment does not close untested quality claims. Reopen the affected accepted dependency before an out-of-scope change, retaining unaffected work.

## 7. Levels, worlds, encounters and content

| Artefact concept | Minimum content / acceptance question |
|---|---|
| Level brief | Player task/knowledge, movement/view, constraints/outcome and upstream revisions; does actual play expose the intended task? |
| Encounter brief | Capabilities, information, challenge/recovery and space/time; do interacting parts support the decision? |
| Flow map | Connections, choices/gates and information; topology needs separate geometry proof |
| Critical path | Required dependencies, alternatives/recovery; can legal play reach the outcome? |
| Spawn/pacing plan | Conditions, location/order, workload and reset/despawn; inspect actual overlapping demands |
| Greybox | Playable changeable geometry tied to movement/camera/contact revisions |
| Navigation constraints | Actor clearance, traversability, dynamic obstruction and connections; execute movement, not just pathfinding |
| Local tags/sockets/interaction contract | Required names/attachment/event meanings and missing-reference handling |
| Asset integration requirements | Source/export revision, units/axes/scale/pivot, formats/dependencies/import and gameplay use |
| Collision requirements | Shape, clearance, layers/filter, trigger/block and dynamic changes |
| Animation requirements | Clip/state intent, timing/markers, transition/cancel and movement ownership |
| Audio feedback requirements | Meaning, trigger, priority/repetition/mix/loop and non-audio alternative |
| Narrative trigger requirements | Intent, conditions, variables, once/repeat/branch/continuity |
| Performance budgets | Actual target/workload, units/measurement and accepted gameplay trade-offs |

These fourteen concepts may be sections of a composition/handoff; they are not fourteen mandatory files. Non-spatial games can omit spatial artefacts with a reason. Preserve source versus import/configuration versus runtime identity so a replacement/reimport can be diagnosed. Establish gameplay constraints in a bounded representative use before scaling content, then inspect actual player traversal, view, action timing, narrative state, audible cues, access and workload as applicable.

## 8. Handoff contract and repair ownership

Each handoff identifies revision/status; producer, integrator and consumers; purpose and upstream/source evidence; preserved constraints/authority; actual delivery and dependencies/properties/units; integration/bindings/state/placement; concrete runtime; acceptance and actual evidence/limits; suspected repair owner and downstream impact. Proposed requirements, delivered properties and observed results remain distinct.

| Handoff | Producer | Integrator / correction boundary |
|---|---|---|
| Narrative → gameplay | Accepted character/story intent, content revision, branches/variables/triggers and continuity | Bind role/state/once/repeat/interruption/reset/save; wrong binding belongs to integration, contradictory/missing agreed content to Narrative |
| Environment/3D → playable space | Source/export version, units/axes/scale/pivot, geometry/collision contribution, sockets/dependencies | Import/place/configure and play-test collision/navigation/view/workload; wrong scale/placement belongs to integration, bad delivered dimensions to producer |
| Animation → behaviour | Compatible rig/clip version, motion intent, timing/markers, transitions and root-motion contribution | Bind states/hit windows/time conversion/cancel and one movement owner; bad playback binding differs from incorrect marker/motion source |
| Music/audio → feedback | Identified cues/stems, roles, loops/transitions, mix/state inputs and delivery properties | Bind events/priorities/mix/interruption/reset and inspect audibility/meaning/alternatives; bad routing differs from missing/corrupt/incorrect source |

The agreement can divide responsibilities differently when explicit. File extension or job title alone does not assign cause. Preserve valid specialist craft rather than replacing it to hide gameplay integration faults. Material changes to accepted intent/rules retain owner authority.

## 9. Playtest and other evidence

| Evidence kind | Useful claim / limit |
|---|---|
| Scripted tests | Actual exercised transitions/invariants/input; not unchecked play or human experience |
| Headless simulation | Represented rules/policies/distributions/horizon; not omitted rendering/input or human behaviour |
| Bot/agent play | Declared observation/action policy and privileges; not human discovery, learning or fairness |
| Telemetry | Recorded eligible events/sessions/cohorts after collection validation; not intent, cause or missing populations |
| Replay | Visible/reconstructable sequence with build/state/input/seed and divergence checks; not hidden intent or absent state |
| Expert review | Reasoned inspected-scope judgement and alternatives; not representative unfamiliar-player evidence |
| Human comprehension/usability | Actual relevant task attempts/understanding with context/assistance; not broad prevalence or unaided success after coaching |
| Human experience | Situated accounts/observations about agency/challenge/fairness/feel; not universal satisfaction or causal external effect |
| Target profiling | Measured workload/build/device and endpoints/overhead; not untested hardware or human quality |

Select the claim and contrary result before collecting evidence. For humans specify relevant knowledge/access/input/exposure, neutral tasks and observation/account method; record help, failures and withdrawals. For telemetry define event meaning/units, actor/session/attempt/build, ordering/duplicate/drop/outcome semantics and inspect known actions/restarts against records. Zero events may mean broken collection. Retain raw relevant observations, cohort denominators/exclusions and invalid data. Separate observation/account from interpretation and causal claims.

## 10. Balance, tuning and repair loop

Choose applicable metrics for the decision, never a mandatory universal dashboard: win and pick rates need eligible opportunities/cohorts; clear rate needs attempt/completion/retry handling; resource curves need units/flows/policies; time-to-kill needs stated endpoints/combat context; time-to-mastery needs repeated humans/criterion/unfinished cases; strategy diversity needs meaningful viable alternatives; difficulty curves need preparation/information/cohort context; reachability needs actual permitted actions; progression pacing needs stalled/unfinished cases; risk/reward needs distribution/opportunity/information; snowballing needs traced reinforcing relationships; rubber-banding needs agency/intentional-underperformance countercases. Popularity, equal expected value or favourable aggregates are not sufficient balance evidence.

The seven-step loop is:

1. **Observe:** retain expected/actual finding, revision, context and evidence validity.
2. **Diagnose:** compare rule, implementation, cue, composition, source, system and collection explanations.
3. **Locate responsibility:** identify the causal parameter/rule/relationship/owner and affected consumers.
4. **Change:** make the smallest sufficient authorised edit; state expected/adverse effects and comparison. Coordinate edits only when necessary.
5. **Rerun:** reproduce the disputed condition and affected accepted cases with appropriate runtime/human/target evidence.
6. **Compare:** inspect intended effect, regressions, collection and cohort/exposure differences, uncertainty and alternative explanations.
7. **Keep/revert:** keep only a supported authorised correction; otherwise revert/revise/investigate, preserving versions and rationale.

A repair record contains claim/finding identity, creator/consumers, input/authority/preserved revisions, method/setup, expected versus actual observations/accounts, diagnosis and alternatives, change/hypothesis, rerun/preservation, disposition and downstream impact. Failed, blocked or inconclusive claims stay visible. A changed model can require a new baseline; old inputs cannot prove new-player comprehension. Do not retune the game using invalid collection.

## 11. Failure taxonomy and repair routes

These twenty-one diagnostic categories preserve Stage 2 identities. They are hypotheses for classification, not a finding that every game contains them. Severity depends on required task, frequency/recovery and affected players.

| ID / symptom | Distinguishing evidence / initial responsible repair |
|---|---|
| D01 Unclear goal | Relevant player cannot infer useful action; distinguish intended openness; repair implicated purpose/cue/choice and retest without prior explanation |
| D02 Weak loop | Intended decisions/motivation absent despite execution; inspect incentives/accounts; repair causal choice/cost/consequence before scaling |
| D03 Unresponsive controls | Input/eligibility/focus/timing disagreement; fix responsible mapping/state/buffer and neighbouring/remapped paths |
| D04 Poor feedback | Correct consequence but missing/masked/wrong meaning; repair cue/channel/timing and actual recognition conditions |
| D05 Unreadable combat | Threat/counter/hit obscured by competing cues; repair hierarchy/alignment/overlap while preserving challenge |
| D06 Soft lock | Active game lacks required progress/recovery; retain exact history and repair transition/reset/route |
| D07 Unreachable content | Permitted actor cannot reach object/route/trigger; repair placement/clearance/contact/access and dependent play |
| D08 Dominant strategy | Relevant alternatives invalidated, not merely popular; inspect costs/information/counterplay and interacting rules |
| D09 Trivial bypass | Low-engagement tactic bypasses intended challenge; first decide whether discovery is desirable, preserving legitimate creative play |
| D10 Progression dead end | Consumed item/branch/order blocks required later access; repair dependency/recovery and state/save paths |
| D11 Economy runaway/collapse | Reproducible compounding/depletion; repair source/sink/conversion/feedback and compare policies/horizons |
| D12 Difficulty spike | Unintended demand jump for relevant cohort; inspect preparation/resources/information before adjusting challenge |
| D13 Unfair information | Knowledge violates intent or required counter lacks information; repair exposure/agent knowledge/cues while preserving intentional hidden state |
| D14 Level flow failure | Reachable routes produce unintended disorientation/backtracking/pacing; repair connection/landmark/sequence from player view |
| D15 AI deadlock/exploit | Selection, path or motor stalls/oscillates; repair eligibility/fallback/interruption/locomotion and target-loss cases |
| D16 Physics instability | Tunnelling/jitter/divergence under known time/contact/load; repair update/contact/integration assumptions without hiding intended motion |
| D17 Save corruption | Invalid/lost/duplicated/incompatible values/relationships; preserve bad data, repair write/reconstruction/recovery/migration |
| D18 Network desynchronisation | Authoritative disagreement beyond declared policy; retain peer/message/time and repair authority/order/reconciliation under adverse delivery |
| D19 Performance spike | Representative workload exceeds declared budget despite mean; localise work/overload and remeasure while preserving play |
| D20 Input latency | Delay/variation across identified endpoints; diagnose responsible input/simulation/render/presentation segment and actual task |
| D21 Accessibility blocker | Required task unavailable under intended access condition; inspect configuration/full task, supply suitable alternative or remove barrier and retest |

Intentional loss, hidden information, unequal abilities, low difficulty, randomness and unexpected invention are not automatically defects. A classifier must consult accepted intent/rules and actual evidence. A correction closes only the supported finding and affected preservation checks; unrelated questions remain open.
