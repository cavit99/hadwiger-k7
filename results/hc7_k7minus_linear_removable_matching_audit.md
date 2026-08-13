# Internal audit: linear seven-removable matchings

## Verdict and revision

**GREEN for Lemma 2.1, Theorems 2.2, 3.1, 3.2 and 4.2, and their stated
corollaries.**  This is an internal mathematical audit, not external peer
review.

The audited theorem is
[`hc7_k7minus_linear_removable_matching.md`](hc7_k7minus_linear_removable_matching.md)
at SHA-256

```text
27526a0b6a0c077200a04ad1f52185943cd90775fe2b2d0394bc6078a8c9c3fc
```

No computation is used in the proof.

## 1. Critical-host inputs and degree defect

The theorem assumes the already audited critical-host conclusions

```text
kappa(G)>=7, delta(G)>=8, no literal K5,
n8>=25+tau, n>=25.
```

The degree identity was checked directly:

\[
 2e(G)=8n_8+9n_9+\sum_{i\ge10} i n_i
      =9n-n_8+\tau
      \le9n-25.
\]

No extremal inequality is subtracted in the wrong direction.

## 2. The sixteen-edge lemma

A vertex-minimal five-chromatic induced subgraph has minimum degree at
least four.

- Orders five and six are excluded exactly as stated.
- At order at least eight, equality in the degree lower bound would give a
  connected four-regular graph.  Brooks' theorem excludes chromatic number
  five.
- At order seven and fifteen edges, the two displayed degree sequences are
  exhaustive.  The universal-vertex case leaves a cubic four-chromatic
  graph and hence a `K_4` component.  In the second case, the complement is
  one path together with zero or one cycle and always has a matching of
  order three.  Those three nonedges and the remaining vertex give a
  four-colouring.

Thus the lower bound of sixteen edges is valid and uses only literal
`K_5` exclusion.

## 3. Feedback-set accounting

For `R=G-T` a nonempty forest with `r` vertices and `c` components,

\[
 |E(R)|=r-c.
\]

Writing

\[
 D_R=\sum_{x\in R}(d_G(x)-8),
\]

degree summation gives

\[
 |E(T,R)|=8r+D_R-2(r-c)=6r+2c+D_R.
\]

Hence

\[
 e(G)=e(G[T])+7r+c+D_R.
\]

Substitution into `2e(G)<=9(t+r)-25` gives

\[
 5r+2e(G[T])+2c+2D_R\le9t-25.
\]

The forest is bipartite, so disjoint palettes imply
`chi(G[T])>=5`; the sixteen-edge lemma and `c>=1` then yield

\[
 5(n-t)+34\le9t-25,
\]

which is equivalent to

\[
 14t\ge5n+59.
\]

The empty-complement case is handled separately and is harmless because
`n>=25`.

The sharper estimate in Remark 2.3 was also checked.  A degree-eight
vertex in `T` with at most one `T`-neighbour has at least seven neighbours
in the forest, and those contain an independent four-set.  The displayed
star contraction and recolouring really give a six-colouring of `G`.
Counting degree-eight vertices outside the selected critical subgraph then
gives `e(G[T])>=max(16,34-r)`.

## 4. Maximal removable matching

The audited Chu-based theorem supplies a nonempty seven-removable matching,
so an inclusion-maximal one exists.

If a cycle remained outside its endpoint set, all its vertices would retain
their full degree from `G`, because no matching edge is incident with them.
Thus they have degree at least eight in `G-M`.  Mader's critical-cycle
theorem rules out every cycle edge being critical for seven-connectivity,
and a removable cycle edge enlarges the matching while preserving
sevenconnectivity.  This is a contradiction.

Therefore the endpoint set of the maximal matching is a feedback vertex
set.  Applying the proved feedback bound gives

\[
 |M|\ge\left\lceil\frac{5n+59}{28}\right\rceil.
\]

At `n=25` the right side is seven, so the stated universal seven-coordinate
consequence is numerically correct.

## 5. Exact signature cube

For `J` a nonempty subset of a matching `M`, every contraction component is
one matching edge.  No edge of `M-J` is identified, and no edge of `G-M`
becomes a loop: in a simple graph the only edge whose two ends are one
contraction class is the contracted matching edge itself.

Expanding a six-colouring of `G/J` therefore gives exactly signature `J`
on `G-M`.  The empty signature would colour `G`.  The proof does not assume
that the endpoint-induced graph is empty or that different matching edges
have no cross edges.

## 6. Exact model and endpoint visibility

Every submatching `N` of the maximal matching leaves a supergraph of
`G-M`, so `G-N` remains seven-connected.  For `5<=|N|<=8` its density is
at least the Norin--Totschnig threshold.  The order-eight exception is
excluded by `n>=25`.

Target exclusion makes the resulting spanning `K_7^vee` model exact:
either nominal missing adjacency would immediately give `K_7^-`.

The endpoint-visibility argument was checked against the earlier audited
eight-coordinate proof.

- A branch set among `P,B,C` which contains a matching endpoint has a
  genuine far branch set and carries the singleton-coordinate rejected
  trace.
- For an endpoint hidden in `U_i`, splitting a tree path from a
  `P`-portal gives either a far foreign bag, a target model, a response side
  containing an endpoint, or a strict increase of the visibility score.
- At a maximum, every endpoint in every universal bag is adjacent to `P`.
- Five matching edges give ten endpoints in four universal bags, so one bag
  contains at least two selected portals.
- The audited exact-`K_7^vee` separator dichotomy then returns the target or
  a connected actual response side containing an endpoint.

No upper bound on the returned boundary is claimed.

Partitioning the maximal matching into disjoint five-edge blocks makes the
selected coordinate edges in Corollary 4.3 distinct.  The separators and
exact models themselves need not be distinct or compatible.

## 7. Scope

The theorem genuinely removes the need to obtain the first seven
coordinates through the former six-coordinate connectivity fork.  It does
not prove:

- a common boundary partition for two response separators;
- an upper bound on the original labelled separator;
- compatibility of exact models chosen for different five-edge blocks;
- the `K_7^-` six-colour conjecture; or
- `HC_7`.

Those limitations are stated in the theorem note.
