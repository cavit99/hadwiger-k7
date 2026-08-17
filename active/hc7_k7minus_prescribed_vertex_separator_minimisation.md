# Minimising a separator whose boundary contains a prescribed vertex

**Status:** computation-free written proof; adjacent independent cold audit
GREEN.  This is an unbounded structural lemma.  It does not force the minimum
boundary to have order seven.

Write `K_7^-` for `K_7` with one edge deleted.

## Theorem 1 (root-preserving minimum-boundary normal form)

Let `G` be a seven-connected graph with no `K_7^-` minor, let `v` be a
vertex of degree eight, and suppose there is a nonempty set `R` such that

```text
G[R] is connected,
v in N_G(R),
V(G)-(R union N_G(R)) is nonempty.                    (1.1)
```

Choose `R` so that `k=|N_G(R)|` is minimum among all sets satisfying
(1.1), and put `S=N_G(R)`.  Let `C_1,...,C_r` be precisely the components
of `G-S` which have a neighbour at `v`.  Then:

1. `1<=r<=4`, and every `C_i` is adjacent to every vertex of `S`;
2. every other component `D` of `G-S` has

   ```text
   7<=|N_G(D)|<=k-1,   N_G(D) subseteq S-{v},         (1.2)
   ```

   and `N_G(D)` is an actual separator;
3. the degree-eight incidence budget is exact:

   ```text
   d_G[S](v) + sum_i |N_G(v) cap C_i| = 8;            (1.3)
   ```

4. putting `q=7-r`, every `q`-vertex set `Q subseteq S` satisfies

   ```text
   |E(G[Q])| <= binom(q,2)-2.                         (1.4)
   ```

In particular, the boundary restrictions in item 4 are

| `r` | restriction on `G[S]` |
|---:|---|
| 4 | every three vertices span at most one edge; equivalently, `Delta(G[S])<=1` |
| 3 | every four vertices span at most four edges |
| 2 | every five vertices span at most eight edges |
| 1 | every six vertices span at most thirteen edges |

### Proof

The set `R` is a component of `G-S`; it is one of the `C_i`, since
`v in S=N_G(R)`.  Thus `r>=1`.  The far-side condition in (1.1) makes
`S` an actual separator, so seven-connectivity also gives `k>=7`.

Let `C` be any component of `G-S` other than `R`.  Its neighbourhood is
contained in `S`, and `R` survives on the far side after `N_G(C)` is
deleted.  Hence `N_G(C)` is an actual separator and seven-connectivity
gives

```text
|N_G(C)|>=7.                                          (1.5)
```

If `v in N_G(C)`, then `C` itself satisfies (1.1).  The choice of `R`
therefore gives `|N_G(C)|>=k`.  Since `N_G(C) subseteq S` and `|S|=k`,
equality holds and `N_G(C)=S`.  This also holds for `C=R` by the definition
of `S`.  Every `C_i` is consequently `S`-full.

If instead `v notin N_G(C)`, then

```text
N_G(C) subseteq S-{v},
```

which, together with (1.5), proves item 2.  These are all the components
of `G-S`.  Counting the neighbours of `v` inside `S` and in the components
which it meets gives (1.3).

Suppose `r>=5`.  Choose five of the full components, six distinct vertices

```text
a_1,a_2,a_3,a_4,z_1,z_2 in S,
```

and use the seven branch sets

```text
C_1 union {a_1}, ..., C_4 union {a_4}, C_5, {z_1}, {z_2}.  (1.6)
```

Every displayed union is connected.  Two component-derived branch sets
are adjacent because each component contacts the other set's boundary
anchor, and each is adjacent to both boundary singletons.  The only
possibly absent pair is `{z_1},{z_2}`.  Thus (1.6) is a `K_7^-`-minor
model, a contradiction.  Hence `r<=4`.

It remains to prove (1.4).  Suppose a set `Q subseteq S` of order
`q=7-r` spans all but at most one of its possible edges.  Since `k>=7`,
there are at least `r-1` distinct vertices

```text
a_1,...,a_{r-1} in S-Q.
```

Now take the seven branch sets

```text
C_i union {a_i}  (1<=i<r),   C_r,   {z}  (z in Q).    (1.7)
```

The same fullness argument makes every pair involving a component-derived
bag adjacent.  Among the singleton bags indexed by `Q`, at most one pair
is nonadjacent.  Hence (1.7) is again a `K_7^-`-minor model.  This
contradiction proves (1.4).  The four displayed specialisations are the
values `q=3,4,5,6`; for `q=3`, the condition that every triple spans at
most one edge is equivalent to maximum degree at most one.  `\square`

## Corollary 2 (the first two excess levels)

Under the hypotheses of Theorem 1:

1. if `k=8`, then either there is an actual order-seven separator
   `S-{v}`, or every component of `G-S` is `S`-full;
2. if `k=9`, then either every component of `G-S` is `S`-full, or there
   is an actual separator contained in `S-{v}` of order seven or eight.

### Proof

Apply (1.2).  At `k=8`, every component not adjacent to `v` has a
neighbourhood of order seven contained in the seven-set `S-{v}`, so that
neighbourhood equals `S-{v}`.  If there is no such component, every
component meets `v` and Theorem 1 makes it full.  The same calculation at
`k=9` leaves orders seven and eight.  `\square`

## Exact limitation

The theorem gives a smaller literal separator whenever a complementary
component does not meet the prescribed vertex.  That smaller separator
need not contain `v`, so it cannot be iterated as a root-preserving descent.
If every component meets `v`, the exact residue is a full interface with at
most four components and the boundary sparsity in (1.4); its order remains
unbounded by this argument.

Nor can connectivity, degree eight, side minimality and fullness alone
bound the rooted separator order.  The explicit family in
[the prescribed-separator order barrier](../barriers/hc7_degree_eight_prescribed_separator_order_barrier.md)
has `kappa(G)=8`, `d(v)=8`, and arbitrarily large minimum rooted boundary,
with every component full.  That family contains a `K_7` minor, so it does
not refute an order bound which makes essential further use of target
exclusion or chromatic criticality.
