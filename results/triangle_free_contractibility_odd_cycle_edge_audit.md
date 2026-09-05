# Audit: one edge meeting every odd cycle

**Status:** separate internal mathematical audit, 5 September 2026.
This is an internal agent audit, not external peer review.

**Audited source:** [the written theorem](triangle_free_contractibility_odd_cycle_edge.md),
whole-file SHA256
`21bd3accaf4bc2df5483a05712c851aa0482e5c1be2508d3e450b3950e183eb6`.

**Verdict: GREEN** for Lemma 3 and Theorems 1, 2 and 4, including
the componentwise conclusion and the cycle-space equivalences. No unresolved
mathematical gap was found under their explicit hypotheses. These are necessary structural
conditions; the audit does not establish the converse or a classification
of contractible graphs.

## Revision and independent review

The initial separate agent audit checked Lemma 3 and Theorems 1--2 at
SHA256 `39b35a2b94c5cc6de6ba12f0a8174111f9aa55f2b62fd059d666fcc102538efb`,
committed in `d3bf131`. That mathematical text is unchanged in this
revision; its audit reasoning is preserved below. The added Theorem 4
was written by the literature agent and independently reviewed by the
parent agent. The parent checked the primary cycle-basis statement,
the coordinate lift and the series-class argument, and verified the
unchanged earlier proof against that commit. This is a separate internal
review of the new inference, not a new claim of external review.

## Added Theorem 4: cycle spaces and series classes

Benchetrit--Sebő [Theorem 2.2](https://arxiv.org/pdf/1509.05586)
was checked in the primary paper. Its hypotheses are 2-connectivity
and nonbipartiteness; its totally odd circuit basis consists of odd
cycles having pairwise odd edge intersections. Bilinearity gives
`x.y=p(x)p(y)` for every pair of cycle-space vectors. Since `H-e` is
connected and bipartite, the ends of `e` lie in the same shore. Hence
every cycle through `e` is odd and every cycle avoiding it is even,
so `p(x)=x_e` also holds for arbitrary cycle vectors by linearity.

Contraction is checked at the level actually claimed. Deleting the
coordinate of `e` bijects the two cycle spaces: an even-degree edge set
after contraction lifts with equal degree parities at `u,v`, and adding
`e` precisely when both are odd supplies its unique even-degree lift.
Edge identities are retained; parallel edges are not simplified away.
Thus `x'.y'=x.y+x_e y_e`. This proves both directions of the stated
self-orthogonality equivalence, using the exact Lemma 2.3 for the reverse
skewed-theta exclusion. It also proves bipartiteness of the quotient by
applying the identity to one cycle twice. The two cycles in an all-odd
theta would have odd intersection, so that exclusion follows as well.

The strongest new combinatorial step is the series-class criterion.
For an edge `f=ab` of a connected bridgeless loopless multigraph, every
bridge of `F-f` separates `a,b`; otherwise it would still be a bridge
in `F`. Conversely, an edge used by every `a,b` path is such a bridge.
Every cycle containing that bridge must use `f`, which verifies both
directions of the series relation. The bridge blocks form a chain.
Inside each block two edge-disjoint paths join its entry and exit,
or both paths are empty if those vertices coincide. The resulting two
simple `a,b` paths intersect in exactly the bridges, so adding `f`
gives two cycles whose common edges are exactly its series class.
This proves necessity of even class size. Sufficiency follows because
every cycle, and therefore every cycle intersection, is a union of
whole series classes. Coordinate identities between remaining edges
are preserved by the cycle-space bijection; no additional series
classes merge after contracting `e`. This establishes the precise
single-odd-class conclusion, including when the class of `e` was a
singleton and disappears in the quotient.

No unresolved gap was found in Theorem 4. These operations concern the
target cycle space only. They do not preserve the two original scheme
roots separately or split an arbitrary quotient branch set, and the
theorem expressly does not claim that missing rooted-scheme lift. No
finite enumeration is a premise of the equivalences.

## Exact signed-graph input

The auditor independently read the signed-minor definitions, statement
1.1 and the beginning of its proof in Section 3 of
[Geelen--Guenin's primary paper](https://www.math.uwaterloo.ca/~jfgeelen/Publications/even.pdf).
Their signed minors allow switching and contraction of an edge set
with no odd circuit. Isomorphism preserves circuit parities, so it is
understood up to switching. Statement 1.1 characterizes packing for
every nonnegative integral capacity vector by absence of a signed
odd-`K_4` minor. Taking every capacity equal to one gives equality
between minimum odd-circuit edge cover and maximum edge-disjoint
odd-circuit packing. This statement has no Eulerian hypothesis; the
later odd-`K_5` result does not replace it in this application.

For the all-one signature on an ordinary graph, signed odd circuits
are precisely its ordinary odd cycles. Hence the cited packing and
covering quantities are exactly those used in Theorem 1. The proof
does not infer signed-minor exclusion merely from unit-capacity packing.

## Strongest inference: a parity-correct subdivision lift

A certificate for the signed odd-`K_4` minor supplies four disjoint
connected branch sets and one retained edge for each of their six
pairs. The contracted edge set has no signed odd circuit, so switching
can make all its edges even. The retained signature is equivalent to
the all-one signature on `K_4`. A further switch constant on each
branch set makes all six chosen joining edges odd while leaving each
branch tree even. These switches combine into one vertex potential
function on the original graph.

The three selected attachment vertices in a branch tree have a median.
The paths from that median to the attachments intersect only at the
median, even if two or all three attachments coincide. Joining these
arms through the six selected interbranch edges gives six paths with
disjoint interiors. Distinct branch sets supply distinct medians.
Every path has positive length because it uses an interbranch edge.
Thus this is an actual subdivision in the original graph, with no
vertex shared by two unintended paths.

Each path has switched sign sum one. Undoing the switch changes its
parity only at its two endpoints, giving the exact relation

```text
p_ij = 1 + s_i + s_j  (mod 2).
```

If the four endpoint potentials agree, all six replacement paths are
odd. Otherwise choose two different potentials. Their direct path is
even, and the routes through the two other branch vertices are both
odd. The subdivision's disjoint interiors make these three routes
internally disjoint. This proves the claimed skewed theta alternative.
No arbitrary minor-to-subdivision conversion has been invoked without
checking its degree-three attachments and parity.

This extraction does not claim to preserve roots of an unrelated
scheme. It uses a finite signed-minor certificate, with no induction
or well-founded reduction obligation. In particular it does not
reintroduce the branch-set ownership gap of an arbitrary split-and-lift
argument for schemes.

## From packing to a common edge

The primary [Benchetrit--Sebő Lemma 2.3](https://arxiv.org/pdf/1509.05586)
was checked: for a two-connected graph, a skewed theta exists exactly
when two odd circuits have an even number of common edges. In the
absence of a skewed theta, edge-disjoint odd cycles are therefore
impossible. Nonbipartiteness ensures at least one odd cycle, so the
packing number is exactly one. Lemma 3 excludes the forbidden signed
minor, allowing the verified packing theorem to give an odd-cycle
edge cover of size one. Deleting that edge leaves a bipartite graph.
All hypotheses of both external results are explicitly present in
Theorem 1.

## Contractibility and the passage through blocks

Theorem 2 uses rooted subgraph heredity, the triangle-free skewed-theta
obstruction, and the two-long-odd-cycles obstruction from
[Kündgen--Pelsmajer--Ramamurthi](https://arxiv.org/pdf/1207.6141),
respectively Lemma 2.2, Theorem 7.10 and Corollary 7.8. These exact
primary statements were checked. The paper counts internal vertices
in its theta notation; converting to edge lengths gives the parity
pattern in the source. Corollary 7.8 applies to a connected graph
containing two odd cycles of length at least five meeting in at most
one vertex, exactly as used here.

The additional input is the
[audited odd-subdivision obstruction](../barriers/triangle_free_odd_subdivision_contractibility.md),
whole-file SHA256
`2fbd3199943469303fbac7ca820312bed8188a98d2429290e4ab34762061bc03`.
Its Corollary 4 excludes every triangle-free totally odd subdivision
of `K_4`. Any such subdivision in the present target is triangle-free
because the whole target is. Heredity therefore rules out both
subgraph alternatives of Lemma 3 in every nonbipartite two-connected
subgraph of the target.

Odd cycles from distinct blocks meet in at most one vertex, and
triangle-freeness makes their lengths at least five. The verified
external obstruction therefore permits at most one nonbipartite block
in a connected contractible target. If it exists, that block is
two-connected and satisfies Theorem 1. Its common odd-cycle edge
meets every odd cycle of the whole target, since every cycle lies
in a block and all the other blocks are bipartite. This validates
the extension from Theorem 1 to connected targets and then to each
connected component.

No finite computation is a premise of these deductions. The example
with theta-path lengths `2,3,3` correctly demonstrates that the
necessary common-edge condition alone is insufficient: its two odd
cycles share the even path, while the external theta theorem excludes
contractibility. Full classification, arbitrary rooted scheme allocation
in the remaining class, Hadwiger's conjecture, novelty and significance
comparable to Norin--Totschnig remain outside this verdict.
