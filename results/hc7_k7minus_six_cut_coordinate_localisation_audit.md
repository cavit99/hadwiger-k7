# Internal audit: singleton-coordinate localisation at a lifted six-cut

**Verdict:** **GREEN** for Theorem 1.1, Corollaries 2.1 and 3.1,
Lemma 4.1, Theorem 4.2, Corollary 4.3, and the stated trust boundary.  This
is a separate internal mathematical audit, not external peer review.

## Exact revision

The audited source is
[`hc7_k7minus_six_cut_coordinate_localisation.md`](hc7_k7minus_six_cut_coordinate_localisation.md),
with SHA-256

```text
b2803d6cabf6684aaa0af8487be66ab7ac738909719028fd304f29b1b9682555
```

The dependencies used in the proof were checked at their audited revisions:

The revision after the cold audit changes only the status line to link this
audit.  A mechanical diff check found no mathematical change.

- the six-coordinate induced-forest reduction at
  `cc2b56362d52a3ef23559a4a0e5cbf5eded5abbe7d54b57e73f66f74f1dd3405`;
- the complementary-cube lift at
  `007ee9ce7aaced1564fae9ada9b0e33dd65ef29cf12f0adc396d278653189f74`;
- split-boundary synchronisation at
  `3e3030d6e206fd81b3a79256be2d94cb4a4aac5ad5985fb95008488d9412edf8`;
  and
- the large-boundary singleton-response theorem at
  `bce97974e2d3d543aaf9ae2f07ff13b61684ddc9cb6bdf08bacdb750c2be2c97`.

## 1. Coordinate localisation and gluing

For a component `K_W` of an open shore, every neighbour outside it lies
in `T`: there are no edges to the opposite shore and no edges to another
component of the same induced shore.  Its neighbourhood `Q_W` is therefore
a separator contained in `T`.  The opposite shore is nonempty, so
seven-connectivity gives `7<=|Q_W|<=|T|`.

The singleton-signature colouring on `X=G-F` has exactly one defect after
the forest is restored, namely `e_W=u_Wv_W`.  Since `u_W` belongs to
`K_W`, deleting `K_W` removes that defect and gives a proper colouring of
`G-K_W`.  If its equality partition on `Q_W` extended through the intact
closed component side, a permutation of the six colour names would align
the two colourings on `Q_W`; their union would colour `G`.  Thus the
partition is genuinely rejected.  This verifies all assertions before the
full-component alternative without assuming labelled colour agreement.

When both selected components are full to `T`, they are connected and
anticomplete.  A `K_5` model in `G[T]`, together with these two components,
would give seven branch sets with only their mutual adjacency possibly
missing.  Hence target exclusion makes `G[T]` `K_5`-minor-free, and the
established case `HC_5` makes it four-colourable.

For every nonempty independent set `I` of `G[T]`, the set `K_B union I`
is connected because `K_B` is full to `T`.  Contracting it is a proper
minor operation.  Its image is adjacent to every vertex of `T-I`, so after
expansion and restriction to the opposite closed shore, its colour occurs
on `T` exactly on `I`.  The symmetric contraction supplies the same
exact-block witness for the other shore.  A common boundary partition
would glue; the two languages are therefore disjoint.  The audited
split-boundary theorem applies with `r=6` and `chi(G[T])<=4`, and correctly
forces `G[T]` to be nonsplit.

## 2. Lifted cuts and the large-boundary exit

In every matching lift, a coordinate from each nonempty crossing part has
one end in the corresponding open shore and the other in the lifted
boundary.  In the induced-path lift, a crossing matching coordinate enters
`C'`, while either path edge has its leaf in `D'` and its common end in the
boundary.  These are exactly the two orientations required by Theorem 1.1;
no extra fullness assumption is used.

In the full-component outcome, the large-boundary theorem applies to the
same decomposition: the open shores are nonempty and anticomplete,
`G[T]` is `K_5`-minor-free, and the critical host is seven-connected,
seven-chromatic and `K_7`-minor-free.  Its vertex has degree between seven
and `|T|-1`, and every incident edge deletion supplies the stated fresh
rejected response.  The remaining arithmetic is exact: `|T|=6+q` leaves
only `q=3` below ten in the matching range, while `|T|=7+k` leaves only
`k=1,2` in the path range.

## 3. Full-component count

In Lemma 4.1, `r>=k+1` permits the `k` boundary blocks to be assigned to
distinct components other than the component being coloured.  Each block
together with its assigned full component is connected; the `k` sets are
disjoint and pairwise adjacent.  Contracting them forces distinct colours
on distinct blocks and one colour throughout each block.  Repeating this
construction for every component gives the same prescribed equality
partition on `T`; colour-name permutations then make the closed-component
colourings agree, and the anticomplete components glue.  The proof does not
silently contract intersecting sets or identify two prescribed blocks.

For four full components, if three boundary vertices span at least two
edges, three further boundary vertices can be absorbed into three distinct
components.  Along with the fourth component and the original three
singleton boundary vertices, these are seven connected branch sets with
at most one missing adjacency.  If no such triple exists, every boundary
vertex has degree at most one, so the boundary is bipartite and Lemma 4.1
applies.  Five or more components are eliminated by an optimal boundary
partition with at most four blocks.  Hence exactly two or three components
remain, and three components force boundary chromatic number three or four.

Corollary 4.3 then follows component by component.  Any non-full component
has a proper neighbourhood contained strictly in `T`, of order at least
seven by connectivity; a colouring of `G-K` supplies a rejected partition
there.  If every component is full, Theorem 4.2 applies, and excluding the
fresh response from the large-boundary theorem restricts `|T|` to eight or
nine.

## 4. Trust boundary

This proof gives an actual smaller response-bearing separator, but it does
not preserve a previously selected minimum side, a model-bag labelling, or
the original forest-coordinate label when the fresh singleton response is
used.  In the surviving order-eight or order-nine case it leaves two or
three full components.  The theorem neither synchronises the two extension
languages nor closes the three-component case.  Its uses of `HC_5`, the
strict Mader--Jorgensen consequence inside the large-boundary theorem, and
the two audited six-coordinate inputs remain within those cited results'
stated hypotheses.
