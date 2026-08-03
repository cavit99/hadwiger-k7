# Internal audit: low-endpoint density-safe atoms

**Audited draft:**
[`hc7_k7minus_low_endpoint_safe_atom_reduction.md`](hc7_k7minus_low_endpoint_safe_atom_reduction.md)

**Draft SHA-256:**
`eb97bf93b188625fc82e58a88e8e8a89f44cc5813fe6eb4bf242671ad2d23901`

**Verdict:** **GREEN for the stated reduction.**  The proofs are
computation-free.  They do not eliminate a singleton atom or prove the
`4n-2` extremal theorem.  This is a separate internal audit, not external
peer review.

## 1. Generalised criticality

The family `\mathcal Y` consists of density-safe edges with an endpoint of
degree at most eight.  For every `ab\in\mathcal Y`,

\[
 q(G/ab)=q(G)+3-c(ab)\ge q(G).
\]

Minimality therefore makes `G/ab` fail seven-connectivity.  Since the
strict density forces `|V(G)|\ge9`, a cut of order at most six exists in
the quotient.  It contains the contracted vertex; its pullback has order
seven and contains `a,b`.  This verifies the first clause in Mader's
definition of `\mathcal Y`-criticality.

For a `\mathcal Y`-fragment `A` meeting the degree-seven set, the audited
safe-contraction theorem supplies an incident edge with at most three
common neighbours.  Its degree-seven endpoint makes it a member of
`\mathcal Y`, and its certifying separator meets `A`.

If `A` avoids the degree-seven set, a leaf `z` of a component of `G-N(A)`
inside `A` has degree exactly eight, is complete to the order-seven
boundary, and has one neighbour `w` in its component.  The boundary has a
vertex `s` of boundary degree at most three.  In the two-component case,
the only exception from the seven-vertex structure theorem is the
pentagonal bipyramid; the seven displayed branch sets in the draft do give
`K_7^-`, with only `\{r_1\}` and `\{r_3\}` possibly nonadjacent.  Hence

\[
 c(zs)=d_{G[S]}(s)+[sw\in E(G)]\le4\le q+3.
\]

The degree-eight endpoint places `zs` in `\mathcal Y`, and its certifying
separator meets `A`.  This is exactly Mader's second criticality clause.
The half-connectivity atom bound therefore gives atom order at most three.

## 2. Atoms inside the high-degree forest

Every component behind an atom boundary is full to the boundary and is
itself a `\mathcal Y`-fragment.  Atom minimality makes the selected atom a
single component and every opposite component at least as large.

If an atom avoided all degree-seven vertices, it would be a connected
subgraph of the high-degree forest.

- A singleton would have exactly seven boundary neighbours and hence
  degree seven.
- An edge would have two degree-eight endpoints complete to the boundary.
  Their seven common neighbours cannot fit in the separating six-set
  supplied by the essential-edge theorem.
- A three-vertex atom would be a path.  Its leaves are boundary-full, its
  middle vertex has at least six boundary neighbours, and an opposite
  component has at least three vertices.  The four-rooted diamond in that
  opposite closed shore, together with the three displayed path-derived
  bags, has all required adjacencies and at most the rooted diamond's one
  missing pair.

Thus every low-endpoint atom contains a degree-seven vertex.

## 3. Singleton arithmetic and rooted reduction

For a singleton atom `\{x\}`, its order-seven boundary `S=N(x)` contains a
member `uv` of `\mathcal Y`; orient it so that `d(u)\le8`.  With

\[
 J=G-\{x,u\},\qquad T=S-\{u\},
\]

deleting two vertices gives `\kappa(J)\ge5`, and direct edge accounting
gives

\[
\begin{aligned}
 |E(J)|
 &=|E(G)|-7-d(u)+1\\
 &=4|V(J)|+q-d(u)\\
 &\ge4|V(J)|-7.
\end{aligned}
\]

The internal six-connectivity assertion is also exact.  The graph `G-u`
is six-connected.  A separation `(A,B)` of `(J,T)` of order at most five,
with `T\subseteq A` and `B-A` nonempty, would extend to the separation
`(A\cup\{x\},B)` of `G-u`: all neighbours of `x` there belong to `T`.
The added vertex also makes the second side proper.  This contradicts
six-connectivity.

Norin--Totschnig's theorem applies.  Its sole exception
`K_{2,2,2,2}` has exactly `4|V|-8` edges and cannot equal `J`.  A spanning
exact `K_7^\vee` model follows: if enlargement created either nominally
missing adjacency, the host would already contain `K_7^-`.  Absorbing the
deficient bag into a universal bag gives a spanning `K_6` model.

If five bags of any `K_6` model met `T`, adding `\{x\}` would give a
`K_7^-` model.  This proves the exact rooted obstruction.  The same argument
with `u` proves both four-contact bounds.  If `x` contacts four bags and
`u` contacts a fifth, absorbing `u` into that fifth bag preserves the
`K_6` model and the edge `xu` creates a fifth contact for `x`; this verifies
the joint-contact inclusion and its symmetric form.

## 4. Correction of the crossing inference

The draft correctly rejects a stronger geometry considered during the
attack.  Although the boundary edge `uv` is density-safe, its failed
contraction need not have a certifying separator meeting `\{x\}`.  The
six-vertex image of `S` in `G/uv` already isolates `x`, and its pullback is
`S` itself.  Mader's atom crossing lemma therefore cannot put `x` into a
separator containing `u,v`.

The second criticality clause does give a certifying separator meeting the
atom for an incident safe edge `xs`, but it supplies no bound
`d(s)\le8`.  The low-degree deletion arithmetic and the crossing separator
cannot presently be imposed on the same boundary vertex.  Any claimed cut

\[
 \{x,u\}\cup Q,
\]

or component/excess/crossed-miss conclusion derived from it, would be
unsupported.  None is asserted in the draft.

The diagnostic `K_3\vee C_5` is correct.  It is five-connected and has a
`K_6` minor.  On eight vertices, obtaining a seven-bag minor means deleting
one vertex or contracting one edge.  The resulting graphs have at most
19 edges, below the 20 edges of `K_7^-`; hence it has no `K_7^-` minor.
Its 23 edges equal `4|V|-9`, so it does not satisfy the live density bound.

## 5. Scope and trust boundary

The adjacent GREEN audits were checked for the strict-surplus structure,
degree-seven safe contraction, essential-edge separation, seven-cut
component bounds, seven-vertex `K_5`-minor-free structure, and closed-shore
rooted connectivity.  The external statements used are Mader's
generalised atom theorem, Jørgensen's rooted-diamond theorem, and
Norin--Totschnig Theorem 6.

The exact remaining statement is a prescribed-root strengthening: the
internally six-connected rooted pair `(J,T)` in Theorem 3.1 must have a
`K_6` model with at least five bags meeting `T`.  Neither the unrooted
extremal theorem nor the present atom calculus proves that assertion.
