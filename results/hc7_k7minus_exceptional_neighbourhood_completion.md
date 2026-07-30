# Independent triples and exterior completion at an exceptional vertex

**Status:** written proofs, with an independent computational cross-check of
the order-eight input; separate internal audit GREEN for this revision.
They concern a hypothetical counterexample and do not prove the `K_7^-`
six-colour conjecture or `HC_7`.

Let `K_7^-` denote `K_7` with one edge deleted.  Throughout, let `G` be a
finite simple graph satisfying

\[
 \kappa(G)\ge7,
 \qquad \chi(G)=7,
 \qquad \text{every proper minor of `G` is six-colourable},
 \qquad K_7^-\npreccurlyeq G.                              \tag{H}
\]

A degree-eight vertex is **exceptional** if its neighbourhood contains no
literal `K_4`, equivalently if the vertex lies in no literal `K_5`.

## Lemma 1 (the order-eight Ramsey classification)

**Status:** established external input with an independent retained finite
verifier.

If `J` is a graph on eight vertices with no literal `K_4` and
`alpha(J)<=2`, then `J` contains a spanning copy of `C_8^{1,2}`, the square
of an eight-cycle.

This is [Rolek--Song--Thomas, Lemma 2.1](https://arxiv.org/abs/2208.07335),
where their graph `H_8` is the square-antiprism `C_8^{1,2}`.  The verifier
[`hc7_k7minus_exceptional_neighbourhood_completion_verify.py`](hc7_k7minus_exceptional_neighbourhood_completion_verify.py)
enumerates all 12,346 unlabelled graphs of order eight with `geng`, finds
the three graphs satisfying the two hypotheses, and checks a spanning
`C_8^{1,2}` in each.  It separately checks the explicit minor model used
below for every possible missed boundary vertex.

## Theorem 2 (every exceptional neighbourhood has an independent triple)

If `u` is an exceptional vertex of `G`, then

\[
                         \alpha(G[N(u)])=3.               \tag{1}
\]

### Proof

First, `alpha(G[N(u)])<=3`.  Otherwise choose an independent four-set `I`
in `N(u)` and contract the connected star `G[{u}\cup I]`.  Six-colour the
resulting proper minor.  Expanding the contracted vertex gives one colour
to all of `I`; that colour is absent from `N(u)-I`.  Since the latter set
has four vertices, at most five colours occur on `N(u)`, and an absent sixth
colour can be assigned to `u`.  This contradicts `chi(G)=7`.

Suppose instead that `alpha(G[N(u)])<=2`.  Exceptionalness and Lemma 1 give
a spanning `C_8^{1,2}` in `G[N(u)]`.  Label its vertices cyclically
`0,1,...,7`, with indices modulo eight.  The audited minimum-order theorem
for (H) gives `|V(G)|>=19`, so `G-N[u]` is nonempty.  Let `C` be one of its
components.  Since `N_G(C)` separates `C` from `u`, seven-connectivity gives

\[
                N_G(C)\subseteq N(u),\qquad |N_G(C)|\ge7. \tag{2}
\]

Contract `C` to a vertex `c`, delete every other exterior vertex, retain
only the displayed cycle-square edges, and, if necessary, delete one
`c`--`N(u)` edge.  By cyclic symmetry we may suppose that only `c0` is
absent.  The seven branch sets

\[
 \{0,7,2\},\quad \{3\},\quad \{4\},\quad \{1,u\},
 \quad \{6\},\quad \{5\},\quad \{c\}                    \tag{3}
\]

are connected and pairwise adjacent except possibly for `\{3\}` and
`\{6\}`.  They form an explicit `K_7^-`-minor model, a contradiction.
Therefore `alpha(G[N(u)])` is not at most two, and (1) follows.  \(\square\)

## Lemma 3 (exterior-component completion)

Let `u` be a degree-eight vertex in a seven-connected graph, let
`I\subseteq N(u)` have order three, and put `R=N(u)-I`.  Suppose that
`G-({u}\cup I)` contains an `R`-rooted `K_5`-minor model: five pairwise
disjoint connected branch sets `(B_r:r\in R)`, with `r\in B_r`, every two
of which are adjacent.  If these five branch sets avoid some component `C`
of `G-N[u]`, then `G` contains a `K_7^-` minor.

### Proof

The set `A={u}\cup I` is connected and is disjoint from `C` and from all
five rooted branch sets.  As in (2), seven-connectivity implies that `C` is
adjacent to at least seven of the eight vertices of `N(u)`.  Hence `C` sees
at least two vertices of `I`, so it is adjacent to `A`, and it sees at least
four of the five roots in `R`, so it is adjacent to at least four rooted
branch sets.  The set `A` is adjacent to every rooted branch set through
the edges `ur`.  Thus

\[
                         A,\ C,\ (B_r:r\in R)
\]

are seven disjoint connected branch sets with at most one missing
adjacency.  \(\square\)

## Corollary 4 (the exact surviving allocation conditions)

Let `G` satisfy (H), let `u` be exceptional, choose an independent triple
`I\subseteq N(u)`, and put `R=N(u)-I`.  Then:

1. every `R`-rooted `K_5` model in `G-({u}\cup I)` meets every component
   of `G-N[u]`;
2. because an audited theorem gives at most two such components, in the
   two-component case every rooted model is necessarily bilateral; and
3. if `(B_r:r\in R)` is such a model and `D` is a component of
   `(G-N[u])-\bigcup_{r\in R}B_r`, then either `D` has no neighbour in `I`
   or it is adjacent to at most three of the five rooted branch sets.

### Proof

The first two assertions follow from Lemma 3 and `K_7^-\npreccurlyeq G`.
For the third, if `D` had an `I`-neighbour and met at least four rooted
branch sets, then `A={u}\cup I`, `D`, and the five rooted branch sets would
again be a `K_7^-` model.  \(\square\)

## Scope

Theorem 2 removes the independence-number-two neighbourhood branch that
appears in Albar's earlier seven-colour proof and makes an independent
triple available at every exceptional centre.  Lemma 3 turns any rooted
`K_5` model avoiding an exterior component into the desired near-clique
minor.  Neither result constructs such an avoiding model.  In particular,
the one-component case requires a residual connected subgraph adjacent to
the star and at least four rooted bags, while the two-component case
requires a one-shore rooted model or an equivalent residual-contact
argument.
