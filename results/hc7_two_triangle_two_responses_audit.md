# Audit of the unique triangle-root boundary theorem

**Verdict: GREEN.** Separate internal audit of the complete written proof;
this is not external peer review.

## Exact source and scope

Audited [source](hc7_two_triangle_two_responses.md), SHA-256:

`f190c8e63df3d12b301440280babeee611db897a5542216f2d074314fb5a6b18`.

Under the source's seven-connectivity, minimum-degree-eight, Q-exclusion
and degree-eight neighbourhood hypotheses, at most one A root occurs
on any tight four-vertex H-boundary of a nonempty exterior set. The
quantifier covers all such sets, not merely failed rooted-clique responses.
The corollary gives at least two deletions preserving every exterior-set
boundary at four or more, and a separate rooted four-clique for each.

The entire stronger draft was cold-read at SHA-256
`9033233163b5406ca3aec9af1cc4cdea6c2d100a097b768e345518916053474b`.
Reversing only the final status wording and four sibling-link changes
in the promoted source reconstructs that exact hash. No mathematics
changed on promotion. The earlier response-only draft was also reviewed;
the stronger quantifier received a fresh complete-source check.

## Strongest checks

- The boundary lemma treats all possible additional neighbourhood roots.
  Seven-connectivity gives the actual seven-vertex side boundary. Deleting
  two boundary roots preserves the degree-six and boundary-five packet
  hypotheses. Its two admissible triangle centres suffice to avoid a
  possible outside component's missing B contact. The two-component
  endpoint case uses disjoint side models and explicit connected bags.
- A component of an arbitrary witnessing exterior set retains the same
  four-boundary by four-connectivity. Thus inclusion-minimal connected
  regions exist with boundary exactly their A root and three W ports.
  Their order is at least three by the minimum-degree-six bound in H.
- Overlap forces both union and intersection boundaries to be four by
  submodularity. The union still sees both distinct A roots and violates
  the proved boundary lemma. For disjoint regions with a cross-edge,
  the exact port count leaves only `(a,b)=(1,2),(2,1),(1,1)`.
  The first two cases expose a nonempty component with boundary at most
  three. In the last, deleting the unique cross-port exposes a proper
  smaller region whose four-boundary still contains the same A root.
  This contradicts the stated minimality and proves anticompleteness.
- In the two-connected graph obtained by deleting the two A roots,
  each component outside the second region containing a nonport vertex
  uses at least two of its three ports. Hence the remaining A root and
  the first region lie in the same component. The path stopped at its
  first port of the first region avoids both regions and all other packet roots.
- Extending only that port bag along the path preserves disjointness.
  The second region plus its A root meets B through the region and the
  other two core bags through the literal triangle edges. The singleton
  v meets all five core bags and this additional bag. The seven actual
  bags form a `K_7^-` model, and therefore contain Q.
- For each A root outside the exceptional set, deleting it cannot lower
  a W-set boundary below four. Its W neighbours had degree at least seven
  in H; all other W vertices lose nothing. The four-root packet therefore
  applies with exactly the asserted roots and nonroot set W.

## Inputs and limitations

Both input source hashes and both adjacent audit hashes listed in the
source were independently checked against the files on disk. The packaged
rooted-four and degree-six statements were checked against their precise
hypotheses. No fresh primary-source inspection or finite computation is
claimed by this audit.

No unresolved mathematical gap was found. The proof uses no colouring
assumption, no quotient-criticality assumption and no virtual-edge lift.
It does not give one model serving both successful deletions, exclude the
remaining two-triangle configuration, or prove Conjecture 19 or HC7.
