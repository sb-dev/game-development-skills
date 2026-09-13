# Progressive Examples Contract

**Version:** 1.0  
**Selection evidence:** [Stage 13 candidate comparison](../research-logs/2026-09-13-stage-13-progressive-examples.md)  
**State:** Fifteen complete example designs and prompts; no example generation, gameplay, human session, benchmark or installation has run at this stage.

## 1. Curriculum and proof boundary

The primary curriculum is exactly **five levels × three examples = fifteen examples**, selected from thirty candidates. Level describes the production responsibility under test, not code size, artistic finish or a mandatory order for every consumer task. Each trio complements the other two. Pack showcases and independent reuse fixtures remain additional evidence; they do not replace or inflate this count.

| Level / meaning | Primary examples | Combined proof |
|---|---|---|
| 1 — one mechanic | E01 Latch Room; E02 Rebound Lab; E03 Depth Dock | Rule/state and reset; continuous input/contact and basic tuning; actual 3D manipulation and depth information. Each includes feedback, small automated checks and local repair |
| 2 — repeatable loop | E04 Spark Run; E05 Quiet Parcel; E06 Reservoir Shift | Motor/score risk, stealth information/AI and discrete resource incentives. Each includes goal, challenge, reward/failure, retry, pacing/basic balance and actual human playtest |
| 3 — coherent vertical slice | E07 Beacon Walk; E08 Switchyard Tactics; E09 Orbit Courier | Traversal/content, tactical encounter/progression and 3D camera/physics. Each integrates representative content, UI/audio/visual handoffs, workload budget and broader evaluation |
| 4 — scale, systems and repair | E10 Seeded Vault; E11 Canal Works; E12 Twin Signal | Generated progression/placement, interacting simulation/persistence and actual multi-peer authority/recovery, with multiple content units, load evidence and stable-system preservation |
| 5 — full thesis | E13 Signal Orchard; E14 Harbor Accord; E15 Lantern Atlas | Small complete precision game, tactical narrative campaign and coherent 3D world. Together exercise both packs and core-only production, broad cross-domain integration and actual release-candidate validation |

## 2. Complete prompt and output locations

The linked files contain three **standalone, copyable prompts** each. Copy the entire relevant fenced prompt into an installed-skill consumer. No prompt requires another example's artefacts or earlier prompt text. Each requests original content and records any selected ordinary runtime dependencies. These are generation tasks with explicit proof and failure handling, not claims of existing game outputs.

| Examples | Complete prompts | Future output / evidence location |
|---|---|---|
| E01–E03 | [Level 1](../research-logs/stage-13-prompts/level-1.md) | `examples/level-1/<example-id>/` |
| E04–E06 | [Level 2](../research-logs/stage-13-prompts/level-2.md) | `examples/level-2/<example-id>/` |
| E07–E09 | [Level 3](../research-logs/stage-13-prompts/level-3.md) | `examples/level-3/<example-id>/` |
| E10–E12 | [Level 4](../research-logs/stage-13-prompts/level-4.md) | `examples/level-4/<example-id>/` |
| E13–E15 | [Level 5](../research-logs/stage-13-prompts/level-5.md) | `examples/level-5/<example-id>/` |

At the implementation stage each primary example gets its own README containing the **exact generation prompt actually used**, premise, prerequisites/run commands, selected skills/packs and revisions, expected behaviour, generated artefacts, actual execution provenance, evaluation and limitations. Keep the planned prompt and any authorised deviation visible. Preserve actual playable output, source/data/assets, required local test drivers, baseline/fault/repair evidence and status. A link to a prompt without output is not a demonstrated example.

## 3. Required gates at each level

| Level | Gate for each primary example | Additional combined coverage |
|---|---|---|
| 1 | Bounded playable interaction with actual input/state/feedback, stated rule values, one basic tuning comparison, small automated normal/invalid/reset checks and smallest responsible repair | Temporal/physics and discrete semantics plus a genuine 3D depth case; the first core vertical may select one of these |
| 2 | Complete goal/challenge/outcome/retry loop, pacing and basic balance analysis, automated technical checks and an actual question-led human session | Distinct score, information and resource pressures; human actions/accounts separate from scripts and expert inference |
| 3 | Representative composed slice, level/encounter progression, actual delivered/integrated UI/audio/visual content, target/workload budget and broader rule/experience/access/performance review | 2D/3D, physical/tactical control and source/import/runtime fault ownership |
| 4 | Multiple content units, interacting systems/strategies, procedural or systemic content, complex balance questions, representative load and regression-protected repair | Procedural post-placement validity, simulation trajectories/persistence and real two-peer session recovery |
| 5 | Coherent thesis, mechanics/systems/space, integrated content, actual playtesting, balance/performance/access review and identified local release-candidate validation | Both selected packs, a core-only world, all four required content handoff disciplines and a bounded creator revision/evidence review |

Human requirements cannot be satisfied by fabricated participants, LLM roles, bot telemetry or author intuition. Use relevant actual participants with neutral tasks and recorded familiarity/assistance. A small session supports only its situated observations. If required participants or another necessary execution capability are unavailable, the affected example/proof remains blocked with the precise need; do not silently remove that gate. Stage 13 designs these gates and does not require their execution yet.

## 4. Whole-set coverage matrix

This is a coverage map, not a measured support catalogue. Each cell names the relevant planned proof. Hardware and broad platform claims require actual representative evidence.

| Bootstrap dimension | Deliberate examples and limits |
|---|---|
| 2D vs 3D | 2D E01/02/04–08/10–14; actual 3D scene/camera E03/E09/E15. A flat projection pretending to be 3D cannot pass those examples |
| Real-time vs turn-based | Continuous E02/04/05/07/09/13/15; discrete E01/03/06/08/11/14; E10 mixes exploration with discrete resource decisions; E12 multi-peer real-time input with discrete authoritative outcomes |
| Precision vs systemic | Precision/contact E02/07/13; resource/strategy/phase interaction E06/08/10–12/14; information/space E01/03/05/09/15 |
| Authored vs procedural content | Authored rooms/encounters across L1–3 and L5; E10 seeded generation after placement; E11 systemic flow/demand. No procedural-quality guarantee from a seed or assembly check |
| Physics dependence | E02 collision/deflection, E07/13 movement/contact, E09 steering/inertia; E01/06/08/11/14 intentionally rule-based |
| AI dependence | E05 perception/patrol/recovery, E08 opponents, E10 encounters, E11 agents and E14 encounter decisions. E01–03 do not require AI |
| Single-player vs multiplayer | Most are single-player; E12 actually uses two browser clients and one authoritative local server. Production service operation, matchmaking and internet-scale fairness are outside this bounded proof |
| Short-session vs progression-heavy | L1/2 bounded attempts/loops; E08/10/11/13–15 multi-content progression with declared retained state |
| Level-based vs world-based | E07/08/10/13/14 explicit sequences; E11 connected systemic scenarios; E15 three connected zones with persistent world-state relationships |
| Platform / input differences | All can use ordinary browser delivery; keyboard E01/04/05/07/12/13, pointer plus keyboard alternatives E01/03/06/08/11/14/15, multi-client E12 and 3D camera E09/15. Browser touch events may be inspected where relevant but do not establish real mobile, gamepad, console or XR support; those remain explicit gaps |
| Core skills | game-development and independent game-evaluate across the set; game-extension-pack-creator bounded profile/evidence revision in E14. No sibling family is an undeclared runtime prerequisite |
| Commands | Complete operation mapping in section 5; game-native invocation without a new command executable |
| Extension Packs | E08/E14 tactical-turn-based; E13 precision-platformer; other examples core-only, including E07 to preserve a substantive no-pack traversal baseline. Both P5 showcases/reuse cases remain additional P6/P7 work |
| Failure modes | E01 stale reset; E02 contact double effect; E03 transform/depth mismatch; E04 stale score session; E05 invalid target/knowledge; E06 coupled cost loop; E07 content collision; E08 phase/preview; E09 camera/cue occlusion; E10 post-placement soft lock; E11 save/collection; E12 duplicate reward/reconnect; E13 route regression; E14 narrative/phase/pack conflict; E15 linked-world restore/release dependency |
| Repair behaviour | Each names a local fault and accepted stable decisions; retain baseline, faulty and repaired output and rerun affected cases. Do not regenerate unrelated content or weaken expectations |
| Performance risks | Timing/contact E02/07/13; perception E05; rendering/camera E03/09/15; generated/state/agent load E10/11; message/backlog E12; cumulative content/assets E13–15 |
| Accessibility challenges | Complete keyboard paths, redundant cues and focus throughout; precision/input demand E02/07/13, hidden-information clarity E05/08, depth/camera E03/09/15, timers/pacing E04/06, dense data E11 and two-player state E12 |
| Cross-domain handoffs | E07–09 UI/environment/animation/audio, E13 environment/visual/audio, E14 narrative/animation/audio/UI and E15 environment/3D/narrative/audio. Original source deliveries and integration records must exist; a list of desired assets is not a handoff |
| Benchmarkability | Identified oracle/setup, actual input/state, deterministic small cases where adequate, seeds/policies/network schedules where relevant, human/target claims separated |
| Showcase clarity | One named production question per L1 example; one complete loop per L2; representative integrated slice at L3; identifiable systemic fault at L4; bounded finished thesis at L5. Each README explains the observed benefit and remaining limits |

The entire set covers all twenty requested dimensions without promising every platform or genre. Breadth is deliberate and bounded: first proof remains local single-player; 3D and multi-peer paths earn their own execution evidence later. Level numbers do not certify maturity. Additional mobile/gamepad/XR/console examples require suitable tooling and actual device evidence before expansion.

## 5. Commands and source-derived case coverage

| Named operation | Principal examples / observable work |
|---|---|
| define-game-thesis | E04–06 loop question; E13–15 complete thesis and accepted scope |
| design-mechanic | E01–03 rules/input/state; E08 discrete actions |
| model-system | E06 costs/feedback; E10 progression/placement; E11 flow; E12 authority; E14 campaign dependencies |
| build-playable-proof | Every example; initial core vertical selected later from L1 |
| integrate-content | E07–09 and E13–15 actual versioned source deliveries and runtime binding |
| repair-gameplay | Every example's bounded fault, preservation and actual reruns |
| prepare-playable-build | E07–09 representative candidate; E13–15 identified local release candidates |
| validate-gameplay | All rule/phase/reset/interaction cases, especially E01/06/08/10–12 |
| evaluate-player-experience | Actual sessions E04–06 and question-led L3/L5 playtesting; contact/depth/feedback technical observations kept separate |
| evaluate-balance | E04–06 risk/pacing, E08/10–12 strategies and E13–15 appropriate experience/system questions |
| evaluate-accessibility | Whole task paths in every example; critical motor/colour/focus/depth/data barriers remain explicit |
| evaluate-performance | Target/workload measurements E07–15; timing and representation checks where needed in L1/2 |
| diagnose-gameplay | Every named fault; independent evaluation recommendations before authorised source changes |
| author-extension-pack | E14: review actual tactical-profile applicability and evidence, make only a justified bounded revision with affected cases; a no-change finding is valid, invented authoring work is not |

Core candidate cases remain hypotheses until selected and executed by the benchmark stage: BC01→E04/06, BC02→E01, BC03/05→E02, BC04→E06/11, BC06→E07, BC07/09→E03/05/09, BC08→E04/11, BC10→E07–09 scope review, BC11→E13, BC12→E13/15, BC13→E10, BC14→E05, BC15→E11/15, BC16→E12. The mapping supplies a concrete production context without converting every example into a full benchmark suite or claiming the fixture has run.

## 6. Execution and preservation protocol

At Stage 20, run each complete prompt with recorded installed skill/pack revisions, model/tool/runtime versions where relevant, project/build identity, actual commands and allowed resources. Use ordinary game-specific code and suitable existing libraries; do not create a shared engine to make the examples uniform. Games with 3D or transport needs select declared normal dependencies and validate those paths directly. No accounts, paid services, public hosting or platform certification are required by this curriculum.

Choose and record project-specific rule values and representative workload/measurement limits before accepting the baseline. Tuning comparisons declare permitted variation; post-acceptance repairs preserve fixed rules and stable content. Every example retains a reproducible negative or injected-fault case and the expected result, plus baseline/fault/repair versions. Where an evaluator intentionally supplies a faulty fixture, disclose the injection in evidence and avoid pretending the author was blind to a fault they themselves inserted.

Use real input for input claims and authoritative game state for rule claims. Label controlled setup, model-only simulation, synthetic network delivery conditions and human evidence separately. Observe player-facing content at the appropriate modality. A generated audio file or waveform alone cannot establish audible mix quality; a screenshot cannot establish timing, depth control or performance. Local release-candidate validation means build/package and fresh local run with identified content/dependencies and quality gates; it does not authorise external publication.

Stage 14 specifies evaluation cases and thresholds without weakening these gates. Stage 15 specification 04 consolidates this curriculum and links all prompts. Stage 18 may scaffold output directories, Stage 19 proves one installed core vertical, and Stage 20 must produce and inspect all fifteen actual examples plus the separately required pack evidence. Unavailable required proof is a blocker at its owning execution gate, not a reason to count a plan as an example.
