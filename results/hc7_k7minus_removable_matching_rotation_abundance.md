# Replacement abundance and a four-way common core

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_removable_matching_rotation_abundance_audit.md).  This
note strengthens the seven-removable matching reduction.  It does not prove
the `K_7^-` six-colour conjecture or `HC_7`.

Throughout, `K_7^-` is `K_7` with one edge deleted and `K_7^vee` is `K_7`
with two incident edges deleted.

## 1. Setting

Let `G` be a finite simple graph satisfying

\[
 \chi(G)=7,\qquad
 \chi(J)\leq6\text{ for every proper minor }J\text{ of }G,
 \qquad K_7^-\npreccurlyeq G,                       \tag{1.1}
\]

and

\[
 \kappa(G)\geq7,\qquad \delta(G)\geq8,
 \qquad |E(G)|\geq4|V(G)|,
 \qquad |V(G)|\geq25.                              \tag{1.2}
\]

Fix a matching

\[
                         M=\{e_1,\ldots,e_5\}       \tag{1.3}
\]

such that

\[
                         H=G-M                      \tag{1.4}
\]

is seven-connected.  The audited seven-removable matching theorem supplies
such an `M` under (1.1)--(1.2).

Put

\[
 R=V(G)-V(M),\qquad r=|R|=|V(G)|-10.                \tag{1.5}
\]

For `e_i=u_iv_i`, call an edge

\[
 f\in E\bigl(H[R\cup\{u_i,v_i\}]\bigr)             \tag{1.6}
\]

an **`i`-replacement** if

\[
                    G-\bigl((M-\{e_i\})\cup\{f\}\bigr)
                    \quad\text{is seven-connected}. \tag{1.7}
\]

Condition (1.6) ensures that `(M-{e_i}) union {f}` is again a matching of
order five.  Let `F_i` be the set of all `i`-replacements and put

\[
                         D=\bigcup_{i=1}^5F_i,       \tag{1.8}
\]

where `D` is a set of distinct edges.

## 2. Every coordinate has a feedback set

### Lemma 2.1 (replacement-forest lemma)

For every `i`,

\[
             H[R\cup\{u_i,v_i\}]-F_i
             \quad\text{is a forest}.              \tag{2.1}
\]

#### Proof

Put

\[
                         K_i=H+e_i=G-(M-\{e_i\}).   \tag{2.2}
\]

This graph is seven-connected.  Moreover, no edge of `M-{e_i}` is incident
with a vertex of `R union {u_i,v_i}`.  Hence

\[
                   d_{K_i}(x)=d_G(x)\geq8
                   \quad(x\in R\cup\{u_i,v_i\}).   \tag{2.3}
\]

Suppose that (2.1) contains a cycle `C`.  For every `f in E(C)`, the edge
`f` is not an `i`-replacement, so `K_i-f` is not seven-connected.  Thus
every edge of `C` is critical for seven-connectivity in `K_i`.  Mader's
critical-cycle theorem says that a cycle of critical edges in a
`k`-connected graph contains a vertex of degree `k`.  Applied with `k=7`,
it gives a vertex of `C` of degree seven in `K_i`, contrary to (2.3).
`\square`

## 3. At least twenty distinct replacements

### Theorem 3.1 (replacement abundance)

The number of distinct replacement edges satisfies

\[
                  |D|\geq
                  \left\lceil\frac{3r-5}{2}\right\rceil
                  \geq20.                           \tag{3.1}
\]

Consequently some coordinate `i` has at least four distinct replacements:

\[
                              |F_i|\geq4.            \tag{3.2}
\]

#### Proof

Let

\[
                              J=H-D.                 \tag{3.3}
\]

By Lemma 2.1, `J[R union {u_i,v_i}]` is a forest for every `i`.  In
particular, `J[R]` is a forest.  Let `c` be its number of components.  Then

\[
                              |E(J[R])|=r-c.         \tag{3.4}
\]

Fix `i` and contract each component of `J[R]` to one vertex.  The resulting
graph on those `c` vertices and `u_i,v_i` is still a forest.  The edge
`u_iv_i=e_i` does not belong to `H`.  Therefore

\[
                         |E_J(R,\{u_i,v_i\})|\leq c+1. \tag{3.5}
\]

Summing degrees in `J` over `R` and using (3.4)--(3.5) gives

\[
\begin{aligned}
 \sum_{x\in R}d_J(x)
  &=2|E(J[R])|+\sum_{i=1}^5|E_J(R,\{u_i,v_i\})|\\
  &\leq2(r-c)+5(c+1)\\
  &=2r+3c+5\\
  &\leq5r+5.                                         \tag{3.6}
\end{aligned}
\]

No edge of `M` is incident with `R`, so `d_H(x)=d_G(x)>=8` for every
`x in R`.  Deleting one edge of `D` reduces the degree sum over `R` by at
most two.  Hence

\[
                         8r-2|D|\leq5r+5.            \tag{3.7}
\]

This proves the first inequality in (3.1).  Since `|V(G)|>=25`, we have
`r>=15`, which gives the second.  Finally,

\[
                          \sum_{i=1}^5|F_i|\geq|D|\geq20,
\]

so one `F_i` has order at least four. `\square`

The use of distinct edges in (3.1) is important: the count is not merely a
count of the same replacement edge with several coordinate labels.

## 4. The four-way common core

Choose `i` satisfying (3.2), put

\[
                         M_0=M-\{e_i\},              \tag{4.1}
\]

and choose four distinct edges

\[
                         A=\{a_1,a_2,a_3,a_4\}\subseteq F_i. \tag{4.2}
\]

Each `M_0 union {a}` is a matching of order five.  Define the common core

\[
                         L=G-(M_0\cup A).             \tag{4.3}
\]

The four edges in `A` need not be pairwise disjoint.

### Theorem 4.1 (four-way rotation and exact model)

The graph `L` has all of the following properties.

1. For every `a in A`,

   \[
             L+(A-\{a\})=G-(M_0\cup\{a\})
             \quad\text{is seven-connected}.        \tag{4.4}
   \]

2. `L` is four-connected and

   \[
                         |E(L)|\geq4|V(L)|-8.         \tag{4.5}
   \]

3. `L` has a spanning `K_7^vee`-minor model.  It may be labelled

   \[
                         P,B,C,U_1,U_2,U_3,U_4       \tag{4.6}
   \]

   so that only `PB` and `PC` may be absent.  Under the target-exclusion
   hypothesis in (1.1), both pairs are anticomplete even in `G`; hence
   (4.6) is an exact spanning `K_7^vee` model in `G`.

4. For a proper six-colouring `c` of `L`, define

   \[
      \Sigma_{M_0\cup A}(c)
       =\{xy\in M_0\cup A:c(x)=c(y)\}.               \tag{4.7}
   \]

   The signature family on this one graph contains all `79` sets

   \[
   \begin{split}
      &K &&(\varnothing\ne K\subseteq M_0),\\
      &K\cup\{a\} &&(K\subseteq M_0,\ a\in A).      \tag{4.8}
   \end{split}
   \]

#### Proof

Equation (4.4) is the definition of an `i`-replacement.  Adding one edge
can increase vertex-connectivity by at most one.  Since adding the three
edges `A-{a}` to `L` gives a seven-connected graph, `kappa(L)>=4`.  The
eight deleted edges in `M_0 union A` are distinct, so (1.2) gives (4.5).

Norin--Totschnig's density theorem now gives a `K_7^vee` minor in `L`; its
exceptional graph `K_{2,2,2,2}` is excluded by `|V(L)|=|V(G)|>=25`.
Absorb all unused components into adjacent branch sets to make the model
spanning.  If either nominally missing pair in (4.6) were adjacent in `G`,
the same seven branch sets would form a `K_7^-` model.  Target exclusion
therefore makes both pairs anticomplete in `G`.

It remains to prove (4.8).  Let `K` be a nonempty subset of `M_0`.
Six-colour the proper minor `G/K` and expand the contracted edges.  Every
edge of `K` then has equal-coloured ends.  All edges of
`(M_0-K) union A` remain literal edges after the contractions and are
therefore bichromatic.  Restriction to `L` gives signature exactly `K`.

Now let `K subseteq M_0` be arbitrary and fix `a in A`.  Six-colour
`G/(K union {a})` and expand.  The contracted set is a matching.  Every
other edge of `M_0 union A` remains a literal edge after the contractions,
even when two members of `A` share an end, and is therefore bichromatic.
The resulting colouring of `L` has signature exactly `K union {a}`.
There are `15+4*16=79` distinct displayed signatures. `\square`

### Theorem 4.2 (exact low-cut quotient condition)

Let `S subseteq V(L)`, `|S|<=6`, and suppose that `L-S` is disconnected.
Form a labelled multigraph `Q_S` as follows:

- its vertices are the components of `L-S`;
- an edge `a in A` joins the two component vertices when the ends of `a`
  lie outside `S` in different components;
- an edge of `A` incident with `S`, or with both ends in one component, is
  omitted as it cannot join two components of `L-S`.

Then

\[
                         Q_S-a\text{ is connected}
                         \qquad(a\in A).             \tag{4.9}
\]

In particular, `Q_S` has no bridge and `L-S` has at most four components.
Since `L` is four-connected, such a cut has order four, five or six.

#### Proof

For each `a in A`, the graph `L+(A-{a})` is seven-connected by (4.4).
Deleting `S` therefore leaves it connected.  Contracting the components of
`L-S` gives exactly `Q_S-a`, so (4.9) follows.  A connected bridgeless
multigraph on `q>=2` vertices has at least `q` edges.  Since `Q_S` has at
most four edges, `q<=4`. `\square`

The quotient statement deliberately allows parallel edges and shared
endpoints in `G`.  It does not say that the four alternatives form a
matching, nor does it produce four vertex-disjoint linkage coordinates.

### Corollary 4.3 (five overlapping common cores)

Put

\[
                         A^*=A\cup\{e_i\}.           \tag{4.10}
\]

For every `t in A^*`, the graph

\[
                         L_t=G-\bigl(M_0\cup(A^*-\{t\})\bigr) \tag{4.11}
\]

satisfies Theorems 4.1 and 4.2 with `A^*-{t}` in place of `A`.  Thus there
are five overlapping four-way cores, each with four-connectivity, density
at least `4|V(G)|-8`, an exact spanning `K_7^vee` model, at least `79`
displayed signatures and the quotient condition (4.9).

#### Proof

Every edge `a in A^*` makes `M_0 union {a}` a seven-removable matching:
this is the original matching when `a=e_i`, and follows from the definition
of `F_i` otherwise.  The proof of Theorems 4.1 and 4.2 therefore applies to
each four-element set `A^*-{t}`. `\square`

## 5. A six-coordinate fork

### Theorem 5.1 (six-edge cube or a five-edge star)

Exactly one of the following structural alternatives is forced.

1. Two edges `a,b in A^*` are disjoint.  Then

   \[
                              N=M_0\cup\{a,b\}       \tag{5.1}
   \]

   is a matching of order six, and

   \[
                              X=G-N                 \tag{5.2}
   \]

   is at least six-connected with

   \[
                              |E(X)|\geq4|V(X)|-6.  \tag{5.3}
   \]

   Its exact signature family is the full punctured six-cube:

   \[
      \{\Sigma_N(c):c\text{ is a proper six-colouring of }X\}
                              =2^N-\{\varnothing\}. \tag{5.4}
   \]

   Moreover, `X` has a spanning `K_7^vee` model which is exact even in
   target-free `G`.

2. The five edges in `A^*` form a star.  Its centre is one end of `e_i`,
   and its other four edges are the chosen replacements.

#### Proof

Suppose first that `a,b in A^*` are disjoint.  Both are disjoint from
`M_0`, so `N` is a matching of order six.  The graph
`G-(M_0 union {a})` is seven-connected.  Deleting the further edge `b`
reduces vertex-connectivity by at most one, proving that `X` is
six-connected.  Equation (5.3) follows by deleting the six distinct edges
of `N` from (1.2).

For every nonempty `J subseteq N`, six-colour the proper minor `G/J` and
expand its contracted matching edges.  Exactly the edges in `J` have
equal-coloured ends; every edge of `N-J` remains literal and is
bichromatic.  An empty signature would six-colour `G`.  This proves (5.4).
Norin--Totschnig's theorem applies to the six-connected graph `X` at the
stronger density (5.3).  As in Theorem 4.1, the model can be made spanning,
and target exclusion makes its two nominally missing pairs anticomplete
even after `N` is restored.

It remains to suppose that no two edges of `A^*` are disjoint.  A
pairwise-intersecting family of edges in a simple graph is either a star or
is contained in a triangle: if two edges meet at `v`, an edge avoiding `v`
must join their other ends, after which no fourth distinct edge can meet
all three without containing `v`.  Since `|A^*|=5`, the triangle case is
impossible.  Hence `A^*` is a star.  Because it contains `e_i`, its centre
is one end of `e_i`. `\square`

This fork is the strongest automatic compatibility consequence presently
available.  In the first outcome all six coordinates are genuine matching
coordinates on one six-connected graph.  The second outcome identifies a
single explicit obstruction to that upgrade; it is not a claim that the
star itself is impossible.

## 6. Automaticity and exact scope

The signatures in (4.8) are automatic consequences of proper-minor
six-colourability.  They require no alignment of independently chosen
colourings.  What has been proved is a `79`-member subfamily of the
eight-edge response cube on `M_0 union A`: all nonempty signatures using no
edge of `A`, and all signatures using exactly one edge of `A`.

This is **not** the full punctured eight-cube.  The alternatives in `A` may
share endpoints, and the argument does not realise signatures containing
two or more of them.  Nor does it prove that `chi(G/M)=6` for the original
five-edge matching, or supply a spanning `K_6` model co-bagging all five
original pairs.

Accordingly, this theorem replaces the proposed common co-bagged-`K_6`
split as the immediate proof gate.  That proposed common model is not a
consequence of the audited removable-matching theorem.  What is forced is
stronger and more precise: either the six-connected host in Theorem 5.1
carries a full punctured six-cube and one exact spanning `K_7^vee` model,
or the failure is concentrated in a five-edge star.  Independently, every
case has the five overlapping four-way cores of Corollary 4.3.

The theorem is still nonterminal.  To force `K_7^-`, a further argument
must either terminalise the six-coordinate host or eliminate the star
obstruction by coupling the alternatives to the internal geometry of the
exact models.  A blocked coupling may instead yield one of the cuts in
Theorem 4.2, but that cut still needs enough colouring data to close it.  No
simultaneous linkage choice is asserted here.

## Dependencies and provenance

The existence and response properties of `M` are in the audited
[seven-removable matching reduction](hc7_k7minus_seven_removable_matching_reduction.md).

The critical-cycle input is Wolfgang Mader, *Ecken vom Grad n in minimalen
n-fach zusammenhängenden Graphen*, Archiv der Mathematik **23** (1972),
219--224, Satz 1: a cycle of connectivity-critical edges in a
`k`-connected graph contains a vertex of degree `k`.  The same statement is
restated as Theorem 2.1 in Hojin Chu,
[*A sharp extension of Halin's removable-edge theorem to matchings*](https://arxiv.org/abs/2608.09394).

The density input is Theorem 6 of Sergey Norin and Agnès Totschnig,
[*Every graph with no `K_7^vee` minor is 6-colourable*](https://arxiv.org/abs/2507.03244).
