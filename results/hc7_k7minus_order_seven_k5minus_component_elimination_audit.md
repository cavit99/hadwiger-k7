# Internal audit of the order-seven `K_5^-` component elimination

**Verdict:** **GREEN.**

**Audited theorem:**
[`hc7_k7minus_order_seven_k5minus_component_elimination.md`](hc7_k7minus_order_seven_k5minus_component_elimination.md)

**Audited SHA-256:**
`39fbb29038292795bcdf5eb46ddbb1710efd46a9529b5495e8d9292d94f29517`

The only change from the initially frozen revision was replacing the
pending-audit status line by the link to this GREEN audit; the mathematical
statement and proof are unchanged.

This is a separate internal mathematical audit, not external peer review.

## 1. Statement and degree accounting

The theorem assumes seven-connectivity, minimum degree eight, no literal
`K_5`, an order-seven cut `S`, and distinct components `C,D` of `G-S`,
with `G[C]` isomorphic to `K_5^-`.  If `a,b` are the missing-edge ends,
their internal degrees are three and the other three internal degrees are
four.  Since a component of `G-S` has no neighbour outside `C union S`,
minimum degree gives the displayed boundary lower bounds

```text
5,5,4,4,4
```

and hence at least 22 `C`--`S` edges.

A boundary vertex adjacent to all five vertices of `C` would be adjacent
to either literal `K_4` in `G[C]`, producing a literal `K_5`.  Thus every
boundary vertex has at most four neighbours in `C`.  With seven boundary
vertices and at least 22 incidences, some boundary vertex `t` has exactly
four neighbours in `C`, as claimed.

## 2. Forced Hall matching

The sets `P(a),P(b)` each have order at least five in the seven-set `S`,
so their intersection has order at least three.  Removing `t` leaves an
available common neighbour `s` of `a,b`.

For every nonempty `X subseteq C-{a}`, the open neighbourhood `N_G(X)`
is contained in `C union S`, is disjointly partitioned into its `C` and
`S` parts, and separates `X` from the nonempty component `D`.
Seven-connectivity therefore gives

```text
|N_S(X)| >= 7-|N_C(X)| >= 7-(5-|X|)=|X|+2.
```

Deleting `s,t` leaves at least `|X|` available neighbours.  These are
exactly Hall's inequalities for matching all four vertices of `C-{a}`
into `S-{s,t}`.  Setting `f(a)=s` preserves injectivity because the Hall
matching's codomain omits `s`.

No hidden assumption that `G[S]` has an edge, or that the boundary degrees
equal their lower bounds, is used in this argument.

## 3. Minor model

The five sets `B_v={v,f(v)}` are disjoint and connected.  Core edges give
all pairwise adjacencies except the one corresponding to `ab`; the actual
edge `sb`, with `s=f(a)`, supplies that last adjacency.  Hence these five
sets form a `K_5` model.  The singleton `{t}` is adjacent to the four bags
whose core vertices are neighbours of `t`, so the six displayed bags have
at most one missing adjacency.

Seven-connectivity forces `N_G(D)=S`.  Exactly one boundary vertex `u`
is unused by the five values of `f` and by `t`.  The set `V(D) union {u}`
is connected, disjoint from the six earlier bags, and adjacent to each of
them through the corresponding literal boundary vertex.  Adding it gives
seven connected, pairwise disjoint branch sets with at most one missing
pairwise adjacency.  This is an explicit `K_7^-` minor model.

## 4. Verdict and scope

The proof establishes Theorem 1.1 under exactly its stated hypotheses.
The two-cut application correctly identifies the theorem as a closure of
only the five-vertex `K_5^-` component row.  It does not claim to reduce an
arbitrary two-cut component to that row.

No unresolved assumption or proof gap was found.
