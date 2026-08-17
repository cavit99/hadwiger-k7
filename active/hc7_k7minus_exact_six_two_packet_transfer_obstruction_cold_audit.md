# Cold audit: the exact two-root packet-transfer obstruction

**Verdict:** **GREEN** at the pinned revision below.  This is an independent
internal audit, not external peer review.

## Pinned source and dependency

```text
99b59c50f39b43653348997e137d799ff47d8c9e7f402b8dc330e481fd424416
  active/hc7_k7minus_exact_six_two_packet_transfer_obstruction.md
53c91cee74ae8b1f5251e13c14095f8abc65f05625eedb401d3d53173996da15
  active/hc7_k7minus_six_boundary_fragment_rerooting.md
c30aa69b6919edd2cfba80d6df1f02e2c75d38d9544bd87e4332ba4d823526a3
  active/hc7_k7minus_six_boundary_fragment_rerooting_cold_audit.md
```

Relative to the initially audited source
`f669088cb8199000d0ef8b47ddeb3d7fc6b7f1e0a017fc81f7c0997c5e3ce0e1`,
the final source changes only the status from audit-pending to independently
cold-audited.  Its theorem statements and proofs are unchanged.

The cited clean-path and packet-repair comparison hashes also match the
current files.

## 1. Seven-bag terminal composition

For two disjoint `T`-packets `P_1,P_2`, the four bags

```text
P_1 union {z_1},  P_2 union {z_2},  {z_3},  {z_4}
```

are connected and pairwise disjoint.  Packet fullness supplies every one of
their six mutual contacts except possibly `z_3z_4`: in particular,
`P_1` sees `z_2,z_3,z_4`, and `P_2` sees `z_1,z_3,z_4`.

The three further bags

```text
A union {q_1},  D union {q_2},  E
```

are connected and disjoint from the first four.  They form a clique:
`D` sees `q_1`, whilst the `S`-packet `E` sees both `q_1,q_2`.  Each of
them contacts each of the first four through the literal `z_i` in that
bag.  Thus the displayed seven bags lose at most `z_3z_4`, exactly as
claimed.  No adjacency inside the artificially completed clique on `S` is
used.

It follows correctly that, in a target-free host, every `S`-packet in `C`
meets the union of any fixed pair of disjoint `T`-packets.  In particular,
an `S`-packet contained in `C-L` would be disjoint from that pair, proving
`mu_S(C-L)=0` when `mu_T(L)>=2`.

## 2. One-packet linkage extension

The pinned saturated-linkage lemma supplies two mutually disjoint paths in

```text
G[(C-L) union Q]-Z
```

which saturate `R={r_1,r_2}` and `Q={q_1,q_2}`.  After trimming, each path
meets `R union Q` only at its own ends.  Deleting the final `Q`-vertex leaves
a path contained in `C`; this includes its initial portal.  A `T`-packet
`P` has a neighbour at each initial portal, so adjoining both truncated
paths to `P` gives one connected subgraph.  It still sees all four vertices
of `Z` through `P`, and it sees each `q_i` through the deleted path's final
edge.  Hence it is an `S`-packet.

The length-one case is sound: deleting `q_i` leaves the singleton portal
`r_j`, which is joined to `P` and remains adjacent to `q_i`.  All added
vertices lie outside `L`.  Therefore extending one selected member of a
disjoint `T`-packet family leaves it disjoint from every unselected member.

With three derived packets, extend the third and use the other two in the
seven-bag composition.  This proves the target-free cap
`mu_T(L)<=2`; `L` itself supplies the lower bound one because it is connected
and has neighbourhood exactly `T`.

## 3. Packing bounds and the residual vector

The claimed bound `mu_S(C)<=2` is correct.  Three disjoint packets in `C`,
together with the two other `S`-full components, give five disjoint
`S`-packets.  Anchoring four at distinct roots, leaving the fifth bare, and
using the remaining two roots as singleton bags gives seven connected
disjoint bags; every pair contacts except possibly the singleton-root pair.

If `mu_T(L)>mu_S(C)`, the integer bounds force

```text
mu_T(L)=2,        mu_S(C)=1.
```

The first composition then gives `mu_S(C-L)=0`, so `(2,0,1)` is the only
remaining vector.  Every `S`-packet meets `L`, since otherwise it is
disjoint from a fixed derived pair.  It also meets `C-L`: a subgraph wholly
inside `L` cannot see `q_1` or `q_2`, because `N_G(L)=T`.  Finally, two
disjoint one-packet extensions would contradict `mu_S(C)=1`.  These are
precisely the source's crossing and simultaneous-transfer assertions; it
does not incorrectly claim that an original packet meets each member of the
derived pair separately.

## 4. Scope

The proof is unbounded and computation-free.  It resolves the numerical
transfer except for the explicit `(2,0,1)` row in the two-exchanged-root
orientation.  It deliberately does not eliminate that row, assert its
realisation in a `K_7^-`-minor-free graph, or treat the three- and
four-exchanged-root orientations.  No defect was found within that stated
scope.
