# Internal audit: exclusion of the two nonroot ports

**Verdict: GREEN.**

**Audited source:** [the nonroot-port closure](hc7_two_triangle_nonroot_port_closure.md).

**Whole-source SHA-256:**
`2b3d6945c1dbf85ac6c17444a95baaf400a115d6b5c48359668f302811f75140`.

This records separate internal mathematical reviews, not external peer
review. The first reviewer co-developed related reserved-core results,
audited the new boundary repair and checked this proposed construction
before independently reading the complete source written by another agent.
A second reviewer independently read the same complete draft, reporting
GREEN; that reviewer contributed earlier packet and omission lemmas and
had conceptually checked the boundary repair. These prior contributions
are not presented as independence from all proof development. The parent
also reported a complete read; the two reviews detailed here are the
first and second reviewers' exact-source checks.

## Exact revisions and dependencies

Both reviewers read the complete draft at SHA-256
`6c1cfcdfd2e2031d1117bd3ab0e0548ac8505cf7ccb87f0f4b4f59c4682db2dc`.
Two wording changes explicitly made both maxima cardinality maxima,
giving `553408e1b12fd63ea37d5c248ba1679f5279bb197a400069016e24b1223cdcd6`.
Promotion changed only the status and eight relative links. Reversing
those changes recovers the latter hash; reversing the two cardinality
clarifications then recovers the jointly reviewed draft. Both exact
reconstructions were checked, and the final source was inspected.

All eight direct source/audit pins match disk. Their invoked statements
were checked at the recorded revisions:

- Contraction closure: `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`;
  audit `26b2f5ad7226c7bb3f194cac8523f043d7ae6ca955036249f04ddc9fb6d94394`.
- Whole-class reservation: `6c40aab52c5e5c8dc822640ce3c801f6cc46e04b161fd49f108dfd6835116eb3`;
  audit `10d4ab2970bb45f41ffc228a5748cd4ee963016d4d89fe0db7ff11124abab636`.
- Connected residual component: `b02d2c88ebf4879b45e36031d9bf9b7ac0722d8c7302a26d7637d8ba3fcf0e3c`;
  audit `7851c856c4a37b92fc1dcea6c823d25c55718eaf575e723c118eaa65d48bf923`.
- Contraction-boundary repair: `da0e3fd73fb52815d01bdfd7d9e56a0fd9d1bca4c93bb2d332fc0f4fe67de571`;
  audit `d2348e8500d49aeda6a9d8d220ce3b3fe41c0e5edf2e680749aa76e9a2683dc5`.

No new external theorem or finite computation is a premise of this audit.

## The maximum and the quotient

The small contractions leave the specified four-cliques untouched and
prove both the single A--B edge bound and the single triangle vertex
contacted by x,y. They give an a missing B,x,y and at least two eligible
B roots. The reservation applies separately for every eligible b.
The finite maximum over all these omissions is also a maximum for its
selected b, so the fixed-reservation normalisation and connectedness
theorem apply without a quantifier exchange.

The unique residual C contacts b. Any other B root missing C would also
miss M and a, leaving at most seven possible neighbours. Thus C is full
to B, and the boundary-repair corollary applies with all its actual-host
hypotheses. The choice of eligible B1 distinct from b is justified.

At most one C vertex meets all of a,x,y, by the stated va contraction.
A common neighbour of b,B1 cannot meet any of a,x,y: its two labels in
the v+B clique exclude an outside neighbour carrying the v label.
Such a vertex retains degree at least seven after the merge. Every
other C vertex loses only its a,x,y neighbours, giving degree at least
six apart from the one possible degree-five vertex. Together with the
repaired four-neighbour condition, these are exactly Lemma 3's hypotheses.
No general preservation of degree or connectivity under contraction is
assumed.

## Normalisation and the actual-root lifts

The literal q--B2 edge retains the mutual contact of the two non-helper
bags. In a tree spanning the minimal q bag, an irrelevant nonroot leaf
can be removed. A leaf with a helper contact can be donated to that
helper whenever another vertex retains contact to the other helper;
its old tree edge restores the donated helper's contact to the remaining
q bag. Thus every nonroot leaf is the sole contact to both helpers.
There is at most one, making the tree a q-rooted path or a singleton.
No spanning assertion about the union of all model bags is needed.

For a positive-length path, its first edge has an actual b or B1
endpoint. Retaining that endpoint and the path, and discarding the other
merged endpoint, preserves connectivity and both helper contacts. The
literal edge to B2 supplies the third contact. All other bags avoid
both merged vertices, so lifting introduces no root collision. Appending
the two helper bags to the old A bags adds both ports and yields a model
with an eligible omitted root in the original comparison class.

For a singleton q, B1 either contacts both helpers or b contacts at
least one. In the latter case, assign a b-contacted helper to the old
A bag not chosen for its existing b contact. Assign the other helper
to the old b-contacting A bag. Both assignments are connected because
each actual port contacts both old A bags. Retain b singleton and the
B2 bag, omit eligible B1, and use the old A--A edge and literal bB2
edge. All six required contacts are actual; all four prescribed roots
remain in separate bags. The new A union contains M and both old ports,
contradicting the same cardinal maximum.

## Scope

The cases exhaust the normalised q bag and close the two-nonroot-port
branch for the stated global maximum. Old B-root paths are discarded;
an edge inherited from b is never silently attributed to B1. The proof
does not exclude two root ports or complete the two-triangle case,
Conjecture 19 or HC7. No mathematical gap was found in the stated result.
