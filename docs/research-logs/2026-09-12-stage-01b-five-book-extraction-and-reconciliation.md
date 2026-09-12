# Stage 1B — Five-Book Extraction and Reconciliation

**Project:** `game-development-skills`  
**Bootstrap stage:** 1B — Extract and Reconcile the Five-Book Corpus  
**Status:** Complete  
**Date:** 12 September 2026

## 1. Stage purpose

Stage 1A selected five complementary books. Stage 1B turns those selected sources into directly examined evidence before broader professional-practice research begins.

This stage asks a different question from Stage 1A:

```text
Stage 1A
→ Which five books best cover the Stage 1 boundary?

Stage 1B
→ What production knowledge do those five books actually support,
   where do they overlap or disagree,
   and what provisional game-development capability model follows?
```

The corpus is evidence for capabilities, not a template for repository architecture. No book-specific skill, mandatory source taxonomy, engine choice or provider architecture is derived here.

## 2. Inputs and source-access resolution

Canonical project inputs:

- [`2026-09-12-stage-01-project-goal-and-domain-boundary.md`](2026-09-12-stage-01-project-goal-and-domain-boundary.md)
- [`2026-09-12-stage-01a-domain-coverage-and-five-book-corpus.md`](2026-09-12-stage-01a-domain-coverage-and-five-book-corpus.md)
- [`2026-09-07-game-development-skills-new-project-bootstrap-process.md`](2026-09-07-game-development-skills-new-project-bootstrap-process.md)

The user supplied direct source copies of all five selected books. The books themselves are private source material and are **not** committed to this repository. This log records only independently expressed synthesis and traceable chapter / section locations.

The Stage 1A access blocker is therefore resolved for all five sources.

## 3. Corpus and reading-coverage register

Stage 1B requires meaningful examination for each book's intended contribution, not an assertion of exhaustive cover-to-cover reading. The following records the material directly examined for this stage.

| Source | Edition / source identity | Intended corpus contribution | Material directly examined for Stage 1B | Coverage limitation |
|---|---|---|---|---|
| Tracy Fullerton, *Game Design Workshop: A Playcentric Approach to Creating Innovative Games* | 5th ed., CRC Press, 2024 | Player-centred design, formal/dynamic systems, prototyping, playtesting, iteration | Ch. 1 playcentric process and experience goals; Chs. 3–5 formal elements / system dynamics / interaction loops; Chs. 7–8 physical and digital prototyping; Ch. 9 playtesting / metrics; Ch. 10 functionality, completeness and balance; relevant fifth-edition contents and examples | Targeted extraction, not exhaustive treatment of every dramatic, professional or industry-interview section |
| Ernest Adams & Joris Dormans, *Game Mechanics: Advanced Game Design* | New Riders, 2012 | Formal mechanics, emergence, internal economies, simulation, balancing and progression | Ch. 1 mechanics / prototyping / design process; Chs. 2–4 emergence, progression and economy; Chs. 5–8 Machinations, feedback, patterns, simulation and balance; Chs. 10–11 mechanics / level / progression integration; relevant caveats about modelling | Machinations-specific syntax was examined only far enough to understand its modelling role and limits; it is not adopted as a project dependency |
| Steve Swink, *Game Feel: A Game Designer's Guide to Virtual Sensation* | Morgan Kaufmann / Elsevier, copyright 2009, ISBN 978-0-12-374328-2 | Controls, response, perception, feedback and game feel | Chs. 1–4 definition, perception and interactivity model; input / response / context / polish metric sections; representative case-study material; Ch. 17 principles of game feel; relevant sections on player skill and parameter relationships | The book deliberately defines “true game feel” narrowly around real-time control, simulated space and polish; this limits direct generalisation to turn-based and non-spatial games |
| Christopher W. Totten, *An Architectural Approach to Level Design* | 2nd ed., CRC Press, 2019 | Level / spatial design, greyboxing, player guidance, pacing and world integration | Introduction and scope; Chs. 2–3 representation and level workflows; Chs. 4–7 spatial arrangement / communication / pacing / rewards; Ch. 8 tutorial design; Ch. 10 possibility spaces / worldbuilding; Ch. 11 procedural integration; Chs. 12–13 social space and sound / rhythm; conclusion | Architectural and psychological analogies are treated as design lenses until Stage 2 challenges their wider evidential strength |
| Richard Lemarchand, *A Playful Production Process: For Game Designers (and Everyone)* | MIT Press, 2021 | End-to-end production, commitment, integration, playtesting and delivery | Ideation and prototype chapters; project goals; preproduction / vertical slice / playtesting / concentric development; game-design macro and scheduling; milestone reviews; formal playtesting and metrics; alpha / beta / postproduction / release-candidate material; performance and release concerns | The four-phase Playful Production Process is one coherent process, not evidence that every game project should use the same phase model |

### 3.1 Direct-source standard

For each source, extraction was based on the supplied book itself. Publisher copy, search snippets, bibliographic pages and the Stage 1A candidate comparison were not treated as substitutes for source examination.

No substantial source text is reproduced here.

---

# 4. Per-book findings

## 4.1 Fullerton — playcentric design as a continuous evidence loop

### F1 — Player experience is an explicit design target, not a feature list

**Source location:** Ch. 1, “A Playcentric Design Process” / “Setting Player Experience Goals”; Ch. 6, player-experience-goal examples.

**Problem / concept:** Teams can confuse implementation features with the experience they intend players to have.

**Applicability:** Useful whenever a design needs a stable statement of intended player experience before detailed implementation choices are made.

**Production behaviour:** Define player-experience goals independently from features; generate candidate mechanics / content against them; later evaluate observed play against those goals.

**Evaluation:** Ask whether target players actually exhibit or report evidence consistent with the intended experience rather than whether a requested feature merely exists.

**Failure / repair:** If implementation satisfies its feature checklist but players do not experience the intended result, reopen the responsible mechanic / feedback / pacing / content assumption rather than redefining success around the implementation.

**Relationship:** Strongly supports Lemarchand's project goals and playtest loops. Swink provides a lower-level version for control / feel. Totten applies the same logic to spatial experience.

**Disposition:** **RETAIN**, but experiential claims require human evidence and Stage 2 must challenge construct validity for subjective goals.

### F2 — Iteration is a closed evidence loop

**Source location:** Ch. 1 iterative process.

**Problem / concept:** Design intent is speculative until exposed to players.

**Production behaviour:** Use a repeatable loop:

```text
experience goal
→ candidate system / idea
→ prototype
→ playtest
→ compare evidence with goal
→ prioritise issues
→ revise
→ retest
```

**Evaluation:** A revision is successful when the next test improves the relevant evidence without unacceptable regressions.

**Failure / repair:** Do not treat first implementation as proof. Persist the goal and previous evidence so changes can be judged rather than merely preferred.

**Relationship:** The strongest corpus-wide common pattern. Supported by Totten and Lemarchand; Adams/Dormans add formal simulation and systems analysis.

**Disposition:** **RETAIN / MERGE** as a foundational capability, not a fixed repository lifecycle.

### F3 — Prototype fidelity should follow the question

**Source location:** Ch. 7 “Prototyping”; Ch. 8 “Digital Prototyping” / software-prototype guidance.

**Problem / concept:** A prototype can cost more than the uncertainty it is meant to resolve.

**Production behaviour:** Isolate the question first, then choose physical, visual, video, software or other representation. Physical prototypes keep attention on gameplay where timing / simulation are not essential; software is justified when the relevant interaction cannot be represented cheaply elsewhere.

**Evaluation:** A prototype succeeds if it answers its design question with sufficient confidence, not if it resembles the final game.

**Failure / repair:** If a prototype grows into an architecture exercise, remove non-evidential work and reduce it to the minimum representation that still exposes the uncertainty.

**Relationship:** Directly aligns with Adams/Dormans' focus-dependent prototype medium, Totten's paper-to-greybox transition and Lemarchand's prototype-before-demo distinction.

**Disposition:** **RETAIN / MERGE** into cheapest-adequate-representation logic.

### F4 — Systems must be understood through relationships, feedback and emergence

**Source location:** Ch. 5 “Working with System Dynamics”; interaction-loop material; Ch. 10 balance.

**Problem / concept:** Local rules that appear correct can produce unwanted global behaviour.

**Production behaviour:** Model objects, properties, behaviours, relationships, information, control and feedback. Inspect reinforcing / balancing loops and the player's interaction loop from mental model through action, rules, feedback and learning.

**Evaluation:** Test system-level trajectories, player choices, learning, balance and unintended patterns rather than individual rules alone.

**Failure / repair:** Isolate the object / relationship generating the failure and alter the minimum responsible element; change one variable at a time where causal diagnosis matters.

**Relationship:** Strongly reinforced by Adams/Dormans' complex-systems and feedback analysis.

**Disposition:** **RETAIN / MERGE**.

### F5 — Playtesting and metrics connect intent to observed player behaviour

**Source location:** Ch. 9 “Playtesting”; “Metrics in Game Design.”

**Problem / concept:** Developers are poor substitutes for the intended audience, and recollection of playtests is unreliable evidence.

**Production behaviour:** Recruit appropriate players, observe behaviour, take structured notes, collect qualitative and quantitative evidence where useful, and define metrics against explicit design intent.

**Evaluation:** Behavioural and attitudinal evidence should be interpreted against the experience question; metrics operationalise a concept but do not automatically prove overall quality.

**Failure / repair:** If a metric does not correspond to the design question, redesign the measure rather than tune the game to an irrelevant number.

**Relationship:** Reinforced by Lemarchand's formal playtesting / telemetry. Stage 2 must challenge both with specialist Games User Research evidence.

**Disposition:** **RETAIN / QUALIFY**.

### F6 — Complexity is not a quality target

**Source location:** Ch. 5 systems examples; Ch. 10 functionality / completeness / balance.

**Problem / concept:** Adding variables, objects or rules can increase possibility-space complexity without improving player experience.

**Production behaviour:** Add complexity only when it contributes to intended play. Test for completeness, loopholes, dead ends, fairness, dominant objects / strategies and target-player challenge.

**Evaluation:** Meaningful choice, comprehensibility and experience value matter more than raw system size.

**Failure / repair:** Remove extraneous elements and retest; preserve only complexity that carries gameplay responsibility.

**Disposition:** **RETAIN**.

---

## 4.2 Adams & Dormans — mechanics as inspectable dynamic systems

### AD1 — Mechanics should be explicit enough to reason about and implement

**Source location:** Ch. 1 “Designing Game Mechanics.”

**Problem / concept:** Hidden implementation detail makes rule interactions difficult for designers to reason about.

**Production behaviour:** Specify the entities, rules / processes, data / resources, states and consequences needed to explain how player action changes the game.

**Evaluation:** Another designer or implementer should be able to identify permitted actions, state transitions, resource effects and success / failure implications without reverse-engineering implementation code.

**Failure / repair:** Clarify the smallest ambiguous mechanism rather than expanding a monolithic design document.

**Relationship:** Complements Fullerton's formal elements and Lemarchand's verbs / player activities.

**Disposition:** **RETAIN / ADAPT** into a minimal mechanics-and-state model; do not impose the book's terminology as the only valid game-design vocabulary.

### AD2 — Emergence and progression are distinct structural forces

**Source location:** Chs. 2–3 “Emergence and Progression” / “Complex Systems and the Structure of Emergence.”

**Problem / concept:** Designers need to distinguish behaviour arising from interacting rules from behaviour intentionally sequenced by progression structures.

**Production behaviour:** Examine whether a design expands possibility through interacting systems, restricts it through gates / sequence, or combines both. Use the distinction to reason about agency, pacing, difficulty and narrative control.

**Evaluation:** Test both intended routes and player-created strategies; inspect whether progression overconstrains play or emergence undermines intended pacing / state.

**Failure / repair:** Adjust the responsible gate, feedback structure, resource relationship or progression constraint rather than suppressing all emergent behaviour.

**Relationship:** Totten's possibility spaces and linear-to-emergent onboarding provide spatial equivalents.

**Disposition:** **RETAIN AS ANALYSIS LENS**, not a universal two-category taxonomy.

### AD3 — Internal economies and feedback loops benefit from executable abstraction

**Source location:** Chs. 4–8, especially Machinations, common mechanisms, simulation and balance.

**Problem / concept:** Economy behaviour, feedback and resource trajectories may be expensive to discover only through a full game build.

**Production behaviour:** Represent resource sources, sinks, conversions, pools and feedback at the minimum level needed to simulate behaviour. Run repeated simulations where they answer balance questions.

**Evaluation:** Look for runaway growth / collapse, deadlocks, unstable feedback, dominant strategies, resource starvation, inaccessible progression and sensitivity to parameter changes.

**Failure / repair:** Change the responsible resource flow / feedback structure and rerun both model and playable evidence.

**Limitation:** The authors explicitly treat Machinations as a simplified model and simulation tool, not a playable-game substitute.

**Disposition:** **RETAIN CAPABILITY; REFERENCE TOOL**. The project should support model / simulation reasoning without requiring Machinations.

### AD4 — Prototype medium follows the uncertainty

**Source location:** Ch. 1 prototyping sections.

**Problem / concept:** Paper, physical and software prototypes reveal different classes of evidence.

**Production behaviour:** Use paper for discrete economies / progression where suitable; physical enactment for some embodied interaction questions; software when continuous timing, physics, controls or target-like interaction are material. Give each prototype a single explicit focus where practical.

**Evaluation:** Evidence quality is judged relative to the question, not the nominal fidelity of the representation.

**Relationship:** Direct corpus consensus with Fullerton, Totten and Lemarchand.

**Disposition:** **RETAIN / MERGE**.

### AD5 — Formal methods support judgement; they do not replace it

**Source location:** Ch. 7 design-pattern discussion.

**Problem / concept:** A reusable pattern library can become prescriptive and suppress contextual design.

**Production behaviour:** Use patterns and formal models to expose structure, communicate and generate alternatives; treat them as hypotheses / aids, then validate in the game context.

**Evaluation:** A pattern survives because it solves the observed problem without unacceptable side effects, not because it is canonical.

**Disposition:** **RETAIN** as a guard against turning this repository into a rules engine.

### AD6 — Strong early locking is useful risk control but too absolute as stated

**Source location:** Ch. 1 concept / elaboration / tuning process.

**Problem / concept:** The source recommends fixing key concept decisions after concept and later imposing feature freeze so tuning can stabilise.

**Evidence value:** It correctly identifies escalating change cost and the risk of late feature additions destabilising a game.

**Conflict:** Fullerton's continuous evidence loop and Lemarchand's explicit willingness to modify project goals when evidence demands it make an unconditional “never change” rule too strong.

**Disposition:** **QUALIFY**:

```text
approved decision
→ preserve by default
→ reopen only with material evidence / explicit authority
→ assess downstream impact
→ revise deliberately
→ revalidate affected work
```

The repository needs commitment boundaries, not irreversible dogma.

---

## 4.3 Swink — game feel as a tunable perception / response problem

### S1 — Moment-to-moment interaction is a perception loop

**Source location:** Chs. 1–4, especially the game-feel model of interactivity.

**Problem / concept:** A mechanic may be logically correct while control still feels ambiguous, delayed, weak or disconnected.

**Production behaviour:** Analyse:

```text
player intent
→ input
→ mapping / filtering
→ simulation / state
→ response
→ visual / audio / haptic feedback
→ player perception and correction
```

**Evaluation:** Inspect response timing, continuity, predictability, state legibility, sensitivity and the player's ability to correct action.

**Failure / repair:** Tune the smallest responsible mapping, parameter, state transition, response or feedback channel before rewriting the whole mechanic.

**Disposition:** **RETAIN / GENERALISE** as interaction-feel and feedback analysis.

### S2 — Polish can materially change perceived interaction without changing rules

**Source location:** Ch. 1 polish; polish metric / case-study sections.

**Problem / concept:** Simulation correctness alone does not determine how physical or responsive interaction feels.

**Production behaviour:** Treat animation, sound, VFX, camera response and haptics as gameplay-facing feedback layers when they alter how the player perceives consequence, mass, impact or state.

**Evaluation:** Compare behaviour with / without feedback layers and test whether cues improve clarity and intended feel.

**Cross-domain boundary:** Game Development owns the gameplay requirement and integrated acceptance criteria. Animation, Audio, VFX and other specialist domains may own production of the assets themselves.

**Disposition:** **RETAIN**.

### S3 — Goals and constraints shape the possibility space of control

**Source location:** Ch. 1 “Challenge Alters the Sensation of Control.”

**Problem / concept:** Good controls in isolation do not determine the skill or experience players develop.

**Production behaviour:** Design goals and constraints around the control system so players are encouraged to explore useful motion / action possibilities and develop intended skills.

**Evaluation:** Observe whether players discover, practise and intentionally reproduce desired actions at appropriate levels of skill.

**Disposition:** **RETAIN / MERGE** with progression, onboarding and encounter design.

### S4 — Player skill changes perceived feel

**Source location:** Ch. 1 skill / mastery discussion; later principle sections.

**Problem / concept:** The same control mapping can feel different to novice and expert players.

**Production behaviour:** Do not assess feel from expert developers alone. Test across relevant player skill states and expose new complexity in a sequence that makes state / control relationships learnable.

**Evaluation:** Separate actual control defects from expected learning cost; monitor whether intent-to-outcome ambiguity decreases with appropriate learning.

**Disposition:** **RETAIN**, with Stage 2 challenge from user-research and accessibility evidence.

### S5 — The book's “true game feel” definition is intentionally narrow

**Source location:** Ch. 1 definition and examples.

**Finding:** Swink centres “true game feel” on real-time control of a virtual object, simulated space and polish, and explicitly excludes or places outside the centre many turn-based / indirectly controlled games.

**Conflict:** Stage 1 explicitly allows game forms where direct continuous spatial control is not the main interaction model.

**Disposition:** **QUALIFY / DO NOT UNIVERSALISE**. Use Swink's model when direct real-time control is material. For the project as a whole, use the broader concept of interaction response / feedback quality so strategy, puzzle, card, simulation and other forms remain first-class.

### S6 — Fixed latency / frame-rate thresholds require current challenge research

**Source location:** Ch. 4 measurable thresholds for real-time control.

**Finding:** The book proposes perceptual thresholds for frame rate, response time and continuous feedback.

**Limitation:** The book is from 2009 and hardware, displays, input pipelines and player expectations have changed materially.

**Disposition:** **RESEARCH FURTHER** in Stage 2 / Stage 8. Preserve the principle—latency and continuity materially affect feel—but do not promote the historical numeric thresholds to current core requirements without modern evidence.

---

## 4.4 Totten — gameplay expressed through designed space

### T1 — Level design is not environment art

**Source location:** Introduction / “What This Book Will Not Teach You”; Chs. 2–3.

**Problem / concept:** Spatial gameplay responsibility can be blurred with visual asset production.

**Production behaviour:** Treat level design as arrangement and sequencing of interactive space to support mechanics, player behaviour, meaning, pacing and navigation. Use environment art as a communicating / contextual layer without collapsing the disciplines.

**Evaluation:** A level can be visually attractive and still fail gameplay flow; test spatial behaviour directly.

**Cross-domain boundary:** Game Development owns gameplay layout, affordance and integrated spatial acceptance. Environment / 2D / 3D production owns specialist asset creation.

**Disposition:** **RETAIN**.

### T2 — Paper representation and greybox are different evidence instruments

**Source location:** Chs. 2–3, level-design workflow / greyboxing sections.

**Problem / concept:** Spatial uncertainty changes as a level moves from topology / pacing questions to exact movement / camera / collision questions.

**Production behaviour:** Begin with sketches, diagrams, plans, flow or other non-digital representations where adequate; move to engine primitives / placeholder art when spatial scale, movement, camera, collision or timing needs playable evidence.

**Evaluation:** A greybox is successful when it demonstrates the intended gameplay / spatial question, not when it resembles final environment art.

**Disposition:** **RETAIN / MERGE** with prototype strategy.

### T3 — Pacing exists at both macro and micro spatial scales

**Source location:** Ch. 3 level-design workflows / pacing discussion.

**Problem / concept:** Constant intensity produces fatigue and makes moments indistinguishable.

**Production behaviour:** Map the whole level and its local encounter / traversal beats together; deliberately space intense, exploratory, movement and recovery moments.

**Evaluation:** Observe route, dwell time, repeated failures, missed cues and intensity / recovery patterns during playtest.

**Disposition:** **RETAIN** as a level / encounter capability, not a universal pacing formula.

### T4 — Tutorials are controlled possibility spaces, not merely instruction text

**Source location:** Ch. 8 “Level 1–1: The Tutorial Level.”

**Problem / concept:** New players need safe opportunities to perceive, attempt, fail, retry and combine mechanics.

**Production behaviour:** Introduce mechanics in bounded scenes / contexts; control possibility through space, available abilities and threat; allow practice; escalate to variation / final test; tune checkpoint / retry cost; use redundant visual / audio cues where useful.

**Evaluation:** Test with players who do not already know the game. Observe what they attempt, misunderstand, fail to perceive or cannot reproduce.

**Disposition:** **RETAIN / MERGE** with player-learning progression and accessibility challenge research.

### T5 — World / level design can deliberately combine progression and emergence

**Source location:** Ch. 10 possibility spaces / worldbuilding; Ch. 11 procedural levels.

**Problem / concept:** A world can be unreadably open or excessively linear.

**Production behaviour:** Create a bounded, learnable rule / object vocabulary; provide overview / orientation; expose possibilities in controlled ways, then permit deeper emergent combination and exploration.

**Evaluation:** Test whether players understand choices, can orient themselves, discover affordances and generate valid unexpected play without soft-locking progression.

**Relationship:** Strong alignment with Adams/Dormans' progression / emergence distinction.

**Disposition:** **RETAIN / MERGE**.

### T6 — Architectural analogy is a design lens, not evidence of universal player response

**Source location:** Introduction and throughout spatial / psychological analogies.

**Finding:** The book productively imports concepts from architecture, teaching, urbanism and environmental psychology.

**Limitation:** A historical or architectural precedent does not by itself prove a universal gameplay effect across players, cultures, abilities or game forms.

**Disposition:** **QUALIFY**. Retain reusable spatial hypotheses and representations; challenge behavioural claims with Stage 2 empirical / professional evidence and actual playtests.

---

## 4.5 Lemarchand — escalation from cheap proof to integrated production evidence

### L1 — Prototype first; representative demo later

**Source location:** Phase One prototyping; Chs. 10–11 vertical slice.

**Problem / concept:** Early prototypes and production-representative slices answer different questions.

**Production behaviour:** Use small prototypes during ideation to answer narrow design questions. After the core direction survives evidence, build an integrated, representative playable slice containing the important production layers needed to expose scope, quality and integration risk.

**Evaluation:** A prototype passes by answering its uncertainty. A representative slice passes by proving the chosen game can be built and integrated at the required level of quality.

**Disposition:** **RETAIN / MERGE**, while keeping “vertical slice” semantics explicit because the corpus uses the term at different fidelity levels.

### L2 — Build from the game's dependency centre outward

**Source location:** Ch. 13 “Concentric Development.”

**Problem / concept:** Secondary systems become unstable when built on unresolved primary interaction.

**Production behaviour:** Identify the smallest mechanics / control / state foundation on which later gameplay depends; make it sufficiently representative and stable before expanding outward. For direct-character games, character / camera / movement controls may form that centre; other forms require different centres.

**Limitation:** Lemarchand explicitly notes that some games do not have a clean mechanic hierarchy.

**Disposition:** **ADAPT** into **dependency-aware core-first integration**, not a mandatory primary / secondary / tertiary hierarchy and not a requirement to over-polish isolated mechanics before testing interactions.

### L3 — Debuggability and tunability are production features

**Source location:** Ch. 11 “Start to Add Debug Functions”; subsequent production / metrics material.

**Problem / concept:** Iteration slows dramatically if designers cannot reset, inspect hidden state, jump to scenarios or adjust parameters.

**Production behaviour:** Introduce developer-facing reset / teleport / state visibility / parameter controls / instrumentation when their iteration value becomes material.

**Evaluation:** Measure whether a gameplay question can be reproduced, inspected and retested without avoidable setup cost.

**Disposition:** **RETAIN**, with exact implementation left to Software Engineering / execution tooling where appropriate.

### L4 — Playtesting should mature with the game

**Source location:** Ch. 12 regular playtesting; Chs. 24–26 formal playtesting and metrics.

**Problem / concept:** Early exploratory tests and late confidence-building tests need different rigor.

**Production behaviour:** Test throughout development; as commitment increases, formalise scripts, participant selection, observations, surveys, interviews and telemetry where useful. Preserve records and compare changes across rounds.

**Evaluation:** Triangulate behaviour, reported experience and instrumented data against design intent. Track whether changes improve, regress or leave the target unchanged.

**Failure / repair:** Triage observations into clear failure, unresolved question and new idea; solve the problem rather than blindly implement a player's proposed solution.

**Disposition:** **RETAIN / QUALIFY** with Stage 2 specialist Games User Research challenge.

### L5 — Production locks should reflect rising change cost

**Source location:** preproduction commitment; alpha / beta / postproduction; release-candidate discussion.

**Problem / concept:** Late systemic / interactive changes are disproportionately risky.

**Production behaviour:** Increase commitment as evidence and downstream investment grow. Before content scale, require representative proof. At later completeness gates, bias toward correction / removal / polish rather than uncontrolled feature expansion.

**Evaluation:** A proposed late change must justify benefit against affected systems, content, QA, performance and schedule.

**Disposition:** **RETAIN / GENERALISE** as a cost-aware commitment policy, not the mandatory four-phase schedule of this book.

### L6 — Release-quality gameplay includes technical behaviour on the target path

**Source location:** beta / postproduction / release-candidate material.

**Problem / concept:** A playable design can still fail because of frame-time, load, severe bugs, certification or build behaviour.

**Production behaviour:** Treat technical performance and target build validation as part of gameplay delivery, while delegating general engineering implementation to adjacent Software Engineering skills.

**Disposition:** **RETAIN AS BOUNDARY REQUIREMENT; RESEARCH FURTHER** for current platform-specific thresholds and certification practice.

---

# 5. Source-to-capability matrix

The books do not map one-to-one to skills. Multiple sources converge on shared production capabilities, and some capabilities remain under-evidenced until Stage 2.

Legend:

```text
P = primary evidence contribution
S = supporting contribution
Q = useful but materially qualified
— = not a material corpus contribution
```

| Provisional capability | Fullerton | Adams / Dormans | Swink | Totten | Lemarchand |
|---|---:|---:|---:|---:|---:|
| 1. Player-experience / game-thesis intent | P | S | S | S | P |
| 2. Mechanics, rules, state and system modelling | P | P | S | S | S |
| 3. Uncertainty decomposition and prototype strategy | P | P | S | P | P |
| 4. Tunable playable proof / debug visibility | S | S | P | S | P |
| 5. Interaction feel, control and feedback | S | S | P | S | P |
| 6. Economy, feedback, emergence and balance analysis | P | P | S | S | S |
| 7. Level, encounter and world gameplay integration | S | P | S | P | P |
| 8. Player learning, onboarding and progression | S | P | P | P | P |
| 9. Playtest design and evidence interpretation | P | S | S | P | P |
| 10. Fidelity escalation and commitment decisions | S | Q | S | S | P |
| 11. Cross-domain production integration | S | S | S | P | P |
| 12. Diagnosis, tuning and smallest-sufficient repair | P | P | P | S | P |
| 13. Target / release gameplay validation | S | S | Q | S | P |
| Accessibility / inclusive interaction | limited | — | limited | limited | limited |
| Networked / multiplayer runtime concerns | limited | limited | — | limited spatial / social | limited |
| Live-service / longitudinal tuning | limited | limited | — | — | limited metrics |

The bottom three rows are deliberately **not** promoted to adequately evidenced corpus capabilities. They remain Stage 2 gaps inherited from Stage 1A.

---

# 6. Corpus-wide agreements

## 6.1 Design intent must survive contact with players

Across different terminology, the corpus converges on:

```text
intent
→ representation
→ interaction
→ observation
→ diagnosis
→ revision
```

Fullerton states this most explicitly as a playcentric loop. Totten applies it to level spaces, Lemarchand to the whole production arc, Adams/Dormans to mechanics and systems, and Swink to moment-to-moment input / response.

**Provisional rule:** design claims become progressively credible through playable evidence; experiential claims do not become true merely because the implementation matches the specification.

## 6.2 Use the cheapest representation capable of answering the current question

The sources disagree on exact media but agree on the governing logic:

```text
rule / economy uncertainty
→ paper, table, diagram or simulation may be enough

embodied interaction uncertainty
→ physical enactment may help

control / timing / physics uncertainty
→ executable prototype

spatial flow uncertainty
→ diagram → greybox

production integration uncertainty
→ representative playable slice
```

**Provisional rule:** fidelity is a response to uncertainty, not a maturity status to maximise.

## 6.3 Complex gameplay must be evaluated as a system

Fullerton and Adams/Dormans explicitly model feedback and emergence. Totten shows spatial possibility spaces producing player-created behaviour. Lemarchand repeatedly treats games as complex dynamic systems. Swink shows that even a control sensation emerges from relationships among mapping, simulation, response, context and feedback.

**Provisional rule:** local correctness is necessary but insufficient. Evaluation must include system interaction, emergent strategy, player behaviour and edge conditions.

## 6.4 Human play is authoritative for experiential claims

Every source that makes substantial claims about experience ultimately returns to players.

**Provisional rule:** simulation, telemetry and deterministic tests can expose structural failures; they cannot by themselves establish fun, clarity, fairness, emotion, satisfaction or feel.

## 6.5 Learning is designed through exposure, feedback and progression

Adams/Dormans distinguish emergence from progression; Totten treats tutorials as controlled possibility spaces; Fullerton ties player mental models to feedback loops; Swink links skill and challenge to perceived control; Lemarchand joins player goal, design goal and emotional beat.

**Provisional rule:** onboarding is not a detached help screen. It is the staged design of what the player can perceive, attempt, fail, retry and combine.

## 6.6 Change cost should alter decision authority

Adams/Dormans and Lemarchand are strongest on freeze / milestone risk, while Fullerton preserves iteration throughout development.

**Provisional rule:** the project needs deliberate commitment boundaries whose strength increases with downstream cost. Approved decisions remain authoritative until explicitly reopened; evidence can justify reopening, but change is never silent.

---

# 7. Conflicts and reconciliations

## 7.1 Absolute concept locks vs evidence-led reopening

**Source tension:** Adams/Dormans state that key concept-stage decisions should remain fixed; Fullerton's process continuously checks design against player evidence; Lemarchand allows project goals to change when the project reveals better information.

**Reconciliation:** preserve approved decisions by default, but do not make them irreversibly immutable.

```text
commit
→ build against decision
→ new material evidence?
   ├─ no → preserve
   └─ yes → explicit reopen decision
            → impact analysis
            → revise affected scope
            → revalidate
```

This matches the Production Skills family principle of preserving approved work without preventing deliberate revision.

## 7.2 Mechanics-first sequencing vs coupled mechanic / space / feel design

**Source tension:** Adams/Dormans sometimes describe getting mechanics working before levels / art; Totten demonstrates that space itself structures gameplay; Swink shows that context changes feel; Lemarchand's representative slice integrates multiple layers.

**Reconciliation:** do not impose a universal serial order. Identify the smallest **coupled uncertainty unit**. A discrete economy may be testable without a level. A traversal mechanic may be meaningless without representative space. A combat mechanic may require enemies, feedback and a small arena.

**Disposition:** replace “mechanics first” with **playability first at the minimum responsible integration scope**.

## 7.3 Concentric development vs interaction effects

**Source tension:** Lemarchand recommends stabilising primary mechanics before expanding outward, but later behaviour can only be understood through interaction among systems; he also explicitly concedes that not all games have a clean hierarchy.

**Reconciliation:** use dependency-aware core-first development while bringing dependent systems together as soon as their interaction is the dominant uncertainty. “Core first” must not become “polish one system in isolation.”

## 7.4 Narrow game-feel definition vs broad game forms

**Source tension:** Swink's central definition deliberately excludes many turn-based and indirect-control forms.

**Reconciliation:** keep `game feel` as a specialist real-time-control lens. At project level use the broader capability **interaction feel and feedback**, which can examine responsiveness, legibility, consequence and player mental model across game forms.

## 7.5 Formal models vs playable reality

**Source tension:** Machinations and other abstractions make hidden systems inspectable, but Adams/Dormans explicitly warn that such models simplify games and do not replace the game itself.

**Reconciliation:** models are cheap evidence for the questions they encode. A model can qualify a mechanic for playable implementation; it cannot certify experiential quality.

## 7.6 Architectural / psychological precedent vs empirical gameplay evidence

**Source tension:** Totten imports powerful concepts from architecture and human-behaviour theory, but analogy and historical precedent do not guarantee contemporary player response.

**Reconciliation:** use them to generate design hypotheses and representations, then playtest. Stage 2 must challenge stronger behavioural claims with broader empirical / professional evidence.

## 7.7 Historical performance thresholds vs current targets

**Source tension:** Swink offers concrete response / frame-rate thresholds useful for explaining perception, but the source is from 2009. Lemarchand provides more recent production attention to frame rate and load time but not universal thresholds.

**Reconciliation:** retain latency / continuity / frame pacing / load behaviour as required evaluation dimensions. Research current target-platform expectations later; do not encode historical numbers as timeless requirements.

## 7.8 “Vertical slice” has more than one fidelity meaning

**Source tension:** Adams/Dormans use vertical slice for a prototype covering all layers of one / few features; Lemarchand treats the vertical slice as a high-quality representative portion of the real game and a production commitment artefact.

**Reconciliation:** use **representative slice** as the generic concept in provisional architecture and require every use of `vertical slice` to declare its purpose and expected fidelity. Do not assume the term itself proves production readiness.

---

# 8. Provisional game-development capability model

This model is the main Stage 1B handoff to Stage 2. It is deliberately capability-shaped rather than book-shaped or skill-shaped.

## C1 — Define player-experience and game-thesis intent

Own a compact, revisable statement of:

```text
target player / context
player fantasy / intended experience
core activities / verbs
primary challenge and mastery
high-level goals / constraints
social mode / viewpoint / input assumptions
success / failure intent
known non-goals
```

Separate intended experience from features. Mark which claims are directly testable, which require human evidence and which are assumptions.

**Candidate evidence:** target-player playtest questions linked to each material experience claim.

## C2 — Model mechanics, rules, state and system relationships

Represent enough of the interactive system to reason about:

```text
entities
state
resources
rules / procedures
player actions / verbs
constraints
goals / outcomes
feedback
progression / gates
relationships / dependencies
```

Do not require one universal formalism. The representation should make the current uncertainty inspectable.

**Candidate evidence:** another agent / designer can trace a player action through state change, consequence and feedback without relying on hidden implementation assumptions.

## C3 — Decompose uncertainty and choose prototype strategy

For every significant unknown:

```text
question
→ evidence needed
→ cheapest adequate representation
→ acceptance / rejection criterion
```

Candidate representations include text rules, tables, spreadsheets, diagrams, simulations, paper prototypes, physical enactments, executable sandboxes and greyboxes.

**Candidate evidence:** the representation answers the stated question without unnecessary fidelity.

## C4 — Build a tunable playable proof

When executable evidence is required, produce the smallest runtime proof that exposes the question and is easy to modify.

Useful characteristics:

```text
placeholder assets where adequate
parameters externally tunable where useful
reset / replay support
state visibility / debug information
scenario isolation
basic instrumentation where valuable
```

**Candidate evidence:** repeated experiment cost is low enough to support iterative comparison.

## C5 — Design and evaluate interaction feel / feedback

Analyse direct and indirect interaction through:

```text
intent
→ input
→ mapping / state
→ simulation / rule response
→ feedback
→ perception
→ correction
```

Inspect ambiguity, responsiveness, state legibility, timing, context, animation, audio, VFX and haptics according to the game form.

**Candidate evidence:** target players can form an accurate control / consequence model and reproduce intended actions; experiential quality remains human-evaluated.

## C6 — Analyse systems, economies, emergence and balance

Inspect resource flows, feedback, progression, probability / choice, interaction among mechanics and player strategies.

Failure classes include:

```text
runaway growth / collapse
deadlock / resource starvation
dominant or trivial strategy
meaningless choice
unreachable progression
unstable difficulty
exploit created by system composition
```

Use simulation when it is cheaper than full play and preserves the relevant structure.

**Candidate evidence:** model / simulation + representative playable validation where player behaviour matters.

## C7 — Integrate mechanics into levels, encounters and worlds

Translate mechanics and player intent into spatial / encounter affordances:

```text
mission / activity
↔ space
↔ player movement / camera
↔ challenge
↔ information / feedback
↔ pacing / recovery
↔ reward / progression
```

Move from drawings / maps to greybox only when spatial evidence requires it.

**Candidate evidence:** players can orient, perceive affordances, execute intended activities and discover legitimate alternatives without the level designer explaining the space.

## C8 — Design player learning, onboarding and progression

Control when and how players encounter mechanics and combinations:

```text
safe introduction
→ practice
→ variation
→ combination
→ pressure / final test
→ freer application
```

Treat retry cost, checkpointing, cue redundancy, skill assumptions and state legibility as design variables.

**Candidate evidence:** fresh players demonstrate the intended mechanic / concept without developer intervention at the expected stage.

## C9 — Plan playtests and interpret evidence

Match the playtest method to the current maturity and question.

Capture where applicable:

```text
participant fit
scenario / task
observation notes
behavioural measures
attitudinal measures
interview evidence
telemetry / metrics
consent / privacy constraints
known test limitations
```

Do not implement player suggestions blindly. Diagnose the underlying failure against project intent.

**Candidate evidence:** every material design conclusion is traceable to observed behaviour, measured data, explicit judgement or a clearly marked assumption.

## C10 — Escalate fidelity and commitment deliberately

Use evidence gates before expensive expansion:

```text
cheap proof
→ evidence sufficient?
→ representative integrated slice
→ scope / quality evidence sufficient?
→ production scale
→ completeness locks
→ post-lock correction / polish
```

Record approved decisions and reopening authority. The later and more coupled the work, the stronger the justification required for change.

**Candidate evidence:** no expensive production phase begins with unresolved uncertainty that a cheaper representation could have answered.

## C11 — Integrate cross-domain production into playable behaviour

Game Development defines what adjacent outputs must accomplish in play and validates them in runtime.

Examples:

```text
Animation
→ movement / attack timing and readable state

Audio
→ mechanic consequence, orientation, warning, reward

Environment / 3D / 2D
→ spatial affordance, collision / silhouette / readability requirements

Narrative
→ gameplay-compatible world / character / choice constraints

UI/UX
→ game-state information and interaction requirements

Software Engineering
→ robust implementation of the accepted runtime behaviour
```

The adjacent domain owns specialist production; Game Development owns gameplay integration and acceptance.

## C12 — Diagnose and repair the smallest responsible unit

Given a failed playtest or system condition:

```text
observed failure
→ intended behaviour
→ responsible layer
→ smallest plausible cause
→ minimal change
→ focused retest
→ regression check
```

Candidate correction units include a parameter, mapping, rule, feedback cue, progression gate, encounter, level scene, checkpoint, resource flow or cross-domain integration requirement.

**Candidate evidence:** unaffected approved work is preserved and the defect becomes a reproducible test case where practical.

## C13 — Validate target and release gameplay behaviour

Before release claims, validate on representative target paths:

```text
complete playable flow
onboarding
save / state continuity where applicable
performance / frame behaviour
load behaviour
input responsiveness
severe bugs / soft locks
content integration
platform / certification requirements where applicable
```

This capability defines gameplay-facing acceptance; general implementation / infrastructure remains adjacent Software Engineering responsibility.

**Evidence status:** **provisional / under-challenged**. Stage 2 and Stage 8 must provide current platform evidence.

---

# 9. Cross-cutting capability that the corpus does not adequately support

## 9.1 Accessibility / inclusive gameplay

Stage 1 already requires accessibility to remain a core quality dimension. The five-book corpus contains scattered relevant material—player variability, feedback redundancy, novice learning, target-player research—but does **not** provide sufficient specialist evidence to define an accessibility capability safely.

Therefore:

```text
accessibility
≠ absent from the project

accessibility
= mandatory Stage 2 evidence gap
```

Stage 2 must independently research current accessibility practice, including applicable control remapping, input alternatives, timing / sensitivity tolerances, redundant feedback, colour / readability, subtitles / captions, cognitive and motor demands, player research with disabled participants and platform guidance.

No provisional book-derived rule should override that later evidence.

---

# 10. Source idea → capability → behaviour → evaluation mapping

| Source-derived idea | Provisional capability | Production behaviour | Evaluation criterion | Candidate benchmark fixture |
|---|---|---|---|---|
| Fullerton: experience goals + iterative playtest | C1 / C9 | Express intended experience separately from implementation and retest against it | Evidence addresses the stated player outcome | Feature-complete prototype that misses intended experience; diagnose instead of declaring success |
| Fullerton: prototype only what must be learned | C3 | Select cheapest medium / fidelity for a question | Prototype answers question without irrelevant work | Economy uncertainty wrongly implemented as expensive 3D prototype; choose cheaper proof |
| Fullerton: system relationships / interaction loops | C2 / C12 | Trace action → rule → feedback → mental model | Failure can be localized to responsible relationship | Player repeatedly misunderstands consequence despite correct rule execution |
| Adams/Dormans: emergence / progression | C6 / C8 | Model freedom, gates and system interaction separately | No unintended dominant route / progression deadlock | Progression gate plus emergent economy creates unwinnable state |
| Adams/Dormans: executable economy abstraction | C6 | Simulate resource / feedback behaviour before full build | Model exposes instability; playable test confirms relevant behaviour | Currency source / sink creates runaway economy |
| Adams/Dormans: prototype focus determines medium | C3 | Choose paper, physical, software or model from learning goal | Representation preserves variables material to question | Control-scheme question incorrectly tested with paper prototype |
| Swink: input / response / feedback loop | C5 / C12 | Expose mapping, state and feedback variables | Player intent maps predictably to perceived outcome | State-dependent input produces ambiguous response |
| Swink: polish changes perceived consequence | C5 / C11 | Test gameplay feedback layers independently | Cue improves consequence readability without rule change | Collision is mechanically correct but impact is unreadable |
| Totten: diagram → greybox | C3 / C7 | Increase spatial fidelity when movement / camera evidence is needed | Greybox reveals flow / scale issue not answerable on paper | Route readable in plan but confusing in first-person play |
| Totten: tutorial as controlled possibility space | C8 | Introduce → practise → vary → test → release | Fresh player demonstrates skill without explanation | Tutorial introduces three mechanics at once and creates confusion |
| Lemarchand: representative vertical slice | C10 / C11 | Integrate core layers before production scale | Slice demonstrates accepted quality and exposes scope / dependency risk | Prototype is fun but representative art/audio/content integration breaks readability |
| Lemarchand: formal playtesting / metrics | C9 | Use repeated recorded tests as commitment rises | Revision is demonstrably better / worse / neutral | Conflicting player comments resolved through behaviour + survey + telemetry |
| Lemarchand: debug functions | C4 / C12 | Add reset / state inspection / scenario access | Diagnosis / retest setup cost materially reduced | Rare encounter defect cannot be reproduced without 20-minute replay |
| Corpus consensus: late change cost | C10 | Require explicit reopen and impact analysis | Approved work changes only through recorded decision | Late “small” mechanic change invalidates levels and onboarding |

---

# 11. Provisional production reasoning chain

The corpus supports the following **reasoning shape**, not a mandatory named workflow:

```text
player / product intent
→ define experience / activity hypothesis
→ model rules, state, systems and relevant spatial context
→ identify highest-value uncertainty
→ choose cheapest adequate representation
→ build / simulate / greybox
→ observe behaviour and collect evidence
→ diagnose against intent
→ repair smallest responsible unit
→ repeat until uncertainty is sufficiently reduced
→ build representative integrated slice
→ deliberate commitment / approval
→ expand content and dependent systems
→ continue playtesting, telemetry and tuning
→ increase locks as change cost rises
→ target / release validation
→ playable delivery
```

This is compatible with the Stage 1 target shape while adding source-backed detail around prototype choice, player evidence, system interaction, commitment and correction.

It remains provisional until Stage 2 challenges it against broader professional and empirical evidence.

---

# 12. Claims that Stage 2 must challenge explicitly

The following are not allowed to become unconditional core rules yet.

| Claim / area | Why challenge is required | Stage 1B disposition |
|---|---|---|
| Player-experience goals reliably predict / constrain good design | Strong practice support, but subjective constructs require research validity | QUALIFY |
| Specific playtest participant counts or cadence heuristics | Corpus examples are context-dependent | RESEARCH FURTHER |
| Formal metrics can establish experiential quality | Metrics can operationalise proxies but may miss meaning / bias | QUALIFY |
| Machinations / resource-flow models generalise to all game systems | Authors explicitly bound the model and simplify games | REFERENCE / BOUNDED |
| Emergence vs progression is sufficient as a full game taxonomy | Useful structural distinction, incomplete taxonomy | ANALYSIS LENS |
| Concept decisions should never change | Conflicts with evidence-led iteration | REJECT AS ABSOLUTE; ADAPT TO COMMIT / REOPEN |
| Primary mechanics should always reach shippable polish before secondary mechanics | Useful dependency heuristic, but coupled systems may require earlier integration | QUALIFY |
| Swink's “true game feel” defines feel for every game | Intentionally excludes valid game forms | REJECT AS UNIVERSAL |
| Swink's 2009 frame-rate / response thresholds should be current acceptance limits | Technology and expectations have changed | RESEARCH FURTHER |
| Architectural precedent predicts player behaviour | Useful hypothesis source, not universal behavioural proof | QUALIFY |
| A fixed four-phase production process fits all game scales / forms | One coherent production model, not universal evidence | REJECT AS UNIVERSAL; RETAIN CAPABILITIES |
| Beta / alpha semantics are universal | Studio / platform / delivery models vary | QUALIFY |
| Accessibility can be derived from general usability / novice-learning material | Specialist evidence is insufficient | RESEARCH FURTHER — HIGH PRIORITY |
| Multiplayer / networked behaviour is adequately covered | Corpus is too thin on authority / latency / sync / cheating / social-system runtime issues | RESEARCH FURTHER |
| Current target-platform performance / certification is adequately covered | Current official evidence required | RESEARCH FURTHER |

---

# 13. Provisional failure taxonomy derived from the corpus

Stage 2 owns the broader evidence-qualified failure taxonomy. Stage 1B nevertheless identifies recurring failure classes worth challenging:

### Intent / evidence failures

- feature delivered but intended experience absent;
- evaluation question does not match design claim;
- designer / team substitutes for target players;
- metric optimised without validating what it represents.

### Mechanics / systems failures

- incomplete or contradictory rule behaviour;
- hidden state / consequence is illegible;
- dominant / trivial strategy;
- runaway positive feedback;
- economy collapse / starvation;
- progression deadlock / no-win state;
- local mechanic correct but composed system broken;
- unnecessary complexity obscures meaningful choice.

### Interaction-feel failures

- ambiguous input mapping;
- state change not perceived;
- response too weak / delayed / inconsistent for intended interaction;
- feedback contradicts simulation / state;
- novice and expert skill assumptions confused;
- polish masks rather than communicates behaviour.

### Spatial / encounter failures

- route / goal unreadable;
- spatial scale mismatched to movement / camera;
- encounter or level pacing has no contrast;
- mission and space work against each other;
- tutorial exposes too much at once;
- failure / retry cost blocks learning;
- world offers choices the player cannot interpret.

### Production / commitment failures

- high-fidelity content built before underlying playability is proven;
- prototype becomes a production architecture project;
- representative slice deferred until scale hides integration problems;
- downstream systems built on unstable dependencies;
- late systemic change silently invalidates approved content;
- debug / tuning path too expensive to reproduce defects;
- beta / release claims made without representative target validation.

---

# 14. Remaining evidence gaps after the five-book foundation

Stage 1A's major gaps remain and are now more precisely bounded.

## 14.1 Accessibility and inclusive interaction — highest priority

The corpus is insufficient. Stage 2 must bring specialist and current evidence into the core model rather than relegating accessibility to an Extension Pack.

## 14.2 Games User Research methodology

Fullerton and Lemarchand provide practical playtesting; the project still needs broader evidence on:

- research design and bias;
- participant sampling;
- validity / reliability;
- qualitative synthesis;
- telemetry interpretation;
- privacy / consent;
- accessibility-inclusive research;
- remote / longitudinal / live research;
- when specialist GUR owns the method versus game design.

## 14.3 Gameplay-design / gameplay-engineering boundary

The corpus supports tunable prototypes, implementation-aware design and debug instrumentation but does not settle ownership between Game Development and Software Engineering for production code architecture.

## 14.4 Networked and multiplayer runtime design

Spatial / social and general multiplayer structures appear in the books, but the corpus does not sufficiently cover latency, authority, replication, prediction, desynchronisation, exploit / cheat surfaces or network-aware balance.

## 14.5 Performance and target-platform behaviour

Swink establishes that latency / frame behaviour matters; Lemarchand establishes production relevance. Current target-specific thresholds, profiling methods and certification requirements remain outside the corpus.

## 14.6 Live operations and longitudinal tuning

Metrics and post-release updates appear in the corpus, but economy intervention, remote configuration, experiments, seasons, live incidents and long-term player ecology need broader research where relevant.

## 14.7 Automated gameplay evaluation

Adams/Dormans support simulation and the bootstrap already anticipates automated agents, but the corpus is insufficient to define the boundary between structural automation and human experiential authority.

---

# 15. Book-to-book relationship summary

| Relationship | Finding |
|---|---|
| Fullerton ↔ Lemarchand | Strong support. Lemarchand explicitly builds on playcentric design and extends it into an end-to-end production / commitment system. |
| Fullerton ↔ Adams/Dormans | Strong support on formal systems, prototyping and balance. Adams/Dormans add deeper formal / simulation methods; Fullerton keeps stronger continuous player-evidence emphasis. |
| Fullerton ↔ Swink | Complementary. Fullerton defines broad experience goals; Swink decomposes a narrow but important moment-to-moment experience into tunable interaction variables. |
| Fullerton ↔ Totten | Strong support. Totten spatialises the playcentric loop through diagrams, greyboxes and audience observation. |
| Adams/Dormans ↔ Totten | Complementary and sometimes tension-producing. Mechanics structure missions / progression; Totten shows that spatial design itself generates and communicates gameplay. Neither should be subordinate by default. |
| Adams/Dormans ↔ Swink | Complementary. Adams/Dormans focus largely on discrete / systemic mechanics; Swink fills continuous control / perception / response. |
| Adams/Dormans ↔ Lemarchand | Support on early proof and late freezes, but exact lifecycle prescriptions differ. Use shared risk logic rather than either phase model verbatim. |
| Swink ↔ Totten | Strong complement. Swink's simulated-space context and Totten's level geometry both show that control cannot be evaluated independently of space. |
| Swink ↔ Lemarchand | Strong support around primary controls / game feel / polish and iterative tuning, with Lemarchand adding production integration. |
| Totten ↔ Lemarchand | Strong support around blockout / greybox, tutorial design, representative production and cross-discipline integration. |

---

# 16. Stage 2 handoff

Stage 2 should use this model to **challenge, not merely decorate**, the corpus.

Research should test:

```text
which provisional capabilities match strong professional practice
which book heuristics fail outside their original context
which gaps require new core capabilities
which roles own each responsibility in contemporary production
which artefacts actually carry decisions between disciplines
which approval / commitment points are used and why
which failures recur in practice
which repair scopes minimise wasted work
which quality claims require human, deterministic, telemetry or target-hardware evidence
```

Priority challenge areas:

1. accessibility / inclusive game interaction;
2. specialist Games User Research;
3. gameplay design vs technical design vs gameplay programming boundaries;
4. current prototyping / vertical-slice / production practice across indie, AA, AAA, mobile and other scales;
5. modern performance / input-latency / target-build practice;
6. automated gameplay testing and simulation limits;
7. multiplayer / network-aware gameplay production;
8. live tuning where relevant;
9. counterexamples to hard locks, concentric ordering and architecture-derived heuristics.

Stage 2 must preserve claim dispositions:

```text
supported finding
qualified method
context-dependent heuristic
disputed claim
unresolved question
rejected idea
```

---

# 17. Exit-criteria verification

Stage 1B requires all five selected books to be meaningfully examined for their intended contributions, with traceable findings, conflicts, limitations and a provisional capability model.

Verification:

- [x] all five selected books were directly accessible in full source form;
- [x] all five were directly examined beyond metadata, contents pages and publisher summaries;
- [x] reading coverage is recorded honestly rather than claiming exhaustive cover-to-cover review;
- [x] each source has independently expressed findings tied to identifiable chapters / sections;
- [x] source concepts are translated into production behaviour, evaluation, failure / repair and dispositions;
- [x] overlap and mutual support are explicit;
- [x] material conflicts are preserved rather than erased;
- [x] unconditional concept locking is rejected in favour of explicit commit / reopen semantics;
- [x] Swink's narrow game-feel definition is prevented from excluding legitimate game forms;
- [x] Machinations is treated as an optional modelling method, not project architecture;
- [x] architectural analogy is treated as a hypothesis source rather than universal behavioural proof;
- [x] historical numeric performance / response thresholds are marked for current challenge research;
- [x] a source-to-capability matrix exists;
- [x] the provisional capability model is capability-shaped rather than book-shaped;
- [x] candidate evaluation / benchmark fixtures are identified;
- [x] unresolved accessibility, GUR, engineering-boundary, network, platform, live and automation gaps are explicit;
- [x] no source PDF, substantial copyrighted passage or private source location is committed;
- [x] Stage 2 has a clear evidence-qualified challenge agenda.

**Stage 1B exit gate: PASS.**

**Next stage:** Stage 2 — Challenge and Extend Professional Game-Development Practice.
