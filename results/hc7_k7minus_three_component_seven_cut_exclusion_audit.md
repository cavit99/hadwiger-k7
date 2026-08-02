# Internal audit: three-component `3,2,2` seven-cut exclusion

Audited file:
`results/hc7_k7minus_three_component_seven_cut_exclusion.md`.

Audited SHA-256:

```text
1041988a33b749bef5802dd21d3cd9419b5afc754735a20174bf5a13c0a56c96
```

**Verdict:** **GREEN** for the exact revision above.

This is a separate internal mathematical audit, not external peer review.
The proof and its transfer to the current `K_7^-` host were independently
reconstructed in a cold agent audit before extraction from the archive.
The present audit checks the exact extracted statement, proof, citations,
and corollary.

## 1. Hypotheses and the capable-shore reflection

Seven-connectivity and the existence of three components imply
`N_G(D_i)=S` for every `i`.  Hence each component is connected and full at
the literal boundary.

A shortest path between two disjoint connected realisers can be divided at
one edge and absorbed into them.  This makes them adjacent without losing
disjointness or any prescribed boundary contact.

If two components realise the two two-vertex blocks, then, for each retained
component, the three sets in display (2) are connected, disjoint, and
pairwise adjacent.  Contracting them is a proper minor operation.  Every
edge from a contracted boundary block to the retained component remains
represented at the contracted image, so the pullback is a proper colouring
of the whole closed shore.  The three contracted images form a clique and
therefore receive distinct colours.  The returned boundary equality
partition is exactly `T|A|B`, not a coarsening.  Palette permutations align
these labelled blocks on the three closed shores, which then glue because
their open components are anticomplete.

Thus at least two components are genuine two-linkage obstructions.

## 2. Crossless auxiliary graph and the bare web

For one obstructing component, a crossing of the ordered artificial
terminals gives disjoint paths for the pairs `(a_1^*,a_2^*)` and
`(b_1^*,b_2^*)`.  Removing their artificial ends leaves disjoint connected
subgraphs with the required literal root contacts.  Conversely that is the
only implication needed.

Adding an edge between consecutive frame terminals cannot create the
prescribed crossing: any crossing path using that edge would meet an
endpoint of the other prescribed path.  Hence the frame cycle may be added
before taking a same-vertex edge-maximal crossless completion.

Humeau and Pous, *On the Two Paths Theorem and the Two Disjoint Paths
Problem*, [arXiv:2505.16431v2, Theorem 1.3](https://arxiv.org/abs/2505.16431),
state that a graph with a cycle `C` is a web with frame `C` exactly when it
is maximally `C`-crossless.  This is the required same-vertex completion
statement.

In a web, a clique inserted behind a facial triangle has no neighbours
outside that clique and the three facial vertices.  If it contained any
original shore vertex, replacing artificial facial terminals by their
literal roots and adding the three omitted roots in `T` would give an
actual separator of order at most six.  Another nonempty component lies on
the other side, contradicting seven-connectivity.  Therefore every
original shore vertex belongs to the planar rib.

Replacing the four artificial terminals by their distinct literal roots
preserves planarity.  The two roots in each colour block are nonadjacent,
so adding all four cross-block edges produces an induced frame `C_4`.
These completion edges are auxiliary and are never used as edges in a
minor model of `G`.

## 3. Proper-minor colouring and planar extension

Both sets `Q_0=D_1\cup T` and `Q_1=D_2\cup A` are connected.  They are
disjoint and adjacent, and each sees both retained `B` vertices.  Their
contraction is proper and a six-colouring pulls back on `G[D_3\cup S]` so
that:

- `T` has one colour `0`;
- `A` has a distinct colour `1`;
- both vertices of `B` avoid `0` and `1`.

On each auxiliary induced `C_4`, the resulting precolouring is proper and
uses at most three colours from the five-colour palette excluding `0`.
Diwan, *Colouring planar graphs with a precoloured induced cycle*,
[arXiv:2306.04944, Corollary 1](https://arxiv.org/abs/2306.04944), applies
with `k=5`: the cycle length `4` is at most `2k-5=5`, and at most
`3<k` colours occur.  Each planar shore therefore has a five-colour
extension which preserves the boundary precolouring and avoids `0`.

The two extensions agree with the retained closed-shore colouring on
`A\cup B`; avoiding `0` makes every edge to `T` proper.  All other relevant
edges were already coloured on one piece, and different components of
`G-S` are anticomplete.  The claimed global six-colouring follows.

## 4. Current-host transfer and dependency integrity

The imported current result is
`results/hc7_k7minus_critical_seven_cut_capacity.md`, audited at SHA-256

```text
d4d650fee168fc2ff0e00a3b7b0faed6ff674ba8cd3c06c263f63c4170656f34
```

Its Theorem 3 proves that an order-seven cut in the current critical host
has two or three components.  If it has three, the boundary has a proper
three-colouring and every such colouring has class sizes `3,2,2`.
Theorem 1 excludes exactly that alternative.  The packing and boundary-edge
statements in Corollary 2 are copied from the surviving two-component case
of the imported theorem.

No computation or finite classification enters the new theorem.  It
eliminates the critical three-component order-seven-cut branch, but it does
not eliminate two-component cuts, prove the bare extremal theorem, settle
Norin--Totschnig Conjecture 21, or settle `HC_7`.
