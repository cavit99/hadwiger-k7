# The two-exchanged-root packet transfer has one exact residual vector

**Status:** proved unbounded transfer trichotomy; independently cold-audited.
In a target-free two-root exchange, the derived-side packet
packing number is at most two.  If it is two, those packets hit every
original-boundary packet and the open remainder contains none.  Thus the
only failure of packet transfer has vector `(2,0,1)`.

Write `K_7^-` for `K_7` with one edge deleted.  Let `G` be a six-connected
graph, let `S` be a six-cut, and suppose that `G-S` has at least three
connected `S`-full components.  Fix one of them, `C`, and choose two others,
`A,D`.

Complete `S` to a clique in the closed `C`-shore and call the resulting
graph `F`.  Let `T` be a cut of order six in `F`, and let `L` be a component
of `F-T` remote from `S-T`.  Assume the two-root exchange

```text
Z=S intersect T={z_1,z_2,z_3,z_4},
R=T-S={r_1,r_2},
Q=S-T={q_1,q_2}.                                    (1)
```

Every edge incident with `L` is an actual edge of `G`, and
`N_G(L)=T`.  A **`T`-packet in `L`** is a connected subgraph of `L`
adjacent to all six vertices of `T`.  An **`S`-packet in `X subseteq C`**
is a connected subgraph of `G[X]` adjacent to every vertex of `S`.  Write
`mu_T(L)`, `mu_S(C)`, and `mu_S(C-L)` for their maximum disjoint packing
numbers; the last value may be zero because `C-L` need not be connected.

## 1. Two derived packets hit every original packet

### Lemma 1 (two packets plus one disjoint transfer are terminal)

Let `P_1,P_2` be disjoint `T`-packets in `L`.  If `E subseteq C` is an
`S`-packet disjoint from `P_1 union P_2`, then `G` contains a `K_7^-`
minor.

### Proof

The four bags

```text
B_1=P_1 union {z_1},       B_2=P_2 union {z_2},
B_3={z_3},                 B_4={z_4}                 (2)
```

are pairwise disjoint and connected.  The first two packets see every
vertex of `Z`.  Hence all six contacts among the four bags in (2) are
present except possibly `B_3B_4`.

Add

```text
B_5=A union {q_1},         B_6=D union {q_2},
B_7=E.                                               (3)
```

These three bags are connected and disjoint from one another and from (2).
They form a clique: `D` has a neighbour at `q_1`, while `E` has neighbours
at both `q_1` and `q_2`.  Each bag in (3) contacts each bag in (2) through
the corresponding literal vertex of `Z`, because `A,D,E` are all
`S`-full.  Thus the seven bags miss at most the pair `B_3B_4` and form a
`K_7^-` model.  \(\square\)

Consequently, in a graph with no `K_7^-` minor, every `S`-packet in `C`
meets `P_1 union P_2`.  In particular,

```text
mu_T(L)>=2  =>  mu_S(C-L)=0.                         (4)
```

This conclusion uses neither a clean portal path nor a rooted-`K_4` model:
the two packets themselves supply the four-rooted `K_4^-` in (2).

## 2. One linkage eliminates a third derived packet

### Lemma 2 (one-packet transfer)

Every `T`-packet `P subseteq L` is contained in an `S`-packet of `C`.
If `P_1,...,P_m` are disjoint `T`-packets, the extension of any selected
`P_i` can be chosen disjoint from all the other `P_j`.

### Proof

The saturated opposite-side linkage theorem gives two vertex-disjoint paths
from `R` to `Q` in

```text
G[(C-L) union Q]-Z,                                  (5)
```

with distinct ends and saturating both `R` and `Q`.  Trim them so that they
meet `R union Q` only at their ends.  From each path delete its final vertex
in `Q`, and add the remaining vertices to `P`.

The resulting subgraph lies in `C` and is connected: `P` has a neighbour
at each initial vertex in `R`.  It sees `Z` through `P`, and it sees each
vertex of `Q` through the last edge of the corresponding path.  It is
therefore an `S`-packet.  The added vertices lie outside `L`, so the
extension is disjoint from every other packet `P_j subseteq L`.  \(\square\)

### Corollary 3 (derived packing cap)

If `G` has no `K_7^-` minor, then

```text
1<=mu_T(L)<=2.                                       (6)
```

### Proof

The connected component `L` itself is a `T`-packet, so the lower bound is
immediate.  If three disjoint packets existed, use two of them as
`P_1,P_2` in Lemma 1.  Lemma 2 extends the third to an `S`-packet disjoint
from both, invoking Lemma 1 and giving a contradiction.  \(\square\)

Thus the generic cap four obtained from punctured-rooted-model exclusion
improves to two in the actual three-lobe, two-root-exchange setting.

## 3. Exact transfer trichotomy

### Theorem 4

If `G` has no `K_7^-` minor, then

```text
1<=mu_T(L)<=2,       1<=mu_S(C)<=2.                  (7)
```

Moreover, either

```text
mu_T(L)<=mu_S(C),                                    (8)
```

or the complete residual data are

```text
(mu_T(L),mu_S(C-L),mu_S(C))=(2,0,1).                (9)
```

In the residual case, every `S`-packet in `C` meets both `L` and `C-L`,
and every pair of candidate one-packet extensions intersects.

### Proof

Corollary 3 gives the first half of (7), and Lemma 2 gives
`mu_S(C)>=1`.

For the upper bound, if `C` contained three disjoint `S`-packets, then
those three packets together with the connected full components `A,D`
would give five disjoint `S`-packets across `G-S`.  Choose four distinct
roots, attach them to four packets, leave the fifth packet unanchored, and
retain the two unused roots as singleton bags.  All pairs contact except
possibly the two singleton roots.  This is a `K_7^-` model.  Hence
`mu_S(C)<=2`.

If (8) fails, the integer bounds in (7) force

```text
mu_T(L)=2,                 mu_S(C)=1.
```

Equation (4) then gives `mu_S(C-L)=0`, proving (9).  Lemma 1 says more:
for any fixed pair of disjoint `T`-packets, their union meets every
`S`-packet in `C`, so every such packet meets `L`.  No `S`-packet can lie
inside `L`, because `N_G(L)=T` and the two vertices of `Q=S-T` have no
neighbour in `L`.  Hence every `S`-packet also meets `C-L`.

Finally, two disjoint one-packet extensions would be two disjoint
`S`-packets, contrary to `mu_S(C)=1`.  This proves the last assertion.
\(\square\)

## 4. Consequence for the rooted-`K_4` portal descent

In the `k=2` portal orientation, the induction fork

```text
eta_T(L)>=6  =>  mu_T(L)>=2
```

now has only two target-free continuations.  Either the two packets transfer
and `mu_S(C)=2`, or the exact residual (9) holds.  In the latter row:

* no component of `C-L` is `S`-full;
* every original packet crosses the exchanged boundary; and
* the obstruction is genuinely simultaneous--each packet transfers alone,
  but no two transfers can be made disjoint.

The clean-path and packet-repaired portal decoders eliminate broad parts of
this residual by constructing the forbidden model in Lemma 1 directly from
one controlled return path.  The theorem above isolates what remains
without assuming that such a clean path exists.

It does not settle the `k=3` or `k=4` portal orientations.  There
`|S intersect T|` is too small for the four rooted bags in (2).  Nor does it
prove that the residual vector (9) occurs in a `K_7^-`-minor-free graph.
Eliminating (9), rather than proving an unrestricted two-copy linkage, is
the exact remaining `k=2` transfer target.

## Pinned dependencies

The only theorem needed in the proof is the saturated opposite-side linkage,
Lemma 1 of
[`hc7_k7minus_six_boundary_fragment_rerooting.md`](hc7_k7minus_six_boundary_fragment_rerooting.md),
source SHA-256
`53c91cee74ae8b1f5251e13c14095f8abc65f05625eedb401d3d53173996da15`,
with independent GREEN audit SHA-256
`c30aa69b6919edd2cfba80d6df1f02e2c75d38d9544bd87e4332ba4d823526a3`.

For comparison, the existing `k=2` decoders are:

* clean portal path completion, source SHA-256
  `dacb0bab3c1811e5c5e8425a22595443ae7216d8a4378d1bcf93e23f5a2acd4a`,
  audit SHA-256
  `7c824a966bfacf91291aedb4566cd4a64bda22d88414599b0d89ce9ad1cf3c42`;
* packet-repaired portal completion, source SHA-256
  `acd033e17c40df8b791eeb9eb07114c0f558abc3654bf30c9030d12604faf55a`,
  audit SHA-256
  `61701ad0f75632907b8934fa3d970593fcf73a313e51b7404d3e9d0b827230ca`.
