# Independent cold audit: six-boundary fragment rerooting

**Audited source:**
[`hc7_k7minus_six_boundary_fragment_rerooting.md`](hc7_k7minus_six_boundary_fragment_rerooting.md)

**Source SHA-256:**
`53c91cee74ae8b1f5251e13c14095f8abc65f05625eedb401d3d53173996da15`

**Verdict:** **GREEN.**  This is an independent, computation-free cold
audit.  The exact-six linkage, both positions of the omitted derived root,
path endpoint cleanliness, the two excess identities and the stated
minimal-counterexample consequence all check.  The source correctly stops
before a packing-weighted induction: one saturated linkage cannot be used
twice disjointly.

## 1. Six-connectivity and orientation of the derived cut

Completing `S` to a clique does make

```text
F=G[C union S]+E(K_S)
```

six-connected.  If at most five vertices separated a set in `C` from the
surviving clique `S`, the same set could not leave `C` in `G` except through
`S`; the same deletion would therefore disconnect `G`.  Since fewer than
six vertices cannot delete all of `S`, no exceptional case is hidden here.

For an order-six cut `T`, the surviving set `S-T` lies in one component of
`F-T` whenever it is nonempty.  Every other selected component `L` is
contained in `C`.  Six-connectivity forces every vertex of `T` to have a
neighbour in `L`: otherwise `T-{z}` would still separate `L`.  Hence

```text
N_F(L)=T.
```

Writing `Z=T cap S`, `R=T-S`, and `Q=S-T` gives

```text
|R|=6-|Z|=|Q|.
```

In the contraction application, `T` contains both ends of an internal
edge, so `R` is nonempty.  If `R=Q=emptyset` in the general statement, the
linkage is empty and the rerooting assertion is simply the already rooted
model on `S-{t}`; no later inference relies on choosing a distinguished
`S-T` component in that vacuous orientation.

## 2. Saturated `R`--`Q` linkage

Put

```text
H=G[(C-L) union Q]-Z,
k=|R|=|Q|.
```

Suppose there are not `k` disjoint `R`--`Q` paths.  The set form of
Menger's theorem gives a transversal `W` of order less than `k`, with
endpoints allowed in `W`.  Thus both `R-W` and `Q-W` are nonempty.

For an explicit separation check, let `U` be the union of the components
of `H-W` which meet `R-W`.  No vertex of `Q-W` lies in `U`.  Moreover,
after deleting `Z union W`, every surviving neighbour of `L` lies in
`R-W subseteq U`, because `N_F(L)=Z union R`.  The set `L union U` cannot
reach another component of `G-S`: such a route must first meet a surviving
vertex of `S`, and the only candidates are in `Q-W`, which Menger's
separator keeps outside `U`.  Consequently `Z union W` separates the
nonempty set `L union U` from `Q-W` and has order

```text
|Z|+|W| < (6-k)+k=6.
```

This contradicts six-connectivity.  The linkage therefore exists.  Its
`k` disjoint paths use distinct endpoints, and since both endpoint sets
have order `k`, they saturate both `R` and `Q`.

This reformulation also checks the reachability sentence in the source:
allowing `W` to contain endpoints loses neither a surviving initial root
nor a surviving final root.

## 3. Endpoint-clean rerooting

Orient each linkage path from `R` to `Q`, retain the segment after its last
vertex of `R` and stop at its first vertex of `Q`.  The retained paths are
still disjoint.  Saturation ensures that no retained path can contain a
second vertex of `R` or `Q`: that vertex is the endpoint of another
disjoint path.  The paths lie in `C-L` apart from their final vertices in
`Q`, avoid `Z`, and meet `T=Z union R` only at their own initial vertices.
Thus their interiors are disjoint from every old branch set, which lies in
`L union (T-{t})`.

There are exactly two positions for the omitted derived root.

- If `t in R`, enlarge the branch sets rooted at `R-{t}` along their
  corresponding paths.  The unused `t`-path ends at a
  unique `q in Q`.  Disjointness makes every used branch set avoid `q`, and
  the resulting five literal roots are

  ```text
  Z union (Q-{q})=S-{q}.
  ```

- If `t in Z`, every `R`-path is used.  The old model avoids `t` by its
  punctured ambient graph, while all added paths avoid `Z`.  The five new
  roots are

  ```text
  (Z-{t}) union Q=S-{t}.
  ```

In both cases each enlargement is connected, distinct branch sets remain
disjoint, and every old `K_5^-` adjacency remains.  Paths of length one
only add their final `Q` root and require no separate treatment.  All new
vertices lie in `C union (S-{s})`, so the conclusion has the exact
punctured-shore quantifier claimed.  Taking the contrapositive proves the
hereditary exclusion in Corollary 3; it would not be valid if an omitted
root were allowed as an internal old-model vertex, which is why the source
states that hypothesis explicitly.

## 4. Fragment additivity

The equality `N_F(L)=T` involves no artificial edge incident with `L`,
because only pairs inside `S` were added to form `F`.  Thus every actual
edge counted by `eta_S(C)` belongs to exactly one of the following groups:

1. an edge internal to `L`, or an edge from `L` to
   `T=(T cap C) union (T cap S)`;
2. an edge internal to `C-L`, or an edge from `C-L` to `S`.

The first group is exactly the edge contribution to `eta_T(L)` and the
second is exactly the contribution to the bookkeeping expression
`eta_S(C-L)`.  The vertex terms also partition:

```text
-4|C|=-4|L|-4|C-L|.
```

Hence

```text
eta_S(C)=eta_T(L)+eta_S(C-L)
```

without a hidden edge in both summands.  No connectedness of `C-L` is
needed for this identity, as the source correctly notes.

## 5. One-edge contraction

For an internal edge `uv`, simplification after contraction removes

```text
1 + |N_C(u) cap N_C(v)| + |N_S(u) cap N_S(v)|
```

counted edges or boundary incidences.  The contracted component has one
fewer vertex, contributing a gain of four to the coefficient-four term.
Therefore the net change is exactly

```text
eta_S(C/uv)-eta_S(C)=3-lambda(uv).
```

The boundary vertices remain distinct because neither endpoint lies in
`S`.  Replacing the contraction image by the connected edge `uv` lifts a
branch set or an `S`-full connected subgraph.  Only one member of a
disjoint family can contain the contraction image, so disjointness,
connectivity, all model adjacencies and all six literal boundary contacts
lift simultaneously.

## 6. Minimal-counterexample consequence and exact stopping point

If `lambda(uv)<=3`, contraction does not decrease excess.  It also cannot
create a forbidden rooted model or a two-packet family without one lifting
to the original pair.  Thus, in either minimum-order counterexample named
in Section 5, `F/uv` cannot remain six-connected.

Any cut of order at most five in `F/uv` must contain the contraction
vertex; otherwise it would already cut the six-connected graph `F`.
Replacing that vertex by `u,v` gives a cut of order at most six in `F`.
Six-connectivity makes its order exactly six.  This verifies the derived
exact-six separator and the availability of Corollary 3 on every component
oriented away from the surviving original boundary.

The source makes no unjustified packing comparison.  One `T`-full packet
in `L` can absorb the single saturated `R`--`Q` linkage and become
`S`-full.  Two disjoint `T`-full packets would need disjoint copies of that
saturated linkage, which Lemma 1 does not supply.  Hence neither
`mu_T(L)<=mu_S(C)` nor packing-weighted additivity follows.  The stated
two-copy linkage-or-rooted-model lemma is exactly the remaining unsupported
step, and the source correctly records it as open.
