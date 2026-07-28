# Internal audit: density and low-degree rigidity under `K_7^-` exclusion

Audited file:
`results/hc7_k7minus_five_exceptional_vertices_reduction.md`.

Audited SHA-256:

```text
834b70c1a1ad076ad00a0468226788e33f6f7bab70590b67a629f0d33b5945ff
```

**Verdict:** **GREEN** for the exact revision above.

This is a separate internal mathematical audit, not external peer review.
The cold audit checked the theorem at the immediately preceding content
revision; the final revision changes only the status line and adds the
explicit reason that the remainder in one eight-vertex clique-union case is
nonempty.  Both changes were rechecked against the proof.

## 1. Dependencies and hypotheses

The audited local dependencies are:

| result | SHA-256 |
|---|---|
| degree-seven aligned near-`K_7` model | `51bd2cf191f848a398a1a4aee711ef0c4d36c747468ce9613b9514cbc56cd060` |
| degree-seven clique incidence | `8378b1920987284abf3ff33d476d28efee5c9a13659afe7a192febaacb3d501f` |
| at most two literal `K_5`s | `5b5e399122b996186e861f5075e7808c8e6fe4353082256ee12d5074499d2574` |

The displayed host hypotheses match all three inputs.  Exclusion of a
`K_7^-` minor also excludes a `K_7` minor.  Seven-chromaticity excludes the
two-apex case used by the three-clique theorem.

Jakobsen's threshold and cockade exception were checked in the form quoted
by Albar, Theorem 2 and Corollary 4.  Seven-connectivity excludes every
nontrivial four-sum cockade, while the two base graphs are at most
six-chromatic.  The strict threshold therefore gives

\[
                              2m\le9n-25.
\]

## 2. Exact degree-seven neighbourhoods

The aligned-model proof first classifies the complement of the
seven-vertex neighbourhood.  Its degree-two branch gives an explicit
`K_7^-` model; its earlier alternatives give `K_7`; and the only remaining
complements are `K_{3,4}` and `K_{3,3} dotcup K_1`.  Taking complements
gives exactly

\[
 K_4\mathbin{\dot\cup}K_3,
 \qquad
 K_1\vee(K_3\mathbin{\dot\cup}K_3).
\]

The first type has one literal `K_4`.  The second has two, sharing its
universal vertex.  Thus the asserted one- or two-`K_5` membership and the
two-vertex intersection in the latter case are exact.  The audit also
checked the important distinction that, in the two-clique type, the outside
triangle remains adjacent to the shared universal vertex; the proof does
not incorrectly call that triangle fully anticomplete to the chosen
clique.

## 3. Private-triangle capacity

If an all-degree-seven `K_5` met a second literal `K_5` through one of its
vertices, the local classification would make the intersection a
two-set.  Both shared vertices have all seven neighbours in the eight-vertex
union, while the two exclusive triples are anticomplete.  Six vertices then
separate the shared pair from any exterior.  With no exterior,
seven-connectivity forces `K_8`.  Both outcomes contradict the hypotheses.

The five clique vertices therefore have five pairwise disjoint private
external triangles, giving order at least twenty.  With four private
degree-seven vertices and one degree-`d` vertex, the four triangles occupy
twelve vertices and are anticomplete to the fifth vertex; its `d-4`
external neighbours are additional.  This verifies the bound `n>=d+13`.

## 4. Density and order arithmetic

At most two literal `K_5`s cover all degree-seven vertices, so `n_7<=10`.
With

\[
 s=\sum_{i\ge9}(i-8)n_i,
 \qquad q=n_7-s,
\]

degree summation gives the exact identity `2m=8n-q`.  Therefore
`m>=4n-5`.  Defining `epsilon=10-q` gives

\[
 2m=(8n-10)+\varepsilon,
 \qquad
 0\le\varepsilon\le n-15.
\]

Parity is exact because `epsilon` is the difference of two even integers.

The clique-overlap analysis for `n_7=8,9,10` is exhaustive.  In particular,
a shared degree-seven vertex forces clique intersection two; when both
shared vertices have degree seven, the two exclusive triples form a
six-cut.  The resulting bounds are

\[
 n_7=10\Rightarrow n\ge21,
 \quad
 n_7=9\Rightarrow n\ge20,
 \quad
 n_7=8\Rightarrow n\ge20.
\]

For `n<=18`, Jakobsen gives `epsilon<=3`; evenness reduces this to at most
two, which forces `n_7>=8` and contradicts the displayed bounds.  Hence
`n>=19`.

At order nineteen only `epsilon=4` remains.  The exact equation
`n_7-s=6` gives precisely `7^6 8^13` or `7^7 8^11 9^1`.  In the latter
case a private four-vertex low-degree set would force order at least
twenty-one, so one degree-seven vertex is shared.  The local classification
then forces intersection two; the second shared vertex cannot also have
degree seven because of the six-cut.  This verifies the stated residue.

## 5. The order-twenty equality construction

When `n_7=10` and `n=20`, the two all-degree-seven `K_5`s are disjoint.
Their private triangles partition the complement of either clique, so the
edges between the cliques form a perfect matching.  The audit checked that
the paired external edges form a perfect matching on the remaining ten
vertices and that every such vertex has exactly two clique neighbours.
Minimum degree seven therefore gives minimum degree five in the remainder,
which must be connected.

The five singleton vertices of the first clique, the second clique as one
branch set, and the connected remainder as one branch set are seven
pairwise adjacent connected sets.  This is an explicit `K_7` model, so the
order-twenty case is correctly excluded.

## 6. Exceptional vertices and trust boundary

The original exceptional-degree-eight count remains valid.  Jakobsen's
defect count and the ten-vertex union bound give at least five degree-eight
vertices in no literal `K_5`; five such vertices cannot be a clique, so two
are nonadjacent.

The result does not prove the `4n-5` extremal target, exclude the two
order-nineteen degree patterns, prove the five-exceptional-vertices target,
or prove either colouring conjecture.  The local proof depends on the
audited critical-host machinery and is not a theorem of bare
seven-connectivity.  No finite enumeration is a dependency.
