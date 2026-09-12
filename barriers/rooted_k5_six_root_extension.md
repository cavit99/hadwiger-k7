# A rooted K5 need not extend to six rooted almost-clique bags

**Status:** explicit counterexample; the [adjacent audit](rooted_k5_six_root_extension_audit.md)
records its separate review.
This scratch construction is now recorded; no literature provenance or
priority claim is asserted.

**False assertion.** If L is four-connected and five members of a prescribed
six-set T root a K5 minor, then T roots Q6 = K6 minus two independent edges.
The unselected sixth root is allowed to lie in the starting model, as in
the proved five-root wheel extension.

Let L be the square of the seven-cycle: its vertices are 0,...,6 modulo
seven, and two vertices are adjacent exactly when their cyclic distance
is one or two. Set T = {0,1,2,3,4,5}. The five bags

    {0}, {1}, {2}, {3,5}, {4,6}

are connected and pairwise adjacent, giving a K5 rooted at 0,1,2,3,4.
The sixth root 5 belongs to the starting bag rooted at 3.

**Connectivity.** Deleting at most three vertices leaves L connected:
two different components would require two separating gaps in the cyclic
order, each containing at least two consecutive deleted vertices. That
requires at least four deletions. Every vertex has degree four, so
kappa(L) = 4.

**Minor exclusion.** L has seven vertices and fourteen edges. Every edge
has a common neighbour, so every edge contraction leaves at most twelve
edges. Deleting a vertex leaves ten edges. Any minor with six vertices
is a subgraph of one of these quotients or vertex deletions: only one
vertex-reducing operation is possible, and prior edge deletions cannot
increase the resulting edge count. Since Q6 has thirteen edges, L has
no Q6 minor at all, and hence no T-rooted one.

**Scope.** The partition {0,3}, {1,4}, {2,5}, {6} properly four-colours L.
An independent set has order at most two, since three cyclic gaps of
length at least three cannot fit in a seven-cycle; thus chi(L) = 4.
The first failed inference is an arbitrary sixth-root extension from
four-connectivity and an existing rooted clique model. This example does
not satisfy the five-chromatic universally colourful marked hypothesis,
and does not refute that target, the five-root wheel theorem, or HC7.
