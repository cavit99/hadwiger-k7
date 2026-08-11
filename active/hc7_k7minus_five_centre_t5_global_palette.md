# The five-root row: a global palette and critical-completion alternative

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_five_centre_t5_global_palette_audit.md`](hc7_k7minus_five_centre_t5_global_palette_audit.md).
This note gives an unbounded all-five-centre reduction in the
no-singleton-contact branch.  It does not turn the final rainbow-triangle
row or the critical completions below into a `K_7^-` minor.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting

Use the notation and hypotheses of the audited
[five-centre two-cut reduction](../results/hc7_k7minus_five_centre_two_cut_reduction.md).
Thus

\[
 S=Z\mathbin{\dot\cup}\{p,q\},\qquad |Z|=5,
\]

`G-S` has connected full components `C,D`, the permitted response on `C`
has `p=q`, and the permitted response on `D` has `p!=q`.  Assume the
no-singleton-contact branch

\[
 c_z=|N_C(z)|\ge2,\qquad d_z=|N_D(z)|\ge2
 \quad(z\in Z).                                      \tag{1.1}
\]

Assume also that the full rooted instance on each shore is infeasible and
that deleting any one root makes it feasible.  For every `z in Z`, use the
critical-host facts that `G[N(z)]` is `K_4`-free and has independence number
at most three.  The audited
[equality-side transfer](hc7_k7minus_five_centre_four_root_transfer.md)
then gives

\[
 c_z\ge4,
 \qquad N_D(z)\text{ is a clique of order at most three}. \tag{1.2}
\]

The audited distinct-side transfer in the same note gives

\[
 \rho_z=|N_{\{p,q\}}(z)|\le1.                        \tag{1.3}
\]

Fix one permitted colouring `phi_D` of `G[D union S]`, and name its
boundary colours by

\[
 \phi_D(Z)=\alpha,\qquad
 \phi_D(p)=\beta,\qquad
 \phi_D(q)=\delta.
\tag{1.4}
\]

Write

\[
                         \Gamma=[6]-\{\alpha,\beta,\delta\}.
\tag{1.5}
\]

## 2. The equality side has one common four-colour transversal

### Lemma 2.1 (universal equality-shore palette)

Let `phi_C` be any permitted colouring of `G[C union S]`, with `Z` given
colour `alpha` and `p,q` given a common different colour `beta`.  Then

\[
 [6]-\{\alpha,\beta\}
       \subseteq \phi_C(N_C(z))
       \qquad(z\in Z).                               \tag{2.1}
\]

In particular, the same four free colours occur at the `C`-contacts of
all five centres in one fixed colouring.

#### Proof

Fix `z` and put `A=Z-{z}`.  Feasibility of `A` on `C` and infeasibility of
`Z` give, by the equal-response transfer, a proper colouring of the closed
`D`-side in which `A` is monochromatic, `p,q` have one common different
colour, and `z` avoids the pole colour.  Align the first two colours with
`alpha,beta` in `phi_C`.

Use `phi_C` on `C union A union {p,q}` and the transferred colouring on
`D union {z}`.  Their only untested edges are those between `z` and `C`.
If the transferred colour of `z` is `alpha`, these edges are proper because
`phi_C` originally colours `z` with `alpha`.  Otherwise the colour of `z`
is one of the four colours outside `\{alpha,beta\}`.  Those four colour
names may be permuted arbitrarily on the `D`-side while the common boundary
remains fixed.  If one of them were absent from `phi_C(N_C(z))`, send the
colour of `z` to that absent colour and glue.  Either case six-colours `G`,
a contradiction.  Hence all four colours occur, proving (2.1). \(\square\)

## 3. The exact four contact profiles

### Lemma 3.1 (profile table)

Every centre has exactly one of the four profiles

\[
 (c_z,d_z,\rho_z)\in
 \{(4,3,1),(5,2,1),(5,3,0),(6,2,0)\}.               \tag{3.1}
\]

#### Proof

By (1.1)--(1.3), `c_z>=4`, `d_z in {2,3}`, and `rho_z in {0,1}`.
The degree-eight identity

\[
                         c_z+d_z+\rho_z=8
\]

now gives exactly (3.1). \(\square\)

Let

\[
                         b=\sum_{z\in Z}\rho_z.
\tag{3.2}
\]

The audited
[exact boundary matching theorem](hc7_k7minus_five_centre_t4_boundary_incidence.md)
says that the centre--pole graph has matching number two.  Since every
centre has at most one pole edge,

\[
 2\le b\le5,                                         \tag{3.3}
\]

both pole labels occur, and if `b>=3` two pole-incident centres have the
same pole neighbour.  If `b=2`, there is exactly one `p`-incident centre,
one `q`-incident centre, and three pole-free centres.

## 4. Transfer minors and their exact chromatic completions

Fix `z in Z`.  Choose a `D`-side four-root witness omitting `z`.  In the
notation of the distinct-response transfer, contract the component
containing `Z-{z}` to `k_z` and the two connected halves of its `p`--`q`
path to `a_z,b_z`, with `p in a_z` and `q in b_z`.  Delete the unused
vertices of `D` and retain `C` and `z`.  Denote the resulting proper minor
by `M_z`.  The vertices

\[
                         k_z,a_z,b_z                 \tag{4.1}
\]

form a triangle.  Every proper six-colouring of `M_z` pulls back to a
colouring of the closed `C`-side in which `Z-{z}`, `p`, and `q` have three
distinct colours.

Call `z` **rainbow on `D`** in `phi_D` when `d_z=3` and

\[
                         \phi_D(N_D(z))=\Gamma.       \tag{4.2}
\]

The clique conclusion in (1.2) makes the three colours in (4.2) distinct.

### Theorem 4.1 (rainbow or exact critical completion)

For every `z in Z`, the following exhaustive alternative is available,
classified first according to whether (4.2) holds.

1. The centre `z` is rainbow on `D`.
2. If `rho_z=1`, let `t_z` be the pole not adjacent to `z`, and let
   `v_z` be the corresponding one of `a_z,b_z`.  Then

   \[
                         \chi(M_z+zv_z)=7.            \tag{4.3}
   \]

3. If `rho_z=0`, add to `M_z` every missing edge in
   `\{za_z,zb_z\}`.  The resulting graph `M_z^+` satisfies

   \[
                         \chi(M_z^+)=7.               \tag{4.4}
   \]

In conclusion 2, `zv_z` is absent from `M_z`, and every proper
six-colouring of `M_z` gives `z` and `v_z` one common colour.  In conclusion
3, every proper six-colouring of `M_z` gives `z` the colour of `a_z` or
the colour of `b_z`; at least one of the two displayed edges is missing.

#### Proof

Take an arbitrary proper six-colouring of `M_z`.  Since (4.1) is a
triangle, rename its colours `alpha,beta,delta`, respectively.  Pull the
colouring back to the closed `C`-side and compare it with the fixed
colouring `phi_D`.  Use the pulled-back colouring on `C union {z}` and
`phi_D` on `D union (S-{z})`.  The only untested edges are those between
`z` and `N_D(z)`.

The colour `alpha` is absent from `phi_D(N_D(z))`.  If `z` has colour
`alpha`, the two colourings therefore glue.  Suppose `z` has a colour in
`Gamma`.  If (4.2) fails, some colour of `Gamma` is absent from
`phi_D(N_D(z))`: this uses `d_z<=3`, and also uses the fact that
`N_D(z)` is a clique.  Permute the three names in `Gamma` in the colouring
of `M_z`, sending the colour of `z` to an absent one.  The triangle colours
stay fixed and the two shore colourings again glue.

Consequently, when (4.2) fails, every six-colouring of `M_z` gives `z`
colour `beta` or `delta`.  If `rho_z=1`, the literal edge from `z` to its
pole lies in the corresponding path bag, so properness excludes that
bag's colour.  Thus `z` always copies the opposite pole bag, and that edge
is absent.  Adding it destroys every six-colouring.  Conversely, a
six-colouring of `M_z` followed by a fresh seventh colour on `z` colours
the augmented graph, proving (4.3).

If `rho_z=0`, the same argument says that `z` always copies one of the two
pole bags.  Hence adding both missing incidences destroys every
six-colouring.  At least one incidence is missing because `M_z` itself is
six-colourable.  Again a fresh seventh colour on `z` proves (4.4).
\(\square\)

For conclusion 2, the added edge is a critical edge of the exactly
seven-chromatic graph in (4.3).  In particular, after fixing a
six-colouring of `M_z`, `z` and `v_z` lie in one bichromatic component for
each of the other five colours.  For each of the three colours in
`Gamma`, the corresponding path in `M_z` has all internal vertices in
`C`; the other two triangle vertices have the colours of `k_z` and of the
pole bag different from `v_z`, and therefore cannot occur on it.

## 5. The all-rainbow row has thirty simultaneous Kempe connections

### Lemma 5.1 (global pole--triangle Kempe connections)

Suppose `z` is rainbow on `D`, and let `t_z^gamma` be the unique vertex of
`N_D(z)` having colour `gamma in Gamma`.  For each
`epsilon in {beta,delta}`, the vertex `t_z^gamma` lies in the
`epsilon`--`gamma` component of `phi_D` containing the pole of colour
`epsilon`.

#### Proof

Suppose not.  Interchange `epsilon` and `gamma` on the component containing
`t_z^gamma`.  The two pole colours and the colour on `Z` remain fixed, and
the altered triangle `N_D(z)` now omits `gamma`.

Fix any six-colouring of `M_z`.  Compared with the original rainbow
colouring `phi_D`, the colour of `z` cannot be `alpha`, `beta`, or `delta`,
because each of those colours is absent from `N_D(z)` and would permit the
two shores to glue.  Thus `z` has a colour in `Gamma`.  Permute the three
free colours on `M_z` so that `z` has colour `gamma`, and glue to the
altered `D`-colouring.  The crossing edges are now proper because the
triangle omits `gamma`, a contradiction. \(\square\)

Consequently, if all five centres are rainbow, then for each of the six
pairs

\[
                (\epsilon,\gamma)\in
                \{\beta,\delta\}\mathbin{\times}\Gamma,
\tag{5.1}
\]

one common bichromatic component contains the corresponding contact vertex
of every one of the five triangles.  These are thirty simultaneous,
literal pole--triangle incidences in one colouring; they are not five
unrelated transfer colourings.

### Theorem 5.2 (the global `t=5` split)

Under the standing hypotheses, one of the following holds.

1. Some proper transfer minor has one of the exact seven-chromatic
   completions (4.3)--(4.4).
2. Every centre is rainbow on `D`.  Then

   \[
                    d_z=3,\qquad c_z=5-\rho_z
                    \quad(z\in Z),                  \tag{5.2}
   \]

   and all thirty connections of Lemma 5.1 hold.  Moreover:

   * if `b>=3`, two rainbow centres `z,w` share one pole neighbour;
   * if `b=2`, the boundary incidence is exactly one `p`-only centre, one
     `q`-only centre, and three pole-free centres, all with rainbow
     `D`-contact triangles.

#### Proof

Apply Theorem 4.1 to all five centres in the one fixed colouring `phi_D`.
If its first conclusion fails anywhere, outcome 1 holds.  Otherwise every
centre has `d_z=3`; the degree identity gives (5.2), Lemma 5.1 gives the
connections, and the boundary assertions follow from (3.3). \(\square\)

In the `b>=3` subcase, let `T=N_D(z)` and choose the same-pole centre `w`.
Since `G-z` is six-connected, the fan lemma gives three paths from `w` to
the three vertices of `T`, pairwise disjoint except at `w`.  If `B_i` is
the `i`th arm with `w` deleted, then

\[
                         \{z\},\quad\{w\},\quad
                         B_1,B_2,B_3                 \tag{5.3}
\]

are five explicit pairwise adjacent connected branch sets except possibly
for `\{z\},\{w\}`.  Thus they form a `K_5^-` minor core, and the common pole
is adjacent to both singleton centre bags.  This is not yet a `K_7^-`
model: the fan need not avoid the two poles or the opposite shore, and two
disjoint completing branch sets meeting all three arms have not been
proved.

## 6. Exact remaining obstruction

The previous unrestricted `t=5` row is now replaced by two sharply
different mechanisms.

* In the critical-completion row, the missing edge or pair of edges is
  literal on a proper transfer minor, and the one-edge case carries a full
  critical-edge Kempe packet.  The missing geometric step is to realize
  one added incidence by changing the witness path or absorbing a
  `z`-contact component without destroying the three contracted branch
  sets.
* In the all-rainbow row, all five contact profiles, both pole-incidence
  possibilities, and all thirty bichromatic connections live in one
  colouring.  The remaining step is a pole-reserving simultaneous path
  packing.  The
  ordinary fan core (5.3) is unreserved and therefore nonterminal.

Thus neither an abstract palette count nor one more independent Kempe path
closes the row.  A terminal continuation must either realize one of the
critical-completion edges inside `G`, or extract two prescribed completing
branch sets from the common all-rainbow bichromatic connections.
