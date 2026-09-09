# A five-root wheel under relative boundary and degree bounds

**Status:** written proof; a separate exact-source internal audit accompanies this source.
This is a proposed construction input, not a closure of C19 or HC7.

All graphs are finite and simple; neighbourhoods of sets are external.
A rooted model has disjoint connected bags containing its prescribed
roots separately. A W4 has a hub and a four-vertex rim; neither the hub
nor the rim order is prescribed in the conclusion.

**Theorem.** Let T be five roots of a graph F and put D=V(F)-T.
Suppose |D|>=3, every nonempty subset of D has at least five neighbours,
and every vertex of D has degree at least six. Then F has a T-rooted W4.
No root triangle or pre-existing rooted four-clique is required.

## Inputs

We use the exact four-root alternatives recorded from Norin--Totschnig
Theorem 8 in [the five-root almost-clique source](hc7_five_root_almost_clique.md),
SHA-256 `de183e350c412739c05a744e811304454ba90856efee9e097813c70617bba9cd`,
with [audit](hc7_five_root_almost_clique_audit.md) SHA-256
`dc7db3d391ef2701516d64dd32e7546d40e2e4171406193f17d8feadcc4abb47`.
These give a rooted K4, the stated order-two rooted trisection, the
stated rooted separation of order at most three, or a plane drawing
with all four roots on one face. We retain the exact definitions there.

We also use [the five-root wheel extension](hc7_rooted_wheel_extension.md),
SHA-256 `f72e0b3d4254724a58f55b9445c0c173ea6c96e535416da47b1efc7fd5eb43b3`,
with [audit](hc7_rooted_wheel_extension_audit.md) SHA-256
`c93612165de23798c63922425fbd8d9e74407d2eb1a85b365853bd1343969178`:
in a three-connected graph, a K4 rooted at four members of a five-set
extends to a wheel rooted at all five. The fifth root may already
belong to the four-root model. No new literature inspection is claimed.

## Normalisation and its endpoints

With exactly two nonroots p,q of degree at least six, both are universal.
There is a five-root wheel precisely when F[T] is not a matching.
Indeed, two incident root edges form a three-vertex path; assign p,q to
the other two roots, obtaining K2 joined to that path, which contains W4.
Conversely, in a root graph of maximum degree one, if p,q are in one bag
or one is unused, a singleton root bag has at most two other neighbours.
If they occupy distinct bags, at least three root bags are singleton.
One of these has no matching neighbour in another singleton bag, so
again has at most two other neighbours. A W4 bag has at least three.
Thus the exceptional endpoint is K2 joined to a matching on its five
roots, and every root in it has degree at most three.

**Proof of the theorem.** Choose a counterexample minimizing |D|.
Every root sees D, since N(D)=T. If root a has a unique D-neighbour p,
contract ap and retain its label. No surviving nonroot sees old a;
every surviving degree and nonroot-set boundary is unchanged, with p
replaced by the new root. The roots have fixed disjoint preimages.
If |D|>=4 minimality applies. If |D|=3, the two-nonroot endpoint applies;
the merged root has degree at least d(p)-1>=5, so that endpoint is not
exceptional. Hence every root has at least two D-neighbours.

No two roots a,b have exactly the same two D-neighbours p,q. Otherwise
contract the disjoint edges ap,bq. Surviving nonroots see neither old
root, so their degrees and boundary cardinalities are unchanged and
models lift. With at least three remaining nonroots, minimality applies.
One remaining nonroot is impossible, since its preserved degree is at
least six in a six-vertex graph. With two remaining nonroots, the new
a-root has degree at least d(p)-2>=4: absorbing a loses at most one
neighbour of p, and the second contraction loses at most one more.
This excludes the exceptional endpoint. Both reductions strictly
decrease nonroot order within the class or reach a proved endpoint.

## A four-root clique in the normalized graph

For u in T put J_u=F-u, rooted at T-{u}. Every nonempty D-set has
boundary at least four in J_u, excluding the small rooted separation.
In a trisection the two specified open parts consist solely of roots:
any nonroots there would have boundary at most three. The common
two-set contains no root, since otherwise the nonempty set D minus
that two-set would have boundary at most three. The two open roots
therefore have the same pair of D-neighbours, already excluded.

If J_u has no rooted K4, the planar alternative follows. This graph
is two-connected: every component after at most one deletion contains
a nonroot, since each remaining root originally had two D-neighbours;
the boundary bound forces at least three roots into each component.
With no deletion the analogous count proves connectivity. Its
distinguished facial boundary is thus a cycle through all four roots.

Write k_a=|N_F(a) intersect D|, K=sum_(a in T) k_a, and e_D=e(F[D]).
The nonroot degree sum gives 2e_D+K>=6|D|, and every k_a>=2.
If the facial cycle for u has h nonroots, Euler's formula gives
e(J_u)<=3|D|+5-h. The cycle has at least 4-h root-root edges.
Subtracting these yields e_D+K-k_u<=3|D|+1 and hence

`2k_u >= K-2`.

If two different roots u,w lacked rooted four-cliques after deletion,
adding their inequalities would make the sum of the other three k_a
at most two, although it is at least six. Thus some F-u contains a
K4 rooted at the other four roots. Fix such a model.

## Suppressing peripheral roots

Let L be the roots of degree two. By normalization each has two
neighbours in D and no root neighbour. Their two-neighbour sets are
distinct by the paired reduction above. Form K0 by deleting L and
adding the edge between the two neighbours of each deleted root.

Every separation of order at most two in F has only one component
containing nonroots outside its separator: two such components would
each require at least three roots by the five-neighbour bound. There
is a nonroot outside the separator since |D|>=3. Any other component
contains only roots. Their two D-neighbours force the separator to be
two nonroots, and two roots in such a component would have the same
D-neighbour pair. Thus each such component is a singleton member of L.
Suppressing these vertices leaves K0 connected after every deletion
of at most two vertices. The matching below gives |V(K0)|>=5, so K0
is three-connected.

The roots in L can be matched injectively to their D-neighbours.
Indeed, a deficient set A of roots in the usual alternating-path
matching criterion would have |N_D(A)|<|A|<=5. Distinct two-neighbour
sets are edges of a simple graph on N_D(A). The only possibility is
|A|=5 and |N_D(A)|=4. Then A=T. If D has another vertex, the nonempty
set D-N_D(A) has boundary contained in four vertices, impossible.
Otherwise |D|=4 and its total degree is at most 2 binom(4,2)+10=22,
less than the required 24. Hence no deficient set exists.

## Preserving four marked bags

Project the fixed four-root model to K0 by removing L from its bags.
Every bag retains a vertex: a singleton degree-two root cannot have
the three contacts required of a K4 bag. A removed root used by a bag
has a neighbour in that bag. If deleting it disconnects the bag, its
two ports belong to the bag and the added edge reconnects the pieces.
If it supplied an interbag contact, the added edge from its in-bag
port to the other port restores that contact. Thus the four projected
bags remain disjoint connected K4 bags.

For each selected root in L, initially match it to a port in its own
projected bag. These choices are distinct because the bags are disjoint.
At most one L root is unmatched, namely the omitted root u if it lies
in L. Extend this partial matching by an augmenting path to cover it.
Such a path exists by the matching criterion just proved. Augmentation
keeps every previously occupied port occupied, though its assigned root
may change. Each projected bag therefore still contains a terminal
image: either its retained non-L root or an occupied port. These give
four distinct images of members of T in the four bags.

Contract each edge from a root in L to its matched port. The preimages
are disjoint pairs, and no other root is in a pair. The resulting
graph is exactly K0, with the five roots renamed at distinct vertices.
Its four projected clique bags contain four of these root images;
the fifth may lie anywhere. The audited three-connected wheel extension
gives a wheel rooted at all five images. Expanding the fixed contraction
preimages gives the required T-rooted W4 in F, a contradiction. QED

The two-nonroot exceptional graphs show why the order restriction cannot
be dropped. The theorem gives an unlabelled five-root wheel; it does not
prescribe its hub, reserve a further helper, or complete C19 or HC7.
