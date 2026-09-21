# Internal audit: five-root density in a six-cut

**Verdict: GREEN for the stated theorem and corollary.** This is a separate
internal mathematical audit, not external peer review. The proof has no
finite-order restriction and uses no computer-assisted mathematical claim.

Audited [proof](hc7_five_root_density_sixcut.md), SHA-256:

```text
4c31950cca633178dbcff0800a0ac1b55bc5a58cf9fe0127f165b1a24017a812
```

Reversing the promotion's status and relative-link changes reproduces
the previously audited hash
`cad750a9b40adabedf976cf9f397ecfbcec67273c8f5f1a79104b031ffcaf20e`.
The mathematical text is unchanged.

The external theorem is accepted as an input. Its statement, definitions
and this application were checked against Dvořák--Norin--Rahman,
[arXiv:2609.17760v1, Section 2](https://arxiv.org/html/2609.17760v1#S2),
accessed 21 September 2026. This audit does not reconstruct that paper's
proof or its cited proof of Theorem 2.6.

## External hypotheses and retained vertex

Observation 2.5 tests every nonempty root-free set with at most four
external neighbours. There is no additional independence requirement on
the roots. Theorem 2.6 supplies every bijection of each target's five
vertices to the five prescribed roots, not just an unlabelled model.

Fix any component `C` and any `x in S`. For every nonempty `W subseteq C`,
all neighbours outside `W` lie in `(C-W) union S`; a vertex of either
other component survives outside `W union N_G(W)`. Consequently a boundary
of order at most five would contradict six-connectivity. In particular,
each entire component has all six boundary vertices as neighbours.

For a root-free set `Y subseteq C union {x}`, putting `W=Y intersect C`
gives `N_G(W) subseteq N_H(Y) union {x}`. If `W` is nonempty and
`|N_H(Y)|<=4`, this contradicts the preceding bound.
The only remaining test is `Y={x}`, whose density is its degree in `H`
minus four and is nonpositive whenever its boundary has order at most
four. Thus lightness holds for **every** choice of the omitted root.

The edges from `C` to `x` remain counted in `eta(C)`. Making `x` a
nonroot adds exactly `d_B(x)` previously uncounted boundary edges and
one nonroot vertex, giving `rho4=eta(C)+d_B(x)-4`. No incidence edges
are discarded.

## Seven branch sets and numerical thresholds

Use the identity labelling for the complement `F` of `B[S-{x}]`.
Every root lies in its own distinct model bag, so each literal boundary
edge absent from `F` supplies the corresponding missing bag contact.
The resulting five bags form a full `K5` model. Their vertex sets lie in
`C union S`. The two other entire components are connected, disjoint
from these bags and from one another, and each contacts every prescribed
root. The resulting seven bags miss at most the pair between the two
external components. Nothing requires `x` to remain available afterwards.

Here are the pairs `(rho4, e(F))` obtained at the asserted terminal
values, with maximum degrees listed in the order used in the proof:

| `b` | Pairs at the terminal value |
|---:|---|
| 0 | `(7,10)` |
| 1 | `(7,10)` |
| 2 | `(6,9), (7,10)` |
| 3 | `(5,8), (6,9), (7,10)` |
| 4 | `(5,8), (6,9), (7,10)` |
| 5 | `(5,7), (6,8), (7,9), (8,10)` |
| 6 | `(4,6), (5,7), (6,8), (7,9)` |

All maximum-degree possibilities are covered. Each pair belongs to the
claimed external target. In particular the exceptional density-three
target, which excludes `K2+K3`, is never used. The target capacities are
monotone throughout the invoked range. Integer excesses therefore satisfy
exactly the upper bounds stated in the theorem.

When there are exactly three components, each non-boundary edge is counted
once in their excesses, giving `sum eta=24+sigma-b`. The upper sums for
`b=4,5,6` are respectively `18,18,15`; the lower sums are respectively
`20,19,18`. These are strict contradictions. For `b=3`, the sum bounds
instead force `sigma=0` and three excesses of seven, as stated.

For arbitrary `b`, excess at least eleven gives density at least seven
for any `x`, so the all-targets row proves `eta<=10`. Consequently
`eta<=5 mu_S(C)` follows when `mu_S(C)>=2`. This does not establish the
packet-one alternative or close `b=0,1,2,3`.

The appended matching-quotient limitation is also valid. If the five root
vertices induce a matching, granting every possible contact among the
other four vertices and from them to the roots produces the join of `K4`
with a matching and possibly an isolated vertex. This is a subgraph of
the matching-join obstruction described in the external paper's
introduction. In any seven-bag model, at least three bags avoid the four
universal vertices; their contacts form a minor of a matching. They cannot
supply the two or more edges required on any three vertices of `K7^-`.
This establishes a limitation of those indivisible quotient bags, not a
counterexample satisfying the original six-connectivity hypotheses.

## Separate check of the external C19 application

The external statements and their application in Sections 1--2 of the
[C21 construction frontier](../active/hc7_c21_rooted_density_construction.md) were
also checked at SHA-256:

```text
8fc21f9a9cf0ae185a2bf3c8699a955ce66654b5b984a7c2100519f371a26dd3
```

Sections 1--2 are unchanged from the first audited version; the pin was
updated after new local results were recorded in later sections.

**Scoped verdict: GREEN.** Theorem 1.1 has exactly the `K7-2K2`-free
six-colour conclusion. Theorem 1.3 requires five-connectivity, order at
least six and at least `4n-7` edges. The former C19 host is `K7-2K2`-free,
seven-connected and has minimum degree eight. It therefore has order at
least nine and at least `4n` edges, so Theorem 1.3 excludes it directly,
regardless of its neighbourhood or exterior-colouring case. Theorem 1.6
also has the critical-host hypotheses and conclusion reported there.

The retained rooted-helper corollary supplies the stronger local lower
bound `e>=4n` and absence of a literal `K5`. Its source hash remains
`6ffee04cf9ff66275f9674c24bc2b9c669b1e108b76e5b1d2a18ec7d0106fe67`,
matching its existing separate audit. Those earlier proofs were not
reaudited here. This application check does not audit the conjectural
construction in the later sections or prove C21.

## Remaining assumptions and scope

No unresolved inference was found in the six-cut theorem, its corollary
or the scoped C19 application. Their external theorem assumptions remain
explicit. No claim of novelty, full sparse-case closure, C21, HC7 or
achievement of the user's comparable-theorem objective is certified.
