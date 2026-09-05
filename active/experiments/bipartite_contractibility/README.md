# Bipartite scheme diagnostics

**Status:** exploratory finite computations. The unbounded singleton-shore
barrier has a separate [written proof](../../../barriers/bipartite_scheme_singleton_shore_barrier.md)
and [internal audit](../../../barriers/bipartite_scheme_singleton_shore_barrier_audit.md).
The primary target and exact proof limits are in the
[technical frontier](../../bipartite_contractibility_frontier.md).

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
