# Stage 2 - Professional Practice and Evidence-Qualified Capability Model

**Date:** 13 September 2026  
**Version:** 1.0  
**Status:** Stage 2 complete; Stage 3 not started  
**Bootstrap:** [Version 1.1, Stage 2](2026-09-07-game-development-skills-new-project-bootstrap-process.md#7-stage-2---challenge-and-extend-professional-game-development-practice)  
**Primary-source register:** [24 additional sources, examined locations and reading limits](2026-09-13-stage-02-source-evidence.md)

## 1. Outcome, inputs and research boundary

Stage 2 retains the five-book model as a useful starting point, qualifies its claims and extends its account of professional work. The resulting model connects design intent to implementable behaviour, integrated play, suitable evidence, bounded repair and delivery decisions. It explicitly adds gameplay AI/navigation, persistent-state recovery and networked-session responsibilities; strengthens accessibility, content integration, automation and profiling; and keeps live tuning conditional on an operating game.

The inputs are the [Stage 1 charter](2026-09-12-stage-01-project-charter-and-domain-boundary.md), [Stage 1A coverage map](2026-09-12-stage-01a-knowledge-coverage-and-five-book-corpus.md), [Stage 1B synthesis](2026-09-13-stage-01b-five-book-extraction-and-reconciliation.md) and its [35 direct findings](2026-09-13-stage-01b-book-findings.md). The branch baseline is [`18c5ecc4`](https://github.com/sb-dev/game-development-skills/commit/18c5ecc44e42f23f9d2794ab3b7cef45b7188aaf). The [family domain-research process v1.0](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/bootstrap/domain-research-process.md) governs the challenge method.

Corpus revision 2 remains **B1 Fullerton, B6 Adams/Dormans, B3 Swink, B4 Totten and B5 Lemarchand**. Finding IDs F1–F7, M1–M7, S1–S6, T1–T7 and L1–L8 retain their meanings and original page locations. This log supersedes their provisional dispositions where specified; it does not rewrite the historical extraction records.

Research used original studies, first-person production accounts, specialist practitioner material and current official guidance. It sought both counterexamples and missing responsibilities. R01–R24 below resolve to primary URLs; the companion records exactly what was examined. The source mix is uneven: concrete engine behaviour is better documented than universal claims about player psychology or production efficiency. Repeated citations are not counted as independent validation.

This is a **domain research result**. No game, simulation, participant session, benchmark, engine build, clean installation or release procedure was executed. The proposed checks are future evidence requirements. The charter's first proof remains one bounded local single-player session. Engine/provider selection, AI tooling, production architecture, skill contracts and the game-thesis representation belong to later stages; this stage does not select them.

## 2. Professional-practice map

### 2.1 Roles, decisions, working artefacts and handoffs

These are responsibilities, not a required staffing chart. A solo developer may perform several roles, but still needs the distinct decisions and evidence. Specialist craft and platform authority remain with the relevant owner under the charter.

| Discipline / role | Professional decision and working artefact | Evaluation and repair responsibility | Evidence / applicability |
|---|---|---|---|
| Game / gameplay designer | Translate audience, intended activity and constraints into candidate verbs, goals, consequences and an experience question. Maintain behaviour examples alongside intent. | Compare intended and observed choices; revise the implicated incentive, rule or premise. Preserve a negative prototype result as useful evidence. | F1–F3, M7, L1. Judgement about a particular game. |
| Systems / economy / progression designer | Make resources, conversion rules, prerequisites and strategy assumptions inspectable in diagrams, spreadsheets or executable models. | Check bounded scenarios and extreme strategies; explain omissions before extrapolating to players. Separate a healthy metric from an appropriate design change. | M1–M6, F6; live-balance limitations [R05]. Model validity depends on represented behaviour. |
| Technical designer / gameplay programmer | Connect allowed actions and state changes to runtime logic, timing, physics and reset behaviour. Supply diagnostic state and explicit integration assumptions. | Reproduce the failing state and isolate rule, update, input or integration causes. Check the correction at relevant boundary states. | F2, M1, S3, L7; timing analysis [R07]. Engine implementation is conditional. |
| Prototyper / producer | Choose evidence proportionate to uncertainty, then decide whether to continue, cut or invest in more representative work. Keep omissions and dependencies visible. | Judge what the proof actually demonstrates, including production cost where relevant; revise estimates as real work accumulates. | F3, L1–L4; [R04]. No universal prototype/slice schedule. |
| Level designer | Relate tasks and routes to movement metrics, camera, collision and content placement. Use dependency diagrams and playable blockouts for different questions. | Play from the normal viewpoint; change the implicated route, scale or obstruction and check affected traversal. | M5–M6, T1–T3; [R08]. Primarily authored spatial practice. |
| Combat / encounter designer | Compose available actions, threats, counters, information and recovery. Keep the encounter's intended challenge distinguishable from missing information. | Review attack outcomes, cue competition and first-use interpretation; repair an unreadable cue or invalid counter separately from intended difficulty. | T5–T6, S5; competitive clarity account [R06]. Encounter goals vary by genre. |
| Gameplay AI designer / programmer | Define an agent's available knowledge, legal decisions, targets and execution conditions. Inspect selection separately from path following and physical movement. | Diagnose invalid targets, stalled actions or locomotion failure at the responsible layer; preserve a trace explaining the choice. | Production case [R12], navigation responsibilities [R19]. Utility scoring is optional. |
| Technical artist / content integrator | Agree source assets, runtime scale, collision, animation hooks, references, import settings and playable acceptance conditions. Preserve authored/customised boundaries. | Reimport and inspect resulting behaviour; trace a missing reference or changed animation/collision property before requesting broad asset rework. | T2, L7; content checks [R13], import behaviour [R24]. Asset creation craft remains adjacent. |
| Games user researcher / playtest facilitator | Choose a question, relevant participants, conditions and method; record observations, assistance and interpretation separately. | Decide whether evidence concerns discovery, first use, repeated mastery or comparison. Investigate test artefacts and verify corrections. | F4–F5, L5–L6; [R01]–[R03]. A method is not population-wide certainty. |
| Accessibility designer / specialist reviewer | Identify barriers along critical tasks, including starting and configuring play. Select usable input and information alternatives for relevant needs. | Inspect requirements and observe their use with appropriate players; record remaining barriers and overlapping needs. | Charter, F7; specialist guidance [R09]–[R11]. Guidance is not certification. |
| QA / automation engineer | Turn stated behaviour and content constraints into isolated checks and reproducible findings tied to a build. | Distinguish static, component, integrated and human evidence; recheck changed and affected behaviour after repair. | F5, L7; content validation [R13], automation design [R16]. Passing checks covers their assertions. |
| Performance / runtime engineer | Declare target conditions and measurement boundaries; capture representative activity and diagnose costly work. | Validate a change in the relevant built target; distinguish input-to-display delay, simulation behaviour and rendering measurements. | S2; [R07], [R14], [R18]. No universal latency or frame budget adopted. |
| Persistence / online engineer | Specify which progress and relationships survive restart or device/session transitions, and who may change shared state. | Check restoration, incompatible state and interrupted sessions against a declared recovery policy. Escalate architecture-specific gaps before claiming support. | [R15], [R20], [R22], [R23]. New responsibilities; detailed recovery methods remain conditional. |
| Build / release owner | Identify the candidate, prerequisites, included content, access conditions and unresolved findings; prepare the actual consumer delivery path. | Reproduce start, play, outcome and recovery in the distributed candidate. Give the authorised owner evidence for a delivery decision. | L7–L8; export prerequisites [R21], distribution conditions [R17]. Release authority is unchanged. |
| Live designer / analyst, when relevant | State the tuning hypothesis, affected cohorts and content/rule version; connect observed changes to intended game health. | Compare expected and observed effects, investigate cohort/sample shifts, and propose a bounded follow-up or reversal. | M4, L6, L8; historical account [R05]. Live balance is additional operating work, not required for the first proof. |

### 2.2 Terms must identify the uncertainty being reduced

**Prototype** means an investigation with deliberate omissions. Paper can reveal rule and choice problems; a spreadsheet can expose resource arithmetic; simulation can explore specified strategies; a runnable interaction can expose control, timing and integration problems. None answers every question. This adapts F3/M4/S1/L1.

**Greybox, whitebox and blockout** refer here to changeable spatial representations tested with relevant gameplay conditions. A relationship diagram is not a floor plan, and a traversable empty layout is not a completed encounter. T1–T3 and [R08] supply the spatial basis.

**Representative slice** needs an explicit dimension of representation: player activity, integrated quality, content variety or production pipeline. L2 emphasises representative integrated play; [R04] emphasises production repeatability. Our resulting requirement is to state which claim the slice actually investigates before using it to justify a commitment.

**Alpha, beta and release candidate** are local coordination labels. Their useful meaning comes from the project's stated completeness, defect, compatibility and delivery conditions (L7–L8). A label is not replacement evidence.

### 2.3 A decision loop, with several legitimate entry points

The following is a project synthesis of the books and practice map. It does not transplant one studio's phases. A technical uncertainty may require a runtime experiment before spatial design; a turn-based rule question may begin on paper; an existing game may enter at a reproducible defect.

| Situation and input | Work that reduces uncertainty | Working output and commitment point | Return path when evidence fails |
|---|---|---|---|
| A proposed experience or an unclear defect | State a falsifiable question; select an adequate representation or reproduction setup. | Question, relevant conditions, omissions and criterion for the next decision. Authorise only the scope needed to learn. | Revise the premise or test setup before increasing content or fidelity. |
| A promising interaction with unknown combinations | Integrate a coherent session or representative combination; inspect rules, controls, space and feedback together. | Playable increment, affected dependencies and observed limitations. Decide what additional work the evidence justifies. | Reduce scope, repair integration or test a competing design. |
| Repeated content production | Exercise authoring, import, implementation and review with representative content; include rework and testing effort. | Accepted content conditions and revisable effort/dependency estimates. Commit to a bounded increment. | Change the pipeline or content specification when repetition exposes hidden cost. |
| A candidate requiring evaluation | Run the method matched to the claim; preserve build, conditions, interventions, observations and traces. | Findings with limits, owner and expected versus actual behaviour. Decide repair, accepted exception or further investigation. | Correct collection when evidence is invalid; correct play when the evidence supports that diagnosis. |
| A correction to accepted work | Inspect cause and affected dependencies; make the smallest sufficient change, including coordinated changes when necessary. | Replacement evidence for the defect and affected accepted play. Reopen material decisions only under existing charter authority. | Restore an accepted condition or revise the authorised decision if the proposed repair damages it. |
| A delivery or live-update commitment | Check the identified consumer candidate and relevant operating conditions. | Versioned readiness evidence, unresolved issues and owner decision. Publication follows the established authority boundary. | Repair the candidate or defer the commitment; retain evidence explaining the decision. |

Routine authorised work proceeds without a fresh permission gate. Material scope changes, publication decisions and reopening accepted decisions follow the charter. Researching a platform's publishing controls does not authorise using them.

## 3. Challenge results and evidential standing

### 3.1 What the additional evidence changes

The distinction between **decision** and **standing** matters. A method can be retained while remaining a qualified practitioner method. A rejected universal extension does not reject the narrower useful observation or imply that an author made that extension without qualification.

| Standing | Concrete result of challenge | Consequence for this project |
|---|---|---|
| Supported finding, bounded to its study | Small-group problem discovery varied substantially in Faulkner's task; tutorial effects differed across Andersen's games. [R02], [R03] | Universal participant quotas and uniform tutorial-benefit claims are not defensible gates. Neither study supplies a universal alternative. |
| Qualified method | RITE depends on diagnosis and the capacity to change/retest; representative target profiling differs from editor measurement. [R01], [R14] | Specify prerequisites and evidence conditions before claiming a correction or performance result. |
| Context-dependent heuristic | Blockout iteration and slices are useful for particular spatial or production uncertainties. [R08], [R04] | Retain the question and representation fit; avoid a mandatory stage order for every game. |
| Disputed claim | “Objective” usability certainty or a numeric balance result establishing the right experience goes beyond the evidence. L5, M4; [R02], [R05] | Preserve interpretation and uncertainty; design decisions still require situated judgement. |
| Unresolved question | Historical perceptual thresholds and universal spatial-risk/real-world learning claims lack adequate validation in this research. S2, T6, M7 | Do not encode them as unconditional defaults. See G03, G07 and G09. |
| Rejected idea | More feedback always improves clarity; a successful automated or editor check establishes whole-game quality. [R06], [R14], [R16] | Evaluate the relevant information/task and the actual claim. These are rejected extrapolations, not blanket rejections of feedback or automation. |

### 3.2 Dispositions for all 35 book findings

The short finding names below point to the fuller, page-located Stage 1B records. “Retain” accepts a bounded responsibility for later design, not implemented support. Where new evidence is indirect or absent, that limit is stated rather than filled by source counting.

| ID / finding | Decision | Evidential standing | Challenge and resulting boundary |
|---|---|---|---|
| F1 — Experience hypothesis | Retain | Qualified method | Keep intended emotion as a hypothesis. No study here proves that expressing it guarantees success; negative observations must remain admissible. |
| F2 — Procedures and rules | Retain | Qualified method | Retain joint player/system specification and boundary cases. The later implementation must supply runtime evidence; this method does not select an architecture. |
| F3 — Appropriate prototype fidelity | Retain / adapt | Context-dependent heuristic | The book already permits digital-first investigation. Retain question/representation fit; no universal cost advantage or mandatory prototype order is established. |
| F4 — Uncoached observation | Retain with limits | Qualified method | Preserve interventions when making unaided-use claims. R01 is related lineage, not independent validation. Think-aloud effects on timed/immersive play remain unquantified here. |
| F5 — Reproduce and retest | Retain method; reject universal quota | Qualified method; rejected extrapolation | Primary RITE leaves verification count open [R01]; sampling variability challenges fixed sufficiency [R02]. Focused reproduction does not establish complete coverage. |
| F6 — Functionality, completeness, balance | Retain / qualify | Qualified method | Keep distinct diagnostic questions. Multi-use ability design [R12] challenges a blanket one-purpose rule; modular code does not guarantee independent gameplay effects. |
| F7 — Access from the outset | Strengthen; reject late-only timing | Qualified method | Specialist guidance supplies additional task/input/channel responsibilities [R09]–[R11]. Majority success and fixed samples cannot certify accessibility. |
| M1 — Implementable mechanics/state | Retain / qualify | Qualified method | Keep state modelling relevant to the mechanic. A single exhaustive graph is optional; network authority adds requirements beyond a local action graph [R23]. |
| M2 — Resource flows and feedback | Retain with bounded use | Qualified analytical method | Inspect flows under explicit assumptions. Broader research did not independently validate every Machinations pattern or a complete long-running economy; G05 remains bounded. |
| M3 — Consistent interactions and emergence | Retain / qualify | Context-dependent heuristic | Randomness is not inherently a defect. Exact determinism is a conditional network requirement [R20], not a general prohibition on stochastic gameplay. |
| M4 — Simulated strategies | Retain; reject model-equals-balance | Qualified method | Production metrics can locate outliers without determining an appropriate repair [R05]. Scripted strategy coverage and human interpretation remain separate. |
| M5 — Mission versus space | Retain | Qualified decomposition | [R08] adds actual-play spatial checks. Mission-first and space-first remain legitimate; a dependency diagram alone does not establish good encounters. |
| M6 — Progression dependencies | Retain / qualify | Qualified method | Retain declared prerequisites and integrated placement checks; obstacle-before-key is contextual. Independent end-to-end progression-validation methods remain incomplete in G05. |
| M7 — Meaning through actions | Retain interpretation; bound external claims | Context-dependent heuristic; unresolved question | Analyse incentives and player interpretations. No evidence gathered establishes real-world educational, behavioural or scientific transfer from the book's examples; G07 excludes that inference. |
| S1 — Whole interaction loop | Retain within scope | Qualified method | Runtime and end-to-end measurements describe only parts of experience [R14], [R18]. Direct real-time feel is one game form, not the definition of all play. |
| S2 — Response measurement | Retain method; defer thresholds | Qualified method; unresolved question | Distinguish measurement endpoints [R18]. No imported historical millisecond value becomes a budget; target and task-specific perceptual evidence are still needed. |
| S3 — Response over time | Retain / qualify | Qualified technical method | Update timing can alter simulated behaviour [R07]. Intended acceleration or anticipation is distinct from unintended delay; changing either needs its own hypothesis. |
| S4 — Spatial/control context | Retain | Qualified method | Actual blockout play [R08] supports checking control against geometry; navigation/motion separation [R19] adds implementation limits. Controller acceptance is context-bound. |
| S5 — Informative feedback | Retain; reject “more is better” | Qualified method; rejected extrapolation | Clarity work identifies cue competition [R06]; alternative channels address sensory barriers [R11]. Added effects need task evidence. |
| S6 — Apparent control unpredictability | Retain / qualify | Qualified diagnostic method | Input accessibility includes context-dependent activation/cancellation [R10]. Separate acknowledgement, allowed state transition and irreversible action; deterministic code alone does not settle perceived control. |
| T1 — Spatial representations | Retain | Qualified method | [R08] supports testing geometry with gameplay metrics. Diagrams and playable spaces answer different questions; 3D practice is not universal evidence for every game form. |
| T2 — Greybox to content | Strengthen preservation; qualify cutoff | Qualified method | Reimport/configuration can alter resulting content [R24]. Preserve accepted behaviour through replacement; late evidence cannot be dismissed solely by a phase label. |
| T3 — Player viewpoint | Retain / broaden conditions | Qualified method | [R08] supports actual-play inspection. Camera, available display area and access conditions belong in the setup; editor visibility is insufficient. |
| T4 — Environmental cues | Retain / qualify | Qualified method | Cue hierarchy [R06] and sensory alternatives [R11] strengthen the requirement. A colour-only convention is inadequate for critical information. |
| T5 — Observed onboarding needs | Retain; reject instruction quantity as success | Qualified method | The tutorial experiment supplies a contextual counterexample to uniform benefit [R03]. Judge the relevant player's learning and task, not tutorial length. |
| T6 — Spatial risk/respite/reward | Retain as optional heuristic | Context-dependent heuristic | No universal survival analogy is established. Use encounter-specific hypotheses; competitive clarity practice is not independent proof of the underlying psychology. |
| T7 — Generated playability | Retain with specialist boundary | Qualified method | Post-placement evaluation remains necessary. A complete PCG evaluation method and sufficient seed count are not established; retain the specialist boundary in G08. |
| L1 — Question-led early toys | Retain | Qualified method | Apply the evidence distinctions in section 2.2. An answered toy question can still leave integration, content production and delivery unproved. |
| L2 — Representative integrated slice | Retain / clarify representation | Context-dependent heuristic | Apply the representation distinction in section 2.2. Neither a beautiful corner nor the label alone warrants broader commitments. |
| L3 — Stable core, incremental integration | Retain; qualify absolutes | Qualified method | Retain incremental integration as a revisable strategy. Early finish and isolation are aids, not universal prerequisites; subsystem checks cannot establish integrated play. |
| L4 — Scope and dependencies | Retain; qualify forecasts | Context-dependent heuristic | Keep actual effort and dependencies visible. Comparative forecasting accuracy remains unresolved; no plan representation guarantees a delivery date. |
| L5 — Match test to claim | Retain distinctions; reject certainty | Qualified method; disputed stronger claim | [R01]–[R03] show different questions and limits. Informal convenience, numeric output and a fixed participant count do not remove methodological uncertainty. |
| L6 — Verify telemetry | Retain / qualify | Qualified method | [R03] treats behaviour metrics as proxies. Session/data integrity remains necessary but cannot establish enjoyment, interpretation or causation by itself. |
| L7 — Build, combinations and bug state | Strengthen | Qualified method | Isolation guidance [R16], explicit exports [R21] and distribution conditions [R17] extend the evidence boundary. Milestone labels remain project-specific. |
| L8 — Late change and release impact | Retain / adapt | Qualified method | Build branches [R17] provide a concrete update-testing path. A small edit can need broad affected-case checks; coordinated repair is allowed when justified. |

The rejection set is narrow and explicit: universal sample sufficiency; automatic experience/access certification from metrics or automation; always-more feedback/instruction; mandatory paper-first or prototype-code disposal; absolute independence from modularity; and milestone cutoffs that suppress material contrary evidence. None becomes a core rule. No selected book is removed because one claim is qualified.

## 4. Evaluation model: what each kind of evidence can establish

This table is the project's synthesis for later evaluation design. It preserves all eight charter quality dimensions: formal correctness, systems/balance, human experience, accessibility, content integration, performance, preservation and reproducible installation/execution. These dimensions cannot be averaged into one score that hides a critical blocker.

| Evidence class | Appropriate question and future artefact | Inference limit / repair when inadequate |
|---|---|---|
| Formal rule or static content check | Does a declared transition, prerequisite, reference or invariant hold in the represented cases? Retain assertions and offending state/content identifiers. | An unrepresented rule or unchecked data path remains unknown. Correct the rule, checker or content according to cause; compilation alone is insufficient. |
| Bounded model / strategy simulation | What happens under stated resource flows, strategies, parameters and seeds? Retain assumptions and scenario traces. | Coverage of scripted agents is not coverage of people. Challenge assumptions and extreme cases before changing the real game. |
| Integrated runtime check | Does the identified build perform the required action, consequence, outcome and reset under specified conditions? Retain reproduction and actual result. | A component passing does not establish its combinations. A headless run cannot answer an unobserved visual question. |
| Human observation and account | What did relevant participants do, understand or report? Retain task, prior experience, assistance and conditions. | First use, repeat mastery and facilitated discussion require different interpretation. Missing recruitment or intervention information limits the conclusion. |
| Comparative experiment | Did a specified change alter a defined outcome under the design's allocation and analysis assumptions? Retain condition identity and uncertainty. | Group differences, repeat exposure and metric choice can constrain causality/generalisation. Required sample planning belongs to the actual question. |
| Accessibility inspection and use | Can the declared critical tasks be completed under relevant access conditions? Retain barriers, alternatives and participant evidence where claimed. | Coverage of one impairment, device or task does not cover combinations or the entire experience. Recheck the task chain after repair. |
| Performance / latency capture | What workload was measured, where, on which build/device and across which events? Retain individual/problematic intervals as well as summaries. | Component timing, average frame rate and end-to-end response answer different questions. Reproduce the relevant spike or delay before accepting a change. |
| Consumer delivery / preservation check | Can a fresh consumer obtain and run the intended candidate, and does corrected play preserve accepted behaviour? Retain version, prerequisites, changed cases and unresolved findings. | A developer machine or account can conceal dependencies. Runtime game delivery and clean installation of this future skill package require separate proofs. |

A later evidence record should make the claim, build/configuration, setup, relevant population or input cases, expected/actual behaviour, intervention, limitation and resulting decision recoverable. This is a domain requirement, not a selected schema. Invalid evidence must be corrected or narrowed before it closes a finding. A failed test can be valuable evidence; an unexecuted test plan cannot be reported as a result.

## 5. Failure taxonomy and smallest-sufficient repair

These **21 original diagnostic descriptions** instantiate the bootstrap's required failure set using the books and practice map. They are proposed future checks, not observed defects in an existing game. Symptoms can share a cause; severity depends on the required task, frequency, recovery and affected players. “Smallest sufficient” concerns the causal scope, not the number of edited lines.

| ID / failure | Distinguishing symptom and evidence to seek | Initial repair scope and affected recheck | Capability |
|---|---|---|---|
| D01 — Unclear player goal | A relevant player cannot infer a useful next action; distinguish absent purpose from an intentionally open goal. | Clarify the implicated objective/cue or available choice; re-observe without the prior explanation. | P01, P07, P08 |
| D02 — Weak core loop | Repeated actions technically resolve but produce no intended decision, tension or motivation. Inspect incentives and accounts, not feature count. | Revise the responsible choice, cost or consequence; replay the loop before expanding content. | P01, P02, P04 |
| D03 — Unresponsive controls | Valid attempts are ignored, inconsistently accepted or mapped unexpectedly at a state boundary. Capture input and adjudication. | Correct mapping, focus, buffering or state eligibility as diagnosed; recheck neighbouring actions and remapped input. | P02, P05, P09 |
| D04 — Poor feedback | A consequence occurs but its relevant meaning is missing, misleading or masked. Compare the event with what players can perceive. | Change the implicated cue/timing/channel; recheck recognition under actual viewing/listening conditions. | P05, P09 |
| D05 — Unreadable combat | Threat, counter or hit outcome cannot be distinguished amid competing cues. Capture the encounter from the player's view. | Correct cue hierarchy, hit/cue alignment or encounter overlap; preserve intended challenge and re-observe response. | P05, P07 |
| D06 — Soft lock | The game remains active, but required progress and recovery are unavailable. Preserve the exact state and action history. | Repair the missing transition, reset or recovery route; repeat the failing sequence and nearby paths. | P02, P11, P15 when persistent |
| D07 — Unreachable content | A required object, route or trigger cannot be reached with permitted movement/interactions. | Correct placement, clearance, collision or access condition; retest actual traversal and dependent content. | P06, P11 |
| D08 — Dominant strategy | One strategy invalidates intended alternatives under the relevant conditions. High selection rate alone does not prove dominance. | Inspect costs, information and counterplay; change the responsible interaction and examine viable alternatives. | P04, P08 |
| D09 — Trivial strategy | A low-engagement tactic bypasses the intended challenge, even if it is not best in every situation. | Decide whether the discovery is desirable; if not, repair its enabling rule while preserving legitimate creative play. | P01, P04 |
| D10 — Progression dead end | Prerequisite order, a consumed item or a branch prevents required later progress. Trace access dependencies and retained state. | Repair the dependency or supported recovery; replay relevant orders, branches and save/load boundaries. | P02, P04, P06, P15 |
| D11 — Economy runaway / collapse | Resources compound uncontrollably or cannot sustain required play under a reproducible scenario. | Correct the responsible source, sink, conversion or feedback interaction; inspect other strategies and time horizons. | P04, P11 |
| D12 — Difficulty spike | A particular encounter or transition produces an unintended jump for the relevant cohort. Inspect prior learning, resources and information. | Adjust the identified challenge, preparation or cue; retest earlier learning and subsequent progression. | P04, P07, P08 |
| D13 — Unfair information asymmetry | A player or agent has information contrary to the intended rules, or a counter requires unavailable knowledge. | Repair information exposure, agent knowledge or communicated rules; preserve intentional hidden-information play. | P02, P07, P14, P16 when online |
| D14 — Level flow failure | Routes cause unintended disorientation, backtracking or broken pacing despite being reachable. | Change the implicated connection, landmark or encounter sequence; test navigation from the normal viewpoint. | P06, P07 |
| D15 — AI deadlock / exploit | An agent oscillates, stalls on an invalid target or follows a repeatably exploitable decision. Inspect choice, path and motor separately. | Correct preconditions, fallback, interruption or locomotion at the responsible layer; replay target loss and relevant transitions. | P14, P11 |
| D16 — Physics instability | Objects tunnel, explode, jitter or diverge under a known load/configuration. Capture timing and contact conditions. | Repair solver/update assumptions, collision or integration settings; test stressed conditions without silently changing intended motion. | P02, P05, P12 |
| D17 — Save-state corruption | Restored values or relationships are invalid, duplicated, incompatible or lose required progress. Preserve the original failing save. | Repair serialisation/reconstruction or provide a declared recovery/migration path; check restart and affected progress without overwriting the only evidence. | P15, P11 |
| D18 — Network desynchronisation | Peers disagree on authoritative outcome/state beyond the declared reconciliation policy. Preserve version, input/message and timing conditions. | Correct the implicated authority, ordering, simulation or reconciliation behaviour; repeat under impaired delivery and reconnect conditions. | P16, P11 |
| D19 — Performance spike | A reproducible workload stalls or exceeds its declared target condition despite acceptable averages. | Localise expensive work or overload; remeasure the affected build/target and confirm the repair preserves play. | P12, P11 |
| D20 — Input latency | An accepted input has excessive or variable delay before its relevant visible consequence. Identify measurement endpoints. | Correct the responsible input/simulation/render/presentation segment; remeasure and evaluate the intended task, not only average frame rate. | P05, P12 |
| D21 — Accessibility blocker | A required task is unavailable or unreasonably obstructed under an intended access condition. Inspect setup and configuration as well as play. | Provide a workable alternative or remove the barrier; retest the task chain and related needs with scoped evidence. | P09 and affected owner |

Intentional loss, hidden information, unequal abilities, low difficulty, randomness or unexpected player invention are not automatically defects. Classification requires the intended rules and experience. A repair closes the identified issue only when its replacement evidence covers the defect and affected accepted behaviour; other findings remain open.

## 6. Evidence-qualified capability model

### 6.1 Retained responsibilities and additions

P01–P13 retain their identities. The rows below revise their evidence conditions and add P14–P16 where research revealed distinct responsibilities. K1–K9 retain the [Stage 1A coverage meanings](2026-09-12-stage-01a-knowledge-coverage-and-five-book-corpus.md#3-knowledge-coverage-map). This is **16 responsibility descriptions**, not a sixteen-skill architecture or a claim of equal research depth.

| Capability / coverage | Owned input, decision and output | Evidence qualification and future acceptance obligation |
|---|---|---|
| P01 — Frame an experience hypothesis; K1 | From audience, brief and constraints, choose an intended activity/experience and observable question. Produce a reasoned hypothesis with alternatives. | F1/M7/L1 qualified. Compare relevant player choices/accounts with intent; external-effect claims require separate evidence. |
| P02 — Specify actionable mechanics; K2 | From verbs and rules, define allowed actions, state/data, timing, consequences and reset. Produce implementable behaviour examples. | F2/M1/S3 retained. Verify normal, unavailable and boundary behaviour in the selected execution path; assumptions about simulation time must be explicit. |
| P03 — Select adequate proof; K3/K6 | From uncertainty and cost, choose paper, model, simulation, runnable proof or a suitable combination. Produce a question-led experiment with omissions. | F3/S1/T1/L1/L2 qualified. Show that the representation can answer the question; no mandatory fidelity sequence. |
| P04 — Analyse systems and balance; K2/K5 | From rules, resources, goals and strategy assumptions, identify feedback and cases; produce model findings and proposed tuning. | F6/M2–M4 bounded. Check assumptions, alternatives and actual play separately. For live work, retain cohort/configuration identity and examine unintended effects. |
| P05 — Tune controls and feedback; K3 | From action intent, device, state and information needs, choose mapping, response and cues. Produce a tuned interaction and scoped evidence. | S2/S3/S5/S6 qualified. Measure the relevant events and observe task interpretation; historical numeric thresholds remain unadopted. |
| P06 — Integrate spatial play and content; K4 | From task structure, movement/camera metrics and asset requirements, choose layout and integration conditions. Produce playable content and a handoff record. | M5/M6/S4/T1–T4 retained with R13/R24 extensions. Verify references, imports, collision, routes and cues after replacement/reimport. |
| P07 — Compose learnable encounters; K1/K4/K5 | From audience knowledge, available actions and intended challenge, choose information, sequence and recovery. Produce an encounter/onboarding hypothesis. | T5/T6/M5/F4 qualified. Use appropriate first-use or mastery evidence; more instruction and survival analogies are not universal solutions. |
| P08 — Design and interpret evaluation; K5 | From a claim, select methods, participants/cases and instrumentation. Produce observations/results with explicit limits and a supported decision. | F4/F5/M4/L5/L6 qualified. Verify collection; separate formal, experiential and causal claims. No fixed sample quota closes all questions. |
| P09 — Integrate baseline accessibility; K7 | From critical tasks and relevant needs, choose input/presentation alternatives and configuration access. Produce requirements, barrier findings and repairs. | Charter remains core; R09–R11 deepen F7. Evaluate relevant task chains and overlapping needs; guidance inspection is not whole-game certification. |
| P10 — Scope and integrate deliverable increments; K6 | From demonstrated work, dependencies and commitments, choose the next coherent scope/fidelity. Produce a revisable plan and accepted increment. | L2–L4/T2 qualified. Include integration, testing and rework; evidence supports a bounded commitment, not guaranteed dates. |
| P11 — Diagnose, repair and preserve accepted play; K2/K6 | From a reproducible finding and accepted conditions, identify cause and affected work. Produce the smallest sufficient authorised correction. | F5/F6/S6/L7/L8 strengthened by R13/R16. Verify the defect and affected behaviour; distinguish accepted exceptions from verified fixes. |
| P12 — Establish playable delivery readiness; K8 | From a candidate, target and quality requirements, decide what evidence supports delivery. Produce identified build/run/profile and consumer-path findings. | L4/L7/L8 strengthened by R14/R17/R21. Actual built execution, clean skill consumption and target profiling are separate, still unperformed obligations. |
| P13 — Constrain procedural and emergent content; K2/K9 | From construction, placement and progression rules, select reproducible cases and invariants. Produce constraint and integrated-play findings. | M3/M6/T7 remain specialist and bounded; R13 complements them. Verify after placement, preserve failing seeds and retain human experience questions. |
| P14 — Integrate and diagnose gameplay AI/navigation; K2/K4/K9 | From agent knowledge, goals and actions, define decision/execution and movement conditions. Produce inspectable behaviour and a failure explanation. | **Added**, grounded in R12/R19. Future proof must cover invalid targets, blocked movement, fallback and permitted information. One AI architecture does not establish general support. |
| P15 — Preserve and recover persistent play state; K2/K6/K8 | From progression and portability requirements, define retained state, relationships and recovery expectations. Produce restoration rules and identified compatibility limits. | **Added**, grounded in R15/R22. Restart/load, incompatible data and interrupted writes need implementation-specific evidence; migration and conflict policy remain open. |
| P16 — Integrate networked simulation and sessions; K2/K8/K9 | From multiplayer rules and topology, define authority, state/time assumptions and session lifecycle. Produce a synchronisation and recovery hypothesis. | **Added**, grounded in R20/R23. Requires concrete multi-peer and impaired-network evidence later; no multiplayer path is currently demonstrated or required for the first proof. |

P15 applies when the game promises persistent progress, including local single-player games; reset alone does not imply a save system is needed. P14 applies when autonomous agents/navigation are part of play. P13 and P16 remain specialist directions. Live tuning is an operating context spanning P04/P08/P10–P12, so it does not need a separate capability identity at this stage.

### 6.2 Deterministic, generative, judgement-heavy and tool-dependent work

| Kind of work | Suitable responsibility and limit |
|---|---|
| Deterministic within declared assumptions | Rule assertions, arithmetic, reference checks and reproduction scripts can have definite outcomes. Global determinism is not presumed; timing, seeds, engine/platform behaviour and network architecture can change the assumption. |
| Generative / exploratory | Candidate mechanics, layouts, encounters and parameter scenarios can be proposed or generated. Construction success requires subsequent constraint and play evaluation; novelty is not a quality certificate. |
| Judgement-heavy | Selecting the experience, interpreting player evidence, accepting a strategy, trading challenge against access and committing scope need reasoned contextual decisions. Automation can inform these decisions without supplying their value judgement. |
| Tool-dependent | Imports, collision, navigation, profiling, exports, persistent storage and network transport require a declared implementation path and real execution. Durable responsibilities survive an engine change; API behaviour and operational proof do not transfer automatically. |

### 6.3 Candidate evaluation consequences

The Stage 1B candidates **BC01–BC13 remain unexecuted** and keep their identities. The qualifications above govern their interpretation. In particular, BC05 needs event-level response evidence, BC08 cannot claim unaided success after assistance, BC09 needs relevant access conditions, and BC12 needs both the built game and clean consumer path. These are clarifications, not a selected benchmark suite.

Three additional original fixtures make the new responsibilities reviewable:

| Candidate | Proposed failure situation | Evidence a future implementation would need |
|---|---|---|
| BC14 / P14 | An ally selects a target that disappears while approaching; repeated reselection prevents useful action. | Preserve decision and movement traces; identify invalidation/fallback cause; show recovery without breaking the declared commitment rules of other actions. |
| BC15 / P15 | A saved key/door state restores the key but leaves a dependent object missing; another save is interrupted. | Preserve failing data; distinguish reconstruction from write/recovery failure; demonstrate the declared restore/recovery policy and affected progression. |
| BC16 / P16 | Two peers duplicate a reward after a repeated message; one disconnects during resolution. | Identify authority and message/session conditions; show the intended single outcome and declared recovery under replayed delivery failures. Exact equality is required only where the architecture says so. |

Performance spikes, reimport damage and competing combat cues should also inform later case selection through D19, D07/D04 and D05. The later evaluation stage must choose executable fixtures and defensible thresholds; this log invents no measured pass rate or capability result.

## 7. Coverage gaps, unresolved questions and bounded use

Every Stage 1B queue item G01–G10 was revisited. “Addressed for the domain model” means the responsibility and its limits are explicit. It does not mean implementation, all-genre coverage or all empirical questions are complete.

| Gap | Investigation and change in this stage | Remaining boundary and trigger for further work |
|---|---|---|
| G01 — Research validity | R01–R03 challenge sample sufficiency, uniform tutorial effects and overinterpretation of metrics. P08 now separates evidence classes explicitly. | Detailed recruitment/sample planning, think-aloud effects and repeat-exposure controls require the actual claim and population. Resolve before asserting those study outcomes. |
| G02 — Accessibility | R09–R11 supply specialist scope, input and information-channel requirements. P09 is strengthened beyond introductory book treatment. | Cognitive, speech, haptic, timing and intersecting needs were not comprehensively reviewed. Select further relevant guidance and participants once critical tasks/devices are known; do not claim complete coverage. |
| G03 — Responsiveness / performance | R07/R14/R18 establish distinct timing and measurement responsibilities, including the target/build context. | No universal perceptual threshold has been validated. Investigate the chosen task/device and measure an actual build before setting or accepting budgets. |
| G04 — Reproducible content and execution | R13/R16/R17/R21/R24 add static constraints, isolation, export/import and distribution conditions. P06/P11/P12 become more concrete. | Clean installation of the eventual skill package remains a separate required proof. Engine/version, dependencies, package path and target cases are deliberately not selected here. |
| G05 — Coupled mechanics / economy / progression | R05 adds live-balance limitations; R12 shows coordinated multi-use abilities; R13 supplies content checks. P04/P11 preserve causal and affected-case reasoning. | Long-running economy validity, broad strategy exploration and automated progression coverage remain incomplete. Bounded models are usable as investigations; broader support needs representative cases. |
| G06 — Small-team and atypical production | R04 supplies a contrasting producer's slice framing; R08 supplies a cheap spatial iteration workflow. Absolute finish, disposal and forecast rules are qualified. | No comparative study establishes an optimal solo-team process. Adapt to actual uncertainty and demonstrated work; revisit before claiming efficiency across team/game forms. |
| G07 — Meaning / external effects | Reassessed M7 against evidence-class boundaries; R03 illustrates limits even for measured in-game outcomes. Interpretive design analysis remains permitted. | No dedicated learning-transfer or real-world-behaviour evidence was established. Exclude efficacy claims unless a later task supplies appropriate domain evidence and study design. |
| G08 — Broader forms and platforms | R12/R19/R20/R23 expose AI, navigation and online responsibilities; R15/R22 expose persistence; R13 includes a simulation-game content case. | This does not establish narrative, turn-based, mobile, console or XR execution. Those paths need their own representative workflow and evidence before a support claim. First proof stays bounded local single-player. |
| G09 — Camera / cues / onboarding / spatial risk | R03/R06/R08/R11 supply contrasting study, combat, blockout and access perspectives. T5 is qualified; T6 remains a contextual heuristic. | No universal camera choice, optimal instruction dose or survival-based spatial law is adopted. Test the chosen encounter, ability and viewpoint; broader empirical claims remain excluded. |
| G10 — Late changes / delivery | R16/R17/R21 add concrete test, build and distribution responsibilities; the charter still owns material exceptions and publication authority. | Detailed platform certification, production incident response, rollback operations and specialist obligations require their actual platform/owner. They are not inferred from milestone names or historical accounts. |

The new P15 gap is particularly concrete: serialisation and cloud replication documentation does not settle crash-safe writes, schema migration, conflict resolution or acceptable loss of progress. P16 similarly does not settle prediction/reconciliation, matchmaking, anti-cheat or service operation. These are conditional expansion questions, not hidden promises in a generic “save” or “multiplayer” capability.

## 8. Completion evidence and next handoff

| Stage 2 exit requirement | Durable evidence in this record |
|---|---|
| Study professional practice independently of the books | Section 2 maps specialist responsibilities and artefacts; R01–R24 include primary studies, production accounts and current implementation guidance. |
| Challenge material book-derived claims | Section 3 gives separate decisions and evidential standing for all 35 finding IDs, including contrary results, dependence and rejected extrapolations. |
| Investigate important missing responsibilities | Sections 2 and 6 extend accessibility, content, QA, runtime and delivery work and add P14–P16; Section 7 bounds incomplete depth. |
| Explain uncertainty reduction, commitments and integration | Section 2.3 identifies decisions, outputs and return paths under the existing charter authority. |
| Evaluate playability and repair without overclaiming | Sections 4–5 separate evidence classes and cover all 21 required failure modes with diagnostic and repair scopes. |
| Produce an evidence-qualified domain model | Section 6 preserves P01–P13, adds three responsibilities and distinguishes types of work; no row claims implementation. |
| Keep unresolved claims out of unconditional core rules | Section 7 dispositions every G01–G10 gap and the new persistence/networking limits. |

**Stage 2 is complete as research.** The companion source register and this log are the authoritative handoff; the prior books and extraction remain available for precise source context. The research-log index advances to **Stage 3: define the player experience and game thesis model**. That stage should consume P01/P02/P07/P08, the evidence-class distinctions and the bounded claims here when defining a concise representation. No Stage 3 model or contract is authored in this commit.

[R01]: https://www.jpattonassociates.com/wp-content/uploads/2015/04/rite_method.pdf
[R02]: https://link.springer.com/content/pdf/10.3758/BF03195514.pdf
[R03]: https://grail.cs.washington.edu/projects/game-abtesting/chi2012/chi2012.pdf
[R04]: https://ltpf.ramiismail.com/prototypes-and-vertical-slice/
[R05]: https://www.leagueoflegends.com/en-us/news/dev/dev-balance-framework-update/
[R06]: https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/
[R07]: https://gafferongames.com/post/fix_your_timestep/
[R08]: https://book.leveldesignbook.com/process/blockout
[R09]: https://learn.microsoft.com/en-us/xbox/accessibility/guidelines
[R10]: https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107
[R11]: https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103
[R12]: https://www.gameaipro.com/GameAIPro3/GameAIPro3_Chapter31_Behavior_Decision_System_Dragon_Age_Inquisition%E2%80%99s_Utility_Scoring_Architecture.pdf
[R13]: https://www.gameaipro.com/GameAIPro3/GameAIPro3_Chapter42_Building_Custom_Static_Checkers_Using_Declarative_Programming.pdf
[R14]: https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-collect-data-introduction.html
[R15]: https://docs.godotengine.org/en/stable/tutorials/io/saving_games.html
[R16]: https://dev.epicgames.com/documentation/en-us/unreal-engine/automation-test-framework-in-unreal-engine
[R17]: https://partner.steamgames.com/doc/store/testing
[R18]: https://www.nvidia.com/en-us/geforce/guides/gfecnt/202010/system-latency-optimization-guide/
[R19]: https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_using_navigationagents.html
[R20]: https://gafferongames.com/post/deterministic_lockstep/
[R21]: https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html
[R22]: https://partner.steamgames.com/doc/features/cloud
[R23]: https://docs.godotengine.org/en/stable/tutorials/networking/high_level_multiplayer.html
[R24]: https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/import_configuration.html
