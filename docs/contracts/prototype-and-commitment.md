# Prototype, Fidelity and Commitment Contract

**Version:** 1.0  
**Defined by:** [Stage 5 research and verification](../research-logs/2026-09-13-stage-05-prototype-fidelity-and-commitment.md)  
**Inputs:** [Game thesis](game-thesis.md), [behaviour/system definitions](gameplay-behaviour.md), accepted constraints and the finding or uncertainty being investigated.

## 1. Choose for the question

Choose the least costly representation that preserves the variables and conditions needed to answer the current question. Adequacy comes before cost. A low-cost artefact that omits the disputed behaviour is not an experiment for that claim.

1. Name the uncertain claim, its consequence for a decision and the evidence kind it needs.
2. Identify behaviour, dependencies, information, participants and target conditions that must be represented. Distinguish required fidelity from unrelated finish.
3. Compare plausible representations. Reject those unable to reveal a meaningful contrary result. State omissions and the claims those omissions prevent.
4. Among adequate options, compare creation/change effort, integration, evidence collection, prerequisites, external spend, reuse and the cost of undoing the choice. Use observed effort when available; label estimates and unknowns. No universal weighted score or fixed hour budget is required.
5. Choose the next bounded proof within existing authority. Execute it when the production task calls for execution, then record actual results and limitations. Decide whether to retain, repair, reject, investigate again or propose a larger commitment.

An experiment plan or selection decision is not its execution result. Missing required participants, runtime or target access blocks the affected proof; it does not license a weaker claim. Apply the project's stop rules whenever a blocker requires input. Separate mechanical work is permissible only when those rules and existing authority allow it, and cannot substitute for the blocked proof.

## 2. Uncertainty-to-evidence map

These are starting hypotheses, not automatic choices. Include coupled conditions when they are necessary to evaluate the question.

| Uncertainty | Cheapest useful starting representation | Must preserve / adequacy limit |
|---|---|---|
| Core rule | Written rule examples or bounded state table | Preconditions, effects, invalid actions and outcomes; runtime correctness still needs execution. |
| Probability or economy | Spreadsheet, calculation or headless simulation | Units, distributions, flows, strategies and horizon; model outputs do not establish human balance. |
| Movement | Isolated controller sandbox | Relevant input, response, collision, viewpoint and representative spacing; a velocity constant alone is inadequate. |
| Combat timing | Small placeholder arena | Player/enemy actions, cue timing, hit consequences and required movement; final art is unnecessary unless its properties are the uncertainty. |
| Camera | Dedicated camera sandbox | Player motion, occlusion, framing, geometry and input coupling; a static screenshot cannot establish motion behaviour. |
| AI behaviour | Isolated encounter with inspectable state | Knowledge, decisions, targets, execution and movement dependencies; path selection alone does not prove agent movement. |
| Level flow | Greybox/blockout | Actual player movement, routes, information and relevant encounters; editor flight cannot substitute for play. |
| Progression | Dependency/data table and simulated sequences | Prerequisites, consumption, branches, reset/persistence and access changes; spatial/content effects need integrated checks. |
| Procedural generation | Generator with reproducible cases and reachability/constraint checks | Rules, seeds/configurations and post-placement constraints; generated assembly is not proof of good play. |
| Network behaviour | Minimal replicated/multi-peer proof with declared synthetic conditions | Authority, message/state timing, loss/delay, join/leave and relevant recovery; local single-runtime behaviour is insufficient. |
| Performance | Representative stress scene and target build | Relevant workload, build/device and measurement boundary; convenient editor timings cannot certify the target. |
| Player comprehension | Human playtest with minimal adequate content | Relevant participants, usable controls, essential cues and unassisted observation where claimed; minimal art must not remove the information being tested. |

## 3. Fidelity is a set of choices

Record the fidelity that matters across rules, input/timing, feedback, space/content, system combinations, production workflow and target runtime. An experiment can be precise in one dimension and rough in another. Audio, animation or visual timing belongs early when it carries the disputed information or sensation.

The bootstrap's possible ladder offers ten useful representations/contexts, not ten compulsory phases:

| Representation / context | Decision it can help inform |
|---|---|
| Written rule / state table | Are the local semantics and cases coherent? |
| Spreadsheet / headless simulation | What follows from specified quantities and strategies? |
| Isolated mechanic toy | Does the essential interaction merit further investigation? |
| Placeholder playable prototype | What happens across a bounded integrated play sequence? |
| Greybox / blockout | Does spatial arrangement support relevant play? |
| Representative encounter or level | Do significant combinations and content conditions work together? |
| Vertical slice | What selected gameplay, quality or production-readiness claim is actually represented? |
| Integrated content production | Can additional content preserve accepted play and practical production assumptions? |
| Target-platform build | Does the chosen runtime satisfy the relevant behaviour and quality conditions? |
| Release candidate | Does the identified distributable candidate meet its declared delivery conditions? |

A target constraint can require an early build; a later economy defect can return to a table. A representative slice may test repeatable production as well as play. Specify its claim, representative parts, temporary parts and observed work. A polished corner or concept movie supports only what was actually demonstrated; neither establishes unobserved runtime or production breadth.

Preserve experiment inputs, meaningful results, rejected alternatives and accepted decisions. Retain or replace prototype implementation according to its suitability and reuse cost; there is no blanket throwaway-code rule. A failed prototype can justify stopping or changing direction without being a production failure.

## 4. Commitment points and authority

A commitment increases cost, scope or downstream reliance on a decision. The eight candidate points below are **reviewable decisions when relevant**, not eight mandatory meetings or new permission prompts. Existing explicit authority remains valid. Cheap reversible work and tuning within accepted ranges proceed under that authority.

| Candidate commitment | Concrete evidence/decision before wider reliance | Material change that needs review beyond existing authority |
|---|---|---|
| Game thesis selected | Selected revision, alternatives, intended players/experience, constraints, available evidence and uncertainties | Different thesis, audience or material scope/constraint |
| Core mechanic accepted | Identified rule/runtime behaviour, relevant cases and remaining experience questions | Changed rule semantics or an accepted dependency |
| Control model accepted | Mapping/response, relevant devices, access conditions and scoped evidence | New control demands, unsupported device assumptions or out-of-range tuning |
| Core loop accepted | Integrated action/consequence/outcome/reset evidence and relevant player questions | Changed incentives, core activity or loop consequences |
| Representative level / encounter accepted | Actual coupled play, route/placement/cue conditions and known limitations | Layout, timing or content change affecting accepted play |
| Vertical slice accepted | Named representative claims, actual integration/production work, omissions and cost uncertainty | Treating unproved content types or production volume as already demonstrated |
| Content scope accepted | Coherent volume, dependencies, estimates/observed effort, integration and review/test work | Additional content, spend, delivery commitment or a cut that breaks dependencies |
| Release candidate accepted | Identified built/distributed candidate, relevant quality/recovery/target evidence and unresolved issues | Material waiver or publication outside existing release authority |

For a new material commitment, present the candidate and exact revisions, evidence and contrary findings, unresolved questions, cost/resource envelope, affected accepted work, alternatives and requested decision. The designated owner accepts, rejects or requests more evidence. Record authority, scope and permitted ranges. Acceptance does not convert unresolved quality claims into verified results.

When contrary evidence affects an accepted dependency, identify the finding, smallest proposed change, affected consumers and re-evaluation. Obtain the required reopen decision before changing that dependency. Avoid expanding approval to unrelated work. Publication, external spend and changes to accepted decisions retain the charter's authority rules.

## 5. Compact proof and decision record

Use a project-native record or a section in the relevant thesis/behaviour record. When kept separately, identify its creator, consumers and revision; retain the applicable lifecycle properties from the behaviour contract rather than leaving authority or downstream impact implicit.

```markdown
Identity / creator / consumers: <record revision and responsible/affected roles>
Question / decision: <uncertainty, claim kind and consequence>
Inputs: <thesis/behaviour/system revisions and accepted constraints>
Adequate representation: <choice; essential variables/conditions>
Alternatives / cost: <rejected options; effort, prerequisites, spend,
integration/review and reversibility; measured versus estimated>
Omissions: <what is absent and which conclusions remain unavailable>
Authority / bounds: <existing instruction or required owner decision>
Evidence plan: <cases/participants/target, observations and contrary result>
Actual result: <not run, or identified outputs/conditions/limitations>
Decision: <retain | repair | reject | further investigation | proposed commitment>
Preservation / impact: <accepted dependencies, retained evidence and next scope>
```

Do not automatically raise fidelity after a favourable result. Increase or change representation only because the next unresolved question, integration dependency or proposed commitment requires it.
