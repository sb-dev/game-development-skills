# Stage 1A — Domain Knowledge Coverage and Five-Book Corpus

**Project:** `game-development-skills`  
**Bootstrap stage:** 1A — Map Domain Knowledge Coverage and Select Five-Book Corpus  
**Status:** Complete  
**Date:** 12 September 2026

## 1. Stage purpose

This stage uses the completed Stage 1 charter as the Seed for bounded reconnaissance. Its purpose is to identify the important knowledge dimensions inside the `game-development-skills` boundary, compare a broader candidate pool, and select exactly five complementary books for direct examination in Stage 1B.

This stage does **not** perform the five-book extraction, broader Stage 2 professional-practice challenge, engine/tool research, or skill architecture.

The governing sequence is:

```text
Stage 1
→ define project goal and domain boundary

Stage 1A
→ bounded reconnaissance + select five complementary books

Stage 1B
→ directly examine, extract and reconcile the five books

Stage 2
→ challenge and extend the provisional model through broader professional research
```

## 2. Canonical inputs reviewed

Primary repository inputs:

- [`2026-09-12-stage-01-project-goal-and-domain-boundary.md`](2026-09-12-stage-01-project-goal-and-domain-boundary.md)
- [`2026-09-07-game-development-skills-new-project-bootstrap-process.md`](2026-09-07-game-development-skills-new-project-bootstrap-process.md)
- [`production-skills/docs/bootstrap/README.md`](https://github.com/sb-dev/production-skills/blob/main/docs/bootstrap/README.md)
- [`production-skills/docs/bootstrap/domain-research-process.md`](https://github.com/sb-dev/production-skills/blob/main/docs/bootstrap/domain-research-process.md)
- [`production-skills/docs/specs/01-production-skills-family-system.md`](https://github.com/sb-dev/production-skills/blob/main/docs/specs/01-production-skills-family-system.md)
- [`production-skills/docs/specs/02-production-skills-project-contract.md`](https://github.com/sb-dev/production-skills/blob/main/docs/specs/02-production-skills-project-contract.md)

Stage 1 established that `game-development-skills` owns **game design plus playable integration**: reusable production intelligence for designing gameplay, proving it cheaply, integrating it into a playable runtime, evaluating observed behaviour, and directing the smallest sufficient gameplay correction.

General software engineering, specialist asset-production pipelines, and consuming-project governance remain adjacent responsibilities.

## 3. Bounded reconnaissance method

Reconnaissance was deliberately limited to what was needed to choose the five-book foundation.

The selection process used four rules:

1. cover the Stage 1 ownership boundary rather than selecting five famous books;
2. prefer durable game-development knowledge over engine/provider-specific material;
3. favour books whose contributions are complementary rather than heavily overlapping;
4. preserve important gaps explicitly for Stage 2 instead of distorting the corpus to claim complete coverage.

The candidate pool was compared against:

```text
relevance to owned game-development responsibilities
coverage and depth added to the corpus
practical production contribution
credibility and limitations
useful contrasting perspective
currency / durability
source access
```

Publisher, bibliographic, table-of-contents, catalogue and preview material was examined only for **selection**. No book is treated as directly read or extracted in this stage.

## 4. Knowledge-coverage map

| Knowledge dimension | Why it belongs inside the boundary | Foundational need | Stage 1A conclusion |
|---|---|---|---|
| Player experience / game design | The repository must connect intended player experience to rules, decisions and observed play | A broad design and iteration backbone | Must be represented directly |
| Mechanics / systems / emergence | Interactive behaviour emerges from interacting rules, resources, feedback loops and state | Formal system reasoning, economy/progression modelling, simulation and balance | Must be represented directly |
| Controls / feedback / game feel | Playability depends on how input, motion, timing and feedback are perceived | Dedicated treatment rather than assuming mechanics correctness implies good feel | Must be represented directly |
| Levels / encounters / spatial design | Gameplay is expressed through spaces, encounters, pacing and player routing | Spatial workflows, greyboxing, guidance, level iteration and environment/gameplay coupling | Must be represented directly |
| Playtesting / balancing / iteration | Experiential claims require observed play and iterative correction | Prototype → playtest → evidence → revision methods | Covered across multiple selected books, with specialist GUR left for Stage 2 challenge |
| Production / integration / delivery | The project owns playable integration, not only abstract design | Milestones, commitment points, cross-discipline integration, representative slices and delivery | Must be represented directly |
| Accessibility / inclusive interaction | Accessibility is a core quality dimension in the bootstrap | Baseline inclusive practice and applicable player constraints | Important residual gap; must be challenged through specialist and current guidance in Stage 2 |
| Gameplay implementation boundary | The project specifies game-specific implementation decisions and acceptance criteria | Enough implementation awareness to connect design to runtime without becoming Software Engineering Skills | Covered indirectly; engine/code practice remains Stage 2/8 research |
| Multiplayer / networking | Some mature targets are networked | Game-specific behaviour and testing concerns, not transport/runtime engineering | Deliberately not foundational; Stage 2/8 gap |
| Performance / target-platform validation | Editor success is insufficient shipping evidence | Gameplay-facing performance budgets and representative-target validation | Deliberately not book-core; current official guidance belongs in Stage 2/8 |

### 4.1 Coverage principle

The five books are not one-book-per-category. The selected set is intended to produce interacting perspectives:

```text
playcentric design and iteration
+
formal mechanics / systems / balancing
+
control / feedback / feel
+
spatial / level production
+
end-to-end production discipline
```

The corpus is therefore a foundation, not a claim that all mature game-development knowledge fits into five texts.

## 5. Candidate pool

The bounded candidate pool contained eleven books with materially relevant coverage.

| Candidate | Relevance | Distinct contribution | Practical production value | Main limitation / overlap | Durability | Selection decision |
|---|---|---|---|---|---|---|
| **Game Design Workshop, 5th ed. — Tracy Fullerton (2024)** | Very high | Playcentric design, formal/dynamic systems, prototyping, playtesting, iterative design | Very high | Broad rather than deeply specialised in systems, feel or spatial design | High | **SELECT** |
| **Game Mechanics: Advanced Game Design — Ernest Adams & Joris Dormans (2012)** | Very high | Mechanics, emergence, internal economies, simulation, balancing, progression | Very high | Some tooling/examples are older; specialised rather than lifecycle-wide | High for underlying models | **SELECT** |
| **Game Feel — Steve Swink (2008)** | High | Virtual sensation, input response, feedback, perception, metrics for feel | High | Older examples; narrow by design | High for core interaction principles | **SELECT** |
| **An Architectural Approach to Level Design, 2nd ed. — Christopher W. Totten (2019)** | Very high | Spatial design, level workflows, greyboxing, guidance, pacing, tutorial and procedural-space concerns | Very high | Primarily spatial/level focused | High | **SELECT** |
| **A Playful Production Process — Richard Lemarchand (2021)** | Very high | Ideation through post-production, milestones, deliverables, collaboration, playtesting and sustainable production | Very high | One structured production framing must not become the universal workflow | High | **SELECT** |
| Rules of Play — Katie Salen Tekinbaş & Eric Zimmerman (2003) | High | Deep theoretical vocabulary, meaningful play, systems, emergence, information and culture | Medium-high | Significant overlap with Fullerton + Adams/Dormans; less direct production coverage per slot | High | HOLD / REFERENCE |
| The Art of Game Design, 3rd ed. — Jesse Schell (2019) | High | Broad multi-lens design heuristics and perspective shifting | High | Broad overlap with Fullerton; does not close a stronger missing dimension than the selected specialists | High | HOLD / REFERENCE |
| Advanced Game Design: A Systems Approach — Michael Sellers (2017) | Very high | Systems thinking and systemic game design | High | Strong overlap with Adams/Dormans in the five-slot corpus | High | HOLD / ALTERNATIVE |
| Games User Research — Anders Drachen, Pejman Mirza-Babaei & Lennart Nacke, eds. (2018) | Very high | Professional player research, playtesting methods, analytics, reporting, bias and special-needs research | Very high | Would displace a core design/production dimension; better used as high-priority Stage 2 challenge evidence | High | **STAGE 2 PRIORITY** |
| Designing Games — Tynan Sylvester (2013) | High | Experience engineering, emotion, rewards, multiplayer interaction, iteration and team process | High | Material overlap with Fullerton and Lemarchand | High | HOLD / REFERENCE |
| Challenges for Game Designers — Brenda Brathwaite & Ian Schreiber (2008) | High | Non-digital exercises across practical game-design topics | High for practice | Exercise-driven coverage overlaps Fullerton without closing a major gap | High | HOLD / REFERENCE |

## 6. Selected five-book foundational corpus

Exactly five books are selected.

### 6.1 Game Design Workshop: A Playcentric Approach to Creating Innovative Games

**Author:** Tracy Fullerton  
**Edition:** 5th  
**Publication:** 2024, A K Peters/CRC Press  
**Origin:** Selected during Stage 1A  
**Role in corpus:** Broad playcentric design and iteration backbone

Intended contribution:

```text
player experience goals
→ formal / dramatic / dynamic game systems
→ prototypes
→ playtests
→ evidence
→ revision
```

Why selected:

- directly links design intent to prototypes and observed player behaviour;
- supplies a practical foundation broad enough to connect the specialist books;
- current fifth edition refreshes the playcentric method and examples;
- provides deliberate overlap with later playtesting evidence so the corpus can reconcile methods rather than rely on one specialist source.

Limitations to test later:

- broad coverage may under-specify implementation, accessibility, telemetry and platform constraints;
- its process vocabulary must not automatically become repository architecture.

Selection evidence examined:

- publisher description;
- edition metadata;
- publisher table of contents / feature summary.

Direct Stage 1B source access: **not yet established**.

Publisher source: <https://www.routledge.com/link/link/p/book/9781032607016>

### 6.2 Game Mechanics: Advanced Game Design

**Authors:** Ernest Adams and Joris Dormans  
**Edition:** 1st  
**Publication:** 2012, New Riders  
**Origin:** Selected during Stage 1A  
**Role in corpus:** Formal mechanics, systems, economy, simulation and balancing

Intended contribution:

```text
mechanics
→ resource / state relationships
→ feedback structures
→ emergence / progression
→ simulation
→ balance diagnosis
```

Why selected:

- directly covers complex systems, emergence, internal economies, simulation and balancing;
- strengthens the bootstrap's requirement to treat emergence as evidence rather than noise;
- introduces cheap non-runtime representations for mechanics and economy uncertainty;
- offers explicit links among mechanics, level design and progression.

Limitations to test later:

- Machinations-specific examples are useful execution evidence but must not become a mandatory repository dependency;
- older implementation/tool assumptions require separation from durable mechanics principles.

Selection evidence examined:

- publisher/distributor description;
- chapter list including emergence, internal economy, simulation/balance, economies and progression;
- bibliographic metadata.

Direct Stage 1B source access: **not yet established**.

Publisher/distributor sources:

- <https://www.informit.com/store/game-mechanics-advanced-game-design-9780321820273>
- <https://www.oreilly.com/library/view/game-mechanics-advanced/9780132946728/copyright.html>

### 6.3 Game Feel: A Game Designer's Guide to Virtual Sensation

**Author:** Steve Swink  
**Edition:** 1st  
**Publication:** 2008, Morgan Kaufmann / Elsevier  
**Origin:** Selected during Stage 1A  
**Role in corpus:** Controls, feedback, perception and game feel

Intended contribution:

```text
player input
+
runtime response
+
movement / timing constraints
+
visual / audio / ancillary feedback
→ perceived virtual sensation
→ measurable feel questions
```

Why selected:

- isolates a production dimension that broad design texts routinely flatten into generic “polish”;
- directly supports the Stage 1 boundary around controls, feedback and playable integration;
- gives the corpus a specialist perspective on perception and response rather than only rules and systems.

Limitations to test later:

- published in 2008, so platform-specific examples and technology assumptions require qualification;
- “feel” remains partly experiential and cannot be reduced to automated metrics.

Selection evidence examined:

- Elsevier description;
- edition/publication metadata;
- table-of-contents summary including perception, sound, indicators, measurement and exercises.

Direct Stage 1B source access: **not yet established**.

Publisher source: <https://shop.elsevier.com/books/game-feel/swink/978-0-12-374328-2>

### 6.4 An Architectural Approach to Level Design

**Author:** Christopher W. Totten  
**Edition:** 2nd  
**Publication:** 2019, A K Peters/CRC Press  
**Origin:** Selected during Stage 1A  
**Role in corpus:** Level, encounter and spatial gameplay design

Intended contribution:

```text
mechanics / player needs
→ paper / diagrammatic spatial reasoning
→ greybox / blockout
→ pacing / guidance / encounters
→ playtest
→ spatial correction
```

Why selected:

- supplies dedicated spatial-design reasoning rather than treating levels as containers for mechanics;
- covers non-digital prototypes, digital greyboxing, iterative playtesting and level-design workflows;
- connects architecture, player behaviour, readability, tutorial design, procedural spaces and social interaction;
- is software-independent, matching the engine-agnostic bootstrap direction.

Limitations to test later:

- architecture is a productive lens, not a universal theory of level design;
- detailed combat/encounter tuning and non-spatial game forms need broader research.

Selection evidence examined:

- publisher description;
- detailed table of contents;
- publisher-provided excerpt material for part of the book.

Direct Stage 1B source access: **partial only; insufficient for complete extraction**.

Publisher source: <https://www.routledge.com/Architectural-Approach-to-Level-Design-Second-edition/Totten/p/book/9781351116305>

### 6.5 A Playful Production Process: For Game Designers (and Everyone)

**Author:** Richard Lemarchand  
**Edition:** 1st  
**Publication:** 2021, The MIT Press  
**Origin:** Selected during Stage 1A  
**Role in corpus:** End-to-end production, milestones, collaboration and delivery

Intended contribution:

```text
ideation
→ preproduction
→ playable proof / iteration
→ production commitments
→ collaboration / integration
→ post-production / delivery
```

Why selected:

- directly addresses taking a digital game project from concept through building, playtesting, iteration and completion;
- contributes milestone, deliverable and collaboration reasoning needed by the “playable integration” boundary;
- brings production cost and sustainability concerns into the corpus instead of treating design as detached from delivery;
- complements Fullerton by focusing more explicitly on project phases and production management.

Limitations to test later:

- the four-phase process is one strong production model, not a mandatory repository lifecycle;
- AAA/academic experience must be challenged against indie, live, mobile, multiplayer and other production contexts.

Selection evidence examined:

- MIT Press description;
- publication metadata;
- phase/milestone summary and author background.

Direct Stage 1B source access: **not yet established**.

Publisher source: <https://mitpress.mit.edu/9780262045513/a-playful-production-process/>

## 7. Corpus coverage matrix

Legend:

```text
P = primary contribution
S = supporting contribution
— = not a reason for selection
```

| Coverage dimension | Fullerton | Adams / Dormans | Swink | Totten | Lemarchand |
|---|---:|---:|---:|---:|---:|
| Player experience / game design | P | S | S | S | S |
| Mechanics / systems / emergence | S | P | S | S | S |
| Controls / feedback / game feel | S | — | P | S | — |
| Levels / encounters / spatial design | S | S | — | P | S |
| Playtesting / iteration | P | S | S | S | P |
| Balancing / progression / economy | S | P | — | S | — |
| Production / integration / delivery | S | S | — | S | P |
| Cheap representations / prototyping | P | P | S | P | P |
| Human experiential evidence | P | — | P | S | P |
| Accessibility / inclusive interaction | S / limited | — | limited | limited | limited |
| Platform / performance validation | — | — | limited | — | limited |
| Multiplayer / network-specific practice | limited | limited | — | limited | limited |

### 7.1 Why this combination won

The combination is stronger than five broad game-design books because each selected specialist adds a production capability that the others do not cover deeply:

```text
Fullerton
→ playcentric design backbone

Adams + Dormans
→ formal mechanics, economies, emergence and balancing

Swink
→ input, response, feedback and feel

Totten
→ level / spatial workflow and greybox reasoning

Lemarchand
→ production milestones, collaboration, integration and delivery
```

Replacing any specialist with another broad design text would improve redundancy more than coverage.

## 8. Important candidates not selected

### 8.1 Rules of Play

**Katie Salen Tekinbaş & Eric Zimmerman, 2003, MIT Press**

Strengths:

- deep vocabulary for play, rules, systems, emergence, information, social play and culture;
- highly durable theoretical reference.

Reason not selected:

- the five-slot corpus already gets broad game design from Fullerton and formal systems from Adams/Dormans;
- its marginal coverage gain is therefore lower than Swink, Totten or Lemarchand.

Disposition: retain as an important Stage 1B/2 reference if directly useful, but not one of the five foundational extraction obligations.

Source: <https://mitpress.mit.edu/9780262240451/rules-of-play/>

### 8.2 The Art of Game Design: A Book of Lenses

**Jesse Schell, 3rd ed., 2019, A K Peters/CRC Press**

Strengths:

- broad practical heuristic set;
- useful perspective-shifting questions across many design concerns.

Reason not selected:

- overlaps substantially with Fullerton's broad design role;
- does not close the specialist systems, feel, level-design or production gaps more efficiently than the selected corpus.

Disposition: broader reference and challenge source.

Bibliographic source: <https://books.google.com/books/about/Art_of_Game_Design.html?id=ihwU0QEACAAJ>

### 8.3 Advanced Game Design: A Systems Approach

**Michael Sellers, 2017, Addison-Wesley Professional**

Strengths:

- deep systems-thinking treatment;
- strong candidate for emergence and systemic design.

Reason not selected:

- overlaps directly with the Adams/Dormans specialist slot;
- Adams/Dormans was preferred because simulation, internal economy, balancing and progression map especially well to the bootstrap's cheap-representation and evaluation requirements.

Disposition: strong alternative / Stage 2 challenge source.

Source: <https://www.oreilly.com/library/view/advanced-game-design/9780134668185/>

### 8.4 Games User Research

**Edited by Anders Drachen, Pejman Mirza-Babaei & Lennart E. Nacke, 2018, Oxford University Press**

Strengths:

- professional player-research methods;
- testing in production;
- surveys, interviews, observation, RITE, heuristics, biometrics and analytics;
- reporting findings to production teams;
- affordability/scaling for smaller studios;
- coverage of players with special needs and mobile/VR contexts.

Reason not selected:

- extremely valuable, but the five foundational slots must also cover feel, level design, mechanics and production;
- Fullerton and Lemarchand provide enough initial playtest coverage for the foundational synthesis;
- GUR methods are ideal for Stage 2 because that stage explicitly challenges book-derived experiential claims with professional practice and current evidence.

Disposition: **high-priority Stage 2 source**.

Source: <https://academic.oup.com/book/26677>

### 8.5 Designing Games

**Tynan Sylvester, 2013, O'Reilly Media**

Strengths:

- experience engineering, emotions, mechanics, rewards, multiplayer interaction and iterative process;
- useful bridge between design and production.

Reason not selected:

- overlaps both Fullerton and Lemarchand;
- the selected specialist books close larger coverage gaps.

Disposition: supporting Stage 2 reference.

Source: <https://books.google.com/books/about/Designing_Games.html?id=sckajE19pFAC>

### 8.6 Challenges for Game Designers

**Brenda Brathwaite & Ian Schreiber, 2008**

Strengths:

- practical non-digital exercises;
- strong deliberate-practice orientation.

Reason not selected:

- valuable exercise format but significant overlap with Fullerton's prototype/playtest/design-practice role;
- does not close a larger Stage 1 boundary gap than the selected specialists.

Disposition: exercise and example reference.

Bibliographic source: <https://books.google.com/books/about/Challenges_for_Game_Designers.html?id=bS0W0QEACAAJ>

## 9. Source-access register

Stage 1A may complete with access gaps recorded. Stage 1B may not.

| Selected book | Selection evidence available | Full direct source access for Stage 1B | Stage 1B status |
|---|---|---|---|
| Game Design Workshop, 5th ed. | Publisher description, edition metadata, contents/feature summary | Not established | **BLOCKED pending access** |
| Game Mechanics: Advanced Game Design | InformIT/O'Reilly metadata, description and chapter list; limited preview material | Not established | **BLOCKED pending access** |
| Game Feel | Elsevier metadata, description and contents summary | Not established | **BLOCKED pending access** |
| An Architectural Approach to Level Design, 2nd ed. | Publisher description and detailed contents; limited publisher excerpt material | Partial only | **BLOCKED pending adequate access** |
| A Playful Production Process | MIT Press metadata and production-process summary | Not established | **BLOCKED pending access** |

No selected book has been treated as directly examined merely because catalogue, preview or publisher material was accessible.

## 10. Provided / retained / added / substituted decision log

No user-provided foundational game-development books were identified for this bootstrap stage.

Therefore:

| Decision type | Count | Result |
|---|---:|---|
| Provided books retained | 0 | No supplied books to preserve |
| Books added into empty corpus slots | 5 | Fullerton; Adams/Dormans; Swink; Totten; Lemarchand |
| Supplied-book substitutions proposed | 0 | Permission gate not triggered |
| Supplied books demoted | 0 | None |
| Pending substitution approvals | 0 | None |

The five selections therefore require no substitution permission under the canonical process.

## 11. Remaining gaps after corpus selection

The corpus intentionally leaves several questions for Stage 2 rather than pretending five books resolve the whole domain.

### 11.1 Accessibility and inclusive interaction

Highest-priority residual gap.

Stage 2 must challenge the corpus with current, authoritative accessibility practice covering applicable concerns such as:

```text
control remapping
input alternatives
sensitivity and timing tolerance
readability and colour dependence
captioning / subtitles
feedback redundancy
cognitive and motor demands
pause / speed options where compatible
players with disabilities in research
platform accessibility guidance
```

`Games User Research` provides one useful bridge but should be supplemented by current specialist and platform guidance.

### 11.2 Specialist playtesting, telemetry and research validity

The corpus has strong iterative design coverage but not enough methodological depth to make claims about:

```text
research design
bias / validity
sample selection
qualitative vs quantitative evidence
telemetry interpretation
RITE and other test methods
reporting and prioritisation
post-launch research
```

Stage 2 should use Games User Research and current professional evidence here.

### 11.3 Gameplay engineering boundary

The selected books are intentionally not engine/programming manuals.

Stage 2 must investigate how professional gameplay designers, technical designers and gameplay programmers divide responsibilities; Stage 8 later evaluates engines, coding agents and execution tools.

### 11.4 Multiplayer / networked play

The foundational corpus is not sufficient for:

- authority and replication implications for gameplay design;
- latency-sensitive feel;
- synchronised state and exploit surfaces;
- multiplayer encounter and social-system validation.

These are bounded Stage 2/8 research gaps.

### 11.5 Performance and target hardware

Current platform profiling, frame-time, memory, load-time, input-latency and build-validation practices are not suitable to freeze into a durable five-book corpus.

They require current official and professional research in Stage 2/8.

### 11.6 Live operations and post-launch tuning

The selected production book reaches post-production, but live-service telemetry, remote configuration, economy intervention and longitudinal tuning need separate professional research when relevant.

## 12. Stage 1B handoff

Stage 1B must directly examine the five selected books for their intended contributions and produce:

```text
per-book findings
reading-coverage records
source-to-capability matrix
overlap / conflict analysis
provisional game-development capability model
unresolved claims and gaps
```

The extraction must not rely on this Stage 1A comparison, publisher descriptions, model memory, secondary summaries or bibliographic metadata.

Before Stage 1B can pass, adequate direct access must exist for all five books.

## 13. Exit-criteria verification

Stage 1A requires:

- exactly five books selected;
- required supplied-book decisions resolved;
- access needs explicit;
- remaining knowledge gaps explicit.

Verification:

- [x] exactly five distinct books selected;
- [x] selection is based on complementary coverage rather than fame alone;
- [x] candidate pool is broader than the final five;
- [x] every candidate was assessed for contribution, limitations, durability and access at a selection level;
- [x] no user-supplied book substitution is pending;
- [x] source-access status is recorded for each selected book;
- [x] Stage 1B access blockers are explicit;
- [x] residual knowledge gaps are explicit;
- [x] engine/provider material was not used to pad the five-book corpus;
- [x] no book has been treated as directly examined in this stage;
- [x] no book-specific skill architecture has been inferred.

**Stage 1A exit gate: PASS.**

**Next dependency:** Stage 1B may begin only when adequate direct source access is available for all five selected books. Numbered Stage 2 remains gated on a completed Stage 1B provisional capability model.

## 14. Selection-source register

Selection-level public sources consulted:

1. Tracy Fullerton — *Game Design Workshop*, 5th ed., A K Peters/CRC Press: <https://www.routledge.com/link/link/p/book/9781032607016>
2. Ernest Adams & Joris Dormans — *Game Mechanics: Advanced Game Design*, New Riders: <https://www.informit.com/store/game-mechanics-advanced-game-design-9780321820273>
3. Ernest Adams & Joris Dormans — O'Reilly bibliographic / contents view: <https://www.oreilly.com/library/view/game-mechanics-advanced/9780132946728/copyright.html>
4. Steve Swink — *Game Feel*, Elsevier: <https://shop.elsevier.com/books/game-feel/swink/978-0-12-374328-2>
5. Christopher W. Totten — *An Architectural Approach to Level Design*, 2nd ed., A K Peters/CRC Press: <https://www.routledge.com/Architectural-Approach-to-Level-Design-Second-edition/Totten/p/book/9781351116305>
6. Richard Lemarchand — *A Playful Production Process*, MIT Press: <https://mitpress.mit.edu/9780262045513/a-playful-production-process/>
7. Katie Salen Tekinbaş & Eric Zimmerman — *Rules of Play*, MIT Press: <https://mitpress.mit.edu/9780262240451/rules-of-play/>
8. Michael Sellers — *Advanced Game Design*, O'Reilly/Addison-Wesley listing: <https://www.oreilly.com/library/view/advanced-game-design/9780134668185/>
9. Anders Drachen, Pejman Mirza-Babaei & Lennart E. Nacke, eds. — *Games User Research*, Oxford University Press: <https://academic.oup.com/book/26677>
10. Tynan Sylvester — *Designing Games*, bibliographic preview: <https://books.google.com/books/about/Designing_Games.html?id=sckajE19pFAC>
11. Jesse Schell — *The Art of Game Design*, 3rd ed., bibliographic preview: <https://books.google.com/books/about/Art_of_Game_Design.html?id=ihwU0QEACAAJ>
12. Brenda Brathwaite & Ian Schreiber — *Challenges for Game Designers*, bibliographic preview: <https://books.google.com/books/about/Challenges_for_Game_Designers.html?id=bS0W0QEACAAJ>

These sources justify corpus selection only. They are not substitutes for Stage 1B direct examination.