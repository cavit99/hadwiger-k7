# Internal audit: three-full-component partition barrier

**Verdict:** **GREEN** for Proposition 1.1 and its stated scope.  The graph
is an exact counterexample to the displayed boundary-allocation lemma, not
to the `K_7^-` six-colour conjecture or to `HC_7`.  This is a separate
internal mathematical audit, not external peer review.

## Exact revision

The audited source is
[`hc7_k7minus_three_full_component_partition_barrier.md`](hc7_k7minus_three_full_component_partition_barrier.md),
with SHA-256

```text
d8ff6502d4da17e26d65685e2a7751f18440f90571a8f65a9b1510c0996cfafe
```

## Construction and boundary properties

The revision after the cold audit changes only the status line to link this
audit.  A mechanical diff check found no mathematical change.

The boundary `T=2K_3 dotunion 2K_1` has eight vertices and chromatic number
three.  Choosing one edge from each triangle gives an induced `2K_2`, which
no split graph contains, so `T` is nonsplit.  Every connected minor model
inside the disconnected graph `T` lies in one component; its components
have order at most three.  Thus `T` is `K_5`-minor-free.

In `Q=overline K_3 vee T`, the three vertices outside `T` are independent,
are pairwise distinct components of `Q-T`, and each is adjacent to every
boundary vertex.  Hence the construction has exactly the three
anticomplete connected boundary-full components claimed.

## Exclusion of the target minor

At most three disjoint branch sets of a putative `K_7^-` model can contain
one of the three exterior vertices.  At least four branch sets would
therefore avoid them.  Every connected such branch set is contained in a
single component of `T`.

Branch sets placed in two distinct components of `T` are pairwise
nonadjacent across those components.  Since a `K_7^-` model permits at
most one missing pair, all exterior-avoiding branch sets would either have
to lie in one component, or there could be exactly one in each of two
components.  The first alternative has at most three branch sets and the
second has two.  Neither accommodates the required four.  This proves
`K_7^- not preccurlyeq Q`; the reasoning also covers branch sets containing
more than one exterior vertex.

## Failure of the proposed allocation

Every edge of `T` belongs to one of its two triangles.  Deleting both ends
of that edge leaves the other triangle intact, so the remainder is not
bipartite.  Consequently no boundary edge has the proposed property,
although all three full-component, nonsplit, `K_5`-minor-free and target-
exclusion hypotheses hold.

The source correctly limits the conclusion.  The graph is four-colourable,
has degree-three boundary vertices and is not seven-connected or
minor-minimal non-six-colourable.  It carries no six-coordinate forest
responses.  It therefore refutes only the boundary-allocation inference
stated in Proposition 1.1 and leaves any theorem using criticality,
connectivity or labelled coordinate colourings untouched.
