# A marked bipartite scheme completes the cycle-and-triangle configuration

**Status:** written proof; the adjacent audit records its separate internal
verdict at the exact source hash. The full critical cycle-and-triangle case
remains open: the sufficient bichromatic connections in Sections 3 and 5
are not supplied here. No external peer-review or novelty claim is made.

All graphs are finite and simple. Write `Q=K_7^=` for `K_7` with two
independent edges deleted. The sole proof input here is
[universal bipartite contractibility](bipartite_contractibility_via_matroid_reduction.md),
including its graphic-matroid Lemmas 1 and 2, at SHA-256
`3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`.
Those lemmas require neither minimum nonroot degree nor multiple path
membership. We use no additional scheme normalization.

## 1. Statement and terminal configurations

**Theorem.** Suppose a graph `G` has nine distinct vertices
`v,a0,a1,a2,0,1,2,3,4`. Suppose:

* `a0,a1,a2` span a triangle, and `0,1,2,3,4,0` is a cycle;
* `v` is adjacent to the other eight named vertices;
* `G-v` contains a `K_{3,3}` scheme rooted at shores
  `A={a0,a1,a2}` and `B={1,3,4}`, with a proper endpoint-colouring:
  each root has its target label, and each scheme path uses only its
  endpoint labels;
* each of `0,2` that belongs to the scheme union has colour `a0`.

Then `G` contains a `Q` minor. Extra host edges are allowed. No
connectivity, degree or chromatic hypothesis is imposed.

The cycle, triangle and edges incident with `v` are auxiliary host
edges: they need not be scheme edges. Throughout a nonterminal
reduction they are retained separately from the coloured scheme union.

First observe three terminal situations for a rooted `K_{3,3}` model
with bags `Y0,Y1,Y2,X1,X3,X4`, all avoiding `v`.

1. If either marked vertex `0,2` is unused, or belongs to an `X` bag,
   the model gives `Q`. Indeed, `34` already supplies an edge between
   two `X` bags. An unused `0` can be added to `X4`, and `01` supplies
   a second such edge; an unused `2` can instead be added to `X3`.
   If the marker is already in an `X` bag, its two cycle neighbours
   similarly supply an `X` contact different from `X3-X4`, whichever
   `X` bag owns it. The literal triangle supplies all three `Y`
   contacts. These six bags have at least fourteen of their fifteen
   contacts, and adding `{v}` gives `K_7^-`, hence `Q`.
2. If both markers belong to the same `Y` bag, the model gives `Q`.
   In that bag take a minimal tree spanning its prescribed triangle
   root and `0,2`. At least one marker is a leaf, say `0`. Transfer
   the pendant segment at `0`, stopping before the remaining subtree
   spanning the root and `2`, into `X4` through `04`. The retained
   tree contacts `X1,X3` through `2`, and the enlarged `X4` through
   its old cut edge. It retains its prescribed root and hence both
   other `Y` contacts. All nine cross-contacts survive or are restored;
   `01` and `34` supply two `X` contacts. Add `{v}` as before. The
   case of leaf `2` is symmetric.
3. Suppose instead we have a rooted `K_{2,3}` model with roots
   `a1,a2` and `1,3,4`, avoiding both markers and `v`, and a connected
   set `D` disjoint from it, containing `a0` and at least one marker.
   Then `Q` exists. If `D` contains `0` but not `2`, add `2` to `X3`.
   The five root bags have all contacts except possibly `X1-X4`.
   The set `D` contacts both ends of that missing pair through `0`,
   both `Y` bags through `a0`, and `{v}`. Its only possible missing
   root contact is `X3`; the two possible missing pairs are therefore
   independent. If `D` contains only `2`, interchange `0,2` and `4,3`.
   If it contains both, the tree transfer in item 2 applies to `D`.

These arguments use only explicitly disjoint connected sets. In each
case every bag used with `{v}` retains a named neighbour of `v`.

## 2. Marked component reduction

We prove the theorem by strong induction on the number of vertices in
the union `J` of the nine scheme paths. The six prescribed roots are
included. If either marker is outside `J`, use universal bipartite
contractibility inside `J` and terminal situation 1. Hence assume both
markers lie in `J`.

Let `N_A,N_B` count its nonroots with labels in the two target shores.
For either orientation form the projections of the input's Section 2.
Each projection is connected: suppressing the opposite-shore nonroots
on each incident scheme path gives a path beginning at its prescribed
root, and these paths cover its colour class. Thus the total full rank
of the `A` projections is `N_A`, and that of the `B` projections is
`N_B`. A nonroot on just one scheme path still gives a nonloop label
in its other-shore projection. In particular, neither marker needs to
have degree greater than two in `J`.

### The orientation with `A` as projected vertices

Suppose `N_A <= N_B`. Its ground set `E` consists of all `B` nonroots.
If the union rank is `N_A`, a full packing gives the rooted model
`Y_i = f^{-1}(a_i) union I_i`, with the `B` roots singleton. Both
markers lie in `Y0`, so terminal situation 2 applies.

Otherwise the union rank `R` satisfies `R<N_A<=|E|`. Lemma 1 gives a
nonempty minimizing set `X` and disjoint forests spanning every
component of every projection on `X`. Use Lemma 2 to contract the
connected sets `D_(a,K)` of coloured vertices and their allocated
labels, and delete the unallocated labels of `X`.

The vertices `a0,0,2` belong to components of the same projection.
There are two possible collisions to settle before continuing:

* If one contracted component contains `a0` and a marker, call its
  original connected preimage `D`. In the reduced scheme delete all
  vertices coloured `a0` and retain just the six paths from `a1,a2`
  to `1,3,4`. They form a `K_{2,3}` scheme. Its rooted model lifts
  disjointly from `D` and from both original markers, since every
  `a0` component was excluded. Terminal situation 3 applies in the
  original host.
* If one component contains `0,2` but not `a0`, apply universal
  bipartite contractibility to the reduced `K_{3,3}` scheme. In its
  lift the two markers are either both unused or lie in the same bag.
  Terminal situation 1 or 2 applies.

If there is no collision, all nine named vertices remain distinct.
The two markers and the root `a0` retain colour `a0`; the other roots
retain their labels. All auxiliary literal edges survive. Lemma 2
strictly decreases `|V(J)|`. If simplifying the resulting paths makes
a marker unused, situation 1 applies; otherwise the induction
hypothesis applies to this smaller marked instance.

### The orientation with `B` as projected vertices

Suppose `N_A>N_B`. Now `E` consists of the `A` nonroots and includes
`0,2`. If the union rank is `N_B`, the full packing model has the `A`
roots singleton. Each marker is therefore unused or belongs to a `B`
bag, and terminal situation 1 applies.

Otherwise write its union rank as `R<N_B`. Remove just the two marked
labels from its ground set, putting `E'=E-{0,2}`, and let `R'` be the
union rank restricted to `E'`. The projection vertex sets are unchanged;
their restricted spanning graphs need not be connected. We have

`|E'| = N_A-2 >= N_B-1 >= R >= R'`.

If `R'<|E'|`, the restricted rank formula has a nonempty minimizing
set `X subseteq E'`. Lemma 1 gives disjoint forests spanning every
component of each projection on `X`. These are precisely the full
projections' `X` components as well, so Lemma 2 applies. Its contracted
sets contain only `B`-coloured vertices and allocated labels from `X`.
Consequently neither marker nor any `A` root is contracted or deleted.
All nine names, both marked colours and the auxiliary edges survive.
The scheme order strictly decreases, giving the induction step, with
the same terminal check if path simplification makes a marker unused.

It remains that `R'=|E'|`. The displayed inequalities and `R<N_B`
force

`N_A=N_B+1`, and `R'=R=N_B-1`.

Choose disjoint independent sets allocating every label of `E'`.
Their total size is `R`, so they are a maximizing family also on the
full ground set `E`, leaving exactly `0,2` unallocated. Choose a
minimizing set `X` for the full rank formula. Equality in Lemma 1
forces every label of `E-X` to be allocated. Thus `0,2` both lie in
`X`. Lemma 1 also gives spanning forests on every `X` component.
Lemma 2 consequently produces a rooted `K_{3,3}` scheme while deleting
both markers as unallocated labels. Its rooted model lifts to one
avoiding both original markers. Terminal situation 1 applies in the
original host, using the original auxiliary cycle edges.

This exhausts both orientations. Every recursive step uses a nonempty
`X` and strictly decreases the scheme order. Each reduction contracts
pairwise disjoint connected preimages containing at most one prescribed
root; in every nonterminal step all nine named vertices remain distinct.
Composing these preimages lifts connectivity, disjointness, root
ownership and every required contact. Auxiliary edges are retained when
recursing, and terminal models are always interpreted in the host before
the terminal contraction or deletion. This completes the induction. QED

## 3. Exact critical-colouring scope

In the reserved-triple colouring of
[the degree-eight cycle-and-triangle construction](../active/hc7_degree8_cycle_triangle_construction.md),
the six paths between `{a1,a2}` and `{1,3,4}` exist and avoid the whole
colour class containing `{a0,0,2}`. If, in the same colouring, `a0` is
bichromatically connected to each of `1,3,4`, choose those three paths
as well. The six named scheme roots have distinct colours, so all nine
paths form the properly endpoint-coloured scheme in the theorem.
Consequently this stronger colouring state is terminal.

The theorem chooses its reductions and model jointly; it makes no
assertion about the ownership of markers in an arbitrary returned
`K_{3,3}` model. Section 5 weakens the sufficient colouring state to
the connection to `1` and at least one connection to `3,4`. The
outstanding critical-colouring obligation is to force that state or
a different sufficient helper construction
using the family of proper-minor six-colourings. That obligation, and
Conjectures 19, 21 and `HC_7`, remain open here.

## 4. Two auxiliary inductions with one marked vertex

For the rest of the proof fix

`H* = K_{3,3} - a0-3`, with shores `A={a0,a1,a2}`, `B={1,3,4}`.

Use the same proper endpoint-colouring and projection definitions.
All projections remain connected, with full rank totals `N_A,N_B`.
The six prescribed roots retain the literal `A` triangle and the
edge `34`, and `v` is outside the scheme and adjacent to all six roots.
Every auxiliary marker is distinct from `v`. In the preimage statements
below, `v` remains its original singleton vertex, and every scheme or
marked preimage avoids it.

We prove two auxiliary statements at every finite order before using
them in Section 5. Their inductions do not invoke Section 5.

**Auxiliary L.** Suppose additionally `14` is an actual edge and there
is a nonroot marker `m` of colour `a0`, adjacent to `1,3`. Then `Q`
exists. If `m` is outside the scheme union, its colour is immaterial.

An unused `m` is terminal: a rooted `H*` model avoiding it gains the
third `B` contact `13` by adding `m` to `X1`; only `Y0-X3` may now be
absent among the six root bags. Adding `{v}` gives `K_7^-`.
There is a second terminal configuration: a connected preimage `D`
containing `a0,m`, disjoint from a rooted `K_{2,3}` model on the other
five roots. That core has every contact except possibly `X1-X3`.
The set `D` contacts both ends of this possible missing pair, and both
`Y` bags. Its only possible missing core contact is `X4`; the two
possible missing pairs are independent after adding `{v}`.

Induct on the scheme-union order, first disposing of an unused marker.
If `N_A<=N_B`, use the `A` projections exactly as in Section 2.
A full packing puts `a0,m` in one bag and is terminal. In a deficient
packing, Lemmas 1 and 2 strictly reduce the order. If the `a0`
component absorbs `m`, delete all `a0`-coloured quotient vertices and
extract the rooted `K_{2,3}` model on the other five roots. Its lift
avoids `D`, so the second terminal configuration applies. Otherwise
the roots and marker remain distinct, with all literal edges preserved,
and induction applies after checking whether cleanup discarded `m`.

If `N_A>N_B`, use the `B` projections but restrict the ground set to
`E'=E-{m}`. A packing of rank `N_B` on `E'` gives a rooted `H*` model
with `m` unused. If its rank is smaller, then

`R'<N_B<=N_A-1=|E'|`.

The restricted rank formula therefore has a nonempty minimizing set
`X subseteq E'`. Its allocated forests span all full projections'
`X` components. Lemma 2 strictly reduces the scheme order, leaving
`m` and all `A` roots untouched. The marker remains coloured `a0`;
the auxiliary edges and all roots survive. Induction, or the unused
marker terminal case after cleanup, finishes. This proves Auxiliary L.

**Auxiliary C.** Instead suppose one current nonroot vertex `m` of
colour `a0` has a specified connected preimage containing both original
markers `0,2`. The six current root preimages contain their original
roots, are pairwise disjoint and disjoint from this marked preimage.
The original cycle and triangle edges are retained as preimage contacts.
Then the original host contains `Q`.

This is a statement about an explicit minor of the original decorated
host, with its disjoint connected preimages retained. All subsequent
contractions compose those preimages. If `m` is unused by a rooted
`H*` model, both original markers are unused in its lift. Add `0` to
`X4` and `2` to `X3`: all three `B` contacts now exist, so only
`Y0-X3` may be missing. This is terminal. If a connected component
preimage contains both `a0` and `m`, it contains `a0,0,2` in the
original host. Extract the other five rooted bags by deleting all
`a0`-coloured quotient vertices. The tree transfer in terminal
situation 3 of Section 1 gives `Q` in the original host.

The induction is otherwise identical to Auxiliary L: in the `A`
orientation a full packing or root-marker collision is terminal; in
the `B` orientation test for a full packing on `E-{m}`. Such a
packing leaves `m` unused. If it does not exist, the same displayed
strict rank inequality supplies a nonempty reduction avoiding `m`.
Thus a nonterminal step never splits the marked preimage or assigns it
to a `B` component. Scheme order strictly decreases. A full reverse
packing that uses `m` is neither needed nor asserted to be terminal.
This proves Auxiliary C, including every preimage lift.

## 5. The common cycle neighbour and one further connection suffice

**Theorem (two-path strengthening).** In the theorem of Section 1,
replace the `K_{3,3}` scheme by an `H*` scheme: the path `a0-3` is
not required. Then `Q` still exists. By reflecting the cycle, the
same is true when `a0-4` is omitted. In both versions the path `a0-1`
is required. No assertion is made here for omitting `a0-1`.

**Proof.** Induct on the `H*` scheme-union order, using the already
proved auxiliaries at any order. If `2` is unused, extract a rooted
`H*` model avoiding it and add `2` to `X3`. The six root bags may
miss only `Y0-X3` and `X1-X4`, which are independent. Adding `{v}`
gives `Q`, regardless of the ownership of `0`.

If `0` is unused, keep it outside the scheme and contract `04` into
the root `4`; the edge `01` supplies the new literal edge `14`.
No scheme vertex other than the root `4` is changed. Auxiliary L
with marker `2` now applies. This transition may leave scheme order
unchanged, but invokes a separately proved auxiliary theorem, not the
induction hypothesis.

Assume both markers are used. If `N_A<=N_B`, perform the `A`-projection
step of Section 2. A full packing puts `a0,0,2` in one bag. Delete
that bag except for a minimal tree spanning those three vertices;
terminal situation 3 gives `Q` using the other five bags. In a
deficient packing use Lemmas 1 and 2. A component collision between
`a0` and a marker is terminal by the same situation, extracting the
other five bags after deleting the `a0` colour. A component collision
between `0,2` but not `a0` gives exactly Auxiliary C, with that
component's connected preimage as its marked object. With no
collision the smaller marked instance retains the original hypotheses.

If `N_A>N_B`, restrict the `B`-projection ground set to `E'=E-{2}`.
A packing of rank `N_B` on `E'` leaves `2` unused and is terminal as
above. Otherwise `R'<N_B<=N_A-1=|E'|`, so the restricted minimizer
is nonempty and Lemma 2 applies while leaving `2` untouched.

If `0` survives as a separate `a0`-coloured vertex, all nine names
and their literal edges survive, and the smaller marked instance
allows induction (with the preceding unused-marker checks).
There are two other outcomes, both giving Auxiliary L:

* If `0` is allocated to a contracted `B` component, that component
  has colour `1` or `4`: the label `0`, of colour `a0`, can occur
  only in the projections of those two actual incident target edges.
  Its image has an auxiliary edge to the root of that same colour,
  through `01` or `04`. Contract this monochromatic edge if its ends
  are distinct. The opposite auxiliary edge now supplies `14`.
  This merges at most one prescribed root and does not touch `2`.
  Every scheme path maps to a two-colour walk; simplifying it retains
  the scheme and its roots. No other root has the merged colour.
* If `0` was an unallocated label of the minimizing set, Lemma 2
  deletes it from the scheme. Instead retain its preimage outside
  the reduced scheme and join it to the root-`4` preimage through
  `04`. All allocated component preimages and `2` are disjoint from
  it. Again `01` supplies `14`, and no scheme path is altered except
  for the root's enlarged preimage.

In both cases the resulting properly coloured `H*` scheme, literal
`A` triangle, literal edges `14,34` and unchanged marker `2` satisfy
Auxiliary L. These auxiliary contractions never require an increase
in scheme order. Every invocation of this theorem's own induction
hypothesis follows a nonempty Lemma 2 reduction and strictly decreases
that order. All lifts use the specified disjoint connected preimages,
including the terminal transfers in Auxiliary C. The two auxiliary
inductions have no dependence on this theorem, so no state transition
creates an induction cycle. This completes the proof. QED

Consequently, in the reserved-triple critical colouring, it suffices
that `a0` be bichromatically connected to `1` and to at least one of
`3,4`. Under target exclusion this conjunction fails in every such
colouring. Connections only to `3,4` are not covered by the proof.
Forcing a terminal colouring or another sufficient helper still
requires a global argument using the actual critical host.
