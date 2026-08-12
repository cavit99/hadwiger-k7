# Fixed-coordinate response inheritance and side reduction

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_fixed_coordinate_response_core_reduction_audit.md);
and recorded route nonclosure.  This note does not prove the `K_7^-`
six-colour conjecture or `HC_7`.

The purpose of this note is to separate two kinds of minimisation.  A fixed
edge-deletion response is inherited by every connected subset containing an
endpoint of the deleted edge.  Boundary-list-critical minimisation therefore
strictly reduces the order of the selected side whenever its critical core is
proper.  It need not reduce the order of the boundary.

## 1. Setting

Let `G` be a finite graph which is not six-colourable.  Let

\[
                              e=uv
\]

be an edge, and let `c` be a proper six-colouring of `G-e`.  Necessarily
`c(u)=c(v)`, since otherwise `c` would colour `G`.

Call a nonempty connected set `Y` an **actual side** when

\[
                         V(G)-N_G[Y]\ne\varnothing.       \tag{1.1}
\]

Suppose that `Y` meets `{u,v}`, and put `S=N_G(Y)`.  For `x in Y`, define
the boundary list

\[
              L_Y(x)=[6]-c\bigl(N_G(x)\cap S\bigr).       \tag{1.2}
\]

In the eight-coordinate application, `e` is one edge of the coordinate
forest and `c` is its singleton-signature colouring.  After the other forest
edges are restored, `c` is precisely a proper colouring of `G-e`.

## 2. Inheritance by connected rooted subsets

### Lemma 2.1 (fixed-coordinate response inheritance)

Let `K` be a nonempty connected subset of `Y` with

\[
                              K\cap\{u,v\}\ne\varnothing. \tag{2.1}
\]

Then `N_G(K)` is an actual separator, `c|G-K` is proper, and the equality
partition induced by `c` on `N_G(K)` is not induced by any proper
six-colouring of

\[
                         G[K\cup N_G(K)].             \tag{2.2}
\]

Thus the same edge `e` and the same colouring `c` give a rejected exterior
trace on `K`.  If `G` is seven-connected, then

\[
                              |N_G(K)|\ge7.             \tag{2.3}
\]

#### Proof

Let `R=V(G)-N_G[Y]`.  The set `R` is nonempty and anticomplete to `Y`, so
it is disjoint from `K\cup N_G(K)`.  Hence `N_G(K)` is an actual separator.

The sole edge on which `c` can fail after `e` is restored is `e` itself.
Condition (2.1) deletes at least one end of that edge, so `c|G-K` is proper.
If the equality partition on `N_G(K)` extended through (2.2), permute the
six colour names in that extension so that it agrees with `c` on the
boundary.  Gluing it to `c|G-K` would give a proper six-colouring of `G`, a
contradiction.  This proves the response assertion.  Seven-connectivity
gives (2.3). `\square`

The lemma requires no inherited minor-model labels and no upper bound on
the original boundary.

## 3. The boundary-list-critical core

### Theorem 3.1 (rooted list-critical side reduction)

The graph `G[Y]` is not colourable from the lists in (1.2).  Let `K` be
vertex-minimal subject to `G[K]` not being colourable from the restricted
lists `L_Y|K`.  Then:

1. `G[K]` is connected;
2. if exactly one end of `e` lies in `Y`, that end belongs to `K`;
3. if both ends of `e` lie in `Y`, both belong to `K`; and
4. `K` carries the same fixed-coordinate response described in Lemma 2.1.

In particular, if `K` is a proper subset of `Y`, then

\[
                              |K|<|Y|,                 \tag{3.1}
\]

so the fixed edge and colouring are retained under a strict decrease in
the order of the connected side.

#### Proof

The colouring `c|G-Y` is proper because `Y` contains an end of `e`.  If
`G[Y]` had an `L_Y`-colouring, it would agree properly with `c` across every
edge between `Y` and `S`; adjoining `c|G-Y` would colour `G`.  Thus the
claimed list obstruction exists.

If `G[K]` were disconnected, each of its components would be a proper
induced subgraph and hence colourable from its restricted lists by the
choice of `K`.  Their colourings would combine, contradicting the choice of
`K`.  This proves item 1.

Suppose first that `Y` contains exactly one end of `e`, say `u`.  For every
induced subgraph of `G[Y-u]`, the restriction of `c` is proper and respects
all the lists in (1.2): the only improper boundary incidence under `c` can
be the edge `uv`.  Hence a non-`L_Y`-colourable subgraph must contain `u`.

Suppose instead that `u,v in Y`.  Every edge from `Y` to `S` is proper
under `c`, and the only improper edge inside `Y` is `uv`.  If an induced
subgraph omits either `u` or `v`, the restriction of `c` is a proper
`L_Y`-colouring of that subgraph.  Thus `K` contains both ends.  Items 2
and 3 follow, and Lemma 2.1 gives item 4.  Proper containment gives (3.1).
`\square`

### Corollary 3.2 (well-founded reduction of the side)

Repeat Theorem 3.1 using the new boundary lists induced by the same
colouring `c`.  Every proper step retains the relevant end or ends of `e`
and strictly decreases the number of vertices in the connected side.
Consequently the process terminates at a connected actual side `Y_*` which
still carries the response at `e` and for which `G[Y_*]` is vertex-minimal
uncolourable from the lists induced by `c|N_G(Y_*)`.

#### Proof

Lemma 2.1 makes every new side actual and preserves the fixed response.
Theorem 3.1 retains the required endpoint set at the next step.  The lists
induced by the new boundary are no larger than the old lists on the chosen
core, so the new side remains list-uncolourable.  Every proper replacement
strictly lowers its positive integer order. `\square`

## 4. Exact nonclosure

The preceding reduction controls `|Y|`, not `|N_G(Y)|`.  For a proper core
`K subsetneq Y`, one has

\[
 N_G(K)=\bigl(N_G(K)\cap S\bigr)
          \mathbin{\dot\cup}
          \bigl(N_G(K)\cap(Y-K)\bigr),               \tag{4.1}
\]

and the second term has no bound in terms of `|S|`.  The new boundary may
therefore be larger than the old one.  At the terminal side `Y_*`, the
whole side is already a boundary-list-critical graph, so Theorem 3.1 gives
no further reduction.  In particular `Y_*` may be the singleton containing
one end of `e`.

This failure is genuine at the level of the displayed hypotheses.  The
[rooted boundary-compression barrier](../barriers/hc7_k7minus_anchored_coordinate_compression_barrier.md)
gives graphs of arbitrarily high connectivity and minimum degree in which
the fixed-coordinate response side is a singleton with arbitrarily large
boundary.  Those graphs contain a `K_7^-` minor and are not critical hosts,
so the construction does not refute a theorem which spends target exclusion.

The audited
[large actual-boundary reduction](../results/hc7_k7minus_matching_lock_boundary_reduction.md)
does strictly lower every boundary of order at least ten, but it chooses a
fresh low-degree singleton and a fresh edge-deletion colouring.  That
singleton need not meet `e`, so the reduction need not retain the coordinate
or the colouring `c`.  We therefore have the exact quantifier mismatch

\[
 \begin{array}{c|c|c}
 \text{operation}&\text{strictly decreases}&\text{may lose}\\ \hline
 \text{fixed-trace list core}&|Y|&\text{boundary order}\\
 \text{generic large-boundary reduction}&|N_G(Y)|&e\text{ and }c.
 \end{array}                                           \tag{4.2}
\]

Consequently an arbitrary-order coordinate response is not yet terminal.
The smallest missing positive statement must use `K_7^-`-minor exclusion to
give either the target, a compatible boundary partition, or a reduction to
boundary order seven or eight which retains one original coordinate and
its exterior colouring.  Without such a statement, Corollary 3.2 stops at
the boundary-list-critical or singleton endpoint above.

## 5. Application

The starting fixed-coordinate response in the forced eight-coordinate
host is supplied by the
[endpoint-visibility theorem](../results/hc7_k7minus_eight_coordinate_endpoint_visibility.md).
The present note shows exactly what can be iterated from that response
without preserving the exact near-clique model: the connected side can be
made boundary-list-critical while retaining one coordinate, but its
boundary cannot presently be compressed.
