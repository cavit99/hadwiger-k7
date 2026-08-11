# The `b=2` rectangle is a two-root colourful-set transition

**Status:** written proof; separate internal audit GREEN at the revision
recorded in the adjacent audit.
This note sharpens the all-rainbow `b=2` row of the five-centre two-cut
attack.  It converts the Hall rectangle into one fixed five-chromatic core
with two opposite colourful-set responses and a literal separator for every
orientation-changing coordinate.  It also proves that one such coordinate
cannot directly be the desired minimum-side two-cut.  It does not construct
the paired-rooted `K_5` model and does not close the branch.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting

Use the notation and conclusions of the separately audited
[`b=2` rectangle theorem](hc7_k7minus_five_centre_b2_rectangle_locks.md).
Thus the two pole-incident centres are `z_p,z_q`,

\[
 z_pp,z_qq\in E(G),\qquad z_pq,z_qp\notin E(G),
\tag{1.1}
\]

and

\[
 T=(Z-\{z_p,z_q\})\cup\{p,q\}
\tag{1.2}
\]

is an independent five-set.  There are proper six-colourings

\[
 \phi_C\text{ of }G[C\cup T],\qquad
 \phi_R\text{ of }G[D\cup\{z_p,z_q\}\cup T]
\tag{1.3}
\]

in which `T` has one colour `gamma`.  Put

\[
                         \Omega=[6]-\{\gamma\}.
\tag{1.4}
\]

After erasing the colours of `z_p,z_q` in `phi_R`, their available lists
`L_p,L_q subseteq Omega` are disjoint and have orders `(2,3)` or `(2,2)`.
There is a four-set `Q subseteq Omega` such that both four-vertex contact
sets in `C` use `Q`, once each.  Write

\[
                         Q=\Omega-\{r_0\}.
\tag{1.5}
\]

For `x in {p,q}` and `a in Q`, let `x_x^a` be the unique vertex of
`N_C(z_x)` having colour `a`.

## 2. Every palette hole is attained by one coordinate switch

### Lemma 2.1 (complete common-hole orbit)

For every `r in Omega`, there is a proper six-colouring `phi_C^r` of
`G[C union T]` such that `T` has colour `gamma` and

\[
       \phi_C^r(N_C(z_p))
       =\phi_C^r(N_C(z_q))=\Omega-\{r\},
\tag{2.1}
\]

with each displayed colour occurring once in each contact set.

More strongly, fix such a colouring `phi_C^r` and let `s in Omega-{r}`.
The two `s`-coloured contacts of `z_p,z_q` lie in one common `r`--`s`
component `K_{rs}`.  Interchanging `r,s` on `K_{rs}` gives a colouring
`phi_C^s` satisfying (2.1) with hole `s`.

#### Proof

The initial colouring in (1.3) gives the assertion for `r=r_0`.  Suppose
that `phi_C^r` has already been obtained, and let `s!=r`.  If the two
`s`-coloured contacts lay in different `r`--`s` components, interchange
the two colours on the component containing exactly one of them.  The
boundary `T` remains monochromatic because its colour is `gamma`.

For the changed centre, its four distinct contact colours become
`Omega-{s}`; the other centre retains `Omega-{r}`.  Compare this altered
colouring with the fixed colouring `phi_R`, choosing one available colour
from each of the disjoint nonempty lists `L_p,L_q` for the two centres.
The forbidden-position relation has two rows of order four whose
intersection has order three.  It has no full row or column, no `4 by 2`
rectangle, and no `2 by 4` rectangle.  The exact eight-position Hall
criterion from the rectangle theorem therefore supplies an avoiding
permutation, which glues the two shores and six-colours `G`.  This is
impossible.  Hence both contacts lie in `K_{rs}`.

Neither row has an `r`-coloured contact, and each has exactly one
`s`-coloured contact.  Interchanging the two colours on `K_{rs}` therefore
replaces `s` by `r` in both contact sets and changes no other contact
colour.  It also fixes `T`.  This gives `phi_C^s`, and induction from
`r_0` reaches every member of `Omega`. \(\square\)

## 3. One fixed five-chromatic core

Delete `z_p,z_q` and glue `phi_C^r` to the restriction of `phi_R`.  This
gives a proper six-colouring `c_r` of

\[
                         H=G-\{z_p,z_q\}.
\tag{3.1}
\]

All switches in Lemma 2.1 use colours in `Omega`; hence the `gamma` colour
class is one fixed independent set, denoted `Gamma`, for every `c_r`.
Put

\[
                         X=H-\Gamma,
\qquad S_x=N_X(z_x)\quad(x\in\{p,q\}).
\tag{3.2}
\]

### Theorem 3.1 (two-root colourful-set core)

The graph `X` is exactly five-chromatic.  In every proper five-colouring
of `X`, at least one of `S_p,S_q` uses all five colours.

In the five-colouring `c_r|X`, one has

\[
 S_x\text{ uses all five colours}
       \quad\Longleftrightarrow\quad r\notin L_x.
\tag{3.3}
\]

Consequently both exclusive orientations occur: a hole in `L_p` makes
`S_q` colourful and `S_p` noncolourful, while a hole in `L_q` does the
reverse.  In the `(2,2)` list row, the unique member of
`Omega-(L_p union L_q)` gives a colouring in which both sets are colourful.

#### Proof

The restriction of any `c_r` is a five-colouring of `X`.  If `X` were
four-colourable, use four colours on `X`, a fifth colour on the independent
set `Gamma`, and one sixth colour on both nonadjacent vertices `z_p,z_q`.
This would six-colour `G`.  Hence `chi(X)=5`.

Now take an arbitrary proper five-colouring of `X`.  If `S_p` missed one
colour and `S_q` missed one colour, assign the respective missing colours
to `z_p,z_q` and give all of `Gamma` a fresh sixth colour.  The two centres
are nonadjacent, so the two missing colours need not be distinct.  This
again six-colours `G`, a contradiction.  Thus at least one contact set is
colourful.

In `c_r`, the `C`-contacts of either centre use `Omega-{r}`.  On the other
shore, the non-`gamma` colours on its contact triangle are

\[
                         \Omega-L_x.
\tag{3.4}
\]

The incident pole belongs to `Gamma` and has been deleted from `X`.
Therefore the colour set on `S_x` is

\[
                  (\Omega-\{r\})\cup(\Omega-L_x),
\tag{3.5}
\]

which is all of `Omega` exactly when `r notin L_x`.  The final assertions
follow from the disjointness and sizes of the two lists. \(\square\)

### Corollary 3.2 (the terminal paired-rooted model)

If `X` contains a `K_5`-minor model whose every branch set meets both
`S_p` and `S_q`, then `G` contains a `K_7^-` minor.

#### Proof

Every one of the five branch sets is adjacent to each of the singleton
sets `{z_p},{z_q}`.  The five model bags are pairwise adjacent, while the
two centres are nonadjacent.  These seven bags form a `K_7^-` model.
\(\square\)

Thus target exclusion turns the `b=2` row into a paired colourful-set
obstruction in one literal five-chromatic graph, not merely two unrelated
four-contact locks.

## 4. Every orientation change exposes a strict separator

Fix

\[
                         r\in L_p,\qquad s\in L_q,
\tag{4.1}
\]

and use the adjacent colourings `c_r,c_s` supplied by Lemma 2.1.  Let
`K_{rs} subseteq C` be their switched `r`--`s` component.

### Theorem 4.1 (coordinate-transition separator)

The component `K_{rs}` is a proper connected subset of `C`, is adjacent
to both `z_p,z_q`, and

\[
 N_G(K_{rs})=N_H(K_{rs})\mathbin{\dot\cup}\{z_p,z_q\}
\tag{4.2}
\]

is the boundary of an actual separation.  Moreover,

\[
                         |N_H(K_{rs})|\ge5,
\tag{4.3}
\]

and `N_H(K_{rs})` meets every one of the four colour classes outside
`{r,s}`.  More precisely, the `s`-coloured side of `K_{rs}` has a neighbour
in each of those four classes.

#### Proof

For every proper six-colouring of `H`, at least one of the two omitted
centres has neighbours in all six colour classes; otherwise give each a
colour missing from its neighbourhood and obtain a six-colouring of `G`.

In `c_r`, equation (3.3) says that `z_p` misses `r`, while `z_q` sees all
five colours in `Omega`; it also sees `gamma` through its incident pole.
Thus `z_q` is colour-dominating and `z_p` is not.  In `c_s` the roles are
reversed.  The two colourings differ by the interchange on `K_{rs}`.

Apply the separately audited
[two-root orientation-transition theorem](../results/hc7_two_root_kempe_orientation_transition.md)
with roots `z_q,z_p`.  It says that the switched component is adjacent to
both roots, its open neighbourhood in `G` is an actual separator, and its
neighbourhood in `H` has order at least `7-2=5`.  It also says that the
root-facing colour side which changes the orientation has a neighbour in
every untouched colour class.

Here that side has colour `s`.  Indeed, `s in L_q`, so the only
`s`-coloured neighbour of `z_q` in `c_r` is its unique `C`-contact in
`K_{rs}`; the interchange removes that colour from its neighbourhood.
Similarly `r in L_p`, so the interchange creates the previously missing
`r`-contact at `z_p`.  The two other occurrences needed to retain the
opposite colours lie on the `D`-side because the lists are disjoint.
This identifies the saturated side and proves all assertions except
proper containment.

The component is two-coloured.  If it were all of `C`, then `G[C]` would
be bipartite, contrary to the established bound `chi(G[C])>=4` in the
five-centre two-cut reduction.  Thus `K_{rs}` is a proper subset of `C`.
\(\square\)

## 5. Why one coordinate cannot be the anchored two-cut

Let

\[
                         A=Z-\{z_p,z_q\}.
\tag{5.1}
\]

All three vertices of `A` have colour `gamma` in every `c_r`.

### Corollary 5.1 (no direct minimum-side two-cut)

If `A subseteq N_H(K_{rs})`, then

\[
                         |N_H(K_{rs})|\ge6,
       \qquad |N_{G-Z}(K_{rs})|\ge3.
\tag{5.2}
\]

In particular, the separator returned by one orientation-changing
coordinate is never an anchored two-cut of `G-Z`.

#### Proof

Theorem 4.1 forces `N_H(K_{rs})` to meet the four untouched colour classes:
`gamma` and the three members of `Omega-{r,s}`.  The three vertices of `A`
account only for the `gamma` class.  Three further boundary vertices are
therefore needed for the other three classes, proving the first inequality.
Deleting all five centres removes exactly `A` from `N_H(K_{rs})` and
removes `z_p,z_q` from (4.2), so the second follows. \(\square\)

Thus the natural one-coordinate descent does produce a strict literal
component and an actual separator, but colour saturation prevents that
separator from being the required same-form two-cut.  A terminal proof must
either synchronize at least two coordinate transitions, construct the
paired-rooted `K_5` of Corollary 3.2, or use a larger transition boundary
without discarding its four untouched-colour incidences.

## Dependencies and claim status

- the all-rainbow `b=2` geometry, common rectangle, disjoint lists, and
  exact Hall criterion come from the separately audited rectangle theorem;
- `chi(G[C])>=4` comes from the separately audited five-centre two-cut
  reduction; and
- Theorem 4.1 invokes the separately audited two-root
  orientation-transition theorem.

All other deductions are proved here.  The paired-rooted `K_5` conclusion
is a terminal criterion, not an asserted existence theorem.
