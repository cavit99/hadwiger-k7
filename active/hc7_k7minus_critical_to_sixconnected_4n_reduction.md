# A six-connected density reduction for Conjecture 21

**Status:** written proof; [two separate internal audits are
GREEN](hc7_k7minus_critical_to_sixconnected_4n_reduction_audit.md).  These
are internal mathematical audits, not external peer review.  This reduction
does not prove Conjecture 21.  It records the additional colouring and
vertex-splitting data that must not be discarded when the dense
six-connected graph is used.

Write `K_7^-` for `K_7` with one edge deleted.

## Theorem 1 (critical contraction)

Suppose that `G` is minor-minimal subject to being non-six-colourable and
having no `K_7^-` minor.  Then there are adjacent vertices `v,x` and a graph

\[
                              H=G/vx
\]

with the following properties.

1. `d_G(v)=8` and

   \[
                  |N_G(v)\cap N_G(x)|\le3.             \tag{1}
   \]

2. `H` is six-connected, `K_7^-`-minor-free, and exactly six-chromatic.
3. One has

   \[
                  |E(H)|\ge4|V(H)|.                    \tag{2}
   \]

4. Let `w` be the vertex of `H` obtained by contracting `vx`, and put

   \[
                         T=N_G(v)-\{x\}.
   \]

   Thus `|T|=7`.  In every proper six-colouring of `H`, if `w` has colour
   `alpha`, then the vertices of `T` use all five colours other than
   `alpha` and do not use `alpha`.

In particular, the following extremal statement would imply
Norin--Totschnig Conjecture 21:

> Every six-connected graph `J` with
> `|E(J)|>=4|V(J)|` contains a `K_7^-` minor.

The stronger statement is not needed: it is enough to exclude graphs `H`
with the vertex-splitting and colouring properties in items 1--4.

### Proof

Every proper minor of `G` is six-colourable.  In particular `G-u` is
six-colourable for any vertex `u`, so `G` is seven-colourable.  Since `G`
is not six-colourable, `chi(G)=7`.

The promoted critical-host reductions give

\[
 \kappa(G)\ge7,\qquad \delta(G)\ge8,
 \qquad |E(G)|\ge4|V(G)|,                              \tag{3}
\]

and at least one degree-eight vertex.  The promoted six-connected
degree-eight theorem applies to `G`, so choose a degree-eight vertex `v` and
an incident edge `vx` satisfying (1).

Contraction lowers vertex connectivity by at most one, so `H` is
six-connected.  It is a proper minor of `G`, and hence it is
`K_7^-`-minor-free and six-colourable.  If it had a five-colouring, expand
the contracted vertex to `v,x`, give both ends its old colour, and then
recolour `v` with a new sixth colour.  This would be a proper six-colouring
of `G`, a contradiction.  Hence `chi(H)=6`.

Let `c=|N_G(v)\cap N_G(x)|`.  Suppressing parallel edges after contracting
`vx` gives

\[
 |V(H)|=|V(G)|-1,
 \qquad |E(H)|=|E(G)|-1-c.
\]

Equations (1) and (3) now give

\[
 |E(H)|\ge4|V(G)|-4=4|V(H)|,
\]

which is (2).

Finally fix a proper six-colouring of `H` and let `alpha` be the colour of
`w`.  Expanding `w` gives a proper colouring of the edge-deletion graph
`G-vx` in which `v` and `x` both have colour `alpha`.  Every member of `T`
is joined to `v` by an edge
which was not contracted, so no member of `T` has colour `alpha`.  If one
of the other five colours were absent from `T`, recolouring `v` with that
colour would properly six-colour `G`.  Thus all five other colours occur on
`T`, proving item 4.  The final implication is immediate from items 2 and
3. `\square`

## Exact scope

The theorem provides a new sufficient conditional refinement for the
critical-host route alongside the former arbitrary seven-connected `4n-2`
target.  The two universal extremal statements are logically incomparable:
the present one assumes less connectivity but more density.  Its critical
quotient carries strictly more provenance: a specified vertex split, a
degree-eight end, at most three common neighbours, and the
five-colour-surjectivity condition on the other seven neighbours.  The
theorem does not prove that every arbitrary six-connected graph at this
density contains `K_7^-`, nor does an unrooted `K_6^-` or `K_7^\vee` model
in `H` automatically respect `T`.

## Repository inputs

- Mader's seven-connectivity theorem for contraction-critical graphs, in the
  modern form quoted as Theorem 1.8 by Rolek and Song, *Coloring graphs with
  forbidden minors*;
- [critical-host degree and density reduction](../results/hc7_k7minus_degree7_rooted_helper_closure.md);
- [six-connected degree-eight low-codegree theorem](../results/hc7_k7minus_sixconnected_degree_eight_low_codegree.md).
