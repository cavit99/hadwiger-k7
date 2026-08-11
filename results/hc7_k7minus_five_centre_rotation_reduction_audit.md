# Internal audit: five-centre global rotation reduction

**Verdict:** GREEN.  A separate cold reading reconstructed the common-core
saturation theorem, all twenty rooted-model/web applications, the labelled
lift-order calculation, both corner classifications and the fixed-root
packet.  No unresolved mathematical gap was found within the stated scope.

This is internal mathematical review, not external peer review.

**Audited source:**
[`hc7_k7minus_five_centre_rotation_reduction.md`](hc7_k7minus_five_centre_rotation_reduction.md)

**Source SHA-256:**

```text
aff5e5a4c5900c4bc126df728126d7bf91db879123e9b16ac05285b5af5705b3
```

## 1. Common core and saturation

Independence and degree eight give

\[
 |E(F)|=|E(G)|-40\geq4|V(F)|-20>3|V(F)|-6,
\]

because `|V(F)|>=20`.  Thus `F` is nonplanar.  Deleting five vertices from
a seven-connected graph leaves it two-connected.  A five-colouring of `F`
would extend with one new colour on the independent set `Z`, so `chi(F)=6`.

Every six-colouring of `F` saturates some centre; otherwise independent
missing-colour choices extend it to `G`.  A colouring of `G-r` makes every
other centre unsaturated because its own colour is missing from its
neighbourhood.  The root `r` must be saturated or the colouring extends to
`G`.  Hence the singleton saturation identity is exact and invariant under
permuting colour names.

## 2. Ordered rooted-model/web applications

For `r ne z_i`, the four-set `U_i=Z-\{z_i\}` contains `r`, while
`H_i=G-U_i=F+z_i`.  The four singleton-colour neighbours of `r` lie in
`F`, so the audited four-centre theorem applies with the same literal
colouring and roots for all four values of `i` at fixed `r`.

In a web outcome, if `z_i` belongs to the facial three-set, deleting it
leaves a genuine two-cut of `F`.  Otherwise the exact cut restricts to a
proper order-three separation of `F`.  Every centre in `U_i` crosses it by
fullness and independence of `Z`; `z_i` does not cross because it belongs
to one original component.  The crossing set is therefore exactly
`Z-\{z_i\}`.  Deleting `z_i` may disconnect its shore, but the theorem only
requires a separation, so no connectedness is silently assumed.

## 3. Labelled uncrossing

The minimum lift of a separation of `F` consists of its ordinary separator
and precisely the crossing centres.  Independence of `Z` permits every
other centre to be assigned to one shore.  The ordinary order is modular,
each centre's crossing indicator is submodular, and equality in the total
forces equality centre by centre.

For anchor-compatible inputs, both corners are proper.  Seven-connectivity
and submodularity force lift order seven at both.  The three common centre
labels cross both corners; each omitted label crosses exactly one.  The
crossing counts are consequently `5,3` or `4,4`, giving ordinary orders
`2,4` or `3,3`.  Same-corner omitted labels therefore produce a genuine
two-cut; split labels are the exact surviving three-connected case.  No
boundary colouring is inferred.

If the two pairs of open shores have no perfect matching, their `2` by `2`
intersection graph has an isolated vertex.  The corresponding shore lies
inside the other three-vertex separator.  Its original exact-cut component
has order at most four.  The cited critical-host consequences exclude
orders one and two: minimum degree excludes one, while order two would put
the independent four-set `U_i` in a degree-eight neighbourhood, contrary to
the audited bound `alpha(N(v))<=3`.  Hence the component has order three or
four.

## 4. Fixed-root packet

Each set `A_i` is nonempty and supplies a literal extension colour on its
selected shore.  Intersecting `A_i,A_j` therefore give the claimed common
colour.  If the four sets are pairwise disjoint, they are the singleton
parts of the four-set `X_r`; all other roots must occupy the three-vertex
separator.  This proves the four exact boundary identities.

For the resulting maximal packet, call `i` internal when `z_i in C_i`.
An external selected component avoids `Z union X_r`; relative to every
other exact cut it must lie on the opposite side, because fullness gives an
edge to that cut's vertex `x_j`.  Hence it is disjoint from every other
selected component.  If at most one index were internal, fullness at `r`
would give four independent neighbours of `r`, contradicting
`alpha(N(r))<=3`.  There are therefore two internal indices `i,j`.

Fullness at `z_j` gives a vertex of `C_i cap C_j` outside `Z union X_r`.
The exact meet calculation then has separator

\[
                         Z\mathbin{\dot\cup}(X_r-\{x_i,x_j\}).
\]

The common vertex makes one open shore nonempty and `x_i,x_j` lie in the
other.  The order-seven two-component theorem makes this an exact full cut,
and deleting `Z` gives a two-cut of `F`.  Both omitted roots lie on the
opposite side and are the unique neighbours of `r` in two distinct colours,
so either colour extends the same literal colouring on the selected shore.
This proves Theorem 4.2 and eliminates the maximal packet when `F` is
three-connected.

For the two edges `rx_i,rx_j`, the two restorations create precisely the
two singleton monochromatic-edge signatures and agree away from `r`.  If
`x_ix_j` is absent, contraction of the induced path supplies the double
signature; if it is present, the retained chord makes that signature
impossible.  The empty signature would colour `G`.

With `theta=phi_r|F`, assigning one restoration colour `t` to all centres
is proper exactly when `t` lies in every missing-colour set
`[6]-theta(N(z))` for `z ne r`.  The other two singleton representatives
are distinct and avoid `t`, proving the exact normalization criterion.
The two unnormalised boundary partitions agree exactly when neither
restoration colour occurs on `Q-r`, since the colourings differ there only
at `r`.

## 5. Citation and limits

The parameter check against Lafferty--Liu--Rolek--Yu, Theorem 1.6, is
correct: the smallest permitted `t=3` and `s=7` require `k>=8`.  It does
not treat the seven-contraction-critical host or the three-connected
rotation problem.

The source correctly leaves open rooted-model completion, composition of
the five fixed-root rooted/common-trace alternatives, simultaneous
normalization of the coupled operations, the order-at-least-eight two-cut
branch, Conjecture 21 and `HC_7`.  The maximal incompatible packet itself is
proved to return to the two-cut branch and is not listed as a surviving
three-connected obstruction.
