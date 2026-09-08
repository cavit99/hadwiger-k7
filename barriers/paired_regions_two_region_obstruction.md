# Two full regions need not give a paired four-cycle

**Status:** explicit counterexample with a written proof and a
[separate internal audit](paired_regions_two_region_obstruction_audit.md).
No computation is a premise.

## Refuted conclusion

The following assertion is false even for `k=4,t=2`:

> If R,S are disjoint k-vertex sets with k vertex-disjoint R--S paths,
> and t disjoint connected nonterminal regions are each full to all
> `2k` terminals, then there are k disjoint connected paired bags whose
> contact graph has minimum degree at least t.

A **paired bag** contains exactly one R vertex and exactly one S vertex;
the pairing is free. The contact graph has one vertex per bag, with an
edge for every actual host edge between bags. For four bags, minimum
degree at least two is equivalent to containing a four-cycle, or to
containing `K_4` with at most two independent edges deleted. The example
therefore also refutes the proposed `k-2`-region conclusion with a
matching of missing edges, including its stronger two-hole version.

## The graph and its hypotheses

The vertex set is `{0,...,14}`, with

`R={0,1,2,3}`, `S={4,5,6,7}`.

The two regions are the paths

`U: 8--9--11--10`, `V: 12--13--14`.

There are three additional edges between the regions:

`8--13`, `11--12`, `11--14`.

The terminal neighbourhoods are exactly those in the table, and there
are no other edges.

| Terminal | Neighbours |
|---|---|
| 0 | 8,12 |
| 1 | 9,12 |
| 2 | 10,12 |
| 3 | 10,12 |
| 4 | 9,13,14 |
| 5 | 9,14 |
| 6 | 10,14 |
| 7 | 10,14 |

Thus U,V are disjoint connected sets avoiding all eight terminals, and
every terminal has a neighbour in each region. The four paths

`0--8--13--4`, `1--9--5`, `2--10--6`, `3--12--11--14--7`

are vertex-disjoint and use all terminals as distinct ends. In particular
the required R--S linkage number is four.

## Every paired model has a leaf

Consider any four disjoint connected paired bags, allowing arbitrary
foreign vertices and unused vertices. Roots 2 and 3 have only neighbours
10 and 12. Their two bags must therefore contain 10 and 12 separately.
Call these bags A and X, respectively. Consequently the bags at roots
0 and 1 contain 8 and 9, respectively, since 12 is already owned by X.

Likewise, the bags at roots 6 and 7 must contain 10 and 14 separately.
Thus A contains one of 6,7, and the bag Y containing 14 contains the
other. Root 5 must belong to the bag containing 9: its only other
neighbour is 14, whose bag already owns a different S terminal. The
bag containing 9 is therefore rooted at 1 and 5.

Suppose first that `X!=Y`. Then Y must be the bag rooted at 0, since
the other R roots already belong to A, X and the bag rooted at 1.
Hence Y contains 8 and 14. The only remaining S terminal, 4, belongs
to X. Since 9 and 14 lie in other bags, root 4 forces 13 into X.
But `{0,8}` has no exit within Y: its only external neighbours are
12,9,13, all owned by other bags. It cannot connect to 14. This
contradicts connectedness, so `X=Y`.

Now X contains 12 and 14, one of 2,3, and one of 6,7. The bag rooted
at 0 must contain 4, and the neighbourhood of 4 forces it to contain
13, since 9 and 14 are elsewhere. Thus X cannot use 8,9,10 or 13,
nor any terminal besides its own two. With those vertices unavailable,
connecting 12 to 14 requires 11. Hence `11 in X`.

All neighbours of 10 are now either in A or X: they are 11,2,3,6,7.
The only vertices reachable from 10 within A are 10 and its own R and
S terminals. Those terminals also have all their external neighbours
in X. Consequently A has exactly one neighbour in the contact graph,
namely X. No paired model has minimum degree at least two.

For completeness, paired models do exist. One is

`{0,8,13,4}`, `{1,9,5}`, `{2,10,6}`, `{3,12,11,14,7}`.

Its contact graph is a triangle on the first, second and fourth bags
with the third bag attached only to the fourth. The proof above in
fact forces this contact graph in every paired model, with only the
choices of roots 2,3 and 6,7 in A and X changing.

## A counterexample for every k at least four

For any `k>=4`, enlarge each of the twin terminal classes `{2,3}` and
`{6,7}` to size `k-2`, with their old neighbourhoods unchanged. Add
`k-4` new vertices Z, each adjacent to every terminal, and no other
edges. Use U,V and the singleton Z vertices as the `k-2` full regions.
The graph has `3k+3` vertices. The old four paths, using two roots from
each enlarged class, together with one new terminal pair through each
Z vertex give a k-linkage.

The large R class has exactly the `k-2` neighbours `{10,12} union Z`.
They must occur in distinct bags, one for each of its roots. The large
S class similarly forces `{10,14} union Z` into distinct bags. Every
Z bag therefore owns a root from each large class and is unavailable
to roots 0,1,4,5. The preceding four-bag forcing applies unchanged to
the remaining bags, assigning all seven old nonterminals as before.
Each Z bag is universal in the contact graph through its terminal
edges. Hence every paired contact graph is exactly `K_k` with two
edges having a common endpoint deleted, and its minimum degree is
`k-3`. This is an unbounded family, not an extrapolation from a finite
check.

## The abstract clique-boundary variant also fails

Modify the original 15-vertex graph by deleting `3--10` and adding the
three clique edges on `K={0,1,3}`. Keep `2--12` and set `r=2`, retaining
`R=K union {r}` and the same S.
The two sets

`H_1={0,1,8,9,11,10}`, `H_2={3,12,13,14}`

are disjoint, connected, full to S, and avoid r and S. They cover K
and each contains a K vertex. The displayed four-linkage is unchanged.
Thus this graph satisfies the proposed abstract clique-boundary state:
a literal `(k-1)`-clique K, a further R root r, `k-2` regions full to S
and covering K, and a full linkage from `K union {r}` to S.

Nevertheless there is no paired `K_4` with at most one missing edge.
An added clique edge cannot be internal to any paired bag, since its
two endpoints are distinct R terminals. The preceding forcing argument
therefore still applies to connected bags. Root 3 has only non-K
neighbour 12, forcing 12 into its bag and 10 into the r bag A. The
three added clique edges have no endpoint in A and create no new
contact for it. A still has exactly one neighbouring bag. In particular,
the literal clique on the other three R roots does not supply the two
contacts needed at r.

Even a two-fan from r to S avoiding K is present: its paths are
`2--10--6` and `2--12--13--4`. They share only r and have distinct S
ends. Thus adding this root-clean fan hypothesis does not repair the
abstract conclusion. Its second path uses 12, which is necessarily
owned by the bag at the different R root 3; the fan cannot be allocated
independently of the paired model.

This refutes the stated abstract state. It does not assert that the
modified graph arises from a tight-cut replacement in a host retaining
all the original two-sided fullness or critical-host hypotheses.

## Failed inference and unaffected scope

With `k-1` full regions, the cut-chain proof makes every region's
occurrence-interval graph a forest: a cut contains at most two vertices
of a region. Connectedness then forces the actual region to equal that
forest. With `k-2` regions a region can occur three times in a cut; its
interval graph can have a connected proper spanning subgraph. The
clique-contact inference no longer follows. More directly, contacts
with different full regions can all reach the same other paired bag,
as they do from A in this example.

The proved [k-1 full-region theorem](../results/paired_clique_full_regions.md)
and [one-sided theorem](../results/paired_clique_one_sided_regions.md)
are unaffected. This graph has only two full nonterminal regions for
four terminal pairs, and the one-sided theorem would require three
regions full to one terminal set and covering the other.
No critical-colouring, high-degree or C19 host hypotheses are asserted
for this graph. It is not a counterexample to C19, HC7, rooted K5
contractibility or the project's global objective.
