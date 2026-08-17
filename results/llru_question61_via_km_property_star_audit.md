# Cold audit: partial five-root routing from Kriesell--Mohr property `(*)`

**Audited file:** `llru_question61_via_km_property_star.md`

**Audited SHA-256:**
`8cac1bbffdc41825c6934921b4f778eea60a593615e4ae5e1ce5fe2606cf3797`

**Verdict:** GREEN for Theorem 1.1, Corollary 1.2 and Corollary 5.1,
subject only to the explicit singleton-`b` justification recorded below.
This audit verifies a rooted-minor theorem and its published
contraction-critical consequence.  It does not prove `HC_7`, the
`K_7^-` six-colour conjecture, or close the induced-`C_7` twin residue.

## 1. Statements audited

The partial-routing theorem says the following.  Let `v_1,...,v_5` be
five roots spanning at least four literal edges.  Let `V_1,...,V_5` be
pairwise disjoint vertex sets with `v_i in V_i`.  If, for every
nonliteral root pair `v_iv_j`, there is a `v_i`--`v_j` path in
`G[V_i union V_j]`, then `G` has a `K_5` minor rooted at the five roots.

The Lafferty--Liu--Rolek--Yu corollary replaces the four-edge hypothesis
by `alpha(G[{v_1,...,v_5}])<=2` and assumes all pairwise two-packet
paths.

The degree-eight handoff says the following.  In a
seven-contraction-critical graph, let `d(x)=8`,
`alpha(G[N(x)])=3`, let `S subseteq N(x)` be an independent triple, and
put `R=N(x)-S`.  If `e(G[R])>=4`, then
`G-(S union {x})` has an `R`-rooted `K_5` minor.

## 2. Primary-source verification

The exact Kriesell--Mohr source is Matthias Kriesell and Samuel Mohr,
*Kempe Chains and Rooted Minors*, arXiv:1911.09998v2 (29 November
2022).

* Definition 1 says that a graph `K` has property `(*)` if, whenever an
  isomorphic copy of `K` is a spanning subgraph of the routing graph of
  a coloured graph and a transversal, the coloured graph has the
  corresponding rooted certificate.
* Theorem 7 says that every graph on five vertices with at most six
  edges has property `(*)`.
* Corollary 1 uses exactly the same complement mechanism: missing
  literal root edges are supplied by a property-`(*)` certificate and
  literal root edges supply the remaining bag contacts.

The exact Rolek--Song source is Martin Rolek and Zi-Xia Song,
*Coloring graphs with forbidden minors*, Journal of Combinatorial
Theory, Series B 127 (2017), 14--31, Lemma 1.7.

With their parameters `k=7,s=1`, the hypotheses are precisely
`d(x)=k+s=8`, `alpha(G[N(x)])=s+2=3`, and an independent set
`S` of order `s+2=3`.  Their proof contracts `S union {x}` to a vertex
`w`, six-colours the proper minor with `c(w)=1`, and proves that the five
vertices in `R=N(x)-S` receive the five distinct colours `2,...,6`.
For each nominated missing edge `uv` in `G[R]`, proof lines corresponding
to the paragraph after Lemma 1.7 construct a `u`--`v` path in the
`c(u),c(v)` bichromatic subgraph, with every internal vertex outside
`N[x]`.  The bichromatic containment needed by the partial-routing
theorem is therefore present in the proof, even though the displayed
statement of Lemma 1.7 records only the stronger path-location and
disjointness consequences.

The question source is Michael Lafferty, Runrun Liu, Martin Rolek and
Gexin Yu, *Connectivity of contraction-critical graphs*,
arXiv:2509.07144v1, Question 6.1.  The question does not require the
output bag rooted at `v_i` to remain inside the input set `V_i`.  The
colour mixing permitted by a property-`(*)` certificate is therefore
legal.  The sentence immediately following the question states that an
affirmative answer improves their eight-connectivity threshold for
`k`-contraction-critical graphs from `k>=17` to `k>=11`.

## 3. Line-by-line proof audit

1. Contracting each connected component of each `G[V_i]` produces a
   simple quotient with a proper five-colouring.  Two different
   components carrying the same colour cannot have an edge between
   them, since then they were not different components.
2. A prescribed path in `G[V_i union V_j]` maps to a walk using only
   quotient colours `i,j`; erasing closed portions gives a bichromatic
   path between the two root components.  Hence every nonliteral root
   pair is an edge of the routing graph.
3. If `R_0` is the literal graph on the five roots, then
   `K=overline{R_0}` has at most `10-4=6` edges and is a spanning
   subgraph of the routing graph.  Kriesell--Mohr Theorem 7 and
   Definition 1 therefore give disjoint connected bags supplying every
   `K`-edge.
4. A pair not in `K` is a literal root edge.  That edge survives between
   the two root-component quotient vertices, which lie in their
   respective certificate bags.  Thus it supplies every remaining
   bag adjacency, and the quotient bags form a rooted `K_5` model.
5. Replacing a quotient vertex by the connected monochromatic component
   it represents preserves bag disjointness, connectivity, every bag
   adjacency, and the nominated root.  The contraction lift is exact.
6. If the literal root graph has independence number at most two, its
   complement is triangle-free.  Mantel's five-vertex bound gives at
   most six complement edges, equivalently at least four literal edges.
   This proves the stated answer to Question 6.1.
7. For the Rolek--Song handoff, take the five colour classes
   `c^{-1}(2),...,c^{-1}(6)` as the five packets.  The five roots in `R`
   lie in distinct packets, and the Rolek--Song bichromatic path for
   each missing root edge lies in the required packet pair.  Since
   `e(G[R])>=4`, the partial-routing theorem applies.
8. The contracted vertex `w` has colour one and is in none of the five
   packets.  Deleting `w` from the contracted graph is exactly the
   deletion of `S union {x}` before contraction.  All other vertices
   are unchanged by the contraction, so the rooted model lifts to
   `G-(S union {x})` without a hidden branch vertex.

No quotient-colouring, complement, certificate, or lifting error occurs
in these steps.

## 4. The singleton-`b` point and exact repair

In the induced-`C_7` true-twin application, `R` consists of the twin `b`
and four cycle vertices.  The vertex `b` is literal-adjacent to all four
other roots, so it is isolated in the complement demand graph.

It is correct that the rooted model may be chosen with the `b`-bag equal
to the singleton `{b}`, but this requires one explicit postprocessing
step.  The demand graph used in Theorem 7 is the complement of the literal
root graph, so `b` is isolated in that demand graph.  Start with the five
certificate bags returned by property `(*)` and replace the bag rooted at
`b` by `{b}`.  No required certificate adjacency is lost, because none is
incident with the isolated demand vertex.  The other four bags are
unchanged and remain disjoint, connected, and mutually adjacent after
literal-edge completion.  Finally, the four literal edges from `b` to the
other roots join `{b}` to all four bags.  This returns a rooted `K_4` model
on the four cycle roots plus the singleton bag `{b}` without importing an
additional theorem or assuming that property `(*)` preserves colours.

## 5. Exact `C_7` consequence and nonclosure

Let `a,b` be the adjacent true twins and let their external common
neighbourhood be an induced `C_7`.  For any independent triple `S` on
the cycle, apply the repaired handoff with `x=a`.  Adding `{a}` to the
rooted four-cycle-vertex model and `{b}` gives a `K_6` model.

For `s in S`, both cycle neighbours of `s` lie outside `S`.  Hence the
seven bags consisting of `{a}`, `{s}`, `{b}`, and the four rooted cycle
bags have every contact except possibly the two contacts from `{s}` to
the two bags rooted at its cycle nonneighbours outside `S`.  If either
of those contacts exists, the bags form a `K_7^-` model.

Thus a target-free graph must, for every independent triple and every
chosen `s`, admit the Rolek--Song/Kriesell--Mohr model only in the
two-opposite-bag avoidance profile.  Neither property `(*)` nor Lemma 1.7
forces an additional contact.  This is a strict sharpening of the pure
`C_7` connector obstruction, not its elimination.

## 6. Release assessment

The answer to Lafferty--Liu--Rolek--Yu Question 6.1 and the stated
`k>=11` contraction-critical connectivity consequence are rigorous
applications of existing Kriesell--Mohr machinery.  The appropriate
priority description is a new observation/application, not new
property-`(*)` machinery.  Before public priority claims, later versions
and citations of both source papers should be checked and the two author
groups notified.

The result is broad and publishable as a short note or communicated
observation, but it does not meet the Norin--Totschnig campaign benchmark
and must not be entered as a solution of the primary conjecture.
