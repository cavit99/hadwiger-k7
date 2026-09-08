# Two spanning helpers outside the neighbourhood triangles

**Status:** written proof; a separate internal audit is recorded beside it.
This proves
a rooted five-vertex conclusion in the remaining neighbourhood case, not
that the case is impossible or that Conjecture 19 or HC7 is proved.

Graphs are finite and simple. Write `Q=K_7` minus two independent edges;
set neighbourhoods are external. A rooted model keeps every prescribed
root in a separate connected bag. Extra contacts are allowed.

**Theorem.** Suppose `G` is seven-connected, `delta(G)>=8`, has no
`Q` minor, and `d(v)=8`. Let
`N(v)=A dotcup B dotcup {x,y}`, where `A,B` span triangles and `xy`
is an edge; all other edges are allowed. Put
`W=G-N[v]`, `H=G-v-B`, and `K=H-A=W union {x,y}`.
Then some `r in A` has the following property: `H-r` contains a
`(A-{r}) union {x,y}`-rooted `K_4` model.

**Corollary.** The graph `K` is two-connected. It has a partition into
connected sets `U,V`, containing `x,y` respectively, that are adjacent
and both contact the two vertices of `A-{r}`. At least one also contacts
`r`. Consequently `H` has an `A union {x,y}`-rooted `K_5^-` model with
the three A bags singleton and with `U,V` spanning all remaining vertices.
The assertions hold with `A,B` exchanged. No colouring assumption is used.

## Inputs

The following separately audited sources are used at these exact hashes:

- [Contraction closure, Theorem 1 and Corollary 3](../active/hc7_companion_contraction_closure.md),
  SHA-256 `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`.
  Its [audit](../active/hc7_companion_contraction_closure_audit.md) has SHA-256
  `26b2f5ad7226c7bb3f194cac8523f043d7ae6ca955036249f04ddc9fb6d94394`.
- [The two-triangle exterior theorem and its degree-free wheel Lemma 1](hc7_degree8_two_triangle_exterior.md),
  SHA-256 `e51564c9ffd857d15eb3d1de9c5cfa4ce9b9bfac514ac3188ac5379e2a745776`;
  [audit](hc7_degree8_two_triangle_exterior_audit.md), SHA-256
  `5ff953f5f2b019fee85fb810af8619bae929f8dbd12559ccb01a6f4b1fbeb50d`.
- [Four-connectivity of `H`](hc7_two_triangle_complement_four_connectivity.md),
  SHA-256 `0a75273d2270d5a675e3aa565610d47e375fa89e982b565fbd0ad4f4e5fd3b69`;
  [first audit](hc7_two_triangle_complement_four_connectivity_audit.md), SHA-256
  `d074cc7eb384222f1b68ed53728fd721c7a6e7edbf266c55cec313a5c73b2014`.
- The exact [Norin--Totschnig Theorem 8](https://arxiv.org/html/2507.03244v1#S2)
  rooted-four alternative recorded in the
  [five-root almost-clique source](hc7_five_root_almost_clique.md),
  SHA-256 `de183e350c412739c05a744e811304454ba90856efee9e097813c70617bba9cd`;
  [audit](hc7_five_root_almost_clique_audit.md), SHA-256
  `dc7db3d391ef2701516d64dd32e7546d40e2e4171406193f17d8feadcc4abb47`.
  The primary statement was inspected for that source; no fresh primary
  inspection is claimed here. Its four alternatives are a rooted `K_4`,
  an order-two trisection with two open parts each containing exactly
  one root, a separation of order at most three with all four roots on
  one closed side and at least two nonroots on the other open side,
  or a plane drawing with the four roots on one face.

## 1. A four-root packet

**Lemma 1.** Let `Z` be four roots of `F`, and let the nonroot set
`D=V(F)-Z` be nonempty. If every nonempty subset of `D` has at least
four external neighbours and every vertex of `D` has degree at least
six, then `F` has a `Z`-rooted `K_4` model.

**Proof.** Choose a counterexample minimizing `|D|`. The degree bound
forces `|D|>=3`, and the boundary of `D` forces every root to see `D`.
If a root `a` has only one nonroot neighbour `p`, contract `ap` and
retain the label `a`. Every surviving nonroot degree and every surviving
nonroot-set boundary are unchanged: old `a` has no remaining nonroot
neighbour, and the old vertex `p` is simply replaced by its root preimage.
The nonroot set remains nonempty, giving a smaller counterexample.
Thus each root has at least two nonroot neighbours.

Apply the stated four-root alternative. Its small rooted separation
contradicts the boundary hypothesis. In its trisection, each of the two
open parts containing one root consists of that root alone: its nonroot
subset would otherwise have at most three neighbours. Every nonroot
neighbour of either isolated root lies in the common separator of order
two. The normalization therefore makes both separator vertices `p,q`
nonroots, and both isolated roots `a,b` see exactly these two nonroots.
Contract the disjoint edges `ap,bq`. Every surviving nonroot degree and
boundary is again unchanged, and all four root preimages remain separate.
Since `|D|>=3`, the new nonroot set is nonempty. This is a strict reduction.

For the planar alternative, the normalized graph is two-connected.
After deleting at most one vertex, every component contains a nonroot,
since each root had two nonroot neighbours. If a component has nonroot
set `X`, its boundary is contained in the roots in that component and
the deleted vertex. It must therefore contain at least three of the
four roots. Two components are impossible; the argument without a
deleted vertex also proves connectivity.

The distinguished facial boundary is consequently a cycle containing
the four roots and `h>=0` nonroots. Euler's formula gives

`2e(F) <= 6|D|+10-2h`.

Nonroots contribute at least `6|D|` to the degree sum. Roots have at
least eight incidences with nonroots. Of the facial cycle's eight root
incidences, at most `2h` join nonroots, so the root degree sum is at least
`8+max(0,8-2h)`. The resulting lower bound exceeds the displayed upper
bound by at least six, a contradiction. The remaining alternative is
the rooted clique. Both reductions strictly decrease nonroot order and
lift through disjoint connected root preimages. QED

## 2. An all-A boundary is terminal

The inputs give `W` connected and full to all eight neighbours of `v`,
and `H` four-connected. Contraction closure implies `delta(H)>=6`:
every vertex outside the four-clique `{v} union B` has at most two
contacts into that clique. If `w in W` sees an A vertex, Corollary 3
also gives at most one B contact, so `d_H(w)>=7`.

**Lemma 2.** There is no nonempty `D subseteq W` with
`N_H(D)=A union {q}` for a vertex `q` outside `A union D`.

**Proof.** If `q` were `x` or `y`, no edge would join `D` to `W-D`.
Connectedness would give `D=W`, contrary to `W` contacting the other
edge endpoint. Thus `q in W`. In `G`, the boundary of `D` is contained
in `A union B union {q}`. Seven-connectivity, with `v` surviving outside
the boundary, forces equality. Also `|D|>=2`, since a singleton with
this seven-vertex boundary would have degree seven.

Let `Y` be the component containing `x,y` in
`G-(D union A union B union {q,v})`; the literal edge `xy` puts them
together. There are no edges from `D` to `Y`, and
`N_G(Y) subseteq A union B union {q,v}`. Seven-connectivity forces
at least seven of these eight contacts, and `v` is contacted through
`x` and `y`. Thus `Y` misses at most one vertex of `A union B`.

In the side on `D union A union B`, contract an edge of the triangle
containing that possible missed vertex, using an edge incident with it.
If neither triangle has an omission, choose any edge of either triangle.
There are now five prescribed roots, with the other triangle intact.
For every nonempty subset of `D`, deleting `q` and this one root merger
lose at most two of its original at least seven boundary vertices.
The degree-free wheel lemma applies, since at least two nonroots remain.
The bag `Y` is disjoint from that model and full to its five roots:
the only possible omission was covered by the contracted edge. The
singleton `v` is also full to the five rooted bags and contacts `Y`.
These seven disjoint bags give `K_2 join W_4=Q`, a contradiction. QED

**Corollary 3.** `K=W union {x,y}` is two-connected.

**Proof.** It is connected, and neither `x` nor `y` is a cutvertex,
because `W` is connected and contacts both. If a cutvertex `q in W`
exists, take a component `D` of `K-q` not containing `x,y`. It lies
in `W`, and `N_H(D) subseteq A union {q}`. Four-connectivity of `H`
forces equality, contradicting Lemma 2. QED

## 3. A boundary meeting two A roots returns a rooted clique

**Lemma 4.** Suppose `D subseteq W` is nonempty,
`|N_H(D)|=4`, and this boundary contains at least two A vertices.
Then some `r in A` has the rooted four-clique conclusion of the theorem.

**Proof.** A boundary containing all three A vertices contradicts
Lemma 2. Otherwise write it as `T={s,t,p,q}`, with
`A={r,s,t}` and `p,q` outside `A`. The side `H[D union T]` preserves
all degrees of its nonroots, which are at least six. Every nonempty
subset of `D` has at least four neighbours in this side: it has the
same boundary as in `H`, where four-connectivity applies with the five
vertices `A union {x,y}` outside `D`. Lemma 1 gives a T-rooted `K_4`.

In the two-connected graph `K`, the two-set form of vertex Menger gives
two vertex-disjoint paths joining `{x,y}` to `{p,q}`, bijectively.
Trivial paths are allowed for shared terminals. Stop each at its first
vertex in `{p,q}`. Their interiors avoid `D`, because those two vertices
are its only possible neighbours in `K`; they also avoid `A`.
Attach these paths to the p/q bags of the fixed packet. They are
disjoint from each other and from the packet except at their distinct
endpoints. This gives a `{s,t,x,y}`-rooted `K_4` in `H-r`. QED

## 4. Three root deletions

**Proof of the theorem.** For each `r in A`, put `J_r=H-r`, with four
roots `(A-{r}) union {x,y}`. This graph is three-connected. Each of
its nonroots `w in W` has degree at least six: an r-neighbour had
degree at least seven in `H`, and a non-neighbour loses nothing.
Each of its four roots has degree at least five. Consequently

`2e(J_r) >= 6|W|+20 = 6|V(J_r)|-4`,

so `J_r` is not planar. Suppose none of these three graphs has its
prescribed rooted `K_4`. In the four-root alternative, three-connectivity
excludes the order-two trisection, and the degree count excludes the
planar outcome. Its remaining separation gives a nonempty connected
root-free set `D_r subseteq W` with at most three neighbours in `J_r`.
One may take any component of the separation's open side. In `H`, its
boundary has exactly four vertices and contains `r`. In `G`, its
boundary is contained in these four vertices and `B`; since `v`
survives outside, seven-connectivity makes `D_r` full to `B`.

For any nonempty `X subseteq W`, `|N_H(X)|>=4`: a smaller boundary
would leave at least one of the five prescribed vertices outside it,
contrary to four-connectivity. The function
`f(X)=|N_H(X)|=|N_H[X]|-|X|` is submodular, since closed-neighbourhood
cardinality is a coverage function. If `D_r,D_s` overlap for distinct
`r,s in A`, submodularity and this lower bound give

`f(D_r union D_s)=f(D_r intersect D_s)=4`.

Both `r,s` remain outside the union and retain their edges into it.
Lemma 4 therefore returns a successful rooted clique, a contradiction.
Hence the three sets `D_r` are pairwise disjoint. Their enlargements
`D_r union {r}` are connected, pairwise adjacent by the literal A
triangle, and full to all three B vertices. Together with the three
singleton B roots they give a six-clique model. The singleton `v`
contacts all six bags, giving `K_7` and hence `Q`. This contradiction
proves that some root deletion succeeds. QED

## 5. The spanning two-part form

Fix a successful `r`, and write `A-{r}={s,t}`. In its rooted `K_4`
in `J_r`, maximize the union of the x/y bags, then minimize the s/t
bags. Each latter bag has only one actual vertex adjacent to that union.
Indeed, two different ports allow distinct choices for the two helpers;
a minimal tree through these ports and the prescribed root has a nonroot
contact leaf. Moving it into its contacted helper preserves the other
contact and supplies the first through the old tree edge. The literal
edge `st` retains the contact between the two root bags. This contradicts
maximality. Minimizing each remaining bag makes it a root-to-port path.
No unused component contacts the helper union, since it could be absorbed.

Its boundary in `J_r` thus consists of at most two actual ports.
Three-connectivity forces every vertex outside the union to be one of
these ports. In particular they are precisely the two roots `s,t`:
both their bags are singleton, there is no unused vertex, and the
connected x/y bags partition all of `K`. They are adjacent and both
contact `s,t`. Since `r` has at least six neighbours in `H` and only
two other A vertices, it contacts at least one of these parts. Keeping
the A triangle singleton now proves the stated rooted `K_5^-` corollary.

This construction neither makes both parts full to all three A vertices
nor controls their simultaneous contacts with the separate B triangle.
It supplies no third helper and does not close the two-triangle case.
