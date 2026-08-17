# Cold audit: packet repair of an essential rooted-`K_4` portal

**Audit status:** GREEN.

**Source audited:**
[`hc7_k7minus_sparse_sixcut_packet_repaired_portal_completion.md`](hc7_k7minus_sparse_sixcut_packet_repaired_portal_completion.md),
SHA-256

```text
acd033e17c40df8b791eeb9eb07114c0f558abc3654bf30c9030d12604faf55a
```

The first candidate omitted the clean path's ambient confinement and was
rejected.  The pinned revision repairs that omission explicitly.  This audit
reconstructs the seven bags from the repaired statement.

## 1. Connectivity and ownership

The packet `P_1` sees `z_2`, so it joins the `z_2`-component `K` of
`M_2-r`.  It also sees the other internal portal contained in every `H_i`.
Thus `U` is connected.  Its constituent sets are disjoint: `P_1` lies in
`L`, while `K,H_1,...,H_m` are different components of `M_2-r`.

The path `W` lies in `G[(C-L) union {x_3,x_4}]`, avoids `L`, and meets the
old four-bag model only at `r,y`.  Hence `P_2 union (W-{y})` is connected
through the `P_2`--`r` edge and is disjoint from `U`, `M_1`, `M_3`, `M_4`,
`D`, `E`, `p`, and `q`.

If `U` misses `M_4`, the `M_2` end of an old `M_2M_4` contact lies at `r`
or in a component `H` of `M_2-r` outside `K,H_1,...,H_m`.  In the latter
case connectedness of `M_2` gives an `rH` edge, and `M_4 union H` is
connected through the old `HM_4` edge.  This `H` is disjoint from `U`; it
also misses `W-{y}`, since the latter meets `M_2` only at `r`.  Therefore
all five local bags are pairwise disjoint and connected.

## 2. All local contacts

Nine of the ten local pairs are present in one of the two cases:

| Pair | Contact |
|---|---|
| `B_1B_2` | `z_1`--`P_2` |
| `B_1B_3` | `z_1`--`P_1` |
| `B_1B_4`, `B_1B_5` | old `M_1M_3`, `M_1M_4` edges |
| `B_2B_3` | `P_2`--`z_2` |
| `B_2B_4` | last edge of `W` at `y` |
| `B_3B_4` | hypothesis `U`--`M_3` |
| `B_4B_5` | old `M_3M_4` edge |

If `U` meets `M_4`, then `B_3B_5` is the ninth contact and only `B_2B_5`
may be absent.  If it does not, either the direct `rM_4` edge or the `rH`
edge into the absorbed component gives `B_2B_5`; only `B_3B_5` may then be
absent.  No other pair is lost by the component absorption.

## 3. The eleven outer contacts

The two bags `D union {p}` and `E union {q}` are connected, disjoint, and
adjacent to one another, for example through an `E`--`p` edge.  Each sees

* `B_1`, `B_4`, and `B_5` through the retained boundary vertices
  `z_1`, `x_3`, and `x_4`, respectively; and
* `B_2` and `B_3` through the `p`- or `q`-contacts of `P_2` and `P_1`.

This accounts for all ten outer-to-local pairs and the outer pair.  Together
with the local check, the seven bags miss at most one adjacency and form the
claimed `K_7^-` model.

## 4. Corollary and scope

A saturated linkage prefix has exactly the ambient confinement required in
the repaired hypothesis.  If the `z_2`-component or a component containing a
second portal retained a contact with the first non-support bag met by the
prefix, it would be included in `U` and invoke the theorem.  The two listed
locations for every surviving contact are therefore the exact negation.

In a minimal connector tree, any surviving portal assigned to a duty
separates `z_2` from the selected contact for that duty.  The component beyond
it contains no other portal, so two surviving portals cannot be nested on the
same duty arm.  This justifies the outermost-duty conclusion.

The final scope paragraph is necessary and correct.  Connectivity of `U`
uses the retained boundary anchor `z_2 in N_G(L)`, a feature of the `k=2`
orientation.  No analogous anchor is supplied at `k=4`, and the proof makes
no claim there.
