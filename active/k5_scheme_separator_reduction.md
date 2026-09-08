# Separators in a minimal rooted K5-scheme counterexample

**Status:** written deductions with a separate adjacent internal audit.
The theorem below is a separator normal form, not a proof that K5 is
contractible. Its final three-cut allocation remains open.

All graphs are finite and simple. A properly coloured K5-scheme consists
of five distinct roots, named by their colours, and a path `P_ij` for each
pair of roots, using only colours `i,j` and no other root internally.
The host is the union of these paths. The colouring is proper.
A rooted minor must retain every original root in its own connected bag.

## 1. Exact statement and elementary tools

**Theorem.** Suppose `G` has minimum order among properly coloured
K5-schemes without a fully rooted K5 minor. Then `G` is three-connected.
Every three-cut `S` has exactly two components in `G-S`, contains no
original root, and has three distinct colours. One component contains
exactly the three roots whose colours occur on `S`; the other contains
the two remaining roots. Every other separator pattern of order at most
three admits a strictly smaller, root-preserving minor with a properly
coloured K5-scheme.

This is conditional on a counterexample existing. No chromatic-criticality
or connectivity hypothesis from the Hadwiger-seven project is used.

Every nonroot of a minimum counterexample lies on at least two scheme
paths. Otherwise contract its two-edge segment on its sole path into
one vertex of the neighbours' common colour. The neighbours include at
most one original root, and all other paths retain their colours. This
strictly reduces order. Edges belong to unique paths, so each nonroot
has degree at least four. Each root has degree four.

We use the following elementary rooted triangle fact, including subgraphs
of the triangle. Fix `P_jk`; take the `i`-prefixes of `P_ij,P_ik` before
their first contacts with `P_jk`. Their union is a connected `i`-bag.
The contacts are distinct: otherwise all three demands meet at one vertex,
contrary to their endpoint-colour condition. Split `P_jk` between them.
The resulting three bags give the rooted triangle, in either contact
order. A path or a smaller target is immediate.

An **exterior** is one component `D` of `G-S`; the interior is the rest
of `G-D`, including `S`. An exterior excursion of a path has its interior
in `D` and its two ends in `S`. If a colour `i` is absent from `S` and
its root is not in `D`, then a vertex of colour `i` in `D` can belong to
`P_ij` only if root `j` is in `D`, or `S` contains two vertices of colour
`j`. Indeed, if both roots are outside `D`, that path needs two distinct
boundary vertices, both necessarily coloured `j`. We call this the
two-boundary-vertices observation.

All contractions below have specified disjoint connected preimages.
Boundary colours are retained. Replacing an exterior excursion by an
edge between its boundary images preserves its two endpoint colours;
identified equal-colour boundary vertices omit that excursion. Erasing
closed subwalks gives paths with no other root internally. Their common
vertex colour certifies the full scheme intersection condition. Therefore
a rooted model in any resulting smaller scheme lifts to the original
roots. Unused exterior vertices are deleted.

## 2. Root-free sides and cuts of order at most two

If `D` contains no root and `|S|<=3`, every colour in `D` occurs on `S`:
otherwise a nonroot on two distinct demands would require two boundary
vertices in each of two distinct partner colours. If `S` has at most two
colours, vertices in `D` can lie on only the single demand between those
colours, a contradiction. Hence `S` is a rainbow triple. Every path
meeting `D` gives its unique exterior segment between the appropriate
two vertices of `S`. These segments form a sub-triangle scheme. Its
rooted model replaces the exterior by the needed boundary edges, strictly
reducing order and retaining all original roots.

For any `S` of order at most three, all roots whose colours are absent
from `S` lie in one component `C0`: their pair paths avoid `S` entirely.
The host is connected, since it is a union of root-to-root paths.

A component with just one root `a` requires colour `a` on `S`: otherwise
its four paths to the other roots would require four distinct boundary
colours. If `|S|<=2`, choose an inside root colour `i` absent from `S`.
The exterior `a`-to-first-boundary prefix of `P_ai` has equal-coloured
ends and therefore an exterior `i`-vertex. The observation above leaves
that vertex on only `P_ai`, a contradiction.

Thus no one-cut exists. For a two-cut, every component other than `C0`
must contain two roots `a,b`, and `S={s_a,s_b}` has their distinct
colours. Pick distinct inside colours `c,d`. The exterior prefixes of
`P_ac,P_bd` connect `a` to `s_a` and `b` to `s_b` disjointly. Grow these
two seeds to a connected partition of `D+S`; its parts are adjacent.
Contract the parts to the two boundary images. Every cross-path uses
its untouched interior suffix after its unique boundary vertex; the
three inside-root paths stay inside, and `ab` is now literal. This is
a smaller proper K5-scheme with fixed original-root preimages.

## 3. A single exterior root at a three-cut

Now `G` is three-connected, so every component of `G-S` has boundary `S`.
Suppose `D` has just root `a`. Its colour occurs on `S`. Choose a root
colour `i` absent from `S`. As above, `P_ai` has an exterior `i`-vertex.
Its second demand forces a repeated boundary colour different from `a`.
Consequently the only possible pattern is `S={s_a,p_b,q_b}`.

Choose distinct absent colours `c,d`. Take the exterior `a`-to-`s_a`
prefix of `P_ac`. An exterior `d`-vertex on the corresponding prefix
of `P_ad` must also belong to `P_bd`. The latter supplies an exterior
`p_b`-to-`q_b` segment. The two chosen paths have disjoint colour sets
`{a,c}` and `{b,d}`. Contract them, merging the two `b`-ports and moving
`a` to its port. This never merges two original roots.

Every `ai`, `i!=b`, uses its interior suffix. Every `bi`, `i!=a`, loses
only excursions between the now-identified `b`-ports; paths avoiding
`a,b` stay inside. The `ab` image retains its two colours. Any required
exterior segment between the two remaining boundary images can be
contracted to their edge. Thus order strictly decreases and all five
original roots lift.

## 4. Two exterior roots with their colours on the cut

Let these roots be `a,b`, and call the other roots `c,d,e`.

**Rainbow cut.** Write `S={s_a,s_b,s_c}`; root `c` may itself be `s_c`.
Contract the disjoint exterior prefixes of `P_ad,P_be` to `s_a,s_b`.
The paths in the `a,b,c` subsystem retain their colours: the foreign
vertices absorbed by these two contractions have colours `d,e`.
Simplify their images. Their exterior segments form a sub-triangle
scheme on `S`; replace them by its rooted boundary model.
Every path to `d` or `e` from `a` or `b` has an untouched interior
suffix after its unique possible boundary vertex. The paths `cd,ce,de`
never leave the interior. These paths, together with the boundary
replacements for `ab,ac,bc`, give the smaller proper K5-scheme.

**Repeated colour.** By symmetry write `S={p,q,z}`, with colours `a,a,b`.
If two `a`-to-inside paths first hit different `a`-ports, unite their
exterior prefixes into one connected set containing `a,p,q`; take a
`b`-to-`z` prefix in the third inside colour. These sets are disjoint.
If all first hits are `p` but one path has an exterior `p`-to-`q`
excursion, that prefix plus excursion also connects `a,p,q`; choose
a `b`-prefix in a different inside colour. Contract the two sets.
All `a`-ports are now one vertex and every cross-demand can use its
interior suffix after its last boundary visit. The `ab` subsystem
provides any needed exterior edge between the two boundary images.

In the remaining case all first hits are `p` and no exterior `p`-to-`q`
excursion exists. Every `ai` path then stays in the interior after `p`:
a later exit and return would require exactly that excluded excursion.
Contract one `a`-to-`p` prefix and a `b`-to-`z` prefix in another colour,
leaving `q` as a nonroot. Again all six cross-path suffixes are interior.
Only the `ab` image needs exterior pieces. Its simple image visits each
of `p,q,z` at most once, so those pieces have disjoint interiors and
can be replaced by edges on a subpath of these ports. If an exterior
`p`-to-`q` piece now gives an equal-colour edge, merge its ends; `q` is
not an original root. This also preserves every interior suffix.

All these operations absorb the two exterior roots into distinct port
images, hence strictly reduce order. The three inside-root paths avoid
the two boundary colours throughout the repeated-colour case.

## 5. Exhaustion and the sole unresolved state

There are at least two colours absent from a three-cut. Their roots
belong to `C0`. Every other component contains at most three roots,
all in boundary colours. Zero or one root is excluded by Sections 2--3;
two roots are excluded by Section 4. Hence any surviving component
contains all three boundary-colour roots. These colours are distinct,
none of their roots is on `S`, and the other two roots lie in `C0`.
No additional component can contain a root, and root-free components
have already been excluded. This proves the stated normal form.

Write the surviving cut as `S={s_c,s_d,s_e}`, with roots `c,d,e` on
one side and roots `a,b` on the other. Three disjoint paths from
`{c,d,e}` to `S` exist by three-connectivity, and their first-hit
prefixes stay on the three-root side. They alone do not give three
pairwise adjacent root-and-port bags. The complete remaining input
also includes the two simultaneous systems of properly coloured
`i`-to-`s_i` paths, of palettes `{i,a}` and `{i,b}`, and the three
`c,d,e` demand paths (which may have excursions on the other side).
Their compatible allocation is unproved here. In particular, neither
four-connectivity of a minimal counterexample nor K5 contractibility
has been established.

## 6. Why repeated ports must not be grouped unnecessarily

There is an explicit positive scheme refuting that stronger grouping.
Take ports `p,q` of colour `a`, port `z` of colour `b`, and vertices
`u_i,j_i` of colour `i` for `i=c,d,e`. Besides the five roots, these
are all vertices. Use

`P_ai=a-u_i-p-j_i-q-i`, `P_bi=b-u_i-z-i`, `P_ab=a-z-q-b`,
and `P_ij=i-j_j-j_i-j` for `i,j in {c,d,e}`.

Every nonroot lies on at least two paths. The cut `{p,q,z}` separates
`D={a,b,u_c,u_d,u_e}` from the other roots. In `G[D+S]`, `q` has only
neighbours `b,z`, so no exterior `a,p,q`-bag avoids a `b,z`-bag.
Nevertheless

`{a,u_c,p}`, `{b,u_d,z}`, `{c,j_d}`, `{d,j_c}`, `{e,j_e,q}`

are five disjoint connected rooted K5 bags. Section 4 instead contracts
the first two exterior prefixes and leaves `q` available to the interior.
This is a counterexample only to unnecessary fixed-colour port grouping.
