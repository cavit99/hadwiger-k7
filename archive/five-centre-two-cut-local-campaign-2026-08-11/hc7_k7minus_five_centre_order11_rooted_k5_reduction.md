# The order-eleven atom row reduces to a five-rooted `K_5` obstruction

**Status:** archived written proof, not separately audited and superseded by
the audited elimination of the order-eleven row.  This is a terminal
minor-model implication at equality-shore order eleven.
It does not prove that the five-rooted `K_5` model exists.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## Theorem 1 (five atom roots complete the two poles)

Use the minimally infeasible all-rainbow five-centre two-cut setting, and
suppose that the equality-response component `C` has order eleven.  For
each `z in Z`, let `v_z in C` be the atom vertex supplied by the separately
audited
[order-eleven atom theorem](../../active/hc7_k7minus_five_centre_t5_atom_slack.md#6-the-exact-order-eleven-survivor).

If `G[C]` contains a `K_5` minor rooted at the five distinct vertices

\[
                              \{v_z:z\in Z\},
\tag{1.1}
\]

then `G` contains a `K_7^-` minor.

### Proof

Let `(M_z:z in Z)` be five pairwise disjoint connected branch sets of the
rooted `K_5` model, labelled so that `v_z in M_z`.  The order-eleven atom
theorem gives

\[
 zv_z\in E(G),\qquad pv_z,qv_z\in E(G)
                    \quad(z\in Z).                  \tag{1.2}
\]

Therefore

\[
                              M'_z=M_z\cup\{z\}
\tag{1.3}
\]

is connected for every `z`.  The five sets in (1.3) remain pairwise
disjoint and pairwise adjacent, because the original `M_z` form a rooted
`K_5` model.  They are also disjoint from the singleton sets `{p},{q}`.
Equation (1.2) makes each of `{p},{q}` adjacent to every `M'_z`.

The permitted equality-response colouring assigns one common colour to
`p,q`, so `pq` is not an edge.  Hence

\[
                      \{p\},\quad\{q\},\quad(M'_z:z\in Z)
\tag{1.4}
\]

are seven disjoint connected branch sets with exactly the `pq` adjacency
possibly absent.  They form a `K_7^-` minor model. \(\square\)

## Corollary 2 (exact order-eleven residue)

In a `K_7^-`-minor-free survivor, the eleven-vertex graph `G[C]` has no
`K_5` minor rooted at the five atom vertices.

Thus the order-eleven row is a finite five-rooted-minor problem inside
`C`.  The five separately chosen induced pole paths from the atom theorem
do not yet supply one common rooted model: proving that synchronization,
or returning a smaller response-preserving separation when it fails, is
the remaining step.

## Dependencies and claim status

- The distinct atom vertices, the five edges `zv_z`, and the two pole
  adjacencies at every `v_z` are written and separately audited in the
  order-eleven atom theorem.
- Theorem 1 and Corollary 2 are written proofs in this note.
- No finite enumeration or unbounded existence theorem for the rooted
  `K_5` model is claimed.
