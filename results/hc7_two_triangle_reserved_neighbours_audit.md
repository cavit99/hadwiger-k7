# Internal audit: a rooted four-clique with three reserved neighbours

**Verdict: GREEN.**

Audited source: [the reserved-neighbour theorem](hc7_two_triangle_reserved_neighbours.md),
SHA-256 `f96680f0556ec70a089d6efe04d38f9ae0683b2a8db6c6c569e5d7850506c2d7`.
This is an internal mathematical audit, not external peer review.

Promotion changed only the status sentence and relative input links.
Reversing those edits recovers the audited draft SHA-256
`9ec428d689724e26842d031874f1a35bff545661597c7b95d16665dd521c8f23` exactly.

The auditor previously checked the author's four-region terminal model.
The complete frozen source was then read separately, with an independent
check of the density input, all four deletion responses, their actual
boundaries, and the disjointness argument. That earlier spot-check is not
presented as independence from the entire development.

## Inputs and strongest checks

The four input source hashes in the draft were recomputed and matched:
contraction closure `ab7ce8ad…`, exterior theorem `e51564c9…`,
exterior helpers `b3fe07ea…`, and triangle-poor-edge packing `2ffeb857…`.
The last source's audit also matches `bfc73f1d…`.
The invoked contraction statements, exterior conclusion, exact recorded
Norin–Totschnig alternative, and Jakobsen bound/cockade exception were
reread. No fresh primary-source inspection or finite enumeration is claimed.

- **Root choice.** Contracting `xy` permits at most one contact into each
  triangle, because its contact with `v` is retained. Contracting either
  triangle forbids two cross-edges with distinct ends in the other one;
  consequently at most one A–B edge exists. Two available choices in each
  triangle suffice to avoid it and obtain exactly the stated induced `R`.
- **Every four-deletion is nonplanar.** A `K_7^-` minor contains `Q`.
  Seven-connectivity excludes both cockade bases and every nontrivial
  four-clique sum. Thus `2m<=9n-25`, while `delta>=8` gives
  `q=m-4n>=0`, total degree excess `2q`, and `q<=(n-25)/2`.
  For an arbitrary four-set, the degree sum is at most `32+2q`.
  The source's deletion count includes the internal-edge correction,
  and exceeds the planar bound by at least `n-14-q>0`.
- **Actual failure sides.** Each `J_r` is three-connected and nonplanar,
  excluding the trisection and planar alternatives. A component of the
  root-free open side avoiding `r` lies in `W` and has at most six actual
  G-neighbours, with `v` surviving outside. Hence the whole open side is
  connected, contains `r`, and has a nonempty W remainder. A surviving
  T root then forces all seven boundary contacts in G, giving exactly
  six in `F=G-v`. The separator vertices are disjoint from `R`.
- **Disjointness.** External neighbourhood cardinality is submodular via
  closed-neighbourhood coverage minus set cardinality. A nonempty
  intersection lies in `W`, has no `v` contact, and has F-boundary at
  least seven. The union avoids six named vertices, so its F-boundary
  is at least six. These bounds contradict `6+6>=7+6`; no assumption
  of equal intersection and union bounds is used.
- **Seed extraction and model.** Each chosen component of `D_r-r` has
  boundary contained in the seven actual vertices `R union S_r`, and
  `v` survives outside; it is therefore full to `R`. Disjointness survives
  choosing one component per response and growing them to partition `W`.
  The displayed two universal bags and the five-bag `W_4` are connected
  and disjoint. Their double cone is `Q`; no unused port path or contact
  between the fourth part and another part is required.

## Scope

For every allowed choice of `a,b`, at least one reserved root `r` gives
the stated T-rooted clique avoiding the other three and `v`. The model
may use `r`. No common model for different choices, compatible additional
helper, five-connected contraction quotient, or two-triangle case closure
follows. No unresolved gap was found within the stated theorem.
