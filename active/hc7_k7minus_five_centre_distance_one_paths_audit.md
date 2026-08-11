# Internal audit: synchronized Kempe paths at a five-centre two-cut

Audited file:
`active/hc7_k7minus_five_centre_distance_one_paths.md`

Audited SHA-256:

```text
d044a7c7765d5b72b8aa469a188323bb48597cf22a9e6f318c82bccdf6afbedc
```

**Verdict:** **GREEN** for Theorem 2.1, Lemmas 3.1, 3.3, 4.1, and
5.1, Corollary 3.2, and the explicitly nonterminal scope of this revision.

This is a hash-pinned internal mathematical audit, not external peer
review.  Relative to the theorem revision originally checked, the source
changes only its audit-status metadata; no theorem or proof text changed,
so the GREEN verdict is retained.  Its final
interval-uncrossing or rooted-minor allocation step is still open.

## 1. The four synchronized transitions

In the fixed six-colouring of `M_C`, the contraction vertex has the root
colour `alpha`, while `p,q` have the common colour `beta`.  Criticality of
`pq` in `M_C+pq` therefore gives a `beta`--`gamma` component containing
both poles for every one of the four colours outside
`{alpha,beta}`.  Such a component avoids the contraction vertex.  After
pullback, a shortest pole-to-pole path consequently has nonempty interior
in `C` and is induced.

On the opposite shore, the singleton response is distinct.  Once the root
and `p` colours are aligned with `alpha,beta`, the colour at `q` is one of
the same four remaining names.  The standard Kempe swap obstruction joins
`p` to `q` in the corresponding two-colour component.  A global
permutation of the four remaining colour names fixes `alpha,beta` and
turns one shortest literal path into the required path for each coordinate.
Thus the source really does use one common path `R`, rather than four paths
chosen independently.

On either boundary trace the `beta`--`gamma` graph consists of the two
singleton components `{p}` and `{q}`: `Z` has colour `alpha` and `pq` is
absent.  Hence the traces are at Kempe distance one on precisely `{q}`.
For distinct coordinates, a common vertex of two `C`-paths must have
colour `beta`; a shared edge would then violate properness.  The `C`-path
has even length and `R` has odd length.  Their interiors lie in the two
anticomplete shores, and inducedness of each path together with the missing
edge `pq` excludes every possible chord.  This verifies all five parts of
Theorem 2.1.

## 2. Residual components and the three-fan

For a component `A` of `G[X-P^circ]`, every neighbour outside `A` is
either a root or a vertex of `P`: the other original shore is anticomplete
to `X`, and distinct components of `X-P^circ` are anticomplete.  The
resulting neighbourhood separates `A` from the nonempty opposite shore, so
seven-connectivity gives `a(A)+h(A)>=7`.  If all five roots met `A`, then
the connected set `A` would contain all of them in one component after
deleting `P`, contradicting rooted infeasibility.  Therefore `a(A)<=4`
and `h(A)>=3` exactly as claimed.

Two distinct `P_gamma` cannot both span `C`: every vertex common to them
would have colour `beta`, whereas the first internal vertex on a
`beta`--`gamma` path has colour `gamma`.  This checks Corollary 3.2.

For Lemma 3.3, a separator of order at most two between the prescribed
triple `T` and the path-neighbour set leaves at least one vertex of `T`.
The union of the corresponding components of `A-K` has all its neighbours
in `K` together with at most four roots.  This would be an at-most-six
separator from the opposite shore, contrary to seven-connectivity.
Set-to-set Menger therefore gives three disjoint paths; truncating each at
its first target makes its internal vertices lie in `A` and ensures three
distinct target vertices.  Deleting those target endpoints from the three
paths leaves the branch sets described in the source.  The triangle edges,
the last path edges, and the three `z`--triangle edges verify every claimed
adjacency in the `K_5^-` model.

## 3. Odd-cycle deletion

If no component of `G-V(O_gamma)` contains all roots, then every component
meeting a root is separated from another root by a subset of the cycle.
Seven-connectivity forces at least seven distinct cycle neighbours.  This
immediately excludes the second outcome for a five-cycle.

For a seven-cycle, the same argument makes every component full to the
cycle.  The audited critical seven-cut capacity theorem permits at most
three components.  Its three-component row would force every proper
three-colouring of the boundary to have class sizes `3,2,2`, while the
seven-cycle has a proper colouring with class sizes `3,3,1`.  Hence exactly
two full components remain.  The use of the capacity theorem is within its
stated hypotheses and proves the complete order-five/order-seven claim.

## 4. Minimum-side descent

An exact equality `N_F(L)={u,v}` makes `{u,v}` an actual two-cut, since
`L` is nonempty and the original opposite shore remains outside it.
Moreover, `N_G(L)={u,v} union N_Z(L)` separates `L` from that shore.
Seven-connectivity and `|Z|=5` force `N_Z(L)=Z`.  The fixed equality-shore
colouring restricts to a permitted colouring of the new closed side: the
roots have colour `alpha`, while same-coloured vertices `u,v` have either
`beta` or `gamma`, never `alpha`.  The audited unconditional two-cut
reduction then identifies `L` as the unique equality-response component.
Its smaller order contradicts the stipulated minimum choice of `C`.

The parity reformulation is correct because each `P_gamma` alternates its
two colours.  The source also correctly observes that its three-attachment
bound does not itself supply the two-vertex neighbourhood needed for this
descent.

## 5. Scope and unresolved obligation

The hypotheses used conditionally in Corollary 3.2 are explicit: rooted
infeasibility is required on both closed shores.  The base five-centre
two-cut reduction supplies it unconditionally on the equality shore only,
so the source does not silently infer the opposite-shore instance from
that theorem.

The audit confirms that the note proves synchronization, induced odd
cycles, exact residual attachment bounds, the prescribed three-fan, and
the stated cycle and descent alternatives.  It does **not** derive a
six-colouring, a forbidden `K_7^-` minor, or a smaller equality side.  The
remaining need for an interval-uncrossing or labelled branch-set allocation
theorem is genuine and is stated without overclaim.
