# Independent audit of the low-degree incident-source fork

## Verdict

**GREEN** at the exact audited source revision

```text
bcaeaceda7f57fbcf8b28316fcd23b2cd5d838b88ac62698ebb2995f55b5a478  results/hc7_order8_low_degree_incident_source_fork.md
```

The noncontacting-source count, four response signatures, exact trace,
bichromatic fork and clean-bypass absorption are valid under the stated
hypotheses.  This is a separate internal audit, not external peer review.

The only source change after the mathematical audit was replacing the
pending-audit status text with the link to this audit; no theorem or proof
content changed.

The direct dependency revisions checked were

```text
bb78ac1cc61c501a5f871ab9b69a402f765ee333dabe0c9deeff5805bc94a323  results/hc7_order8_dual_free_root_response_star.md
1002b613be45b830372c88dc3f3c7c16d501ab8779f38169976a865ebe8c6e8d  results/hc7_order8_arbitrary_edge_response_star.md
720b3a93f646f4515824c01f3da1ec7ce9ba90694d0227585c498d2740f6617c  results/hc7_six_vertex_source_rooted_k4.md
5d5a5eda08701262a1bf6b821194aacd7192a41f0ecf997134764b5b59c80961  results/hc7_shared_interface_bichromatic_bypass.md
```

## 1. Source selection and literal nonadjacency

A source of contact degree at most three already uses one contact on the
target.  Among the four other sources and the auxiliary label it therefore
has at least three nonneighbours, at least two of which are sources.  Since
contact-graph nonadjacency means literal anticompleteness of the columns,
the corresponding first neighbours of the common vertex are nonadjacent.
The two incident edges can consequently be contracted simultaneously and
expanded without creating an unrecorded edge between their outer ends.

## 2. Colouring table and exact trace

The original edge-deletion colouring gives the first signature.  Colouring
each single-edge contraction and the two-edge star contraction gives the
other three.  All four colourings restrict to the common graph with the
three displayed edges deleted.  An all-proper signature would restore all
three edges and six-colour `G`.

The two-edge contraction colouring is correctly retained on
`G-{f_i,f_j}`, not merely on the graph with the original edge also deleted.
Every other neighbour of the common vertex remains adjacent to the
contraction image, so the stated two-vertex monochromatic neighbourhood is
exact.

The hypotheses of the cited incident-edge theorem now match literally:
the outer ends are nonadjacent, the star contraction is a proper minor, and
the host is not six-colourable.  Its saturation components and bypass live
in `G-{f_i,f_j}`, and its two component switches give the claimed opposite
one-edge responses.

## 3. Clean bypass absorption and scope

After truncation, anticompleteness of the endpoint columns makes the path
interior nonempty.  If the interior avoids every old root and column, adding
it to one endpoint column preserves connectedness, disjointness, labels,
root contacts and all old contacts while adding the missing source-source
contact.  A resulting contact-graph `K_5` model lifts with the two roots to
an explicit `K_7` model; otherwise the contact count strictly increases.

The theorem does not align the simultaneous-contraction colouring with the
original boundary partition, assign the saturated palette paths to all
column labels, or solve a dirty encounter.  Its stated stopping point is
therefore accurate.
