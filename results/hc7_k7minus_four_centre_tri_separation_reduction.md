# Canonical tri-separation form of the rooted-web order-seven cut

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_four_centre_tri_separation_reduction_audit.md`](hc7_k7minus_four_centre_tri_separation_reduction_audit.md).

This note applies the tri-separation theory of Carmesin and Kurkofka to the
exact cut supplied by the audited
[four-vertex rooted-web theorem](hc7_k7minus_four_centre_web_cut_lattice.md).
It proves an unlabelled nested-or-wheel reduction.  It does not preserve the
colouring and rooted-minor data needed to eliminate the web outcome.

## 1. Setting

Let `G` be a graph satisfying

\[
 \chi(G)=7,\qquad
 \chi(M)\leq 6\text{ for every proper minor }M\text{ of }G,
 \qquad K_7^-\npreccurlyeq G,
\]

and suppose that `G` is seven-connected and has minimum degree at least
eight.  Let `U` be an independent set of four degree-eight vertices and put
`H=G-U`.  Then `H` is three-connected.

Assume that the rooted-web outcome gives a three-set `T subseteq V(H)` such
that

\[
                         H-T=C\mathbin{\dot\cup}D,       \tag{1.1}
\]

where `C,D` are the two connected components, and every vertex of
`U dotcup T` has a neighbour in each of `C,D`.  Put

\[
                         A=C\cup T,\qquad B=D\cup T.     \tag{1.2}
\]

Thus `(A,B)` is a proper ordinary three-separation of `H`.

For a mixed separation `(X,Y)`, its separator is

\[
 (X\cap Y)\mathbin{\dot\cup}E_H(X-Y,Y-X).
\]

A tri-separation is a mixed separation of order three in which every vertex
of `X cap Y` has at least two neighbours in each closed side.  It is
nontrivial when both closed sides contain a cycle, strong when every vertex
in its mixed separator has degree at least four, and half-connected when at
least one open side is connected.

## 2. The reduced tri-separation

### Theorem 2.1 (strong two-sided-connected reduction)

The separation `(A,B)` is nontrivial.  Its Carmesin--Kurkofka reduction is
uniquely determined, is a strong nontrivial tri-separation `(A',B')`, and
has both open sides `H[A'-B']` and `H[B'-A']` connected.

More explicitly, define

\[
\begin{aligned}
 T_C&=\{t\in T:d_{H[C\cup T]}(t)=1\},\\
 T_D&=\{t\in T:d_{H[D\cup T]}(t)=1\},\\
 T_0&=T-(T_C\cup T_D).
\end{aligned}                                           \tag{2.1}
\]

For `t in T_C`, let `c_t` be its unique neighbour in `C`; for
`t in T_D`, let `d_t` be its unique neighbour in `D`.  Then

\[
 A'=C\cup T_0\cup T_D,\qquad
 B'=D\cup T_0\cup T_C,                                  \tag{2.2}
\]

and the mixed separator is

\[
 T_0\mathbin{\dot\cup}
 \{tc_t:t\in T_C\}\mathbin{\dot\cup}
 \{td_t:t\in T_D\}.                                    \tag{2.3}
\]

#### Proof

Fix `X in {C,D}`.  The other component in (1.1) is anticomplete to `X`, so
every neighbour of a vertex `v in X` outside `H[X union T]` belongs to `U`.
Consequently

\[
                     d_{H[X\cup T]}(v)\geq d_G(v)-4\geq4. \tag{2.4}
\]

Suppose that `H[X union T]` were a forest.  Since `|T|=3`,

\[
 4|X|
 \leq\sum_{v\in X}d_{H[X\cup T]}(v)
 \leq2|E(H[X\cup T])|
 \leq2(|X|+2),                                         \tag{2.5}
\]

and hence `|X|<=2`.  If `|X|=1`, (2.4) is impossible because the sole
vertex has only the three vertices of `T` available in its closed side.  If
`|X|=2`, connectedness supplies the edge inside `X`, and (2.4) makes both
vertices adjacent to all of `T`.  Either vertex of `T` then completes a
triangle, again contradicting acyclicity.  Thus both `H[A]` and `H[B]`
contain cycles, so `(A,B)` is nontrivial.

Carmesin--Kurkofka reduction replaces a boundary vertex deficient on one
closed side by its unique edge into that side.  Three-connectivity makes
the deficient side and the replacement edge unique.  Their Lemma 1.3.4 and
Definition 1.3.5 give exactly (2.1)--(2.3), including preservation of
nontriviality.

If `t in T_D`, then the same reduction lemma gives at least two neighbours
of `t` in `C`; hence adjoining `t` to connected `C` preserves
connectedness.  The symmetric statement holds for `t in T_C` and `D`.
Equation (2.2) therefore has two connected open sides.  Finally,
`delta(H)>=4`, because deleting `U` removes at most four incident edges
from any vertex of `H`.  Every vertex element of (2.3) consequently has
degree at least four, so the tri-separation is strong.  \(\square\)

Every member of `U` still has a neighbour in each reduced open side,
because the original components `C,D` remain subsets of those sides.
Consequently

\[
                       (A'\cup U,B'\cup U)             \tag{2.6}
\]

is a mixed separation of `G` of order seven: its mixed separator is the
disjoint union of `U` and (2.3).  It is not generally an ordinary vertex
separation.

## 3. Canonical adhesion or a generalized-wheel torso

Let `N(H)` be the canonical nested set of all totally nested nontrivial
tri-separations of `H`, and let `rho(A,B)` denote the reduction in
Theorem 2.1.

### Corollary 3.1 (nested-or-wheel normalization)

Exactly one of the following holds.

1. `rho(A,B)` belongs to `N(H)` and is induced by an edge of the canonical
   mixed-tree-decomposition of `H`; its mixed separator is the corresponding
   adhesion.
2. `rho(A,B)` interlaces a unique splitting star of `N(H)`.  The compressed
   torso of that splitting star is a wheel, and its expanded torso is a
   generalized wheel.

#### Proof

Put `q=rho(A,B)`.  If `q` is totally nested, the first conclusion holds by
definition.  Otherwise `q` remains nested with every member of `N(H)`,
since those members are nested with every tri-separation.  The set `N(H)`
is symmetric under reversing orientations.  Let

\[
       \mathcal M=\{s\in N(H):s<q\text{ or }s<q^*\},   \tag{3.1}
\]

where `q^*` is the inverse orientation.  One orientation of every
separation in `N(H)` lies in `mathcal M`.  Let `sigma` be the set of maximal
members of `mathcal M`; take the empty star when `N(H)` is empty.
For two distinct maximal members, nestedness and maximality leave only the
opposite-facing relation required of a star.  Since `H` is finite, every
member of `mathcal M` lies below a maximal one.  Thus every separation in
`N(H)`, in one of its orientations, lies below a member of `sigma`; this is
the splitting property.  Definition (3.1) says that `q` interlaces
`sigma`.  Carmesin and Kurkofka's Lemma 2.2.5 shows that no second splitting
star is interlaced.

By Theorem 2.1, `rho(A,B)` is strong, nontrivial and half-connected.  It
therefore interlaces the splitting star heavily.  Carmesin and Kurkofka's
torso theorem gives a wheel as the compressed torso and a generalized wheel
as the expanded torso.  Finally, Lemma 2.2.3 says that a member of `N(H)`
cannot interlace a splitting star of `N(H)`, so the alternatives are
exclusive.  \(\square\)

### Corollary 3.2 (two crossing reductions)

If two exact cuts in the same graph `H` have crossing reductions, their
crossing has a one-vertex centre and four links, each consisting of one
separator element.  There are no jumping or diagonal edges.

#### Proof

The graph `H` is six-chromatic: it is six-colourable as a proper minor of
`G`, while a five-colouring would extend to `G` by giving the independent
set `U` a sixth colour.  Thus `H` is not `K_4`.  Both reductions are
nontrivial and half-connected.  Carmesin and Kurkofka's Crossing Lemma
gives the one-vertex centre, the four size-one links and the absence of
jumping edges; its proof also excludes diagonal edges.  \(\square\)

A size-one link may be an edge.  Thus this corollary identifies the exact
mixed-separation geometry of the former crossing configuration; it does not
turn that configuration into an ordinary vertex separation.

## 4. What must be retained

The reduction has a natural bijection from its mixed separator to the
original boundary `T`:

\[
 t\longmapsto t\quad(t\in T_0),\qquad
 tc_t\longmapsto t\quad(t\in T_C),\qquad
 td_t\longmapsto t\quad(t\in T_D).                    \tag{4.1}
\]

Together with the oriented reduced pair, this map recovers the original
three-separation: add each labelled endpoint of a replacement edge back to
the opposite side.  It is sufficient to retain the literal boundary
vertices.  The undecorated mixed separation does not in general determine
which endpoint of a replacement edge was in `T`; the
[boundary-trace counterexample](../barriers/hc7_k7minus_tri_separation_boundary_trace_loss.md)
shows that two distinct ordinary three-separations can have the same
reduction.

The present theorem deliberately makes no colouring-preservation claim.
The one-sided colouring trace belongs to the original closed graph on
`C union T union U`, while reduction may move a vertex of `T` into the
opposite open side.  Likewise, the forced Kempe component lives in `G-r`
and may contain another member of `U`, whereas the canonical decomposition
is taken in `H=G-U`.  Compressed torsos also contract separator edges.

A concise labelled interface for the next step is:

- the oriented reduction `q` and the inverse boundary map
  `theta:S(q) to T` from (4.1), identifying the original endpoint of every
  separator-edge element;
- the literal set `U`, the selected vertex `r`, the fixed colouring `phi`
  and the ordered rooted terminals `x_1,...,x_4`;
- the orientation selecting the `C`-side on which the colouring extends,
  a terminal `x_j in D-T` and `gamma=phi(x_j)`; and
- one crossing pair `\{i,k\}` together with the named vertex
  `s in U-\{r\}` lying in its `phi`-bichromatic component.

The colouring and crossing pair determine that component, so a separate
component object is unnecessary.  With this data fixed, the remaining work
has two branches.

1. At a canonical adhesion, either use the original unreduction to obtain a
   rooted augmentation or a common boundary colouring, or select a different
   canonical adhesion strictly inside the selected side and expand it to an
   ordinary three-separation while retaining `U,r,phi,(x_1,...,x_4)`, the
   selected-side trace `(j,gamma)` and the named Kempe datum
   `(\{i,k\},s)`.  The new reduction \(\widetilde q\) must carry its own
   inverse boundary map
   \(\widetilde\theta:S(\widetilde q)\to\widetilde T\).
2. In a generalized-wheel torso, lift through the expanded torso while
   retaining the same data.  The wheel apex lies in `H` and has no proved
   relation to the named vertex `s in U`.

In either branch the required output is a label-preserving rooted
augmentation, a common boundary colouring, or a strictly smaller ordinary
three-separation whose lift to `G` has boundary
\(U\mathbin{\dot\cup}\widetilde T\), retains the one-sided colouring trace and carries
its own inverse boundary map.

Without these statements, the nested-or-wheel normalization is structural
compression rather than a minor-model or colouring closure.

## External source and internal dependency

- Johannes Carmesin and Jan Kurkofka, *Canonical Decompositions of
  3-Connected Graphs*, Advances in Combinatorics 2025:7,
  <https://doi.org/10.19086/aic.2025.7>.  The inputs used here are
  Definition 1.1.1, the mixed-tree-decomposition correspondence in
  Section 1.2, Lemma 1.3.4 and Definition 1.3.5, Lemmas 1.4.8 and
  1.4.11 (the Crossing Lemma), Lemmas 2.2.3 and 2.2.5, and
  Theorem 2.2.8(ii).
- [Four independent degree-eight vertices: rooted model or exact-cut
  lattice](hc7_k7minus_four_centre_web_cut_lattice.md).
- [Boundary labels are not recoverable from an undecorated reduction](../barriers/hc7_k7minus_tri_separation_boundary_trace_loss.md).
