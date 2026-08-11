# Four crossing response edges form a tight signed Boolean separator cube

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_four_crossing_signed_boolean_reduction_audit.md`](hc7_k7minus_four_crossing_signed_boolean_reduction_audit.md).
This is an unbounded, computation-free reduction of the four-crossing
three-cut row in the five-centre common-host theorem.  It is not a proof of
the `K_7^-` six-colour conjecture or `HC_7`.

## 1. Setting

Use the hypotheses and notation of the audited
[five-centre common-matching theorem](hc7_k7minus_five_centre_common_matching_reduction.md).
Thus `G` is seven-connected, seven-chromatic and `K_7^-`-minor-free, every
proper minor is six-colourable,

\[
                         M=\{z x_z:z\in Z\},
 \qquad                  H=G-M,                       \tag{1.1}
\]

where `M` is a matching of order five, and every nonempty subset of `M` is
the exact monochromatic-edge signature of a proper six-colouring of `H`.
Also `|E(G)|>=4|V(G)|` and `|V(G)|>=25`.

Suppose `H` has a three-cut `S` for which exactly four edges of `M` run
between the two components `A,D` of `H-S`.  Write these edges as

\[
                         E=\{a_i d_i:1\le i\le4\},
 \qquad a_i\in A,\quad d_i\in D.                    \tag{1.2}
\]

No orientation of the centre ends is assumed: a centre may be `a_i` or
`d_i` independently for each coordinate.  This is why the cube below is
called signed.

For `R subseteq E`, let `X` choose one end of every edge of `E-R`, and put

\[
                         Q(R,X)=S\mathbin{\dot\cup}X. \tag{1.3}
\]

## 2. The tight deletion hierarchy

### Theorem 2.1 (signed Boolean separator cube)

For every nonempty `R subseteq E` and every endpoint choice `X` in (1.3),
all of the following hold.

1. The graph `(G-R)-Q(R,X)` has exactly two components

   \[
                A-(X\cap A),\qquad D-(X\cap D),       \tag{2.1}
   \]

   and both are adjacent to every vertex of `Q(R,X)`.
2. The separator is tight:

   \[
          |Q(R,X)|=7-|R|,
          \qquad \kappa(G-R)=7-|R|.                  \tag{2.2}
   \]
3. One has

   \[
          \chi(G-R)=6,
          \qquad |E(G-R)|\ge4|V(G)|-|R|.             \tag{2.3}
   \]
4. Relative to the deleted edges `R`, the matching signatures of proper
   six-colourings of `G-R` are exactly

   \[
                              2^R-\{\varnothing\}.    \tag{2.4}
   \]

Thus the four rows are

\[
\begin{array}{c|c|c}
 |R|&\kappa(G-R)&\text{exact separator order}\\ \hline
 1&6&6\\
 2&5&5\\
 3&4&4\\
 4&3&3.
\end{array}                                           \tag{2.5}
\]

#### Proof

When one endpoint is chosen from every edge of `E`, Theorem 3.2 of the
common-matching theorem, together with its subsequent order-seven upgrade,
says that `S` and those four endpoints form an exact order-seven cut with
two full complementary components.

Fix `R,X`.  Extend `X` to a full transversal by choosing the `D`-end of
every edge of `R`.  In the resulting exact cut, the `A`-side is precisely
`A-(X cap A)`, so that graph is connected.  Choosing instead every
`A`-end of `R` proves that `D-(X cap D)` is connected.  The same two full
cuts show that every vertex of `S` has a neighbour in both displayed sets.

If `x in X cap A`, its matching mate lies in `D-(X cap D)` and supplies
the cross-shore boundary contact; fullness of a full transversal cut
supplies a neighbour of `x` in `A-(X cap A)`.  The argument is symmetric
for `x in X cap D`.  Hence both connected sets in (2.1) are full at
`Q(R,X)`.  No edge joins them in `G-R`: an edge of `E-R` has one end in
`X`, the edges of `R` were deleted, and the fifth edge of `M` did not cross
the original components.  This proves item 1 and the separator upper bound
in (2.2).

For the lower bound, suppose a set `T` of order less than `7-|R|`
separated `G-R`, and choose one component `K` of `(G-R)-T`.  The only
edges of `G-T` from `K` to the other components belong to `R`; let there be
`s<=|R|` of them.  If `K` has a vertex which is not an end of those edges,
add their `K`-ends to `T`.  Otherwise `K` consists of at most four such
ends; add one opposite end and the remaining `K`-ends.  The latter choice
leaves a vertex on each side because `|V(G)|>=25` and `|T|+|R|<=6`.
In either case one obtains a proper separator of `G` of order at most

\[
                         |T|+s<7,
\]

contrary to seven-connectivity.  This proves the lower bound and item 2.

Item 3 is Theorem 2.2 of the common-matching theorem and deletion of
`|R|` edges from the standing density bound.  For nonempty `I subseteq R`,
six-colour `G/I` and expand the contractions into `G-R`.  Exactly the edges
of `I` have equal-coloured ends, since every edge of `R-I` remains in the
quotient.  An empty signature would restore all of `R` and six-colour `G`.
This proves item 4. `\square`

## 3. One linkage identifies all four signed coordinates

### Theorem 3.1 (simultaneous coordinate paths)

Choose

\[
 a\in A-\{a_1,a_2,a_3,a_4\},
 \qquad d\in D-\{d_1,d_2,d_3,d_4\}.                 \tag{3.1}
\]

Such vertices exist.  Every family of seven internally vertex-disjoint
`a`--`d` paths has one path for each `i` on which `a_i d_i` occurs as a
literal consecutive edge.  Distinct coordinate edges lie on distinct
paths, and the same path assignment works for all sixteen endpoint
transversals.

#### Proof

The component-size argument in the common-matching theorem gives
`|A|,|D|>=6`, so (3.1) is possible.  Seven-connectivity supplies seven
internally disjoint `a`--`d` paths.  Every full-transversal separator has
order seven and separates `a` from `d`; hence each path meets it once, and
the seven paths exhaust it.

Start with the transversal containing all four `D`-ends.  For a fixed
`i`, compare it with the cut obtained by replacing `d_i` by `a_i`.  Six
boundary vertices are unchanged, so the remaining path contains both
`a_i,d_i`.  Traversed from `A` to `D`, `a_i` precedes `d_i`.  A vertex
strictly between them would lie on the `A`-side of the first cut and the
`D`-side of the second, which is impossible.  Thus the two vertices are
consecutive.  Repeating this for all four coordinates assigns distinct
paths to them, and every other transversal contains exactly the prescribed
endpoint on each assigned path. `\square`

## 4. Dense rows return a near-clique or a response-bearing separator

### Corollary 4.1

Let `R subseteq E` with `1<=|R|<=3`.  The graph `G-R` is four-connected
and satisfies the Norin--Totschnig density threshold.  It therefore has a
spanning `K_7^\vee`-minor model.  In `G`, either this already gives a
`K_7^-` minor, or the audited
[exact `K_7^\vee` dichotomy](hc7_k7minus_exact_k7vee_separator_dichotomy.md)
returns a nonempty proper connected model-bag piece `Y` whose complement
in its bag is connected and whose open neighbourhood is an actual
separator of order at least seven.

Put

\[
                         R_Y=\{e\in R:e\cap Y\ne\varnothing\}. \tag{4.1}
\]

For every nonempty `I subseteq R_Y`, a signature-`I` colouring of `G-R`
is proper on `G-Y`, and its exact precolouring of `N_G(Y)` does not extend
over `G[Y union N_G(Y)]`.  Hence `Y` carries
`2^{|R_Y|}-1` literal response traces when `R_Y` is nonempty.  Their
boundary partitions need not be distinct.

#### Proof

By (2.2), `G-R` is at least four-connected.  By (2.3),

\[
                         |E(G-R)|\ge4|V(G-R)|-3,
\]

which is above the `4|V|-8` threshold.  The exceptional graph
`K_{2,2,2,2}` is excluded by `|V(G)|>=25`.  Enlarge the resulting
`K_7^\vee` model to span.

Target-freeness first makes both nominal missing adjacencies absent in
`G-R`.  If restoring an edge of `R` fills either one, the seven bags contain
a `K_7^-` model.  Otherwise the spanning model remains exact in `G`, and
the cited dichotomy gives `Y`.

For nonempty `I subseteq R_Y`, take the colouring in (2.4) with signature
`I`.  Its only monochromatic restored edges are those in `I`, all hit by
`Y`; it is therefore proper on `G-Y`.  An extension of its exact boundary
precolouring through `Y` would glue to a six-colouring of `G`. `\square`

## 5. Exact scope

The theorem closes the connectivity and linkage questions for the complete
four-crossing cube, including the previously unrecorded order-four and
order-three deletion rows.  It does not synchronize the boundary
partitions of different signature colourings.  The nested set in
Corollary 4.1 may avoid every endpoint of `R`, and its boundary may have
order greater than seven.

The fifth selected edge is noncrossing in this row.  It remains proper in
all colourings used above and does not supply a common boundary partition
or a second compatible model-bag piece.  The four-coordinate cube need not
be anchored to the distinguished minimum trace-admissible side from the
older four-centre argument.  Consequently this result does not close the
four-crossing row.

## Dependencies

The signed cube starts from the audited common-matching theorem cited in
Section 1 and its audited order-seven two-component input.  The dense-row
input is Theorem 6 of Sergey Norin and Agnès Totschnig,
[*Every graph with no `K_7^\vee` minor is
6-colorable*](https://arxiv.org/abs/2507.03244).  The returned separator is
the audited exact `K_7^\vee` dichotomy cited in Corollary 4.1.  No finite
enumeration is used.
