# An intact pair of helpers does not resolve prism ownership

**Status:** written counterexample with a direct proof and a
[separate internal audit](hc7_prism_intact_helper_barrier_audit.md).
This is a barrier to a construction step, not a closure of
the two-triangle case or HC7.

## Graph and exact scope

Let B have vertex set

    P={p1,p2,p3}, Q={q1,q2,q3}, A={a1,a2,a3}, {x,y}.

Its edges are exactly the two triangle edge sets on P and Q, together
with

    pi-ai, ai-qi, x-pi, x-ai, y-qi, y-ai  (i=1,2,3),
    xy.

Thus P and Q are anticomplete literal triangles. With E={x,y}, B-E is
an induced prism subdivision with three nontrivial vertical paths
pi-ai-qi. The connected pieces {x},{y} are adjacent; x owns all
E-neighbours of P, y owns all E-neighbours of Q, and both pieces contact
every vertical interior. Put T=P union Q.

We prove that B is four-connected and has an ordinary K5 minor, but has
no K5 model all five of whose bags meet T. Moreover E is a maximum
helper in the sense of the
[extremal prism normalisation](../results/hc7_two_triangle_extremal_prism.md).
Therefore moving triangle roots cannot universally repair this ownership
pattern while treating the two pieces as indivisible vertices.

These are quotient-level hypotheses. B is not five-connected: each pi
has degree four. The root-free singleton {ai} has only four neighbours,
so the actual six-neighbour boundary condition also fails. No chromatic
criticality, proper-minor colouring constraints, or preservation of
actual contact multiplicity under contraction is asserted.

## Connectivity and the ordinary minor

Delete at most three vertices. If x,y both survive, every surviving
vertex connects to their edge. If only x is deleted, at most two other
vertices are deleted. All surviving Q and A vertices connect to y, and
the surviving P clique connects to them through an intact pair pi,ai:
the three such pairs are disjoint, so two deletions cannot hit all three.
The case where only y is deleted is symmetric. If both x,y are deleted,
at most one further vertex is deleted from the subdivided prism, which
remains connected. Hence B is four-connected; a degree-four root gives
the matching upper bound.

The five bags

    {p1}, {p2}, {p3}, {x,y}, Q union A

are connected, disjoint and pairwise adjacent, giving an ordinary K5
minor.

## No model can meet T in all five bags

Suppose such a model exists. There are only six roots, so at most one
bag contains two roots, and every other bag contains exactly one.
Call a bag **ordinary** if it avoids x,y. An ordinary one-root bag is
either {pi} or {pi,ai}, or the corresponding qi set. In particular,
three pairwise adjacent ordinary one-root bags must use one whole
triangle: a P-rooted bag can contact a Q-rooted bag only at the matched
index, so no mixed triple is pairwise adjacent.

First suppose at most one bag meets {x,y}. There are at least four
ordinary bags. Four ordinary one-root bags cannot be pairwise adjacent.
Otherwise one ordinary bag contains two roots and three ordinary
one-root bags use one whole triangle. The two-root bag uses roots of
the other triangle and can contact at most two of those three bags,
again impossible. Thus x,y belong to distinct bags, denoted X,Y,
and there are exactly three ordinary bags.

If all three ordinary bags contain one root, assume by symmetry that
they are P-rooted. To contact the pi bag, Y must use ai itself or the
pi bag must contain ai. Thus no ai belongs to X. But X must contain a
Q root. Every path from x to Q avoiding y and the three P vertices
passes through A, so X cannot be connected. This excludes the case.

It remains that one ordinary bag H contains two roots and the other
two ordinary bags contain one root each. All six roots are now used,
and X,Y each contain one root.

**Two roots in the same triangle.** Suppose H contains pi,pj, with
{i,j,k}={1,2,3}. The other two ordinary roots must be qi,qj: both need
contact with H and with each other, and a mixed pair cannot do so.
The roots in X,Y are therefore pk,qk. They must be assigned as
pk in X and qk in Y. Indeed, the reverse assignment would require ak
in both connected bags: all other roots are unavailable, and ak is the
only remaining route from x to qk or from y to pk.

For the qi bag to contact X, ai must belong to that ordinary bag or to
X; the analogous statement holds for aj. Consequently neither ai nor
aj belongs to H or Y. But H can contact Y only through one of these
two vertices, a contradiction. The case of two Q roots is symmetric.

**One root in each triangle.** They must be a matched pair pi,qi:
an ordinary connected bag cannot join an unmatched pair without a
third root. Thus H contains ai as well. The two remaining ordinary
roots are either both P roots, both Q roots, or a matched pair pj,qj.
In the first case Y must contact the two P-rooted bags through aj,ak,
excluding both vertices from X. Yet X owns a Q root and needs one of
aj,ak to reach it. The second case is symmetric.

Finally suppose the two ordinary roots are pj,qj. The special bags
own pk,qk, necessarily with pk in X and qk in Y, by the same ak
argument above. Contact between the pj bag and Y requires aj in the
pj bag or Y. Contact between the qj bag and X requires aj in the
qj bag or X. These two pairs of bags are disjoint. This last
contradiction proves the noncontainment claim.

## Maximality and the unresolved host construction

Consider any connected P-full partition D',E' of B-P with Q contained
in D'. If x belongs to E', then D' must contain every ai: the only
neighbours of pi outside P are x,ai. Thus E' is contained in {x,y}.
If instead x belongs to D', then E' must contain every ai. Connecting
these three vertices without x or Q requires y in E'. But D' is then
contained in Q union {x}, with both Q and x present and no x--Q edge,
contradicting its connectivity. Therefore |E'|<=2, attained by the
displayed E={x,y}. This proves maximality directly, without invoking
the normalisation theorem.

The example permits arbitrary placements of all six roots; the failure
is not an artefact of freezing P or Q as singleton bags. It does not
show that an actual pair of connected pieces X,Y in the original host
cannot be repaired. Those pieces may be split internally or exchanged
with parts of several vertical paths. Five-connectivity, the six-neighbour
boundary condition, and the original critical-host colourings remain
available for that construction. Contracting each piece first discards
precisely the internal choices this example shows can be necessary.
