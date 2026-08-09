# Trace-preserving descent from a four-centre exact cut

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_four_centre_trace_descent_audit.md`](hc7_k7minus_four_centre_trace_descent_audit.md).

This note preserves the fixed colouring and named vertices in the exact-cut
outcome of the four-centre rooted-web theorem.  It gives two strict descent
steps and identifies the remaining canonical-adhesion case.  It does not
eliminate that case or prove the `K_7^-` six-colour conjecture.

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

Fix `r in U`, a proper six-colouring `phi` of `G-r`, and four neighbours
`x_1,...,x_4` of `r` whose colours are distinct and occur uniquely on
`N_G(r)`.  Suppose the rooted-web theorem returns a three-set `T` and
connected sets `C,D` such that

\[
 H-T=C\mathbin{\dot\cup}D,
 \qquad N_G(C)=N_G(D)=U\mathbin{\dot\cup}T.             \tag{1.1}
\]

Every `x_i` avoids `C`.  Fix `x_j in D` and put
`gamma=phi(x_j)`.  Assigning colour `gamma` to `r` extends `phi` to a
proper six-colouring of `G[C union U union T]`.

The global data `U,r,phi,(x_1,...,x_4)` will remain fixed.  Consequently,
any assertion about a named member of `U-{r}` in a specified bichromatic
component of `G-r` also remains fixed.

## 2. Replacing a deficient boundary vertex

### Theorem 2.1 (one-vertex boundary descent)

Suppose that some `t in T` has a unique neighbour `c` in `C`.  Define

\[
 T'=(T-\{t\})\cup\{c\},\qquad
 C'=C-\{c\},\qquad
 D'=D\cup\{t\}.                                      \tag{2.1}
\]

Then `U dotcup T'` is an exact order-seven cut and

\[
                         H-T'=C'\mathbin{\dot\cup}D', \tag{2.2}
\]

where `C',D'` are connected and adjacent to every vertex of
`U dotcup T'`.  Moreover,

\[
 |C'|=|C|-1,\qquad x_i\notin C'\ (1\leq i\leq4),
 \qquad x_j\in D',                                   \tag{2.3}
\]

and the fixed colouring extends to the new closed `C'`-side by assigning
colour `gamma` to `r`.

#### Proof

The set `C` has at least two vertices.  Indeed, if `C=\{c\}`, then every
neighbour of `c` belongs to the seven-set `U dotcup T`, contrary to
`delta(G)>=8`.

The set `D'` is connected because `D` is connected and `t` has a neighbour
in `D`.  There is no edge from `C'` to `D'`: the original components are
anticomplete, and the only neighbour of `t` in `C` is the deleted vertex
`c`.  Thus `U dotcup T'` is a seven-vertex cut with `C'` and `D'` on
opposite sides.  The audited two-component theorem for seven-vertex cuts
in `G` now makes `C'` connected and shows that (2.2) lists exactly the two
components.  Seven-connectivity makes each component adjacent to every
vertex of the new boundary.

Finally,

\[
 C'\cup U\cup T'=C\cup U\cup(T-\{t\}).                \tag{2.4}
\]

The new colouring is therefore a restriction of the old one.
The vertex `x_j`, the unique neighbour of `r` with colour `gamma`, remains
in the opposite open side, so assigning `gamma` to `r` is proper.  The
remaining assertions in (2.3) are immediate.  \(\square\)

Call an exact cut with boundary `U dotcup T` **trace-admissible** if it has
an orientation `(C,D)` satisfying the fixed conditions in Section 1,
including `x_j in D` and the extension of `phi` to the closed `C`-side.

### Corollary 2.2 (minimum coloured side)

Choose a trace-admissible cut with `|C|` minimum.  Then

\[
                         |N_H(t)\cap C|\geq2
                         \qquad(t\in T).               \tag{2.5}
\]

In the Carmesin and Kurkofka reduction of
`(C union T,D union T)`, no member of `T` is deleted from the selected
side.  That side of the reduced tri-separation is therefore literally
`C union T`.

#### Proof

Fullness gives at least one neighbour in `C` for every `t in T`.  Equality
would contradict minimality by Theorem 2.1.  In the reduction, a boundary
vertex is deleted from the `C`-side exactly when it has a unique neighbour
there, so (2.5) gives the final assertion.  \(\square\)

## 3. A separation that splits the selected component

Let

\[
                         p_0=(C\cup T,D\cup T)          \tag{3.1}
\]

be a minimum trace-admissible separation as in Corollary 2.2.

### Theorem 3.1 (anchored meet descent)

Let `a=(P,Q)` be a nontrivial tri-separation of `H`.  Write `rho(p_0)` for
the reduction of `p_0`, orient `a` so that

\[
                              a\leq\rho(p_0),           \tag{3.2}
\]

and suppose that `a` splits `C`:

\[
 C\cap(P-Q)\ne\varnothing\ne C\cap(Q-P).              \tag{3.3}
\]

Then there is a trace-admissible exact cut whose selected component is a
nonempty proper subset of `C`.  Its ordinary three-separation has its own
Carmesin and Kurkofka reduction and inverse boundary map.

#### Proof

Choose

\[
 c_0\in C\cap(P-Q),\qquad z\in C\cap(Q-P).             \tag{3.4}
\]

Corollary 2.2 says that the selected side of the reduction of `p_0` is
`C union T`.  Since `a` lies below that oriented reduction, `D` lies in
`Q-P`; in particular, `x_j in Q-P`.  Also `c_0x_j` is not an edge because
`C,D` are anticomplete.

The edge elements of the mixed separator of `a` form a matching.  Convert
`a` to an ordinary three-separation `bar a=(bar P,bar Q)` by choosing one
endpoint of each separator edge as a boundary vertex.  For an edge incident
with `c_0` or `x_j`, choose its other endpoint.  These instructions do not
conflict because `c_0x_j` is not an edge.  Choose either endpoint on every
remaining separator edge.  The two named vertices remain in opposite open
sides:

\[
 c_0\in\bar P-\bar Q,\qquad x_j\in\bar Q-\bar P.       \tag{3.5}
\]

Both `p_0` and `bar a` are proper ordinary three-separations of `H`.
The cut in (1.1) shows that `kappa(G)=7`.
Every member of `U` crosses each of them, and both have lifted order seven.
Apply the fixed-anchor exact uncrossing theorem to the common opposite
anchors `c_0,x_j`.  Their meet

\[
                         \widetilde p=p_0\wedge\bar a \tag{3.6}
\]

is proper, has lifted order seven and is crossed by every member of `U`.
Its ordinary separator `widetilde T` consequently has order three, and
`U dotcup widetilde T` is an exact order-seven cut.

The selected open side of (3.6) is

\[
                 \widetilde C=C\cap(\bar P-\bar Q).    \tag{3.7}
\]

It contains `c_0`.  The vertex `z` is either in the opposite open side of
`bar a` or in its boundary, so it is not in `widetilde C`.  Hence

\[
                         \varnothing\ne\widetilde C
                         \subsetneq C.                 \tag{3.8}
\]

The two-component theorem makes `widetilde C` connected, and the opposite
component contains `x_j`.  Seven-connectivity makes both components
adjacent to every vertex of `U dotcup widetilde T`.  The selected closed
side of (3.6) is contained in `C union T`.  The old colouring therefore
restricts to it, and assigning colour `gamma` to `r` remains proper.  Since
`widetilde C subsetneq C`, all four `x_i` avoid the new selected component.
The fixed vertices and named bichromatic component are unchanged.

Reducing `widetilde p` supplies its own inverse boundary map from the new
mixed separator to `widetilde T`.  This proves the claimed descent.
\(\square\)

### Corollary 3.2 (canonical-adhesion residue)

If the reduction of a minimum trace-admissible cut is totally nested, no
nontrivial tri-separation of `H` splits `C`.

#### Proof

Every nontrivial tri-separation is nested with the totally nested
reduction.  Its opposite side contains no vertex of `C`, by Corollary 2.2.
If a tri-separation split `C`, nestedness would therefore orient it below
the selected side.  Theorem 3.1 would contradict the minimum choice of
`C`.  \(\square\)

Thus the unresolved canonical case is exact: every boundary vertex has at
least two neighbours in `C`, the reduced canonical adhesion retains
`C union T` literally, and no nontrivial tri-separation of `H` splits `C`.
Canonical decomposition alone does not provide a common boundary colouring
or an explicit `K_7^-`-minor model extending the rooted branch sets in this
remaining case.

## Dependencies

- [Four independent centres: rooted model or exact-cut lattice](hc7_k7minus_four_centre_web_cut_lattice.md), especially Theorems 3.1--3.2 and Corollary 3.3.
- [Canonical tri-separation form of the rooted-web cut](hc7_k7minus_four_centre_tri_separation_reduction.md).
- Johannes Carmesin and Jan Kurkofka, *Canonical Decompositions of
  3-Connected Graphs*, Advances in Combinatorics 2025:7,
  <https://doi.org/10.19086/aic.2025.7>, especially Lemma 1.3.3 and the
  reduction in Definition 1.3.5.
