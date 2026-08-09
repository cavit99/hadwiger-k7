# Exact boundary traces and a bounded shore reduction

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_four_centre_exact_u_bridge_reduction_audit.md`](hc7_k7minus_four_centre_exact_u_bridge_reduction_audit.md).

This note uses exact boundary colourings at the four independent centres to
reduce the minimum selected component of the four-centre cut.  The reduction
does not prove the required rooted minor.  It replaces an unrestricted shore
by one bichromatic support and at most eight components that contain a
neighbour of a centre.

## 1. Setting

Use the minimum trace-admissible cut from the audited
[generalized-wheel leaf theorem](hc7_k7minus_four_centre_wheel_leaf_descent.md):

\[
 H-T=C\mathbin{\dot\cup}D,
 \qquad
 N_G(C)=N_G(D)=S=U\mathbin{\dot\cup}T,                \tag{1.1}
\]

where `U` is an independent set of four degree-eight vertices, `|T|=3`,
and `C` has minimum order among the selected components carrying the fixed
trace.  The graph `G[T]` has an edge and is not a triangle, and `G[S]` has
no `K_5` minor.  Hence `G[T]` is either a three-vertex path or the disjoint
union of an edge and an isolated vertex.

A proper six-colouring of a closed shore is **exact at `U`** if one colour
occurs on `S` precisely at `U`.  Write

\[
 \Delta=U\mid\{p\}\mid\{p'\}\mid\{q\},
 \qquad
 \Pi=U\mid\{p,p'\}\mid\{q\},                          \tag{1.2}
\]

where `pp'` is a nonedge and `q` is adjacent to at least one of `p,p'`.
The symbols in (1.2) denote equality partitions of the literal boundary,
not prescribed colour names.

The exact-block anchor theorem gives an exact-`U` colouring of each closed
shore.  The two shores cannot realize the same equality partition: after a
permutation of colour names, the two colourings would agree on `S` and
glue to a six-colouring of `G`.

## 2. A bichromatic support on the minimum side

### Theorem 2.1

For some labelling `T={p,p',q}` as in (1.2), the minimum side `C` satisfies
one of the following alternatives.

1. **Paired boundary vertices.**  The closed `C`-shore has an exact-`U`
   colouring with partition `Pi` and has no such colouring with partition
   `Delta`.  Let `alpha` be the colour of `p,p'`.  For each of the three
   colours `lambda` absent from `S`, there is an `alpha`--`lambda` path
   from `p` to `p'` whose nonempty interior lies in `C`.  Paths belonging
   to distinct choices of `lambda` can meet only at vertices of colour
   `alpha`.

2. **Distinct boundary colours.**  The closed `C`-shore has an exact-`U`
   colouring with partition `Delta` and rejects a partition `Pi` realized
   on the closed `D`-shore.  There is a bichromatic `p`--`p'` path whose
   nonempty interior lies in `C`.

#### Proof

If the `C`-shore rejects `Delta`, any exact-`U` anchor on that shore pairs
two nonadjacent vertices of `T`; this is alternative 1.  Fix its colouring.
For a colour `lambda` absent from `S`, suppose that `p` and `p'` lie in
different `alpha`--`lambda` components.  Interchanging the two colours on
the component containing `p` produces a proper colouring with boundary
partition `Delta`, a contradiction.  A shortest path in the common
component has all its internal vertices in `C`.  Two paths using distinct
secondary colours can share only vertices of their common colour `alpha`.

Now suppose that the `C`-shore realizes `Delta`.  The `D`-shore cannot do
so, and therefore it realizes some paired partition `Pi`.  The `C`-shore
rejects that same partition.  Apply the exact singleton-block Kempe
exchange to `p,p'` in the `Delta` colouring of the closed `C`-shore.  A
successful interchange would give exactly `Pi`; hence the other outcome
is a bichromatic `p`--`p'` path with its interior in `C`.  The interior is
nonempty because `pp'` is a nonedge.  \(\square\)

The two alternatives cover the case in which neither shore realizes
`Delta`: then `G[T]` is an edge plus an isolated vertex, and the two shores
realize the two different possible paired partitions.

## 3. Attachment inequalities

Choose a connected set `Y subseteq C` and a clique `Q subseteq T` as
follows.

- In alternative 1, let `Y` be the interior of any one of the three paths
  and put `Q={q}`.
- In alternative 2, if `G[T]` is a three-vertex path, let `q` be its middle
  vertex, let `Y` be the path interior, and put `Q={p,q}`.
- In alternative 2, if `G[T]` is an edge plus an isolated vertex, label
  `p` as the endpoint of the edge which is paired with the isolated vertex
  `p'`, and let `q` be the other endpoint.  Enlarge the path interior to a
  connected set `Y subseteq C` containing a neighbour of `q`, and put
  `Q={p,q}`.  Such an enlargement exists because `C` is connected and is
  full to `q`.

In the first case `Y union {p,p'}` is connected and adjacent to `q`.  In
the other two cases `Y union {p'}` is connected and adjacent to both
vertices of the clique `Q`.

For a component `K` of `C-Y`, define

\[
 A_K=N_C(K)\cap Y,
 \qquad
 B_K=N_S(K),                                           \tag{3.1}
\]

and put

\[
 a_K=|A_K|,
 \qquad
 d_K=4-|B_K\cap U|,
 \qquad
 e_K=3-|B_K\cap T|.                                   \tag{3.2}
\]

### Theorem 3.1

Every component `K` of `C-Y` satisfies

\[
 N_G(K)=A_K\mathbin{\dot\cup}B_K,
 \qquad
 a_K\ge d_K+e_K,                                      \tag{3.3}
\]

and

\[
                         U\cup Q\nsubseteq B_K.       \tag{3.4}
\]

If `d_K=0`, then the stronger inequality

\[
                         a_K\ge e_K+1                 \tag{3.5}
\]

holds.

#### Proof

Different components of `C-Y` are anticomplete, and `C` is anticomplete to
`D`.  This proves the equality in (3.3).  The connected set `D` lies
outside `K union N_G(K)`, so seven-connectivity gives
`|N_G(K)|>=7`.  Since `|B_K|=7-d_K-e_K`, the inequality in (3.3) follows.

Suppose that `U union Q subseteq B_K`.  In alternative 1, the connected
set `K` supports the boundary block `U`, while `Y` supports `{p,p'}` and
`Q={q}`.  In alternative 2, `K` supports `U`, while `Y` supports `{p'}`.
In both cases the vertices of `Q` are singleton blocks and form a clique.
An edge from `K` to `Y` supplies the adjacency between the two supported
blocks.  The definition of `Y` supplies every remaining adjacency to `Q`.
These connected subgraphs and their boundary blocks satisfy the hypotheses
of the exact response-reflection theorem for the partition realized on the
closed `C`-shore.  That theorem would six-colour `G`, a contradiction.  This
proves (3.4).

It remains to prove (3.5).  Suppose `d_K=0` and equality holds in (3.3).
By (3.4), some vertex of `Q subseteq T` is absent from `B_K`, so
`e_K>=1`.  In the four-connected completed side

\[
                         F=H[C\cup T]+\binom{T}{2},     \tag{3.6}
\]

the set

\[
                         A_K\cup(B_K\cap T)             \tag{3.7}
\]

separates `K` from any vertex of `T-B_K`.  Its order is
`a_K+3-e_K`.  Four-connectivity of `F` gives
`a_K+3-e_K>=4`, which is (3.5).  \(\square\)

## 4. Bounded centre-bearing remainder

### Corollary 4.1

The set `Y` may be enlarged, without losing the properties above, so that
`C-Y` has at most eight components.  Every remaining component contains a
neighbour of a vertex of `U`, at most two remaining components are adjacent
to all four vertices of `U`, and at most two have `|A_K|=1`.

If `|A_K|=1`, then for a unique `u in U`,

\[
 B_K=S-\{u\}.                                          \tag{4.1}
\]

#### Proof

Fix `u in U` and choose a neighbour of `u` in `D`.  This vertex is
anticomplete to `N_C(u)`.  Since the independence number of the
neighbourhood of every degree-eight centre is three, one has

\[
                         \alpha(G[N_C(u)])\le2.        \tag{4.2}
\]

Neighbours of `u` in distinct components of `C-Y` are pairwise
nonadjacent.  Thus `u` meets at most two such components.  Over the four
centres, at most eight components meet `U`.

Absorb every other component into `Y`.  Each absorbed component has an edge
to the old `Y`, so the enlarged set remains connected and retains the
required boundary contacts.  Distinct old components are anticomplete, so
the centre-bearing components are not merged.  There are at most eight of
them.  A component adjacent to all four centres contributes four of the at
most eight centre-component incidences, so there are at most two such
components.

Finally, let `a_K=1`.  Equations (3.3) and (3.4) give
`d_K+e_K=1`.  The case `d_K=0` is excluded by (3.5).  Hence
`d_K=1` and `e_K=0`, which is exactly (4.1).  Such a component meets three
centres.  The same incidence bound permits at most two of them.  \(\square\)

For any bichromatic path used above, each centre has at most two neighbours
of either path colour by (4.2).  Thus it has at most four neighbours on the
path interior.  Intersections among the three paths in alternative 1 may
still be unbounded, and Corollary 4.1 does not produce a rooted
`K_6^-` model by itself.

## Dependencies

- [Four-centre rooted-web cut and exact static residue](hc7_k7minus_four_centre_web_cut_lattice.md), especially Corollary 5.2.
- [Generalized-wheel leaf descent](hc7_k7minus_four_centre_wheel_leaf_descent.md), Corollary 2.2.
- [Exact-block anchors across two full shores](hc7_two_full_shore_exact_block_kempe_transition.md), Theorem 2.1.
- [Exact singleton-block Kempe exchange](hc7_exact7_singleton_block_kempe_exchange.md).
- [Exact response reflection](hc7_exact7_selected_response_preservation.md), Theorem 1.1.
- [Four-connectivity of the completed minimum side](hc7_k7minus_four_centre_completed_side.md), Theorem 2.1.
- [Degree-eight neighbourhood structure](hc7_k7minus_exceptional_neighbourhood_completion.md), Theorem 2.
