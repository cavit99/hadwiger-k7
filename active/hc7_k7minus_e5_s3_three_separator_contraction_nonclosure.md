# The inherited four-cut after contracting the three-separator atom

**Status:** recorded computation-free route nonclosure; see the
[separate internal audit](hc7_k7minus_e5_s3_three_separator_contraction_nonclosure_audit.md).
This is not a counterexample and does not prove `(E5)`.

Use the notation of the
[atomic six-boundary reduction](hc7_k7minus_e5_six_boundary_atomic_reduction.md)
and its
[companion-cut elimination](hc7_k7minus_e5_s3_companion_cut_elimination.md).
After the maximum-excess tie-break eliminates the four-separator branch,
the remaining `s=3`, singleton-`q` row has a three-set `T` for which

\[
                         T\cup\{t,q\}                 \tag{1}
\]

is an exact five-cut.  Its low component is either `{p}` or `{p,b}`.
In the singleton case

```text
N_G(p)=T union {t,q};
```

in the edge case `pb` is an edge, `p` meets two or three members of `T`,
and `b` is complete to `T`.  In both cases

```text
N_G(t)={x,y,u_t,p,q},
N_G(q)={t,p,b} union R_0,            |R_0|=2.
```

## Proposition 1 (the safe contraction returns the old cut)

Let `z` be the vertex obtained by contracting `pt`, and put `J=G/pt`.
Then

\[
 \kappa(J)=4,
 \qquad |E(J)|\ge4|V(J)|-6.                         \tag{2}
\]

The four-cut certifying `kappa(J)=4` is precisely

\[
                         \{z,b\}\cup R_0,             \tag{3}
\]

the image of the already known cut `N_G(q)`.

### Proof

The common neighbours of `p,t` are `q` and, possibly, the sole boundary
neighbour `u_t` of `t`.  The vertex `b` is not adjacent to `t`, and
`x,y` have no neighbour in `A`.  Hence contraction loses at most three
edges:

\[
 |E(J)|\ge(4|V(G)|-7)-3=4|V(J)|-6.                  \tag{4}
\]

No set of at most three vertices disconnects `J`.  A cut avoiding `z`
would lift unchanged to `G`; a cut containing `z` would lift after
replacing `z` by `p,t` to a cut of `G` of order at most four.  Both
possibilities contradict five-connectivity of `G`.

On the other hand, `N_G(q)={t,p,b} union R_0` is the exact five-cut whose
low component is `{q}`.  Contracting its two members `p,t` turns it into
(3), still separating `q`.  Thus `J` is not five-connected and (2)
follows.  \(\square\)

This identifies the first failure of the tempting repeated-contraction
argument: minimum-counterexample reasoning does not produce a new cut.
The quotient already carries a four-cut inherited from the configuration
being analysed.

## 2. The exact limit of the published density theorem

Norin--Totschnig, Theorem 6, states that a four-connected `n`-vertex graph
with at least `4n-8` edges contains `K_7^vee`, apart from
`K_{2,2,2,2}`.  Here `K_7^vee` is `K_7` with two incident edges deleted.
Proposition 1 applies the theorem to `J`; the exceptional graph is excluded
because `J` has at least `4|V(J)|-6` edges.  Therefore

\[
                              K_7^\vee\preccurlyeq J. \tag{5}
\]

Statement (5) is not a `K_7^-` conclusion.  The theorem neither puts `z`
in the branch set incident with the two missing adjacencies nor controls
how that branch set meets the two preimages `p,t`.  A model avoiding `z`
still lifts only as `K_7^vee`; a model using `z` need not split into two
connected, disjoint bags while preserving the required adjacencies.

The primary source is S. Norin and A. Totschnig,
[*Every graph with no `K_7^vee`-minor is 6-colorable*, Theorem 6](https://arxiv.org/abs/2507.03244).

## 3. Finite diagnostic and smallest repair

The dependency-free
[`atomic portal-concentration verifier`](hc7_k7minus_e5_s3_atomic_portal_concentration_verify.py)
checks the generic contact quotients for both low sides `{p}` and `{p,b}`.
Each has minimum seven-bag defect two.  This is finite evidence about the
abstract quotient, not a host counterexample and not an unbounded proof.

The subsequent
[edge-atom elimination](hc7_k7minus_e5_s3_edge_atom_elimination.md)
shows that `{p,b}` is not a separate obstruction: its excess-one form is a
singleton atom under a different adhesion, and its excess-two form gives an
explicit `K_7^-` model.  The repair below is therefore needed only for the
singleton `{p}`.

The smallest repair exposed by this route is the following model-or-cut
statement.

> In `G/pt`, either a `K_7^vee` model can be chosen so that expanding the
> contracted vertex restores one of its two incident missing adjacencies,
> or there is an order-four cut distinct from the inherited image (3) and
> whose lift yields a strict lexicographic high-excess descent.

Without one of these two labelled conclusions, the surplus in (4), the
unrooted near-clique model (5), and the mere existence of a four-cut do not
close the remaining singleton atom.
