# Game Thesis Contract

**Version:** 1.0  
**Defined by:** [Stage 3 research and verification](../research-logs/2026-09-13-stage-03-player-experience-and-game-thesis.md)

## Purpose and scope

A game thesis states what the player should do, understand and experience, the proposed play that might produce it, and the conditions under which that proposition will be evaluated. It directs the next prototype and constrains downstream decisions. Acceptance records a production decision; it does not prove that players have the intended experience.

Keep the active thesis to a short brief. Use the copyable form below, or equivalent project-native fields. Link detailed mechanics, content inventories, research plans and evidence rather than embedding a Game Design Document. A new field earns space only if it changes a current design, evidence or commitment decision.

## Copyable form

```markdown
# <Working title> — <thesis ID>@<revision>
State: <draft | accepted | rejected | superseded>
Owner: <designated project decision owner>
Scope: <whole bounded game | named subsystem / experience>
Authority: <existing instruction / decision reference; none if unaccepted>

## Players and context
<Intended players, relevant prior knowledge/access needs, play context and
session shape. Mark assumptions instead of claiming a researched audience.>

## Intended play
<Player role/fantasy when useful; core verbs; meaningful challenge or choice;
what players should learn/master. Name the desired experience as a hypothesis.
State a proposed differentiator only when it matters; otherwise say none claimed.>

## Loop and outcomes
<Situation → player choice/action → consequence → changed situation.
State risk/reward, session entry/end, success/failure or open-ended outcomes,
and retry/reset/continuation intent. Give the causal idea, not full state code.>

## Conditions and boundaries
<Relevant viewpoint, inputs, platform/runtime constraints and social mode.
Include access requirements and non-goals. Label each unsettled condition
proposed or unknown, with the decision it could block; use N/A with a reason.>

## Evidence questions
| Claim / question | Evidence kind and proposed check | Contrary result / next decision |
|---|---|---|
| <specific claim> | <rule/runtime; observed behaviour; participant experience; external> | <what would challenge it and what to reconsider> |

Evidence status: <unexamined | evidence linked with conditions and limitations>
Next proof: <question, minimum behaviour/conditions needed, permitted omissions>

## Commitment
<Accepted constraints and decision references; authorised next work and bounds;
unresolved material questions; link to alternatives/history. Do not invent approval.>
```

## Meaning of the fields

**Players/context** must be precise enough to choose relevant evidence conditions. “Everyone” is not a useful sampling or access assumption. Record first-use knowledge, available controls and material needs without presuming that one demographic label explains ability.

**Intended play** connects verbs and consequences to the intended challenge, mastery and experience. “Fun”, “immersive” or a list of features alone cannot direct a prototype. Fiction is optional for an abstract game; a novelty claim is optional and must remain proposed until supported.

**Loop/outcomes** identifies a repeated opportunity for action and how its consequences affect the next choice. A brief must explain what counts as reaching an outcome, ending or continuing the session. Open-ended play can state that it has no win/fail condition; it still needs entry, meaningful consequences and a clear way to stop or resume. Do not invent progression, saving or competition when the game does not need them.

**Conditions/boundaries** distinguish requirements from hypotheses. A proposed camera, control or platform is not an approved commitment. Non-spatial play can mark a moving camera inapplicable while still naming its information/view constraints. State social mode explicitly so a local prototype is not mistaken for network evidence. Access requirements influence the prototype from the outset.

**Evidence questions** keep implementation claims, player behaviour and experience separate:

| Kind | Example of a scoped statement | What could support it |
|---|---|---|
| Rule/runtime | Choosing to wait consumes the stated opportunity cost. | Specified rule cases and an identified runtime when implementation is claimed. |
| Observed behaviour | New players distinguish waiting from committing without assistance in this encounter. | Relevant participant observations with prior knowledge, conditions and interventions recorded. Completion alone may not establish understanding. |
| Experience aspiration | Choosing when to commit should create anticipation and agency. | Appropriately scoped human play observations/accounts; treat behaviour measures as supporting evidence. An aspiration is not an achieved result. |
| External effect | Play improves a real-world ability or changes real-world behaviour. | Appropriate external-domain evidence and study design. In-game success is insufficient. |

Each material question needs a possible contrary observation and a decision it informs. A threshold, device target or sample size may be proposed for a later test; do not report it as measured or universal. If the means to evaluate a claim is unknown, say so and restrict the commitment accordingly. Detailed study design belongs to the evaluation model.

## Review and downstream use

Before a prototype, check that an implementer can identify the player action, consequence, outcome and disputed assumption; an evaluator can identify the claim, conditions and possible contrary result; and the proposed proof includes the behaviour necessary to investigate that claim. Unresolved details may remain only if they do not undermine that investigation and their omission is explicit.

Before substantial downstream content production, the designated owner must have accepted the selected direction and all material constraints on that work: audience/context, core activity and intended experience, applicable platform/input/view/social constraints, scope/non-goals, access requirements and relevant evidence/quality commitments. Record the exact accepted revision, scope, rationale, evidence, limitations and authorised work. Do not lock every tuning value or every detail of a future game.

A draft can direct reversible exploration already authorised by the project. It cannot silently replace an accepted baseline or authorise expensive expansion. Routine changes within approved ranges retain their existing authority. A material change to an accepted dependency requires the charter's reopen decision: evidence and reason, affected consumers, proposed revision, owner approval and affected re-evaluation. Rejected ideas do not become rules through quotation or reuse.

## Alternatives and active state

Use a stable thesis/alternative identity and a revision. The project must identify which revision is active for each declared scope and whether it is an exploratory draft or an accepted production baseline. Downstream work cites that revision.

Preserve rejected or superseded thesis/mechanic alternatives in the project's decision history with a reconstructable snapshot or immutable revision link, parent/competing option, disposition, rationale, available evidence/limitations and decision authority. Store only a short history link in the active thesis; exclude rejected content from active requirements. A mechanic alternative can later link its detailed rule record without expanding this brief.

When a replacement is approved, record the supersession relationship and update the active reference explicitly. Historical evidence remains attached to the version and conditions it tested; acceptance of a replacement does not transfer old results automatically. Contradictory active instructions or a proposed change outside existing authority require the owner's decision before affected work proceeds.
