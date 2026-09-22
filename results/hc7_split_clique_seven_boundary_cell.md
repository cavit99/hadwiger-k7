# Four path contacts and a seven-vertex boundary

**Status:** written proof with a separate GREEN [internal audit](hc7_split_clique_seven_boundary_cell_audit.md).
This closes an unbounded family of cells in the split-clique construction,
not the whole neighbourhood case or Hadwiger's conjecture.

All graphs are finite and simple. Neighbourhoods of sets are external.
A model rooted at a set has one distinct prescribed root in each bag.

## Theorem

Let `G` be seven-connected and contain a literal five-clique `K`.
Let `X` be a nonempty connected vertex set disjoint from `K`, with

    N_G(X)=S=T dotunion {f1,f2,f3,f4},       |T|=3.

Suppose there is a path `F` disjoint from `X union T`, containing
`f1,f2,f3,f4` in that order, which meets `K` in exactly one vertex `q`.
Assume that no vertex of `X` is adjacent to both `f1` and `f4`, and that

    alpha(G[N_G(x)]) <= d_G(x)-5                 for every x in X.  (1)

If every vertex of `X` has at least five neighbours in `S`, then `G`
contains a `K7` minor. The same conclusion holds if `G[X]` is triangle-free.

In the split-clique application, `K={u} union D` and `F` is the reserved
`p3`--`q3` path. Minimality of the reserved union excludes a common
`f1,f4` neighbour in `X`: its two-edge path would replace a segment of
at least three edges. Inequality (1) is Dirac's neighbourhood bound in
the original seven-contraction-critical graph. No quotient is assumed
to retain that bound or contraction-criticality.

## An exterior clique retaining five boundary roots

For any two of the four path contacts, put `U=T` together with those
two contacts. There is a `U`-rooted `K5` model in `G-X`.

Indeed, if five vertex-disjoint `U`--`K` paths did not exist, the set
form of Menger's theorem would give a separator `W` of order at most
four in `G-X`. Trivial paths at vertices of `U intersect K` are allowed.
Let `A` be the component of `(G-X)-W` containing the nonempty clique
`K-W`. It contains no vertex of `U-W`. Write `Z=S-U`, the two omitted
path contacts. The set `A-Z` has no neighbour in `X`, and all its other
external neighbours lie in `W union Z`. If it were nonempty, this set
of at most six vertices would separate it from `X`, contrary to
seven-connectivity. Thus `A subseteq Z`.

Only `q` can belong to both `F` and `K`. Consequently `K-W={q}` and
`W=K-{q}`. But the whole path `F` avoids `X union W` and connects `q`
to the two selected contacts in `U`, contradicting the choice of `W`.

Truncate the five disjoint paths at their first vertices of `K`. Their
five distinct ends exhaust `K`; the paths themselves are connected bags
with all ten mutual contacts supplied by the literal clique. They retain
the five distinct prescribed roots. The two omitted contacts may lie
in these bags; the constructions below use only vertices of `X` for
their additional bags.

## Two elementary constructions using the outside clique

Assume for contradiction that `G` has no `K7` minor.

**Common neighbours of an edge.** Every edge `xy` disjoint from `K` has
at most four common neighbours. Otherwise `G-{x,y}` is five-connected,
and Menger's theorem links five common neighbours disjointly to `K`.
The five path bags, followed by the adjacent singleton bags `{x},{y}`,
give a `K7` model.

**An edge covering the boundary.** Suppose `B={x,y}` is an edge in `X`
adjacent to every vertex of `S`, and `X-B` is nonempty. Let `C` be a
component of `G[X-B]`. In the five-connected graph `G-B`, take a
five-fan from any vertex of `C` to `K`. On each fan path keep only the
suffix strictly after its last vertex in `C`. These five disjoint
suffixes end at distinct vertices of `K`, so are mutually adjacent.
Each starts in `N_G(C)-B`, which is contained in `S`, and therefore
contacts both `C` and `B`. The sets `B,C` are adjacent because `X`
is connected. They and the five suffixes give a `K7` model. All bags
are nonempty and disjoint.

## Constructing both remaining bags

First assume `d_S(x)>=5` for every `x in X`. A singleton `X` would
see both extreme contacts. If `|X|=2`, seven-connectivity gives at
least six `S` neighbours at each end of its edge, hence five common
neighbours, already impossible. Thus `|X|>=3`.

If some `x` had at least six `S` neighbours, choose a neighbour `y`
in `X`. The common-neighbour bound gives

    |N_S(x) union N_S(y)| >= 6+5-4=7.

The edge `xy` would cover `S`, giving the preceding construction.
Hence every vertex of `X` has exactly five `S` neighbours. For any
edge `xy` in `X`, their `S`-neighbourhoods intersect in exactly four
vertices: five violates the common-neighbour bound, while at most
three makes their union all of `S`. These four common neighbours
also show that `xy` has no common neighbour in `X`. Thus `G[X]` is
triangle-free.

Put `A=N_X(f1)` and `B=N_X(f4)`. Both are nonempty and they are
disjoint by hypothesis. If `x in A` had no neighbour in `A`, then
`N_X(x) union {f1}` would be independent: `N_X(x)` is independent
by triangle-freeness, and none of its vertices sees `f1`. Its size
would be `d_X(x)+1`, contrary to (1), whose right side is now `d_X(x)`.
Consequently `G[A]` contains an edge. The same argument applies to `B`.

Both ends of the edge in `A` miss `f4`. Each misses exactly two
vertices of `S`, and the two missing pairs are distinct, since
otherwise the ends have five common neighbours. Their only common
missing vertex is therefore `f4`; the edge is adjacent to every
vertex of `S-{f4}`. Similarly the edge in `B` is adjacent to every
vertex of `S-{f1}`.

Join these disjoint edges by a shortest path in `G[X]`. Give the
internal path vertices to the first edge. This yields two disjoint,
connected, adjacent bags, both adjacent to every vertex of

    U=T union {f2,f3}.

The exterior `U`-rooted `K5` constructed above is disjoint from both
bags. Each helper meets each exterior bag at its prescribed root,
and their mutual contact is retained. These are all seven bags of
a `K7` model, the required contradiction.

Finally, if `G[X]` was assumed triangle-free instead, its independent
set `N_X(x)` and (1) give

    d_X(x) <= d_G(x)-5 = d_X(x)+d_S(x)-5.

Thus `d_S(x)>=5` for every `x`, reducing to the case just proved.

## Exact remaining scope

Every surviving exact cell in this construction has a vertex with
at most four boundary neighbours, and that vertex lies in a triangle
of `G[X]`, by (1). Cells of this kind, cells with additional reserved
contacts, and the final colouring of the whole host remain unresolved.
The proof is a direct construction in `G`; it introduces no induction
and makes no finite-computation assumption. It does not alter the C21
manuscript.
