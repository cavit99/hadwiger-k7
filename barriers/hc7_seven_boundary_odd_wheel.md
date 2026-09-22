# A seven-boundary odd wheel need not force `K7`

**Status:** explicit counterexample to an intermediate structural claim.
The small [verifier](hc7_seven_boundary_odd_wheel_verify.py) checks the
connectivity, neighbourhood inequalities and labelled data. Minor exclusion
and the colouring below have direct proofs.

## Construction

All subscripts are modulo five. Let `I` have vertices

    p,z,a0,...,a4,b0,...,b4

and precisely the edges

    p-ai, z-bi, ai-a(i+1), bi-b(i+1), bi-ai, bi-a(i+1)

for every `i`. This is the icosahedron: the two pentagons bound a
triangulated annulus, with the `p` and `z` fans capping its two boundaries.
In particular, `I` is planar. Add adjacent vertices `h0,h1`, each complete
to `I`, to obtain `G`. Put

    X={z,b0,b1,b2,b3,b4},       T={h0,h1,a4},
    F=a0-a1-a2-a3,             K={h0,h1,p,a3,a4}.

Then `N_G(X)=T union V(F)` has order seven. The connected graph `G[X]`
is a five-wheel and contains triangles. The path `F` is induced, avoids
`X union T`, and meets the literal five-clique `K` only at `a3`. No vertex
of `X` sees both extreme contacts `a0,a3`. Each `bi` has four boundary
neighbours; `z` has two.

## Verification of the structural hypotheses

The verifier checks that deleting any at most four vertices from `I`
leaves it connected. Thus `G` is seven-connected: after deleting at most
six vertices, either a universal vertex remains, or at most four vertices
have been deleted from `I`. Its vertices in `I` have degree seven, so its
connectivity is exactly seven.

For each `v in I`, its neighbourhood in `I` is a five-cycle. Consequently

    alpha(G[N_G(v)])=2=d_G(v)-5.

The same inequality holds at either universal vertex. Its degree is
thirteen, and the six disjoint edges

    p-a0, z-b2, a1-a2, a3-a4, b0-b1, b3-b4

cover `I`, giving neighbourhood independence number at most six, below
the required bound eight.

The graph `Q=G[X union T]+K_T` is four-connected. Indeed `T` already
induces a triangle, and `Q` is the join of `{h0,h1}` with a five-wheel
and a vertex `a4` adjacent to its consecutive rim vertices `b3,b4`.
That latter graph remains connected after deleting any one vertex.
Deleting `h0,h1,b3,b4` isolates `a4`, so the connectivity is exactly four.

## Minor exclusion and colouring

The graph `G` has no `K7` minor. Of seven disjoint branch sets, at least
five avoid both universal vertices. If those sets were pairwise adjacent,
they would give a `K5` minor in the planar graph `I`.

A proper six-colouring is given by the classes

    {p,b1,b3}, {z,a0,a2}, {a1,a3,b4}, {a4,b0,b2}, {h0}, {h1}.

## All six five-root choices meet the helper threshold

For every choice `U=T union {fi,fj}` of two path contacts, put
`H_U=G[X union U]`. Here `|X|=6`, `e(G[X])=10`, `e_G(X,T)=14`,
and each path contact has exactly two neighbours in `X`. Therefore

    rho4(H_U,U)=e(H_U)-e(H_U[U])-4|X|=10+14+4-24=4.

Every nonempty `Y subseteq X` has at least seven external neighbours in
`G`. Otherwise a cut of at most six vertices would separate it from
`p`, which has no neighbour in `X`. Passing to `H_U` removes at most
the two omitted path contacts from that neighbourhood. Thus `H_U` is
internally five-connected relative to `U`, and hence 4-light.

Consequently all six root choices meet the hypotheses and density
threshold of [H2](../results/five_root_one_missing_contact.md). None
admits an unconditional upgrade to all eleven helper contacts. Indeed,
the [exterior five-root linkage](../results/hc7_split_clique_seven_boundary_cell.md#an-exterior-clique-retaining-five-boundary-roots)
gives a `U`-rooted `K5` in `G-X`. Gluing its root bags to a full-contact
helper model in `H_U` would give a `K7` model: corresponding bags meet
only at their prescribed roots, and both helpers lie in `X`. This
contradicts the minor exclusion above. The verifier checks the counts
and all nonempty root-free subsets for all six choices.

## Exact scope

This refutes extending the seven-boundary cell theorem to arbitrary
connected cells with a **`K7`-minor conclusion** using only the displayed
connectivity, Dirac bounds, four path contacts, outside five-clique and
four-connected completed side. Triangle-containing cells require a further
argument, such as a six-colouring construction.

It does not refute a colouring-or-minor theorem. The example is
six-colourable, not seven-contraction-critical, and is not asserted to
realise the original split-clique neighbourhood or a minimum reserved
state in that frame. The full critical-host construction remains possible.

Run `uv run python3 barriers/hc7_seven_boundary_odd_wheel_verify.py`.
