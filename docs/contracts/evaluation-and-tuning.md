# Playtesting, Evidence, Tuning and Balance

**Version:** 1.0  
**Defined by:** [Stage 7 research and verification](../research-logs/2026-09-13-stage-07-playtesting-telemetry-tuning-and-balance.md)  
**Inputs:** [Thesis](game-thesis.md), [behaviour/composition](gameplay-behaviour.md), [adequate proof and commitment](prototype-and-commitment.md), and [content/handoffs](content-and-handoffs.md).

## 1. Start with the claim

Separate three judgements. **Mechanical correctness** asks whether specified rules, state, interactions and constraints hold in the represented cases. **Balance evidence** concerns incentives, viable choices, advantage, challenge and progression under declared strategies and conditions. **Subjective player experience** concerns what relevant people perceive, understand, value and feel. A game can satisfy one judgement while leaving the others unresolved.

Automated execution supplies mechanical evidence; telemetry records observed behaviour and can extend its coverage; human play supplies experiential evidence. These sources overlap, but one must not silently replace another. A human may expose a rule defect; a trace may support an account of frustration. Neither makes the remaining evidence unnecessary for a different claim. Large-scale telemetry requires actual scale and sampling information; the word telemetry does not establish either.

Choose a method because its observations could change a named decision. State the contrary result, relevant cases/players and conditions before collecting evidence. Use the smallest adequate proof under the existing contract. There is no universal participant quota, win-rate target, frame budget or aggregate quality score.

## 2. Nine evidence sources

| Source | What it can establish within scope | What it cannot establish alone | Required context and retained evidence |
|---|---|---|---|
| Scripted automated tests | Expected versus actual transitions, invariants, references, interactions or runtime actions exercised by assertions | Unchecked paths, unspecified intent, viable human strategies or enjoyment; passing a checker does not validate its oracle | Build/data, setup and isolation, actions, expected results, actual assertions, coverage and cleanup/reset; distinguish model from actual runtime |
| Headless simulation | Outcomes and sensitivity under represented rules, strategies, distributions and horizons | Rendering/input coupling it omits, model-to-runtime equivalence, human skill or experience | Model revision, assumptions/omissions, strategy definitions, seeds/configuration, termination and outcome distributions; validate represented rules independently |
| Bot / agent playtests | Actions, reachability and failures found by identified policies through their available observation/action interface | Human discovery, learning, perception, strategic coverage or fairness; a privileged bot may bypass the actual challenge | Policy/model/version, knowledge privileges, action limits, runtime interface, seeds/budget, traces, failed/unfinished runs and unseen strategies |
| Telemetry | Recorded events and outcome patterns among the observed sessions, with scale when actually measured | Intent, thought, enjoyment, cause, missing/offline populations or events the logger failed to capture | Event definitions, version/cohort, eligibility and denominator, session/retry boundaries, timestamps/order, duplication/drop rules and collection integrity checks |
| Replay analysis | Reconstructable sequences, timing and context visible in the recording or supported state replay; candidate failure relationships | Hidden intent or missing state; perfect reproduction across changed runtimes, nondeterminism or incomplete inputs | Replay type, build/configuration, starting state and relevant inputs/seeds, viewpoint/signals present, divergence checks and annotated failure interval |
| Expert review | Reasoned design, usability, access or implementation findings based on the reviewer's expertise and inspected scope | Representative first-use behaviour, actual player prevalence, target performance or universal preference | Reviewer role/familiarity, inspected material, criteria, rationale, contrary possibilities and checks proposed for uncertain findings |
| Human usability / comprehension playtest | What selected participants attempt, understand and accomplish under the observed tasks and assistance conditions | Population-wide success, later mastery, unaided success after coaching, or enjoyment inferred from completion | Relevant knowledge/access/input conditions, task/script, exposure history, interventions, direct observations and separate interpretations |
| Human experiential playtest | Situated participant accounts and observations about challenge, agency, fairness, sensation or satisfaction | That all players share the response, a survey number is objective quality, or a local session proves retention or external effects | Experience question, relevant participants/context, play exposure, observation/account method, assistance and method effects, variation and limits |
| Platform profiling | Measured workload, timing, memory or other declared quantities on the identified build/device under the capture conditions | Unmeasured hardware/workloads, full input-to-display delay from one component, player satisfaction or release readiness alone | Target/build and settings, workload, measurement endpoints/tool overhead, samples and problematic intervals, comparisons and omitted conditions |

Name the actual evidence source when tools overlap. A bot's event log is bot-generated telemetry, not a human cohort. A video and an input/state replay retain different information. A seed is useful but does not guarantee reproduction. An expert who personally plays supplies a situated account, not a substitute for unfamiliar participants.

## 3. Collection and interpretation

For human work, identify the relevant population and question: first use, repeated mastery, accessibility, comparative performance or experience. Choose neutral tasks and record help, failures and withdrawals. Deliberately choose think-aloud, observation and later questions because the method can affect timing and experience. Keep observed action, participant account and evaluator interpretation distinguishable. Follow the project's participant permissions and data-handling requirements; retain only material needed for the question.

For telemetry, derive a small event set from the decision. Specify event meaning, units, actor/session/attempt identity, start/end/outcome and build/configuration. Check known actions against emitted records, including repeats, resets, successive sessions, missing outcomes and relevant offline/reconnect behaviour. Inspect duplication, loss, time ordering and collection overhead. Zero events can mean no activity or failed collection. Repair invalid instrumentation before using it to justify a design change; preserve the invalid dataset and its limitation.

For comparisons, retain denominators, exclusions, incomplete observations, cohort composition and exposure/order. Report distributions or relevant spread and uncertainty, not only means. State whether the comparison is descriptive, model-based or supported by an experimental allocation. A before/after change is not automatically causal: learning, selection, content, matchmaking and collection changes may explain the difference. Plan sampling and analysis for the actual claim; do not invent precision from repeated trials of the same player or seed.

When evidence conflicts, inspect scope and integrity before averaging it. A passing rule assertion can coexist with a comprehension failure. An aggregate can hide an adverse cohort result. A reported unfair feeling remains a real account even if the rule is implemented correctly; diagnosing its cause requires more than changing a number.

## 4. A tuning loop that preserves accepted play

1. **Observe:** retain the finding, expected and actual behaviour, evidence source, affected revision and conditions. Confirm the evidence is valid; record unresolved cause and impact.
2. **Diagnose:** follow the accepted dependency chain. Distinguish requirement ambiguity, implementation, information/feedback, composition, source delivery, system dynamics and collection defects. Inspect alternatives that could explain the symptom.
3. **Locate responsibility:** identify the parameter, rule, encounter, layout or integration relationship whose change could address the cause. Record the responsible owner, affected consumers and preserved constraints. Do not infer cause from edit convenience.
4. **Make the smallest sufficient authorised change:** state the hypothesis, expected effect, plausible adverse effect and comparison plan. Work within existing ranges/authority; prepare a concrete reopen proposal before changing accepted dependencies outside that authority. Prefer an interpretable bounded change; coordinated edits are legitimate when causally necessary and explicitly recorded.
5. **Replay or rerun:** exercise the disputed situation and affected accepted cases in the new version. Replays must support the required reconstruction. A changed model may require a fresh baseline. Human first-use questions need suitable unexposed participants; replaying old inputs cannot demonstrate new comprehension.
6. **Compare evidence:** inspect the hypothesised outcome, side effects, collection validity, cohort/exposure differences and remaining uncertainty using the appropriate source. A better aggregate cannot hide a violated invariant or access barrier. Separate discovery from confirmatory claims.
7. **Keep or revert:** keep within the authorised scope only when the change addresses the finding and relevant preservation checks pass. Revert or revise when it fails or causes unacceptable effects; investigate when inconclusive. Retain both versions/results and rationale. A new material decision or blocked proof follows the project's stop rules; an unverified change cannot close the finding.

Do not automatically increase difficulty after a clear-rate rise or nerf a popular strategy. The intended task, available information and actual strategic relationship determine whether the observation is a problem. A local arithmetic repair can restore a required cost while leaving human balance unverified.

## 5. Thirteen balance concepts, selected by applicability

These are questions and possible measures, not a mandatory dashboard. Every selected metric names its decision, definition/units, eligible observations, cohort/version, intended direction or accepted range, uncertainty and complementary evidence. Omit inapplicable metrics with a reason. Targets belong to the game and are not inherited from source examples.

| Concept | Useful measure or investigation when applicable | Interpretation limit and companion question |
|---|---|---|
| Win rate | Wins among defined eligible outcomes, by matchup, role, skill/context and version; state draws, exclusions and repeated-player dependence | An aggregate near one half does not establish strategy balance or fairness. Who had access to which choices and opponents? |
| Pick rate | Selections among eligible selection opportunities; distinguish ownership, availability, bans and repeated picks | Popularity can reflect familiarity, availability or appeal. Is the choice strong, attractive, necessary or merely exposed more often? |
| Clear rate | Completed encounters/tasks among defined attempts or entrants, with completion window and handling of retries/abandonment | Completion is not comprehension or enjoyment. Did assistance, survivor selection or missing outcomes alter the denominator? |
| Resource curves | Resource stock and source/sink/conversion flow by game time, turn or progression state, across strategies | An average can conceal depletion or runaway accumulation. Which feedback relationship controls the path and are its units consistent? |
| Time-to-kill | Time from a defined combat event to the specified defeat under health, equipment, aim and encounter conditions | Weapon arithmetic is not observed combat duration. Are misses, cover, interruptions, cues and reset conditions represented? |
| Time-to-mastery | Exposure/time or attempts until a declared performance criterion, with repeated relevant participants and unfinished cases retained | Fast completion or repeated script success is not mastery. Does learning transfer to the intended new situation? |
| Strategy diversity | Use and viability of meaningfully distinct strategies under relevant opponents, information and skill; optionally distribution/concentration measures | Distinct names or equal pick counts need not represent viable alternatives. Are counters, costs and outcomes meaningfully different? |
| Difficulty curves | Challenge indicators across content/progression for stated knowledge, resources and access conditions | Death counts alone mix difficulty, learning, unclear information and technical failure. Which demand changes and was preparation available? |
| Content reachability | Required states/locations/outcomes reachable under permitted actions and actual dependencies; coverage by defined cases/seeds | Graph connectivity or a privileged bot's route does not prove player traversal/discovery. Was placement, collision and usable information included? |
| Progression pacing | Time/attempts/actions and resource demands between meaningful access or accomplishment changes, with stalled and unfinished paths | More time can be engagement, confusion or grind. Which intended session and experience does the pace support? |
| Risk / reward | Possible gains/losses, likelihoods and opportunity costs under stated information, choices and recovery; inspect distributions and player interpretation | Equal expected value need not mean equal appeal or fairness. What can the player anticipate and how costly is failure in context? |
| Snowballing | How an earlier advantage changes future earning, power, options and outcome likelihood under the represented conditions | Advantage/outcome correlation alone does not identify reinforcing causation. Trace the feedback and compare relevant strategies or controlled conditions. |
| Rubber-banding | Catch-up rules conditional on relative position/state; inspect comeback opportunities, completion times, visibility and strategic responses | Closer outcomes do not establish fairness or preserve mastery. Check whether intentional underperformance is rewarded and whether agency is harmed. |

A non-combat puzzle may use state reachability, attempts, hints and first-use observation while omitting win/pick rates and time-to-kill. A competitive combat game may need matchup-conditioned outcomes, selection opportunity and encounter timing. An open-ended simulation may emphasise resource trajectories and agency accounts without a win predicate. These are example choices, not new game commitments.

## 6. Evidence and tuning record

Keep this as a section of the responsible project record or a separately identified finding/run. Retain the lifecycle properties from the behaviour contract; no central telemetry service or universal metric schema is required.

```markdown
Identity / creator / consumers: <finding/run/decision revision and owners>
Question / claim kind: <mechanical, balance, experiential or other explicit claim>
Inputs / authority: <thesis, behaviour/content/build revisions, preserved decisions and ranges>
Method / setup: <source, cases/participants, conditions, exposure, omissions>
Measurement / contrary result: <definitions, units, denominators, integrity and expected comparison>
Actual observations / accounts: <linked run data or notes; not run if absent>
Interpretation / limitations: <supported conclusion, uncertainty and alternative explanations>
Diagnosis / change: <responsible unit, hypothesis, smallest correction and adverse effects>
Rerun / preservation: <new version, failing and affected cases, actual outcomes and remaining gaps>
Disposition / impact: <keep, revert, revise, investigate or proposed commitment; authority and downstream work>
```

Evidence closes only the claim it supports. Keep missing mechanical, balance, human or target proof visible even after another check passes.
