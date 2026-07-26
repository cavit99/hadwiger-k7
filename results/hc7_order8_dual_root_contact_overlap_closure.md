# Dual-root contact overlap closes the pentagonal-bipyramid branch

**Status:** written proof; [separately audited **GREEN**](hc7_order8_dual_root_contact_overlap_closure_audit.md).
This result closes the
pentagonal-bipyramid alternative in the dual-free-root response-star
construction.  It does not close the remaining low-degree contact-graph
alternative, the order-eight response-coupling theorem, or `HC_7`.

## 1. An eight-vertex contact-graph lemma

Write

\[
             B_5=\overline {K_2}\vee C_5
\]

for the pentagonal bipyramid.  Its two nonadjacent vertices are called its
poles and the vertices of its five-cycle are called its rim vertices.

### Theorem 1.1 (dual-deletion overlap)

Let `K` be a simple graph on eight vertices and let `a,b` be distinct
vertices.  If both `K-a` and `K-b` are pentagonal bipyramids, then there is
a vertex `r` such that `K-r` contains a `K_5` minor.

### Proof

Put `U=V(K)-{a,b}`.  Deleting a pole from `B_5` leaves

\[
                       K_1\vee C_5,
\]

whose degree multiset is `(5,3,3,3,3,3)`.  Deleting a rim vertex leaves

\[
                       \overline {K_2}\vee P_4,
\]

whose degree multiset is `(4,4,4,4,3,3)`.  Since

\[
                 K-U=K[\{a,b\}],\qquad
                 K[U]=(K-a)-b=(K-b)-a,
\]

the vertex `b` has the same pole-or-rim role in `K-a` as `a` has in
`K-b`.  We treat the two possibilities.

Suppose first that both are poles.  Then

\[
                 K[U]=\{p\}\vee C_5,
\]

where the rim cycle is

\[
                       x_1x_2x_3x_4x_5x_1.
\]

Both `a` and `b` are adjacent to every `x_i` and nonadjacent to `p`; the
edge `ab` is unrestricted.  In `K-x_5` the five sets

\[
       \{a,x_1\},\qquad \{b,x_2\},\qquad
       \{p\},\qquad \{x_3\},\qquad \{x_4\}
\]

are connected and pairwise adjacent.  They are therefore branch sets of a
`K_5`-minor model.

Suppose instead that both deleted vertices are rim vertices.  Now

\[
                 K[U]=\overline {K_2}\vee P_4.
\]

Write `p,q` for the nonadjacent poles and

\[
                         x_1x_2x_3x_4
\]

for the path.  The pair `p,q` is the unique nonadjacent pair among the four
degree-four vertices of `K[U]`, so the two pentagonal-bipyramid
representations identify the same pole pair and the same path, up to
reversal.  Each of `a,b` is adjacent to `p,q,x_1,x_4` and nonadjacent to
`x_2,x_3`; again `ab` is unrestricted.  In `K-x_2` use

\[
       \{a\},\qquad \{x_1\},\qquad \{p\},\qquad
       \{b,x_4\},\qquad \{q,x_3\}.
\]

The last two sets are connected.  The pole--path contacts, the two restored
rim contacts from each of `a,b`, and the path edge `x_3x_4` verify all ten
pairwise adjacencies.  These five sets form a `K_5`-minor model.

Thus one of the two displayed deletions supplies the required model in
every case.  \(\square\)

## 2. Application to two free root choices

Use the setting of the audited
[dual-free-root response-star theorem](hc7_order8_dual_free_root_response_star.md).
Thus `G` is seven-connected,

\[
       \chi(G)=7,
       \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G,
\]

`S` has order eight, and `G-S` has exactly two connected components, each
adjacent to every vertex of `S`.  Fix one edge `e=vx` and one six-colouring
of `G-e`.

Assume that the order-seven and strict order-eight response-side outcomes
do not occur.  The dual-free-root construction gives eight pairwise
disjoint connected latent columns

\[
                 K_s\qquad(s\in S)
\]

with contact graph `K`, including two nonresponse labels `a,b`.  For every
label `r`, consuming `K_r` gives two adjacent connected roots, each
adjacent to every one of the other seven columns.

### Theorem 2.1 (low-degree alternative for one free-root choice)

If `G` has no `K_7` minor, then at least one of `K-a` and `K-b` has a
vertex of degree at most three.

### Proof

For either `r in {a,b}`, a `K_5` minor in `K-r` would lift through the
seven surviving columns and the two roots obtained by consuming `K_r` to
an explicit `K_7`-minor model in `G`.  Hence both `K-a` and `K-b` are
`K_5`-minor-free.

Apply the audited
[seven-column contact theorem](hc7_seven_column_contact_structure.md) to
each graph.  If either has a vertex of degree at most three, the conclusion
holds.  Otherwise both graphs are pentagonal bipyramids.  Theorem 1.1 then
gives a label `r` for which `K-r` contains a `K_5` minor.  Consume `K_r`
and lift that model as above, contradicting the exclusion of a `K_7`
minor.  \(\square\)

## 3. Exact gain and trust boundary

Theorem 2.1 strictly strengthens the previously proposed source-selection
corollary.  It eliminates the entire simultaneous pentagonal-bipyramid
branch before any response path is analysed.  No source--target noncontact,
column split, or contact-maximization argument is needed in that branch.

The surviving low-degree vertex need not be the target, a response source,
or the remaining nonresponse label.  Its at most three neighbours are
**column labels** representing connected subgraphs of unbounded order; they
do not constitute a host separator of order at most three.  The result
therefore does not prove a bounded separation, a common boundary partition,
or a strict response-preserving descent.  Those are precisely the remaining
obligations in the low-degree response-column branch.
