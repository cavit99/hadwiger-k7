# Independent cold audit: prescribed-vertex separator minimisation

**Audited source:**
[`hc7_k7minus_prescribed_vertex_separator_minimisation.md`](hc7_k7minus_prescribed_vertex_separator_minimisation.md)

**Source SHA-256:**
`d19f38e99bd3b797b59f9932015f9c55279fa363b1c24346d5af36f48e5ef221`

The current source SHA-256 is
`21461ea83788b2a696a944ca8befaf0b99fe8e18de64c020ec6a88af65b5489d`.
The only later change records this GREEN audit in the status line; the
mathematical content is unchanged.

**Verdict:** **GREEN.**  This is an independent, computation-free cold
proof audit, not external peer review.  The minimum-boundary quantifier,
component classification, fullness, degree-eight budget, bound `r<=4`,
all seven-bag completions, and the order-eight/nine corollaries check.

## 1. The selected side is a component and its boundary is a cut

Put `S=N_G(R)`.  No vertex of `R` has a neighbour outside `R union S`,
and `G[R]` is connected, so `R` is exactly one component of `G-S`.
The prescribed condition `v in N_G(R)` puts this component among the
components meeting `v`.  The nonempty far side makes `S` an actual
separator; seven-connectivity consequently gives `|S|=k>=7`.

For any other component `C` of `G-S`, one has `N(C) subseteq S`.  Deleting
`N(C)` leaves both `C` and the original component `R`, so `N(C)` is an
actual separator and has order at least seven.  If it contains `v`, then
`C` itself is admissible in the minimisation defining `R`: it is connected,
has `v` in its boundary, and `R` is a nonempty far side.  Minimality gives
`|N(C)|>=k`; containment in the `k`-set `S` forces `N(C)=S`.  The selected
component `R` also has boundary `S` by definition.

Thus every component meeting `v` is `S`-full.  Every component not meeting
`v` has an actual boundary satisfying

```text
7<=|N(C)|<=k-1,       N(C) subseteq S-{v}.
```

These two classes exhaust the components.  Partitioning the eight
neighbours of `v` between `S` and the components it meets proves the exact
incidence identity (1.3), with no uncounted component or overlap.

## 2. At most four full components

If five full components existed, choose four distinct anchors and two
further singleton vertices in `S`; this is possible because `k>=7`.
The four anchored component bags, a fifth bare component and the two
singletons are seven disjoint connected bags.  Any two component-derived
bags are adjacent through an anchor and fullness, and every such bag meets
both singleton roots.  Only the singleton--singleton pair can be absent.
This is a `K_7^-` model.  Hence `1<=r<=4` exactly as stated.

## 3. Boundary sparsity and every quantifier

Set `q=7-r` and fix an arbitrary `q`-set `Q subseteq S`.  If `G[Q]` had
at most one missing edge, then

```text
|S-Q|=k-q>=7-(7-r)=r,
```

so there are enough distinct anchors for `r-1` full components.  Anchor
those components, leave the last full component bare, and retain every
vertex of `Q` as a singleton.  These are exactly seven disjoint connected
bags.  Fullness supplies all pairs involving a component bag, whilst the
singleton bags have at most one absent pair.  Again this is a `K_7^-`
model.  The contradiction holds for every choice of `Q`, proving

```text
|E(G[Q])|<=binom(q,2)-2.
```

For `r=4,3,2,1`, the four bounds are respectively `1,4,8,13` on sets of
orders `3,4,5,6`.  Every triple spanning at most one edge is equivalent to
`Delta(G[S])<=1`: a vertex with two neighbours supplies a two-edge triple,
and a matching contributes at most one edge to any triple.

## 4. The first two boundary orders

When `k=8`, a component not meeting `v` has boundary of order seven inside
the seven-set `S-{v}`, so its boundary equals `S-{v}` and is an actual
order-seven separator.  If no such component exists, every component meets
`v` and is `S`-full.

When `k=9`, the same component classification gives an actual boundary of
order seven or eight inside `S-{v}`.  If there is no component of that
kind, all components are full.  These alternatives establish Corollary 2
without asserting exclusivity or an upper bound for general `k`.

## 5. Scope

The smaller separator arising from a component which misses `v` is
contained in `S-{v}` and therefore cannot itself drive a root-preserving
iteration.  If all components meet `v`, the proof leaves a full interface
of unbounded order, with at most four components and the stated induced-
subgraph restrictions.  The cited `K_{8,n}` family really is target-rich
and bipartite, so the source correctly uses it only to rule out a bound
from connectivity, prescribed degree, side minimality and fullness alone.

The theorem is consequently an unbounded normal form, not an order-seven
separator theorem and not a proof of the colouring conjecture.
