# Audit of the K5-scheme separator reduction

**Verdict: GREEN.**

This separate internal audit covers the complete
[source](k5_scheme_separator_reduction.md) at SHA-256
`5d7dc02cc98cd96817f0919e46212a27cc3831c67a7b84cb950aebedcca4cf96`.
The current revision changes only three scope paragraphs to point to the
separate four-connectivity theorem. Comparison with Git `2df86a9`
(source SHA-256 `fc00d9890006e9f786a4b194e38a74b9c44873733d20126b86ce9638e00938d4`)
confirms that every mathematical argument is unchanged. The review below
records that revision and its predecessor.
The source remains conditional on a minimum counterexample existing.
The previous audited revision was
`102bced36c8fd794b7d52870fb4c2041e2955068c54d5130ac23adc24538e616`.
Only its status sentence changed after the original complete proof review;
reversing that sentence exactly recovers the reviewed source at
`ebea05fc794fe48745a1d7d31aba7d075a4905a57f5872302232722c203ca1b7`;
the mathematics of that revision was unchanged.

## Checks

- The degree and path-membership normalization preserves all roots and
  proper colours. The two-boundary-vertices observation excludes the
  stated absent colours and root-free small sides.
- The rooted triangle construction is proved in the source, including
  distinct contact points and reversed contact order. No external
  rooted-clique theorem is silently used.
- The one-root three-cut case forces exactly one port in its root's
  colour and two in another colour. The two contractions are disjoint,
  even when one repeated-colour port is itself an original root.
- In the two-root repeated-colour case, the two prefix/excursion
  alternatives genuinely connect both equal-colour ports. In the last
  alternative, every cross-path remains interior after its first port;
  the simple remaining two-colour path permits only the stated disjoint
  exterior segments. An equal-colour merger consumes no foreign root.
- Every reduction has fixed disjoint connected preimages, preserves all
  five original roots, and strictly decreases host order. Interior
  suffixes avoid the consumed exterior material. Proper quotient paths
  certify arbitrary multiple-path intersections, not merely pairwise
  disjointness of independent demands.
- The exhaustion includes cuts containing original roots and proves
  exactly the stated two-component, three-versus-two-root residue.
  The explicit repeated-port example is a proper scheme; its five
  displayed bags are connected, disjoint and pairwise adjacent.

## Section 7: terminal constructions

In the `2df86a9` revision, removing Section 7 and its separating blank line
byte-recovers the source at Git `24d2631` and SHA-256 `102bced36...` above.
Sections 1–6 have not changed. The new section received a separate
exact-source review after the reviewer checked its application sketch.

The terminal criterion is valid for every returned outer rooted model.
A triangle path leaving `J` has exactly one outside excursion between
its two permitted ports. The six outer prefixes, reserved excursions,
original a–b path and filled root edges form a proper smaller K5-scheme.
The fixed interior bags realise every filled edge and intersect the outer
host only at their respective ports. All five original roots remain in
distinct bags; an arbitrary permutation of the three interior roots is
valid because the target is complete. The order decreases by at least three.

For the prescribed-colour alternative, contraction can create only
endpoint revisits on an inside triangle path. Trimming them preserves a
proper sub-triangle scheme: no such path uses an allocated a/b vertex or
meets the third bag, and new intersections have a common target endpoint.
The elementary rooted model expands the same fixed preimages entirely
inside `J`. The all-outside alternative requires no filled contact and
therefore works with any disjoint three-path root-to-port linkage.

First-hit trimming of a linkage supplied by three-connectivity places it
inside `J`, validating the full-region alternative. The invoked
[two-region source](../results/two_full_regions_paired_triangle.md) matches
its stated hash `7659e347...`; its adjacent GREEN audit was also checked
(SHA-256 `15eb754137fd49895a63210ca658c47ae8057f60a4d9d29a8be388d97d215f06`).
No allocation-existence assertion is added by these sufficient conditions.

## Scope and provenance

The auditor previously checked the rainbow and repeated-colour outlines
in discussion with the author. This is a subsequent complete review of
the exact source bytes, not a claim of independent discovery or a blind
review. No computation is needed for the deductions or the example.

This source supplies the separator normal form and terminal lifts used
by the separate four-connectivity proof. It does not prove K5
contractibility or make a Hadwiger-seven or comparative significance
claim. This is an internal audit, not external peer review.
