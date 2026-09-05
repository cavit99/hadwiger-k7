# Audit: expanding separator roots

**Status:** separate internal mathematical audit, 5 September 2026.
This is an internal agent audit, not external peer review.

**Audited source:** [the theorem and planar construction](hc7_k44_expanding_separator_roots.md),
whole-file SHA256
`239cf15baa7d513c292f6b7f50d232ff432989cceaef5c1913d80121ff52e68e`.

**Verdict: GREEN** for the equal-three-contact theorem with `|R|>=2`
and the counterexample to the stated local rooted-allocation inference.
No unresolved mathematical gap was found in either statement. Neither
statement closes the whole singleton residue or proves T44.

## Positive theorem: exact connectivity and ownership

The [Norin--Totschnig primary statement](https://arxiv.org/html/2507.03244v1)
was inspected at its definition preceding Observation 7 and at Lemma 10.
Internal four-connectivity excludes separations of order at most three
whose first closed side contains all four roots and whose other open
side is nonempty. Lemma 10 additionally requires at least six vertices
and concludes a model rooted at all four named vertices. The source
uses exactly this statement; the omitted edge of the resulting
`K_4^-` is not assumed to have prescribed ends.

For `F=G[R union {a,p,x,y}]`, any such other open side `W` is a subset
of `R`. Its neighbours outside `F` belong to the three vertices of
`C`: no edge joins the distinct open components `R,D` of `G-E`.
Thus its neighbourhood in `G` is contained in a set of order at most
six. Among the four roots of `F`, at least one is outside this set
and outside `W`. Removing the set disconnects this root from the
nonempty set `W`, contradicting seven-connectivity. This argument
checks nontrivial separation on both sides, including when `W=R`.
The hypothesis `|R|>=2` gives the required order of `F`.

The obtained four branch sets contain exactly one of `a,p,x,y` each.
They lie in `R union {a,p,x,y}`. The fixed five rooted clique bags lie
in `D union T`. Hence the only intersections between the two families
are the prescribed vertices `x,y`, lying in the correspondingly named
bags. The unions at those vertices are connected and preserve all
original contacts. The other five final bags remain disjoint from
these unions and from one another.

There are ten contacts between the five enlarged `T` bags, one between
the `a,p` bags from the actual edge `ap`, six from those two roots to
the three `C` bags, and at least three to the other two `T` bags from
the four-root model. These are different pairs of bags. Thus at most
one of the 21 possible contacts is absent. No rooting, endpoint-degree,
colouring or branch-set ownership is silently transferred to a new
induction instance; this is a direct minor construction. The excluded
case `|R|=1` is not covered by the cited order hypothesis.

## Planar construction: boundary and arbitrary expansion

The wheel together with the five roots can be embedded by placing each
`q_i` outside its rim edge. The four added root edges leave a face with
boundary

```text
a, p, r_2, t_0, t_1, t_2, a.
```

In particular the five specified roots occur on a single simple facial
cycle in the claimed order. The boundary counts in the source cover
all nonempty subsets of the six wheel vertices: hub present with zero,
one through four, or five rim vertices; and hub absent with one, two,
or at least three rim vertices. In each case there are at least five
distinct external neighbours in the wheel-plus-five-roots graph. The
additional roots `c,d` are distinct from these neighbours and adjacent
to every wheel vertex, increasing every boundary count by two.

The two wheel-neighbour sets of `a,p` intersect only at `r_1`.
Their local degrees are four and three. Using three and four distinct
new vertices, respectively, in the two external bags can supply the
remaining degree incidences and both recorded contacts with `c,d`,
without another common neighbour. This establishes exactly the stated
compatibility of local incidences. It does not construct the missing
global component `D`, a seven-connected completion, or a target-free
completion.

Every `K_{2,3}` minus at most one edge has two vertices in its
three-vertex part adjacent to both vertices in its two-vertex part.
A fully rooted model therefore contains the contacts of a four-cycle
with `a,p` opposite. Name its other roots `t_i,t_j` in their facial
order. Inside its four disjoint branch sets, the contacts `a--t_i`
and `p--t_j` yield disjoint paths between these two pairs of original
roots. Their endpoints alternate on the displayed facial cycle,
contradicting the Jordan-curve separation property. This excludes
arbitrary connected branch sets, not merely paths, singletons or a
particular selection of contractions.

After discarding the `c,d` bags of any hypothetical seven-root local
allocation, all remaining bags are subsets of the planar graph `F`:
ownership forbids them from using either discarded root, and the local
host has no other vertices. At most one of the ten desired contacts
can fail, so at least five of the six contacts to `t_0,t_1,t_2` remain.
The sole externally recorded contact among these pairs is `a--t_2`,
whose actual root edge already lies in `F`. Thus the remaining bags
would give exactly the forbidden rooted minor. Allowing all seven
root bags to expand does not evade the obstruction.

## First failed inference and remaining scope

The explicit graph refutes the implication from the listed local
boundary and recorded-contact data to the requested almost-complete
rooted bipartite allocation. Those data do not establish an appropriate
scheme. A theorem converting schemes into rooted minors cannot supply
this missing premise.

The source does not infer failure of the original global singleton
target, T44, Conjecture 21, Hadwiger's conjecture or universal bipartite
contractibility. It identifies the need for additional global information
or a construction with different final branch sets. The constructions
and boundary arguments are direct; no unverified lift or induction
parameter occurs, and no finite computation is used as a premise.
