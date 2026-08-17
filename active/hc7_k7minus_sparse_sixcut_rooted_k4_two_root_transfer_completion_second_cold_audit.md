# Second independent cold audit: complete `k=2` packet transfer

**Verdict:** **GREEN** at the exact source revision pinned below.  This audit
was rederived independently and is internal review, not external peer review.

## Pinned theorem and inputs

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

All nine hashes match the files checked.  Relative to the originally audited
source
`e1e08f683dfdbf350eb9dc33e127ddd71720242d3b7363df55c63fe05f31650f`,
the final source changes only its status from audit-pending to independently
twice cold-audited.  The theorem statement, allocations, proofs, dependencies,
and scope are unchanged.

## 1. Independent reduction to three portal rows

If transfer failed, the connected full shore `C` would still give
`mu_S(C)>=1`, so failure means `mu_S(C)=1`.  Since two disjoint `T`-packets
are present, the pinned transfer trichotomy gives the exceptional
`(2,0,1)` row, and portal collapse gives

```text
C-L={r_1,r_2}.
```

The four rooted `K_4` bags avoid `L`.  Each prescribed root must lie in its
own bag, and every portal lies in one of the first two support bags.  There
is therefore no possible extra vertex in a model bag, and necessarily

```text
M_1={z_1} union R_1,  M_2={z_2} union R_2,
M_3={x_3},            M_4={x_4},
```

where `R_1,R_2` partition the two portals.  The collapse theorem also gives,
after a simultaneous relabelling, `r_1x_3,r_2x_4`, at most one cross edge,
and the notation `e,c,z` used in the source.

If the portals are split, the two root--portal edges needed to connect the
support bags already give `z>=2`.  If they are together, their exact
three-vertex support bag needs two edges among its root--portal edges and
`r_1r_2`.  Thus in both allocations `e+z>=2`.  The independently audited
quotient inequality `e+c+z<=2` forces

```text
c=0,  e+z=2.
```

This leaves exactly three rows: split portals with `(e,z)=(0,2)`, or one
support bag with `(e,z)=(1,1)` or `(0,2)`.

## 2. Split portals: all twenty-one contacts

Relabel simultaneously so that the seven source bags are

```text
B_1=P_1, B_2=P_2, B_3={z_1}, B_4={z_2},
B_5={x_3,r_1}, B_6={x_4,r_2}, B_7=A union {p}.
```

The support edges use all of `z=2`; hence the portal edge, every other
`R`--`Z_0` edge, and both cross edges are absent.  The rooted `K_4` contacts
then force `z_1z_2,z_1x_4,z_2x_3,x_3x_4`, exactly as the source states.

The ten contacts among `B_3,...,B_7` have the following explicit suppliers:

```text
34:z_1z_2   35:z_1r_1   36:z_1x_4   37:z_1A
45:z_2x_3   46:z_2r_2   47:z_2A
56:x_3x_4   57:x_3A     67:x_4A.
```

For each `i=1,2`, packet fullness supplies `B_iB_3,B_iB_4,B_iB_5,B_iB_6`
through `z_1,z_2,r_1,r_2`, and supplies `B_iB_7` through `p`.  Thus twenty
of the twenty-one pairs are present; only `B_1B_2` may be absent.  The
portal bags are connected by the matching edges, `B_7` is connected by
fullness of `A`, and shores make all seven bags disjoint.

## 3. One support, with the portal edge

Here `(e,z)=(1,1)`.  Let `u` be the unique common-root endpoint of the one
`R`--`Z_0` edge, and put `Z_0-{u}={u_1,u_2,u_3}`.  Allocation (12) is

```text
C_1=P_1, C_2=P_2 union {u_1}, C_3=A union {u_2},
C_4=D union {u_3}, C_5={u}, C_6={x_3,r_1}, C_7={x_4,r_2}.
```

Every displayed union is connected and the bags are disjoint.  A direct
contact census gives:

* `C_1` sees `C_2,C_3,C_4,C_5,C_6,C_7` through
  `u_1,u_2,u_3,u,r_1,r_2`;
* `C_2` sees `C_3,C_4` through the outer components at `u_1`, sees `C_5`
  through packet contact at `u`, and sees `C_6,C_7` at the portals;
* `C_3C_4` is supplied by an outer component at the other's displayed
  root; `C_3` sees `C_5,C_6,C_7` at `u,x_3,x_4`, and `C_4` does likewise;
* `C_6C_7` is supplied by `r_1r_2`, and `C_5` contacts the portal bag
  containing the neighbour of `u`.

Therefore at most the other pair incident with `C_5` is missing.  Again the
allocation is a genuine `K_7^-` model using actual edges only.

## 4. One support, without the portal edge

Now `(e,z)=(0,2)`.  Connectedness of
`M_1={z_1,r_1,r_2}` forces both `z_1r_1,z_1r_2`; equality leaves no other
portal--`Z_0` incidence.  The four remaining rooted-model contacts force

```text
z_1z_2,  z_2x_3,  z_2x_4,  x_3x_4.
```

Reuse the bags `B_1,...,B_7` from the split row.  Packet contacts with
`B_3,...,B_7` are unchanged.  The ten contacts among the last five now have
suppliers

```text
34:z_1z_2   35:z_1r_1   36:z_1r_2   37:z_1A
45:z_2x_3   46:z_2x_4   47:z_2A
56:x_3x_4   57:x_3A     67:x_4A.
```

Thus this row also has every pair except possibly the packet pair.  The
three rows exhaust both partitions of two portals among the support bags.

## 5. Conclusion and exact scope

Every putative `(2,0,1)` return produces a seven-bag `K_7^-` model, so it is
impossible.  Hence the two derived packets force `mu_S(C)>=2`; the general
five-packet cap gives equality two, although the transfer conclusion needs
only the lower bound.  No artificial edge from the completed boundary is
used in any allocation.

The corollary correctly closes only the two-exchanged-root branch after a
separate fragment argument has produced two `T`-packets.  It neither proves
that local excess dichotomy nor handles the three- and four-root exchange
orientations.  Within that stated unbounded scope, no defect was found.
