# Cold audit: orientation of the packet-free complement

**Verdict:** **GREEN** at the pinned revision below.  This is an independent
internal audit, not external peer review.

## Pinned source and dependencies

```text
a6a903ce09c2503edcbdd860123936d2a1d0789eae554bcb11d89da2c4eeeb42
  active/hc7_k7minus_exact_six_packetfree_complement_orientation.md
99b59c50f39b43653348997e137d799ff47d8c9e7f402b8dc330e481fd424416
  active/hc7_k7minus_exact_six_two_packet_transfer_obstruction.md
fd9bb404244c0dc247a9d30480e83bfec356ca2d686a64f23e91cfa5164cfc46
  active/hc7_k7minus_exact_six_two_packet_transfer_obstruction_cold_audit.md
53c91cee74ae8b1f5251e13c14095f8abc65f05625eedb401d3d53173996da15
  active/hc7_k7minus_six_boundary_fragment_rerooting.md
c30aa69b6919edd2cfba80d6df1f02e2c75d38d9544bd87e4332ba4d823526a3
  active/hc7_k7minus_six_boundary_fragment_rerooting_cold_audit.md
```

All five hashes match the files audited.  Relative to the initially audited
source
`072b69c4ba9c70ef8c4c78226dd0d34b1046fc65d01dc7d40672faae2fc5c188`,
the final source changes only the status from audit-pending to independently
cold-audited; its statements and proofs are byte-for-byte unchanged.
The source's hypotheses are
exactly the exceptional `(mu_T(L),mu_S(C-L),mu_S(C))=(2,0,1)` data supplied
by the pinned transfer theorem, together with a fixed disjoint pair of
`T`-packets.

## 1. The seven-bag decoder

In Lemma 1, a vertex of `E intersect R` contacts both `P_1` and `P_2`, since
both packets see each portal.  The two `Q`-contacts of `E` contact the bags
`A union {q_1}` and `D union {q_2}`, and the selected `Z`-contacts contact
the two singleton-root bags.  Packet fullness supplies all contacts among

```text
P_1 union {z_1},  P_2 union {z_2},  {z_3},  {z_4}
```

except possibly `z_3z_4`.  The two outer full components contact one another
through a literal `Q`-vertex and contact all four displayed bags through
their literal `Z`-vertices.  The seven bags are connected and pairwise
disjoint, and no artificial edge of the completed boundary clique is used.

## 2. Cell contact classification

For a cell `X`, there is no edge to `L`, to another cell, or to another
component of `G-S`; hence `N_G(X) subseteq S union R`.  This neighbourhood
separates the surviving cell from a surviving vertex of either outer full
component, so six-connectivity applies.  Since `X` is connected and
`C-L` is packet-free, it has at most five contacts in `S`.  It must
therefore meet a portal.

With one portal contact, the boundary count is exactly five in `S`.  Two
`Q`-contacts would leave three `Z`-contacts and invoke Lemma 1 after adjoining
the portal.  Thus the five contacts are exactly all four vertices of `Z`
and one vertex of `Q`.  With two portal contacts there are at least four
contacts in `S`; if both `Q`-vertices occurred, at least two `Z`-vertices
would remain and the same decoder would apply.  Hence there is at most one
`Q`-contact and at least three `Z`-contacts.  These deductions exhaust the
integer possibilities.

## 3. Linkage paths and elimination of two-portal cells

After the standard trimming, the saturated `R`--`Q` linkage consists of
two disjoint paths with distinct ends and no extra vertex in `R union Q`.
The path from `r_i` cannot use the other portal, which is the end of the
other disjoint path.  Apart from a possible length-one edge `r_iq_i`, all
of its internal vertices consequently lie in `W`; being connected, they
lie in a single cell incident with `r_i` and `q_i`.  Thus the path-cell
reduction in Lemma 3 is complete.

If a two-portal cell `X` sees one `Q`-vertex, adjoining the other linkage
path (including its starting portal and its internal cell, if any) gives a
connected set which sees both `Q`-vertices and at least three vertices of
`Z`.  The direct-edge case is included because the starting portal remains
adjacent to the deleted `Q` end.  If `X` sees neither `Q`-vertex, adjoining
both paths is connected through the two portal contacts of `X` and supplies
both `Q`-contacts.  Lemma 1 contradicts both cases.  No disjointness or
length-one exception is missing.

## 4. Global orientation and the cell-free exception

Two cells at one portal cannot use different `Q`-vertices: their union with
that portal would meet both vertices of `Q` and all of `Z`.  The same
argument excludes a direct edge from that portal to the other `Q`-vertex.
The saturated linkage therefore assigns distinct `Q` orientations to the
two portals.  A portal with no cell must realise its linkage path by a direct
edge.  If both cell-free portals had both direct `Q`-edges, then

```text
P_1 union {r_1},  P_2 union {r_2}
```

would be two disjoint `S`-packets, contradicting `mu_S(C)=1`; this proves
the precise at-most-one direct-cross-edge exception.

When both portals have cells, their orientations are opposite.  A cell
cannot meet both portals by Lemma 3.  An edge `r_1r_2` would connect one
cell from each side into a Lemma 1 set, so it is absent.  Since every cell
meets exactly one portal, the two portal stars are exactly the two
components of `C-L`, with boundary sets `Z union {q_1}` and
`Z union {q_2}` as claimed.

## 5. Scope

The result is an unbounded, computation-free structural reduction.  It does
not claim that the exceptional packet row exists in a `K_7^-`-minor-free
host, nor that the resulting oriented interface already satisfies the
coefficient-five excess bound.  Within its stated scope, no defect was
found.
