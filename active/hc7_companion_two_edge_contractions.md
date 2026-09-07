# Two edge contractions with controlled degree deficits

**Status:** written proof. The adjacent audit records its separate internal
verdict at an exact source hash. The global conjecture remains open.

All graphs are finite and simple. Put `Q=K_7^=`, the complete graph on
seven vertices with two independent edges deleted. We use Theorem 2 of
[the five-connected helper closure](hc7_five_connected_helper_closure.md),
at SHA-256
`d68986c2c5228b322c8f1c93fff532d4c5f5b49009448a827ea7204fe5016513`.
Its relevant contrapositive is: in a five-connected `Q`-minor-free graph
`J`, a vertex whose neighbourhood contains `K_4^-` has degree at least
`e(J)-4|V(J)|+14`.

## 1. A six-connected class closed for one literal exclusion

**Theorem 1.** Let `F` be six-connected and `Q`-minor-free, with
`delta(F)>=7` and at most five vertices of degree seven. Then `F` and
every simple quotient `F/uv`, for `uv in E(F)`, contain no `K_5^-`
subgraph.

**Proof.** Write `e(F)=4n+q`. The identity
`sum_z(d_F(z)-8)=2q`, together with the degree hypotheses, gives
`2q>=-5`, hence `q>=-2` by integrality.

If `F` contained a `K_5^-`, three of its vertices would each have a
`K_4^-` in their neighbourhood. The helper contrapositive gives degree
at least `q+14` at each. These three vertices contribute at least
`3(q+6)` to the degree-excess sum; all other vertices contribute at least
`-5`. This exceeds `2q`, since `q+13>0`, a contradiction.

Fix an edge `uv`, put `c=|N_F(u) intersect N_F(v)|`, and write

`t=|N_F(u)-N_F[v]|+|N_F(v)-N_F[u]|`.

Thus `d_F(u)+d_F(v)=2c+2+t`. If either endpoint has no private neighbour,
its closed neighbourhood is contained in that of the other endpoint.
The simple contraction is then isomorphic to the graph obtained by
deleting that endpoint, so it cannot create a literal `K_5^-`.
We may therefore assume that both endpoints have a private neighbour,
and hence `t>=2`.

The quotient `J=F/uv` is five-connected: any cut of at most four vertices
lifts to a cut of at most five in `F`, replacing the merged vertex by
`u,v` when necessary. Also `J` is `Q`-minor-free, and

`e(J)-4|V(J)|=q+3-c`.

Suppose `J` contains a literal `K_5^-`. Among its three universal
vertices choose two, `x,y`, different from the merged vertex. Their
neighbourhoods in `J` contain `K_4^-`, so

`d_F(x),d_F(y)>=d_J(x),d_J(y)>=q+17-c`.

The four distinct original vertices `u,v,x,y` therefore contribute at
least `2q+4+t` to `sum_z(d_F(z)-8)`. The other vertices contribute at
least `-5`. Since `t>=2`, the total is at least `2q+1`, contradicting
its exact value `2q`. QED

No condition on adjacency between the degree-seven vertices is needed.
The theorem preserves a literal exclusion in the quotient; it does not
assert that the quotient remains in its six-connected induction class.

## 2. Degree-eight neighbourhoods and a second contraction

**Lemma 2.** If an eight-vertex graph `L` has no `K_4^-` subgraph and
`alpha(L)<=3`, then `Delta(L)<=5`.

**Proof.** The neighbourhood of any vertex induces a matching and
isolated vertices: a two-edge path there would give `K_4^-` together
with that vertex. A vertex of degree seven would therefore have four
independent neighbours, impossible. Suppose `u` has degree six. Its
six neighbours must induce three independent edges, since otherwise
that matching and its isolates have independence number at least four.
Let `w` be the eighth vertex. Every transversal choosing one end of
each of the three edges must contain a neighbour of `w`; otherwise
that transversal together with `w` is independent. Consequently `w`
is adjacent to both ends of one of the three edges. Those ends, `u,w`
span a `K_4^-`, a contradiction. QED

**Corollary 3.** Let `G` be seven-connected and `Q`-minor-free, with
`delta(G)>=8`. Let `v` have degree eight and suppose
`alpha(G[N(v)])<=3`. For every `u in N(v)` and every edge `f` of
`G/vu`, the graph `(G/vu)/f` contains no `K_5^-` subgraph.
The edge `f` may be incident with the merged vertex or disjoint from it.

**Proof.** First `G` contains no literal `K_5^-`. Indeed, put
`q_G=e(G)-4|V(G)|>=0`. Three universal vertices in such a subgraph
would each have degree at least `q_G+14`, contributing
`3(q_G+6)>2q_G` to the degree-excess sum, whose other summands are
nonnegative. Therefore `G[N(v)]` contains no `K_4^-`.

Lemma 2 gives `c=|N_G(u) intersect N_G(v)|<=5`. The graph `F=G/vu`
is six-connected and `Q`-minor-free. Every unmerged vertex has degree
at least seven; only degree-eight common neighbours of `u,v` can become
degree seven, so there are at most five of them. The merged vertex has
degree

`d_G(u)+8-2-c>=9`.

Thus `F` meets Theorem 1, which applies to every choice of its edge `f`.
QED

The neighbourhood independence hypothesis holds in the critical host:
contracting the star from `v` to an independent four-set and six-colouring
that proper minor would give the four original independent vertices one
colour. The other four neighbours use at most four further colours,
leaving a sixth colour for `v`, a contradiction.

Each operation decreases host order by one. A minor in the final quotient
lifts by replacing each used quotient vertex by its fixed connected
preimage. These preimages are disjoint: either two disjoint edges were
contracted, or one connected three-vertex set was contracted. The claim
does not preserve distinct prescribed roots merged by either operation,
nor assert chromatic criticality or minimum degree seven afterward.
Further iteration and the global minor construction remain open.
