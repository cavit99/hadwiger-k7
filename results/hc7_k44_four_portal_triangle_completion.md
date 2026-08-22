# Four-portal triangle completion over a literal `K_{4,4}`

**Status.** Proved computer-assisted local completion lemma, with a
separate independent exhaustive verifier and a human-checkable ten-orbit
fallback table.  This is a side result.  It does **not** prove
Norin--Totschnig Conjecture 21, eliminate the whole literal-`K_{4,4}`
branch, or meet the campaign's major-theorem benchmark.

Write `K_7^-` for the graph obtained from `K_7` by deleting one edge.

## Theorem (four-portal triangle completion)

Let `G` be a finite simple graph.  Suppose that `G` contains a specified
literal copy `H` of `K_{4,4}` with shores

\[
 A=\{0,1,2,3\},\qquad B=\{4,5,6,7\},
\]

and three distinct vertices `x,y,z` outside `H` which induce, or merely
contain, the triangle `xyzx`.  If

\[
 |N_G(x)\cap V(H)|,\ |N_G(y)\cap V(H)|,\
 |N_G(z)\cap V(H)|\ \ge 4,                 \tag{1}
\]

then `G` contains a `K_7^-` minor.

No inducedness is required for `H`, and edges from the displayed eleven
vertices to the rest of `G` are unrestricted.

## Finite core lemma

For a portal `p in {x,y,z}`, put

\[
                         M_p=V(H)-N_G(p).                \tag{2}
\]

Thus `|M_p|<=4`.  For every unordered triple
`(M_x,M_y,M_z)` satisfying this bound, at least one of the following holds.

1. There is a four-bag `K_4` minor model `B_1,B_2,B_3,B_4` in `H` such
   that among the twelve portal--bag pairs

   \[
      (p,B_i),\qquad p\in\{x,y,z\},\quad 1\le i\le4,
   \]

   at most one is nonadjacent.
2. After an automorphism of `H` and a permutation of `x,y,z`, the missed
   triple is one of the ten rows in Table 1.  The seven branch sets in that
   row form a `K_7^-` model directly.

Here a portal `p` is adjacent to a core bag `B_i` exactly when
`B_i` is not contained in `M_p`.

### Table 1. The ten exceptional core-profile orbits

In the table, the vertices `8,9,10` mean `x,y,z`, respectively.  Every
displayed branch set is connected, the seven sets are pairwise disjoint,
and every pair is adjacent except possibly the pair in the last column.

| row | orbit size | `(M_x,M_y,M_z)` | seven branch sets | possible missing pair |
|---:|---:|---|---|---|
| 1 | 36 | `((0,1),(2,3,4,5),(2,3,6,7))` | `(0,4,z),(1,5),(2,6),(3),(7),(x),(y)` | `(3),(y)` |
| 2 | 72 | `((0,1,2),(0,3,4,5),(0,3,6,7))` | `(0,4,z),(1,5),(2,6),(3),(7),(x),(y)` | `(3),(y)` |
| 3 | 36 | `((0,1,2,3),(0,1,4,5),(0,1,6,7))` | `(0,4,z),(1,6),(2,5),(3),(7),(x),(y)` | `(3),(x)` |
| 4 | 144 | `((0,1,2,4),(0,1,3,5),(0,1,6,7))` | `(0,1,4),(3,6),(5,x),(2),(7),(y),(z)` | `(7),(z)` |
| 5 | 288 | `((0,1,2,4),(0,3,4,5),(0,3,6,7))` | `(0,4,z),(1,5),(2,6),(3),(7),(x),(y)` | `(3),(y)` |
| 6 | 144 | `((0,1,2,4),(0,3,4,5),(0,4,6,7))` | `(0,1,4),(3,6),(5,x),(2),(7),(y),(z)` | `(7),(z)` |
| 7 | 144 | `((0,1,4),(2,3,4,5),(2,3,6,7))` | `(0,4,z),(1,5),(2,6),(3),(7),(x),(y)` | `(3),(y)` |
| 8 | 36 | `((0,1,4,5),(0,1,6,7),(2,3,4,5))` | `(0,4),(1,5),(2,6),(3,x),(7),(y),(z)` | `(7),(y)` |
| 9 | 144 | `((0,1,4,5),(0,1,6,7),(2,3,4,6))` | `(0,4,y),(1,6),(2,5),(3),(7),(x),(z)` | `(3),(z)` |
| 10 | 96 | `((0,1,4,5),(0,2,4,6),(0,3,4,7))` | `(0,5,6),(1,z),(3,4),(2),(7),(x),(y)` | `(2),(y)` |

The orbit sizes sum to `1,140`.

## Proof of the finite core lemma

There are

\[
                  \sum_{i=4}^{8}\binom8i=163            \tag{3}
\]

possible portal neighbourhoods in `H`.  Since the three portals form a
triangle and may be permuted, there are

\[
                       \binom{163+3-1}{3}=735{,}130      \tag{4}
\]

unordered profiles.

The primary verifier enumerates every four-bag `K_4` minor model in `H`.
Unused core vertices are allowed.  It finds `1,656` distinct bag families.
For each one of the `163` neighbourhood masks it records, as bitsets, the
models which miss zero bags and the models which miss exactly one bag.
Four bitset intersections then test whether a common model has at most one
miss over the three portals.  Of the `735,130` profiles, `733,990` pass
this test and `1,140` remain.

The primary exact fallback independently searches all seven-bag models in
the eleven-vertex graph for each of those `1,140` profiles.  It finds a
model in every profile and no negative profile.  During those positive
searches it examines `8,601,313` candidate models before the first witness
for each profile is found.

For a shorter check of the positive fallback, the separate orbit verifier
regenerates the core calculation without importing either primary
enumerator.  It assigns each of the eight core vertices independently to
one of four labelled bags or to an unused class, so its universe is the
explicit `5^8` assignments.  It tests nonemptiness, connectivity, and all
six bag contacts, removes the four-bag label symmetry, and again obtains
exactly `1,656` core models and exactly `1,140` failed profiles.  It then
acts by

\[
             \operatorname{Aut}(K_{4,4})
             \cong (S_4\times S_4)\rtimes C_2           \tag{5}
\]

and by the `S_3` symmetry of the portal triangle.  Exactly ten orbits
remain, with sizes

\[
 36,36,36,72,96,144,144,144,144,288.                   \tag{6}
\]

Their canonical representatives are precisely the ten rows of Table 1.
The same verifier checks the displayed fixed branch sets directly.  Thus
every remaining profile is carried by the symmetries to a row with an
explicit `K_7^-` model.  This proves the finite core lemma.  \(\square\)

## Proof of the theorem

Apply the finite core lemma to the three missed sets in (2).

In outcome 1, use the seven branch sets

\[
                 B_1,B_2,B_3,B_4,\{x\},\{y\},\{z\}.    \tag{7}
\]

The first four form a clique minor, contributing six pairwise contacts.
The last three are a triangle, contributing three.  Of the twelve
cross-contacts, at least eleven are present.  Hence the quotient on the
seven branch sets has at least

\[
                             6+3+11=20                  \tag{8}
\]

edges, and therefore contains `K_7^-`.

In outcome 2, take the seven branch sets displayed in the appropriate row
of Table 1.  They are connected and disjoint, and their quotient has at
least twenty of the twenty-one possible edges.  They again give a
`K_7^-` minor.

All used edges lie in the displayed copy of `H`, the portal triangle, and
the portal--`H` edges.  Additional vertices or edges of `G` cannot destroy
the model, so the construction is an unbounded host-level lift rather than
an assertion restricted to eleven-vertex graphs.  \(\square\)

## Reproduction and trust boundary

From the repository root run

```text
python3 results/hc7_k44_four_portal_triangle_completion_verify.py
```

The expected terminal summary is

```text
core_models 1656
fallback_profiles 1140
orbits 10
orbit_sizes [36, 36, 36, 72, 96, 144, 144, 144, 144, 288]
sha256 755316af73023902cbe205ec2f0b914b25677a61a5fb77dc129567a46fe6f552
all_ten_certificates_valid
```

The finite trust boundary is the Python interpreter, exact integer bit
operations, the stated exhaustive loops, and the retained verifier.  The ten
final models are also inspectable directly from Table 1.  This cold audit is
an internal independent audit, not external peer review.

## Scope and immediate consequence

The theorem terminalises any literal-`K_{4,4}` configuration whose
connected exterior contains a triangle all three of whose vertices have
at least four neighbours on the core.  In particular, in a
`K_7^-`-minor-free host, every exterior triangle has a vertex with at most
three core neighbours.

It does not show that a three-connected exterior contains such a triangle,
nor does it reconstruct a literal core from an arbitrary `K_{4,4}` minor.
Those are separate unresolved steps.
