# Stage 2 - Source Evidence and Reading Limits

**Date:** 13 September 2026  
**Version:** 1.0  
**Status:** Supporting evidence for the completed [Stage 2 domain research](2026-09-13-stage-02-professional-practice-and-capability-model.md)  
**Access date for every web source:** 13 September 2026

## Reading and interpretation

This register identifies the additional primary material actually examined and the limits of its contribution. It complements the five supplied books and their [35 extracted findings](2026-09-13-stage-01b-book-findings.md); it does not change corpus revision 2 (`CORPUS-02`). The two *Game AI Pro 3* chapters and the living *Level Design Book* are supplementary sources.

Research followed two tracks: challenge material book claims, and investigate responsibilities missing from the provisional model. Searches located original studies, first-person production accounts and official documentation; substantive body passages, rather than search summaries or contents pages, support the findings below. Reading was selective. Linked demonstrations, source code and products were not executed, and videos were not evaluated. Source PDFs and lengthy extracts are not included.

Studies can support findings within their observed conditions. Production accounts describe situated practice. Official documentation establishes documented behaviour or guidance for its stated version, not independently measured game quality. Dates on historical accounts are retained; they are not current product recommendations. Godot's `stable` URLs are moving aliases, so execution stages must resolve an exact version. Unity references explicitly target 6.0 (6000.0). The Unreal page displayed 5.8 when accessed; no claim that this is the project's selected or installed engine follows.

## Primary sources

### R01 — RITE: rapid correction and verification

Medlock, Wixon, Terrano, Romero and Fulton, **2002**, [*Using the RITE method to improve products: a definition and a case study*](https://www.jpattonassociates.com/wp-content/uploads/2015/04/rite_method.pdf). Primary paper hosted in Jeff Patton's archive. Examined PDF pp. 1–3: definition, assumptions, issue categories and case setup.

The method needs decision-makers and capacity to change the product. Unclear causes require further investigation. It specifies no fixed participant count for verifying a correction. This is the underlying work cited by Fullerton, not independent corroboration of F5; its game case does not establish universal sample sufficiency or commercial causation.

### R02 — Variability hidden by a five-user rule

Laura Faulkner, **2003**, [*Beyond the five-user assumption: Benefits of increased sample sizes in usability testing*](https://link.springer.com/content/pdf/10.3758/BF03195514.pdf), *Behavior Research Methods, Instruments, & Computers* 35, 379–383. Examined method, results and discussion, especially print pp. 380–381.

Resampling a 60-person timesheet-task study produced five-person groups finding 55–99% of the observed problems. That challenges universal small-sample sufficiency, but the task was not a game; the observed problem set was not every possible defect. It supplies neither a universal replacement quota nor a measure of game quality.

### R03 — Tutorials and measured outcomes

Erik Andersen and colleagues, **CHI 2012**, [*The Impact of Tutorials on Games of Varying Complexity*](https://grail.cs.washington.edu/projects/game-abtesting/chi2012/chi2012.pdf). Examined experimental procedure and metrics on PDF p. 4, and results, limitations and discussion on pp. 7–9.

Randomised tutorial conditions across three games and over 45,000 players did not produce a uniform benefit. Complexity was not isolated from differences such as download barriers between games. Duration, progress and return were proxies; the authors could not directly observe players' thoughts. Historical recruitment/data practices are not adopted as present-day requirements.

### R04 — Prototype questions versus production proof

Rami Ismail, **26 September 2022**, [*Prototypes & Vertical Slice*](https://ltpf.ramiismail.com/prototypes-and-vertical-slice/). Examined the complete article text.

The account separates investigating a game idea from investigating repeatable production, including making another unit after the slice to expose production cost. This is practitioner advice, not a controlled comparison of pipelines. Its categorical prototype-code disposal and forecasting advice are not adopted as universal rules. A different producer's framing challenges a mandatory sequence or finish level without proving one ideal workflow.

### R05 — Live balance metrics and their blind spots

Summoner's Rift Team, **30 June 2020**, [*/dev: Balance Framework Update*](https://www.leagueoflegends.com/en-us/news/dev/dev-balance-framework-update/). Examined the article's audience segmentation, framework adjustments, power-creep discussion and limitations.

Metrics identified outliers but did not determine the right design change or capture all game-health concerns. Missing professional play affected the buff/nerf balance. This is a historical League of Legends production account: its cohorts, thresholds and patch practices are not imported into other games or asserted to be Riot's current policy.

### R06 — Combat clarity and visual noise

Riot Games / bananaband1t, **12 March 2021**, [*Clarity in League*](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/). Examined the definitions, information hierarchy, silhouettes, hitbox/effect alignment and noise discussion.

The account explains why stronger or more numerous effects can obscure actionable information. It supports examining a cue relative to competing cues and gameplay consequences. Competitive camera, roster and art constraints limit transfer. It shares an organisation with R05; these are distinct production concerns, not independent experimental replications.

### R07 — Simulation timing and overload

Glenn Fiedler, **10 June 2004**, [*Fix Your Timestep!*](https://gafferongames.com/post/fix_your_timestep/). Examined fixed, variable and semi-fixed updates, overload/catch-up and rendering separation.

The engineering examples connect timestep variation with simulation changes and describe catch-up work exceeding available time. They motivate explicit time assumptions and overload tests, not a universal tick rate, solver or determinism guarantee. This is a durable technical argument in historical code context, not a benchmark of a current engine.

### R08 — Blockout iteration in actual play

*The Level Design Book* contributors, **living text**, [*Blockout*](https://book.leveldesignbook.com/process/blockout). Examined definition, construction methods, gameplay-metric steps, playtesting and common problems.

The chapter distinguishes editing or flying through geometry from playing with actual movement and collision. It argues for cheap changes while spatial hypotheses remain uncertain. Its mainly authored 3D examples do not establish universal spatial rules; unnamed studio anecdotes and rhetorical percentages are not measured evidence. The shared level-design tradition limits independence from Totten.

### R09 — Accessibility guidance: scope and authority

Microsoft, [*Xbox Accessibility Guidelines*](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines), **V3.2 published 8 June 2023; page updated 14 August 2026**. Examined introduction, development/feedback process, scoping guidance and guideline index.

The guidance draws on industry and the Gaming & Disability Community and expressly is not a compliance or legal certification checklist. Only selected guidelines below were examined in depth; viewing the index is not an audit of every guideline. It supplies a specialist basis for access work, not proof that a particular game serves every player.

### R10 — Accessible input and configuration

Microsoft, [*Xbox Accessibility Guideline 107: Input*](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107), **page updated 4 March 2026**. Examined remapping, alternative interactions, simultaneous/repeated/held inputs, keyboard operation and pointer cancellation/activation provisions.

Input requirements extend to configuration and other critical tasks. The pointer-up guidance has essential down-event exceptions, so it does not justify delaying every gameplay action. Apply relevant provisions to declared tasks and devices; neither device-specific dimensions nor this page alone establish universal access or response-time thresholds.

### R11 — Redundant information channels

Microsoft, [*Xbox Accessibility Guideline 103: Additional channels for visual and audio cues*](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103), **current page at access**. Examined overview and text, shape, colour and audio-channel examples.

Critical information needs usable alternatives when a sensory channel is unavailable; colour alone is insufficient. This is task-oriented prescriptive guidance. Adding another signal does not by itself establish that a player can notice, understand and act on it under the game's actual conditions.

### R12 — Gameplay AI decision and execution responsibilities

Sebastian Hanlon and Cody Watts, **2017**, [*Behavior Decision System: Dragon Age Inquisition's Utility Scoring Architecture*](https://www.gameaipro.com/GameAIPro3/GameAIPro3_Chapter31_Behavior_Decision_System_Dragon_Age_Inquisition%E2%80%99s_Utility_Scoring_Architecture.pdf), *Game AI Pro 3*, chapter 31. Examined sections 31.1–31.7, print pp. 371–378.

The shipped-game account distinguishes legal choices, contextual scoring/targets, preparation and execution; retained decision data aids debugging. It discusses invalidated targets, committed ability execution and fallback movement. Finite, quantifiable choices are explicit assumptions. One ability serving attack and retreat also counters universal single-purpose gameplay-component rules. Utility scoring remains one architecture, not the domain definition.

### R13 — Static checking of authored content

Ian Horswill, Robert Zubek and Matthew Viglione, **2017**, [*Building Custom Static Checkers Using Declarative Programming*](https://www.gameaipro.com/GameAIPro3/GameAIPro3_Chapter42_Building_Custom_Static_Checkers_Using_Declarative_Programming.pdf), *Game AI Pro 3*, chapter 42. Examined introduction, sections 42.3–42.4 and the start of 42.5; print pp. 487–488 and 492–495.

MKULTRA and Project Highrise examples address content references and constraints that ordinary compilation misses. Diagnostics should identify offending data. These are reported applications, not measured universal savings; local assumptions such as required components must be declared. Prolog and the chapter's sample implementation are not selected dependencies.

### R14 — Representative performance measurement

Unity, **6.0 (6000.0) Manual**, [*Collect performance data introduction*](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-collect-data-introduction.html). Examined target-platform, Play mode and Editor profiling sections.

Editor activity affects measurements. The documented workflow uses target-device profiling to identify and validate problems while permitting quicker editor investigation between builds. This establishes the measurement-context distinction for this version. It supplies no project frame budget, hardware coverage claim or evidence that an optimisation was performed.

### R15 — Saved-state reconstruction

Godot Engine, **stable documentation at access**, [*Saving games*](https://docs.godotengine.org/en/stable/tutorials/io/saving_games.html). Examined load/reconstruction example, “Some notes” and JSON limitations.

Restoration involves object creation order and relationships, not merely writing values. The tutorial describes nesting and identifier complications. It does not supply a complete migration, interrupted-write or conflict-recovery design. Those are explicit further responsibilities in the domain model, not capabilities proved by running this example.

### R16 — Automated tests and state isolation

Epic Games, **Unreal Engine documentation, displayed version 5.8**, [*Automation Test Framework*](https://dev.epicgames.com/documentation/en-us/unreal-engine/automation-test-framework-in-unreal-engine). Examined overview, test categories and test-design guidance.

The framework distinguishes several test scopes and advises against reliance on execution order or pre-existing editor/game state, with cleanup after tests. These are applicable automation principles illustrated by one engine. The framework's own smoke-test timing guidance is not a universal project gate; passing automation does not establish enjoyment.

### R17 — Distribution and tester access

Valve, **Steamworks documentation at access**, [*Testing On Steam*](https://partner.steamgames.com/doc/store/testing). Examined developer packages/depots, external testing and update branches.

Content availability depends on package entitlements as well as uploaded files. Playtest applications and alternate build branches provide distinct testing paths. This adds distribution/account conditions to delivery evidence. The page is not a complete release-certification procedure, and no Steam configuration, tester invitation or publication was performed.

### R18 — Input-to-display measurement boundary

NVIDIA, **October 2020 guide**, [*How To Reduce Lag — A Guide To Better System Latency*](https://www.nvidia.com/en-us/geforce/guides/gfecnt/202010/system-latency-optimization-guide/). Examined system-latency definition and peripheral, PC and display components.

The useful distinction is end-to-end input-to-pixel delay versus one component such as rendering. Vendor hardware, optimisation advice and product claims are outside this finding. This historical commercial guide neither resolves perceptual thresholds nor supplies current purchasing or configuration recommendations.

### R19 — Navigation, avoidance and movement integration

Godot Engine, **stable documentation at access**, [*Using NavigationAgents*](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_using_navigationagents.html). Examined path following, arrival/update guidance and avoidance behaviour/limitations.

Path queries do not move the actor; avoidance is separate from navigation geometry and physics. The documentation describes jitter and avoidance failure conditions. It supports diagnosing the responsible layer instead of treating every stuck actor as a decision-tree problem. It is not a general collision-avoidance guarantee or a tested implementation here.

### R20 — Network determinism as a conditional requirement

Glenn Fiedler, **29 November 2014**, [*Deterministic Lockstep*](https://gafferongames.com/post/deterministic_lockstep/). Examined determinism and networking-input sections.

Lockstep requires identical results from matching initial conditions and inputs; apparently small numeric differences can diverge, and platform/compiler differences matter. Buffering inputs introduces a timing trade-off. These requirements apply to this synchronisation approach, not every networked game. R07 and R20 share an author and are engineering explanations, not independent empirical studies.

### R21 — Explicit build and run prerequisites

Godot Engine, **stable documentation at access**, [*Command line tutorial*](https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html). Examined running the game and exporting sections, including project paths, export presets and templates.

Successful execution depends on declared project/build prerequisites. A headless export can establish a packaging step, but cannot establish visual or interactive correctness. These are concrete execution responsibilities; no Godot implementation path, command contract or installation procedure is selected in this stage.

### R22 — Persistent state across accounts and devices

Valve, **Steamworks documentation at access**, [*Steam Cloud*](https://partner.steamgames.com/doc/features/cloud). Examined overview, best practices, save paths, cross-platform saves and initial setup.

Synchronisation can be disabled; account-specific paths and platform rules affect which files travel. Machine-specific settings should be distinguished from portable progress. File replication alone does not validate gameplay state or settle an application's recovery semantics. Corruption, migration and conflicting-progress tests remain project design proposals requiring further implementation research.

### R23 — Authority, messages and session lifecycle

Godot Engine, **stable documentation at access**, [*High-level multiplayer*](https://docs.godotengine.org/en/stable/tutorials/networking/high_level_multiplayer.html). Examined managing connections, RPCs, transfer modes/channels and lobby introduction.

The documented distinctions include call authority, delivery/ordering behaviour and connection failure/disconnection. They establish additional responsibilities beyond a local gameplay loop. The introductory protocol generalisations are not adopted as universal networking laws; its references to Fiedler also prevent treating the whole page as independent corroboration of R20. The lobby code was not executed.

### R24 — Source assets, imports and retained customisation

Godot Engine, **stable documentation at access**, [*Import configuration*](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/import_configuration.html). Examined import workflows, animation options, post-import scripts and scene inheritance.

Import settings can change animation content and behaviour; source changes trigger reimport. Separate customisation mechanisms exist with specific inheritance limits. This grounds a handoff that records both source and import configuration and rechecks resulting play. It does not demonstrate that every asset pipeline, animation rig or reimport survives unchanged.

## Dependence, omissions and use by later stages

The register contains **24 additional source records**, not 24 independent validations. R01 revisits F5's upstream evidence. R09–R11 are one guidance family; R05–R06 one studio; R12–R13 one edited volume with different case contributors; R07/R20 one author; the engine and platform documents share their respective maintainers. R03 supplies a game experiment with explicit limits; R02 supplies a contrasting non-game sampling study. No authority count is used as a confidence score.

Broader evidence remains limited for real-world learning transfer, genre-wide spatial psychology, perceptual latency thresholds, long-running economies, comprehensive disability coverage, console/XR execution and save migration. These omissions are bounded in the main log's gap register. Unavailable pages, source indexes without substantive text and unexamined secondary summaries are excluded from the evidence base.

Use the main log for accepted responsibilities and dispositions. Use this companion to recover primary locations, reading scope and limits before carrying a claim into a later design or execution stage.
