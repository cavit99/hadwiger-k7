# A universal four-root `K_4^-` lemma in three-connected graphs

Status: complete elementary proof, with a bounded exact falsification screen.
This is a reusable side lemma; by itself it does not prove the literal
`K_{4,4}` closure theorem, Conjecture 21, or `(HC_7)`.

## Theorem

Let `G` be a finite simple three-connected graph, and let `a,b,c,d` be four
distinct vertices of `G`.  Then `G` contains four pairwise disjoint connected
branch sets `A,B,C,D`, respectively containing `a,b,c,d`, such that at least
five of the six pairs of branch sets are adjacent.  Equivalently, `G` has a
`K_4^-` minor rooted at `a,b,c,d` (with the missing pair not prescribed).

## Proof

We use two elementary observations.

**Observation 1 (cycle-or-clique).**  Either `G` has a `K_4` minor rooted at
`a,b,c,d`, or a cycle of `G` contains all four roots.

Indeed, take a cycle `Z` through `a,b,c`; this is the `k=3` case of Dirac's
cycle lemma.  If `d` lies on `Z`, there is nothing to prove.  Otherwise,
three-connectivity and Menger's theorem give a three-fan from `d` to `Z`:
three paths that meet pairwise only at `d`, end at distinct vertices of `Z`,
and have no other vertex on `Z`.

The roots `a,b,c` split `Z` into three closed root-to-root arcs.  If two fan
ends lie on one of these arcs, the two corresponding fan paths together
with the complementary subpath of `Z` form a cycle through `a,b,c,d`.  If
this never happens, no fan end is a root and the three fan ends lie one in
the interior of each of the three arcs.  Cut each arc just after its fan end,
with cyclic orientations chosen consistently.  The three resulting
connected `Z`-bags contain `a,b,c`, are pairwise adjacent, and contain one
fan end each.  The union of the three fan paths with their ends deleted is
a connected fourth bag containing `d` and adjacent to all three `Z`-bags.
This is a rooted `K_4` model.  Observation 1 follows.

This fan construction also appears, in precisely this setting, in the proof
of Fabila-Monroy and Wood, *Rooted K4-Minors*, Electronic Journal of
Combinatorics 20(2) (2013), P64, Theorem 8, pp. 4--5.  Their Theorem 9 is a
different, planar-only strengthening and is not needed here.

If Observation 1 gives a rooted `K_4`, delete any one quotient edge and we
are done.  Hence suppose that `Z` is a cycle containing all four roots.  In
their cyclic order, rename them `a,b,c,d`.  Let

`I_ab, I_bc, I_cd, I_da`

be the four closed consecutive-root arcs of `Z`.

A `Z`-bridge is either a chord of `Z`, with its two ends as attachments, or
a component of `G-V(Z)` together with its incident edges to `Z`, whose
attachments are its neighbours on `Z`.  Call a bridge *local* if all its
attachments lie in one of the four arcs displayed above.

Not every `Z`-bridge is local.  For suppose otherwise.  A component bridge
has at least three distinct attachments, since one or two attachments would
separate that component from `Z` in the three-connected graph `G`.  It is
therefore local to a unique consecutive-root arc.  A chord with both ends in
a consecutive-root arc is likewise local to a unique arc.  For each arc
`I_xy`, take the union of the arc and all bridges local to it.  There is no
edge from the interior of this union to the corresponding unions for the
other arcs.  Consequently, if it contains any vertex other than `x,y`, then
deleting `{x,y}` disconnects it from the two other roots, contrary to
three-connectivity.  Thus every consecutive-root arc is just its root edge
and there are no bridges.  This says `G=Z=C_4`, again contrary to
three-connectivity.

Choose a nonlocal bridge `R`.  The following elementary cyclic-interval fact
will be used.

**Observation 2 (opposite-bag placement).**  If a set of points on a circle
is not contained in any one of four closed consecutive marked-point arcs,
then it contains points `x,y` for which the circle can be cut once in each
marked-point arc so that the four resulting paths contain one marked point
each and `x,y` lie in opposite paths.

Here is a complete four-case verification.  Index the marked points and arcs
cyclically by `0,1,2,3`, with arc `i` joining marks `i` and `i+1`.  An
interior point of arc `i` belongs to the one-element arc-index set `{i}`; mark
`i` belongs to the two-element set `{i-1,i}`.  A family of sets of these two
forms is pairwise intersecting only if all its members have a common index:
after rotating, if it contains `{0}`, this is immediate, while if all its
members have size two, the only allowed sets are the four consecutive pairs
of a four-cycle and any pairwise-intersecting subfamily of these has a common
element.  Therefore a point set not contained in one marked-point arc has
two points whose arc-index sets are disjoint.

For those two points, choose opposite containing bags as follows.  An
interior point of arc `i` may be put in either endpoint bag `i` or `i+1`,
whereas marked point `i` is fixed in bag `i`.  Direct inspection of the
disjoint possibilities gives opposite choices: two interior points lie in
distinct arcs and are assigned to their noncommon endpoints when the arcs
are adjacent, or to an opposite endpoint pair when the arcs are opposite;
a marked point `i` can only be paired with an interior point of arc `i+1` or
`i+2`, either of which can be assigned to the opposite bag `i+2`; and two
marked points with disjoint
arc-index sets are opposite marks.  Put a cut between the two endpoint-bag
portions of every open arc (using the edge immediately before or after a
point when necessary).  This realizes all four assignments simultaneously.

Apply Observation 2 to the attachment set of `R`.  Let `x,y` be the two
attachments it supplies.  There is an `x-y` path `P` in `R` whose internal
vertices avoid `Z` (and `P=xy` when `R` is a chord).  Make the four rooted
path bags on `Z` supplied by Observation 2.  Consecutive bags are adjacent,
so their quotient is a four-cycle.  Put all internal vertices of `P` into
the bag containing `x`; this preserves connectivity and creates an edge to
the opposite bag containing `y`.  The quotient is therefore a four-cycle
plus a diagonal, namely `K_4^-`, and the four bags contain `a,b,c,d`
respectively.  This proves the theorem.  QED

## Exact bounded falsification

`rooted_k4minus_four_roots_verify.c` uses no graph library.  By label
symmetry it fixes roots `0,1,2,3`, enumerates every labelled graph through
order seven, checks three-connectivity by every deletion of at most two
vertices, and exhausts the five choices (four bags or unused) for every
nonroot vertex.  Its output is

```
n=4 three_connected_labelled=1 assignment_upper_bound=1 all_green
n=5 three_connected_labelled=26 assignment_upper_bound=130 all_green
n=6 three_connected_labelled=1768 assignment_upper_bound=44200 all_green
n=7 three_connected_labelled=225096 assignment_upper_bound=28137000 all_green
```

The source SHA-256 is pinned in
`hc7_k44_closure_local_normal_forms_audit.md`.  This is a falsification
screen only; the unbounded statement follows from the proof above.

## Scope for the literal `K_{4,4}` route

In a three-connected exterior, any four prescribed connected singleton
roots can always be expanded to a rooted `K_4^-`, but the theorem controls
neither whether the four bags span the exterior nor their core-portal
weights.  Those are exactly the extra properties required by the current
weighted completion lemmas, so this result does not by itself establish the
open core-sensitive capstone.
