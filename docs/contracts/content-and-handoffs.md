# Levels, Content and Gameplay Handoffs

**Version:** 1.0  
**Defined by:** [Stage 6 research and verification](../research-logs/2026-09-13-stage-06-levels-content-and-handoffs.md)  
**Inputs:** [Thesis](game-thesis.md), [behaviour/system definitions](gameplay-behaviour.md), [proof/commitment strategy](prototype-and-commitment.md) and relevant accepted specialist work.

## 1. Ownership at the boundary

The producing discipline owns specialist content and its craft decisions. Game Development defines gameplay use, implements or directs the integration, and judges the resulting behaviour. Engineering owns general implementation quality. The project's designated owner resolves conflicts that affect accepted work or material commitments.

A producer's acceptance of an asset does not establish gameplay integration. A gameplay defect does not authorise replacing otherwise valid specialist work. Compare the delivered item, import/configuration, runtime behaviour and intended use before assigning correction.

Use versioned project-native agreements and direct references. No universal cross-domain asset graph, global tag vocabulary or shared runtime schema is required.

## 2. Game-native artefacts and their jobs

These fourteen concepts may be sections of a level/encounter composition or handoff record. Give an independent record identity only when its decision, owner, consumer or repair scope needs one. Carry the lifecycle properties from the behaviour contract, including source evidence, authority, runtime expression, validation and downstream impact.

| Artefact / concept | Minimum useful content and consumer | Gameplay acceptance question |
|---|---|---|
| Level brief | Thesis/behaviour revisions, player task, knowledge, movement/view assumptions, constraints and intended outcome; used by layout/content work | Does this level expose the intended task under its actual conditions? |
| Encounter brief | Player/agent capabilities, information, challenge, recovery, timing and relevant space/content; used by encounter integration | Do the interacting parts support the intended decision and outcome? |
| Flow map | Connections, choices, gates and information routes; used by level/progression work | Are intended alternatives and connections represented? Geometry still needs separate proof. |
| Critical path | Required dependency chain to an outcome, with permitted alternatives and recovery; used by progression/QA | Can required progress be completed under the declared state and placement? |
| Spawn / pacing plan | Activation conditions, positions, population/workload assumptions, order and reset/despawn; used by encounter/runtime work | Do actual arrivals and overlapping demands create the intended sequence? |
| Greybox | Changeable playable geometry tied to movement/camera/collision revisions; used for spatial investigation | Does actual traversal and information access work before detailed replacement? |
| Navigation constraints | Traversable classes, clearances, connections, dynamic obstacles and agent/motor assumptions; used by navigation/integration | Can the relevant actor reach and execute its action, not merely obtain a path? |
| Gameplay tags / sockets / interaction contracts | Local semantic names, required attachment points, event/state meanings and missing-reference behaviour; used by integration | Do references resolve to the intended object/action after import and composition? |
| Asset integration requirements | Source/version, units, axes, scale, pivots, formats, dependencies, import/customisation and intended use; used by producer/integrator | Does the delivered version retain the required properties in the consuming runtime? |
| Collision requirements | Gameplay shape, clearance, layers/filters, trigger versus blocking behaviour and dynamic changes; used by art/physics integration | Is required movement/contact adjudicated correctly with the accepted controller? |
| Animation gameplay requirements | State/clip intent, timing units/windows, markers, transitions, cancellation and movement ownership; used by animation/gameplay integration | Do motion, hit/action timing and state changes agree, including interruption? |
| Audio feedback requirements | Cue meaning, triggers, priority, repetition, spatial/mix states, transition/loop needs and non-audio alternatives; used by audio/runtime work | Is required information delivered at the relevant time without being masked or lost? |
| Narrative trigger requirements | Character/story intent, entry/exit conditions, variables/events, repeat/once rules, branches and continuity; used by narrative/gameplay integration | Does the intended story consequence occur in the correct gameplay state without duplication or an invalid branch? |
| Performance budgets | Relevant target/workload, units, constraints, measurement method and accepted trade-offs; used by producers/integrators | Does the integrated target meet the scoped budget while preserving required play? Unmeasured budgets remain targets. |

Non-spatial games can omit greybox or navigation work with a reason; they still require meaningful state, information, outcome and content integration. Exact dimensions, timing windows, budgets and names belong to the consuming game. No example number is a reusable default.

## 3. Delivery, integration and correction by discipline

| Handoff | Producer must deliver or explicitly identify | Game Development adds and checks | Correction ownership |
|---|---|---|---|
| Narrative → character/story intent → gameplay | Accepted role/intent and content revision; available branches, variables/tags/events and dependencies; intended entry, consequence and continuity constraints | Bind to gameplay roles/states/triggers; present choices; handle repeat, interruption, reset/save continuity and unavailable content as applicable | Wrong game binding/trigger/continuity belongs to gameplay integration. Contradictory story logic or missing agreed content returns to Narrative. Changes to accepted intent need owner review. |
| Environment/3D → runtime-ready asset → playable space | Source/export revision, units/axes/scale/pivot, required visual/structural pieces, collision contribution, sockets/tags, dependencies and agreed content limits | Import/place/configure collision and navigation; test traversal, encounters, camera visibility, interaction and representative performance | Wrong import/placement/configuration belongs to integration. Delivered geometry, collision or attachment defects relative to agreement return to the producer. Do not retune an accepted controller to hide either. |
| Animation → motion assets → action/state behaviour | Compatible rig/skeleton and clip versions, motion intent, timing basis, markers/windows, movement/root-motion contribution and transition capabilities | Map gameplay states and action/hit windows, apply playback/transition rules, choose one responsible movement contribution and handle cancellation/interruption | Mis-timed bindings, playback conversion or double-applied movement belongs to integration. Incorrect agreed motion/marker content returns to Animation. Changed gameplay timing requires its owner. |
| Music/Audio → audio assets → runtime feedback | Identified clips/stems/cues, intended roles, loop/transition information, supported mix/state inputs and relevant delivery properties | Bind events and mix states; apply priorities, interruption/reset rules, triggering and redundancy; inspect actual audibility, transitions and gameplay meaning | Wrong routing, event mapping or runtime prioritisation belongs to integration. Missing/corrupt agreed cue/stem or unsuitable supplied loop returns to Music/Audio. Artistic revisions retain specialist authority. |

An integration agreement can divide collision, animation events or audio-state authoring differently. Record that split explicitly; job titles or file extensions alone do not determine responsibility.

## 4. Reusable handoff record

```markdown
Identity / revision / status: <handoff and actual delivery state>
Producer / integrator / consumers: <roles and responsible owners>
Purpose / source evidence: <thesis, behaviour, composition and specialist revisions>
Preserved decisions / authority: <constraints, approved ranges and change owner>
Producer delivery: <items, dependencies and required properties with units>
Game Development addition: <bindings, states, placement and runtime use>
Runtime expression: <target/import/configuration or explicitly unimplemented>
Acceptance: <static/reference, runtime, perceptual and performance checks as relevant>
Actual evidence / limitations: <what was checked and what remains unperformed>
Failure / repair scope: <expected versus actual, suspected owner and proposed correction>
Downstream impact: <affected routes, encounters, behaviours, content and evidence>
```

Keep proposed requirements, delivered properties and observed results separate. A declared socket or cue must resolve in the delivered version; a valid reference still does not prove its transform, timing or meaning in play. Producer-ready, integrated and gameplay-accepted are distinct states.

## 5. Integrate, inspect and repair

1. Agree the purpose and required gameplay properties before requesting substantial content. Preserve the accepted behaviour/greybox reference and list permitted variation.
2. Check delivery identity, dependencies, units and required names/properties. Report missing information explicitly. Do not invent compatibility or silently convert a material assumption.
3. Integrate a bounded representative use. Keep source assets distinguishable from import settings, placement and local customisation so a reimport or revision can be diagnosed.
4. Inspect the actual player's view/actions, not only an editor preview: traversal/contact, event/animation timing, narrative state, audio/mix behaviour, access alternatives and relevant target workload.
5. Compare failure evidence against both sides of the agreement. Identify whether the cause is the source delivery, import/configuration, gameplay rule, composition or evidence collection. Request the smallest sufficient correction from its owner.
6. Recheck the corrected case and affected accepted behaviour after replacement/reimport. Record the new versions, result and remaining limits; use the existing reopen process for material changes.

Examples of ownership decisions: a correctly sized doorway imported at half scale needs an integration correction; an opening that violates agreed source dimensions needs a producer correction. A correct contact marker played with the wrong timing conversion is an integration defect; a marker outside its agreed window is a producer finding. A story's deliberate character constraint must not be rewritten merely to avoid fixing a trigger binding.

Static reference, arithmetic and data checks are useful early evidence. They cannot establish collision behaviour, animation blending, player comprehension, artistic quality, audible mix quality or target performance without the appropriate runtime or human evaluation. A contract test that rejects a deliberately defective synthetic fixture is evidence about that predicate only.
