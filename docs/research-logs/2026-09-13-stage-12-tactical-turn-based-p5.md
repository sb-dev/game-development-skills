# Tactical Turn-based: P5 production profile and evaluation design

**Date / profile:** 2026-09-13 / `TT-01`  
**Pack:** `tactical-turn-based`  
**Accepted evidence:** [P1](2026-09-13-stage-12-tactical-turn-based-p1.md), [P2](2026-09-13-stage-12-tactical-turn-based-p2.md), [P3](2026-09-13-stage-12-tactical-turn-based-p3.md), [P4](2026-09-13-stage-12-tactical-turn-based-p4.md).  
**Core baseline:** `10101f5e01661d6622964e2c0a030be7c7c1ad05`, specified, not implemented or measured.

This profile defines operational behaviour and falsifiable cases before implementation. Research establishes a qualified hypothesis; Stage 20 must still demonstrate useful specialisation in actual production, comparison, reuse and installed use.

## 1. Scope, qualification, activation and precedence

Use for bounded local 2D tactical encounters where discrete actions, position, limited opportunities and declared phase resolution shape player decisions. The reusable method is decision information → legal action/opportunity cost → commitment → ordered resolution → changed tactical situation → evidence and causal repair. These recurring relationships justify specialist research; a grid size, damage table or named genre alone does not justify a pack. Core remains capable of the complete substantive P1 task. If ordinary project instructions perform equally well without meaningful recurring burden, packaging value remains unproven.

Activate through an explicit user request or the consuming project's selected-pack configuration. Record the selected profile revision and applicable task. A board screenshot, menu, turn counter or unrelated genre mention does not activate it. Apply only relevant rules to a bounded design, review or repair request; do not rebuild a game to satisfy the full authoring workflow.

Precedence is **explicit project instructions → approved / locked game decisions → selected pack → core defaults**. Identify the accepted rules and authorised change scope before proposing a default. A new explicit instruction may authorise a change; the pack itself cannot reopen locked decisions. Surface a genuine unresolved conflict, perform useful non-conflicting work and obtain only missing authority. Do not ask again for authority already provided. Equal conflicting pack defaults have no implicit winner.

Initial qualification excludes network synchronisation, real-time strategy, grand-strategy economies, general tactical AI, art style and narrative genre. Simultaneous orders, random combat and hidden information are possible project rules, not universally implemented pack features: declare their semantics and prove the cases actually used. Do not claim their readiness from a deterministic showcase.

## 2. Operational rules and effects

| Rule | Required production behaviour | Mechanical / artefact effect |
|---|---|---|
| **TT-R1: establish decision and phase semantics** | Inspect existing units, objectives, actions, information and accepted state. Record eligible actor/phase, prerequisites, movement/range/occupancy, opportunity cost, effects, turn advancement, removal, outcome and reset. Separate selection, cancellation, commitment and optional committed undo | An action/phase matrix predicts legal transitions and costs, including empty/removed actors. AP, grids, undo and a fixed turn length are not mandatory |
| **TT-R2: reconcile information with commitment** | Define known, conditional, random and deliberately hidden information. Preview the current selected actor/action/target within that scope. Validate eligibility at commitment; handle changed/removed targets, repeated input and stale previews without undeclared partial effects | Offered choices and actual effects agree about costs, legality and uncertainty. A forecast states its assumptions rather than exposing hidden information or promising a guaranteed outcome |
| **TT-R3: make resolution order deliberate** | Declare sequential initiative or simultaneous observation/collision rules. Check action consumption, effect count, phase entry/exit and delayed work against the current encounter/session. Use a suitable native implementation, not a required command or state-machine framework | Repeated confirmations and old callbacks cannot spend twice, refresh opportunities twice or mutate a restarted encounter. Storage order affects results only when it implements a declared order |
| **TT-R4: analyse choices in the encounter** | Relate costs and effects to position, information, objective and available alternatives. Exercise bounded strategies with declared knowledge, starting cases and randomness. Separate correctness, reachability, tactical value and human decision quality | A useful route/action is executable under the opportunity limits. Strategy traces show assumptions and omitted cases; equal damage, a fitted curve or two scripted outcomes cannot certify balance |
| **TT-R5: verify the complete decision cycle** | Exercise selection, preview, cancel/commit, opponent/phase resolution, removal, win/loss and restart using actual supported input. Inspect navigation/focus and critical information channels. Reconcile accepted/rejected action records with actual session boundaries | The game remains controllable through phase/UI changes. Complete-cycle and collection evidence complements isolated rule tests. Human understanding and assistive-device claims require the relevant actual evidence |
| **TT-R6: diagnose and preserve** | Reproduce the finding and distinguish rule/cost, spatial composition, information, execution/order and evidence faults. Change the smallest sufficient responsible unit within authority; rerun affected legal actions, alternatives and encounter outcomes | A repair restores the failed contract without secretly changing accepted budgets, visibility, initiative or unrelated units. Record cause, change, preservation and observed reruns; a small diff alone is insufficient |

## 3. Core effects, constraints and boundaries

| Core responsibility | Specialised effect | What remains core |
|---|---|---|
| game-development: design-mechanic / model-system | TT-R1–R4 connect opportunity, information, spatial eligibility and resolution | Authority, rule identity, system assumptions and adequate evidence |
| game-development: build-playable-proof / integrate-content | Derive an adequate board/rules representation, interactive decision path and complete encounter; check placement against legal plans | Fidelity choice, actual implementation, handoff and source/import/runtime responsibility |
| game-development: repair-gameplay / prepare-playable-build | Preserve declared costs/order/knowledge and test phase/outcome/reset in the resulting build | Authorised mutation, target/tool selection, build identity and release boundaries |
| game-evaluate: validation / balance / diagnosis | Use the action/phase matrix, bounded policy coverage and responsible-layer cases | Independent findings, collection integrity, smallest repair recommendation and no silent game changes |
| game-evaluate: player experience / accessibility / performance | Assess actual decision information, complete navigation/focus and relevant resolution/UI behaviour | Human/target evidence limits and core access responsibility; untimed turns are not an accessibility pass |
| game-extension-pack-creator: author-extension-pack | Consume completed P1–P5 and implement local guidance, fixtures and comparative proof | Domain-owned authoring, source permissions, installation and truthful readiness; no P-stage command hierarchy |

**Hard constraints:** preserve accepted action opportunities, movement/range/occupancy, information, randomness, initiative, outcome and reset; illegal actions cannot have undeclared partial spend/effects; record actual evidence conditions; preserve critical task information and applicable access requirements. A review remains a review unless mutation is authorised.

**Soft defaults / qualified methods:** start with a small encounter, few distinct actions, inspectable costs, clear selection versus commitment and deterministic diagnostic cases when adequate. No universal AP system, damage curve, perfect information, undo, grid, cover, timer or opponent algorithm. Truthful previews may be conditional or probabilistic. Cancellation and committed undo differ. A snapshot can implement some resolution contracts but is not always necessary; fixed strategies diagnose their model, not all tactical play.

Gameplay owns legal actions, opportunity/position relationships and information requirements. Engineering owns native state/UI/pathfinding, concurrency, performance and network architecture. Art, environment, animation and audio owners receive gameplay meaning and integration checks while retaining their craft. Narrative style and content-provider choice stay adjacent/project-specific. No new engine, transaction service or universal tactical solver is required. Each core skill works independently; the creator is not a consuming-game dependency.

## 4. Predefined acceptance cases

All cases below are **designed, not executed**. Actual tests must preserve their expected outcomes before observing the run. Scripted setup/model results, native browser input, human observations and target measurements remain separately labelled.

| ID | Setup / expected effect | Failure and acceptance criterion |
|---|---|---|
| **TT-A01 Activation / non-use** | Same substantive task with requested pack, no pack, and a grid-art near miss | Selected run applies relevant rules; core-only remains useful without claiming activation; art request does not acquire tactical gameplay |
| **TT-A02 Legal action and opportunity** | Showcase: inspect legal move/pulse/guard, blocked/out-of-bounds/occupied move, out-of-range pulse, zero-budget action and cancellation | Accepted action spends exactly its declared cost and effect; rejected/cancelled request spends nothing. Recorded action matrix matches actual runtime input/results |
| **TT-A03 Stale and repeated commitment** | Select a legal action, change actor/target or remove that target in a disposable setup; issue repeated confirm input for the same pending request | Current legality is checked and the same committed request resolves once. A second separately selected legal action remains allowed; the guard cannot suppress legitimate later play |
| **TT-A04 Preview and knowledge** | Reproduce stale range/cost information; also inspect a conditional enemy forecast after player movement | Preview updates or clearly expires and matches its declared scope. Repair presentation/validation without changing accepted range/cost or revealing withheld intent. Conditional forecasts must not imply a guarantee |
| **TT-A05 Declared order / removal** | Showcase resolves E1 then E2, including E1 removed and all enemies removed; independent fixture uses alternating initiative | Correct remaining actors act once; removal does not stall or duplicate phases. Permute storage only for explicitly order-independent work; do not demand equal results from intentionally different initiative |
| **TT-A06 Delayed resolution / restart** | If delayed presentation/opponent work exists, restart while it is pending and let the original callback arrive; also check ordinary immediate restart | New session keeps its initial state and phase; no old effect/log entry leaks. Immediate implementation can prove the absence of scheduled mutation and still test restart; do not manufacture an asynchronous subsystem just to use this case |
| **TT-A07 Complete encounter / access** | Win, lose, restart twice; traverse unit/action/target, cancel, End Turn and outcome/restart using keyboard, with visible focus and sound off | Actual complete paths work, focus remains usable when controls/actors disappear, essential meanings have declared readable cues. Technical success does not claim human comprehension or full accessibility certification |
| **TT-A08 Tactical alternatives / evidence** | Run at least a passive and objective-directed policy from the showcase start; declare available knowledge and record legal actions/outcomes | Actual strategies and logs reconcile with session state. Report limits; two policies or equal expected damage cannot certify depth/balance. Invalid policy information or mixed-session counts must be repaired before tuning |
| **TT-A09 Responsible repair / preservation** | After a valid baseline, evaluator injects a local stale-preview or illegal-range defect without identifying its location in the repair request | Diagnosis identifies the responsible layer; correction preserves accepted action costs, phase order, board identity, information policy and unaffected actions. Global damage/budget changes that conceal it fail |
| **TT-A10 Precedence / intentional trait** | Accepted strict commitment/no undo and undisclosed opponent intent; request a narrow cue repair | Preserve commitment and withheld intent while fixing actual stale cues/illegal effects. Do not add undo or perfect prediction as presumed improvements; genuine faults remain defects |
| **TT-A11 Independent reuse** | Run Two Couriers in section 6 with alternating initiative and one action per activation | Derive the new action/phase and information cases, including target handoff/removal; do not paste the showcase's AP, enemy order, objective or full-information assumptions |
| **TT-A12 Fair differential** | Matched fresh core-only and packed contexts use section 5 verbatim; ordinary-instructions arm if value remains unclear | Compare actual legality/information reasoning, defect detection, repair and preservation under comparable tools/resources. Retain negatives/inconclusives; pack name, extra prose or a richer packed brief earns no credit |
| **TT-A13 Installed closure / incompatibility** | Clean external selective install; separately request networked simultaneous tactics or conflicting selected-pack defaults | Supported installed task resolves required local guidance without creator, books, research or source checkout. Unsupported/conflicting scope is bounded honestly; no network or universal simultaneous-order readiness claim |

Evaluate useful behaviour, correctness, preservation and access as separate dimensions. Record effort/context costs only when measured. P7 may refine or retain the pack as unproven if it does not demonstrate reusable benefit; a favourable single sample is limited evidence.

## 5. Showcase brief and exact copyable prompt

**Relay Hold** is an original small defensive encounter. It makes action opportunities, position, conditional intent and sequential resolution observable. The fixed values are this example's project instructions, not pack defaults. A deliberately passive policy should lose; an objective-directed legal plan must be demonstrated in the actual game. No human strategic-quality result is presumed.

For the packed arm select `tactical-turn-based` in the consumer's pack configuration before issuing the prompt. Core-only leaves selection empty. Keep the task text, inputs, tools, resource constraints and evaluation identical; record the effective contexts and revisions.

```text
Build Relay Hold, an original small local browser tactical game, using the installed game-development capability and any pack explicitly selected in this project's configuration.

Use a 6 by 5 board with integer coordinates x=0..5, y=0..4, origin top left. A movement-blocking wall is at (2,2). The relay is at (3,2), has 3 health and blocks movement. Couriers A and B start at (1,1) and (1,3), each with 3 health. Enemies E1 and E2 start at (4,2) and (3,4), each with 2 health. Occupied tiles block movement. All adjacency is cardinal. Remove any courier or enemy immediately at zero health. Use original shapes, text and readable instructions; no accounts, downloaded assets, remote service or networking.

Player phase: each living courier starts with 2 action points. Select a courier, action and target, inspect the proposal, then confirm or cancel. Move costs 1 and enters one empty cardinally adjacent in-bounds non-wall tile. Pulse costs 1 and deals 1 damage to one enemy within Manhattan distance 2; it ignores the movement-only wall and has no line-of-sight rule. Guard costs 1, requires adjacency to the relay, and sets the relay's shield to 1 for the next enemy phase; it cannot stack beyond 1. Removing an enemy at zero health is immediate. Cancel and invalid actions spend nothing. End Turn explicitly ends the player phase even with unused points. No committed-action undo, randomness or player turn timer.

Enemy phase: living enemies act once in E1 then E2 order. An enemy adjacent to the relay attacks it for 1; otherwise it attacks an adjacent courier for 1, choosing A before B; otherwise it moves one legal tile that strictly reduces Manhattan distance to the relay, breaking ties up, left, down, right. If no such move exists it waits. Each action uses the current state after prior actions. The relay shield absorbs the first incoming relay damage of that enemy phase, then clears; any unused shield clears at phase end. Check loss after each effect if relay health is zero or both couriers are gone. Survive three completed enemy phases with a living courier and relay health above zero to win. Otherwise start a new player phase with 2 points per living courier. Removed enemies cannot stall the phase; outcome resolves once.

All board units and rules are visible. Show a conditional forecast of each enemy's next action from the current state, labelled as conditional on no further player change and updated when that state changes. Do not promise the forecast survives later player actions. Show selected actor, action cost, eligibility/rejection reason, phase and outcome with text or symbols as well as colour. The full selection, preview, cancel/confirm, End Turn and restart path must work with keyboard and visible focus. Restart restores every initial value and invalidates any pending action or delayed work.

Keep these rules stable while repairing implementation or cue faults. Provide the actual playable project and exact local run instructions, a compact action/phase record, and observed checks for legal/illegal/repeated actions, changed targets, complete win/loss/restart, keyboard use and forecast agreement. Demonstrate a passive policy and a legal objective-directed winning plan; record their assumptions and outcomes without claiming this proves tactical depth or balance. Separate controlled setup from real browser input and do not invent human playtest evidence. Do not publish or release externally.
```

After a valid baseline, an evaluator introduces TT-A09's bounded fault in a disposable copy and asks for diagnosis/repair without disclosing the responsible location. Retain pre-fault, faulty and repaired versions and observed evidence. Do not credit a prompt that names the answer as independent diagnosis.

## 6. Independent reuse brief / fixture

**Two Couriers** is a separate delivery encounter. Two couriers must hand a parcel between them and deliver it to an exit while avoiding a warden. Each actor has **one action per activation**, with alternating initiative A → warden → B → warden. A courier can move up to two connected legal cardinal tiles or hand the parcel to an adjacent courier; there is no AP bank, ranged damage or relay. Commitment is strict, cancellation before commitment is allowed, and the warden's next intent is intentionally undisclosed. Its observed position and resolved effects remain visible and truthful.

At the owning implementation stage, author and pin its own small board, obstacle layout, start/exit positions, patrol/encounter rules and outcome/restart semantics. Establish at least one actual legal delivery path and a failed encounter before adding the fault. Specify exactly what the player may know; a validation harness may inspect internal state but a player-policy claim cannot use withheld information. This is a distinct authoring output with independent acceptance, not a reskin of Relay Hold.

Introduce a stale parcel-target/selection fault after a handoff or actor-state change. Request a narrow correction preserving one-action alternating initiative, accepted paths, strict commitment and hidden next intent. Acceptance requires runnable delivery/failure/restart, actual input, action/phase and information evidence, correct-layer repair and unaffected behaviour. Reusing the method means deriving these cases; importing AP, pulse, forecast or showcase board constants fails. This brief does not establish broad hidden-information game quality or network support.

## 7. Source → behaviour → test mapping

| Reviewed evidence | Operational consequence | Cases |
|---|---|---|
| TTF-01–03/07/09; TTS-02/03 with P4 qualifications | TT-R1/R4: opportunity, spatial/objective dependencies and bounded alternative coverage | TT-A02, A08–09, A11–12 |
| TTF-04/08/10; contrasting TTS-01/02 | TT-R1/R2: proposal versus commitment, truthful scoped information, conditional undo | TT-A03–04, A09–11 |
| TTF-05–06/11; TTS-04 | TT-R3/R5: deliberate order, phase guards, removal and session-safe delayed work | TT-A03, A05–07, A11 |
| TTF-08/10/12; TTS-05–08 | TT-R5: complete navigation/information and evidence collection with appropriate limits | TT-A04, A07–08, A10 |
| P1 qualification, P4 boundaries, canonical contract and TTF-09–12 | TT-R6, optional activation, fair comparison and installed closure | TT-A01, A09–13 |

P4 standing and source dependence remain applicable. These mappings do not convert practitioner methods into empirical universals. Source records support development and revision; they are not required at runtime.

## 8. Implementation plan and separate status

Stage 20 consumes this profile after the installed core vertical exists. Implement concise skill-local guidance and only justified scenario helpers. Run P6 actual showcase/fixtures, then P7 matched comparison, independent reuse, intent preservation, negative cases and clean external installation. Record real outputs, conditions, failures and corrections. Consuming skills need local operational guidance without cross-pack inheritance, source books or creator dependencies.

| Dimension | Current state | Evidence required to advance |
|---|---|---|
| Research | **P1–P5 complete** for bounded initial scope after this checkpoint's verification | Revisit affected assumptions when scope/evidence changes |
| Implementation | **Planned** | Actual packaged guidance, fixtures and playable outputs |
| Evaluation | **Not run** | Showcase, faults/repair, fair comparison, distinct reuse and installed-use evidence |
| Readiness | **Not ready** | Useful specialist effect without unacceptable regressions and actual proof gates |

## 9. Conformance verification

Re-read bootstrap 17.7 and canonical P5; inspect all 21 required fields, six operational rules, six responsibility mappings and thirteen cases. The full prompt fixes an executable project while keeping its parameters out of pack defaults. The additional brief changes mechanics, information and turn structure. Neither is presented as an executed result.

| Requirement | Evidence | Verification | Result |
|---|---|---|---|
| Scope / qualification, activation, precedence | Section 1 | Bounded recurring need; explicit selection; stronger authority and non-use preserved | PASS |
| Production rules, mechanical/systemic effects, core effects, what remains core | Sections 2–3 | Six operational rules and six core mappings with observable consequences | PASS |
| Hard/soft constraints, qualified methods, cross-domain boundaries | Section 3 | Project policies separated from obligations and engineering/craft ownership | PASS |
| Specialised evaluation, negative/incompatibility cases, smallest repair | Sections 2/4 | Thirteen falsifiable cases cover defects, intentional traits, preservation and limitations | PASS |
| Showcase brief, exact prompt, independent reuse | Sections 5–6 | Substantive equal-task prompt and distinct alternating-initiative fixture; no actual-play claim | PASS |
| Source-to-behaviour-to-test mapping | Section 7 | Five groups cover all six rules and thirteen cases with retained evidence limits | PASS |
| Research, implementation, evaluation, readiness | Section 8 | Four separate states; P6/P7 actual proof required | PASS |

**P5: COMPLETE.** Tactical Turn-based P1–P5 research is complete after this checkpoint is committed and remotely verified. Overall Stage 12 awaits the domain authoring contract and final conformance audit. Neither selected pack is implemented or ready.
