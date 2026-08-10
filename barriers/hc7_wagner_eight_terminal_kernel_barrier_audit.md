# Audit: Wagner eight-terminal kernel barrier

## Verdict and audited revision

**Verdict:** **GREEN** as a barrier to the precisely stated one-centre
eight-terminal kernel lemma.

The audited source is
[`hc7_wagner_eight_terminal_kernel_barrier.md`](hc7_wagner_eight_terminal_kernel_barrier.md)
at SHA-256

```text
7e496ab79efebb1356492f256953ec9d3d1c91bd772fa647fc2402767d9cf9d9
```

This is a separate internal mathematical audit, not external peer review.
No computational result is used.

## Independent checks

The construction has eight vertices and the twelve distinct edges of an
eight-cycle and a disjoint four-edge opposite matching.  With `T=V(W)`, every
edge has two terminal ends, so terminal irreducibility is vacuous and exact.

The connectivity case split is complete.  Up to a dihedral automorphism, a
deleted pair has cyclic distance `1`, `2`, `3`, or `4`.  At distance `1` the
remaining cycle edges form a spanning path.  At distances `2`, `3`, and `4`,
respectively, the displayed opposite edges join the residual cycle
intervals.  Hence no set of at most two vertices disconnects `W`.

For independence number, a four-set independent in the spanning `C_8` must
have exactly one unchosen vertex in each cyclic gap, so it is an alternating
class.  Both alternating classes contain opposite matching edges.  The set
`{0,2,5}` checks the reverse inequality, proving `alpha(W)=3`.  An opposite
pair has disjoint cycle-neighbour sets, and the opposite edges form a
matching, so no triangle uses an opposite edge; the cycle itself has no
triangle.  Thus `W` is triangle-free and hence `K_4`-free.

The edge-count obstruction is decisive.  A simple minor operation never
increases the number of edges, while

```text
|E(W)|=12 < 14=|E(K_6^-)|.
```

For the cone, `|V(z join W)|=9` and `|E(z join W)|=20`.  Any seven-vertex
minor requires a vertex-reducing operation.  If edges were deleted first,
the count has already dropped; otherwise the first such operation either
deletes a positive-degree vertex from the connected graph or contracts an
edge, again dropping the count.  Later minor operations cannot restore an
edge.  Every seven-vertex minor therefore has at most nineteen edges, less
than the twenty edges of `K_7^-`.

Eight is the minimum possible order of a graph containing eight distinct
terminals, so the claimed minimality by order is correct.

## Scope and unresolved assumptions

There are no unresolved assumptions in the counterexample.  It refutes only
the local implication written in the source.  The construction is not a
hypothetical counterexample to `HC_7`, and it does not address a composition
that retains other centres' contacts, critical colourings, or the global
relative-connectivity data.  Those qualifications are stated explicitly in
the audited source.
