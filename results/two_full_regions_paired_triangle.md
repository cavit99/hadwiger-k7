# Two full regions force a triangle joining two terminal triples

**Status:** written proof; separate internal audit recorded beside it.
The theorem below does not establish K5 contractibility.

All graphs are finite and simple. Two vertex sets are adjacent if an
actual edge joins them. Write `kappa_G(R,S)` for the maximum number of
pairwise vertex-disjoint paths joining `R` to `S`, with distinct endpoints
in each set.

## Theorem

Let `R,S` be disjoint three-vertex sets in a graph `G`, and suppose
`kappa_G(R,S)>=3`. Let `U,V` be disjoint connected sets avoiding `R union S`.
Suppose every vertex of `R union S` has a neighbour in each of `U,V`.
Then there are three pairwise disjoint connected, pairwise adjacent bags,
each containing exactly one vertex of `R` and exactly one vertex of `S`.
The pairing between `R` and `S` is not prescribed.

In particular, three-connectivity of the whole graph is sufficient but
is not required. No colouring or scheme hypothesis is used.

## Proof

Suppose a counterexample exists and choose one with minimum `|V(G)|`.
Every three-path `R`--`S` linkage uses all six terminals as its distinct
ends, so no terminal lies internally on any of its paths.

First note two elementary terminal constructions.

* If an `R`--`S` path with no other terminal internally avoids both hubs,
  take it as one bag and append one of the two remaining terminal pairs
  to each hub. These three bags are connected and pairwise adjacent:
  each hub sees the path's ends, and also the terminals in the other hub's
  bag.
* If `G-V` has two disjoint `R`--`S` paths, trim them so no other terminal
  lies internally, then join their union through `U`.
  The union with `U` is connected because `U` meets or neighbours both
  paths. Starting with the two paths, grow two disjoint connected sets
  to partition this union; the resulting sets are adjacent. The third
  bag is `V` with the unused terminal pair. It sees each of the first
  two bags through their terminals. This construction is symmetric.

We may assume the hubs cover every nonterminal. Indeed, consider a
component `C` of `G-(U union V union R union S)`. If it contacts a hub,
add it to that hub. Otherwise its boundary is contained in `R union S`.
If it contacts both terminal sets, the first construction applies.
If it contacts at most one, every three-path linkage avoids it: entering
and leaving it would put another terminal of that same set internally
on a linkage path. Deleting `C` therefore preserves a three-path linkage
and both full hubs, contradicting minimum order. Absorbing all remaining
components gives

`V(G) = R disjoint-union S disjoint-union U disjoint-union V`.

Neither hub is a singleton. Deleting a singleton hub from any three-path
linkage leaves at least two of its paths intact, giving the second
construction. Also, a literal `R`--`S` edge would give the first
construction. Thus every linkage path has an internal vertex.

### Edge contractions give exact three-vertex separators

Let `xy` be an edge with both ends in `U`. Contracting it preserves the
six distinct terminals and the two disjoint connected full hubs. Any
three-bag model in the quotient lifts through the connected preimage
`{x,y}` and preserves every terminal's ownership. Hence minimum order
implies `kappa_(G/xy)(R,S)<=2`.

By the vertex version of Menger's theorem, the quotient has a separator
of order at most two between the terminal sets. It must contain the
contracted vertex: otherwise it lifts to a separator of the same order
in `G`. It has exactly one other vertex `z`, since otherwise its lift
`{x,y}` contradicts `kappa_G(R,S)>=3`. Consequently

`{x,y,z}` is an `R`--`S` separator in `G`.

Moreover `z` belongs to `V`. If not, the connected set `V` survives the
separator and joins a surviving `R` terminal to a surviving `S` terminal;
at most the vertex `z` could remove a terminal. This is a contradiction.
Thus every internal `U` edge belongs to a separator consisting of its
two ends and one vertex of `V`; the symmetric assertion holds for `V`.

Fix three disjoint linkage paths `P_1,P_2,P_3`, oriented from `R` to `S`.
Every separator just constructed meets each path exactly once, since
it has three vertices. Both ends of every internal hub edge therefore
lie on different linkage paths. Every hub vertex has a neighbour in
its hub, because that hub is connected and has at least two vertices.
It follows that every vertex of `G` lies on the linkage.

If the three paths are pairwise adjacent, they already give the desired
bags. Otherwise relabel a nonadjacent pair as `P_1,P_3`. There is no edge
between these two paths.

### Uncrossing the separators

A separator with one internal vertex on each `P_i` is described by its
three positions along the oriented paths. Because the paths span `G`,
such a vector is a separator precisely when no edge joins a vertex
strictly before the chosen position on one path to a vertex strictly
after the chosen position on another path (or on the same path).
Each prefix connects to its `R` end and each suffix to its `S` end.

These separating vectors are closed under coordinatewise minimum.
For if an edge crossed the minimum vector, its prefix end would be
before both original positions on its path. Choose the original vector
attaining the smaller position at the suffix end's path. The same edge
would cross that original separator, which is impossible.

Let `f_i` be the first internal vertex of `P_i`. Each `f_i` belongs to
one of the edge separators above. Taking the coordinatewise minimum of
three such separators, one containing each `f_i`, shows that

`F={f_1,f_2,f_3}` is an `R`--`S` separator.

Every hub neighbour of an `R` terminal must consequently lie in `F`:
any later internal vertex has a suffix to an `S` terminal avoiding `F`.
The `R` end of `P_1` has neighbours in both hubs, but none on `P_3`.
Thus `f_1,f_2` lie in opposite hubs. Similarly `f_2,f_3` lie in opposite
hubs. Interchanging the hub names if necessary, we have

`f_1,f_3 in U`, and `f_2 in V`.

Choose a neighbour `x` of `f_1` within `U` and a neighbour `y` of `f_3`
within `U`. Internal hub edges cannot have both ends on one linkage
path, and there are no `P_1`--`P_3` edges. Hence `x,y` both lie on `P_2`.
Their edge separators have position vectors

`(f_1,x,z_3)` and `(z_1,y,f_3)`, where `z_1,z_3 in V`.

Here `z_1` is later than `f_1`, and `z_3` is later than `f_3`, since their
hub memberships differ. Their coordinatewise minimum is therefore

`(f_1, the earlier of x and y on P_2, f_3)`.

This is an `R`--`S` separator contained entirely in `U`. But the intact
connected full hub `V` joins the two terminal sets while avoiding it.
The contradiction proves the theorem. All contractions used above have
fixed connected nonterminal preimages, so the minimality argument
preserves the six original terminals separately throughout.

## Scope

The theorem supplies the terminal construction when a K5-scheme
allocation produces two actual disjoint regions full to its six roots
and ports. It does not prove that every reverse forest packing is full,
or justify a deficient-packing reduction whose labels are not independent
in the whole scheme host. Those are separate application obligations.
