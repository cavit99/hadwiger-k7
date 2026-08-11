# Global five-centre rotation reduction

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_five_centre_rotation_reduction_audit.md`](hc7_k7minus_five_centre_rotation_reduction_audit.md).
This note opens the three-connected branch of the five-centre argument.  It
gives an exact common-core formulation, a labelled uncrossing theorem and a
rigid fixed-root alternative.  It does not eliminate either branch of the
global argument and does not prove the `K_7^-` six-colour conjecture.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting

Let `G` be a graph satisfying

\[
 \chi(G)=7,\qquad
 \chi(M)\leq6\text{ for every proper minor }M\text{ of }G,
 \qquad K_7^-\npreccurlyeq G,                         \tag{1.1}
\]

and suppose

\[
 \kappa(G)\geq7,\qquad |E(G)|\geq4|V(G)|,
 \qquad |V(G)|\geq25.                               \tag{1.2}
\]

We use two audited consequences of these hypotheses.  Corollary 3 of the
[critical-host theorem](../results/hc7_k7minus_degree7_rooted_helper_closure.md)
gives `delta(G)>=8` and excludes literal `K_5` subgraphs.  Theorem 2 of the
[exceptional-neighbourhood
theorem](../results/hc7_k7minus_exceptional_neighbourhood_completion.md)
then gives `alpha(G[N_G(v)])<=3` for every degree-eight vertex `v`.

Fix five independent degree-eight vertices

\[
                         Z=\{z_1,\ldots,z_5\},
 \qquad                  F=G-Z.                     \tag{1.3}
\]

For a proper six-colouring `theta` of `F`, put

\[
 \operatorname{Sat}(\theta)=
 \{z\in Z:\theta(N_G(z))=[6]\}.                    \tag{1.4}
\]

The notation is independent of the names assigned to the six colours.
All neighbours of a vertex in `Z` lie in `F`, since `Z` is independent.

### Theorem 1.1 (the common core and its five singleton responses)

The graph `F` is two-connected, nonplanar and exactly six-chromatic.  Every
proper six-colouring `theta` of `F` satisfies

\[
                         \operatorname{Sat}(\theta)\ne\varnothing. \tag{1.5}
\]

For each `r in Z`, every proper six-colouring `phi_r` of `G-r` restricts to
a colouring `theta_r` of `F` for which

\[
                         \operatorname{Sat}(\theta_r)=\{r\}.       \tag{1.6}
\]

Thus the five critical deletion responses have one literal common host and
five distinct singleton saturation sets, without any preliminary alignment
of colour names or Kempe classes.

#### Proof

Deleting five vertices lowers connectivity by at most five, so `F` is
two-connected.  Since the vertices of `Z` are independent and each has
degree eight,

\[
 |E(F)|=|E(G)|-40\geq4|V(F)|-20.
\]

Here `|V(F)|>=20`, and hence the right-hand side is greater than
`3|V(F)|-6`.  Thus `F` is nonplanar.  It is six-colourable because it is a
proper subgraph of `G`.  A five-colouring of `F` would extend to a
six-colouring of `G` by assigning one new colour to every vertex of the
independent set `Z`.  Hence `chi(F)=6`.

If (1.5) failed, assign to each `z in Z` a colour absent from its
neighbourhood under `theta`.  These assignments are independent and would
six-colour `G`, a contradiction.

Now fix `r` and `phi_r`.  If `z ne r`, the colour `phi_r(z)` is absent from
`N_G(z)`, so `z` is not saturated by `theta_r`.  If `r` were also
unsaturated, a missing colour at `r` would extend `phi_r` to `G`.  This is
again impossible, and (1.6) follows.  `\square`

The data in (1.6), rather than the raw ordered pair of colour names
`(phi_i(z_j),phi_j(z_i))`, are the first colour-permutation-invariant
five-centre transition data.

## 2. Twenty rooted-model/web applications on one core

Fix distinct `r,z_i in Z`, and put

\[
 U_i=Z-\{z_i\},\qquad H_i=G-U_i=F+z_i.              \tag{2.1}
\]

Choose a proper six-colouring `phi_r` of `G-r`.  Since every colour occurs
on the eight neighbours of `r`, at least four colours occur exactly once.
Choose four of them and let

\[
                         X_r=\{x_1,x_2,x_3,x_4\}\subseteq V(F)     \tag{2.2}
\]

be their representatives.  The inclusion in `F` follows from the
independence of `Z`.

The audited four-centre rooted-model/web theorem applies to `U_i`, with
common graph `H_i`, root `r`, colouring `phi_r` and roots `X_r`.  There are
therefore twenty ordered applications `(r,i)`, grouped into five packets of
four applications with the same literal colouring and the same four roots.

### Proposition 2.1 (a web outcome is a labelled separation of `F`)

Consider the web outcome for an ordered pair `(r,i)`.  It gives a
three-set `T_{r,i} subseteq V(H_i)` and an exact order-seven cut

\[
                         U_i\mathbin{\dot\cup}T_{r,i}               \tag{2.3}
\]

of `G`, with two full connected complementary components.

If `z_i in T_{r,i}`, then `T_{r,i}-\{z_i\}` is a two-cut of `F`.  Otherwise
`T_{r,i} subseteq V(F)`, and deleting `z_i` from the component which
contains it gives a proper separation `p_{r,i}` of `F` such that

\[
 |S_{p_{r,i}}|=3,\qquad
 C_Z(p_{r,i})=Z-\{z_i\}.                             \tag{2.4}
\]

Here `S_p` is the separator of `p`, and

\[
 C_Z(p)=\{z\in Z:N_G(z)\text{ meets both open shores of }p\}.       \tag{2.5}
\]

In particular, when `F` is three-connected, every web outcome has the
second form in (2.4): it is an order-three separation crossed by precisely
the four centres other than its omitted label.

#### Proof

If `z_i in T_{r,i}`, removing it from the separator in `H_i=F+z_i`
leaves the two nonempty complementary components separated in `F`.  This
is the asserted two-cut.

Suppose instead that `T_{r,i} subseteq V(F)`.  Let `K,L` be the two
components of `G-(U_i union T_{r,i})`, and suppose `z_i in L`.  Then

\[
 (K\cup T_{r,i},\ (L-\{z_i\})\cup T_{r,i})            \tag{2.6}
\]

is a separation of `F`.  It is proper: `K` is nonempty, while fullness of
`L` at the centre `r in U_i` gives a neighbour of `r` in `L` which cannot
be `z_i`.

Every centre in `U_i` has a neighbour in each of `K,L`; its neighbour in
`L` is not `z_i`, because `Z` is independent.  Thus all four members of
`U_i` cross (2.6).  The omitted centre `z_i` has no edge to `K`, since it
lies in the other component of the exact cut.  This proves (2.4).  The last
assertion follows because a three-connected graph has no two-cut.
`\square`

The rooted-model outcomes remain literal as well: for `(r,i)` they give an
`X_r`-rooted `K_4` model in `F+z_i`, and hence an `r`-rooted `K_5` model
in `G-(Z-\{r,z_i\})`.  The proposition does not assert that such a model
can already be completed to `K_7^-`.

## 3. Exact labelled uncrossing

For any separation `p` of `F`, define

\[
                         \lambda_Z(p)=|S_p|+|C_Z(p)|.                \tag{3.1}
\]

### Lemma 3.1 (minimum lift order)

The function `lambda_Z` is symmetric and submodular.  It is the minimum
order of a separation of `G` whose restriction to `F` is `p`.  Consequently

\[
                         \lambda_Z(p)\geq7                           \tag{3.2}
\]

for every proper separation `p` of `F`.

If equality holds in the submodular inequality for two separations, then
equality holds separately for the crossing indicator of every centre in
`Z`.

#### Proof

Every lift must place `S_p` and every crossing centre in its separator.
Conversely, put precisely those vertices there.  A noncrossing centre can
be placed on a shore containing all its neighbours outside `S_p`; centres
have no edges to one another.  This constructs a lift of order (3.1).

Symmetry is immediate.  The separator-order term is modular under meet and
join, and the crossing indicator of each fixed centre is submodular by the
four-corner identities.  Summing proves submodularity.  If equality holds
in the sum, none of the individual zero-one inequalities can be strict.
Finally, a lift of a proper separation is proper, so (1.2) gives (3.2).
`\square`

Two oriented separations `p,q` of `F` are **anchor-compatible** if their
left open shores have a common vertex and their right open shores have a
common vertex.  Reversing either separation is allowed before making this
test.

### Theorem 3.2 (two labelled web separations)

Let `p_i,p_j` be separations obtained from Proposition 2.1 with distinct
omitted labels `z_i,z_j`, and suppose they are anchor-compatible.  Their
meet and join are proper and have `lambda_Z=7`.  Their ordinary separator
orders are, up to exchange, exactly one of

\[
                              (2,4),\qquad(3,3).       \tag{3.3}
\]

More precisely, the three centres in `Z-\{z_i,z_j\}` cross both corner
separations, while each of `z_i,z_j` crosses exactly one corner.

If the two omitted labels cross the same corner, that corner has ordinary
order two, is crossed by all five centres, and is a genuine two-cut of
`F`.  If the labels cross different corners, both corners have order three
and each is crossed by exactly four centres, with one of `z_i,z_j` omitted
at each corner.

Thus, in the three-connected branch, every anchor-compatible pair is
forced into the second, label-rotating `3+3` alternative.

#### Proof

Common left and right anchors make both meet and join proper.  Each input
has `lambda_Z=7` by (2.4).  Submodularity and (3.2) therefore force equality
and value seven at both corners.

The ordinary separator orders of the corners sum to the input sum six.
Since at most five centres can cross a corner of lift order seven, each
ordinary order is at least two, giving (3.3).

Each centre outside `\{z_i,z_j\}` crosses both inputs.  Centre-wise equality
in Lemma 3.1 makes it cross both corners.  Each omitted label crosses one
input and not the other, so it crosses exactly one corner.  A corner crossed
by `3+a` centres, where `a in \{0,1,2\}`, has ordinary order `4-a`.
This gives all remaining assertions.  `\square`

The theorem isolates the exact missing incidence: a returned two-cut is
equivalent to putting both omitted labels on the same corner.  Ordinary
uncrossing alone permits them to split and supplies no colouring response
on either new boundary.

### Proposition 3.3 (the alternative to anchor compatibility)

If two labelled web separations are not anchor-compatible under either
orientation, one open shore of one separation is contained in the
three-vertex separator of the other.  The corresponding component of its
original exact order-seven cut in `G` has order three or four.

#### Proof

Form the bipartite graph whose two classes are the two open shores of each
separation, joining two shores when they intersect.  Anchor compatibility
is exactly the existence of a perfect matching.  A bipartite graph with
two vertices in each class and no perfect matching has an isolated vertex.
The associated nonempty open shore is therefore contained in the other
separator and has order at most three.

That shore is obtained from a component of the original exact cut either
unchanged or by deleting its omitted centre.  Hence the original component
has order at most four.  Every component behind an order-seven cut here has
order at least three: order one contradicts minimum degree eight, and order
two would put the independent four-set `U_i` in the neighbourhood of a
degree-eight vertex, contrary to the audited degree-eight neighbourhood
theorem.  The component therefore has order three or four.  `\square`

This is a finite endpoint, but it is not declared terminal here.

## 4. A fixed-root packet

Fix `r`, `phi_r` and `X_r` as in Section 2, and suppose all four ordered
applications `(r,i)`, with `z_i ne r`, have web outcomes and do not return
a two-cut through `z_i in T_{r,i}`.  For each application, orient its exact
cut so that `C_i` is the component selected behind the facial three-set and
`D_i` is the other component.  Put

\[
                         A_i=X_r\cap(D_i-T_{r,i}).     \tag{4.1}
\]

Every `A_i` is nonempty, all vertices of `X_r` avoid `C_i`, and Lemma 2.3
of the four-centre theorem says that every `x in A_i` supplies the
one-sided extension colour `phi_r(x)` for `r` on the closed `C_i`-shore.

### Theorem 4.1 (trace collision or the maximal incompatible packet)

Exactly one of the following holds.

1. **Common literal extension.**  There are distinct `i,j` and a literal
   vertex `x in A_i cap A_j`.  The same colouring `phi_r` extends on both
   selected closed shores after restoring `r` with the same named colour
   `phi_r(x)`.
2. **Maximal incompatible packet.**  The four sets `A_i` are pairwise
   disjoint.  After a bijective relabelling of `X_r` as
   `\{x_i:z_i ne r\}`, one has

   \[
    A_i=\{x_i\},\qquad T_{r,i}=X_r-\{x_i\},           \tag{4.2}
   \]

   and hence four exact cuts

   \[
    N_G(C_i)=(Z-\{z_i\})\mathbin{\dot\cup}
                         (X_r-\{x_i\}).               \tag{4.3}
   \]

   The opposite component `D_i` contains `x_i`, while the selected
   component `C_i` avoids all four vertices of `X_r`.

#### Proof

The first outcome is simply the meaning of a nonempty intersection in
(4.1), together with the retained-trace statement of the four-centre
theorem.

If no two sets meet, four nonempty subsets of the four-set `X_r` must be
its four singleton parts.  Relabel so that `A_i=\{x_i\}`.  Every member of
`X_r` avoids `C_i`, and any member other than `x_i` is neither in `C_i` nor
in `D_i-T_{r,i}`.  It therefore lies in `T_{r,i}`.  Since that separator has
order three, it is exactly `X_r-\{x_i\}`.  Equation (4.3) is the exact-cut
identity from the web theorem.  `\square`

The second outcome is not a vague failure of pigeonhole.  It is a fully
labelled tetrahedral pattern: every omitted centre has its own omitted
root, and the other three roots are the whole ordinary separator.

### Theorem 4.2 (the maximal packet returns a five-centre two-cut)

The maximal incompatible packet forces a two-cut of `F`.  More precisely,
there are distinct indices `i,j` such that

\[
 Q=Z\mathbin{\dot\cup}(X_r-\{x_i,x_j\})               \tag{4.4}
\]

is an exact order-seven cut of `G`.  Hence
`X_r-\{x_i,x_j\}` is a two-cut of `F`, and the audited five-centre
two-cut reduction applies to its two full complementary components.

One of the two closed `Q`-shores has additional fixed-colouring data.  The
restriction of `phi_r` to that shore minus `r` extends after restoring `r`
with either of the two distinct colours

\[
                         \phi_r(x_i),\qquad\phi_r(x_j).              \tag{4.5}
\]

#### Proof

Put `B=Z union X_r`, so that the four packet boundaries are

\[
                         S_i=B-\{z_i,x_i\}.            \tag{4.6}
\]

Call an index `i` **internal** when `z_i in C_i`; otherwise `z_i in D_i`.
If `e` is not internal, then `C_e cap B` is empty.  For every `j ne e`, the
connected set `C_e` is disjoint from `S_j`, and hence lies wholly in `C_j`
or `D_j`.  It cannot lie in `C_j`: fullness of `C_e` at
`x_j in S_e` gives an edge from `x_j` to `C_e`, whereas `x_j in D_j`.
Thus

\[
                         C_e\cap C_j=\varnothing       \tag{4.7}
\]

for every `j ne e`.

There are at least two internal indices.  Otherwise (4.7) makes the four
sets `C_i` pairwise disjoint.  Fullness at the fixed centre `r` supplies a
vertex

\[
                         y_i\in N_G(r)\cap C_i
\]

for each `i`.  Every `y_i` lies outside `B`: selected components avoid
`X_r`, and independence of `Z` prevents `y_i=z_i`.  The four vertices are
pairwise nonadjacent, since an edge `y_i y_j` would put the vertex
`y_j notin B` in `N_G(C_i)=S_i subseteq B`.  This gives an independent
four-set in `N_G(r)`, contrary to the audited bound
`alpha(G[N_G(r)])<=3`.

Choose two internal indices `i,j`.  Since `z_j in S_i` and `C_i` is full,
there is an edge `z_jv` with `v in C_i`.  Independence of `Z` and avoidance
of `X_r` give `v notin B`.  But `z_j in C_j`, so the exact cut `S_j`
forces `v in C_j`.  Thus

\[
                         C_i\cap C_j\ne\varnothing.    \tag{4.8}
\]

Take the meet of the two exact separations oriented towards `C_i,C_j`.
A direct membership check using (4.6) and internality gives its separator
exactly as `Q` in (4.4).  No vertex outside `B` enters the separator: such a
vertex belongs to an open shore of each input, and a vertex in both selected
shores is in neither opposite shore.  The meet is proper.  Its left open
shore contains the vertex in (4.8), while its right open shore contains
`x_i` and `x_j`.  Thus `Q` is an order-seven cut.  Removing `Z` proves that
`X_r-\{x_i,x_j\}` is a two-cut of `F`.  The two-component theorem for
order-seven cuts and the five-centre two-cut theorem give the stated full
two-shore conclusion.

Finally, both `x_i,x_j` lie on the opposite open shore of this meet.  They
are the unique neighbours of `r` in two distinct colour classes under
`phi_r`.  Neither colour therefore appears on a neighbour of `r` in the
selected closed shore.  Assigning either colour to `r` proves (4.5).
`\square`

### Corollary 4.3 (coupled critical-edge operations at the returned cut)

Use `i,j,Q` from Theorem 4.2 and put

\[
 a=\phi_r(x_i),\qquad b=\phi_r(x_j),\qquad
 e_i=rx_i,\qquad e_j=rx_j.                           \tag{4.9}
\]

Restoring `r` with colour `a` gives a proper six-colouring of `G-e_i`, and
restoring it with `b` gives one of `G-e_j`.  The two colourings agree
literally on `G-r` and hence on `Q-r`.  On the common deletion
`G-\{e_i,e_j\}`, their monochromatic-edge signatures are respectively
`\{e_i\}` and `\{e_j\}`.

If `x_ix_j` is absent, contraction of the induced path `x_i r x_j` also
gives a six-colouring with both selected edges monochromatic.  If `x_ix_j`
is present, that double signature is impossible.  A signature with neither
edge monochromatic is always impossible because it would six-colour `G`.

The exact remaining normalization can be stated on the common core.  Put

\[
 \theta=\phi_r|F,\qquad
 L_z=[6]\setminus\theta(N_G(z))\quad(z\in Z-\{r\}).   \tag{4.10}
\]

One of the two literal restorations can be changed only on `Z-r` so that
the returned boundary has the standard distinct partition

\[
                         Z\mid\{p\}\mid\{q\},
 \qquad \{p,q\}=X_r-\{x_i,x_j\},                     \tag{4.11}
\]

if and only if

\[
             \{a,b\}\cap\bigcap_{z\in Z-\{r\}}L_z
                         \ne\varnothing.              \tag{4.12}
\]

When (4.12) holds, the selected shore in Theorem 4.2 is the
distinct-response shore, and the deleted edge lies in the opposite closed
shore, joining `r in Q` to its open side.
Without (4.12), singleton saturation gives only the four separate
nonempty sets `L_z`; it does not normalize either operation.

Finally, before this normalization, the two restorations induce the same
equality partition on `Q` exactly when neither `a` nor `b` occurs on
`Q-r`; in that case `r` is a singleton block in both partitions.  This
common partition need not be the standard partition in (4.11).

#### Proof

The colours `a,b` occur at the unique neighbours `x_i,x_j` of `r` in their
respective colour classes.  Assigning `a` to `r` therefore creates exactly
the monochromatic edge `e_i`; assigning `b` creates exactly `e_j`.  This
proves the two singleton signatures and their literal agreement away from
`r`.  If `x_ix_j` is absent, the three vertices induce a path, so a
six-colouring of its contraction expands to the double signature.  If the
edge is present, a double signature would make that retained edge
monochromatic.  The empty signature would be a colouring of `G`.

For `t in \{a,b\}`, all five centres can receive `t` while the colouring
`theta` of `F` is fixed exactly when `t in L_z` for every `z ne r`; the one
edge from `r` to its unique representative of colour `t` is the selected
deleted edge.  The two vertices in `X_r-\{x_i,x_j\}` retain two other
singleton colours, proving (4.11)--(4.12).  The selected shore omits
`x_i,x_j`, so its restriction is unmodified and has the distinct response;
the audited two-cut theorem fixes the opposite orientation.  The last
partition assertion follows because the two colourings differ on `Q` only
at `r`.  `\square`

### Corollary 4.4 (fixed-root rotation collision)

If `F` is three-connected, then for every fixed `r`, `phi_r` and `X_r`,
one of the four ordered applications has a rooted-model outcome, or two web
outcomes have a common literal extension vertex as in Theorem 4.1(1).

#### Proof

If all four outcomes are webs and there is no common literal extension,
Theorem 4.1 gives the maximal packet.  Theorem 4.2 then gives a two-cut of
`F`, contrary to three-connectivity.  `\square`

## 5. Consequence for the global campaign

The exhaustive split remains

\[
                         \kappa(F)=2
              \qquad\text{or}\qquad
                         \kappa(F)\geq3.              \tag{5.1}
\]

The first branch is the audited five-centre two-cut problem.  In the second
branch, this note replaces an unspecified comparison of five unrelated
colourings by the following exact available outcomes among the twenty
ordered applications:

1. a literal rooted-model outcome in some `F+z_i`;
2. a common-root trace collision;
3. a returned five-centre two-cut, with the two-colour extension in (4.5);
4. an anchor-compatible `3+3` label rotation; or
5. an original exact-cut component of order three or four.

In particular, the three-connected branch has the fixed-root alternative
in Corollary 4.4; the maximal packet is eliminated there.  The next theorem
must compose the rooted-model or common-literal-trace outcomes across the
five roots.  Neither a raw colour-name transition graph nor the old
four-region interaction graph does this: the five colourings may lie in
different Kempe classes, and the four-region theorem has one fixed deleted
four-set as a hypothesis.

The nearest general separator result is Theorem 1.6 of Lafferty, Liu, Rolek
and Yu, [*Connectivity of contraction-critical
graphs*](https://arxiv.org/abs/2509.07144) (2025 preprint).  In the two-cut
branch, a two-cut `\{p,q\}` of `F` makes `Z union \{p,q\}` a seven-vertex
separator of `G` with independence number at least five.  Taking `s=7` and
the smallest permitted value `t=3` in their theorem requires only
independence number at least four, but it requires

\[
                         k\geq7+2^2-3=8.
\]

It therefore misses the present seven-contraction-critical host by exactly
one chromatic unit.  The theorem does not apply directly in the
three-connected branch and does not compose the twenty labelled
rooted-model/web outcomes above.
