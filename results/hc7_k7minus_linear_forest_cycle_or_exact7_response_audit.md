# Internal audit: linear-forest cycle or labelled minimum separation

**Verdict:** GREEN.  This is a separate internal mathematical audit, not
external peer review.

## 1. Exact revision and scope

The audited source is
[`hc7_k7minus_linear_forest_cycle_or_exact7_response.md`](hc7_k7minus_linear_forest_cycle_or_exact7_response.md),
with SHA-256

```text
a8f06843ac08fcfa2c8cda40e05a54f69209029c502c058f115b509a18db209d
```

The audit covers Theorem 1.1, Theorem 2.1 and Corollary 3.1.  It checks the
general threshold statement, the complete seven-coordinate signature
localisation and the fixed-model portal specialization.  The result does
not prove the `K_7^-` six-colour conjecture or `HC_7`.

## 2. General threshold theorem

The hypothesis `q\ge2` is necessary: without it `K_2`, with its sole edge
as `L`, would be an exception.  With the displayed hypothesis, both order
cases are correct.

- If `\kappa(G)\ge q+1`, the path components of `L` are pairwise disjoint
  and have total length `q`.  The independent-path form of
  Haggkvist--Thomassen applies with `k=q+1` and puts all components on one
  cycle.
- If `\kappa(G)=q` and `|V(G)|=q+1`, connectivity forces
  `G=K_{q+1}`.  The vertex count `|V(L)|=q+t\le q+1` forces `t=1`, so `L`
  is a spanning path.  Since `q\ge2`, its ends are distinct and their edge
  in the complete graph closes the required cycle.
- If `|V(G)|\ge q+2`, a proper `q`-cut exists.  Because
  `|V(L)|>q`, some forest vertex lies outside the cut.  An incident forest
  edge has its other end in the same component or on the cut, since no edge
  joins distinct components after the cut is removed.

In a proper colouring of `G-g`, the two ends of `g` must be equal-coloured.
Deleting the selected component removes the only possible defect.
Equality of the two literal boundary partitions is sufficient for
colour-name alignment: the injective map on used boundary colours extends
to a permutation of all `r` colours.  The resulting gluing contradiction is
valid.  Thus the returned separation is both proper and labelled by the
actual deleted edge.

## 3. Seven-coordinate localisation

For every nonempty `J\subseteq L`, contracting `J` and expanding a
six-colouring gives signature exactly `J`.  Forestness prevents an edge of
`L-J` from collapsing; componentwise inducedness prevents an edge of
`G-L` from collapsing.  An empty signature would colour `G`.  Hence the
punctured cube (2.3) is exact.

When the cycle outcome fails, `\kappa(G)=7`.  Corollary 2 of the separately
audited
[`hc7_k7minus_three_component_seven_cut_exclusion.md`](hc7_k7minus_three_component_seven_cut_exclusion.md)
correctly supplies exactly two full components after every seven-cut.  The
partition `L=L_A\dot\cup L_S\dot\cup L_B` is exhaustive because no edge
joins the two components.

For nonempty `J\subseteq L_A`, deleting `A` removes an end of every
monochromatic restored edge; the restriction to the opposite closed shore
is proper and its partition is rejected by gluing.  The symmetric statement
holds for `L_B`.  If a partition occurred in both oriented families, those
two proper closed-shore colourings would themselves glue, so the languages
are disjoint.

The numerical bounds are exact:

- a seven-set contains at most three edges of `7K_2`;
- it contains at most four edges of `5K_2\dot\cup P_3`;
- among at least three outside edges in the second case there are two
  disjoint ones, even when two of the three are the adjacent path edges.

The resulting same-shore two-coordinate subcube and the globally disjoint
outside pair are therefore both justified.

## 4. Portal specialization

The portal corollary explicitly assumes the redundant model adjacency used
by the construction: the exceptional bag has two distinct neighbours in
one universal bag and `e` is one corresponding cross-bag edge.  Deleting
`e` disconnects no bag and leaves the other cross-bag edge as the required
adjacency witness.  The original exact spanning `K_7^\vee` model therefore
survives in `H=X-e`.

Cleanliness makes `e` a new single-edge forest component, so the full
seven-coordinate theorem applies and gives all `127` signatures.  Restoring
all but two selected outside edges gives the three nonempty signatures on
one common two-edge-deletion host.  Adding restored edges cannot damage the
fixed model; target exclusion prevents either nominally missing pair from
becoming adjacent in `G`.  The same-side and opposite-side boundary claims
are exactly the restrictions already audited in Section 3.

## 5. Trust boundary

The theorem legitimately supersedes the earlier two-cycle composition
target: it returns either the desired one cycle or an operation-labelled
minimum separation.  It does not prove the parameter-seven
Lovasz--Woodall assertion, merge two cycles inside a merely
seven-connected graph, provide a shared Kempe pivot, or align a colour
component with a prescribed branch bag.  The scope paragraph records these
limitations accurately.
