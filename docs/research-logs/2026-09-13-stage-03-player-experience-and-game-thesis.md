# Stage 3 - Player Experience and Game Thesis

**Date:** 13 September 2026  
**Version:** 1.0  
**Status:** Stage 3 complete  
**Output:** [Game Thesis Contract](../contracts/game-thesis.md)  
**Working branch:** `feat/bootstrap-2`  
**Baseline:** [`e0ae05b9c195208c5418ea66301367dec31cd809`](https://github.com/sb-dev/game-development-skills/commit/e0ae05b9c195208c5418ea66301367dec31cd809)

## 1. Acceptance checklist and authoritative inputs

The [execution contract](2026-09-13-bootstrap-execution-contract.md) accepts Stages 1, 1A, 1B and 2 and authorises later stages individually. [Bootstrap Stage 3](2026-09-07-game-development-skills-new-project-bootstrap-process.md#8-stage-3---define-player-experience-and-game-thesis-model) requires research and a compact thesis contract that guides prototype design and later evaluation.

The acceptance checklist is:

- Use the accepted charter, book findings and evidence-qualified Stage 2 model on this branch; preserve earlier work.
- Research and define the minimum useful representation, considering all 16 candidate fields without assuming 16 mandatory top-level keys.
- Separate testable implementation/behaviour statements from experience aspirations and identify suitable evidence.
- Define what is accepted before dependent content production and how it can be reopened.
- Preserve rejected thesis/mechanic alternatives without making them active requirements.
- Deliver one reusable contract, this research/decision log and conformance evidence; verify substance with worked document cases and structural/link checks.
- Confirm the result can direct a bounded prototype and evaluation without requiring a large design document. Stage 3 does not require an implemented game or a participant study.

Inputs reviewed: [Stage 1](2026-09-12-stage-01-project-charter-and-domain-boundary.md), especially §§1–3 and 5–7; [Stage 1A](2026-09-12-stage-01a-knowledge-coverage-and-five-book-corpus.md) coverage identities; [Stage 1B synthesis](2026-09-13-stage-01b-five-book-extraction-and-reconciliation.md), and [findings F1–F4, M7 and T5](2026-09-13-stage-01b-book-findings.md); [Stage 2](2026-09-13-stage-02-professional-practice-and-capability-model.md), especially dispositions, evidence classes, P01/P02/P03/P07/P08/P09/P11 and unresolved questions. Their local contents were checked against the branch's Git blob identities before use. The branch's accepted corpus revision 2 is unchanged.

## 2. Research and design decisions

### 2.1 Evidence consumed

| Input | Examined contribution and limit | Consequence for the contract |
|---|---|---|
| Accepted F1/F2/F3 and P01–P03 | Experience is a hypothesis; procedures and rules need a relationship; a proof answers selected uncertainty. These remain qualified methods. | Connect intended activity, consequences and a question; state the minimum behaviour the next proof needs. |
| Accepted F4/T5 and P07/P08 | Prior knowledge and assistance affect interpretation of first-use evidence. | Record relevant audience assumptions and distinguish observed behaviour from comprehension or reported experience. |
| Accepted M7 and Stage 2 G07 | Interpretation of in-game incentives cannot establish external effectiveness. | Explicitly separate external-effect claims and require appropriate evidence before adopting them. |
| Accepted charter §6 and P11 | Accepted constraints require traceable authority and bounded reopening. | Separate proposed conditions, exploratory authority and accepted production dependencies. Preserve prior revisions. |
| Accepted P09 and Stage 2 accessibility limits | Access conditions belong in core tasks but no general certificate follows from one check. | Include material access requirements in context/conditions, with scoped evidence questions. |
| Hunicke, LeBlanc and Zubek, 2004, *MDA* | Newly examined original PDF pp. 1–3: framework, designer/player perspectives, aesthetics and dynamic models. It distinguishes implementation, runtime interaction and intended experience, and offers vocabulary beyond a single “fun” label. | Use the causal distinction as a review lens, not a required schema or exhaustive experience taxonomy. The article is a framework with illustrative examples, not proof of universal emotional effects. |

The additional source is [*MDA: A Formal Approach to Game Design and Game Research*](https://users.cs.northwestern.edu/~hunicke/MDA.pdf), by Robin Hunicke, Marc LeBlanc and Robert Zubek; bibliographic identity was checked at [AAAI](https://aaai.org/papers/ws04-04-001-mda-a-formal-approach-to-game-design-and-game-research/) on 13 September 2026. The five-page PDF was accessed; only the stated passages are claimed as examined. No code, study or source illustration was reproduced or executed. Previously accepted findings were reused as accepted research, not counted as fresh primary-source examination.

### 2.2 Minimum useful model

Choose a short project-native brief with identity/authority and six content sections: players/context, intended play, loop/outcomes, conditions/boundaries, evidence questions and commitment. This grouping is our design decision. It is not a book's template, an engine object model or a mandatory serialisation format.

The active brief should expose the current causal proposition and decision. Detailed rules, state tables, content lists, implementation choices and full test plans remain linked downstream artefacts. Required information can be brief or explicitly inapplicable. A material unknown must identify what it prevents deciding; it cannot be silently filled with a convenient default.

| Bootstrap candidate field | Contract location | Decision / reason |
|---|---|---|
| Target player / context | Players and context | Required; include relevant knowledge, setting and access assumptions. |
| Player fantasy | Intended play | Conditional; useful fiction/role, or explicitly no fiction for abstract play. |
| Core verbs | Intended play | Required; identify what the player controls. |
| Primary challenge | Intended play | Required as a challenge or meaningful choice; competition is not assumed. |
| Intended mastery | Intended play | State intended learning/skill, or why mastery is not a goal. |
| Core loop | Loop and outcomes | Required causal repetition; no large system diagram. |
| Session structure | Players/context and loop/outcomes | Required entry, continuation/end and expected context; duration can remain an unmeasured target. |
| Success / failure model | Loop and outcomes | Required disposition, including open-ended outcomes when appropriate. |
| Risk / reward structure | Loop and outcomes | State costs/consequences, or explain intentional absence. |
| Desired emotional or experiential qualities | Intended play and evidence questions | Required hypothesis, with suitable human evidence if achievement is claimed. |
| Camera / viewpoint constraints | Conditions and boundaries | Applicable viewpoint/information limits; moving camera may be N/A. |
| Input assumptions | Conditions and boundaries | Required relevant input and access constraints, labelled proposed when unsettled. |
| Platform constraints | Conditions and boundaries | Required known constraints or explicit unknown and its consequence; no engine chosen here. |
| Social mode | Conditions and boundaries | Required; prevents mistaking local proof for networked/social proof. |
| Novelty / differentiator | Intended play | Optional claim; do not manufacture a market distinction. |
| Non-goals | Conditions and boundaries | Required exclusions that constrain the current work. |

Identity, authority and evidence questions supplement the candidate fields because they make revision and downstream use safe under the accepted charter. They do not impose a universal project graph.

### 2.3 Alternatives considered

| Alternative | Decision |
|---|---|
| A single evocative pitch sentence | Insufficient on its own: cannot identify conditions, contrary evidence or accepted constraints. Keep it as a possible opening sentence. |
| All candidate fields as mandatory separate long sections | Reject that structure: it repeats information and forces fiction/novelty/camera claims into unsuitable games. Preserve their meanings through the mapping above. |
| Full GDD with content inventories and implementation detail | Reject for this contract: it raises revision cost and obscures the current experiment. Link detail when it becomes necessary. |
| Mandatory MDA categories | Reject as a schema requirement: retain its analytical distinction without restricting experience vocabulary. |
| Accepting a thesis means its experience is validated | Reject: a decision can authorise exploration while the experience remains untested. |
| Keep rejected ideas beside active instructions | Reject: retain reconstructable history behind an explicit link and select one active revision per scope. |

## 3. Worked document checks

The following **two synthetic briefs** exercise the contract's representation. They are authored examples for document review, not selected progressive examples, implemented prototypes, user-owned game commitments, player observations or measured results. Their owners and authority states are fictional placeholders; neither records real approval.

### 3.1 Synthetic case A: Signal Crossing

**Identity:** `SYN-A@1`; draft; hypothetical example owner; bounded game; no approval recorded.

**Players/context:** A new keyboard player who can inspect a static scene; short local session, with configurable input and pause available. Prior familiarity with timed gates is an assumption to investigate.

**Intended play:** Move, wait and commit through a visible timed opening to reach a beacon. Learn to choose an opening against a remaining-light allowance. Hypothesis: the choice creates anticipation and a sense of control. No novelty claim.

**Loop/outcomes:** Observe opening and allowance → wait or cross → spend allowance and change position → decide again. Waiting during active play costs allowance; pausing does not. Reaching the beacon succeeds; exhausting the allowance ends the attempt. Retry restores the initial attempt.

**Conditions/boundaries:** Proposed browser, keyboard remapping and fixed 2D view; single-player. Critical gate/allowance information must have shape/text cues rather than hue alone. Non-goals: online play, final art, progression and persistent saves. Exact timing values are unknown and block tuning acceptance, not definition of the prototype question.

**Evidence:** Rule question: does waiting spend allowance while pause preserves it? Later check identified state transitions/runtime. Behaviour question: does a new participant distinguish wait from commit without help? Observe choices and explanations. Experience hypothesis: is anticipation experienced as an understandable choice? Use neutral accounts of the decisions. No evidence yet. Indefinite safe waiting, unexplained failures or unclear costs would challenge the design and prompt rule/cue review.

**Next proof/commitment:** A controller/gate sandbox showing allowance, outcome and retry can investigate the action and cue questions. Placeholder content is permitted in this hypothetical setup; no production expansion or accepted baseline exists. History: none.

### 3.2 Synthetic case B: Parcel Ledger

**Identity:** `SYN-B@1`; draft; hypothetical example owner; bounded game; no approval recorded.

**Players/context:** A first-time player using a keyboard or pointer at their own pace. No assumed logistics knowledge. One session has five shifts; elapsed duration is unmeasured.

**Intended play:** Act as a depot planner: allocate effort between repairing storage and dispatching parcels. Learn to anticipate the consequences of sharing limited effort. Hypothesis: understandable trade-offs produce satisfaction. No market novelty claimed.

**Loop/outcomes:** Inspect stock/orders → allocate effort → resolve the shift → inspect changed stock and demands. Repairs consume effort otherwise available for dispatch. A final report records fulfilled/missed requests; retry resets all five shifts. The aim is improving that outcome, not defeating an opponent.

**Conditions/boundaries:** Untimed turns, single-player, visible stock/order information and keyboard/pointer alternatives proposed. Moving camera N/A: a stable ledger view is sufficient. Platform unknown; delivery/performance claims are blocked until selected. Required information must not depend on colour. Non-goals: real-world training efficacy, online economy and generated art.

**Evidence:** Rule question: is effort allocated only once per shift? Later inspect rule cases and runtime. Behaviour question: can new participants explain what they sacrificed by repairing? Observe choices/accounts; a filled dispatch quota alone does not prove understanding. Experience question: what made the outcome satisfying or frustrating? Human evidence is required. No evidence exists. Costless repairs or misunderstood reports would challenge the intended trade-off.

**Next proof/commitment:** Written shift rules and a small table simulation can investigate allocation before a runnable ledger addresses input/readability. Unknown platform does not block the arithmetic question. This hypothetical scope has no accepted production decision or rejected alternatives.

### 3.3 Review results and adverse cases

Document inspection was performed on the actual briefs and contract. PASS below refers only to the listed contract property.

| Case / inspection | Actual result | Contract property verified |
|---|---|---|
| A: identify action, consequence and proof without a full GDD | Move/wait/commit, allowance cost, gate outcome and retry are stated. The next sandbox is specific; tuning values are explicitly unknown. | A concise thesis constrains a prototype while keeping detailed mechanics downstream. |
| A: separate rule, behaviour and experience | The pause/cost question permits formal checking; unassisted distinction needs observation; anticipation remains an experience hypothesis. | One result cannot silently certify another evidence class. |
| B: remove avatar, moving camera and real-time demands | The ledger has meaningful choices and outcomes; camera is explicitly N/A; an arithmetic proof remains possible before platform selection. | The model is not restricted to direct-avatar real-time play. |
| B: inspect omitted detail | Exact effort values and demand schedule belong in later rules; their absence prevents balance proof, but not stating the design question. | Unknowns constrain claims rather than being silently assigned. |
| Replace A's intent with only “make it fun” | It loses the challenge/mastery link and an actionable evidence question. The contract's review rejects this as inadequate for prototype direction. | Vague aspiration alone is insufficient. |
| Claim A's experience is proven by a passing allowance check | The evidence-kind rule rejects the inference; a future rule result would cover only its assertion. | Automated correctness is not human-experience proof. |
| Add incompatible “fixed view” and “free orbit required” conditions | The contradiction needs resolution before work that depends on the viewpoint. Neither value is chosen automatically. | Material conflict stops affected work and goes to the owner. |
| Hypothetically reject `SYN-A-ALT@1`, which automatically crosses gates | Archive its snapshot, competing option, reason (removes the intended choice), evidence status (none) and authority status (hypothetical). The active brief retains only a history link. | Rejection is traceable without becoming an active instruction. No real decision or evidence is fabricated. |
| Hypothetically approve `SYN-A@2` after changing an accepted input constraint | A proposal alone cannot replace the active accepted version. The reopen rule requires actual owner authority and affected checks before switching the reference. | Approval identity and evidence remain version/scope-specific. |

The numerical five-shift case is a synthetic design choice, not an observed optimum. These checks establish that the representation distinguishes the required information; they do not establish that either game is playable, balanced or enjoyable.

## 4. Verification and handoff

The complete original Stage 3 section was re-read after drafting. The actual contract and worked briefs were then inspected against it. A local Python check counted the 16 candidate mappings and six template sections, checked relative links/anchors, and matched all six accepted Stage 1–2 input files to their branch blob identities. It exited successfully. The synthetic briefs contain 268 and 263 whitespace-delimited words respectively; compactness is demonstrated here rather than imposed as a universal numeric gate.

| Requirement | Evidence | Verification | Result |
|---|---|---|---|
| Use accepted prerequisites and preserve earlier work | §1 inputs; baseline Git tree | Compared six accepted input blob identities and read relevant contracts/findings; no earlier-stage edits in this change | PASS |
| Research the minimum useful thesis model | §2.1 source examination and §2.3 alternatives | Reviewed accepted evidence and newly examined MDA passages; separated source claims from project design decisions | PASS |
| Consider all candidate fields | §2.2 mapping | Counted exactly 16 mappings and checked each meaning against the contract; conditional fields have reasons | PASS |
| State intended player action, understanding and experience | Contract intended-play and loop sections; cases A/B | Identified verbs, consequences, learning and experience hypotheses in both actual briefs | PASS |
| Distinguish testable statements and aspirations requiring human evidence | Contract evidence-kind table; §3.3 adverse inference case | Checked rule, behavioural, experiential and external claims; rejected automatic experience proof | PASS |
| Decide what is locked before dependent content production | Contract review/downstream section | Checked exact revision, authority, constraints, scope, evidence and reopen procedure against charter §6 | PASS |
| Preserve rejected thesis/mechanic alternatives without active-state pollution | Contract alternatives section; §3.3 archive/replacement cases | Checked reconstructable history, reason, authority, active reference and version-bound evidence | PASS |
| Remain concise and avoid a universal GDD | Copyable six-section brief; §3.1–3.2 | Reviewed two complete briefs of 268/263 words; detailed rules/content/studies remain linked rather than embedded | PASS |
| Guide prototype design and later evaluation | Contract review rule and evidence questions; §3.3 | Derived a gate sandbox and a rule/table investigation with explicit omissions and contrary-result decisions | PASS |
| Persist stage outputs, verification and accurate progression | Contract, this log and research index | Checked local paths/anchors and Stage 4 handoff; no runtime or human-study result claimed | PASS |

**Exit decision:** every mandatory Stage 3 requirement passes. The output is the reusable [Game Thesis Contract](../contracts/game-thesis.md), with research rationale and actual document-verification evidence here. There are no remaining Stage 3 blockers. The synthetic games are not selected implementation examples and carry no actual project approval.

After the stage commit is verified remotely, the next authorised task is **Stage 4: model mechanics, rules, systems, loops and state**. It should consume the thesis identity, causal loop, conditions, evidence questions and authority rules; detailed mechanics must not be pushed back into the active thesis. No Stage 4 contract or runtime implementation is part of this commit.
