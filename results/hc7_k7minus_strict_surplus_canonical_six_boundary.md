# Canonical sparse six-boundaries in a strict-surplus minimum counterexample

**Status:** written proof; separate internal audit GREEN for the revision
identified in the adjacent audit.  This is a computation-free reduction of
the positive-surplus case.  It does not prove the seven-connected `4n-2`
extremal target, Conjecture 21, or `HC_7`.

Throughout, `K_7^-` denotes the graph obtained from `K_7` by deleting one
edge.  For a graph `G` of order `n`, put

\[
                         q(G)=|E(G)|-(4n-2).
\]

## Lemma 1 (a six-vertex boundary lemma)

Every graph on six vertices which contains neither a literal `K_4` nor a
`K_5^-` minor has at most ten edges.

### Proof

Suppose that such a graph has at least eleven edges, and delete edges until
exactly eleven remain.  Let `R` be the resulting graph.  Its complement has
four edges.  Since `R` has no literal `K_4`, the complement has independence
number at most three.

We record the short complement classification.  If the four-edge graph is
a forest, it has two components.  Their orders are `1+5`, `2+4`, or `3+3`.
The first and third partitions have independence number at least four.  In
the `2+4` partition the two-vertex component is `K_2`; among the two trees
of order four, only `P_4` keeps the total independence number at three.
If the graph contains a cycle, its four edges permit only one cyclic
component.  The component formula then gives three components.  A
four-vertex cyclic component leaves two isolated vertices and again gives
independence number at least four.  The only survivor is a triangle,
together with one edge and one isolated vertex.  Thus, up to isomorphism,
the complement is one of

\[
 K_1\mathbin{\dot\cup}K_2\mathbin{\dot\cup}K_3,
 \qquad
 K_2\mathbin{\dot\cup}P_4.                           \tag{1}
\]

In the first case, contract in `R` an edge joining a vertex of the
complementary `K_2` to a vertex of the complementary `K_3`.  Its ends have
exactly one common neighbour in `R`, namely the vertex isolated in the
complement.  In the second case, write the complementary components as the
edge `ab` and the path `c-d-e-f`, and contract `ae`.  Again the ends have
exactly one common neighbour in `R`, namely `c`.

Either contraction loses exactly two edges.  It therefore produces a
five-vertex graph with nine edges, which is a literal `K_5^-`.  This is a
minor of the original graph, a contradiction.  \(\square\)

## Theorem 2 (reserve blindness and the canonical six-boundary)

Suppose that

\[
 \kappa(H)\ge7,\qquad |E(H)|\ge4|V(H)|-2
 \quad\Longrightarrow\quad K_7^-\preccurlyeq H       \tag{2}
\]

is false.  Choose a counterexample `G` first with minimum order and then
with minimum size, assume `q=q(G)>=1`, and put

\[
 L=\{v\in V(G):d_G(v)=7\},\qquad F=G-L.
\]

There is at most one literal `K_5` in `G`; denote it by `K` when it exists
and otherwise put `K=\varnothing`.  Then:

1. `|L|>=13`, and
   \[
   \{x\in L:N_G(x)\text{ contains a literal }K_4\}=L\cap K. \tag{3}
   \]
   Consequently at least eight vertices of `L` have `K_4`-free
   neighbourhoods.
2. Let `x in L-K` and `y in N_G(x)`, and put
   \[
   T_y=N_G(x)-\{y\},\qquad J_x=G-x.
   \]
   Then `|T_y|=6`, and in `G-xy` the deletion of `T_y` leaves exactly two
   components,
   \[
                    \{x\}\mathbin{\dot\cup}B_y,       \tag{4}
   \]
   where `B_y` is connected and both components are adjacent to every
   vertex of `T_y`.
3. The boundary `G[T_y]` is literal-`K_4`-free and `K_5^-`-minor-free, and
   \[
                         |E(G[T_y])|\le10.             \tag{5}
   \]
4. Define
   \[
    \delta_{B_y}=|E(G[B_y])|+|E_G(B_y,T_y)|-4|B_y|.
   \]
   Then
   \[
    \delta_{B_y}=19+q-|E(G[T_y])|\ge9+q.              \tag{6}
   \]
   Moreover
   \[
    (J_x,T_y)\text{ is internally six-connected},
    \qquad |E(J_x)|=4|V(J_x)|-5+q.                    \tag{7}
   \]
5. The graph `J_x` contains a spanning exact `K_7^vee` model and hence a
   spanning `K_6` model.  Nevertheless every `K_6` model in `J_x` has at
   most four branch sets meeting `T_y`.                         \(\tag{8}\)

Here a pair `(J,T)` is internally six-connected when there is no
separation `(U,W)` of `J` with `T subseteq U`, `W-U` nonempty, and
`|U cap W|<6`.  A branch set meets `T_y` when it contains a vertex of
`T_y`.

### Proof

The audited
[strict-surplus theorem](hc7_k7minus_strict_surplus_minimal_enemy.md)
makes `G` minimally seven-connected and gives

\[
                         |L|-|F|\ge2.                 \tag{9}
\]

Jakobsen's extremal theorem applies to the seven-connected target-free
graph `G`; none of its four-sum cockade exceptions is seven-connected.
Consequently

\[
                         2|E(G)|\le9|V(G)|-25.
\]

Substituting `|E(G)|=4|V(G)|-2+q` gives

\[
                         |V(G)|\ge21+2q\ge23.         \tag{10}
\]

Equation (9) and `|V(G)|=|L|+|F|` now imply `|L|>=13`.

The audited
[two-clique theorem](hc7_k7minus_two_literal_k5_exclusion.md)
says that a six-connected target-free graph contains at most one literal
`K_5`.  A literal `K_4` in `N_G(x)`, together with `x`, is a literal
`K_5`; conversely, if `x` belongs to the unique literal `K_5`, its other
four vertices form a literal `K_4` in `N_G(x)`.  This proves (3) and item
1.

Fix `x in L-K` and `y in N_G(x)`.  Since `G` is minimally
seven-connected, the audited
[essential-edge theorem](hc7_k7minus_essential_edge_six_separation.md)
makes `G-xy` six-connected.  The six-set `T_y` disconnects `G-xy`, because
it isolates `x`.  Let `C` be the component of `(G-xy)-T_y-x` containing
`y`.  If there were another component `D`, restoring the sole edge `xy`
would join `x` only to `C`, so `T_y` would still separate `D` in `G`,
contrary to seven-connectivity.  Hence `C=B_y` is the only other component.
If a vertex of `T_y` missed either component, deleting the other five
vertices of `T_y` would disconnect `G-xy`, contrary to six-connectivity.
This proves item 2.

Contract `B_y` to one branch set and retain `{x}`.  These two branch sets
are adjacent through `xy` in `G`, and both are adjacent to every vertex of
`T_y`.  A `K_5^-` model in `G[T_y]` would therefore extend to a `K_7^-`
model in `G`.  Hence `G[T_y]` has no `K_5^-` minor.  It has no literal
`K_4` by (3) and the choice of `x`, so Lemma 1 proves (5).

The vertex partition `{x}`, `T_y`, `B_y` has exactly six edges from `x`
to `T_y`, the edge `xy` from `x` to `B_y`, and no other edge between `x`
and `B_y`; the `B_y`--`T_y` edges are included in `\delta_{B_y}`.
Consequently

\[
 \begin{aligned}
 |E(G)|
   &=4|B_y|+\delta_{B_y}+|E(G[T_y])|+7,\\
 |V(G)|&=|B_y|+7.
 \end{aligned}
\]

Comparison with `|E(G)|=4|V(G)|-2+q` gives the equality in (6), and (5)
gives its inequality.  Direct deletion of the degree-seven vertex gives

\[
 |E(J_x)|=|E(G)|-7=4(|V(G)|-1)-5+q.
\]

For completeness, suppose that `(U,W)` were a separation forbidden by the
internal-connectivity assertion in item 4.  In `G-xy`, the set `U cap W`
would separate the nonempty set `W-U subseteq B_y` from the singleton
component `{x}`: the only neighbours of `x` there are the vertices of
`T_y subseteq U`.  Its order is less than six, contradicting the
six-connectivity of `G-xy`.  This proves (7).

Deleting one vertex from the seven-connected graph `G` leaves `J_x`
six-connected.  By (7) and `q>=1`, it has at least `4|V(J_x)|-4` edges.
Its order is at least 22, so the eight-vertex exception in
Norin--Totschnig's Theorem 6 cannot occur.  That theorem gives a `K_7^vee`
model in `J_x`.  Assigning each component outside the model union to an
adjacent branch set makes the model spanning.  In the target-free graph the
two nominally missing adjacencies cannot be created during enlargement, so
the spanning model is exact.  Absorbing its deficient branch set into any
universal branch set gives a spanning `K_6` model.

Finally, if any `K_6` model in `J_x` had five branch sets meeting `T_y`,
the singleton branch set `{x}` would be adjacent to those five bags.  The
seven bags would have at most one missing adjacency and would form a
`K_7^-` model in `G`.  Thus every such model has at most four bags meeting
`T_y`, proving item 5.  \(\square\)

## Proposition 3 (the visible stratum)

Retain the hypotheses of Theorem 2 and let `x in L cap K`.  Put

\[
 Z=K-\{x\},\qquad W=N_G(x)-Z.
\]

For every distinct `p,q in W`,

\[
 d_G(p)+d_G(q)\ge15+q(G)+\mathbf1_{pq\in E(G)}.       \tag{11}
\]

Consequently `W` contains at most one degree-seven vertex, and

\[
 2\sum_{w\in W}(d_G(w)-7)
 \ge3+3q(G)+|E(G[W])|.                               \tag{12}
\]

### Proof

If `y` is the third vertex of `W`, the prescribed cut is
`T_y=Z union {p,q}` and contains the literal clique `Z`.  Theorem 1 of the
audited
[six-cut reserve inequality](hc7_k7minus_six_cut_k4_reserve_inequality.md)
applies directly to this cut.  Indeed, the proof of item 2, which does not
use `x notin K`, shows that `(G-xy)-T_y` has the two full components `{x}`
and a connected component `B_y`.  Put

\[
 t=|E_G(\{p,q\},Z)|,
 \qquad \varepsilon=\mathbf1_{pq\in E(G)}.
\]

The same direct edge partition as in the proof of Theorem 2 gives

\[
 \delta_{\{x\}}+\delta_{B_y}
 =21+q(G)-|E(G[T_y])|
 =15+q(G)-t-\varepsilon.
\]

Summing the two shore bounds now gives

\[
 15+q(G)-t-\varepsilon
 \le |E_G(\{x\}\cup B_y,\{p,q\})|.
\]

The right side is `d_G(p)+d_G(q)-t-2\varepsilon`, which proves (11).
Two degree-seven vertices cannot satisfy it.  Summing (11) over the three
pairs in `W` and rearranging gives (12).  \(\square\)

## Scope and next obligation

Theorem 2 is an unbounded localisation of the entire strict-surplus layer:
at least eight degree-seven vertices each supply seven overlapping
six-boundaries `T_y` in the same graph `J_x`.  Each boundary is sparse,
the connected shore has excess at least `9+q`, and a spanning `K_6` model
already exists.  The obstruction is therefore not existence of an
unrooted clique minor; it is concentration of all seven neighbours of `x`
in at most four branch sets of every `K_6` model.

Proposition 3 also shows why the proposed **canonical vertexwise**
aggregation of the `K_4`-reserve inequality does not cover the strict
majority of degree-seven vertices: the required boundary `K_4` is visible
only at vertices of the unique possible literal `K_5`.  This is a recorded
route nonclosure, not a theorem that every indirect use of the reserve
inequality must fail.

The smallest sufficient next statement is a five-contact model-or-descent
lemma for the seven canonical choices `T_y`: either some `K_6` model in
`J_x` has five bags meeting one `T_y`, or failure returns a canonical
connected shore of smaller order (or a crossing pair of canonical cuts)
with all host labels and coefficient-four density accounting preserved.
The first outcome gives `K_7^-` immediately.  An ordinary unrooted `K_6`
theorem cannot address this obligation, since such a model is already
present.

## External inputs

- I. T. Jakobsen, *On a certain homomorphism properties of graphs II*,
  Mathematica Scandinavica **52** (1983), 229--261,
  doi:`10.7146/math.scand.a-12004`.
- S. Norin and A. Totschnig,
  [*Every graph with no `K_7^vee`-minor is 6-colourable*, Theorem 6](https://arxiv.org/abs/2507.03244).

The other inputs are the adjacent repository results linked in the proof:
the strict-surplus minimum-counterexample theorem, the two-`K_5` theorem,
the essential-edge six-separation theorem, and the six-cut reserve
inequality.
