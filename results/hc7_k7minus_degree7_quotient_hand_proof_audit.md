# Audit: the elementary nine-vertex minor lemma

**Verdict:** GREEN.

**Date:** 21 September 2026.

This separate internal audit independently reconstructed the classification
and checked every displayed minor model. No unresolved gap or computational
premise was found. It is not external peer review.

## Exact sources

| Source | SHA-256 |
|---|---|
| [Research proof](hc7_k7minus_degree7_quotient_hand_proof.md) | `34b881c8b29ca1abfd3d322ee1aa63d7cbc5b7f132aecca7edeb682844af3bd6` |
| [Manuscript proof](../paper/k7minus-six-colour/finite.tex) | `24af117b72808d1675e1e708663d08da708583f925dda38d7c67aa22226092fd` |
| [Global application](hc7_k7minus_bilight_extremal.md) | `4c48b60d4de77de2afc357ba81b47d8f2107656b5684005f743d247f894620d3` |

## Coverage and models

Deleting `vc`, and one edge from `c` if it meets all seven vertices,
reduces to a unique missed vertex `x`. Saturating the complement of `R`
subject to maximum degree two deletes only edges of the host. A minor in
this spanning subgraph therefore gives a minor in the original graph.

In a maximal complement, a path of order at least three could be closed,
and deficient vertices in distinct path components could be joined.
Consequently all components are cycles except possibly one `K1` or `K2`.
Partitioning the remaining order into cycle lengths at least three gives
exactly the five listed forms. Cycle rotations, the swap of equal triangles
and the swap of the two ends of `K2` give the stated nine marked orbits.
No orbit of the missed vertex is lost when the complement is enlarged.

Each table row partitions all nine vertices into seven nonempty bags.
Every two-vertex bag is an edge; the only three-vertex bag, `024` in the
complement of `C6 + K1`, is a triangle. Directly checking all 21 pairs
gives the following sole missing contacts; hence all 20 required contacts
are present.

| Complement | Missed vertex | Only missing pair |
|---|---|---|
| `C7` | `0` | `v:c` |
| `C4 + C3` | `0` or `4` | `v:c` |
| `C6 + K1` | `0` | `v:c` |
| `C6 + K1` | `6` | `02:1` |
| `C3 + C3 + K1` | `0` | `v:c` |
| `C3 + C3 + K1` | `6` | `4:5` |
| `C5 + K2` | `0` or `5` | `3:4` |

In particular, when `c` misses the isolated vertex `6`, the bag `4c`
or `1c` remains adjacent to `6` through its other member. In the final
row the missed vertex lies in `05`, whose other member retains the
contact with `c`. These checks cover the potentially lost attachments.

## Global substitution and scope

The global-source diff replaces the earlier finite proof and its
description, without changing its statement or any other mathematical
argument. The exterior component `C` still contracts to `c`; six-connectivity
gives at least six neighbours in `R`. Replacing `c` in its unique bag by
all of the connected set `C` preserves connectivity, disjointness and every
contact. The original host order is unrestricted. No colouring or prescribed
root condition is discarded: the quotient lemma has an unrooted conclusion.
There is no recursive reduction in the replacement proof.

The old 232-case calculation remains corroboration, not a proof dependency.
The theorem is unchanged; this audit neither strengthens it nor independently
reconstructs the remainder of the global proof.
