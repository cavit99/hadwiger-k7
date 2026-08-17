# Rerooting a five-rooted near-clique across a derived six-cut

**Status:** written unbounded proof, independently audited.  The rerooting
lemma makes five-rooted-`K_5^-` exclusion hereditary on every component
behind a derived order-six separator.  The accompanying identities give
the exact induction bookkeeping for coefficient-four excess.  They do not
prove the remaining packing-weighted excess bound: two disjoint connected
subgraphs adjacent to all six vertices of the derived separator need not
extend disjointly to the original six boundary vertices.

Let `G` be a six-connected graph, let `S` be a six-set, and let `C` be a
component of `G-S` adjacent to every vertex of `S`.  Form

```text
F=G[C union S]+E(K_S),
```

where the last operation completes `S` to a clique.  Thus `F` is
six-connected.  Indeed, a component separated from `S` by at most five
vertices in `F` has the same external neighbourhood in `G`, whilst the
clique on `S` keeps all surviving boundary vertices on one side.

Suppose that `T` is a cut of order six in `F`, and that `L` is a component
of `F-T` not containing `S-T`.  The clique on `S` implies `L subseteq C`.
Six-connectivity gives

```text
N_F(L)=T.                                             (1)
```

Put

```text
Z=T intersect S,   R=T-S,   Q=S-T.
```

Since both `S` and `T` have order six,

```text
|R|=|Q|.                                             (2)
```

All rooted models below use only actual edges of `G`; the added clique
edges defining `F` are used only to locate the separator and orient its
sides.

## Lemma 1 (saturated opposite-side linkage)

There are `|R|` pairwise vertex-disjoint paths from `R` to `Q` in

```text
G[(C-L) union Q]-Z,                                  (3)
```

with distinct initial vertices and distinct final vertices.  In
particular, the paths saturate both `R` and `Q`.

### Proof

Write `k=|R|=|Q|`.  The assertion is empty when `k=0`, so suppose `k>0`.
If the asserted linkage does not exist, the set version of Menger's
theorem gives a set `W` of order less than `k` separating `R` from `Q` in
the graph in (3).  The separator is allowed to contain endpoints; because
`|W|<k`, at least one vertex of each of `R-W` and `Q-W` remains.

In `G-(Z union W)`, take the union of `L` with all vertices reachable from
`R-W` without meeting `Q-W`.  This union is nonempty: by (1), `L` has a
neighbour at every vertex of `R-W`.  It cannot reach `Q-W`, by the choice
of `W`.  Nor can it reach a component of `G-S` other than `C`, since every
edge from such a component to the rest of `G` ends in `S`, and the only
surviving vertices of `S` outside `Z` are in `Q`.

Consequently `Z union W` separates this union from both `Q-W` and every
other component of `G-S`.  But

```text
|Z union W| < (6-k)+k=6,
```

contrary to six-connectivity.  The linkage exists.  Since its two endpoint
sets both have order `k`, it saturates them.  `\square`

## Theorem 2 (punctured five-rooted models reroot to the original boundary)

If `G[L union (T-{t})]` contains a `(T-{t})`-rooted `K_5^-` model for
some `t in T`, then `G[C union (S-{s})]` contains an
`(S-{s})`-rooted `K_5^-` model for some `s in S`.

The punctured-shore hypothesis is essential: it prevents the omitted
boundary vertex `t` from being used internally by an old branch set.

### Proof

Take the linkage of Lemma 1 and regard it as a bijection between `R` and
`Q`.  Truncate each path at its first vertex in `Q` and, if necessary, at
its last vertex in `R`.  The resulting paths still form a saturated
linkage, avoid `L union Z`, and meet `R union Q` only at their own
endpoints.  In particular, distinct paths meet `T` only at their distinct
initial vertices in `R`.  Paths of length one cause no exception to the
argument below.

Start with the five branch sets of the rooted model in
`G[L union (T-{t})]`.
For every selected root `r in R-{t}`, enlarge the branch set containing
`r` along the `r`-path, including its final vertex in `Q`.  The enlarged
branch sets remain connected and pairwise disjoint, and all old branch-set
adjacencies are retained.

If `t in R`, do not use the path beginning at `t`; its final vertex
`q in Q` is the unique omitted original root.  The five enlarged branch
sets are then rooted at

```text
Z union (Q-{q})=S-{q}.
```

They avoid `q`: the unused path is disjoint from every used path, and the
old model lies in `L union (T-{t})`, which is disjoint from `Q`.

If `t in Z`, use all the paths.  The resulting five branch sets are rooted
at

```text
(Z-{t}) union Q=S-{t}.
```

They avoid `t` by the punctured-shore hypothesis, and every added path
lies outside `Z`.

Thus in either case they give the asserted five-rooted `K_5^-` model in
the original closed shore.  `\square`

### Corollary 3 (hereditary exclusion on exact-six fragments)

If `G[C union S]` has no `(S-{s})`-rooted `K_5^-` model for any `s in S`,
where each model is required to lie in `G[C union (S-{s})]`, then
`G[L union (T-{t})]` has no `(T-{t})`-rooted `K_5^-` model for any
`t in T`.

This is the contrapositive of Theorem 2.  Notice that `T` may contain
vertices of `C`; it need not be a subset of the original boundary.

## 4. Exact coefficient-four bookkeeping

For a connected subgraph `X subseteq C` whose external neighbourhood in
`F` is a six-set `U`, define its excess relative to `U` by

```text
eta_U(X)=|E(G[X])|+|E_G(X,U)|-4|X|.                  (4)
```

The edges added inside `S` are not counted in (4).

### Lemma 4 (fragment additivity)

For the component `L` above,

```text
eta_S(C)=eta_T(L)+eta_S(C-L).                        (5)
```

Here the second term is defined by the same edge expression even if it is
being used only as bookkeeping rather than as the excess of an internally
six-connected rooted pair.

### Proof

Every edge incident with `L` either has both ends in `L` or joins `L` to
`T`, by (1).  These are exactly the edge terms in `eta_T(L)`.  Every other
internal or boundary edge counted by `eta_S(C)` is counted by
`eta_S(C-L)`, and the vertex sets partition `C`.  This proves (5).
`\square`

### Lemma 5 (one-edge contraction formula)

Let `uv` be an edge of `G[C]`, and put

```text
lambda(uv)=|N_C(u) intersect N_C(v)|
           +|N_S(u) intersect N_S(v)|.               (6)
```

After contracting `uv`, simplifying parallel edges and keeping all six
boundary vertices distinct,

```text
eta_S(C/uv)=eta_S(C)+3-lambda(uv).                   (7)
```

Moreover, every five-rooted `K_5^-` model and every family of pairwise
vertex-disjoint connected subgraphs adjacent to all of `S` in the
contracted pair lifts to the original pair.

### Proof

The contraction removes one internal edge, one copy for each common
internal neighbour, and one boundary incidence for each common boundary
neighbour.  It also reduces the order by one.  Substitution in (4) gives

```text
(-1-lambda(uv))+4=3-lambda(uv),
```

which is (7).  To lift a connected branch set or full connected subgraph
containing the contracted vertex, replace that vertex by the edge `uv`;
all other sets are unchanged.  Disjointness and every required adjacency
are preserved.  `\square`

## 5. Consequence for a minimal-counterexample induction

Assume a minimum-order counterexample to either

```text
eta_S(C)>=6 => a five-rooted K_5^- model or two disjoint
               connected subgraphs adjacent to every vertex of S,
```

or the stronger packing-weighted inequality.  Lemma 5 shows that every
edge `uv in E(G[C])` with `lambda(uv)<=3` is non-contractible in `F`.
Hence such an edge lies in an order-six cut of `F`: a cut of order at most
five after contraction lifts to a cut of order six containing `u,v`.
Corollary 3 now makes the five-rooted-model exclusion available on every
proper component behind that cut, and Lemma 4 gives exact excess
additivity there.

This removes the former rooted-model stability obstruction from the
separator induction.  One obstruction remains.  A connected subgraph of
`L` adjacent to all of `T` can be extended through Lemma 1 to the original
boundary, but two such subgraphs would require two disjoint saturated
opposite-side linkages.  Lemma 1 supplies only one.  Thus neither

```text
mu_T(L)<=mu_S(C)
```

nor an additive packing inequality follows from the present argument.
The missing step is precisely a two-copy linkage-or-rooted-model lemma at
the derived separator; no finite-order assumption is involved.
