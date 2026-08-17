# Large exact forests retain an original coordinate after boundary descent

**Status:** written proof; awaiting separate internal audit.  This is a
conditional reduction inside a hypothetical critical host.  It does not
prove the `K_7^-` six-colour conjecture or `HC_7`.

## 1. Setting

Let `G` satisfy

\[
 \chi(G)=7,\qquad
 \chi(J)\leq6\text{ for every proper minor }J\text{ of }G,
 \qquad \kappa(G)\geq7,
 \qquad K_7^-\npreccurlyeq G.                         \tag{1.1}
\]

Let `F` be a componentwise-induced forest in `G`, put `H=G-F`, and assume
that

\[
 \{\Sigma_F(c):c\in\operatorname{Col}_6(H)\}
                         =2^F-\{\varnothing\}.        \tag{1.2}
\]

Thus, for every `q in F`, there is a six-colouring `c_q` of `H` whose
only equal-coloured selected edge is `q`.  After the other selected edges
are restored, `c_q` is a proper six-colouring of `G-q` and its only
conflict in `G` is `q`.

Assume also that `H` has a spanning exact `K_7^\vee` model in `G`, in the
sense of the audited exact-model separator dichotomy, and that

\[
                              |V(F)|\geq10.             \tag{1.3}
\]

A boundary response **retains an original coordinate** if it is induced
by the restriction of one of the colourings `c_q`, rather than by the
fresh edge deletion used during a large-boundary descent.

## 2. A coordinate is visible on every boundary smaller than its endpoint set

### Lemma 2.1 (small-boundary coordinate visibility)

Let `Y` be a nonempty connected set whose open neighbourhood

\[
                              S=N_G(Y)                  \tag{2.1}
\]

is an actual boundary, and suppose that `|S|<|V(F)|`.  Then some original
singleton coordinate `q in F` induces a proper six-colouring on one of
the two closed sides of `S`.  Its equality partition on `S` is rejected by
the intact opposite closed side.

#### Proof

Since `S` has fewer vertices than `V(F)`, not every endpoint of `F` lies in
`S`.  Choose `q=ab in F` with at least one endpoint outside `S`.  Put

\[
                         Z=V(G)-N_G[Y].                \tag{2.2}
\]

The set `Z` is nonempty because `S` is an actual boundary, and there is no
edge from `Y` to `Z`.  Since `q` is an edge and is not contained in `S`,
it has an endpoint in exactly one of the two open sides, or both endpoints
in the same open side.

If `q` has an endpoint in `Y`, delete `Y`.  The restriction of `c_q` to
the opposite closed side `G[S\cup Z]=G-Y` is proper.  Otherwise `q` has
an endpoint in `Z`, and the restriction of `c_q` to `G[Y\cup S]=G-Z` is
proper.  In either case the only conflict of `c_q` in `G` has been removed.

If the induced equality partition on `S` extended through the intact
opposite closed side, a permutation of the six colour names would align
the two boundary colourings.  Gluing them would give a proper six-colouring
of `G`, contrary to (1.1).  Hence the opposite side rejects the partition.
`\square`

The argument uses the literal selected edge only to locate its unique
conflict.  It does not require that the edge cross the boundary, and it
does not require any model label to survive the descent.

## 3. Original-coordinate bounded boundary

### Theorem 3.1 (coordinate-preserving boundary descent)

Under the hypotheses of Section 1, either `G` contains a `K_7^-` minor,
or there are a nonempty proper connected set `Y`, an actual boundary
`S=N_G(Y)`, and an edge `q in F` such that

\[
                              7\leq |S|\leq9,           \tag{3.1}
\]

and the original singleton-signature colouring `c_q` is proper on one
closed side of `S` and induces a boundary partition rejected by the intact
opposite closed side.

If the boundary is produced by at least one descent step, it is the open
neighbourhood of a singleton.  In that case the critical-host conclusion
`\delta(G)>=8` improves its order to eight or nine.  An initial order-seven
model boundary remains possible.

#### Proof

Apply the audited exact-`K_7^\vee` model-separator dichotomy to the spanning
exact model in `H`, viewed as a model in `G`.  Its first outcome is the
target.  Otherwise it gives a nonempty connected side with an actual
boundary `S_0` of order at least seven.

If `|S_0|<=9`, Lemma 2.1 applies because of (1.3).  Suppose instead that
`|S_0|>=10`.  Apply the audited large actual-boundary singleton descent.
It gives another actual boundary of strictly smaller order.  Iterate while
the current boundary has order at least ten.  Boundary order is a positive
integer, so the process terminates at an actual boundary `S` with

\[
                              7\leq |S|\leq9.           \tag{3.2}
\]

The descended response colourings may use fresh deleted edges; discard
them.  The global punctured signature cube (1.2) has not changed.  Since
`|S|<|V(F)|`, Lemma 2.1 reapplies directly to `S` and supplies one of the
original colourings `c_q`.  This proves (3.1) and the coordinate-retention
claim.  When at least one descent step was used, its last boundary is
`N_G(w)` for a singleton `w`; minimum degree eight then excludes order
seven. `\square`

### Corollary 3.2 (the eleven-vertex three-centre forest)

Suppose the common three-centre construction supplies

\[
               F_7\cong3P_3\mathbin{\dot\cup}K_2,
               \qquad |V(F_7)|=11,                       \tag{3.3}
\]

all `127` nonempty signatures on `G-F_7`, and a spanning exact
`K_7^\vee` model.  Then the target occurs or an original `F_7` singleton
coordinate is exposed on an actual response boundary of order seven,
eight, or nine.

### Corollary 3.3 (upgrade of the eight-coordinate endpoint theorem)

The conclusion of Corollary 5.2 in
[`hc7_k7minus_eight_coordinate_endpoint_visibility.md`](hc7_k7minus_eight_coordinate_endpoint_visibility.md)
may retain an original `F_8` coordinate even after a large-boundary
descent.  Indeed that forest has fifteen or sixteen distinct vertices, so
Theorem 3.1 applies.

## 4. Sharp limit for the five-edge cube

The five-edge forest

\[
                    P_3\mathbin{\dot\cup}P_3
                         \mathbin{\dot\cup}K_2          \tag{4.1}
\]

has only eight distinct vertices.  A terminal boundary of order eight or
nine can contain all of them.  Every nonempty equality signature then has
a monochromatic selected edge wholly in the shared boundary, so none of
the signature colourings is automatically proper on either closed side.
Thus endpoint counting alone cannot close the original five-cube hidden
allocation.  The eleven-vertex forest in Corollary 3.2 bypasses exactly
that numerical obstruction; it does not by itself terminalise the resulting
degree-eight or degree-nine response interface.

## 5. Dependencies and provenance

- the exact-`K_7^\vee` model-separator dichotomy;
- the large actual-boundary singleton descent; and
- the full punctured equality-signature cube on `F`.

The proof does not identify the descended singleton with a model bag or a
selected endpoint.  Its point is that no such identification is needed:
after numerical descent, one simply reuses an original singleton colouring
whose unique conflict cannot lie wholly in the smaller boundary.
