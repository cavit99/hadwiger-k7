# Cold audit: complete transfer in the two-root rooted-`K_4` orientation

**Verdict:** **GREEN** at the pinned revision below.  This is an independent
internal audit, not external peer review.

## Pinned source and dependencies

```text
f3060dc4004438bbe963f3b65ff50f1a8bc54b86453f42d50b2407eddfb9af58
  active/hc7_k7minus_sparse_sixcut_rooted_k4_two_root_transfer_completion.md
99b59c50f39b43653348997e137d799ff47d8c9e7f402b8dc330e481fd424416
  active/hc7_k7minus_exact_six_two_packet_transfer_obstruction.md
fd9bb404244c0dc247a9d30480e83bfec356ca2d686a64f23e91cfa5164cfc46
  active/hc7_k7minus_exact_six_two_packet_transfer_obstruction_cold_audit.md
9e1742e20e89f1df3cdb02f944873cc48dbc61bb6830e8e1a8be16b50b214eb1
  active/hc7_k7minus_exact_six_residual_portal_collapse.md
3df2585010cd685c346a1149b36bf89fe9ec95c1dfab0b0a7222e54dd765dd1d
  active/hc7_k7minus_exact_six_residual_portal_collapse_cold_audit.md
557b10d311f008962a1d0d65ba713a6f1c02d2b5dcdd74c7f5ce26baedbd65c9
  active/hc7_k7minus_exact_six_residual_minus_four_descent.md
6c998571d6152a0faa671281d210acd0f6b8b226d048ff32cb98984654cd2eea
  active/hc7_k7minus_exact_six_residual_minus_four_descent_cold_audit.md
6118da0fbbca965c241c8ff5259552744f96c2364d50f95ef0a8b87355be168c
  active/hc7_k7minus_sparse_sixcut_rooted_k4_portal_descent.md
55f1b477cc665f633ca036d06e373d44c1c559f71ddc98fc6f312aa12ce94262
  active/hc7_k7minus_sparse_sixcut_rooted_k4_portal_descent_cold_audit.md
```

All hashes match the files checked.  Relative to the initially audited
source
`e1e08f683dfdbf350eb9dc33e127ddd71720242d3b7363df55c63fe05f31650f`,
the final source changes only the status from audit-pending to independently
cold-audited; its statements and proofs are unchanged.

## 1. Collapse of the model bags

Assuming transfer fails gives `mu_S(C)=1`, so the pinned transfer theorem
places the configuration in the residual `(2,0,1)` row and the portal
collapse gives `C-L={r_1,r_2}`.  The four rooted bags are disjoint from
`L`, use no boundary vertices beyond their four prescribed roots, and every
portal belongs to one of the two support bags.  There is consequently no
unaccounted internal vertex, and the exact forms

```text
M_1={z_1} union R_1,  M_2={z_2} union R_2,
M_3={x_3},            M_4={x_4}
```

follow, with `R_1,R_2` a partition of the two portals.

If the portals are split, each support edge from its root to its portal is
required.  If both portals lie in one support bag, a connected graph on its
root and two portals has at least two of the three possible internal edges.
All these edges are counted by `e+z`, where `z` includes every portal
incidence with the common-root set.  Hence `e+z>=2`.  Combining this with
the independently audited `e+c+z<=2` correctly forces

```text
c=0,  e+z=2.
```

The relabelling in the split case is simultaneous: exchange the portals,
their matched `Q` roots, and the two corresponding singleton model bags if
needed.  It therefore preserves the literal matching and puts the portal
in `M_i` under the name `r_i` without changing the argument.

## 2. Split-support allocation

With `M_1={z_1,r_1}` and `M_2={z_2,r_2}`, connectedness consumes both
units of `z`; hence the portal edge, all other common-root incidences, and
both crossed `R`--`Q` edges are absent.  The model contacts then have only
the following possible suppliers:

```text
M_1M_2: z_1z_2,    M_1M_4: z_1x_4,
M_2M_3: z_2x_3,    M_3M_4: x_3x_4.
```

Thus all four displayed edges are genuinely forced.  In allocation (11),
the last five bags are a clique: the four forced edges, the two support
edges, and the fullness of `A` cover all ten pairs.  Each packet sees the
two singleton support roots, the two portal-containing bags, and
`A union {p}` through the five distinct boundary duties
`z_1,z_2,r_1,r_2,p`.  The packets need not contact one another, so precisely
that one pair may be absent.  Connectedness and disjointness of all seven
bags are immediate from their shores and the two matching edges.

## 3. One-support allocations

Suppose both portals lie with `z_1`.

If the portal edge is present, `e+z=2` leaves exactly one portal--common-root
incidence.  In allocation (12), the first packet sees all four common roots
and both portals.  The second packet, and the two outer-component bags, are
made connected by their displayed common roots.  Packet and outer fullness
makes the first four bags universal.  Among the final three, the portal
edge supplies their portal-bag contact and the unique common-root incidence
joins the singleton to one portal bag.  At most the other pair is absent.

If the portal edge is absent, connectedness of the three-vertex support bag
forces both `z_1r_1,z_1r_2`, exhausting `z=2`.  There is no other
portal--common-root edge.  The `M_1M_2`, `M_2M_3`, `M_2M_4`, and `M_3M_4`
contacts therefore force respectively

```text
z_1z_2,  z_2x_3,  z_2x_4,  x_3x_4.
```

Using allocation (11), these four edges and the two support edges again
make the four non-outer rooted bags a clique; fullness of `A` supplies all
contacts involving `A union {p}`.  Both packets meet all five bags through
their `T` duties.  Only the packet pair may be missing.

The split allocation and the two one-support subcases exhaust every
partition of two portals between two support bags.  Every contradiction is
a literal seven-bag `K_7^-` model; no artificial completed-boundary edge is
used.

## 4. Conclusion and scope

Failure of two-packet transfer is impossible, so the selected two derived
packets force `mu_S(C)>=2`.  The general five-packet cap gives the stated
equality two, although only the lower bound is needed for the theorem.
Hereditary rerooting then makes the `k=2` outcome terminal in the stated
fragment-closed induction.

The proof is unbounded and computation-free.  It does not treat the
three- or four-exchanged-root orientations or supply the local excess
dichotomy that produces the two derived packets.  Within its stated scope,
no defect was found.
