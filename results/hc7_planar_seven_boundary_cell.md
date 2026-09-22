# A planar seven-boundary cell admits a six-colouring lift

**Status:** written proof with a separate GREEN [internal audit](hc7_planar_seven_boundary_cell_audit.md).
This closes the planar torso branch of an inclusion-minimal exact
seven-boundary cell in the
[reserved-frame construction](../active/hc7_split_clique_rooted_construction_working.md).
It does not close the nonplanar torso branch, the split-clique case, or HC7.

## Statement

Let `G` be a finite simple seven-connected graph whose every proper minor
is six-colourable. Let `X` be a connected vertex set with `|X|>=2` and

    N_G(X)=T dotunion Z,
    T={a,b,c},  Z={f1,f2,f3,f4}.

Assume that `f1f3` and `f2f4` are not edges and that the actual graph
`B=G[X union T]` has a plane embedding in which the three vertices of `T`
are cofacial. Then `G` is six-colourable.

In the reserved-frame application, the four ports occur in the displayed
order on the induced path `F`, so the two opposite pairs are independent.
For an inclusion-minimal exact cell, the completed torso
`Q=B+K3[T]` is four-connected. If this torso is planar, its triangle `T`
bounds a face: vertices on both sides would give a three-cut. Thus its
embedding supplies the hypothesis on the actual graph `B` after removing
the virtual gate edges.

The only structural external input below is the ordered two-paths theorem,
in the exact form stated by Fabila-Monroy and Wood,
[*Rooted K4-Minors*, Lemma 2](https://arxiv.org/html/1102.3760v1#S2).
For any graph with four distinct terminals, either the prescribed two
disjoint paths exist, or the graph is a spanning subgraph of the ordered
web. The theorem has no connectivity or terminal-degree assumption.
Four-colourability of planar graphs is the colouring input.

## 1. The opposite-port linkage exists

Put `L=G[X union Z]` and `n=|X|`. Every nonempty `Y subseteq X` has

    |N_L(Y)|>=4.                                           (1)

Otherwise `N_G(Y) subseteq N_L(Y) union T` has order at most six.
The seven vertices of `T union Z` all lie outside `Y`, so at least one
vertex remains outside `Y union N_G(Y)`. Deleting `N_G(Y)` would therefore
disconnect `G`, contrary to seven-connectivity. This argument applies
even when `Y` is disconnected.

Suppose that `L` has no disjoint `f1`--`f3` and `f2`--`f4` paths.
The cited theorem makes `L` a spanning subgraph of an
`(f1,f2,f3,f4)`-web. Its plane skeleton has the four terminals as its outer
quadrilateral; every extra cell has its vertices outside the skeleton and
has neighbours only in its three skeleton gates. All four terminals are
skeleton vertices. Thus any nonempty cell interior `Y` is a subset of `X`
and has `|N_L(Y)|<=3`, contradicting (1). No nonempty cell survives, so
`L` itself is a spanning subgraph of the plane skeleton `H`.

This also covers low-degree terminals and possible low-connectivity
obstructions: the external theorem already permits them, and only
terminal-free cell interiors are discarded. In this application `L` is
in fact connected, since `X` is connected and every member of `Z` has an
actual neighbour in `X`.

The skeleton has `n+4` vertices and an outer quadrilateral, whence

    e(G[X])+e_G(X,Z) <= e(H)-4 <= 3n+1.                    (2)

The subtraction removes the four distinct outer edges of the skeleton;
none is counted on the left. They need not be actual edges of `G`.
Likewise the cofacial embedding of `B` permits completion of `T` to a
triangle in that face. The planar edge bound gives

    e(G[X])+e_G(X,T) <= 3n.                               (3)

Indeed the completion has `n+3` vertices and exactly three edges within
`T`, so subtracting those three edges from `3(n+3)-6` gives (3).
Summing (2) and (3), and using the exact boundary of `X`, yields

    7n <= sum_{x in X} d_G(x)
       = 2e(G[X])+e_G(X,T)+e_G(X,Z)
       <= 6n+1.

This contradicts `n>=2`. The required disjoint paths therefore exist.
Their internal vertices lie in `X`: their four distinct endpoints exhaust
`Z`, and disjointness prevents either path from using another endpoint.

## 2. A proper minor makes the ports use two colours

Contract each of the two paths to a single vertex, and delete all remaining
vertices of `X`. Call the resulting graph `G'`. It is a proper minor.
Its two merged port vertices represent `{f1,f3}` and `{f2,f4}`,
respectively. Take a six-colouring of `G'` and copy each merged colour to
its two original ports. Retain all other colours outside `X`.

This is a proper colouring of `G-X`. The only identified pairs among its
vertices are the two assumed nonedges; every edge between distinct
preimages remains an edge of the quotient. In particular, all four ports
use a set `C` of at most two colours. Added quotient adjacencies may
restrict this colouring but cause no difficulty when it is pulled back.

## 3. Extend across the actual planar cell

Choose four colours `A` disjoint from `C`, including every colour used on
`T` that is outside `C`. This is possible: there are six available colours,
at most two in `C`, and at most three required gate colours.

Temporarily change each gate whose actual colour belongs to `C` to an
unused colour in `A`, using distinct new colours for these gates and
avoiding the colours of the unchanged gates. At most three gate colours
are needed. The resulting precolouring of `T` is proper on its actual
edges. Equal colours among unchanged gates are allowed.

Start with the actual plane graph `B`, with all virtual gate edges
removed. Identify any equally precoloured gates across their common
face. Since there are at most three gates, these identifications can be
made without crossings. No actual edge becomes a loop, because the
gate precolouring is proper. The distinct gate images remain cofacial;
complete them to a clique of order at most three in that face. The
resulting graph is planar. Apply the Four Colour Theorem and permute its
four colours to match the prescribed distinct colours of the gate images.
Expanding the identifications gives a proper `A`-colouring of `B` with
the temporary gate colours.

Restore the actual colours of the changed gates. Each restored colour
lies in `C`, while every vertex of `X` has a colour in `A`, so no edge
from such a gate to `X` becomes monochromatic. Actual edges within `T`
remain proper by the original colouring of `G-X`. Finally every port has
a colour in `C`, so every edge from `X` to `Z` is proper as well.
These are all edges leaving `X`. Together with the retained colouring
outside `X`, this gives a proper six-colouring of the original graph `G`.

The web skeleton edges, the completed gate triangle, and the face edges
used for the Four Colour Theorem serve only in planarity bounds or an
auxiliary colouring graph. None is used as an actual minor-model contact.
