# Internal audit: the all-lock branch-set transfer gate

**Verdict:** **GREEN for Lemmas 1.1, 2.1, 3.1 and 4.1, with the route
nonclosure in Section 5 of the source correctly scoped.**

This is a separate internal mathematical audit, not external peer review.
It checks the exact source revision identified below.  The note does not
prove the matching row or the proposed critical forest-split theorem.

## Exact revision

The audited source is
[`hc7_k7minus_all_lock_branch_transfer_gate.md`](hc7_k7minus_all_lock_branch_transfer_gate.md).
Its SHA-256 is recorded here after the source is finalised:

```text
a1e0664404c2dc7c0ce25f93147fdead53a24295dfd0087c419a2aab27940295
```

The direct audited inputs are:

- the [matching common-state theorem](../results/hc7_k7minus_matching_square_common_state.md);
- the [matching-lock boundary reduction](../results/hc7_k7minus_matching_lock_boundary_reduction.md); and
- `HC_4`, used only to observe the existence of an unrooted `K_4` model in
  an exactly four-chromatic complement.

## 1. Four exact four-chromatic complements

For fixed `beta`, an `alpha`- or `beta`-coloured vertex outside the
component `K_beta` cannot have an edge of `H` into that component.  Since
`K_beta` dominates in `G`, it must nevertheless have an edge into the
component.  The edge cannot be `e`, whose ends both belong to `K_beta`, so
it is `f`.  Its mate in `K_beta` also has one of the two colours.  Properness
of `f` in the fixed `EP` colouring therefore makes the fixed unordered
pair of endpoint colours of `f` exactly `{alpha,beta}`.

There is at most one such alternate `beta`.  For every other alternate
colour, no vertex of the two relevant colours lies outside `K_beta`, so
the component is the entire induced two-colour subgraph.  Removing it
leaves only the four other colour classes.  The edge `f` survives but is
proper, while `e` loses both ends.  Hence the complement is at most
four-chromatic; the lower bound four is the audited all-lock theorem.
This verifies Lemma 1.1.

The source does not overinterpret this conclusion.  A `K_4` model in the
complement is not rooted at contacts to the two pieces of a split inside
`K_beta`.  Domination supplies contact to their union only.  Nor is this
four-bag model identified with four foreign bags of the common `K_6`
model.

## 2. Minimum root bag

In Lemma 2.1, if a detachable unprotected piece `W` owns no foreign
root-bag adjacency, it can be omitted.  If it owns exactly one label, it
can be absorbed into that foreign bag.  The cut edge between `W` and the
connected residual root bag restores the root--owner adjacency; every
other root adjacency survives, and enlarging a foreign bag preserves all
foreign--foreign adjacencies.  Thus a minimum protected root bag forces at
least two owner labels.

The source correctly distinguishes owner labels from boundary vertices.
It also correctly observes that minimising the root bag is not monotone
with maximising double contacts: removing `W` may preserve the model but
destroy a double contact whose only endpoint on one split side lay in
`W`.

## 3. Foreign-piece absorption

Lemma 3.1 lists every condition needed for the inward transfer.  The
absorbed piece is connected to the nominated split side; the residual
foreign bag is connected; their cut edge supplies the new root--foreign
adjacency; and every foreign--foreign adjacency involving the residual
bag is explicitly required to survive.  All other adjacencies are
unchanged.  No unlisted colouring or separator conclusion is claimed.

The failure certificate is exact but nonterminal.  A residual component
or a monopolised model adjacency may have arbitrarily many literal
neighbours.  Seven-connectivity supplies no upper bound of eight, and the
model ownership certificate carries no boundary partition.

## 4. Kempe indivisibility

For Lemma 4.1, a proper nonempty subset of a connected bichromatic
component has a crossing bichromatic edge.  Swapping the two colours on
only that subset makes the crossing edge monochromatic.  Hence a lock-path
prefix is not a valid Kempe interchange.  Switching the whole component
is proper, but moves both ends of `e` together and leaves them
equal-coloured.  The missing all-proper signature therefore supplies no
opposite response from this fixed all-lock colouring.

This verifies the source's first unsupported inference: blocked
branch-set absorption cannot presently be converted into an
original-labelled order-seven/eight response or a common shore partition.
The proposed blocked-transfer response theorem would require genuinely new
comparison across the three realised signature colourings; it is not
proved in the source.

## Scope

The result is unbounded and computation-free.  The cited static multi-owner
construction is used only as supporting evidence for the route diagnosis;
it is explicitly not treated as a counterexample to the critical-host
theorem.
