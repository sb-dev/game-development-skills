# 05 — Game Development Customisation and Extension Packs Specification

**Status:** Canonical pack contract; operational implementations/proof pending  
**Version / date:** 1.0 / 2026-09-13  
**Companions:** [system](01-game-development-skills-system-spec.md), [repository](03-game-development-skills-repository-and-contracts-spec.md), [evaluation](04-testing-and-benchmark-spec.md), [curated catalogue](06-game-development-extension-pack-catalogue.md).  
**Provenance:** Completed Stage 12 authoring contract and per-pack P1–P5, qualified by Stage 14 evaluation gates.

Customisation means explicit consumer choices and optional domain-owned specialist guidance. A project setting is not automatically an Extension Pack. This document defines the complete authoring, research, selection, packaging, precedence and readiness contract; the independently evolving catalogue owns actual entries and evidence. It does not introduce a shared runtime or claim implementation from research.

## 1. Qualification and catalogue ownership

A Game Development Extension Pack is optional reusable gameplay-production knowledge that materially changes decisions for a coherent specialisation. It must be useful across projects, irrelevant as a universal core default, observable in playable/artefact effects and distinguishable from competent core behaviour through evaluation. A project brief, engine adapter, provider configuration or adjacent-domain style does not qualify by itself.

Classify a requested need before authoring: existing pack covers it → reuse/refine; existing core covers it → use core; broad missing gameplay responsibility → core-improvement candidate; one game's values/layout → project instructions; reusable specialised grammar → research a pack; insufficient distinction/evidence → defer/reject. Catalogue size follows complementary coverage, not the number of books. Preserve existing approved identities and evidence until an explicit migration decision permits change.

The initial researched selection is `precision-platformer` (`PP-01`) and `tactical-turn-based` (`TT-01`). Their P5 profiles own operational rules and predefined cases. Both have P1–P5 research complete, implementation planned, evaluation not run and readiness not ready. Other curation ideas remain planned or deferred. This specification owns domain semantics; specification 06 owns the actual catalogue and evidence state. Neither a listed entry nor a directory proves quality.

Art style belongs to visual/environment/character production; narrative genre/prose to Narrative Production; music genre to Music Production; cinematic language to Video Production. Gameplay supplies rules, state, timing and integration agreements. Networked-cooperative and other production-constraint proposals must distinguish specialised gameplay grammar from software architecture, synchronisation, backend and security responsibilities.

## 2. Production profile

Use a concise Markdown profile with stable identity/revision and these semantic fields; no universal metadata database or executable pack language is required:

| Field group | Required content |
|---|---|
| Qualification | Scope, use/non-use, recurring need, core revision/status, expected behavioural difference, existing/core/project alternatives and catalogue contribution |
| Selection and authority | Explicit activation, precedence, conflict handling, relevant core skills and what remains core |
| Production grammar | Operational rules, mechanical/systemic and artefact effects, hard constraints, soft defaults, qualified methods and assumptions |
| Preservation and boundaries | Approved work that must remain stable, smallest-sufficient repair, incompatible/negative cases and cross-domain handoffs |
| Evaluation design | Falsifiable specialist cases defined before execution, intended traits to retain and actual defects to reject; source → behaviour → test mapping |
| Demonstration and reuse | Realistic showcase brief, exact copyable prompt, expected behaviour/priorities, distinct additional brief/fixture and actual outputs when run |
| Provenance and status | Five-book identity/contribution and examined-source limits; supporting/challenging evidence; separate research, implementation, evaluation, installation and readiness records |

Dimensions are chosen for the specialisation. Movement response, action opportunities, information policy or resolution structure can matter; a compulsory genre/perspective/format taxonomy would add no evidence. Hard constraints protect declared rules, authority and evidence integrity. Defaults remain defeasible. A method's standing—supported finding, contextual method, heuristic, disputed claim or unresolved question—remains separate from retaining, adapting or rejecting it.

## 3. Selection, precedence and loading

An explicit user request or ordinary consuming-project instruction selects pack identities and optional revisions. For example, a project may state `Game Development packs: precision-platformer (PP-01)` in its existing instructions. This is a readable selection convention, not a mandatory file format, CLI, parser or new project service. No selection means core behaviour. Directory presence, a screenshot or an incidental genre word does not activate a pack.

The consuming skill reads its local pack index, resolves explicitly selected identities/revisions, then loads only relevant local guidance. Record the effective selection and supported scope in the task's evidence. An absent or incompatible requested revision is a concrete capability mismatch; do useful supported work and report it without silently substituting a pack. No source-repository fetch or creator installation is required to use a bundled pack.

Precedence is **explicit project instructions → approved / locked game decisions → selected Game Development pack → core defaults**. An explicit authorised change can revise approved work; a pack default cannot. Preserve the strongest applicable instruction and document deliberate overrides with affected checks. Resolve actual missing authority only; never re-request permission already granted. Equal conflicting selected-pack defaults require a project decision, not arbitrary loading order. Non-conflicting parts remain usable.

Use only the relevant operation for the request. A narrow evaluation does not author a whole game; a repair does not repeat adequate research; a design request does not imply production. Other families interpret their own packs; no cross-domain pack interpreter or Pactwright runtime is introduced.

## 4. Self-contained packaging

The initial packaging design bundles optional Markdown profiles inside each consuming skill under `references/packs/`, with a local index describing identity, applicability, revision, status and the corresponding file. `game-development` and `game-evaluate` each carry their required operational guidance. Their core instructions remain useful when no profile is selected. The standard Skills CLI installs the selected skill with its local resources; selecting a pack is a separate project instruction, not a new installation executable.

Necessary invariants can be repeated across independently installable consumers. Tailor routing to the skill's production or evaluation responsibility and validate both copies against the accepted profile; do not require one skill to read a sibling skill's files. Avoid copying full research logs. Source citations establish provenance, but source books, central family documents and research logs are never required to apply the operational method.

`game-extension-pack-creator` carries its own authoring contract, research/permission rules and proof requirements. It may inspect installed profiles or project-supplied evidence when requested, but ordinary pack use does not depend on it. Its authoring outputs include the relevant consuming-skill resources and domain-owned fixtures/showcase evidence. No new generic pack-authoring subsystem is needed.

At implementation, run resource/link/metadata checks, then use the selected profiles in actual tasks. Local packaging validation and a clean external consumer installation are distinct gates. For the latter, exclude the source checkout, source books, research logs and unselected sibling skills from required access. Validate each intended selective installation and actual supported operation. Record installed revision/resource identity and limitations.

## 5. Domain-owned authoring workflow

The existing named operation **`author-extension-pack`** in **`game-extension-pack-creator`** owns authoring. Accept new research, bounded revision, implementation or evaluation scope. Read the exact core/catalogue/pack/evidence revisions; direct entry at a later phase is permitted after reviewing adequate prerequisite evidence. A small correction revisits affected findings and tests without rerunning unrelated research or the entire bootstrap.

| Work phase | Required work and output | Completion gate |
|---|---|---|
| Catalogue / P1 | Compare relevant alternatives and complementary coverage; define all eleven specialisation/baseline fields against the real production need | Reusable bounded delta, competent core baseline, preserved work and evaluation questions explicit |
| P2 selection | Build a pack-specific coverage map and broader candidate comparison; select exactly five distinct justified books; record editions, origin, access, intended/actual reading, reuse and permission decisions | Exactly five selected; required approvals resolved; access needs and gaps explicit |
| P3 extraction | Meaningfully examine all five or review adequate original direct-source findings with edition, location, scope, assumptions and pack applicability; add direct reading where needed | Source → specialist decision → effect → criterion → failure/repair; overlap/conflicts reconciled, core/pack/project distinct |
| P4 challenge | Independently test material claims, contrary/alternative methods, failure conditions and missing responsibilities; check current technical practices with primary sources | Evidence-qualified guidance; source dependence and standing separate from disposition; unsupported certainty removed |
| P5 profile | Specify section 2 fields, operational rules, exact prompt, distinct reuse and falsifiable criteria | Testable bounded behaviour before implementation, separate evidence states |
| P6 implementation | Use this domain authoring capability to package local guidance, justified helpers/fixtures and showcase; execute the production path and preserve actual outputs/provenance | Implemented, inspectable output and local checks; a prompt alone or unavailable execution cannot pass |
| P7 evaluation / installation | Matched competent core-versus-pack production, behavioural/negative/preservation checks, distinct reuse and clean external install | Useful intended effect without unacceptable regressions; honest limitations and readiness/catalogue decision |

P2, P3 and P4 each require substantive separate committed research records. Do not compress them into a bibliography in P5 or create mandatory runtime commands named after the P stages. Persist detailed development evidence in domain research logs and maintain an accurate catalogue index.

Source rules apply per corpus. Clarify which supplied works are intended for the pack. Keep user-provided corpus members unless their removal, replacement or demotion is explicitly authorised; a proposed substitution records the coverage gain/loss, evidence, alternatives and decision. Declined means retain; unanswered means pending. Empty slots can be filled without an extra approval. More than five supplied foundational books requires an explicit selection decision rather than silently changing the count. Preserve corpus revisions and affected downstream evidence.

Access is `full text available`, `relevant excerpts available`, `secondary material only` or `unavailable`, separately from actual examination. Contents pages, descriptions, summaries and model memory cannot satisfy extraction. Sufficient excerpts must expose the intended method's context/limits. Five means distinct works, not editions, articles or games, and does not mean five new books. Reviewed reuse must earn its pack-specific contribution; shared lineage is not independent corroboration. A selected book may contribute little after examination without invented guidance.

Publish independently expressed synthesis and bibliographic/reading scope. Do not commit supplied books, substantial copied text, private source paths or credentials without appropriate publication authority. Relevant games demonstrate observed techniques, not causal commercial success or universal desirability. An inaccessible required contribution blocks its extraction; uncertainty about an ideal design value is qualified, not fabricated into a rule.

## 6. Behavioural evidence and readiness

Predefine changes expected from activation, what must not regress, intentional traits to preserve and real defects still to reject. Test activation/non-activation, specialised effects, precedence, domain boundaries, incompatible cases and smallest repair. Keep deterministic correctness, command behaviour, specialist usefulness, access, human experience and target performance visible rather than collapsing them into one score.

Run core-only and core-plus-pack on the **same substantive prompt**, constraints and comparable tools/resources in fresh contexts where available. Record exact effective prompts, core/pack revisions, model/tool versions when relevant, settings, resources, deviations, actual outputs and evaluator limits. A core-plus-ordinary-instructions arm can test whether packaging adds useful reuse. Do not give the packed arm more task requirements or credit pack-name mentions. Preserve negative and inconclusive results; one favourable run does not establish general superiority.

The showcase needs actual generation, run evidence and inspectable outputs. The independent brief/fixture must change meaningful mechanics, conditions or failure cause to test transfer beyond the showcase recipe. Repair evidence preserves pre-fault, faulty and corrected states and affected-case reruns. A scripted policy cannot supply human understanding/depth evidence; a simulated clock cannot silently become measured target-input latency.

| State dimension | Meaning |
|---|---|
| Research | Planned, partial or P1–P5 complete for an identified scope/revision |
| Implementation | Planned or implemented with inspectable packaged guidance/output |
| Evaluation | Not run, passed within declared scope, failed or inconclusive, with actual cases and conditions |
| Installation | Not run or observed result for identified clean consumer and selected resources |
| Readiness | Not ready / unproven / ready for explicitly demonstrated scope; requires actual production, useful comparison, reuse, behaviour and installation gates |

If the intended benefit is absent or regressions unacceptable, refine and rerun affected cases or retain an unproven/deferred entry. Do not call it ready merely to close authoring. Readiness does not promote repository maturity. Public release, merging or other externally consequential actions retain the user's applicable authority.

## 7. Revision and migration

Retain stable pack identity, old prompts, accepted outputs and evidence history. A changed source finding triggers an impact review of consuming rules and tests; unchanged evidence remains valid only within its recorded scope. Update both independent consumer copies when their common guidance changes and check for stale revisions. A parameter change confined to one game belongs in project instructions unless it exposes a reusable method correction. Catalogue merge/retirement and altered installed interfaces need an explicit migration decision preserving approved work; no silent recertification follows a documentation edit.

## 8. Initial gameplay dimensions and core-skill effects

The initial catalogue has two researched profiles, not five mandatory categories. Precision Platformer relates movement response/action boundaries to executable envelopes, spatial demand/information, attempts and causal repair. Tactical Turn-based relates available information to legal actions/opportunity cost, commitment, declared resolution and changed tactical situations. Their parameter values, particular boards/levels, recovery, visibility and timing policies remain project decisions.

Production uses applicable specialist rules when defining/modeling behaviour, building/integrating a proof and repairing/preparing a candidate. Evaluation uses the same qualified semantics to select relevant checks and distinguish intentional traits from defects; it retains independent review authority. The creator consumes completed source and evaluation evidence for a bounded revision. Core thesis, adequate proof, basic correctness/access, evidence integrity, native tooling, scope/authority and preservation remain useful without any pack.

Do not import continuous platformer tolerances into tactical phases or force full outcome certainty into intentionally uncertain tactics. Multiple selected profiles compose only where their actual rules do not conflict; explicit project and approved decisions govern. Unsupported 3D/network/input/genre variants need their own qualification, not a name-based compatibility claim. Specification 06 contains the full six-rule profiles, constraints, exact prompts, reuse briefs and source-to-test mappings.

## 9. Conformance and proof gates

A complete researched entry has all eleven P1 fields; exactly five justified works in P2 with origin/edition/access/examined scope and resolved applicable permission; adequate direct or reviewed direct-source P3 examination for every intended contribution; independent P4 support/contrary/gap assessment with standing separate from disposition; and all twenty-one P5 fields including operational rules, tests, exact prompt, distinct reuse and separate states. P2/P3/P4 each retain substantive independent committed records.

An implemented entry additionally carries local operational guidance and actual showcase/fixture outputs. Every implemented pack must execute its exact-prompt showcase, distinct additional reuse, behavioural/precedence cases and fair competent-core comparison. Structural checks, exact prompts or one favourable sample do not establish reusable benefit. Retain negative/inconclusive results, effort/context costs when measured and evaluator/target/human limits. Specification 04 preserves all twelve Precision and thirteen Tactical cases and the six clean-installation scenarios.

Ready-to-use status requires useful intended specialist effect without unacceptable regressions, actual reuse, authority/negative/repair behaviour and clean external installed use. A failed or inconclusive benefit requires refinement/retest or an explicitly unproven/deferred entry; do not claim ready for catalogue symmetry or bootstrap progress. Publication, interface migration and maturity changes remain separate authorised evidence-based decisions.
