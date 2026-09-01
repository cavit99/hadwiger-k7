# Weighted-splitter hostile finite screen

**Status:** computer-assisted bounded evidence only.  No counterexample was
found.  This experiment does not prove the weighted splitter theorem, the
literal `K_{4,4}` case of T44, T44, or Conjecture 21.

## Exact fixed-graph formula

For a fixed three-connected graph `C`, the search represents all eight label
incidences at every vertex by Boolean variables.  It writes

```text
w(X) = |union_{v in X} L(v)|
```

and enforces

```text
|N_C(X)| + w(X) >= 7
```

for every nonempty proper `X`, together with `w(C) >= 7`.  The implementation
uses the same formula for every nonempty `X`, including `X=V(C)`.

The solver excludes all three terminal configurations:

1. three disjoint connected pairwise-touching bags of weight at least four;
2. a spanning four-bag `K_4` model whose bags all have weight at least three;
3. six disjoint connected positive-weight bags, unused vertices allowed,
   whose quotient has at least fourteen of the fifteen `K_6` edges.

Every edge `uv` is contracted concretely and retained exactly when `C/uv` is
three-connected.  For each retained edge the solver requires a blocker among
**all** nonempty sets

```text
X subseteq V(C)-{u,v}
```

such that `u,v in N_C(X)` and

```text
|N_C(X)| + w(X) = 7.
```

In particular, the encoding does not restrict blockers to separation
fragments, connected sets, boundary order at least four, or non-co-spanning
sets.

## Complete order-eight screen after the cubic-vertex reduction

Three-connected graphs have minimum degree at least three.  If three vertices
have degree three, their singleton inequalities give all three weight at least
four.  A cycle through the three prescribed vertices, split into three arcs,
then gives terminal configuration 1.  It is therefore enough at order eight
to search graphs with at most two cubic vertices.

`geng -c -d3 8` generates 2,589 unlabelled connected graphs.  Of these, 1,655
have at most two cubic vertices; 1,619 are three-connected and 36 are not.
Every one of the 1,619 solver instances was UNSAT.  Their cubic-vertex count is

```text
0 cubic vertices: 422
1 cubic vertex:    582
2 cubic vertices: 615
```

The stable digest over the sorted deterministic graph records is

```text
77fc8b9575328030a69bd4da9b68f31f909168b4d00d909a87f3e7ecf8c0dc4a
```

The digest excludes timings, input order and shard-local names.  Its records
retain the graph6 string, status, terminal-model counts, contractible edges,
tight-witness counts and small-atom counts.

## Theory-guided small-atom probes

A second formula additionally requires a connected tight set `A` satisfying

```text
1 <= |A| <= 3,   w(A) <= 3,
```

whose boundary contains both endpoints of a three-contractible edge.  This
was run on every connected unlabelled 4-regular graph of orders nine and
ten:

```text
order 9:  16 generated, 16 three-connected, all UNSAT
order 10: 59 generated, 57 three-connected, 2 not three-connected, all 57 UNSAT
```

At order nine the graph-side candidates realise the pairs

```text
(|A|,w(A)) = (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3).
```

At order ten they also realise `(3,0)`.  None of these pairs survives the
complete label, terminal-exclusion and all-edge blocker formula.  The stable
record digests are respectively

```text
2903c8e0435862474a558f189edf309c913f326675c71c9438ac33d611ef1aea
60d7e292ba123fe8dfdb2b178eef14636a7ea74c05d65eff8e3c9d078baae36c
```

These order-nine and order-ten runs are targeted probes, not complete censuses
of all three-connected graphs at those orders.

## Reproduction

The search needs NetworkX 3.6.1, Z3, and Brendan McKay's `geng`.  From this
directory, the retained runs used Z3 5.1.0 and nauty/geng 2.9.3.  The
complete order-eight command is

```text
geng -q -c -d3 8 | \
  UV_CACHE_DIR=/tmp/k44-splitter-uv \
  uv run --with networkx==3.6.1 --with z3-solver==5.1.0 \
  python search_weighted_splitter_counterexample.py \
    --stdin --max-cubic 2 --summary-only --timeout-ms 60000
```

The small-atom commands replace the `geng` invocation by

```text
geng -q -c -d4 -D4 9
geng -q -c -d4 -D4 10
```

and add `--require-small-atom`.

If a future run returns SAT, it writes a concrete graph6 string and eight-bit
label mask for each vertex to the path selected by `--witness`.  Validate that
file without importing the Z3 encoding by running

```text
uv run --with networkx==3.6.1 \
  python check_weighted_splitter_counterexample.py /path/to/witness.json
```

The checker directly enumerates all boundary inequalities and all three
terminal configurations, recomputes three-connectivity after each edge
contraction, and verifies that every three-contractible edge is unsafe.

As a generator regression test, the search routines reproduce the retained
atlas totals through order seven exactly:

```text
order 4: [10, 1, 0]
order 5: [159, 20, 0]
order 6: [3615, 469, 2]
order 7: [111765, 14509, 197]
```

The entries count the generated configurations of types 1, 2 and 3.

## Trust boundary

Z3 5.1.0 returned UNSAT for the recorded fixed-graph instances.  No
independently checkable UNSAT certificate is retained; Z3 is the decisive
trust boundary.  The concrete checker can validate SAT witnesses but cannot
certify these UNSAT results.  The concise `hostile_screen.out` is an
assembled retention record, not the byte-for-byte output of one command.
Graph6 representatives and their digest are pinned to the recorded
nauty/geng version.  No unbounded conclusion is inferred from the finite
computations.
