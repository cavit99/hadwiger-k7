# Internal audit: rooted diamond or strict order-seven shore

**Audited source:** `hc7_k7minus_both_full_diamond_or_exact7.md`

**SHA-256:**
`72364039544922eea08997d1057a56d6d6a408609fa6893333165f4cedd1edb3`

**Verdict:** **GREEN.**  The proof is computation-free and uses Jorgensen's
rooted-`K_4^-` theorem, in the form stated as Lemma 10 by Norin and
Totschnig.
This is a separate internal mathematical audit, not external peer review.

## Dependency and trust boundary

The application to the current fan families cites the audited minimal
root-star response theorem at SHA-256
`8378f08308ce6fd7b4b701f76a925c61c0d3f15e09965ac185ce60e39b06a580`.
The rooted-diamond implication itself is an external literature input; no
finite enumeration is used in this source.

## Mathematical check

If `G[F union Q]` is not internally four-connected relative to the four
roots, a separator of order at most three combines with the four omitted
vertices of the order-eight boundary.  Seven-connectivity forces equality
throughout, so the full neighbourhood of a component on the root-free side
is an actual order-seven cut.  Fullness shows that this component is a
proper subset of `F`.  Otherwise Jorgensen supplies the rooted diamond.

For two adjacent connected supports, the defect inequalities leave four
common boundary roots and permit two further distinct boundary vertices,
one assigned to each support.  The four rooted-diamond bags, the two enlarged
supports, and `{u}` are disjoint and connected; all contacts are literal,
with at most the diamond's one missing adjacency.  This is a valid
`K_7^-` model.

Joining disjoint fan supports by a shortest path preserves their disjointness
and boundary contacts.  In the intersecting case, deleting a connected set
that meets at most two arms leaves the fan centre connected to at least five
boundary ends, giving exactly the defect bounds required above.  A returned
separation lies wholly in the opposite component, so the literal fans and
their first edges remain on the other closed side.

## Exact limitations

The theorem preserves literal fan paths, not an entire proper-minor colouring
response.  It does not eliminate intersections using at least three arms,
synchronize two independently generated rooted diamonds, eliminate the
both-full case, or prove exceptional-centre connectivity.
