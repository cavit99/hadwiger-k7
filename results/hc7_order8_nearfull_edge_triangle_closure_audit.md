# Internal audit: order-eight near-full edge-component closure

**Verdict:** **GREEN** for the exact written and computer-assisted result at
the revisions below.  This was a separate cold mathematical audit and a
separate implementation/certificate audit, not external peer review.

## Exact revisions audited

```text
9fa601e3e8a1d29dc9de239029809379e92b9187750034d590ea4989dad48667  results/hc7_order8_nearfull_edge_triangle_closure.md
5805b098e305fd1c2b74f7913bed4a235ea21becc3679f12d2d5ca96b2355caf  results/hc7_order8_rooted_oct_triangle_certificate.py
05d6c41ff9331b427c2f4c69f56b6bd1705451877a8415f0838dba4f59f66b7f  results/hc7_order8_rooted_oct_triangle_check.py
```

Any mathematical change to the theorem or any change to the finite
universe, witness construction, expected counts, certificate format or
digest requires renewed audit.

## 1. Written reductions

### Rooted odd-cycle transversal

For distinct marks `r,s`, adding `rs` encodes exactly the requirement that
surviving marks lie on opposite sides of the bipartition.  If one or both
marks are deleted, the added edge disappears from the remaining graph and
the surviving marked component may be reversed independently.  Lemma 2.1
therefore handles all deletion cases and proves both implications.

### Contraction obstruction

The sets `{v} union P` and `{a} union Q` are disjoint and connected, and at
least one is nontrivially contracted because `|S|>=3` and `|Z|<=2`.  The
edge `va` keeps the two contraction images distinct and forces different
colours.  Expanding only over the boundary sets `P,Q` gives a proper
colouring of the opposite closed shore: independence handles edges inside
each set, and every other relevant edge is represented at a contraction
image.  The boundary uses at most four colours, so two unused colours extend
over the intact edge `va`.  This is a valid contradiction to
minor-criticality.

### Explicit `K_7`-minor model

For a triangle `t_1t_2t_3` avoiding the two misses, the seven displayed
branch sets

```text
{v}, {a}, C_1 union {x}, C_2 union {y}, {t_1}, {t_2}, {t_3}
```

are disjoint and connected.  Component fullness supplies their contacts
with all triangle vertices, connects each absorbed anchor, and supplies an
edge between the two enlarged component bags.  The five selected boundary
vertices avoid both endpoint misses, and `va` supplies the final endpoint
adjacency.  All 21 pairwise adjacencies are therefore present.

### Aligned-host integration

In the aligned degree-eight setting, `G-S` contains the two exterior
components and the singleton `{u}`.  If one exterior component is the
two-vertex edge, the opposite component and `{u}` give the two additional
`S`-full branch sets required by the construction.

The low-degree neighbourhood bound gives `alpha(G[S])<=3`.  If
`Z={z_1,z_2}` and `G[S]-Z` had a `K_4` model, then that model together with

```text
{u}, E union {z_1}, F union {z_2}
```

would be a `K_7` model.  Thus the compact boundary hypotheses used by the
finite lemma follow literally.  Seven-connectivity also bounds each
endpoint defect of a two-vertex exterior component by two; the theorem
correctly claims only the profiles with both defects at most one.

## 2. Finite certificate

Using nauty's complete order-eight catalogue, both programs return

```text
graphs 12346
eligible_graphs 185
marked_profiles 13505
oct_witnesses 13247 by_miss_count=[185, 2960, 10102]
triangle_witnesses 258 by_miss_count=[0, 0, 258]
records_sha256 c7a4323ec9f23faa1499d8891c33eced2f11ca7270db98bb44dcc8832bb0520d
PASS
```

The generator retains exactly the graphs with independence number at most
three and no `K_4` minor after any two-vertex deletion.  It covers every
full/full, one-miss and ordered distinct-two-miss endpoint profile.  For
each profile it records either a deletion set of order at most two making
the appropriately edge-augmented graph bipartite, or a triangle avoiding
both actual misses.

The checker imports no generator code.  It separately decodes graph6 into
edge sets, recognizes a `K_4` minor directly from four disjoint connected
pairwise adjacent branch sets, reconstructs every eligible marked profile,
and validates every OCT and triangle witness.  For every triangle record it
also exhausts all 37 deletion sets and confirms that no OCT of order at
most two exists.  Its exact `K_4` decisions agree with the generator's
degree-two suppression algorithm on all `345,688` graph/two-deletion
instances.  Duplicate, missing, unexpected or noncanonical records are
rejected, and both programs fail closed under optimized Python.

Catalogue completeness is delegated to nauty's `geng`; the two programs
are independent at graph decoding, `K_4` recognition and witness
validation, not at the external catalogue source.

## 3. Scope and unresolved cases

The result closes the aligned three-component two-vertex exterior case
when each endpoint misses at most one boundary vertex.  It includes the
full/full, one-miss and distinct-one-miss profiles and does not require
colouring-operation provenance.

It does not prove that an aligned exterior component has order two.  For a
two-vertex component it leaves the cases in which at least one endpoint has
defect two.  It does not close the minimum-boundary interface with exactly
two full components, other small shores, or the general bounded-interface
composition theorem.  It does not prove `HC_7`.
