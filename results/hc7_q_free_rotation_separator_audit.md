# Audit: a missing pair is fixed across a Q-free transfer

Date: 9 September 2026.

**Verdict: GREEN — separate internal whole-source review.** The reviewed
[source](hc7_q_free_rotation_separator.md) has SHA-256
`5f8c447153fd5961f7fb5835db426cbe8e7f89ada25f854c4700958b31d2f815`.
No unresolved inference was found under its explicit hypotheses.

## Strongest checks

- Both connected-union assumptions force every component of G[Z] to
  contact both centres. The XW edge is separately assumed and supplies
  the centre adjacency; it is not inferred from either union.
- With one common deficient label, merging its row with a touching
  component leaves exactly seven connected disjoint bags and two
  independent holes. For disjoint pairs, two different components repair
  different row labels; if unavailable, the two nonempty component
  families must be one singleton, giving the stated combined-centre
  seven-bag model with at most one hole. Hence the pairs are equal.
- For the equal pair, contacts with its two rows likewise belong to one
  component K. Every other transfer component misses both rows, so its
  absorption preserves the exact pair, connectedness and XW adjacency.
  This works for any number of components, with no spanning assumption.
- In the ambient Menger graph, the four contracted bags become distinct
  terminals and all other undeleted vertices remain. A two-path set
  linkage uses every terminal as an endpoint, never internally. Its
  lifted interiors therefore avoid every row and centre preimage, and
  the seven final bags have only the two independent possible holes.
- Connected K supplies a surviving source-to-target path after deletion
  of any auxiliary terminal or any vertex outside K. Thus the singleton
  Menger separator is an actual uncontracted p in K. Any original path
  avoiding p and the three deleted row bags would descend to a forbidden
  auxiliary walk. The separation therefore includes all unused bypasses.

## Scope and provenance

The constructive arguments are proved in the reviewed source. The older
rotation files are comparison and application links, not proof
dependencies here.

The reviewer previously checked the pair-lock and component reductions
and the local unordered linkage. Route-assessment proposed the ambient
strengthening; the reviewer independently checked it and the complete
written source. This is internal review, not external peer review.

The conclusion fixes a pair only while the five literal row bags remain
fixed. It does not transport colouring constraints or additional roots,
cover transfers lacking XW or either union's connectedness, or supply a
decreasing induction. The separator contains three whole bags: seven-
connectivity bounds their total size below, not above. No C19, HC7 or
global exchange closure is established.
