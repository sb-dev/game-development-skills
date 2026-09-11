# Game Development Skills - New Project Bootstrap Process

**Status:** Bootstrap specification  
**Version:** 1.1  
**Created:** 7 September 2026  
**Updated:** 12 September 2026

## 1. Purpose

This process defines how `game-development-skills` moves from a project idea to a **scaffolded, benchmarked, installable open-source Agent Skills repository**.

The repository should encode reusable game-development production intelligence: how to turn a game premise into a playable, testable and progressively refined interactive system without making one game engine, one provider or one coding agent the workflow.

The bootstrap is governed by `production-skills/docs/bootstrap` and the current Production Skills family specifications. In particular, it adopts the canonical **Seed → Five → Challenge** domain-research process and the evidence-led Extension Pack process while preserving the game-specific stage identifiers established by Version 1.0.

Mature Video, Narrative and Music Production Skills repositories remain reference implementations for proven family patterns, but this process must remain native to game development.

The target production shape is provisionally:

```text
player / product intent
→ game thesis
→ mechanics and rules
→ cheapest playable proof
→ playtest evidence
→ selection / commitment
→ systems and content integration
→ greybox / representative slice
→ evaluation and balancing
→ targeted correction
→ higher-fidelity production
→ performance / accessibility / release validation
→ playable delivery
```

The exact workflow, artefacts and core skills remain provisional until the staged research qualifies them with evidence.

The project is complete only when its installed skills can guide a clean consumer project through a realistic game-development workflow and produce a playable result with reproducible evaluation evidence.

### 1.1 Migration rule

This revision updates the research method without rewriting bootstrap history.

The repository is still a minimal bootstrap workspace and no substantive Stage 1–23 execution logs exist beyond this bootstrap specification. Preserve the existing numbered stages and insert the new domain-research gates as **Stage 1A** and **Stage 1B** before Stage 2.

```text
Stage 1
→ define the boundary

Stage 1A
→ bounded reconnaissance + select five complementary books

Stage 1B
→ directly examine, extract and reconcile those five books

Stage 2
→ challenge and extend the provisional model through broader professional research
```

For Extension Packs, preserve Stage 12 and Stage 20 while embedding the canonical pack stages:

```text
Stage 12
→ catalogue curation + P1–P5 research / design

Stage 20
→ P6 implementation / demonstration + P7 comparative proof / installation / catalogue readiness
```

Generating or revising this bootstrap defines work to perform. It does **not** prove that corpus selection, book extraction, broader research, per-pack research, implementation or evaluation has already occurred.

---

## 2. Required Outputs

The bootstrap must produce:

1. a clear game-development domain goal, scope and boundary;
2. a domain knowledge-coverage map produced through bounded reconnaissance;
3. a complementary five-book foundational corpus with supplied-book decisions and source-access records;
4. direct-source reading coverage and per-book extraction records;
5. a source-to-capability matrix plus overlap / conflict analysis;
6. a provisional game-development capability model derived from the five books without making the repository book-shaped;
7. broader professional, empirical and current-practice challenge research;
8. an evidence-qualified game-development model with supported, qualified, disputed, unresolved and rejected findings distinguished;
9. a player-experience and game-thesis model;
10. a domain-native mechanics, systems, loops and state model;
11. a prototype, fidelity, cost and commitment strategy;
12. a level/world/content integration model where relevant;
13. a playtesting, telemetry, tuning and balancing evidence model;
14. research into AI skills, game engines, editor agents, MCPs, CLIs, APIs and deterministic tools;
15. execution-layer decisions and a gap analysis;
16. a justified core Agent Skills architecture;
17. decomposed commands where useful;
18. a first-class Extension Pack architecture;
19. complementary Extension Pack catalogue analysis rather than an unreviewed list of genres or formats;
20. a five-book foundation for every selected Extension Pack, with reviewed evidence reuse where applicable;
21. per-pack source-to-behaviour-to-test traceability and separate research / implementation / evaluation / readiness status;
22. a domain-native Extension Pack authoring skill or equivalent workflow;
23. five progressive example levels;
24. three complementary primary examples per level selected through capability coverage;
25. deterministic, behavioural, semantic, performance and installation evaluation;
26. a benchmark and regression architecture;
27. six canonical project specifications;
28. a Video-style public README design;
29. an open-source repository scaffold design;
30. standalone and selective Agent Skills installation contracts;
31. local validation and clean external installation smoke tests;
32. optional Pactwright integration without runtime coupling;
33. maturity and publication gates;
34. a cross-domain review with evidence-backed extraction candidates only.

The six canonical specifications are:

```text
docs/
├── 01-game-development-skills-system-spec.md
├── 02-game-development-skills-workflows-and-artifacts-spec.md
├── 03-game-development-skills-repository-and-contracts-spec.md
├── 04-testing-and-benchmark-spec.md
├── 05-game-development-customisation-packs-spec.md
└── 06-game-development-extension-pack-catalogue.md
```

Specifications 05 and 06 remain separate because the Extension Pack contract and the curated catalogue evolve for different reasons.

---

# 3. Governing Principles

Retain the Production Skills family principles:

- **Domain first** - understand professional game development before designing Agent Skills.
- **Evidence foundation first** - establish a complementary five-book foundation, then challenge and extend it through broader professional research before encoding production capabilities.
- **Books inform capabilities, not architecture** - do not create book-specific skills, stages or pack categories merely because a source uses that structure.
- **Source access is not reading** - record what was actually examined; summaries, model memory and a bibliography are not direct-source extraction.
- **Production intelligence above execution** - game engines, coding agents, editor assistants and deterministic tools execute work; the repository owns the production reasoning that decides what work is required.
- **Cheapest adequate representation** - resolve uncertainty with the least expensive representation capable of answering the current design question.
- **Vertical first** - prove a playable end-to-end production path before broadening the architecture.
- **Preserve approved work** - accepted mechanics, tuned parameters, layouts and other committed decisions must not be silently discarded during refinement.
- **Correct the smallest responsible unit** - diagnose the production layer that owns a failure and modify the minimum sufficient scope.
- **Evaluation is product behaviour** - structural correctness, game quality, performance, accessibility and installation are first-class concerns.
- **Standalone first** - `game-development-skills` must remain usable without Pactwright.
- **Extract later** - share abstractions only after at least two independent Production Skills domains demonstrate substantially the same need.

### 3.1 Stage execution and evidence gates

Treat every stage as a standalone task.

```text
read canonical inputs
→ perform the substantive work
→ persist the detailed research / decision output
→ verify exit criteria
→ commit the completed stage
→ proceed only when dependencies are satisfied
```

A short summary, candidate list, bibliography or generated specification is not completion evidence for a substantive research stage.

Pending required permission to remove, replace or demote a user-provided book blocks corpus selection. Inadequate direct source access blocks book extraction. Uncertainty in broader research must be recorded and bounded rather than converted into invented certainty.

User-provided books remain members of a corpus unless the user explicitly authorises their removal, replacement or demotion. Selecting books for genuinely empty slots requires no additional approval unless separately requested.

Add game-development-specific principles.

## 3.2 Playability before production scale

A design document is not proof that a game works.

Important gameplay uncertainty should reach a playable representation as early as practical.

Examples:

```text
rule uncertainty
→ written rule set / state table / small simulation

movement uncertainty
→ isolated controller sandbox

combat uncertainty
→ small combat arena with placeholders

level-flow uncertainty
→ greybox / blockout

economy uncertainty
→ spreadsheet or headless simulation

AI behaviour uncertainty
→ isolated encounter + debug visualisation

network uncertainty
→ minimal multi-client proof under synthetic latency
```

Do not commission or generate expensive final content to discover that the underlying interaction is not viable.

## 3.3 Player experience must remain connected to mechanics

Game-development artefacts must preserve the reasoning chain between intended player experience and implemented rules.

A useful analysis lens is:

```text
intended player experience
→ mechanics / rules
→ runtime dynamics
→ observed player behaviour
→ playtest evidence
→ tuning or redesign
```

Frameworks such as Mechanics-Dynamics-Aesthetics are useful research inputs because they explicitly distinguish implemented mechanics from the dynamics and experience that emerge during play. They are not mandatory repository schemas.

## 3.4 Emergence is evidence, not noise

Games contain interacting systems whose combined behaviour may differ from the designer's local intent.

Evaluation must therefore inspect:

```text
individual mechanic correctness
+
system interactions
+
player strategies
+
edge cases
+
emergent behaviour
```

A locally correct rule can still create a broken dominant strategy, soft lock, exploit, pacing collapse or inaccessible interaction when composed with other systems.

## 3.5 Human play remains authoritative for experiential claims

Automated agents, simulations and scripted playtests can detect:

```text
reachability
rule violations
soft locks
state corruption
dead content
economy instability
obvious balance failures
performance regressions
```

They must not be treated as conclusive evidence that a game is fun, readable, emotionally effective, fair or satisfying.

Claims about player experience require appropriately scoped human evidence when the question is experiential.

## 3.6 Accessibility is a core quality dimension

Accessibility must not be hidden inside an optional Extension Pack.

The core production model should account for applicable concerns such as:

```text
control remapping
input alternatives
sensitivity / timing tolerance
readability
colour dependence
subtitles / captions
feedback redundancy
cognitive load
motor demands
pause / speed options where compatible
```

Specialist packs may extend an accessibility target, but baseline inclusive practice remains core.

## 3.7 Target-platform behaviour matters

Editor behaviour is not sufficient evidence for shipping performance.

The production model must distinguish fast iteration inside the editor from representative validation on target hardware or equivalent builds.

Performance, memory, load-time, input-latency and platform integration claims should be tested on a representative target path before release claims are made.

---

# 4. Domain Boundary Hypothesis

The exact boundary is decided in Stage 1, but bootstrap research should test the following hypothesis.

`game-development-skills` owns reusable expertise for designing, producing, integrating and evaluating **interactive gameplay**.

Likely owned responsibilities include:

```text
game thesis and player fantasy
core verbs
rules and mechanics
gameplay loops
system interactions
game states and progression
controls and feedback requirements
game feel targets
encounter design
level / world gameplay requirements
greybox validation
balance and tuning
playtest planning and diagnosis
accessibility requirements for gameplay
performance budgets from a gameplay-production perspective
integration of domain assets into playable behaviour
release-quality gameplay validation
```

Likely adjacent responsibilities include:

```text
Software Engineering Skills
→ general code architecture, implementation quality, refactoring, infrastructure, CI and non-game-specific engineering

UI/UX Design Skills
→ interface research, information architecture and general interaction-design practice

Narrative Production Skills
→ story, character arcs, dialogue and narrative structure

Music Production Skills
→ composition, music production and mastering

Video Production Skills
→ cinematics, trailers and rendered video production

2D / 3D / Character / Environment Production Skills
→ visual asset creation

Animation Skills
→ reusable animation production

Audio / Sound Production Skills
→ sound design and audio asset production

Deep Research Skills
→ external evidence gathering, market research and source-based domain investigation
```

Game Development may specify what these adjacent domains must deliver and integrate their outputs into gameplay, but it should not duplicate their specialist production pipelines.

The boundary must also decide how much game-specific implementation belongs here versus future `software-engineering-skills`.

A likely rule is:

> Game Development owns the game-specific production decision and acceptance criteria. Software Engineering owns general implementation engineering. The engine or coding execution layer performs the concrete code/editor operation.

---

# 5. Bootstrap Flow

```text
PROJECT IDEA
    ↓
1. Define Project Goal and Domain Boundary
    ↓
1A. Map Domain Knowledge Coverage and Select Five-Book Corpus
    ↓
1B. Extract and Reconcile the Five-Book Corpus
    ↓
2. Challenge and Extend Professional Game-Development Practice
    ↓
3. Define Player Experience and Game Thesis Model
    ↓
4. Model Mechanics, Rules, Systems, Loops and State
    ↓
5. Define Prototype / Fidelity / Commitment Strategy
    ↓
6. Model Levels, Worlds, Content and Cross-Domain Handoffs
    ↓
7. Define Playtesting, Telemetry, Tuning and Balance Model
    ↓
8. Research AI Skills, Engines and Tools
    ↓
9. Choose Execution Layer and Engine Integration Strategy
    ↓
10. Gap Analysis and Over-Engineering Review
    ↓
11. Design Core Skills and Commands
    ↓
12. Design Extension Packs and Pack Authoring
    ├─ P1 Define Specialisation and Core Baseline
    ├─ P2 Select Five Complementary Books
    ├─ P3 Extract and Reconcile Specialised Knowledge
    ├─ P4 Challenge Claims and Extend Coverage
    └─ P5 Specify Behaviour and Evaluation
    ↓
13. Design Progressive Examples
    ↓
14. Design Evals and Benchmarks
    ↓
15. Generate Six Canonical Specs
    ↓
16. Design the Public README
    ↓
17. Cross-Project Review
    ↓
18. Scaffold Repository
    ↓
19. Implement and Prove One Core Vertical
    ↓
20. Expand Progressive Coverage and Extension Packs
    ├─ P6 Implement and Demonstrate
    └─ P7 Evaluate, Validate Installation and Catalogue
    ↓
21. Validate Installation and Repository Integrity
    ↓
22. Add Optional Pactwright Integration and Register Maturity
    ↓
23. Review Shared Abstraction Candidates
    ↓
MATURE PRODUCTION SKILLS PROJECT
```

The bootstrap specification defines all stages. It does not scaffold `game-development-skills` while this document is being generated.

---

# 6. Stage 1 - Define Project Goal and Domain Boundary

Do not begin with a proposed skill list or engine selection.

Define:

```text
target game-development outcomes
intended users
supported project scales
supported game forms
engine expectations
platform expectations
multiplayer expectations
game-design responsibilities
gameplay implementation responsibilities
content integration responsibilities
quality definition
human approval points
persistent / locked decisions
cross-domain handoffs
non-goals
```

Resolve explicitly:

- Does the project own game design only, or game design plus playable integration?
- Where does game-specific engineering end and general software engineering begin?
- Does the project support engine-agnostic production intelligence with engine-specific execution adapters?
- What kinds of game are legitimate targets at maturity: 2D, 3D, simulation-heavy, networked, procedural, mobile, desktop, console, XR?
- Which classes should be deferred until the core has evidence?
- What is the smallest meaningful playable outcome the project should be able to produce end to end?
- What decisions require human approval before substantially more expensive work begins?

### Exit criteria

A short project charter exists with a defensible boundary, explicit adjacent disciplines and a clear definition of what a successful installed skill set should produce.

---

# 6A. Stage 1A - Map Domain Knowledge Coverage and Select Five-Book Corpus

Use the completed Stage 1 charter as the Seed for the canonical domain-research process.

Conduct **bounded reconnaissance** only far enough to identify the important game-development knowledge dimensions and compare candidate books. Do not duplicate Stage 2's full professional-practice research.

Candidate coverage dimensions include:

```text
player experience / game design
mechanics / systems / emergence
controls / feedback / game feel
levels / encounters / spatial design
playtesting / balancing / iteration
production / integration / delivery
accessibility / inclusive interaction
```

These are coverage questions, not mandatory one-book-per-slot categories.

Select exactly **five distinct complementary books** as the foundational corpus. Research a broader candidate pool and choose the combination that best covers the Stage 1 boundary rather than simply selecting five famous books.

Prefer durable game-development and design knowledge in the foundational corpus. Rapidly changing engine documentation, provider features and editor automation belong primarily in Stages 2 and 8 rather than being used to pad the five-book requirement.

For each candidate assess:

```text
relevance to owned game-development responsibilities
coverage and depth added to the existing corpus
practical production contribution
credibility and limitations
useful contrasting perspective
currency / durability
source access
```

For every selected book record:

```text
title / author
edition / publication year
provided or selected origin
source location / non-public identifier
access status
intended contribution
material actually examined
reading limitations
```

User-provided books remain in the corpus unless the user explicitly approves removal, replacement or demotion. A proposed substitution must record the overlap or coverage problem, expected gain, potential loss and alternative before permission is requested. Silence is not approval.

The five-book corpus does not limit the wider bibliography and does not imply five skills, packs, commands or knowledge categories.

### Research-log output

```text
knowledge-coverage map
candidate-book comparison
selected five-book corpus
source-access register
provided / retained / added / substituted decision log
remaining gaps
```

### Exit criteria

Exactly five books are selected; required supplied-book decisions are resolved; access needs and remaining knowledge gaps are explicit. Missing direct access may remain recorded at selection time but must be resolved before Stage 1B can complete.

---

# 6B. Stage 1B - Extract and Reconcile the Five-Book Corpus

Meaningfully examine all five selected books for their intended contributions before treating the corpus as evidence.

A bibliography, publisher summary, contents page, model memory or secondary discussion is not direct-source examination.

For each material concept capture:

| Field | Required content |
|---|---|
| Source | Book, edition and identifiable chapter, section, page or stable location actually examined |
| Problem / concept | Game-development problem addressed and independently expressed principle, method or heuristic |
| Applicability | Context, assumptions, prerequisites and limitations |
| Production behaviour | Inputs, decisions, workflow implications and outputs affected |
| Evaluation | Relevant evidence, metrics or possible evaluation criteria |
| Failure / repair | Failure conditions, misuse risks and smallest-sufficient correction strategies |
| Relationships | Overlap, support, tension or contradiction with other sources |
| Disposition | Retain, merge, adapt, qualify, reject or research further |

Map useful findings as:

```text
source idea
→ provisional game-development capability
→ production responsibility
→ workflow / command implication
→ evaluation criterion
→ candidate benchmark case
```

Do not create book-specific skills or force every selected source to contribute a core rule. Several books repeating a claim do not automatically constitute independent corroboration.

Reconcile overlap without erasing meaningful differences. Contradictory methods may be context-dependent, require a deliberate choice or remain unresolved until Stage 2.

Keep source access separate from publication. Do not commit supplied books, substantial copyrighted text or private source locations. Persist independently expressed synthesis and traceable source locations only.

### Research-log output

```text
per-book findings
reading-coverage records
source-to-capability matrix
overlap / conflict analysis
provisional game-development capability model
unresolved claims and gaps
```

### Exit criteria

All five books have been meaningfully examined for their intended contributions; material findings are traceable; limitations, conflicts and unresolved questions are explicit. Inadequate source access blocks completion rather than justifying inferred extraction.

---

# 7. Stage 2 - Challenge and Extend Professional Game-Development Practice

Use the Stage 1B provisional capability model to guide, **not limit**, broader research.

This stage has two simultaneous responsibilities:

1. challenge book-derived claims and determine where they are supported, qualified, context-dependent, disputed or rejected;
2. independently investigate important game-development responsibilities absent from the five-book corpus.

Study strong production practice before researching AI tooling.

Cover applicable disciplines such as:

```text
game design
gameplay design
systems design
technical design
level design
combat design
economy / progression design
AI / encounter design
gameplay programming
prototyping
technical art handoff
content integration
playtesting
QA
balancing
accessibility
performance optimisation
build / release validation
live tuning where relevant
```

Research:

- specialist roles, authoritative practitioners and terminology;
- real pre-production and production workflows;
- paper, spreadsheet, simulation and playable prototypes;
- greyboxing / whiteboxing / blockouts;
- vertical slices and representative slices;
- approval and commitment points;
- level and encounter iteration;
- game-feel tuning;
- balance methods;
- playtest methods;
- telemetry use;
- automated gameplay testing;
- platform profiling;
- content production and integration boundaries;
- common failures and their repair scopes;
- criticism, counterexamples and failure conditions for material book-derived methods;
- current standards and official guidance where practices can change materially.

Capture domain failure modes such as:

```text
unclear player goal
weak core loop
unresponsive controls
poor feedback
unreadable combat
soft lock
unreachable content
dominant strategy
trivial strategy
progression dead end
economy runaway / collapse
difficulty spike
unfair information asymmetry
level flow failure
AI deadlock / exploit
physics instability
save-state corruption
network desynchronisation
performance spike
input latency
accessibility blocker
```

Distinguish:

```text
supported finding
qualified method
context-dependent heuristic
disputed claim
unresolved question
rejected idea
```

Do not import a single studio methodology as the universal workflow, and do not promote an unresolved book claim into an unconditional core rule.

Identify what is deterministic, generative, judgement-heavy or tool-dependent. Separate durable game-development knowledge from engine/provider-specific behaviour; Stage 8 remains the dedicated AI/tool landscape stage.

### Research-log output

```text
professional-practice map
supporting and contrary evidence
gap analysis
claim dispositions
failure taxonomy
evidence-qualified game-development capability model
unresolved questions
```

### Exit criteria

The project has an evidence-qualified domain research log showing how professional game-development work reduces uncertainty, commits decisions, integrates systems and evaluates playability. Material book-derived claims have been assessed, important coverage gaps are addressed or bounded, and unresolved claims are not silently promoted to core rules.

---

# 8. Stage 3 - Define Player Experience and Game Thesis Model

This is a game-development-specific stage.

The repository needs a concise representation of what the game is trying to make the player do, understand and experience before detailed production begins.

Research and define the minimum useful game-thesis model.

Candidate fields include:

```text
target player / context
player fantasy
core verbs
primary challenge
intended mastery
core loop
session structure
success / failure model
risk / reward structure
desired emotional or experiential qualities
camera / viewpoint constraints
input assumptions
platform constraints
social mode
novelty / differentiator
non-goals
```

The thesis must be compact enough to revise cheaply and precise enough to constrain mechanics and evaluation.

Do not turn this into a universal Game Design Document.

### Questions

- Which player-experience statements are testable?
- Which are aspirations that require human play evidence?
- What should be locked before downstream content production?
- How should a rejected thesis or mechanic alternative be preserved for traceability without polluting the active production state?

### Exit criteria

A game-thesis contract exists that can guide prototype design and later evaluation without requiring a large design document.

---

# 9. Stage 4 - Model Mechanics, Rules, Systems, Loops and State

Define how the project represents interactive behaviour.

Research the smallest useful distinction among:

```text
player verbs
rules
mechanics
resources
entities
state
feedback
systems
loops
progression
win / fail conditions
encounters
system interactions
```

Candidate artefacts may include:

```text
game-thesis.md
mechanics/
rules/
systems/
loops.md
balance/
state-models/
controls/
feedback/
```

These are hypotheses, not mandatory folders.

For every first-class artefact identify:

```text
creator
purpose
consumers
source evidence
decisions preserved
status / confidence
approval behaviour
runtime expression
validation method
repair scope
downstream impact
```

Map common dependency chains such as:

```text
player goal
→ verb
→ rule
→ feedback
→ resulting dynamic
→ playtest observation
→ tuning decision
```

and:

```text
resource source
→ resource sink
→ progression pressure
→ player strategy
→ economy result
```

### Exit criteria

The project has a domain-native model for gameplay behaviour and can identify the smallest responsible unit when a systemic failure is observed.

---

# 10. Stage 5 - Define Prototype, Fidelity and Commitment Strategy

Translate the family cheap-first principle into game-development fidelity.

A possible fidelity ladder is:

```text
written rule / state table
→ spreadsheet or headless simulation
→ isolated mechanic toy
→ placeholder playable prototype
→ greybox / blockout
→ representative encounter or level
→ vertical slice
→ integrated content production
→ target-platform build
→ release candidate
```

The ladder is not mandatory. Different uncertainties require different representations.

Map uncertainty to cheap evidence:

| Uncertainty | Cheapest useful representation hypothesis |
|---|---|
| core rule | written rules / examples / state table |
| probability or economy | spreadsheet / simulation |
| movement | isolated controller sandbox |
| combat timing | small placeholder arena |
| camera | dedicated camera sandbox |
| AI behaviour | isolated encounter + debug state |
| level flow | greybox |
| progression | data table + simulated runs |
| procedural generation | seed-based generator + reachability checks |
| network behaviour | minimal replicated proof + synthetic conditions |
| performance | representative stress scene / target build |
| player comprehension | human playtest with minimal art |

Define commitment points for expensive or wide-impact changes.

Candidate approvals include:

```text
game thesis selected
core mechanic accepted
control model accepted
core loop accepted
representative level / encounter accepted
vertical slice accepted
content scope accepted
release candidate accepted
```

Do not create approval bureaucracy for cheap reversible decisions.

### Exit criteria

The project can choose a representation based on uncertainty and cost rather than defaulting to high-fidelity implementation.

---

# 11. Stage 6 - Model Levels, Worlds, Content and Cross-Domain Handoffs

Game development integrates content produced by several domains.

Define what the game-development repository owns at integration boundaries.

Research game-native artefacts such as:

```text
level brief
encounter brief
flow map
critical path
spawn / pacing plan
greybox
navigation constraints
gameplay tags / sockets / interaction contracts
asset integration requirements
collision requirements
animation gameplay requirements
audio feedback requirements
narrative trigger requirements
performance budgets
```

Test reusable handoff patterns such as:

```text
Narrative
→ character / story intent
→ Game Development
→ gameplay role, trigger, state and interaction integration
```

```text
Environment / 3D Production
→ runtime-ready environment asset
→ Game Development
→ collision, traversal, encounter, camera and performance integration
```

```text
Animation
→ motion assets
→ Game Development
→ state transitions, timing windows, hit / movement behaviour
```

```text
Music / Audio
→ audio assets
→ Game Development
→ runtime triggers, mix states and feedback behaviour
```

Do not introduce a universal cross-domain asset graph unless later evidence proves it necessary.

### Exit criteria

The project can state what an adjacent Production Skills domain must deliver, what Game Development adds, and who owns correction when integrated behaviour fails.

---

# 12. Stage 7 - Define Playtesting, Telemetry, Tuning and Balance Model

This is another game-development-specific stage.

Separate evidence sources:

```text
scripted automated tests
headless simulation
bot / agent playtests
telemetry
replay analysis
expert review
human usability / comprehension playtest
human experiential playtest
platform profiling
```

For each source define what it can and cannot establish.

A useful evidence rule is:

```text
automation establishes mechanical evidence
telemetry establishes observed behaviour at scale
human play establishes experiential evidence
```

with overlap but no silent substitution.

Research tuning loops such as:

```text
observation
→ diagnosis
→ responsible parameter / rule / encounter / layout
→ smallest change
→ replay or rerun
→ compare evidence
→ keep / revert
```

Balance research should cover applicable concepts such as:

```text
win rate
pick rate
clear rate
resource curves
time-to-kill
time-to-mastery
strategy diversity
difficulty curves
content reachability
progression pacing
risk / reward
snowballing
rubber-banding
```

Do not make every game use the same metrics.

### Exit criteria

The project has an evidence taxonomy and can distinguish mechanical correctness, balance evidence and subjective player experience.

---

# 13. Stage 8 - Research AI Skills, Engines and Tools

Research capabilities, not brand names.

Search for:

```text
game-design Agent Skills
gameplay programming skills
Unity skills / MCP / editor agents
Unreal skills / editor automation / Python / commandlets
Godot skills / editor automation
Roblox Studio AI / MCP
engine-agnostic coding agents
game-engine CLIs
scene / object graph inspection
asset import automation
headless builds
headless play
input simulation
replay systems
functional tests
screenshot / video capture
state inspection
profilers
telemetry tools
procedural-generation tools
AI / behaviour-tree tools
navigation tools
physics-debug tools
network simulation
automated playtesting agents
accessibility validation
store / platform build tooling
```

Current evidence already shows why this research matters:

- Unreal Engine exposes a gameplay framework and layered automation facilities including feature, gameplay, content-stress and screenshot testing.
- Unity exposes profiling and target-platform validation, and its 2026 AI tooling includes an editor-grounded assistant, MCP server and gateway.
- Roblox Studio exposes AI/MCP capabilities that can inspect the data model, edit instances, create/run scripts and playtest.

These examples are execution evidence, not a decision to standardise on any engine.

For each candidate record:

| Field | Meaning |
|---|---|
| Capability | What production operation it performs |
| Source | Repository/provider |
| Licence | Reuse constraints |
| Maturity | Stability / adoption |
| Engine / platform | Coupling |
| Installation | How it is consumed |
| Production role | Workflow position |
| Deterministic vs generative | Behaviour class |
| Editor / runtime access | Available state and actions |
| Composability | Agent / CLI / API fit |
| Quality suitability | Production usefulness |
| Maintenance | Current activity |
| Classification | USE / ADAPT / REFERENCE / REJECT |
| Gaps | Missing behaviour |

### Exit criteria

A current capability landscape exists and makes clear which operations should be delegated to existing execution tools.

---

# 14. Stage 9 - Choose Execution Layer and Engine Integration Strategy

Separate:

```text
game-development production intelligence
```

from:

```text
code generation
engine editor manipulation
scene creation
asset generation
build execution
input simulation
runtime state inspection
profiling
capture
telemetry
platform deployment
```

The repository should define engine-neutral production semantics only where real evidence supports them.

Possible architecture to investigate:

```text
Game Development Skills
        ↓ production intent
engine / coding execution capability
        ↓
Unity / Unreal / Godot / Roblox / custom runtime
        ↓
deterministic test + capture + profile tools
```

Engine-specific references or commands may be justified when they encode materially different production operations, but the core must not become a fake lowest-common-denominator game engine.

Resolve:

- whether engine-specific adapters belong inside skills, references, examples or separate packages;
- what minimum editor/runtime inspection surface is required;
- how a skill detects available engine tooling;
- how engine-specific behaviour is benchmarked;
- how clean installation works without hidden source-repository dependencies.

### Exit criteria

The project has a minimal execution architecture with explicit provider and engine boundaries.

---

# 15. Stage 10 - Gap Analysis and Over-Engineering Review

Compare:

```text
required game-development workflow
        vs
available engines, skills, tools and providers
```

Classify capabilities:

```text
covered
partially covered
missing
```

Pay special attention to gaps in:

```text
player-experience to mechanic traceability
prototype selection
system-interaction reasoning
playtest diagnosis
game-feel evaluation
balance diagnosis
level-flow evaluation
approved-decision preservation
small-scope repair
cross-domain integration
engine-state inspection
automated mechanical playtesting
human evidence handling
performance-budget validation
accessibility
installation
```

## Early over-engineering flags

Do not build these during bootstrap unless a proven gap requires them:

```text
custom game engine
universal gameplay DSL
universal entity-component system
cross-engine runtime abstraction layer
custom scene editor
universal asset pipeline
general-purpose autonomous playtester
universal simulation platform
custom telemetry backend
universal behaviour-tree system
central provider router
universal game artefact graph
universal benchmark score
```

Record promising ideas as follow-up candidates rather than letting them block the core vertical.

### Exit criteria

Native skills are justified only for production intelligence not already solved well by existing capabilities, and deferred architecture is clearly identified.

---

# 16. Stage 11 - Design Core Skills and Commands

Derive the smallest installable skill set capable of executing the game-development workflow.

Do not start from a fixed number of skills.

Compare at least these architectural hypotheses.

## Hypothesis A - Minimal orchestration

```text
game-development
game-evaluate
game-extension-pack-creator
```

`game-development` owns planning, prototyping, integration and refinement.

## Hypothesis B - Split design and playable production

```text
game-design
game-development
game-evaluate
game-extension-pack-creator
```

Use only if isolated installation, evaluation or responsibility boundaries justify the split.

## Hypothesis C - Specialist skills only where evidence proves them

Possible future additions:

```text
game-balance
game-level-design
game-playtest
```

Do not create them merely because these are professional roles.

### Candidate commands

Commands should be bounded operations with independent evaluation value.

For example:

```text
game-development
├── define-game-thesis
├── design-mechanic
├── model-system
├── define-core-loop
├── prototype-mechanic
├── greybox-level
├── design-encounter
├── integrate-content
├── tune-parameters
├── prepare-representative-build
└── produce-release-build
```

and:

```text
game-evaluate
├── validate-rules
├── test-state-transitions
├── check-reachability
├── evaluate-controls
├── evaluate-feedback
├── evaluate-level-flow
├── evaluate-balance
├── evaluate-game-feel
├── evaluate-accessibility
├── evaluate-performance
├── diagnose-system-interaction
└── recommend-smallest-repair
```

The final command surface must come from the workflow and benchmark design.

### Exit criteria

Every installable skill has a coherent production responsibility, and every command exists for composition, diagnosis, reuse or benchmark precision.

---

# 17. Stage 12 - Design Extension Packs and Pack Authoring

Extension Packs are a first-class target capability.

The core skills must remain useful without a pack.

Use the canonical `production-skills/docs/bootstrap/extension-pack-process.md` at two levels:

1. curate a complementary Game Development Extension Pack catalogue;
2. run P1–P5 separately for each selected pack before implementation.

Catalogue size is determined by useful complementary coverage, not by the five-book requirement and not by the size of the existing candidate list.

## 17.1 Catalogue curation

Research or generate a broader candidate pool across game-development specialisation dimensions.

### Gameplay / genre grammar candidates

```text
precision-platformer
arcade-score-attack
roguelite
tactical-turn-based
survival-horror
stealth
fighting
racing
rhythm
puzzle
simulation / management
```

### Perspective / interaction format candidates

```text
2d-side-view
top-down / isometric
first-person
third-person
touch-first
gamepad-first
local-multiplayer
```

### Production-constraint specialisation candidates

```text
low-spec-mobile
deterministic-replay
short-session-arcade
high-density-simulation
networked-cooperative
```

Treat these as **candidate specialisations**, not an initial catalogue.

Classify every need:

```text
existing core already covers it
→ keep core

one-project detail
→ project instructions

broad game-development responsibility
→ core-improvement candidate

reusable specialised production behaviour
→ Extension Pack candidate

insufficient distinction or evidence
→ defer / reject
```

Assess the selected catalogue as a set. Avoid near-duplicate packs that merely rename a perspective, genre or platform without changing production behaviour.

## 17.2 Pack boundaries

Do not put these into Game Development packs by default:

```text
visual art style
→ 2D / 3D / environment / character production

narrative genre or prose style
→ Narrative Production Skills

music genre
→ Music Production Skills

cinematic language
→ Video Production Skills

provider or model choice
→ execution configuration unless it truly changes reusable production grammar
```

Production-constraint packs such as `networked-cooperative` require explicit checks against Software Engineering ownership.

## 17.3 P1 - Define the specialisation and core baseline

For each selected pack define:

```text
intended use / non-use
reusable production need
core revision / baseline
why core + ordinary project instructions is insufficient
expected specialised behaviour
relevant core skills
hard constraints
soft defaults
what must remain stable
adjacent-domain boundaries
provisional evaluation questions
```

The baseline must represent the actual production need rather than an intentionally vague core prompt designed to make the pack appear useful.

## 17.4 P2 - Select five complementary foundational books

Each selected pack has exactly five justified foundational books.

The books need not be unique to that pack and there is **no quota of five new books**. Existing domain or other-pack research may be reused only after reviewing the original source location, edition, reading scope, assumptions, limitations and applicability to this specialisation.

Do not automatically inherit the core five-book corpus or copy another pack's bibliography.

Apply the same supplied-book permission, access and publication rules as Stage 1A / 1B.

Record:

```text
pack-specific knowledge-coverage map
candidate comparison
selected five books
book contribution to this pack
access / reading status
reviewed evidence reuse
substitution approvals where needed
remaining gaps
```

## 17.5 P3 - Extract and reconcile specialised knowledge

Map material findings as:

```text
source finding + examined location
→ applicability to this game specialisation
→ change to a core-skill decision
→ observable playable / artefact effect
→ evaluation criterion
→ failure / repair case
```

A previous citation or another pack profile is not proof of adequate examination. Reused findings must be reviewed for this pack's context.

Keep general Game Development knowledge, specialised pack guidance and project-specific detail distinct.

## 17.6 P4 - Challenge claims and extend coverage

Research supporting and contrary evidence, alternative methods, failure conditions and important requirements absent from the five books.

Additional books, research, standards, practitioner material, official engine/platform documentation and relevant games may supplement this stage. Non-book sources do not count toward the pack's foundational five books.

A technique observed in a successful game is evidence that the technique exists in that work; it is not proof that the technique caused success or is universally desirable.

Record evidential standing separately from disposition.

## 17.7 P5 - Specify behaviour and evaluation

Every selected pack must define:

```text
scope and qualification rationale
activation
precedence
production rules
mechanical / systemic effects
core-skill effects
what remains core
hard constraints / soft defaults
qualified methods / heuristics
cross-domain boundaries
specialised evaluation
negative / incompatibility cases
smallest-sufficient repair behaviour
showcase brief
exact copyable generation prompt
independent reuse brief / fixture
source-to-behaviour-to-test mapping
research status
implementation status
evaluation status
readiness status
```

Precedence should normally remain:

```text
explicit project instructions
→ approved / locked game decisions
→ selected Game Development Extension Pack
→ core Game Development defaults
```

Define falsifiable acceptance cases before implementing a pack.

A mature repository should provide `game-extension-pack-creator` or an equivalent workflow. Extend that domain-owned capability to consume completed P1–P5 evidence rather than creating a second generic pack-authoring system or mirroring the P-stage names as mandatory runtime commands.

### Stage 12 research-log outputs

Persist:

```text
catalogue candidate pool
combined coverage matrix
selected catalogue rationale
existing/core/project-instruction alternatives
per-pack P1 specialisation brief
per-pack P2 corpus and access record
per-pack P3 extraction / reconciliation
per-pack P4 challenge / gap research
per-pack P5 production profile and source-to-behaviour-to-test mapping
separate per-pack evidence status
```

Additional catalogue ideas may remain explicitly `planned`; do not present them as researched or ready.

### Exit criteria

The project can distinguish a reusable game-development specialisation from a project brief, engine adapter or adjacent-domain style pack. Selected packs have evidence-qualified, testable profiles from completed P1–P5 work; unresolved entries remain visibly planned. Actual production proof waits for the implemented core vertical and Stage 20.

---

# 18. Stage 13 - Design Progressive Examples

Examples are part of the public product and benchmark surface.

The family target is:

```text
5 levels
×
3 primary examples per level
=
15 primary examples
```

The following level meanings are hypotheses to validate.

## Level 1 - Prove one mechanic

Bounded playable interactions.

Demonstrate:

```text
rules
input
state
feedback
basic tuning
small automated tests
smallest-scope repair
```

Candidate seeds:

```text
precision jump / dash sandbox
top-down dodge-and-attack arena
single-room push / spatial puzzle
```

## Level 2 - Prove one repeatable gameplay loop

Compose several mechanics into a short complete loop.

Demonstrate:

```text
goal
challenge
reward / failure
restart / retry
pacing
basic balance
human playtest
```

Candidate seeds:

```text
arcade score-attack loop
stealth infiltrate-and-extract micro-loop
resource collect / upgrade / survive loop
```

## Level 3 - Produce a coherent vertical slice

A representative gameplay slice with level or encounter structure.

Demonstrate:

```text
system composition
content integration
level / encounter design
progression
UI / audio / visual handoffs
performance budget
broader evaluation
```

Candidate seeds:

```text
action-platformer slice
turn-based tactical encounter + progression slice
racing time-trial / opponent slice
```

## Level 4 - Handle scale, systemic interaction and repair

Several systems, content units or players interact.

Demonstrate:

```text
multi-level or multi-encounter consistency
emergent strategies
procedural or systemic content
complex balance
regression protection
performance under representative load
repair without invalidating stable systems
```

Candidate seeds:

```text
small roguelite run
management / simulation scenario
small cooperative or competitive networked scenario
```

## Level 5 - Deliver the full game-development thesis

Demonstrate broad production responsibility and cross-domain composition.

Possible targets include:

```text
small complete polished game
multi-system world or campaign slice
content-rich game slice using several Production Skills handoffs
```

Level 5 should test:

```text
game thesis
mechanics
systems
levels / world
content integration
playtesting
balance
performance
accessibility
release validation
Extension Packs
cross-domain handoffs
```

### Example discovery process

Do not accept the seed examples automatically.

For each level:

1. derive the capabilities the level must prove;
2. research or generate a larger candidate pool;
3. score candidates against a capability-coverage matrix;
4. remove examples with substantially overlapping behaviour;
5. select the three whose combined coverage is strongest;
6. inspect the complete 15-example set for gaps and excessive repetition.

Coverage dimensions should include:

```text
2D vs 3D
real-time vs turn-based
precision vs systemic play
authored vs procedural content
physics dependence
AI dependence
single-player vs multiplayer
short-session vs progression-heavy
level-based vs world-based
platform / input differences
core skills
commands
Extension Packs
failure modes
repair behaviour
performance risks
accessibility challenges
cross-domain handoffs
benchmarkability
showcase clarity
```

Every primary example must include the complete copyable generation prompt.

### Exit criteria

The selected 15 examples form a deliberate capability curriculum rather than fifteen variants of one game type.

---

# 19. Stage 14 - Design Evals and Benchmarks

Evaluation must separate structural correctness from game quality.

A build can be correct and still feel bad. A game can feel promising and still contain deterministic failures.

Use layered evaluation.

## 19.1 Repository and deterministic validation

Examples:

```text
skill self-containment
required references present
command contracts valid
artefact schemas valid where schemas exist
broken asset / scene references
invalid state transitions
missing input bindings
build failures
missing test fixtures
invalid Extension Packs
installation integrity
```

## 19.2 Mechanical correctness

Examples:

```text
rules execute as specified
win / fail conditions reachable
restart / checkpoint works
save / load preserves valid state
cooldowns and resource changes are valid
collision / interaction contracts work
no known soft locks
required content reachable
```

## 19.3 Systemic and simulation evaluation

Examples:

```text
strategy diversity
dominant strategy detection
economy stability
progression curves
AI interaction
procedural reachability
seed reproducibility
content utilisation
pacing distributions
```

## 19.4 Player-experience evaluation

Keep dimensions inspectable rather than collapsing them into one score.

Candidate dimensions:

```text
responsiveness
control clarity
feedback quality
readability
player agency
challenge legibility
fairness
pacing
mastery curve
flow
game feel
satisfaction
comprehension
```

Some dimensions require human play evidence.

## 19.5 Level and encounter evaluation

Measure applicable concerns such as:

```text
navigation
critical-path readability
choice quality
encounter pacing
spawn fairness
cover / traversal utility
camera safety
checkpoint placement
dead space
content reachability
```

## 19.6 Accessibility evaluation

Test applicable baseline requirements and game-specific constraints.

## 19.7 Performance evaluation

Record representative budgets and verify them on suitable builds.

Possible dimensions:

```text
frame time
CPU / GPU cost
memory
allocation spikes
load time
streaming stalls
input latency
network latency / replication cost
```

Do not make engine-editor profiling the only release evidence.

## 19.8 Preservation and repair evaluation

Test that:

```text
approved mechanics survive unrelated content refinement
accepted control feel survives level changes
local balance fixes do not rewrite unrelated systems
level repair preserves unaffected rooms / encounters
pack activation does not override locked decisions
```

## 19.9 Extension Pack evaluation

Require:

```text
activation when requested
non-activation when absent
meaningful specialised production behaviour
explicit instruction precedence
approved-decision precedence
pack-aware quality criteria without hiding genuine defects
negative / incompatibility cases
targeted refinement without unrelated regeneration
boundary discipline
```

Define pack acceptance before implementation.

For comparative evaluation use the **same substantive game brief, constraints and comparable execution conditions**:

```text
core only
vs
core + pack
```

The intentional difference is pack activation and its packaged guidance. Do not make the packed run appear superior by giving it a richer task brief.

Where useful, add:

```text
core + ordinary project instructions
```

as a third baseline to test whether the pack actually adds reusable depth, consistency or reduced prompting burden.

Every implemented pack must run:

1. its primary showcase with the exact recorded prompt;
2. a distinct additional reuse brief / fixture;
3. behavioural and precedence cases;
4. fair core-vs-pack comparison.

Preserve actual outputs, relevant execution provenance, failures, regressions, inconclusive results and evaluator limitations. A prompt, directory, pack label or single favourable run is not sufficient evidence of reusable improvement.

## 19.10 Installation smoke tests

Separate:

```text
source-repository validation
```

from:

```text
clean consumer-project installation and execution
```

## Regression loop

```text
escaped gameplay defect
→ diagnose responsible unit
→ create smallest reproducible fixture
→ add eval / benchmark
→ fix
→ retain permanent regression protection
```

### Exit criteria

The project can detect important regressions cheaply and distinguish correctness, balance, player experience, accessibility and performance evidence. Extension Pack evaluation can distinguish useful specialisation from metadata or prompt advantage and has a clean-installation proof gate.

---

# 20. Stage 15 - Generate Six Canonical Specifications

Generate:

```text
docs/
├── 01-game-development-skills-system-spec.md
├── 02-game-development-skills-workflows-and-artifacts-spec.md
├── 03-game-development-skills-repository-and-contracts-spec.md
├── 04-testing-and-benchmark-spec.md
├── 05-game-development-customisation-packs-spec.md
└── 06-game-development-extension-pack-catalogue.md
```

## Spec 01 - System

Owns:

```text
mission
scope and boundaries
game-development principles
core skills
execution architecture
engine / provider boundary
prototype / fidelity / commitment policy
player-evidence policy
cross-domain integration model
build order
system acceptance
```

## Spec 02 - Workflows and Artifacts

Owns:

```text
game-development workflow
game thesis
mechanics / rules / systems / loops
state and progression
prototype strategy
levels / worlds / encounters
playtest evidence
balance / tuning
approval and preservation
failure taxonomy
repair routes
handoffs
```

## Spec 03 - Repository and Contracts

Owns:

```text
repository structure
SKILL.md contracts
command contracts
skill self-containment
engine-specific references / adapters
scripts / tools / assets
installation
runtime dependencies
CI
technical acceptance
```

## Spec 04 - Testing and Benchmark

Owns:

```text
testing layers
benchmark suites
case contracts
mechanical correctness
systemic evaluation
player-experience evaluation
playtest evidence rules
performance / accessibility
progressive-example coverage
Extension Pack evaluation
regression policy
release gates
measured evidence
```

## Spec 05 - Customisation / Extension Packs

Owns:

```text
pack definition
pack dimensions
qualification
catalogue-curation method
activation
precedence
core-skill effects
gameplay specialisation
cross-domain boundaries
pack packaging
pack-aware evaluation
per-pack Seed → Five → Challenge application
reviewed research-reuse rules
baseline-comparison contract
pack readiness gates
pack-authoring contract
```

## Spec 06 - Extension Pack Catalogue

Owns, for each curated pack:

```text
identity and intended use / non-use
selection rationale and complementary catalogue contribution
core baseline
specialised behavioural difference
five-book corpus and each book's contribution
research-log references
source-access / reading limitations
unresolved findings
hard constraints
soft defaults
qualified methods / heuristics
core-skill effects
what remains stable
source-to-behaviour-to-test mapping
showcase premise
exact generation prompt
actual showcase outputs when executed
independent reuse fixture
pack-specific evaluation evidence
research status
implementation status
evaluation status
readiness status
clean-installation evidence
limitations / compatibility / migration notes
```

A planned catalogue entry must not imply completed research, implementation or evaluation. An implemented pack directory must not imply passed comparison or readiness.

### Exit criteria

Implementation can proceed without inventing the game-development architecture inside code or examples, and the pack contract / catalogue can distinguish planned specialisations from evidence-qualified and demonstrated packs.

---

# 21. Stage 16 - Design the Public README

Follow the public structure proven by `video-production-skills`, adapted to games.

The target README should contain, where relevant:

```text
project positioning
what can be produced
playability / approval / fidelity control
installation
quick start using a strong Level 1 playable example
Learn by producing
  Level 1 - 3 examples
  Level 2 - 3 examples
  Level 3 - 3 examples
  Level 4 - 3 examples
  Level 5 - 3 examples
project structure grows with the game
core skills
Extension Packs
execution layer / supported engine paths
playtesting / evaluation / benchmark entry points
documentation index
project boundary
contributing
licence
```

The quick start should produce something playable, not only a design document.

The README must never claim engine support, examples, packs or benchmark results that are only planned.

### Exit criteria

A public reader can understand the project, install it, run the smallest playable example and see how capability grows through the five levels.

---

# 22. Stage 17 - Cross-Project Review

Only now compare the domain architecture with Video, Narrative, Music and the current Production Skills family specifications.

Look for independently reproduced needs such as:

```text
cheap representation before expensive production
selection / approval before commitment
candidate alternatives
preservation of accepted work
smallest-scope repair
Extension Pack precedence
pack authoring
progressive examples
layered evaluation
clean external installation
```

Also identify game-specific concepts that must remain local, such as:

```text
game feel
mechanics / dynamics
playtesting
balance
levels / encounters
runtime simulation
input behaviour
performance budgets
```

Apply the required shared-abstraction record:

```yaml
candidate: <name>
observed_in:
  - game-development
  - <other-domain>
common_need: <domain-independent need>
domain_variations:
  game-development: <variation>
  <other-domain>: <variation>
evidence:
  - <link or research record>
recommendation: <family principle | project contract | reject>
not_recommended:
  - <over-generalisation to avoid>
```

### Exit criteria

Useful family candidates are recorded without modifying the family merely to simplify the game repository.

---

# 23. Stage 18 - Scaffold Repository

Create only structure justified by the specifications.

A likely starting surface is:

```text
game-development-skills/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── docs/
├── skills/
├── examples/
├── evals/ or benchmarks/
├── tests/
├── tools/                 # only if required
├── integrations/          # optional
└── .github/
```

Do not create empty engine folders, adapters, packs or provider directories for symmetry.

### Exit criteria

A contributor can navigate the repository and every committed directory has an immediate purpose.

---

# 24. Stage 19 - Implement and Prove One Core Vertical

Implement the minimum core skills and commands required to produce one meaningful playable example end to end.

A suitable first vertical should test:

```text
brief / thesis
→ mechanic
→ playable prototype
→ deterministic checks
→ human or agent play evidence as appropriate
→ diagnosis
→ targeted correction
→ repeatable playable build
```

Use placeholders and cheap assets wherever they keep the gameplay question observable.

Do not begin by supporting every engine or genre.

### Exit criteria

Installed core skills can produce, inspect, evaluate and repair one realistic playable result.

---

# 25. Stage 20 - Expand Progressive Coverage and Extension Packs

Implement the planned capability breadth through the selected progressive examples.

Add Extension Packs only when the core workflow is stable enough to prove differential behaviour.

Use the evidence-qualified P1–P5 profiles from Stage 12 and complete **P6** and **P7** for every implemented pack.

## 25.1 P6 - Implement and demonstrate

Use `game-extension-pack-creator` or the selected domain-owned authoring workflow.

Implement a self-contained pack containing the concise guidance it actually needs at runtime. Research reuse must not create runtime dependencies on the central Production Skills repository, another pack's files, research logs or access to the source books.

For every implemented pack:

```text
create / refine installable pack
→ create behavioural fixtures
→ record exact showcase prompt
→ run the showcase
→ preserve actual playable / production outputs
→ preserve relevant execution provenance
→ run local validation
```

A prompt alone is not a demonstration. Unavailable execution remains a blocker rather than being reported as a successful showcase.

## 25.2 P7 - Evaluate, validate installation and catalogue

Run the Stage 14.9 comparison and the independent reuse fixture.

For each implemented pack prove:

```text
core works without pack
core + pack changes intended game-development behaviour
explicit project instruction outranks pack
approved game decision outranks pack
pack-aware evaluation recognises intended specialisation without hiding defects
pack authoring can create or revise a valid pack
specialisation survives a second production brief / fixture
clean consumer-project installation and use succeeds
```

Record:

```text
core / pack revisions
exact prompts
model / tool versions where relevant
settings / resource constraints
actual outputs
behavioural results
comparative findings
regressions
inconclusive cases
evaluator limitations
installation evidence
readiness decision
```

Where useful, compare core + ordinary project instructions against the pack to ensure packaging contributes reusable value.

Every ready catalogue pack must include:

```text
realistic executed showcase
exact copyable prompt
actual outputs
independent reuse fixture
behavioural evaluation
fair core-vs-pack comparison
clean external installation evidence
limitations
separate research / implementation / evaluation / readiness status
```

If useful specialised behaviour is not demonstrated or regressions are unacceptable, refine and retest or retain the entry as unproven / deferred. Do not publish it as ready merely because its files exist.

### Exit criteria

The repository demonstrates breadth through implemented examples and evidence-qualified packs rather than specifications alone. Ready pack claims are backed by actual production, comparative evaluation and clean external installation evidence.

---

# 26. Stage 21 - Validate Installation and Repository Integrity

Validate:

```text
repository contracts
skill self-containment
command discovery
selective installation
clean consumer-project installation
engine/tool prerequisites
no undocumented repository-relative runtime dependencies
benchmark entry points
example reproducibility
```

Test at least:

1. validation inside the source repository;
2. installation into a clean external project using the Skills CLI;
3. discovery of selected skills only;
4. execution of a representative example without relying on hidden source files.

Where engine software is required, distinguish skill installation from engine prerequisite setup.

Extension Pack research evidence may be shared during development, but installed packs must carry necessary runtime guidance locally and remain independently installable according to the repository contract.

### Exit criteria

The repository behaves as an installable Agent Skills product rather than a set of instructions that only work in its own checkout.

---

# 27. Stage 22 - Optional Pactwright Integration and Maturity Registration

If useful, add:

```text
integrations/pactwright.yml
```

It may declare identity, compatibility, capability bindings and Extension Pack discovery.

It must not define:

```text
Pactwright lifecycle topology
Project Graph semantics
Pactwright prompts or agents
game-development workflow
provider routing
consuming-project game state
```

Register or update the project in the Production Skills family registry.

Use the maturity progression:

```text
proposed
→ researching
→ specified
→ scaffolded
→ working
→ benchmarked
→ mature
```

Promotion requires demonstrated evidence, not intended architecture.

### Mature evidence should include

```text
six specification responsibilities represented
public README accurate
core playable workflow works end to end
5 levels × 3 primary examples represented
copyable primary prompts
Extension Pack contract + evidence-qualified catalogue represented
pack authoring capability represented
implemented ready packs have executed showcases + behavioural evals + reuse fixtures
core works without packs
domain evaluation + regression protection operational
clean external installation works
quality claims measured or explicitly marked unmeasured
```

Completing the new book or pack research gates does not by itself promote repository maturity.

---

# 28. Stage 23 - Review Shared Abstraction Candidates

After implementation evidence exists, apply the Production Skills shared-abstraction process.

Promote a family abstraction only when:

- at least two independent domains demonstrate the need;
- the abstraction removes duplicated family-level reasoning rather than useful game-development detail;
- domain variations remain domain-owned;
- the common contract is smaller and clearer than independent implementations.

Do not promote:

```text
universal playable artefact schema
universal game-state model
universal production runtime
universal game engine abstraction
universal benchmark score
universal Extension Pack interpreter
```

without independent multi-domain evidence.

### Exit criteria

Reusable evidence is captured without coupling `game-development-skills` to speculative family infrastructure.

---

# 29. Research Basis for This Bootstrap

This bootstrap uses the current Production Skills family process as its governing source.

## Production Skills family

- `production-skills/docs/bootstrap/README.md`
- `production-skills/docs/bootstrap/new-project-process.md`
- `production-skills/docs/bootstrap/domain-research-process.md`
- `production-skills/docs/bootstrap/extension-pack-process.md`
- `production-skills/docs/bootstrap/shared-abstraction-process.md`
- current family specifications under `production-skills/docs/specs/`
- mature Video, Narrative and Music Production Skills repositories

## Initial reconnaissance and broader-research inputs

The following sources informed the original bootstrap questions and remain useful inputs for Stage 2, Stage 8 and later specialist research. **They are not the five-book foundational corpus, and their presence here is not evidence that Stage 1A or Stage 1B has been executed.**

### MDA: A Formal Approach to Game Design and Game Research

Robin Hunicke, Marc LeBlanc and Robert Zubek.

Useful because it separates mechanics, runtime dynamics and player experience and emphasises iterative analysis of interacting game systems.

- https://aaai.org/papers/ws04-04-001-mda-a-formal-approach-to-game-design-and-game-research/

### Unreal Engine Gameplay Framework

Useful evidence that game runtimes naturally decompose into rules, player state, controllers, actors, cameras and related gameplay systems rather than one monolithic game object.

- https://dev.epicgames.com/documentation/unreal-engine/gameplay-framework-in-unreal-engine

### Unreal Engine Automation Test Framework

Useful evidence for layered automated validation including unit, feature, gameplay-level, content-stress and screenshot-comparison tests.

- https://dev.epicgames.com/documentation/unreal-engine/automation-test-framework-in-unreal-engine

### Unity profiling guidance

Useful evidence for distinguishing rapid editor iteration from representative target-platform performance validation.

- https://docs.unity3d.com/Manual/profiler-profiling-applications.html

### Unity AI tools, 2026

Useful current evidence that engine-aware AI execution is moving into editors through contextual assistants, agents and MCP surfaces. This strengthens the case for keeping reusable production intelligence above provider execution.

- https://unity.com/blog/unity-ai-how-to-get-started
- https://learn.unity.com/collection/build-with-unity-ai

### Roblox AI creation workflows

Useful current evidence that MCP-enabled tools can inspect an editor data model, create/run scripts, edit objects and playtest, again supporting a production-intelligence-above-execution architecture.

- https://create.roblox.com/docs/ai/accelerated-workflows

### Game Accessibility Guidelines

Useful baseline for treating inclusive controls, perception and cognitive accessibility as core game quality rather than an optional style layer.

- https://gameaccessibilityguidelines.com/full-list/

These sources seed questions and later challenge, current-practice and tooling research. They do not predetermine the final engine, skill list, artefact model, five-book corpus, Extension Pack catalogue or benchmark implementation.

---

# 30. Success Criterion

A successful `game-development-skills` bootstrap is not the generic Production Skills process with the word "game" substituted into it.

It must encode enough game-development understanding that later sessions can execute one stage at a time and answer, with evidence:

```text
What experience is the game trying to produce?
What mechanics and systems could produce it?
Which five complementary books establish the foundational domain corpus?
What did those books actually contribute, conflict on or fail to cover?
Which claims survive broader professional and current-practice challenge?
What is the cheapest playable way to test the current uncertainty?
What evidence is mechanical, behavioural or experiential?
What has been accepted and must be preserved?
What subsystem actually owns a failure?
What is the smallest sufficient correction?
What work belongs to another Production Skills domain?
What should the engine or execution tool do rather than this repository?
How will quality, balance, accessibility and performance be evaluated?
Which specialised behaviours justify Extension Packs rather than core rules or project instructions?
What five-book and challenge evidence supports each selected pack?
Can each implemented pack demonstrate reusable value beyond its showcase under a fair core-vs-pack comparison?
How can the installed skills and packs prove useful in a clean external game project?
```

The bootstrap succeeds when it can drive the repository from evidence-qualified research through playable evidence, six canonical specifications, progressive examples, Extension Packs, benchmarks, installation validation and maturity without prematurely building a universal game-development platform.
