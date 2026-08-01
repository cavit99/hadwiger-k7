# Independent computational-reproducibility audit

**Target commit:** `f4705983bd5de40661236943f80be80a5a2c961a`  
**Audit date:** 2026-07-31  
**Auditor role:** independent computational-reproducibility auditor  
**Checkout policy:** read-only; no repository modifications  

---

## 1. Provenance and environment

### 1.1 Source identity

| Check | Result |
|---|---|
| `git rev-parse HEAD` | `f4705983bd5de40661236943f80be80a5a2c961a` |
| `git status --porcelain` | empty (clean) before and after audit |
| Commit subject | `review: retain fan-tree checker and harden verifiers` |
| Commit fetchable | yes (already present; no substitution) |

### 1.2 Required source SHA-256 (all match)

| SHA-256 | Path |
|---|---|
| `6be5e7e36e3cfa899db9577354511a31653c843acc90ad0eb2b02a541384f03e` | `results/hc7_k7minus_exceptional_neighbourhood_completion_verify.py` |
| `e3109f45dabfcfb946a8fb852e011ab6041f3a7a1ca70ca142ce30c63b7d0a87` | `results/hc7_k7minus_nonfull_attachment_reduction_verify.py` |
| `0764c36cb01ff9a4ba1f09b8c6cb3dded40cdb2bd93ed827c9017dd63b68b7cc` | `barriers/hc7_k7minus_nonfull_two_entrance_allocation_barrier_verify.py` |
| `300e8e0d2496dc540887261798c9bd675c298e6d6cfe4a85de221885d3834db4` | `results/hc7_k7minus_overlap_trace_synchronization_verify.py` |
| `3be279d9fd322b8dfee9647156651bc6b32cd83b2a603d9d5acfa64236e3079a` | `results/hc7_k7minus_distinct_miss_fan_tree_completion_verify.py` |
| `a90337234cc340df6c21551532877f192c66b8adc8454011ae906f3ea99c7ce2` | `results/hc7_k7minus_distinct_miss_fan_tree_completion_independent_verify.py` |
| `e82e9733cb71705cd5b7c0832385a305e2fa0e6349d4bf515690a4a52196a28d` | `results/hc7_k7minus_both_full_shore_reduction_verify.py` |
| `a41e5125738eab3cf2180d883f349f73f34c564b8568c8d62763d70173686643` | `barriers/hc7_k7minus_shore_allocation_barrier_verify.py` |

### 1.3 Environment

| Item | Value |
|---|---|
| OS | macOS 26.5.2 (Darwin 25.5.0) |
| Architecture | arm64 (Apple Silicon) |
| Python | CPython 3.14.3 (`/opt/homebrew/opt/python@3.14/bin/python3.14`) |
| nauty | Homebrew formula **2.9.3** |
| geng path | `/opt/homebrew/bin/geng` → `../Cellar/nauty/2.9.3/bin/geng` |
| Python deps used by verifiers | **stdlib only** (no networkx/sage required by these scripts) |
| Available on host (unused by principal runs) | numpy 2.4.2, scipy 1.17.0 |
| Isolation note | Clean git checkout at exact commit; no repo edits. Host environment (not Docker/VM). All runs invoked with fresh processes; catalogue data regenerated via `geng` each time (no reused generated bulk artefacts). |

### 1.4 Research index

```text
python3 tools/research_index.py check   → Research integrity check: PASS (exit 0)
python3 tools/research_index.py report  → exit 0 (writes under .cache/research/; not staged)
```

---

## 2. Principal runs (command-by-command)

All runs used `python3` **without** `-O`. Each command was executed twice.  
Stdout compared byte-for-byte to `expected_stdout` in `tools/research_manifest.toml`.  
Pass-1 vs pass-2 complete stdout: identical for every script (**deterministic**).  
All exit statuses: **0**.

Times and peak RSS from macOS `/usr/bin/time -l` (pass 1). RSS is maximum resident set size.

| # | Command | Exit | Wall (s) | Peak RSS | Observed vs expected | Det. rerun |
|---|---|---:|---:|---:|---|---|
| 1 | `python3 results/hc7_k7minus_exceptional_neighbourhood_completion_verify.py` | 0 | 0.34 | ~18.8 MB | **exact match** | identical |
| 2 | `python3 results/hc7_k7minus_nonfull_attachment_reduction_verify.py` | 0 | 0.10 | ~22.7 MB | **exact match** | identical |
| 3 | `python3 barriers/hc7_k7minus_nonfull_two_entrance_allocation_barrier_verify.py` | 0 | 0.03 | ~16.6 MB | **exact match** | identical |
| 4 | `python3 results/hc7_k7minus_overlap_trace_synchronization_verify.py` | 0 | 0.05 | ~23.3 MB | **exact match** | identical |
| 5 | `python3 results/hc7_k7minus_distinct_miss_fan_tree_completion_verify.py` | 0 | 133.84 | ~88.9 MB | **exact match** | identical (132.79 s) |
| 6 | `python3 results/hc7_k7minus_distinct_miss_fan_tree_completion_independent_verify.py` | 0 | 19.31 | ~67.8 MB | **exact match** | identical (19.48 s) |
| 7 | `python3 results/hc7_k7minus_both_full_shore_reduction_verify.py` | 0 | 0.50 | ~22.7 MB | **exact match** | identical |
| 8 | `python3 barriers/hc7_k7minus_shore_allocation_barrier_verify.py` | 0 | 0.19 | ~19.4 MB | **exact match** | identical |

### 2.1 Observed principal outputs (all matched expected)

**Exceptional neighbourhood**
```text
order-eight graphs=12346; K4-free alpha<=2=3; spanning C8^1,2=3
near-full exterior K7-minus certificates=9/9
```

**One-nonfull**
```text
order-seven graphs=1044 alpha3=578 K4-free=353 sparse=103
diamond-deletion=29 one-nonfull-residue=28
residue sha256=a045e1d21098d0789ea1c549ed00f380ab97df9120335ff24127f9c8a039eacd
edges 5:1 6:4 7:10 8:11 9:2; connectivity 0:9 1:15 2:4; chi3=28
clique-OCT vertex:21 edge:4 none:3
PASS K7-minus one-nonfull boundary census
```

**Nonfull two-entrance barrier**
```text
PASS K7-minus one-nonfull two-entrance allocation barrier
order=13 edges=48 boundary=FCdeG alpha_Nu=3 K4_Nu=no
cuts_le6=4096 connectivity=7 packing=(1,2)
x_boundary_contacts=4 x_F_entrances=2 defect2_allocations=0
chromatic_number=5 explicit_K7_model=yes
scope=violates K7-minus exclusion and seven-chromatic criticality
```

**Overlap-trace**
```text
common_six_survivors=28 digest=9349e3f0c53068bdbdac7068c8fa347ac6658b5231c8abd3dc8e99804118bec9
reflection_demand_distribution=1:1,2:26,3:1
triangular=16 triangle_free=12
unique_demand_one=ECqg(net) unique_demand_three=EQhO(2K3)
matching_parity_languages=PASS
PASS overlap_trace_synchronization_finite_checks
```

**Principal fan-tree**
```text
GREEN: distinct-miss fan-tree completion verified
bridge=0 labelled_valid=1032 valid_orbits=21 quotient_survivor_orbits=3 tree_pair_counts=(2000, 256, 256)
bridge=1 labelled_valid=1113 valid_orbits=109 quotient_survivor_orbits=6 tree_pair_counts=(2000, 2000, 256, 256, 256, 256)
mask_orbit_digest=1d653544a19aed2fac36589f1d113583fe29f7a2af58679e90b574558d9f3203
quotient_certificate_digest=cb251c5518e05b5b1ba79a9149600226777cee5e8677f6bf9a8af90b18b626c3
fan_tree_certificate_digest=5c19a21365f7380afef89b6164dcbee3752db001198cb04aa9270bc4aad33785
```

**Independent fan-tree**
```text
GREEN: independent direct-contraction fan-tree check verified
bridge=0 labelled_valid=1032 valid_orbits=21 quotient_survivor_orbits=3 tree_pair_counts=(2000, 256, 256)
bridge=1 labelled_valid=1113 valid_orbits=109 quotient_survivor_orbits=6 tree_pair_counts=(2000, 2000, 256, 256, 256, 256)
mask_orbit_digest=1d653544a19aed2fac36589f1d113583fe29f7a2af58679e90b574558d9f3203
direct_contraction_certificate_digest=a75aae228f346587a12ab0821c1a1e735b4d25e7ad9181b161a6512bab5c4ce4
```

**Both-full**
```text
order-eight graphs=12346 exceptional-alpha3-K4-free=2076
diamond-deletion survivors=15 lambda=5:1,6:7,7:5,8:2
diamond-code sha256=6e2633b0f4999a1d09fb98f38f7c268044cada0095be8e84aa4b8fe72d879ebe
clique-OCT exclusions=8 critical-host survivors=7
critical-host codes=GCOcaO GCOcbO GCOcbW GCOe`W GCOebW GCQQV? GCQR@O
critical-host-code sha256=bf063de64c772c1c9c1c83cba7dc39d11bb9c214f3e101595889fe63f25861a0
minimum-reserve shapes P5=2 P3+K2=3 2K2+K1=2
PASS K7-minus both-full boundary reduction
```

**Shore-allocation barrier**
```text
balanced global shore labels=15/15 every rotation keeps 2 demands per shore
balanced-witness sha256=325a008189de182c099d60990d72c94f02fe78709e4858bc5aa48ec8eba59367
mechanism graph vertices=11 connectivity=3 chromatic_number=4
mechanism independent triples=18 shore-rooted K5-minus=0
mechanism K7-minus minor=no
PASS K7-minus shore-allocation barriers
```

### 2.2 Recorded invariants (verified)

| Invariant | Status |
|---|---|
| 12,346 unlabelled order-eight graphs | confirmed (`geng -q 8` and both verifiers) |
| Exactly three exceptional α≤2, K₄-free order-8 survivors | confirmed; independent codes `GQyurg`, `GQyurw`, `GQyuzw` |
| Order-7 chain → 28 types; digest `a045e1d2…eacd` | confirmed (principal + independent re-filter) |
| Common-six 28 survivors; digest `9349e3f0…bec9` | confirmed (principal + independent re-filter) |
| Both-full 2076 → 15 → 7; digests `6e2633b0…` and `bf063de6…` | confirmed (principal + independent re-filter) |
| Fan-tree principal counts 1032/21/3 and 1113/109/6 | confirmed |
| All **7,536** labelled fan-tree pairs | confirmed (`2000+256+256+2000+2000+256×4=7536`) |
| Mask / quotient / rooted digests | confirmed |
| Independent same orbit/tree counts + mask digest | confirmed |
| Independent direct certificate digest `a75aae22…4ce4` | confirmed (principal independent script + auditor reimplementation) |
| Barrier scopes and exact outputs | confirmed |

---

## 3. Optimized-mode hardening

| Script | `python3 -O` exit | Message |
|---|---:|---|
| exceptional_neighbourhood | 1 | `verification requires assertions; do not run Python with -O` |
| nonfull_attachment | 1 | same |
| nonfull_two_entrance barrier | 1 | same |
| overlap_trace | 1 | same |
| distinct_miss fan-tree (principal) | 1 | same |
| both_full_shore | 1 | same |
| shore_allocation barrier | 1 | same |
| **independent** fan-tree checker | **0** | full GREEN output; digest `a75aae22…4ce4` (wall ~19.5 s) |

Printed `PASS`/`GREEN` alone is **not** treated as verification: all assertion-based scripts refuse `-O`, and independent checks re-validate certificates and digests.

---

## 4. Verifier-by-verifier encoding review

### 4.1 Exceptional neighbourhood completion

- **Encoding:** `geng -q 8` → graph6 decode → filter K₄-free and α≤2 → require spanning C₈^{1,2} → rebuild 9 quotients with explicit 7-bag certificates.
- **Predicate alignment:** Finite lemma only (order-8 classification + near-full exterior models). Host lift is written, not computed.
- **Certificates:** Nonempty, pairwise disjoint, connected bags; ≤1 missing inter-bag adjacency (K₇⁻). Independently revalidated for all 9.
- **External input:** Rolek–Song–Thomas arXiv:2208.07335v2 Lemma 2.1 (α=2 order-8 → K₄ or H₈≅C₈^{1,2}) is cited in the audit; the finite enumeration agrees but does not replace that citation for unbounded theory.

### 4.2 One-nonfull attachment reduction

- **Encoding:** `geng -q 7` full catalogue; successive filters α=3, K₄-free, ≤9 edges, κ≤3, no K₅-minor, **single-vertex** diamond deletion (no K₄⁻ minor after deleting any one vertex), no “robust” independent triple.
- **Predicate alignment:** Matches Theorem 3 finite census in the theorem file; host separation lift is written under (H).
- **Note:** “Diamond-deletion” here is **single-vertex** deletion, unlike both-full (pair deletion). Naming is historical; predicates differ.

### 4.3 Nonfull two-entrance allocation **barrier**

- **Encoding:** Fixed order-13 host; exhaustive cuts of size ≤6; packing of full/near-full connected subgraphs; explicit 5-colouring; explicit **K₇** (not K₇⁻) model.
- **Scope (correctly limited):** Proves a topology-only shortcut is false; graph **violates** K₇⁻-exclusion and seven-chromatic criticality. Not a counterexample to (H).
- **Independent rebuild:** Same edge list, connectivity, K₇ model, colouring, boundary code `FCdeG`.

### 4.4 Overlap-trace synchronization

- **Encoding:** `geng -q 6` → α≤3, K₄-minor-free, no vertex-deleted K₄⁻ → 28 codes; reflection demands; matching-parity language check.
- **Predicate alignment:** Finite Corollary 4 / barrier claims only; host trace lifts are written.
- **Independent:** Full re-filter of order-6 recovers exactly 28 codes and digest `9349e3f0…`. Matching-parity language subroutine was **not** reimplemented line-by-line in the auditor suite (see AMBER note).

### 4.5 Distinct-miss fan-tree (principal)

- **State machine:** Portal masks (64×64) with K₄-free / α=3 boundary; orbit under Aut(Z) including swap of shores; Prüfer labelled trees on missed roots; **side-state** enumeration of root-labelled assignments with **contact masks**; **dominance pruning** of dominated masks; combination requires `(base ∪ x ∪ y).bit_count() ≥ 14`; attach singleton `{u}` for K₇⁻.
- **Soundness of dominance:** Contact combination is monotone in masks; if a dominated mask succeeds in combination, the dominating mask does too. Keeping only undominated witnesses is sound for **existence**. Completeness of state generation (all assignments product) is finite and exhaustive on the gadget.
- **Quotient pre-screen:** Deletion/contraction search for whole-component K₇⁻ before fan-tree cases.
- **Predicate alignment:** Finite completion of distinct-miss residue only (not adjacent-miss / one-nonfull / both-full).

### 4.6 Distinct-miss fan-tree (**independent**)

- **Independence:** AST import check — only `__future__`, `functools`, `hashlib`, `itertools`. **No import** of the principal verifier; **no** `SideState` / `side_states` / contact-mask dominance machinery.
- **Method:** Rebuilds portal orbits; quotient via component deletion/contraction; builds sparse fan-tree graphs by **adding limb vertices and contracting actual edges** to six root-distinct bags with `{u}` singleton; validates partition, connectivity, roots, ≥20 bag contacts for K₇⁻.
- **7536 pairs** checked case-by-case with serialized digest `a75aae22…4ce4`.

### 4.7 Both-full shore reduction

- **Encoding:** `geng -q 8` → exceptional α=3 K₄-free (2076) → **pair**-diamond property (every 2-vertex deletion leaves K₄⁻-minor-free order-6) → 15 → no clique OCT → 7 critical-host codes.
- **Independent:** Reproduced 2076, 15, 7 and both digests with separate deletion/contraction minor code.

### 4.8 Shore-allocation **barrier**

- **Encoding:** 15 fixed witnesses (masks) on diamond survivors; balanced 2+2 demand under every independent triple; mechanism graph (boundary + 3 universal apices) has κ=3, χ=4, no K₇⁻.
- **Scope:** Refutes boundary-only demand-concentration inference; **not** a counterexample to critical-host targets or K₇⁻ six-colour.
- **Independent:** Witness digest and balanced checks; mechanism connectivity and no K₇⁻ via partition search.

---

## 5. Independent cross-check suite

**Location (outside repository):**  
`/tmp/k7minus_audit_f4705983/independent/cross_check.py`  
**SHA-256:** `800b9c76f36c3f9e106c7339204220c9653c20ef6e9674c66bbff02cc6ddf275`  
**Runtime:** ~13.1 s wall, ~56 MB peak RSS  
**Result:** `ALL INDEPENDENT CROSS-CHECKS PASSED` (exit 0)

### 5.1 Methods used (deliberately distinct from project code)

1. **graph6:** Independent McKay graph6 bit-stream decoder/encoder; roundtrip vs `geng` samples; catalogue sizes 156/1044/12346.
2. **Minors:** Separate deletion/contraction recursion (K₄, K₄⁻, K₅) and restricted-growth **connected-partition** search for K₇⁻.
3. **Controls:** K₄, C₅, K₄⁻, C₄, K₅, K₇⁻, K₆, P₁₀ positive/negative tests.
4. **Certificates:** All 9 exceptional quotients; all 7536 fan-tree certificates (nonempty, disjoint, connected, root containment, ≤1 missing contact).
5. **Orbits:** Every valid labelled portal assigned to exactly one canonical orbit representative under Aut(Z)∪swap.
6. **Principal side-state:** Code review of dominance + combination monotonicity (sound for existence).
7. **Independence:** Confirmed independent checker imports no principal code and contracts real edges.
8. **7536 pairs:** Case-by-case in auditor script; digest matches `a75aae22…4ce4`.
9. **Predicate vs prose:** Spot-checked against theorem/barrier files; no encoding claimed unbounded host theorems.
10. **Hidden finite assumptions:** Finite scripts bound order (6/7/8/13/fan gadgets). Host lifts rely on written (H): κ≥7, χ=7, proper minors 6-colourable, no K₇⁻ — **not** discharged by enumeration alone.

### 5.2 Serialized hashes from independent work

| Object | SHA-256 |
|---|---|
| Order-7 residue codes | `a045e1d21098d0789ea1c549ed00f380ab97df9120335ff24127f9c8a039eacd` |
| Common-six codes | `9349e3f0c53068bdbdac7068c8fa347ac6658b5231c8abd3dc8e99804118bec9` |
| Both-full diamond-15 | `6e2633b0f4999a1d09fb98f38f7c268044cada0095be8e84aa4b8fe72d879ebe` |
| Both-full host-7 | `bf063de64c772c1c9c1c83cba7dc39d11bb9c214f3e101595889fe63f25861a0` |
| Fan-tree mask orbit digest | `1d653544a19aed2fac36589f1d113583fe29f7a2af58679e90b574558d9f3203` |
| Independent direct-contraction certificates | `a75aae228f346587a12ab0821c1a1e735b4d25e7ad9181b161a6512bab5c4ce4` |
| Shore balanced witnesses | `325a008189de182c099d60990d72c94f02fe78709e4858bc5aa48ec8eba59367` |
| Auditor scratch script | `800b9c76f36c3f9e106c7339204220c9653c20ef6e9674c66bbff02cc6ddf275` |

Principal-only digests (not re-serialized by auditor, but reproduced by principal twice):  
`quotient_certificate_digest=cb251c55…`, `fan_tree_certificate_digest=5c19a213…`.

---

## 6. Trust-boundary table

| Layer | What is established | What is **not** established by computation alone |
|---|---|---|
| **Finite catalogue reproduction** | geng counts; filter chain counts; digests; determinism; `-O` hardening | Correctness of nauty geng as an external oracle (standard, but external) |
| **Validity of emitted certificates** | Checked branch-set properties for exceptional quotients and all 7536 fan-tree models (two independent algorithms) | That every possible host configuration reduces to these gadgets (written lift) |
| **Completeness of finite encoding** | Exhaustive over claimed finite domains (orders 6–8 catalogues; 64×64 portals; Prüfer trees; fixed barrier graphs) | That the finite domain list is complete for the **unbounded** host without the written reduction |
| **Written reduction host → finite cases** | Present in theorem files under hypotheses (H); audited in adjacent `_audit.md` files (internal) | This computational audit does **not** re-prove the host-level mathematics |
| **External mathematical inputs** | Rolek–Song–Thomas order-8 α=2 lemma; R(3,3)=6; standard connectivity/critical-graph facts as cited | Independent external peer review |

**Explicit:** A clean finite reproduction does **not** prove the unbounded K₇⁻ six-colour conjecture or HC₇.

---

## 7. Verdicts by claim

| Claim / artefact | Verdict | Rationale |
|---|---|---|
| Exceptional neighbourhood finite lemma + certificates | **GREEN** | Reproduced; independent catalogue + 9 certificates |
| One-nonfull order-7 residue (28 types) | **GREEN** | Reproduced; independent filter + digest |
| Nonfull two-entrance allocation barrier | **GREEN** | Reproduced; independent rebuild; scope correctly limited |
| Overlap-trace common-six census + digests | **GREEN** | Reproduced; independent re-filter |
| Overlap-trace matching-parity language subcheck | **AMBER** | Reproduced deterministically; not reimplemented by auditor as a separate encoding |
| Distinct-miss fan-tree principal finite completion | **GREEN** | Reproduced; cross-validated by independent contraction checker + auditor 7536-pair suite; same mask digest |
| Independent direct-contraction fan-tree checker | **GREEN** | Reproduced (incl. under `-O`); independent of principal code; digest match |
| Both-full 2076→15→7 census | **GREEN** | Reproduced; independent pair-diamond + clique-OCT re-filter |
| Shore-allocation barriers | **GREEN** | Reproduced; independent witness + mechanism checks; scope limited |
| Unbounded host theorems / conjecture | **out of scope / not GREEN by computation** | Require written lifts + external review |

No **RED** mismatches or encoding unsoundness found in the eight principal finite programs at this commit.

### Discrepancies

**None.** No file/line failure, no stdout mismatch, no digest mismatch, no nondeterminism.

---

## 8. What remains necessary for publication (even if every computation is GREEN)

1. **Human mathematical peer review** of written host reductions under (H), not only finite verifiers.
2. **Traceable external citations** (Rolek–Song–Thomas, Ramsey R(3,3)=6, connectivity facts) with exact lemma numbers, distinguished from new deductions.
3. **Complete residual case analysis** beyond these finite pieces (adjacent-miss, remaining one-nonfull/both-full host arguments, global HC₇ spine) as named in the research ledger.
4. **Containerized reproducibility package** (pinned nauty + Python image) for third-party runs; this audit used a clean checkout on a developer host, not a sealed VM image.
5. **Clear trust-boundary language** in any paper: finite enumeration + certificate validation **≠** unbounded theorem.
6. **Audit freshness:** keep content-hash-bound audits beside theorems when text changes.
7. Optional strengthening: independent reimplementation of the overlap-trace matching-parity language checker; third-party networkx/Sage minor cross-check; formal verification of graph6/geng trust if required by venue.

---

## 9. Auditor notes

- Two deliberately different fan-tree implementations exist and agree; the independent checker is not a clone of the principal side-state engine.
- “Diamond-deletion” is **not** a single global predicate: one-nonfull uses single-vertex deletion; both-full uses every pair deletion. Encoding review must not conflate them.
- Barrier verifiers correctly document that their hosts **leave** the critical K₇⁻-free setting.
- Checkout remained clean: `git status --porcelain` empty at end; `HEAD` unchanged.

**Audit artefacts (non-repo):** `/tmp/k7minus_audit_f4705983/`  
(runs/, expected/, independent/cross_check.py, this report)
