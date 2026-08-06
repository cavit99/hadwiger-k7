# Surplus at least three: a Yuan root-swap terminal

**Status:** experimental computation-free proof; independent audit pending.

Let `G` be a minimum-order, then minimum-size, seven-connected
`K_7^-`-minor-free graph with

\[
q=q(G)=|E(G)|-(4|V(G)|-2)\ge3.
\]

Fix a reserve-blind degree-seven vertex `x`, put

\[
N=N_G(x),\qquad J=G-x.
\]

The canonical six-boundary theorem gives that `J` is six-connected.

## Theorem 1 (local criticality at all seven roots)

One has

\[
\kappa(J)=6,
\qquad
\kappa(J-s)=5\quad(s\in N).                            \tag{1.1}
\]

Every fragment of `J` meets `N`, and every fragment of `J-s` meets
`N-{s}`.

### Proof

For `s in N`, the common-neighbour count on `xs` is

\[
|N_G(x)\cap N_G(s)|=d_{G[N]}(s)\le6\le q+3.
\]

Thus every edge `xs` is density-safe.  The quotient `G/xs` is target-free
and still satisfies the `4n-2` density threshold.  It cannot be
seven-connected by the minimum choice of `G`.

Let `z` be the contracted vertex and choose a cut `X` of `G/xs` of order
at most six.  Necessarily `z in X`; otherwise the cut lifts unchanged to
`G`.  Seven-connectivity of `G` forces `|X|=6`.  Deleting `X` from the
quotient is the same as deleting

\[
(X-\{z\})\cup\{x,s\}
\]

from `G`, and also the same as deleting

\[
(X-\{z\})\cup\{s\}
\]

from `J`.  Hence `J-s` has a five-cut.  Since `J` is six-connected,
`J-s` is at least five-connected, proving the second equality in (1.1).

If `J` were seven-connected, then

\[
|E(J)|=|E(G)|-7
      =4|V(J)|-2+(q-3)
      \ge4|V(J)|-2.
\]

It would be a smaller counterexample, impossible.  Thus `kappa(J)=6`.

Let `F` be a component behind a minimum six-cut `Q` of `J`.  In `G`, all
external neighbours of `F` lie in `Q union {x}`.  Seven-connectivity forces
`F` to be adjacent to `x`, so `F` contains a member of `N`.  Every fragment
contains such a component and, after choosing an inclusion-minimal
fragment, may be taken connected.

Similarly, let `F` be a component behind a minimum five-cut `Q` of `J-s`.
Its external neighbourhood in `G` lies in

\[
Q\cup\{x,s\},
\]

an order-seven set.  Seven-connectivity forces equality, in particular an
edge from `F` to `x`.  Since `s` is absent, `F` contains a member of
`N-{s}`.  `\square`

## Theorem 2 (root-only fragment)

The graph `J` has four fragments whose intersections with `N` are nonempty
and pairwise disjoint.  Consequently there is a connected fragment `F`
and a root `t in N` such that

\[
F\cap N=\{t\}.                                          \tag{2.1}
\]

Writing

\[
Q=N_J(F),\qquad |Q|=6,
\]

one of the following holds.

1. `F={t}` and `d_G(t)=7`.
2. `F-{t}` is nonempty; every component `K` of `F-{t}` satisfies
   \[
   N_G(K)=Q\cup\{t\},                                  \tag{2.2}
   \]
   and there are at most two such components.  Thus both
   \[
   Q\cup\{x\},
   \qquad Q\cup\{t\}                                  \tag{2.3}
   \]
   are actual exact seven-cuts, and (2.2) is a strict root-free
   exact-seven shore inside `F`.

### Proof

Theorem 1 says that `J` is a noncomplete `N`-locally `(6,1)`-critical
graph in Yuan's sense.  Noncompleteness is automatic: a complete
six-connected `J` of the present order contains a `K_7` minor.  Yuan's
fragment theorem gives four fragments with nonempty pairwise disjoint
traces on the seven-set `N`.  At least one trace is a singleton; choose it
as in (2.1).

Every component behind the minimum cut `Q` is itself a fragment and hence
meets `N`.  Only the root `t` is available on the selected side, so `F` is
one component and is connected.

If `F={t}`, then `N_J(t)=Q`; the additional edge `tx` gives `d_G(t)=7`.
Suppose `F-{t}` is nonempty and let `K` be one of its components.  It
contains no member of `N`, so `x` has no neighbour in it.  All its external
neighbours lie in `Q union {t}`.  This set has order seven and separates
`K` from the nonempty anti-fragment of `F`; seven-connectivity forces
(2.2).  Therefore `Q union {t}` is an exact seven-cut.  The set
`Q union {x}` is already the exact cut obtained by restoring `x` to the
minimum cut of `J`.

Deleting `Q union {t}` leaves at most three components in a target-free
seven-connected graph.  At least one lies outside `F`, so `F-{t}` has at
most two components.  `\square`

## Scope

For `q>=3`, the high-shore obstruction is absent because every edge is
density-safe, and Theorem 2 simultaneously removes the vague singleton
case.  The exact remaining state is the nested root swap (2.2)--(2.3):
either two adjacent degree-seven vertices occur, or a strict root-free
component is full to a new exact seven-boundary.

The theorem does not prove that this new component is density-eligible or
that contracting it preserves seven-connectivity.  Closing `q>=3`
therefore requires coupling its excess to the two labelled cuts in (2.3),
not another contact census.
