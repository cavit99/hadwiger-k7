# Five-root density in a three-component six-cut

**Status:** written proof with a separate hash-pinned internal audit. This closes the
four-, five- and six-edge boundary cases below, not the whole sparse case,
the six-connected `4n` theorem, Conjecture 21 or HC7. No novelty claim is made.

All graphs are finite and simple; `K7^-` means `K7` with one edge deleted.

## 1. Exact external input

We use Dvořák--Norin--Rahman, *Every graph with no K7^= minor is
6-colorable*, [arXiv:2609.17760v1, 15 September 2026,
Theorem 2.6](https://arxiv.org/html/2609.17760v1#S2), which attributes the
result to Dvořák, Theorem 4. Its primary statement and definitions were
inspected for this draft.

For a graph `H` with five prescribed roots `Z`, put

```text
rho4(H) = e(H)-e(H[Z])-4|V(H)-Z|.
```

The graph is **4-light** if every nonempty root-free set `Y` with at most
four external neighbours satisfies

```text
e(H[Y])+e_H(Y,N_H(Y))-4|Y| <= 0.
```

This is the fragment formulation in their Observation 2.5. Theorem 2.6
says that a 4-light five-rooted graph is universal for its density target:
every graph in that target occurs as a rooted minor for every bijection
of its vertices with the five roots. The exact target rows needed here are:

| `rho4(H)` | Every labelled graph on the five roots with at most |
|---:|---:|
| 4 | 6 edges |
| 5 | 8 edges |
| 6 | 9 edges |
| at least 7 | 10 edges |

Universality is stronger than an unlabelled minor assertion. We use it to
specify precisely the missing edges of the literal graph on the roots.

## 2. Retaining the sixth vertex

**Lemma.** Let `G` be six-connected and let a six-set `S` separate three
components `A,C,D` of `G-S`. Write `B=G[S]`, `b=e(B)`, and

```text
eta(C)=e(G[C])+e_G(C,S)-4|C|.
```

For any `x in S`, regard `H=G[C union S]` as rooted at `Z=S-{x}`.
Then `H` is 4-light and

```text
rho4(H)=eta(C)+d_B(x)-4.                         (1)
```

**Proof.** Every component of `G-S` is adjacent to every vertex of `S`:
otherwise its boundary would be a cut of order at most five. Likewise,
every nonempty subset of `C` has at least six external neighbours in `G`,
all in `C union S`; another component survives outside its closed boundary.

Let `Y subseteq C union {x}` be nonempty with `|N_H(Y)|<=4`. If
`W=Y intersect C` were nonempty, then

```text
N_G(W) subseteq N_H(Y) union {x},
```

contradicting the preceding six-neighbour bound. Therefore `Y={x}`.
Its fragment density is `d_H(x)-4<=0`, proving 4-lightness. Edges incident
with a nonroot are exactly the internal and boundary edges counted in
`eta(C)`, together with the `d_B(x)` edges from `x` to `Z`. There are
`|C|+1` nonroots. This gives (1). QED

**Lemma (full-clique completion).** In the preceding setting, if the
density target in Theorem 2.6 contains the graph `F` on `Z` whose edges
are precisely the nonedges of `B[Z]`, then `G` contains `K7^-`.

**Proof.** Obtain an `F` model with its prescribed five roots distinct.
Each literal edge of `B[Z]` supplies the corresponding bag contact,
because its two ends belong to their own distinct root bags. Thus the
five bags form a full `K5`. Add `A,D` as two further bags. They are
connected, disjoint from each other and from the five bags, and each
contacts every root bag through its prescribed root in `S`. Only their
mutual contact can be missing, so these seven bags give `K7^-`.
The vertex `x` may occur in any one of the five root bags or be unused;
it is never assigned to either added bag. All preimages are actual
disjoint connected subsets of the original graph. QED

## 3. Complete boundary rows

**Theorem.** Under the preceding hypotheses, suppose `G` has no `K7^-`
minor and `0<=b<=6`. Every component `C` satisfies the following bounds.

| `b` | Choose `x` of maximum boundary degree `d` | Terminal value of `eta(C)` | Hence `eta(C)<=` |
|---:|---:|---:|---:|
| 0 | 0 | 11 | 10 |
| 1 | 1 | 10 | 9 |
| 2 | 1 or 2 | 9 | 8 |
| 3 | 1, 2 or 3 | 8 | 7 |
| 4 | 2, 3 or 4 | 7 | 6 |
| 5 | 2, 3, 4 or 5 | 7 | 6 |
| 6 | 2, 3, 4 or 5 | 6 | 5 |

**Proof.** The missing-edge graph `F` has `10-b+d` edges. At each listed
terminal value, substitute `rho4=eta+d-4` in the external target table.
For every listed degree its edge capacity is at least `10-b+d`.
The preceding completion lemma gives `K7^-`, a contradiction. Larger
values remain terminal because the target edge capacities are monotone.
Integrality gives the final column. QED

**Corollary (three complete sparse cases).** Suppose additionally that
`G-S` has exactly these three components and `e(G)=4|V(G)|+sigma`, with
`sigma>=0`. Then `b` cannot be 4, 5 or 6.

**Proof.** Exact edge accounting gives
`sum_C eta(C)=24+sigma-b`. For `b=4,5`, the theorem bounds this sum by
18, while accounting makes it at least 20 or 19, respectively. For
`b=6`, the upper bound is 15 and the lower bound is 18. QED

## 4. Remaining scope

For any `b`, equation (1) and `eta(C)>=11` give `rho4>=7`, so the same
completion proves `eta(C)<=10`. If `mu_S(C)` is the maximum number of
disjoint connected subsets of `C` each adjacent to every vertex of `S`,
this proves `eta(C)<=5 mu_S(C)` whenever `mu_S(C)>=2`.

The packet-one range `6<=eta(C)<=10` is not eliminated. For `b=3`, the
table and accounting force `sigma=0` and all three excesses equal to 7;
the rows `b=0,1,2` also remain unresolved. Deleting `x` instead gives an
internally five-connected rooted graph with density `eta(C)-e_G(C,{x})`.
That lost incidence term cannot be discarded. A near-clique model using
`x` cannot reserve `x` again to join the two external bags. These are
the precise limits of this application, not counterexamples to the
[sparse-case target](../active/hc7_k7minus_sixconnected_4n_sparse_threecut_frontier.md).

DNR's introduction already records the obstruction obtained by joining a
four-clique to a matching. For a matching boundary, treating five root
bags, two helpers and the two other lobes as indivisible can give a subgraph
of this obstruction, even after granting all helper contacts. Strengthening
those contacts alone does not supply the missing original-host allocation.
