# Independent audit of the unified noncontacting incident-pair normal form

## Verdict

**GREEN** at the exact mathematical source revision

```text
089011bc0c8a13bee24238ec587f888c4ad4de919c4c01867499041ce2289c58  results/hc7_order8_unified_incident_pair_normal_form.md
```

The final source hash is

```text
f1c9bb1131d2ea406c6e2d77395a0c45e3446adf43792aa986507427cd9642be  results/hc7_order8_unified_incident_pair_normal_form.md
```

The subsequent source changes replaced the pending-audit status with this
link and corrected one malformed sentence to the exact neighbour-containment
statement already checked below.  No inference changed.  This is a separate
internal audit, not external peer review.

The direct dependency revisions checked were

```text
1002b613be45b830372c88dc3f3c7c16d501ab8779f38169976a865ebe8c6e8d  results/hc7_order8_arbitrary_edge_response_star.md
bb78ac1cc61c501a5f871ab9b69a402f765ee333dabe0c9deeff5805bc94a323  results/hc7_order8_dual_free_root_response_star.md
d42eb35b88280f98a062c2c231a9e0fac7fe47de8e05bb4e0edac80af35845e6  results/hc7_order8_dual_root_contact_overlap_closure.md
720b3a93f646f4515824c01f3da1ec7ce9ba90694d0227585c498d2740f6617c  results/hc7_six_vertex_source_rooted_k4.md
5d5a5eda08701262a1bf6b821194aacd7192a41f0ecf997134764b5b59c80961  results/hc7_shared_interface_bichromatic_bypass.md
```

## 1. Source selection and response table

If a source misses the target, their seed edges give the required incident
pair directly.  Otherwise the source-rooted `K_4` lemma forces a source of
degree at most three, and the elementary count gives a noncontacting source
mate.  Literal noncontact makes the two outer endpoints nonadjacent.

The two single contractions and the simultaneous two-edge-tree contraction
give exactly `(=,not equal)`, `(not equal,=)`, and `(=,=)`.  An all-proper
signature would restore both edges and six-colour `G`.  Every other neighbour
of the common endpoint remains adjacent to the double-contraction image, so
the exact two-vertex monochromatic trace is correct.

## 2. Bypass and saturation alternatives

The hypotheses of the incident-edge saturation-or-bypass theorem match
literally.  The two component switches have the stated orientations.  In a
clean bypass, truncation removes endpoint-column revisits, and absorbing the
interior preserves all old objects and contacts while adding the missing
contact.

For universal saturation, switching a component which omits the other outer
endpoint gives the asserted named one-edge response.  Otherwise the five
alternate colours give five distinct first edges, none equal to either
deleted edge.  Every neighbour of the operated vertex lies in its old
component or boundary, so the prescribed-first-edge fan theorem applies.

The simultaneous-contraction colouring need not induce the original
boundary partition, and the all-boundary fan preserves only first edges.
The source accurately leaves dirty-column composition and joint-saturation
allocation open.
