# Audit: universal rainbow roots and a prescribed singleton bag

**Verdict: GREEN.** The [source](critical_colour_singleton_root.md), SHA-256
`b0707c128fa1d8847295fc5bbfd2c43d9a68d424b2b3e94ad17d98ef8e2272d7`,
proves the stated counterexample. This is a separate internal mathematical
audit, not external peer review or a computer-assisted finite result.

## Exact scope and provenance

The construction was supplied by this auditor and written independently by
the source author. This review therefore independently checks the written
argument and its quantifiers, but is not independent discovery of the example.
The complete draft at SHA-256
`88e1486bdd6e21d32dde5b7546ee47143436757aaa7fca8e306bdb692487e884`
was read before the final status-only replacement. No mathematical correction
was required. The source invokes no external theorem.

## Substantive checks

- The graph has exactly the stated two disjoint K4s, the independent pair
  x,y, the x--Q edges and the y--(L union Q) edges. In particular there is
  no unlisted x--y or L--Q edge.
- The displayed colouring supplies the five-colour upper bound, while
  Q union {x} supplies the matching lower bound.
- In **every** five-colouring, Q consumes four colours and forces both x
  and y into the remaining colour. The K4 on L avoids that colour because
  every L vertex sees y. Thus L union {x} is rainbow and the entire colour
  class of x is exactly the same fixed set J={x,y} in every such colouring.
- Deleting J leaves two K4 components. Hence chi(K)=4, and both L and Q
  use all four colours in every four-colouring of this fixed graph K.
- The minor obstruction applies in all of F, not merely K. If x is a
  singleton bag, each L-rooted bag must contain a Q vertex. Connectivity
  then forces y into every one of those four bags, contradicting disjointness.
  Extra unused vertices or a different assignment of Q vertices cannot
  avoid this single-vertex obstruction.
- The contrasting fully rooted model is valid: {x,y} union Q is connected,
  avoids all four L roots, and meets every singleton L bag through y.
  The four L bags already have all six mutual contacts.

There is no unresolved assumption in the stated finite construction. It
refutes only the additional demand that the x bag remain singleton. It does
not refute fully rooted K5 contractibility or establish a counterexample
inside the original seven-contraction-critical host.
