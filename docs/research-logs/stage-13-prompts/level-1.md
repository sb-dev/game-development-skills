# Level 1: three single-mechanic example designs

**State:** Designed in Stage 13; all execution, tuning comparisons and repair results remain not run. Each fenced block is a complete independent generation prompt. See the [curriculum contract](../../contracts/progressive-examples.md).

## E01 — Latch Room

**Production question:** Does a pushed object drive a gate's actual state consistently across movement, invalid pushes and restart?  
**Distinct evidence:** Discrete spatial/rule semantics, a small state oracle, feedback and reset repair. No continuous physics or AI required.  
**Stable decisions after baseline:** Board identity, push eligibility, gate dependency and input alternatives.  
**Fault:** Gate remains open after restart because the previous plate state survives; repair the responsible reset/derivation boundary.

```text
Create Latch Room in a fresh local consumer project using the installed game-development skill, with no Extension Pack selected. Make a small original keyboard-playable browser room in which the player pushes one crate onto a pressure plate to open a gate and reach an exit. Use a bounded grid, a safe starting position and simple original shapes/text. Choose and record a compact solvable layout whose exit really requires the gate; do not make a decorative gate the player can bypass.

Movement is one cardinal grid step per fresh action. A crate moves only when the next cell is free and in bounds; wall, occupied and out-of-bounds pushes change nothing. The gate is open exactly while the crate occupies the plate, and its collision/passability and visible state must agree. Restart restores all initial positions, plate/gate state and outcome. Explain the rules on screen, identify player/crate/plate/gate without colour alone, and make start/restart and the complete interaction keyboard operable with visible focus. Offer pointer buttons as an additional route without replacing the keyboard proof.

Implement and run the actual game through its normal browser input. Preserve a compact rule/state record, an authoritative read-only state observation for tests and observed checks for normal push, blocked push, plate enter/leave, gate crossing, win and two restarts. Do a bounded basic tuning comparison of two feedback durations chosen and recorded before testing; observe cue overlap/clarity mechanically and treat human readability as untested unless someone actually participates. Select a duration within that declared range and record the reason.

After accepting the working baseline, create a disposable fault variant in which gate state survives restart. Retain the baseline and faulty version. Reproduce the fault, diagnose the responsible state/reset boundary, and repair it while preserving the accepted board, push rules and input paths. Run the failing case and unaffected push/win cases again. Label deliberate fault injection and do not claim blind diagnosis.

Provide runnable source, exact dependency and local run commands, the complete prompt, baseline/fault/repair identities, actual test output and a player-view capture. Distinguish real input from privileged fixture setup and do not invent tests, people or device support. Keep the implementation game-specific; no shared engine, service, account or external publication.
```

## E02 — Rebound Lab

**Production question:** Can the player deliberately change a moving ball's rebound while input, contact, feedback and time basis agree?  
**Distinct evidence:** Continuous response, contact timing, basic tuning and single-effect collision.  
**Stable decisions:** Accepted speed/angle response, target positions, one impact per contact and keyboard controls.  
**Fault:** A ball resting across a contact boundary scores more than once; repair contact eligibility rather than increasing cooldown or rebuilding the arena.

```text
Build Rebound Lab in a fresh local browser project using installed game-development and no selected Extension Pack. Make an original small single-screen mechanic toy: a ball travels through a bounded field, and the player rotates a deflector to aim one rebound at a visible target. A launch control starts a trial; the trial ends on target contact or a visible miss boundary and can restart. Use a small game-specific implementation and ordinary declared runtime dependencies, not a new physics framework.

Record world units, time basis, ball radius/speed, deflector geometry, legal rotation range, contact response, target and miss/reset rules. Left/right keys rotate the deflector; provide labelled on-screen equivalents. One contact may create one rebound and one target hit, never repeated reward from overlapping frames. Choose a simple response rule and explain it; plausibility is not a claim of real-world physics. Restart clears velocity, contact eligibility, score/outcome and held/queued trial input.

Run the actual browser game. Measure the deflector response to a declared held-key sequence and the resulting ball trajectory/contact at the runtime's observed times. Keep a controlled-time rule test distinct from real browser input. Compare two rotation rates within an explicitly recorded tuning range, checking achievable aim, input acknowledgement and overshoot; choose and preserve one based on actual evidence without inventing a human feel verdict. Check launch, boundary rotation, contact, target, miss, repeated overlap and two resets with small automated tests. Inspect instructions, target/result cues without sound or colour dependence and keyboard focus through trial transitions.

Keep a valid baseline, introduce a disclosed disposable variant that scores repeatedly while the ball overlaps the target, reproduce it and repair the contact/effect-consumption boundary. Preserve the chosen rotation/speed values, target geometry and unrelated rebound behaviour. Retain failed and repaired traces and rerun affected cases; a long arbitrary cooldown that hides repeated scoring is not sufficient diagnosis.

Deliver playable source, complete prompt, exact local run/dependency commands, rule/tuning record, actual input/state/test evidence and representative player-view capture. Report timing and runtime limits; no universal responsiveness, mobile or human-quality claim, accounts, paid services or external publication.
```

## E03 — Depth Dock

**Production question:** Does a genuine 3D object's visible position and collision/alignment state support a small docking action?  
**Distinct evidence:** Three-dimensional coordinates, camera/depth cues, input alternatives and source-to-runtime transform repair.  
**Stable decisions:** Accepted docking volume, spatial axis convention, camera and movement step.  
**Fault:** Visual Z transform and authoritative docking/collision position diverge.

```text
Create Depth Dock as an original small local browser 3D mechanic using installed game-development with no Extension Pack. Use a suitable existing 3D renderer/library with recorded dependency version and local build/run instructions. Render a real 3D scene with depth, an inspectable camera, one movable solid and one docking volume; a flat canvas illustration with a fake depth label is insufficient. Keep geometry and materials simple and original. This is a bounded manipulation proof, not an engine or asset pipeline.

Let the player choose X, Y or Z movement and move the solid in discrete steps with keyboard controls and equivalent labelled pointer buttons. Show the selected axis, coordinates and target relationship using text/shape as well as colour. Include an obstruction and bounded world limits. A move into forbidden volume is rejected without a partial state change. Docking succeeds only when the actual solid is fully within the target volume under a recorded tolerance. Supply a camera reset and a game restart; reset restores position, outcome and selection consistently.

Choose and record units, axis directions, solid/target bounds, tolerance and camera conditions. Compare two movement step sizes within a declared range, checking target reachability and input effort using actual observed actions; preserve the chosen step for repair. Execute normal, boundary, obstruction, docking and repeated-reset cases through real browser input and inspect authoritative scene transforms plus player-view captures from relevant views. Automated geometry checks must observe the actual scene state, not an unrelated test model. Report any missing depth-comprehension or device evidence honestly.

After accepting the valid baseline, retain a disposable fault version with a mismatched visual versus authoritative Z transform. Reproduce the docking discrepancy, inspect source/configuration/runtime responsibility and make the smallest correction at the transform binding. Preserve target dimensions, tolerance, accepted step, camera and unaffected axes. Rerun the failing depth case and normal/blocked/docking/reset regressions. Disclose the injected fault; do not pretend this is blind evaluation.

Deliver runnable source and declared dependencies, the exact prompt, rule/tuning record, actual browser/test/capture results, baseline/fault/repair versions and limitations. Keep controls keyboard operable with visible focus. Do not claim installed 3D support beyond the path actually run, or human usability from screenshots. No accounts, remote assets, paid service or external publication.
```
