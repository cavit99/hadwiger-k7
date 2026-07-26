# A noncontacting incident-source pair in the order-eight response columns

**Status:** written proof;
[separately audited GREEN](hc7_order8_low_degree_incident_source_fork_audit.md).

This note uses the low contact degree now attached to a response-source
label.  It produces two noncontacting source columns, a common three-edge
response table, and an exact bichromatic saturation-or-bypass alternative.
It does not solve the remaining dirty-path exchange.

## 1. Setting

Use the order-eight two-full-component setting of the audited
[dual-free-root response-star theorem](hc7_order8_dual_free_root_response_star.md).
Assume that `G` has no `K_7` minor and that the theorem's separation and
strict-descent alternatives have not occurred.  Thus a `K_5` minor in the
column contact graph would lift with the two roots to a `K_7` minor.
Fix its original edge `e=vx`, its six-colouring `c` of `G-e`, and a surviving
free-root choice with two roots and seven columns.  Label the target column
`L_t`, the five source columns `L_0,...,L_4`, and the auxiliary column
`L_q`.  For each `i`, let

\[
                         v_i\in V(L_i)                 \tag{1.1}
\]

be the prescribed first neighbour of `v` on the corresponding
`c`-bichromatic path from `v` to `x`.  Thus `vv_i` is an edge and the five
vertices `v_i` are distinct.

Let `J` be the contact graph of the seven columns.  Assume that

\[
                  t i\in E(J)\quad(0\le i\le4)        \tag{1.2}
\]

and that some source `i` satisfies \(d_J(i)\le3\).  The audited six-vertex
rooted-`K_4` lemma guarantees such a source whenever \(\delta(J)\le3\) and
(1.2) holds, because `J` is `K_5`-minor-free.

## 2. Noncontacting source pair

### Proposition 2.1

There are at least two source labels \(j\ne i\) for which

\[
                         ij\notin E(J).                \tag{2.1}
\]

For every such `j`, the literal vertices `v_i,v_j` are nonadjacent in `G`.

### Proof

Besides `i`, the contact graph has the target, four other sources and the
auxiliary label.  The target is already one neighbour of `i`, so at most
two of the other five labels can be neighbours.  At least three are
nonneighbours, and at most one of those is auxiliary.  This proves (2.1)
for at least two sources.  Noncontacting columns have no edge between any
of their literal vertices, so in particular `v_iv_j` is absent. \(\square\)

Fix one label `j` given by Proposition 2.1 and put

\[
             f_i=vv_i,\qquad f_j=vv_j,
             \qquad H=G-\{e,f_i,f_j\}.                \tag{2.2}
\]

## 3. Common operation table and bichromatic fork

### Theorem 3.1 (noncontacting incident-source fork)

The graph `H` has six-colourings with the following equality signatures on
the ordered edge triple `(e,f_i,f_j)`:

\[
       (=,\ne,\ne),\qquad(\ne,=,\ne),\qquad
       (\ne,\ne,=),\qquad(\ne,=,=).                  \tag{3.1}
\]

It has no six-colouring with signature \((\ne,\ne,\ne)\).

Moreover, the last colouring is the restriction to `H` of a proper
six-colouring `kappa` of `G-{f_i,f_j}` satisfying

\[
 N_G(v)\cap\kappa^{-1}(\kappa(v))=\{v_i,v_j\}.       \tag{3.2}
\]

In this same colouring, at least one of the following holds.

1. One of `f_i,f_j` has its two endpoints in one component of

   \[
   (G-\{f_i,f_j\})
      [\kappa^{-1}(\{\kappa(v),\gamma\})]
   \]

   for every one of the five colours `gamma` different from `kappa(v)`.
2. The graph `(G-{f_i,f_j})-v` has a `v_i`--`v_j` path contained in two
   named bichromatic components and at most one edge between them.
   Interchanging one component gives a six-colouring of `G-f_j`, while
   interchanging the other gives a six-colouring of `G-f_i`.

All edge labels, source vertices, roots and columns remain the literal
objects selected from the original `(e,c)` response star.  The colouring
`kappa` is a new simultaneous-contraction colouring and need not induce the
same boundary partition as `c`.

### Proof

The original colouring `c` of `G-e`, restricted to `H`, has signature
\((=,\ne,\ne)\).  Colour the proper minor `G/f_i` and expand its contracted
edge; restricting to `H` gives \((\ne,=,\ne)\).  The symmetric contraction
of `f_j` gives \((\ne,\ne,=)\).

The edges `f_i,f_j` form a two-edge tree and their outer endpoints are
nonadjacent by Proposition 2.1.  Contract both edges, colour the resulting
proper minor, and expand the contracted vertex over `v,v_i,v_j`.  This is a
proper colouring of `G-{f_i,f_j}` and hence restricts to a colouring
`kappa` of `H` with signature \((\ne,=,=)\).  Every other neighbour of `v` is
adjacent to the contraction vertex, proving the exact trace (3.2).

A colouring with signature \((\ne,\ne,\ne)\) would restore all three deleted
edges and six-colour `G`, which is impossible.  Finally apply Theorem 1.1
of the audited
[incident-edge bichromatic saturation-or-bypass theorem](hc7_shared_interface_bichromatic_bypass.md)
to `f_i,f_j` and the simultaneous-contraction colouring.  Its two outcomes
and the coupled one-edge response colourings are exactly those displayed
above. \(\square\)

## 4. Clean bypass or a dirty old object

### Corollary 4.1

In outcome 2 of Theorem 3.1, truncate the bypass after its last visit to
`L_i` and before its first subsequent visit to `L_j`.  Its internal vertices
avoid both endpoint columns and are nonempty.  If they also avoid the two
roots and the other five columns, then they may be absorbed into `L_i`,
preserving all labels, root contacts and old column contacts while adding
the missing contact `ij`.

Consequently, either the enlarged contact graph has a `K_5` minor and gives
an explicit `K_7`-minor model with the two roots, or it is a valid
same-label column system with strictly more contacts.  In a
contact-maximal system, every bypass from Theorem 3.1 therefore meets a root
or a third column before reaching `L_j`.

### Proof

The endpoint columns are anticomplete, so the truncated path has nonempty
interior.  Under the clean-interior hypothesis, adjoining that interior to
`L_i` preserves connectedness and disjointness and creates the contact with
`L_j`; no old vertex or edge is removed.  A `K_5` model in the new contact
graph lifts through the five column unions and the two roots.  Otherwise the
new system contradicts contact maximality. \(\square\)

## 5. Exact remaining alternatives

The source-saturated low-degree branch is reduced to two objects tied to
prescribed source edges of the original response:

1. one incident edge is bichromatically saturated for all five alternate
   colours in the common contraction colouring; or
2. a bypass with two coupled one-edge responses first meets an old root or
   column.

The saturation paths are not assigned to column labels beyond their named
edge, and a dirty bypass does not by itself permit a no-contact-loss
reassignment.  Neither alternative is a common boundary partition, an
exact-seven response, or a strict shore descent.
