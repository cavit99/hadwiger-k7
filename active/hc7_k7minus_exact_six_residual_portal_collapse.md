# The exceptional two-root return collapses to a nonpositive portal pair

**Status:** written unbounded proof; independently cold-audited.  In the
exceptional `(2,0,1)` return, the part outside the derived fragment consists
of the two exchanged vertices alone.  Its exact coefficient-four
contribution is nonpositive, so the return cannot increase excess.

Write `K_7^-` for `K_7` with one edge deleted.  Let `G` be a six-connected
graph with no `K_7^-` minor, let `S` be a six-cut, and suppose that `G-S`
has at least three connected `S`-full components.  Fix one of them, `C`,
and two others, `A,D`.

Complete `S` to a clique in the closed `C`-shore.  Let `T` be an order-six
cut in the completed shore, and let `L` be a component behind `T`, remote
from `S-T`.  Assume the two-root exchange

```text
Z=S intersect T={z_1,z_2,z_3,z_4},
R=T-S={r_1,r_2},
Q=S-T={q_1,q_2}.                                    (1)
```

Thus `N_G(L)=T`.  Suppose that `L` contains two disjoint connected
subgraphs `P_1,P_2`, each adjacent to every vertex of `T`, and that the
exceptional transfer data hold:

```text
mu_S(C-L)=0,                 mu_S(C)=1.              (2)
```

Here `mu_S(X)` is the maximum number of pairwise disjoint connected
subgraphs of `G[X]` adjacent to every vertex of `S`.  These hypotheses are
exactly the residual `(2,0,1)` row of the audited two-packet transfer
theorem.

## 1. No vertex remains outside the fragment and the portals

### Theorem 1 (portal collapse)

```text
C-L=R.                                               (3)
```

### Proof

Put `W=C-(L union R)`.  The audited orientation theorem says that every
component `X` of `G[W]` is adjacent to all four vertices of `Z`.  Thus `X`
is a connected `Z`-carrier in `C`.

The two disjoint subgraphs `P_1,P_2` are also `Z`-carriers, because they
are `T`-full.  They are disjoint from `X`, since they lie in `L` and
`X subseteq W`.  This would give three pairwise disjoint `Z`-carriers in
the component `C` of `G-S`.  The audited four-root carrier-packing theorem
says that every four-set of `S` has carrier packing number at most two.
Therefore `W` is empty, proving (3).  \(\square\)

This use of the carrier bound is target-sensitive: its proof completes
three four-root carriers through the other two full components to a
`K_7^-` model.

## 2. Exact portal restrictions

### Lemma 2 (matching and contact bounds)

After relabelling `Q`, the following statements hold.

1. `r_1q_1,r_2q_2` are edges of `G`.
2. At most one of `r_1q_2,r_2q_1` is an edge.
3. Each portal has at most three neighbours in `Z`.
4. If a portal is adjacent to both vertices of `Q`, then it has at most
   one neighbour in `Z`.
5. If `r_1r_2` is an edge, then

   ```text
   |(N_G(r_1) union N_G(r_2)) intersect Z|<=1.        (4)
   ```

### Proof

The saturated opposite-side linkage gives two disjoint `R`--`Q` paths in

```text
G[(C-L) union Q]-Z.                                  (5)
```

By Theorem 1 this graph has vertex set `R union Q`.  Trimming the paths so
that they meet `R union Q` only at their ends therefore makes both paths
single edges.  They give a perfect matching between `R` and `Q`, proving
statement 1 after relabelling.

If both cross-edges in statement 2 existed, then

```text
P_1 union {r_1},             P_2 union {r_2}
```

would be disjoint connected `S`-full subgraphs of `C`: each `P_i` sees all
of `Z`, and its attached portal would see both vertices of `Q`.  This
contradicts `mu_S(C)=1` in (2).

If some `r_i` saw all four vertices of `Z`, then its singleton would be a
third `Z`-carrier in `C`, disjoint from `P_1,P_2`.  The same four-root
carrier bound proves statement 3.

The terminal-composition lemma from the orientation theorem says that a
connected subgraph of `C-L` which contains a portal, sees both vertices of
`Q`, and sees two vertices of `Z` gives a `K_7^-` minor.  Apply it first to
the singleton `{r_i}`.  A portal adjacent to both vertices of `Q` can
therefore see at most one vertex of `Z`, proving statement 4.  If
`r_1r_2` is an edge, apply it to the connected subgraph induced by
`{r_1,r_2}`.  Statement 1 supplies both `Q`-contacts, so two distinct
vertices in the union of their `Z`-neighbourhoods would again be terminal.
This proves (4).  \(\square\)

## 3. The portal contribution is nonpositive

For a vertex set `X subseteq C`, use the coefficient-four bookkeeping

```text
eta_S(X)=|E(G[X])|+|E_G(X,S)|-4|X|.                 (6)
```

The notation is allowed for a disconnected bookkeeping remainder.

### Theorem 3 (nonpositive portal charge)

```text
eta_S(R)<=0.                                        (7)
```

More precisely:

* if `r_1r_2` is an edge, then `eta_S(R)<=-2`;
* if the portals are nonadjacent and one cross-edge is present, then
  `eta_S(R)<=-1`; and
* equality in (7) is possible only when the portals are nonadjacent, the
  two matching edges are their only edges to `Q`, and each portal has
  exactly three neighbours in `Z`.

### Proof

There are always the two matching incidences from Lemma 2, and statement 2
of that lemma bounds the total number of `R`--`Q` edges by three.

If `r_1r_2` is an edge, (4) allows at most one distinct `Z`-neighbour.
Both portals may see that same vertex, so there are at most two `R`--`Z`
edges.  Hence

```text
eta_S(R)<=1+3+2-8=-2.                               (8)
```

Suppose instead that the portals are nonadjacent.  If there is no
cross-edge, Lemma 2(3) gives at most six `R`--`Z` edges, and therefore

```text
eta_S(R)<=0+2+6-8=0.                                (9)
```

If one cross-edge is present, the incident portal sees both vertices of
`Q` and has at most one `Z`-neighbour by Lemma 2(4).  The other portal has
at most three.  Thus

```text
eta_S(R)<=0+3+(1+3)-8=-1.                           (10)
```

These cases prove (7), and their equality conditions give the last
assertion.  \(\square\)

### Corollary 4 (excess does not increase on return)

With excess on the derived fragment measured against `T`,

```text
eta_S(C)=eta_T(L)+eta_S(R)<=eta_T(L).                (11)
```

### Proof

The exact fragment-additivity theorem gives

```text
eta_S(C)=eta_T(L)+eta_S(C-L).
```

Theorem 1 identifies `C-L` with `R`, and Theorem 3 bounds its contribution
by zero.  \(\square\)

## Consequence and remaining scope

The exceptional two-copy transfer failure has no unbounded open remainder.
It consists only of two matched portal vertices, and the entire return side
has coefficient-four contribution at most zero.  Consequently neither an
arbitrarily dense packet-free complement nor a positive return charge can
be the obstruction in the two-exchanged-root induction.

The equality row is still not declared realisable in a `K_7^-`-minor-free
host.  Nor does (11) by itself prove the packing-weighted bound
`eta_S(C)<=5 mu_S(C)`: the derived fragment has two disjoint `T`-full
subgraphs, so a bound of the form `eta_T(L)<=5 mu_T(L)` permits excess ten.
The remaining target is therefore confined to the equality-or-near-equality
portal pair and the internal structure of `L`; no second-side density is
left uncontrolled.

## Pinned dependencies

* packet-free complement orientation, source SHA-256
  `a6a903ce09c2503edcbdd860123936d2a1d0789eae554bcb11d89da2c4eeeb42`,
  independent GREEN audit SHA-256
  `a7195eeb02deb61dd3f4a312d421ed77cf704d8dba64d5619d51448d6662f604`;
* four-root carrier packing, source SHA-256
  `2d71dcc2110efe7aea44889e8671b0e9289d0ce3b25e95407f35574c37b12a42`,
  independent GREEN audit SHA-256
  `998bbf2e0dcfc5cfeeae48c1e95dde464367be1f5a2c2c9b76964a567cdc33fd`;
* exact-six rerooting, linkage and fragment additivity, source SHA-256
  `53c91cee74ae8b1f5251e13c14095f8abc65f05625eedb401d3d53173996da15`,
  independent GREEN audit SHA-256
  `c30aa69b6919edd2cfba80d6df1f02e2c75d38d9544bd87e4332ba4d823526a3`;
* exact two-packet transfer obstruction, source SHA-256
  `99b59c50f39b43653348997e137d799ff47d8c9e7f402b8dc330e481fd424416`,
  independent GREEN audit SHA-256
  `fd9bb404244c0dc247a9d30480e83bfec356ca2d686a64f23e91cfa5164cfc46`.
