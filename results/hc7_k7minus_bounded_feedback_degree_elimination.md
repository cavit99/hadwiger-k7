# Degree counting eliminates the bounded-feedback branch

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_bounded_feedback_degree_elimination_audit.md).
This is a
conditional refinement inside a hypothetical critical host.  It does not by
itself prove the `K_7^-` six-colour conjecture or `HC_7`.

## Theorem 1 (no five-chromatic feedback set of order at most fourteen)

Let `G` be a finite simple graph satisfying

\[
 \kappa(G)\geq7,\qquad \chi(G)=7,\qquad
 \chi(M)\leq6\text{ for every proper minor `M` of `G`},
 \qquad K_7^-\npreccurlyeq G,
\tag{1.1}
\]

and suppose that the critical-host conclusions

\[
 \delta(G)\geq8,\qquad K_5\nsubseteq G,
 \qquad |E(G)|\leq5|V(G)|-16                         \tag{1.2}
\]

hold.  For `i\geq8`, let `n_i` be the number of degree-`i` vertices, put

\[
                    \tau=\sum_{i\geq10}(i-9)n_i,
\]

and suppose also that

\[
                            n_8\geq25+\tau.           \tag{1.3}
\]

Then `G` has no feedback vertex set `T` such that

\[
                         |T|\leq14,
                 \qquad \chi(G[T])\geq5.             \tag{1.4}
\]

### Proof

Suppose that `T` satisfies (1.4).  Put

\[
 t=|T|,\qquad R=G-T,\qquad r=|V(R)|,
 \qquad c=\text{the number of components of `R`},
\]

and write `e_T=|E(G[T])|`.  Since `R` is a forest,
`|E(R)|=r-c`.

We first record a sharp edge bound needed for `G[T]`.  Choose an induced
subgraph `J` of `G[T]` minimal subject to having chromatic number at least
five, and put `s=|V(J)|`.  Vertex minimality gives

\[
                       \chi(J)=5,\qquad \delta(J)\geq4. \tag{1.5}
\]

The graph `J` contains no `K_5`.  It follows that `s\geq7`: for `s=5`
this is immediate, while for `s=6` the complement of `J` is a matching.
At most one complementary edge leaves a literal `K_5`, whereas two
complementary edges give a four-colouring by using their ends as two
colour classes.

If `s\geq8`, the degree bound in (1.5) gives `|E(J)|\geq2s`.  Equality
would make `J` a connected four-regular five-chromatic graph, so Brooks'
theorem would force `J=K_5`.  Hence

\[
                         |E(J)|\geq2s+1\qquad(s\geq8). \tag{1.6}
\]

If `s=7`, the same argument excludes `|E(J)|=14`.  If instead
`|E(J)|=15`, its degree sequence is either

\[
                         (6,4,4,4,4,4,4)
              \quad\text{or}\quad (5,5,4,4,4,4,4).  \tag{1.7}
\]

In the first case, deleting the universal vertex leaves a cubic
four-chromatic graph.  Brooks' theorem gives a `K_4` component, which
together with the universal vertex is a `K_5`.  In the second case,
`\overline J` has degree sequence `(1,1,2,2,2,2,2)`.  It is one of

\[
                         P_7,\quad P_2\mathbin{\dot\cup}C_5,
              \quad P_3\mathbin{\dot\cup}C_4,
              \quad P_4\mathbin{\dot\cup}C_3,
\]

and therefore has a matching of order three.  The three corresponding
nonedges of `J`, together with the remaining singleton, four-colour `J`.
Both cases are impossible.  Consequently

\[
                 |E(J)|\geq16\quad(s=7),
              \qquad\text{and in particular}\qquad e_T\geq16. \tag{1.8}
\]

We next count degrees outside `T`.  From (1.3),

\[
\begin{aligned}
 2|E(G)|
   &=8n_8+9n_9+\sum_{i\geq10}i n_i\\
   &=9|V(G)|-n_8+\tau
    \leq9|V(G)|-25.                                  \tag{1.9}
\end{aligned}
\]

Set

\[
                  D_R=\sum_{v\in V(R)}(d_G(v)-8)\geq0.
\]

Degree summation over `R` gives

\[
 |E(T,V(R))|=8r+D_R-2(r-c)=6r+2c+D_R,
\]

and hence the exact identity

\[
                  |E(G)|=e_T+7r+c+D_R.               \tag{1.10}
\]

Combining (1.9) and (1.10), and discarding `2D_R`, yields

\[
                         5r+2e_T+2c\leq9t-25.         \tag{1.11}
\]

At least `25-t` of the degree-eight vertices lie outside `T`, so

\[
                              r\geq25-t.              \tag{1.12}
\]

In particular `R` is nonempty and `c\geq1`.  Using (1.8) and (1.12) in
(1.11) gives

\[
             5(25-t)+32+2\leq9t-25,
\]

so `t\geq14`.  Thus `t=14`, and (1.11) first gives the finite residue

\[
                         11\leq r\leq13,
                    \qquad 25\leq |V(G)|\leq27.       \tag{1.13}
\]

It remains to use the degree-eight vertices of `T`.  Let `h` be the
number of vertices of `T` whose degree in `G` is not eight.  From
`n_8\geq25` and (1.13),

\[
                       h\leq |V(G)|-n_8\leq r-11.     \tag{1.14}
\]

Every degree-eight vertex `v` in `T` has at least two neighbours in `T`.
Indeed, otherwise `v` has at least seven neighbours in the forest `R`.
Those neighbours induce a forest and hence contain an independent set of
order four.  Contracting the star from `v` to such a four-set and
six-colouring the resulting proper minor gives a six-colouring of `G`:
after expansion the four independent vertices receive the contracted
colour, at most four further colours occur on the other four neighbours
of `v`, and a missing sixth colour is available for `v`.  This contradicts
(1.1).

Let `Q` be the set of degree-eight vertices in `T-V(J)`.  Then

\[
                              |Q|\geq14-s-h.           \tag{1.15}
\]

The sum of the degrees in `G[T]` of the vertices in `Q` is at least
`2|Q|`.  Every edge of `G[T]` not internal to `J` is counted at most twice
in this sum.  Therefore

\[
                         e_T\geq |E(J)|+|Q|.           \tag{1.16}
\]

If `s=7`, equations (1.8), (1.15), and (1.16) give
`e_T\geq23-h`.  If `s\geq8`, equations (1.6), (1.15), and (1.16) give

\[
                    e_T\geq2s+1+14-s-h
                         =s+15-h\geq23-h.
\]

Thus in all cases, by (1.14),

\[
                              e_T\geq34-r.             \tag{1.17}
\]

Finally, substitute `t=14` and (1.17) into (1.11).  This gives

\[
                        3r+68+2c\leq101.               \tag{1.18}
\]

But `r\geq11` and `c\geq1`, so the left side of (1.18) is at least
`103`.  This contradiction proves the theorem. `\square`

## Corollary 2 (forced eight-coordinate growth)

Let `F` and `X=G-F` be the six-coordinate induced forest and its deletion
host from the audited
[coordinate-growth theorem](hc7_k7minus_six_coordinate_growth_or_feedback.md).
If `X` is seven-connected, then there is an eight-edge componentwise-induced
forest `F_8` such that

\[
 G-F_8\text{ is seven-connected},\qquad
 |E(G-F_8)|\geq4|V(G)|-8,
\]

the exact signature language of `G-F_8` is
`2^{F_8}-\{\varnothing\}`, and `G-F_8` has a spanning exact
`K_7^\vee`-minor model.

### Proof

Corollary 2 of the coordinate-growth theorem returns either precisely this
eight-coordinate outcome or a feedback vertex set `T` with
`|T|\leq14` and `chi(G[T])\geq5`.  The latter alternative is excluded by
Theorem 1. `\square`

## Density note and scope

The strict bound in (1.2) is the available host bound.  Mader's exact
extremal theorem first gives `|E(G)|\leq5|V(G)|-15`.  In Jørgensen's
equality classification, `K_{2,2,2,3}` has connectivity six, a nontrivial
five-clique sum has a separator of order five, and a single two-apex
summand is six-colourable by the Four Colour Theorem and two fresh colours.
Thus equality is impossible in the host (1.1).  The proof above records
this input for completeness but does not need it: the degree-defect
consequence (1.9) of (1.3) is stronger for the feedback-set count.

Thus the feedback-set outcome of the audited coordinate-growth theorem is
empty once the full audited critical-host degree package is retained.  The
argument is unbounded and purely structural; no finite enumeration is
used.  Corollary 2 does not eliminate the surviving eight-coordinate
exact-model host.
