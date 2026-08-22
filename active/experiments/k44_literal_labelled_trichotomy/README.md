# Literal-`K_{4,4}` capstone scratch: a sharper direct alternative

This scratch checkpoint records a bounded falsification test for the open
literal-core capstone.  It does not prove the capstone or T44.

## Sound reduction

Let `C` be the three-connected exterior and let

`w(X)=|union_{v in X}(N_S(v))|`.

Besides the existing rich-triangle and weighted spanning-`K_4` alternatives,
it is enough to allow this explicit third alternative:

> `C` has six disjoint connected branch bags, each of positive weight, whose
> quotient has at least fourteen of the fifteen `K_6` edges.

Indeed, use the whole literal `K_{4,4}` core `S` as one connected seventh bag.
It touches all six exterior bags.  The quotient therefore has at least
`14+6=20` contacts and is a `K_7^-` model.  This avoids all branch-set ownership
or label-synchronisation issues.

Thus the following purely labelled trichotomy would imply the capstone:

1. three pairwise-touching connected bags of weight at least four;
2. a spanning `K_4` model with all four bags of weight at least three;
3. the positive-weight six-bag `K_6^-` model above.

The verifier asks for a counterexample to exactly this trichotomy under

`|N_C(X)|+w(X)>=7`

for every nonempty `X subseteq V(C)` (the full set gives `w(C)>=7`).

## Computation-free slice through order six

The trichotomy is provable without computation when `|C|<=6`.

For `|C|=4`, three-connectivity makes `C=K_4`.  Every singleton has
weight at least four, so any three vertices give the first outcome.

For `|C|=5`, every singleton has weight at least three.  Every
three-connected graph contains a `K_4` minor, and a minor model in a
connected graph can be enlarged to span all vertices.  The resulting four
bags therefore give the second outcome.

Let `|C|=6`.  Every bag of order at least two has exterior boundary at most
four and hence weight at least three.  Every nonuniversal singleton also
has weight at least three.  Moreover, any three vertices of degree at most
three have singleton weight at least four; the three-prescribed-vertex
cycle theorem in a three-connected graph turns them into three
pairwise-touching rooted bags, giving the first outcome.

Let `b` be the number of universal vertices of `C`.

- If `b=0`, enlarge any `K_4` minor to a spanning model.  Every bag has
  weight at least three.
- If `b=1`, write `u` for the universal vertex.  The graph `C-u` is
  two-connected.  Unless it is `C_5`, it has a cycle of length at most four;
  choose a vertex `x` outside that cycle, enlarge the cycle to a spanning
  three-bag triangle model of `C-{u,x}`, and add the bag `{u,x}`.  This is
  the second outcome.  If `C-u=C_5`, its five vertices have degree three in
  `C`, so three of them give the first outcome.
- If `b=2`, the other four vertices induce a connected graph.  Choose an
  edge `zw`, pair the other two vertices separately with the two universal
  vertices, and leave `z,w` as singleton bags.  These four bags give the
  second outcome.
- If `b=3` and two of the other three vertices are adjacent, use those two
  as singleton bags, pair the third with one universal vertex, and pair the
  other two universal vertices.  This is the second outcome.  If the other
  three are independent, all three have degree three and give the first
  outcome.
- If `b=4`, the two remaining vertices are nonadjacent unless all six
  vertices are universal.  Thus `C=K_6-e`, and the six singleton bags give
  the third outcome.  The case `b>=5` is `K_6` and gives the same outcome.

All six bags in the last outcome have positive weight by the singleton
inequality.  Thus the solver contributes genuinely new bounded evidence
only at order seven.

## Exact bounded universe and trust boundary

`verify_labelled_trichotomy_through_order7.py` checks every unlabeled
three-connected graph of orders four through seven in the NetworkX graph
atlas.  For each fixed `n`-vertex graph, the label universe is every
`8 x n` Boolean incidence matrix: exactly `2^(8n)` assignments, represented
symbolically rather than sampled.

All connected triangle bags, all spanning four-bag `K_4` partitions, and all
six-bag `K_6^-` models (unused vertices allowed) are generated explicitly.
Z3 proves that the conjunction avoiding all three outcomes is unsatisfiable.
There is no independently checkable UNSAT certificate; Z3 is the decisive
trust boundary.  If a SAT assignment is ever returned, a separate concrete
bit-mask evaluator in the same source validates every inequality and the
absence of all generated outcomes before reporting it.

Run from this directory with:

```text
UV_CACHE_DIR=/tmp/k44-capstone-uv uv run --with networkx --with z3-solver \
  python verify_labelled_trichotomy_through_order7.py
```

Expected output is retained in `verify_labelled_trichotomy_through_order7.out`.

## Scope

The bounded census supplies no unbounded inference.  The smallest credible
literal-core target is now the pure labelled trichotomy above.  A lexicographic
`K_4` exchange proof still needs to produce the positive-weight `K_6^-` outcome
when the weighted `K_4` exchange stalls; no such exchange proof was found here.
