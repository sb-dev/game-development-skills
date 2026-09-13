# Gameplay Behaviour and Systems Contract

**Version:** 1.0  
**Defined by:** [Stage 4 research and verification](../research-logs/2026-09-13-stage-04-mechanics-rules-systems-and-state.md)  
**Upstream:** [Game Thesis Contract](game-thesis.md)

## 1. The distinctions the model preserves

Use the smallest representation that explains the behaviour and its dependencies. These are related concepts, not thirteen required files or runtime classes.

| Concept | Meaning in this model | Distinction that matters for diagnosis |
|---|---|---|
| Player verb | An action the player can intentionally request, such as wait, trade or aim. | The verb is not a particular key binding or proof the action was allowed. |
| Rule | A condition, transformation or constraint governing what may happen. | The rule can be correct on paper and implemented incorrectly. |
| Mechanic | An operative combination of rules, data and processes enabling an interaction. | One mechanic can serve several player purposes; not every mechanic needs its own subsystem. |
| Resource | A quantity with a unit, owner, bounds and rules for production, consumption, transfer or conversion. | A resource value is state; its source/sink rules explain how it changes. |
| Entity | An identifiable participant or object whose properties or lifetime matter to the rules. | Logical entities need not have a visible object or map directly to an engine class. |
| State | Values and relationships relevant to what can happen next, at a declared scope and time. | Distinguish authoritative values, derived presentation and durable progress. A complete whole-game graph is optional. |
| Feedback | Information expressing a relevant action, state or consequence to a player. | A correct state change with a misleading cue is a feedback/integration failure. |
| System | A bounded set of interacting mechanics, resources and entities serving a gameplay responsibility. | System boundaries aid reasoning but do not guarantee independent effects. |
| Loop | A repeated action/consequence sequence, or a feedback cycle that changes later behaviour. | Distinguish the player's activity loop from an economy's reinforcing/stabilising feedback. |
| Progression | Changes in access, capability, challenge or persistent accomplishment over play. | Ordered mission steps, spatial reachability and saved progress are related but distinct. |
| Win / fail conditions | Predicates or decisions resolving an outcome, with continuation/reset implications. | Declare absent outcomes for open-ended play; avoid inventing a terminal state. |
| Encounter | A bounded situation combining player capabilities, other agents/systems, information and relevant space/content. | Encounters may be non-spatial; a valid asset or mechanic alone does not establish the encounter. |
| System interaction | A dependency through shared state, events, resources, timing, information or space. | Correct local rules can produce a harmful combined dynamic. Diagnose the relationship when that is where the defect arises. |

## 2. Three first-class records

The model has three independently identifiable records: the existing **thesis**, a **behaviour definition**, and a **system/encounter composition**. Split a record when it has an independent decision, consumer, validation or repair scope; keep small related rules together otherwise. One Markdown file may contain several identified records. Candidate folders such as `mechanics/`, `state-models/` or `balance/` are not mandatory.

Findings, run evidence and decisions are referenced inputs/outputs whose detailed contracts belong to their owning stages. This contract does not introduce a separate evidence database or duplicate those records.

### 2.1 Lifecycle and ownership

Every instance supplies or references the following eleven properties. A role below may be carried by the same person as another role; references must resolve within the consuming project's available material.

| Property | Thesis | Behaviour definition | System/encounter composition |
|---|---|---|---|
| Creator | Designer with designated project owner | Gameplay/technical designer with implementation collaborator as needed | Systems, level or encounter designer with participating owners |
| Purpose | State intended activity/experience and bounded commitment | Make a local interaction implementable and inspectable | Explain combined behaviour, dependencies and systemic uncertainty |
| Consumers | Prototype, mechanics, content and evaluation work | Runtime implementer, content integrator, system designer and evaluator | Integrators, balancing/encounter work, evaluation and delivery review |
| Source evidence | Brief, research, constraints and prior findings | Exact thesis revision, relevant source findings and observed defect if any | Exact member revisions, integration conditions, strategy hypotheses and prior findings |
| Decisions preserved | Accepted direction, scope and constraints | Accepted rule semantics, parameter ranges, input/feedback and state requirements | Accepted dependencies, progression, placement, information and interaction constraints |
| Status / confidence | Draft/accepted/rejected/superseded plus evidence limitations | Decision status separately from specified/implemented/verified evidence state and tested conditions | Decision status separately from modelled/integrated/evaluated evidence state and coverage limits |
| Approval behaviour | Existing thesis acceptance/reopen rules | Existing authority covers routine work/range tuning; material semantic change needs the designated owner | A change to accepted interactions or dependent content needs affected-owner review under project authority |
| Runtime expression | Constrains the chosen game/prototype; has no required runtime class | Rule code, data, script, controller, event or engine configuration, identified when implemented | Concrete scene/configuration, system wiring or simulation setup, identified when implemented |
| Validation method | Thesis review and evidence appropriate to its claims | Rule/state/boundary checks, runtime comparison and relevant input/feedback observation | Combined scenarios, flows, progression/recovery and scoped human play where experience is claimed |
| Repair scope | Implicated premise or constraint, with explicit reopening | Responsible rule, value, transition, binding or feedback relationship | Responsible interaction, dependency, placement or schedule; coordinate member changes when required |
| Downstream impact | Identify affected prototypes, mechanics, content and evidence | List consuming systems, controls, cues, content, saves/network state and relevant tests | List affected encounters, progression, content, strategy evidence, target conditions and delivery checks |

“Accepted”, “implemented” and “verified” are different statements. Preserve identities/revisions and evidence conditions instead of treating a status word as proof. A current record may link an accepted baseline and a proposed replacement, but only the selected version governs its declared scope.

## 3. Behaviour definition

Use this form or equivalent project-native fields. Omit an inapplicable detail with a reason; do not omit behaviour necessary to adjudicate the current action.

```markdown
# <behaviour ID>@<revision>: <name>
Purpose / thesis: <intended activity and exact upstream revision>
Creator / consumers: <roles and affected records>
Decision status / authority: <status and instruction/decision reference>
Evidence state: <what has actually been specified, run or verified; limitations>
Sources / preserved decisions: <references, constraints and permitted ranges>

## State and participation
<Entities, identity/lifetime, state ownership, resource units/bounds,
initial values or unresolved parameters, derived values and invariants.
Identify what resets, persists or belongs to another owner.>

## Action and rules
<Player/system trigger; input-to-verb mapping where relevant; preconditions;
state/resource effects; unavailable/invalid action; feedback;
outcome, interruption, cancellation and retry/reset behaviour.>

| Trigger / prior condition | Allowed result and state/resource change | Feedback / unavailable result |
|---|---|---|
| <case> | <effect or declared no-op> | <what the player can perceive> |

## Time, parameters and dependencies
<Turn/event/update basis, ordering/tie policy where material, durations/units,
continuous response/reference frame where applicable, accepted tuning ranges,
randomness assumptions and dependencies. Mark unresolved conflicts.>

## Runtime, validation and repair
<Implementation expression/revision or explicitly unimplemented;
normal, invalid, boundary and reset checks with expected results;
relevant human question; responsible repair unit and affected consumers.>
```

A state table represents only its declared scope. If two events can compete, specify the relevant order, simultaneous resolution or priority instead of relying on undocumented engine order. Repeated inputs, unavailable actions, target loss and interruptions need a declared result when they affect the mechanic. A curve or equation may describe continuous motion more clearly than enumerating states.

Resources state their unit and time basis; the same number cannot silently mean per frame, per second and per turn. Feedback describes meaning and availability rather than commissioning a final asset. Randomness needs its relevant distribution/seed assumptions for reproduction, without imposing global determinism. Save and network ownership are explicit when applicable, not default dependencies for every mechanic.

## 4. System and encounter composition

```markdown
# <system ID>@<revision>: <name and bounded responsibility>
Creator / consumers: <participating owners and affected records>
Thesis / sources / preserved decisions: <exact references and constraints>
Decision status / authority: <accepted or proposed scope and owner>
Evidence state: <modelled, integrated or evaluated; actual evidence and limits>

## Members and relationships
<Member behaviour revisions, entities/resources/state owners, shared events,
ordering, information, spatial/content dependencies and interfaces.>

## Loops, progression and scenarios
<Player activity loop; resource sources/sinks/conversions and feedback;
prerequisites/access changes; success/fail/continuation/reset;
encounter conditions, strategies, expected dynamics and counterexamples.>

## Runtime, evaluation and repair
<Concrete composition or explicitly unimplemented model; invariant and
interaction checks; bounded simulation assumptions and termination;
integrated/human evidence questions; suspected responsible relationships,
candidate repair scopes and downstream impact.>
```

Describe both a normal sequence and a plausible adverse combination. For an economy, distinguish the movement of resources from conditions controlling that movement. For progression, inspect dependencies after content/agent placement, not only an abstract task graph. For an encounter, include the coupled conditions necessary to expose the question: player capability, other behaviour, information and relevant space/content timing.

Models must declare omitted strategies, time horizons and variables. Successful arithmetic or construction does not establish balanced or enjoyable play. Unexpected play is a finding to interpret against the thesis; it is not automatically an exploit to remove.

## 5. Dependency and repair reasoning

Preserve these two relationships, using local references rather than requiring a global graph service:

1. **Player goal → verb → rule → feedback → resulting dynamic → playtest observation → tuning decision.** Early links can be specified or modelled; the observation link stays unperformed until evidence exists. A tuning decision cites the finding, affected revision and authority.
2. **Resource source → resource sink → progression pressure → player strategy → economy result.** Trace rates, quantities and controls; identify where an assumed human strategy is merely a script/model. Missing or zero-cost sinks may interact with other rules even when local arithmetic passes.

For a systemic failure:

1. Preserve the build/model, member versions, starting state, input/event sequence and relevant seed/timing/target conditions. If those are unknown, narrow the claim first.
2. Compare expected and actual behaviour along the dependency chain. Separate an ambiguous requirement, implementation defect, invalid data/content, feedback failure, interaction failure and invalid evidence collection.
3. Identify the earliest unsupported or violated relationship that explains the symptom. Do not assume the earliest event is the cause or change every related subsystem.
4. Propose the smallest sufficient correction and list affected accepted conditions. Multiple coordinated edits may be necessary; a one-line tuning change can still have broad consequences.
5. Use existing authority or obtain the required reopen decision. Recheck the failing case and affected consumers with the appropriate evidence; preserve useful behaviour and report remaining limits.

If a rule table and runtime disagree, fix the responsible implementation unless an authorised design change is needed. If the rules themselves create an unwanted dynamic, propose a rule/interaction change. If play is correct but the cue is wrong, repair the cue or integration. If the intended outcome is ambiguous, obtain the missing decision; do not silently tune away the ambiguity.
