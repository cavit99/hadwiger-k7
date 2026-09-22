# Separate internal audit: excluding the split-clique Ore core

**Verdict: GREEN** for the structural theorem in
[Excluding the Ore core in the split-clique frame](hc7_split_clique_ore_core.md),
at SHA-256

```text
9948d60a5f425edc94ac05592178db2c7ae06e1f52a0bd9ac769fb32896ca468
```

This is an independent reconstruction by a separate internal agent, not
external peer review. The mathematical source was first examined at
SHA-256 `248641e06c0a2b532902f9b2d5a2215e43d14a0cf7920b34e66b93f088bc969c`.
Only its status and links were then prepared for promotion; the statement
and proof are unchanged. The verdict covers the final hash above.

## Exact statement checked

For every finite seven-connected graph `G`, suppose disjoint sets `A,E,D`
have orders `2,3,4`, respectively; `R=A union E` is a five-clique; `D`
is a four-clique; and distinct vertices `u,b,y` lie outside `R union D`.
Assume

```text
N_G(u)=A union D union {b},
b is adjacent to every vertex of A,
y is adjacent to every vertex of E union D.
```

Then `G` contains a `K7` minor. No bound on the number of further vertices
and no other nonadjacency hypothesis is used.

## Independent reconstruction

Take `H=R union D union {u,y}` and let `C0` be the component of `G-H`
containing `b`. For any component `C` of `G-H`, its external neighbourhood
lies in `H`. If it had at most six vertices, removing that neighbourhood
would leave `C` separated from some vertex of the eleven-set `H`. This
contradicts seven-connectivity. Thus each component has at least seven
distinct boundary vertices; counting edges would not suffice.

The only neighbour of `u` outside `H` is `b`. Consequently a component
other than `C0` has no `u` contact. If it also had no `D` contact, its
boundary would lie in the six-set `R union {y}`, which is impossible.
This proves the required connection from every auxiliary component to
`D` without any assumption on its internal structure or size.

Let `F` be the vertices of `E` with no edge to `C0`, and let `m=|F|`.
The component `C0` has both `A` contacts through `b`. For `m=0`, it is
therefore adjacent to all five roots. Any `d in D` gives a second connected
set `{u,d,y}`, adjacent to all five roots and to `C0` through `ub`.

For `m>0`, put `B=N_G(C0) intersection D`. Outside `D`, the boundary of
`C0` is contained in the `(7-m)`-set
`{u,y} union A union (E-F)`. Therefore `|B|>=m`.

Each `r in F` has at most five neighbours in `H-D`: the four other roots
and `y`; the exact neighbourhood of `u` excludes `ru`. Seven-connectivity
implies minimum degree at least seven, so `r` has a neighbour in `D` or
outside `H`. In the former case select that `D` vertex. Otherwise, take a
component adjacent to `r` outside `H` and select one of its `D` contacts.
This component is not `C0`, by the definition of `F`, so the preceding
boundary argument applies.

Let `D0` collect the selected `D` vertices. It is nonempty and has size
at most `m`. If it meets `B`, no further vertex is needed. If it misses
`B` and `m<=2`, adding one vertex of `B` gives at most three vertices.
If it misses `B` and `m=3`, then `|B|>=3` inside the four-set `D`, so
the nonempty set `D0 subseteq D-B` has size one. Adding a vertex of `B`
then gives only two vertices. Hence a set `D1` containing all selected
contacts and at least one `C0` contact always has size at most three.

Let `W` consist of `C0`, `D1` and all the selected auxiliary components.
The set `D1` is a nonempty clique, every selected component attaches to it,
and `C0` attaches to it. Thus `W` is connected. The component `C0` supplies
the two `A` contacts and every `E-F` contact; the selected direct edge or
auxiliary component supplies each `F` contact. Auxiliary components need
not be distinct: reusing a component only identifies part of the same
branch set and causes no ownership conflict.

Choose `d* in D-D1` and take `T={u,d*,y}`. Its edges `ud*` and `d*y`
make it connected. It sees `A` through `u` and `E` through `y`.

## Disjointness and all 21 contacts

The seven branch sets are the five singleton vertices of `R`, together
with `W` and `T`. Every component used in `W` lies outside `H`; its only
vertices of `H` are in `D1`. The set `T` lies in `H-R`, and its `D` vertex
is outside `D1`. Hence all seven branch sets are nonempty, connected and
pairwise disjoint. This also applies to the `m=0` construction, with
`W=C0`.

| Pairs of branch sets | Number | Witness |
| --- | ---: | --- |
| Two singleton roots in `R` | 10 | `R` is a five-clique. |
| `T` and a singleton root | 5 | Edges from `u` to `A` and from `y` to `E`. |
| `W` and a singleton root | 5 | The `C0` contacts and the chosen contacts for `F`. |
| `T` and `W` | 1 | The edge `ub`, with `b in C0 subseteq W`. |

These are all `binom(7,2)=21` required adjacencies. No path is required to
avoid vertices belonging to its own branch set, and no connectivity is
inferred from contact with a different branch set. Arbitrary extra edges
consistent with `N_G(u)` preserve the argument.

## Scope and unresolved obligations

No gap or additional hypothesis was found in the structural theorem. It
is a direct construction in the original graph, so there is no induction,
quotient, colouring extension or minor-model lift to validate. The only
general inputs are the definition of seven-connectivity and its elementary
minimum-degree consequence.

This audit does not establish that an arbitrary list-critical instance
contains the stated literal five-clique and vertex `y`, nor does it audit
the separate derivation of this configuration from a list-colouring probe.
The result closes this precise Ore-core configuration. It does not close
the whole split-clique case or prove Hadwiger's conjecture for `K7`.
