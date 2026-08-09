# Independent audit: tri-separation reduction of the rooted-web cut

**Verdict:** **GREEN** for the exact revision below.

**Audited source:**
[`hc7_k7minus_four_centre_tri_separation_reduction.md`](hc7_k7minus_four_centre_tri_separation_reduction.md)

**Mathematical revision SHA-256:**

```text
aa675edd6356a0f619bfbdd3c4307092c8f12b96e0f7eba7d8e956c7a0d65bc5
```

After the GREEN verdict, only the opening status was changed to link this
audit.  The promoted source SHA-256 is

```text
b5b0ff71e8942d4b16674a25362c9459523c4c7460f15176892d4ded8a82b682
```

This is a separate internal mathematical audit, not external peer review.
No mathematical defect was found.  The result is an unlabelled structural
normalization; it does not eliminate the rooted-web outcome.

## Reduction and lifted separator

The exact cut gives a proper three-separation
`(C union T,D union T)` of the three-connected graph `H=G-U`, with `C,D`
connected and anticomplete.  For `X` equal to either component, every
neighbour outside `H[X union T]` lies in the four-set `U`, so every vertex
of `X` has at least four neighbours in that closed side.  If the side were
a forest, degree summation would give `|X|<=2`; a singleton has at most
three available neighbours, while two connected vertices of closed-side
degree at least four form a triangle with every member of `T`.  Both sides
therefore contain cycles.

Carmesin--Kurkofka Lemma 1.3.4 makes the deficient side and its unique
open-side neighbour well defined.  Definition 1.3.5 then gives exactly the
sets `T_C,T_D,T_0`, the reduced sides in (2.2), and the three mixed
separator elements in (2.3).  A boundary vertex moved into one open side
has at least two neighbours in its original component there, so both
reduced open sides are connected.  Nontriviality survives reduction, and
`delta(H)>=4` makes every vertex element of the separator strong.

Placing all four vertices of `U` in both sides adds four vertex elements
and no new crossing edge.  Thus (2.6) is a mixed separation of `G` of order
seven, but need not be an ordinary vertex separation.

## Carmesin--Kurkofka anchors

The audit checked the cited claims against the published paper,
*Canonical Decompositions of 3-Connected Graphs*, Advances in
Combinatorics 2025:7, <https://doi.org/10.19086/aic.2025.7>:

- Definition 1.1.1 gives tri-separation, nontriviality and strongness;
- Lemma 1.3.4 and Definition 1.3.5 give the canonical reduction;
- Section 1.2 gives the mixed-tree-decomposition associated with a nested
  symmetric separation system;
- Lemmas 1.4.8 and 1.4.11 give the one-vertex centre, four size-one links,
  and absence of diagonal and jumping edges;
- Lemmas 2.2.3 and 2.2.5 give exclusivity and uniqueness of the interlaced
  splitting star; and
- Theorem 2.2.8(ii) gives the wheel compressed torso and generalized-wheel
  expanded torso in the heavily interlaced case.

For a reduction `q` not in `N(H)`, symmetry and nestedness orient every
member of `N(H)` below `q` or its inverse.  Finiteness supplies maximal
such members; nestedness makes them a star, and maximality gives the
splitting property.  Hence `q` interlaces that star.  Lemma 2.2.5 makes it
unique, and the strong, nontrivial, half-connected reduction interlaces it
heavily.  If `q` belongs to `N(H)`, Lemma 2.2.3 prevents it from
interlacing a splitting star, so the two outcomes are exclusive.

## Pinned local inputs and scope

```text
four-centre rooted-web theorem
e7fcf00c9bdbd2fcbab78bb13d4244a659f4f7db0ae45a97cfbd9a8d599a0ee3

boundary-provenance counterexample (current audited source)
08f89cfcfdd097044a00c6b5969e90ea8a2e1337c7614020d0899affa9797f19

boundary-provenance counterexample audit
75ed63f1ba34dc8dbc9953a3826b97a58b7b5abc527b596908e9497982c09c58
```

The earlier pin
`571bbc768500fb9ca38a97f537586309f382f6317c0e6a45f6a208fe8458c9a2`
identified a working revision of the same counterexample.  The current
audited revision does not change the graph, the two ordinary separations,
their common reduction or the lost-boundary conclusion; it tightens the
connectivity presentation and states the scope and endpoint provenance more
precisely.  This audit relies on the current exact source above.

The counterexample has eleven vertices, twenty-four edges, minimum degree
four and connectivity three.  Its two distinct nontrivial ordinary
three-separations have the same strong nontrivial reduction, so an
undecorated reduction does not recover the original boundary endpoint.

The labelled interface in Section 4 faithfully records the data already
proved by the rooted-web theorem: the inverse boundary map, the oriented
accepted side and its `(j,gamma)` trace, the ordered rooted terminals, and
one crossing colour-pair with a named vertex of `U-{r}` in its bichromatic
component.  The colouring and colour-pair determine that component.  The
source correctly presents preservation of this interface as future work;
it does not identify the generalized-wheel apex in `H` with the named
vertex in `U`.

Two obligations remain unresolved:

1. In the canonical-decomposition branch, unreduction or passage to a
   strictly inner adhesion must preserve the literal boundary, accepted
   colouring trace, ordered roots and named Kempe datum while yielding a
   rooted augmentation, strict descent or a common boundary colouring.
2. In the generalized-wheel branch, lifting through the expanded torso
   must preserve the same data and return one of those three outcomes.

The audited theorem proves neither obligation, a `K_7^-` minor, the
`K_7^-` six-colour conjecture, nor Hadwiger's conjecture for `t=7`.
