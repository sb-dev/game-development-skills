# Stage 4 - Mechanics, Rules, Systems, Loops and State

**Date:** 13 September 2026  
**Version:** 1.0  
**Status:** Stage 4 complete  
**Output:** [Gameplay Behaviour and Systems Contract](../contracts/gameplay-behaviour.md)  
**Branch / baseline:** `feat/bootstrap-2`, [`41f7e4a7a5f6153d4aee3c525c86e366bac2fb50`](https://github.com/sb-dev/game-development-skills/commit/41f7e4a7a5f6153d4aee3c525c86e366bac2fb50)

## 1. Stage acceptance and inputs

[Bootstrap Stage 4](2026-09-07-game-development-skills-new-project-bootstrap-process.md#9-stage-4---model-mechanics-rules-systems-loops-and-state) and the [execution contract](2026-09-13-bootstrap-execution-contract.md) govern this work.

Acceptance checklist:

- Read the accepted thesis and relevant prior research; preserve those outputs.
- Research the smallest useful distinctions among all 13 listed gameplay concepts.
- Choose useful artefacts without turning candidate folder names into mandatory structure.
- Define all 11 lifecycle properties for every first-class artefact.
- Map both specified dependency chains, including the difference between predicted and observed results.
- Demonstrate that the model can identify a responsible repair scope for systemic failure.
- Produce the actual behaviour model, research/decision record and conformance evidence; verify their substance before the stage commit.

Accepted inputs reviewed are the [charter](2026-09-12-stage-01-project-charter-and-domain-boundary.md), [book findings](2026-09-13-stage-01b-book-findings.md) F2/F6, M1–M6 and S3/S4, [Stage 2 model](2026-09-13-stage-02-professional-practice-and-capability-model.md) P02/P04/P05/P06/P11/P13–P16 and its failure/evidence distinctions, and the [Stage 3 thesis contract](../contracts/game-thesis.md). These are accepted research and decisions, not fresh book extraction in this stage.

## 2. Research and model decisions

| Evidence / reasoning | Finding used | Resulting decision and limit |
|---|---|---|
| Accepted M1/F2 | Mechanics combine rules, processes and data; bounded state descriptions are useful. | Keep verbs, adjudicating rules and runtime expression distinct without requiring a whole-game state machine. |
| Accepted M2/M4 | Flows and their controls can explain systemic effects, while model results remain conditional. | Resources have units/time bases; compositions state sources/sinks, strategies, horizons and omitted behaviour. |
| Accepted M3/F6 | Local correctness and modularity do not establish desirable combined behaviour. | Give interactions an explicit diagnostic home; preserve useful emergence and inspect dependent cases after repair. |
| Accepted M5/M6 and P06/P13 | Task dependencies, actual space and later content placement interact. | An encounter/composition can bind progression, information and spatial constraints without treating geometry as the mission itself. |
| Accepted S3/S4/P05 | State, timing, response and spatial context affect controls. | Represent temporal response, input mapping and feedback alongside rule consequences, using the smallest suitable notation. |
| Epic Games, *Gameplay Framework*, displayed Unreal Engine 5.8 documentation | Newly examined overview and class table distinguish rule/session management, shared and player state, controllers and physical representation, with different lifetimes and replication roles. | This gives a concrete counterexample to one monolithic game object. Our records describe gameplay responsibilities and may map to several runtime objects; Unreal classes are not the repository schema or a selected engine. |

The additional primary source is [Epic's Gameplay Framework documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-in-unreal-engine), accessed 13 September 2026. The textual overview and class table were examined; linked class documentation, videos and engine execution were not. No portability, replication correctness or engine capability was demonstrated here.

### 2.1 Artefact selection

Select three first-class record kinds: **thesis**, **behaviour definition**, **system/encounter composition**. The thesis is the unchanged Stage 3 contract. A behaviour definition brings one interaction's rules, relevant state, control and feedback into a reviewable unit. A composition identifies dependencies and effects that would be lost if each mechanic were judged alone.

This is a responsibility model rather than three mandatory files. Rules, resources, local state tables, controls, feedback and loops may be sections inside the appropriate record. Split only when they have an independent owner/consumer, revision, decision or validation/repair scope. Evidence and decisions remain linked to their owners; no additional evidence store is introduced.

| Alternative | Disposition and reason |
|---|---|
| One folder or artefact type for every vocabulary term | Reject: terminology alone does not justify lifecycle overhead or split tightly related behaviour. |
| One giant game-state model | Reject as a requirement: bounded models can preserve relevant relationships without enumerating the entire game. |
| Mechanics only, with interactions implicit | Reject: fails to explain coupled economies, progression and encounters. |
| One engine class per behaviour record | Reject: rule, input, state and presentation responsibilities can have different runtime lifetimes and mappings. |
| Every unexpected strategy is a defect | Reject: classify against the intended experience before proposing repair. |
| Always change one parameter or one file | Reject as a law: choose a causally sufficient scope and inspect downstream effects. |

The contract's concept table covers all 13 requested terms. Its lifecycle table covers all 11 required properties for each of the three first-class records, including the reused thesis. No Stage 3 wording is changed.

## 3. Worked representation and diagnostic checks

These are **synthetic design/model fixtures**, not implemented games, observed player behaviour or selected progressive examples. Numeric values and traces exist only to test representation and reasoning. No actual owner approval is claimed.

### 3.1 Local behaviour, state and feedback: a retry defect

`SYN-RETRY@1` is a draft behaviour proposed under a hypothetical bounded-session thesis. Its creator is a technical designer; consumers are a controller, outcome display and encounter setup. Source evidence is the synthetic rule below, not a player report. No runtime implementation or accepted production decision exists.

| Prior state / trigger | Required result | Feedback / dependency |
|---|---|---|
| New attempt | Position=start; allowance=4 units; outcome=active | Show active attempt and remaining allowance. |
| Active / wait | Allowance decreases by 1 unit; zero allowance ends the attempt | Cue the cost and failure if applicable. |
| Failed or succeeded / retry | Restore the new-attempt state, including outcome=active | Clear previous outcome presentation; scene setup must consume the restored state. |

A deliberately faulty synthetic trace resets position and allowance but retains outcome=failed. A subsequent wait is unavailable because only the active state permits it. The stated rule identifies the violated responsibility: reset of authoritative attempt outcome, or consumption of that reset if the state is correct but the display remains stale. Increasing allowance does not explain the defect.

The smallest proposed correction is restoring the missing outcome transition, followed by failed→retry→wait and succeeded→retry→wait checks. The consumers affected are input eligibility, outcome presentation and encounter setup. If the outcome value already resets correctly, the trace directs diagnosis to stale derived feedback instead; it does not prescribe a rewrite of the rule. No runtime repair is reported.

### 3.2 Progression/content composition: an inaccessible prerequisite

`SYN-ACCESS@1` is a draft system record. It composes a collect-key behaviour, a key-required gate and a final-goal condition. A level/system designer creates it; content integration and progression checks consume it. The hypothetical source constraint requires an available route to the key before opening the gate. The composition has no implementation or accepted owner decision.

The adverse setup places the sole key behind its own locked gate. Each local rule is intelligible: collecting grants the key; opening requires it. The composition is not reachable from the keyless initial state. The responsible relationship is **key placement/access dependency**, not the collect input or final-goal reward.

A candidate placement change moves the key to a reachable region while preserving the lock rule. Its affected checks include key reachability, route/collision validity, gate opening, any alternative route, and reset. If the placement or lock is already accepted in a real project, the proposal needs that owner's reopen decision. A dependency diagram alone cannot prove the revised spatial route; the runtime/greybox check remains unperformed.

### 3.3 Resource interaction: a free-upgrade cycle

`SYN-ECONOMY@1` is a draft system record combining purchase, price discount and later income. Its hypothetical creator is a systems designer; progression, tuning and evaluation work consume it. There is no accepted production decision or implemented runtime. Its source/preserved constraint is the synthetic requirement that each upgrade purchase consumes positive credits. Start with 10 credits and upgrade level 0, owned by the local player. Each purchase raises the level by one; a later income tick would grant `1 + level` credits. No income occurs during this purchase sequence.

The faulty composition uses `cost = max(0, 3 - level)` and permits another purchase whenever credits cover that cost. After three purchases, 4 credits remain and the next purchase is free. Repeating a free purchase can raise level without reaching a funds-based stop. The defect lies in the **discount/sink interaction and its positive-cost requirement**, although individual subtraction and increment operations are arithmetically valid.

One candidate repair for this synthetic requirement is `cost = max(1, 3 - level)`. This preserves a positive cost and exhausts the finite purchase budget after seven upgrades. A per-turn purchase limit would be a different rule change with different implications; it is not silently substituted. Neither proposal establishes balanced player strategies or an optimal economy.

The bounded arithmetic check below compares the two formulas. It is deliberately limited to ten attempts and cannot be confused with an engine simulation or human test:

```python
def purchases(minimum_cost):
    credits, level, trace = 10, 0, []
    for _ in range(10):
        cost = max(minimum_cost, 3 - level)
        if credits < cost:
            break
        credits -= cost
        level += 1
        trace.append((level, cost, credits))
    return trace

before = purchases(0)
candidate = purchases(1)
assert before[-1] == (10, 0, 4)
assert candidate[-1] == (7, 1, 0)
assert all(cost > 0 for _, cost, _ in candidate)
```

Runtime expression would be price/income configuration and purchase logic in a declared implementation. Validation needs the stated invariant, boundary prices, purchase ordering, income timing and affected strategy/progression scenarios. Repair may change downstream pacing and income, so a real accepted design needs impact/authority review. The arithmetic result alone cannot close those concerns.

### 3.4 Both required dependency chains

| Chain | Concrete synthetic mapping | Evidence boundary |
|---|---|---|
| Player goal → verb → rule → feedback → resulting dynamic → playtest observation → tuning decision | Reach a beacon → wait/commit → waiting spends allowance → allowance cue → predicted pressure to choose an opening → future observation of comprehension and choices → evidence-linked proposal about cue/rule/timing | Dynamic is a hypothesis; observation and tuning acceptance are unperformed. A rule check cannot fill those links. |
| Resource source → resource sink → progression pressure → player strategy → economy result | Later income tick → upgrade purchase cost → incentive to increase income capacity → synthetic repeated-purchase strategy → free-upgrade cycle in the faulty model | Scripted purchases establish the stated arithmetic case only; population balance and actual play remain unknown. |

### 3.5 Adverse modelling checks

| Case | Required response found in the contract |
|---|---|
| Success and failure can occur in the same update but priority is unspecified | Mark the material rule ambiguity; obtain the decision before affected implementation. Do not infer a universal win-over-fail order. |
| A diagram omits a known reset or state owner | Incomplete for that mechanic: complete the relevant transition/ownership or restrict the claim. |
| “Verified” is asserted without build/model and conditions | Evidence state is unsupported; preserve specified/implemented/verified separately. |
| A final asset is blamed although authoritative state is stale | Trace expected/actual state and cue separately; correct the responsible layer. |
| A surprising but legal player tactic appears | Evaluate its effect against the thesis; accept it or propose repair with reasons rather than deleting it automatically. |

These checks show how the contract identifies missing information and scopes a proposed repair. Hypothetical missing game decisions are not unresolved bootstrap decisions: no such game is being implemented or committed here.

## 4. Verification and handoff

The original Stage 4 section was re-read after drafting and compared with the actual contract. Local checks counted **13 concept distinctions**, **three first-class record kinds**, and **11 lifecycle properties × 3 records = 33 populated property cells**, and validated relative links/anchors. The published Python block in §3.3 was extracted from this file and executed unchanged; its assertions passed.

Actual arithmetic output, tuples `(level, cost, remaining credits)`:

```text
before: [(1,3,7), (2,2,5), (3,1,4), (4,0,4), (5,0,4),
         (6,0,4), (7,0,4), (8,0,4), (9,0,4), (10,0,4)]
candidate: [(1,3,7), (2,2,5), (3,1,4), (4,1,3), (5,1,2),
            (6,1,1), (7,1,0)]
```

This run verifies bounded integer arithmetic and the candidate's positive-cost invariant in the stated sequence. It does not verify an engine, long-run economy, player strategy distribution or human experience. The other worked cases were inspected as rule/dependency traces, not executed as games.

| Requirement | Evidence | Verification | Result |
|---|---|---|---|
| Read accepted prerequisites; preserve prior work | §1 input references and unchanged thesis contract | Compared scope, evidence and authority rules with accepted inputs; this stage adds its contract/log and updates only progress | PASS |
| Research the smallest useful distinctions | §2 evidence/alternatives; contract §1 | Reviewed qualified book findings and current primary framework text; checked distinct diagnostic use for all 13 concepts | PASS |
| Treat artefact/folder candidates as hypotheses | §2.1; contract §2 | Selected three record kinds for independent responsibilities; no candidate directory scaffold required | PASS |
| Identify creator, purpose and consumers for every first-class artefact | Contract lifecycle rows 1–3 | Inspected all three kinds, including the existing thesis | PASS |
| Identify source evidence, preserved decisions and status/confidence | Contract lifecycle rows 4–6 | Checked evidence references, revision/constraint preservation and separate decision/evidence states | PASS |
| Identify approval, runtime expression and validation | Contract lifecycle rows 7–9 | Checked existing authority/reopening, concrete-or-unimplemented runtime mappings and scoped checks | PASS |
| Identify repair scope and downstream impact | Contract lifecycle rows 10–11 | Checked local versus interaction repair and affected consumers; 33 lifecycle cells populated overall | PASS |
| Map goal → verb → rule → feedback → dynamic → observation → tuning | Contract §5 and §3.4 of this log | Traced all seven links; future observation/acceptance remains explicitly unperformed | PASS |
| Map source → sink → progression pressure → strategy → economy result | Contract §5 and §§3.3–3.4 | Traced all five links and executed the bounded synthetic arithmetic; human balance not inferred | PASS |
| Identify the smallest responsible unit in systemic failure | Contract diagnostic procedure; §§3.1–3.5 | Located reset state, placement/access dependency and discount/sink interaction; distinguished ambiguous intent and misleading evidence | PASS |
| Persist substantive output and conformance evidence | Contract, this log and index | Checked links, exact required coverage and accurate next-stage progression | PASS |

**Exit decision:** all mandatory Stage 4 requirements pass; no Stage 4 blocker remains. The domain model supports behaviour specification, integration reasoning and bounded diagnosis without requiring a universal runtime or state graph. The next task after remote commit verification is **Stage 5: define prototype, fidelity and commitment strategy**. It must consume these decision/evidence boundaries rather than treat synthetic model checks as playable proof.
