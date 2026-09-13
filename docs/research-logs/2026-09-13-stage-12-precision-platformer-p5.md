# Precision Platformer: P5 production profile and evaluation design

**Date / profile revision:** 2026-09-13 / `PP-01`  
**Pack:** `precision-platformer`  
**Accepted research:** [P1](2026-09-13-stage-12-precision-platformer-p1.md), [P2](2026-09-13-stage-12-precision-platformer-p2.md), [P3](2026-09-13-stage-12-precision-platformer-p3.md), [P4](2026-09-13-stage-12-precision-platformer-p4.md).  
**Core baseline:** `10101f5e01661d6622964e2c0a030be7c7c1ad05`, specified, not implemented or measured.

P5 specifies bounded operational guidance and falsifiable evaluation before implementation. This is the design source for a later skill-local pack resource; consumers must not need this research log or the source books at runtime.

## 1. Scope, activation and precedence

Use for local continuous 2D run/jump games in which repeated spatial execution is central. The reusable contribution is a workflow connecting movement response, legal action opportunities, geometric demand, available information, attempted traversal and causal repair. This detail would be irrelevant as a default for many core tasks. P7 must still demonstrate useful behaviour beyond core or ordinary project instructions; research qualification alone does not prove a pack is warranted.

Activate when the user or the consuming project's selected-pack configuration requests `precision-platformer`. Record the profile revision and task scope. A side-view screenshot, a genre word in unrelated text or the presence of one jump does not select it. If an explicit request fits only part of the profile, apply that bounded part and disclose the limits. Do not introduce new verbs or physics requirements for a design-only request.

Precedence is **explicit project instructions → approved / locked game decisions → selected pack → core defaults**. First identify the current instructions, accepted decisions and authorised change scope. A newly explicit instruction can authorise a revision; a pack default cannot. Surface an unresolved conflict with locked work and obtain only the missing authority, after doing the useful non-conflicting work. Do not ask again for authority already supplied. Record a deliberate override and affected checks rather than silently replacing accepted behaviour.

Do not use this profile to design turn-based tactics, an autonomous simulation, art style or a network synchronisation protocol. Initial qualification does not include mobile, gamepad, 3D cameras, wall jumps, dashes or moving-platform rules. Such additions need project-specific evidence or later profile qualification; the word platformer does not imply them.

## 2. Production rules and expected effects

| Rule | Required production behaviour | Mechanical / artefact effect |
|---|---|---|
| **PP-R1: establish the movement contract** | Inspect the existing controller before proposing a new one. Record each supported input/action, units, coordinate frame, legal states, response over time, contact and jump/release semantics, outcome/reset, tested runtime and accepted values/ranges. Explicitly record whether buffering or edge tolerance exists | State/rule and movement records identify what legal input should do. Published constants are not borrowed as defaults; existing accepted behaviour is retained |
| **PP-R2: measure the relevant envelope** | Use the smallest runnable setup that exercises the question. Observe movement under declared start/input/timing conditions; separate continuous response from input acknowledgement. Check boundary ordering and any tolerance's eligibility, expiry, consumption and reset | Measured rise/fall, travel or stopping evidence supports the needed route cases. A formula may guide the setup but cannot replace actual runtime evidence |
| **PP-R3: bind demand and information to movement** | For each required route under review, identify approach, takeoff, destination, clearance, relevant state/verbs and view/cue information. Check the executable route before repeating geometry or replacing accepted content | The layout's demands are traceable to controller behaviour and player information. Optional routes remain optional; unavailable verbs cannot quietly become prerequisites |
| **PP-R4: separate attempts from experience claims** | Derive focused cases for the disputed boundary and complete-route cases for approach/outcome/retry. Use actual game input for player-path checks and label privileged simulation/setup separately. Use suitable human sessions for recognition, difficulty or feel claims | Results identify build, setup, input, observed outcome, assistance and limitations. Automated completion cannot produce a human verdict |
| **PP-R5: inspect access and timing conditions** | Check declared input alternatives, simultaneous/held/rapid demands, available cue channels, instruction/retry controls and relevant pause/resume/cadence conditions. Test a selected assist/movement variant separately from the default | Controls and evidence do not silently depend on one render rate or one unreported assist. An alternative setting must preserve its declared route and outcome rules; no global accessibility certificate follows |
| **PP-R6: diagnose and preserve** | Reproduce the finding, compare controller/contact, geometry, information and test/runtime explanations, then change the smallest adequate responsible unit within authority. Recheck affected accepted routes and repeated outcomes/reset | A repair record identifies cause/evidence, changed unit, preserved decisions and rerun results. An entire level or approved controller is not regenerated to conceal a local collider/cue defect |

The rules can be entered at the relevant point for existing work. A supplied level can precede a controller proposal; PP-R2/R3 reconcile their relationship before acceptance. A review task does not mutate the game. A narrow repair does not restart the whole production process.

## 3. Core-skill effects, constraints and handoffs

| Core responsibility | Pack effect | What remains core |
|---|---|---|
| game-development: define-game-thesis / design-mechanic / model-system | Clarify intended execution, movement/contact and recovery choices; use PP-R1 | Thesis authority, rules, state, evidence and scope; no required platformer template for all games |
| game-development: build-playable-proof / integrate-content | Couple controller measurements to representative routes and content/cue agreements using PP-R2–R3 | Adequate fidelity, real execution, delivery/integration contracts and complete bounded session |
| game-development: repair-gameplay / prepare-playable-build | Preserve movement-dependent routes and test relevant timing/reset in the resulting build | Change authority, engineering delegation, release constraints and build identity |
| game-evaluate: validate-gameplay / evaluate-player-experience / evaluate-accessibility / evaluate-performance / diagnose-gameplay | Derive platformer boundary, landing/view, attempt and smallest-repair cases; apply PP-R4–R6 | Independent assessment, source limits, technical versus human/target evidence and no unrequested game changes |
| game-evaluate: evaluate-balance | Consider spatial/motor demand and recovery costs when that is the actual balance question | Question-led comparison; no mandatory economy or universal difficulty score |
| game-extension-pack-creator: author-extension-pack | Consume completed P1–P5 and implement the bounded guidance/fixtures at the owning stage | Domain authoring workflow, corpus permission/access, comparison and installation gates; no separate P-stage runtime command hierarchy |

**Hard constraints:** obey accepted movement and geometry; declare legal action/tolerance/outcome/reset rules and units; keep runtime/build/input/assist conditions in evidence; preserve critical information and applicable project access requirements; do not present proposed or automated evidence as human/target proof. An exact conflict or unavailable required evidence stays visible.

**Soft defaults and qualified methods:** a small controller/route sandbox, simple geometry, a focused diagnostic restart and a limited change are useful starting points. Buffering, edge tolerance, variable jump height, visual effects, instant shipped retries and any particular update method are optional choices, not mandatory features. Project intent can prefer a different response or recovery cost. Acceptability depends on relevant evidence and authority.

Engineering owns native input/physics, collision implementation, browser/engine tools and optimisation. Art/environment owns finish and asset craft; animation/audio owns presentation craft. The pack supplies gameplay dimensions, collision/cue meaning and integration criteria. It does not build a universal controller framework or require a content provider. Core works independently with no pack; the optional creator is not a consumer dependency.

## 4. Falsifiable acceptance cases

These cases are designed now and **not executed**. Project-specific numeric values belong to each fixture. A pass requires actual evidence appropriate to its claim; a missing human or target condition remains untested. Structural validation, rule correctness, specialist usefulness, preservation and player quality remain separate dimensions.

| ID | Setup / expected effect | Failure and acceptance criterion |
|---|---|---|
| **PP-A01 Activation / non-use** | Run the same bounded production request with pack requested, absent, and an unrelated side-view art request | Requested run applies relevant PP-R rules; absent run remains useful core and does not claim pack activation; art request does not grow a controller or game scope |
| **PP-A02 Declared response** | For the showcase, record horizontal motion and jumping from a known grounded start, then attempted airborne input | Runtime agrees with declared movement, legal jump and single-use input semantics; measured envelope and actual input trace exist. A named constant or rendered image alone fails |
| **PP-A03 Boundary opportunity** | Showcase uses an 80 ms landing-input buffer, no edge tolerance. Controlled cases exercise a press 60 ms before landing, 100 ms before landing, and a consumed press carried into the next landing | Inside case triggers once at eligible landing; expired and consumed cases do not trigger. A native controlled-time check may pin exact boundaries; a separate real-input case verifies the binding. A script calling jump directly cannot stand in for the input path |
| **PP-A04 Route / content regression** | Establish required routes; introduce a local collider/landing-width defect without changing visible identity or accepted movement | Diagnosis identifies the affected geometry/contact relationship. Repair restores that route and preserves controller values, other routes and unchanged content; raising jump strength or rebuilding the level without cause fails |
| **PP-A05 View / cue diagnosis** | Present a mechanically legal route whose required hazard/landing information is obscured in the player view | Inspection reports the information defect; any human-comprehension conclusion names real evidence or remains pending. Repair targets cue/framing/obstruction before unrelated physics; shape/text and sound-off checks follow declared channels |
| **PP-A06 Repeated outcome / reset** | Exercise failure, restart, goal, restart, with held and queued input at transition where relevant | Each outcome resolves once according to rules; restart restores declared state and clears stale action/contact/outcome. New play requires the declared fresh action; old buffer cannot leak into the next attempt |
| **PP-A07 Timing conditions** | Compare movement under the declared normal and varied callback conditions, then interruption/resume | Elapsed-time behaviour remains within fixture acceptance or an explicit limitation is reported. Resume cannot consume a long hidden interval as an uncontrolled jump/teleport. Simulated cadence checks are labelled separately from actual browser/target measurements |
| **PP-A08 Precedence / intentional trait** | Give an accepted no-buffer controller or deliberately costly recovery, then request a narrow cue repair with the pack active | Preserve those intentional rules; do not add forgiveness or checkpoints as a presumed improvement. Reject genuine stale-input/reset or unavailable-information defects even when difficulty is intentional. Explain any authority conflict without silently changing stronger decisions |
| **PP-A09 Independent reuse** | Use the low-ceiling brief in section 6 with different response, geometry and failure cause | Method derives release/clearance and approach cases for this controller, rather than importing showcase constants, buffer or room layout. Actual output and rerun evidence are required |
| **PP-A10 Fair differential** | Run section 5's substantive prompt in matched fresh core-only and packed contexts; add a core-plus-ordinary-instructions arm if packaging value is unclear | Compare movement-to-route reasoning, boundary-fault detection, responsible repair and preservation without withholding requirements from core. Metadata or longer prose is not improvement. Record negative/inconclusive results and costs |
| **PP-A11 Installed resource closure** | Install selected production/evaluation skills and this pack into a clean external consumer; perform a bounded specialised task | Necessary operational guidance resolves locally without source checkout, research logs, source books or creator skill. Local repository success alone fails this installation claim |
| **PP-A12 Scope / incompatibility** | Request networked platform physics, a 3D camera or simultaneous conflicting selected-pack defaults | Identify the unproved/competing responsibility and apply only supported, non-conflicting guidance. No claimed network/mobile/3D readiness or automatic pack precedence between equal conflicting defaults |

PP-A10 should examine actual task outcomes, identified defects, repair scope and regression results, with effort/context costs when reliably recorded. Do not invent weighted quality scores. One favourable run is limited evidence, and an inconclusive result must remain inconclusive. P7 decides whether to qualify, revise, defer or reject ready-catalogue status.

## 5. Showcase brief and exact prompt

**Showcase: Copper Steps.** A small original fixed-view run/jump session tests measured landing opportunities and a complete retry loop. It needs a safe introduction, three required jumps, an optional narrower route, hazards and a goal. The parameters below are **project instructions for this example**, not pack defaults. Primary evaluation is route/contact correctness, evidence of measurement, single-use buffer/reset, view/cue information and preserved movement after a local repair. Human feel and first-use recognition are separate pending evidence.

For the packed run, select `precision-platformer` in the consuming project's pack configuration before issuing the prompt. For core-only, leave pack selection empty. All other task text, inputs, available tools and constraints remain identical. Record both exact effective contexts and revisions.

```text
Build Copper Steps, an original small local browser platformer, using the installed game-development capability and any pack explicitly selected in this project's configuration.

Make one fixed-view 2D session with a safe start, three required jumps, one optional narrower route, visible hazards, a visible goal, win/failure feedback and a keyboard-operable restart. Use simple original shapes; do not require downloaded art, accounts, remote services or networking. Include readable instructions and shape/text information so hazards and outcomes do not depend only on colour or sound.

The project movement contract is: world units independent of rendered CSS size; horizontal speed 220 units/second with immediate left/right response; gravity 1440 units/second squared; jump starts with upward velocity 480 units/second from eligible ground; no extra airborne jump and no variable jump height. Include an 80 ms input buffer: a fresh jump press at most 80 ms before eligible landing may trigger exactly once on landing. A consumed or expired press cannot trigger again. Do not add edge tolerance, dash or wall jump. Restart clears queued input, outcome and contact state. Keep these decisions stable while fixing level or cue defects.

Choose and record player dimensions, coordinates and geometry so the required routes work with those rules. Establish movement and landing evidence in the actual runnable game before repeating the geometry. Check normal and boundary actions, complete failure/goal/restart, required routes, input binding and relevant timing/interruption behaviour. State tested runtime, inputs and limits. Keep privileged simulation checks distinct from real browser input, and do not invent human playtest findings.

Provide the playable project, exact local run instructions, a compact movement/route record and observed verification results. Identify any remaining player-experience or target-device questions honestly. Do not publish or release the game externally as part of this task.
```

After generation, an evaluator introduces PP-A04's bounded fault in a disposable fixture copy and requests a repair under the accepted movement contract. The generation prompt does not reveal the fault location. Preserve pre-fault, faulty and repaired outputs and observed checks. This tests diagnosis rather than merely following a prompt naming the answer.

## 6. Independent reuse brief / fixture

**Low Ceiling Traverse** is a separate small game, not a reskin of Copper Steps. Start from a different controller: horizontal acceleration and stopping, a variable-height jump whose early release reduces upward motion, and **no jump buffer or edge tolerance**. The supplied level includes a low ceiling, an approach requiring stopping control, an optional high alcove and a required exit. Failure restarts the current short room; the ordinary restart control is untimed.

The consuming project will pin the actual units, dimensions, response parameters and accepted routes before the repair task, using its own measured baseline. That setup is a distinct authoring output, not copied showcase physics. Introduce a cue/ceiling-clearance fault that causes a short held/released-input sequence to be misunderstood or blocked; retain its actual reproduction. Request diagnosis and the smallest adequate repair while preserving the accepted controller and optional-route identity.

Reuse acceptance requires an actual runnable output, measured held/released jump and stopping cases, approach/ceiling checks, correct layer diagnosis, preserved no-buffer semantics and repeated reset. The evaluator must distinguish a mechanical obstruction from an unobserved human interpretation claim. It fails reuse if the agent pastes Copper Steps's constant-speed movement, buffer, layout or measurements into this game. Scope still covers the run/jump grammar; no new dash, wall, moving-platform or network capability is implied.

## 7. Source → behaviour → test mapping

| Reviewed evidence | Operational rule | Falsifiable cases |
|---|---|---|
| PPF-01–02; PPS-01, 03–04 qualified by P4 | PP-R1–R2: declared mapping, measured response and explicit boundary opportunities | PP-A02–03, A07–08 |
| PPF-03, 05, 07, 11 | PP-R3 / R6: movement-dependent geometry, content preservation and causal repair | PP-A04, A08–10 |
| PPF-04, 09; PPS-05–08 with scope limits | PP-R4–R5: view/information, input demands and evidence appropriate to the claim | PP-A05, A07–09 |
| PPF-06, 08, 10; PPS-02 as a contrasting intent | PP-R1 / R4: integrated outcome/retry and representative proof without universal recovery cost | PP-A02, A06, A08 |
| P1 qualification, P4 uncertainty and canonical pack contract | Optional activation, fair comparison, bounded composition and installed closure | PP-A01, A10–12 |

Mappings retain evidence strength from P4. They do not mean each method has independent empirical support. Traceability assists review and future revision; research documents are not runtime dependencies.

## 8. Implementation plan and separate status

At Stage 20, after the installed core vertical exists, implement concise skill-local operational guidance and only the scenario helpers justified by actual tests. Necessary instructions must ship with each selected consumer skill or an explicitly supported local pack mechanism; do not introduce cross-skill/root-research dependencies. Preserve the exact prompts, actual outputs, failures and corrections. Run P6 implementation/local proof and P7 fair comparison, independent reuse, precedence/non-use and clean external installation before judging readiness.

| Dimension | Current state | Evidence needed to advance |
|---|---|---|
| Research | **P1–P5 complete** for initial bounded qualification after this checkpoint's verification | Revisit only affected findings if later scope or contrary evidence changes decisions |
| Implementation | **Planned; no operational pack installed** | Actual packaged guidance and behaviour fixtures in Stage 20 |
| Evaluation | **Not run** | Showcase, faults/repairs, matched core comparison, independent reuse and external install records |
| Readiness | **Not ready** | Useful intended specialised effect without unacceptable regression, appropriate limitations and actual proof gates |

## 9. Conformance verification

Re-read bootstrap 17.7, canonical P5 and the family pack contract, then inspected the actual profile and prompts. This table accounts for all 21 required fields; the twelve cases are pre-implementation designs.

| Requirement | Evidence | Verification | Result |
|---|---|---|---|
| Scope / qualification, activation, precedence | Section 1 | Bounded need, explicit selection, non-use and stronger-instruction handling | PASS |
| Production rules, mechanical/systemic effects, core-skill effects, what remains core | Sections 2–3 | Six operational rules with observable effects and six responsibility mappings | PASS |
| Hard/soft constraints, qualified methods, cross-domain boundaries | Section 3 | Conditional tolerance/retry/timing methods separated from obligations and craft/engineering ownership | PASS |
| Specialised evaluation, negative/incompatibility cases, smallest repair | Sections 2 and 4 | Twelve falsifiable cases include intent preservation, genuine defects, diagnosis, scope and regression | PASS |
| Showcase brief, exact copyable generation prompt, independent reuse | Sections 5–6 | Complete prompt, equal comparison task and distinct controller/geometry/failure fixture; no executed-output claim | PASS |
| Source-to-behaviour-to-test mapping | Section 7 | Five mapping groups cover all six rules and twelve cases | PASS |
| Research, implementation, evaluation and readiness status | Section 8 | Four separate explicit states; actual production proof reserved for P6/P7 | PASS |

**P5: COMPLETE.** Precision Platformer P1–P5 research is complete after this checkpoint is committed and remotely verified. Overall Stage 12 remains in progress; Tactical Turn-based P1 is next. No installed or ready-to-use pack is claimed.
