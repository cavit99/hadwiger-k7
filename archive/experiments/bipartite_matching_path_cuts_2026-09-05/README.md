# Supplied matching-path cuts: frozen diagnostic

**Status:** finite diagnostic and explicit barrier to an intermediate
construction, frozen on 5 September 2026 after the universal
[bipartite theorem](../../../results/bipartite_contractibility_via_matroid_reduction.md).
This is not a counterexample to contractibility and is not a live target.

The attempted construction chooses a target perfect matching, retains its
four supplied scheme paths, and splits each once into its two rooted
branch sets. The fixed 24-vertex, 48-edge coloured `K_{4,4}` scheme in
[the checker](check.py) defeats all 24 matchings and all `3^4` cut choices
per matching. Every path has length three and every nonroot occurs in
exactly two paths. The checker also retains and independently verifies an
explicit fully rooted model in the same host.

The first unsupported inference was that optimizing over supplied matching
paths would suffice for the required minor. It cannot: every allowed
matching and cut is excluded here. This says nothing against rerouting the
selected paths, expanding branch sets outside those paths, or using trees.
The smallest useful repair must permit one of those additional operations
and prove preservation. The subsequently proved component contraction
does so using simultaneously allocated trees.

There is also a short reason for the restricted failure. If a selected
`A` branch is singleton, adjacency to it requires every `B` branch to
include its selected internal `B` vertex. Thus every cut is immediately
after its `A` root. Each selected internal `B` vertex sees only two `A`
roots, so these branch sets cannot give `K_{4,4}`. The symmetric argument
excludes a singleton `B` branch. All four cuts would therefore have to
be in the middle. Required contacts could then use only edges between
the selected internal vertices. Each such vertex has only two neighbours
of the opposite internal type, whereas four distinct contacts are needed.

```sh
uv run python3 archive/experiments/bipartite_matching_path_cuts_2026-09-05/check.py
uv run python3 archive/experiments/bipartite_matching_path_cuts_2026-09-05/check.py --json
```

Expected result: all 1,944 restricted models fail and the displayed rooted
model passes. The JSON output includes the exact paths and positive model.
This archived diagnostic is independent of the universal proof's validity.
