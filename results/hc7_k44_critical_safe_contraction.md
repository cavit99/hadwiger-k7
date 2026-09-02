# Safe contraction in a seven-contraction-critical literal `K_{4,4}` exterior

**Status.** Written unbounded corollary; the adjacent audit identifies the
exact checked revision.  The proof uses the audited singleton-atom theorem,
which contains one computer-assisted finite lemma.  This result does not
iterate after contraction and does not prove the literal case of T44, T44,
Norin--Totschnig Conjecture 21, or `HC_7`.

## 1. Setting

A finite simple graph `G` is **strongly seven-contraction-critical** here if

\[
 \chi(G)=7
 \quad\hbox{and}\quad
 \chi(M)\le 6\text{ for every proper minor }M\text{ of }G.       \tag{1}
\]

Suppose that `G` has no `K_7^-` minor and contains a specified literal
`K_{4,4}` on vertex set `S`; extra edges in `G[S]` are allowed.  Put
`C=G-S`.  For `v in V(C)` and nonempty `Y subseteq V(C)`, define

\[
 L(v)=N_G(v)\cap S,\qquad
 w(Y)=\left|\bigcup_{y\in Y}L(y)\right|,
 \qquad \lambda(Y)=|N_C(Y)|+w(Y).                    \tag{2}
\]

An edge `uv` of `C` is **three-contractible** if simplifying `C/uv` gives a
three-connected graph.  It is **safe** if, after giving the contracted
vertex the label set `L(u) union L(v)`, every inequality

\[
                              \lambda(Y)\ge 7        \tag{3}
\]

continues to hold in the contracted labelled graph.

## 2. Critical safe-contraction theorem

### Theorem 2.1

Let `G` satisfy (1), have no `K_7^-` minor, and contain the specified literal
`K_{4,4}` above.  If

\[
                              |V(C)|\ge 7,            \tag{4}
\]

then `C` contains a safe three-contractible edge.

#### Proof

Mader's theorem makes `G` seven-connected.  In particular, (3) holds for
every nonempty `Y subseteq V(C)`.

Suppose that `C` has no safe three-contractible edge.  Apply the audited
[singleton-atom theorem](hc7_k44_positive_atom_elimination.md).  It gives a
vertex `a in V(C)` such that

\[
             Z=N_G(a),\qquad |Z|=7,                  \tag{5}
\]

and `G[Z]` is bipartite with class orders three and four.  Thus
`d_G(a)=7`, and the class of order four is an independent set in
`G[N_G(a)]`.  Consequently

\[
                         \alpha(G[N_G(a)])\ge 4.     \tag{6}
\]

Dirac's neighbourhood inequality for a seven-contraction-critical graph
gives

\[
             \alpha(G[N_G(a)])
                  \le d_G(a)-7+2=2,                 \tag{7}
\]

contradicting (6).  Hence the required edge exists.  \(\square\)

The degree-seven contradiction is also consistent with the stronger
audited conclusion `delta(G)>=8` in the
[critical-host degree-seven closure](hc7_k7minus_degree7_rooted_helper_closure.md).
The direct proof above isolates the only additional consequence needed here.

## 3. The proper-minor colouring response

### Corollary 3.1

Let `uv` be a safe edge supplied by Theorem 2.1.  The proper minor `G/uv` is
six-colourable.  Equivalently, `G-uv` has a proper six-colouring in which
`u` and `v` receive the same colour.

For every other colour `beta`, the two vertices belong to the same component
of the subgraph induced by their common colour and `beta`; in particular,
that subgraph contains a bichromatic `u`--`v` path.

#### Proof

Strong contraction-criticality gives a colouring of `G/uv` with at most six
colours.  Pulling it back to `G-uv` gives `u` and `v` the colour of the
contracted vertex.  It cannot use at most five colours, since then one
endpoint could be assigned a sixth colour and the edge `uv` restored,
six-colouring `G`.  Thus it uses six colours.

Let their common colour be `alpha`.  If the `alpha`--`beta` component
containing `u` omitted `v`, interchange `alpha` and `beta` on that component.
The resulting colouring of `G-uv` gives `u` and `v` different colours and
therefore extends across `uv`, again six-colouring `G`.  Hence every such
component contains both endpoints.  \(\square\)

## 4. Exact scope and external inputs

Safety refers only to three-connectivity of the labelled exterior and
preservation of (3).  It does not assert that `G/uv` is seven-connected.
Indeed, `G/uv` is six-colourable and is not another instance of (1), so
Theorem 2.1 cannot simply be iterated.  The theorem also says nothing about
exteriors of order at most six or nonliteral `K_{4,4}` models.

The two classical inputs are quoted in the exact forms needed as Theorems
15 and 16 of Sergey Norin and Agnès Totschnig,
[*Every graph with no `K_7^\vee`-minor is 6-colorable*](https://arxiv.org/abs/2507.03244):

- Dirac's 1960 neighbourhood inequality
  `alpha(G[N_G(v)])<=d_G(v)-k+2` for a `k`-contraction-critical graph; and
- Mader's 1967 seven-connectivity theorem for `k`-contraction-critical
  graphs when `k>=7`.
