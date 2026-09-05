# AGENTS.md

Do not change this file unless the user explicitly requests it.

## Workflow

Work toward the user's stated completion criterion. Local lemmas, finite
checks, failed approaches and commits are checkpoints, not substitutes for
the requested theorem. Continue through plausible repairs and alternative
global constructions; report unresolved gaps and comparative significance
honestly. Do not force a preferred route when the evidence favours another.

For research decisions, consult `RESEARCH_LEDGER.md`, `active/INDEX.md` and
the designated technical frontier. Reuse that orientation until relevant
state changes; revisit history only for a disputed dependency or claim.
For a narrow edit, read the affected material and its dependencies. Load
skills and additional sources only when they serve the task.

Continue authorized local research, reversible edits and relevant checks
without repeated permission requests or a routine stop after the first
result. Existing user authorization governs commits, merging and publishing;
this file does not authorize contacting others or using Clawpatch.

Use short-lived `feature/`, `fix/`, `experiment/` or `refactor/` branches.
Keep commits focused and merge or retire branches promptly. Keep code and
verification scripts simple, deterministic and proportionate to the task.

## Research records

- `RESEARCH_LEDGER.md` is the sole current status authority. Its opening
  frontier has three levels: global obligation, conditional refinement and
  immediate laboratory. Put detailed residues in designated technical
  frontiers; archive superseded snapshots without appending live updates to
  frozen history. Do not create competing ledgers or proof spines.
- `active/INDEX.md` is navigation: exactly one primary target, direct proved
  inputs and immediate barriers, then concise links to conditional routes.
  A direct input is invoked without another listed theorem in between.
  Keep history, transitive dependencies and case analysis out of this map.
  Every live direction must be reachable through it; classify unlisted
  files before treating them as current proof work.
- Develop drafts and scripts in `active/`; promote written proofs with
  adjacent audits to `results/`; put explicit counterexamples in `barriers/`.
  Preserve superseded work and provenance in `archive/`, not by deletion.
- Keep `README.md` stable: change it for scope, navigation, durable results,
  claim policy or repository structure, not the latest local lemma.

Update the ledger and designated technical frontier when the mathematical
position changes. Update the active index only when its targets or direct
dependencies change. In `tools/research_manifest.toml`, `active = true`
must match the primary target and direct inputs/barriers in that index;
other claims and richer relations may remain inactive for retrieval.
When the primary target changes, update the ledger frontier, active index,
manifest flags and direct target relations together in one commit.

Generated context packs aid retrieval; they do not establish status or a
complete dependency closure. Consult the authoritative records before using
them. Discovery connections require separate review and promotion to typed
manifest relations before becoming proof dependencies.

## Mathematical claims and audits

Label substantive claims with their applicable statuses: written proof;
separate internal audit; computer-assisted finite result; conjectural target;
recorded negative finding / route nonclosure (not a counterexample); or
barrier/counterexample to an intermediate claim.

- State exact hypotheses, quantifiers and conclusion before each proof.
  For reductions, verify all retained roots, colouring constraints and
  branch-set ownership, closure of the induction class, a genuinely
  decreasing well-founded parameter and a valid lift.
- Inspect primary statements and hypotheses before applying literature;
  cite the exact theorem or lemma where practical. Distinguish external
  input from new deductions and substantiate novelty or significance claims.
- Independent audits should attack the strongest inference, not merely
  exposition. Internal audits are not external peer review. Promotion to
  `results/` requires an adjacent `_audit.md`; unaudited drafts and legacy
  files remain explicitly unaudited regardless of directory placement.
- New or materially updated audits must identify the exact revision or
  content hash, verdict and unresolved assumptions or gaps. Bring older
  audits to this standard before reusing their results in current proofs.
  If audited mathematics changes, update or replace its audit and rerun
  recorded hash checks; never silently alter the audited source.
- Record material failed mechanisms in the designated frontier: hypotheses,
  attempted inference, first unsupported step, what remains possible and
  the smallest repair needed. Summarize in the ledger only when standing
  changes; archive when frozen. A barrier requires an explicit construction
  refuting a stated claim, with its unaffected scope made clear.

Use established graph-theoretic terminology and define necessary shorthand.
Distinguish subgraphs from explicit minor models; specify boundary colouring
partitions, preserved branch sets and exact chromatic conditions instead of
unexplained metaphors or labels. Retain historical filenames and hashes,
using descriptive link text.

## Computation and verification

Run Python through `uv run python3`; dependencies belong in `pyproject.toml`
and `uv.lock` and are managed with `uv add` / `uv sync`. If the cache is
unwritable, prefix commands with `UV_CACHE_DIR=/tmp/hadwiger-k7-uv-cache`.
Use plain Python only for an explicitly documented dependency-free script
whose standard-library-only trust boundary is being checked.

Finite checks establish only their stated finite conclusions unless a
written reduction proves more. State bounds prominently, retain generating
scripts and checkable certificates where practical, and test new encodings
against known positive and negative examples before promotion. Retain an
independent checker when feasible. Document invocation and expected output;
keep bulk data out of Git unless essential and reasonably sized.

For changes to research records, proofs, instructions or index tooling, run
`uv run python3 tools/research_index.py check` and
`uv run python3 tools/research_index.py report`, then inspect the regenerated
target context pack. Run affected mathematical verifiers when their claims,
inputs or implementations change. Once the relevant checks pass, repeat or
broaden them only for a new change, failure or unresolved concern.

## Commit hygiene

Before committing, inspect staged paths and check changed documentation's
links and formatting. Do not add root-level research files beyond the
documented structure. Exclude `.codex/`, runtimes, caches, credentials,
personal data, device-specific paths, non-redistributable third-party
material and unrelated or unclassified files from commits.
