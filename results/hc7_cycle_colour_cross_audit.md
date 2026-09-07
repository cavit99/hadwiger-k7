# Independent audit of the five-colour cycle-cross theorem

**Verdict: GREEN.**

Date: 7 September 2026. This is a separate internal mathematical audit,
not external peer review or a significance assessment.

The complete [source](hc7_cycle_colour_cross.md) was checked at SHA-256
`1057b5ef2a5dda04590b55cfc64128b536a8c831b809847c15ca5b2c235a420a`.
Reversing only its promotion status paragraph exactly recovers the
independently reviewed draft at
`23e95b470b380123dd5385488bbe72fda49f3b4be93a8f22ed4548f5c1d1e269`.
The flexible-root input was checked against disk and its adjacent audit at
`5435c44801978073092cfaef1b685e8b5b52723a52ea28a87e3089d44127ec44`.

## Strongest inference: the recolouring sequence

Theorem 1 applies to any five-colourable graph and a specified five-cycle:
if every colouring with a five-colour palette uses at least four cycle
colours, there are two vertex-disjoint crossing paths with interiors off
the cycle. The proof does not assume planarity or absence of cycle chords.

In the initial rainbow case, the two proposed paths have disjoint palettes
and alternating endpoints. Each palette appears only at its two endpoints
on the cycle, so the paths are cycle-clean. A failed connection permits
the one-vertex boundary recolouring claimed in the source.

In the four-colour state, `P13` and `P14` need not be mutually disjoint;
the proof never uses them as one cross. The `alpha,epsilon` path would
cross `P13` with a disjoint palette. If absent, its component swap leaves
both selected paths unchanged. The later hypothetical `0--3` path crosses
`P14`, and the hypothetical `2--4` path crosses `P13`; again their palettes
are disjoint and their endpoint orders alternate. The `epsilon,gamma`
swap leaves the entire `alpha,delta` subgraph unchanged, so the last
disconnection persists. The resulting pairs `0,3` and `2,4` give exactly
three cycle colours. There are at most four swaps, including the initial
rainbow-to-four-colour step. Every swap acts on the unchanged host.

## Critical application, ownership and limits

Contracting `va` is a proper minor. Its merged vertex is adjacent to all
seven other neighbours of `v`; expanding it only to `a` gives a proper
six-colouring of `G-v` with that colour unique on the neighbourhood.
For every such colouring, deleting its whole independent colour class
`I` leaves a five-colourable graph containing the cycle. Every five-colouring
of this graph extends over `I` using a fresh sixth colour. If the cycle
used three colours, both remaining triangle vertices would have to use
distinct colours absent from the cycle, or `v` could be coloured. This
is precisely the audited three-colour-cycle exclusion after relabelling.

The cross avoids `v` and all of `I`, including the selected triangle root.
Its two paths and four cycle arcs give the asserted actual subdivision.
The fifth cycle vertex lies on a rim arc and is not an unused helper.
The other two triangle roots can lie on the paths or in resulting bags;
crosses from different colourings need not be compatible. No unresolved
gap was found in either theorem or the four-swap bound. A disjoint seven-bag
construction, Conjectures 19 and 21, and `HC_7` remain unproved here.
