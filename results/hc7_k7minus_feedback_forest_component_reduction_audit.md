# Internal audit: forest-component reduction in the bounded-feedback branch

**Verdict:** GREEN.  The trichotomy, all seven-connectivity counts, the
order-seven separator conclusions, the cycle statements and the common
model split certificate are correct at the stated quantifiers.  This is a
separate internal mathematical audit, not external peer review.

## 1. Exact revision

The audited source is
[`hc7_k7minus_feedback_forest_component_reduction.md`](hc7_k7minus_feedback_forest_component_reduction.md),
with SHA-256

```text
71350698ced99eb0976c0f4d0bc64345d8cc243fad41fd9971f5f6ae50f58ff3
```

The principal cited input is the separately audited
[`six-centre feedback theorem`](../results/hc7_k7minus_feedback_six_centre_common_matching.md),
revision
`400a3ecedfbff8dbed58fe1ccdb380a443452828753195ca1b08eaf09fd9cc06`.
Its boundary-crossing matching, punctured signature cube, saturation
statement and co-bagged spanning `K_6` model are used at exactly their
proved quantifiers.

The promoted revision differs from the cold-audited active revision only
in its status line, relative links, and the later scope paragraph recording
the dominating-`K_5` theorem of Girão et al.; the final revision also
corrects two malformed Markdown delimiters in that paragraph.  A mechanical diff check
found no change to any theorem or proof.  The cited dominating-model
theorem supplies the stated model but is explicitly not used to infer a
contact allocation.

## 2. The middle-piece far side

Lemma 2.1 applies to a connected set `Y` only when

```text
V(G) - (Y union N_G(Y)) is nonempty.
```

In both constructions in Theorem 3.1 this is automatic for the two end
pieces `A,C`, because the opposite end piece survives outside the closed
neighbourhood.  It is not automatic for the middle piece `B`: both end
pieces can consist entirely of the two vertices in `N_R(B)`, and every
vertex of `T` can be adjacent to `B`.

The audited revision treats the two spanning cases directly, rather than
invoking Lemma 2.1 outside its hypotheses.

1. If a selected centre `z` has forest degree at least two and
   `B union N_G(B)=V(G)`, then `T=N_G(B) cap T`.  Since
   `chi(G[T])>=5` and `G` has no literal `K_5`, one has `|T|>=6`.
   Hence `|N_G(B) cap T|>=6`, which is the required middle-piece bound.
2. If `A={z_i}` and `C={z_j}` are two selected leaves and
   `B union N_G(B)=V(G)`, the four other selected centres lie in `B`:
   they lie outside `T`, and the only vertices of `R-B` are `z_i,z_j`.
   Each has forest degree at most one and total degree eight, so `B` has
   at least seven neighbours in `T`.  Again the required middle-piece
   bound follows directly.

If the corresponding closed neighbourhood is not spanning, Lemma 2.1
applies exactly as written.  The two repairs are exhaustive, so no fourth
spanning-tree residue is missing.

## 3. Remaining checks

The following parts of the audited revision were checked adversarially and
are correct.

- For a connected forest piece with a nonempty far side,
  seven-connectivity gives boundary order at least seven.  At equality,
  every component on either side is full to the separator; otherwise its
  open neighbourhood would have order at most six.
- A `K_5` minor in an equality boundary, together with two full components,
  gives seven branch sets with only the two component bags nonadjacent.
  Hence the boundary is `K_5`-minor-free in the target-free host.
- A common boundary partition from the two proper-minor shore colourings
  can be aligned by a permutation of six colours and glued.  Therefore the
  two partition languages are disjoint.
- In the first forest construction, `A,B,C` are connected, cover one tree
  component, and have forest-boundary orders `1,2,1`.  In the second,
  independent selected centres in one tree are nonadjacent leaves; deleting
  them leaves a nonempty connected middle piece with forest-boundary order
  two.  The asserted selected-centre placement is exact.
- If all selected centres occupy distinct forest components, another
  selected component supplies the far side for each application of
  Lemma 2.1.  Equality returns the full order-seven separation; otherwise
  the six component boundaries have order at least eight in `T`.
- The Haggkvist--Thomassen theorem applies to the six independent
  boundary-crossing edges in the seven-connected graph.  A seven-fan from
  a prescribed vertex to that cycle leaves one of seven cyclic intervals
  free of the six selected edges, so the usual interval replacement keeps
  all six edges and inserts the prescribed vertex.
- The six selected matching edges assigned inside the branch bags of the
  common spanning `K_6` model extend simultaneously to bag-spanning trees.
  If four foreign bags met both components of one selected-edge tree cut,
  splitting that bag would give a seven-bag model missing at most one
  adjacency.  The bound of at most three such foreign bags is therefore
  valid.

No forest component is silently replaced by an arbitrary connected
subgraph, and the source does not combine the independent-triple
representatives with the separately chosen boundary-crossing
representatives.

## 4. Trust boundary

The theorem is a conditional reduction inside the bounded-feedback branch.
It does not prove that any of its three outcomes is terminal.  In
particular, it does not infer a rooted model from boundary sizes alone, does
not align the boundary partitions of an order-seven separation, and does
not claim that the common cycle and common spanning model can be chosen
compatibly.  These are the explicit remaining composition tasks in the
source.  No unresolved assumption or proof gap remains in the theorem as
stated.
