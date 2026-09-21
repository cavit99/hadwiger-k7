# Degree and connectivity restrictions for the rooted helper construction

**Status:** written proofs with a separate hash-pinned internal audit.
These are proof inputs to the [completed rooted helper theorem](five_root_one_missing_contact.md).
These reductions alone prove neither Conjecture 21 nor HC7. This is a reduction within a
hypothetical minimal counterexample, not a completed significance-level
target. Its application is recorded in the
[construction frontier](../active/hc7_c21_rooted_density_construction.md).

## Target and external inputs

Write `P(G,X)` for the following conclusion in a five-rooted graph: there
are five disjoint connected prescribed-root bags and two further disjoint
connected bags avoiding every root, with at least ten of the eleven
helper–root and helper–helper contacts. Root–root contacts are immaterial.
The candidate is that every 4-light `(G,X)` with `rho4(G)>=2` has `P`.

The inspected primary source is Dvořák–Norin–Rahman,
[arXiv:2609.17760v1](https://arxiv.org/html/2609.17760v1), specifically
Lemma 3.3, Observation 4.1, the proof of Corollary 4.2, and Lemmas 4.3–4.6.
Their reducible fragments are the clique/dart fragments of Section 3.
Their Theorem 2.9 permits two missing contacts; it does not establish `P`.
The reductions below use their existing clique/dart reduction and the
proper-subset restriction of a helper model, rather than treating a
counterexample to `P` as a counterexample to their theorem.

## Restrictions that do transfer to a minimal counterexample

**Theorem.** Suppose the candidate is false, and
choose a counterexample `(G,X)` lexicographically minimizing
`(|V(G)|,|E(G)|)`. Then:

1. `G[X]` is edgeless.
2. There is no reducible root-free fragment with at most four neighbours.
3. There is no proper root five-separation with right-side density at
   least two.
4. `G-X` is connected, every nonroot has at most three root neighbours,
   and every root has degree at least two.
5. `rho4(G)=2`.

**Proof of 1 and 2.** Removing root–root edges changes neither hypotheses
nor conclusion. For 2, take an inclusionwise-maximal reducible fragment.
DNR Lemma 3.3 supplies a 4-light rooted minor of nondecreasing density on
fewer vertices. A `P` model in that minor lifts by replacing its vertices
with the fixed, disjoint connected preimages; each original root remains
in its prescribed bag. Minimality therefore excludes the fragment.

**Proof of 3.** Let `(A,B)` be the supposed separation and `S=A cap B`.
Its right side is 4-light: each of its small root separations extends to
one in `G` with the same interior and incident edges. Since the separation
is proper, `|B|<|V(G)|`, so minimality gives a `P` model rooted at `S`.
If there are five disjoint paths from `X` to `S` in `G[A]`, append those
paths to the corresponding root bags. The paths have disjoint interiors
outside `B`, so this preserves every helper bag and gives `P(G,X)`.

Otherwise take an isolator of order at most four. The proper-subset
restriction argument of DNR Observation 4.1 applies to the `P` model:
after deleting unused boundary roots, it yields the required rooted
clique, or a dart when there are four retained roots. Append the
isolator linkage to those retained bags. The isolator interior has at
least two vertices, since it contains the two helper bags, and has
nonpositive density by 4-lightness. It is therefore a reducible fragment,
contrary to 2. Notice that the first alternative of DNR Corollary 4.2
cannot simply be invoked as a contradiction: a counterexample to `P`
may contain their weaker helper model. The linked case must retain `P`
itself as done above.

**Proof of connectedness in 4.** Densities of the components of `G-X`
sum to `rho4(G)`. A positive-density component sees all five roots by
4-lightness. Two such components, contracted separately, give two full
helpers and hence `P`. Thus only one component has positive density;
it has density at least two. If another component exists, this gives
the proper five-separation excluded in 3. Consequently `G-X` is
connected and sees every root.

**Proof of the nonroot bound in 4.** Suppose a nonroot `z` has `d>=4`
root neighbours. Let `Q_i` be the components of `G-(X union {z})`.
Each has an edge to `z`, and

`sum_i rho4(G,Q_i) = rho4(G)+4-d`.

Every positive component sees at least four roots. If `d=5`, a positive
component exists and, with `{z}`, supplies one full and one at-least-four
helper, which are adjacent. If `d=4`, write `x` for the missing root.
A component seeing all five roots already gives `P` with `{z}`. Otherwise
every positive component sees exactly four roots. Its five-boundary side
has density at most one by 3, since the omitted fifth root makes that
separation proper. The displayed sum is at least two, so there are at
least two positive components. Some component `R` has a neighbour of `x`.
Choose a positive component `Q` different from `R`. Then `{z} union R`
is connected and sees all roots, while `Q` sees at least four roots and
has an edge to `z`. These are disjoint root-free helpers proving `P`, a
contradiction. Thus every nonroot has at most three root neighbours.

Finally, if a root `x` has unique neighbour `v`, the proper five-separation
with right side `G-x` rooted at `(X-{x}) union {v}` has density
`rho4(G)+4-deg_X(v)>=rho4(G)+1>=3`, contradicting 3. This proves 4.

**Proof of 5.** Suppose `rho4(G)>=3` and delete any edge `uv`, with `v`
a nonroot. The remaining rooted graph has density at least two, so if it
were 4-light, minimality would give a lifting `P` model. Thus it has a
positive-density fragment `Y` with at most four neighbours. The deleted
edge must have one end in `Y` and its other end outside `Y union partial Y`;
otherwise it was already a forbidden fragment of `G`. Restoring the edge
therefore gives a five-boundary fragment of density at least two. By 3 its
closed side must be all of `G`. Its boundary is then exactly `X`, and the
restored edge gives its root end a unique neighbour, contrary to 4. Hence
`rho4(G)=2`. The deletion has a strictly smaller edge count and unchanged
vertex count; no contraction-criticality is asserted for any minor.

## Exact remaining obstruction to contracting an edge

**Theorem.** In the same minimal counterexample,
let `e=uv` have at least one nonroot end. Suppose
`rho4(G/e)>=2`. If `G/e` is not 4-light, then there is a proper root
five-separation of `G` with interior `Y` and boundary
`S={u,v,a,b,c}` such that:

- `rho4(G,Y)=1`;
- no vertex of `Y` is adjacent to both `u` and `v`;
- identifying `u,v` gives a positive four-boundary side of density one.

**Derivation.** Choose a positive small side of the quotient with
inclusionwise-minimal closed side. If the contracted vertex is outside
that closed side, the same fragment violates 4-lightness in `G`. If it
is in the interior, its rooted clique/dart minor lifts across the
contraction, giving a reducible fragment of `G`; this is excluded by 2.
It must therefore be on the quotient boundary. Splitting it increases
boundary order by one. If `t` is the number of common neighbours of
`u,v` in `Y`, the lifted density is the quotient density plus `t`.
4-lightness forces the lifted boundary order to be exactly five, and 3
forces its density to be at most one. Both assertions above follow.
The separation is proper because its root-containing side also contains
the nonroot endpoint of `e`.

This is the exact case that the density-two induction does not cover.
An edge with completed-root triangle count at most three has quotient
density at least two, but the preceding obstruction prevents concluding
that every such edge is contractible within the induction class.

## The final small-neighbourhood construction does strengthen

**Lemma (a rooted star).**
Let `H` be a finite simple graph, let `Z` be a set of `k` vertices, and
let `X subset Z` be independent in `H`, with `X` a proper subset of `Z`.
Suppose

- `|V(H)|+|X|<=2k-1`;
- each vertex outside `X` has degree at least `k-1`;
- each vertex in `X` has degree at least `k-|X|`.

Then some `z in Z-X` is the centre of a spanning star rooted at `Z`,
whose other `k-1` bags are singletons. In particular, this gives four
spokes when `k=5`, strengthening the three-spoke output needed in the
published proof's final neighbourhood construction.

**Proof.** Set `T=V(H)-Z`. Every component `D` of `H[T]` sees all but at
most `|D|` vertices of `Z`: a vertex of `D` has at most `|D|-1` neighbours
in `T`, hence at least `k-|D|` neighbours in `Z`. Thus the union, over all
components, of their sets of missed roots has size at most `|T|`.
Because `|T|+|X|<=k-1`, some `z in Z-X` sees every component. Consequently
`T union {z}` is connected (also when `T` is empty).

Let `r in Z-{z}`. If `r` sees `T`, it is adjacent to the central bag.
Otherwise all its neighbours lie in `Z`. If `r` is outside `X`, its
degree bound `k-1` forces it to see `z`. If `r` is in `X`, independence
of `X` leaves exactly `k-|X|` possible neighbours in `Z-X`, and its
degree bound forces it to see every one, including `z`. Thus the central
bag and the singleton bags at all other roots give the asserted star.
All bags are disjoint, and the centre retains its prescribed root.

This closes the local construction after the required triangle bounds
are established. It supplies no triangle bound or safe contraction by
itself.

## A forbidden degree-five edge and every two-vertex blocker

**Theorem (a forbidden edge).** In the
minimal-counterexample class above, two adjacent nonroots of degree five
cannot have exactly three common neighbours. In particular, a split-pair
obstruction cannot have two interior vertices. This uses an alternate
edge and closes opposite blocking sides of arbitrary size, not just
two-vertex sides.

**Proof.** Suppose `p,q` are adjacent nonroots of degree five with exactly
three common neighbours `A={a,b,c}`. Their respective unique exclusive
neighbours `u,v` are distinct and outside `A union {p,q}`. Thus the edges
incident with `Y={p,q}` are exactly

`pq, pu, qv, pa, pb, pc, qa, qb, qc`.

No adjacency between `u,v` is assumed. The edge `pq` has three common neighbours,
so contracting it preserves global density two. If its quotient is
4-light, it is a smaller graph in the induction class and its `P` model
lifts, a contradiction. Otherwise the contraction analysis supplies
another density-one fragment `T` with boundary `{p,q,d,e,f}`, with no
vertex of `T` adjacent to both `p,q`. In particular `T` avoids `A`.
Because `p,q` must each have a neighbour in `T`, their displayed
neighbourhoods force `u,v in T`. Thus `u,v` are nonroots.
Write `D={d,e,f}`; these are distinct from `p,q,u,v`, although
`D` may overlap `A`.

Delete `p,q` from this latter side and reroot it at `{u,v} union D`:

`R = G[T union D]`, with roots `{u,v} union D`.

This five-rooted graph is 4-light. Indeed, its nonroot fragments lie in
`T-{u,v}`. Their neighbours and incident edges are exactly the same as
in `G`, since `p` has the unique neighbour `u` in `T`, and `q` has the
unique neighbour `v` in `T`. Every fragment with at most four neighbours
therefore has nonpositive density by 4-lightness of `G`.

Let `a0=e_G({u,v},D)`, let `delta` be one when `uv` is an edge and zero
otherwise, and put `m=7-delta-a0`. The original side has
`4|T|+1` edges incident with `T`. Removing `pu,qv`, and then excluding
the newly root–root edges (the possible `uv` and the `a0` edges to `D`), gives

`rho4(R)=(4|T|+1-2-delta-a0)-4(|T|-2)=7-delta-a0=m`.

Here `0<=m<=7`, and `m` is exactly the number of missing edges from
the seven-edge graph consisting of `uv` and all six edges between
`{u,v}` and `D`. The rooted universality theorem, DNR Theorem 2.6,
supplies all these missing edges simultaneously.
Its target table contains every graph of exactly `m` edges throughout
this range: at `m=3`, only a four-edge graph is exceptional, so it is
irrelevant, and at `m=7` the target is all subgraphs of `K5`.
Keep the already present root edges as well; each survives
between the corresponding root bags. We obtain five disjoint rooted
bags in `R`, with the bags at `u,v` adjacent and both adjacent to all
three bags at `D`.

Append `p` to the `u` bag and `q` to the `v` bag. These are connected,
disjoint, root-free helper bags, adjacent to each other and to all root
bags indexed by `A union D`. The bags at `D` are the rooted bags just
constructed; for vertices of `A-D`, take singleton bags. A vertex of
`A cap D` keeps its `D` bag. No conflict occurs because `T` avoids `A`,
and all previous bags lie in `T union D`. Both helpers see every such
root bag through their contacts with `D`, or through `p,q` and `A`.

It remains to transfer these helpers to the original five roots, not
merely to the intermediate boundary. Let

`U=T union {p,q}` and `B=U union (A union D)`.

The set `U` is root-free and its boundary is exactly `A union D`, which
has between three and six vertices. In particular, any original root in
`B` lies in this boundary.
Take the root separation `(V(G)-U,B)` and let its root connectivity be
`k<=5`. If `k=5`, five disjoint paths from the original roots to `B`
terminate at five distinct vertices of `A union D` and are otherwise
outside `B`. Every original root already in `B` is a trivial terminator,
so appending the linkage cannot put another original root into its bag.
Retain only their five boundary root bags and the two
helpers, and append the paths to the corresponding root bags. This
gives two adjacent helpers full to all five original roots, proving `P`.

If `k<=4`, take an isolator `(C,E)` with `C subset V(G)-U` and
`B subset E`, of order `k`. Inside `G[E]`, its root linkage terminates
at `k` distinct boundary vertices of `B`. Restrict the full two-helper
model to those `k` roots and append the linkage. For `k<=3`, the full
two-helper configuration contains a rooted `K_k`: for `k=3`, absorb
one helper into each of two root bags; the smaller cases follow by
restriction. For `k=4`, absorb one helper into one root bag. The other
helper remains universal to the four roots, and the absorbed helper
gives a root star with three edges, containing a three-vertex root
path; this contains a dart. For `k=0`, use the empty rooted clique.

The isolator interior `E-C` contains `U`, so has at least two vertices.
It is root-free, has at most four neighbours, and has nonpositive
density by 4-lightness. The just-constructed clique or dart makes it
reducible, contrary to restriction 2. Both values of `k` are impossible,
which eliminates the supposed degree-five edge. A two-vertex blocker has nine incident edges and neither vertex sees both
split endpoints. Consequently its two vertices are adjacent, both see the
other three boundary vertices, and each sees a different split endpoint.
They have degree five and three common neighbours, so this case is excluded. Every contraction
used above is accompanied by its fixed rooted preimages, and the
alternate single-edge contraction strictly decreases vertex count.

## Nonroot minimum degree at least five

**Theorem.** In the minimum counterexample above, every vertex of
`V(G)-X` has degree at least five.

**Proof.** Suppose a nonroot `v` has degree at most four. The graph
`H=G-v`, with the same five roots, satisfies

`rho4(H)=rho4(G)+4-deg_G(v)>=2`.

Suppose `H` is not 4-light. Then it has a root-free fragment `Y` with at
most four neighbours and positive density. If `v` has no neighbour in
`Y`, its boundary and incident edges are unchanged in `G`, contrary to
4-lightness of `G`. Otherwise, adding `v` to the boundary increases its
density by the positive integer `e_G(v,Y)`, so the side in `G` has
density at least two. Its boundary has at most five vertices, and
4-lightness of `G` forces exactly five.

This root five-separation is proper. Its nonempty interior is `Y`; if
its closed side were all of `G`, its boundary would contain all five
original roots as well as the distinct nonroot `v`, which is impossible
for a boundary of order five. We have obtained the excluded proper
density-at-least-two side. Thus `H` is 4-light.

The graph `H` has fewer vertices and retains density at least two and
all five roots. Minimality gives `P(H,X)`, whose unchanged bags give
`P(G,X)`, a contradiction. This proves the claim. No chromatic
criticality is asserted for `H`.

## A rooted triangle lemma

**Lemma.** Let `(R,S)` be an internally three-connected three-rooted
finite simple graph with at least one nonroot. Suppose `R-S` is
connected, every root has a neighbour in `R-S`, and every nonroot has
degree at least four. Then `R` has an `S`-rooted triangle minor.

**Proof.** We first recall and prove the elementary fact that three
distinct vertices `a,b,c` of a two-connected graph admit a rooted
triangle minor. Take a cycle through `a,b`. If it contains `c`, contract
its three root-to-root arcs into the three root bags. Otherwise take a
two-fan from `c` to the cycle, with distinct ends `x,y` and internally
disjoint paths meeting the cycle only at their ends. If an `x`–`y` arc
of the cycle contains both `a,b`, that arc together with the fan gives
a cycle through all three roots. In the remaining case the two cycle
arcs contain `a,b` separately, and the fan gives a third `x`–`y` path
containing `c`. These three paths form a theta. Put `x` and all but `y`
of the first path in the `a` bag, put `y` and all but `x` of the second
path in the `b` bag, and use the interior of the third path for the `c`
bag. They are connected and pairwise adjacent. Cases with `a` or `b`
at `x` or `y` already fall in the cycle-through-three-roots case.

The graph `R` is connected. Consider its block-cut tree, representing a
root at its cutvertex node when it is a cutvertex and otherwise at its
unique block node. Take the median of the three root nodes: the unique
node lying on all three pairwise connecting paths, allowing coincident
root nodes.

If the median is a block node, the three roots have three distinct
attachment vertices in that block, where a root already in the block
is its own attachment. They are distinct because a shared cutvertex
attachment for two roots would put their median at that cutvertex
node; roots represented by the block node itself are distinct noncut
vertices. Consequently the block is not a bridge. The elementary
two-connected fact gives a rooted triangle at the three attachment
vertices. The three root-to-block paths have disjoint interiors outside
the block. Appending them to the appropriate bags supplies the required
triangle rooted at the original roots.

If the median is a cutvertex `c`, every component of `R-c` contains at
most one of the three roots (a root equal to `c` is allowed). Any
nonroots in such a component, after removing its possible root, form
a nonempty root-free set with boundary contained in `c` and that root.
That is a boundary of order at most two, contrary to internal
three-connectivity. Thus all nonroots are contained in `{c}`. Since
there is at least one, `c` is a nonroot and is the unique nonroot. It
has degree at most three, contrary to the hypothesis. This excludes
the cutvertex case and completes the proof.

## Internal five-connectivity

The additional input is the separately audited
[degree-five dart lemma](rooted_dart_nonroot_degree_five.md): an internally
four-connected four-rooted graph with at least two nonroots, each of
degree at least five, has a rooted dart. Its proof identifies the exact
terminal construction imported from Dvořák–Norin–Rahman Lemma 3.1.
The source SHA-256 is
`37dcf256f64fca7c49a1bd4ec66021371fba9a7863bf9523597ba4b898ecfad2`.

**Theorem.** The minimum counterexample `(G,X)` is internally five-connected.

**Proof.** Suppose there is a nonempty root-free set with boundary of
order at most four. Among all nonempty root-free sets choose one with
minimum boundary order `k<=4`. Passing to a component of its induced
graph cannot increase the boundary, so choose a connected such set `Y`.
Write `S=partial_G(Y)`; then `|S|=k` and every vertex of `S` has a
neighbour in `Y`. Let `R=G[Y union S]`, rooted at `S`.

For every nonroot subset of `R`, all incident edges and neighbours are
the same as in `G`. Therefore minimality of `k` implies that `R` is
internally `k`-connected. Its nonroots retain their full degrees from
`G`, which are at least five by the nonroot degree bound above. Its density
is nonpositive because `G` is 4-light.

If `k=0` or `k=1`, the empty rooted clique or the one-vertex rooted
clique makes `Y` reducible immediately. If `k=2`, connectedness of `Y`
and its contacts with both roots give a path between the two roots
with interior in `Y`. Its contraction gives a boundary-rooted `K2`,
so again `Y` is reducible. If `k=3`, apply the rooted triangle lemma,
whose degree-four bound is weaker than the present degree-five bound,
to obtain a boundary-rooted `K3`, again making `Y` reducible.

Finally, if `k=4`, then `|Y|>=2`: a single nonroot would have degree
at most four in `R`. The degree-five dart lemma supplies a rooted dart,
making `Y` reducible in this case as well. Every case contradicts the
audited exclusion of reducible fragments. Thus no such `Y` exists,
which is exactly internal five-connectivity.

## Historical reduction gap and its closure

The restrictions above alone do not justify removing or replacing an
arbitrary positive quotient fragment while retaining 4-lightness, density
at least two, all five original roots and a strictly decreasing measure.
Selecting a minimum positive-density obstruction does not justify forcing
a smaller one through crossing: internal five-connectivity neither makes
every edge contractible nor makes every fragment at such a cut positive
in density.

The [degree-six reduction](hc7_c21_helper_degree_six.md) and
[padded atom argument](five_root_one_missing_contact.md) close the rooted
helper theorem using these restrictions. The latter minimizes over all
eligible ordinary fragments after padding, verifies the exact atom
theorem hypotheses, and obtains a contradiction without the unsupported
positive-density intersection claim. It does not supply an arbitrary
fragment replacement lemma. These reductions alone prove neither
Conjecture 21 nor HC7.
