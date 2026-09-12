# Two boundary arcs obstruct a jointly rooted wheel

**Status:** written counterexample; a separate internal audit accompanies this source.
No finite computation is a premise.

**Claim refuted.** Every five-connected nonplanar graph \(M\) with
\(\delta(M)\ge6\), and sets \(S,T\subseteq V(M)\) of size at least seven,
has five disjoint connected branch sets forming a \(W_4\) minor, each meeting
both \(S\) and \(T\). The counterexample has \(S\cap T=\varnothing\).
Here \(W_4\) is the four-cycle with a universal hub, and \(Q_7=K_7-2K_2\).

## Construction and hypotheses

Fix \(m\ge14\). Let \(P\) have disjoint cycles
\(A=(a_i:i\in\mathbb Z_m)\), \(B=(b_j:j\in\mathbb Z_{2m})\),
\(C=(c_j:j\in\mathbb Z_{2m})\), and one further vertex \(h\).
Besides the cycle edges, put in precisely
\[
 a_i b_{2i-1},\ a_i b_{2i},\ a_i b_{2i+1},\qquad
 b_jc_{j-1},\ b_jc_j,\qquad hc_j.
\]
Indices on \(B,C\) are taken modulo \(2m\). Embed the three cycles
concentrically, with \(A\) outermost and \(h\) inside \(C\).
The annulus between \(A,B\) has triangular faces
\(a_i a_{i+1}b_{2i+1}\), \(a_i b_{2i-1}b_{2i}\), and
\(a_i b_{2i}b_{2i+1}\). Between \(B,C\) the faces are
\(b_jb_{j+1}c_j\) and \(b_jc_{j-1}c_j\); the inner faces are
\(hc_jc_{j+1}\). Thus \(P\) is planar with facial cycle \(A\).
Its degrees are five on \(A\), the even-indexed \(B\), and \(C\);
six on the odd-indexed \(B\); and \(2m\) at \(h\).

We prove \(P-D\) connected whenever \(|D|\le3\).
If \(h\notin D\), all surviving \(C\) vertices join \(h\).
If at most one \(C\) vertex is deleted, every surviving \(B\) vertex
retains a \(C\)-neighbour. Otherwise at most one \(B\) vertex is deleted,
so the surviving \(B\) cycle or path is connected and joins surviving \(C\).
If at most two \(B\) vertices are deleted, every surviving \(A\) vertex
retains a \(B\)-neighbour. If three are deleted, \(A\) is intact and
has an edge to surviving \(B\). Hence all surviving vertices join \(h\).
If \(h\in D\), at most two other vertices are deleted. With at most one
\(C\) deletion, surviving \(C\) is connected, every surviving \(B\) joins
it, and every surviving \(A\) joins \(B\). With two \(C\) deletions,
\(A,B\) are intact and connected together, and every surviving \(C\)
vertex joins \(B\). This proves \(\kappa(P)\ge4\).

Let \(M=K_1\vee P\), with universal apex \(z\), and set
\(S=\{a_0,\ldots,a_6\}\), \(T=\{a_7,\ldots,a_{13}\}\).
Deleting at most four vertices leaves \(M\) connected: a surviving \(z\)
connects everything, and deleting \(z\) leaves at most three deletions in \(P\).
Thus \(\kappa(M)\ge5\); moreover \(\delta(M)=6\), so Euler's planar
degree bound implies that \(M\) is nonplanar. Both sets have size seven.

## Exclusion of all jointly rooted wheel models

Add adjacent vertices \(p,q\) in the outer face of \(P\), joining \(p\)
to every vertex of \(S\) and \(q\) to every vertex of \(T\).
The resulting graph \(P^+\) is planar: the two disjoint contiguous boundary
arcs admit disjoint fans, with \(pq\) drawn between them in the same face.
For any disjoint connected bags in \(P\) each meeting both sets, their
contact graph is a forest. Indeed, a cycle in that graph can be contracted
to three connected unions of consecutive cycle bags forming a triangle.
Each union still meets both sets. These three unions and \(\{p\},\{q\}\)
would be a \(K_5\) minor in the planar graph \(P^+\), a contradiction.

In a putative jointly rooted \(W_4\) model in \(M\), at most one bag
contains \(z\). If none does, the contact graph in \(P\) contains a cycle.
If one does, discard that bag: deleting the hub of \(W_4\) leaves a
four-cycle, and deleting a rim vertex leaves a triangle. The remaining
bags lie in \(P\), still meet both sets, and again have a cyclic contact
graph. Both cases contradict the forest conclusion.

## Scope

The example also has no \(Q_7\) minor. A model avoiding \(z\) would lie in
planar \(P\); a model using \(z\), after deleting its owning bag, would
give a planar minor isomorphic to \(Q_7\) minus one vertex. Every such
six-vertex graph has at least thirteen edges, exceeding the planar bound twelve.
For \(m=14\), \(P\) has 71 vertices and 196 edges, and \(M\) has 72 vertices
and 267 edges. In the family, exactly \(4m\) vertices of \(M\) have degree six.
Thus this barrier does not satisfy the stronger residual degree condition
that all vertices have degree at least seven except at most four of degree six.
It also has planar \(M-z\). No counterexample to the actual seven-connected
minimum-degree-eight host, or to its retained marked conditions, is claimed.
