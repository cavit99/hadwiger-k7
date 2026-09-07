# Independent audit of the five-root almost-clique theorem

**Verdict: GREEN.** Separate internal mathematical audit.
**Date:** 7 September 2026. This is not external peer review or a claim that the programme's
global objective has been achieved.

## Exact source and external input

The complete source audited is
[hc7_five_root_almost_clique.md](hc7_five_root_almost_clique.md), SHA-256
`de183e350c412739c05a744e811304454ba90856efee9e097813c70617bba9cd`.
Its conclusion is an `S`-rooted `K_5^-`, for five roots containing a literal
triangle, internal five-connectivity relative to those roots, a nonempty
nonroot set, and nonroot minimum degree seven. One triangle root `r` is
designated in advance; the only possible missing pair is `rb` or `rc`, and
at most one is absent.
The appended extension retains the conclusion when every nonroot has
degree at least six and at most five nonroots have degree exactly six.

The initial audit covered draft hash
`a9e29a0f92fbe507b8de31304e33dceced9aa8d31e75ee7148560b798853c3f4`.
I then reread the complete promoted source at SHA-256
`03a5fb70196132aea5a31fb024b41742d4b36895f3f9516607df6c6905571857`, including the stronger
designated-root conclusion and the explicit exclusion of root-only
components in the planar case. The bounded-deficit extension was appended
without changing those earlier bytes at source SHA-256
`c02c6169f2a74a8201132215f17e600bb93e40c0003f1b5f5cc743571d169cfd`.
A separate reviewer independently checked that complete appended section,
including its degree count and induction class, at that hash. The only
subsequent source change clarifies that the open minimum-degree-six
question in the old Scope paragraph allows an unrestricted location for
the missing pair. The original theorem and proof are unchanged. The
verdict applies to both the original theorem and the extension at the
final bytes pinned above.

I independently reread the complete source and
[Norin--Totschnig, Theorem 8 and the preceding definitions](https://arxiv.org/html/2507.03244v1#S2).
The four alternatives, the order-two common intersection in a trisection,
and the definition of internal connectivity agree with the input quoted
in the draft. No stronger rooted-model assertion is substituted.

## Strongest inference checks

- **Induction and root transfer.** Initially there are at least three
  nonroots. Absorbing a root's unique nonroot neighbour leaves every
  surviving nonroot neighbourhood unchanged except for relabelling that
  neighbour. When `b,c` have precisely the nonroot neighbours `p,q`, the
  simultaneous contractions `bp,cq` likewise replace `p,q` injectively by
  two distinct roots. The old `b,c` were adjacent to no surviving
  nonroot. Thus both boundary cardinalities and nonroot degrees are
  preserved exactly. The parameter `|B|` strictly decreases; all prescribed
  roots and the literal triangle remain distinct and intact. Connected,
  disjoint preimages provide the required lift.

- **Location of the possible missing pair.** The strengthened induction
  fixes `r` from the outset. Both reductions preserve its named label and
  all three root-triangle edges. The only direct model construction is
  the four-clique rooted at `b,c,s,t`, together with the `r` bag. Its
  contacts to `s,t` are literal and at least one of its `b,c` contacts is
  supplied. Thus exactly the claimed pair restriction is retained in
  both the direct construction and every inductive lift.

- **All six four-clique contacts survive the helper argument.** The two
  helper bags retain their mutual contact. For either other bag, distinct
  ports can be selected for its two helper contacts whenever at least two
  actual ports exist. Minimality permits restriction to a tree joining
  these ports and its root. Some nonroot selected port is a leaf and can
  be transferred to its helper; the cut tree edge replaces that helper
  contact, while the other port remains. The literal root edge `st`
  preserves the remaining clique contact. This contradicts the maximal
  helper union, so each other bag has one actual port. Unused components
  touching the helpers can also be absorbed. The resulting boundary has
  at most two actual vertices, rather than merely two bag labels.

- **The singleton conclusion uses the right boundary.** If `r` misses
  the helper union `W`, the root-free set `W-{b,c}` has boundary among
  those two ports and `b,c`. Internal five-connectivity forces it empty.
  Each singleton helper then has both ports as neighbours. Since every
  root has at least two nonroot neighbours after normalization, both
  ports are nonroots and the simultaneous transfer applies.

- **Trisection.** Each open side is its single prescribed root; any
  additional nonroots would have boundary of order at most three.
  At least one nonroot remains off the two ports. A root port would leave
  this nonempty set with at most the two central roots and one nonroot
  port as neighbours, again contradicting internal four-connectivity.
  With nonroot ports, the literal edge `st` prevents either endpoint from
  being an isolated open root. The two open roots are consequently `b,c`
  and have the same two nonroot neighbours.

- **Planar equality.** Connectivity follows from internal four-connectivity
  and the normalized root-to-nonroot degrees. The cofacial four-root
  drawing gives `e(J)<=3|J|-7`; the degree lower bound gives equality.
  Its distinguished face walk therefore has length four and contains
  four distinct roots, so it is their four-cycle. This contradicts the
  equality degrees of `b,c`, which already have two nonroot neighbours.

## Bounded-deficit extension

The extension was checked separately from the original minimum-degree-seven
proof. Its additional cases and strongest new inference are as follows.

- **Small base and induction class.** With two nonroots, their degree at
  least six in a seven-vertex graph makes both universal. Adding one to
  each of `b,c` gives a rooted `K_5`, retaining all designated contacts.
  Every surviving nonroot degree is unchanged under either transfer, so
  the number of degree-six nonroots cannot increase. A one-nonroot result
  is impossible because it would have degree at least six on six vertices.
  The same strict parameter and disjoint rooted lifts therefore apply.

- **Two-connectivity is proved before counting a facial cycle.** After
  normalization, each root has at least two nonroot neighbours. Following
  deletion of at most one vertex, every component contains a nonroot;
  otherwise a root-only component contradicts those two neighbours. The
  nonroots of each component have neighbours only at its roots and the
  deleted vertex. Internal four-connectivity forces at least three of
  the four roots into each component, ruling out two components. Thus the
  cofacial boundary is a simple cycle, rather than an unrestricted walk.

- **The deficit count is strict.** If the boundary contains `h` nonroots,
  its length is `4+h` and `2e(J)<=6|B|+10-2h`. The nonroot degree sum is
  at least `6|B|-5`. At least eight root-to-nonroot incidences are supplied
  by normalization; the cycle supplies at least `8-2h` root-root incidences,
  while `st` always supplies two. The lower bound therefore exceeds the
  upper bound by at least `max(2h,6)-5>=1`. Incidences to roots and to
  nonroots are disjoint categories, so none is counted twice.

The other three external alternatives use the unchanged boundary, port
and root-normalization arguments; they do not require every nonroot of
`J` to have degree at least six. No extra literature or finite computation
is used for the extension.

## Scope and unresolved work

No mathematical gap or additional hypothesis was found at the pinned
revision. No finite computation is a premise of this proof. The audit
does not establish novelty or a disjoint sixth helper. Although the
triangle endpoint of the possible missing edge is controlled, the proof
does not choose which of `rb,rc` may be absent. It does not prove the six-root
strengthening, Conjecture 19, Conjecture 21, or Hadwiger's conjecture for
`t=7`.
