# Stage 7 — Playtesting, Telemetry, Tuning and Balance

**Date:** 2026-09-13  
**Status:** Complete as an evidence and tuning model  
**Branch:** `feat/bootstrap-2`  
**Prerequisite:** accepted Stage 6 commit `5341007e46a4e38a7d2a47404b7d7fc20118282a`  
**Output:** [Evaluation and tuning contract](../contracts/evaluation-and-tuning.md)

## 1. Acceptance checklist and prerequisites

The complete [Stage 7 specification](2026-09-07-game-development-skills-new-project-bootstrap-process.md#12-stage-7---define-playtesting-telemetry-tuning-and-balance-model) was read before work. The acceptance checklist covered all nine named evidence sources, what each can and cannot establish, their overlap without substitution, the complete observation-to-keep/revert tuning loop, all thirteen named balance concepts with applicability limits, an evidence taxonomy distinguishing mechanical/balance/experiential claims, and a research log with actual conformance verification.

Accepted prerequisites inspected were the [charter's quality and authority rules](2026-09-12-stage-01-project-charter-and-domain-boundary.md), the [Stage 2 evidence, failure and capability model](2026-09-13-stage-02-professional-practice-and-capability-model.md), relevant [book findings](2026-09-13-stage-01b-book-findings.md) and [source evidence](2026-09-13-stage-02-source-evidence.md), and the accepted [thesis](../contracts/game-thesis.md), [behaviour](../contracts/gameplay-behaviour.md), [prototype/commitment](../contracts/prototype-and-commitment.md) and [content/handoff](../contracts/content-and-handoffs.md) contracts. Earlier outputs were preserved.

The accepted inputs already reject a fixed participant quota, simulation-equals-human-balance, metrics-equal-enjoyment and editor-equals-target proof. F4–F6 and L5–L6 distinguish session methods, observed behaviour, interpretation and verified collection. M2–M4 identify flows, feedback, strategy assumptions and model limits. S2–S3 distinguish temporal response, measurement and perceived feel. T3/T5/T6 connect view, learning and encounter demands. Stage 2 P04/P08/P11/P12 and failures D01–D21 make the diagnosis and repair responsibilities concrete. These uses refer to accepted, located findings; they do not claim another full reading of the books.

## 2. Primary research and decisions

The following source bodies were directly examined on 2026-09-13. The first two revisit accepted sources for the current decision; they are not counted as new independent validations.

| Source / examined scope | Contribution and disposition | Limits retained |
|---|---|---|
| Medlock, Wixon, Terrano, Romero and Fulton, 2002, [Using the RITE method to improve products](https://www.jpattonassociates.com/wp-content/uploads/2015/04/rite_method.pdf), PDF pp. 1–3: method, issue categories, prerequisites and game-case setup | Retain the need to verify a correction, distinguish an unclear cause from an obvious repair, and identify test-procedure effects. Build identity and decision capacity matter to rapid iteration. | This is the primary work behind F5, not independent corroboration. No universal sample count, two-hour deadline, mandatory think-aloud protocol or commercial success claim is adopted. The result graph was not used as new quantitative evidence. |
| Summoner's Rift Team, 2020-06-30, [Balance Framework Update](https://www.leagueoflegends.com/en-us/news/dev/dev-balance-framework-update/), audience groups, adjustment rationale, predicted/actual outcomes, diversity and framework limitations | Retain cohort-aware outcomes and comparison of expected versus observed effects. Outlier detection does not identify the appropriate design repair or cover every game-health concern. | Historical League of Legends practice; no current Riot policy, thresholds or patch cadence are imported. Selection and viability remain different questions. |
| Ian Schreiber, 2010-07-07, [Level 1: Intro to Game Balance](https://gamebalanceconcepts.wordpress.com/2010/07/07/level-1-intro-to-game-balance/), article body, especially symmetry, metagame/root causes and leader-targeting feedback | Use the practitioner argument that symptoms can occur downstream of the responsible system, and that corrective feedback can change incentives. Treat those as questions to investigate in the actual game. | No linked video or complete course was examined. Do not adopt its broad reductions of balance to numbers, hidden-information/determinism terminology, historical game/sport claims or universal judgement about player-balancing mechanics. This is teaching, not a controlled study. |

Accepted R02/R03 continue to qualify sampling and behavioural proxies; R14/R16 support target-specific profiling and isolated automated checks. Those records were read in the repository, without claiming new execution. The taxonomy and measurement definitions are this stage's synthesis, not a quotation of a source's framework.

The balance table covers all thirteen concepts. Outcome/selection/diversity questions use the cohort and interpretation lessons above. Resource, risk/reward, snowballing and catch-up questions use the qualified M2–M4 feedback analysis. Timing, learning, difficulty, reachability and progression questions connect the accepted control, content and playtest findings. The table gives operational definitions and necessary context rather than asserting empirical ideal values.

## 3. Evidence taxonomy and tuning design

The contract contains nine distinct source rows, each with an affirmative capability, an explicit inference limit and retained context. It separates mechanical correctness, balance evidence and subjective experience before selecting methods. Overlap is explicit: human play can reveal a rule defect and bot sessions can emit telemetry, while neither source changes identity merely because its output is numeric.

The tuning procedure retains all seven steps in the bootstrap's example: observe, diagnose, locate the responsible unit, make the smallest sufficient change, rerun/replay, compare, and keep/revert. It adds the accepted requirements to verify collection, preserve revisions/ranges and recheck affected behaviour. It permits coordinated edits when necessary and within authority; it does not require a new approval for every adjustment or pretend that the smallest text edit has the smallest gameplay impact.

Rejected alternatives are a universal metric dashboard, a scalar score averaging away failures, automatic changes at a fixed win/clear-rate threshold, replacing human first-use work with replayed inputs, and universal player quotas. Context-specific metric selection is demonstrated for a non-combat puzzle, competitive combat and open-ended simulation. These are method examples, not selected consumer games or accepted production scopes.

## 4. Adverse evidence review

The following nine cases are synthetic document-review cases. Each row was reviewed against the actual contract's claim limits and response; no participant, bot, engine, profiler or live telemetry session was executed for these cases.

| Case / evidence source | Invalid inference challenged | Reviewed response and supported scope |
|---|---|---|
| E1: scripted automated tests | A reward invariant passes, so the whole encounter is fair and enjoyable | Retain the scoped invariant result; require the relevant strategic and human evidence for the broader claims. Check oracle and case coverage. |
| E2: headless simulation | Two fixed strategies earn equally, so the game is balanced | Retain the result for the two scripts and model; inspect other strategies, omitted coupling and actual play before generalising. |
| E3: bot/agent playtests | A bot with hidden-state access reaches the exit, so new players can discover it | Label the knowledge privilege. Reachability under that policy does not establish permitted-player discovery or comprehension. |
| E4: telemetry | No failed jumps are logged, so jump controls need no investigation | Check collection against known failed actions, event definitions and session boundaries first. Missing records can invalidate the denominator and claim. |
| E5: replay analysis | An old input sequence completes after a cue change, so first-use understanding improved | Use it only for reconstructed mechanical behaviour if compatible. New comprehension evidence requires relevant unexposed participants. |
| E6: expert review | A designer familiar with the map navigates it, so onboarding works | Retain expert critique and the situated account; familiar knowledge cannot establish unfamiliar-player behaviour. |
| E7: human usability/comprehension | A participant finishes after the facilitator explains the answer, so unaided comprehension passed | Record the assistance and narrower outcome; inspect the missing information and use suitable first-use evidence for a repair. |
| E8: human experiential play | A positive account or average survey score proves all players find the game fun | Keep the scoped account and its conditions, variation and method limits; no universal or external-effect claim follows. |
| E9: platform profiling | An editor average meets a budget, so the target build has no stalls | Preserve the editor result as investigation evidence; target/workload capture and problematic intervals remain necessary for that claim. |

All nine reviewed responses preserve the appropriate source and reject the unsupported substitution. They are evidence about the design's responses to the stated cases, not evidence that a game's evaluation has been performed.

### 4.1 Executed cohort arithmetic

To check the comparison rule against a concrete counterexample, the following invented data were evaluated with Python 3.12.14. This is arithmetic about cohort composition, with no actual players and no causal experiment.

```python
baseline = {"new": (20, 100), "experienced": (81, 90)}
candidate = {"new": (30, 100), "experienced": (19, 20)}

def rates(data):
    return {
        **{group: clears / attempts for group, (clears, attempts) in data.items()},
        "aggregate": sum(x[0] for x in data.values()) / sum(x[1] for x in data.values()),
    }

before, after = rates(baseline), rates(candidate)
assert all(after[group] > before[group] for group in baseline)
assert after["aggregate"] < before["aggregate"]
print(before, after)
```

| Declared cohort | Baseline | Candidate | Actual arithmetic result |
|---|---|---|---|
| New | 20/100 | 30/100 | 20% → 30% |
| Experienced | 81/90 | 19/20 | 90% → 95% |
| Pooled | 101/190 | 49/120 | 53.1578947368421% → 40.83333333333333% |

Both assertions passed. The pooled rate falls while both within-cohort rates rise because the observed mix differs. This counterexample invalidates an aggregate-only interpretation; it does not show that a candidate caused either improvement. The actual decision under the contract is to inspect comparability and retain cohort counts before proposing a gameplay change. No target, validator or denominator was changed to make the example pass.

### 4.2 Full-loop repair and preservation review

The accepted [Stage 4 economy calculation](2026-09-13-stage-04-mechanics-rules-systems-and-state.md) supplies a prior synthetic mechanical finding. Reviewing it through the new loop gives: observe a zero-cost upgrade despite a positive-cost requirement; diagnose the cost-floor relationship; locate the cost rule and its consumers; propose a positive floor under the fixture's stated constraint; rerun the relevant sequence; compare required cost and progression consequences; retain only the supported mechanical correction while leaving human balance open. The previously executed bounded results are still evidence for their original sequence, not a new whole-game evaluation in Stage 7.

A contrasting synthetic case changes jump strength to improve one route but violates another accepted route. Even with an improved local completion metric, the keep condition fails: revert/revise, identify whether geometry, cue or motion caused the symptom, and obtain any required reopening before changing accepted dependencies. Both cases were reviewed as decisions, not runtime repairs or user approvals.

## 5. Verification and exit

The full original Stage 7 section and actual contract were re-read after drafting. Structural checks counted nine evidence sources, thirteen balance concepts, seven tuning steps and nine adverse review cases; local links/anchors were checked. The cohort code was executed and its real output inspected. Substance was checked against the original distinctions and exit criterion rather than inferred from those counts alone.

| Requirement | Evidence | Verification | Result |
|---|---|---|---|
| Reconstruct accepted evidence and authority inputs | §1; linked prior records | Inspected relevant findings, qualifications, quality dimensions, ranges and correction boundaries | PASS |
| Separate all nine named evidence sources | Contract §2 | Counted nine rows; checked individual capabilities, limits and retained context | PASS |
| Define what each can and cannot establish | Contract §§1–3; E1–E9 | Reviewed nine contrasting inference cases, including overlaps and invalid substitutions | PASS |
| Preserve mechanical/telemetry/human evidence distinctions | Contract §§1/2/6 | Checked bot telemetry, human defect discovery, scoped accounts and unperformed claims explicitly | PASS |
| Research and define the complete tuning loop | §2 research, contract §4 and §4.2 review | Inspected seven steps from observation to keep/revert, causal scope, actual rerun requirements and preservation | PASS |
| Cover all thirteen applicable balance concepts | Contract §5; §2 research synthesis | Counted and inspected all thirteen definitions with units/denominators or causal questions and interpretation limits | PASS |
| Do not impose the same metrics on every game | Contract §5; §3 alternatives | Checked contextual selection, omitted metrics and three contrasting game-form examples; no universal targets | PASS |
| Make comparison and collection limits actionable | Contract §3 and E4; §4.1 | Executed cohort arithmetic; inspected both asserted directions and retained the non-causal limitation | PASS |
| Distinguish correctness, balance and subjective experience | Contract §§1/6; E1/E2/E7/E8 and §4.2 | Checked that one pass cannot close another claim and that a preservation failure prevents keeping a change | PASS |
| Persist complete output, research and truthful evidence | Contract, this log and index | Inspected actual content and relative links; no game, human-session or profiling result fabricated | PASS |

**Exit decision:** all mandatory Stage 7 requirements pass and no Stage 7 blocker remains. After remote commit verification, the next stage is **Stage 8: research AI skills, engines and tools**. Actual game evaluation and installed capability proofs remain unperformed.
