# A unified noncontacting incident-pair response at order eight

**Status:** written proof;
[separately audited GREEN](hc7_order8_unified_incident_pair_normal_form_audit.md).

This note combines the exposed source--target branch and the
source-saturated branch of the order-eight response-column construction.
In either branch, two noncontacting column labels are represented by two
literal edges incident with the same vertex, and one simultaneous
contraction gives the same exact colouring alternative.  The result does
not resolve a dirty bypass or universal bichromatic saturation.

## 1. Setting

Let `G` be seven-connected and satisfy

\[
 \chi(G)=7,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G,
 \qquad K_7\not\preccurlyeq G.                         \tag{1.1}
\]

Use outcome 3 of the audited
[dual-free-root response-star theorem](hc7_order8_dual_free_root_response_star.md)
for one fixed edge

\[
                         e=vx                         \tag{1.2}
\]

and one fixed six-colouring `c` of `G-e`.  Choose a surviving free-root
system whose seven-column contact graph `J` has minimum degree at most
three, as guaranteed by the audited
[dual-root contact-overlap theorem](hc7_order8_dual_root_contact_overlap_closure.md).
Write `L_t` for the target column containing `x`, write
`L_0,...,L_4` for the five response-source columns containing the prescribed
first neighbours `v_0,...,v_4` of `v`, and write `L_q` for the auxiliary
column.  Put

\[
             g_t=vx=e,
             \qquad g_i=vv_i\quad(0\le i\le4).        \tag{1.3}
\]

The contact graph `J` is `K_5`-minor-free, since a `K_5` model in its
columns together with the two roots would lift to a `K_7`-minor model in
`G`.

## 2. Selecting one noncontacting incident pair

### Proposition 2.1

There are distinct response labels

\[
                    p,q\in\{t,0,1,2,3,4\}            \tag{2.1}
\]

such that `L_p,L_q` do not contact and the corresponding edges

\[
                    g_p=vy_p,\qquad g_q=vy_q          \tag{2.2}
\]

are distinct edges incident with `v`.  Their outer endpoints `y_p,y_q`
are nonadjacent.

More precisely, one may choose:

1. `p=t,q=i` if some source `L_i` does not contact `L_t`; or
2. `p=i,q=j` if the target contacts all five sources, where `L_i` has
   contact degree at most three and `L_j` is another source not contacting
   `L_i`.

#### Proof

The first case is immediate from (1.3).  Suppose instead that the target
contacts all five sources.  The audited
[six-vertex source-rooted `K_4` lemma](hc7_six_vertex_source_rooted_k4.md)
then gives a response source `L_i` of contact degree at most three.  One of
its contacts is the target.  Among the four other sources and the auxiliary
column, it therefore has at least three nonneighbours, at least two of which
are sources.  Choose one of them as `L_j`.

In either case, contact-graph nonadjacency means that no host edge joins
the two literal columns.  Their prescribed vertices `y_p,y_q` are therefore
nonadjacent.  The edges in (2.2) are distinct by the response-star
construction. \(\square\)

## 3. One exact response table and one bichromatic fork

### Theorem 3.1 (unified noncontacting incident-pair normal form)

Choose `p,q` as in Proposition 2.1 and put

\[
                        F=G-\{g_p,g_q\}.               \tag{3.1}
\]

The graph `F` has six-colourings with equality signatures

\[
                  (=,\ne),\qquad(\ne,=),\qquad(=,=)    \tag{3.2}
\]

on the ordered pair `(g_p,g_q)`, and it has no six-colouring with signature
`(\ne,\ne)`.

The `(=,=)` colouring `kappa` may be chosen by contracting the two-edge
tree on `y_p,v,y_q`.  It satisfies the exact trace

\[
 N_G(v)\cap\kappa^{-1}(\kappa(v))=\{y_p,y_q\}.         \tag{3.3}
\]

In this same colouring, at least one of the following holds.

1. One of `g_p,g_q` has its endpoints in one component of

   \[
   F[\kappa^{-1}(\{\kappa(v),\gamma\})]
   \]

   for every colour `gamma` different from `kappa(v)`.
2. The graph `F-v` has a `y_p`--`y_q` path contained in two named
   bichromatic components and at most one edge between them.  Interchanging
   the component through `y_p` gives a six-colouring of `G-g_q`, while
   interchanging the component through `y_q` gives a six-colouring of
   `G-g_p`.

The endpoint columns, endpoint vertices and incident edges retain their
literal labels from the original fixed `(e,c)` response star.  The new
colouring `kappa` need not induce the boundary partition of `c`.

#### Proof

Colour the proper minor `G/g_p` and expand the contracted edge.  Since
`g_q` remains present, its endpoints have different colours; restricting
to `F` gives signature `(=,ne)`.  The symmetric contraction of `g_q`
gives `(ne,=)`.

The outer endpoints are nonadjacent by Proposition 2.1, so contracting
both edges and then expanding the contracted vertex gives a proper
six-colouring `kappa` of `F` with signature `(=,=)`.  Every neighbour of
`v` other than `y_p,y_q` remains adjacent to the contraction image, which
proves (3.3).  A colouring with signature `(ne,ne)` would allow both
deleted edges to be restored and would six-colour `G`.

The hypotheses of the audited
[incident-edge saturation-or-bypass theorem](hc7_shared_interface_bichromatic_bypass.md)
now hold literally.  Applying it to `g_p,g_q` and `kappa` gives the two
displayed alternatives and the two coupled one-edge responses. \(\square\)

### Corollary 3.2 (clean bypass augmentation)

In outcome 2, truncate the bypass after its last visit to `L_p` and before
its first subsequent visit to `L_q`.  If its internal vertices avoid both
roots and the other five columns, they can be absorbed into `L_p`,
preserving all labels, root contacts and old column contacts while adding
the missing contact `pq`.

Consequently the enlarged contact graph either contains a `K_5` minor,
which lifts with the two roots to an explicit `K_7`-minor model, or is a
same-label column system with strictly more contacts.

#### Proof

The endpoint columns are anticomplete, so the truncated path has nonempty
interior.  Under the stated avoidance condition, adjoining that interior
to `L_p` preserves connectedness and disjointness and removes no old
vertex or contact.  It creates an edge from the enlarged `L_p` to `L_q`.
The standard contact-graph lifting gives the final alternative. \(\square\)

## 4. A precise refinement of universal saturation

### Proposition 4.1 (response switch or joint triad saturation)

Suppose outcome 1 of Theorem 3.1 holds, and orient the pair so that
`g_p=vy_p` is linked for all five alternate colours.  For each such colour
`gamma`, let `Q_gamma` be the `kappa(v)`--`gamma` component containing
`v,y_p`.  Then at least one of the following holds.

1. For some `gamma`, the component `Q_gamma` omits `y_q`.  Interchanging
   its two colours and restoring `g_q` gives a named six-colouring of
   `G-g_p`.
2. Every `Q_gamma` contains the whole triad `v,y_p,y_q`.  There are five
   distinct edges at `v`, different from `g_p,g_q`, which are first edges
   of paths in the five components `Q_gamma`.  Together with `g_p,g_q`,
   these are seven prescribed incident edges.  Applying the
   prescribed-first-edge all-boundary fan theorem gives an explicit
   order-seven full-neighbourhood separation, a strict order-eight
   response-side descent, or an eight-fan preserving all seven first
   edges.

The eight-fan outcome preserves only the seven literal first edges.  It
does not assign the five bichromatic path interiors to distinct columns.

#### Proof

If `Q_gamma` omits `y_q`, its interchange changes `v,y_p` together and
leaves `y_q` unchanged.  Thus `g_p` remains monochromatic while `g_q`
becomes proper, so restoring `g_q` gives a proper colouring of `G-g_p`.

Otherwise each of the five components contains all three named vertices.
For each alternate colour, choose a simple path from `v` to `y_p` in its
component.  Its first neighbour has that alternate colour.  The five first
edges are consequently distinct, and none is one of the two deleted
edges.  Every neighbour of `v` lies in `C union S`, because `C` is
a component of `G-S`.  The two selected incident edges therefore complete
the required seven-edge set, so the audited prescribed-first-edge theorem
applies.  Its conclusions are exactly those stated. \(\square\)

## 5. Exact gain and trust boundary

The two formerly separate response-column branches now have one common
input to the remaining composition problem:

\[
 \text{one fixed response star}
 +\text{ two noncontacting incident seed edges}
 +\text{ one exact contraction colouring}.
\]

The common conclusion is universal saturation or a coupled dirty bypass.
The richer three-edge response table available when both labels are
sources is not asserted in the source--target case.  Neither the bypass nor
the joint-saturation eight-fan is a terminal conclusion.  In particular,
this theorem does not prove a no-loss column exchange, a common boundary
partition, a strict response-preserving descent in every case, closure of
the two-component order-eight interface, or `HC_7`.

## 6. Dependencies

- [two free root choices](hc7_order8_dual_free_root_response_star.md);
- [dual-root contact overlap closure](hc7_order8_dual_root_contact_overlap_closure.md);
- [six-vertex source-rooted `K_4` lemma](hc7_six_vertex_source_rooted_k4.md);
- [incident-edge saturation or bypass](hc7_shared_interface_bichromatic_bypass.md); and
- [prescribed-first-edge all-boundary fan](hc7_order8_arbitrary_edge_response_star.md).
