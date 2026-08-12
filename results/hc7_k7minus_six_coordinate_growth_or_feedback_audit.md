# Internal audit: coordinate growth or bounded feedback set

**Verdict:** GREEN for Theorem 1, Corollary 2, and their stated scope.  This
is a separate internal mathematical audit, not external peer review.

## 1. Exact revision

The audited source is
[`hc7_k7minus_six_coordinate_growth_or_feedback.md`](hc7_k7minus_six_coordinate_growth_or_feedback.md),
with SHA-256

```text
c49b8b736475c9a71410fb9e4a79dad0de862ed6304d2e71b472a07b791c7422
```

The source was promoted from `active/` after the audit; only its status
changed.  Its mathematical content is unchanged.

The result is conditional on the six-coordinate componentwise-induced
forest reduction.  In particular, the host `G` is seven-connected,
seven-chromatic and minor-minimal non-six-colourable, has minimum degree at
least eight and at least `4|V(G)|` edges, and contains no `K_7^-` minor.
The six-edge forest `F` has either six single-edge components or four
single-edge components and one induced three-vertex path.

## 2. Critical-cycle step

Put `X=G-F`, assume that `X` is seven-connected, and put
`R=V(G)-V(F)`.  No deleted forest edge is incident with a vertex of `R`, so

```text
d_X(v)=d_G(v)>=8  for every v in R.
```

If `X[R]` contains a cycle and every edge of that cycle is critical for
seven-connectivity in `X`, Mader's critical-cycle theorem gives a vertex of
degree seven on the cycle.  This contradicts the displayed degree bound.
Consequently some cycle edge `f` leaves `X-f` seven-connected.

The edge `f` is disjoint from `V(F)`.  It therefore forms a new single-edge
component of `F'=F union {f}` and preserves componentwise inducedness.  The
identity `G-F'=X-f` gives the claimed connectivity, while deleting seven
edges from `G` gives the density `4|V(G)|-7`.

## 3. Exact signature cube and model

For every nonempty `J subseteq F'`, the proper minor `G/J` is
six-colourable.  Because `F'` is a forest, every edge of `F'-J` survives
the contractions.  Because every component of `F'` is induced, no edge of
`G-F'` collapses inside a contracted component.  Expanding the colouring
therefore gives signature exactly `J`.  An empty signature would extend to
a six-colouring of `G`.  This proves the full punctured seven-cube without
asserting compatibility between different colourings.

The graph `G-F'` is seven-connected and has strictly more than
`4|V(G)|-8` edges.  Norin--Totschnig, Theorem 6, supplies a `K_7^vee`
model; connectedness permits absorption of unused vertices.  If either
nominally missing branch-set adjacency appeared after restoring `F'`, the
same bags would give a `K_7^-` model.  Target exclusion therefore makes
the spanning model exact in `G`.

## 4. Feedback alternative

If `X[R]` is acyclic, then

```text
G-V(F)=X[R]
```

is a forest.  Thus `V(F)` is a feedback vertex set, of order twelve in the
matching case and eleven in the induced-path case.  Colouring the induced
subgraph on this set and the complementary forest with disjoint palettes
gives

```text
7=chi(G)<=chi(G[V(F)])+2,
```

so the induced subgraph has chromatic number at least five.

## 5. Second iteration

If the first step produces `F'`, the same argument applies to
`G-F'`.  Vertices outside `V(F')` still retain their full degree from `G`,
and a further cycle edge outside `V(F')` becomes a disjoint eighth
single-edge component.  The resulting deletion host is seven-connected,
has at least `4|V(G)|-8` edges and has the full punctured `255`-signature
cube.  Norin--Totschnig applies at equality; the order hypothesis excludes
the exceptional graph `K_{2,2,2,2}`.

If no such cycle exists, `V(F')` is a feedback vertex set.  Its order is
fourteen in the matching case and thirteen in the induced-path case, and
the same disjoint-palette argument gives chromatic number at least five.
If the first iteration had already returned a feedback set, its sharper
bound of at most twelve also satisfies the corollary.

## 6. Trust boundary

The theorem does not eliminate either outcome.  In particular, a full
punctured signature cube does not by itself locate the forest endpoints in
the exact near-clique branch sets or synchronise different colourings.  Nor
does the proof show that a five-chromatic graph on at most fourteen vertices
whose deletion leaves a forest is impossible in the critical host.  These
are the two genuine residual tasks.
