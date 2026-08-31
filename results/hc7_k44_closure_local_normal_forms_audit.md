# Cold audit: local normal forms for the `K_{4,4}` closure campaign

**Verdict:** GREEN for the five statements listed below.  The verdict does
not cover the open literal-core capstone, a peel/reconstruction theorem for
nonliteral branch bags, T44, Conjecture 21, or `HC_7`.

## 1. Hash-pinned sources

```text
c848504c758371545c27e60f577c06d096f5fd61714bfcab37f4cd80402af598  rooted_k4minus_four_roots.md
15ff05aec0d17184a9a50b3fe62e6097b27bfe10eafb5fda2e77dd4316a1f18b  rooted_k4minus_four_roots_verify.c
3aa9c7b2fb013d8da68695d6e4285c4829695fde2e6fa0c8e2163592d7b50c5f  hc7_k44_branch_model_and_double_cone.md
4b863b62699f62131e874d22bda0af127fb29c73de7da82da46c1f3d3e34811a  hc7_literal_k44_exterior_threeconnectivity.md
c77769fe640a75289106b1854cca35eeaa4ac379aec62cab95eb30a4f826365d  hc7_literal_k44_adjacent_portal_census_verify.c
965a92a736c4d9c891ebbd37f1bfd81415b864faea01c19e7b12adcac9787920  hc7_k44_four_portal_triangle_completion.md
1aaa5b12e0e9ad09024db2a87ad1a12aa84bc9474846359a3a862a55ce18d81d  hc7_k44_four_portal_triangle_completion_verify.py
115dcd59a36ae51db6dd59ecd4c8f8a09f0da91e1e0d6c974d7935418ca68ca4  hc7_k44_three_portal_k4_tetrahedral_dichotomy.md
f337ddc96f7354c14e642c315bb4798b53be45f4e2ec2e0848a7304223c96576  hc7_k44_three_portal_k4_tetrahedral_dichotomy_verify.py
```

The paths in this block are relative to `results/`.

The refreshed theorem-file hashes record documentation-only corrections to a
reproduction block, a provenance link, and an exact small-order scope
qualification; the audited statements, proofs, verifier inputs, and verdict
are unchanged.

## 2. Statements audited

1. Every three-connected graph has a rooted `K_4^-` model at any four
   prescribed distinct vertices, with the missing quotient edge unspecified.
2. Adding two vertices universal to a five-connected graph, with their
   mutual edge optional, forces a `K_7^-` minor.  Consequently an exact
   seven-cut boundary in a seven-connected target-free graph has no
   five-connected minor.
3. If a seven-connected target-free graph contains a literal `K_{4,4}` on
   `S`, then the exterior `G-S` is connected and has no cut of order at most
   two.
4. Three pairwise adjacent disjoint connected exterior bags, each seeing at
   least four core vertices, force a `K_7^-` minor.
5. Four pairwise adjacent disjoint connected exterior bags, each seeing at
   least three core vertices, force the target except for the tetrahedral
   profile `N(p_s)=Q-{s}`.  If the four bags span the exterior, global portal
   coverage excludes that profile.

The standard contraction criterion and its consequence are also sound: in
a vertex-minimal universal-T44 counterexample, every internal edge of every
nontrivial bag of every displayed `K_{4,4}` model belongs to an exact
seven-cut.  This assertion uses vertex-minimality among all T44
counterexamples.  It must not be transferred without proof to a merely
chromatic-critical host.

The separator-trace lemma is also GREEN.  It applies the two-near-full-model-
bridges lemma only when two complementary components are disjoint from the
entire model.  It expressly does not treat a component containing pieces of
branch bags as an exterior bridge and therefore yields no unsupported bound
on the number of traced bags.

## 3. Human proof audit

For the rooted diamond theorem, Dirac's three-vertex cycle theorem and a
three-fan either give a rooted `K_4` immediately or a cycle through all four
roots.  In the latter case, three-connectivity rules out the possibility
that every bridge of the cycle is confined to one consecutive-root arc.  A
nonlocal bridge has two attachments which can be placed in opposite rooted
arc bags.  Its internal path adds one diagonal to the four-cycle quotient.
No prescribed missing-edge location is inferred.

For the double cone, choose `v`, five neighbours `q,r_1,...,r_4`, and apply
the rooted diamond theorem in the three-connected graph `H-{v,q}`.  The
seven bags

```text
{x}, {y,q}, {v}, D_1, D_2, D_3, D_4
```

are disjoint and connected.  Absorbing `q` creates the first apex-apex
contact even when `xy` is absent, and the rooted diamond leaves at most one
other missing contact.  For an exact seven-cut, every complementary
component is full to the cut: if cut vertex `s` missed a component, the
other six cut vertices would still separate it.  Contracting two components
therefore gives the required double cone over any boundary minor.

For literal-exterior three-connectivity, disconnected exterior components
contract to two anticomplete seven-portal vertices.  A cutvertex gives two
adjacent six-portal bags.  At a two-cut `{p,q}`, two-connectivity makes every
component adjacent to both cut vertices and hence gives two adjacent
five-portal bags under both assignments of `p,q`.  The exact five-portal
census forces the complementary pair

```text
(B-{b_0}) union U,
(B-{b_0}) union (A-U),   |U|=2.
```

It also makes a third component impossible.  Deleting `{p,q} union B`
would then separate the two remaining sides unless `G[A]` has an edge
crossing `U,A-U`; the census verifies that any such edge closes the target.
This uses exactly six deleted vertices and is a valid invocation of
seven-connectivity.

The triangle and `K_4` results lift from portal vertices to arbitrary
connected exterior bags by contracting each bag first.  In the tetrahedral
exception the union of all four portal sets has order four.  A spanning
exterior model has portal union `N(S) cap V(K_{4,4})`, whose order is at least
seven by seven-connectivity, so the exception cannot occur there.

## 4. Independent executable audit

From the repository root:

```bash
cc -O3 results/rooted_k4minus_four_roots_verify.c -o /tmp/t44-root
/tmp/t44-root

cc -O3 results/hc7_literal_k44_adjacent_portal_census_verify.c \
  -o /tmp/t44-adj
/tmp/t44-adj >/tmp/t44-adj-profiles.txt

python3 results/hc7_k44_four_portal_triangle_completion_verify.py
python3 results/hc7_k44_three_portal_k4_tetrahedral_dichotomy_verify.py
```

The reproduced terminal counts are:

```text
rooted diamond: 225096 labelled three-connected order-seven graphs, GREEN
adjacent portals: partitions=11880, total=26569, negative=5428
five-plus-five exceptional profiles=48, crossing-edge positives=192
triangle: core_models=1656, fallback_profiles=1140, orbits=10
triangle digest=755316af73023902cbe205ec2f0b914b25677a61a5fb77dc129567a46fe6f552
portal K4: core_models=3784, restricted_failures=1170, negative_profiles=70
portal K4 digest=95b9d40e6e9ff1778b364b0a883fe0d72e7f41f9f5d9258c31af215ea38272bf
tetrahedral near-miss orbits=3, quotient edges=19
```

The two portal verifiers independently regenerate their restricted core
models by explicit assignments and validate the displayed fallback branch
sets.  The `K_4` verifier additionally checks the two eight-vertex summands
used in the clique-sum proof of target-freeness.  These are exact integer
enumerations, but still internal computer-assisted audits rather than
external peer review.

## 5. Explicit nonclosure

The exterior theorem supplies connectivity and excludes separators of order
at most two; for an exterior of order at least four, this is conventional
three-connectivity.  It does not supply a rich model.  The statement that
every such three-connected exterior has either a four-portal triangle, a
spanning three-portal `K_4`, or the target is still open; in a target-free
host it is already the whole literal T44 theorem in structured form.

Likewise, an exact seven-cut through a branch-bag edge does not say that a
component lies inside that bag, that cut traces are laminar, or that either
side preserves the eight model labels.  A component may itself contain
pieces of several branch bags.  No peel or reconstruction conclusion is
audited here.
