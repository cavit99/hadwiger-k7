# Singleton-neighbour boundary collapse at four root contacts

**Status:** active computation-free written proof; see the
[adjacent internal audit](hc7_k7minus_e5_singleton_neighbour_boundary_collapse_audit.md).
This theorem closes one orientation of the exact two-singleton branch of
`(E5)`.  It does not prove `(E5)`.

Let `G` be a minimum `E5` enemy, and use the exact two-singleton setup of
the [anchored four-root reduction](hc7_k7minus_e5_anchored_four_root_reduction.md):

```text
G-S has components A,{x},{y},
N_G(x)=N_G(y)=S,                    xy is not an edge,
G[S]=P_3 disjoint union K_2.
```

The pair `(S,A)` is chosen so that

```text
delta_S(A)>=4
```

and `a=|A|` is minimum among all components with this property behind a
five-cut.  Fix a degree-five leaf root `t`, write

```text
P_t=N_G(t) intersect A={p,q},
N_G(t)={x,y,u_t,p,q},
```

where `u_t` is the unique neighbour of `t` in `G[S]`, and consider the
exact five-cut `Q=Q_{t,p}` through the edge `tp`.

Assume that the low component of `G-Q` is the singleton `{q}`.  The
leaf-cut classification then gives

```text
Q=N_G(q),                           x,y are not in Q.
```

Put `R=S intersect Q`.  This note treats the orientation

```text
|R|=4.                                                     (1)
```

## Theorem (strict high-excess descent)

Under (1), there is a five-cut `Q^*` and a component `C` of `G-Q^*` such
that

```text
C is a subset of A,              |C|<a,
delta_{Q^*}(C)>=4.                                      (2)
```

Consequently the orientation (1) cannot occur in a minimum `E5` enemy.

### Proof

Let `z` be the unique member of `S-R`, put

```text
Z=S-{t},                           Q^*=Z union {p},
X=A-{p,q}.
```

Since `Q` has order five, contains `t,p`, and satisfies (1),

```text
Q=R union {p}.                                             (3)
```

The edge `tq` gives `t in R`, and hence `z` is not `t`.  In particular
`q` has no neighbour in `X`.  The leaf-cut crossing identity
also gives

```text
N_G(X) subseteq S union {p}.
```

The only neighbours of `t` in `A` are `p,q`.  Hence `t` has no neighbour
in `X`, and therefore every component `C` of `G[X]` satisfies

```text
N_G(C) subseteq Q^*.                                      (4)
```

The set `X` is nonempty: the anchored reduction gives `a>=8`.  Define

```text
E={x,y,t,q}.
```

There is no edge from `E` to `X`.  Indeed, `x,y` have no neighbours in
`A`, the vertex `t` has no neighbour in `X`, and (3) together with
`Q=N_G(q)` excludes every `q`--`X` edge.  On the other hand `E` is
connected, since all three edges

```text
xt,                         yt,                         tq
```

are present.  Thus, for every component `C` of `G[X]`, deleting
`N_G(C)` separates `C` from the nonempty connected set `E`.
Five-connectivity and (4) now give

```text
5<=|N_G(C)|<=|Q^*|=5.
```

Consequently

```text
N_G(C)=Q^*                                               (5)
```

for every component `C` of `G[X]`.  It follows that `Q^*` is a five-cut
and that the components of `G-Q^*` are exactly `E` and the components of
`G[X]`.

We next calculate the excess of `E` behind `Q^*`.  Its only internal
edges are `xt,yt,tq`, so

```text
|E(G[E])|=3.                                             (6)
```

The boundary incidences split as follows.

- Each of `x,y` is adjacent to all four vertices of `Z` and not to `p`,
  contributing eight edges.
- The vertex `t` is adjacent in `Q^*` precisely to `p` and `u_t`,
  contributing two edges.
- By (3), the neighbours of `q` in `Q^*` are `p` and the three vertices
  of `R-{t}`, contributing four edges.

Therefore

```text
|E_G(E,Q^*)|=8+2+4=14.                                  (7)
```

Equations (6) and (7) give

```text
delta_{Q^*}(E)=3+14-4(4)=1.                              (8)
```

The universal five-cut excess lemma says that every five-cut of a minimum
`E5` enemy has a component of excess at least four.  Apply it to `Q^*`.
Equation (8) excludes `E`, so some component `C` of `G[X]` satisfies

```text
delta_{Q^*}(C)>=4.
```

Finally,

```text
|C|<=|X|=a-2<a.
```

This proves (2), contrary to the minimum-order choice of `(S,A)`.
\(\square\)

## Scope

The theorem closes exactly the singleton-neighbour orientation

```text
L={q_t},                 |S intersect Q_{t,p}|=4.
```

It does not address the orientations with at most three roots in
`Q_{t,p}`, the singleton low side `{u_t}`, or a two-vertex low component.
No rooted minor model is inferred: the conclusion is the required strict
high-excess descent.

## Dependencies

- [Singleton-contraction uncrossing](hc7_k7minus_e5_singleton_contraction_uncrossing.md),
  Lemma 1 for the universal five-cut excess conclusion and Theorem 7 for
  the exact cut `Q_{t,p}`.
- [Anchored four-root reduction](hc7_k7minus_e5_anchored_four_root_reduction.md),
  for the degree-five leaf description and the bound `a>=8`.
- [Leaf-cut quotient classification](hc7_k7minus_e5_leaf_cut_quotient_nonclosure.md),
  Theorems 3 and 4 for `Q=N_G(q)`, the crossing sets, and the neighbourhood
  inclusion for `X`.
