# Cold audit: collapse and charge of the residual portal pair

**Verdict:** **GREEN** at the pinned revision below.  This is an independent
internal audit, not external peer review.

## Pinned source and dependencies

```text
9e1742e20e89f1df3cdb02f944873cc48dbc61bb6830e8e1a8be16b50b214eb1
  active/hc7_k7minus_exact_six_residual_portal_collapse.md
a6a903ce09c2503edcbdd860123936d2a1d0789eae554bcb11d89da2c4eeeb42
  active/hc7_k7minus_exact_six_packetfree_complement_orientation.md
a7195eeb02deb61dd3f4a312d421ed77cf704d8dba64d5619d51448d6662f604
  active/hc7_k7minus_exact_six_packetfree_complement_orientation_cold_audit.md
2d71dcc2110efe7aea44889e8671b0e9289d0ce3b25e95407f35574c37b12a42
  active/hc7_k7minus_sparse_sixcut_four_root_carrier_packing.md
998bbf2e0dcfc5cfeeae48c1e95dde464367be1f5a2c2c9b76964a567cdc33fd
  active/hc7_k7minus_sparse_sixcut_four_root_carrier_packing_cold_audit.md
53c91cee74ae8b1f5251e13c14095f8abc65f05625eedb401d3d53173996da15
  active/hc7_k7minus_six_boundary_fragment_rerooting.md
c30aa69b6919edd2cfba80d6df1f02e2c75d38d9544bd87e4332ba4d823526a3
  active/hc7_k7minus_six_boundary_fragment_rerooting_cold_audit.md
99b59c50f39b43653348997e137d799ff47d8c9e7f402b8dc330e481fd424416
  active/hc7_k7minus_exact_six_two_packet_transfer_obstruction.md
fd9bb404244c0dc247a9d30480e83bfec356ca2d686a64f23e91cfa5164cfc46
  active/hc7_k7minus_exact_six_two_packet_transfer_obstruction_cold_audit.md
```

All hashes match the files checked.  Relative to the initially audited
source
`b99242fe49be5acfb898c587062aff742b59d73b17f018babe008eff0585e4bd`,
the final source changes only the status from audit-pending to independently
cold-audited; its statements and proofs are unchanged.

## 1. Carrier collapse

Every component `X` of `C-(L union R)` is, by the pinned orientation
theorem, connected and adjacent to all four vertices of `Z`.  It is disjoint
from `P_1,P_2`, which lie in `L`; those two packets are themselves disjoint
`Z`-carriers because they are `T`-full.  Thus any such `X` would be a third
disjoint `Z`-carrier in the same component `C` of `G-S`, contradicting the
pinned four-root packing cap.  This proves `C-L=R`; no assumption that a
cell meets the two packets individually is used.

## 2. Literal matching and portal restrictions

After the collapse, the saturated linkage lies in the graph on `R union Q`
with `Z` deleted.  A trimmed path has no internal vertex, so the two paths
are literal independent edges and give an `R`--`Q` perfect matching.

If both cross-edges existed, adjoining distinct portals to `P_1,P_2` would
give two disjoint connected `S`-packets: packet fullness supplies all four
`Z`-contacts, while each portal supplies both `Q`-contacts.  This correctly
uses `mu_S(C)=1`.  A portal adjacent to all of `Z` would be a third singleton
`Z`-carrier.  Finally, the orientation theorem's terminal-composition lemma
applies to `{r_i}` when that portal sees both `Q`-vertices, and to
`{r_1,r_2}` when the portal edge is present.  It yields respectively at
most one `Z`-neighbour and at most one *distinct* `Z`-neighbour in the
union.  In the latter row that one root may be adjacent to both portals,
so the source correctly counts at most two incidences rather than one.

## 3. Charge arithmetic

The two obligatory matching edges and at most one cross-edge give at most
three `R`--`Q` incidences.

* With `r_1r_2` present, there is one internal edge and at most two
  `R`--`Z` incidences, so `eta_S(R)<=1+3+2-8=-2`.
* With no portal edge and no cross-edge, the two portal-wise carrier bounds
  allow at most six `Z` incidences, so `eta_S(R)<=2+6-8=0`.
* With no portal edge and one cross-edge, the cross-edge portal has at most
  one `Z`-neighbour and the other at most three, giving
  `eta_S(R)<=3+4-8=-1`.

These cases exhaust the portal edge/cross-edge possibilities and justify
the stated equality condition.  Exact fragment additivity then gives
`eta_S(C)=eta_T(L)+eta_S(R)<=eta_T(L)` with no omitted `L`--`R` edge: those
edges belong to the `eta_T(L)` term.

## 4. Scope

The theorem removes every unbounded or positive-charge complement in the
exceptional two-root transfer row.  It deliberately does not recover the
five units lost when two derived packets collapse to one original packet,
nor assert that an equality profile is realisable in a target-free host.
Within this stated scope, no defect was found.
