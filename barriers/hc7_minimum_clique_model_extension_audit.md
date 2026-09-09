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
