# Stage 1B - Direct Book Findings

**Date:** 13 September 2026  
**Version:** 1.0  
**Corpus revision:** 2  
**Companion:** [Stage 1B extraction and reconciliation](2026-09-13-stage-01b-five-book-extraction-and-reconciliation.md)

These independently expressed findings come from the user-supplied books. Every page reference is a **one-based PDF page in the supplied copy**, including front matter; it is not a print-page claim. Edition identities and reading coverage are recorded in the companion log. Production translations, proposed evidence and repair actions are this project's adaptations, not assertions that the authors specified these exact artefacts or tests.

Disposition and evidential standing are separate. A retained method remains a practitioner heuristic unless Stage 2 supplies stronger evidence. None of the proposed checks or benchmarks has been executed in this research stage.

## 1. Tracy Fullerton - Game Design Workshop, fifth edition, 2024

### F1. Make intended experience a design hypothesis

**Source:** Chapter 1, PDF pp. 45-46 and 50-54. **Disposition:** retain and adapt. **Standing:** practitioner method, with a contributed example by Eric Zimmerman on pp. 53-54.

**Concept and applicability:** Describe the situation or experience sought for players before choosing the features intended to create it. Prototypes and observations test those choices. This applies beyond competition or conventional entertainment; it does not make a designer's intended emotion an observed fact.

**Production and evaluation:** Input the brief, audience and constraints; produce an experience hypothesis, a proposed interaction and a question for a playable test. Compare observed choices and participant accounts with the hypothesis, preserving contrary findings. A feature checklist alone cannot close the experience question.

**Failure and repair:** If a technically correct feature produces the wrong experience, revisit the causal design assumption and change the smallest relevant interaction before adding more content. **Relationships:** F3 chooses the representation; L1 separates prototype purposes; M7 qualifies claims about meaning and real-world outcomes.

### F2. Specify player procedures and system rules together

**Source:** Chapter 3, PDF pp. 111-116. **Disposition:** retain. **Standing:** design-analysis method.

**Concept and applicability:** An actionable design distinguishes what players can do from the rules that adjudicate the result. Actor, timing, location, state and input constraints matter, including beginning and resolving play. Rules enforced invisibly by software still need an understandable player-facing consequence.

**Production and evaluation:** Translate a mechanic brief into allowed actions, preconditions, state changes, feedback and resolution conditions. Check normal, unavailable and boundary actions against those expectations; also observe whether players understand the consequences. These are gameplay requirements, not a mandate for a particular software architecture.

**Failure and repair:** Ambiguous adjudication, uncommunicated restrictions or a missing resolving action call for a rule clarification and corresponding runtime/feedback change, followed by affected-state checks. **Relationships:** M1 deepens state and mechanic specification; F6 examines completeness; S3 handles time-dependent response.

### F3. Choose prototype fidelity for the uncertainty

**Source:** Chapters 1, 7 and 8, PDF pp. 46, 51-54, 251-253 and 290-292. **Disposition:** adapt. **Standing:** practitioner heuristic supported by illustrative cases, not a universal cost model.

**Concept and applicability:** A prototype is a working investigation of selected questions. Physical representations can expose rules cheaply; digital ones can investigate interaction, technical feasibility or integration. Chapter 8 explicitly permits starting digitally when the question cannot be modelled adequately on paper.

**Production and evaluation:** Input an uncertainty and the conditions under which it matters. Select the cheapest adequate representation and state what it omits. Judge success by whether it answers the question, including a negative answer, rather than by resemblance to the finished game.

**Failure and repair:** A polished mock-up without the disputed behaviour gives weak evidence. Reduce unrelated finish or move to a runnable representation when timing, controls or coupling are the uncertainty. **Relationships:** S1 and L1-L2 explain when feel or integration requires richer fidelity; T1 supplies spatial representations.

### F4. Preserve an uncoached view of player behaviour

**Source:** Chapter 9, PDF pp. 326-329, 331 and 334-336; p. 352. **Disposition:** retain with qualification. **Standing:** practical playtest guidance; study validity remains subject to Stage 2.

**Concept and applicability:** Designer review, software QA and observation of target players answer different questions. Familiarity and explanation can conceal first-use failures. Participant selection, a focused script and recording interventions matter; friends and experienced repeat testers cannot substitute for every audience or learning question.

**Production and evaluation:** Produce a question-led session plan, relevant participant criteria, neutral tasks and a record separating observation, help given and interpretation. Evaluate unaided progress, misunderstandings and task-specific feedback. Choose think-aloud deliberately: its effect on timed or immersive play requires investigation.

**Failure and repair:** If coaching produces apparent success, retain that intervention in the evidence and retest the repaired interaction with suitable fresh participants. **Relationships:** T5 applies this to tutorials; L5-L6 distinguish testing purposes and metrics. Human participants remain necessary for human-experience claims.

### F5. Reproduce the disputed situation and recheck corrections

**Source:** Chapter 9, PDF pp. 358-359. **Disposition:** retain the controlled-test method; qualify quantitative claims. **Standing:** practitioner method with cited research claims requiring primary-source challenge.

**Concept and applicability:** A test can start at a relevant state or force a rare event instead of replaying the whole game. Repeated comparison can expose consequences of a change. This focused evidence does not replace full-session or population coverage.

**Production and evaluation:** Record the setup, relevant state, condition being varied, build and observed failure. After a bounded correction, repeat that situation and check affected accepted behaviours. Track unresolved and newly introduced findings as well as fixes.

**Failure and repair:** A fix may change neighbouring behaviour; an artificial setup may itself explain the failure. Diagnose both before expanding the implementation change. Do not turn the book's small-sample discovery estimate into a universal participant quota or percentage-of-quality gate. **Relationships:** M4 tests model assumptions; F6 and L7-L8 guide repair and change scope.

### F6. Separate functionality, completeness and balance

**Source:** Chapter 10, PDF pp. 363-368 and 387-388. **Disposition:** adapt. **Standing:** practical diagnostic framework; the author explicitly describes the staged account as a simplification.

**Concept and applicability:** A playable system may still have unresolved rules, dead ends or strategies that defeat the intended experience. Different failures need different questions. Balance depends on interactions and information, not only values in a spreadsheet; unexpected play is not automatically an exploit.

**Production and evaluation:** Classify a finding, identify the responsible rules and their dependencies, and compare possible corrections against the experience goal. Evaluate reachable resolution, declared invariants and observed strategic effects separately. Preserve useful emergence and record why an unintended strategy is accepted or repaired.

**Failure and repair:** Changing many rules at once obscures cause. Localise a change and recheck its connections. Treat modularity as an aid to reasoning, not a guarantee of independent effects or a ban on components serving several gameplay purposes. **Relationships:** M2-M4 address coupled systems; L3 supplies an incremental integration method.

### F7. Treat access barriers as production findings from the outset

**Source:** Chapter 11, PDF pp. 433-434 and 438-439; chapter 10, p. 365. **Disposition:** retain the task-based approach, adapt its timing and qualify sufficiency. **Standing:** introductory usability/accessibility guidance, not comprehensive accessibility evidence.

**Concept and applicability:** Fresh participants and a range of access needs can reveal barriers to starting, understanding and using a game that its designers no longer notice. The book recognises that accessibility extends beyond basic usability and points to specialist guidance.

**Production and evaluation:** Carry access needs into the brief, prototypes, control choices and presentation. Define critical tasks and relevant conditions; record barriers, assistance and remaining exclusions. Evaluate alternative interactions with appropriate participants rather than infer accessibility from majority success.

**Failure and repair:** Late discovery can require redesign, so reject late refinement as the sole timing for this work. Neither a small fixed sample nor successful familiar-player testing certifies access. Repair the specific barrier and revisit related tasks. **Relationships:** S2/S5 and T3/T5 affect input and presentation; Stage 2 must supply specialist coverage.

## 2. Ernest Adams and Joris Dormans - Game Mechanics: Advanced Game Design, 2012

### M1. Make mechanics implementable without requiring a complete state graph

**Source:** Chapter 1, PDF pp. 19-25. **Disposition:** retain and qualify. **Standing:** analytic design method.

**Concept and applicability:** Mechanics include operative rules, processes and data. Local state transitions can clarify behaviour, while enumerating every state of a complex game is impractical. A distinction between core and peripheral mechanics depends on the game; the book itself acknowledges that judgement.

**Production and evaluation:** Turn an intended action into precise data, conditions, transitions and interactions, with examples a runtime implementation can satisfy. Use state models where they clarify a bounded component. Check agreement between specified behaviour and the playable implementation, including outcomes and invalid actions.

**Failure and repair:** A diagram covering only a convenient subset can conceal missing behaviour. Document omissions and test relevant boundaries; do not infer that every game needs a universal state-machine architecture or that gameplay AI is always peripheral. **Relationships:** F2 provides player-facing procedures; M2 represents resource dynamics; S3 handles continuous response.

### M2. Trace resource flows and feedback before tuning values

**Source:** Chapters 4-6, PDF pp. 94-99, 120-124 and 170-175; figure 6.21 on PDF p. 174 visually inspected. **Disposition:** retain the analysis, adapt the notation. **Standing:** formal modelling method with illustrative simulations.

**Concept and applicability:** Health, ammunition, time and other quantities can form an economy. Record where resources enter, leave, transform or exchange, and how their state changes subsequent flows. Reinforcing and stabilising loops can alter advantage or pacing; a loop's presence does not prove its effect is desirable.

**Production and evaluation:** Input resource definitions, rates, timing and player choices. Produce a bounded flow model with explicit abstractions; examine depletion, accumulation and advantage over time against the game's goals. Distinguish resource movement from control of that movement.

**Failure and repair:** Fix the feedback cause of a runaway advantage or stall rather than repeatedly compensating with unrelated values. Recheck neighbouring loops. Machinations is one notation, not a required installed provider or proof that all gameplay reduces to resource flow. **Relationships:** M4 qualifies simulation; F6 and L3 address change impact.

### M3. Preserve consistent interactions while investigating emergence

**Source:** Chapters 3 and 6, PDF pp. 75-80 and 188-190. **Disposition:** retain consistency and investigation; qualify general preferences about randomness. **Standing:** practitioner/complex-systems framing, not a validated universal theory of enjoyable play.

**Concept and applicability:** Unexpected behaviour can arise from combinations of simple rules and player choices rather than chance alone. Consistent interactions may create useful new tactics. Randomness has distinct frequency, distribution and impact; these are design choices, not interchangeable ways to create depth.

**Production and evaluation:** Record interaction hypotheses and declared invariants. Exercise combinations and varied conditions, distinguishing intended variation, novel strategies and harmful exploits. Compare player agency and outcome distributions under the actual intended conditions; preserve reproducible setups for failures.

**Failure and repair:** Removing every surprising tactic can destroy the intended play. Classify its effect before changing a rule. Conversely, increasing randomness may conceal a dominant strategy rather than repair it. Do not promote the book's preference for sparse chance, or its scientific analogies, into unconditional design laws. **Relationships:** F6 classifies exploits; S6 distinguishes local predictability from overall uncertainty.

### M4. Use simulated strategies to find questions for the real game

**Source:** Chapter 8, PDF pp. 246-255 and 273-278; chapter 6, p. 188. **Disposition:** retain with strong qualification. **Standing:** model-based analysis with explicit author-stated limitations.

**Concept and applicability:** Repeated runs of simple, fixed strategies can expose resource imbalances and parameter sensitivity. The authors explicitly distinguish artificial players from people and a balanced model from a balanced game. Some notation for skill or other players is simulated through random values, not an actual model of those abilities.

**Production and evaluation:** Declare the model, omitted behaviour, strategy scripts, parameters, termination limits and recorded outcomes. Compare strategy success, duration and resource trajectories. Confirm important effects in the actual playable game and with humans where skill, bluffing or perception matters.

**Failure and repair:** Equal results for two scripts do not establish general balance. Improve the model or strategy coverage before retuning the game. Large temporary parameter changes can reveal direction; restore context, randomness and integration before accepting a bounded fix. **Relationships:** F5 supplies repeatable conditions; S2 and L5 preserve the human-evidence boundary.

### M5. Relate mission structure to playable space

**Source:** Chapter 10, PDF pp. 323-326. **Disposition:** retain. **Standing:** design decomposition with worked examples.

**Concept and applicability:** A sequence of challenges and the geometry accommodating it are related but distinct. The same space can support different missions; a linear task dependency need not require a linear corridor. Starting with mission structure is useful in some cases, but the text explicitly allows space-first design.

**Production and evaluation:** Input the available mechanics, intended challenges and spatial constraints. Produce a challenge/dependency representation and map it onto a greybox. Check whether the space supports the required choices, timing and alternatives, and whether repeated tasks supply meaningful variation for the intended experience.

**Failure and repair:** A valid task list can still create dull repetition or forced geometry. Adjust challenge composition or its mapping before rebuilding the whole level. **Relationships:** T1-T4 develop spatial representations and encounter context; M6 checks progression dependencies; L4 connects content structure to planning.

### M6. Check progression dependencies in the space and state model

**Source:** Chapter 11, PDF pp. 345-349. **Disposition:** retain and qualify. **Standing:** practical progression-pattern analysis.

**Concept and applicability:** Access conditions can represent capabilities or other state changes as well as literal keys. Mapping dependencies to nonlinear space can change what players encounter and understand. Seeing an obstacle before its solution is a contextual guidance heuristic, not a requirement for open exploration.

**Production and evaluation:** Define prerequisites, access effects and intended alternatives, then inspect their placement and order in a playable layout. Check required-item reachability, bypasses, prematurely accessible challenges and whether players recognise a newly available route. These checks can inform generated-level constraints later.

**Failure and repair:** Sharing one access capability among several routes can permit an unintended encounter order. Repair the dependency or placement and recheck affected routes instead of closing all exploration. **Relationships:** F2/F6 supply rule completeness; M5 separates task and space; T5 addresses learning and T7 generated layouts.

### M7. Test the meaning conveyed by required and rewarded actions

**Source:** Chapter 12, PDF pp. 385-394. **Disposition:** adapt; research further for external-effect claims. **Standing:** interpretive design argument with illustrative cases.

**Concept and applicability:** What a game requires, rewards and permits can communicate something different from its stated theme. Players participate in producing and interpreting that meaning; the authors acknowledge that the intended message may not be received. A successful simulation strategy does not validate an equivalent real-world claim.

**Production and evaluation:** Compare the intended theme or experience with viable player actions, incentives and outcomes. Use participant interpretation and observed strategy as evidence about this game. Educational, behavioural or scientific effectiveness needs separate appropriate evidence.

**Failure and repair:** Explanatory text cannot reliably compensate for mechanics that reward the opposite behaviour. Revisit incentives or available choices and retest interpretation. Avoid claiming that the source's examples prove universal political, psychological or learning effects. **Relationships:** F1 states intent; S5 and T4 align presentation; broader empirical claims remain for Stage 2.

## 3. Steve Swink - Game Feel, first edition, copyright 2009

### S1. Evaluate the interaction loop as a whole

**Source:** Chapter 1, PDF pp. 20-23; chapter 5, pp. 100-103. **Disposition:** retain within scope. **Standing:** practitioner framework with an explicitly chosen definition.

**Concept and applicability:** Swink's account of feel links continuous control, spatial interaction and perceptual effects. The player's intent and interpretation are part of the loop. It is especially useful for direct real-time interaction; its definition is not a boundary excluding turn-based, non-spatial or other legitimate games from the repository.

**Production and evaluation:** From an intended verb and experience, identify the device, response, space and feedback needed for a meaningful playable trial. Evaluate their relationship through both runtime observations and people controlling the game. A polished video or isolated rule simulation cannot establish the full interaction experience.

**Failure and repair:** If an isolated controller feels right but the game does not, investigate the surrounding space and feedback before replacing the controller. **Relationships:** F3 selects adequate fidelity; S3-S5 locate specific causes; L2 integrates the pieces into a representative playable.

### S2. Measure response without turning historical thresholds into gates

**Source:** Chapters 2, 5 and 6, PDF pp. 62-65, 100-103 and 120-124. **Disposition:** retain measurement; research further on numerical and perceptual claims. **Standing:** engineering observations mixed with historical perceptual-model claims.

**Concept and applicability:** Physical input, its mapping and the delay until perceptible feedback affect control. Traces can reveal what happened around an apparently ignored action. Measured timings and a player's perceived responsiveness are related but distinct; device design and player capabilities matter.

**Production and evaluation:** Record the input method, relevant signals, runtime events and visible/audible response under declared execution conditions. Inspect latency and variation alongside task performance and player reports. Preserve both measurement limits and differences between supported input paths.

**Failure and repair:** An acceptable average can conceal missed inputs or intermittent delay. Locate the responsible stage and retest it under representative conditions. Do not adopt the book's frame-rate, response-time or fixed human-processing thresholds as current universal acceptance values. **Relationships:** F7 adds access needs; S3/S6 diagnose mapping; execution and performance still need current research.

### S3. Specify and tune the response over time

**Source:** Chapter 7, PDF pp. 138-143; chapter 17, pp. 318-320. **Disposition:** retain as a useful representation. **Standing:** practical control-analysis method.

**Concept and applicability:** A button or axis can change position, force, orientation, animation or another simulation parameter. The shape of the response over time matters, as do reference frame and state. The book's envelope analogy is useful for explaining acceleration and release, but is not a required model for every controller.

**Production and evaluation:** Given a verb, specify what each input changes, in which state and reference frame, and its temporal response. Compare recorded input and output curves with intended behaviour; test transitions as well as sustained input and obtain human judgements of control.

**Failure and repair:** Slow acceleration and delayed acknowledgement are different problems. Adjust the appropriate curve, state transition or feedback rather than making every movement instantaneous. **Relationships:** F2/M1 specify mechanics; S2 measures delay; S4 evaluates response in its intended space; S6 checks ambiguous transitions.

### S4. Tune movement against its spatial and collision context

**Source:** Chapter 8, PDF pp. 158-161 and 164-168. **Disposition:** retain and qualify. **Standing:** practitioner spatial/interaction analysis with subjective examples.

**Concept and applicability:** Movement values acquire experiential significance through object spacing, camera reference and collision behaviour. A controller cannot be judged solely by a speed constant. The source's personal impressions and comparisons do not establish uniform perception across players.

**Production and evaluation:** Input intended movement, obstacle layout and collision response. Use representative test spaces to compare traversal, avoidance and contact behaviour. Record geometry and controller versions together; evaluate successful actions, collisions, perceived speed and unwanted camera effects under declared conditions.

**Failure and repair:** A change to layout or camera may invalidate previously accepted movement. Determine whether the failure lies in response, spacing, collision or presentation; revise that relationship and recheck neighbouring encounters. **Relationships:** T2-T4 connect greyboxing, cameras and spatial information; M5/M6 add task and progression constraints.

### S5. Integrate feedback around the information it must convey

**Source:** Chapters 9-10, PDF pp. 170-173 and 190-192; chapter 17, pp. 325-327. **Disposition:** adapt. **Standing:** aesthetic and perceptual heuristics, not universal laws.

**Concept and applicability:** Sound, animation, effects and visual treatment jointly communicate an interaction and establish expectations. They can contradict each other even when the underlying simulation is unchanged. The source's definition of polish concerns perceptual effects; it should not imply that gameplay feedback is optional or always late work.

**Production and evaluation:** Specify the event and intended information for each content handoff, then evaluate the combined cues in the running game. Check recognisability, synchronisation, obstruction and consistency with behaviour, including relevant alternative feedback paths.

**Failure and repair:** More effects can make an event less clear. Remove, retime or replace the conflicting cue while preserving the useful ones. Do not universalise the book's animation/style prescriptions or assume strong effects improve accessibility. **Relationships:** F7 constrains presentation; T4/T5 use cues spatially; L3 supports polishing a proven core without finishing all content.

### S6. Diagnose apparent unpredictability at control boundaries

**Source:** Chapter 17, PDF pp. 316-321 and 325-327. **Disposition:** retain within the intended experience. **Standing:** practitioner diagnosis and design heuristics.

**Concept and applicability:** Technically deterministic controls can feel inconsistent when near-simultaneous inputs resolve ambiguously, mappings change in an unnoticed state, or feedback is hidden. Predictable local response can coexist with uncertain strategic outcomes and emergent play.

**Production and evaluation:** Capture input ordering, relevant state and displayed result for a complaint. Exercise adjacent timings and state boundaries, then observe whether players can deliberately reproduce the intended action. This is a proposed test method; no universal grace period or buffering value is established here.

**Failure and repair:** Treat repeated input complaints as evidence to investigate rather than dismissing them because code behaved as written. Clarify the mapping, state indication or timing rule and retest accepted actions. **Relationships:** S2/S3 supply traces and response models; M3 preserves higher-level emergence; F5 provides controlled reproduction.

## 4. Christopher W. Totten - An Architectural Approach to Level Design, second edition, 2019

### T1. Use spatial representations to answer specific design questions

**Source:** Chapters 2-3, PDF pp. 123-126 and 155-158; figure 2.31 on p. 125 visually inspected. **Disposition:** retain. **Standing:** architectural/design method adapted to gameplay.

**Concept and applicability:** A relationship diagram explains required connections, views or functions; it is not already a floor plan. A level's spatial dimensions must accommodate its actual mechanics and moving elements. The book illustrates how an added cart required changing an existing tunnel convention.

**Production and evaluation:** Input the experience goal, mechanics and spatial requirements. Choose a relationship diagram, measured plan or runnable greybox according to the question. Check adjacency, sightlines, clearance and traversal against the actual gameplay configuration, including interacting objects.

**Failure and repair:** Reusing a standard layout or metric without its original assumptions can block play. Correct the affected geometry or requirement and recheck related routes before detailed art work. **Relationships:** M5 separates mission from space; S4 binds movement to context; T2 supports the transition to an integrated level.

### T2. Preserve gameplay through greyboxing and content replacement

**Source:** Chapter 3, PDF pp. 170-179. **Disposition:** retain with qualification. **Standing:** production practice illustrated by examples.

**Concept and applicability:** Simple geometry exposes spatial gameplay and approximates collision before detailed environment art. Iteration reveals reusable pieces and useful metrics. Modular assets can support change, but their dimensions and behaviour still need validation in context.

**Production and evaluation:** Produce a playable greybox with declared spatial/collision expectations and record the parts accepted in playtests. Supply these expectations to content production. After replacing or combining assets, recheck traversal, interaction, camera view and the relevant gameplay questions.

**Failure and repair:** Attractive geometry can silently alter collision or block an accepted route. Restore or adjust the affected piece and repeat the relevant checks. Prefer a local repair where the rest remains valid. The book's strong restriction on late gameplay feedback is qualified: important late findings still need explicit triage. **Relationships:** F5/F6 preserve accepted behaviour; S4 and L2-L3 cover integration.

### T3. Validate the player's view alongside the level layout

**Source:** Chapter 4, PDF pp. 232-239. **Disposition:** retain within the selected camera/interaction context. **Standing:** practical spatial heuristics, not a ranking of camera styles.

**Concept and applicability:** First-person, third-person and 2D views expose different information and impose different action constraints. Geometry visible in an editor may be unreadable while playing. The source connects platform landing, aiming and the visibility of approaching hazards to viewpoint.

**Production and evaluation:** For the intended actions, inspect approach, landing, target and hazard views through the actual camera. Record the available information and opportunity to react, with relevant screen and control conditions. Establish project-specific expectations through testing; the book supplies no universal reaction-time gate.

**Failure and repair:** A failed jump can be a view problem rather than a jump-strength problem. Adjust framing, obstruction, geometry or feedback and retest the action before retuning movement. **Relationships:** S2-S4 address timing and response; F7 carries access requirements; T4 provides environmental cues.

### T4. Make environmental cues consistent with behaviour

**Source:** Chapter 5, PDF pp. 268-272; chapter 3, pp. 177-178. **Disposition:** adapt. **Standing:** communication/design heuristics with practitioner examples.

**Concept and applicability:** Repeated assets teach expectations when their appearance and behaviour remain recognisable. Interactive elements must be distinguishable from scenery, and the relationship between an action and its consequence must be perceptible. Repetition alone does not prove understanding.

**Production and evaluation:** Specify the gameplay meaning of cues, their behaviour and the circumstances in which players must notice them. Evaluate recognition and appropriate action in context, including alternative channels where needed. Content handoffs must preserve this information, not only visual similarity.

**Failure and repair:** An unnoticed cue calls for diagnosis of contrast, placement, timing or meaning. The source's advice to add more effects is a possible intervention, not a universal minimum cue count; excessive effects can obstruct play. **Relationships:** S5 checks combined feedback; T5 checks learning; F7 prevents colour-only or otherwise exclusionary acceptance assumptions.

### T5. Derive onboarding from observed missing knowledge

**Source:** Chapter 3, PDF pp. 176-178; chapter 8, pp. 396-402. **Disposition:** retain and qualify. **Standing:** practical learning-design method supported by case studies.

**Concept and applicability:** Audience labels do not reliably tell a designer what players already understand. Playtests reveal which controls, conventions or contextual ideas need introduction. Building final first levels later can avoid teaching obsolete mechanics, while testing learnability remains an early responsibility.

**Production and evaluation:** Record assumed prior knowledge, observe where intended players struggle, and build the smallest useful explanation or practice situation. Evaluate unaided use and later application of the mechanic; track assistance and prior familiarity.

**Failure and repair:** More exposition is not always better. If confusion comes from a missing premise or control distinction, repair that specific gap and retest, rather than adding a long generic tutorial. **Relationships:** F4 supplies neutral observation; T4/S6 clarify cues and states; L1/L2 separate early learning experiments from production-ready introduction content.

### T6. Compose encounter risk, respite and reward spatially

**Source:** Chapters 3, 6 and 7, PDF pp. 174-175, 311-314 and 345-348. **Disposition:** retain as contextual heuristics. **Standing:** architectural and motivational framing requiring broader challenge.

**Concept and applicability:** The relation between exposed areas, protected viewpoints, traversal distance and visible rewards can shape decisions and pacing. Alternating demands may make an encounter readable, but neither a spatial form nor a reward guarantees a particular emotion.

**Production and evaluation:** Map threats, information, potential refuge, resource costs and optional rewards onto the playable space. Observe route choices, ability to assess danger and recovery opportunities against the intended experience. Include the actual enemy and resource configuration in the test.

**Failure and repair:** An apparently optional reward may become compulsory because of resource balance, or cover may be ineffective against the actual enemy. Adjust the responsible spatial/resource relationship and retest. Avoid universalising the book's human-survival analogies or prescribing evenly spaced intensity for every genre. **Relationships:** M2/M5 and S4 connect systems, missions and space.

### T7. Evaluate generated levels beyond successful assembly

**Source:** Chapter 11, PDF pp. 530-537. **Disposition:** retain as a specialist provisional direction. **Standing:** bounded practitioner account; the author states limits to his procedural-design experience.

**Concept and applicability:** Authored encounter chunks, placement rules and procedural variation can work together. Generation includes enemies and events as well as geometry. The account describes tested escape-route patterns and explains how the same geometry can play differently after enemy placement.

**Production and evaluation:** Define chunk purpose, connection constraints, progression and placement assumptions. Proposed checks should cover routes, required capabilities and encounter configurations across reproducible generated cases, with human review of the resulting play. A generator returning a level is only construction evidence.

**Failure and repair:** A valid route can become unusable after content placement. Preserve the failing generated case, repair the constraint or placement rule, then inspect affected variations. These checks are project translations; neither generator correctness nor procedural support is demonstrated here. **Relationships:** M3/M6 address emergence and dependencies; T2/T6 address authored content and encounter behaviour.

## 5. Richard Lemarchand - A Playful Production Process, 2021

### L1. Give each early prototype a question about player activity

**Source:** Chapters 4-5, PDF pp. 42-47 and 54-58. **Disposition:** retain and qualify. **Standing:** practitioner method, explicitly drawing on Fullerton and contributed prototyping advice.

**Concept and applicability:** Early experiments can investigate a small interaction without implementing the whole proposed game. The useful unit is what a player does and experiences, not merely a feature name. Physical, playful and digital representations reveal different things; platform constraints can make early execution choices important.

**Production and evaluation:** Record the question, relevant activity, representation and omitted systems. Build enough interaction and feedback to investigate it, then decide whether to retain, change or abandon the idea. Sound belongs early when it carries the information or sensation being tested.

**Failure and repair:** Building a complete scoring, enemy and narrative structure around an untested verb can bury the uncertainty in unnecessary work. Reduce the experiment to its question. A successful toy remains insufficient for the charter's complete bounded-session proof; required goals, outcomes and reset behaviour must later be integrated. **Relationships:** F1/F3 align intent and fidelity; S5 supplies perceptual context; L2 tests a broader commitment.

### L2. Use representative integrated play to support production commitments

**Source:** Chapter 10, PDF pp. 109-112 and 118-124. **Disposition:** adapt. **Standing:** practitioner method with large-studio and small-team variants, including an admitted incomplete vertical slice.

**Concept and applicability:** A vertical slice samples the core activity and significant kinds of content at enough fidelity to communicate the proposed game. A small finished area can establish audiovisual direction while the surrounding playable remains rough. Representation must disclose which qualities are demonstrated and which are only illustrated.

**Production and evaluation:** Select representative interactions, context, feedback and difficult integrations. Produce a playable sample, a record of actual work and an explicit list of unproven features or content types. Use these to review scope and quality commitments. A visually finished corner establishes only that corner's achieved quality, not whole-game completeness or predictable total cost.

**Failure and repair:** The book permits supplementary concept movies when a full slice is impractical. Retain their communication value, but do not count a movie as evidence of runtime behaviour. Repair the missing proof with a bounded playable experiment before accepting a claim that depends on it. **Relationships:** S1/S4 and T2/T3 constrain integrated play; L4 translates observed work into a revisable plan.

### L3. Integrate outward from a stable, evaluable core

**Source:** Chapter 13, PDF pp. 160-163 and 168-173; chapter 27, p. 352; chapter 31, p. 394. **Disposition:** retain the incremental method and qualify its absolutes. **Standing:** practitioner account, drawing on systems analogies and Sellers as a secondary source.

**Concept and applicability:** Working outward from a few fundamental interactions can leave useful, playable intermediate results and expose integration problems earlier. What counts as fundamental depends on the game. Modularity does not prevent unexpected interactions; the book explicitly recognises both bugs and useful emergence, and later adjusts the method near milestones.

**Production and evaluation:** Identify the current core, integrate necessary behaviour and feedback, and add a supporting element only with a way to evaluate its effect. Keep a known working version and compare affected behaviour after each addition. Test at the level of the question; do not require every final detail before any valid evaluation can occur.

**Failure and repair:** Finishing isolated parts while their combination remains broken defeats the method. Stabilise the affected combination, reduce scope or revisit a dependency. Do not treat early polish as photorealism, mandatory replacement of every default, or a guarantee that a project cannot overrun. **Relationships:** F6/M3 qualify coupling; S5 explains useful early feedback; L7 handles incomplete feature combinations.

### L4. Plan scope from demonstrated work and explicit dependencies

**Source:** Chapters 17-19, PDF pp. 202-205, 222-224, 237-241 and 254-256; figure 18.2 on p. 224 visually inspected for its matrix structure. **Disposition:** retain and adapt. **Standing:** studio-derived planning practice with explicit scale limits and acknowledged forecast uncertainty.

**Concept and applicability:** A compact overview can connect experience goals, content and required work without pretending that all details are settled. Task estimates, available effort and priorities help expose excess scope. A nominally low-priority item may still be indispensable because other content or progression depends on it.

**Production and evaluation:** Derive a scope map and task plan from the brief and playable discoveries. Include integration, review, testing and coordination work; identify responsibility, dependencies and uncertainty. Update the plan when observed effort or new requirements invalidate it. Evaluate coherence and feasibility of the remaining scope, not just completed-task counts.

**Failure and repair:** Cutting an apparently optional location can break progression. Trace dependencies before cutting and recheck the retained experience. Adapt task granularity to team and project size. A burndown projection informs decisions; it does not guarantee completion or require a particular tool, sprint length or document length. **Relationships:** M5/M6 connect content to progression; L2/L3 expose actual integration work; L8 includes delivery demands.

### L5. Match testing methods and participants to the claim

**Source:** Chapters 23-25, PDF pp. 294-300, 302-304 and 322-324. **Disposition:** retain distinctions, qualify objectivity and fixed sample sizes. **Standing:** practical account of studio testing and its adaptation to smaller settings.

**Concept and applicability:** Self-review, peer critique, first-use playtesting, usability work, market discussion, QA and automation answer different questions. Repeated developer play can conceal difficulty or legibility problems. Fresh participants are valuable for first-use questions; experienced participants remain appropriate for other questions.

**Production and evaluation:** State the question and relevant population, choose the method, and record build, task, setup and interventions. Prevent unintended advance knowledge when evaluating first use. Separate behavioural observation, participant reports, interpretation and code-check results. Preserve assistance and environmental differences in the record.

**Failure and repair:** Coached success, numeric survey scores or passing automation cannot independently establish the intended experience. Repair the design or test setup indicated by the evidence and retest. Do not import the book's participant counts, late-project cadence, strong claims of usability certainty or equivalence between informal rooms and controlled studies as universal rules. **Relationships:** F4/F5 and T5 guide observation and correction; L6 handles instrumentation.

### L6. Verify instrumentation before using telemetry to judge a design

**Source:** Chapter 26, PDF pp. 346-350. **Disposition:** retain and qualify. **Standing:** practitioner guidance with concrete accounts of missing data, session confusion and excessive recording.

**Concept and applicability:** Events, resource values, attempts and time in a section can reveal where to investigate a gameplay problem. Data is only useful if it records the intended behaviour under the actual session conditions. Frequency, performance cost and participant permissions constrain collection.

**Production and evaluation:** Derive a small event set from a design question, define session boundaries and inspect sample output against known actions. Test under the planned playtest conditions, including successive participants or restarts. Relate the resulting trace to observation and participant accounts. Honour applicable consent and data-handling requirements; this book is not current legal guidance.

**Failure and repair:** A silent logger failure or mixed sessions can invalidate a study. Repair and verify collection before interpreting or rerunning the affected evidence. Prefer data needed for the question to the source's general suggestion to collect more and filter later. A count does not by itself establish enjoyment, causation or an acceptable experience. **Relationships:** S2 supplies response traces; M4 limits model evidence; L5 establishes the human question.

### L7. Make build identity, feature combinations and bug status explicit

**Source:** Chapter 23, PDF pp. 299-300; chapters 27-28, pp. 351-356 and 361-364; chapter 31, pp. 390-395. **Disposition:** retain the evidence discipline; adapt milestone terminology and timing. **Standing:** production/QA practice within the author's process.

**Concept and applicability:** Feature presence, content completeness and reliable integrated behaviour are different claims. One example of each feature can leave risky combinations untested. A built game may behave differently from an editor session, and a developer's fix must still be checked in the resulting build.

**Production and evaluation:** Tie findings to a build and reproducible situation, expected and actual behaviour, severity, responsibility and resolution evidence. Choose a bounded test plan covering important combinations, progression and recovery. Distinguish implemented, verified, deferred and unresolved work. Explicit project exit conditions matter more than the label alpha or beta.

**Failure and repair:** Calling new behaviour content can conceal unfinished functionality. Expose the dependency and test the integrated case. An inaccessible required object or unrecoverable state needs a progression/reset repair unless the failure state is intentional and communicated. Do not postpone all QA, accessibility or performance investigation until a named milestone. **Relationships:** F2/F5/F6 define correctness and correction; M6/T7 expose progression failures; L8 governs late changes.

### L8. Reassess late changes against their full impact and release evidence

**Source:** Chapters 32-33, PDF pp. 403-407 and 413-415; chapter 35, pp. 426-430. **Disposition:** adapt and qualify. **Standing:** practitioner release account; platform-specific requirements remain unexamined here.

**Concept and applicability:** A tiny numeric or visual change can alter many encounters. As remaining verification time shrinks, changes need clearer impact analysis and prioritisation. Delivery preparation also consumes development effort; reaching a milestone name does not establish that a distributable build is acceptable.

**Production and evaluation:** For a proposed correction, identify the affected rule or asset, dependent play situations, remaining test time and accepted decisions it would reopen. Prefer a bounded change that resolves the finding, then verify the changed build and affected accepted behaviour. Record unresolved issues and explicit release decisions. Include actual delivery work in scope, handing specialist marketing, legal and platform matters to their owners.

**Failure and repair:** Lowering jump height slightly can break required routes; treating it as a harmless value edit hides its impact. Recheck traversal or restore the accepted range. One-change-at-a-time is a useful diagnostic preference, not a ban on a justified coordinated repair. The book's strict postproduction cutoffs and treatment of closed known bugs do not override the charter's reopening and material-exception authority. **Relationships:** S3/S4 and T2 connect control, assets and space; L4/L7 connect scope and verification.

---

The [companion reconciliation](2026-09-13-stage-01b-five-book-extraction-and-reconciliation.md) maps all 35 findings to provisional owned capabilities, evaluation criteria and unexecuted candidate benchmarks. It records source dependence, rejected unconditional rules and the Stage 2 research queue.
