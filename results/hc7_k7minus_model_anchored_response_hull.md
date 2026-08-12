# A model-anchored hull for a fixed coordinate response

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_model_anchored_response_hull_audit.md).
This is a conditional reduction inside the eight-coordinate campaign.  It
does not prove the `K_7^-` six-colour conjecture or `HC_7`.

The fixed-coordinate list-core reduction preserves an edge-deletion
colouring while decreasing the selected side, but it need not preserve a
connected complement inside the branch set containing that side.  The
following construction restores that complement.  Its exact limitation is
important: a proper list-critical core need not give a proper anchored hull.

## 1. Setting

Let `G` be a finite graph which is not six-colourable.  Let

\[
                              e=uv
\]

be an edge, and let `c` be a proper six-colouring of `G-e`.  Let `R` be a
connected vertex set and let `Y` be a nonempty proper connected subset of
`R` such that `R-Y` is nonempty and connected.  Suppose that:

1. `Y` meets `{u,v}`;
2. there is a nonempty connected set `D` disjoint from `R` and anticomplete
   to `Y`.

In the eight-coordinate application, `R` is a named branch set of the
spanning exact `K_7^vee` model, `D` is a named far branch set, `e` belongs
to `F_8`, and `c` is the singleton-signature colouring belonging to `e`.

Put `S=N_G(Y)` and, for `x in Y`, define

\[
                   L_Y(x)=[6]-c(N_G(x)\cap S).          \tag{1.1}
\]

Let `K` be vertex-minimal subject to `G[K]` not being colourable from
`L_Y|K`.  By the fixed-coordinate response-core theorem, `K` is connected;
it contains the unique end of `e` in `Y`, or both ends when both lie in
`Y`.

The connected set `R-Y` lies in one component `W` of `G[R-K]`.  Define the
**anchored hull** of `K` in `R` by

\[
                         \widehat K=R-W.                \tag{1.2}
\]

## 2. Exact hull theorem

### Theorem 2.1 (model-anchored fixed-response hull)

In the setting above:

1. `K subseteq widehat K subseteq Y`, both `widehat K` and `R-widehat K`
   are nonempty and connected, and `D` is anticomplete to `widehat K`;
2. `N_G(widehat K)` is an actual separator, `c|G-widehat K` is proper, and
   the equality partition induced by `c` on `N_G(widehat K)` is rejected by
   the intact closed `widehat K`-side;
3. if

   \[
       L_{\widehat K}(x)
       =[6]-c(N_G(x)\cap N_G(\widehat K)),
   \]

   then `G[widehat K]` is not colourable from `L_widehat K`;
4. every adjacency from `R-Y` to a named set outside `R` is retained by
   `R-widehat K`.  Consequently, any prescribed branch-set contacts already
   retained by `R-Y` remain retained after the replacement of `Y` by
   `widehat K`.

Moreover,

\[
 \widehat K\subsetneq Y
 \quad\Longleftrightarrow\quad
 W\cap(Y-K)\ne\varnothing.                             \tag{2.1}
\]

Thus a proper anchored hull is a strict side-order reduction preserving the
same model bag, its connected complement, the named far branch set, the edge
`e`, and the colouring `c`.  If `G` is seven-connected, its actual boundary
has order at least seven.

#### Proof

Since `K subseteq Y`, the connected set `R-Y` is contained in `R-K` and
therefore lies wholly in one component `W`.  Hence

\[
                         R-Y\subseteq W,                \tag{2.2}
\]

which gives `widehat K subseteq Y`.  The component `W` is nonempty and
connected.  The set `K` is contained in `widehat K`, so `widehat K` is
nonempty and contains the required end or ends of `e`.

Every component of `G[R-K]` other than `W` has an edge to `K`.  Indeed,
`G[R]` is connected, and the first edge leaving such a component on a path
to `K` has its other end in `K`; it cannot enter another component of
`G[R-K]`.  Since `K` is connected, the union of `K` with all components
other than `W` is connected.  This union is exactly `widehat K`.  Thus both
parts of the split

\[
                        R=\widehat K\mathbin{\dot\cup}W
\]

are connected.  As `widehat K subseteq Y`, the named far set `D` remains
anticomplete to it.  In particular, `D` lies outside
`N_G[widehat K]`, so `N_G(widehat K)` is an actual separator.

The colouring `c` can fail on `G` only at `e`.  Since `widehat K` contains
an end of `e`, its restriction to `G-widehat K` is proper.  If its boundary
partition extended through `G[widehat K union N_G(widehat K)]`, a
permutation of the six colour names followed by gluing would six-colour
`G`, a contradiction.  This proves item 2.

For every `x in K`, each old boundary neighbour of `x` is also a boundary
neighbour of `widehat K`, because `widehat K subseteq Y`.  Therefore

\[
 c(N_G(x)\cap N_G(Y))
 \subseteq
 c(N_G(x)\cap N_G(\widehat K))
\]

and hence

\[
                        L_{\widehat K}(x)\subseteq L_Y(x). \tag{2.3}
\]

The graph `G[K]` is not colourable from the larger lists `L_Y|K`, so it is
not colourable from `L_widehat K|K`.  A colouring of `G[widehat K]` from
`L_widehat K` would restrict to one of `G[K]`, proving item 3.

Item 4 follows directly from (2.2), because `R-Y` is a subset of
`R-widehat K=W`.  Finally, (2.2) and the partition

\[
             R-K=(R-Y)\mathbin{\dot\cup}(Y-K)
\]

show that `widehat K=Y` exactly when `W` contains no vertex of `Y-K`.
This is (2.1).  Proper containment then strictly decreases the positive
integer side order.  Seven-connectivity gives the final boundary bound.
`\square`

### Corollary 2.2 (exact-model provenance)

Let

\[
                     P,B,C,U_1,U_2,U_3,U_4
\]

be the labelled spanning exact `K_7^vee` model in the eight-coordinate
host.  Let `R` be one of its branch sets, let `Y subsetneq R` satisfy the
hypotheses of Theorem 2.1, and suppose that the far set `D` is another named
branch set.  If `e in F_8` and `c` is its singleton-signature colouring,
then the anchored hull retains all of the following data on the same graph:

- the original labelled exact model;
- the same containing branch set `R` and a connected complement
  `R-widehat K` inside it;
- the same named far branch set `D`, anticomplete to `widehat K`;
- the same coordinate `e`, colouring `c`, and rejected exterior trace; and
- every labelled model adjacency whose witness from `R` already had an end
  in `R-Y`.

#### Proof

The anchored hull changes none of the seven original branch sets, so the
labelled spanning exact model itself remains fixed.  The remaining claims
are items 1, 2 and 4 of Theorem 2.1. `\square`

## 3. Iteration and the exact stopping configuration

### Corollary 3.1 (anchored descent or an internal separating core)

Starting with `Y`, repeatedly take a vertex-minimal boundary-list-critical
core and replace the current side by its anchored hull whenever that hull is
proper.  The process terminates.  At every step it preserves:

- the same edge `e` and colouring `c`;
- an actual rejected exterior trace;
- containment in `R` and connectedness of both parts of the split of `R`;
- the named far set `D`; and
- every prescribed external contact retained by the preceding branch-set
  complement.

At the terminal side `Z`, one of the following holds.

1. `Z` itself is vertex-minimal uncolourable from its boundary lists.
2. Its vertex-minimal uncolourable core `K_Z` is proper, and the component
   of `G[R-K_Z]` containing `R-Z` is exactly `R-Z`.  Equivalently, `K_Z`
   separates every component of `G[R-K_Z]` contained in `Z-K_Z` from the
   exterior branch-set complement `R-Z`.

#### Proof

Every proper replacement strictly decreases the finite positive integer
`|Y|`, so the process terminates.  The preserved properties are Theorem
2.1.  If the terminal critical core is not the whole side, failure of a
proper anchored hull and (2.1) say that its exterior component contains no
vertex of `Z-K_Z`; because it contains all of `R-Z`, it is exactly `R-Z`.
The stated separation description follows from the component definition.
`\square`

## 4. Why a proper critical core does not suffice

The second outcome of Corollary 3.1 is genuine at the level of the hull
operation.  Let `G[R]` be the path `r-k-a`, take `Y={k,a}` and `K={k}`.
Then `R-Y={r}` is connected, but the component of `R-K` containing `r` is
the singleton `{r}`.  Consequently

\[
                         \widehat K=Y
\]

although `K` is a proper subset of `Y`.  Assigning an empty list to `k`
makes `K` a vertex-minimal list obstruction, so list-criticality alone does
not repair the failure.

The same topology can occur with a genuine fixed-edge response.  Take a
`K_7` on vertices `u,v,a_1,...,a_5`, let `e=uv`, and colour `K_7-e` with
`u,v` equal and `a_1,...,a_5` using the other five colours.  Add a vertex
`t` adjacent only to `u` and a vertex `d` adjacent only to `a_1`.  Extend
the colouring by giving `t` the colour of `a_1` and `d` the colour of `u`.
With

\[
             R=\{a_1,u,t\},\qquad Y=\{u,t\},\qquad D=\{d\},
\]

the singleton `K={u}` has an empty boundary list, carries the same
fixed-edge response, and is proper in `Y`; nevertheless its anchored hull
is all of `Y`.  This graph contains a literal `K_7` and is not a critical
host.  It therefore does not refute a theorem that spends target exclusion
and the full eight-coordinate exact-model structure.  It proves only that
strictness is not a formal consequence of the anchored hull construction.

Accordingly, the next host-level theorem must analyse the second outcome of
Corollary 3.1: the list-critical core together with the branch-set
appendages which it separates from the connected complement.  Repeating
the hull operation alone cannot remove those appendages.

## Dependencies and scope

The endpoint and list-critical assertions used here are
[`hc7_k7minus_fixed_coordinate_response_core_reduction.md`](../results/hc7_k7minus_fixed_coordinate_response_core_reduction.md).
The exact-model response side which motivates the hypotheses is supplied by
[`hc7_k7minus_eight_coordinate_endpoint_visibility.md`](../results/hc7_k7minus_eight_coordinate_endpoint_visibility.md).

The theorem is unbounded and computation-free.  It supplies a corrected
model-anchored reduction, not boundary compression.  It does not prove that
the anchored hull is proper whenever the list-critical core is proper; the
explicit response example above shows that inference is unsupported without
additional critical-host structure.
