# Rotation visibility in the dense five-centre branch

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_dense_branch_rotation_visibility_audit.md`](hc7_k7minus_dense_branch_rotation_visibility_audit.md).
The results are
unbounded and computation-free.  They do not prove the `K_7^-` six-colour
conjecture or `HC_7`.

Throughout, let `G` be a finite simple graph such that

\[
 \chi(G)=7,\qquad
 \chi(J)\leq 6\text{ for every proper minor }J\text{ of }G,
 \qquad \kappa(G)\geq 7,                              \tag{1.1}
\]

and let

\[
                         Z=\{z_1,\ldots,z_5\}          \tag{1.2}
\]

be an independent set of degree-eight vertices satisfying

\[
                         \alpha(G[N_G(z)])=3
                         \qquad(z\in Z).               \tag{1.3}
\]

Put `F=G-Z`.  These are the hypotheses supplied in the critical host by the
[exceptional-neighbourhood theorem](hc7_k7minus_exceptional_neighbourhood_completion.md)
and the
[common five-edge response theorem](hc7_k7minus_five_centre_common_matching_reduction.md).

## 1. Boundary traces

Let `Y` be a nonempty proper vertex set and put `T=N_G(Y)`.  A proper
six-colouring of `G-Y` induces an equality partition of `T`: two boundary
vertices lie in the same block precisely when they have the same colour.
Call this partition a **rejected exterior trace on `Y`** if no proper
six-colouring of `G[Y\cup T]` induces the same partition on `T`.

This definition ignores colour names.  If the same partition were realised
on both sides, a permutation of the six colours would make the boundary
colourings agree, and the two colourings would glue to a six-colouring of
`G`.  Thus every proper six-colouring of `G-Y` induces a rejected exterior
trace.

For `z\in Z`, define

\[
 \mathcal I_z=\{I\subseteq N_G(z): |I|=3\text{ and }I\text{ is independent}\},
 \qquad
 K_z=\bigcap_{I\in\mathcal I_z} I.                   \tag{1.4}
\]

The family `\mathcal I_z` is nonempty by (1.3), and `|K_z|\leq3`.

### Lemma 1.1 (single-edge star visibility)

Fix `z\in Z`.

1. If `y\in N_G(z)-K_z`, then there is a proper six-colouring of `G-zy`
   whose only monochromatic edge after `zy` is restored is `zy` itself.
   Consequently every vertex set `Y` with `y\in Y` and `z\notin Y` carries
   a rejected exterior trace obtained from this colouring.
2. Every vertex set `Y` containing `z` carries a rejected exterior trace
   obtained from a proper six-colouring of `G-z`.
3. If `Y` carries no rejected exterior trace obtained from a centre deletion
   or a centre-star contraction, then

   \[
        Y\cap Z=\varnothing,\qquad
        Y\cap N_G(z)\subseteq K_z,qquad
        |Y\cap N_G(z)|\leq2\quad(z\in Z).             \tag{1.5}
   \]

#### Proof

Let `y\in N_G(z)-K_z`.  By the definition of `K_z`, choose
`I\in\mathcal I_z` with `y\notin I`.  Contract the connected star
`G[\{z\}\cup I]` and six-colour the resulting proper minor.  On expanding
the contracted vertex, this gives a proper six-colouring `phi` of `G-z` in
which the three vertices of `I` have one common colour.

Put `R=N_G(z)-I`.  Every vertex of `R` avoids the colour on `I`.  Moreover,
the five vertices of `R` have pairwise distinct colours.  Otherwise at most
five colours occur on `N_G(z)`, and a missing sixth colour could be assigned
to `z`, contrary to `chi(G)=7`.

Since `y\in R`, assign to `z` the colour `phi(y)`.  The edge `zy` is then
monochromatic.  Every other edge at `z` is proper: the colour of `y` occurs
on no other vertex of `R` and differs from the common colour on `I`.
All other edges were already proper under `phi`.  This proves the first
assertion.  If `y\in Y` and `z\notin Y`, deleting `Y` removes the unique
monochromatic edge, so the restricted colouring is proper on `G-Y` and
induces a rejected exterior trace.

If `z\in Y`, restrict any proper six-colouring of the proper minor `G-z` to
`G-Y`.  This proves the second assertion.

Now suppose that none of the stated direct traces is present.  The second
assertion gives `Y\cap Z=\varnothing`, and the first gives
`Y\cap N_G(z)\subseteq K_z`.  This already proves the final bound when
`|K_z|\leq2`.  If `|K_z|=3`, then `K_z` is the unique member of
`\mathcal I_z`.  Contract its star and expand a six-colouring as above.
If `K_z\subseteq Y`, delete `Y` and assign to `z` the common colour on
`K_z`.  Every remaining neighbour of `z` lies in
`N_G(z)-K_z` and avoids that colour, so this is a proper six-colouring of
`G-Y` and hence supplies a rejected exterior trace.  Therefore
`|Y\cap N_G(z)|\leq2` also in this case. `\square`

Define the **five-centre response-support set**

\[
                 W=Z\cup\bigcup_{z\in Z}(N_G(z)-K_z). \tag{1.6}
\]

Lemma 1.1 says that every set meeting `W` carries a direct star trace.  It
also explains why the exceptional vertices outside `W` are genuinely
different: they lie in the intersection of all independent triples at a
centre.

## 2. Capture inside a spanning `K_7^\vee` model

Suppose that the vertex sets

\[
                         P,B,C,U_1,U_2,U_3,U_4         \tag{2.1}
\]

are pairwise disjoint, connected and partition `V(G)`, and that

1. `B,C,U_1,U_2,U_3,U_4` form a `K_6`-minor model;
2. `P` is anticomplete to `B,C`; and
3. `P` is adjacent to every `U_i`.

This is the exact spanning model supplied in the four-connected outcome of
the common five-edge response theorem when `G` is `K_7^-`-minor-free.

### Theorem 2.1 (two-support capture)

If, for some `i`, the universal branch set `U_i` contains two distinct
vertices

\[
                       p,q\in N_G(P)\cap U_i\cap W,    \tag{2.2}
\]

then one of the following holds.

1. `G` contains a `K_7^-` minor.
2. There is a nonempty proper connected set `Y\subset U_i` such that
   `U_i-Y` is connected, `N_G(Y)` is an actual separator of order at least
   seven, `Y` contains at least one of `p,q`, and `Y` carries a rejected
   exterior trace supplied by Lemma 1.1.

If `|N_G(Y)|=7`, every component of `G-N_G(Y)` is adjacent to every vertex
of `N_G(Y)`.

#### Proof

Rerun the proof of the audited
[exact `K_7^\vee` separator dichotomy](hc7_k7minus_exact_k7vee_separator_dichotomy.md)
with `p,q` as its two selected neighbours of `P` in `U_i`.

In the retaining-core case, the returned component contains the selected
vertex avoided by the retaining core, namely `q` (or `p` after interchanging
their roles).  If that component meets one of `B,C`, the branch-set transfer
in the cited proof gives a `K_7^-` minor.  Otherwise its open neighbourhood
is an actual separator.

In the remaining case, the cited proof constructs two disjoint unavoidable
sets, one containing `p` and the other containing `q`.  If either misses one
of `B,C`, that set has an actual open-neighbourhood separator.  If neither
does, the monopoly-set count in the cited proof gives a `K_7^-` minor.

Thus every separator returned by this rerun contains `p` or `q`.  Each lies
in `W`.  If the contained vertex is a centre `z\in Z`, Lemma 1.1(2)
supplies the trace.  Otherwise it belongs to `N_G(z)-K_z` for some centre
`z`.  Lemma 1.1(1) supplies the trace when `z\notin Y`, while Lemma 1.1(2)
does so when `z\in Y`.  Seven-connectivity gives the boundary lower bound,
and the final assertion is the order-seven fullness conclusion of the cited
dichotomy. `\square`

### Corollary 2.2 (the exact unsupported residue)

Under the hypotheses of Theorem 2.1, at least one of the following holds.

1. `G` contains a `K_7^-` minor.
2. The model supplies a separator carrying a direct star trace.
3. Every universal branch set satisfies

   \[
                       |N_G(P)\cap U_i\cap W|\leq1.   \tag{2.3}
   \]

   Consequently

   \[
                       |N_G(P)\cap W|\leq4,
                       \qquad |N_G(P)-W|\geq3.        \tag{2.4}
   \]

#### Proof

If (2.3) fails, Theorem 2.1 gives the first or second outcome.  Otherwise
the first inequality in (2.4) follows by summing over the four universal
branch sets.  The connected set `B` lies outside `P\cup N_G(P)`, so
`N_G(P)` is an actual separator.  Seven-connectivity gives
`|N_G(P)|\geq7`, and the second inequality follows. `\square`

## 3. Exact order seven returns to `F=G-Z`

The next statement records what an exact order-seven outcome means in the
five-centre geometry.  Here the `K_7^-`-minor exclusion is needed through
the audited three-component cut theorem.

For a separation of `F` with boundary `S` and open shores `A,D`, say that a
centre `z\in Z` **crosses** the separation if it has a neighbour in each of
`A,D`.

### Theorem 3.1 (labelled order-seven fallback)

Assume in addition that `K_7^-` is not a minor of `G`.  Let `Y` be a
nonempty connected set whose open neighbourhood is an actual separator and
such that

\[
                  T=N_G(Y),\qquad |T|=7,qquad Y\cap Z=\varnothing.       \tag{3.1}
\]

Then `G-T` has exactly two components, namely `Y` and a component `D`, and
both are full at `T`.  Put

\[
                     S=T-Z,qquad k=|T\cap Z|.          \tag{3.2}
\]

Then `S` is the boundary of a proper separation of `F` with open shores
`Y` and `D-Z`, its order is `7-k`, and its crossing-centre set is exactly
`T\cap Z`.  In particular, the minimum lift of this separation which keeps
these two open shores separated in `G` has order

\[
                         |S|+|T\cap Z|=7.              \tag{3.3}
\]

Consequently:

1. if `k=5`, then `T=Z\mathbin{\dot\cup}S` and `S` is a two-cut of `F`;
2. if `k=4`, then `S` is an order-three separation of `F`, crossed by
   precisely four labelled centres, with the fifth centre omitted; and
3. if `kappa(F)\geq3`, then `k\leq4`.

#### Proof

Since `N_G(Y)=T` and `Y` is connected, `Y` is a component of `G-T`.
The audited
[three-component seven-cut exclusion](hc7_k7minus_three_component_seven_cut_exclusion.md)
says that `G-T` has exactly two components.  Write the other one as `D`.
Seven-connectivity makes both components full at `T`.

The set `D-Z` is nonempty.  Otherwise `D\subseteq Z`; since `D` is connected
and `Z` is independent, `D=\{z\}` for some `z\in Z`.  All neighbours of
`z` would then lie in the seven-vertex set `T`, contradicting `d_G(z)=8`.

Deleting `Z` from the two full sides therefore leaves the proper separation
of `F` with boundary `S`, open shores `Y` and `D-Z`, and order `7-k`.
Every `z\in T\cap Z` has a neighbour in `Y` and a neighbour in `D` by
fullness.  The latter neighbour lies in `D-Z`, because `Z` is independent.
Hence every such centre crosses the separation.  Conversely, a centre in
`Z-T` lies in `D` and has no neighbour in the distinct component `Y` of
`G-T`; it does not cross.  The crossing-centre set is therefore exactly
`T\cap Z`.

Every crossing centre must be included in any lifted separator which keeps
the two displayed open shores apart, while the noncrossing centres can be
placed on a shore.  The separator `T` itself realises the lift, proving
(3.3).

Finally, deleting five vertices from a seven-connected graph leaves `F`
at least two-connected.  If `k=5`, the proper separator `S` has order two
and is therefore a two-cut.  The `k=4` statement is immediate, and
`kappa(F)\geq3` excludes `|S|\leq2`, giving `k\leq4`. `\square`

## 4. Scope and remaining obstruction

Theorem 2.1 makes the exact near-clique dichotomy sensitive to the five
centre responses: two response-support neighbours of `P` in one universal
branch set force either the forbidden minor or a response-bearing
separator.  Theorem 3.1 turns an exact order-seven response-free outcome
into a labelled low-order separation of `F`.

The argument does **not** prove that `N_G(P)` contains five vertices of
`W`, or that two of its response-support vertices lie in one `U_i`.
Corollary 2.2 leaves the precise residue `|N_G(P)-W|\geq3`.  Rechoosing the
five matching representatives may change the common host and its spanning
near-clique model, so it cannot be used here to prescribe those neighbours.

Nor does one rejected exterior trace provide a matching interior boundary
partition, a compatible second operation, or the branch-set contacts needed
for a `K_7^-` model.  The present note therefore supplies a rigorous
visibility and fallback theorem, not a terminal colouring or minor theorem.
