# Four-connectivity after completing a minimum exact-cut side

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_four_centre_completed_side_audit.md`](hc7_k7minus_four_centre_completed_side_audit.md).

This note strengthens the minimum exact-cut outcome of the four-centre
theorem.  Completing its three auxiliary boundary vertices to a triangle
gives a four-connected graph.  It also isolates a six-terminal rooted-minor
condition that would produce the required `K_7^-` minor.  The condition is
not proved here.

## 1. Setting

Let `G` satisfy

\[
 \chi(G)=7,\qquad
 \chi(M)\leq6\text{ for every proper minor }M\text{ of }G,
 \qquad K_7^-\npreccurlyeq G,
\]

and suppose that `G` is seven-connected and has minimum degree at least
eight.  Let `U` be an independent set of four degree-eight vertices and put
`H=G-U`.

Choose a trace-admissible exact cut of minimum selected-side order, in the
notation of the audited
[trace-preserving descent theorem](hc7_k7minus_four_centre_trace_descent.md):

\[
 H-T=C\mathbin{\dot\cup}D,
 \qquad N_G(C)=N_G(D)=U\mathbin{\dot\cup}T.           \tag{1.1}
\]

Thus `C,D` are connected, the four nominated rooted terminals avoid `C`,
one fixed terminal `x_j` lies in `D`, and the fixed six-colouring extends
over `G[C union U union T]` after the selected vertex `r in U` is restored.
The component `C` has at least two vertices.

Complete the boundary `T` to a triangle and write

\[
                         F=H[C\cup T]+\binom{T}{2}.   \tag{1.2}
\]

## 2. Four-connectivity of the completed side

### Theorem 2.1

The graph `F` is four-connected.

#### Proof

The graph `F` has at least five vertices.  Suppose that a set
`Z subseteq V(F)` of order at most three disconnects it.  If `T subseteq Z`,
then `Z=T` and `F-Z=H[C]` is connected.  Hence `T-Z` is nonempty.  Since
`T-Z` is a clique in `F-Z`, its vertices lie in one component.  Let `X` be
any other component.  Then `X subseteq C`.

The inclusion is strict.  This is immediate if `Z` meets `C`.  If
`Z subseteq T`, every vertex of `T-Z` has a neighbour in `C`, so the
component containing `T-Z` also contains a vertex of `C`.  Therefore

\[
                         \varnothing\ne X\subsetneq C. \tag{2.1}
\]

The added edges in (1.2) have both ends in `T`.  Since `X` is a component
of `F-Z` and `C,D` are anticomplete,

\[
                         N_G(X)\subseteq U\cup Z.     \tag{2.2}
\]

The set `D` lies outside `X union N_G(X)`.  Seven-connectivity and (2.2)
force

\[
 |Z|=3,\qquad N_G(X)=U\mathbin{\dot\cup}Z.           \tag{2.3}
\]

The audited two-component theorem now makes `X` one component of
`G-(U union Z)` and puts `x_j` in the other component.  Both components are
adjacent to every boundary vertex.  Moreover,

\[
                         X\cup U\cup Z
                         \subseteq C\cup U\cup T.     \tag{2.4}
\]

The old colouring therefore restricts to the new selected closed side, and
the same colour restores `r`.  The nominated terminals still avoid `X`, and
the named Kempe component in the unchanged graph is unchanged.  Thus
`U union Z` is a trace-admissible exact cut with selected component
`X subsetneq C`, contradicting the choice of `C`.  \(\square\)

The completion edges in (1.2) are auxiliary.  A minor model in `F` does not
automatically lift to `G`.

## 3. Rooted consequences in the original graph

Put `S=U dotcup T`.  Applying the audited
[closed-side rooted-connectivity lemma](hc7_closed_shore_rooted_connectivity.md)
to (1.1) gives the following.

### Corollary 3.1

For every nonempty `Q subseteq S`, the rooted pair

\[
                         (G[C\cup Q],Q)
\]

is internally `|Q|`-connected.  In particular,
`(G[C union U],U)` is internally four-connected and contains a
`U`-rooted `K_4^-` model by Jorgensen's rooted-minor theorem.

For every two-set `P subseteq T`, the pair

\[
 (L_P,U\cup P),\qquad L_P=G[C\cup U\cup P],          \tag{3.1}
\]

is internally six-connected.

## 4. The six-terminal rooted-minor criterion

### Proposition 4.1

Let `P subseteq T` have order two.  If `L_P` contains a
`(U union P)`-rooted `K_6^-` minor, then `G` contains a `K_7^-` minor.

#### Proof

Let `B_q`, for `q in U union P`, be the six rooted branch sets.  The set
`D` is a connected seventh branch set, disjoint from them and adjacent to
each through the literal root `q`.  Among the first six branch sets at most
one pair is nonadjacent.  Adding `D` gives a `K_7^-`-minor model.  \(\square\)

In the generalized-wheel branch, the audited
[canonical-leaf theorem](hc7_k7minus_four_centre_wheel_leaf_descent.md)
gives an edge `ab in E(H[T])`.  Proposition 4.1 reduces that branch to the
following precise question:

> Does `G[C union U union {a,b}]` contain a
> `(U union {a,b})`-rooted `K_6^-` minor, or does failure produce an ordinary
> three-separation of `H` with a nonempty proper open side contained in `C`?

The second outcome is excluded by trace minimality.  Internal
six-connectivity, the edge `ab`, and the rooted `K_4^-` alone do not prove
the first outcome; an explicit
[rooted-minor barrier](../barriers/hc7_k7minus_internal_six_rooted_k6minus_barrier.md)
records the obstruction.
Any theorem forcing either the prescribed rooted `K_6^-` minor or the
displayed trace-preserving descent must also use the critical-host data and,
in the generalized-wheel branch, the absence of two disjoint connected
subgraphs adjacent to every boundary vertex.

## Dependencies

- [Trace-preserving descent from a four-centre exact cut](hc7_k7minus_four_centre_trace_descent.md).
- [Four independent centres: rooted model or exact-cut lattice](hc7_k7minus_four_centre_web_cut_lattice.md).
- [Two-component normal form for order-seven cuts](hc7_k7minus_three_component_seven_cut_exclusion.md).
- [Closed-side rooted connectivity](hc7_closed_shore_rooted_connectivity.md).
- [Generalized-wheel leaf descent](hc7_k7minus_four_centre_wheel_leaf_descent.md).
- Jorgensen's rooted `K_4^-` theorem, as quoted in Norin and Totschnig,
  *Every graph with no `K_7^\vee`-minor is 6-colorable*, Lemma 10.
