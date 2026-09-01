# Independent internal audit: literal-`K_{4,4}` singleton-atom reduction

**Verdict: GREEN.**  The exact theorem and verifier revisions identified
below are valid at their stated scope.  The theorem is an unbounded written
reduction with one finite local lemma; it reduces every complete system of
tight blockers to a singleton all-edge atom and proves that every crossing
blocker meets its seven-neighbourhood in exactly one exterior vertex.

This is a separate internal mathematical audit, not external peer review.

**Audited theorem:**
[`hc7_k44_positive_atom_elimination.md`](hc7_k44_positive_atom_elimination.md)

**Theorem SHA-256:**
`775a4f5a6cf2f455a2ca54a232146fd2f4b22a1c88e7e38770b26bfb83df8e07`

**Audited verifier:**
[`hc7_k44_positive_atom_elimination_verify.py`](hc7_k44_positive_atom_elimination_verify.py)

**Verifier SHA-256:**
`fc6e0eb9173bfd24a9c823b0f5f0634ae10ed93a5a707e048268015733e97250`

## 1. Audit method and verdict

The proof was reconstructed line by line after the final one-resource
strengthening.  The audit checked the safe-contraction pullback, the
all-contractible-edge atom selection, every resource identity, the marked
partition reduction, every displayed minor model, the new seven-root
boundary colouring, and the prescribed-portal Menger dichotomy.  A separate
run of the verifier reproduced every advertised count and digest.

No unresolved gap was found in Theorem 1.1 or Propositions 7.1--7.3.  The
weighted splitter theorem and the literal case of T44 remain outside the
verdict.

## 2. Atom selection and exact blocker obstruction

The safe-contraction obstruction is exact, including a co-spanning blocker.
A quotient set containing the contracted vertex has the same boundary and
label union as its preimage.  A quotient set avoiding it loses one boundary
vertex exactly when both ends of the contracted edge belonged to its old
boundary.  Since every old resource value is at least seven, failure is
equivalent to an old tight blocker.

The ballast augmentation has connectivity exactly seven.  The family of
endpoint pairs of all three-contractible edges is connected because it
contains the contractible spanning tree from the preceding audited theorem.
The generalized Mader atom estimate therefore applies to every crossing-edge
blocker, not merely a blocker chosen for one tree edge.  Chan's Lemma 7.19,
the Mader trace lemma, applies to the same family and gives

\[
                         |X\cap B|\ge |A|.
\]

The order-three equality, the local strict resource inequality, and the
proof that `C-A` is connected were independently recomputed and are exact.

## 3. Marked partition and portal computation

Lemma 3.1 is a valid application of Theorem 23 of
Chen--Kleinberg--Lovasz--Rajaraman--Sundaram--Vetta.  In the bidirected graph
with arcs leaving the roots deleted, the Fan Lemma supplies the required
sink connectivity.  Unit and zero demands have maximum demand one.  The
strict sink-capacity bounds, integrality of marked-origin loads, and equality
of the total demand force the prescribed exact quotas.  Removing circulation
and attaching unused components preserves disjointness, rooted connectivity,
and all marked counts.  Lemma 3.2's Hall-deficiency calculation is also
exact.

The verifier exhausts the two finite local statements and nothing unbounded:

- all 295 symmetry orbits for the positive `q=1,2,3` seven-portal triangle;
- all three distinguished `5,1,1` orbits; and
- all ten one-incidence completions of the unique negative `5,1,1` orbit.

The action has order `4!^2 times 2=1152`, sorting the three rows gives the
exact `S_3` quotient, and the restricted-growth enumeration contains all
`S(11,7)=63,987` spanning seven-bag partitions.  Connectivity and at least
twenty quotient contacts are tested directly.  The negative assertion is
exhaustive because any seven-bag model in the connected eleven-vertex host
can be made spanning by attaching each unused component to an adjacent bag.

The reproduced output was

```text
partitions 63987
q 1 positive 20
q 2 positive 77
q 3 positive 198
digest 48afac546bfa7bb92768b77581a774eeb735faf477a870886ea03f02b3a2c3f5
singleton_5_1_1_orbits 3
singleton_5_1_1_positive 2
singleton_5_1_1_survivor (55, 8, 64)
singleton_5_1_1_digest a0812a66b38384445f877fa4cac909b4bea11a13d36364643cf9e1100ae2c6e8
singleton_big_to_small_additions 10
singleton_addition_digest ce2f0641c454480ccd151d3d4679cc320b7a15abfd7a559622273240893e8565
```

## 4. Elimination of every non-singleton atom

For positive label weight, the strict local inequality supplies exactly the
label multiplicities used in the order-two, triangle, and path cases.  In
the path case the two endpoint bags touch either through a cross-incidence or
through the fixed contractible boundary edge.  Lemma 4.1 then applies.

For zero label weight, the seven disjoint `B`--`S` paths avoid the atom and
give a `K_{3,4}` quotient.  The matching choices in the order-two and
three-vertex path cases cover both miss sets.  In the triangle case the
three miss-set identities, strict boundary restrictions, and two-edge
matching choice cover every shore distribution.  Each construction gives a
five-bag `K_5^-` quotient complete to two adjacent atom bags, hence twenty
contacts.  Thus the conclusion `|A|=1` is valid.

The exact singleton `5,1,1` enclosure and the bipartite `3`-by-`4`
neighbourhood follow from the finite profile classification and the
seven-path core linkage.  The same-shore chord construction has the stated
twenty contacts.

## 5. Exact one-resource crossing blockers

The resource split in Proposition 7.1 was checked directly.  For
`D=partial X`, the identity

\[
                         |S-D|=|D-S|+1
\]

and the at-most-three-component theorem permit all exterior roots in `D` to
be allocated among the complementary components within their literal-core
capacities.  Closed-shore rooted connectivity and Menger's theorem then give
seven disjoint `D`-rooted path bags, each meeting `S` in exactly one distinct
representative and leaving one core vertex unused.

If an edge of `G[D]` had same-shore representatives, adding the unused core
vertex to an opposite-shore bag leaves a `K_{3,3}` plus that chord on the
other six bags.  One contraction gives `K_5^-`; the enlarged bag and `X` are
both universal.  The contact count is

\[
                              9+5+6=20.
\]

Hence `G[D]` is bipartite with class orders three and four.  If
`m=|R|+|T|>=2`, the edges from `a` to `M=R dotcup T` put all `M` representatives
on one shore.  Delete the entire `a`-rooted bag, prescribe two `M` bags as a
pure same-shore pair in the six-root `K_6`-minus-matching extension, and add
`a` to one of them.  This repairs one missing contact, while `X` is universal
to all six bags.  The result again has twenty contacts.  Therefore `m=1`;
because `b in R`, necessarily

\[
                         R=\{b\},\qquad T=\varnothing,
                         \qquad |K|=5.
\]

The `P`-leaf argument is also valid.  A leaf `p` of the minimal subtree on
`P` leaves all of `P-\{p\}` in one component `Y_0`.  Any other component
`Y_1` is `P`-free and has exact boundary `H union \{p\}`.  The component
`Y_0` sees `a,p` and at least five of the six roots in `H`; two corresponding
representatives share a shore.  Absorbing `Y_0` repairs that prescribed pure
pair, and `Y_1` is universal to the six bags.  Thus `X-p` is connected, and
two subtree leaves give two distinct non-cutvertices when `|P|>=2`.  The
separate `P=\{p\}` two-component construction is correct as written.

## 6. Recentring and prescribed portal omission

For a singleton blocker `X=\{p\}`, the exact boundary contains the ends of
the three-contractible edge `ab`, so `p` is another all-edge singleton atom.
The recentered small `a`-rooted bag proves `L(a) cap L(p)=varnothing`.
Repeating the `5,1,1` argument on the triangle `a,p,b` proves both
three-portal union bounds.  Hence adjacent singleton atoms have exactly one
common neighbour, and it is exterior.

Proposition 7.3 is an exact set-Menger dichotomy.  Failure of the saturated
linkage gives a separator of order at most `6-q`; seven-connectivity upgrades
it to equality and an exact seven-cut.  Inclusion-minimality removes `a`
from the separator.  When `q>=1`, omitting one portal from each literal-core
shore gives two proper boundary colourings agreeing on `Q`; their class-size
change is one, so some flipped `Q`-free component has nonzero odd imbalance.

## 7. Pinned inputs and trust boundary

The audit accepted the following adjacent GREEN inputs at these source
revisions:

| input | source SHA-256 |
|---|---|
| literal exterior three-connectivity | `4b863b62699f62131e874d22bda0af127fb29c73de7da82da46c1f3d3e34811a` |
| weighted-splitter small-atom reduction | `bc4f7d38d94beed2d86b9858a2290fd1cb85af398653b5b16a5d3231f80eb2db` |
| four-portal triangle completion | `965a92a736c4d9c891ebbd37f1bfd81415b864faea01c19e7b12adcac9787920` |
| exact seven-boundary double-cone theorem | `88b93cb80a4bd916fed0d10b68e74d0caba5c7c62492f8f667e59c0bef8a900e` |
| at-most-three components behind a seven-cut | `cbd3ecb73bea0530797ad58080ae6db6052bfbf69f90af558283e3f250772ef8` |
| closed-shore rooted connectivity | `ba6dbfe1ca9e89041b1a77174844c24598984cbe76349a55c41f15b2e997cc03` |

The external inputs accepted at their cited strength are Costalonga's
Theorem 1.5, Mader's generalized atom lemma and trace lemma in the cited
formulations, and Chen et al. Theorem 23.  Fan, Hall, and Menger are used in
their standard forms reconstructed in the proof.

The finite trust boundary is Python integer, tuple, and set semantics;
successful assertion execution; the explicit eleven-vertex graph
construction; the complete restricted-growth enumeration; and the stated
automorphism action.  No bounded exterior census appears in this theorem.

## 8. Exact unresolved scope

The audit is GREEN only for the all-edge singleton-atom and exact
one-resource blocker reduction.  The remaining unbounded task is the
singleton all-edge atom completion lemma in Section 8 of the theorem.  In
particular, this audit does **not** prove the weighted splitter theorem, the
literal `K_{4,4}` case of T44, T44, Norin--Totschnig Conjecture 21, or
`HC_7`.
