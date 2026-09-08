# Separator allocation in the two-triangle case

**Status:** written proof; the adjacent audit records its separate verdict
and exact source hash. The entire
three-cut case and the remaining global colouring conclusion are open.
All graphs are finite and simple; set neighbourhoods are external.

Throughout, let `G` be seven-connected, with `delta(G)>=8`, no
`Q=K_7` minus two independent edges as a minor, and `d(v)=8`. Write
`N(v)=A dotcup B dotcup {x,y}`, where `A,B` are triangles and `xy` is
an edge. Additional edges are allowed. Put `H=G-v-B`.

## Inputs

The following written inputs have adjacent internal audits; no new
literature inspection or finite enumeration is used here.

- [Contraction closure, Corollary 3](../active/hc7_companion_contraction_closure.md),
  SHA-256 `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`:
  a vertex outside the literal clique `{v} union B` has at most two
  neighbours in it. In particular `delta(H)>=6`.
- [Five-root wheel, Corollary 3](hc7_five_root_wheel.md),
  SHA-256 `f0fbab79d23d8079b91ff1a812b83db96059aa4fb0024c809b1037f3f533f62a`:
  a three-cut of `H` contains at most one neighbour of `v`.
- [Degree-free wheel, Lemma 1](hc7_degree8_two_triangle_exterior.md),
  SHA-256 `e51564c9ffd857d15eb3d1de9c5cfa4ce9b9bfac514ac3188ac5379e2a745776`:
  five roots including a triangle, at least two nonroots, and boundary
  at least five for every nonempty nonroot set give a rooted `W_4`.
- [Five-root almost-clique, bounded-deficit extension](hc7_five_root_almost_clique.md),
  SHA-256 `de183e350c412739c05a744e811304454ba90856efee9e097813c70617bba9cd`:
  the same boundary condition, nonroot minimum degree six, and at most
  five degree-six nonroots give all five-root contacts except possibly
  one joining a designated triangle root to either other root.
- The actual-port argument is recorded in
  [the helper audit](../active/hc7_companion_helper_construction_audit.md), SHA-256
  `73b9e61aee4c11d0a3c9025e4976ee4e26f196778c3e30c939c8617ab05e5601`,
  pinning helper source `0c1ac8052f7734d8d0267381c030e177bd70010eded63d15fdca8c0db6d1f375`.
  We give its application below; we do not invoke singleton normalization
  for an insufficiently connected host.

## 1. Every A-side is two-connected

**Theorem 1.** Let `T` be a three-cut of `H`. Then `H-T` has exactly
two components `L,O`, containing `A-T` and `{x,y}-T`, respectively.
Both are full to `{v} union B union T`, and `L` is two-connected.

**Proof.** Deleting four vertices from `G` gives three-connectivity of
`H`. Every component of `H-T` is full to the displayed seven-set: a
missed vertex would leave an actual boundary of order at most six.
Each component therefore contains a neighbour of `v`. The cut restriction
leaves the surviving `A` triangle connected and the surviving `xy` edge
connected, so there are exactly the two stated components. Each has at
least four vertices, since a vertex in either has at most three neighbours
outside that component in `H`, while `delta(H)>=6`.

The torso `K=H[L union T]+K_3(T)` is three-connected. Indeed, after
deleting at most two vertices, the surviving vertices of `T` form a
clique; any component not reaching that clique would also be separated
in `H` by those deleted vertices.

Suppose `z` is a cutvertex of `L`. The nonempty set `A-(T union {z})`
lies in one component `L_A` of `L-z`. Choose another component `L_0`;
it contains no neighbour of `v`. If `T` avoids `A`, choose two distinct
vertices of `A-{z}`. Two-connectivity of `K-z` gives disjoint paths from
them to distinct vertices of `T`. Stop at the first `T` vertex: their
prefixes lie in `L_A`. If `T` contains `a* in A`, retain `a*` as one
endpoint. Connectivity of `K-{z,a*}` supplies a path from a remaining
`A` vertex in `L_A` to `T-{a*}`, again stopped at its first `T` vertex.
This also covers `z in A`. In either case call the two chosen cut roots
`t1,t2`, and the omitted cut root `t3`.

In `F=G[L_0 union B union {t1,t2}]`, every nonempty subset of `L_0`
has at least five neighbours: its original neighbours lie in
`L_0 union B union T union {z}`, and only `z,t3` were removed.
Also `|L_0|>=3`, since its vertices have degree at least six in `H`
and at most four neighbours outside `L_0`. Apply the degree-free wheel.
Extend its two `T`-root bags along the chosen paths with their final
`T` vertices omitted, or retain the singleton `a*` endpoint. These
extensions are disjoint from the wheel's nonroots and from each other.

The connected bag `D=O union {t3}` is disjoint from all five extended
bags and contacts each through its original `B` or `T` root. The vertex
`v` contacts them through `B` and the retained `A` vertices, and contacts
`D` through `{x,y}-T`. Thus `{v},D` are full adjacent apices over the
wheel, giving `K_2 join W_4=Q`, a contradiction. QED

## 2. A minimal A-side has a four-connected torso

**Theorem 2.** Choose a three-cut `T` minimizing the order of its A-side
`L` over all three-cuts of `H`. Then `K=H[L union T]+K_3(T)` is
four-connected.

**Proof of the torso assertion.** Theorem 1's argument gives
three-connectivity. If `Z` were a three-cut of `K`, then `T-Z` would
be nonempty: deleting `T` leaves the connected graph `L`. All of `T-Z`
lies in one component of `K-Z`. Any other component `C` lies in `L`
and is also separated by `Z` in `H`. By Theorem 1 it contains `A-Z`,
since the surviving `xy` vertices remain on the original opposite side.
Thus `C` is the A-side of this new three-cut. It is a strict subset of
`L`: equality would force `Z` to be disjoint from `L`, hence `Z=T`.
This contradicts the choice of `L`. QED

## 3. A full five-root packet is terminal

Retain the minimal A-side choice, write `T={t1,t2,t3}`, and put
`F_C=G[C union B union {t1,t2}]` for `C=L,O`. Each such five-root
graph has nonroot boundaries at least five and nonroot degrees at least
six. A degree-six vertex must be one of its at most three neighbours
of `v`, since only `v,t3` were deleted from its original neighbourhood.
Thus the bounded-deficit almost-clique theorem applies on either side.

**Packet normalization.** For either full rooted five-clique models or
models allowing only one missing contact from a fixed `b in B` to
`t1` or `t2`, maximize the union `W` of the two `T` bags, then minimize
the three `B` bags. Each `B` bag has one actual port to `W`, and is
a path from its prescribed root to that port. When both `T` bags are
contacted, distinct ports give a nonroot contact leaf in a minimal
root-and-ports tree. Moving it to its helper retains both contacts via
the other port and the old tree edge, contradicting maximality. When
only one helper is contacted, a shortest root-to-contact path has just
one port. Literal `B`-triangle edges preserve all other required contacts.
No unused component contacts `W`, since it could be absorbed. In the
designated-one-hole class, the `b` bag is singleton: moving a nonroot
port to a contacted helper either preserves the existing allowed hole
or creates exactly one allowed hole at `b`.

We will use two actual-boundary observations. If `X=W-{t1,t2}` is
nonempty and `v` misses `W`, its boundary in `G` lies in the three
`B` ports together with `T`, of order at most six. The opposite side
survives, a contradiction. On the minimal side `L`, an empty `X` also
cannot have at most two ports in `L`: deleting those ports and `t3`
separates nonempty `L` minus those ports from `O`. By three-connectivity
this is a three-cut; Theorem 1 makes its component inside `L` a strictly
smaller A-side. Here `|L|>=4` ensures nonemptiness.

**Theorem 3.** If `F_L` has a `B union {t1,t2}`-rooted `K_5` model,
then `G` has a `Q` minor. Consequently no such full model exists under
the standing hypotheses.

**Proof.** Normalize in the full-clique class. If `v` contacts its
`T` union, the connected bag `O union {t3}` is full to all five bags
and adjacent to `v`. The latter misses at most the other `T` bag,
giving `K_7^-` and hence `Q`.

Otherwise the first boundary observation makes both `T` bags singleton.
The second forces all three `B` ports `p_i` to lie in `L`. The three
root bags are disjoint paths `P_i` from `b_i` to `p_i`; both `t1,t2`
see every `p_i`, and neither has any actual neighbour in `B`. Write
`P_i^o=P_i-{b_i}`, three nonempty connected paths in `L`.

Choose an `A` root in `L`. Contract the three paths `P_i^o` separately
inside connected `L`, and take a minimal tree spanning their three
images and the chosen A-root image. Some marked path image is a leaf
different from the A-root image. Deleting that leaf and lifting the
remaining tree shows that, for some `k`, a component `D` of `L-P_k^o`
contains the other two whole paths and an A root. Since `L` is connected,
`D` also has an edge to `P_k^o`.

On the opposite side `F_O`, apply the almost-clique theorem designating
`b_k`, and normalize in its allowed one-hole class. Its `b_k` bag is
singleton. The `T` union has nonempty interior, because singleton `T`
bags would have no contact to `b_k`, whereas at least one is required.
The first boundary observation therefore forces `v` to contact a `T`
bag of this opposite-side model.

Append the original path `P_k^o` to its `b_k` bag. This is connected
through the original edge at `b_k`, and `p_k` supplies both `T` contacts,
repairing its sole possible hole. The five new bags form a rooted `K_5`.
The disjoint bag `D` contacts the other two `B` bags through their
original root-to-port paths, the enlarged `b_k` bag through `P_k^o`,
and both `T` bags through the other common ports. Also `vD` is present
through its A root. Thus these five bags, `D` and `{v}` have at most
one missing contact, from `v` to an uncontacted `T` bag, and give `Q`.
No vertex of the opposite component used in its model is assigned to
`D`; every appended path has its fixed disjoint original preimage. QED

**Corollary 4.** No two vertices of a minimal A-side cut `T` have a
common neighbour in `B`. Indeed, designate that neighbour in the
almost-clique theorem on `F_L`. Its two allowed missing positions are
literal root edges, so it supplies the full packet forbidden by Theorem 3.

**Normalized one-hole packet.** For any designated `b in B`, normalize
the almost-clique model on `F_L` in its allowed one-hole class. Its
`b` bag is singleton. Its `T` interior is nonempty by the two-port
observation, so `v` contacts the union. Exactly one `T` bag is contacted,
and the core's sole missing edge joins `b` to the uncontacted bag:
a full core is excluded by Theorem 3; otherwise adjoining
`O union {t3}` and `v` gives `Q` if both T bags are contacted or if
the missing core edge is incident with the contacted one. This does
not prove a transfer repairing the remaining aligned pair of holes.

Choose `t1,t2` outside `N(v)`, which is always possible. Then all of
`A-T` lies in the contacted, full `T` bag `U`. Indeed, `U` contains an
A root. Any other A root outside `U` cannot lie in the uncontacted bag
or an unused component; its A edge into `U` makes it the unique port
of a non-designated B bag. Transfer that port to the other T bag `V`.
Its old path edge retains `V`'s contact with that B bag; only `U`'s
contact to that root may be lost. This loss and the old `Vb` hole have
distinct B ends. Both T bags now meet `N(v)`, so their rooted wheel,
`O union {t3}`, and `v` give `Q`, a contradiction.

## 4. Exact scope

These are structural conclusions; proper-minor six-colourability was not
assumed. If it is assumed and `chi(G)=7`, the existing independent-cut
argument also excludes independent `T`: contract the opposite component
together with `T` to obtain each closed-side colouring with the same
boundary partition, namely the four singleton roots `{v} union B` and
the independent block `T`; align and glue those colourings.

The results do not exclude every three-cut of `H`. In particular, neither
the four-connected torso nor separately chosen A-to-port and B-to-port
paths supplies disjoint bags meeting all three sets. A simultaneous
allocation or another global construction remains required.
