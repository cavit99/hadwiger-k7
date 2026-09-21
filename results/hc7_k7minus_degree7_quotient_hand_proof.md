# An elementary nine-vertex minor lemma

**Status:** written proof; [separate internal audit](hc7_k7minus_degree7_quotient_hand_proof_audit.md).

## Lemma (nine-vertex quotient)

Let `R` be a finite simple graph on seven vertices with minimum degree at
least four. Add a vertex `v` adjacent to every vertex of `R`, and another
vertex `c` adjacent to at least six vertices of `R`. No edge `vc` is
required. The resulting graph contains a `K7^-` minor.

### Proof

Delete edges if necessary so that `vc` is absent and `c` misses exactly
one vertex `x` of `R`. The complement `F` of `R` has maximum degree at
most two. Add edges to `F` until it is edge-maximal subject to this bound,
obtaining `F'`. Replacing `R` by the complement of `F'` only deletes edges,
so a minor in the resulting graph also exists in the original graph.

Every component of `F'` is a path or a cycle. A path of order at least
three could be closed into a cycle, and two distinct path components
could be joined at vertices of degree less than two. Maximality therefore
leaves only cycles and at most one additional `K1` or `K2`. On seven
vertices the possible forms are exactly

```text
C7, C4 + C3, C6 + K1, C3 + C3 + K1, C5 + K2,
```

where `+` denotes disjoint union. Label cycles consecutively as below.
Automorphisms leave nine possible positions of `x`: one for `C7` and
two for each other form. The following seven rows cover them all;
two rows each cover two choices. Concatenated labels denote one bag,
for example `03={0,3}` and `2v={2,v}`.

| Complement `F'` | Missed vertex `x` | Seven branch sets | Only missing pair |
|---|---|---|---|
| `C7(0,...,6)` | `0` | `03,15,2,4,6,v,c` | `v:c` |
| `C4(0,...,3) + C3(4,5,6)` | `0` or `4` | `04,1,25,3,6,v,c` | `v:c` |
| `C6(0,...,5) + K1(6)` | `0` | `024,1,3,5,6,v,c` | `v:c` |
| `C6(0,...,5) + K1(6)` | `6` | `02,1,3,4c,5,6,v` | `02:1` |
| `C3(0,1,2) + C3(3,4,5) + K1(6)` | `0` | `03,14,2,5,6,v,c` | `v:c` |
| `C3(0,1,2) + C3(3,4,5) + K1(6)` | `6` | `03,1c,2,4,5,6,v` | `4:5` |
| `C5(0,...,4) + K2(5,6)` | `0` or `5` | `05,1,2v,3,4,6,c` | `3:4` |

In every row the seven bags are disjoint and connected, and all pairs
except the indicated pair are adjacent. For example, in the first row
`03` and `15` are edges of the complement of `F'`; together with the
singleton bags `2,4,6`, they are pairwise adjacent. Both `v` and `c` are
adjacent to all five bags. The other rows are checked in the same way.
Contracting the bags gives a `K7^-` minor. QED

## Provenance and scope

This replaces the [earlier computer-assisted proof](../active/hc7_k7minus_degree7_common_neighbour_exclusion.md#lemma-1-nine-vertex-quotient)
of the same lemma. That note, its audit and the
[232-case verifier](../active/hc7_k7minus_degree7_quotient_verify.py)
remain unchanged as corroborating records. The complement-maximalisation
argument also appears in the repository's
[eight-vertex complement lemma](hc7_k7minus_degree_eight_triangle_poor_edge_packing.md#lemma-1-the-eight-vertex-complement-lemma).

No computation is required to verify this proof. The lemma concerns nine
vertices; the [global theorem](hc7_k7minus_bilight_extremal.md#8-the-extremal-theorem-and-six-colour-corollary)
separately proves the reduction from arbitrary host order and lifts the
model through a fixed connected contraction preimage.
