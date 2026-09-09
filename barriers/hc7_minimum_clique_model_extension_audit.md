# Audit of the minimum-clique-model extension barrier

**Verdict: GREEN — separate internal audit of the complete source.**
No unresolved mathematical gap was found in the stated construction or
its two minimum-model exclusions. This is internal review, not external
peer review.

## Exact source and scope

Reviewed [source](hc7_minimum_clique_model_extension.md), SHA-256
`b6e60ee98160a719b83df968f1705d571f18f27f470577c24beb19bcfad43739`.
The claim concerns **every K6 model minimising its used vertex set's
cardinality**: neither splitting one of its bags nor adjoining an exterior
component meeting five bags is guaranteed. Arbitrary enlargement or
replacement of the model is not excluded. The explicit K7 certificate
prevents interpreting this as a counterexample to the unrooted augmentation
candidate, C19 or HC7.

## Strongest checks

- **Torus boundary.** After rotating the clear row and column to coordinate
  zero, a component outside their backbone also avoids coordinates
  `±1` in either direction. Its lift and all lattice neighbours therefore
  lie in a rectangle whose coordinates have distinct images in the torus.
  The two upper, two lower and two horizontal extreme neighbours are six
  distinct actual vertices. They would all have to belong to the deleted
  set. This establishes six-connectivity without a boundary-identification
  exception.
- **Local planarity and spacing.** Each fundamental cycle of a connected
  subgraph on at most 21 vertices has length at most 21. Its coordinate
  increments cannot be nonzero multiples of 22 or 1320, so the spanning-tree
  lift is consistent and injective. The sixty attachment vertices have
  mutual distance at least 22; such a component contains at most one of
  them and has at most one attachment edge to S.
- **Connectivity of F.** Six private neighbours keep every surviving
  S vertex attached to each relevant torus after five deletions. If the
  four original U vertices are deleted, at least five of the six internal
  subdivision vertices survive. Any one of these joins `R_U` to a torus
  containing its endpoint labels and a surviving original vertex. This
  covers four original-root deletions plus an attachment deletion, and
  five original-root deletions. The order `15·1320·22+21=435621` is correct.
- **All minimum models.** A planar component attached through one edge
  cannot contain K6 or contribute essential bags on both sides of that
  separation. Trimming every such component leaves a K6 model in S.
  Each of its six bags must contain an original vertex, since a singleton
  subdivision-vertex bag has at most two contacts. Connectivity then makes
  each bag a star, and every `z_ij` is necessary for its two endpoint bags
  to be adjacent. Thus any model using at most 21 vertices uses exactly S;
  this proves the universal minimum-model quantifier, not merely existence
  of one inconvenient model.
- **Both exclusions and the positive certificate.** Splitting a star
  leaves a singleton subdivision vertex with at most one foreign old-bag
  contact. Each exterior component `R_U` meets exactly its four original
  root labels, whatever the subdivision ownership. The six cyclic `U_i`
  are distinct, and T is different from all of them, so the seven displayed
  bags are disjoint and connected. The cyclic incidence rule supplies all
  `B_i–B_j` contacts; `|U_i∩T|≥2` supplies each `D–B_i` contact.

## Inputs and provenance

The proof uses only elementary graph connectivity, spanning-tree lifts,
minor models and minor-closed planarity. No computation, high-girth
existence theorem or finite census is a dependency. The reviewer did not
author the source; a prior independent check of the communicated
construction was followed by this complete rereading of the frozen bytes.
No source changes were requested or made.

## Appended spanning-model example

**Scoped verdict: GREEN**, 9 September 2026. The current complete source
has SHA-256
`67c42df2943647e8d19e01e3ee6a944175ca7e094f6b9ea320d44b93ac0456ec`.
Removing only its final section, including the leading blank line,
byte-recovers the original source at `b6e60ee98160a719b83df968f1705d571f18f27f470577c24beb19bcfad43739`.
That comparison was performed against Git `c74784a`; the preceding audit
remains unchanged. Bacon found the construction and wrote the appendix;
route-assessment independently checked both the initial
claim and the complete frozen section. This addendum reviews the new
section rather than claiming independent discovery or a fresh review of
the unchanged torus proof.

The six-centre clique, twelve private spokes and leaf biclique give
exactly 63 edges. After five deletions both leaf shores survive, and
disconnecting all surviving centres from them exceeds the deletion
budget. Equal bag sizes attain the absolute squared-size minimum 54;
connectivity requires at least twelve internal edges in any spanning
six-bag partition, giving the attained interbag-edge maximum 51.
These are host-edge counts, not counts of adjacent bag pairs.

Every split of an original star isolates a leaf with precisely three
foreign-bag contacts and its own-centre contact, below Q's minimum degree
five. The leaf swap keeps both changed bags connected paths, all six
centres separate, and both numerical optima unchanged. In the final split,
the mixed leaf pair sees bags 1,2 through t_3, bags 4,5 through s_0,
and bag 3 through its centre or leaves; it also sees the singleton c_0
through s_0. The centre clique supplies every remaining contact. Thus
the displayed seven bags are a disjoint connected K7 model.

The quantifier is exactly one unsplittable spanning optimiser, with a
splittable optimiser also present. This does not extend the earlier
every-minimum-used-model statement to all spanning optimisers, and does
not exclude further tie-breakers, exchanges or the unrooted conjecture.
No computation is a premise, and no source correction was needed.
