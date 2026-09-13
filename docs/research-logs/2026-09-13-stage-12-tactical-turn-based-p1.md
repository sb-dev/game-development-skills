# Tactical Turn-based: P1 specialisation and core baseline

**Date:** 2026-09-13  
**Pack / phase:** `tactical-turn-based` / P1 within Stage 12  
**Inputs:** [catalogue curation](2026-09-13-stage-12-catalogue-curation.md), [core skills and commands](../contracts/skills-and-commands.md), [gameplay behaviour](../contracts/gameplay-behaviour.md), [prototype / commitment](../contracts/prototype-and-commitment.md), [content integration](../contracts/content-and-handoffs.md), [evaluation](../contracts/evaluation-and-tuning.md), [execution](../contracts/execution-and-installation.md).

P1 accepts a bounded reusable need and honest core comparison, all eleven definition areas, explicit constraints/defaults and provisional evaluation. It does not select a corpus, complete specialist research or demonstrate an implemented pack.

## 1. Specialisation brief

| Required area | Decision |
|---|---|
| Intended use / non-use | Local player-paced tactical encounters where discrete actions, spatial position, limited opportunities and declared turn/phase resolution shape decisions. Initially qualify a small 2D board/grid with a few units. Not every game with a menu, grid, pause button or turn counter qualifies. Real-time strategy, networking, grand strategy, narrative style and non-spatial card economies need different or additional evidence |
| Reusable production need | Connect available decision information to legal actions and costs, spatial constraints, commitment/cancellation and ordered resolution; evaluate resulting choices and repair state/preview/cost faults without changing accepted rules |
| Core revision / baseline | Core design `10101f5e01661d6622964e2c0a030be7c7c1ad05`; specified, not implemented/measured. The baseline is the complete substantive encounter in section 2, not a vague game request |
| Why core + ordinary project instructions is insufficient | Core can implement rules, state and a tactical brief. The research hypothesis is that a reusable procedure for deriving an action/phase matrix, reconciling preview with current legality, analysing opportunity costs and checking resolution edge cases provides consistent depth beyond repeating each project's instructions. If actual fair comparisons show no useful difference, P7 must qualify, revise or reject the pack |
| Expected specialised behaviour | Define decision and resolution phases and what the player can know; make action eligibility/cost/effects explicit; evaluate spatial and opportunity trade-offs; test stale information, repeated actions, actor removal and outcome/reset; localise a correction at the responsible rule, presentation or execution layer |
| Relevant core skills | game-development: design-mechanic, model-system, build-playable-proof, integrate-content, repair-gameplay, prepare-playable-build; game-evaluate: validation, balance, player experience, accessibility, performance and diagnosis as relevant. Creator owns optional authoring; consuming games do not depend on it |
| Hard constraints | Preserve approved action budgets, turn order, movement/range/occupancy, information visibility, randomisation policy and outcome/restart. Reject illegal actions without undeclared cost or partial effects; resolve committed actions and phases consistently. Report evidence scope and actual versus proposed results. Baseline access remains core |
| Soft defaults | Begin with a tiny encounter and few distinct actions; make relevant costs and legal/illegal choices inspectable; distinguish preview, commitment and resolution; use bounded deterministic cases when adequate to expose a fault. Do not mandate perfect information, grids, action points, undo, fixed unit counts, hit percentages or a particular enemy algorithm for every project |
| What must remain stable | Accepted rule identities, costs, visibility policy, unit/board state, turn and outcome semantics, input alternatives and evidence provenance. A preview repair must not secretly change combat rules; a cost repair must not rebalance all units or reveal hidden information |
| Adjacent-domain boundaries | Engineering implements state transitions, UI, pathfinding and native tools. Gameplay owns legal movement/range, decision information and opponent-behaviour requirements. General transaction infrastructure, network replication, backend/security and engine architecture remain engineering-owned. Art/narrative/audio craft remain adjacent |
| Provisional evaluation questions | Can a produced action/phase model expose duplicate spending, stale preview, illegal occupancy or lost turn resolution? Does a bounded repair preserve accepted action economy and legal routes? Are tactical alternatives actually available under the encounter's information/constraints? Does a distinct turn structure still benefit? Do automated strategies stay separate from claims about human comprehension, depth or balance? |

## 2. Honest core baseline and comparison

The substantive production need is a small original local tactical encounter with controllable units, at least two meaningful actions, limited action opportunities, spatial restrictions, opposition or a conflicting objective, declared information, visible action/outcome feedback, win/loss and restart. Choices must have consequences in the actual running game. A board mock-up with clickable tiles is insufficient.

Use the selected local browser proof path or another explicitly accepted native path, identical across comparison arms. Supply the same units/rules, objective, information constraints, input/access needs, starting assets, time/resource budget and evaluation cases to core-only and core-plus-pack runs. Core must receive a complete brief and retains its own full rules/evidence/repair workflow. Only pack selection and its packaged guidance differ in the primary comparison. If a longer ordinary instruction sheet explains the same benefit, test that alternative instead of crediting pack metadata.

The proposed delta is **decision information → legal action and opportunity cost → commitment → ordered resolution → changed tactical situation → evidence and causal repair**. This is an authoring/evaluation workflow, not a required engine architecture or a claim that every tactical game is deterministic or fully visible. The initial showcase can use a deterministic small board to make defects inspectable; other information/turn structures require declared rules and appropriately bounded tests.

## 3. Qualification, alternatives and boundaries

The accepted precision-platformer profile does not serve this need: movement envelopes and continuous landing input do not supply action-budget, decision-preview or turn-resolution reasoning. Both reuse the same core evidence and preservation obligations. Neither replaces core, and neither should silently activate the other.

A single encounter's grid size, damage table or team composition belongs in project instructions. Basic accessibility, testing, state inspection and asset integration are core responsibilities. A general command bus, state-machine library or distributed transaction layer is an engineering implementation option, not a new Game Development pack. What qualifies for research is the recurring tactical decision/resolution method across different encounters and rule configurations.

Information availability is a design constraint. A prediction must be truthful about what it represents, but need not reveal an opponent's hidden intent or a random result the game intentionally withholds. Cancellation and undo also need declared semantics; neither is assumed universally available after commitment. Distinguish invalid input, a changed situation, an intentional risk and a harmful rules exploit before proposing repairs.

Provisional falsification opportunities include a preview that retains an old target/range after movement, a rapid repeated action that spends twice, a removed actor that stalls phase advancement, and a superficially different action made pointless by its opportunity cost. The first three permit technical checks under declared rules; the last also requires adequate strategy/encounter coverage and human evidence for experiential claims. No fixture has run yet.

## 4. Verification and handoff

Re-read bootstrap 17.3 and canonical P1, then inspected the brief against the selected catalogue and accepted core. All eleven required definition areas are explicit. The baseline includes actual tactical production, and the core alternative remains competent and testable.

| Requirement | Evidence | Verification | Result |
|---|---|---|---|
| Bounded intended use, repeated need and relevant skills | Section 1 | Discrete tactical production distinguished from grid/view labels, broad core and adjacent work | PASS |
| Exact honest core baseline | Section 2 | Core revision/status and equal substantive comparison conditions recorded | PASS |
| Explain specialised delta and alternatives | Sections 2–3 | Reusable action/phase method justified as a hypothesis; existing platformer/core/project alternatives assessed | PASS |
| Hard constraints, defaults and stable work | Sections 1 and 3 | Action/cost/visibility rules preserved; undo, randomness, grid and action points remain project choices | PASS |
| Boundaries and falsifiable questions | Sections 1 and 3 | Engineering/craft ownership retained; technical and human questions separated | PASS |

**P1: COMPLETE.** P2 corpus selection is next after this checkpoint is committed and remotely verified. Overall Stage 12 remains in progress; Tactical Turn-based implementation planned, evaluation not run, readiness not ready.
