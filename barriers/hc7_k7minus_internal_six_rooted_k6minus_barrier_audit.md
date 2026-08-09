# Independent audit: internally six-connected rooted-minor barrier

**Verdict:** **GREEN** for the exact source revision below.

**Audited source:**
[`hc7_k7minus_internal_six_rooted_k6minus_barrier.md`](hc7_k7minus_internal_six_rooted_k6minus_barrier.md)

**Promoted source SHA-256:**

```text
a0f223ff50443990a4b5055cd118f4ee826787d51f51af544d857c8144d38e6f
```

**Originally audited source SHA-256:**

```text
36151f3f81f001c71d37bf412d3e8f2f3fd85e80cf5a62fd8bf5a8cb5dbcae25
```

Relative to the originally audited source, the promoted source replaces
`internal audit pending` in the opening status with the GREEN link to this
audit and expands the final vague reference to augmentation into the exact
alternatives: the prescribed rooted `K_6^-` minor or trace-preserving
exact-cut descent.  These changes affect only status and scope language.
No hypothesis, construction, conclusion or proof step changed, so the GREEN
verdict applies to the promoted source.

This is a separate internal mathematical audit, not external peer review.
The construction, rooted separations, minor models and completed-side claims
were checked directly.  No unresolved inference was found within the stated
scope.

## Internal six-connectivity

The graph has vertex set `R dotcup W`, where `|R|=6`, `|W|=3`, every
`R`--`W` edge is present, `J[R]` has the single edge `ab`, and `J[W]` is the
path `w_1w_2w_3`.

Let `(X,Y)` be a separation with `R subseteq X` and `Y-X` nonempty.  The
open side `Y-X` contains a vertex of `W`.  That vertex is adjacent to every
root, while a separation has no edge from `X-Y` to `Y-X`.  Every root must
therefore lie in `X cap Y`, proving `|X cap Y|>=6`.  The separation
`(R,V(J))` has order six, so the rooted connectivity is exactly six under
the asymmetric definition used in the programme.

This does not imply ordinary six-connectivity.  The degrees are

```text
d(u_i)=3,  d(a)=d(b)=4,  d(w_1)=d(w_3)=7,  d(w_2)=8.
```

The spanning `K_{6,3}` gives `kappa(J)>=3`, while deleting `W` disconnects
the roots (equivalently, a vertex `u_i` has degree three).  Hence
`kappa(J)=3`, exactly as asserted.

## The rooted models

The four displayed branch sets are disjoint and connected.  Pairwise
adjacency is witnessed, for example, by

```text
u_1w_2, u_1w_3, w_1u_4,
u_2w_3, w_2u_4, w_3u_4.
```

They therefore form the stated `U`-rooted `K_4` model.

For an `R`-rooted six-branch-set model, no branch set may contain two roots.
Only the three vertices of `W` are nonroots, so at most three branch sets
meet `W`; at least three branch sets are singleton roots.  Among any three
roots there is at most one edge, because `ab` is the only edge of `J[R]`.
Thus at least two pairs of singleton branch sets are nonadjacent.  A
`K_6^-` model may omit only one branch-set adjacency, so the claimed rooted
model cannot exist.  The two edges of the path on `W` do not affect this
count.

As an independent finite cross-check, assigning each vertex of `W` to one
of the six rooted bags or leaving it unused exhausts `7^3=343` possible
models.  Every assignment has at most thirteen of the fifteen branch-set
adjacencies.  Repeating the check after adjoining `t`, both before and after
the formal boundary completion, again gives at most thirteen adjacencies.
Thus even the broad reading of the statement that the obstruction persists
is safe.

## Clique and criticality scope

Every clique contains at most two vertices of `R` and at most two vertices
of `W`, so `omega(J)=4` and `J` contains no `K_5` subgraph.  This is the
standard literal meaning of “`K_5`-free” in the source.  It is not a claim
of `K_5`-minor-freeness: the five bags

```text
{a}, {b}, {u_1,w_1}, {u_2,w_2}, {u_3,w_3}
```

form a `K_5`-minor model.

The complete `R`--`W` join forces disjoint colour palettes on the two
parts.  Since both `J[R]` and `J[W]` have chromatic number two,
`chi(J)=4`.  The proper subgraph `J-u_4` still contains the literal clique
`{a,b,w_1,w_2}`.  After contracting `w_1w_2`, the contraction vertex,
`w_3,a,b` still induce a `K_4`.  Consequently `J` is neither a
seven-chromatic critical host nor contraction-critical even at its own
chromatic number.

## The seven-boundary completion

After adding `t` adjacent precisely to `w_1,w_3`, the three degrees on `W`
are

```text
d(w_1)=6+1+1=8,
d(w_2)=6+2=8,
d(w_3)=6+1+1=8.
```

Completing `T={a,b,t}` to a triangle adds only `at` and `bt`.  The graph
induced by `W union T` then has every edge of `K_6` except the two disjoint
edges `w_1w_3` and `tw_2`.  Deleting at most three vertices leaves at least
three vertices, and a graph in which each vertex has at most one nonneighbour
cannot be disconnected on at least three vertices.  Hence the completed
graph is four-connected.  Deleting the four common neighbours of
`w_1,w_3` separates that pair, so its connectivity is exactly four.

Finally, deleting the seven-vertex boundary `R union {t}` leaves the
connected path `W`.  Both singleton connected subgraphs `{w_1}` and
`{w_3}` are adjacent to all six vertices of `R` and to `t`.  They are
therefore two vertex-disjoint connected subgraphs in the same component,
each adjacent to every boundary vertex.  This verifies the advertised
failure of the generalized-wheel no-two-subgraphs condition.

The construction has no opposite full component and fails the global
degree, connectivity and criticality hypotheses.  It therefore refutes
only the displayed intermediate rooted-minor implication and is not an
`HC_7` counterexample.
