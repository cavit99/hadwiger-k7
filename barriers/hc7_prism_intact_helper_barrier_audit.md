# Audit: intact helper ownership barrier

Date: 21 September 2026.

**Verdict: GREEN for the stated construction-step barrier.** The reviewed
[source](hc7_prism_intact_helper_barrier.md) has SHA-256
`956c8ae01234f20d26d8dc74c45a30f513423aa021d18a700c4b8717a54d624d`.
No gap was found in the claimed four-connectivity, ordinary K5 model,
absence of a T-meeting K5 model, or helper maximality. The noncontainment
and connectivity arguments were reconstructed independently of their
author. The reviewer supplied the direct maximality simplification
before source freeze; that component is not an independent audit of a
different author's argument. This is internal review, not external peer
review.

## Strongest checks

- **Exhaustive branch-bag cases.** Five disjoint bags meeting six roots
  leave at most one two-root bag. A bag avoiding x,y and containing one
  root can contain only that root and its matched ai. Three such bags
  forming a clique therefore use one whole triangle. This also rules
  out a model with fewer than two distinct bags containing x,y, including
  models leaving vertices or one root unused.

- **Two special bags.** If all three other bags have one root, their
  whole triangle forces every ai outside the opposite special bag,
  disconnecting that bag's helper vertex from its required root. If
  an ordinary bag has two P roots, the two remaining ordinary roots
  must be the opposite matched Q roots: a mixed pair would have to be
  matched at the third index and could not contact the two-root bag.
  The special roots must then have their natural assignment, since
  reversing them requires the same ak in both bags. The two required
  cross-contacts exclude ai,aj from the only locations allowing the
  final contact. The Q case is symmetric.

- **Mixed two-root bag.** Connectivity without x,y forces a matched
  pair pi,qi and its ai. The other ordinary roots are either in one
  triangle or form another matched pair. The first choice again removes
  both possible connecting vertices from a special bag; the second
  requires aj in two disjoint pairs of bags. These alternatives exhaust
  all remaining root placements. No fixed singleton normal form or
  finite-search conclusion is assumed.

- **Other claims.** The deletion argument covers every set of at most
  three vertices; a degree-four root supplies the upper bound. The five
  displayed ordinary-minor bags have every required contact. In a
  spanning P-full partition with Q in D', placing x in E' forces every
  ai into D'; placing x in D' forces A and then y into E', leaving x
  disconnected from Q in D'. Thus the claimed maximum is exactly two.

## Scope retained

The source is a self-contained obstruction to a universal repair after
contracting each of two helper pieces to one vertex. It retains an
induced nontrivial prism complement and a maximum helper. It does not
retain five-connectivity, the root-free six-neighbour boundary condition,
or the original critical-host colouring constraints. Splitting or
exchanging vertices inside actual helper pieces remains possible. There
is no counterexample to the actual-host target, no closure of the
two-triangle or degree-seven cases, and no proof of HC7 here.
