# Internal audit: exact degree-seven neighbourhoods under `K_7^-` exclusion

Audited file:
`results/hc7_k7minus_degree7_clique_incidence.md`.

Audited SHA-256:

```text
04e085032a096ef3fd508ca4ee287ef82417a718ae3d95646ae4cbd0b911ed2e
```

**Verdict:** **GREEN** for the exact revision above.

This is a separate internal mathematical audit, not external peer review.
The audit reconstructed both proofs from their stated hypotheses and checked
every branch-set adjacency.  No repository theorem or finite classification
from the earlier degree-seven proof spine is used.

## 1. Hypotheses and the contraction colouring

The assumptions `chi(G)=7` and every proper minor six-colourable make `G`
strongly seven-contraction-critical, so Dirac's inequality applies.  At a
degree-seven vertex it gives

\[
                       \alpha(G[N(v)])\le7-7+2=2.
\]

Thus the complement of the neighbourhood is triangle-free.

For a neighbourhood nonedge `ab`, contracting the connected star on
`v,a,b` produces a proper minor.  In a six-colouring of that minor, the
contracted vertex can be expanded to the same colour on the nonadjacent
vertices `a,b` after `v` is deleted.  All five remaining neighbours avoid
that colour.  They must use the other five colours distinctly, since any
missing neighbourhood colour could be assigned to `v`.

This argument does not assume that the six-colouring uses all six colours
globally.  If fewer colours occur on the neighbourhood, the same extension
contradiction applies.

## 2. Kempe-chain and rooted-minor conversion

Let `x,y` be a nonedge among the five rainbow roots.  If their bichromatic
components were different, interchanging the two colours on the component
containing `x` would remove the old colour of `x` from the entire
neighbourhood.  Assigning it to `v` would six-colour `G`.  Hence every edge
of the complement graph on the roots is represented in its corresponding
bichromatic component in one fixed colouring.

Deleting the colour class containing `a,b` leaves a proper five-colouring
with all five colour classes represented by the roots.  The bichromatic
connections survive because they use only their two root colours.  The
demand graph is triangle-free on five vertices, so it has at most six edges
by Mantel's theorem.  Kriesell--Mohr, *Kempe Chains and Rooted Minors*,
Theorem 7 applies exactly: its property `(*)` supplies five disjoint
connected rooted branch sets adjacent across every demanded pair.  Every
nondemanded pair is a literal neighbourhood edge between its two roots.
These two sources of adjacency exhaust all ten pairs, proving the uniform
rooted `K_5` statement inside `G-v-\{a,b\}`.

## 3. Low complement degrees

Fix a nonisolated complement vertex `a` and a complement neighbour `b`.
If `d_F(a)=1`, the singleton `\{a\}` is adjacent through the five literal
roots to all five rooted branch sets.  Together with `\{v\}` these are seven
disjoint connected pairwise adjacent branch sets, hence a `K_7` minor.

If `d_F(a)=2`, let `x` be its other complement neighbour.  Since the
complement is triangle-free, `b` and `x` are adjacent in the original
neighbourhood.  Therefore `D=\{b\}\cup B_x` is connected.  The branch sets

\[
       \{v\},\quad\{a\},\quad D,
       \quad(B_y:y\in N(v)-\{a,b,x\})
\]

are disjoint.  The rooted branch sets supply all mutual contacts; `B_x`
supplies every contact from `D` to the other rooted branch sets; `v`
contacts every set through a root; and `a` contacts all four unchanged
rooted branch sets because its only complement neighbours are `b,x`.  Only
the `aD` contact may be absent.
Thus the model is `K_7^-`, or `K_7` if that contact is present.  Since a
`K_7` minor also contains `K_7^-` after deleting an edge, both low-degree
cases contradict the hypothesis.

## 4. Exhaustive seven-vertex classification

Every nontrivial component of the triangle-free complement now has minimum
degree at least three.  A component on at most five vertices violates
Mantel's edge bound, so exactly one nontrivial component occurs and it has
order six or seven.

- At order six, the degree lower bound and Mantel's upper bound both give
  nine edges.  The equality case of Mantel's theorem gives `K_{3,3}`, with
  the seventh vertex isolated.
- At order seven, a vertex of degree at least five would have an independent
  neighbourhood and force each of five of its neighbours to have degree at
  most two.  Hence all degrees are three or four.  Parity forces a
  degree-four vertex `z`.  Its four neighbours are independent and must
  each contact both vertices outside `N_F[z]`; triangle-freeness forbids an
  edge between those two vertices.  This is exactly `K_{3,4}`.

Taking complements gives precisely

\[
                 K_4\mathbin{\dot\cup}K_3,
                 \qquad K_1\vee(K_3\mathbin{\dot\cup}K_3).
\]

Their literal `K_4`s give exactly the asserted one- or two-`K_5`
incidence after adjoining `v`.

## 5. Dependency and trust boundary

The logical dependencies are only Dirac's neighbourhood-independence
inequality, Kriesell--Mohr Theorem 7, and Mantel's theorem.  The earlier
anti-neighbourhood connectivity theorem, matching-language theorem,
aligned near-`K_7` theorem, exterior-component analysis, and 129-graph
residual are not used.

Seven-connectivity is stated for the intended critical-host application but
is not used locally.  The result does not treat degree-eight vertices, prove
the `K_7^-` six-colour conjecture, or prove `HC_7`.  No unresolved internal
assumption remains in the displayed theorem; the cited published inputs
remain part of the external source-review boundary.
