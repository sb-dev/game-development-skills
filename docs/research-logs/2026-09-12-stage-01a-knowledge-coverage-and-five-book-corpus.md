# Stage 1A - Knowledge Coverage and Five-Book Corpus

**Date:** 12 September 2026  
**Version:** 1.0  
**Corpus revision:** 1 (`CORPUS-01`)  
**Status:** Stage 1A complete; direct-source access remains incomplete for Stage 1B  
**Bootstrap:** [Version 1.1, Stage 1A](2026-09-07-game-development-skills-new-project-bootstrap-process.md#6a-stage-1a---map-domain-knowledge-coverage-and-select-five-book-corpus)

## 1. Decision and governing inputs

Select five distinct foundational books: Tracy Fullerton's *Game Design Workshop*, Michael Sellers's *Advanced Game Design*, Steve Swink's *Game Feel*, Christopher W. Totten's *An Architectural Approach to Level Design*, and Richard Lemarchand's *A Playful Production Process*. Edition identities appear in Section 5. Ten candidates were assessed; the choice is a qualitative judgement about their combined contribution to the charter.

The Seed is the completed [Stage 1 charter](2026-09-12-stage-01-project-charter-and-domain-boundary.md), reviewed at commit [`125e31b3`](https://github.com/sb-dev/game-development-skills/commit/125e31b39a4a3048b676128b7098d2c41ccb93da). It establishes ownership of **game design plus playable integration**, including human evaluation, accessibility, reproducible delivery and targeted repair. Its first proof is a bounded local single-player game; its mature boundary includes broader game forms and platforms subject to evidence.

The governing method is the [family domain-research process v1.0](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/bootstrap/domain-research-process.md), reviewed at family commit `20979e0c`. This record completes its selection gate, as required by the game-specific bootstrap. No books, book files or private reading locations were supplied by the user. All five places were therefore available for selection without a supplied-book substitution decision.

**Evidence boundary:** the coverage below is expected contribution, inferred from identified descriptions, contents, practitioner material and limited previews. It is not an extracted or validated capability model. No selected book has been examined sufficiently for its full intended contribution. Stage 1B extraction and reconciliation, and Stage 2 challenge research, remain separate unperformed gates.

## 2. Bounded reconnaissance

Reconnaissance began with the charter's owned decisions and failure conditions. Candidate discovery then sought books addressing those responsibilities, including plausible alternatives in general design, systems, spatial practice, human factors, research, programming and production. Publisher and author material established edition identity and intended scope. Accessible preview text was inspected to distinguish book content from marketing and to establish the limits of access.

Three practitioner sources helped check that the map did not collapse into general game-design advice:

| Source examined on 12 September 2026 | Observation used for selection | Consequence for the map |
|---|---|---|
| Steve Swink, [Game Feel: The Secret Ingredient](https://www.gamedeveloper.com/design/game-feel-the-secret-ingredient), 23 November 2007; opening discussion and sections on input, response and context | The author treats the sensation of control as something to prototype through the relationship between player action, runtime response and surrounding space. This is a practitioner account, not evidence that one control scheme suits everyone. | Keep moment-to-moment interaction distinct from rule correctness and visual finish. The article informs reconnaissance; it is not examination of the selected book. |
| Richard Lemarchand interviewed by Steve Bromley, [playtesting and A Playful Production Process](https://gamesuserresearch.com/richard-lemarchand-playtesting-and-a-playful-production-process/), 8 December 2021; discussion of early prototypes and types of testing | Early playable experiments need not be miniature finished games. Lemarchand also distinguishes design playtesting from rigorous user research. | Separate uncertainty reduction, delivery commitments and research validity. A production book cannot automatically satisfy the research-method gap. |
| [Game Accessibility Guidelines, full list](https://gameaccessibilityguidelines.com/full-list/); categorised guidance, including controls, information presentation and sensory alternatives | Inclusive interaction involves concrete constraints across input and presentation, beyond whether a typical player understands or enjoys a game. This is a practitioner guidance source, not certification. | Keep accessibility an explicit core requirement and investigate it independently of general usability or a chapter mentioning accessibility. |

Book contents also supplied useful contrasts: [Fullerton's fifth-edition overview](https://www.gamedesignworkshop.com/whats-new) spans design through iteration; [the Games User Research contents](https://academic.oup.com/book/26677) expose research validity and participant-inclusion questions; and [Lemarchand's contents](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/13082/toc_final.pdf?dl=1) expose production commitments and delivery. These helped compare likely contributions, without accepting chapter headings as demonstrated methods.

**Stopping rule:** stop after a charter-derived map, a ten-book comparison, a defensible five-book combination and an explicit access/gap register exist. This is not an exhaustive bibliography or Stage 2's investigation of professional roles, workflows, empirical findings and recurring failures. Unsuccessful page requests were not treated as reading evidence.

## 3. Knowledge-coverage map

Required depth comes from the charter, not the books. **Deep** means enough knowledge to direct a production decision, specify its evidence, diagnose failure and guide a bounded repair. **Interface** means enough to specify and assess an adjacent discipline's contribution. There is **no supplied-book coverage** in any row because no books were provided.

The B identifiers refer to the selected books in Section 5. “Expected” indicates a selection hypothesis; it does not mean the relevant chapters have been read or the responsibility is covered in practice.

| ID | Owned knowledge dimension and required depth | Expected foundational contribution | Remaining question or gap |
|---|---|---|---|
| K1 | Player intent, intended experience, meaningful choices and a testable game thesis — deep | B1 as the design-method anchor; B2 connects player experience to interacting systems | How do methods change for open-ended, narrative-led, turn-based or non-spatial play? Designer intent is not evidence of player experience. |
| K2 | Rules, state, mechanics, progression, balancing and emergence — deep | B2 supplies the main systems perspective; B1 provides complementary design iteration | Formal invariants, economy exploits, long-run behaviour, procedural constraints and reproducible failure cases need further investigation. |
| K3 | Controls, response, camera relationships, feedback and game feel — deep | B3 supplies specialist depth; B4 connects interaction to spatial context | Device variation, latency, motor access and the applicability of real-time examples beyond avatar control remain open. |
| K4 | Levels, encounters, traversal, pacing, collision intent and integrated content — deep; specialist asset craft — interface | B4 supplies spatial and level-production depth; B5 connects playable representations to production | Geometry alone does not establish collision correctness, readable affordances or successful art/audio/animation handoffs. Non-spatial games need different representations. |
| K5 | Playtest questions, observation, interpretation, balancing evidence and diagnosis — deep | B1 anchors iterative evaluation; B2 contributes balance questions; B5 connects testing to production decisions | Participant recruitment, bias, validity, telemetry interpretation and limits on claims need specialist research evidence. No autonomous proof of fun is implied. |
| K6 | Prototype purpose and fidelity, integration sequence, scope, commitments, preservation and targeted repair — deep | B5 supplies production depth; B1 and B4 add prototype and level iteration perspectives | Solo/small-team adaptations, approval reopening and preservation of accepted work need explicit methods and executed evidence. |
| K7 | Accessibility and inclusive interaction — deep core responsibility | B1 offers a starting point; B3/B4 may supply interaction questions, but specialist accessibility coverage is not established | Investigate barriers across input, presentation and cognition, representative participation and acceptable alternatives. Do not defer this responsibility with specialised platforms. |
| K8 | Gameplay readiness, target performance, repeatable build/run and clean consumer installation — deep game-specific acceptance; general engineering — interface | B5 provides delivery framing; no selected book establishes this repository's installation contract | Current engine/build behaviour, profiling, reproducibility, installation and regression evidence require current primary documentation and actual execution. |
| K9 | Broader game forms: procedural and emergent systems, multiplayer, mobile, console and XR — baseline awareness now; specialist depth before claiming support | B2/B4 offer possible foundations for some systems and spatial questions | Each claimed form needs its own methods, limitations and representative tests. A broad book description does not establish platform or genre support. |

The foundation deliberately combines a broad design method with specialist systems, interaction, spatial and production perspectives. This structure does not assign one book to each responsibility: K5 and K6 need several perspectives, while K7-K9 expose material gaps. It also does not propose five skills, packs, commands or mandatory workflow phases.

## 4. Candidate comparison and portfolio trade-offs

### 4.1 Relevance, practical contribution and added perspective

The following are selection judgements, not extracted findings. Titles not selected remain recorded alternatives; none was supplied and then demoted.

| Candidate | Relevance and practical contribution sought | Added coverage or useful contrast | Decision |
|---|---|---|---|
| B1 — Fullerton, *Game Design Workshop*, 5th edition (2024) | A connected method for framing a game, making prototypes, observing play and revising the design | A practical backbone against which specialist claims can be reconciled; its [author overview](https://www.gamedesignworkshop.com/) emphasises exercises and iteration | Select as the general design anchor. Prefer its connected practice to adding several broad survey books. |
| B2 — Sellers, *Advanced Game Design: A Systems Approach*, 1st edition (2017; copyright 2018) | Model interacting rules, loops and balance; connect local decisions to the whole game | [Publisher scope and contents](https://www.pearson.com/en-us/subject-catalog/p/advanced-game-design-a-systems-approach/P200000009594/9780134669458) indicate more systems depth than the general anchor, with links to experience and making a game | Select. Its anticipated breadth across systems and production is useful before choosing a particular economy or simulation tool. |
| B3 — Swink, *Game Feel*, 1st edition (2008; copyright 2009) | Direct the quality of player control and feedback, with concrete interaction experiments | The [publisher description](https://www.routledge.com/Game-Feel-A-Game-Designers-Guide-to-Virtual-Sensation/Swink/p/book/9780123743282) and the author's article point toward embodied interaction rather than only abstract rules | Select. This fills a specialist gap that another broad design book would leave shallow. |
| B4 — Totten, *An Architectural Approach to Level Design*, 2nd edition (2019) | Develop playable spatial representations and relate mechanics, layout and player understanding | The [second-edition preview](https://api.pageplace.de/preview/DT0400.9781351116299_A37413136/preview-9781351116299_A37413136.pdf) connects architecture and level practice; its contents include drawing, workflows and spatial organisation | Select. It strengthens owned level and content-integration decisions while keeping finished environment craft adjacent. |
| B5 — Lemarchand, *A Playful Production Process*, first edition (2021) | Make playable work achievable through scoped representations, production decisions, testing and delivery | The [publisher overview](https://mitpress.mit.edu/9780262045513/a-playful-production-process/) connects design to milestones and collaboration; its planned role is delivery depth beyond B1's design backbone | Select. A corpus ending at a convincing prototype would underserve the charter. |
| C6 — Jesse Schell, *The Art of Game Design: A Book of Lenses*, 3rd edition (2019) | Broad design questioning and review of decisions from different viewpoints | The [author's studio description](https://schellgames.com/art-of-game-design) offers a useful diagnostic counterpoint to a connected exercise-led process | Do not select: a strong alternative to B1, but adding both would displace specialist depth. Reconsider as supplementary diagnostic material when specific blind spots appear. |
| C7 — Ernest Adams and Joris Dormans, *Game Mechanics: Advanced Game Design* (2012) | Analyse mechanics, internal economies and emergent behaviour through models and practical exercises | The [publisher contents](https://www.peachpit.com/store/game-mechanics-advanced-game-design-9780321820273) offer a more concentrated mechanics/modelling alternative to B2, including Machinations-based work | Do not select: B2 is the broader initial systems bridge. This is a strong follow-up candidate for economy modelling or procedural-system gaps. |
| C8 — Anders Drachen, Pejman Mirza-Babaei and Lennart E. Nacke, editors, *Games User Research* (2018) | Design studies, assess validity and turn qualitative/quantitative observations into useful findings | The [OUP record and contents](https://academic.oup.com/book/26677) add specialist evaluation depth, including bias, resource constraints and participation by people with disabilities | Do not select for the five: the closest alternative to B5. Keep it as a priority Stage 2 candidate for the explicit research-method gap. |
| C9 — Celia Hodent, *The Gamer's Brain: How Neuroscience and UX Can Impact Video Game Design*, 1st edition (2017) | Examine player cognition, usability and onboarding rather than relying on designer intuition | The [publisher record](https://www.routledge.com/The-Gamers-Brain-How-Neuroscience-and-UX-Can-Impact-Video-Game-Design/Hodent/p/book/9781498775502) and [author's UX material](https://celiahodent.com/video-game-ux-psychology/) offer a cognitive/UX lens distinct from spatial craft or production | Do not select: valuable specialist human-factors follow-up, but substituting it now would reduce either production or spatial depth. |
| C10 — Robert Nystrom, *Game Programming Patterns*, author-hosted online book | Organise game code so changes remain manageable | The [author's introduction](https://github.com/munificent/game-programming-patterns/blob/master/book/introduction.markdown) frames the problem through programming experience; this offers implementation depth beyond design practice | Do not select: much of the contribution sits on the general engineering side of the charter. Free access alone does not justify spending a foundational place. |

### 4.2 Credibility, limitations, durability and access

Professional experience and specialist publication make these plausible candidates; neither is proof that every claim is correct. “Secondary material only” is the canonical **access label** for descriptions or discussion about a book. It includes author/publisher metadata here and does not mean that those bibliographic sources are unreliable or that they are third-party commentary.

| Candidate | Credibility and limitations to carry forward | Durability and currency assessment | Access actually established in this stage |
|---|---|---|---|
| B1 | An established design-practice text with an author-maintained fifth-edition site. Its pedagogical framing must be tested against professional constraints and atypical games. | Design/iteration principles are plausible durable material. A 2024 edition does not establish current engine or platform behaviour. | **secondary material only** — author overview, edition announcement and contents; no chapter body obtained. Section 6 records the missing reading. |
| B2 | A practitioner-authored Pearson text; the sample includes author background and a substantive systems chapter. One systems vocabulary must not become the only valid model. | Systems reasoning can outlast tooling. Examples and implementation assumptions from 2017/2018 need checking. | **relevant excerpts available** — official sample contains chapter 5; selected passages were inspected. Balance and loop chapters remain unexamined. |
| B3 | Swink's first-person practitioner article demonstrates an articulated interaction perspective. It cannot validate all claims in the book or universal player preferences. | Interaction reasoning is a durable candidate. Old devices, game examples and real-time assumptions need qualification. | **secondary material only** for the book — indexed publisher metadata/description; the separately read article is not book text. |
| B4 | A specialist CRC text with an identifiable second-edition imprint and an architectural perspective. Spatial explanations and historical analogies need gameplay evidence. | Layout and representation methods are plausible durable material. Named tools and pipelines require current verification. | **relevant excerpts available** — preview front matter, introduction and beginning of chapter 1; later practical chapters are absent. |
| B5 | A practitioner production text published by MIT Press. Large-production experience must be adapted to bounded solo/small-team work; its testing advice is not automatically research science. | Scope, iteration and commitment reasoning are durable candidates. Team structures, certification and release details are context dependent. | **secondary material only** — publisher/author descriptions, contents PDF and an interview; no book chapter body obtained. |
| C6 | A practitioner/educator's broad lens collection, described on the author's studio site. Many perspectives can aid diagnosis but do not settle which decision matters most. | Broad design questions may endure; specific products and examples need contextual review. The assessed edition is the third, not a claim about the latest edition. | **secondary material only** — studio description and indexed publisher edition information; no book chapters examined. |
| C7 | Specialist practitioner authors and a practical publisher text. A particular modelling notation can clarify some systems while obscuring experiences it does not represent. | Mechanics reasoning may endure; the 2012 tool-specific exercises require version and feasibility checks. | **secondary material only** — publisher description and contents. Sample links were advertised but their chapter bodies were not examined. |
| C8 | An edited OUP research/practice collection supplies multiple specialist contributions. Chapters may differ in method and strength; an edited volume is not one validated universal procedure. | Study-design reasoning is a durable candidate. Instrumentation, platform examples and data practices need current checks. | **secondary material only** — OUP abstract, bibliographic record and chapter listing; chapter bodies not examined. |
| C9 | An author with psychology and game UX experience provides a distinct human-factors perspective. Specific cognitive or causal claims require primary empirical scrutiny. | Human-factors questions remain relevant; neither the 2017 edition nor a neuroscience label establishes current consensus. | **secondary material only** — indexed publisher material and author UX discussion; no book body. Direct publisher access was restricted. |
| C10 | The author exposes the book's source and describes industry programming experience. Patterns are choices with costs, not a mandated architecture. | Architectural trade-offs can remain useful, but the [repository README](https://github.com/munificent/game-programming-patterns/blob/master/README.md) says active maintenance has stopped. Old build instructions are not current guidance. | **full text available** through the author-hosted book source; repository structure, README and the first 100 lines of the introduction were inspected. Availability is not a full-book reading claim. |

### 4.3 Why this combination

B1 plus B2 provides breadth and systems depth. Replacing B2 with C7 would favour concentrated mechanics/economy modelling; retain B2 initially because the Seed also needs connections between systems, player experience and making the game real. Stage 1B must test whether that expected advantage survives examination.

B3 and B4 make two easily underdeveloped responsibilities explicit: how the player-controlled interaction feels and how play works in space. Replacing either with another general design text would increase broad discussion while weakening a concrete integration responsibility. These specialisms must not narrow the whole repository to real-time 3D avatar games.

B5 protects the path from experiments to completed playable work. **The strongest cost of this choice is excluding C8 from the foundational five.** Choosing C8 instead would improve expected study-method depth but reduce dedicated production and delivery depth. Retain B5 because the charter owns delivery and repair, then require independent investigation of research validity and inclusive participation in Stage 2. Mentioning playtesting in B1/B5 is not equivalent to covering that gap.

B1 and B5 share a playcentric/USC-associated perspective. Their overlap is useful only if extraction reveals distinct decisions: B1 is expected to anchor what to design and learn; B5 is expected to deepen how to scope, integrate and finish the work. Repetition from this shared lineage is not independent corroboration. C6, C8 and C9 remain contrasting candidates for later challenge research.

No authority scores, overlap percentages or measured optimisation result were assigned. A later corpus revision may be justified by direct examination or access failure, but must preserve the decision history and identify affected research.

## 5. Selected five-book corpus

Edition identities are pinned for subsequent reading; they are not assertions that each is the newest available edition. ISBNs below identify a print edition, while linked previews may identify an electronic format of the same work. Different formats or editions do not create additional corpus members.

| ID | Title and author | Selected edition / publication year | Origin and bibliographic location | Intended contribution |
|---|---|---|---|---|
| B1 | *Game Design Workshop: A Playcentric Approach to Creating Innovative Games* — Tracy Fullerton | 5th edition, 2024 | **Selected**; ISBN `9781032607009`; [publisher](https://www.routledge.com/Game-Design-Workshop-A-Playcentric-Approach-to-Creating-Innovative-Games/Fullerton/p/book/9781032607009), [author's edition announcement](https://www.tracyfullerton.com/news/2024/4/5/fifth-edition-of-game-design-workshop-launches) | Connected design and iteration practice: intent, rules, prototypes, player observation and revision; a baseline for reconciling the specialist sources. |
| B2 | *Advanced Game Design: A Systems Approach* — Michael Sellers | 1st edition; published 30 October 2017, copyright 2018 | **Selected**; ISBN `9780134667607`; [Pearson record](https://www.pearson.com/en-us/subject-catalog/p/advanced-game-design-a-systems-approach/P200000009594/9780134669458) | Systems, interacting mechanics, loops, emergence and balance, with links to player experience and production decisions. |
| B3 | *Game Feel: A Game Designer's Guide to Virtual Sensation* — Steve Swink | 1st edition; first published 2008, copyright 2009 | **Selected**; ISBN `9780123743282`; [publisher](https://www.routledge.com/Game-Feel-A-Game-Designers-Guide-to-Virtual-Sensation/Swink/p/book/9780123743282) | Control/response relationships, feedback and spatial context as subjects for prototyping, tuning and human evaluation. |
| B4 | *An Architectural Approach to Level Design* — Christopher W. Totten | 2nd edition, 2019 | **Selected**; ISBN `9780815361367`; [publisher](https://www.routledge.com/Architectural-Approach-to-Level-Design-Second-edition/Totten/p/book/9780815361367), [preview imprint](https://api.pageplace.de/preview/DT0400.9781351116299_A37413136/preview-9781351116299_A37413136.pdf) | Spatial gameplay, cheap level representations, traversal/readability and the transition toward integrated playable levels. |
| B5 | *A Playful Production Process: For Game Designers (and Everyone)* — Richard Lemarchand | First edition, 2021; published 12 October 2021 | **Selected**; ISBN `9780262045513`; [MIT Press record](https://mitpress.mit.edu/9780262045513/a-playful-production-process/) | Prototype and production scope, commitment points, integrated playables, testing, bug/fix work and delivery; adapt methods to the charter's scale. |

The 2017/2018 and 2008/2009 pairs distinguish publication from copyright years, not different books. B3's first-publication year was checked against indexed Taylor & Francis bibliographic metadata; its copyright year and ISBN against indexed publisher metadata. Restricted product-page access is recorded below rather than presented as chapter access.

## 6. Source-access register and reading limits

Access was checked on **12 September 2026**. All locations here are public bibliographic or preview URLs. No private source identifier is needed. Source books, substantial extracts and private access data are not part of this repository change.

| Book | Access status | Material actually examined and source location | Reading limitation and outstanding access |
|---|---|---|---|
| B1 | **secondary material only** | Author overview, [fifth-edition contents and changes](https://www.gamedesignworkshop.com/whats-new), edition announcement and indexed publisher metadata | No chapter body was obtained. The author's purchase/sample route led to a restricted publisher page. Obtain lawful full text or contextually sufficient excerpts for the assigned design/prototype/playtest contribution; a sample link alone is not access. |
| B2 | **relevant excerpts available** | [Official Pearson sample PDF](https://ptgmedia.pearsoncmg.com/images/9780134667607/samplepages/9780134667607_Sample.pdf), 54 PDF pages: bibliographic/front matter, contents and author background inspected; sampled chapter 5 passages around printed pp. 175-184 | The sample includes chapter 5, printed pp. 171-185, plus front matter and an index. It is not 54 continuous pages of book argument. No complete chapter extraction was performed. It does not provide the later loop and balance chapters needed for the assigned contribution. |
| B3 | **secondary material only** | Indexed publisher description/edition metadata and the separate [2007 author article](https://www.gamedeveloper.com/design/game-feel-the-secret-ingredient) identified in Section 2 | No book chapters or reliable book-body preview were obtained; direct publisher/author-site requests were restricted or failed. Obtain book text with definitions, worked interaction examples and surrounding qualifications. The article cannot stand in for this corpus member. |
| B4 | **relevant excerpts available** | [Distributor-hosted publisher preview](https://api.pageplace.de/preview/DT0400.9781351116299_A37413136/preview-9781351116299_A37413136.pdf), 63 PDF pages: imprint/contents and selected introductory passages, including material around printed pp. xxxii-xli, inspected | Available material includes front matter, the introduction and chapter 1 only through printed p. 16. It does not contain the later practical chapters named in the intended reading scope. Neither the whole introduction nor chapter 1 was exhaustively read. |
| B5 | **secondary material only** | [MIT Press overview](https://mitpress.mit.edu/9780262045513/a-playful-production-process/), [author site](https://www.playfulproductionprocess.com/), eight-page [contents PDF](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/13082/toc_final.pdf?dl=1), and the Section 2 interview | The PDF is a contents list, not eight pages of production-method exposition. No book chapter body was obtained. Obtain meaningful access to the production, testing and delivery sections before extraction. |

PDF observations above are based on extracted text and printed page labels. They establish bibliographic identity and preview boundaries, not a visual review of every diagram or a full reading. **None of the five currently has sufficient examined material to close its Stage 1B contribution.**

### Intended Stage 1B reading scope

These are targets to investigate after access is obtained, not findings or a mechanical page quota. Record exact examined locations, context and limitations during extraction, and expand the scope when an argument depends on earlier definitions or later qualifications.

| Book | Initial source units to investigate | Questions the examination must resolve |
|---|---|---|
| B1 | Fifth-edition chapters 1-14, prioritising design structure, prototyping and chapters 9-11 on evaluation; chapter names/sequence checked against the author's contents | Which methods connect intended experience to observable play? What evidence changes a design, and what does the text actually support about accessibility and repair? |
| B2 | Definitions and systems/design context in chapters 1-6, loops and balancing in chapters 7-10, with relevant production context from chapters 11-12 | What can be modelled and tested, under what assumptions? How are unintended interactions and balance failures diagnosed without reducing player experience to a model? |
| B3 | Locate book sections addressing input, response, context and feedback, together with definitions and worked examples; exact chapter/page identifiers remain pending book access | Which relationships are actionable and testable? Which claims depend on real-time control, particular hardware, genre or player preferences? |
| B4 | Practical material in chapters 2-8, with necessary framing from the introduction/chapter 1 and later material when the intended level task requires it | How do representations guide playable spatial decisions? What can be checked cheaply, what needs a player, and where does level design hand off to specialist content craft? |
| B5 | Relevant sections within chapters 4-14 for playable representations; 17-29 for planning, commitments, testing and bug work; 31-36 for finishing and review | What makes a production commitment justified? How can work be corrected while retaining accepted behaviour? Which team-scale and release assumptions need adaptation? |

Use authorised publisher, institutional or user-supplied access. No purchase or subscription was made. If the missing material cannot be obtained at Stage 1B, record the exact unresolved contribution and request excerpts/access or propose a documented corpus revision. Do not fill missing arguments from model memory or silently relabel descriptions as extraction.

## 7. Provided / retained / added / substituted decision log

All decisions below are dated **12 September 2026**, under `CORPUS-01`. Decision reference: the user's instruction to perform the next stage after the Stage 1 commit, together with the canonical rule permitting selection into empty places. This authorises stage execution; it is not a claim that the user individually endorsed each book or authorised purchasing it.

| Decision | Book or material | Rationale | Permission / resolution |
|---|---|---|---|
| Provided | None | No titles or book files were supplied | No supplied-source obligation pending |
| Retained from supplied material | None | There was no existing supplied corpus | Not applicable |
| Added | B1 — Fullerton, fifth edition | General design/iteration anchor | Selected into an empty place |
| Added | B2 — Sellers, first edition | Additional systems and balance depth | Selected into an empty place |
| Added | B3 — Swink, first edition | Specialist control and feedback depth | Selected into an empty place |
| Added | B4 — Totten, second edition | Specialist spatial and level-production depth | Selected into an empty place |
| Added | B5 — Lemarchand, first edition | Production commitment, completion and repair depth | Selected into an empty place |
| Substituted / removed / demoted | None | No supplied or established corpus member was changed | No substitution approval needed or pending |
| Compared but not selected | C6-C10 | Portfolio trade-offs in Section 4 | Preserved as alternatives; they are not extra foundational members |

Later supplied material must be registered separately. Any proposed removal, replacement or demotion of a user-provided book requires explicit permission. Any later change to this established corpus must increment the corpus revision, explain expected gain and loss, and identify affected extraction or design work; do not rewrite revision 1 as though the change had always been present.

## 8. Remaining gaps and ownership of follow-up

| Gap | Why selection does not resolve it | Required follow-up and gate |
|---|---|---|
| Direct access and examination of all five contributions | Three books have only material about them; the two previews do not reach the intended breadth | **Stage 1B blocker:** obtain sufficient book text, examine it and produce traceable per-book findings before completing extraction. Selection can close with these needs recorded. |
| Research validity and human judgement | General playtesting coverage does not establish recruitment, bias control, study validity or justified causal claims | Stage 1B must expose the books' actual limits. Stage 2 must investigate specialist research methods, including C8 as a candidate, and separate observed behaviour, interpretation and unresolved experience judgements. |
| Accessibility and inclusive participation | No specialist accessibility book is selected; a heading or general usability method is insufficient | Stage 2 must investigate current practitioner guidance, applicable primary research and participation by players with relevant access needs. Carry concrete inclusive interaction requirements into the first proof and its evaluation. |
| Engine execution, target performance and reproducibility | Durable books cannot prove current engine, editor, input, build or deployment behaviour | Stages 2 and 8 must consult relevant current primary documentation; later execution-path, evaluation and consumer-installation stages must demonstrate results. Keep gameplay acceptance distinct from general engineering mechanisms. |
| Broader forms and platforms | Spatial and real-time examples may dominate; general systems coverage does not establish network, mobile or XR competence | Revisit K1-K9 independently during Stage 2. Add specialist investigation and representative execution before expanding support claims; retain the charter's bounded single-player first proof. |
| Preservation, approvals and cross-discipline repair | Candidate production coverage does not establish this project's consumer-owned decisions, locks or handoff contracts | Stage 1B should look for applicable production principles. Stage 2 and later workflow/artefact design must address reopening decisions, preserving accepted work and game-specific acceptance of adjacent contributions. |
| Independence and counterexamples | Shared educational/practitioner lineage and successful-game examples can repeat assumptions | Stage 1B must record overlaps and tensions. Stage 2 must seek criticism, failure cases and empirical evidence rather than count agreement as validation. |

These gaps do not narrow the charter. In particular, accessibility remains core, and choosing a production book does not remove the need for rigorous human evaluation. Additional books, articles, standards and official documentation may extend the wider bibliography without increasing the foundational corpus beyond five.

## 9. Completion check and next-stage handoff

| Stage 1A requirement | Completion evidence |
|---|---|
| Use the Stage 1 charter as Seed | Section 1 pins the charter and preserves its ownership and scope |
| Bounded reconnaissance and knowledge dimensions | Sections 2-3 record examined sources, stopping rule, required depth and gaps |
| Broader candidate pool and comparative assessment | Section 4 assesses ten books for relevance, added depth, practical use, credibility, contrast, currency and access |
| Exactly five distinct complementary books | Section 5 identifies B1-B5 by title, author, edition/year and ISBN; no edition or format is counted twice |
| Source location, access, actual examination and limitations | Sections 5-6 distinguish metadata, available excerpts, inspected passages and missing reading |
| Supplied-book and substitution decisions resolved | Section 7 records no supplied books, five additions and no substitutions or pending approvals |
| Remaining knowledge and access needs explicit | Sections 6 and 8 assign the unresolved work and the gate it affects |
| Durable standalone stage record | This log contains the selection rationale and is linked from the research-log index |

**Exit decision:** Stage 1A selection is complete at corpus revision 1. It does not establish that the books' methods are correct, that all five have been meaningfully examined, or that any game-development capability is implemented or installable.

The **next stage is Stage 1B**. Read the charter and this corpus/access record, resolve the missing source access, then extract and reconcile all five intended contributions using the canonical fields. Do not mark Stage 1B complete from the previews and descriptions recorded here. Stage 2 follows extraction and must challenge the resulting model as well as investigate the uncovered responsibilities. No engine selection, skill decomposition or production scaffold is created by this stage.

---

**Version:** 1.0 | **Stage:** 1A | **Corpus revision:** 1 | **Updated:** 12 September 2026
