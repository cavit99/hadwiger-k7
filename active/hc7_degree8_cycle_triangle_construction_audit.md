# Internal audit: reserved neighbours in the cycle-and-triangle case

**Verdict: GREEN.** The two theorems and their separator consequence hold
at the revision below. This is a separate internal mathematical audit,
not external peer review or completion of Conjecture 19 or `HC_7`.

**Audited source:** [cycle-and-triangle construction](hc7_degree8_cycle_triangle_construction.md).

**Whole-source SHA-256:**
`b3c43b4682c4554c2100d75dd14ea9df07aa898686b1cb6e3a1d9603985f68fe`.

## Inputs and quantifiers

The bipartite theorem's actual source hash is
`3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`;
both adjacent GREEN audits pin that revision. The companion-helper source
also matches the stated
`0c1ac8052f7734d8d0267381c030e177bd70010eded63d15fdca8c0db6d1f375`.
Its campaign reductions are contextual: the current theorem states its
criticality and connectivity hypotheses explicitly. No new literature
application or finite enumeration is used.

The cycle and triangle need only be spanning subgraphs of the eight-vertex
neighbourhood. The explicit independence of `S` supplies the colour lift;
no step requires the absence of any other neighbourhood edge.

Contracting the star is an actual proper minor. A six-colouring expands
properly to `F` because `S` is independent. All five other neighbours
avoid the star colour, and any repetition would let `v` be coloured.
The stronger statement about every five-colouring of `H=F-C` is also
valid: give the independent class `C` colour six; the neighbours of `v`
are exactly `S union T`, so a repetition on `T` again leaves a colour.
This does not assert that arbitrary Kempe components are connected.

## Ownership and terminal checks

1. If two transversal roots were in different bichromatic components,
   swapping one component would identify their colours, contradicting
   the proved universal distinctness. The six chosen cross paths avoid
   `C` and every foreign root. A common vertex has the colour of a
   common target endpoint. This is an actual bipartite scheme, so the
   extraction input applies without any assumed path-disjointness lift.
2. For every returned model avoiding `S`, adding `0` to `X4` and `2`
   to `X3` uses literal joining edges and distinct unused vertices.
   The three cycle-shore contacts and the triangle-shore edge are
   explicitly present; the six cross contacts survive. The rooted
   five-clique therefore exists unconditionally in this neighbourhood
   case and avoids `a0,v`.
3. If a proposed helper contains neither reserved cycle vertex, the
   completed clique and `v` form six mutually adjacent bags, and the
   helper contacts at least five of them. If it contains exactly one,
   its two cycle neighbours are the endpoints of the remaining root
   hole. The only other possible omission has disjoint ends, giving `Q`.
4. If it contains both, a minimal tree spanning `a0,0,2` has a leaf
   among `0,2`. Its transferred pendant segment contains no other
   marked vertex. Removing it leaves a connected helper through `a0`
   and the other reserved vertex. The cut edge supplies the new contact
   to the enlarged root bag; the retained marks supply all other
   required contacts. All five roots remain in distinct connected bags.

## Remaining global obligation

The `a0` component outside any such model therefore contacts at most one
cycle bag and contains neither `0` nor `2`. Its actual neighbourhood lies
in the three stated bags and `v`. At least two entire cycle bags survive
outside that neighbourhood, so it is a separator and has order at least
seven. The three bag labels do not bound its number of vertices.
No gap was found in the stated deductions. A compatible model/helper
choice or a decreasing exchange through this residue remains unproved.
