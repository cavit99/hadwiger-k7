# Cold independent audit: dominated-component response inertness

**Verdict:** GREEN for Theorems 1.1 and 2.1, under their stated
hypotheses, and GREEN for the stated route nonclosure.  The proof correctly
shows that only the fresh-edge response is a proper exterior shore
colouring at the dominated component, and that any first Kempe transition
between the two exclusive response families has the asserted separation or
dominating-complement outcome.  No portal co-location or branch closure is
proved.

**Audited source:**
[`hc7_k7minus_dominated_portal_response_inertness.md`](hc7_k7minus_dominated_portal_response_inertness.md)

**SHA-256:**

```text
cf1a4c0ab795c89646caf61ba49d8134208a1569f1dadb8be9909fa79e11a732
```

This is a cold, separate internal mathematical audit, not external peer
review.  It was performed independently of the adjacent first audit.  No
finite computation is involved.

## 1. Setup and literal boundary placement

Because `Q` is a subgraph of `G[N_G(u)-{v}]`, every vertex of the nonempty
set `A` is adjacent to `u`, and neither `u` nor `v` belongs to `A`.  The
domination hypothesis makes every vertex of `A` adjacent to `v` as well.
Consequently

\[
                    u,v\in T=N_G(A),
\]

the edge `uv` lies wholly in `G[T]`, and `ux` crosses from `T` to `A`
because `x in A`.  This establishes all placement claims in Theorem 1.1(1)
without using any minor model.

## 2. Properness on the two shores

The common deletion graph `H=G-{uv,ux}` is properly coloured by both
displayed colourings.  Thus, after the two edges are restored, the only
possible monochromatic edges are the selected edges themselves.

- Under `c_f`, the edge `ux` is monochromatic and `uv` is proper.  Removing
  `A` removes `x`, so `c_f|G-A` is proper.  The intact closed side
  `G[A union T]` contains both ends of `ux`, so the restriction of `c_f`
  itself is improper there.
- Under `c_e`, the edge `uv` is monochromatic.  Since `u,v in T`, that
  edge and both its ends occur in both `G-A` and `G[A union T]`.  Hence
  neither restriction is proper.

The proper exterior restriction of `c_f` defines a partition of `T` into
colour classes.  If a proper colouring of the intact closed side induced
the same partition, the bijection between the colours used on `T` would
extend to a permutation of the six colour names.  After that permutation,
the two colourings would agree on `T`; gluing them is proper because
`T=N_G(A)` contains every edge from `A` to its complement.  This would
six-colour `G`, a contradiction.  The exterior partition is therefore
rejected.  An improper restriction, such as either restriction of `c_e`,
is not a shore colouring and supplies no admissible boundary partition.
This verifies Theorem 1.1(2)--(3).

## 3. Critical-triangle theorem hypotheses

Minor-minimality subject to non-six-colourability gives a six-colouring of
every proper minor.  Moreover, deleting any vertex and then assigning that
vertex one new colour shows `chi(G)<=7`; hence `chi(G)=7`.  The hypotheses
of the cited critical-triangle theorem therefore hold with `q=6`, centre
`u`, and outer ends `v,x`.

The edge `vx` remains in `H`.  No six-colouring of `H` can have the
all-proper signature, because restoring both deleted edges would colour
`G`; it cannot have equality on both edges, because that would give the
same colour to adjacent `v,x`.  Colourings of `G/uv` and `G/ux` supply the
two exclusive signatures.  Thus the two displayed response families are
nonempty and exhaust `Col_6(H)`.

If a Kempe-reconfiguration component meets both families, a shortest path
between them contains consecutive colourings of opposite signature.  The
critical-triangle theorem applies to this one interchange and gives exactly

```text
u in D and v,x outside D; or v,x in D and u outside D.
```

There is no unverified inference from arbitrary reconfiguration
connectivity here: disconnection of the two response families is retained
as outcome 1.

## 4. Exterior colourings and their common boundary

In the first placement `D` contains the common endpoint `u`; in the second
it contains both outer endpoints `v,x`.  Therefore `D` meets each of the
two selected edges in either placement.  For either response colouring,
deleting `D` removes an endpoint of its sole monochromatic restored edge,
so both restrictions to `G-D` are proper.

The adjacent response colourings differ only on `D`.  Hence they agree
pointwise, not merely up to a permutation, on `N_G(D)` and induce the same
boundary partition there.  A proper colouring of the intact closed
`D`-side with this partition could be permuted to agree with either proper
exterior restriction and glued to it, producing a six-colouring of `G`.
The common exterior partition is therefore rejected.

If `D` is not dominating, a vertex outside `N_G[D]` makes `N_G(D)` an
actual separator: after its deletion, `D` and that far side are nonempty
and anticomplete.  Seven-connectivity yields boundary order at least seven.
This verifies outcome 2.  The phrase “partition on `D`” in the outcome is
read in the proof's precise sense of the exterior partition on
`N_G(D)`; it is a harmless locution rather than an additional claim.

## 5. The dominating outcome

Neither deleted edge has both ends in `D` in either permitted placement.
Consequently `G[D]=H[D]`.  Since `D` is a connected component of a
bichromatic subgraph of the properly coloured graph `H`, it is connected
and bipartite in `G`.

If `G-D` were four-colourable, a two-colouring of `D` on two disjoint
colours and a four-colouring of `G-D` on four further colours would
six-colour `G`.  Thus `chi(G-D)>=5`.

If `G-D` contained a `K_6` minor, the connected dominating set `D` would
serve as a seventh branch set adjacent to all six model bags, giving a
`K_7` minor in `G`.  Such a minor contains a `K_7^-` minor, contrary to
the target-exclusion hypothesis.  Therefore `G-D` is `K_6`-minor-free,
and the established `HC_6` theorem gives `chi(G-D)<=5`.  Equality follows.

Finally, a `K_6^-` model in `G-D`, together with the connected dominating
branch set `D`, gives exactly a `K_7^-` model in `G`.  Hence

\[
                   \chi(G-D)=5,
       \qquad K_6^-\npreccurlyeq G-D
\]

is valid.  This verifies outcome 3 and the requested sharpening beyond the
`K_6`-minor exclusion used to invoke `HC_6`.

## 6. Scope and nonclosure

The fixed spanning exact model is unchanged as a collection of branch
sets when the graph is recoloured, but no proof step identifies palette
colours with branch-set labels.  The old-coordinate response is improper
on both original shores, and the transition component may cross several
bags or miss a whole named portal set.  If the two response families are
Kempe-disconnected, no transition component exists at all.

Accordingly, the source correctly records the portal implication as
unsupported rather than false.  It proves neither portal co-location nor
its negation, does not upper-bound the transition separator, does not
eliminate the dominating five-chromatic complement, and does not prove the
eight-coordinate branch closure, Conjecture 21, or `HC_7`.
