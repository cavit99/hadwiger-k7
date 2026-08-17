# The exact-defect regular layer is empty

**Status:** active written proof with one deterministic finite lemma and a
separate independent cold audit.  This is a structural theorem inside the
hypothetical critical host.  It does not prove the `K_7^-` six-colour
conjecture or `HC_7`.

## 1. Statement

Let `G` be a minor-minimal non-six-colourable graph with no `K_7^-` minor.
Then

\[
                              |V(G)|\geq26.             \tag{1.1}
\]

Equivalently, the critical host cannot have the degree distribution

\[
                              n_8=25,
              \qquad n_i=0\quad(i\ne8).                \tag{1.2}
\]

The proof gives a little more.  Any connected eight-regular graph in the
purely local setting in which every neighbourhood is the hexagonal
bipyramid is forced to be

\[
                              C_6\vee C_6,              \tag{1.3}
\]

which has order twelve rather than twenty-five.

There is also a mixed-degree consequence.  If `\tau=0` and `n_8=25`, then

\[
                              n_9\geq4,
                    \qquad n_9\equiv0\pmod2.           \tag{1.4}
\]

Thus the first two degree distributions in that layer, `8^{25}` and
`8^{25}9^2`, are both empty.

## 2. Exact defect and local codegree

Suppose for a contradiction that `|V(G)|=25`.  The audited critical-host
package gives

\[
 \delta(G)\geq8,
 \qquad n_8\geq25+\sum_{i\geq10}(i-9)n_i.              \tag{2.1}
\]

There are only twenty-five vertices, so equality forces every vertex to
have degree eight.  Hence

\[
                 |E(G)|=100,
       \qquad D:=9|V(G)|-2|E(G)|=25.                   \tag{2.2}
\]

### Lemma 2.1 (every edge has codegree at least four)

For every edge `xy` of `G`,

\[
                         |N_G(x)\cap N_G(y)|\geq4.     \tag{2.3}
\]

#### Proof

Contract `xy` and put `c=|N_G(x)\cap N_G(y)|`.  The contraction is
six-connected, target-free, and has order twenty-four and `99-c` edges.
It is neither a base graph nor a nontrivial
`(K_{2,2,2,2},K_6,4)`-cockade: the orders exclude the bases and a
nontrivial cockade has a four-cut.  Jakobsen's strict bound therefore gives

\[
                         2(99-c)\leq9\cdot24-25=191.
\]

Thus `2c\geq7`, and integrality gives (2.3). `\square`

Fix `z\in V(G)`, put `X=N_G(z)`, and write `H=G[X]`.  The exceptional-
neighbourhood theorem gives

\[
                         \alpha(H)=3,
              \qquad K_4\not\subseteq H.              \tag{2.4}
\]

For `x\in X`, the degree of `x` in `H` is the codegree of `zx`.
Lemma 2.1 therefore gives

\[
                              \delta(H)\geq4.          \tag{2.5}
\]

## 3. The exterior is connected and boundary-full

### Lemma 3.1 (two exterior components are impossible)

The graph `G-N_G[z]` is connected.

#### Proof

It is nonempty because `G` has twenty-five vertices.  For every component
`C` of `G-N_G[z]`, the set `N_G(C)` lies in `X` and separates `C` from
`z`.  Seven-connectivity gives

\[
                              |N_G(C)|\geq7.           \tag{3.1}
\]

Suppose there are two components.  Contract one connected subgraph from
each to vertices `c_1,c_2`, delete all other exterior vertices, and retain
`H` and `z`.  The vertices `z,c_1,c_2` are pairwise nonadjacent, `z` is
complete to `H`, and each `c_i` is adjacent to at least seven vertices of
`H`.

The finite quotient lemma verified in
[`verify.py`](experiments/defect25_regular_elimination/verify.py) says that
every such quotient contains `K_7^-`.  It exhausts all order-eight graphs
satisfying (2.4)--(2.5), both equal and distinct one-vertex misses, and
hence also the full-attachment supergraphs.  This contradicts the choice
of `G`. `\square`

Write

\[
                         C=G-N_G[z].                  \tag{3.2}
\]

### Lemma 3.2 (the connected exterior is full)

One has `N_G(C)=X`.

#### Proof

By seven-connectivity, `C` misses at most one vertex of `X`.  Suppose it
misses `r`.  Since `G` is eight-regular and `r` has no neighbour in `C`,
the vertex `r` is adjacent to all seven vertices of `X-r`.  Put
`J=H-r`.  Equation (2.5) gives `\delta(J)\geq3`, while the literal `K_4`
exclusion in (2.4) makes `J` triangle-free.

A triangle-free graph of order seven and minimum degree at least three has
an independent set of order four.  Indeed, if some vertex has degree at
least four, its neighbourhood is such a set; if not, every degree is
three, contradicting the handshaking lemma.  Hence `\alpha(H)\geq4`,
contrary to (2.4). `\square`

### Lemma 3.3 (the neighbourhood is the hexagonal bipyramid)

For every `z\in V(G)`,

\[
                         G[N_G(z)]\cong
                         C_6\vee\overline {K_2}.       \tag{3.3}
\]

#### Proof

If `H` had a `K_5` minor, its five branch sets, the singleton `{z}`, and
the connected `X`-full set `C` from Lemmas 3.1--3.2 would be a `K_7^-`
model: only the `zC` adjacency can be absent.  Thus `H` is
`K_5`-minor-free.

The same finite enumeration used for Lemma 3.1 checks all order-eight
graphs satisfying (2.4)--(2.5).  Exactly two atlas-extension
representations are `K_5`-minor-free, and both are isomorphic to the single
unlabelled graph `C_6\vee\overline {K_2}`.  This also agrees with the
separately audited order-eight minimum-degree-four `K_5`-minor-free core
census. `\square`

## 4. Global propagation

For an edge `xy`, write

\[
                         c(xy)=|N_G(x)\cap N_G(y)|.
\]

Call `xy` a **pole edge** when `c(xy)=6` and a **rim edge** when
`c(xy)=4`.  Lemma 3.3 says that every vertex is incident with exactly two
pole edges and six rim edges.  The pole edges therefore form a spanning
two-regular graph `P`.  Its cycles have order at least four, since the two
pole neighbours of a vertex are nonadjacent in the hexagonal bipyramid.

### Lemma 4.1 (rim neighbourhoods are constant on a pole cycle)

If `xy` is a pole edge, then

\[
             N_{G-P}(x)=N_G(x)\cap N_G(y)=N_{G-P}(y),             \tag{4.1}
\]

and this common six-set induces a cycle.

#### Proof

In `G[N_G(x)]\cong C_6\vee\overline {K_2}`, the vertex `y` is one of the
two poles.  Its six neighbours inside `N_G(x)` are exactly the six rim
vertices, and they induce `C_6`.  They are also precisely the common
neighbours of `x,y`.  Applying the same description at `y` gives (4.1).
`\square`

Consequently all vertices in one component `A` of `P` have the same
six-vertex rim-neighbourhood `S_A`.

### Lemma 4.2 (pole cycles occur in joined pairs of order six)

Two components of `P` are either complete or anticomplete to one another
in rim edges.  Every component has one rim-adjacent component, and the two
components both have order six.

#### Proof

There is no rim edge inside one component `A` of `P`.  Otherwise, for
`x,y\in A` with `xy` a rim edge, constancy of the rim-neighbourhood along
`A` would put `y` in both `N_{G-P}(x)` and `N_{G-P}(y)`, the latter being
impossible in a simple graph.

If one rim edge joins components `A,B`, the same constancy first along
`A` and then along `B` makes every vertex of `A` adjacent to every vertex
of `B`.  Thus rim adjacency between pole components is complete or empty.

Every pole component has order at least four.  A vertex has six rim
neighbours, so the orders of all rim-adjacent pole components sum to six.
There can therefore be only one such component, say `B`, and `|B|=6`.
Applying the same argument from a vertex of `B` gives `|A|=6`. `\square`

The union of a paired pair from Lemma 4.2 induces `C_6\vee C_6` and has no
edge to another pair.  Since `G` is connected, it follows that

\[
                              G\cong C_6\vee C_6,
                    \qquad |V(G)|=12,                \tag{4.2}
\]

contrary to `|V(G)|=25`.  This proves (1.1). `\square`

## 5. Extension to the zero-high-excess layer, and its exact limit

Put

\[
        B=\{v:d_G(v)=8\},\qquad
        \tau=\sum_{i\geq10}(i-9)n_i,
        \qquad D=|B|-\tau.                           \tag{5.1}
\]

### Proposition 5.1 (the mixed defect-25 local structure)

If `\tau=0` and `|B|=25`, then every member `z` of `B` has

\[
 G-N_G[z]\text{ connected and }N_G(G-N_G[z])=N_G(z),
 \qquad G[N_G(z)]\cong C_6\vee\overline {K_2}.         \tag{5.2}
\]

#### Proof

Every vertex now has degree eight or nine and `D=25`.  Lemmas 2.1 and 3.1
apply unchanged at a member of `B`.  In Lemma 3.2, a possible missed
boundary vertex cannot have degree nine, because all its neighbours would
lie in the eight-vertex set `N_G[z]`.  If it has degree eight, the original
proof applies.  Lemma 3.3 then gives the displayed neighbourhood. `\square`

For `z\in B`, retain the names **pole edge** and **rim edge** for its two
codegree-six and six codegree-four incident edges.  This label is symmetric
on an edge whose two ends lie in `B`.  Let `P_B` be the graph on `B` formed
by the pole edges with both ends in `B`.

### Lemma 5.2 (no four-centre pole path)

Every component of `P_B` is a path on at most three vertices.  Consequently
at least eighteen pole edges join `B` to `V(G)-B`.

#### Proof

Along a pole edge with both ends in `B`, Lemma 4.1 remains valid.  Hence all
vertices of a pole path in `B` have one common six-vertex rim-neighbourhood,
and that set induces `C_6`.

Suppose four vertices `a_0a_1a_2a_3` occur consecutively on such a path,
and label the common rim cycle `b_0b_1\ldots b_5b_0`.  The seven sets

\[
 \{a_3\},\quad \{a_0,b_0\},\quad \{a_1,b_1\},\quad
 \{a_2,b_2\},\quad \{b_3\},\quad\{b_4\},\quad\{b_5\} \tag{5.3}
\]

are connected and pairwise adjacent except possibly the last and the
other endpoint singleton, `{b_3}` and `{b_5}`.  They form a `K_7^-`
model, a contradiction.  A cycle component of `P_B` has order at least
four, because the two poles at one centre are nonadjacent, and is excluded
by the same argument.  Thus every component is a path of order at most
three.

Every vertex of `B` has pole degree two.  Each path component of `P_B`
therefore sends exactly two pole edges to `V(G)-B`, including a singleton
component.  Since twenty-five vertices require at least nine paths, there
are at least eighteen such edges. `\square`

### Corollary 5.3 (the first mixed distribution is also empty)

Under `\tau=0` and `|B|=25`, the number `n_9` is even and at least four.

#### Proof

Write `a=n_9`.  The degree sum `8\cdot25+9a` is even, so `a` is even.
The case `a=0` is the regular layer already eliminated.  Suppose `a=2`.
The two degree-nine vertices have total degree eighteen.  Lemma 5.2 gives
at least eighteen pole edges from `B` to them, so equality holds
throughout.  In particular:

* `P_B` has exactly nine path components;
* the two degree-nine vertices have no rim edge to `B` and are nonadjacent.

Vertices in one component of `P_B` have the same six rim neighbours.
There is no rim edge inside a component, and rim adjacency between two
components is complete or empty, by the proof of Lemma 4.2.  Since no rim
edge goes to either degree-nine vertex, the component orders adjacent to
any fixed component must sum to six.

Nine positive component orders, each at most three and summing to twenty-five,
have one of the two multisets

```text
3,3,3,3,3,3,3,3,1       or       3,3,3,3,3,3,3,2,2.  (5.4)
```

In the first case, apply the rim-neighbour sum to the singleton component.
It must be rim-adjacent to exactly two order-three components.  Either of
those components then has one rim neighbour in the singleton and must
obtain five more rim neighbours as a union of order-three components,
which is impossible.

In the second case, an order-three component cannot be rim-adjacent to an
order-two component: its adjacent component orders must sum to six, while
`3u+2v=6` has only the possibilities `(u,v)=(2,0)` and `(0,3)`, and there
are only two order-two components in total.  Thus neither order-two
component has a rim edge to an order-three component.  The two order-two
components can supply only two rim neighbours to one another, not six,
again a contradiction.  Hence `a\ne2`, and evenness gives `a\ge4`.
`\square`

The pure two-factor propagation in Section 4 still does **not** extend
through a degree-nine endpoint: that endpoint need not have exactly two
pole edges and six rim edges.  Lemma 5.2 is the target-free replacement,
but it does not eliminate every arrangement of at least four degree-nine
vertices.  In particular, this note does not eliminate the full
`\tau=0` layer.

Nor can the exterior argument simply be repeated at the next defect.
When `D=26`, contraction gives only `c(xy)\geq3`.  The verifier records the
cubic eligible neighbourhood

```text
GMs`KK
```

and two component images missing vertices `3` and `5`; the resulting
eleven-vertex quotient has no `K_7^-` minor.  This is a static route
nonclosure, not a critical-host counterexample, but it falsifies the first
local inference needed to extend Lemma 3.1 from minimum neighbourhood
degree four to three.

Thus the proved broad consequences are exactly:

1. the order-25 critical-host layer is empty;
2. the all-degree-eight exact-defect distribution is empty; and
3. in the `\tau=0`, `|B|=25` layer, all twenty-five exceptional centres
   have the same connected-full hexagonal local structure, at least
   eighteen pole edges leave `B`, and `n_9` is even and at least four.

None is claimed comparable in scope to the Norin--Totschnig colouring
theorem.

## 6. Dependencies and reproducibility

- the audited critical-host density, minimum-degree, exceptional-
  neighbourhood, and literal `K_5` exclusion theorems;
- Jakobsen's sharp `K_7^-` extremal theorem in the form already used in the
  critical-host package;
- the established critical-host lower bound `|V(G)|\geq25`;
- the separately audited
  [order-eight `K_5`-minor-free core census](../results/hc7_order8_full_five_colour_reconfiguration.md),
  used only as a cross-check of Lemma 3.3; and
- the deterministic
  [finite verifier](experiments/defect25_regular_elimination/verify.py),
  which proves both finite assertions used here and records the defect-26
  route nonclosure.
