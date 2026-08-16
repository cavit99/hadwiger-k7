# Minimal path-bag ownership compresses to order seven or eight

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_p3_owner_circuit_compression_audit.md).
This theorem
removes the nonrepeated order-nine branch from the induced-path allocation
problem while retaining the original path-operation colourings.  It does
not prove the `K_7^-` six-colour conjecture or `HC_7`.

## 1. Setting

Let `G` satisfy

\[
 \chi(G)=7,
 \qquad \chi(J)\le6\text{ for every proper minor }J\text{ of }G,
 \qquad \kappa(G)\ge7,
 \qquad K_7^-\npreccurlyeq G.                       \tag{1.1}
\]

Let

\[
                         P=x-r-y                      \tag{1.2}
\]

be an induced path, with `a=rx,b=ry`.  Fix a spanning `K_6`-minor model

\[
                         (R,D_1,\ldots,D_5)           \tag{1.3}
\]

such that `P\subseteq R`, and choose it to minimise `|R|` among all
spanning `K_6` models having the whole path in one branch set.

For a component `A` of `G[R-V(P)]`, put

\[
 \begin{aligned}
  R_0&=R-A,\\
  T_i&=N_G(D_i)\cap R,\\
  \Omega(A)&=\{i\in\{1,\ldots,5\}:T_i\subseteq A\}.
 \end{aligned}                                      \tag{1.4}
\]

The labels in `\Omega(A)` are the foreign bags whose entire contact with
the path bag lies in `A`.

## 2. Owners and labelled linkages

### Lemma 2.1 (every appendage owns at least two labels)

For every component `A` of `G[R-V(P)]`, the graph `R_0` is connected and

\[
                           |\Omega(A)|\ge2.           \tag{2.1}
\]

The owner sets of distinct components are disjoint.  Consequently
`G[R-V(P)]` has at most two components.

#### Proof

Every component of `G[R-V(P)]` has a neighbour in the connected path `P`,
because `R` is connected.  Thus deleting any one component leaves `R_0`
connected.

Suppose first that `\Omega(A)=\varnothing`.  The set `A` has a neighbour in
some foreign bag `D_i`; otherwise `N_G(A)\subseteq V(P)`, contrary to
seven-connectivity.  Move all of `A` from `R` into that met bag `D_i`.
The new `D_i` is connected.  The set `A` has an edge to `R_0`, which
restores the root--`D_i` model adjacency, and every old root contact with a
foreign bag has a representative in `R_0` because no label was owned by
`A`.  This gives a spanning co-bagged model with a smaller root bag, a
contradiction.

If `\Omega(A)=\{i\}`, move `A` into `D_i`.  All contacts for nonowned
labels survive in `R_0`, while an `A`--`R_0` edge supplies the new
root--`D_i` adjacency.  This is the same contradiction.  Hence (2.1)
holds.

If two distinct components both owned label `i`, the nonempty set `T_i`
would be contained in two disjoint components.  Thus their owner sets are
disjoint.  Disjoint subsets of a five-set, each of order at least two,
number at most two. `\square`

This transfer is the point at which spanningness matters: a zero-owner
component cannot be arbitrary filler, because seven-connectivity forces it
to meet a foreign bag and the resulting move still partitions every vertex
among the six model bags.

For fixed `A`, define

\[
             B=N_G(R_0)\cap A,
 \qquad     A_i=N_G(D_i)\cap A\quad(i\in\Omega(A)).  \tag{2.2}
\]

A **full labelled linkage** in `A` consists of pairwise vertex-disjoint
paths, with trivial paths allowed, one from a vertex of `B` to a vertex of
`A_i` for every `i\in\Omega(A)`.  Pairwise vertex-disjointness makes all
chosen path ends distinct.

### Lemma 2.2 (a full linkage would shrink the path bag)

No full labelled linkage exists in `A`.

#### Proof

Suppose paths `Q_i` form such a linkage.  The disjoint connected subgraphs
`Q_i` can be extended to a partition

\[
                         A=\mathbin{\dot\bigcup}_{i\in\Omega(A)}P_i
                                                               \tag{2.3}
\]

into connected sets with `Q_i\subseteq P_i`: contract the `Q_i`, take a
spanning forest rooted at their contraction images, and assign each
remaining vertex along that forest.

Move `P_i` from `R` into `D_i` for every owner `i`.  Each enlarged foreign
bag is connected because `P_i` meets `A_i`, and it is adjacent to `R_0`
because `P_i` contains its distinct `B`-end.  Every nonowned foreign bag
retains a root contact in `R_0`.  The foreign bags remain pairwise adjacent
and all vertices remain assigned.  The result is a spanning `K_6` model
whose path bag is the proper subset `R_0`, contradicting minimality. `\square`

### Lemma 2.3 (minimal owner circuit)

There are a set `I\subseteq\Omega(A)` and a vertex set `S\subseteq A` such
that

\[
             2\le |I|\le4,
       \qquad |S|=|I|-1,                             \tag{2.4}
\]

and `S` meets every path in `G[A]` from `B` to

\[
                         A_I=\bigcup_{i\in I}A_i.     \tag{2.5}
\]

#### Proof

Apply Rado's independent-transversal theorem to the strict gammoid in
`G[A]` whose independent sets are the vertex sets linkable by disjoint
paths to `B`, and to the family `(A_i:i\in\Omega(A))`.  Lemma 2.2 says
that the family has no independent transversal.  Choose an
inclusion-minimal deficient subfamily `I`.  Every proper subfamily is
linkable.  For any `i\in I`, this gives the rank squeeze

\[
 |I|-1\le r(A_{I-\{i\}})\le r(A_I)<|I|,
\]

so `r(A_I)=|I|-1`.  The vertex form of Menger's theorem therefore supplies
a set `S\subseteq A` of order `|I|-1` meeting every `B`--`A_I` path.  A
singleton family is linkable because `A` is connected and both `B,A_i`
are nonempty, so `|I|\ge2`.

It remains to exclude `|I|=5`.  Then every foreign label is owned by `A`,
so `R_0` has no edge to

\[
                            D=D_1\cup\cdots\cup D_5. \tag{2.6}
\]

The set `D` is nonempty and connected because the five foreign bags are
pairwise adjacent.  Every `R_0`--`D` path first enters `A` at a vertex of
`B` and, before its first vertex in `D`, reaches a vertex of `A_I`.  It
therefore meets `S`.  Thus the four-set `S` separates the nonempty connected
sets `R_0` and `D`, contrary to seven-connectivity.  Hence `|I|\le4`.
`\square`

## 3. The bounded boundary theorem

### Theorem 3.1 (shared portal, repeated contact, or order at most eight)

For every component `A` and the sets `I,S` in Lemma 2.3, at least one of
the following holds.

1. **Shared labelled contact.**  Some vertex `s\in S` is adjacent to two
   differently labelled foreign bags `D_i,D_j`.
2. **Bounded component boundary.**  There is a component `C` of `G[A-S]`
   such that

   \[
       C\text{ is anticomplete to }R_0,
       \qquad 7\le |N_G(C)|\le8.                    \tag{3.1}
   \]

3. **Repeated foreign-bag contact.**  There is such a component `C` with
   `|N_G(C)|\ge9`, and some foreign bag `D_j` contains two distinct
   vertices of `N_G(C)`.

In particular, an order-nine boundary with at most one boundary vertex in
each foreign bag is impossible.

#### Proof

If `A_I\subseteq S`, then the `|I|` nonempty sets `A_i` are contained in
the `( |I|-1 )`-set `S`.  Two of them contain a common vertex, giving
outcome 1.

Otherwise let `C` be a component of `G[A-S]` meeting `A_I-S`.  The set `C`
contains no vertex of `B`, because `S` separates `B` from `A_I`.  Hence it
is anticomplete to `R_0`, and

\[
                         N_G(C)\cap R\subseteq S.     \tag{3.2}
\]

The model is spanning, so every other neighbour belongs to one of the five
foreign bags.  If no foreign bag contains two distinct boundary vertices,

\[
          7\le |N_G(C)|
             \le |S|+5=|I|+4\le8.                  \tag{3.3}
\]

The lower bound is seven-connectivity; the opposite side contains `R_0`.
This is outcome 2.  If the upper estimate fails, some foreign bag repeats;
when the boundary has order at least nine this is outcome 3. `\square`

### Corollary 3.2 (exact numerical forms)

In the nonrepeated outcome:

1. `|I|=2` is impossible.
2. If `|I|=3`, then `|N_G(C)|=7` and

   \[
      N_G(C)=S\mathbin{\dot\cup}
                  \{q_i:q_i\in D_i,\ i=1,\ldots,5\}. \tag{3.4}
   \]

3. Boundary order eight occurs only when `|I|=4`, and then

   \[
      N_G(C)=S\mathbin{\dot\cup}
                  \{q_i:q_i\in D_i,\ i=1,\ldots,5\},
      \qquad |S|=3.                                 \tag{3.5}
   \]

4. If `G[R-V(P)]` has two components, every nonrepeated bounded outcome
   has boundary order exactly seven.

#### Proof

For `|I|=2`, (3.3) gives a boundary of order at most six, contradicting
seven-connectivity.  For `|I|=3`, equality holds throughout (3.3), forcing
both vertices of `S` and one vertex from every foreign bag.  Equality at
eight similarly forces `|I|=4`, all three vertices of `S` and one vertex
from every foreign bag.  Finally, Lemma 2.1 gives two disjoint owner sets
of orders at least two inside a five-set; each then has order at most three.
Apply the preceding cases. `\square`

## 4. The original path responses survive on the returned boundary

The three nonempty signatures on `\{a,b\}` coexist on
`G-\{a,b\}` by minor-criticality and inducedness of `P`.  Fix colourings

\[
                       \phi_a,\quad\phi_b,\quad\phi_{ab}.
                                                               \tag{4.1}
\]

### Theorem 4.1 (literal response inheritance)

For every component `C` returned in Theorem 3.1,

\[
                   P\cap(C\cup N_G(C))=\varnothing. \tag{4.2}
\]

Each of the three colourings in (4.1) restricts properly to
`G[C\cup N_G(C)]`, and its literal equality partition on `N_G(C)` is
rejected by the opposite intact closed shore.

More strongly, let `g=cq` be any edge with `c\in C` and
`q\in N_G(C)`.  The graph `G-\{a,b,g\}` realises all seven nonempty
signatures on the componentwise-induced forest `P_3\dot\cup K_2`.  The
`\{g\}`-only colouring restricts properly to `G-C`, while the three
nonempty path-only colourings restrict properly to
`G[C\cup N_G(C)]`.  Their boundary partitions are rejected by the opposite
intact shores.

#### Proof

The component `C` is anticomplete to `R_0`, and `P\subseteq R_0`.  Hence no
path vertex belongs to `C` or to its neighbourhood, proving (4.2).  The
only possibly monochromatic restored edges under the colourings in (4.1)
belong to `P`, so all three restrictions to the closed `C`-shore are
proper.  If one boundary partition extended through the opposite intact
shore, colour-name alignment and gluing would six-colour `G`.

The edge `g` is vertex-disjoint from `P` by (4.2).  Thus
`\{a,b,g\}` is a componentwise-induced forest.  Contracting every nonempty
subset and expanding a six-colouring gives all seven exact signatures.
In the `g`-only signature, deleting `C` removes the sole monochromatic edge.
In each nonempty path-only signature, (4.2) removes all monochromatic edges
from the closed `C`-shore, while `g` is proper.  The same gluing argument
gives the stated rejections. `\square`

The quantifiers in Theorem 4.1 remain synchronized: the original path
colourings and the original co-bagged model are restricted to the same
literal boundary.  No independently chosen replacement model is used.

## 5. Exact scope

The all-five-owner case and hence the nonrepeated order-nine boundary are
eliminated outright.  The nonrepeated outcomes are the exact labelled
`2+5` order-seven boundary in (3.4) and the exact labelled `3+5`
order-eight boundary in (3.5), both carrying the original path-operation
responses.

Three genuine residues remain.

- A shared vertex adjacent to two foreign bags need not make four bags meet
  all three pieces of the path bag.
- Repeated contact with one foreign bag is only separately
  model-persistent; existing repeated-contact and fixed-trace-rotation
  barriers prevent treating it as an automatic allocation or descent.
- If `R=V(P)`, then no appendage exists.  The existing three-piece
  composition gives a `K_7^-` model when every one of `x,r,y` meets at
  least four foreign bags; the target-free residue has one path vertex
  meeting at most three bags.

An exact order-seven output enters the audited generic exact-seven restart,
which can still return a singleton shore, separator excess or a
shore-filling core.  An exact order-eight output enters the existing
operation-coupled order-eight machinery after any non-full complementary
component has first exposed an exact order-seven boundary.  Those later
theorems retain fan, Hall and branch-set absorption alternatives.  This
note therefore removes a real unbounded/order-nine obstruction without
claiming terminal closure.

## 6. Dependencies

- Rado's independent-transversal theorem and the vertex form of Menger's
  theorem
- [induced-path common-pivot and allocation frontier](../active/hc7_k7minus_p3_common_pivot_allocation_gate.md)
- [generic exact-seven response restart](hc7_generic_exact7_response_restart.md)
- [three-piece `K_5` composition](hc7_k7minus_three_piece_k5_composition.md)
- [full order-eight four-component closure](hc7_full_order8_four_component_closure.md)
- [operation-coupled order-eight response theorem](hc7_operation_coupled_order8_response.md)
- [repeated-contact component-defect barrier](../barriers/hc7_repeated_contact_component_defect_barrier.md)
- [fixed-trace edge-rotation barrier](../barriers/hc7_fixed_trace_edge_rotation_barrier.md)
