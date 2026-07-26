# The common incident-pair deletion is six-connected or gives a strict exact-seven response

**Status:** written proof;
[separately audited GREEN](hc7_order8_incident_pair_common_deletion_connectivity_audit.md).

The unified response-column construction selects two edges incident with one
literal vertex.  This note spends seven-connectivity directly on their
common deletion.  Failure of six-connectivity is not another unbounded cut:
it isolates the common endpoint and returns the exact recursive output
required by the order-eight laboratory.

## 1. A uniform connectivity lemma

### Lemma 1.1

Let `G` be seven-connected, let

\[
                         e=va,\qquad f=vb              \tag{1.1}
\]

be distinct edges, and put

\[
                         H=G-\{e,f\}.                  \tag{1.2}
\]

Then at least one of the following holds.

1. `H` is six-connected.
2. The vertex `v` has degree seven in `G`,

   \[
                    N_G(v)=N_H(v)\mathbin{\dot\cup}\{a,b\},
                    \qquad |N_H(v)|=5,                 \tag{1.3}
   \]

   and `N_H(v)` is a five-vertex cut of `H` whose deletion isolates `v`.

#### Proof

Suppose `H` is not six-connected.  It has a vertex cut `T` of order at most
five.  The vertex `v` does not belong to `T`: if it did, every deleted edge
would already be absent from `G-T`, so

\[
                              H-T=G-T
\]

would be connected by seven-connectivity.

The graph

\[
                         H-(T\cup\{v\})=G-(T\cup\{v\}) \tag{1.4}
\]

is connected, because `|T union {v}|<=6`.  Consequently all vertices of
`H-T` other than `v` lie in one component.  Since `H-T` is disconnected,
`{v}` is its only other component, and hence

\[
                              N_H(v)\subseteq T.        \tag{1.5}
\]

Seven-connectivity gives `d_G(v)>=7`.  Only the two edges in (1.1) were
removed at `v`, so

\[
                  5\le d_H(v)\le |T|\le5.             \tag{1.6}
\]

Every inequality is equality.  Thus `T=N_H(v)`, `d_G(v)=7`, and the two
deleted outer endpoints are precisely the remaining neighbours in (1.3).
This is outcome 2. \(\square\)

## 2. Application to the order-eight response columns

### Theorem 2.1 (six-connected common deletion or strict restart)

Use the exact order-eight two-full-component setting and select the
noncontacting incident pair

\[
                         g_p=vy_p,\qquad g_q=vy_q       \tag{2.1}
\]

from the written
[unified incident-pair normal form](hc7_order8_unified_incident_pair_normal_form.md).
Let `C` be the old connected full component containing `v`, and put

\[
                         H=G-\{g_p,g_q\}.               \tag{2.2}
\]

Then at least one of the following holds.

1. `H` is six-connected and six-chromatic.
2. The singleton `A={v}` and boundary `T=N_G(v)` form a generic exact-seven
   response interface whose selected edge is either `g_p` or `g_q` and
   whose connected shore is a proper subset of `C`.

Thus outcome 2 is a strict recursive exit on the literal shore-order
parameter used by the order-eight response-column target.

#### Proof

First, `H` is a proper minor of `G`, so `chi(H)<=6`.  If `H` had a
five-colouring, recolour `v` with one fresh sixth colour and restore both
deleted edges.  The fresh colour appears at no neighbour of `v`, so this
would be a six-colouring of `G`.  Therefore

\[
                              \chi(H)=6.                \tag{2.3}
\]

Apply Lemma 1.1.  Only its second outcome requires proof.  It gives

\[
                         d_G(v)=|N_G(v)|=7.             \tag{2.4}
\]

The other old full component is anticomplete to `v`, so it lies outside
`{v} union N_G(v)` and supplies a nonempty opposite open shore.  Hence

\[
 V(G)=\{v\}\mathbin{\dot\cup}T\mathbin{\dot\cup}
       \bigl(V(G)-(\{v\}\cup T)\bigr)                 \tag{2.5}
\]

is an actual separation with boundary `T=N_G(v)`.

The colouring table in the unified incident-pair theorem supplies a proper
six-colouring of `G-g_p` in which the ends of `g_p` have the same colour
and `g_q` remains proper.  Its restriction to the closed shore opposite
`{v}` is proper.  The induced equality partition on `T` cannot extend
through the intact closed singleton shore: if it did, a permutation of the
six colours would align the two boundary colourings and would six-colour
`G`.  Thus (2.4), together with `g_p` and that colouring, is a generic
exact-seven response interface.  The same argument can use `g_q`.

Finally, `C` is adjacent to every vertex of the old eight-vertex boundary.
If `C={v}`, then `v` has at least those eight neighbours, contrary to
(2.4).  Therefore `{v}` is a proper connected subset of `C`, so the restart
is strict. \(\square\)

### Corollary 2.2 (the only root-first provenance obstruction)

Assume outcome 1 of Theorem 2.1 and the bypass outcome of the unified
incident-pair theorem.  Let `U` be the union of its two named bichromatic
components and, when they are disjoint, its one named joining edge.  Let
`w` be the opposite fan centre.  Then at least one of the following holds.

1. The support `U-w` contains a `y_p`--`y_q` path.  The ambient support `U`
   retains the two named component switches.  After possibly changing which
   nonresponse label is consumed, either it has a clean interior which adds
   the missing endpoint-column contact, or its first old-object encounter
   is a latent column rather than a root.
2. The vertex `w` separates `y_p` from `y_q` in `U`, while the common
   deletion `H-{v,w}` contains another `y_p`--`y_q` path.  The latter path
   need not lie in `U` and carries no bichromatic-component provenance.

#### Proof

The support `U` is connected, contains `y_p,y_q`, and avoids `v`.  If
`U-w` contains an endpoint path, choose one.  It avoids both fixed centres.
If its first old-object encounter is a noncentral vertex of a current root,
the free-root conversion in the audited
[latent-column spanning normalization](hc7_order8_latent_column_spanning_normalization.md)
turns that hit into a latent-column hit.  Both endpoint labels survive the
change because they are response labels, not the two nonresponse labels.
The same lemma gives the stated “at or before” interpretation for enlarged
columns.  If no old object is met internally, truncate after the last visit
to the first endpoint column and before the first subsequent visit to the
second.  Clean absorption along that subpath adds the missing endpoint
contact.

Otherwise `w` separates the endpoints in `U`.  Six-connectivity of `H`
implies that deleting `v,w` leaves a connected graph, so it contains an
endpoint path avoiding both centres.  Nothing forces this second path to
use the two named bichromatic components, which is exactly the stated loss
of provenance. \(\square\)

## 3. Exact gain and trust boundary

Outside the permitted strict exact-seven restart, all colouring signatures,
the universal-saturation components and the coupled bypass live in one
six-connected six-chromatic graph `H`.  Standard six-connected linkage
theorems may therefore be applied in that same common deletion without a
separate connectivity hypothesis.

This does not allocate such a linkage around the fixed latent columns.  In
particular, an unlabelled rooted minor or two--three linkage may consume the
root and column subgraphs whose operation provenance must be retained.  The
remaining bypass obstruction is now either a first column already contacting
the starting column, or the exact fixed-centre separation in Corollary 2.2.
The remaining theorem is still a label-preserving dirty-bypass or joint-
saturation composition in the six-connected graph `H`.

## 4. Dependencies

- [unified noncontacting incident-pair response](hc7_order8_unified_incident_pair_normal_form.md);
- [eight-latent-column spanning normalization](hc7_order8_latent_column_spanning_normalization.md); and
- [generic exact-seven response restart](hc7_generic_exact7_response_restart.md).
