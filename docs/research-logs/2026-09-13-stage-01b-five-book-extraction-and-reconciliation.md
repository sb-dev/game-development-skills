# Stage 1B - Five-Book Extraction and Reconciliation

**Date:** 13 September 2026  
**Version:** 1.0  
**Corpus revision:** 2 (`CORPUS-02`)  
**Status:** Stage 1B complete; Stage 2 challenge research not started  
**Bootstrap:** [Version 1.1, Stage 1B](2026-09-07-game-development-skills-new-project-bootstrap-process.md#6b-stage-1b---extract-and-reconcile-the-five-book-corpus)  
**Detailed evidence:** [35 direct book findings](2026-09-13-stage-01b-book-findings.md)

## 1. Outcome and governing boundary

All five user-supplied books have now been meaningfully examined through focused body passages for their intended contributions. This record turns that reading into a provisional model of game-development responsibilities, with evidence limits and candidate evaluation cases. It completes the direct-extraction gate; it does not validate the books' claims through independent research or demonstrate an implemented capability.

The governing Seed remains the [Stage 1 charter](2026-09-12-stage-01-project-charter-and-domain-boundary.md): game design plus playable integration, human evidence for experience claims, accessibility as core quality, reproducible execution and targeted repair. The charter's first proof remains one bounded local single-player session. This stage selects no engine, core skill list, command names, Extension Packs or production scaffold.

The branch baseline is [`3777a22e`](https://github.com/sb-dev/game-development-skills/commit/3777a22ee1b657c4310a215c044c985174eb8681), containing the completed [Stage 1A selection record](2026-09-12-stage-01a-knowledge-coverage-and-five-book-corpus.md). The [family domain-research process v1.0](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/bootstrap/domain-research-process.md) remains the research method. Historical selection and access statements in Stage 1A describe 12 September; the active corpus and access state below supersede them.

## 2. Corpus revision and direct-source access

### 2.1 Decision `CORPUS-02`

On 13 September the user supplied five books after the Stage 1B access request. Four retain the Stage 1A selection. The fifth is Adams and Dormans's *Game Mechanics: Advanced Game Design*, previously candidate C7, in place of the assistant-selected Sellers title. Treat the supplied set as the active five-book corpus. No user-supplied book is excluded or demoted.

Preserve B1, B3, B4 and B5 as stable identities. Assign **B6** to Adams/Dormans, retaining C7 as its historical candidate alias. **B2** continues to mean Sellers and is retired from the active corpus; its identity is not reused. This changes one book, not the five-book count or the charter's coverage requirements.

The trade-off is concentrated mechanics, resource-flow and progression analysis in place of the broader systems bridge anticipated for Sellers. Direct reading now supports those particular contributions through M1-M7. It does not prove equivalence to Sellers's unexamined remainder. B1 and B5 help connect systems to experience and production, while broader systems coverage remains a Stage 2 question. Lemarchand's discussion of Sellers in L3 is a **secondary citation**, not direct extraction from a sixth active book.

### 2.2 Edition and access register

All five have the access label **full text available** through user-supplied PDFs. Bibliographic identity was checked in their title/imprint pages; the page counts identify these supplied representations, not every edition or electronic format.

| ID | Active source and edition | Identity checked in supplied copy | PDF pages | Finding IDs |
|---|---|---|---:|---|
| B1 | Tracy Fullerton, *Game Design Workshop: A Playcentric Approach to Creating Innovative Games*, fifth edition, 2024 | Title/imprint PDF pp. 6-7; print ISBN 9781032607009 | 587 | F1-F7 |
| B6 (formerly C7) | Ernest Adams and Joris Dormans, *Game Mechanics: Advanced Game Design*, 2012 | Title/imprint PDF pp. 3-5; ISBN 9780321820273 | 625 | M1-M7 |
| B3 | Steve Swink, *Game Feel: A Game Designer's Guide to Virtual Sensation*, first edition, copyright 2009 | Title/imprint PDF pp. 4-5; ISBN 9780123743282. Stage 1A's 2008 publication / 2009 copyright distinction is retained. | 377 | S1-S6 |
| B4 | Christopher W. Totten, *An Architectural Approach to Level Design*, second edition, 2019 | Title/imprint PDF pp. 2-4; paperback ISBN 9780815361367 | 626 | T1-T7 |
| B5 | Richard Lemarchand, *A Playful Production Process: For Game Designers (and Everyone)*, 2021 | Title/imprint PDF pp. 2-3; ISBN 9780262045513 | 486 | L1-L8 |

**Location convention:** all references in both Stage 1B files are one-based **PDF pages in the supplied copy**, counting front matter. They are not printed-page numbers. Adams/Dormans and Lemarchand use reflowed electronic pagination; chapter identity accompanies each finding so that it can also be located in other copies. No private filenames, access URLs or storage identifiers are needed in the published record.

## 3. Reading coverage and extraction method

The work used direct text from the supplied pages, chapter context, worked examples and selective visual inspection of diagrams. Front matter established identity and navigation; it did not count as substantive examination. Search located candidate passages, after which the surrounding text was examined for the method, example and limitations. Reading was focused on the intended contribution, not a claim of cover-to-cover reading or complete review of every named chapter.

The ranges below identify the **focused passage groups used**. They do not mean that all intervening chapters, exercises, citations or supplemental material were assessed. The more precise citations and dispositions in the findings file govern individual claims.

| Book | Body coverage supporting this stage | Intended contribution actually examined | Reading limits |
|---|---|---|---|
| B1 | Chapters 1, 3 and 7-11: PDF pp. 45-46, 50-54, 111-116, 251-253, 290-292, 326-329, 331-336, 352, 358-359, 363-368, 387-388, 433-439 | Experience hypotheses; procedures/rules; physical versus digital proof; playtest conduct; controlled retesting; completeness/balance; introductory accessibility. Iteration diagram on p. 51 inspected visually. | Selected chapter passages and contributed examples. Later production/career material and the full exercises were not systematically examined; specialist research and accessibility claims remain open. |
| B6 | Chapters 1, 3-6, 8 and 10-12: PDF pp. 19-25, 75-80, 94-99, 120-124, 170-175, 188-190, 246-255, 273-278, 323-326, 345-349, 385-394 | Mechanics/state; resources and feedback; emergence; simulated strategies and explicit model limits; mission versus space; progression dependencies; procedural meaning. Figure 6.21 on p. 174 inspected visually. | Selected modelling and progression examples. Companion software, exercises, appendix code and the complete pattern catalogue were not executed or exhaustively reviewed. |
| B3 | Chapters 1-2, 5-10 and 17: PDF pp. 20-23, 62-65, 100-103, 120-124, 138-143, 158-161, 164-173, 190-192, 316-321, 325-327 | Interaction loop; input/response measurement; response curves; collision/spatial context; feedback and representation; control ambiguity. Response-envelope diagrams on p. 142 inspected visually. | Selected explanation and tuning examples. The full case-study set and companion demonstrations were not exercised. Historical numeric/perceptual claims are not adopted as thresholds. |
| B4 | Chapters 2-8 and 11: PDF pp. 123-126, 155-158, 170-179, 232-239, 268-272, 311-314, 345-348, 396-402, 530-537 | Spatial diagrams and metrics; greybox iteration; camera; environmental cues; risk and respite; onboarding; bounded procedural construction/placement discussion. Figure 2.31 on p. 125 inspected visually. | Selected practical sections. Architectural history, the full narrative examples and all procedural approaches were not systematically examined. The author's procedural-experience limitation is retained. |
| B5 | Chapters 4-5, 10, 13, 17-19, 23-28 and 31-33, 35: PDF pp. 42-47, 54-58, 109-112, 118-124, 160-163, 168-173, 202-205, 222-224, 237-241, 254-256, 294-300, 302-304, 322-324, 346-356, 361-364, 390-395, 403-407, 413-415, 426-430 | Prototype purpose; representative integrated quality; concentric development; scope and dependencies; distinct test methods; telemetry validity; bug/build evidence; milestone limitations; late repair and delivery work. Figure 18.2 on p. 224 inspected visually for its matrix structure. | Selected production and testing passages. Narrative craft, full team-management practice, certification procedures and post-release operation were not investigated in depth. The book's full workflow was not enacted. |

The extraction produces **35 independently expressed records**. Each supplies a source location, concept/problem, applicability, production translation, evaluation, failure/repair, relationship and disposition. “Retain” means useful enough to carry into challenge research, not proven universal truth. Author-stated limitations and project-added qualifications are distinguished in the wording.

No book file, figure reproduction or substantial extract is published. No game, simulation, test session, participant study, analytics system or benchmark was run. The evidence in this stage is source examination; the proposed production behaviours and checks are design outputs.

## 4. Provisional capability model and source mapping

### 4.1 Owned decisions

The model organises responsibilities around decisions in an iterative production loop. Intent informs rules and representation; rules, controls and space are integrated into play; evidence guides a bounded correction or a revised commitment. A change can return work to any affected decision. This is not a mandatory sequence of thirteen phases or a proposed thirteen-skill architecture.

K1-K9 refer to the [Stage 1A knowledge dimensions](2026-09-12-stage-01a-knowledge-coverage-and-five-book-corpus.md#3-knowledge-coverage-map). Their required depth is unchanged by corpus revision. Finding IDs resolve in the [book findings](2026-09-13-stage-01b-book-findings.md). Workflow verbs below describe implications; command names and contracts belong to later stages.

| Capability / coverage | Source ideas | Owned responsibility: inputs, decision and output | Workflow implication |
|---|---|---|---|
| P01 — Frame an experience hypothesis; K1 | F1, M7, L1 | From audience, brief and constraints, decide what experience or meaningful choice to investigate; produce a hypothesis and observable question. | Frame intent, compare alternatives, retain or revise the thesis within existing authority. |
| P02 — Specify actionable mechanics; K2 | F2, M1, S3 | From a proposed verb, define allowed actions, state/data, transitions, timing, feedback, outcomes and reset requirements; produce implementable behaviour examples. | Specify rules, inspect boundary states, connect the contract to runtime checks. |
| P03 — Select adequate proof; K3/K6 | F3, S1, T1, L1, L2 | From uncertainty and material constraints, decide representation and fidelity; produce an experiment with explicit omissions and an evidence question. | Choose physical, modelled or runnable proof according to what must be learned. |
| P04 — Analyse systems and balance; K2/K5 | F6, M2, M3, M4 | From resources, interactions and goals, decide which feedback, strategies and cases need examination; produce a bounded model and hypotheses for actual play. | Model flows, compare scenarios, diagnose dominant or stalled behaviour, retune and recheck. |
| P05 — Tune controls and feedback; K3 | S2, S3, S5, S6, L6 | From intended action, device, states and cues, decide mapping and response; produce a tuned interaction, event traces and scoped human observations. | Instrument response, inspect ambiguous boundaries, change the responsible mapping or cue. |
| P06 — Integrate spatial play and content; K4 | M5, M6, S4, T1, T2, T3, T4 | From tasks, traversal metrics, camera and content requirements, decide layout/collision/cue relationships; produce playable space and handoff acceptance conditions. | Greybox, integrate assets, test in the player's view and preserve accepted routes and interactions. |
| P07 — Compose learnable encounters; K1/K4/K5 | T5, T6, M5, F4 | From audience knowledge, available actions and desired challenge, decide encounter sequence, information and recovery opportunities; produce an onboarding/encounter hypothesis. | Observe first use, expose the missing premise, adjust the relevant cue or challenge and retest. |
| P08 — Design and interpret evaluation; K5 | F4, F5, M4, S1, L5, L6 | From a claim, decide participants, method, conditions and instrumentation; produce evidence separating observation, intervention and interpretation. | Prepare a question-led test, verify collection, observe, analyse and qualify conclusions. |
| P09 — Integrate baseline accessibility; K7 | F7, S2, S5, T3, T5; charter | From critical tasks and relevant access needs, decide workable input/presentation alternatives; produce requirements, barrier findings and remaining exclusions. | Carry access conditions through proof and integration, seek relevant human evidence and repair specific barriers. |
| P10 — Scope and integrate deliverable increments; K6 | L2, L3, L4, T2 | From demonstrated play, dependencies, effort and commitments, decide next scope and fidelity; produce a coherent increment and revisable production plan. | Integrate from the core, expose uncertainty, cut with dependency checks and reopen material commitments when required. |
| P11 — Diagnose and repair while preserving accepted play; K2/K6 | F5, F6, S6, L7, L8 | From a reproducible finding, build and accepted decisions, identify cause and affected work; produce a bounded correction with replacement evidence. | Reproduce, classify, inspect dependencies, repair and recheck the defect plus affected accepted behaviour. |
| P12 — Establish playable delivery readiness; K8 | L4, L7, L8; charter | From a built candidate, target conditions and quality requirements, decide whether the evidence supports delivery; produce versioned run/reproduction evidence and unresolved issues. | Test the built output, inspect completeness/recovery, preserve provenance and record material exceptions or publication decisions with their owner. |
| P13 — Constrain procedural and emergent content; K2/K9 | M3, M6, T7, L7 | From generation/placement rules and progression constraints, decide reproducible cases and invariants; produce construction and playability findings. | Preserve failing seeds or configurations, check after placement, repair constraints and review generated play. |

P01-P12 are provisional responsibility descriptions, not claims of equal coverage. **P09 and P12 retain major evidence gaps** despite being core. P13 is a specialist direction for later demonstrated support. None of these rows establishes multiplayer, mobile, console or XR capability. The books contribute most strongly to K1-K6, introductory K7, delivery framing in K8 and selected systems/spatial aspects of K9.

### 4.2 Evaluation criteria and candidate benchmarks

Join each P row above to the matching row below to obtain the required chain: **source idea → capability → owned responsibility → workflow implication → evidence criterion → benchmark**. These original candidate cases probe failures suggested by the synthesis. They are unexecuted research inputs, not the later selected progressive examples, final benchmark suite or measured acceptance thresholds.

| Capability / case | Original candidate fixture | Evidence that would distinguish adequate work from failure |
|---|---|---|
| P01 / BC01 | A brief seeks tense decisions, but its proposed rewards make waiting indefinitely the safest choice. | Identify the intent/incentive conflict, propose an observable hypothesis and preserve contrary player evidence. Adding features or asserting that the game feels tense does not resolve the question. |
| P02 / BC02 | A short switch-and-gate session works once, but retry leaves the gate unlocked and ignores the interaction rule. | Specify initial, active, outcome and reset behaviour; reproduce the stale state and show that a correction restores the declared rule through repeated sessions. |
| P03 / BC03 | A paper prototype is offered as proof that a narrow input-timing mechanic is responsive. | Explain the representation limit and choose a bounded runnable interaction under declared conditions. Keep paper evidence for questions it actually answers. |
| P04 / BC04 | An inexpensive upgrade both earns more resources and makes later upgrades cheaper; two scripted strategies are compared. | Expose the reinforcing loop and model omissions, compare appropriate scenarios, and keep model outcomes separate from human balance claims. A stable graph alone cannot close the finding. |
| P05 / BC05 | The same button appears to fail near a movement-state boundary; the mean response time looks acceptable. | Tie signals, state changes and feedback to individual attempts; locate the boundary failure, evaluate a targeted change and inspect the relevant player task. No imported universal latency number closes the case. |
| P06 / BC06 | Replacing a greybox doorway with final art changes clearance and conceals its interactive edge from the normal camera. | Recheck collision, traversal and cue visibility in actual play against the accepted requirements. Identify the responsible geometry, collision or presentation change without discarding valid surrounding work. |
| P07 / BC07 | A new player repeatedly enters danger without recognising either the cue or the available defensive action. | Distinguish missing knowledge, unreadable warning and intended challenge; test a focused correction unaided. Extra explanatory text is not automatically a successful repair. |
| P08 / BC08 | A playtest reports high completion after frequent hints, while telemetry silently combines successive sessions. | Preserve the assistance, detect the invalid session boundary, repair collection and plan a suitable repeat. Decline the unsupported unaided-completion claim. |
| P09 / BC09 | A required state change is signalled only by hue and a brief sound. | Derive equivalent usable information and interaction under declared access conditions, check related critical tasks and seek appropriate participant evidence. Typical-player success cannot certify access. |
| P10 / BC10 | A convincing finished corner and several isolated features are used to justify a larger content commitment. | Inventory demonstrated integration and actual work, disclose unproven combinations, include review/test effort and trace dependencies before accepting or reducing scope. |
| P11 / BC11 | A late tuning request proposes a small jump-height reduction that could break an already accepted route. | Trace affected traversal, distinguish allowed tuning from a decision requiring reopening, and either retain the accepted value or support the authorised correction with affected-route evidence. |
| P12 / BC12 | A candidate works in the editor but lacks a required asset in its built output and cannot reproduce restart in a fresh project. | Test the identified built candidate and clean consumer path; record prerequisites and failures, repair the dependency/reset cause and repeat. A successful compile or release label is insufficient. |
| P13 / BC13 | A generated layout initially has a goal route, but later key/enemy placement makes a reproducible case unwinnable. | Check progression after placement, preserve the case, correct the responsible constraint and inspect related variations plus human play. Successful assembly is only one condition. |

### 4.3 Evidence and handoff boundaries

Deterministic work can check declared transitions, resets, bounded reachability and reproducible configurations. Generative work can propose mechanics, layouts, cues and test cases, with the proposal's assumptions kept visible. Judgement is needed to choose meaningful goals, interpret player behaviour, accept useful emergence and resolve creative trade-offs. Runtime tools supply actual execution, traces and builds. Those contributions complement one another; a scripted trace cannot stand in for a participant's experience.

Game Development owns gameplay requirements and their integrated acceptance. General engineering owns its implementation craft; art, animation and audio retain their craft authority. P05/P06 specify the timing, collision, presentation and other runtime properties required at the interface. P12 assesses game-specific delivery readiness, while the consumer retains release authority. The stage introduces no external service dependency or universal handoff schema.

The charter's minimum proof still needs a controlled verb, meaningful goal or choice, interacting rule, feedback, outcome and restart. A question-led toy is useful preparation; it does not close that installed proof. Source citations are bootstrap provenance, not a runtime requirement to possess these books.

## 5. Overlap, conflicts and source dependence

### 5.1 Reconciled methods

| Tension or overlap | Relevant findings | Provisional disposition and reason |
|---|---|---|
| Physical-first prototyping versus digital interaction proof | F3, L1, S1-S3 | **Adapt to the question.** Fullerton explicitly allows digital-first work when physical modelling is inadequate. Low cost is useful only if the representation exposes the disputed behaviour. |
| Rough experiments versus early polished core and vertical slice | F3, T2, S5, L1-L3 | **Separate the commitment being tested.** Cheap mechanics experiments and representative integrated-quality evidence serve different decisions. Feedback needed to perceive an interaction belongs in its test; finishing unrelated content does not. |
| Precise rules versus emergent or unpredictable play | F2/F6, M1/M3, S6 | **Retain both at different levels.** Locally understandable action responses can support globally surprising strategies. Classify surprise against intent before calling it a defect. |
| Balanced model versus balanced human play | M2/M4, F6, L5/L6 | **Qualify model conclusions.** Missing information, skill, bluffing, space and imperfect instrumentation can change the result. Simulation proposes and checks bounded hypotheses; actual interaction and human claims need their own evidence. |
| Single-purpose modularity versus useful coupling | F6, M3, L3/L7 | **Adapt modularity.** Boundaries aid diagnosis and stable integration but do not guarantee independent effects. Multiple uses and unexpected combinations can be valuable; inspect dependencies instead of enforcing an unconditional one-purpose rule. |
| Late feedback restrictions versus serious late findings | T2, F5, L8 | **Qualify cutoffs.** Preserve working content and constrain change impact, while allowing evidence to raise a finding. The charter controls reopening and material exceptions; calendar position alone does not make a defect acceptable. |
| Late accessibility/refinement and late technical-health emphasis versus core quality | F7, L7, S2/S5 | **Adapt timing.** Carry important access and execution constraints from the outset. Revisit them at later integration gates rather than postponing discovery until expensive commitments are fixed. |
| Seeing a lock first, mission-first layouts or making the first level late | M5/M6, T1/T5 | **Retain as contextual options.** Progression and spatial structure can inform one another. Building final onboarding later is compatible with investigating learning early; it does not justify delaying first-use evidence. |
| More instruction, more feedback or more metrics as a general cure | T4/T5, S5, L6 | **Reject the unconditional form.** Additional material can obscure useful signals or add collection cost. Repair the observed information gap and collect what the evaluation question needs. |
| Fixed sample counts, perceptual thresholds and claims of certainty | F5/F7, S2, L5 | **Research further.** Do not derive universal quotas, frame-rate gates, response budgets, discovery percentages or certain usability outcomes from these passages. Methods and thresholds require context and stronger evidence. |
| Tiny late edits versus large exploratory parameter changes | M4, L8, S3/S4 | **Distinguish exploration from acceptance.** Large temporary changes can reveal sensitivity in a model. Even a small accepted value change can affect many scenes; compare under actual conditions and inspect its dependencies. |
| A concept movie or a milestone label versus demonstrated readiness | L2/L7/L8, charter | **Retain communication value; require scoped proof.** Presentation and alpha/beta terminology cannot establish implemented combinations, correct builds, clean installation or permission to publish. |

### 5.2 Dependence is not corroboration

Several connections are explicit in the examined text. Lemarchand cites Fullerton and contributed prototyping advice in PDF pp. 44-46, Swink on sound in pp. 57-58, Totten among level-design resources on p. 121, and Fullerton on completeness on p. 392. Totten's greybox discussion draws on Fullerton's prototyping practice. B1 and B5 also share a playcentric teaching/production lineage.

These are useful links between methods, but they cannot be counted as independent replications. Contributed essays inside Fullerton are attributed where material. Lemarchand's Sellers discussion on pp. 169-170 is secondary material with its own context. Repeated psychological or player-type frameworks likewise remain claims to investigate, not empirical confirmation by the number of books mentioning them.

The corpus is strongest as a collection of practitioner methods and worked examples. Formal notation can make assumptions precise without validating them. Studio success stories do not isolate a method's causal effect, and architectural, perceptual or systems analogies do not automatically establish universal laws of player behaviour.

## 6. Unresolved claims and Stage 2 research queue

Stage 2 must both challenge these findings and investigate responsibilities the books did not establish. The queue below sets priorities without limiting that wider search. These are research tasks, not completed verifications or recommendations of current products.

| ID / priority | Question to resolve | Evidence or investigation needed | Affected responsibilities |
|---|---|---|---|
| G01 / high | Which playtest designs support which claims, with what participants and limitations? | Specialist games user research and relevant primary studies: sampling, facilitation, think-aloud effects, learning/repeat exposure, uncertainty, analysis and inclusion. Challenge F5/F7/L5 sufficiency and objectivity claims. | P07-P09; K5/K7 |
| G02 / high | What baseline access requirements and evaluation methods apply across the intended inputs and game forms? | Specialist accessibility practice, relevant standards and direct work with affected players. Investigate alternatives, configuration, timing, cognition and overlapping needs; distinguish usability from accessibility. | P05/P07/P09; K3/K7 |
| G03 / high | How should responsiveness and performance be measured on a declared target? | Current primary runtime/device documentation and appropriate perceptual evidence; distinguish frame time, input latency, variation and measurement limits. Historical Swink values are questions to check, not budgets. | P05/P12; K3/K8 |
| G04 / high | What makes gameplay, content and installed skills reproducible outside the development session? | Current engine/build and package/installation practice; versioned prerequisites, assets/imports, configuration, clean consumer tests and real execution. Investigate representative profiling and regression workflows. | P06/P11/P12; K4/K6/K8 |
| G05 / high | How do experienced teams detect and repair coupled mechanics, economy and progression failures? | Production postmortems, specialist systems/technical-design practice and research on modelling/automated exploration; compare assumptions, strategy coverage and cases where model findings fail in real play. | P02/P04/P11/P13; K2/K5/K9 |
| G06 / medium | Which prototype, slice and planning practices transfer to solo teams and atypical games? | Contrasting production accounts, small-team constraints, explicit failed cases and alternatives to the shared playcentric lineage. Challenge early-finish absolutes, stage cutoffs and forecasting claims. | P03/P10; K1/K6 |
| G07 / medium | How should required and rewarded actions be interpreted without overclaiming their effects? | Design cases and appropriate empirical work for learning, behaviour or other external-effect claims. Player interpretations and a plausible model cannot establish real-world validity. | P01/P04/P07; K1/K2/K5 |
| G08 / high for each claimed path | What differs in non-spatial, turn-based, procedural, simulation-heavy, multiplayer, mobile, console and XR production? | Independently investigate missing role/workflow responsibilities and representative execution/evaluation constraints. Do not generalise direct-avatar, authored single-player examples into support claims. | All relevant P rows; K9 |
| G09 / medium | Which camera, cue, onboarding and spatial-risk heuristics hold under different player abilities and genres? | Contrasting level/encounter practice, games research and actual observed cases. Challenge universal survival analogies, control assumptions and more-instruction prescriptions. | P05-P09; K3-K5/K7 |
| G10 / high before delivery | How are material changes, known issues and release acceptance handled in practice? | Current production/QA workflows, evidence retention and release verification, with specialist requirements obtained from their owners. Preserve the charter's authority boundary; do not copy historical platform or legal statements as current advice. | P10-P12; K6/K8 |

Additional content and implementation disciplines need independent research: combat and gameplay AI, technical design, animation/audio integration, technical art handoffs, test infrastructure and live tuning where relevant. Their absence from the strongest extracted findings must not remove them from the domain. The Stage 1A alternatives, including *Games User Research* and *The Gamer's Brain*, remain possible challenge inputs, not newly approved additions to the foundational five.

## 7. Exit criteria and next handoff

| Stage 1B requirement | Evidence in this stage | Result |
|---|---|---|
| Meaningfully examine all five books for their intended contributions | Edition/access register; focused body coverage in Section 3; F1-F7, M1-M7, S1-S6, T1-T7 and L1-L8 | Complete for this extraction gate; full-book and execution limits explicit |
| Per-book, traceable material findings with applicability, production, evaluation, repair, relationships and disposition | [Direct book findings](2026-09-13-stage-01b-book-findings.md) | Complete: 35 records |
| Source-to-capability mapping and provisional domain model | Section 4.1, including preserved K1-K9 coverage and owned decisions | Complete; provisional |
| Workflow, evidence and candidate benchmark implications | Joined P01-P13 / BC01-BC13 tables in Sections 4.1-4.2 | Complete as design outputs; no cases executed |
| Overlap/conflict analysis without false corroboration | Section 5 | Complete; conditional resolutions and unresolved empirical claims retained |
| Unresolved claims, gaps and next-stage input | Section 6 | Complete; current tools, specialist methods and runtime proof remain open |
| Respect source/publication and corpus boundaries | Five supplied books retained in revision 2; historical revision 1 preserved; only independent synthesis and source locations published | Complete |

**Next: Stage 2, Challenge and Extend Professional Game-Development Practice.** Its inputs are the charter, this corpus/access/coverage record, all 35 findings, the provisional P model, candidate cases and the gap queue. It must examine contrasting professional practice and missing responsibilities before moving to AI tooling or final architecture. Nothing in Stage 1B marks the installed playable proof, benchmark suite or release gates as passed.
