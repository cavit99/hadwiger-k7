# One edge meets every odd cycle in a connected triangle-free contractible graph

**Status:** written proof with a separate internal audit at the exact
source hash recorded beside this file. This is a necessary structural theorem, not a classification
or a solution of Hadwiger's conjecture. Authoritative status remains in
the [research ledger](../RESEARCH_LEDGER.md).

All graphs are finite and simple. A *skewed theta* consists of three
internally disjoint paths with the same two distinct ends, two paths
of odd length and one of even length. A *totally odd subdivision* of
`K_4` replaces each of its six edges by a positive odd-length path,
with different paths internally disjoint.

## Statements

**Theorem 1.** Let `G` be a 2-connected nonbipartite graph containing
neither a skewed theta nor a totally odd subdivision of `K_4`. Then
there is an edge `e` such that `G-e` is bipartite.

**Theorem 2.** If a connected triangle-free graph `H` is contractible,
then either `H` is bipartite or there is an edge `e` such that `H-e`
is bipartite. Thus each connected component of a triangle-free
contractible graph has an edge set of size at most one meeting all
its odd cycles.

Here *contractible* means that every `H`-scheme has an `H`-minor rooted
at every prescribed vertex. Theorem 2 does not assume or conclude a
model with singleton roots.

## Exact signed-graph input

In a signed graph `(G,Sigma)`, an edge in `Sigma` has sign one and
another edge has sign zero. A cycle is odd when its signs sum to one
modulo two. *Switching* adds a vertex cut to `Sigma` by symmetric
difference, preserving all cycle parities. Signed minors permit edge
deletions, switching, and contraction of edges of sign zero; equivalently
one can contract an edge set containing no odd cycle after switching
all its edges to sign zero. The signed graph `odd-K_4` is `K_4` with
all six edges of sign one.

We use the following consequence of Seymour's theorem: if a signed
graph has no signed `odd-K_4` minor, its minimum number of edges meeting
all odd cycles equals its maximum number of pairwise edge-disjoint odd
cycles. This is the unit-capacity case of statement 1.1 in
Geelen--Guenin [1, pp. 281--282], proved independently there in Section 3.
Their exact theorem characterizes packing for **every** nonnegative
integral edge-capacity vector. It has no Eulerian hypothesis. We use
only the forward implication and do not identify ordinary unit-capacity
packing alone with exclusion of `odd-K_4`.

## Lifting a signed minor to a subdivision

**Lemma 3.** If `(G,E(G))` has a signed `odd-K_4` minor, then `G`
contains a skewed theta or a totally odd subdivision of `K_4`.

**Proof.** Take a signed minor certificate. Its four vertices have
pairwise disjoint connected preimages `B_1,...,B_4` made from the
contracted edge set, which has no odd cycle. Choose a tree `T_i` in
each `B_i` spanning the ends of the three selected edges from `B_i`
to the other branch sets. There is exactly one selected edge for each
pair `i,j`. Delete all other edges for the purpose of this construction.

Switch the original signature so that every contracted edge has sign
zero. The induced signature on the selected six edges is equivalent
to the all-one signature on `K_4`. By a further switch constant on
each `B_i`, make all six selected edges have sign one, without changing
the zero signs inside the branch trees. Both switches together have
the form

```text
sigma(xy) = 1 + s(x) + s(y)  (mod 2)
```

for a function `s:V(G)->{0,1}`, since the original signature gave every
edge sign one.

The three attachment vertices in `T_i` may coincide. Let `q_i` be
their tree median: the common vertex of their three pairwise connecting
paths. The three paths from `q_i` to the attachment vertices intersect
only at `q_i`; some may have length zero. Combine the two corresponding
tree paths and the selected edge between `B_i` and `B_j` to obtain a
`q_i,q_j`-path `P_ij`. The six resulting paths have pairwise disjoint
interiors. This remains true for repeated attachment vertices because
the median construction then makes the repeated arms trivial. They
therefore form a subdivision of `K_4` in the original graph.

Each `P_ij` has switched sign sum one: its tree edges have sign zero
and its one interbranch edge has sign one. If `p_ij` is the ordinary
length parity of `P_ij` and `s_i=s(q_i)`, telescoping the switching
formula gives

```text
p_ij = 1 + s_i + s_j  (mod 2).
```

If all four `s_i` agree, all six paths are odd, as required. Otherwise
choose `i,j` with different values, and let `k,l` be the remaining
indices. The three internally disjoint `q_i,q_j`-paths

```text
P_ij,   P_ik union P_kj,   P_il union P_lj
```

have parities zero, one, one respectively. They form a skewed theta.
This proves the lemma. ∎

The proof explicitly lifts the signed minor through disjoint branch
trees; it does not replace a signed minor by a subdivision without a
parity check. It is an extraction from a finite minor certificate,
not an induction or a reduction of a rooted scheme. No scheme-root
or colouring preservation is asserted for this extraction.

## Proofs of the structural theorems

**Proof of Theorem 1.** Lemma 3 and the two excluded subgraphs imply
that `(G,E(G))` has no signed `odd-K_4` minor. By [1, statement 1.1],
the minimum odd-cycle edge cover equals the maximum number of
edge-disjoint odd cycles.

Benchetrit--Sebő [2, Lemma 2.3] states that a 2-connected graph has a
skewed theta if and only if two of its odd cycles have an even number
of common edges. In particular, the present graph has no two
edge-disjoint odd cycles. Nonbipartiteness supplies an odd cycle, so
the maximum packing size is exactly one. The minimum cover therefore
consists of one edge `e`. The graph `G-e` has no odd cycle and hence
is bipartite. ∎

**Proof of Theorem 2.** Contractibility is inherited by subgraphs by
Kündgen--Pelsmajer--Ramamurthi [3, Lemma 2.2]. Their Theorem 7.10
excludes triangle-free skewed thetas from contractible graphs. The
[odd-subdivision obstruction, Corollary 4](../barriers/triangle_free_odd_subdivision_contractibility.md#an-unbounded-family-of-odd-subdivision-obstructions)
excludes every triangle-free totally odd subdivision of `K_4`.
Consequently every 2-connected nonbipartite subgraph of `H` satisfies
Theorem 1.

There is at most one nonbipartite block of `H`. Indeed, otherwise
choose an odd cycle in each of two such blocks. Cycles in distinct
blocks meet in at most one vertex, and triangle-freeness makes both
cycles have length at least five. Since `H` is connected, [3,
Corollary 7.8] excludes its contractibility.

If there is no nonbipartite block, `H` is bipartite. Otherwise apply
Theorem 1 to the unique nonbipartite block `B` to obtain `e in E(B)`
such that `B-e` is bipartite. Every cycle of `H` lies in a block;
all other blocks already are bipartite. Thus `H-e` contains no odd
cycle and is bipartite. The componentwise statement follows by
applying this argument separately. ∎

## Provenance and limits

The signed packing theorem is established external input, attributed
to Seymour and used through the independent primary proof of
Geelen--Guenin. The cycle-intersection criterion is the exact primary
statement of Benchetrit--Sebő. Lemma 3 and the deductions above are
written here; no novelty claim is made for Theorem 1 as a consequence
of these established results. No construction from Cao's thesis is
used.

Theorem 2 gives a necessary condition only. It is not sufficient:
the triangle-free theta with path lengths `2,3,3` has an edge meeting
all its odd cycles, but [3, Theorem 7.10] excludes contractibility.
Even after excluding all known obstructions, converting schemes of
the remaining graphs into fully rooted minors remains a separate
positive proof obligation. These theorems do not close it, prove
`HC_7`, or establish a significance comparison with Norin--Totschnig.

## References

1. J. F. Geelen and B. Guenin, *Packing Odd Circuits in Eulerian Graphs*,
   Journal of Combinatorial Theory, Series B 86 (2002), 280--295,
   [author PDF](https://www.math.uwaterloo.ca/~jfgeelen/Publications/even.pdf),
   [DOI](https://doi.org/10.1006/jctb.2002.2128).
   Statement 1.1 and Section 3 reprove the signed specialization of
   P. D. Seymour, *The matroids with the Max-Flow Min-Cut Property*,
   Journal of Combinatorial Theory, Series B 23 (1977), 189--222.
2. Y. Benchetrit and A. Sebő, *Ear-decompositions and the complexity of
   the matching polytope*, [primary preprint](https://arxiv.org/pdf/1509.05586),
   Lemma 2.3.
3. A. Kündgen, M. J. Pelsmajer and R. Ramamurthi, *Finding minors in
   graphs with a given path structure*, Journal of Graph Theory 79
   (2015), 30--47, [primary preprint](https://arxiv.org/pdf/1207.6141),
   [DOI](https://doi.org/10.1002/jgt.21812).
   Lemma 2.2, Corollary 7.8 and Theorem 7.10.
