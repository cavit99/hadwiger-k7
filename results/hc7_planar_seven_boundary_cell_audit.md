# Audit: planar seven-boundary cell

**Verdict: GREEN.** This separate internal audit's independent
reconstruction found no unsupported inference in the stated colouring
theorem. This is not external peer review or a closure of the wider case.

- Source: [the planar-cell proof](hc7_planar_seven_boundary_cell.md).
- Current source SHA-256: `b503e1a6175f7cb62071d424c49cb3be7a9db26515024d6661ccb88b82f8f56f`.
- Audit date: 2026-09-22.
- Method: direct proof reconstruction and independent inspection of the
  primary ordered-web statement; no finite computation is required.

The independently reconstructed source originally had SHA-256
`6f951a130489dd9d143c23a8f634bf1b59d598c7228a8c0f20c1289062ab67ca`.
Promotion to `results/` changed only the opening status to link this
GREEN audit and corrected the reserved-frame link to `../active/`.
Reversing exactly those edits reproduces the original hash. The
mathematical text is unchanged, so the verdict applies to the current pin.

## External theorem and deletion of web interiors

The definition of a web and Lemma 2 in Fabila-Monroy and Wood,
[*Rooted K4-Minors*, Section 2](https://arxiv.org/html/1102.3760v1#S2),
were inspected directly. With `s1=f1,t1=f3,s2=f2,t2=f4`, the alternative
to the required disjoint paths is precisely a spanning ordered web
with outer boundary `(f1,f2,f3,f4)`. The statement imposes no
connectivity or terminal-degree hypothesis. Its skeleton is planar;
the set added at any skeleton triangle has external neighbours only
in that triangle.

For each nonempty `Y subseteq X`, including disconnected sets, an
external neighbourhood of at most three in `L=G[X union Z]` would give
at most six neighbours in `G`, since only `T` is omitted. At least one
of the seven original boundary vertices survives outside `Y` and that
neighbourhood, so this is a forbidden cut. Thus the inequality
`|N_L(Y)|>=4` is valid with exactly the stated quantifier.

Every added web interior is terminal-free, since all four terminals
are skeleton vertices. Spanning containment puts its entire nonempty
vertex set in `X`; its neighbourhood in `L` has size at most three.
The preceding inequality excludes every such interior. This step
does not delete terminals or assume that the skeleton has inherited
connectivity. The skeleton consequently has exactly `|X|+4` vertices.

## The two edge counts

Write `n=|X|`. The simple planar skeleton has an outer quadrilateral,
so its edge count is at most `3(n+4)-7=3n+5`. The four distinct
outer edges have both ends in `Z`. Subtracting them therefore leaves
an upper bound `3n+1` for `e(G[X])+e_G(X,Z)`, regardless of whether
those four edges belong to the actual graph.

The three distinct cofacial gates in the actual planar graph
`B=G[X union T]` can be completed to a triangle in their common face.
The completion is simple and planar, has `n+3` vertices, and has
exactly three edges inside `T`. Subtracting those edges from its
planar edge bound gives `e(G[X])+e_G(X,T)<=3n`.

The exact boundary hypothesis ensures that these two counts sum to
`sum_{x in X} d_G(x)`. Seven-connectivity gives minimum degree seven,
and hence `7n<=6n+1`. The assumption `n>=2` is used exactly here.
Thus the required opposite-port linkage exists. Its internal vertices
lie in `X`, since its four disjoint ends exhaust `Z`.

## Minor, pullback and gate extension

The two paths have disjoint vertex sets and distinct ends. Contracting
each path and deleting all other vertices of `X` gives a genuine proper
minor, with `|V(G)|-n-2` vertices. No vertex outside `X union Z` is
identified. In the pullback to `G-X`, only `f1,f3` and `f2,f4` receive
colours from the same respective quotient vertex. Both pairs are
assumed nonedges; every other actual edge outside `X` survives as
an adjacency between different quotient vertices. The pulled-back
six-colouring is consequently proper, and its port palette `C` has
size at most two. Extra quotient edges restrict colour choices without
invalidating this pullback.

A four-element palette `A` disjoint from `C` exists and can contain
all gate colours outside `C`. If `m` gates need temporary colours and
the unchanged gates use `r` distinct colours, then `r+m<=3`; at least
`4-r>=m` colours are available for distinct replacements. These
replacements also avoid every unchanged gate colour, so the temporary
gate precolouring is proper.

The arbitrary proper precolouring of three cofacial gates does extend
to a four-colouring of `B`. If all gate colours are distinct, complete
their triangle in the face. If exactly two coincide, join that nonadjacent
pair through the face and contract the added arc; its image remains
cofacial with the third gate, so complete an edge between them. If all
three coincide, they are independent and may be joined to a new point
in the face and identified by contracting that star. These constructions
preserve planarity. Remove parallel edges if produced; no original edge
becomes a loop. In each case the distinct images form a clique of order
at most three. The Four Colour Theorem followed by a permutation matches
their prescribed colours. Expanding the identifications gives the
required temporary colouring of the actual graph.

Restoring a changed gate's original colour creates no conflict with
`X`, whose colours belong to `A`, disjoint from `C`. Gate-to-gate and
all other edges outside `X` again have their original proper colours.
Every port has a colour in `C`, so the edges from `X` to `Z` are proper
as well. The exact boundary lists all possible remaining edges. This
is a colouring of the original host, with no expansion of a minor
colouring through the contracted path interiors.

## Scope

The theorem assumes seven-connectivity, proper-minor six-colourability,
the exact boundary, both independent port pairs, and a cofacial planar
embedding of the actual graph `B`. It proves six-colourability directly,
without any induction or quotient-criticality assertion. In the stated
application, a planar four-connected completed torso has a facial gate
triangle, so removing virtual gate edges supplies the needed cofacial
embedding. The separate derivation of that torso and its four-connectivity
is an application obligation, not an additional inference used in this
theorem.

No gap was found at the pinned revision. The nonplanar torso branch,
the full split-clique case and `HC_7` remain outside its conclusion.
Index checks are left to the parent's integration pass as requested.
