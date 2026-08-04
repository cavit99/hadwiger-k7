# Internal audit: singleton-neighbour boundary collapse

**Verdict:** GREEN for the pinned source revision.  This is a separate
internal mathematical audit, not external peer review.

**Audited source:**
`active/hc7_k7minus_e5_singleton_neighbour_boundary_collapse.md`

**SHA-256:**
`32091e0beb5cad0721f2a4ae826bac80b9a5f1c4bbc8e21247ef8b8820f90345`

No mathematical correction is required at this revision.

## 1. Hypotheses and the replacement cut

The leaf-cut classification is applied in precisely its singleton
orientation.  Since the low component is `{q}`, fullness to the exact
five-cut gives

```text
Q=N_G(q),                         x,y notin Q.
```

The lifted cut through `tp` contains `t,p`.  Under
`|S intersect Q|=4`, its fifth vertex is `p in A`, so, writing
`R=S intersect Q`,

```text
Q=R union {p}.
```

The edge `tq` is present because `q in P_t`; hence `t in N_G(q)=Q` and
therefore `t in R`.  Thus the unique root `z in S-R` is not `t`, and

```text
Q^*=(S-{t}) union {p}
```

has exactly five distinct vertices.

## 2. Separation and complementary components

Put `X=A-{p,q}` and `E={x,y,t,q}`.  The asserted absence of edges from
`E` to `X` was checked vertex by vertex:

- `x,y` have neighbourhood exactly `S`;
- the degree-five leaf description gives
  `N_G(t)={x,y,u_t,p,q}`; and
- `N_G(q)=Q=R union {p}`.

The vertices remaining after deleting `Q^*` are exactly `E union X`.
The three edges `xt,yt,tq` make `E` connected, while the preceding
neighbourhood identities leave no edge between `E` and `X`.  Since
`a>=8`, the set `X` is nonempty.  Therefore `Q^*` is indeed a cut and
the components of `G-Q^*` are `E` and the components of `G[X]`.

For completeness, the stronger boundary claim in the source is also
valid.  The crossing identity gives `N_G(X) subseteq S union {p}`, and
`t` has no neighbour in `X`.  Hence every component `C` of `G[X]`
satisfies `N_G(C) subseteq Q^*`.  Its neighbourhood separates `C` from
the surviving set `E`, so five-connectivity yields

```text
5<=|N_G(C)|<=|Q^*|=5.
```

Thus every such component is full to `Q^*`.  No possible edge or
remaining component is omitted from this argument.

## 3. Exact excess calculation

Within `E`, the only edges are `xt,yt,tq`: `xy` is absent and neither
`x` nor `y` has a neighbour in `A`.  Hence `|E(G[E])|=3`.

The incidences with `Q^*` are exactly:

- four from each of `x,y` to the four roots in `S-{t}`;
- `tp` and `tu_t` from `t`; and
- `qp` together with the three edges from `q` to `R-{t}`.

This gives fourteen boundary edges and therefore

```text
delta_{Q^*}(E)=3+14-4(4)=1.
```

There is neither double-counting nor an unlisted possible boundary edge:
the exact neighbourhood descriptions determine all four contributions.

## 4. Descent and dependency check

Lemma 1 of the singleton-contraction theorem applies to every five-cut of
the minimum `E5` enemy and supplies a component of excess at least four.
Applied to `Q^*`, it cannot return `E`, whose excess is one.  It therefore
returns a component `C` of `G[X]`, for which

```text
delta_{Q^*}(C)>=4,                  |C|<=a-2<a.
```

This contradicts the defining minimum-order choice of `(S,A)` and proves
the claimed strict descent.

The dependency revisions checked were:

```text
singleton-contraction theorem:
e4720b2641033396aabf333cc97d9f401df4577f8a6f337a44d7ca6aba0ac1c2

anchored four-root reduction:
b22556c8dc6fa22bbd950d53356c6dc46826e755173ca4a36b3fb5425c0995d8

leaf-cut quotient classification:
cd86151b6526af8be0bfc82f92e1cfb998ca6184d8328f62a4a3829d02a2ef49
```

All three have adjacent hash-pinned GREEN audits.  The universal
five-cut lemma and exact leaf-edge cut theorem precede the present result.
The bound `a>=8` uses only the root-only three-cuts from the earlier
singleton theorem.  The quotient classification derives `Q=N_G(q)` and
the crossing identity without invoking this boundary-collapse result.
There is consequently no circular dependency.

## 5. Scope and unresolved orientations

The result closes only

```text
L={q_t},                         |S intersect Q_{t,p}|=4.
```

The singleton orientation with at most three roots in `Q_{t,p}` remains
open, as do the low singleton `{u_t}` and the two-vertex low component.
The proof establishes descent rather than a rooted minor model and does
not by itself prove `(E5)` or the primary seven-connected theorem.
