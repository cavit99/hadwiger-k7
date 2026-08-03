# Hadwiger `K_7` research ledger

**Last updated:** 3 August 2026
**Authoritative status:** `HC_7` is not proved here.  Neither is the
`K_7^-` six-colour conjecture.  Internal audits are not external peer
review.

The previous live ledger is preserved at
[`archive/RESEARCH_LEDGER_2026-08-02.md`](archive/RESEARCH_LEDGER_2026-08-02.md).
This file is the sole authority for the present research frontier.

## Current frontier

### 1. Exhaustive global obligation

The sole active research target is the following unconditional extremal
theorem.

> **`4n-2` extremal target.** Every seven-connected graph `G` with
> \[
> |E(G)|\ge4|V(G)|-2
> \]
> contains a `K_7^-` minor.

This statement is open.  It is exactly sufficient for Norin--Totschnig
Conjecture 21: the audited computation-free critical-host chain proves that
any minor-minimal non-six-colourable `K_7^-`-minor-free graph is
seven-connected and meets this density threshold.  Proving the target would
settle that conjecture, but would not prove `HC_7`.

The global six-edge difference from Norin and Totschnig's `4n-8` threshold
does not identify six edges near a chosen deficient branch set.  Surplus
localisation is therefore not being treated as a proved mechanism.

### 2. Principal conditional refinement: a smallest extremal enemy

Assume the target false, choose a counterexample `G` first with minimum
order and then with minimum size, and put

\[
q(G)=|E(G)|-(4|V(G)|-2).
\]

Jakobsen's audited extremal input rules out `|V(G)|<=20`: at those orders the
`4n-2` threshold reaches `9n/2-12`, while seven-connectivity excludes all
cockade exceptions.  Thus any enemy has at least 21 vertices; the only
possible first rows are `(n,m)=(21,82),(22,86)` and, at order 23,
`m\in\{90,91\}`.

A recorded, separately checked preliminary falsification screen found no
enemy among complete multipartite graphs, ordinary clique sums, the standard
cockades, or universal planar apex joins.  This is not an exhaustive or
separately promoted theorem.

The following computation-free reductions have written proofs and separate
GREEN internal audits.

- Every order-seven cut in a seven-connected `K_7^-`-minor-free graph has
  at most three complementary components.  With three components its
  boundary graph is subcubic.
- The minimum enemy has a degree-seven vertex `v`.  Some edge `vs` satisfies
  \[
  |N(v)\cap N(s)|\le3,
  \qquad q(G/vs)\ge q(G).
  \]
  The contraction cannot remain seven-connected.  Its failure pulls back
  to an exact order-seven cut containing `v,s`, with at most three
  complementary components.
- If `G-N[v]` has two components, every incident contraction is
  density-preserving.  Yuan's fragment theorem then yields a connected
  fragment with a single surviving root and two nested exact seven-cuts.
  This is the precise root-swap residue; it is not a closure.
- If `q(G)>0`, then `G` is minimally seven-connected.  More than half its
  vertices have degree seven.  If `L` is the set of degree-seven vertices
  and `F=G-L`, then `F` is a forest and
  \[
  3(|L|-|F|)=c(F)+|E(G[L])|+q(G)-2,
  \qquad |L|\ge|F|+2.
  \]
  At least `ceil(|L|/2)` distinct density-preserving noncontractible edges
  cover `L`, each lying in an exact order-seven cut.  They include either
  a safe edge inside `L` or a safe two-edge star with two leaves in `L`.
- More generally, deleting any essential edge of an edge-minimal
  seven-connected target-free graph gives a six-connected graph with an
  exact six-separation into two boundary-full shores.  The deleted edge is
  the sole cross-edge.  The boundary is `K_5^-`-minor-free, every closed
  shore is internally rooted-connected, and the shore contraction surplus
  is known exactly.

These results replace the informal instruction to “place six surplus
edges”.  A smallest enemy is now forced into a large, operation-free family
of exact six- and seven-separations with exact density accounting.

### 3. Immediate structural laboratory

Two bounded attacks now meet at the same rooted obstruction.

The direct positive-surplus attack uses Mader's generalised atoms.  It
reduces every nonsingleton atom to an edge, a three-vertex path, or a
triangle behind an exact seven-cut; one complete four-distinct-miss path
case is eliminated by a separately checked finite boundary lemma.  This
does not reach the exact-surplus layer.

The auxiliary five-connected statement

\[
 \kappa(G)\ge5,\qquad |E(G)|\ge4|V(G)|-7
 \quad\Longrightarrow\quad K_7^-\preccurlyeq G
\]

would imply the primary target.  A minimum auxiliary enemy is now proved
to have exact density `4n-7`, connectivity exactly five, and an actual
five-cut with two or three boundary-full components.  Dense, four-component,
all seven-edge, sparse three-component, and several complete two-component
families are eliminated.  This is a substantial reduction, not a proof of
the auxiliary statement.

The next exact theorem is a five-root reserve-or-descent lemma: a dense,
internally five-connected lobe with five prescribed boundary roots must
contain a `K_6` model with five distinct root bags and a root-free sixth
bag, or return a strictly smaller five-cut component which retains the
required high excess.  The full chain and exact surviving rows are in the
[auxiliary technical frontier](active/hc7_k7minus_e5_frontier.md).

An accepted result must prove at least one of:

1. one density-preserving degree-seven edge is seven-contractible;
2. the exact seven-cuts covering the degree-seven vertices uncross to an
   explicit `K_7^-` model; or
3. one shore of an essential-edge six-separation contracts to a smaller
   seven-connected graph still at the `4n-2` threshold; or
4. the five-root reserve-or-descent target holds.

The four exact nonclosures to overcome are:

- **root swap:** a trace-one fragment can support nested exact seven-cuts
  without being a singleton;
- **missing seventh bag:** four rooted bags in one shore of an essential-edge
  six-separation, the opposite shore, and one boundary singleton give only
  six branch sets.  The remaining boundary vertex is not automatically a
  valid seventh bag.
- **safe-star uncrossing:** the positive-surplus count forces a safe edge
  inside the degree-seven set or a safe two-edge star, but their exact
  seven-cut certificates may coincide or nest without a smaller safe shore.
- **rooted reserve:** ordinary two--three linkage is sharp at lobe excess
  one, while an unrooted `K_6` model may consume every useful residual
  vertex.  A smaller arbitrary side is not enough unless it retains the
  high-excess inequality.

Kawarabayashi's contractible-edge theorem for odd connectivity and
`K_4^-`-free graphs supplies a relevant proof architecture, but its
triangle-free safe edge is what forces large shores in the uncrossing.
Here a density-safe edge may have three common neighbours, so a singleton
or root-only shore survives.  Replacing that lost shore-size bound is the
current uncrossing problem.  Another boundary census, isolated graph-code
elimination, or noncritical static barrier is not an accepted principal
outcome.

## Established context retained from the previous programme

The audited computation-free critical-host package remains valid:

\[
n_7\le4,
\qquad |E(G)|\ge4|V(G)|-2,
\qquad b\ge17+\sum_{i\ge10}(i-9)n_i,
\]

where `b` counts degree-eight vertices contained in no literal `K_5`.
If `n_7=4`, then `|V(G)|>=37` and the stronger exceptional-vertex bound is
`b>=32+tau`.  These are necessary conditions on a hypothetical
counterexample, not a colouring theorem.

Every order-seven cut in that critical host has exactly two complementary
components.  The earlier capacity theorem restricts a possible
three-component boundary to colour classes of sizes `3,2,2`, and the
audited
[three-shore planar-extension theorem](results/hc7_k7minus_three_component_seven_cut_exclusion.md)
six-colours that configuration.

The exceptional-centre and bounded-interface programmes remain available as
conditional refinements and sources of techniques.  They are frozen as
principal search directions while the unconditional `4n-2` target is
attacked.  Direct `HC_7` bridge composition is also frozen: Conjecture 21
is the cleaner setting in which to develop the same missing branch-set
transfer and separator-resolution machinery.

The concise computation-free manuscript in [`paper/k7minus-low-degree/`](paper/k7minus-low-degree/)
is preserved but is not the active task.  Its proofs still require normal
specialist validation before publication.

## Trust boundary

- The direct-extremal and auxiliary reductions are written results with
  adjacent hash-pinned GREEN internal audits.  The saturated degree-seven
  quotient and the four-distinct-miss path theorem have explicit finite
  computational trust boundaries; the remaining new reductions are
  computation-free.
- External inputs include Mader, Halin, Jakobsen, Jørgensen, Yuan and
  Schmidt; exact statements and citations are recorded beside the results
  that use them.
- No robust `K_6`-model transversal theorem or two-root dominating-model
  augmentation theorem is claimed.  Both bounded attacks have been frozen
  as principal mechanisms.  The first loses common labels and connectivity
  after deleting its transversal; the second requires a rooted
  cycle-touching model whose failure is not known to give a six-cut.

## Navigation

- [`active/INDEX.md`](active/INDEX.md): concise live navigation.
- [`active/hc7_k7minus_density_frontier.md`](active/hc7_k7minus_density_frontier.md):
  exact technical frontier and recorded nonclosures.
- [`active/hc7_k7minus_e5_frontier.md`](active/hc7_k7minus_e5_frontier.md):
  auxiliary five-connected reduction and five-root reserve target.
- [`results/hc7_k7minus_seven_cut_three_component_bound.md`](results/hc7_k7minus_seven_cut_three_component_bound.md):
  at most three components behind a seven-cut.
- [`results/hc7_k7minus_degree7_safe_contraction.md`](results/hc7_k7minus_degree7_safe_contraction.md):
  density-preserving degree-seven contraction and root-swap residue.
- [`results/hc7_k7minus_strict_surplus_minimal_enemy.md`](results/hc7_k7minus_strict_surplus_minimal_enemy.md):
  Mader--Schmidt structure at positive surplus.
- [`results/hc7_k7minus_essential_edge_six_separation.md`](results/hc7_k7minus_essential_edge_six_separation.md):
  essential-edge separation and shore accounting.
- [`archive/`](archive/): superseded proof spines and the previous ledger.
