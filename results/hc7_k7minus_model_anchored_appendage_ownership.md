# Model ownership and coordinate avoidance behind an anchored core

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_model_anchored_appendage_ownership_audit.md).
This is a conditional reduction inside the eight-coordinate campaign.  It
does not prove the `K_7^-` six-colour conjecture or `HC_7`.

The model-anchored hull reduction can stop with a list-critical core which
separates appendages from the connected complement of its named branch set.
The correct minimisation class consists of ordinary exact minor models, not
only spanning ones.  In that class, every surviving appendage monopolises at
least two model adjacencies.  Minimising simultaneously over all eight
coordinate responses also makes every appendage free of coordinate
endpoints.

## 1. Setting and the global anchored class

Let `G` be seven-connected and not six-colourable.  Let `F_8` be a
componentwise-induced eight-edge forest such that the proper six-colourings
of `G-F_8` realise exactly the nonempty equality signatures on `F_8`.
For `f in F_8`, let `c_f` denote a singleton-signature colouring.  After
the other forest edges are restored, `c_f` is a proper six-colouring of
`G-f` whose only monochromatic edge in `G` is `f`.

An **anchored response configuration** consists of:

1. a labelled exact `K_7^vee`-minor model

   \[
                         P,B,C,U_1,U_2,U_3,U_4,         \tag{1.1}
   \]

   not necessarily spanning, in which `B,C,U_1,...,U_4` form a `K_6`
   model, `P` is anticomplete to `B,C`, and `P` is adjacent to every
   `U_i`;
2. one universal branch set `R=U_i` and a nonempty proper connected set
   `Z subset R` such that `R-Z` is nonempty and connected;
3. a named foreign branch set `D` which is anticomplete to `Z`; and
4. an edge `e in F_8` and its colouring `c_e`, where `Z` meets `e` and the
   boundary partition induced by `c_e` is rejected by the intact closed
   `Z`-side.

The last assertion automatically makes `G[Z]` uncolourable from the lists

\[
              L_Z(x)=[6]-c_e(N_G(x)\cap N_G(Z)).       \tag{1.2}
\]

Choose an anchored response configuration with `|Z|` minimum, globally
over the choice of the coordinate, its singleton-signature colouring, the
exact model and all the displayed labels.  This class is nonempty whenever
the endpoint-support capture outcome of the eight-coordinate visibility
theorem occurs: that theorem supplies a spanning member, which is also an
ordinary minor model.

Let `K subseteq Z` be a connected vertex-minimal subgraph which is not
colourable from `L_Z|K`.  The fixed-coordinate core theorem makes `K`
contain the relevant end or ends of `e`.  Apply the model-anchored hull
reduction.  If it gives a proper hull, global minimality is contradicted.
We may therefore assume that the component of `G[R-K]` containing `R-Z`
is exactly `R-Z`.

Call the other components of `G[R-K]` the **appendages**.  They are exactly
the components of `G[Z-K]`.  Let `mathcal F` be the six labels of the other
branch sets.  For an appendage `A`, define its model-monopoly set by

\[
 \Lambda(A)=\{Q\in\mathcal F:
      N_G(Q)\cap R\ne\varnothing
      \text{ and }N_G(Q)\cap R\subseteq A\}.          \tag{1.3}
\]

## 2. Ownership and coordinate-avoidance theorem

### Theorem 2.1

Either `G` contains a `K_7^-` minor, or all of the following hold.

1. Every appendage `A` satisfies

   \[
                              |\Lambda(A)|\ge2.         \tag{2.1}
   \]

2. The monopoly sets of distinct appendages are disjoint and none contains
   the far label `D`.  Consequently there are at most two appendages.
3. Every appendage is disjoint from `V(F_8)`.

#### Proof

Fix an appendage `A`.  Every component of `G[R-K]` has an edge to the
connected set `K`, because `G[R]` is connected.  Therefore both

\[
                         R'=R-A,
                 \qquad Z'=Z-A                         \tag{2.2}
\]

are nonempty and connected.  Moreover

\[
                              R'-Z'=R-Z,                \tag{2.3}
\]

so the branch-set complement remains connected.

Suppose first that `Lambda(A)=empty`.  Replace the branch set `R` by `R'`
and leave the vertices of `A` unused by the minor model.  Every required
model adjacency incident with `R'` survives by the definition of
`Lambda(A)`.  The other six branch sets and all their adjacencies are
unchanged.  Thus the seven sets remain a labelled exact `K_7^vee` model;
spanningness is neither part of the definition of a minor model nor needed
by the anchored response configuration.

The same edge `e`, colouring `c_e` and far branch set `D` remain available
for `Z'`.  The core `K` lies in `Z'`.  For `x in K`, every old boundary
neighbour remains a new boundary neighbour, while vertices of `A` may add
new boundary colours.  Hence

\[
       [6]-c_e(N_G(x)\cap N_G(Z'))\subseteq L_Z(x).    \tag{2.4}
\]

The core remains list-uncolourable.  Equivalently, the usual gluing
argument shows directly that the fixed exterior trace on `Z'` is rejected.
Equations (2.2)--(2.4) therefore give an anchored response configuration
with smaller side, contrary to global minimality.

Suppose next that `Lambda(A)={Q}`.  Move `A` from `R` into the branch set
`Q`, putting

\[
                              Q'=Q\cup A.               \tag{2.5}
\]

The set `Q'` is connected because the definition of monopoly supplies an
`A-Q` edge.  An edge from `A` to `K subseteq R'` restores the required
`R'Q'` adjacency.  Every other required adjacency at `R'` survives, and
enlarging `Q` destroys none of the remaining model adjacencies.  If the
move creates either of the optional adjacencies `PB,PC`, the seven branch
sets miss at most the other one and give an explicit `K_7^-` model.
Otherwise they remain an exact `K_7^vee` model.

The far label is not `Q`: the branch set `D` is anticomplete to
`A subseteq Z`, whereas membership in `Lambda(A)` supplies an edge to `A`.
Thus `D` remains unchanged and anticomplete to `Z'`.  The argument in
(2.3)--(2.4) again produces a smaller anchored response configuration.
This contradicts global minimality unless the target occurred.  We have
proved (2.1).

For distinct appendages `A,A'`, a nonempty set `N_G(Q) cap R` cannot be
contained in both disjoint components.  Their monopoly sets are therefore
disjoint.  The exact model requires an `R-D` edge, and `D` is anticomplete
to `Z`; every `R-D` endpoint in `R` consequently lies in `R-Z`.  Hence `D`
belongs to no monopoly set.  The monopoly sets are pairwise disjoint
subsets of the five labels in `mathcal F-{D}`, each of order at least two.
There are at most two appendages.

Finally suppose that an appendage `A` contains an endpoint of an edge
`f in F_8`.  Use the singleton-signature colouring `c_f`.  Deleting `A`
removes an end of its only monochromatic edge, so `c_f|G-A` is proper.  If
the boundary partition induced by `c_f` extended through the intact closed
`A`-side, the two colourings would align and glue to a six-colouring of
`G`.  Thus `A` carries a rejected response at the original coordinate `f`.

The same exact model can be used without alteration: `A subset R`, both
`A` and `R-A` are connected, and the named far branch set `D` is
anticomplete to `A subseteq Z`.  Hence `A`, `f`, `c_f` and the same model
form another anchored response configuration.  Since the nonempty core
`K` is disjoint from `A`, one has `|A|<|Z|`, contradicting global
minimality.  This proves item 3. `\square`

## 3. Consequences for the non-singleton terminal

### Corollary 3.1 (finite appendage normal form)

In a target-free host, the terminal model-anchored side has the form

\[
                        Z=K\mathbin{\dot\cup}A_1
                              \mathbin{\dot\cup}\cdots
                              \mathbin{\dot\cup}A_t,
                    \qquad 0\le t\le2,                \tag{3.1}
\]

where:

- `K` is boundary-list-critical and contains the endpoint set of the fixed
  coordinate `e` required by the fixed colouring;
- each `A_j` is connected, anticomplete to the other appendages and to
  `R-Z`, and attaches to `K`;
- each `A_j` monopolises at least two model labels, and those monopoly sets
  are disjoint subsets of the five labels other than `D`; and
- every endpoint of all eight coordinate edges which lies in `Z` lies in
  `K`.

#### Proof

The component description gives the first three structural assertions.
The ownership bound and coordinate avoidance are Theorem 2.1. `\square`

This removes the former internal-appendage escape.  An appendage with no
foreign contact has empty monopoly set and can simply be omitted from the
ordinary minor model.  Requiring the reselected model to remain spanning
would manufacture a false obstruction: spanningness was useful when first
obtaining and optimising the exact model, but is not part of the branch-set
axioms and is not needed after the response side has been anchored.

## 4. Exact remaining obligation

Theorem 2.1 is an unbounded, model-anchored use of the full coordinate
family.  It reduces an arbitrary collection of appendages to at most two
coordinate-free connected pieces with disjoint two-label ownership.

It does not yet eliminate those two pieces.  Moving either one destroys at
least two required contacts of `R`, while moving both may destroy four of
the five available contacts.  The next positive statement must combine
their disjoint ownership pattern with the list-critical structure of `K`
and target exclusion.  Its accepted conclusions should be an explicit
`K_7^-` model, a fixed-coordinate boundary of order seven or eight, or one
boundary partition extending through both sides.  Another minimisation of
unused vertices or branch-set order gives no further reduction in the
normal form (3.1).

There is, however, an exact operation-changing reduction which identifies
the remaining quantifier issue.  Let `A` be an appendage and choose an edge

\[
                              g=ak,
                    \qquad a\in A,quad k\in K.         \tag{4.1}
\]

Such an edge exists by the component description.  A six-colouring `c_g`
of the proper minor `G-g` makes the ends of `g` equal; otherwise it would
colour `G`.  Since deleting `A` removes `a`, the restriction `c_g|G-A` is
proper and its boundary partition is rejected by the intact closed
`A`-side.  Moreover `A` and `R-A` are connected, `D` is anticomplete to
`A`, and the same exact model remains fixed.  Hence `A` is itself a
strictly smaller model-anchored response side for the fresh edge `g`.

This observation eliminates every appendage if the minimisation is enlarged
from the eight forest edges to all edges of `G`.  It does not contradict
Theorem 2.1: global minimisation there deliberately ranges only over
singleton responses of members of `F_8`.  The price of (4.1) is exactly the
loss of the original coordinate and therefore of the punctured eight-
coordinate response cube.

Thus the first unsupported coordinate-preserving inference is now

\[
 \begin{gathered}
   A\text{ carries a fresh attachment-edge response on the same model},\\
   A\cap V(F_8)=\varnothing
 \end{gathered}
 \quad\Longrightarrow\quad
 \begin{gathered}
   \text{a response on }A\text{ retaining a member of }F_8,\quad\text{or}\\
   K_7^-\preccurlyeq G\text{ or a common boundary partition}.
 \end{gathered}                                       \tag{4.2}
\]

The complete signature cube does not supply the first conclusion: every
monochromatic forest edge of a signature survives wholly outside the
coordinate-free set `A`.  Any valid repair of (4.2) must therefore compare
the fresh attachment-edge colouring with the fixed forest-coordinate
colouring through the list-critical core `K`; it cannot come from the
vertex-cover criterion alone.

## Dependencies and scope

The anchored terminal configuration is supplied by
[`hc7_k7minus_model_anchored_response_hull.md`](hc7_k7minus_model_anchored_response_hull.md).
The fixed-coordinate list obstruction is
[`hc7_k7minus_fixed_coordinate_response_core_reduction.md`](../results/hc7_k7minus_fixed_coordinate_response_core_reduction.md).
The singleton-signature colourings and the original exact model are supplied
by
[`hc7_k7minus_eight_coordinate_endpoint_visibility.md`](../results/hc7_k7minus_eight_coordinate_endpoint_visibility.md).
The reassignment in (2.5) is the standard one-piece branch-set transfer used
in
[`hc7_rooted_persistent_model_edge.md`](../results/hc7_rooted_persistent_model_edge.md).

The proof is computation-free.  It deliberately allows the reselected
model to be nonspanning; no later conclusion in this note uses spanningness.
The theorem does not eliminate the surviving one- or two-appendage
ownership patterns, prove eight-coordinate terminalisation, Conjecture 21,
or `HC_7`.
