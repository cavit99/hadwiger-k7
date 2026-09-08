# Audit of the K5-scheme separator reduction

**Verdict: GREEN.**

This separate internal audit covers the complete
[source](k5_scheme_separator_reduction.md) at SHA-256
`102bced36c8fd794b7d52870fb4c2041e2955068c54d5130ac23adc24538e616`.
The source remains conditional on a minimum counterexample existing.
Only the status sentence changed after the complete proof review.
Reversing that sentence exactly recovers the reviewed source at
`ebea05fc794fe48745a1d7d31aba7d075a4905a57f5872302232722c203ca1b7`;
the mathematics is unchanged.

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

## Scope and provenance

The auditor previously checked the rainbow and repeated-colour outlines
in discussion with the author. This is a subsequent complete review of
the exact source bytes, not a claim of independent discovery or a blind
review. No computation is needed for the deductions or the example.

The unresolved rainbow three-cut allocation remains unresolved. The
source establishes neither four-connectivity of a minimum counterexample
nor K5 contractibility, and it makes no Hadwiger-seven or comparative
significance claim. This is an internal audit, not external peer review.
