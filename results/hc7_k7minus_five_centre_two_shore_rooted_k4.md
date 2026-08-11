# Universal four-boundary rooted `K_4` models on both two-cut shores

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_five_centre_two_shore_rooted_k4_audit.md`](hc7_k7minus_five_centre_two_shore_rooted_k4_audit.md).
This is an unbounded, computation-free refinement of the two-cut outcome in
the five-centre common-matching theorem.  It does not prove the `K_7^-`
six-colour conjecture or `HC_7`.

## 1. Setting

Use the hypotheses and notation of the
[five-centre common-matching theorem](hc7_k7minus_five_centre_common_matching_reduction.md).
Thus

\[
                         M=\{zx_z:z\in Z\},
 \qquad                  H=G-M,
\]

where `Z` is an independent set of five degree-eight vertices and `M` is a
matching.  Suppose `kappa(H)=2`.  The cited theorem gives a two-cut
`{p,q}` of `F=G-Z`.  Put

\[
                         S=Z\mathbin{\dot\cup}\{p,q\}.
\]

The graph `G-S` has exactly two connected components, both full at `S`.
Orient them as `C,D`, where `C` has the equal pole-colour response and `D`
has the distinct pole-colour response.  For every `z\in Z`, the selected
vertex `x_z` is the unique neighbour of `z` in one of `C,D`.  Define

\[
                         U=\{z\in Z:x_z\in C\}.       \tag{1.1}
\]

Thus every member of `U` has exactly one neighbour in `C`.  If `U` is
empty, every centre has exactly one neighbour in `D`.

## 2. The two-shore theorem

### Theorem 2.1

For every four-set `Q\subseteq S`, the graph

\[
                         G[D\cup Q]                   \tag{2.1}
\]

contains a `K_4` minor rooted at the four literal vertices of `Q`.

If `U` is nonempty, then, for every four-set `Q\subseteq S`, the graph

\[
                         G[C\cup Q]                   \tag{2.2}
\]

also contains a `Q`-rooted `K_4` minor.

#### Proof

The assertion for `D` is the audited
[universal four-boundary rooted-`K_4` theorem](hc7_k7minus_five_centre_universal_boundary_rooted_k4.md),
which applies because `D` is the distinct-response component.

Suppose `U` is nonempty and choose `z\in U`.  Then `x_z` is the unique
neighbour of `z` in `C`.  The audited
[singleton-shift theorem](../active/hc7_k7minus_five_centre_singleton_shift.md)
therefore gives

\[
                         |E(G[C])|\geq3|C|-2,
 \qquad                  |C|\geq8.                   \tag{2.3}
\]

Fix a four-set `Q\subseteq S` and put `J=G[C\cup Q]`.  The audited
[closed-shore rooted-connectivity lemma](hc7_closed_shore_rooted_connectivity.md),
applied with opposite component `D`, says that `(J,Q)` is internally
four-connected: no separation of order at most three has all four roots
on one closed side and a nonempty root-free open side.

Suppose that `J` has no `Q`-rooted `K_4` minor.  By Theorem 15 of
Fabila-Monroy and Wood, `J` is a spanning subgraph of a graph `J^+` in one
of their six rooted-`K_4` obstruction classes.  Each nominated vertex lies
in the planar base graph, and every vertex outside the base belongs to a
clique whose external neighbourhood is contained in one triangle of the
base.

No such added clique is nonempty.  Indeed, take a component `W` of its
intersection with `J`.  All four roots lie in the base and
`|N_J(W)|\leq3`, so `W\cup N_J(W)` and `V(J)-W` give precisely the
separation excluded by internal four-connectivity.  Hence `J` is a
subgraph of the planar base and is itself planar.  Its induced subgraph
`G[C]` is then planar, so

\[
                         |E(G[C])|\leq3|C|-6,
\]

contrary to (2.3).  Thus (2.2) has the required rooted model. `\square`

### Corollary 2.2 (exact orientation alternative)

In the two-cut outcome of the common-matching theorem, exactly one of the
following descriptions applies.

1. `U` is empty.  All five selected vertices `x_z` lie in `D`, and every
   centre has `x_z` as its unique `D`-neighbour.
2. `U` is nonempty.  Both closed shores contain a rooted `K_4` on every
   prescribed four-set of the seven-vertex boundary `S`.

This is only a description of the selected matching orientation; it does
not assert that the first alternative occurs in a critical host.

## 3. Exact noncomposition residue

Theorem 2.1 is simultaneous only at the level of existence.  In its second
alternative, the rooted models on `C` and `D` may depend independently on
the chosen four-set and need not have compatible branch sets.

The natural seven-bag composition makes the missing allocation explicit.
Choose four-sets on the two shores with one common boundary root, take a
rooted `K_4` model on each shore, and merge the two bags containing the
common root.  This gives seven disjoint connected bags.  The three
unmerged bags on the `C`-side and the three unmerged bags on the `D`-side
already form cliques within their respective shores, and the merged bag is
adjacent to all six.  To obtain `K_7^-`, however, at least eight of the
nine cross-shore pairs must be adjacent.

Since `C` and `D` are anticomplete, those cross-shore adjacencies must be
supplied through literal boundary incidences, the five selected edges
`zx_z`, or other centre contacts.  The separate rooted-model theorems do
not prescribe which branch bag contains any selected vertex `x_z` or any
other centre contact.  The punctured family of 31 matching signatures
controls endpoint colours on the common deleted-edge host, but it supplies
no such branch-set allocation and no common boundary partition for the
independently chosen models.

Making both rooted models spanning does not repair this.  Fullness gives
each of the three exclusive boundary roots on either shore a neighbour in
the opposite open component, but that neighbour may belong to the bag
which is merged at the common root.  Such a contact adds no entry to the
three-by-three cross-shore adjacency matrix.  Thus fullness alone does not
force even a specified entry of that matrix; the terminal threshold remains
eight of its nine entries.

Consequently the first unsupported implication is the following
simultaneous selection statement:

> either choose the two rooted `K_4` models so that all but at most one of
> the nine cross-shore bag pairs receive a literal contact, or obtain a
> six-colouring, an explicit `K_7^-` model by another allocation, or an
> exact response-bearing separation.

Theorem 2.1 does not prove this statement.  In the alternative `U=empty`,
even the universal rooted-`K_4` supply on the equality shore is not yet
available.  These are the two exact residues left by the present argument.

## Dependencies

The common matching orientation and the singleton contact in (1.1) come
from the audited five-centre common-matching theorem.  The distinct-shore
model is the audited universal four-boundary rooted-`K_4` theorem.  The
equality-shore density is the audited singleton-shift theorem, and its
relative connectivity is the audited closed-shore rooted-connectivity
lemma.  The external rooted-minor input is Ruy Fabila-Monroy and David R.
Wood, [*Rooted `K_4`-Minors*](https://doi.org/10.37236/3476), *Electronic
Journal of Combinatorics* **20** (2013), Paper P64, Theorem 15.
