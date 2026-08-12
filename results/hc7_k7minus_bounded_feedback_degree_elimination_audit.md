# Internal audit: degree elimination of the bounded-feedback branch

**Verdict:** **GREEN** for Theorem 1, Corollary 2, and the stated scope.
The theorem excludes every feedback vertex set `T` of order at most
fourteen for which `G[T]` is at least five-chromatic, under exactly the
displayed critical-host degree hypotheses.  The proof is unbounded and
does not use finite enumeration.  Corollary 2 validly composes this
exclusion with the separately audited coordinate-growth theorem.  This is
a separate internal mathematical audit, not external peer review.

## Exact revision

The promoted source is
[`hc7_k7minus_bounded_feedback_degree_elimination.md`](hc7_k7minus_bounded_feedback_degree_elimination.md),
with SHA-256

```text
15c765ab83c396410fab88c57d855f7a594c99f26f7b462a7461bc028fc368f1
```

Theorem 1 was first cold-audited in `active/` at

```text
47829b08b333a7422d0bf671c2ad918d9d699c0f7d419a6790c916de57603953
```

The promoted revision containing the new Corollary 2 was then cold-audited
at

```text
1cfdf9360e17fa36d51d03d5207231ef9871153266154a51ccfd677e89c5c4b2
```

The final hash differs from that second cold-audited revision only in the
status paragraph and adjacent GREEN-audit link.  Promotion before the
corollary had produced the intermediate hash
`0f8177d43f8e7719b850d258032e0fa07c8f897f56187bffe111824adadb70f3`;
it made no mathematical change to Theorem 1.

The strict Mader--Jorgensen bound in (1.2) is not used in the proof.  The
stronger inequality actually used is the degree-defect consequence

\[
                         2|E(G)|\leq9|V(G)|-25,
\]

which follows directly from (1.3).  Thus the unused hypothesis causes no
logical dependence in the argument.

## 1. The five-critical subgraph of the feedback set

Let `J` be induced and vertex-minimal subject to `chi(J)>=5`.  Deleting any
vertex makes it four-colourable, so `chi(J)=5`, `J` is connected and
`delta(J)>=4`.  Since the host has no literal `K_5`, neither does `J`.

The lower bound `|V(J)|>=7` is correct.  On six vertices, the complement
has maximum degree at most one.  With at most one complementary edge the
original graph contains a `K_5`; with at least two, two complementary edges
can be used as two two-vertex colour classes, giving a four-colouring.

For `s=|V(J)|>=8`, degree summation gives `|E(J)|>=2s`.  Equality would
make `J` connected and four-regular.  Brooks' theorem would then give a
four-colouring: neither exceptional case applies, since `J` is not `K_5`
and a four-regular graph is not an odd cycle.  Hence
`|E(J)|>=2s+1`.

For `s=7`, the same argument excludes fourteen edges.  At fifteen edges,
minimum degree four leaves exactly the two degree sequences in (1.7).

- For `(6,4,4,4,4,4,4)`, deleting the universal vertex leaves a cubic
  four-chromatic graph.  A four-chromatic component contradicts Brooks
  unless it is `K_4`; adjoining the universal vertex then gives the
  forbidden literal `K_5`.
- For `(5,5,4,4,4,4,4)`, the complement has degree sequence
  `(1,1,2,2,2,2,2)`.  A graph of maximum degree two with exactly two
  degree-one vertices consists of one path and some cycles.  On seven
  vertices the exhaustive possibilities are precisely
  `P_7`, `P_2 dotcup C_5`, `P_3 dotcup C_4`, and
  `P_4 dotcup C_3`.  Each has a matching of order three.  Those three
  complementary edges and the remaining singleton are four independent
  sets in `J`, again a contradiction.

Therefore `|E(J)|>=16` when `s=7`, and the conclusion `e_T>=16` is valid.

## 2. Degree and forest identities

Because `delta(G)>=8`, the degree classes in (1.9) exhaust `V(G)`.  The
identity

\[
 2|E(G)|=9|V(G)|-n_8+\tau
\]

is exact: every degree-eight vertex contributes one below nine, and a
degree-`i` vertex with `i>=10` contributes `i-9` above nine.  Hypothesis
`n_8>=25+tau` therefore gives (1.9) with the correct inequality direction.

For the forest `R=G-T`, with `r` vertices and `c` components,
`|E(R)|=r-c`.  If

\[
 D_R=\sum_{v\in R}(d_G(v)-8),
\]

then summing degrees over `R` gives exactly

\[
 |E(T,R)|=8r+D_R-2(r-c)=6r+2c+D_R.
\]

Consequently (1.10) is exact.  Combining twice that identity with (1.9)
gives

\[
 5r+2e_T+2c+2D_R\leq9t-25;
\]

dismissing the nonnegative last term gives (1.11).  At least `25-t`
degree-eight vertices lie outside `T`, so `r>=25-t`.  In particular `R`
is nonempty in the displayed range and `c>=1`.

Substitution of `e_T>=16`, `r>=25-t` and `c>=1` into (1.11) gives
`184<=14t`.  Since `t<=14`, this forces `t=14`.  The subsequent range
`11<=r<=13` follows exactly from (1.11).

## 3. Spending the degree-eight vertices in `T`

Let `h` count the vertices of `T` whose degree in `G` is not eight.  With
`t=14`, hypothesis (1.3) gives

\[
 h\leq |V(G)|-n_8\leq r+14-25=r-11,
\]

so (1.14) is correct (and could be sharpened by `tau`).

If a degree-eight vertex `v in T` had at most one neighbour in `T`, it
would have at least seven neighbours in `R`.  Their induced graph is a
forest, not necessarily an independent set; bipartiteness nevertheless
gives an independent four-set.  Contracting the four-edge star centred at
`v`, six-colouring the proper minor, and expanding the independent leaves
uses one colour on those leaves and at most four further colours on the
remaining four neighbours.  A sixth colour is absent from `N_G(v)` and
can be assigned to `v`.  This correctly contradicts `chi(G)=7`.

Now take the degree-eight vertices `Q subseteq T-V(J)`.  At most `h`
vertices of `T-V(J)` fail to have degree eight, so
`|Q|>=14-s-h`.  Each vertex of `Q` has at least two neighbours in `T`.
Every edge of `G[T]` outside `E(J)` is counted at most twice in the sum of
the `T`-degrees over `Q`; no edge internal to `J` is counted.  Hence that
edge set has order at least `|Q|`, proving (1.16).

The two possible core orders then both give `e_T>=23-h`, and (1.14)
strengthens this to `e_T>=34-r`.  Substitution into (1.11), with `t=14`,
gives

\[
                         3r+68+2c\leq101.
\]

But `r>=11` and `c>=1` make the left side at least 103.  This is a genuine
contradiction and completes the exclusion.

## 4. Audit of the forced-growth corollary

Corollary 2 starts with the six-coordinate forest `F` and deletion host
`X=G-F` supplied in the critical host by the separately audited
coordinate-growth theorem, and assumes `X` is seven-connected.  Corollary
2 of that cited theorem has exactly two outcomes:

1. an eight-edge componentwise-induced forest `F_8` whose deletion host is
   seven-connected, has at least `4|V(G)|-8` edges, realises every nonempty
   equality signature on `F_8`, and has a spanning exact `K_7^vee` model;
2. a feedback vertex set `T` with `|T|<=14` and `chi(G[T])>=5`.

The graph is the same hypothetical critical host throughout.  Its audited
degree package supplies every hypothesis of Theorem 1: minimum degree
eight, no literal `K_5`, the strict `5|V(G)|-16` upper edge bound, and
`n_8>=25+tau`.  Theorem 1 therefore excludes outcome 2.  Outcome 1 is
word-for-word the conclusion of the new corollary, including
componentwise inducedness, seven-connectivity, density, the full punctured
eight-signature cube, and exactness of the spanning `K_7^vee` model.

There is no exchange of separately chosen forests or models: Corollary 2
retains the single `F_8` returned by the cited result.  It also correctly
assumes `X` is seven-connected; the corollary makes no claim in the
six-connected case.

## 5. Trust boundary

The audit treats the displayed critical-host package as hypotheses.  In
the repository those inputs are separately audited: minimum degree eight,
absence of a literal `K_5`, and the bound `n_8>=25+tau`.  Brooks' theorem
is the only external theorem used in the proof itself.

The result eliminates the bounded-feedback alternative of the
coordinate-growth theorem and hence forces its eight-coordinate outcome
when `X` is seven-connected.  It does not eliminate that surviving
eight-coordinate exact-model host, the `kappa(X)=6` allocation cases, or
prove the global conjecture by itself.  No unresolved mathematical gap was
found in the audited theorem or corollary.
