# Internal audit: degree and connectivity in the rooted helper construction

**Verdict: GREEN for the stated conditional reductions, rooted-star lemma
and rooted-triangle lemma.** This is a separate internal mathematical
audit, not external peer review.

Audited [source](hc7_c21_rooted_density_low_degree_reduction.md), SHA-256:

```text
431bd7d7d2b5bcb59e385781234c6d7ed6824f62ee50eb8ddf49e69da792cef2
```

The final source preserves the arguments reviewed in the construction
draft at hash
`93a166b494f6fa119c0e84a3be33ee845d946674f0f7d2b7bd4c3d7ccf64d16b`.
The added two-vertex edge count was checked directly. The removed failed
replacement discussion is not an input to the proofs.
The degree and connectivity proofs were separately reviewed at draft hash
`fb251d05e459aca8e4531bb39157e4d24145fd3af2943fe31df6d81167e27ec2`
before consolidation; duplicate introductions and scope statements were
trimmed without changing their arguments.

**Nonmathematical repin:** the source previously pinned at
`11d1897cbcf5ad2d7092affc1161c822fd2f537fdf533a3a8ef73d4f48851b79`
changed only two stale global-status sentences to state the scope of
these reductions alone. All mathematical statements and proofs are
unchanged; the GREEN verdict applies to the current hash above.

## External inputs and minimality

The definitions and statements of Dvořák--Norin--Rahman,
[arXiv:2609.17760v1](https://arxiv.org/html/2609.17760v1), Observation 2.5,
Theorems 2.6--2.7, Lemmas 3.1 and 3.3, Observation 4.1 and the isolator
argument in Corollary 4.2 were inspected. They are accepted external
inputs; this audit does not independently prove that paper.

The additional local input is the separately audited
[degree-five dart lemma](rooted_dart_nonroot_degree_five.md), SHA-256
`37dcf256f64fca7c49a1bd4ec66021371fba9a7863bf9523597ba4b898ecfad2`.
Its adjacent audit isolates the exact external terminal construction
and checks the new decreasing induction and lift.

The target retains all five original roots and at least ten of eleven
helper contacts. Its rooted models lift through fixed disjoint connected
preimages. Removing root--root edges changes neither the density nor the
target: such an edge cannot lie inside a bag containing just one prescribed
root or supply a helper contact. The clique/dart reducent supplied by
Lemma 3.3 has fewer vertices, preserves the five original roots and
4-lightness, and does not decrease density. Minimality therefore excludes
reducible fragments for this stronger target as well.

For a proper root five-separation of density at least two, the smaller
right side inherits 4-lightness and hence has the stronger target model
by minimality. Five exterior paths transfer that model itself. With fewer
paths, its restriction gives the clique/dart used in the external
isolator argument, producing a reducible fragment. This does not mistake
a counterexample to the stronger target for a counterexample to the
external weaker theorem.

Component density sums justify connectedness of the nonroots. The
neighbour-count proof handles both four and five root neighbours; in the
four-neighbour case the two positive components and the component meeting
the missing root can be chosen with the required distinctness. The
unique-root-neighbour separation has density `rho4+4-deg_X(v)>=3`.
Finally edge deletion at density at least three either stays in the
induction class or creates a proper dense five-side. The only nonproper
case forces a root of degree one. Thus the five listed restrictions,
including `rho4=2`, follow.

## Quotient obstruction and rooted star

For a positive small fragment after contraction, minimality of its closed
side gives the lightness needed for the external clique/dart theorem.
If the contracted vertex is interior, lifting that model yields a
reducible fragment with at least two vertices. If it is outside the
closed side, the original graph already violates 4-lightness. In the
remaining boundary case, splitting increases boundary order to exactly
five. The density increase equals the number of common neighbours in
the interior. The proper-five-side restriction forces density one and
zero such common neighbours. The nonroot endpoint outside the closed
side ensures that the separation is proper.

The rooted-star lemma is also valid. Each component outside `Z` misses
at most its own order of the roots. Since `|V(H)-Z|+|X|<=k-1`, a root
outside `X` sees every such component. Their union with that root is a
connected central bag. The two stated degree bounds give its contact
with every other singleton root. This uses all vertices and works when
there are no vertices outside `Z`.

## Forbidden degree-five edge and original-root lift

Degree five and exactly three common neighbours determine the displayed
nine incident edges. Contracting `pq` preserves density two. A blocker
for this contraction avoids all three common neighbours and must contain
both exclusive neighbours `u,v`; in particular these are original
nonroots. The rerooted graph has exactly the same neighbours and incident
edges on every new nonroot fragment as the original graph, because only
`u,v` see the deleted vertices `p,q`.

The calculation `rho4(R)=7-delta-a0` subtracts exactly two deleted edges
and the newly excluded root edges. This equals the number of missing
edges in `K2,3+uv`. For each value zero through seven, the external target
contains that labelled graph; the exceptional target at density three
excludes a four-edge graph and causes no problem. Literal root edges
supply all remaining contacts.

Appending `p,q` to the bags at `u,v` gives adjacent helpers full to
`A union D`. Overlap between `A` and `D` causes no duplication: the
intersection uses its existing `D` bags and `A-D` uses singleton bags.
The helper interiors avoid every original root. The union
`U=T union {p,q}` has boundary `A union D`, of order three through six.

If its root connectivity is five, the exterior linkage attaches all five
original roots to distinct boundary bags; original roots already on the
boundary use trivial paths. If the connectivity is at most four, the
isolator interior contains `U`, avoids the original roots and has
nonpositive density by original 4-lightness. The restricted helper model
and linkage supply a rooted clique, or a dart for four roots, so this
interior is reducible. Its size is at least two. This is a complete lift,
not an assumption that a contraction preserves 4-lightness.

A two-vertex blocker needs nine incident edges. Each vertex has at most
four boundary neighbours, so equality forces their mutual edge, the three
common boundary neighbours and distinct exclusive split endpoints. The
forbidden-edge theorem therefore excludes every such blocker.

## Nonroot minimum degree and internal five-connectivity

Deleting a nonroot of degree at most four keeps global density at least
two and all five roots. If a positive small fragment appears, restoring
the deleted vertex either changes nothing, contradicting original
lightness, or adds that vertex to its boundary and raises its density
to at least two. Its boundary must then have order five. This side is
proper: otherwise its boundary contains all five original roots and the
distinct deleted nonroot. The earlier proper-five-side restriction
therefore proves that deletion preserves lightness in this specific
case. Minimality gives a contradiction and hence nonroot minimum degree
at least five.

The rooted-triangle lemma handles its root allocation explicitly. A
cycle and a two-fan in a two-connected block give either a cycle through
the three attachments or a theta whose three bags are disjoint and
pairwise adjacent. In the block-cut tree, a block median gives three
distinct attachments and disjoint exterior root paths, including when
some root nodes coincide. A cutvertex median places at most one root
in each component after deletion. Any nonroots in such a component
would have a boundary of order at most two. Internal three-connectivity
therefore leaves at most the cutvertex as a nonroot, contradicting its
degree bound. This proves the lemma without a finite census.

For the internal-five conclusion, choose a root-free set of minimum
boundary order `k<=4` and pass to a connected component. Minimality of
the boundary order ensures that its rooted shore is internally
`k`-connected; every nonroot retains all original neighbours and degree
at least five. The whole interior has nonpositive density by original
4-lightness. A rooted clique makes it reducible for `k=0,1,2`; the
rooted-triangle lemma does so for `k=3`. For `k=4`, degree five excludes
a singleton interior, so every hypothesis of the pinned dart lemma
holds and its output again makes the interior reducible. Thus every
possible small boundary is excluded. This proves internal
five-connectivity, without asserting ordinary five-connectivity or
preservation of connectivity under arbitrary contractions.

## Scope

No unresolved inference was found in these statements. The proofs are
unbounded and do not depend on a finite computation. Their former
reduction gap is closed for the rooted helper theorem by the separately
audited [degree-six reduction](hc7_c21_helper_degree_six.md) and
[padded atom proof](five_root_one_missing_contact.md). The present audit
certifies the restrictions and local lemmas, not an arbitrary fragment
replacement operation or the global composition. Neither C21 nor HC7 is
certified by this audit. The source's later status and historical-gap
wording was updated without changing its mathematical arguments.
