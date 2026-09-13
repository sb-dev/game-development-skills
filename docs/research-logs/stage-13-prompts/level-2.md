# Level 2: three repeatable-loop example designs

**State:** Designed, not executed. Each requires a real question-led human playtest as well as technical proof. Missing participant evidence must remain a named blocker at execution; an agent or script is not a participant. Each prompt is independent.

## E04 — Spark Run

**Production question:** Does pursuing score create an observable risk/reward loop without rewarding indefinite waiting?  
**Distinct evidence:** Real-time movement, limited-session scoring, pacing, verified session telemetry and first-use observation.  
**Fault / preservation:** Restart mixes the previous attempt's score events into the new run; repair session collection while retaining movement, spawn rules and accepted scoring.

```text
Build Spark Run in a fresh local browser project using installed game-development and game-evaluate, with no pack selected. Make an original two-minute maximum score-attack loop: move a player to collect sparks while avoiding clearly signalled hazards; carrying more sparks raises the potential banked reward but increases a declared risk or movement cost. Banking at a safe depot records score and clears the carried load. Failure or time expiry ends the attempt; restart begins a fresh one. Use original simple shapes and readable text, keyboard movement and keyboard-operable menus/restart.

Choose and record exact movement, spawn, carry/risk, banking, collision and timing rules. Make a reachable goal/challenge/reward/failure loop, with a pause option and critical hazard/outcome information that survives sound-off and colour-independent review. Prevent waiting forever from becoming the best unbounded reward source under the stated scoring rules; do not assume an external retention effect. Establish actual complete score/bank/failure/expiry/retry paths.

Define minimal attempt-local events before collection. Run an active collection policy and a passive policy, state their information and time horizon, and compare real outcomes and pacing indicators. Verify known actions against event counts and session boundaries. Interpret this as bounded balance evidence, not proof of enjoyment. Perform an actual human playtest with a relevant unfamiliar participant: give the neutral task of trying to bank a score, record prior familiarity, assistance, actions and their account of the risk choice separately from your interpretation. If no participant is available, report that exact unmet gate; do not invent a session or call the example complete.

Preserve an accepted baseline, deliberately create a disposable mixed-session score-log fault, reproduce it, diagnose and repair the collection/session boundary. Retain invalid data and rerun restart and known-action collection checks before making balance conclusions. Keep accepted movement, hazard and scoring rules unchanged. Record the disclosed injection and smallest correction.

Provide the complete playable project, exact prompt and local dependency/run commands, compact loop/rule record, actual technical and human evidence with limits, baseline/fault/repair outputs and representative captures. No accounts, paid services, hosted analytics or external publication; do not claim causality, human mastery or untested platform support.
```

## E05 — Quiet Parcel

**Production question:** Can the player understand and exploit declared guard information while completing infiltration, pickup and extraction repeatedly?  
**Distinct evidence:** AI perception/knowledge, patrol and fallback, stealth pacing and human cue comprehension.  
**Fault / preservation:** Guard chases a removed/discarded target and never recovers; repair invalidation/fallback without granting omniscience or rewriting accepted patrol rules.

```text
Create Quiet Parcel as an original small local browser stealth loop using installed game-development and game-evaluate, with no Extension Pack selected. The player enters a small authored space, collects a parcel and returns to an extraction point while a guard patrols. Detection causes a declared chase/search/recovery sequence; capture ends the attempt. Include restart and pause, simple original geometry and clearly distinguishable player, parcel, guard, cover/obstruction and exit. Use keyboard movement and keyboard-operable controls with visible focus.

Choose and record movement, visibility/obstruction, guard knowledge, detection/recovery timing, pickup/extraction and reset semantics before accepting the baseline. The guard may use only its declared perception and remembered information. Show the relevant warning/alert state with readable visual cues and text/symbol support, not colour or sound alone; hidden information stays hidden where intended. Establish a legal infiltration/extraction path and actual detection/capture/retry path through browser input.

Check normal patrol, detection, lost sight, blocked approach, target removal and fallback in the actual running game, with decision and movement observations. Compare a cautious and direct approach under declared starting conditions to inspect pacing and basic risk; scripted success cannot prove fair or understandable stealth. Run a real human playtest with an unfamiliar participant asked to retrieve the parcel without coaching. Retain relevant experience/input context, observed choices and assistance, and their account of detection cues separately from inference. Missing required participant access is an explicit blocker, never a simulated player result.

After retaining a valid baseline, create a disclosed disposable fault where a removed target traps the guard in repeated reselection. Reproduce it and repair the responsible invalidation/fallback behaviour. Preserve perception limits, accepted chase timing, layout and other guard actions; omniscient target selection or disabling the guard does not close the finding. Rerun the failed recovery and normal infiltration/detection/outcome/reset cases.

Deliver playable source, exact prompt, dependency/run instructions, guard/loop and evidence records, actual human/technical results and baseline/fault/repair outputs with captures. Keep engineering implementation native to this small project; no universal AI framework, account, downloaded art, paid service or external publication. Bound all claims to observed conditions.
```

## E06 — Reservoir Shift

**Production question:** Do coupled gather, upgrade and survival costs produce a complete decision loop with valid incentives and comprehensible trade-offs?  
**Distinct evidence:** Discrete economy, feedback, action opportunities, balance-model limits and human choices.  
**Fault / preservation:** Upgrade cost crosses below zero and creates resources; fix the responsible cost rule within the declared contract without unrelated survival retuning.

```text
Build Reservoir Shift in a fresh local browser project using installed game-development and game-evaluate, with no selected pack. Make an original small turn-based resource loop: the player operates a reservoir over a bounded sequence of shifts, chooses to collect water, repair leakage or buy a pump upgrade, and must meet a visible delivery requirement while preserving enough stored water to survive the final shift. An action advances the stated phase; leakage/demand applies in a declared order. Failure and completion lead to a full restart. Use readable tables/diagrams or simple original shapes and fully keyboard-operable actions with visible focus.

Choose and record exact initial stock, source/sink, action costs, upgrade effects, demand schedule, turn order and success/failure rules. Action and upgrade costs must remain non-negative under every legal discount. State what information is visible and show proposed costs and observed consequences without colour-only meaning. Keep the initial scope short enough for repeated complete runs. Establish at least one legal successful strategy and one failed policy in the actual runnable game. Analyse coupled effects and opportunity costs; do not assume equal arithmetic values imply balanced choices.

Use a bounded calculation or simulation for the economy question, verify its represented rules against actual runtime actions, and distinguish model traces from browser input. Compare at least a gather-first and an upgrade-first policy with declared knowledge, horizon and outcomes. Review pacing in decisions/actions and identify dead turns or dominant loops as hypotheses. Run an actual human session with a relevant unfamiliar participant given the neutral delivery goal. Record actions, help and their understanding of costs separately from interpretation. If that person/evidence is unavailable, name the blocked human gate instead of fabricating it.

Retain a working accepted baseline. In a disclosed disposable variant, make repeated upgrade discounts produce a negative cost and resource gain contrary to the non-negative cost contract. Reproduce the exploit, diagnose the specific cost calculation, repair it and rerun both strategy traces, boundary costs, failure/completion and two restarts. Preserve accepted demand, upgrade effect, ordering and unrelated values; changing the survival target to hide the exploit is not repair.

Provide playable source, complete prompt, exact dependencies/local run instructions, system/loop assumptions, actual automated/runtime/model and human evidence, baseline/fault/repair identities and limits. No hosted telemetry, accounts, paid services, external publication or universal balance/learning claims.
```
