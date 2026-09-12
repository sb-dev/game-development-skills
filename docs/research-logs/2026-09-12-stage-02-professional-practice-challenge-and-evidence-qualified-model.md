# Stage 2 — Professional Practice Challenge and Evidence-Qualified Game-Development Model

**Project:** `game-development-skills`  
**Bootstrap stage:** 2 — Challenge and Extend Professional Game-Development Practice  
**Status:** Complete  
**Date:** 12 September 2026

## 1. Stage purpose

Stage 1B produced a provisional game-development capability model from the five-book corpus. Stage 2 tests that model against broader professional, empirical and current-practice evidence and fills important gaps that the corpus could not support adequately.

The stage has two simultaneous responsibilities:

```text
challenge
→ determine which book-derived claims survive broader evidence

extend
→ investigate important professional responsibilities missing from the books
```

This stage deliberately studies **game-development practice before AI tooling**. It does not select engines, coding agents, MCPs, providers or editor automation. Those remain Stage 8 concerns.

The output is an **evidence-qualified domain model**, not a proposed skill list.

---

# 2. Canonical inputs

Primary repository inputs:

- [`2026-09-12-stage-01-project-goal-and-domain-boundary.md`](2026-09-12-stage-01-project-goal-and-domain-boundary.md)
- [`2026-09-12-stage-01a-domain-coverage-and-five-book-corpus.md`](2026-09-12-stage-01a-domain-coverage-and-five-book-corpus.md)
- [`2026-09-12-stage-01b-five-book-extraction-and-reconciliation.md`](2026-09-12-stage-01b-five-book-extraction-and-reconciliation.md)
- [`2026-09-07-game-development-skills-new-project-bootstrap-process.md`](2026-09-07-game-development-skills-new-project-bootstrap-process.md)

The Stage 1B handoff contained thirteen provisional capabilities and explicit challenge questions covering:

```text
accessibility
Games User Research
gameplay-design / technical-design / programming boundaries
prototyping and representative slices
performance / input latency / target builds
automated gameplay evaluation
multiplayer / network-aware production
live tuning
hard locks and lifecycle assumptions
```

Stage 2 treats those as hypotheses, not conclusions.

---

# 3. Research method

## 3.1 Evidence classes

Sources were evaluated by the kind of claim they can reasonably support.

| Evidence class | Typical source | What it can support | What it cannot establish alone |
|---|---|---|---|
| **Current official platform / engine guidance** | Microsoft XAG, Epic, Unity | Current platform/tool behaviour, supported validation methods, current implementation guidance | Universal game-design quality |
| **Current studio role / production evidence** | Ubisoft, PlayStation / studio job descriptions and practice articles | Responsibilities currently performed in real production teams | A universal studio organisation or job taxonomy |
| **Practitioner production case study** | GDC talks, studio engineering / design articles | A method used in a real project, its stated purpose, failures and trade-offs | Causality or universal superiority |
| **Applied research / professional handbook** | Games User Research literature | Research method, validity, evidence limitations, disciplinary practice | Project-specific design decisions |
| **Formal / academic design framework** | MDA and related research | Analytical distinctions and reasoning lenses | Mandatory production schema |
| **Foundational five-book corpus** | Stage 1B sources | Durable methods and concepts already extracted | Current platform/tool behaviour outside publication context |

Source authority and **claim disposition remain separate**. An authoritative source can still describe a method that is context-specific.

## 3.2 Research questions

The broader research was organised around these questions:

1. How do current professional teams divide game-design, technical-design and implementation responsibilities?
2. What evidence is used before expensive production begins?
3. How do prototypes differ from representative / vertical slices?
4. How are levels, missions, combat, AI and content integrated and iterated?
5. How do teams evaluate player experience without confusing QA, telemetry and user research?
6. What can automated tests establish, and where do they stop?
7. What current accessibility practice is strong enough to become a core responsibility?
8. What does target-platform evidence require?
9. When must networking constraints enter design rather than being deferred to implementation?
10. How does live balancing combine telemetry, expertise and player feedback?
11. Which Stage 1B claims should be retained, qualified, rejected or left unresolved?

## 3.3 Non-goals

This stage does **not**:

- standardise on a studio methodology;
- define one universal game-development lifecycle;
- turn job titles into skill boundaries;
- choose a game engine;
- choose automation products;
- define console certification requirements not publicly available;
- claim that one accessibility guideline covers every player need;
- claim that telemetry or automated agents can measure “fun” conclusively;
- design the Stage 3 game-thesis artefact yet.

---

# 4. Professional-practice map

Role names vary by studio, project scale and genre. The useful unit for this repository is therefore the **production responsibility**, with role titles recorded only as evidence that the responsibility exists in contemporary practice.

| Responsibility | Current professional evidence | Typical production work | Primary evidence | Boundary implication |
|---|---|---|---|---|
| Player / gameplay intent | Gameplay designer, lead designer | Mechanics, rules, game structure, modes, intended player behaviour | Prototype + target-player evidence | Game Development owns the gameplay decision and acceptance criteria |
| Systems / economy / progression | Systems / economy designer | Sources, sinks, progression, rewards, configuration, simulations, live tuning | Tables, simulations, telemetry, play | Core Game Development capability |
| Technical design | Technical designer, mission scripting | Translate design intent into visual scripting / data, validate integrations, troubleshoot workflows | In-engine behaviour + technical validation | Game Development may own design-facing implementation; general software architecture remains adjacent |
| Gameplay implementation | Gameplay programmer | Implement, debug, optimise and expose robust gameplay systems / tools | Automated tests + playable behaviour + profiling | Software Engineering owns general implementation quality; Game Development owns behavioural intent / acceptance |
| Level / mission design | Level / mission designer | Layout, objectives, pacing, branching, scripting, player guidance, integration | Maps / blockouts / playable missions / playtests | Core Game Development capability |
| Combat / AI / encounter design | Combat / AI designer | Enemy behaviours, combat systems, tuning, encounter consequences | Sandboxes, in-engine scripting, expert stress tests, player tests | Core Game Development behaviour; AI implementation internals may be adjacent engineering |
| Content integration | Technical design / technical art / animation / audio / gameplay teams | Turn specialist assets into runtime behaviour under engine and performance constraints | Representative build / runtime inspection | Game Development owns gameplay integration contract, not specialist asset production |
| Player research | Games User Research / UX research | Research questions, participant selection, study method, observation, analysis, reporting | Human behavioural + attitudinal evidence | Distinct evidence discipline; designers consume findings rather than replacing research method with intuition |
| QA | Games tester / QA | Reproduce defects, execute test briefs, verify fixes, stability / compatibility evidence | Deterministic reproduction and regression evidence | QA and GUR must not be conflated |
| Accessibility | Design + UX + engineering + accessibility specialists / players | Remove barriers in input, perception, timing, navigation and communication | Guideline checks + affected-player evidence | Core quality responsibility, not optional pack |
| Performance | Gameplay / engine / graphics / platform engineering plus design | Frame time, memory, load, bandwidth and content budgets on target hardware | Target build + profiler | Game Development owns gameplay-facing budget / acceptance; implementation optimisation remains engineering |
| Network-aware gameplay | Design + network / gameplay engineering | Timing assumptions, authority-visible behaviour, rollback / prediction consequences, network-sensitive balance | Real network tests + deterministic state / multi-client evidence + human play | Conditional core production concern for networked games |
| Live game health | Live balance / economy / analytics / design | Segment-aware balance, meta health, progression health, patch scope | Telemetry + expert play + player feedback + experiments | Conditional capability for updateable / live games |

### 4.1 Role boundaries are responsibility boundaries, not title boundaries

Current evidence is deliberately inconsistent in useful ways:

- ScreenSkills describes gameplay designers as defining mechanics / rules and acting as a bridge between technical and art teams.
- ScreenSkills describes gameplay programmers as implementing interactions, rules, tuning, bug fixing and optimisation.
- Ubisoft's current Senior Technical Designer role includes mission-flow integration, visual scripting, validation and troubleshooting.
- Ubisoft's current Senior Level Designer role owns missions from prototype to final implementation and connects narrative, AI, animation, audio and art through scripting.
- PlayStation / Naughty Dog combat-design evidence includes pitching, implementing, tuning and balancing enemy archetypes with AI programmers and animators.

The conclusion is **not** that every studio should create all of these roles. The durable rule is:

> Model ownership around **intent, runtime behaviour, evidence and handoff**, not around an assumed universal org chart.

Sources:

- <https://www.screenskills.com/job-profiles/browse/games/design/gameplay-designer/>
- <https://www.screenskills.com/job-profiles/browse/games/programming/gameplay-programmer/>
- <https://www.screenskills.com/job-profiles/browse/games/design/level-designer/>
- <https://jobs.smartrecruiters.com/Ubisoft2/744000148308939>
- <https://jobs.smartrecruiters.com/Ubisoft2/744000148310424>
- <https://careers.playstation.com/senior-game-designer-combat/job/6117785004>

---

# 5. Challenge findings

## 5.1 Player-experience intent is useful, but it is not evidence of achieved experience

### Stage 1B hypothesis

Express intended player experience separately from features and evaluate the game against that intent.

### Broader evidence

The MDA framework independently supports separating implemented mechanics from runtime dynamics and player-facing aesthetics / experience, explicitly to help designers reason across implementation and result.

Games User Research defines its purpose around obtaining data-informed feedback so the intended experience created during design is actually realised by players.

### Challenge result

**SUPPORTED, with an evidential qualification.**

A player-experience goal is valuable as:

```text
coordination target
hypothesis
playtest research question
decision criterion
```

It is **not proof** that the experience occurs.

### Core consequence

Every material experiential claim should be representable as:

```text
intent
→ observable / reportable evidence question
→ method
→ result
→ confidence / limitations
→ decision
```

Do not operationalise subjective experience so aggressively that the proxy becomes the goal.

Sources:

- <https://aaai.org/papers/ws04-04-001-mda-a-formal-approach-to-game-design-and-game-research/>
- <https://academic.oup.com/book/26677/chapter-abstract/195455083>

**Disposition:** `SUPPORTED FINDING / QUALIFIED EVIDENCE CLAIM`.

---

## 5.2 Prototype fidelity should be selected by question, not by a universal ladder

### Stage 1B hypothesis

Use the cheapest representation capable of answering the current uncertainty.

### Broader evidence

Professional prototype material repeatedly distinguishes prototype purpose from production fidelity:

- GDC prototype practice describes focused prototypes as a way to make decisions, discard failed features and reduce production waste.
- Finji explicitly distinguishes prototypes, gameplay-mechanic tests and vertical slices because they communicate different evidence.
- Volition uses its vertical-slice gate to ask whether the team understands **what it is making and how to make it**, which is a production-readiness question rather than only a mechanic-fun question.

### Challenge result

**STRONGLY SUPPORTED.**

The useful rule is:

```text
uncertainty
→ minimum variables that must be represented
→ cheapest medium preserving those variables
→ explicit learning criterion
```

A prototype can be discarded after answering its question. A representative slice may deliberately contain production-quality parts because its question is different.

Sources:

- <https://www.gdcvault.com/play/1012473/Prototyping-Based-Design-A-Better>
- <https://www.gdcvault.com/play/1013252/Advanced>
- <https://gdcvault.com/play/1025674/So-You-re-Ready-to>
- <https://gdcvault.com/play/1022328/The-Vertical-Slice>

**Disposition:** `SUPPORTED FINDING`.

---

## 5.3 “Vertical slice” is a purpose-sensitive term, not a universal fidelity contract

### Stage 1B hypothesis

Use `representative slice` as a generic concept and require purpose / fidelity to be explicit.

### Broader evidence

Professional sources use overlapping but non-identical language:

- Volition treats the vertical slice as a readiness gate between pre-production and production.
- Finji distinguishes a vertical slice from prototypes and mechanic tests in a publishing / communication context.
- GDC 2026 production workshop material places first playable and vertical slice among pre-production deliverables alongside core loops, tools / pipelines and a revised production plan.
- Insomniac's *Marvel's Spider-Man* technical postmortem explicitly includes “making the wrong vertical slice” among lessons learned, reinforcing that having a slice is not itself evidence that the right production risk was tested.

### Challenge result

**SUPPORTED AND STRENGTHENED.**

Repository guidance should require a slice to state:

```text
what uncertainty / readiness claim it proves
which systems and content layers must be representative
what may remain temporary
what target environment is required
what acceptance evidence permits production expansion
```

Do not infer readiness from the label `vertical slice`.

Sources:

- <https://gdcvault.com/play/1022328/The-Vertical-Slice>
- <https://gdcvault.com/play/1025674/So-You-re-Ready-to>
- <https://media.gdcvault.com/gdc2026/Slides/Marty_Fleur_ProductionWorkshopPart2.pdf>
- <https://www.gdcvault.com/play/1026496>

**Disposition:** `SUPPORTED FINDING`.

---

## 5.4 Hard concept locks are not defensible as a universal rule

### Stage 1B tension

Some book material described concept decisions as fixed; the reconciled model proposed explicit commit / reopen semantics instead.

### Broader evidence

Professional practice consistently describes iteration through prototypes, playtests, tuning and production evidence. Current roles explicitly include redesigning, rebalancing, troubleshooting and reworking systems when quality targets are not met.

At the same time, production evidence supports stronger change control as downstream cost rises:

- Volition frames pre-production exit as a readiness decision.
- Riot's live-balance process identifies small tuneable levers late in a champion's development because other disciplines have moved on and wide changes are expensive.
- Ubisoft economy roles describe simulation before implementation and rework when required, not immutable early decisions.

### Challenge result

The absolute lock is **REJECTED**.

The stronger replacement is:

```text
cheap / local / reversible decision
→ low approval cost

accepted dependency with downstream consumers
→ explicit commitment record

material contrary evidence
→ reopen request
→ impact analysis
→ responsible approval
→ smallest sufficient revision
→ regression validation
```

A commitment is therefore a **change-cost boundary**, not a claim of infallibility.

Sources:

- <https://gdcvault.com/play/1022328/The-Vertical-Slice>
- <https://2xko.riotgames.com/en-us/news/dev/2xko-live-balance-philosophy/>
- <https://jobs.smartrecruiters.com/ubisoft2/744000120504404>

**Disposition:** `REJECTED IDEA AS ABSOLUTE / ADAPTED METHOD`.

---

## 5.5 “Primary mechanics must be shippable before secondary mechanics” is a heuristic, not a law

### Stage 1B hypothesis

Use dependency-aware core-first development, but integrate systems as soon as their interaction becomes the dominant uncertainty.

### Broader evidence

Contemporary production evidence shows high interdependence:

- combat designers work with AI, animation, programming and levels while mechanics are being prototyped and tuned;
- mission designers connect narrative, AI, animation, audio, art and branching logic during implementation;
- AI designers iterate NPC behaviour against the overall combat experience;
- network-sensitive games may need online constraints present from the beginning.

### Challenge result

**QUALIFIED METHOD.**

Use core-first ordering when it reduces uncertainty. Break the ordering when the core cannot be judged without its dependency.

Examples:

```text
movement
→ may require camera + representative space early

combat
→ may require enemy behaviour + hit reaction + feedback + arena early

network fighter
→ may require rollback / input-delay assumptions from design phase

economy
→ may be usefully isolated in a spreadsheet / simulation before content
```

**Disposition:** `CONTEXT-DEPENDENT HEURISTIC`.

Sources:

- <https://careers.playstation.com/senior-game-designer-combat/job/6117785004>
- <https://jobs.smartrecruiters.com/Ubisoft2/744000148310424>
- <https://jobs.smartrecruiters.com/Ubisoft2/744000127417779-senior-ai-game-designer-tom-clancy-s-the-division-3->
- <https://2xko.riotgames.com/en-us/news/dev/how-2xko-handles-online-play/>

---

# 6. Game-design / technical-design / gameplay-programming boundary

Stage 1B left this unresolved. Stage 2 can now bound it more precisely.

## 6.1 Current evidence

Current practice demonstrates a spectrum rather than a clean “design does not implement” split:

```text
gameplay designer
→ mechanic / rule / gameplay specification

level / mission / combat / AI designer
→ often hands-on in editor, visual scripting, data and tuning

technical designer
→ implementation-facing design logic, scripting, validation, tools and troubleshooting

gameplay programmer
→ production code, system implementation, debugging, optimisation, reusable runtime support
```

Ubisoft's current technical-design role explicitly includes integration, validation, visual scripting and workflow troubleshooting. Ubisoft's gameplay-programming role owns technical realisation from early prototypes to final implementation, including performance-aware code. PlayStation combat-design roles include in-editor implementation and tuning while collaborating with programmers.

## 6.2 Evidence-qualified boundary

The durable project split should be:

### Game Development owns

```text
intended gameplay behaviour
mechanics / rules / state semantics
design-facing data / parameters
required debug / tuning affordances
prototype behaviour
in-editor / visual-script implementation when it is the natural design surface
playability acceptance criteria
cross-domain gameplay integration
game-specific performance / latency budgets
observed gameplay defect diagnosis
```

### Software Engineering owns

```text
general code architecture
maintainability / code quality
engine-level implementation
concurrency / memory / low-level networking
infrastructure
build systems / CI
non-game-specific test architecture
security engineering
general refactoring
```

### Shared seam

```text
Game Development says what runtime behaviour must exist and how it will be accepted.
Software Engineering decides how production software should robustly realise that behaviour.
```

The seam can move on a small project where one person owns both responsibilities. The conceptual separation still matters because it prevents game-design reasoning from being reduced to code generation.

Sources:

- <https://www.screenskills.com/job-profiles/browse/games/design/gameplay-designer/>
- <https://www.screenskills.com/job-profiles/browse/games/programming/gameplay-programmer/>
- <https://jobs.smartrecruiters.com/Ubisoft2/744000148308939>
- <https://jobs.smartrecruiters.com/Ubisoft2/744000145464298>
- <https://careers.playstation.com/combat-designer-contract/job/5650786004>

**Gap status:** `ADDRESSED / BOUNDED`.

---

# 7. Levels, missions, combat, AI and content integration

## 7.1 Level and mission ownership is more than geometry

Current Ubisoft mission-level-design evidence includes:

```text
prototype → final implementation
pacing
structure
objectives
progression
player guidance / readability
branching / multiple outcomes
visual scripting
narrative integration
AI integration
animation / audio / art integration
```

This supports Stage 1B's conclusion that a level is not a container added after mechanics are “finished.” It is a gameplay system where spatial, mission, information and content constraints interact.

## 7.2 Combat / AI iteration is cross-disciplinary

Current PlayStation and Ubisoft evidence shows combat / AI designers:

- prototype and tune enemy behaviours;
- work directly with AI programmers and animators;
- use behaviour trees / node graphs or in-engine scripting;
- evaluate against the overall combat loop;
- iterate from playtest feedback;
- manage production risk and scope.

### Evidence-qualified rule

For encounter / combat / mission work, the smallest useful test unit is often a **coupled scenario**:

```text
player capability
+
enemy / system behaviour
+
space
+
feedback
+
relevant content timing
→ observable encounter outcome
```

Do not diagnose an encounter exclusively from one asset or rule when the failure appears only through composition.

Sources:

- <https://jobs.smartrecruiters.com/Ubisoft2/744000148310424>
- <https://careers.playstation.com/senior-game-designer-combat/job/6117785004>
- <https://jobs.smartrecruiters.com/Ubisoft2/744000127417779-senior-ai-game-designer-tom-clancy-s-the-division-3->

**Stage 1B capability impact:** strengthens C7, C11 and C12.

---

# 8. Systems, economy, progression and balancing

## 8.1 Simulation is established professional practice for suitable systems

Ubisoft's current game-economy roles explicitly include:

```text
sources / sinks
progression
rewards
events / quests
configuration parameters
Excel / simulator tooling
data-driven simulation
live player data
rebalancing / rework
```

This independently supports the five-book claim that discrete systemic uncertainty can often be tested before full playable content exists.

### Evidence-qualified rule

Use analytical or simulated evidence when the important uncertainty is representable as data / state / resource dynamics.

Do not infer player motivation or satisfaction from a stable spreadsheet economy alone.

Source:

- <https://jobs.smartrecruiters.com/ubisoft2/744000120504404>
- <https://jobs.smartrecruiters.com/Ubisoft2/744000148518519>

**Disposition:** `SUPPORTED FINDING`.

## 8.2 Balance is multi-dimensional and population-dependent

Riot's 2XKO live-balance description is a valuable current case because it combines:

- high-skill expert stress testing during development;
- small late-stage tuning levers;
- win rate and pick rate segmented by skill;
- matchup and move-usage data;
- qualitative player discussion / streams / surveys;
- explicit willingness to let the meta evolve before intervening;
- concern for strategic diversity rather than one global numerical target.

The 47–53% range reported by 2XKO is a **game-specific investigation threshold**, not a reusable standard.

### Evidence-qualified balance model

```text
balance question
→ game-specific objective
→ relevant population / skill cohort
→ mechanical / statistical evidence
→ strategy / counterplay evidence
→ human experience evidence
→ intervention threshold
→ smallest tuneable lever
→ regression across affected cohorts
```

Possible dimensions include:

```text
win rate
pick / use rate
matchup spread
strategy diversity
dominant / degenerate strategy
counterplay
learning burden
new-player vs expert performance
resource / progression health
time-to-kill / time-to-complete
player frustration / perceived unfairness
```

No single metric is “balance.”

Source:

- <https://2xko.riotgames.com/en-us/news/dev/2xko-live-balance-philosophy/>

**Stage 1B impact:** C6 strengthened; any universal balance threshold rejected.

---

# 9. Games User Research, playtesting and telemetry

Stage 1B identified specialist GUR as a major gap. Broader evidence materially changes C9.

## 9.1 Playtesting needs a research question

Games User Research literature treats method choice as a function of the research problem. The player-research framework explicitly distinguishes methods by the kind of evidence needed around appeal, understanding, usability, experience and monetisation.

Therefore:

```text
“run a playtest”
```

is under-specified.

A useful study contract should state:

```text
research objective / design question
claim or uncertainty
participant criteria
build / scenario
method
what behaviour will be observed
what attitudes will be collected
what telemetry will be captured
known bias / validity threats
analysis method
what decision the evidence can influence
```

Sources:

- <https://academic.oup.com/book/26677/chapter-abstract/195455905>
- <https://academic.oup.com/book/26677/chapter-abstract/195455186>

## 9.2 Participant selection matters

The intended player population is not interchangeable with:

```text
the designer
team members
friends
expert players
whoever is easiest to recruit
```

Different research questions legitimately require different participant profiles.

Examples:

```text
first-time onboarding
→ fresh players matching relevant target characteristics

high-skill exploit / balance stress
→ expert / high-skill players

accessibility barrier
→ players affected by the relevant access need

broad live behaviour
→ telemetry segmented by meaningful cohorts
```

## 9.3 Test context introduces bias

GUR literature explicitly discusses the tension between controlled lab evidence and ecological validity. The repository therefore must not label a playtest “objective” merely because it generated numbers.

Record at least:

```text
participant selection bias
observer / facilitator effects
build maturity
test environment
novelty / first-exposure effects
sample size limitation
measurement / instrumentation limitation
```

Source:

- <https://academic.oup.com/book/26677/chapter-abstract/195460947>

## 9.4 Telemetry and human research are complementary

Games User Research literature describes analytics as complementary to other research methods, not a replacement for them.

A strong working distinction is:

```text
telemetry
→ what happened, how often, for whom, and under what measurable state

observation
→ what the player did in context

interview / survey
→ what the player reports or believes

research synthesis
→ what those sources plausibly mean for the design question
```

Telemetry can reveal a drop-off. It cannot by itself explain why the player stopped.

Source:

- <https://academic.oup.com/book/26677/chapter-abstract/195460224>

## 9.5 C9 revision

Rename the provisional capability:

```text
C9 — Plan playtests and interpret evidence
```

as:

```text
C9 — Design player research and synthesise play evidence
```

The capability must decide **which evidence source is appropriate**, not merely execute a generic playtest.

**Gap status:** `ADDRESSED / CAPABILITY STRENGTHENED`.

---

# 10. QA is not Games User Research

## 10.1 Current QA evidence

ScreenSkills describes games testers as executing specific test briefs, documenting reproducible defects and retesting after fixes.

This is different from a research study whose purpose is to understand intended player experience.

### Core distinction

```text
QA question
→ is the product behaving according to specified correctness / stability expectations?

GUR question
→ how do relevant players understand, use and experience the product, and why?
```

There is overlap in observable behaviour, but neither discipline subsumes the other.

### Example

```text
player cannot open a door

QA
→ input event fails because state transition is broken

GUR
→ player never understood that the door is interactive

both
→ possible in the same symptom; evidence determines the owner
```

Source:

- <https://www.screenskills.com/job-profiles/browse/games/quality-assurance/games-tester/>

**Stage 1B impact:** strengthens C9 and C12; adds evidence-process failure class.

---

# 11. Automated gameplay evaluation

Stage 1B correctly bounded automation, but Stage 2 can now make the boundary more concrete.

## 11.1 Current automation capabilities

Epic's current Unreal Engine documentation exposes automation for:

```text
unit / API verification
feature tests
smoke tests
content stress tests
screenshot comparison
functional gameplay tests
multi-process sessions
client / server launches
networking tests
logs / crash monitoring
```

Gauntlet can orchestrate sessions involving multiple clients and a server. Unreal's network-testing documentation also records an important limitation: a single Functional Test does not directly provide every multi-instance replicated-state assertion.

### What this evidence establishes

Automation can credibly support claims such as:

```text
state transition occurred
content loads
map is reachable
scenario completes
server / clients boot
expected replicated state is observed through an appropriate harness
known crash does not reproduce
visual regression is absent within the test's tolerance
mechanical invariant holds
```

### What it does not establish alone

```text
fun
clarity
emotional impact
fairness as experienced by players
satisfaction
readability for a target population
accessibility for affected players
```

Sources:

- <https://dev.epicgames.com/documentation/en-us/unreal-engine/automation-test-framework-in-unreal-engine>
- <https://dev.epicgames.com/documentation/en-us/unreal-engine/gauntlet-automation-framework-in-unreal-engine>
- <https://dev.epicgames.com/documentation/unreal-engine/testing-and-debugging-networked-games-in-unreal-engine>

## 11.2 Evidence-qualified automation rule

```text
automate the claim when the claim has a machine-observable oracle
```

Do not replace a judgement-heavy claim with an arbitrary proxy merely because the proxy is easy to automate.

## 11.3 Generative / agent playtests

Stage 2 finds no sufficient evidence to treat a general autonomous game-playing agent as an experiential authority.

Agents may later be useful for:

```text
state exploration
reachability
path / strategy search
stress testing
repeated economic runs
edge-case generation
```

but Stage 8 must evaluate actual tool capabilities and Stage 14 must benchmark them.

**Gap status:** `BOUNDARY ADDRESSED; TOOL CHOICE DEFERRED`.

---

# 12. Accessibility becomes an explicit core capability

The five-book corpus was insufficient here. Current Xbox Accessibility Guidelines provide strong, current platform guidance and explicitly frame accessibility across design, development and testing.

## 12.1 Input is more than remapping buttons

Current XAG 107 covers barriers including:

```text
required input device
analog-only operation
speed of input
repeated presses
long holds
complex simultaneous inputs
control sensitivity
game speed
remappable actions
toggles / auto-hold
menu operability
updated prompts after remapping
```

This directly challenges an overly narrow definition of “accessible controls.”

## 12.2 Perception and information are multi-channel problems

The XAG catalogue separately covers:

```text
text display
contrast
additional visual / audio channels
subtitles / captions
audio accessibility
screen narration
object clarity
haptics
audio description
UI navigation
time limits
motion / visual distraction
photosensitivity
communication
```

The relevant subset depends on the game.

## 12.3 Accessibility is an interaction constraint, not a late compliance pass

An input requirement can make progression impossible. Therefore accessibility affects:

```text
mechanic design
input assumptions
timing windows
feedback channels
onboarding
UI / settings availability
playtesting participants
release validation
```

Waiting until content completion can make remediation far more expensive.

## 12.4 New capability

Add:

```text
C14 — Design and validate inclusive gameplay access
```

This is a core capability, although any given criterion is activated only when applicable.

### C14 responsibility

For relevant interactions:

```text
identify required player perception / action
identify exclusion risks
provide alternatives where appropriate
ensure settings are reachable before the barrier
preserve gameplay intent where possible
validate with deterministic checks where possible
validate with affected players for experiential / usability claims
```

### Boundary

Game Development owns gameplay accessibility requirements and runtime acceptance. UI/UX may own interface-specific design. Software Engineering owns robust implementation. Specialist accessibility expertise may deepen the work but does not make baseline accessibility optional.

Sources:

- <https://learn.microsoft.com/en-us/xbox/accessibility/guidelines>
- <https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107>
- <https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/101>

**Gap status:** `CORE GAP CLOSED AT BASELINE / SPECIALIST DETAIL REMAINS EXTENSIBLE`.

---

# 13. Target-platform performance and responsiveness

## 13.1 Historical thresholds are not universal requirements

Stage 1B marked Swink's old numeric perception / response thresholds for current challenge. Current platform practice supports the **dimension**, not a universal number.

Epic's current performance guidance defines performance relative to target hardware and focuses on frame time, FPS, CPU, GPU, memory and network profiling. Unity's current guidance explicitly supports recording profiler data on the selected target platform to obtain real performance metrics.

### Evidence-qualified rule

```text
performance claim
→ named target class / hardware
→ representative build / scene
→ appropriate profiling setup
→ frame / memory / load / network evidence
→ gameplay-facing acceptance criterion
```

Editor-only data can be useful for diagnosis but is not sufficient release evidence.

Sources:

- <https://dev.epicgames.com/documentation/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine>
- <https://docs.unity3d.com/6000.0/Manual/profiling-target-device.html>

## 13.2 Performance is gameplay when it changes interaction

Frame pacing, stalls, load transitions and latency can alter:

```text
input responsiveness
combat timing
camera motion
perceived control
animation readability
network fairness
```

Therefore Game Development must be able to state gameplay-facing budgets and reject a build that violates them, even when an adjacent engineering discipline owns the optimisation.

## 13.3 No universal FPS rule

Current Epic guidance references common 30 / 60 / 120 FPS targets as examples tied to project budgets and target hardware. They are **not** repository defaults.

The project must record the chosen target and why.

**Stage 1B impact:** C13 upgraded from `under-challenged` to `supported core capability`.

---

# 14. Network-aware gameplay must enter early when it changes the design

Stage 1B lacked sufficient network evidence. Riot's current 2XKO engineering account supplies a strong counterexample to treating networking as a late implementation concern.

## 14.1 Online-first design evidence

2XKO reports that its team:

- integrated rollback technology and moved daily playtests over the real internet early;
- built character moves, animations and effects against online behaviour from the design phase;
- uses a central authority for state / time;
- intentionally applies a fixed input-delay model consistently online and offline;
- invests heavily in frame pacing so timing is consistent across PC / console and online / offline;
- runs a deterministic server-side copy of matches for validation and downstream statistics.

This is one game's architecture, not a universal network recipe. The important reusable principle is that **network behaviour was part of the gameplay contract**.

Source:

- <https://2xko.riotgames.com/en-us/news/dev/how-2xko-handles-online-play/>

## 14.2 Conditional capability

Add:

```text
C15 — Design and validate network-sensitive gameplay constraints
```

activated only when network behaviour is material to the intended experience.

### C15 owns

```text
player-facing latency / consistency assumptions
authority-visible gameplay expectations
network-sensitive timing / control requirements
acceptable degraded behaviour
multiplayer state / fairness acceptance cases
network test scenarios
```

### C15 does not own

```text
socket / transport implementation
server infrastructure
encryption
DDoS architecture
low-level replication framework design
```

Those remain engineering concerns unless a game-specific decision requires an acceptance constraint.

## 14.3 Minimum-coupled-proof rule

If latency, rollback, replication or authority changes the feel / fairness / validity of a mechanic, the network condition belongs in the **minimum useful prototype**, not after the mechanic is approved offline.

**Gap status:** `ADDRESSED / CONDITIONAL CORE CAPABILITY`.

---

# 15. Live tuning and longitudinal game health

Live tuning is not relevant to every game, but the Stage 2 evidence is sufficient to define a conditional responsibility.

## 15.1 Current practice

Riot's 2XKO balance process combines:

```text
expert game analysis
early stress tests
playtests
small late-stage tuning levers
skill-segmented win / pick / matchup / usage data
qualitative community feedback
patch scheduling
meta observation
```

Ubisoft economy roles likewise combine simulations, configuration, live player data and ongoing progression / reward health.

## 15.2 Conditional capability

Add:

```text
C16 — Evaluate and tune longitudinal game health
```

for games that continue changing after release or whose balance depends on population behaviour over time.

### C16 reasoning loop

```text
health objective
→ cohort / population
→ telemetry + qualitative evidence
→ distinguish adaptation from defect
→ select smallest intervention
→ validate locally
→ release
→ monitor side effects / new meta
→ retain / revise / revert
```

### Important qualification

A strategy becoming popular is not automatically a balance bug. Riot explicitly describes allowing players time to discover counters before intervening.

Therefore:

```text
meta shift ≠ defect by default
```

Source:

- <https://2xko.riotgames.com/en-us/news/dev/2xko-live-balance-philosophy/>
- <https://jobs.smartrecruiters.com/Ubisoft2/744000148518519>

**Gap status:** `ADDRESSED AS CONDITIONAL CAPABILITY`.

---

# 16. Evidence taxonomy

Stage 2 can now replace the looser Stage 1B evidence language with an explicit taxonomy.

## 16.1 Evidence types

| Evidence type | Best for | Examples | Cannot establish alone |
|---|---|---|---|
| **Specification / static analysis** | Rule consistency, declared state, content contracts | tables, state models, validators | runtime interaction quality |
| **Deterministic automated test** | Reproducible machine-observable invariants | state transition, save/load invariant, reachability fixture | subjective player response |
| **Simulation** | Repeated systemic outcomes | economy stability, probability distribution, progression runs | how real players choose / feel unless behaviour model is validated |
| **Bot / agent play** | Search / stress / repeated state traversal | exploit search, route exploration | human experiential authority |
| **Runtime instrumentation / telemetry** | What happened at scale | completion, death, pick, usage, progression | why it happened or how it felt |
| **Replay / trace** | Reconstructing behaviour and state | combat sequence, state divergence | general population meaning without analysis |
| **Expert review / stress test** | Domain-specific problems / high-skill edge cases | combat analysis, balance exploit | representative mainstream player experience |
| **Human usability / comprehension study** | Discoverability, understanding, control, navigation | onboarding, objective clarity | broad population prevalence without suitable sampling |
| **Human experiential research** | Felt quality, emotional response, satisfaction, perceived fairness | interview, survey, observed reaction | mechanical correctness |
| **Accessibility evaluation** | Barriers / alternatives / affected-user experience | guideline review + disabled-player research | every impairment / platform need from one test |
| **Target-platform profiling** | Frame, memory, load, bandwidth, platform behaviour | profiler capture on target build | fun / clarity |
| **QA reproduction** | Defect existence and regression | steps, logs, build, expected/actual | underlying player meaning |

## 16.2 Evidence selection rule

```text
claim
→ what observable evidence could falsify it?
→ cheapest credible evidence source
→ limitations
→ decision authority
```

Do not choose the evidence source because it is convenient to automate.

## 16.3 Evidence record

A material game-development decision should be able to preserve:

```text
claim / question
context / build
method
participants / scenario if applicable
evidence
limitations / confidence
decision
decision owner
reopen condition
regression fixture if practical
```

This is a conceptual contract. Stage 3 onward decides the minimum concrete artefacts.

---

# 17. Deterministic, generative, judgement-heavy and tool-dependent work

Stage 2 requires these to remain distinct.

## 17.1 Primarily deterministic

```text
rule / state validation
known reachability cases
save / load invariants
content-reference integrity
known collision / trigger cases
build boot / smoke tests
reproducible network-state cases
performance capture
specified accessibility configuration checks
```

## 17.2 Simulation / search-heavy

```text
economy distributions
probability / progression runs
strategy search
procedural reachability
stress / soak scenarios
agent exploration
```

These may be deterministic under a fixed seed but represent a search / statistical problem rather than one assertion.

## 17.3 Judgement-heavy

```text
fun
game feel quality
emotional effect
perceived fairness
readability
challenge quality
meaningful choice
narrative / gameplay fit
strategic diversity quality
```

These require human or expert judgement appropriately scoped to the claim.

## 17.4 Tool-dependent

```text
engine editor manipulation
runtime inspection
profiling
network emulation
build execution
capture
input simulation
platform deployment
```

Stage 8 will choose execution capabilities. Stage 2 defines only what evidence those tools must eventually provide.

---

# 18. Claim-disposition register

The following table directly challenges material Stage 1B claims.

| Stage 1B claim / question | Broader evidence | Stage 2 disposition | Core implication |
|---|---|---|---|
| Separate intended player experience from feature list | MDA + GUR support intent / result distinction | **SUPPORTED** | Keep C1; experience remains hypothesis until tested |
| Playtest throughout development | GUR + professional production strongly support recurring player evidence | **SUPPORTED, CADENCE CONTEXTUAL** | No universal weekly / N-player rule |
| Cheapest adequate representation | Prototyping literature and studio practice support focused proofs | **SUPPORTED** | Keep C3 |
| Prototype question should drive medium / fidelity | Strong professional support | **SUPPORTED** | Make learning criterion explicit |
| Metrics can establish experiential quality | GUR shows metrics complement other methods | **REJECT AS SOLE EVIDENCE** | C9 must synthesise evidence |
| Machinations / resource models generalise to all games | No broader evidence supports universality; book already bounds itself | **BOUNDED METHOD** | Optional modelling technique only |
| Emergence vs progression is a complete taxonomy | MDA + modern role evidence shows many other useful dimensions | **ANALYSIS LENS ONLY** | No repository taxonomy built around it |
| Concept decisions should never change | Iterative professional evidence contradicts absolute rule | **REJECTED ABSOLUTE** | Commit / reopen semantics |
| Primary mechanics should always reach shippable polish before secondary | Cross-system / network evidence contradicts universal sequencing | **CONTEXT-DEPENDENT HEURISTIC** | Integrate when dependency becomes material |
| Swink's “true game feel” defines game feel generally | Turn-based / indirect games and current design practice make this too narrow | **SPECIALIST LENS** | C5 remains broader interaction feel / feedback |
| Architecture-derived level principles predict player behaviour | Useful practitioner lens, but GUR requires observed player evidence | **QUALIFIED HYPOTHESIS SOURCE** | Use to design tests, not certify quality |
| Historical frame / response thresholds should become requirements | Current profiling practice is target-specific | **REJECT NUMERIC UNIVERSALITY** | C13 target-specific budgets |
| “Vertical slice” has one stable meaning | GDC practice uses the term for different goals / audiences | **REJECT UNIVERSAL DEFINITION** | Require declared evidence purpose |
| One-variable-at-a-time tuning is always required | Useful causal isolation technique, but coupled systemic fixes sometimes require coordinated changes | **HEURISTIC** | Prefer minimal causal scope, not artificial single-variable rule |
| Human play remains authoritative for experiential claims | GUR strongly supports human evidence; automation sources do not replace it | **SUPPORTED** | Preserve human authority by claim class |
| Automation can establish mechanical evidence | Current engine automation strongly supports this | **SUPPORTED / BOUNDED BY ORACLE** | Automate machine-observable claims |
| Target-platform behaviour matters | Current Epic / Unity guidance strongly supports | **SUPPORTED** | C13 core |
| Accessibility is a core quality dimension | Current XAG strongly supports | **SUPPORTED / STRENGTHENED** | New C14 |
| Network can be deferred until after gameplay proof | 2XKO provides strong counterexample where net constraints shape gameplay | **REJECT AS UNIVERSAL** | New conditional C15 |
| Global win rate is sufficient balance evidence | Live-balance practice contradicts | **REJECTED** | Cohort + strategy + qualitative evidence |
| Late changes require stronger justification | Production and live-balance evidence support change-cost reasoning | **SUPPORTED** | C10 commitment gradient |

---

# 19. Failure taxonomy

The failure taxonomy records **symptom class → likely evidence → smallest responsible scope**. It does not pre-assign one team as the owner before diagnosis.

## 19.1 Intent / gameplay proposition failures

| Failure | Detection | Candidate responsible scope | Smallest first repair |
|---|---|---|---|
| Unclear player goal | fresh-player observation, objective comprehension study | objective / feedback / level / UI / thesis | clarify cue or local objective before rewriting whole game |
| Weak core loop | repeated play + progression / retention evidence + expert review | loop reward / challenge / decision structure | alter weakest loop link / reward / friction and retest |
| Experience-goal mismatch | target-player research | mechanics / pacing / presentation / target assumption | change responsible interaction rather than relabelling intent |
| Wrong audience assumption | recruitment / study evidence | target definition / onboarding / challenge | reopen audience assumption and impacted decisions explicitly |

## 19.2 Input / interaction / feedback failures

| Failure | Detection | Candidate responsible scope | Smallest first repair |
|---|---|---|---|
| Unresponsive control | input-to-output trace + target build + human play | mapping / processing / frame / network / animation | isolate latency source or response curve |
| Control ambiguity | player error pattern + mapping inspection | state / mapping / prompt / feedback | remove ambiguous mapping or clarify state |
| Poor consequence feedback | observation + cue-layer test | audio / VFX / animation / UI / haptic | strengthen or add redundant cue |
| State overwhelm | novice observation | state count / mapping / onboarding | stage exposure or simplify context-sensitive actions |
| Input accessibility blocker | XAG review + affected-player test | action mapping / timing / alternative input | provide action-level alternative / timing option where compatible |

## 19.3 System / economy / balance failures

| Failure | Detection | Candidate responsible scope | Smallest first repair |
|---|---|---|---|
| Runaway economy | simulation + telemetry | source / sink / multiplier / feedback loop | adjust responsible flow / cap / friction |
| Economy collapse / starvation | simulation + progression runs | resource availability / gate | add or tune source / recovery path |
| Dominant strategy | expert stress + telemetry + strategy analysis | reward / cost / counterplay / system interaction | improve counterplay or tune enabling parameter |
| Trivial strategy | search / expert play | challenge / exploit / scoring | remove degenerate reward or restore decision cost |
| Progression dead end | state / reachability test + player evidence | gate / resource / save state | restore reachable path / recovery source |
| Difficulty spike | cohort telemetry + fresh-player play | encounter / mechanics combination / progression | tune responsible encounter / prerequisite exposure |
| Skill-cohort imbalance | segmented analytics + expert / novice evidence | skill scaling / accessible power | tune cohort-relevant interaction, not global value blindly |

## 19.4 Level / mission / encounter / AI failures

| Failure | Detection | Candidate responsible scope | Smallest first repair |
|---|---|---|---|
| Level-flow failure | observation / route trace | layout / guidance / mission state | change cue, route or local scene before full layout |
| Unreadable combat | player observation + expert review | enemy telegraph / VFX / camera / space | fix responsible cue / timing / sightline |
| Unfair information asymmetry | play evidence + state review | information timing / hidden state | expose necessary information or change decision cost |
| AI deadlock | functional test / soak / repro | behaviour state / navigation / encounter | repair transition / escape condition |
| AI exploit | expert / agent stress test | behaviour / threat / nav / rules | fix exploit-enabling state or countermeasure |
| Unreachable content | navigation / reachability / QA | gate / collision / spawn / script | repair local gate / spawn / geometry |
| Retry-cost failure | observation / completion attempts | checkpoint / reset / load | move checkpoint or reduce reset cost |

## 19.5 Cross-domain integration failures

| Failure | Detection | Candidate responsible scope | Smallest first repair |
|---|---|---|---|
| Animation timing breaks gameplay | frame / event inspection + play | gameplay timing contract / animation event | align event / cancel / window rather than replace asset family |
| Art obscures affordance | playtest + screenshot / contrast analysis | material / silhouette / lighting / cue | local visual correction |
| Audio cue fails gameplay role | audio-off / visual-off comparative test | event / mix / asset / redundancy | fix trigger / priority / redundant channel |
| Collision mismatches visual | QA + movement trace | collider / geometry contract | local collider / asset integration fix |
| Narrative trigger breaks flow | state trace + mission play | trigger / state / pacing | repair trigger or local dependency |
| Content causes performance spike | target profiler | asset budget / spawning / VFX / script | optimise or reduce responsible content unit |

## 19.6 Runtime / state / network failures

| Failure | Detection | Candidate responsible scope | Smallest first repair |
|---|---|---|---|
| Soft lock | deterministic scenario / QA / replay | state transition / gating | restore exit / reset / transition |
| Save-state corruption | save/load invariant test | serialization / schema / migration | repair offending state / migration; engineering owner likely |
| Physics instability | replay / deterministic scenario / stress | timestep / collider / solver / mechanic | constrain problematic interaction or implementation |
| Network desynchronisation | multi-client trace / checksums | deterministic state / replication / authority | isolate divergent state path |
| Network unfairness / lag-sensitive failure | real-network / emulation + human play | mechanic timing / delay model / network implementation | tune gameplay assumption or network behaviour according to owner |
| Cheat / exploit surface | adversarial QA / server validation | authority / trust / rule | move authoritative decision or validate input; engineering may own implementation |

## 19.7 Performance / platform failures

| Failure | Detection | Candidate responsible scope | Smallest first repair |
|---|---|---|---|
| Frame-time spike | target profiler / trace | scene / AI / physics / rendering / script | optimise responsible budget consumer |
| Load-time failure | target build trace | asset / streaming / packaging | fix load path / content budget |
| Memory budget violation | target profiler | content / cache / system | reduce responsible resident / peak allocation |
| Input latency variance | capture / target comparison | frame pacing / input path / network | fix responsible stage; preserve gameplay timing contract |
| Platform-only integration bug | representative platform QA | build / platform integration / content | local platform path fix with regression |

## 19.8 Accessibility failures

| Failure | Detection | Candidate responsible scope | Smallest first repair |
|---|---|---|---|
| Required rapid / repeated input excludes player | XAG review + affected-player evidence | mechanic input contract | alternative action / hold / toggle / timing adjustment |
| Critical information uses one sensory channel | guideline review + user study | cue design | redundant channel |
| Text unreadable at target context | platform / device review | text / UI settings | size / contrast / configuration |
| Settings inaccessible before barrier | first-run test | startup / menu flow | expose setting earlier |
| Remap does not update prompts | deterministic UI state test | input / prompt integration | propagate action mapping to all hints |

## 19.9 Evidence-process failures

| Failure | Detection | Responsible scope | Smallest first repair |
|---|---|---|---|
| Wrong participants | study review | research design | recruit relevant participants / bound conclusion |
| Leading facilitation | recording / protocol review | research method | neutralise task / facilitator script |
| Telemetry proxy misread | triangulation conflict | analysis | collect missing context / qualitative evidence |
| Instrumentation defect | event validation | telemetry implementation | repair event / discard contaminated data |
| Automation used as “fun” proof | evidence review | evaluation design | replace claim with human evidence |
| Too many simultaneous changes | regression ambiguity | tuning process | isolate causal groups / revert / staged retest |
| Stale baseline | version / build mismatch | experiment setup | rerun against controlled baseline |

---

# 20. Smallest-sufficient repair rule — qualified

Stage 1B proposed repairing the smallest responsible unit. Stage 2 supports the principle but adds an important qualification.

## 20.1 Preserve unaffected work

When evidence localises a defect, prefer a local change:

```text
parameter
mapping
rule
cue
state transition
spawn
encounter
checkpoint
layout scene
integration contract
```

before discarding a larger accepted subsystem.

Riot's late-stage balance practice provides a concrete example: the team deliberately creates small tuning levers so it can change champion power without reopening animation / engineering work unnecessarily.

## 20.2 Do not force an artificially local fix

Some failures are genuinely systemic.

Examples:

```text
combat readability = enemy timing + camera + VFX + arena sightline
network fairness = mechanic timing + rollback / frame pacing
progression dead end = resource model + gate + save state
```

If the failure cannot be repaired at one layer without creating a compensating hack elsewhere, expand the correction scope deliberately.

### Qualified rule

> Correct the smallest **causal** scope that resolves the failure without transferring the defect to another layer.

Source:

- <https://2xko.riotgames.com/en-us/news/dev/2xko-live-balance-philosophy/>

**Disposition:** `SUPPORTED / QUALIFIED`.

---

# 21. Evidence-qualified capability model

Stage 2 retains the Stage 1B capability shape but revises C9, strengthens C13 and adds C14–C16.

No capability below implies a separate installable Agent Skill.

## C1 — Define player-experience and game-thesis intent

Own a compact, revisable statement of what the game expects the player to do, understand and experience.

Required reasoning:

```text
intended experience
≠ feature
≠ achieved experience
```

Mark claims as:

```text
deterministically testable
human-behaviour testable
attitudinal / experiential
assumption
```

**Evidence standing:** `SUPPORTED`.

---

## C2 — Model mechanics, rules, state and system relationships

Represent enough interactive state to reason about:

```text
verbs
rules
entities
resources
state
constraints
feedback
goals / outcomes
progression
system dependencies
```

No universal DSL is justified.

Useful representations may include:

```text
written rules
tables
state models
spreadsheets
diagrams
simulation
engine data
```

**Evidence standing:** `SUPPORTED; REPRESENTATION CONTEXTUAL`.

---

## C3 — Decompose uncertainty and choose the cheapest credible proof

For each material unknown:

```text
question
→ variables that must be preserved
→ evidence source
→ cheapest adequate representation
→ falsification / acceptance criterion
```

The representation is selected by uncertainty, not by project prestige or engine preference.

**Evidence standing:** `STRONGLY SUPPORTED`.

---

## C4 — Build a tunable, observable playable proof

When executable evidence is required, the proof should make iteration cheap.

Prefer where useful:

```text
parameter exposure
fast reset / replay
debug state visibility
scenario selection
seed control
instrumentation
placeholder assets
```

Do not require production architecture in disposable proofs unless architecture itself is the uncertainty.

**Evidence standing:** `SUPPORTED`.

---

## C5 — Design and evaluate interaction feel, responsiveness and feedback

Trace:

```text
player intent
→ input
→ mapping / state
→ rule / simulation response
→ presentation / feedback
→ player perception
→ correction
```

Evaluate relevant dimensions such as:

```text
ambiguity
latency
frame pacing
control sensitivity
camera
animation timing
state legibility
audio / VFX / haptics
spatial context
network context
```

No universal historical latency threshold is retained.

**Evidence standing:** `SUPPORTED; NUMERIC TARGETS PROJECT / PLATFORM SPECIFIC`.

---

## C6 — Analyse systems, economies, emergence, progression and balance

Use the appropriate mix of:

```text
formal reasoning
spreadsheet / model
simulation
expert stress test
human play
telemetry
```

Inspect:

```text
source / sink health
feedback loops
strategy space
counterplay
progression reachability
dominant / degenerate strategies
cohort-specific performance
longitudinal adaptation
```

**Evidence standing:** `STRONGLY SUPPORTED`.

---

## C7 — Integrate mechanics into levels, missions, encounters and worlds

Treat space / mission / encounter as active gameplay systems.

Reason across:

```text
objective
↔ player capability
↔ enemy / system behaviour
↔ space / camera
↔ information
↔ pacing
↔ recovery
↔ reward / progression
↔ narrative / content integration
```

**Evidence standing:** `SUPPORTED AND STRENGTHENED`.

---

## C8 — Design player learning, onboarding and progression

Control what the player can encounter, practise, combine and infer.

Useful pattern when appropriate:

```text
introduction
→ practice
→ variation
→ combination
→ pressure
→ freer application
```

This is a heuristic, not a mandatory sequence.

Validate with fresh relevant players rather than the development team alone.

Include accessibility settings / alternatives before the player meets a barrier.

**Evidence standing:** `SUPPORTED; SEQUENCE CONTEXTUAL`.

---

## C9 — Design player research and synthesise play evidence

**Revised in Stage 2.**

For each research question define:

```text
claim / uncertainty
participant profile
build / scenario
method
behavioural measures
attitudinal measures
telemetry if useful
bias / validity risks
analysis method
intended decision
```

Triangulate evidence rather than substituting one source for another.

Keep:

```text
QA
GUR
analytics
expert review
```

conceptually distinct even when one person performs multiple roles.

**Evidence standing:** `STRONGLY SUPPORTED`.

---

## C10 — Escalate fidelity and commitment deliberately

Use evidence gates before expensive expansion.

A representative slice should declare what risk it proves:

```text
experience
integration
pipeline / throughput
performance
content quality
team readiness
scope / schedule
```

Approved decisions are preserved by default but can be reopened through explicit evidence and impact analysis.

**Evidence standing:** `SUPPORTED; NAMED MILESTONES CONTEXTUAL`.

---

## C11 — Integrate cross-domain production into playable behaviour

Game Development states the runtime gameplay contract for adjacent outputs.

Examples:

```text
Animation
→ timing / cancel / root motion / state readability

Environment / art
→ collision / affordance / silhouette / navigation / performance

Audio
→ warning / consequence / reward / spatial information

Narrative
→ trigger / state / choice / pacing behaviour

UI/UX
→ gameplay-state comprehension and interaction

Software Engineering
→ robust implementation of accepted behaviour
```

Technical-design work often lives at this seam in real studios, but the repository must not require the title.

**Evidence standing:** `STRONGLY SUPPORTED`.

---

## C12 — Diagnose and repair the smallest causal scope

Reason from:

```text
observed failure
→ expected behaviour
→ evidence class
→ responsible interaction / layer
→ smallest causal correction
→ focused retest
→ regression of affected dependencies
```

Escalate repair scope when a local patch would only transfer the defect.

**Evidence standing:** `SUPPORTED / QUALIFIED`.

---

## C13 — Validate target and release gameplay behaviour

**Strengthened in Stage 2.**

Release-facing claims require representative target evidence for applicable dimensions:

```text
playable flow
save / state continuity
frame time / pacing
memory
load behaviour
input responsiveness
network behaviour
content integrity
severe bugs / soft locks
accessibility configuration
platform-facing requirements
```

Game Development owns gameplay acceptance criteria; engineering owns much of the underlying optimisation / implementation.

**Evidence standing:** `SUPPORTED CORE CAPABILITY`.

---

## C14 — Design and validate inclusive gameplay access

**New in Stage 2.**

For applicable interactions:

```text
required player action / perception
→ access barrier
→ alternative / configuration
→ discoverability before barrier
→ deterministic validation where possible
→ affected-player evidence where judgement is required
```

Baseline concerns include relevant portions of:

```text
input alternatives
remappable actions
speed / timing tolerance
holds / repeated input
sensitivity
game-speed options where compatible
text / contrast
redundant audio / visual information
subtitles / captions
navigation
motion / photosensitivity
communication
```

**Evidence standing:** `STRONGLY SUPPORTED CORE CAPABILITY`.

---

## C15 — Design and validate network-sensitive gameplay constraints

**New conditional capability in Stage 2.**

Activate when network conditions materially affect gameplay.

Own:

```text
player-facing consistency / latency assumptions
authority-visible gameplay semantics
network-sensitive timing
acceptable degraded conditions
multiplayer state / fairness scenarios
network-aware prototype requirements
```

Do not absorb general networking engineering.

**Evidence standing:** `SUPPORTED AS CONDITIONAL CAPABILITY`.

---

## C16 — Evaluate and tune longitudinal game health

**New conditional capability in Stage 2.**

Activate for live / updateable games where player population behaviour changes the design problem.

Use:

```text
cohort telemetry
strategy / meta analysis
expert play
user research
community evidence
business / progression data where relevant
```

Distinguish:

```text
adaptation
from
defect
```

and prefer interventions that preserve strategic identity and counterplay.

**Evidence standing:** `SUPPORTED AS CONDITIONAL CAPABILITY`.

---

# 22. Capability changes from Stage 1B

| Stage 1B capability | Stage 2 action | Reason |
|---|---|---|
| C1 player-experience / thesis | Retain + qualify evidence | Experience intent useful; achievement requires player evidence |
| C2 mechanics / state / systems | Retain | Professional roles and MDA support explicit system reasoning |
| C3 prototype strategy | Strengthen | Professional prototype / slice evidence supports question-led fidelity |
| C4 tunable playable proof | Retain | Strong practitioner support |
| C5 interaction feel / feedback | Retain + remove universal historic thresholds | Current target / network evidence is context-specific |
| C6 systems / economy / balance | Strengthen | Current economy + live-balance evidence |
| C7 level / encounter integration | Strengthen | Current mission / AI / combat roles are deeply integrative |
| C8 onboarding / progression | Retain + make sequence heuristic | Fresh-player evidence important; no universal teaching order |
| C9 playtests / evidence | **Rewrite** as player-research / evidence synthesis | GUR methods / validity / participant fit materially missing before |
| C10 fidelity / commitment | Retain + redefine representative-slice contract | Vertical-slice terminology is inconsistent |
| C11 cross-domain integration | Strengthen | Current technical / mission / combat practice supports seam ownership |
| C12 smallest repair | Retain + qualify to smallest causal scope | Some defects are coupled |
| C13 target validation | Strengthen to core | Current official profiling evidence closes provisional gap |
| — | **Add C14 accessibility** | Specialist current evidence establishes core responsibility |
| — | **Add conditional C15 network-sensitive gameplay** | Network assumptions can shape design from inception |
| — | **Add conditional C16 live game health** | Live games require longitudinal, cohort-aware tuning |

The increase from thirteen to sixteen capabilities does **not** justify sixteen Agent Skills. Architecture remains later work.

---

# 23. Evidence-qualified production reasoning chain

Stage 2 supports the following reasoning model:

```text
player / product intent
→ declare experience and activity hypotheses
→ model mechanics / state / systems / relevant spatial or network context
→ identify highest-value uncertainty
→ choose cheapest credible evidence source
→ prototype / simulate / script / greybox
→ validate mechanical behaviour
→ research player behaviour / experience when claim requires it
→ diagnose against intent
→ repair smallest causal scope
→ preserve decision + evidence
→ escalate to representative integrated proof
→ commit decisions whose downstream cost is now material
→ expand dependent content / systems
→ continue QA + player research + telemetry + accessibility validation
→ profile on representative target path
→ strengthen locks as change cost rises
→ if live: monitor population / meta and tune longitudinally
→ playable delivery
```

This is a **reasoning chain**, not a fixed waterfall.

A project may loop backward whenever evidence invalidates a committed assumption, but that reopening must be explicit once downstream cost is material.

---

# 24. Gap analysis after Stage 2

## 24.1 Addressed sufficiently for later modelling

### Accessibility baseline

Current official guidance is sufficient to justify C14 and its core status.

**Status:** `ADDRESSED`.

### GUR / evidence selection

Professional literature provides enough method discipline to strengthen C9.

**Status:** `ADDRESSED`.

### Gameplay design / technical design / gameplay programming seam

Contemporary responsibility evidence supports a behaviour-vs-general-engineering boundary while allowing hands-on design implementation.

**Status:** `BOUNDED`.

### Prototype vs representative slice

Professional sources establish purpose-sensitive distinctions and production-readiness usage.

**Status:** `ADDRESSED`.

### Target-platform performance

Current official engine guidance establishes target-build / target-hardware evidence as necessary for credible performance claims.

**Status:** `ADDRESSED AT DOMAIN LEVEL`.

### Automated testing boundary

Current engine automation demonstrates strong mechanical / session automation and its limitations.

**Status:** `BOUNDED; TOOL CHOICE DEFERRED TO STAGE 8`.

### Network-aware gameplay

Current production evidence establishes that network constraints sometimes belong in early design.

**Status:** `BOUNDED AS CONDITIONAL CAPABILITY`.

### Live tuning

Current economy / balance evidence establishes longitudinal evidence and cohort-aware tuning.

**Status:** `BOUNDED AS CONDITIONAL CAPABILITY`.

## 24.2 Still intentionally unresolved

### Platform certification details

Public sources do not justify a universal certification model for all console / mobile storefronts.

**Disposition:** Stage 13 / release examples and current provider documentation when a platform is selected.

### Universal numeric performance / latency targets

No evidence supports one number across genres / hardware / platforms.

**Disposition:** project-specific budget plus Stage 8 tooling.

### General autonomous experiential playtester

No sufficient evidence supports treating an agent as authoritative for human experience.

**Disposition:** Stage 8 tool research + Stage 14 empirical benchmark if candidate tools exist.

### Exact game-thesis schema

Stage 2 supports the need and evidence semantics but does not decide the minimal fields.

**Disposition:** Stage 3.

### Exact mechanics / state artefact schema

Evidence supports explicit representation but not one universal format.

**Disposition:** Stage 4.

### Exact prototype / commitment ladder

Evidence rejects a universal rigid ladder.

**Disposition:** Stage 5 should model uncertainty-to-proof selection and conditional gates.

### Full cross-domain handoff contracts

Current roles establish the need and responsibility boundary, but exact artefacts remain untested.

**Disposition:** Stage 6.

### Exact balance / telemetry metric catalogue

Metrics must be game-specific.

**Disposition:** Stage 7 defines evidence selection and reusable metric semantics without universal targets.

### Engine / provider implementation

Explicitly out of Stage 2 scope.

**Disposition:** Stage 8–9.

---

# 25. Professional practice implications for later stages

## 25.1 Stage 3 — Game thesis

Must distinguish:

```text
aspiration
assumption
testable gameplay constraint
experiential claim
```

and make player-research questions derivable from the thesis.

## 25.2 Stage 4 — Mechanics / systems model

Must support tracing:

```text
intent
→ player action
→ rule / state
→ runtime dynamic
→ feedback
→ evidence
```

without forcing MDA, Machinations or any single formal notation.

## 25.3 Stage 5 — Prototype / commitment

Must select representations from uncertainty and define representative-slice purpose explicitly.

Must support conditional network context and accessibility constraints before expensive commitment when material.

## 25.4 Stage 6 — Cross-domain integration

Must model technical-design-like seams without requiring a `technical-designer` role.

Each handoff needs:

```text
runtime gameplay requirement
provider / adjacent-domain output
integration owner
acceptance evidence
repair ownership
```

## 25.5 Stage 7 — Evaluation

Must use the Stage 2 evidence taxonomy and preserve the separation among:

```text
QA
automation
simulation
telemetry
expert review
GUR
accessibility evaluation
target profiling
```

## 25.6 Stage 8 — Tools

Should search for execution capabilities that expose the evidence surfaces defined here rather than simply finding popular AI tools.

---

# 26. Source register

The register below lists the primary public sources used for Stage 2. Links are recorded so future stages can re-check current behaviour rather than inheriting conclusions blindly.

## 26.1 Professional roles / responsibilities

1. ScreenSkills — Gameplay Designer  
   <https://www.screenskills.com/job-profiles/browse/games/design/gameplay-designer/>

2. ScreenSkills — Gameplay Programmer  
   <https://www.screenskills.com/job-profiles/browse/games/programming/gameplay-programmer/>

3. ScreenSkills — Level Designer  
   <https://www.screenskills.com/job-profiles/browse/games/design/level-designer/>

4. ScreenSkills — Games Tester / QA  
   <https://www.screenskills.com/job-profiles/browse/games/quality-assurance/games-tester/>

5. ScreenSkills — Technical Art / games roles  
   <https://www.screenskills.com/job-profiles/browse/games/technical-art/technical-artist/>

6. Ubisoft — Senior Technical Designer, current listing examined September 2026  
   <https://jobs.smartrecruiters.com/Ubisoft2/744000148308939>

7. Ubisoft — Senior Level Designer — Mission, current listing examined September 2026  
   <https://jobs.smartrecruiters.com/Ubisoft2/744000148310424>

8. Ubisoft — Senior Gameplay Programmer, current listing examined September 2026  
   <https://jobs.smartrecruiters.com/Ubisoft2/744000145464298>

9. Ubisoft — Senior AI Game Designer, *The Division 3*, current listing examined September 2026  
   <https://jobs.smartrecruiters.com/Ubisoft2/744000127417779-senior-ai-game-designer-tom-clancy-s-the-division-3->

10. PlayStation / Naughty Dog — Senior Game Designer (Combat), current listing examined September 2026  
    <https://careers.playstation.com/senior-game-designer-combat/job/6117785004>

11. PlayStation / Insomniac — Combat Designer role description  
    <https://careers.playstation.com/combat-designer-contract/job/5650786004>

## 26.2 Systems / economy / live balance

12. Ubisoft — Game Economy Designer  
    <https://jobs.smartrecruiters.com/ubisoft2/744000120504404>

13. Ubisoft — Economy Designer, Rainbow Six Siege  
    <https://jobs.smartrecruiters.com/Ubisoft2/744000148518519>

14. Riot Games — *2XKO: Live Balance Philosophy*, 17 November 2025  
    <https://2xko.riotgames.com/en-us/news/dev/2xko-live-balance-philosophy/>

## 26.3 Prototyping / representative slices / production

15. GDC 2006 — *Advanced Prototyping*, Chaim Gingold & Chris Hecker  
    <https://www.gdcvault.com/play/1013252/Advanced>

16. GDC — *Prototyping Based Design: A Better, Faster Way to Design Your Game*  
    <https://www.gdcvault.com/play/1012473/Prototyping-Based-Design-A-Better>

17. GDC 2015 / Volition — *The Vertical Slice Challenge*  
    <https://gdcvault.com/play/1022328/The-Vertical-Slice>

18. GDC 2019 / Finji — *So You're Ready to Pitch to a Publisher? You're Not*  
    <https://gdcvault.com/play/1025674/So-You-re-Ready-to>

19. GDC 2019 / Insomniac — *Marvel's Spider-Man: A Technical Postmortem*  
    <https://www.gdcvault.com/play/1026496>

20. GDC 2026 — Production Workshop, pre-production deliverables  
    <https://media.gdcvault.com/gdc2026/Slides/Marty_Fleur_ProductionWorkshopPart2.pdf>

## 26.4 Formal / analytical game-design evidence

21. Hunicke, LeBlanc & Zubek — *MDA: A Formal Approach to Game Design and Game Research*, AAAI 2004  
    <https://aaai.org/papers/ws04-04-001-mda-a-formal-approach-to-game-design-and-game-research/>

## 26.5 Games User Research

22. Oxford University Press — *Games User Research*  
    <https://academic.oup.com/book/26677>

23. Zammitto — *Games User Research as part of the development process in the game industry*  
    <https://academic.oup.com/book/26677/chapter-abstract/195455186>

24. McAllister & Long — *A framework for player research*  
    <https://academic.oup.com/book/26677/chapter-abstract/195455905>

25. Louvel — *Play as if you were at home: dealing with biases and test validity*  
    <https://academic.oup.com/book/26677/chapter-abstract/195460947>

26. Drachen & Connor — *Game Analytics for Games User Research*  
    <https://academic.oup.com/book/26677/chapter-abstract/195460224>

27. Tisserand — *It is all about process*  
    <https://academic.oup.com/book/26677/chapter-abstract/195455286>

## 26.6 Accessibility

28. Microsoft — Xbox Accessibility Guidelines, current set examined September 2026  
    <https://learn.microsoft.com/en-us/xbox/accessibility/guidelines>

29. Microsoft — XAG 107: Input  
    <https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107>

30. Microsoft — XAG 101: Text Display  
    <https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/101>

## 26.7 Performance / target validation

31. Epic Games — Unreal Engine 5.8, *Introduction to Performance Profiling and Configuration*  
    <https://dev.epicgames.com/documentation/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine>

32. Unity 6 — *Collect performance data on the target platform*  
    <https://docs.unity3d.com/6000.0/Manual/profiling-target-device.html>

## 26.8 Automated and network testing

33. Epic Games — Unreal Engine 5.8, Automation Test Framework  
    <https://dev.epicgames.com/documentation/en-us/unreal-engine/automation-test-framework-in-unreal-engine>

34. Epic Games — Unreal Engine 5.8, Gauntlet Automation Framework  
    <https://dev.epicgames.com/documentation/en-us/unreal-engine/gauntlet-automation-framework-in-unreal-engine>

35. Epic Games — Unreal Engine 5.8, Testing and Debugging Networked Games  
    <https://dev.epicgames.com/documentation/unreal-engine/testing-and-debugging-networked-games-in-unreal-engine>

36. Riot Games — *How 2XKO Handles Online Play*, 16 October 2025  
    <https://2xko.riotgames.com/en-us/news/dev/how-2xko-handles-online-play/>

---

# 27. Source limitations

The source set has important limitations that must remain visible.

## 27.1 Job descriptions are snapshots

A job listing is good evidence that a responsibility exists in a current production context. It is weak evidence for how every studio should organise that responsibility.

Therefore role-title mappings remain illustrative.

## 27.2 Studio case studies are not controlled experiments

Volition, Riot, Ubisoft, Naughty Dog, Insomniac and Finji evidence demonstrates real methods and stated trade-offs. It does not prove those methods caused commercial or critical success.

## 27.3 Engine documentation describes capabilities, not quality

Epic and Unity documentation can establish what can be measured or automated. It cannot establish which game is fun or which design is best.

## 27.4 Accessibility guidance is broad but not exhaustive

Xbox Accessibility Guidelines provide a strong current baseline. A project may need specialist standards, platform-specific requirements, disability-specific research and affected-player testing beyond them.

## 27.5 GUR evidence is methodologically stronger but context still matters

Research validity depends on study design, participants, build, environment and analysis. A named method does not guarantee a valid conclusion.

---

# 28. Unresolved questions carried forward

Stage 2 does not silently convert these into rules.

1. What is the **minimum** useful Stage 3 game-thesis contract without becoming a GDD?
2. Which gameplay relationships deserve persistent first-class artefacts in Stage 4?
3. How should confidence / evidence status be encoded without turning ordinary game development into research bureaucracy?
4. Which commitment points are useful across project scales, and which should remain project-defined?
5. When should a representative slice test production throughput versus only player experience?
6. Which accessibility checks can be deterministic and which always require specialist / affected-player research?
7. What minimal network test contract applies to a networked example without duplicating Software Engineering?
8. Which telemetry primitives are reusable enough for the core without assuming a live-service backend?
9. How should replay / deterministic seed support be requested from an execution layer?
10. Which current engines / tools can expose the required runtime state, target profiling and automated play surfaces cleanly? — Stage 8.
11. Can current autonomous agents discover useful gameplay failures beyond scripted tests without producing misleading “experience” claims? — Stage 8 / 14.
12. Which of C14–C16 should become commands, references, validation concerns or conditional workflows rather than standalone skills? — Stage 11.

---

# 29. Stage 2 handoff

The five-book model survives broader challenge, but in a more disciplined form.

The strongest supported production principles are now:

```text
1. Define intended player outcome separately from implementation.
2. Treat that intent as a hypothesis until credible evidence supports it.
3. Choose representations and tests from the uncertainty being reduced.
4. Move to playable evidence when the relevant variable is interaction.
5. Integrate coupled systems early enough to expose their interaction risk.
6. Distinguish QA, simulation, telemetry, expert review and player research.
7. Preserve human authority for genuinely experiential claims.
8. Make accessibility a core gameplay quality responsibility.
9. Validate performance and responsiveness on representative target paths.
10. Bring network conditions into the design proof when they affect gameplay.
11. Use representative slices as explicit readiness / integration proofs, not labels.
12. Preserve accepted decisions, but permit evidence-backed explicit reopening.
13. Diagnose failure before assigning ownership.
14. Repair the smallest causal scope that does not merely move the defect.
15. For live games, interpret population behaviour over time before treating every meta change as a defect.
```

The Stage 3 game-thesis model should start from this evidence-qualified foundation rather than directly from any one book or studio process.

---

# 30. Exit-criteria verification

Stage 2 requires:

```text
professional-practice map
supporting and contrary evidence
gap analysis
claim dispositions
failure taxonomy
evidence-qualified game-development capability model
unresolved questions
```

Verification:

- [x] contemporary professional roles were researched without treating job titles as universal architecture;
- [x] gameplay design, technical design and gameplay-programming responsibilities were distinguished;
- [x] level, mission, combat and AI integration practice was investigated;
- [x] economy / progression / balance practice was investigated;
- [x] prototypes and representative / vertical slices were challenged against professional practice;
- [x] Games User Research methods, validity and analytics relationships were investigated;
- [x] QA and GUR were separated conceptually;
- [x] automated gameplay testing capabilities and limitations were investigated;
- [x] accessibility now has current specialist / platform evidence and an explicit core capability;
- [x] current target-platform profiling evidence was examined;
- [x] historical numeric performance thresholds were not promoted to universal requirements;
- [x] network-aware production was investigated and bounded as a conditional capability;
- [x] live tuning was investigated and bounded as a conditional capability;
- [x] every material Stage 1B challenge claim has an explicit disposition;
- [x] a domain-native failure taxonomy records detection and smallest repair scope;
- [x] deterministic, simulation/search, judgement-heavy and tool-dependent work are distinguished;
- [x] the provisional thirteen-capability model was revised into an evidence-qualified sixteen-capability model;
- [x] unresolved questions remain explicit rather than being promoted to rules;
- [x] engine / AI tool selection was kept out of Stage 2;
- [x] no single studio methodology was made universal;
- [x] no later-stage specification or skill architecture was prematurely generated.

**Stage 2 exit gate: PASS.**

**Next stage:** Stage 3 — Define Player Experience and Game Thesis Model.
