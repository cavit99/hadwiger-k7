# Audit: one edge meeting every odd cycle

**Status:** separate internal mathematical audit, 5 September 2026.
This is an internal agent audit, not external peer review.

**Audited source:** [the written theorem](triangle_free_contractibility_odd_cycle_edge.md),
whole-file SHA256
`39b35a2b94c5cc6de6ba12f0a8174111f9aa55f2b62fd059d666fcc102538efb`.

**Verdict: GREEN** for Lemma 3, Theorem 1 and Theorem 2, including
the componentwise conclusion. No unresolved mathematical gap was
found under their explicit hypotheses. These are necessary structural
conditions; the audit does not establish the converse or a classification
of contractible graphs.

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
