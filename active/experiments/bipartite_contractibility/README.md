# Bipartite scheme diagnostics

**Status:** exploratory finite computations. The unbounded singleton-shore
barrier has a separate [written proof](../../../barriers/bipartite_scheme_singleton_shore_barrier.md)
and [internal audit](../../../barriers/bipartite_scheme_singleton_shore_barrier_audit.md).
The primary target and exact proof limits are in the
[technical frontier](../../bipartite_contractibility_frontier.md).

## Universal construction diagnostics

The [matroid-reduction implementation](matroid_reduction.py) constructs
models and checks their lifts independently with NetworkX. The
[universal theorem](../../../results/bipartite_contractibility_via_matroid_reduction.md)
has a written computation-free proof; these runs test the implementation.

```text
uv run python3 active/experiments/bipartite_contractibility/matroid_reduction.py --samples 100
uv run python3 active/experiments/bipartite_contractibility/matroid_reduction.py --order 4 --samples 0
uv run python3 active/experiments/bipartite_contractibility/matroid_reduction.py --order 5 --samples 0
uv run python3 active/experiments/bipartite_contractibility/matroid_reduction.py --order 3 --json
```

Recorded checks: the augmentation engine agrees with an independent
exhaustive assignment check on 21 small matroid systems; all 100
variable-support `K_{3,3}` schemes and 100 mixed pair/triple-support
`K_{4,4}` schemes return checked rooted models. The singleton-shore
barriers at `n=3,4,5` reduce in order as `36 -> 21`, `56 -> 32`,
and `80 -> 45`, respectively, then finish with the opposite shore as
the projection shore. This directly exercises expansion on both sides.

The JSON option emits the input paths and colours, allocated forests,
minimizing label sets, contracted pieces, reduced paths and final model.
Checks cover matroid ranks, disjoint connected pieces, all roots, every
reduced path edge, strict order decrease, and the lifted model's contacts.
The diagnostic starts with properly endpoint-coloured schemes; it does
not implement the theorem's general monochromatic normalization.
The finite sample families do not restrict the written theorem's scope.

## Classification falsification

The [classification screen](classification_screen.py) tests the necessary
`M'`-contractibility condition in Kündgen--Pelsmajer--Ramamurthi,
[Theorem 7.7](https://arxiv.org/pdf/1207.6141). For a triangle-free target,
this requires a stable set `S`, a matching in `[S,N(S)]` covering `N(S)`,
and an automorphism of the remaining induced graph taking each vertex to
a neighbour. Every returned positive certificate is checked directly;
every excluded negative target has three checked paths forming a skewed
theta (two odd lengths and one even length).

```text
uv run python3 active/experiments/bipartite_contractibility/classification_screen.py
uv run python3 active/experiments/bipartite_contractibility/classification_screen.py --order 8
uv run python3 active/experiments/bipartite_contractibility/classification_screen.py --order 9 --even-subdivisions --certificates /tmp/classification-certificates.jsonl
```

The candidate requires no skewed theta and deletion of at most one edge
per component to make the target bipartite. All 168 candidate graphs in
the NetworkX atlas through order seven pass the `M'` test. The generator
then exhausts connected nonbipartite triangle-free targets of orders eight
or nine made bipartite by deleting one edge, retaining isomorphic and
labelled repetitions. It writes every such target as a connected
bipartite graph plus an edge within one shore; disjoint neighbourhoods of
the new edge's endpoints enforce triangle-freeness. The deleted edge lies
on an odd cycle, so its deletion leaves the graph connected and this
generation is exhaustive up to relabelling.

At order eight all 10,220 representations pass. At order nine, 180,664 of
241,302 pass; each of the 60,638 failures has a checked skewed theta and
therefore violates the candidate's hypotheses. These are finite
falsification runs, not proofs of sufficiency for arbitrary schemes.
The certificate stream can be retained outside Git with `--certificates`.

Calibration includes the theta with path lengths `2,3,3`: among its 1,279
labelled vertex-and-edge subgraphs, exactly the whole theta fails the
`M'` test. In particular, this example does not refute the separate
proposal that *every* subgraph being `M'`-contractible might suffice.
`M'`-contractibility itself is not hereditary, and a positive test on a
target alone cannot establish that proposal's premise.

The optional larger family replaces every edge of each connected cyclic
atlas graph through order six by a path of length `2`, `4` or `6`, then
adds an edge between two original vertices. When that pair was adjacent
in the base, its replacement path has length at least four. The stable
set of subdivision vertices at odd positions supplies a certificate
which is checked directly, avoiding exponential enumeration of stable
sets in these larger examples. All 5,391 samples, of order at most 81,
pass. These samples also remain finite evidence.

Recorded certificate-stream SHA-256 values are
`f506cb18c219f575e6845e4fbe6e956381464e565852eecbc6f2f920ee1ec724`
for `--order 8`, and
`8f0330a65792e984ce17160f028067ac0f9f580337518e2b71ba19c63f48a2eb`
for `--order 9 --even-subdivisions`. Both streams include the atlas run.

The [frozen supplied-matching-path diagnostic](../../../archive/experiments/bipartite_matching_path_cuts_2026-09-05/README.md)
records an earlier failed restriction: one explicit two-membership
`K_{4,4}` scheme has a rooted model but defeats all 1,944 constructions
obtained by cutting four supplied matching paths once each. The universal
component reduction does not impose that restriction.

## Construction checker

```text
uv run python3 active/experiments/bipartite_contractibility/singleton_shore_obstruction.py --order 3 --json
```

This emits all scheme paths, colours, the local counting certificate and an
explicit rooted model. Checks at `n=3,4,5` passed: respectively `36,56,80`
vertices and `81,144,225` edges. The unbounded claim rests on the written
proof, not these evaluations.

## Flow-prefix counterexamples

```text
uv run python3 active/experiments/bipartite_contractibility/flow_prefix_counterexample.py
```

This checks and prints the two explicit certificates in the
[audited flow-prefix construction finding](../../../barriers/bipartite_flow_prefix_construction.md):
a seven-vertex ordinary scheme giving a disconnected proposed branch set,
and an eight-vertex coloured scheme giving overlapping proposed branches.
Both records include a valid rooted `C_4` model. They refute intermediate
construction claims, not the intended main flow-minor theorem. Both records
return `verified: true`.

## Exploratory rooted-model search

```text
uv run python3 active/experiments/bipartite_contractibility/scheme_search.py --samples 30 --seed 44033 --timeout 8
```

Recorded outcome: 30 SAT, 0 UNSAT, 0 unknown. All 30 returned models passed
a separate NetworkX connectivity, root-containment and contact check.
Generated hosts have 22--34 vertices. The generator chooses a 3-by-3 array
of nonroot incidences between one and four and realizes it with supports
of size two or three, then independently orders the two colour lists on
each path. Thus path lengths are 3,5,7,9; literal edges, longer paths and
arbitrary target graphs are not covered. This is neither exhaustive nor
an unbounded theorem.

## Mixed multiplicities at an odd-cycle attachment

```text
uv run python3 active/experiments/bipartite_contractibility/c5_c4_schemes.py
uv run python3 active/experiments/bipartite_contractibility/c5_c4_schemes.py --json
```

This diagnostic fixes a `C_5` and a `C_4` sharing root `v`. Each
noncentral `C_5` colour has two nonroots; each other `C_4` colour has
one. Both `v` nonroots occur on both incident `C_5` paths, and different
ones occur on the two incident `C_4` paths. The generator checks 64
specified six-bit order patterns on hosts of 21 vertices and 37 edges.
All 64 returned SAT rooted models, independently checked with NetworkX.
The shared Z3 encoder is calibrated on a literal rooted `C_5` and a
star with its five leaves prescribed, respectively positive and negative.
Its original `K_{3,3}` default is retained.

For each host the script also enumerates every nonempty independent
set of nonroots and computes its total projection rank by union-find.
None satisfies the rank condition of the
[general reduction lemma](../../../results/general_scheme_independent_set_reduction.md#lemma-1-a-root-preserving-decreasing-reduction).
Thus these positive examples require something beyond that particular
reduction condition. The JSON option emits all paths, prescribed roots,
target edges, returned models and rank-check counts. This is a bounded
diagnostic, not a theorem for arbitrary schemes of `C_5` joined to
`C_4`, and not evidence sufficient to prove the classification candidate.

## Shared rooted-minor encoding

The solver uses the installed Z3 command-line executable (observed version
4.16.0), with no Python Z3 dependency. Integer branch labels specify
membership or omission. Each assigned nonroot has a same-branch neighbour
with a strictly smaller nonnegative depth, forcing connection to its
unique root. The requested target contacts are asserted explicitly.
The original `K_{3,3}` diagnostic checks a positive literal target and a
negative misrooted target before generating schemes. Separate internal encoding checks also tested a
subdivision, a missing edge, an isolated root and the singleton-shore
barrier host. An UNSAT answer would be only a lead requiring independent
verification, never a counterexample certificate by itself.
