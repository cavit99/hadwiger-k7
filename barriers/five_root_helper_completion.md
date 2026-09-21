# Limits of strengthening and placing rooted helpers

**Status:** explicit counterexamples with a separate hash-pinned internal
audit. They refute the three intermediate assertions below, not the
density-two one-missing-contact target, Conjecture 21 or HC7.

Five-root density means the number of edges not entirely between roots,
minus four times the number of nonroots. A graph is 4-light if every
root-free set with at most four external neighbours has nonpositive
incident four-density. All graphs are finite and simple.

## 1. The density-one extension fails

Let the five roots be `u,v,a,b,c`. Add the root edge `uv` and two
adjacent nonroots `p,q`, with neighbourhoods

```text
N(p)={q,u,a,b,c},     N(q)={p,v,a,b,c}.
```

The only nonempty nonroot sets are `{p}`, `{q}` and `{p,q}`; each has
five external neighbours. Thus the graph is internally five-connected
as a rooted graph and is 4-light. Its rooted density is `9-4*2=1`,
and no nonroot is adjacent to both `u,v`.

A seven-bag model on these seven vertices must use singleton bags.
It has only nine of the eleven contacts involving a helper. Hence the
ten-contact conclusion fails even with the stated split-edge condition.
Contracting `uv` makes `{p,q}` a positive four-boundary fragment.

This blocks extending the density-two induction to every density-one
side produced by an edge contraction. It does not block a construction
using that side together with the rest of its host.

## 2. Two prescribed vertices need not occupy opposite helpers

Let `H=K7-{xa,yb}`, with vertices `x,y,a,b,c,d,w`. Prescribe the six
roots `S={x,y,a,b,c,d}`, and first root the helper model only at
`Z={a,b,c,d}`. The helpers `{x,y}` and `{w}` are adjacent and each
meets all four singleton root bags. Also `e(H)=19=4|V(H)|-9`.

The pair `(H,S)` is internally six-connected: the only nonempty
root-free set is `{w}`, whose boundary is all six roots. Also `H` is
five-connected: deleting at most four vertices leaves at least three,
each missing at most one other vertex, so the remaining graph is
connected. Hence the internal four- and five-connectivity conditions
for the smaller prescribed root sets hold as well.

There is no corresponding full adjacent two-helper model putting `x`
and `y` in different helpers. It would have six separately prescribed
bags, with only `w` available to augment one of them. The absent
contacts `xa` and `yb` have disjoint endpoint pairs. One augmentation
cannot repair both, and unused vertices cannot help.

This refutes unrestricted opposite-helper placement. The example has
thirteen six-root boundary edges and interior excess two; it does not
refute a placement rule using the sparse boundary and excess seven of
the remaining six-cut programme.

## 3. Arbitrary density does not force all eleven contacts

For `m>=4`, let `P_m` be the planar bipyramid over the cycle
`v0,...,v(m-1)`: its nonadjacent poles `a,b` both meet every cycle
vertex. Form `F_m` by adding adjacent universal vertices `s,t` to `P_m`.
Prescribe the five roots

```text
X={s,t,a,v0,v1}.
```

These roots induce a literal `K5`. The nonroots induce a connected
graph through `b`. The bipyramid is four-connected: if a pole remains
after deleting at most three vertices, it joins all remaining cycle
vertices; if both poles are deleted, a cycle with at most one vertex
deleted remains. Consequently `F_m` is six-connected, hence is 4-light
with the prescribed five roots.

There are `m+4` vertices and `5m+5` edges in `F_m`. Its five-root
density is

```text
(5m+5)-10-4(m-1)=m-1,
```

which is unbounded. Nevertheless `F_m` has no `K7` minor. In a
seven-bag model, at most two bags contain `s` or `t`; five bags would
lie entirely in planar `P_m` and give it a `K5` minor, a contradiction.

Two adjacent helpers full to all five rooted bags would combine with
the literal root clique to give that forbidden `K7`. Thus no fixed
density threshold forces all eleven contacts, even with connected
nonroots and six-connectivity. Deleting the root–root edges preserves
rooted density, 4-lightness, nonroot connectedness and nonexistence of
the helper model, so requiring independent roots does not repair it.

This does not refute the target allowing one missing contact. It
blocks replacing its allocation problem by an unrestricted stronger
full-helper density assertion.
