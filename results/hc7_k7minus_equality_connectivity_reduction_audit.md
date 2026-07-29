# Internal audit: equality connectivity and overlap reduction

Audited file:
`results/hc7_k7minus_equality_connectivity_reduction.md`.

Audited SHA-256:

```text
451fd13b2fbd688cafb6f8005aefab92cc90eb7a1b92614ca10bdb7bdc9cc128
```

**Verdict:** **GREEN** for the exact revision above.

This is a separate internal mathematical audit, not external peer review.
Two cold reviews checked the connectivity and order-bound revision,
including the order-eighteen block--cut-tree lemma and all four matching
cases.  A further cold review checked the edge-critical Kempe fork.

## 1. Scope and dependencies

The theorem assumes the full critical-host hypotheses, exclusion of a
`K_7^-` minor, and equality `|E(G)|=4|V(G)|-5`.  Its structural input is the
audited density and low-degree rigidity theorem at SHA-256

```text
604d11d4276ce6a3c57a8375d702624a1c364b5123f122b7e9e3dc18d11bf8f4
```

and supplies exactly ten degree-seven vertices, two disjoint literal `K_5`s
covering them, degree eight elsewhere, and the five pairwise disjoint
private external triangles on each side.  The present proof was rechecked
against that revision.  Its local structure now descends from the audited
computation-free degree-seven neighbourhood theorem; no finite
classification is load-bearing and no unbounded theorem is inferred from
enumeration.

## 2. Equality bookkeeping and connectivity

The cross-edges between the two `K_5`s form a matching.  For a matched pair,
the two vertices remaining in its private triangle are exactly the common
two-vertex port on both sides.  Summing the two clique-incidence indicators
over the central graph `R` verifies

\[
 |E(R)|=4|V(R)|-15+k
\]

and the displayed degree sequence of either clique-deletion graph.

For a component after deleting at most four vertices from `G-A`,
seven-connectivity forces at least `7-|Z|` private-triangle labels.  The
label sets of different components are disjoint because every surviving
part of a private triangle is a clique.  The resulting count proves that
`G-A` and `G-B` are five-connected.  Repeating the argument inside `G-A`
with the five `B`-labels proves that `R` is three-connected.

## 3. Explicit minor model and overlap repair

The five singleton branch sets in `A`, together with `B` and `R`, show that
four cross-edges already give a `K_7^-` model; hence `k\le3`.

The overlap-repair proof correctly retains the original selected set `Z`.
With

\[
 X=R-Z,\qquad Y=B\cup Z,
\]

both branch sets are connected.  Every `A`-vertex remains adjacent to `X`,
while `Y` is adjacent to the `k` matched `A`-vertices and the distinct
owners represented by `Z`.  Thus at most one required `A`--`Y` adjacency is
missing.  Finally, `|Z|\le5-k<15-k=|\bigcup Q_b|`, so an edge from `B` to
`R-Z` remains.  These seven branch sets are therefore an explicit
`K_7^-`-minor model.

This check is important: replacing `Z` by an arbitrary smaller subset would
not preserve connectivity of `R-Z`.  The audited revision makes no such
monotonicity assumption.

## 4. Nonseparating selections and the order bound

In both parts of the small-selection lemma, the three chosen lobes are
genuinely pairwise disjoint.  Minimum degree six gives lobe sizes at least
four in the first part and at least three in the second.  At order eighteen,
two order-four lobes in the first part saturate both deleted vertices to
degree eight, while three-connectivity forces an additional neighbour.  In
the second part, the new lobe-size patterns `3,4,5` and `4,4,4` send at
least twenty-two and twenty-four edges, respectively, into three vertices
whose degree sum is eighteen.

The cutvertex bound in Lemma 5(3) was checked separately.  After deleting
two degree-six vertices, the remaining graph has at least forty-six edges.
Every leaf-block interior has order at least four.  Three leaf blocks give
an immediate edge-count contradiction; with two, the block--cut tree is a
path.  The exact block-edge maxima for four through eight cutvertices are
`46,42,36,31,27`.  Equality in the first case forces a `K_8` end block
followed by a bridge, giving its cutvertex degree at least eight.  Thus the
remaining graph has at most three cutvertices.

The subsequent inclusion--exclusion and case analysis are exact.  The
extended selection lemma excludes central order eighteen for `k=0`; the
explicit two-vertex branch-set repair excludes it for `k=3`; and the earlier
overlap count gives central order at least nineteen for `k=2`.  For `k=1`,
central order eighteen first forces eight off-matching common neighbours,
two in each unmatched private triangle, and degree sequence `6^{10}7^8`.
Fixing common neighbours in two triangles would make all four common
neighbours in the other two triangles cutvertices after the fixed pair is
deleted, contradicting Lemma 5(3).  Hence every matching case has central
order at least nineteen.  Since `G` also contains the ten clique vertices,
the equality layer satisfies

\[
                         |V(G)|\ge29.
\]

## 5. Cycle, bond, and colouring formulations

The union of the five private triangles has independence number at most
five.  Fournier's cyclability theorem, in the form already checked in the
reserved-cycle audit, therefore applies to the five-connected graph `G-A`
and yields one cycle through all fifteen vertices.

The two connected transversals are equivalent to a vertex bipartition with
both sides connected and every private triangle split between the sides;
this is exactly a bond meeting every private-triangle edge set.  The
six-colouring dichotomy is the complete Hall obstruction for the five
three-element lists of colours available to the vertices of `A`: either
four complementary triangle colour sets coincide, or at least two colours
occur on all five triangles.

## 6. Edge-critical Kempe fork

Deleting an edge `a_ix` from a clique vertex to its private triangle and
six-colouring the result must give the same colour `p` to its endpoints.
The unique colour `q` absent from the clique must occur on the private
triangle: otherwise recolouring `a_i` with `q` colours the restored edge.
This verifies the palette decomposition used in Proposition 9.

The list assignments in parts 1 and 3 were checked colour by colour.  If
either `p` or `q` is absent from one of the three indexed triangles, moving
its owner's original colour to `a_i` and using that absent colour at the
owner gives five distinct permissible clique colours.  In the non-universal
case, the analogous assignment at the remaining clique vertex forces all
four specified triangles to have palette `\{p,q,r\}`.

For part 2, if the `p,c_j` component rooted at `x` misses `T_{a_j}`, its
Kempe interchange removes `p` from `T_{a_i}` without changing
`T_{a_j}`.  The original colour at every other clique vertex is either
`c_j` on the unchanged triangle or lies outside `\{p,c_j\}`; hence the
displayed recolouring really extends over the restored edge.  In the rigid
branch, interchanging a different `p,c_j` component similarly makes `p`
available at its triangle owner while leaving `x` fixed.  This proves that
each of the three rooted components contains the `p`-coloured vertex of all
four specified triangles.

## 7. Trust boundary

No unresolved assumption remains in the stated theorem.  The result does
not prove the bond or two-transversal target, close the equality layer,
handle positive density surplus, prove the `K_7^-` six-colour conjecture, or
prove `HC_7`.  The terminal-spanning cycle is explicitly not promoted to a
transversal theorem; the recorded ring of five triangles is a valid
two-connected barrier to that inference.  The three Kempe components in
the rigid branch all contain the same four triangle vertices; the audit
does not infer two disjoint connected transversals from these overlapping
components.
