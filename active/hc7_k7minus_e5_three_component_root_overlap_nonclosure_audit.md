# Audit: three-component rooted-model overlap nonclosure

**Verdict:** GREEN as a negative finding.  No positive theorem is claimed.

**Audited source:**
`active/hc7_k7minus_e5_three_component_root_overlap_nonclosure.md`

**SHA-256:**
`77b3b943a6ec382635c789d90b18d536bc9c40eed28acfd974a9ab1abcfc88f0`

This is an internal mathematical audit, not external peer review.

## Root-overlap diagnosis

The six-bag loss is real.  Fifth-root augmentation places `x` in a helper
of one rooted model.  If the second rooted model also uses `x` in a root
bag, those two bags overlap.  Merging them restores disjointness but leaves
only six branch sets.  The note correctly refrains from treating that
construction as a `K_7^-` model.

The positive theorem in the adjacent
`hc7_k7minus_e5_k23_331_elimination.md` repairs precisely this issue by
proving that the second rooted `K_4` can be chosen in the graph with `x`
deleted.  The warning remains useful for other boundary rows.

## Critical-cycle accounting

The displayed edge identity for `H_0=H^*-x` is correct: completing the
five-boundary clique gives

```text
|E(H^*)|=4|A|+delta(A)+10,
```

and deleting the degree-five vertex `x` leaves
`4|A|+delta(A)+5` edges.

For a four-cut `T` with open components `W,R`, partitioning the edges of
`H_0` into the two closed sides and the boundary gives

```text
eta(W)+eta(R)+|E(H_0[T])|=delta(A)+5.
```

Since `x` has one neighbour in `W` and no other neighbour there, the excess
of `W` behind the returned boundary `T union {x}` is `eta(W)+1`.
Nothing in these equations lower-bounds `eta(W)`; the high excess may
remain in `R`.  Thus the note correctly records a failure of
high-excess localisation rather than a descent theorem.

Finally, `x` has at most two neighbours in `T`.  An eight-edge returned
boundary would force `T=K_4` and exactly two missing edges incident with
`x`, the already eliminated common-end configuration.  A surviving
returned two-component boundary therefore has at most seven edges.

The note does not claim that `(E5)` or any remaining boundary row is
refuted.
