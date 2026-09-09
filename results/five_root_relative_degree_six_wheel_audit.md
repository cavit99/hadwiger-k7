# Audit: a five-root wheel from relative boundary and degree bounds

**Reviewed source:** [the complete proof](five_root_relative_degree_six_wheel.md).

**Exact source SHA-256:**
`46a2211c03938afb9fd5fc3e8e309f31ab7d102c3211a51f7a1c6e1adcb5ed6d`.

The original reviewed draft had SHA-256
`71b5dc798a633750116fe442ad7db3701903a210499b05399d25c3f3b89c9a97`.
Promotion changed only the status, relative links and heading spelling;
the mathematical text is unchanged.

**Verdict:** GREEN — separate internal whole-source audit. No mathematical
gap was found at this revision. This is not external peer review or a
claim that the global research objective has been achieved.

## Scope and provenance

The author, `universal_proof`, developed and wrote the general theorem.
The reviewer, `route_assessment`, developed a narrower actual-host
normalization in parallel and saw the author's outline before reading
this frozen source. This audit independently checked the broader stated
hypotheses and every proof step; it does not import the additional root
degrees, neighbourhood restrictions or pre-existing K4 of that narrower
argument. No finite search is a dependency of this verdict.

The theorem reviewed is exactly: five prescribed roots, at least three
nonroots, every nonempty nonroot set having at least five external
neighbours, and nonroot minimum degree six imply a wheel rooted at all
five roots, with unspecified hub and rim order.

## Strongest inferences checked

- **Two-nonroot endpoint.** Both nonroots are universal. Two incident
  root edges give the displayed rooted wheel. If the root graph is a
  matching, distributing the two nonroots among bags leaves a singleton
  root bag with at most two other bag contacts, including when the
  nonroots share a bag or one is unused. Thus the claimed exceptional
  family is exact, and all its root degrees are at most three.
- **Closed reductions.** A root with one nonroot neighbour can absorb
  that neighbour without changing any surviving nonroot degree or
  boundary cardinality. The same is true when two roots with the same
  two nonroot neighbours absorb those neighbours separately. All five
  root preimages remain distinct. The merged-root degree bounds five
  and four, respectively, exclude the two-nonroot endpoint; one
  remaining nonroot cannot retain degree six. The nonroot count strictly
  decreases, so the minimum-counterexample use is valid.
- **Rooted-four alternatives.** Deleting a root leaves the exact
  internal-four boundary hypothesis. In the NT trisection the two open
  parts must be single roots, its ports must be nonroots, and
  normalization makes the two roots have the same two nonroot
  neighbours. This is precisely the eliminated paired reduction. The
  small rooted separation also violates the boundary hypothesis.
- **Cofacial counts.** The normalized graph after a root deletion is
  two-connected, so the distinguished face has a cycle boundary of
  length `4+h`. The bounds `e(J_u)<=3|D|+5-h` and at least `4-h`
  root-root facial edges imply `e_D+K-k_u<=3|D|+1`, including when
  `4-h` is negative. Combined with `2e_D+K>=6|D|`, this gives
  `2k_u>=K-2`. Two failed deletions would leave the other three
  neighbourhood counts summing to at most two, contrary to their
  normalized lower bound six. Hence a suitable four-root K4 exists.
- **Suppression connectivity.** For every separator of order at most
  two, at least one nonroot survives and only one component can contain
  nonroots. Any other component consists of roots, whose two nonroot
  neighbours force two nonroot separator ports. The paired reduction
  then forces that component to be a single degree-two root. For any
  deletion of at most two vertices of the suppressed graph, its
  components correspond to the original components containing retained
  vertices; suppressed roots with no surviving port are irrelevant.
  Thus the suppressed graph is connected after every such deletion.
- **Hall matching and order.** Distinct two-port pairs give a simple
  graph. With at most five pairs a deficient root set can only consist
  of all five roots on four ports. An additional nonroot contradicts
  the boundary bound; with exactly four nonroots their degree sum is
  at most `12+10=22<24`. An injective matching therefore exists and
  also ensures that the suppressed graph has at least five vertices.
- **Projected ownership and lift.** Every original clique bag survives
  projection: a selected degree-two root cannot by itself have three
  clique contacts. The added port edge restores both internal
  connectivity and any interbag contact previously using that root.
  Ports initially selected in the four bags are distinct. Augmenting
  the matching keeps every occupied port occupied; changing which
  terminal occupies it is permitted because the extension theorem
  needs some four of the five terminals. Matching contractions have
  disjoint two-vertex preimages and realize exactly the suppressed
  graph. The four projected bags still contain four distinct terminal
  images, while the fifth may lie in a bag or outside the model. The
  invoked wheel theorem explicitly permits both situations.

## Dependencies and limitations

The two source hashes and two adjacent audit hashes listed in the draft
were checked against the local files and match exactly. The NT alternative
is used in the form recorded in that pinned source; no fresh literature
inspection is claimed. The wheel-extension input permits a change of the
selected four roots and does not require the fifth to be unused.

The source proves a relative five-root wheel only. It neither prescribes
the hub nor supplies additional exterior contacts or a disjoint helper.
In particular, the weaker single-contact and root-port configurations in
the ongoing C19 application are not made terminal by this theorem. The
full C19, HC7 and NT-comparable completion criteria remain outside its
conclusion.
