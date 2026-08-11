# Hash-pinned internal audit of the `b=2` Hall-rectangle theorem

Audited file:
`active/hc7_k7minus_five_centre_b2_rectangle_locks.md`

Audited SHA-256:

```text
8843b2c86dbf6ccc6555fd198246c5c9f8a85ffa9ffc69b67f6e40a58d0e3674
```

**Verdict:** **GREEN** for every stated Hall, recolouring, Kempe-component,
and rooted-minor conclusion at this revision.

This is a hash-pinned internal mathematical audit, not external peer review.
It verifies the reduction and its stated nonclosure; it does not prove that
the all-rainbow `b=2` row, the five-centre two-cut branch, or the
`K_7^-` six-colour conjecture is closed.

## 1. Audited dependencies and hypothesis match

The exact dependency revisions used by the note are:

| input | source SHA-256 |
|---|---|
| global five-root palette alternative | `b26f9f0d12822f93af55e3aa566fc75b985dcb5a17daa4ea2b329c8efea274c3` |
| contraction-colouring gluing theorem | `591a284e71266eb51fbbd2cd42e2c6e2245bb1bde69884eddd1b7c19d09caa41` |
| degree-seven theorem containing the Kriesell--Mohr conversion | `04e085032a096ef3fd508ca4ee287ef82417a718ae3d95646ae4cbd0b911ed2e` |

The global five-root theorem gives exactly the data used here.  In the
all-rainbow `b=2` row there is one centre incident only with `p`, one
incident only with `q`, and three pole-free centres.  The two incident
centres have profile `(4,3,1)`, and their three `D`-contacts are literal
triangles.  Consequently

\[
 T=(Z-\{z_p,z_q\})\cup\{p,q\}
\]

is independent.  Pointwise fullness of the two components makes both
closed sides in (1.3) connected.  Since `C,D` are different components of
`G-S`, the only edges between the two open sides are the four
`C`-incidences of each of `z_p,z_q`, exactly eight edges.

## 2. Hall calculation and the common rectangle

For a deficient set of `k` columns in the complementary `5 by 5`
bipartite graph, the forbidden relation contains at least

\[
                         k(6-k)
\]

positions.  The values for `k=1,2,3,4,5` are `5,8,9,8,5`.
This proves the exact full-line or `2 by 4`/`4 by 2` classification under
an eight-position bound, including its converse.

The contraction colourings make `T` monochromatic in a colour `gamma` and
make every crossing endpoint avoid that colour.  After erasing either
incident centre, its remaining neighbours on the right closed side are
its `gamma`-coloured pole and a rainbow triangle.  It therefore has at
least two available colours among the other five.  Two sets of order at
least two have distinct representatives, so the centres can first be
given distinct colours.

The resulting forbidden relation uses only those two rows, with at most
four positions in each.  A full row and a full column are impossible.
The only Hall defect is therefore the exact `2 by 4` rectangle.  Equality
in the edge count forces both four-vertex `C`-contact sets to be rainbow on
one common four-set `Q`.  No multiplicity or unrepresented crossing edge is
lost in this inference.

## 3. Available lists and the Kempe interchange

For an incident centre `z_x`, its available nonboundary list is

\[
 L_x=\Omega-\phi_R(T_x).
\]

The literal triangle has either three non-`gamma` colours, giving list
order two, or `gamma` and two other colours, giving list order three.  If
the two lists met, assigning their common colour to both nonadjacent
centres would collapse the forbidden relation to one row on the four
columns `Q`; the gluing permutation would exist.  Thus the lists are
disjoint, and complements in the five-set `Omega` give exactly the
`(2,3)` and `(2,2)` palettes displayed in (3.5)--(3.6).

For `a\in L_p,b\in L_q`, disjointness makes `a` occur uniquely on `T_q`
and `b` occur uniquely on `T_p`.  The audit checks the Kempe interchange in
the graph with the two centres deleted.  If the two named contacts were in
different `a`--`b` components, swapping the component of the `T_q`
contact would replace only `a` by `b` on `T_q`; it cannot change `T_p`,
because `a` is absent there and the unique `b`-contact was assumed to lie
in the other component.  The new list at `z_q` is exactly

\[
                         (L_q-\{b\})\cup\{a\},
\]

while the list at `z_p` is unchanged and already contains `a`.  Both
centres can then be assigned `a`, and the one-row gluing contradiction
applies.

All boundary vertices in `T` have colour `gamma`, while `a,b` differ from
`gamma`.  Hence the forced bichromatic component contains no boundary
vertex.  Its named path, including its interior, is wholly contained in
`D`.  This verifies both the path location and the use of one fixed
contraction colouring.

## 4. Rooted-minor conversion and confinement

In the unequal-list case, the five non-`gamma` contact vertices have the
five distinct colours in `Omega`.  After deleting the `gamma` colour
class, they form a five-colour transversal in a subgraph of `D`.  The six
cross-list pairs form a `K_{2,3}` demand graph.  The Kriesell--Mohr theorem
for five-vertex demand graphs with at most six edges therefore gives five
disjoint connected rooted bags inside this subgraph.  Lemma 4.1 supplies
the six demanded contacts, and the literal `K_2` and `K_3` inside the two
contact triangles supply the remaining four.  The model is consequently
a `D`-confined rooted `K_5` model.

In the equal-list case, the four cross-list roots and either triangle's
`h`-root again form a five-colour transversal after deletion of the
`gamma` class.  Applying the same theorem to the four-edge `K_{2,2}`
demand graph is legitimate even though the fifth demand vertex is
isolated.  Discarding its rooted bag leaves a rooted `K_4`: four demanded
cross contacts and the two literal within-pair edges give all six
adjacencies.  Retaining the fifth bag adds its two literal triangle
contacts, leaving at most the two adjacencies to the opposite pair absent.

The certificate bags cannot leave `D`: the conversion is applied only
after restricting to the five non-`gamma` colour classes in `D`, and every
required bichromatic path was already proved to lie in `D`.

## 5. Scope and unresolved completion

The final limitation is accurate.  In the `(2,3)` row the two centres see
complementary three- and two-element subsets of the five rooted bags; they
are not two universal completing branch sets.  In the `(2,2)` row the
fifth rooted bag may miss both bags of the opposite pair.  Neither output
alone is a seven-bag model with at most one absent adjacency.

No unresolved assumption or inference remains inside the theorem as
stated.  The unresolved task is the additional graph-structural allocation
needed to complete one of these rooted cores, not another Hall or palette
calculation.
