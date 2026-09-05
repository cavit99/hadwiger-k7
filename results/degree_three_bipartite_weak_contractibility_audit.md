# Independent internal audit: degree-three bipartite schemes

**Status:** separate internal audit of a written proof; not external peer review.

**Exact source checked:**
[degree_three_bipartite_weak_contractibility.md](degree_three_bipartite_weak_contractibility.md),
whole-file SHA256
`72e52cdcb734bd5620e4c3d6cc3bdd29d7861563bc9ba2507ff39d1c6c2d609d`.

**Verdict: GREEN.** Lemmas 1 and 2 and Theorem 3 have valid written
proofs. For every finite simple bipartite target `H=(A,B)` with
`d_H(b)<=3` for all `b in B`, every `H`-scheme yields an `H` minor
containing each prescribed `A` root in its named branch set.

The auditor read the full promoted source independently of its author,
checked the supplied proof against the actual hypotheses of its inputs,
and checked root preservation and the induction parameter separately.

## Root relocation

Lemma 1 explicitly requires the new root `x` to lie on all paths incident
with `b` and on no other path. Consequently unchanged paths avoid the
new root, and each truncated path has it only as an endpoint. Its suffix
avoids the old root because the original path is simple. Every other
prescribed root retains its original image. All intersections of retained
paths are inherited, so their target edges still have a common endpoint.
Deleting the old root therefore gives precisely the claimed new scheme.
The abstract target remains fixed; the argument does not preserve `b`.

## Actual-membership packing

The input is Lemma 2.1 of
[even_subdivision_contractibility.md](even_subdivision_contractibility.md),
at whole-file SHA256
`e7e8499d03f440f81bf558f7d42bc6be09830dd68a4bba50b92e1df4e1332ef7`.
Its audited component-incidence inequality and matroid-union argument
apply to these projections without any additional target-degree assumption.

Each label is an actual nonroot vertex. A label on two paths of colour
`b` occurs in two distinct `A` projections: simplicity of `H` supplies
distinct opposite endpoints. Within one projection each label occurs
once, the projected paths partition its edges and share its root, and
each other projected vertex lies on at least two paths. They cover the
colour class. Parallel auxiliary edges and trivial paths are permitted.
Thus every hypothesis of the packing lemma is satisfied. Its disjoint
tree labels lift to disjoint connected branch sets; the final edge of
each original scheme path supplies the required root adjacency.

## Induction and preservation

Kündgen--Pelsmajer--Ramamurthi, Lemma 3.3, produces a root-preserving
minor `K` with `|V(K)|<=|V(G)|`; its coloured-scheme properties are those
in Definition 3.1 and Remark 3.2. A fully supported vertex of `B` colour
cannot occur on a nonincident path, so Lemma 1 applies. The recursive
host has order `|V(K)|-1<|V(G)|`, with every `A` root unchanged.
Strong induction on host order is therefore sufficient even when the
normalization itself leaves the order unchanged.

If no relocation applies, a `B` nonroot has at least two memberships,
cannot have a degree-one colour, and cannot exhaust a degree-two or
degree-three colour. Hence it has exactly two memberships, exhausting
all cases and invoking Lemma 2. Composing the model with the minor map
of `K` preserves all original `A` roots. Isolated target roots are removed
before normalization and restored as unused singleton branches; edgeless
targets are immediate. No counting bound or finite enumeration is used.

**Unresolved assumptions or gaps:** none in the stated theorem beyond
the explicitly cited KPR reduction and audited packing input. Publication
priority and comparison with the reach of Norin--Totschnig are unresolved.
Biswal--Lee--Rao's flow lemma is not an input. This audit establishes no
containment of the original `B` roots, full rooted contractibility of
`K_{3,3}`, universal bipartite contractibility, T44, Conjecture 21, or `HC_7`.
