# The conflict component of a coupled incident-edge bypass

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_incident_bypass_conflict_split_audit.md`](hc7_order8_incident_bypass_conflict_split_audit.md).
The theorem is
parameter-uniform.  In the order-eight application it retains one common
operation and colouring, but it does not identify palette colours with the
seven column labels and does not close the two-full-component branch.

## 1. Coupled bypass setting

Let `q>=3`, and let `G` satisfy

\[
 \chi(G)=q+1,
 \qquad \chi(M)\le q\text{ for every proper minor }M\text{ of }G.
 \tag{1.1}
\]

Let

\[
                         va,vb\in E(G),\qquad ab\notin E(G),
 \tag{1.2}
\]

put `H=G-{va,vb}`, and let `kappa` be a proper `q`-colouring of `H`
with

\[
                         \kappa(v)=\kappa(a)=\kappa(b)=0.
 \tag{1.3}
\]

Suppose distinct colours `i,j` and bichromatic components `A,B` satisfy

\[
\begin{array}{c|c|c}
 &\text{palette}&\text{named vertices}\\ \hline
A&\{0,i\}&a\in A,\quad v,b\notin A,\\
B&\{0,j\}&b\in B,\quad v,a\notin B.
\end{array}                                                \tag{1.4}
\]

This is exactly the bypass outcome of the audited incident-edge
saturation-or-bypass theorem.  That theorem additionally names the two
individual component switches; the result below keeps those literal
components fixed.

Put

\[
 R=A\cap B,
 \qquad X=A\cap\kappa^{-1}(i),
 \qquad Y=B\cap\kappa^{-1}(j),
 \qquad F=E_G(X,Y).                                      \tag{1.5}
\]

## 2. Intersection-safe simultaneous response

### Theorem 2.1 (exact conflict set)

The following statements hold.

1. `R subseteq kappa^{-1}(0)`.
2. There is a proper `q`-colouring `psi` of `G-F` obtained from `kappa`
   by

   - interchanging `0,i` on `A-B`;
   - interchanging `0,j` on `B-A`;
   - giving every vertex of `R` colour `i`; and
   - restoring the two edges `va,vb`.
3. The set `F` is nonempty, and its edges are exactly the monochromatic
   edges of `G` under `psi`.  Both ends of every edge of `F` have colour
   zero.
4. The graph with vertex classes `X,Y` and edge set `F` is bipartite.
   Its nontrivial connected components are induced subgraphs of `G`, and
   distinct such components are anticomplete in `G`.

#### Proof

The palettes of `A` and `B` meet only in colour zero, which proves item 1.
The exclusions in (1.4) also give

\[
                         R\cap\{v,a,b\}=\varnothing.          \tag{2.1}
\]

First ignore edges with one end in `A-B` and the other in `B-A`.  On each
of those two sets the proposed assignment is the pointwise restriction of
the corresponding named component switch.  A vertex of `R` had colour
zero.  Every one of its
colour-`i` neighbours belongs to the same `0,i` component `A`, and every
one of its colour-`j` neighbours belongs to the same `0,j` component `B`.
All these edges occur in `H`, by (2.1), so component maximality applies.
Those neighbours lie respectively in `A-B` and `B-A` and change to colour
zero.  Thus recolouring `R` to `i` creates no conflict.  Neighbours in any
other colour are unchanged and remain different from `i`.

It remains to inspect an edge between `A-B` and `B-A`.  The old colouring
was proper and the two palettes meet only in zero.  The only new equality
has an old colour-`i` end in `A` and an old colour-`j` end in `B`; both
ends change to zero.  These edges are exactly `F`.  The vertex `a` changes
from zero to `i`, the vertex `b` changes from zero to `j`, and `v` remains
zero, so both deleted incident edges can be restored.  This proves item 2
and the description in item 3.  If `F` were empty, the same assignment
would `q`-colour `G`, contrary to (1.1).  Hence `F` is nonempty.

Each of `X,Y` is independent in `G`.  Indeed, it was contained in one
colour class of the colouring `kappa` of `H`, and the two deleted edges
`va,vb` have only colour-zero ends, so neither is incident with `X` or `Y`.
Every edge between `X,Y` belongs to `F` by definition.  Consequently two
different connected components of the bipartite graph `(X,Y;F)` have no
edge between them in `G`, and every nontrivial component is induced on its
own vertex set.  This proves item 4. \(\square\)

The choice of colour `i` on `R` is asymmetric only in notation.  Giving
`R` colour `j` yields the symmetric construction.

## 3. The complete edge-response table on the conflict set

### Proposition 3.1 (all-one and unit signatures)

Regard a `q`-colouring of `G-F` as recording the subset of edges in `F`
whose ends receive the same colour.  Then:

1. `psi` realizes the signature `F`;
2. for every `f in F`, some `q`-colouring realizes the singleton signature
   `{f}`; and
3. the empty signature is impossible.

#### Proof

Theorem 2.1 gives item 1.  Fix `f in F`.  The proper minor `G-f` has a
`q`-colouring.  Every edge of `F-{f}` remains present and therefore has
differently coloured ends.  The ends of `f` must have the same colour,
since otherwise restoring `f` would `q`-colour `G`.  Restriction to `G-F`
therefore gives exactly the singleton signature `{f}`.  An empty signature
would restore every edge of `F` and again `q`-colour `G`. \(\square\)

Thus `F` is an inclusion-minimal set of edges whose restoration destroys
`q`-colourability of the common deletion.  The unit colourings need not
belong to one Kempe class or induce one boundary partition.

### Proposition 3.2 (every unit edge is a full Kempe lock)

Fix `f=xy in F` and any proper `q`-colouring `phi` of `G-f`.  Put

\[
                         \phi(x)=\phi(y)=\alpha.
\]

For every colour `beta` different from `alpha`, the vertices `x,y` belong
to the same connected component of

\[
                (G-f)[\phi^{-1}(\{\alpha,\beta\})].    \tag{3.1}
\]

#### Proof

The ends of `f` have one colour because otherwise `f` could be restored.
If they belonged to different components in (3.1), interchange
`alpha,beta` on the component containing `x`.  This keeps a proper
`q`-colouring of `G-f` and gives `x,y` different colours, so `f` could now
be restored.  The resulting `q`-colouring of `G` contradicts (1.1).
\(\square\)

For `q=6`, every unit response is therefore locked in all five alternate
colours.  These five locks belong to the unit colouring for that particular
edge; Proposition 3.2 does not identify the colourings for different edges
of `F`.

## 4. A same-colouring bilateral palette split

Let `U` be the set of ends of edges in `F`, and let

\[
                         Z_1,\ldots,Z_m                 \tag{4.1}
\]

be the nontrivial connected components of the graph `(X,Y;F)`.  By
Theorem 2.1 they are pairwise anticomplete connected induced bipartite
subgraphs of `G`.

### Theorem 4.1 (one conflict component has a bilateral full-palette cut)

For at least one `Z=Z_l`, and for every spanning tree `T` of `G[Z]`, some
edge of `T` splits `Z` into nonempty connected adjacent sets

\[
                          Z=Z^-\mathbin{\dot\cup}Z^+       \tag{4.2}
\]

such that, in the one fixed colouring `psi`,

\[
 \psi\bigl(N_G(Z^-)-U\bigr)
   =\psi\bigl(N_G(Z^+)-U\bigr)
   =Q-\{0\}.                                             \tag{4.3}
\]

Here `Q` is the `q`-colour palette.  In particular, for `q=6` both
connected sides see all five alternate colours outside the entire conflict
set.

#### Proof

The restriction of `psi` to `G-U` is proper.  For `z in Z_l`, define

\[
             L_l(z)=Q-\psi\bigl(N_G(z)-U\bigr).          \tag{4.4}
\]

Every list contains zero: under `psi`, the vertex `z` has colour zero and
every edge from `z` to `G-U` is proper.  Suppose every `G[Z_l]` had an
`L_l`-colouring.  The components are anticomplete, so those list-colourings
could be combined with `psi|_{G-U}` to give a proper `q`-colouring of
`G`, a contradiction.  Hence one component `Z` is not colourable from its
displayed lists.

Apply the audited poor-edge lemma for connected bipartite graphs to `Z`
and the arbitrarily selected spanning tree `T`.  It returns the two tree
sides in (4.2) with

\[
       \bigcap_{z\in Z^-}L_l(z)=\{0\}
        =\bigcap_{z\in Z^+}L_l(z).                      \tag{4.5}
\]

Taking palette complements in (4.4) gives (4.3).  The deleted tree edge
makes the two sides adjacent. \(\square\)

### Proposition 4.2 (the simultaneous contraction remains tight)

Contract every `Z_l` to one vertex.  The resulting proper minor `M` has

\[
                              \chi(M)=q.                 \tag{4.6}
\]

The colouring `psi` descends to a proper `q`-colouring of `M`.

#### Proof

All vertices of every `Z_l` have colour zero under `psi`; the only
monochromatic edges of `G` are internal to those components.  Hence `psi`
descends to `M`, giving `chi(M)<=q`.

If `M` had a `(q-1)`-colouring, fix a bipartition of each `Z_l`.  On one
class reuse the colour of its contraction image, and on the other use one
common fresh `q`th colour.  Outside neighbours avoid the contraction
colour, the fresh colour occurs nowhere outside `U`, and different
components are anticomplete.  This would `q`-colour `G`, contrary to
(1.1).  Thus `chi(M)>=q`, proving (4.6). \(\square\)

Contracting only one conflict component does not preserve `psi` while
uncontracted conflict edges remain.  Proposition 4.2 deliberately
contracts all of them at once.

## 5. Order-eight application and exact trust boundary

There is one further consequence when the host is displayed as two closed
shores.  Suppose

\[
 V(G)=C\mathbin{\dot\cup}S\mathbin{\dot\cup}D,
 \qquad E(C,D)=\varnothing,                              \tag{5.1}
\]

and put `G_C=G[C union S]`, `G_D=G[D union S]`.  For an edge `f in F`
with an end in `C`, every unit colouring of `G-f` induces a boundary
equality partition which extends through the intact `D`-shore and is
rejected by the intact `C`-shore.  Indeed, an extension through intact
`G_C` could be relabelled to agree with the unit colouring of `G_D` and
would then `q`-colour `G`.  The symmetric statement holds for an edge of
`F` with an end in `D`.

Consequently, if a `C`-edge and a `D`-edge of `F` have unit colourings with
the same boundary equality partition, that partition extends through both
intact closed shores and is terminal by gluing.  The theorem does not force
`F` to contain edges on both open shores, nor does it force independently
chosen unit colourings to have the same boundary partition.

Apply the theorem to the bypass outcome of the audited
[unified noncontacting incident-pair response](hc7_order8_unified_incident_pair_normal_form.md).
It preserves:

- the same two incident edges selected from one order-eight response star;
- their same simultaneous-contraction colouring;
- the two named bichromatic components and their individual switches;
- the exact all-one/unit response table on `F`;
- the five-colour Kempe lock in every individual unit response; and
- one connected conflict component with the same-colouring bilateral
  five-colour split in Theorem 4.1.

This removes the former ambiguity when the two named bichromatic components
intersect: intersection and an explicit joining edge now have one common
normal form.

It does **not** prove that the five palette colours in (4.3) belong to five
distinct latent columns or five pairwise adjacent branch sets.  The
palette-to-label issue is essential: the existing bilateral palette
theorem and paired-colourful-set barriers show that full palette exposure
alone does not manufacture the required labelled `K_5` model.  Nor does
the theorem produce a common boundary partition, an order-seven response
interface, a strict order-eight response-side descent, or a nested
order-eight full interface.

The remaining unresolved obligation in this bypass branch is therefore:

> align the two connected sides in (4.2), together with the unit responses
> on `F`, with five latent column labels; or use failure of that alignment
> to produce an explicit `K_7`-minor model, a common boundary partition, or
> a strict bounded-interface restart.

## 6. Dependencies

- [unified noncontacting incident-pair response](hc7_order8_unified_incident_pair_normal_form.md);
- [incident-edge saturation or bypass](hc7_shared_interface_bichromatic_bypass.md); and
- [poor-edge lemma for connected bipartite graphs](hc7_near_k7_bipartite_total_contraction.md).
