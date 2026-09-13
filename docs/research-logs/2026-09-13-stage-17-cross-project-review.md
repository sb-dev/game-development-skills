# Stage 17 — Cross-project review

**Date / branch:** 2026-09-13 / `feat/bootstrap-2`. **Game input:** Six canonical specifications and public design through `cc6d1645bae184ec18c0b84dfa113a9346a3d88f`.

## 1. Directly examined evidence and limits

Reviewed the game architecture only after its domain research and specifications existed. Retrieved current `main` revisions, pinned each source and examined the actual sections below. These are independent domain repositories with implemented instruction surfaces and documented contracts. This review did **not** execute their production, provider, benchmark or installation workflows. Similar wording can reflect shared family adoption, so it is not independent empirical confirmation of effectiveness.

| Evidence ID / source revision | Material actually examined | Observation / limit |
|---|---|---|
| V / Video `5e82bb9a188d3cfc83cae0979cc39737011411b9` | [README](https://github.com/sb-dev/video-production-skills/blob/5e82bb9a188d3cfc83cae0979cc39737011411b9/README.md) in full at Stage 16; [production skill](https://github.com/sb-dev/video-production-skills/blob/5e82bb9a188d3cfc83cae0979cc39737011411b9/skills/video-production/SKILL.md) adequacy, approval, state, promotion, refinement, retry, evaluation and boundaries; [evaluator](https://github.com/sb-dev/video-production-skills/blob/5e82bb9a188d3cfc83cae0979cc39737011411b9/skills/video-evaluate/SKILL.md) evidence, classification, repair and boundaries; [creator](https://github.com/sb-dev/video-production-skills/blob/5e82bb9a188d3cfc83cae0979cc39737011411b9/skills/video-extension-pack-creator/SKILL.md) in full; [repository spec](https://github.com/sb-dev/video-production-skills/blob/5e82bb9a188d3cfc83cae0979cc39737011411b9/docs/03-creative-skills-repository-and-contracts-spec.md) §§5, 13, 16–17, 19 | Shot/reference/edit/master responsibilities; distinct decision state; local correction; source-only and measured evidence separated. Public progression has four examples per level. No media-quality or actual-install claim verified here |
| N / Narrative `3215a7d89556b770ac3f88e93e6fd46804c5c791` | [README](https://github.com/sb-dev/narrative-production-skills/blob/3215a7d89556b770ac3f88e93e6fd46804c5c791/README.md) creative control, installation, all progressive trios, packs, benchmarks and status; [develop](https://github.com/sb-dev/narrative-production-skills/blob/3215a7d89556b770ac3f88e93e6fd46804c5c791/skills/narrative-develop/SKILL.md), [revise](https://github.com/sb-dev/narrative-production-skills/blob/3215a7d89556b770ac3f88e93e6fd46804c5c791/skills/narrative-revise/SKILL.md), [pack creator](https://github.com/sb-dev/narrative-production-skills/blob/3215a7d89556b770ac3f88e93e6fd46804c5c791/skills/narrative-pack-create/SKILL.md) in full; [repository spec](https://github.com/sb-dev/narrative-production-skills/blob/3215a7d89556b770ac3f88e93e6fd46804c5c791/docs/03-creative-skills-repository-and-contracts-spec.md) §§3, 16, 22–23, 30, 34 | Concept/beat/scene/prose, planned versus canon, bounded revision and independent installed commands. README still has publication placeholders and says its installation gate is pending. Its stated 42 benchmark definitions are not remeasured here |
| M / Music `aa3933bc87f54a48ec018bb868bf6385b340db22` | [README](https://github.com/sb-dev/music-production-skills/blob/aa3933bc87f54a48ec018bb868bf6385b340db22/README.md) approval/cost, installation, all trios, packs, checks and status; [compose](https://github.com/sb-dev/music-production-skills/blob/aa3933bc87f54a48ec018bb868bf6385b340db22/skills/music-compose/SKILL.md), [produce](https://github.com/sb-dev/music-production-skills/blob/aa3933bc87f54a48ec018bb868bf6385b340db22/skills/music-produce/SKILL.md), [evaluate](https://github.com/sb-dev/music-production-skills/blob/aa3933bc87f54a48ec018bb868bf6385b340db22/skills/music-evaluate/SKILL.md), [pack author](https://github.com/sb-dev/music-production-skills/blob/aa3933bc87f54a48ec018bb868bf6385b340db22/skills/music-pack-author/SKILL.md) in full; [repository spec](https://github.com/sb-dev/music-production-skills/blob/aa3933bc87f54a48ec018bb868bf6385b340db22/docs/03-creative-skills-repository-and-contracts-spec.md) §§6, 16, 21–22, 24 | MIDI/text versus audible production, component lineage, region repair, real versus separated stems, technical versus musical judgement. Semantic baseline remains unmeasured and clean installation pending in the inspected public state |
| F / Family `20979e0c68ac4b37433374df7fe10ceb2e7ee69a` | Four specifications read in full: [system v1.0](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/specs/01-production-skills-family-system.md), [project v1.3](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/specs/02-production-skills-project-contract.md), [evaluation/packs v1.2](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/specs/03-production-skills-evaluation-and-extension-packs.md), [integration v1.1](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/specs/04-cross-domain-orchestration-and-integration.md) | Already standardises principles, six semantic specs, fifteen complementary examples, local closure, separate evidence/readiness and domain-owned packs; forbids mandatory shared runtime, universal workflow/score and consumer-project centralisation |
| G / Game through Stage 16 | [System](../01-game-development-skills-system-spec.md), [workflows](../02-game-development-skills-workflows-and-artifacts-spec.md), [repository](../03-game-development-skills-repository-and-contracts-spec.md), [evaluation](../04-testing-and-benchmark-spec.md), [pack contract](../05-game-development-customisation-packs-spec.md), [catalogue](../06-game-development-extension-pack-catalogue.md) | Domain-first source/challenge decisions and complete design; only explicitly historical synthetic checks executed. Operational installed game proof is still pending |

The source IDs in each record below refer to these exact pinned links and examined sections. They are reusable provenance references, not runtime dependencies.

## 2. Common-need candidates

These ten records satisfy the required candidate shape. Recommendations mostly reaffirm existing family principles/contracts. They do not request changes to the family or certify independent production benefit. Stage 23 must revisit actual game evidence before proposing any new shared implementation.

```yaml
candidate: adequate-representation-before-commitment
observed_in: [game-development, narrative-production, music-production, video-production]
common_need: Resolve the material uncertainty before paying for a higher-fidelity commitment.
domain_variations:
  game-development: A rule table cannot prove input timing; a controller or greybox must retain disputed play variables.
  narrative-production: Concept, beat or scene-card work tests story logic before full prose when adequate.
  music-production: A motif, MIDI or partial demo answers different questions from finished audio.
  video-production: References, storyboard or motion prototype precede the relevant costly shot.
evidence: [G-system-section-7, N-develop-Core-rules, M-compose-Draft, V-production-Core-principle, F-system-5.2]
recommendation: family principle
not_recommended: [one universal cheap artefact, fixed fidelity ladder, equating low price with adequate evidence]
```

```yaml
candidate: explicit-decision-authority-at-material-commitment
observed_in: [game-development, narrative-production, music-production, video-production]
common_need: Distinguish a choice for continued work from authority for downstream reliance.
domain_variations:
  game-development: Already granted implementation and tuning authority persists; only affected material decisions reopen.
  narrative-production: Selected direction differs from approved character, ending or canon constraints.
  music-production: Component selection, approval and locking constrain different downstream choices.
  video-production: Current skill specifies human creative approvals and recorded approver before expensive named milestones.
evidence: [G-workflows-sections-2-and-6, N-README-Creative-control, M-compose-Selection-and-decision-state, V-production-Creative-approval, F-system-5.3]
recommendation: family principle
not_recommended: [same approval state machine everywhere, repeated permission already granted, copying another domain's retry cap]
```

```yaml
candidate: meaningful-local-alternatives
observed_in: [game-development, narrative-production, music-production]
common_need: Compare materially different options only around a real unresolved decision.
domain_variations:
  game-development: Compare rule, control, encounter or tuning options using an adequate playable or modelled question.
  narrative-production: Alternatives differ in story logic; branch at the smallest creative unit containing uncertainty.
  music-production: Compare hooks or arrangements and retain component source lineage without generating whole songs needlessly.
evidence: [G-workflows-sections-3-6-and-10, N-develop-Operating-sequence-and-Core-rules, M-compose-Draft-and-Selection]
recommendation: family principle
not_recommended: [mandatory candidate count, cosmetic variants as evidence, universal candidate database]
```

```yaml
candidate: preserve-accepted-decisions-and-provenance
observed_in: [game-development, narrative-production, music-production, video-production]
common_need: Carry accepted upstream constraints and source identity through refinement without silent replacement.
domain_variations:
  game-development: Preserve rule values, routes, state ownership and source/import/runtime relationships.
  narrative-production: Preserve character/world/ending decisions and distinguish planned events from canon.
  music-production: Preserve selected melody, lyric, harmony and section lineage; final composition differs from final master.
  video-production: Use the most specific approved reference or plan and retain the selected parent.
evidence: [G-workflows-sections-2-8-and-10, N-revise-Approved-decisions, M-compose-Refine, V-production-Promotion-and-Refine, F-system-5.4]
recommendation: family principle
not_recommended: [shared artefact graph, mandatory global lifecycle folders, automatic transitive regeneration]
```

```yaml
candidate: causal-repair-and-affected-regression
observed_in: [game-development, narrative-production, music-production, video-production]
common_need: Diagnose the responsible relationship, make the smallest sufficient correction and verify preserved neighbours.
domain_variations:
  game-development: Separate rule, state, input, cue, integration, strategy and collection causes; retain faulty and repaired runtime cases.
  narrative-production: Repair prose, scene design, beat or premise according to cause rather than default page-one rewrite.
  music-production: Repair composition, arrangement, performance or audio boundary before full-track regeneration.
  video-production: Repair reference, shot plan, generated clip or edit according to evidence.
evidence: [G-workflows-section-10, G-evaluation-section-9, N-revise-Root-cause-targeting, M-produce-Refine, V-evaluate-Failure-diagnosis, F-system-5.5]
recommendation: family principle
not_recommended: [smallest textual diff as sufficient cause, one correction-unit hierarchy, guaranteed diagnosis from two failures]
```

```yaml
candidate: explicit-pack-precedence
observed_in: [game-development, narrative-production, music-production, video-production]
common_need: Optional specialisation must respect explicit project intent and accepted work while changing relevant defaults.
domain_variations:
  game-development: Bundled local profiles preserve intentional no-buffer, costly recovery, strict commitment or hidden information.
  narrative-production: A medium/genre profile must preserve accepted story decisions and downstream boundaries.
  music-production: Peer profiles affect applicable composition, production and evaluation while preserving locked music.
  video-production: Peer packs affect relevant visual/editorial/delivery grammar without reopening approved video artefacts.
evidence: [G-pack-contract-section-3, N-pack-creator-Precedence, M-compose-Optional-customisation-pack, V-pack-creator-Precedence, F-packs-section-12]
recommendation: project contract
not_recommended: [universal pack interpreter, genre-word auto-activation, shared loading order resolving semantic conflicts]
```

```yaml
candidate: domain-owned-pack-authoring-and-proof
observed_in: [game-development, narrative-production, music-production, video-production]
common_need: Qualify reusable behavioural difference, check existing alternatives and keep a showcase, tests and honest readiness evidence.
domain_variations:
  game-development: New corpus research uses separate P1-P5 and actual P6-P7 showcase, fair comparison, reuse and installation gates.
  narrative-production: Creator translates medium, genre, style and optional voice into story/continuity effects and evals.
  music-production: Author translates composition, arrangement, delivery and use context without owning audio generation.
  video-production: Creator packages cinematographic/editorial grammar and structural validation; generated output remains separate.
evidence: [G-pack-contract-sections-5-6-and-9, N-pack-creator, M-pack-author, V-pack-creator, F-packs-sections-11-17]
recommendation: project contract
not_recommended: [one skill per adjective, forcing all packs into five labels, silently recertifying older catalogues under new research rules]
```

```yaml
candidate: complementary-progressive-public-productions
observed_in: [game-development, narrative-production, music-production, video-production]
common_need: Expose growing production responsibility through reproducible substantial examples with exact prompts and actual evidence state.
domain_variations:
  game-development: Mechanic, loop, slice, scale and complete thesis; five trios with real input and human requirements where relevant.
  narrative-production: Story, continuity, screenplay, episodic work and audiovisual handoff; five genre-diverse trios.
  music-production: Controlled output, selection, full production, repair and cross-domain work; five trios.
  video-production: Shot, sequence, commercial, short and campaign; inspected README currently has four per level.
evidence: [G-evaluation-section-15, N-README-Learn-by-producing, M-README-Learn-by-producing, V-README-Learn-by-producing, F-project-section-7]
recommendation: project contract
not_recommended: [same level semantics, examples counted from prompts alone, cosmetic migration of other repositories without their own decision]
```

```yaml
candidate: claim-appropriate-layered-evaluation
observed_in: [game-development, narrative-production, music-production, video-production]
common_need: Preserve distinct correctness, specialist quality, behaviour, repair and measurement conclusions with valid evidence.
domain_variations:
  game-development: Rule execution, strategic interaction, human feel/comprehension, accessibility and target performance need different observations.
  narrative-production: Continuity, prose/story judgement and revision behaviour are separate; command and orchestration contracts can fail independently.
  music-production: MIDI, audible musical judgement, technical QC, stems and local repair have different evidence limits.
  video-production: Technical, creative, continuity and generation findings route to different owners; eval definitions do not fill benchmark baselines.
evidence: [G-evaluation-sections-1-12, N-repository-sections-22-23, M-evaluate, V-repository-section-13, F-packs-sections-2-8-and-20]
recommendation: family principle
not_recommended: [universal quality score, file validity as feel, same rubric for every representation, manual cases labelled executed]
```

```yaml
candidate: clean-selective-installation-and-local-closure
observed_in: [game-development, narrative-production, music-production, video-production]
common_need: Required operational resources must survive independent installation and actual use outside the source checkout.
domain_variations:
  game-development: Production alone must build/play/evaluate/repair; evaluator and creator have separate clean tasks; selected profiles are bundled locally.
  narrative-production: Private commands and references ship with each selected skill; project-native story input is valid.
  music-production: Skill-local scripts/dependencies and separately declared provider/native prerequisites must be present for the requested operation.
  video-production: Commands, references, scripts and eval resources ship locally; copy-mode tests expose hidden source and sibling assumptions.
evidence: [G-repository-sections-4-and-6, N-repository-sections-3-and-34, M-repository-sections-6-21-22, V-repository-sections-5-and-19, F-project-section-13]
recommendation: project contract
not_recommended: [new installer, shared mandatory runtime package, successful copy as end-to-end proof, treating other repositories' pending installs as passed]
```

## 3. Game-specific responsibilities stay local

| Concept | Game-owned distinction | Permitted handoff / common boundary |
|---|---|---|
| Game feel | Continuous control, spatial/feedback context and actual situated human response | Ask animation/audio/UI for delivered cues; no family-wide feel rubric |
| Mechanics / dynamics | Eligibility, state/resource effects and emergent interaction over time | Explicit requirements and native engineering implementation, no universal rule DSL |
| Playtesting | Actual participants, tasks, prior exposure, assistance, observations and accounts | Evidence provenance is common; humans cannot be replaced by static media QC |
| Balance | Strategies, opportunity, resource/progression context and incomplete coverage | Keep question and measurement limits; no cross-domain score or exchange rate |
| Levels / encounters | Action-dependent space, knowledge, challenge, camera and final placement | Source environment properties and integrated acceptance, not one mandatory scene schema |
| Runtime simulation | Time basis, authoritative state, update order, reset/save and peer semantics | Existing engine tools; no family simulator or graph |
| Input behaviour | Fresh/held/queued inputs, eligibility, contact and full task navigation | Native input/capture tooling and UI contracts; not a provider abstraction |
| Performance budgets | Actual target, workload, tail/stalls and measurement endpoint | Engineering/profiling handoff; no universal frame, latency or memory target |

Narrative character intent does not own game execution; Music's adaptive-game-score does not own a game audio runtime; a valid 3D asset does not establish traversability. Project-specific bindings, requirements, selected profiles and evidence remain with the consuming game.

## 4. Differences, rejected transfers and decision

The current family contract already contains the useful common principles; no family patch is necessary to scaffold this repository. The game design conforms semantically without copying another domain’s skill count, private command folders, lifecycle fields, provider credential requirements or TypeScript version.

Video’s current strict human creative gates and two-attempt shot rule are local policy. They do not create missing permission where this user has already authorised the bootstrap, nor establish a general statistical claim that a second failure proves the diagnosis wrong. Narrative/Music public installation placeholders and pending gates are observed limitations, not failures repaired by changing those repositories here. Older pack authoring surfaces do not by themselves satisfy the later family Seed → Five → Challenge update; that requires their explicit migration decision, not silent recertification.

Retain existing game decisions: three installable responsibilities, fourteen operations expressed by local guidance, bundled optional pack profiles, browser-first concrete execution, independent human/runtime proof and game-owned tests. No new shared package, schema, router, orchestrator, approval state machine or abstract quality framework is justified. Record these candidates for Stage 23 and reassess using actual game production evidence.

## 5. Original Stage 17 conformance

Re-read original section 22 and inspected the completed record against the exact requested dimensions and record fields.

| Requirement | Evidence | Verification | Result |
|---|---|---|---|
| Review after independent game architecture | Game Stage 15–16 revisions; section 1 | Comparison occurs after complete domain research/specification; no architecture retrofitted from a provider/family template | PASS |
| Compare Video, Narrative, Music and current family | Section 1 pinned sources | All four repositories resolved at current main; four family specs read fully; concrete skill/public/install/eval sections examined | PASS |
| All ten reproduced-need topics | Section 2 | Ten complete records cover adequacy, commitment, alternatives, preservation, repair, precedence, authoring, progression, layered eval and external installation | PASS |
| Required abstraction record fields | Ten fenced YAML records | Every record has candidate, observed_in, common_need, domain_variations, evidence, recommendation and not_recommended; all include game plus another domain | PASS |
| All eight game-local concepts | Section 3 | Feel, mechanics/dynamics, playtesting, balance, levels/encounters, simulation, input and performance have explicit local semantics/boundaries | PASS |
| Evidence strength and meaningful variations | Sections 1–4 | Implemented instructions/documentation separated from unexecuted production/install; shared source lineage and older migration limits explicit | PASS |
| Exit: useful candidates without convenience family changes | Sections 2 and 4 | Existing principles/contracts reaffirmed; no family or other-domain mutation and no universal infrastructure introduced | PASS |

**Stage 17: COMPLETE.** Stage 18 scaffolding follows the verified stage commit. No blocker remains for that authorised work.
