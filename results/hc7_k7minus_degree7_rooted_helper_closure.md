# Degree-seven closure from a rooted two-helper model

**Status:** written proof with a separate hash-pinned internal audit.  The
theorem is computation-free.  Its critical-host corollary eliminates every
degree-seven vertex, but does not by itself settle the `K_7^-` six-colour
conjecture or `HC_7`.

Throughout, `K_7^-` denotes the graph obtained from `K_7` by deleting one
edge.  A `Z`-rooted `K^*_{4,2}` model consists of four pairwise disjoint
connected root bags, one containing each member of the four-set `Z`, and two
further disjoint connected helper bags.  Each helper is adjacent to all four
root bags, and the two helpers are adjacent.  No adjacency between distinct
root bags is included in the definition.

We use the following theorem of Norin and Totschnig in its exact rooted form.

> **Rooted two-helper bound.**  Let `F` be a graph and let `Z` be a four-set
> such that `(F,Z)` is internally four-connected.  If `F` has no `Z`-rooted
> `K^*_{4,2}` model, then
> \[
>                         |E(F)|\le 4|V(F)|-10.        \tag{1}
> \]

This is Norin--Totschnig, Lemma 12.

## Lemma 1 (placing a fifth root in a helper)

Let `F` be a graph, let `S=Z\mathbin{\dot\cup}\{x\}`, where `|Z|=4`, and
suppose that `(F,S)` is internally five-connected.  If `F` has a `Z`-rooted
`K^*_{4,2}` model, then it has one in which `x` belongs to a helper bag.

### Proof

Choose a `Z`-rooted model whose helper bags `U,V` have maximum total order,
and, subject to that, whose four root bags `R_1,\ldots,R_4` have minimum total
order.  Write `z_i` for the root in `R_i`, and put

\[
 P_i=\{r\in R_i:r\text{ has a neighbour in }U\cup V\}.
\]

We claim that `|P_i|=1`.  Both helpers meet `R_i`, so `P_i` is nonempty.  If
it had at least two vertices, there would be distinct `u,v\in R_i` such that
`u` meets `U` and `v` meets `V`; otherwise both helper-contact sets would be
the same singleton.  Take a minimal tree in `F[R_i]` containing `z_i,u,v`.
By the minimal choice of the root bags, this tree spans `R_i`.  One of `u,v`,
say `u`, is a leaf different from `z_i`.  Moving `u` from `R_i` into `U`
preserves connectivity of both altered bags.  The former tree edge from `u`
to `R_i-u` preserves the `R_i`--`U` contact, while `v` preserves the
`R_i`--`V` contact.  Every other required model adjacency is unchanged.  The
helper union has grown, a contradiction.  Hence `|P_i|=1`.

No component outside the six model bags can meet `U\cup V`: absorbing such a
component into a helper that it meets would again enlarge the helper union.
It follows that

\[
                 |N_F(U\cup V)-(U\cup V)|\le4,        \tag{2}
\]

with at most one external neighbour in each root bag.  If `x` were outside
the helpers, (2) would give a separation of `(F,S)` of order at most four
whose second open side is the nonempty set `U\cup V`.  This contradicts
internal five-connectivity.  Thus `x\in U\cup V`.  \(\square\)

## Theorem 2 (low-degree rooted-helper closure)

Let `G` be a six-connected graph of order `n`, let `v\in V(G)` have degree
`d>=5`, and suppose that `G[N_G(v)]` contains a literal `K_4`.  If

\[
                          |E(G)|\ge4n+d-13,            \tag{3}
\]

then `G` contains a `K_7^-` minor.

### Proof

Let `Z\subseteq N_G(v)` induce `K_4`, choose
`x\in N_G(v)-Z`, and put `F=G-v`.  Deleting one vertex from a
six-connected graph leaves a five-connected graph.  In particular,
`(F,Z)` is internally four-connected and
`(F,Z\cup\{x\})` is internally five-connected.

By (3),

\[
 |E(F)|=|E(G)|-d
       \ge4n-13
       =4|V(F)|-9.                                    \tag{4}
\]

The rooted bound (1) therefore supplies a `Z`-rooted `K^*_{4,2}` model in
`F`.  Lemma 1 lets us choose it with `x` in one helper bag.

The four root bags are pairwise adjacent: the literal edges of `G[Z]=K_4`
join the corresponding bags.  Together with the two adjacent helpers they
therefore form a `K_6` model.  The singleton bag `\{v\}` is adjacent to all
four root bags through the edges from `v` to `Z`, and it is adjacent to the
helper containing `x` through `vx`.  It may miss only the other helper.
These seven bags form a `K_7^-` model in `G`.  \(\square\)

## Corollary 3 (the critical host is `K_5`-free and has many degree-eight vertices)

Let `G` satisfy

\[
 \kappa(G)\ge7,\qquad \chi(G)=7,\qquad
 \chi(M)\le6\text{ for every proper minor }M\text{ of }G,
 \qquad K_7^-\npreccurlyeq G.                         \tag{5}
\]

Then

\[
                         \delta(G)\ge8.               \tag{6}
\]

Consequently

\[
                         |E(G)|\ge4|V(G)|.             \tag{7}
\]

Moreover `G` has no literal `K_5`.  If `n_i` denotes the number of
degree-`i` vertices and

\[
                  \tau=\sum_{i\ge10}(i-9)n_i,
\]

then

\[
                         n_8\ge25+\tau.                \tag{8}
\]

In particular, `G` has at least 25 degree-eight vertices, and every one of
them has a `K_4`-free neighbourhood.

### Proof

Suppose that `v` has degree seven.  The audited exact degree-seven
clique-incidence theorem says that `v` belongs to a literal `K_5`.
Therefore `G[N(v)]` contains a literal `K_4`.  The audited critical-host
density theorem gives

\[
                         |E(G)|\ge4|V(G)|-2,
\]

which is stronger than (3) for `d_G(v)=7`.  Theorem 2 produces the forbidden
`K_7^-` minor.  Hence no vertex has degree seven.  Seven-connectivity gives
minimum degree at least seven, proving (6), and degree summation gives (7).

Put `q=|E(G)|-4|V(G)|`, so `q>=0`.  Suppose that a literal `K_5` has vertex
set `K`.  For each `w\in K`, the neighbourhood of `w` contains the literal
`K_4` on `K-\{w\}`.  Since `G` is target-free, the contrapositive of
Theorem 2 gives

\[
 4|V(G)|+q<4|V(G)|+d_G(w)-13,
\]

and hence `d_G(w)>=q+14`.  The five vertices of `K` would therefore
contribute at least `5(q+6)` to

\[
 \sum_{z\in V(G)}(d_G(z)-8)=2q,
\]

which is impossible.  Thus `G` contains no literal `K_5`.

The separately audited Jakobsen defect calculation for the same critical
host says

\[
                   25\le2n_7+n_8-\tau.
\]

We have proved `n_7=0`, so (8) follows.  Finally, a degree-eight vertex with
a `K_4` in its neighbourhood would lie in a literal `K_5`, which has just
been excluded.  \(\square\)

## Scope

Corollary 3 closes the entire degree-seven and literal-`K_5` branches of the
colouring-critical programme without a safe contraction or an
order-seven-cut analysis.  The only surviving critical-host branch has
minimum degree at least eight and at least 25 exceptional degree-eight
vertices.

## External source and internal dependencies

- Sergey Norin and Agnès Totschnig, *Every graph with no
  `K_7^\vee`-minor is 6-colourable*, Lemma 12,
  [arXiv:2507.03244](https://arxiv.org/abs/2507.03244).
- [Exact degree-seven clique incidence](hc7_k7minus_degree7_clique_incidence.md).
- [Critical-host density and Jakobsen defect bounds](hc7_k7minus_two_literal_k5_exclusion.md#corollary-3-critical-host-consequences).
