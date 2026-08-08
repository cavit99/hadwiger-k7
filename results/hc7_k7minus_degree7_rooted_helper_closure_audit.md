# Internal audit: degree-seven rooted-helper closure

**Verdict:** GREEN.

**Audited theorem:**
[`hc7_k7minus_degree7_rooted_helper_closure.md`](hc7_k7minus_degree7_rooted_helper_closure.md)

**Audited SHA-256:**
`6ffee04cf9ff66275f9674c24bc2b9c669b1e108b76e5b1d2a18ec7d0106fe67`

This is an internal mathematical audit, not external peer review.  The proof
is computation-free.

## 1. Rooted input

Norin--Totschnig, Lemma 12, was checked against the cited source.  Its exact
contrapositive is the one used in the theorem: an internally
four-connected pair `(F,Z)`, with `|Z|=4` and

\[
                         |E(F)|\ge4|V(F)|-9,
\]

has a `Z`-rooted `K^*_{4,2}` model.  The target has two adjacent helper
bags, each adjacent to all four root bags; it does not require adjacency
between distinct root bags.

Lemma 1 restates the existing fifth-root augmentation and includes its proof.
The optimisation is finite.  For a selected root bag, distinct contacts to
the two helpers can be chosen whenever their union has order at least two;
otherwise the two contact sets are the same singleton.  Moving the nominated
leaf preserves both helper contacts and both altered bags' connectivity.
Consequently the helper union has at most four external neighbours.  If the
fifth root were outside it, those neighbours would be a separator of order at
most four with all five roots on the opposite side.  This is exactly excluded
by internal five-connectivity.

## 2. Connectivity and density in Theorem 2

Deleting one vertex from a six-connected graph leaves a five-connected graph:
removing at most four further vertices deletes at most five vertices from the
original graph.  Hence both rooted-connectivity hypotheses used in the proof
hold.  No completion of the four roots is needed for connectivity.

If `d_G(v)=d`, then deleting `v` removes exactly `d` edges.  The numerical
hypothesis gives

\[
 |E(G-v)|\ge(4n+d-13)-d=4n-13=4|V(G-v)|-9.
\]

Thus the sharp rooted threshold is met with no omitted edge or hidden
rounding assumption.

The branch-set assembly was checked literally.  The four edges between every
pair of roots in the nominated `K_4` join the four distinct root bags.  The
root bags and two helpers are therefore six pairwise adjacent connected bags.
The singleton `{v}` meets the four root bags and the helper containing the
fifth neighbour `x`; only its contact with the other helper may be absent.
There is exactly one permitted missing pair.

## 3. Critical-host corollary

Under the displayed critical-host hypotheses, the cited clique-incidence
theorem gives a literal `K_5` through every degree-seven vertex, so its
neighbourhood contains the required `K_4`.  The cited density theorem gives
`|E(G)|>=4|V(G)|-2`, while Theorem 2 needs only `4|V(G)|-6` at degree seven.
The contradiction therefore eliminates all degree-seven vertices without
using a safe contraction or a separator reduction.

Seven-connectivity then gives minimum degree at least eight, and the
handshake lemma gives `|E(G)|>=4|V(G)|`.  Write the edge surplus over this
last bound as `q`.  If a literal `K_5` existed, Theorem 2 applied at each of
its five vertices would force each such vertex to have degree at least
`q+14`.  Those five vertices alone would contribute at least `5(q+6)` to
the total degree-above-eight surplus, whereas the exact total surplus is
only `2q`.  This is impossible for `q>=0`.

The separately audited Jakobsen defect inequality is

\[
 25\le2n_7+n_8-\sum_{i\ge10}(i-9)n_i.
\]

Substituting the proved equality `n_7=0` gives the stated lower bound on
`n_8`.  Since the host has no literal `K_5`, every degree-eight
neighbourhood is `K_4`-free.  The meaning of “exceptional” in the repository
is exactly this condition.

## 4. Scope

No unresolved inference occurs in the theorem or corollary.  The result does
not eliminate the surviving literal-`K_5`-free, minimum-degree-eight
critical-host branch and does not prove the bare seven-connected `4n-2`
extremal theorem.
