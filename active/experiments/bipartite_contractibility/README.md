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

The solver uses the installed Z3 command-line executable (observed version
4.16.0), with no Python Z3 dependency. Integer branch labels specify
membership or omission. Each assigned nonroot has a same-branch neighbour
with a strictly smaller nonnegative depth, forcing connection to its
unique root. The nine required contacts are asserted explicitly.
The script checks a positive literal target and a negative misrooted target
before generating schemes. Separate internal encoding checks also tested a
subdivision, a missing edge, an isolated root and the singleton-shore
barrier host. An UNSAT answer would be only a lead requiring independent
verification, never a counterexample certificate by itself.
