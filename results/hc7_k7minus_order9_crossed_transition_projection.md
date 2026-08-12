# Projecting a crossed response transition back to the order-nine boundary

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_order9_crossed_transition_projection_audit.md).
This note
addresses the unbounded separator returned by an unlocked palette in the
opposite-shore matching case.  It does not bound that separator.  Instead it
projects the same transition back to the original nine-vertex boundary,
where it gives either a boundary colouring rejected by both shores or one
single boundary Kempe interchange between opposite-shore colourings.  It
does not prove the `K_7^-` six-colour conjecture or `HC_7`.

## 1. Setting

Let `G` satisfy

\[
 \chi(G)=7,\qquad
 \chi(J)\leq6\text{ for every proper minor }J,
 \qquad \kappa(G)\geq7,
 \qquad K_7\npreccurlyeq G.                         \tag{1.1}
\]

Suppose

\[
 V(G)=A\mathbin{\dot\cup}T\mathbin{\dot\cup}B,
 \qquad A,B\ne\varnothing,
 \qquad E_G(A,B)=\varnothing,
 \qquad |T|=9,                                      \tag{1.2}
\]

and choose vertex-disjoint edges

\[
                       e=up,\qquad f=vq,             \tag{1.3}
\]

with `u in A`, `v in B` and `p,q in T`.  Put

\[
                              H=G-\{e,f\}.            \tag{1.4}
\]

Let `phi` be a proper six-colouring of `H` such that

\[
       \phi(u)=\phi(p)=i,
       \qquad \phi(v)\ne\phi(q).                    \tag{1.5}
\]

Assume that `u,p` lie in different components of the subgraph of `H`
induced by colours `i,j`, for some `j ne i`.  The forbidden all-proper
signature then gives two distinct `i`--`j` components `D_1,D_2`: each
contains one end of `e` and one end of `f`, and interchanging `i,j` on
either component changes (1.5) into the opposite singleton response.

A labelled proper colouring of `G[T]` **extends through `A`** when it is
the restriction of a proper six-colouring of `G[A union T]`; define
extension through `B` symmetrically.  No labelled boundary colouring
extends through both sides, since two such extensions would glue across
the anticomplete sets `A,B`.

## 2. A small boundary support for one actual response separator

### Theorem 2.1 (order-nine projection)

There is a choice `D in {D_1,D_2}` with all the following properties.

1. `D` is not dominating.  Consequently `N_G(D)` is an actual response
   separator of order at least seven: the two opposite singleton
   colourings agree literally on `G-D`, and their common boundary
   partition is rejected by the intact `D`-side.
2. The set

   \[
                              W=D\cap T               \tag{2.1}
   \]

   is nonempty, is a union of components of the `i`--`j` subgraph of
   `G[T]`, and satisfies

   \[
                              1\leq |W|\leq4.          \tag{2.2}
   \]

   If the other one of `D_1,D_2` is dominating, then `|D|=2` and the
   stronger bound `|W|<=2` holds.
3. Let `K_1,...,K_m` be the components of the boundary `i`--`j` graph
   contained in `W`.  Starting with `phi|T` and interchanging `i,j`
   successively on `K_1,...,K_m` gives a sequence

   \[
                         \theta_0,\theta_1,\ldots,\theta_m,       \tag{2.3}
   \]

   of proper labelled boundary colourings with `m<=4`.  The first extends
   through `B`, the last extends through `A`, and at least one of the
   following holds:

   (a) some intermediate `theta_r` extends through neither side; or

   (b) for some `r`, the adjacent colourings `theta_{r-1},theta_r`
   extend through opposite sides.  Their difference is one boundary
   Kempe interchange on the literal component `K_r subseteq W`, with
   `|K_r|<=4`.

#### Proof

The two crossed components cannot both dominate.  For completeness, if
they did, the only edges of `G` between them would be the two omitted
edges `e,f`.  Domination in both directions would force each component to
consist of its two coordinate endpoints.  Connectedness inside `H` would
then make the four endpoints an induced four-cycle whose opposite edges
are `e,f`.  Contract that cycle.  A five-colouring of the contraction
would expand to a six-colouring of `G`, using the old colour on one
independent pair of the cycle and a fresh sixth colour on the other.
Thus the contraction is six-chromatic.  By `HC_6` it has a spanning `K_6`
model.  On lifting the contracted bag, the two dominating components and
the other five bags form a `K_7` model, contrary to (1.1).

If neither component dominates, choose `D` to minimise `|D cap T|`.
Their intersections with `T` are disjoint, so

\[
             |D\cap T|\leq
             \left\lfloor\frac{|T|}{2}\right\rfloor=4.          \tag{2.4}
\]

If exactly one component dominates, choose the other as `D`.  Every
vertex of `D` is then adjacent to the dominating component.  Distinct
`i`--`j` components have no edge between them in `H`, so the only possible
edges are `e,f`.  Each already has one end in `D`; hence `D` consists of
exactly those two ends.  It is nondominating, since both components cannot
dominate, and `|D cap T|<=2`.  This proves the upper bounds and the choice
of a nondominating component.

Both omitted edges have one end in `D`.  Interchanging `i,j` on `D`
therefore changes the signature from `(equal,proper)` to
`(proper,equal)`.  The two colourings agree outside `D`, and after deleting
`D` both restored edges lose one end.  Their common restriction is a
proper colouring of `G-D`.  Because `D` is nondominating, its open
neighbourhood is an actual separator; seven-connectivity gives
`|N_G(D)|>=7`.  If the common exterior boundary partition extended
through the intact `D`-side, the two colourings would align and glue to a
six-colouring of `G`.  This proves item 1.

An edge of the boundary `i`--`j` graph from `D cap T` to
`T-D` would be an edge of `H` joining `D` to another `i`--`j` vertex,
which is impossible.  Thus `W` is a union of boundary components.
If `W` were empty, the two opposite singleton colourings would agree on
all of `T`.  The original colouring is proper on `G[B union T]`, since
the only equal omitted pair there is `e` and its `A`-end has been removed.
The switched colouring is proper on `G[A union T]` by the symmetric
statement for `f`.  They would therefore glue, again six-colouring `G`.
Hence `W` is nonempty and item 2 follows.

Switching one whole component of the boundary two-colour graph preserves
properness.  The underlying two-colour components do not change when
their two colour names are interchanged, so the successive switches in
(2.3) are well defined and their total effect on `T` is exactly the
switch on `D`.  The extension assertions for the two endpoints were
proved in the preceding paragraph.

Suppose no intermediate colouring is rejected by both sides.  Let `r` be
the first index for which `theta_r` extends through `A`.  The index is
positive because `theta_0` already extends through `B` and no colouring
extends through both sides.  By the choice of `r`, `theta_{r-1}` does not
extend through `A`; by the present supposition it therefore extends
through `B`.  Again disjointness of the two extension languages says that
`theta_r` extends only through `A`.  This is outcome 3(b).  If the
supposition fails, outcome 3(a) holds. `\square`

The bound (2.2) controls the support of the transition on the original
boundary, not the order of `N_G(D)`.  Vertices of the four other colours
inside either open side may belong to `N_G(D)`, and neither fullness of an
original component nor seven-connectivity gives an upper bound on their
number.

## 3. What the two projected outcomes give

### Corollary 3.1 (one boundary interchange gives bounded or full original components)

In outcome 3(b) of Theorem 2.1 there are two paths, one with nonempty
interior in `A` and one with nonempty interior in `B`, each joining
`K_r` to a different component of the corresponding boundary two-colour
graph.  If `Q_A,Q_B` are the components of `G-T` containing their
respective interiors, then they are distinct and

\[
                   7\leq |N_G(Q_A)|,|N_G(Q_B)|\leq9.              \tag{3.1}
\]

For either `Q in {Q_A,Q_B}`, one of the following holds.

1. `|N_G(Q)|` is seven or eight, and `Q` gives an actual response
   separation of that order.
2. `N_G(Q)=T`, so `Q` is a connected component full to the original
   nine-vertex boundary.

Thus, after order-seven and order-eight responses have been excluded, the
single-interchange outcome is supported by two named full components of
the original separation.

#### Proof

Let `theta` be the one of `theta_{r-1},theta_r` which extends through
`A`, and let `theta'` be the other, which extends through `B`.  Fix
extensions on the two closed sides.  In the `A`-extension, consider the
full `i`--`j` component containing `K_r`.  If it met the boundary only in
`K_r`, switching it would induce `theta'` on `T`, and that colouring would
glue to the fixed `B`-extension.  Hence this full component reaches a
different boundary component.  A shortest such path, stopped at its first
new boundary vertex, has nonempty interior in `A`.  The reverse argument
inside the `B`-extension gives the second path.  Their interiors lie in
opposite anticomplete open sides.

Each path interior lies in a component `Q` of `G-T`, whose neighbourhood
is contained in `T`.  The opposite open side is nonempty, so this
neighbourhood is an actual separator.  Seven-connectivity and `|T|=9`
give (3.1).  If its order is at most eight, six-colour the proper minor
`G-Q`.  Its boundary partition cannot extend through the intact `Q`-side,
or the two colourings would glue to colour `G`.  This is the asserted
response.  Equality nine is exactly `N_G(Q)=T`. `\square`

### Corollary 3.2 (the other outcome is the order-nine list-critical endpoint)

In outcome 3(a), let `theta` be a boundary colouring rejected by both
sides.  Each of `G[A]` and `G[B]` contains a connected induced subgraph
which is vertex-minimal subject to being uncolourable from the lists left
by `theta` on its literal boundary neighbours.

If `theta` uses all six colours on `T`, this is the paired full-six-colour
order-nine list-critical endpoint.  More generally, let `p` be the maximum
number of boundary colours used by a colouring extending through either
side.  Then exactly one of the following applies.

1. A full-six-colour boundary colouring is rejected by both sides, again
   giving the paired full-six-colour endpoint.
2. `p=6`, no full-six-colour boundary colouring is rejected by both sides,
   and therefore every full-six-colour boundary colouring extends through
   exactly one side.  This is the existing maximum-palette ownership
   residue.

If a selected list-critical subgraph `K` is proper in its original
component of `G-T`, then `K` itself is a strictly smaller connected
response side for a fresh proper-minor colouring, but its new boundary
order is not controlled.  Otherwise the selected kernel fills a named
original component.

#### Proof

Failure of extension through one closed side is exactly failure of list
colourability in its open part, with

\[
              L(x)=[6]-\theta(N_G(x)\cap T).                       \tag{3.2}
\]

A vertex-minimal induced uncolourable subgraph exists and is connected,
since otherwise one of its components would already be uncolourable.
This proves the first assertion.

No boundary colouring extends through both sides.  If some full-six-colour
trace extends through neither, outcome 1 holds.  Otherwise every such
trace extends through at least one side and therefore through exactly one
side.  It remains
only to note that `p<6` forces outcome 1.  Choose an extending boundary
colouring using `p` colours.  Since `|T|=9>p`, one colour class contains at
least two vertices.  Recolour one of them with a previously unused colour;
the boundary colouring remains proper and gains one colour.  Repeat until
all six colours occur.  Every intermediate colouring uses more than `p`
colours and therefore extends through neither side by the definition of
`p`.  In particular the final full-six-colour trace is rejected by both.
Thus failure of outcome 1 forces `p=6` and gives outcome 2.

For the final assertion, a minimal kernel `K` lies in one component `C` of
the corresponding open side.  If `K` is proper in `C`, six-colour the
proper minor `G-K`.  Its restriction to `N_G(K)` cannot extend through
the intact induced graph `G[K union N_G(K)]`, since such an extension
would align with the exterior colouring and six-colour `G`.  Thus `K`
itself is a connected response side, and `|K|<|C|`.  If no proper kernel
occurs, the kernel fills its component. `\square`

## 4. Exact gain and remaining obstruction

Theorem 2.1 removes the apparent need to control the unbounded separator
`N_G(D)` directly.  Every unlocked-palette transition has support on at
most four vertices of the original order-nine boundary.  It therefore
returns to one of two already bounded interfaces:

* a trace rejected by both shores, with paired list-critical subgraphs; or
* one boundary Kempe interchange between opposite-shore traces, with an
  order-seven, order-eight, or full-component conclusion inside each
  original shore.

This is a genuine projection, not an upper bound on `N_G(D)`.  Neither
bounded interface is terminal with the currently proved tools.  A
shore-filling paired list-critical kernel can retain positive excess, and
two full components supporting one boundary interchange do not assign its
paths to branch bags of the common `K_6` or exact `K_7^vee` model.  The
maximum-palette ownership residue is also unchanged.

Thus the next unsupported implication is narrower than arbitrary response
separator control: in the seven-connected common deletion host, combine
the common co-bagged `K_6` model or the exact `K_7^vee` model with either
the paired order-nine kernels or the two named full-component transition
paths.  Reapplying arbitrary donor minimisation to `N_G(D)` would discard
the bounded support proved here.

## Dependencies and scope

The Kempe switch which creates `D_1,D_2` is Theorem 2.6 of the
[`matching common-state theorem`](hc7_k7minus_matching_square_common_state.md),
or equivalently Theorems 2.1--3.2 of the
[`forbidden-signature Kempe note`](hc7_k7minus_matching_forbidden_signature_kempe_coupling.md).
Corollary 3.1 reproves the needed part of the audited
[`opposite-shore single-transition theorem`](../results/hc7_opposite_shore_single_kempe_transition.md).
Corollary 3.2 is the order-nine specialization of the audited maximum-palette
and boundary list-critical reductions.

No finite enumeration is used.  The proof is unbounded in the orders of
the open sides.  The remaining statements in Section 4 are route
nonclosures, not counterexamples to a model-allocation theorem using the
additional common-host structure.
