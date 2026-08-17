# Independent cold audit: one-exchange four-portal reduction

**Verdict:** **GREEN** for Theorem 1 at the hash-pinned revision below.
The theorem is an unbounded reduction, but it is not a completion of the
one-exchanged-root case.  The maximal four-portal augmentation statement is
explicitly **OPEN** and was not used as a proved input in this audit.  This is
an independent internal mathematical audit, not external peer review.

## Audited revision

The audited source is
[`hc7_k7minus_sparse_sixcut_one_exchange_four_portal_gate.md`](hc7_k7minus_sparse_sixcut_one_exchange_four_portal_gate.md)
at SHA-256

```text
e7c01f5a89fa848c6af20e2774227bf6c4df0b083ac41b132dddbafa9ea4abde
```

The current source SHA-256 is
`658cf55a8fa7e438a40d76b3c4655c25981ecc655d7b1127631045c0f9384919`.
The only later change records this GREEN audit in the status paragraph; no
hypothesis, conclusion, proof step, open statement, or scope claim changed.

Its sole imported theorem is the exact-six rerooting result, pinned in the
source at the matching SHA-256

```text
53c91cee74ae8b1f5251e13c14095f8abc65f05625eedb401d3d53173996da15
  active/hc7_k7minus_six_boundary_fragment_rerooting.md
```

Only the setup and notation of that result are needed for Theorem 1.  The
later paragraph about `K_{2,n}` contractibility explains why one natural
attempt does not finish the proof; it is not used to derive the theorem.

## 1. Construction of the two adjacent full subgraphs

The two supplied connected subgraphs `P_1,P_2` lie in the connected graph
`G[L]`.  A shortest `P_1`--`P_2` path has no internal vertex in either
subgraph.  Absorbing its internal vertices into `P_1` therefore produces
disjoint connected subgraphs `A,B` joined by the final path edge.  Both keep
all six of their original contacts with

```text
T=Z union {r}.
```

Thus item 1 of Theorem 1 does not require an unstated disjoint-path or fan
assumption.

## 2. Connectivity and ownership of the remainder

Because `N_F(L)=T` and the only edges added in `F` have both ends in `S`,

```text
N_G(L) intersect C={r}.
```

Put `D=C-L`.  The vertex `r` belongs to `D`.  If a component of `G[D]`
did not contain `r`, connectedness of `G[C]` would force it to have an edge
to `L`; its endpoint in `D` would then be a second member of
`N_G(L) intersect C`.  Hence `D` is connected.

The original component `C` has a neighbour at `q`, while `L` has none
because `q` is not in `T=N_F(L)`.  Therefore `D` is nonempty, contains `r`,
and has a neighbour at `q`.  It is disjoint from `A union B`, so the
component `W` of `G[C-(A union B)]` containing `D` is well-defined.  Each of
`A,B` has an edge to `r in W`, giving both asserted `A`--`W` and `B`--`W`
contacts.

## 3. Two visible old roots force the punctured model

Suppose `W` has neighbours at distinct `x,y in Z`.  Choose distinct
`a,b in Z-{x,y}` and let `z` be the fifth vertex of `Z`.  The five bags

```text
A union {a},  B union {b},  W union {q},  {x},  {y}
```

are pairwise disjoint and connected.  The first two bags are adjacent to
one another, to `W union {q}` through their respective contacts at `r`, and
to both singleton bags because they are `Z`-full.  The third bag meets both
singletons by the choice of `x,y`.  Thus only the pair `{x},{y}` may be
nonadjacent.  These are exactly the five roots of `S-{z}`, and all bags lie
in `G[C union (S-{z})]`.  They form the forbidden punctured rooted
`K_5^-` model.  Consequently

```text
d=|N_G(W) intersect Z|<=1.
```

The construction uses neither an added clique edge of `F` nor the omitted
root `z`.

## 4. Exact boundary count

For every nonempty `X subseteq C`, all neighbours of `X` lie in
`C union S`.  If its open neighbourhood there had order at most five, at
least one of the six vertices of `S` would survive its deletion and would
lie outside `X`; the deletion would separate that vertex from `X`, contrary
to six-connectivity of `G`.  Hence the closed rooted pair is internally
six-connected.

Apply this to `W`.  Distinct components of `G[C-(A union B)]` have no edge
between them, so every neighbour of `W` in `C-W` lies in `A union B`.
Within `S=Z union {q}`, the set has exactly its `d` visible vertices of `Z`
and the already proved contact at `q`.  These three boundary parts are
disjoint, and therefore

```text
6 <= |N_{G[C union S]}(W)| = p+d+1.
```

Together with `d<=1`, this gives `p>=5-d>=4`, exactly as claimed.

There are only finitely many pairs of vertex subsets `A,B`, so a pair
maximising the corresponding component order `|W|` exists.  The preceding
arguments apply unchanged to that choice.

## 5. Open gate and exact scope

The displayed maximal four-portal augmentation statement is not proved by
Theorem 1.  The theorem supplies the numerical premise `p+d>=5`, and in the
rooted-model-free setting maximality would exclude the proposed larger
pair, but no argument in the note establishes the asserted disjunction.
The source correctly labels this as **OPEN** and explains that the placement
of the portal vertices inside `A,B`, or an equivalent new linkage theorem,
is still required.

Accordingly, this audit certifies only the reduction to

```text
d<=1,  p>=5-d>=4
```

and the existence of a maximal pair.  It does not certify transfer of two
derived-boundary-full connected subgraphs to two original-boundary-full
connected subgraphs, and it does not close the sparse six-cut theorem.
