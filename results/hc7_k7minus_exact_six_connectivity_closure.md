# Exact six-connectivity closes the `4n-2` extremal target

**Status:** written proof; separate internal audit **GREEN** for the exact
file hash recorded in the adjacent audit.  Internal audit is not external
peer review.

Here `K_7^-` denotes the graph obtained from `K_7` by deleting one edge.
All graphs are finite and simple.

This note proves the former primary extremal target:

\[
 \boxed{
 \kappa(G)\ge7,\qquad |E(G)|\ge4|V(G)|-2
 \quad\Longrightarrow\quad K_7^-\preccurlyeq G.}
 \tag{T}
\]

The proof does not require the labelled-separator-shore rank proposed in the
preceding experiment.  A stronger closure occurs one level earlier: a
density-safe contraction of a degree-seven vertex leaves a graph of
connectivity at least six, and the exact connectivity-six layer is itself
impossible at the same density.

As a consequence, the repository's established critical-host entrance proves
that every `K_7^-`-minor-free graph is six-colourable.  This still does **not**
prove `HC_7`, whose forbidden minor is `K_7` rather than `K_7^-`.

---

## 1. Rooted inputs

We use two sharp four-root results in the following forms.

### Rooted `K_4` bound

Let `Q` be a four-set in a graph `F`.  If `(F,Q)` is internally
four-connected and `F` has no `Q`-rooted `K_4` model, then

\[
                         |E(F)|\le3|V(F)|-7.            \tag{1.1}
\]

This is Norin--Totschnig, Lemma 9, derived from the rooted theorem of
Robertson, Seymour and Thomas.

### Rooted diamond theorem

If `(F,Q)` is internally four-connected, `|Q|=4`, and `|V(F)|\ge6`, then
`F` has a `Q`-rooted `K_4^-` model.  This is Jørgensen's theorem in the
form quoted as Norin--Totschnig, Lemma 10.

A pair `(F,Q)` is internally four-connected when no separation `(A,B)` of
`F` with `Q\subseteq A`, `B-A\ne\varnothing`, has order at most three.

---

## 2. The exact connectivity-six theorem

### Theorem 2.1

Let `H` satisfy

\[
                         \kappa(H)=6,
 \qquad |E(H)|\ge4|V(H)|-2.                            \tag{2.1}
\]

Then `H` contains a `K_7^-` minor.

### Proof

Suppose not.  Choose a six-cut `S`, and let

\[
                         C_1,\ldots,C_r                 \tag{2.2}
\]

be the components of `H-S`.  Six-connectivity gives

\[
                         N_H(C_i)=S                     \tag{2.3}
\]

for every `i`: if a component missed one boundary vertex, its neighbourhood
would have order at most five.

Put

\[
 c_i=|C_i|,
 \quad e_i=|E(H[C_i])|,
 \quad p_i=|E_H(C_i,S)|,
 \quad \delta_i=e_i+p_i-4c_i,                          \tag{2.4}
\]

and write

\[
 e_S=|E(H[S])|,
 \qquad q_H=|E(H)|-(4|V(H)|-2)\ge0.                    \tag{2.5}
\]

Exact edge accounting gives

\[
                         q_H=e_S+\sum_{i=1}^r\delta_i-22.
                                                                  \tag{2.6}
\]

We first determine the number of components and the literal graph on `S`.

---

### Claim 2.2: there are two or three components

If `r\ge5`, choose five components and label
`S=\{s_1,\ldots,s_6\}`.  The seven branch sets

\[
 C_1\cup\{s_1\},\ C_2\cup\{s_2\},\
 C_3\cup\{s_3\},\ C_4\cup\{s_4\},\ C_5,\
 \{s_5\},\ \{s_6\}                                   \tag{2.7}
\]

are connected and pairwise adjacent except possibly for the last pair.
Fullness (2.3) supplies every asserted edge.  Thus they form a `K_7^-`
model, a contradiction.  Hence `r\le4`.

Suppose `r=4`.  If three boundary vertices span at least two edges, absorb
the other three boundary vertices into three of the components, retain the
fourth component, and retain the selected three boundary vertices as
singletons.  These seven branch sets have at most one missing adjacency.
Consequently every three-set of `S` spans at most one edge, so `H[S]` is a
matching.

Every boundary vertex has a neighbour in each of the four components and
has total degree at least six.  It therefore has at least two neighbours in
`S`, contradicting that `H[S]` is a matching.  Thus

\[
                              r\in\{2,3\}.              \tag{2.8}
\]

---

### Claim 2.3: the two-component boundary is `K_6-3K_2`

Assume `r=2`.  If a five-set `W\subseteq S` spans at least nine edges,
write `S-W=\{z\}`.  The seven bags

\[
                         C_1\cup\{z\},\quad C_2,
                         \quad (\{w\}:w\in W)           \tag{2.9}
\]

form a `K_7^-` model: the absorbed vertex `z` supplies the edge between
the two component-derived bags, and the five singletons have at most one
missing pair.  Therefore every five-set spans at most eight edges.

There are six five-subsets of `S`, and every boundary edge belongs to four
of them.  Hence

\[
                         4e_S\le6\cdot8,
 \qquad e_S\le12.                                      \tag{2.10}
\]

Each boundary vertex has at least two exterior neighbours and total degree
at least six, so its degree in `H[S]` is at least four.  Thus `e_S\ge12`.
Equality holds, `H[S]` is four-regular, and therefore

\[
                         H[S]\cong K_6-3K_2.            \tag{2.11}
\]

In particular, the three boundary nonedges form a perfect matching.

---

### Claim 2.4: the three-component boundary is cubic

Assume `r=3`.  If a four-set `Q\subseteq S` spans at least five edges,
absorb the other two boundary vertices into two components, retain the
third component, and retain the four vertices of `Q` as singletons.  This
again gives seven branch sets with at most one missing adjacency.  Hence
every four-set spans at most four edges.  Since every boundary edge belongs
to six four-sets,

\[
                         6e_S\le15\cdot4,
 \qquad e_S\le10.                                      \tag{2.12}
\]

At least one component, say `C_1`, is non-singleton.  Otherwise
`|V(H)|=9`, and the eighteen component--boundary edges together with
(2.12) give at most twenty-eight edges, below the required thirty-four.

Suppose some `z\in S` has four boundary neighbours, and choose a four-set
`Q\subseteq N_{H[S]}(z)`.  The pair

\[
                         (H[C_1\cup Q],Q)               \tag{2.13}
\]

is internally four-connected.  Indeed, a rooted separation of order at
most three, enlarged by the two vertices of `S-Q`, would be a cut of `H`
of order at most five.

The graph in (2.13) has at least six vertices, so the rooted diamond
theorem gives a `Q`-rooted `K_4^-` model.  Let `w` be the remaining
boundary vertex.  Its four rooted bags, together with

\[
                         C_2\cup\{w\},\quad C_3,
                         \quad\{z\},                    \tag{2.14}
\]

form a `K_7^-` model.  The literal edges from `z` to all four roots and
fullness of the components supply every adjacency outside the single
possible defect of the rooted diamond.  This is impossible, so

\[
                         \Delta(H[S])\le3.              \tag{2.15}
\]

Every boundary vertex has one neighbour in each component and total degree
at least six.  Its boundary degree is therefore at least three.  Combining
this with (2.15),

\[
                         H[S]\text{ is cubic},
 \qquad e_S=9.                                         \tag{2.16}
\]

---

### Claim 2.5: in the two-component case, every component has excess at most two

Assume `r=2`, and fix one component `C` of order `c`.  Write

\[
 e_C=|E(H[C])|,
 \quad p(s)=|E_H(C,\{s\})|\ (s\in S),
 \quad P=\sum_{s\in S}p(s),
 \quad \delta=e_C+P-4c.                                \tag{2.17}
\]

Let `pq` be one of the three nonedges in (2.11), and put

\[
                         Q=S-\{p,q\}.                   \tag{2.18}
\]

The graph `H[Q]` is a four-cycle and has four edges.  The rooted pair
`(H[C\cup Q],Q)` is internally four-connected: a rooted separator of
order at most three, enlarged by `p,q`, would be a cut of `H` of order at
most five.

This pair has no `Q`-rooted `K_4` model.  Such a model, together with the
other full component and the singleton bags `\{p\},\{q\}`, would be a
`K_7^-` model whose only possible missing adjacency is `pq`.

The rooted `K_4` bound (1.1) therefore gives

\[
 e_C+P-p(p)-p(q)+4\le3(c+4)-7=3c+5.                   \tag{2.19}
\]

Equivalently,

\[
                         p(p)+p(q)\ge c+\delta-1.       \tag{2.20}
\]

Summing (2.20) over the three disjoint nonedges yields

\[
                         P\ge3c+3\delta-3.              \tag{2.21}
\]

Connectedness gives `e_C\ge c-1`, and hence

\[
                         P=4c+\delta-e_C
                           \le3c+\delta+1.              \tag{2.22}
\]

Comparing (2.21) and (2.22) gives

\[
                              \delta\le2.               \tag{2.23}
\]

Both components obey (2.23).  But (2.6) and `e_S=12` require

\[
                         \delta_1+\delta_2=q_H+10\ge10, \tag{2.24}
\]

which is impossible.

---

### Claim 2.6: in the three-component case, every component has excess at most three

Assume `r=3`, and retain the notation (2.17) for one component `C`.
For every **ordered** boundary nonedge `(q,p)`, put

\[
                         Q=S-\{q,p\}.                   \tag{2.25}
\]

As before, `(H[C\cup Q],Q)` is internally four-connected and has no
`Q`-rooted `K_4` model.  To see the latter, let `D,E` be the other two
components.  A rooted `K_4` model would combine with

\[
                         D\cup\{p\},\quad E,
                         \quad\{q\}                     \tag{2.26}
\]

as follows.  The vertex `q` has three neighbours in the cubic boundary,
and `p` is one of its two nonneighbours.  Thus `q` meets three of the four
root bags and can miss only one.  Every other required adjacency follows
from fullness.  The resulting seven bags form a `K_7^-` model.

Applying (1.1) gives

\[
 e_C+P-p(p)-p(q)+|E(H[Q])|\le3c+5.                    \tag{2.27}
\]

A cubic graph on six vertices has twelve ordered nonedges.  On summing
(2.27) over them:

- every boundary vertex occurs four times among the two omitted positions,
  so the total coefficient of `P` is `12-4=8`;
- every boundary edge belongs to exactly four of the four-root sets `Q`,
  so
  \[
               \sum_{(q,p)}|E(H[S-\{q,p\}])|=4e_S=36.
  \]

Consequently

\[
                         12e_C+8P+36\le36c+60,
\]

or

\[
                         3e_C+2P\le9c+6.                \tag{2.28}
\]

Using `e_C\ge c-1`,

\[
 \begin{aligned}
  2\delta
     &=2e_C+2P-8c\\
     &\le(9c+6)-e_C-8c\\
     &\le7.
 \end{aligned}                                         \tag{2.29}
\]

Thus

\[
                              \delta\le3.               \tag{2.30}
\]

All three components obey (2.30).  But (2.6) and `e_S=9` require

\[
                         \delta_1+\delta_2+\delta_3
                            =q_H+13\ge13,               \tag{2.31}
\]

again impossible.

Claims 2.5 and 2.6 eliminate the two alternatives in (2.8), proving
Theorem 2.1. `\square`

---

## 3. The seven-connected `4n-2` theorem

### Theorem 3.1

Every seven-connected graph `G` satisfying

\[
                         |E(G)|\ge4|V(G)|-2             \tag{3.1}
\]

contains a `K_7^-` minor.

### Proof

Suppose not, and choose a counterexample first with minimum order and then
with minimum size.  Put

\[
                         q(G)=|E(G)|-(4|V(G)|-2)\ge0.   \tag{3.2}
\]

The audited
[degree-seven safe-contraction theorem](hc7_k7minus_degree7_safe_contraction.md)
supplies a degree-seven vertex `v` and a neighbour `s` satisfying

\[
                         |N(v)\cap N(s)|\le3.           \tag{3.3}
\]

For completeness, the degree-seven entrance used there is as follows.  If
`q(G)=0`, the average degree is strictly below eight, while minimum degree
is at least seven.  If `q(G)>0`, minimum-size choice makes `G` minimally
seven-connected, and Halin's theorem gives a degree-seven vertex.

Let

\[
                         H=G/vs.                        \tag{3.4}
\]

Contraction removes the edge `vs` and one duplicate edge for each common
neighbour.  Hence

\[
 \begin{aligned}
 q(H)
   &=|E(H)|-(4|V(H)|-2)\\
   &=q(G)+3-|N(v)\cap N(s)|\\
   &\ge q(G)\ge0.                                     \tag{3.5}
 \end{aligned}
\]

The graph `H` is a proper `K_7^-`-minor-free minor of `G`.

We claim

\[
                              \kappa(H)\ge6.             \tag{3.6}
\]

Let `w` be the contracted vertex.  A cut of `H` of order at most five
which avoids `w` lifts unchanged to a cut of `G`.  A cut `X` containing
`w` lifts to

\[
                         (X-\{w\})\cup\{v,s\},          \tag{3.7}
\]

which has order at most six and leaves exactly the same disconnected
remainder.  Both alternatives contradict seven-connectivity of `G`,
proving (3.6).

If `H` were seven-connected, (3.5) would make it a smaller counterexample
to (3.1).  Therefore

\[
                              \kappa(H)=6.               \tag{3.8}
\]

Theorem 2.1 now gives a `K_7^-` minor in `H`, and hence in `G`, the final
contradiction. `\square`

---

## 4. Six-colour consequence

### Corollary 4.1

Every graph with no `K_7^-` minor is six-colourable.

### Proof

Suppose not, and choose a minor-minimal non-six-colourable graph `G` with
no `K_7^-` minor.  Then `G` is seven-contraction-critical and, by Mader's
connectivity theorem, seven-connected.

The audited critical-host results in this repository prove:

1. every degree-seven vertex lies in a literal `K_5`;
2. a six-connected target-free graph contains at most one literal `K_5`;
3. a literal `K_5` cannot have all five vertices of degree seven.

Thus at most four vertices of `G` have degree seven.  Every other vertex
has degree at least eight, and therefore

\[
 \begin{aligned}
  2|E(G)|
    &\ge7n_7+8(|V(G)|-n_7)\\
    &=8|V(G)|-n_7\\
    &\ge8|V(G)|-4.
 \end{aligned}                                         \tag{4.1}
\]

Hence

\[
                         |E(G)|\ge4|V(G)|-2.            \tag{4.2}
\]

Theorem 3.1 gives a `K_7^-` minor, a contradiction. `\square`

The three audited repository inputs used in this last paragraph are:

- [`hc7_k7minus_degree7_clique_incidence.md`](hc7_k7minus_degree7_clique_incidence.md);
- [`hc7_k7minus_two_literal_k5_exclusion.md`](hc7_k7minus_two_literal_k5_exclusion.md);
- [`hc7_k7minus_all_degree7_k5_exclusion.md`](hc7_k7minus_all_degree7_k5_exclusion.md).

---

## 5. Scope and verification

Theorem 3.1 proves the former primary `4n-2` extremal target, and
Corollary 4.1 proves the `K_7^-` six-colour conjecture within the stated
standard and audited inputs.

It does **not** prove Hadwiger's conjecture for `t=7`: a graph may contain a
`K_7^-` minor without containing a `K_7` minor.

The dependency-free finite verifier
[`hc7_k7minus_exact_six_connectivity_verify.py`](hc7_k7minus_exact_six_connectivity_verify.py)
checks all `2^15` labelled graphs on the six-vertex boundary.  It confirms:

- no four-component boundary survives the local degree and triple-edge
  conditions;
- the two-component conditions leave exactly the fifteen labelled copies of
  `K_6-3K_2`;
- there are seventy labelled cubic boundaries in the three-component row;
- all ordered-nonedge incidence coefficients in the sum leading to
  (2.28) are exactly four.

These finite checks support only the explicit boundary arithmetic.  The
rooted-minor and connectivity arguments are proved in the text.

Run:

```bash
python3 results/hc7_k7minus_exact_six_connectivity_verify.py
```

## 6. External inputs

- Sergey Norin and Agnès Totschnig,
  [*Every graph with no `K_7^vee`-minor is 6-colorable*](https://arxiv.org/abs/2507.03244),
  Lemmas 9 and 10.
- W. Mader's theorem that every `k`-contraction-critical graph is
  seven-connected for `k\ge7`.
- R. Halin, *A theorem on n-connected graphs*, Journal of Combinatorial
  Theory **7** (1969), 150--154, as already used in the audited safe-edge
  entrance.
