# Rooted-`K_4` portal orientation and hereditary descent

**Status:** proved corollary of the independently audited spanning-support
gate and exact-six rerooting theorem.  It eliminates the one-exchanged-root
return and makes the remaining induction obstruction explicit.  It does not
transfer two derived-boundary packets to two original-boundary packets.

Use the notation and hypotheses of the
[spanning rooted-`K_4` support theorem](hc7_k7minus_sparse_sixcut_spanning_rooted_k4_support.md).
Thus `S=Z union {p,q}`, `|Z|=4`, the closed `C`-shore contains a
`Z`-rooted `K_4` model, and no punctured five-rooted `K_5^-` model occurs.

Suppose Lemma 3 of that theorem returns a component `L` and

```text
T=N_G(L)=A union {p,q},       |A|=4,                  (1)
```

where the four portals in `A` occupy at most two of the four rooted model
bags.  Put

```text
k=|T-S|=|A-S|.                                      (2)
```

## Theorem 1 (the one-root exchange is impossible)

We have `2<=k<=4`.  More precisely, `A intersect S` consists of `4-k`
vertices of `Z`, lying in `4-k` distinct rooted model bags.  Consequently:

- if `k=2`, those two boundary portals occupy the two support bags and all
  internal portals lie in their union;
- if `k=3`, the one boundary portal fixes one support bag and every internal
  portal lies in that bag or one other bag; and
- if `k=4`, all four internal portals lie in at most two bags.

### Proof

The vertices `p,q` already belong to both `S` and `T`.  Every other member
of `T intersect S` is a portal, so

```text
T intersect S={p,q} union (A intersect S).
```

Since `|S|=|T|=6`, equations (1)--(2) give

```text
|S-T|=|T-S|=k,       |A intersect S|=4-k.             (3)
```

Every boundary portal belongs to `Z`.  Distinct roots of the rooted
`K_4` model lie in distinct branch bags.  The four portals collectively
occupy at most two bags, and therefore (3) gives `4-k<=2`, or `k>=2`.
The upper bound `k<=4` is immediate from `|A|=4`.  When equality in (3) is
two, the two boundary portals already use both permitted bags, forcing all
internal portals into the same two bags.  The other two descriptions follow
identically.  \(\square\)

## Theorem 2 (the exact return inherits punctured-model exclusion)

For every `t in T`, the graph

```text
G[L union (T-{t})]
```

has no `(T-{t})`-rooted `K_5^-` model.  Moreover,

```text
eta_S(C)=eta_T(L)+eta_S(C-L).                         (4)
```

### Proof

Complete `S` to a clique and call the resulting closed-shore graph `F`.
No added edge has an end in `L`, so (1) also gives `N_F(L)=T`.  Theorem 1
gives `|S-T|=k>=2`; hence `S-T` is nonempty and `L` is a component of
`F-T` remote from it.  Corollary 3 of the exact-six rerooting theorem now
gives the punctured-model exclusion, and Lemma 4 of that theorem gives
(4).  \(\square\)

## Corollary 3 (the exact induction fork)

Consider a minimum-order counterexample to the local dichotomy

```text
eta_U(X)>=6
  => a punctured U-rooted K_5^- model or mu_U(X)>=2,   (5)
```

in a class closed under the exact fragments above.  For every rooted-`K_4`
portal fragment `L`, either

```text
eta_T(L)<=5,                                         (6)
```

or

```text
mu_T(L)>=2.                                          (7)
```

### Proof

The pair `(G[L union T],T)` is internally six-connected: for every
nonempty `X subseteq L`, all neighbours of `X` lie in `L union T`, and
six-connectivity of `G` gives at least six of them.  The fragment is proper,
so minimality applies when `eta_T(L)>=6`.  The rooted outcome in (5) is
excluded by Theorem 2, leaving (7).  Otherwise (6) holds.  \(\square\)

The fork is exact but nonterminal.  A `T`-full packet in `L` can be extended
to the original boundary using the saturated `(T-S)`--`(S-T)` linkage.
Two disjoint `T`-full packets require two disjoint extensions, while
six-connectivity supplies only one saturated linkage.  Theorem 1 shows that
this obstruction starts with at least two exchanged roots and confines all
of their internal portals to two rooted model bags; it does not remove the
two-copy linkage obstruction.

## Pinned dependencies

- spanning-support source SHA-256
  `ce3dca735b31b20e210ec3c88c7a5ab194968f3405ebaabb5664d246489088ab`;
  independent GREEN audit SHA-256
  `a6796939621817414b279ecb6ef8b5a1ab81298e1507acdd7b74e854d34eea94`;
- exact-six rerooting and additivity source SHA-256
  `53c91cee74ae8b1f5251e13c14095f8abc65f05625eedb401d3d53173996da15`.
