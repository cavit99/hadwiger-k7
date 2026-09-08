# Disjoint full regions force a clique joining two terminal sets

**Status:** written proof with separate internal reviews recorded in
the adjacent audit. The theorem concerns arbitrary finite host order and terminal-set
size. No claim about prior literature or the project's global objective
is made here.

All graphs are finite and simple. For disjoint vertex sets `R,S`, write
`kappa_G(R,S)` for the maximum number of pairwise vertex-disjoint `R`–`S`
paths with distinct endpoints in both sets. A set is **full to** `R union S`
if every vertex of `R union S` has an actual neighbour in that set.

## Theorem

Let `k>=1`, and let `R,S` be disjoint k-vertex sets in a graph `G` with
`kappa_G(R,S)>=k`. Suppose there are `k-1` pairwise disjoint nonempty
connected vertex sets `H_1,...,H_(k-1)` avoiding `R union S`, each full
to `R union S`.

Then `G` contains k pairwise disjoint nonempty connected bags that are
pairwise adjacent, each containing exactly one vertex of `R` and exactly
one vertex of `S`. The pairing between `R` and `S` is not prescribed. Conversely, choosing
a terminal-to-terminal path in each bag gives a k-linkage, so the
linkage and paired clique conditions are equivalent under the region hypothesis.

No connectivity assumption on the whole graph is required. For `k=1`
the region hypothesis is empty. For `k=3` this recovers the
[two-region theorem](two_full_regions_paired_triangle.md);
the proof below is self-contained apart from vertex Menger's theorem.

## 1. Minimality and terminal constructions

For `k=1`, an `R`–`S` path is the required bag. Suppose the theorem fails.
Choose a counterexample with k minimum, then with `|V(G)|` minimum.
Thus `k>=2`. A full k-path linkage uses all `2k` terminals as its distinct
ends, so no terminal lies internally on any of its paths.

Two terminal constructions will be used.

First, if an `R`–`S` path avoids all regions and has no other terminal
internally, take it as one bag. Assign each of the remaining `k-1`
terminal pairs to a different region, adjoining the pair to that region.
Each resulting bag is connected. Any two region bags are adjacent through
their terminals, and each sees the first bag through its terminal ends.
This gives the required k bags. In particular, no literal `R`–`S` edge
can occur in the counterexample.

Second, suppose deleting one region `H_j` leaves `k-1` disjoint `R`–`S`
paths. Trim each path to a segment with one endpoint in each terminal
set and no other terminal internally. Their endpoints are still distinct;
let `r in R,s in S` be the two unused terminals. In

`G-(H_j union {r,s})`,

these paths give a `(k-1)`-linkage between `R-{r}` and `S-{s}`. The other
`k-2` regions remain connected, disjoint and full to those terminals.
Minimality of k supplies `k-1` paired clique bags in this graph. Adjoin
the final bag `H_j union {r,s}`. It is connected and sees every other
bag through that bag's terminals. Both unused terminals were deleted
before induction, so no earlier bag can contain either of them.

Consequently no region is a singleton: deleting its one vertex leaves
at least `k-1` paths of any full linkage intact, invoking the second
construction.

We may make the regions cover all nonterminals. Consider a component
`C` outside all regions and all terminals. If it contacts a region,
absorb it into that region, preserving all hypotheses. Otherwise its
boundary is contained in `R union S`. If it contacts both terminal sets,
it contains the interior of a path for the first construction. If it
contacts at most one set, every full k-linkage avoids it: entering and
leaving C would put a terminal internally on a linkage path. Deleting
C then preserves all hypotheses, contradicting minimum host order.
After absorbing components as needed, we therefore have

`V(G) = R disjoint-union S disjoint-union H_1 ... disjoint-union H_(k-1)`.

The graph is unchanged by absorption, and every region still has at
least two vertices.

## 2. Region edges give internal separators

Let `xy` be an edge within a region `H_j`. Contracting it preserves the
terminals and the `k-1` disjoint connected full regions. If the quotient
still has a k-linkage, minimum host order gives its paired clique model.
Replacing the contracted vertex by the connected preimage `{x,y}` lifts
that model, preserving all terminal ownership. Hence

`kappa_(G/xy)(R,S)<=k-1`.

By vertex Menger, the quotient has an `R`–`S` separator of order at most
`k-1`. It contains the contracted vertex; otherwise it lifts to a cut
of that same size in G. Replacing the contracted vertex by x and y
gives a separator in G of order at most k. Since G has a k-linkage,
the lifted separator has exactly k vertices.

It contains x and y and meets every other region. Indeed, an untouched
connected full region would join a surviving R terminal to a surviving
S terminal; even if all the other `k-2` cut vertices were terminals,
terminals in both sets would survive. There are exactly `k-2` other
regions and exactly `k-2` remaining cut vertices. The separator therefore
contains exactly one vertex of each other region and no terminal.

Fix a k-linkage `P_1,...,P_k`, oriented from R to S. Each separator just
obtained meets every path exactly once. In particular, the ends of a
region edge lie on different paths. Every region vertex has a neighbour
within its region, so every region vertex occurs in one of these cuts
and lies on the linkage. Thus the linkage spans all of G. Each path
has an internal vertex, since literal `R`–`S` edges were excluded.

## 3. A maximal chain of internal separators

Consider all `R`–`S` separators consisting of one internal vertex from
each `P_i`. Represent such a cut by its k positions along the oriented
paths, and order vectors coordinatewise. This collection is nonempty
by Section 2. Only internal cuts are considered in what follows.

Since the paths span G, a vector is separating exactly when no edge
joins a vertex strictly before its selected position on one path to
a vertex strictly after its selected position on another path, allowing
the two paths to be the same. Each strict prefix connects to its R end,
and each strict suffix connects to its S end.

The separating vectors are closed under coordinatewise minimum and
maximum. For a crossing edge at the minimum vector, its prefix end
is before both original cuts on its path. Choose the original cut
attaining the minimum at the suffix end's path; the same edge crosses
that cut. This is impossible. The maximum case is symmetric, choosing
the cut attaining the maximum at the prefix end.

Choose a maximal chain of separating vectors, written

`C^0 < C^1 < ... < C^m`.

It includes the minimum and maximum vectors of this finite lattice.
Every region vertex occurs in a cut on the chain. To see this, let
z lie on `P_i` and choose a cut Z containing z, available by Section 2.
If the chain skipped its position, there would be consecutive cuts
`C<D` with `C_i<z<D_i`. The separating vector

`(Z maximum C) minimum D`

lies between C and D and has i-coordinate z, contradicting maximality
of the chain. The chain's extreme cuts rule out skipping z at either
end. For each region vertex z, the indices of chain cuts containing z
therefore form a nonempty interval `I_z` of integers.

Every region edge `uv` satisfies `I_u intersect I_v != empty`. Suppose
otherwise, and let r be the last index in `I_u` and l the first in
`I_v`, with `r<l` after interchanging u and v. At `C^(r+1)`, u lies
strictly in a prefix. The actual edge uv prevents v from lying strictly
in a suffix. Hence `l=r+1`: this next cut contains v. Section 2 supplies
a cut Z containing both u and v, on different paths. The vector

`(Z maximum C^r) minimum C^(r+1)`

contains both u and v and lies between the two consecutive cuts. It
differs from the first at v's coordinate and from the second at u's
coordinate, a contradiction. The use of the actual edge uv here is
essential; a common cut alone would not force interval intersection.

## 4. Each region is its interval tree

Every internal cut meets every region, since an intact full region
would connect R to S while avoiding it. A chain cut has k vertices
and there are `k-1` regions. It therefore contains at most two vertices
of any one region.

For a fixed region, form the intersection graph of its intervals `I_z`.
No three intervals have a common index. This intersection graph is a
forest. Indeed, in any cycle choose an interval with smallest right
endpoint. Its two neighbours on the cycle both contain that endpoint:
their right endpoints are no smaller, and each meets the chosen interval.
Those three intervals would have a common index, a contradiction.

Every actual edge of the region is an edge of this forest by Section 3.
The region is connected and spans the same vertex set. A forest with a
connected spanning subgraph is a tree and has no additional edges beyond
that subgraph. Thus two vertices in the same region are actually adjacent
whenever their intervals overlap.

Let `f_i` be the first internal vertex of `P_i`. Each `f_i` lies in an
internal cut, so taking the coordinatewise minimum of one such cut for
each i shows that `F={f_1,...,f_k}` is a cut. It is the minimum vector
and belongs to the chain. Consequently any two vertices of F in the
same region are adjacent.

Every region neighbour of an R terminal belongs to F. A neighbour later
on its path would have a suffix to S avoiding F, contradicting that F
separates R from S. Since every region is represented in F, exactly one
region is represented twice and every other region once.

The k linkage paths are now pairwise adjacent. If `f_i,f_j` belong to
the same region, they are joined by an actual edge. If they belong to
different regions, at least one of those regions has a unique vertex
in F. The R terminal of the other path is full to that region, and all
its neighbours there lie in F, so it is adjacent to that unique vertex.
The paths themselves are therefore the required k paired clique bags.

This contradicts minimality and proves the theorem. The only induction
steps were deletion with both unused terminals reserved, and contraction
of an edge inside a region with its fixed connected nonterminal preimage.
Every resulting model retains exactly one original terminal from each
set in every bag.

## 5. The number of regions is sharp

For every `k>=2`, the conclusion can fail with only `k-2` full regions.
Take k disjoint edges `r_i s_i`, with `R={r_1,...,r_k}` and
`S={s_1,...,s_k}`, and add `k-2` vertices, each adjacent to all `2k`
terminals. There are no other edges. The matching gives
`kappa_G(R,S)=k`, and each added vertex is a connected full region.

In any proposed k-bag model, at least two bags contain no added vertex.
Each such bag consists of exactly one R terminal and one S terminal;
connectedness forces it to be an individual matching edge. Those two
bags have no edge between them. Thus the required paired clique does
not exist, proving that `k-1` full regions cannot be replaced by `k-2`.

## 6. Constructive consequence

When the regions are supplied, the paired clique can be found in
polynomial time. Vertex-capacitated maximum flow finds the required
linkages and tests whether a contracted graph still has k disjoint
terminal paths.

For `k=1`, return a path. Otherwise perform the component absorption or
deletion of Section 1, returning
its direct construction if an outside component or a literal edge gives
a path avoiding all regions. If a region is a singleton, retain `k-1`
paths of a full linkage avoiding its vertex, reserve their unused terminal
pair, and recurse with k decreased by one as in Section 1. Otherwise test
every edge within a region. If some contraction preserves a k-linkage,
recurse on that quotient and lift its bags through the contracted edge.

If all those edge contractions fail, Sections 2–4 apply directly: their
only use of minimum host order was to establish these failures. Any
k-linkage then spans the normalised graph and its paths are pairwise
adjacent, so return those paths as the bags. The algorithm does not
enumerate the cut lattice or its maximal chains.

Each recursive call strictly reduces the number of vertices, so there
are at most `|V(G)|` calls. Each call uses polynomially many flow tests
and elementary graph operations. Component deletions and all lifts also
take polynomial time. This proves the claimed algorithmic consequence
without any assumption that the terminal pairing was specified.
