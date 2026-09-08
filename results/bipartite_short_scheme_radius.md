# Intrinsic radius two for short bipartite schemes

**Status:** written proof with a separate [internal audit](bipartite_short_scheme_radius_audit.md). This is a
quantitative refinement of a proved bipartite theorem, not a completion of
the HC7 objective or a claim of comparable significance or priority.

The proof input is the [universal bipartite theorem](bipartite_contractibility_via_matroid_reduction.md),
SHA-256 `3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`.
Its [first audit](bipartite_contractibility_via_matroid_reduction_audit.md)
has SHA-256 `1c8ed74e98829690dc4c1fd6d44631454d330443dd33faea4435d35beb5cca06`;
its [second audit](bipartite_contractibility_via_matroid_reduction_second_audit.md)
has SHA-256 `83df07a306bef1a71b50bf5f36020a48b7240187c40d503819eb10baf5348297`.
We use its Lemmas 0--2 and rank case split, with the invariant proved here.

All graphs are finite and simple. An `H`-scheme with injective root map
`rho` consists of a simple `rho(u)`--`rho(v)` path for every target edge
`uv`, with no other prescribed root internally, such that every collection
of paths having a common vertex has a common target endpoint. Path length
counts edges. A bag has **intrinsic radius at most two at its root** if
each of its vertices can reach that original root by a path of at most two
edges lying entirely in the bag. This is stronger than bounding distances
in the whole host.

## 1. The theorem and invariant

**Theorem.** Let `H` be bipartite. If `G` contains an `H`-scheme whose
paths all have length at most three, then it has a rooted `H`-minor model
in which every bag has intrinsic radius at most two at its prescribed
original root.

**Proof.** Work in the original path union, retaining isolated roots.
Write `G_0` for this host. Maintain a quotient scheme with disjoint
connected preimages in `G_0` and the following invariant:

1. Only prescribed root images can have nonsingleton preimages. Each root
   preimage has intrinsic radius at most two at its original root.
2. Each current scheme path is either a root--root edge or the image of
   its unchanged original three-edge path, whose two internal vertices
   are still original singleton nonroots.
3. The quotient is properly coloured by target vertices; each surviving
   nonroot retains its initially chosen colour.

First establish this invariant by the input's Lemma 0. Assign each
nonroot an endpoint common to its incident scheme paths. A monochromatic
edge on a path of length at most three has a monochromatic route of
length at most two to the root of that colour: the only internal edge
has its colour equal to one of the two endpoint colours. Therefore every
nontrivial monochromatic component contains its own root and all its
vertices have such routes to that root. There is only one root of each
colour, so these are precisely root preimages of radius at most two.
All other preimages are singletons. The reduced paths are properly
bichromatic, hence have odd length. A nonliteral reduced path must have
length three and therefore must be the unchanged original path, with
no vertex identified. Cleanup preserves the invariant.

Choose the shore `(A,B)` having no more nonroots than its opposite shore,
as in Section 3 of the input. For each `a in A`, its projection `M_a`
is now a star centred at the image of `rho(a)`, allowing parallel edges.
Indeed every nonliteral demand has the form

`rho(a), x, y, rho(b)`, with `f(x)=b` and `f(y)=a`,

and contributes the projected edge `rho(a)--y` labelled `x`. Both `x,y`
are original singleton vertices, and the displayed first two edges are
actual original edges of `G_0`.

For any label set `X`, each nontrivial component of `M_a(X)` thus contains
its root. A forest spanning that component allocates one label to each
of its nonroot base vertices. In the input's Lemma 2 contraction, every
newly absorbed label `x` is adjacent to the ORIGINAL root `rho(a)`, and
each newly absorbed base vertex `y` reaches that root through its own
allocated label in two original edges. Old root preimages retain their
existing radius-two witnesses. Consequently only root preimages grow,
and assertion 1 survives, including after reversing the shore choice.

Check assertion 2 for an affected three-edge demand explicitly. If its
label `x` belongs to `X`, the projected component identifies `rho(a)`
and `y`, even when `x` was allocated to a different root or deleted.
The original last edge `y rho(b)` then supplies a root--root edge.
If `x` is outside `X` but `y` is absorbed into `rho(a)`, the first and
last edges also supply a root--root edge, namely `y rho(b)` after
contraction. Otherwise `x,y` remain singleton and the path is unchanged.
These exhaust the possibilities in this orientation. Old root--root
edges survive; the statement is symmetric under shore reversal. The
input's retained-edge rule keeps the stated edges and its colouring
rule gives assertion 3. No foreign-owned label is reused as a path.

The input's matroid-union rank split is unchanged. A deficient maximum
packing supplies a nonempty minimizing set and a strictly decreasing
contraction of the above form. Full packing absorbs every projection
star into its root with the same original radius-two witnesses, leaving
the opposite root preimages as they are. It gives all required contacts.
The host order decreases at every recursive step, so this process
terminates. Its composed preimages are already the bags in `G_0`
described by the invariant, with internal radius at most two; no extra
radius factor is incurred by lifting. Isolated roots stay singleton.
This proves the theorem. QED

## 2. Radius one is impossible in general

Take the target with vertices `a,b,c` and edges `ab,ac`. The host has
prescribed roots `a,b,c`, nonroots `a',b',c'`, and exactly the edges of
the two paths

`P_ab = a,b',a',b`, and `P_ac = a,c',a',c`.

These paths form a scheme; their common nonroot `a'` has common target
endpoint `a`. Both `b` and `c` have the unique neighbour `a'`. In a
rooted radius-one model, their bags cannot both contain `a'`, so one,
say the `b` bag, is singleton. Its required contact to the `a` bag forces
`a'` into that bag. But `a a'` is absent, contradicting radius one at
`a`. Radius two is attained by bags `{a,b',a'}`, `{b}`, `{c}`.

## 3. A precise obstruction to extending this invariant

The following is a proof-method obstruction, not a counterexample to
bounded-radius minor existence for longer schemes. Fix `n>=3` and
target `K_{3,2n}`, with roots `a_1,a_2,a_3` and `b_e`, where
`e=(i,t)`, `0<=i<n`, `t in {0,1}`. Give colour `a_1` to nonroots
`u_0,...,u_n`; colour `a_j` to `w_j,v_{j,0},...,v_{j,n-1}` for
`j=2,3`; and colour `b_e` to `x_e,y_e`. All named vertices are distinct.
Use exactly the following three paths for each `e=(i,t)`:

`a_1,x_e,u_i,y_e,u_(i+1),b_e`,

`a_j,y_e,w_j,x_e,v_(j,i),b_e` for `j=2,3`.

Their union is a properly coloured scheme of length five. Every nonroot
lies on at least two paths, so this example also meets the usual stronger
minimum-nonroot-degree normalization. In the `A` orientation,
`N_A=3n+3<=4n=N_B`, and the common label ground set consists of all
`x_e,y_e`. Take `X={y_e: all e}`. Its projection ranks are `n,1,1`:
`M_1(X)` is the doubled path on `u_0,...,u_n`, with `a_1` isolated;
`M_j(X)` consists of parallel edges `a_j w_j` and isolated vertices.
The matroid-union expression is therefore `2n+n+2=3n+2<N_A`.

Equality is attained: allocate one `y_(i,t)` per link to `M_1`; allocate
`x_(i,0)` to `M_2` and `x_(i,1)` to `M_3` for every `i`; and allocate
two distinct remaining `y` labels, one to each of `M_2,M_3`. These are
disjoint forests of total size `3n+2`. Thus `X` is an actual minimizing
set in a deficient orientation, not an arbitrary projection subset.
Every forest spanning its nontrivial `M_1(X)` component selects one
label per link. Its actual connected preimage is a root-free path of
length `2n`, with precisely that intrinsic diameter. The root-only
invariant consequently fails for length five, even under the stronger
normalization. A bound depending only on the original path length for
intrinsic radii at prescribed roots would require another argument;
no such larger-length theorem is established here.
