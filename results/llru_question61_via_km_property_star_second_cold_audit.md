# Second cold audit: LLRU Question 6.1 via property `(*)`

**Source audited:** `llru_question61_via_km_property_star.md`  
**SHA-256:** `8cac1bbffdc41825c6934921b4f778eea60a593615e4ae5e1ce5fe2606cf3797`  
**Verdict:** GREEN.  This is an independent proof audit, not external peer
review.  The result does not by itself prove `HC_7` or close the induced
`C_7` true-twin residue.

## Core theorem

Contracting every component of each input packet `V_i` gives a quotient
with a proper five-colouring and root transversal `t_1,...,t_5`.  A supplied
`v_i`--`v_j` path inside `V_i union V_j` maps to a two-coloured root walk,
and hence a path, in the quotient.  It is needed only when `v_iv_j` is not a
literal edge.

Let `L` be the literal graph on the five roots and put `K=overline L`.
The hypothesis `e(L)>=4` gives `e(K)<=6`.  Kriesell--Mohr Theorem 7 applies
because Definition 1 requires only that `K` be a *spanning subgraph* of the
routing graph.  Its certificate supplies all `K`-contacts.  Every remaining
pair is a literal root edge, which survives between the two root-component
vertices and supplies that bag contact.  Expanding quotient vertices back
to their connected packet components preserves disjointness, connectivity,
roots, and contacts.  This proves the strengthened theorem in which routing
is assumed only for nonliteral pairs.

If the literal graph has independence number at most two, its complement is
triangle-free and has at most six edges by the five-vertex Mantel bound.
Thus the theorem answers Lafferty--Liu--Rolek--Yu Question 6.1 exactly (and
also covers `alpha<2`).  Their sentence immediately after Question 6.1
states the direct consequence: eight-connectivity of
`k`-contraction-critical graphs for `k>=11`, improving their displayed
threshold `k>=17`.

## Source semantics

The imported statements match their primary sources:

* Kriesell--Mohr, arXiv:1911.09998v2, Definition 1 and Theorem 7: a
  five-vertex graph with at most six edges has property `(*)`, with the
  spanning-subgraph semantics used above.  Their Corollary 1 uses the same
  complement-demand plus literal-edge completion.
* Lafferty--Liu--Rolek--Yu, arXiv:2509.07144v1, Question 6.1: output bags
  need only be disjoint, connected, rooted, and pairwise adjacent; they are
  not required to stay inside their original packets.  Colour mixing in a
  property-`(*)` certificate is therefore legal.
* Rolek--Song, JCTB 127 (2017), Lemma 1.7 and its proof, with `k=7,s=1`:
  after contracting `S union {x}` to the colour-one vertex, the five roots
  in `R=N(x)-S` receive distinct colours `2,...,6`, and every missing root
  pair has the required bichromatic path with internal vertices outside
  `N[x]`.  Taking the five colour classes as packets is valid; the
  colour-one contracted vertex is unused, so deletion/lifting is exact.

## Singleton true-twin bag

In the induced-`C_7` application, the five roots are `b` and the four cycle
vertices outside an independent triple.  The twin `b` is literal-adjacent
to the other four roots, hence isolated in the complement demand graph.
Given a property-`(*)` certificate, replace only its bag rooted at `b` by
the singleton `{b}`.  This loses no demanded contact because the demand
vertex is isolated.  It does not alter the other four bags, their
connectivity, or their mutual certificate contacts.  The four literal
`b`--root edges then join `{b}` to all four bags.  Thus the claimed rooted
`K_4` on the cycle roots, disjoint from `{b}`, follows without assuming
colour-preserving certificate bags.

For a chosen `s` in the deleted independent triple, adding `{a},{s},{b}`
leaves only the two possible contacts from `{s}` to bags rooted at its two
cycle nonneighbours.  One such contact gives `K_7^-`; target-freeness forces
both to be absent.  Absorbing all unused components into the four rooted
bags is safe in the connected remainder and yields the displayed spanning
two-bag neighbourhood concentrations.  This is a genuine sharper normal
form, but neither property `(*)` nor Rolek--Song supplies the missing
contact, so the proof correctly stops short of closing the seam.

## Priority boundary

The argument is a new application of Kriesell--Mohr's existing
complement-certificate machinery.  It should not be described as new
rooted-minor machinery, and later versions/citations and both author groups
should be checked before a priority claim.
