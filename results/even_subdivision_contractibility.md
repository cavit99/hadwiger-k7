# Even subdivisions are contractible

**Status:** computation-free written proof with two separate internal
audits at the exact source hash recorded in the adjacent audit files.
This is an independent graph-scheme theorem, not a completion of T44,
Norin--Totschnig Conjecture 21, or `HC_7`.

## 1. Statement and terminology

All graphs are finite. Target and scheme graphs are simple. Auxiliary
multigraphs may have parallel edges but no loops.

An **`H`-scheme** in `G`, with `V(H) subseteq V(G)`, is a family of paths
`P_uv`, one for each `uv in E(H)`, such that:

1. `P_uv` joins `u` to `v` and contains no other vertex of `H`;
2. whenever a nonempty collection of scheme paths has a common vertex,
   their corresponding edges of `H` have a common endpoint.

A **rooted `H` minor** consists of pairwise disjoint connected sets `C_v`,
one for each `v in V(H)`, with `v in C_v` and an edge between `C_u,C_v`
for every `uv in E(H)`. The graph `H` is **contractible** if every graph
containing an `H`-scheme contains such a rooted minor. These are the
definitions of Kündgen--Pelsmajer--Ramamurthi [1, Definitions 1.1 and 2.1].

### Theorem 1.1

Let `H` be a bipartite graph with a specified bipartition `(A,B)`. If
`d_H(b)<=2` for every `b in B`, then `H` is contractible.

### Corollary 1.2 (even subdivisions)

Let `F` be any finite loopless multigraph. Replace each edge of `F` by a
path of positive even length, with mutually disjoint new internal vertices.
The resulting simple graph is contractible.

**Proof of the corollary.** Put every original vertex of `F`, and every
even-position internal vertex of each replacement path, in `A`. Put the
odd-position internal vertices in `B`. Every vertex of `B` has degree two,
and every edge joins `A` to `B`. Apply Theorem 1.1. Isolated vertices of
`F` cause no difficulty. QED

In particular, the theorem includes the graph obtained by subdividing
every edge of an arbitrary simple graph exactly once. It also includes
`K_{2,n}` for every `n`, by taking the part of order `n` as `B`.

## 2. A packing lemma with partially shared labels

### Lemma 2.1

Let `J` be a finite index set. For each `j in J`, let `M_j` be a connected
multigraph with a distinguished vertex `r_j` and an edge set labelled
bijectively by a finite set `E_j`. Suppose:

1. `M_j` is the union of paths all containing `r_j`, whose edge sets
   partition `E_j`;
2. every vertex other than `r_j` belongs to at least two of those paths;
3. every element of `E=union_j E_j` belongs to at most two of the sets
   `E_j`.

Trivial paths are allowed. A graph with no paths is allowed precisely when
it consists of its distinguished vertex. Then there are pairwise disjoint
sets `T_j subseteq E_j` such that `T_j` is a spanning tree of `M_j` for
every `j`.

### Proof

Fix `X subseteq E`. Let `c_j(X)` count the components, including isolated
vertices, of the spanning subgraph of `M_j` with edge labels `E_j cap X`.
Write `m_j` for the number of prescribed paths. The component containing
`r_j` meets all `m_j` paths, and every other component meets at least two.
Counting incidences between paths and components gives

\[
 m_j+2(c_j(X)-1)
 \leq \sum_C |\{Q:V(Q)\cap V(C)\ne\varnothing\}|
 \leq m_j+|E_j\setminus X|.                         \tag{2.1}
\]

For the last inequality, deleting `E_j-X` breaks each path into at most one
more piece than its number of deleted edges. Each piece lies in one
component. Different pieces may lie in the same component, which only
reduces the incidence count. Edge-disjointness of the paths makes the
sum of deleted-edge counts exactly `|E_j-X|`. Thus

\[
 c_j(X)-1\leq\tfrac12|E_j\setminus X|.              \tag{2.2}
\]

Regard the graphic matroid of `M_j` as a matroid `mathcal M_j` on `E` by
declaring every label outside `E_j` to be a matroid loop. These are loops
in the matroid, not added edges in `M_j`. Its rank function satisfies

\[
 \rho_j(E)=|V(M_j)|-1,
 \qquad \rho_j(X)=|V(M_j)|-c_j(X).
\]

Summing (2.2) and using the label multiplicity hypothesis yields

\[
 \sum_j(\rho_j(E)-\rho_j(X))
 \leq\tfrac12\sum_j|E_j\setminus X|
 \leq |E\setminus X|.                              \tag{2.3}
\]

Edmonds' matroid union rank formula [2] is

\[
 \rho_{\bigvee_j\mathcal M_j}(E)
 =\min_{X\subseteq E}\left(|E\setminus X|+\sum_j\rho_j(X)\right).
\]

Equation (2.3), and the choice `X=E`, show that this rank equals
`sum_j rho_j(E)`. Express a maximum independent set of the union as
`union_j I_j`, with `I_j` independent in `mathcal M_j`. Equality throughout

\[
 |\bigcup_j I_j|\leq\sum_j|I_j|\leq\sum_j\rho_j(E)
\]

forces the `I_j` to be pairwise disjoint bases. A base contains no matroid
loops, so `T_j=I_j subseteq E_j` is a spanning tree of `M_j`. QED

## 3. Proof of Theorem 1.1

Kündgen--Pelsmajer--Ramamurthi [1, Lemma 3.3] reduce an `H`-scheme by
root-preserving minor operations to a **coloured `H`-scheme**. In its
underlying graph `G`, a proper colouring `f:V(G)->V(H)` fixes every root;
`P_uv` uses only colours `u,v`; and every nonroot has degree at least four.
The paths alternate colours, share no edge, and every nonroot lies on at
least two scheme paths [1, Remark 3.2(1), (2), (6), (7)]. Remove isolated
roots before this reduction and restore them as singleton branch sets.
It suffices to construct the rooted model in this reduced
graph and then compose the rooted minor models.

Put `A_a=f^{-1}(a)` for `a in A` and `L_b=f^{-1}(b)` for `b in B`.
If `d_H(b)<=1`, then `L_b={b}`: a nonroot of colour `b` would have to lie
on at least two distinct paths incident with `b`, which do not exist.
If `d_H(b)=2`, every vertex of `L_b-{b}` lies internally on both paths
incident with `b`. Define

\[
 E=\bigcup_{b\in B}(L_b\setminus\{b\}),
 \qquad
 E_a=\bigcup_{b\in N_H(a)}(L_b\setminus\{b\}).       \tag{3.1}
\]

These are sets of actual nonroot vertices, used as edge labels. Every
label in `E` has a degree-two root colour `b` and hence belongs to exactly
two sets `E_a`, corresponding to the two distinct neighbours of `b`.

For each `a in A`, form `M_a` on vertex set `A_a`. For each
`x in L_b-{b}` with `ab in E(H)`, replace `x` on `P_ab` by an auxiliary
edge, labelled `x`, between its two neighbours of colour `a` on that path.
The two neighbours are distinct because `P_ab` is a path. Different
labels may produce parallel edges.

Suppressing all such `x` on `P_ab` and removing its terminal vertex `b`
leaves a path `Q_b^a` in `M_a`, from `a` to the `A_a`-neighbour of `b`.
If `P_ab` is the edge `ab`, this path is trivial. Since every nonroot
vertex of colour `b` lies on `P_ab`, its edge-label set is exactly
`L_b-{b}`. As `b` ranges over `N_H(a)`, these paths partition `E_a`.
They cover `A_a` and all contain `a`, so `M_a` is connected. If `a` is
isolated, take `M_a` to be the single vertex `a`.

Every vertex of `A_a-{a}` lies internally on at least two distinct scheme
paths incident with `a`. It therefore belongs to at least two distinct
paths `Q_b^a`. The graphs `M_a` satisfy every hypothesis of Lemma 2.1.
Choose the resulting pairwise disjoint spanning-tree label sets `T_a`.

In the reduced graph `G`, define

\[
 C_a=A_a\cup T_a\quad(a\in A),
 \qquad C_b=\{b\}\quad(b\in B).                     \tag{3.2}
\]

All these sets are disjoint: the `A_a` are distinct colour classes, the
`T_a` are disjoint sets of nonroot `B`-colour vertices, and none contains
a root of `B`. A tree edge in `M_a` labelled `x` lifts to the two-edge
path through `x` in `G`; thus `G[C_a]` is connected. Each `C_a` contains
`a`. Each edge `ab` of `H` is witnessed by the last edge of `P_ab`, joining
the root `b` to a vertex of `A_a subseteq C_a`. Consequently (3.2) is a
rooted `H`-minor model.

Finally lift the root-preserving reduction from [1, Lemma 3.3]. Replacing
each vertex of a model branch set by its connected preimage preserves
connectivity, disjointness, root containment and all required adjacencies.
This proves Theorem 1.1. The `B` branch sets are singleton only in the
reduced coloured scheme; singleton branch sets in the original arbitrary
scheme are not asserted. QED

## 4. Reach, provenance and limits

The earlier [two-projection proof for `K_{2,n}`](k2n_contractibility_via_matroid_packing.md)
is the special case with two graphs and identical label sets. The new step
is to allow arbitrarily many projections with partially shared labels:
each label is charged to at most two projections, so the same component
count verifies the full matroid union inequality. No induction on a
hypothetical counterexample, separator preservation, or finite enumeration
enters the proof.

The theorem supplies a family of contractible graphs with unbounded
treewidth: it includes a once-subdivision of `K_t` for every `t`, and
contracting its subdivided edges recovers `K_t`. Contractibility itself is
not asserted to be minor-closed. Thus this does not make `K_t`
contractible or prove a Hadwiger conjecture.

For a theta graph formed by three internally disjoint paths between two
vertices, the theorem covers the case where all three paths have even
length. This is only part of [1, Section 8, Question 3]. A bipartite theta
may instead have three odd-length paths, with its two degree-three vertices
in opposite bipartition classes; that case is not covered. Neither
`K_{3,3}` nor all bipartite graphs are covered. Degree two on the specified
side is a hypothesis, not a necessary condition for contractibility.

This is an independent unbounded theorem with a broad family of targets.
It neither closes a T44 subcase nor proves Conjecture 21 or `HC_7`.
Comparison with the significance of Norin--Totschnig's global colouring
theorem requires specialist judgement; no equivalence in significance or
publication priority is claimed here.

## References

1. A. Kündgen, M. J. Pelsmajer and R. Ramamurthi, *Finding minors in graphs
   with a given path structure*, Journal of Graph Theory 79 (2015), 30--47,
   [DOI](https://doi.org/10.1002/jgt.21812),
   [primary preprint](https://arxiv.org/pdf/1207.6141).
2. J. Edmonds, *Submodular functions, matroids, and certain polyhedra*, in
   *Combinatorial Structures and Their Applications*, Gordon and Breach,
   1970, 69--87. The input is the matroid union rank formula stated in
   Section 2, for any finite family of matroids on one ground set.
