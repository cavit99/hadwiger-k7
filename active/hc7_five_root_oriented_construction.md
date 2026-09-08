# A prescribed full root: constructions and the remaining exchange

**Status:** conjectural target; the deductions below have written proofs.
Several strongest steps received separate spot checks during development;
a separate internal audit of this complete source is recorded beside it.
Neither the orientation target nor Conjecture 19 nor HC7 is proved here.

Graphs are finite and simple, and set neighbourhoods are external.
Rooted bags are disjoint connected sets containing their prescribed roots
separately. Additional contacts never invalidate a model.

**Conjectural target.** Let `S=B union {b,c}`, where
`B={B1,B2,B3}` is a literal triangle and `D=V(F)-S` is nonempty.
Assume every nonempty `X subseteq D` has at least five neighbours and
every D vertex has degree at least six. There should be an S-rooted
`K5-minus` model in which the c bag is full to the other four bags;
the sole possible missing pair is `bBi` for some `Bi in B`.

The [degree-six theorem](../results/hc7_five_root_degree_six.md), source
SHA-256 `289c5ad015b6c392ea69e8e26e15eba54b4eba7cb155789edd76b3dbb5c9f9a4`
and [audit](../results/hc7_five_root_degree_six_audit.md) SHA-256
`6f13ffd37126c78a697b5752574fe06b6fd13b68dabb0d63e4e39d76a8f1d065`,
supplies at least two admissible triangle centres, with possible holes
`Bi b` or `Bi c`. It does not prescribe c to be full.
We also use the exact NT Theorem 8 alternatives and actual-port argument
recorded there and in the [almost-clique source](../results/hc7_five_root_almost_clique.md),
SHA-256 `de183e350c412739c05a744e811304454ba90856efee9e097813c70617bba9cd`.
No new primary-source inspection is claimed.

## 1. The minimum counterexample class

Suppose the target fails and choose a counterexample minimizing `|D|`.
All assertions about a minimum counterexample below use this one choice.
If `|D|=2`, both nonroots are universal, and assigning one to b and one
to c gives a rooted K5. Thus `|D|>=3`.

Every component of D is full to S, by its boundary bound. Two components
assigned to b and c give a rooted K5; hence D is connected.
If a root a has its sole D-neighbour p, contract ap, retaining label a.
For every surviving nonroot set, old a was not a neighbour; p is simply
replaced by its root preimage. All degrees and boundary sizes are unchanged.
The root triangle and all five labels survive, and models lift through
the fixed connected preimage. Thus every root has at least two D-neighbours.

**Five-port reduction.** Every proper nonempty `X subset D` has boundary
at least six. Otherwise put `T=N_F(X)`, of size five. There are five
vertex-disjoint S--T paths in `F-X`, allowing trivial paths at common roots.
Indeed, a separator C of size at most four would leave a set Y reachable
from `T-C` in `(F-X)-C` and disjoint from `S-C`; then `X union Y` is
root-free and its whole boundary is contained in C, a contradiction.
The five paths use every S root and every T port. Stop them at the first
T vertex, so their interiors avoid both S and T. Label each port by its
matched S root. In `F[X union T]` all X degrees and subset boundaries
are unchanged. Add the three edges among the B-labelled ports.
The smaller target applies: `|X|>=2` follows from its degree-six condition.
Append the five fixed paths to the returned bags. An added edge joins
distinct prescribed roots, so it was never needed inside a bag; its
required contact lifts through the corresponding original literal B edge.
This preserves the c label and every required contact, contradicting
minimum `|D|`. This proves the asserted boundary-six property.

The configuration `N_D(b)=N_D(c)={p,q}` is also excluded. Contract bp
and cq simultaneously. Old b,c have no surviving nonroot neighbours, so
all surviving degrees and boundaries are unchanged. If `|D|=3`, the
remaining vertex would have degree at most five, already impossible;
otherwise at least two nonroots survive. The fixed disjoint preimages
preserve the roots, triangle and orientation on lifting.

Put `J=F-B`. The graphs J, `J-b`, and `J-c` are two-connected.
For example, after deleting b and a nonroot q, a component not containing
c would be a proper D set with boundary contained in `B union {b,q}`.
The c component contains a nonroot because c has two D-neighbours.
This contradicts the boundary-six property. Deleting both b,c leaves
connected D. The symmetric argument handles `J-c`; in J a cut separating
b,c similarly gives a proper D set with boundary in B, the cutvertex,
and one of b,c. A root-free cut component would have boundary at most four.

## 2. A diamond with unrestricted anchored degree-five vertices

**Lemma.** Suppose the five roots have the literal edges of B and also
`cB2,cB3`. Let `|D|>=2`, every nonempty D subset have boundary at least
five, every D vertex have degree at least five, and every degree-five
D vertex be adjacent to c. Then there is a c-full rooted model with
sole possible hole `bB2` or `bB3`. There is no bound on their number.

Use triangle `R={c,B2,B3}` and nontriangle roots b,B1. If both centres
B2,B3 were inadmissible, choose such a counterexample of minimum D order.
The literal `B1B2,B1B3` edges fill any proposed hole involving B1;
admissibility of either centre therefore proves the lemma.

For `D={p,q}`, both vertices see c: a degree-six vertex is universal,
and the degree-five condition supplies the other case. If pq is absent,
both are full to S. Otherwise each misses at most one S root, and they
cannot both miss b or both miss B1. Assign them to b and B1 with both
attachment edges present. The two expanded bags are adjacent, c is full,
and the b bag misses at most one of B2,B3. This proves the base case.

Thin-root absorption, exactly as in Section 1, preserves every surviving
degree and the condition on degree-five vertices. If c is absorbed, it
had no surviving degree-five neighbour; its label still has the same
fixed preimage. Thus all roots have at least two D-neighbours.
If b,B1 have the same two D-neighbours p,q, their paired absorption
preserves degrees and leaves c fixed. For `|D|>=4` it is a valid reduction.
For `D={p,q,z}`, z misses b,B1, so it has degree exactly five and sees
all of `p,q,c,B2,B3`. If a degree-five p sees at least two R roots,
the bags `b+p`, `B1+q+z`, and singleton R are sufficient. If it sees
only c, its five neighbours are exactly `b,B1,z,c,q`; root normalization
forces q to see B2,B3. Then `b+q`, `c+p`, B1, B2, B3 give a rooted K5;
z is discarded. Finally, if p,q both have degree at least six, each sees
at least two R roots, and one sees c by normalization. Use that vertex
with b and the other with `B1+z`. This handles the endpoint before descent.

For either bad centre u, apply NT Theorem 8 to `F-u`, rooted at the other
four roots. The internal-four boundary excludes its small rooted
separation. In a rooted K4, any u contact to the b/B1 helpers is terminal.
Maximize their union, then minimize the other two bags: the actual-port
argument gives one port in each other bag, and unused components miss
the helper union. Its nonroot part has boundary at most four in F and
is empty. The resulting two common D-neighbours of b,B1 were excluded.
In the trisection outcome the two isolated open parts are sole roots;
the common two ports are nonroots, and the literal edge between the
other two R roots forces those isolated roots to be b,B1. The same
paired reduction excludes it. These are precisely the recorded NT
reductions; none requires minimum degree six in the deleted graph.

Only a cofacial plane drawing remains, and the internal-four bound plus
two D-neighbours at every root makes `F-u` two-connected, as in the
degree-six source. Put `k_a=|N_D(a)|`, `K=sum k_a`, and `e_D=e(F[D])`.
If d is the number of degree-five nonroots, then
`2e_D+K>=6|D|-d`. The distinguished facial cycle has four roots and h
nonroots. Euler gives `e(F-u)<=3|D|+5-h`; its cycle contributes at least
`4-h` root edges. Hence `e_D+K-k_u<=3|D|+1`, and
`2k_u>=K-d-2`. For the two bad centres this implies
`k_c+k_b+k_B1<=d+2`. But `k_c>=d` and `k_b,k_B1>=2`, a contradiction.
All reductions strictly lowered D order and preserved both fixed bad
labels and the anchored-degree condition. This proves the lemma.

## 3. A complete b-star terminal

A single root--D contraction in the minimum counterexample preserves
internal five-connectivity: every surviving D set is proper in the old
D and its boundary loses at most one vertex. A contraction cp creates
only degree-five exceptions adjacent to the new c. Thus if `c+p` sees
two B roots, Section 2 applies. If `b+p` sees two B roots, put any whole
remaining D component with c; it is full to the five new roots, and
singleton b already has its two required B contacts. Consequently each
of `c+p` and `b+p`, for its respective neighbour p, sees at most one B root.

Suppose distinct `p,q in N_D(b)` see B1,B2 respectively. If c has a
D-neighbour outside `{p,q}`, choose its component C in `D-{p,q}`.
Its boundary lies in the seven-set `S union {p,q}` and has size at least
six. If C is B-full, the bags `b+p+q`, `c+C`, and singleton B are terminal.
Their mutual contact follows since C sees at least one of b,p,q.
If C misses B1, it sees all other six boundary vertices. Put p with B1,
q with b, and C with c. The b bag sees B1 through bp and B2 through q;
the c bag sees B1 through Cp. The B2 omission is symmetric.
If C misses B3, choose another component E of `D-{p,q}` meeting B3,
when such a neighbour exists. Its boundary-six condition makes it meet
one of p,q, say p. Put `B3+E+p` together and keep `b+q`, `c+C`, B1,B2.
If B3 has no such neighbour, it sees both p,q by normalization; use
`B3+p` instead. In either case c sees B3 through Cp, b sees it through
bp and retains B2, and C supplies the b--c contact. All bags are disjoint.

It remains to handle `N_D(c)={p,q}`. The single-c-contraction observation
shows c has no B contact and p,q see only B1,B2 respectively. Minimality
forces pq to be an edge and both p,q to have degree six: otherwise cp
or cq would preserve degree six and yield a smaller counterexample.
At least two D vertices remain outside p,q, since otherwise p has at
most the five neighbours b,c,q,B1 and one further D vertex. Contract
the connected set `{c,p,q}`. Old c had no surviving D-neighbour, so
replacing p,q by one root loses at most one boundary vertex. Every new
degree-five vertex is adjacent to c, the remaining D has size at least
two, and c now sees B1,B2. Section 2 applies and lifts through this fixed
preimage. Thus all B contacts of `N_D(b)` are confined to one B label.

## 4. Two spanning responses and a literal contact terminal

For each of the at least two admissible centres Bi, orientation failure
forces the hole to be `cBi`. Delete the Bi bag to obtain a rooted K4 in
`F-Bi` on b,c and the other two B roots. In every such model the c bag
misses Bi, since a contact would be terminal. Maximize the b/c union M,
then minimize the other two bags. Their one actual port each and the
absence of unused components meeting M give
`N_F(M-{b,c}) subseteq {b,c,Bi} union {the two ports}`.
The nonroot part is all D or empty. Empty would force b,c to have exactly
the same two D-neighbours. Thus all D lies in M, the other root bags are
singleton, and we obtain a spanning connected partition
`J=Ui union Vi`, with b in Ui, c in Vi, Ui full to B, and Vi full to
`B-{Bi}` but missing Bi. Different centres may give different partitions.

**Literal-contact terminal.** Suppose b sees B1. Choose a response missing
`Bi != B1`. Contract Vi to z and put `L=Ui union {z,Bi}`. This graph is
two-connected. Deleting u in Ui leaves a connected contraction of
`J-u`, and Bi retains a neighbour since its at least two D-neighbours
all lie in Ui. Deleting z leaves connected `Ui+Bi`; deleting Bi leaves
connected `Ui+z`. A two-connected graph has a rooted triangle at any
three roots, by a cycle and a two-fan, so use roots b,z,Bi in L.
Lift z to all Vi and retain the other B roots singleton. The c bag keeps
both other B contacts; the three new bags are pairwise adjacent; and
the b bag keeps B1 literally as well as Bi. This is the required model.
Therefore b is anticomplete to B in a minimum counterexample.

## 5. Eliminating every two-edge b--B connection

**Deduction.** In the minimum counterexample, `N_D(b)` is anticomplete
to B. Suppose instead that p sees b and Bi, and let Bj,Bk be the other
two B roots. Put `F'=F/bp`, with root `b*` and nonroots `D'=D-{p}`.
Section 1 gives internal five-connectivity. Every nonroot has degree at
least five; its degree is five only if it was a common degree-six
neighbour of old b,p. Let d count these exceptions. All are adjacent
to b*, and none sees Bj or Bk, by Section 3. With `k_a=|N_{D'}(a)|`,
we have `k_b*>=d`, `k_c,k_Bi>=1`, and `k_Bj,k_Bk>=2`.
Also `k_b*>=3`: p has degree at least six and at most the three root
neighbours b,c,Bi. No edge-minimality assumption is used.

Apply NT Theorem 8 to `F'-Bu` for each `u in {j,k}`. Internal four
excludes its small rooted separation. In its trisection the two isolated
open parts would again be singleton roots of actual degree at most two.
But b* has at least three D'-neighbours, Bi sees b* and the remaining
B root and at least one nonroot, and that B root has at least two
nonroot neighbours and Bi. Only c could be such an isolated root,
so this alternative is impossible.

Each of these graphs is two-connected. After deleting at most one
vertex, every component contains a nonroot. The only potentially thin
roots are Bi,c. Bi is joined to b* and the other B root, which retain
nonroot neighbours. If c has just one D'-neighbour q, its original
D-neighbours were p,q, so it also has the new edge cb*; one of q,b*
survives. The internal-four bound would require at least three roots
in each component after a one-vertex deletion, which is impossible
for two components. The case with no deletion also gives connectivity.

Suppose both graphs lack their rooted K4. Both are therefore cofacial.
Write `K=sum k_a` and `e'=e(F'[D'])`. The two drawings give, exactly
as in Section 2,
`2e'+K>=6|D'|-d` and `e'+K-k_Bu<=3|D'|+1`.
Consequently `k_b*+k_c+k_Bi<=d+2`. Equality is forced throughout:
`k_b*=d`, `k_c=k_Bi=1`. Every D'-neighbour of b* is therefore a
degree-five exception, hence a common old b,p neighbour of degree six.
In particular every D-neighbour of p is an old b-neighbour.

The equality `k_c=1` gives `N_D(c)={p,q}`. If pq were absent or q had
degree at least seven, contracting cp would preserve all original
degree-six hypotheses and contradict minimum D order. Hence pq exists
and q has degree six. It lies in `N_{D'}(b*)` and misses Bj,Bk.
Since p sees Bi, Section 3's single-c-contraction argument also forbids
c from seeing Bj or Bk. Thus the root graph in `F'-Bj` has precisely
the edges `cb*,b*Bi,BiBk` and possibly `cBi`.

Let h count the nonroots on its distinguished facial cycle and t its
number of root edges. The preceding equality forces `t=4-h`.
If cBi is present, then `t=4,h=0`, although this root graph has no
four-cycle. Otherwise `t=3,h=1`, and all three root edges must be on
the face, whose remaining segment is `Bk--q--c`: c has only q as a
nonroot neighbour. This requires qBk, a contradiction. Therefore at
least one of `F'-Bj,F'-Bk` has the required rooted K4.

Use one, say `F'-Bj`. If its c bag meets Bj, the oriented model is
immediate. Otherwise maximize the b*/c helper union M and minimize
the Bi/Bk bags, obtaining two actual ports and no unused component
meeting M. Lift just the nonroot part and the contraction preimage:
`X={p} union (M-{b*,c})` is a nonempty subset of the original D with
boundary contained in `{b,c,Bj}` and the two actual ports. Neither
port belongs to b*, so each is an original vertex. Section 1 forces
`X=D`. Thus the two helpers span `J/bp`, and Bi,Bk are singleton.
The c helper misses Bj, so all of Bj's at least two D-neighbours lie
in the other helper; p was not one of them.

The graph `J/bp` is two-connected: its only potentially new cutvertex
is b*, whose deletion is connected `J-{b,p}` because `J-b` is
two-connected. Apply the literal-contact construction of Section 4
to this spanning response and the actual edge b*Bi. Its rooted triangle
gives the c-full model, and lifting bp preserves all five labels.
This contradiction proves the deduction. It supersedes the earlier
separate repairs for a contact vertex in either helper or at a leaf.

## 6. Two contractions and complete four-boundary replacement

The following is a conditional reduction inside the same minimum
counterexample. It does not establish the terminal orientation below.

**Four-root packet.** Let a graph have four distinct roots `h,k,a,d`,
with hk an edge and at least two nonroots. Suppose every nonempty
nonroot subset has at least four neighbours, every nonroot has degree
at least five, and every degree-five nonroot is adjacent to h or k.
Then there is a rooted K4 at these four roots.

Here is a complete proof using the recorded NT alternative. Minimize
nonroot order in a counterexample. With two nonroots, both are universal;
put one with a and one with d, retaining singleton h,k and their edge.
A one-nonroot graph cannot have the stated degree. Absorbing a root's
sole nonroot neighbour preserves every surviving degree and boundary.
If an anchor is absorbed, no surviving exception depended solely on
that old anchor; its adjacency to the other anchor remains. Thus every
root has at least two nonroot neighbours in a minimum counterexample.

The small rooted separation is excluded by internal four-connectivity.
In a trisection, the two isolated open parts are singleton roots. Its
two common ports are nonroots: otherwise the nonempty nonroot set off
the ports has at most three neighbours. The literal hk edge prevents
either anchor from being an open singleton, so the two open roots are
a,d. Absorb the two ports into these roots separately. Every surviving
degree and boundary is unchanged, and the anchors remain fixed. A
one-nonroot endpoint is impossible by the preserved degree-five bound;
a two-nonroot endpoint has the preceding universal-vertex construction.
This strictly decreases order and preserves every labelled model on lift.

If no rooted K4 exists, the graph is therefore planar with its four
roots cofacial. Internal four-connectivity and the two nonroot neighbours
at each root make it two-connected, by the component count of Section 2.
Write n for nonroot order, `K=sum k_u` for the root-to-nonroot incidences,
and delta for the number of degree-five nonroots. Subtracting the forced
root edges of the facial cycle from Euler's bound gives
`e_D+K<=3n+1`. Meanwhile `2e_D+K>=6n-delta`, hence `K<=delta+2`.
But `k_h+k_k>=delta` and `k_a,k_d>=2`, a contradiction. This proves
the packet without any bound on the number of exceptions.

Now suppose there is a path `b-p-q-Bi`, with p,q nonroots. By Section 5
it has minimum possible b--B length, p has no B contact, and q is not
adjacent to b. Contract the two disjoint edges bp and Biq, retaining
root names `h=b*` and `k=Bi*`; their actual contact is the old edge pq.
Call the resulting graph F0 and its nonroot set `D0=D-{p,q}`.
There are at least three remaining nonroots: p has at most the root
neighbours b,c, so its degree-six bound forces `|D|>=5`.

Every remaining nonroot has degree at least five. Indeed, a degree loss
at bp requires adjacency to old b and p, and an old b-neighbour has no
B contact, so it cannot also lose a neighbour at Biq. Every degree-five
vertex is adjacent to h or k. Moreover, a degree-five vertex adjacent
to h but not k is an old bp exception and misses both other B roots.

Every nonempty `X subseteq D0` has at least four neighbours in F0.
If it has exactly four, its old boundary was exactly
`{b,p,Bi,q,a,d}`: both identifications must lose a boundary vertex,
and the original proper-D boundary was at least six. Its F0 boundary
is therefore `{h,k,a,d}`. Such X has at least two vertices, since a
singleton has degree at least five. In the side induced by X and its
boundary, every nonroot degree and subset boundary is retained. The
four-root packet applies with the actual edge hk.

Call these boundary-four sets bad, and choose all inclusion-maximal bad
sets, including a whole-D0 set if it is bad. They are disjoint: for
overlapping sets, external-neighbourhood submodularity and the lower
bound four on their intersection force their union to be bad. They are
also anticomplete. If two disjoint bad sets have an edge, each loses at
least one of its two nonanchor ports into the other set; their union
has boundary at most `2+2+2-1-1=4` and is again bad. Both conclusions
contradict maximality unless the sets coincide. A maximal bad set need
not be connected; the four-root packet imposes no connectivity condition
on its nonroot set.

Replace every maximal bad side by its boundary K4, using its actual
rooted model. No side contains another side's port, by anticompleteness.
Different models thus share only actual boundary vertices. For each
shared vertex, unite its labelled preimages across the incident models;
they are connected through that vertex and remain disjoint from all
other labelled preimages. All original outside edges survive. This
constructs the completed torso as an actual rooted minor, retaining
the five original labels and the hk contact.

The torso has internal five-connectivity at those roots. Otherwise a
nonempty surviving nonroot set Z with boundary at most four can be
lifted by adjoining every removed side whose boundary meets Z. Since
each such boundary is a clique in the torso, all its ports lie in
`Z union N(Z)`. The lifted set has old boundary at most four and is
bad. It contains a surviving vertex outside every maximal bad side,
and, if any side was adjoined, strictly enlarges that side. Either
possibility contradicts the definition of the maximal sides.

In particular every surviving nonroot has degree at least five. Any
surviving vertex whose degree changed is a port of a replaced side,
so it is now adjacent to BOTH h and k. Consequently the torso has
the following precise remaining class: literal B triangle and bBi
edge, internal five-connectivity, nonroot minimum degree five, every
degree-five nonroot adjacent to b or Bi, and every degree-five vertex
adjacent to b but not Bi anticomplete to the other two B roots.
Here h,k have been renamed b,Bi; their fixed original preimages remain
part of the construction. The terminal orientation for this class is
not proved.

The replacement can leave zero or one nonroot, so those endpoints are
not excluded or declared terminal. The looser anchored degree-five
class is insufficient even with two nonroots: take roots with only
the B triangle and bB1, adjacent nonroots u,w, u adjacent to
`b,c,B2,B3`, and w adjacent to `b,B1,B2,B3`. Both have degree five and
every nonroot subset has five neighbours. Any c-full model must put
u in its c bag; obtaining the c--B1 contact then puts w in c's or
B1's bag, leaving singleton b without a second B contact. This example
violates the refined exclusive-b condition above and does not refute
the conditional torso reduction. Further root growth or a terminal
argument requires the full retained data and fixed preimages.

## 7. Remaining scope

The target is still conjectural. A minimum counterexample now has b
and every D-neighbour of b anticomplete to B. Section 6 handles all
four-boundary failures of one further paired contraction, but neither
its terminal class nor unrestricted rooted growth is resolved.
The two spanning responses need not retain each other's branch sets.

In the critical seven-boundary application, even a c-full packet alone
needs care: with c the chosen port, singleton v misses that port, and
the opposite helper may additionally miss a B root. If the core also
has its allowed hole, these are three possible holes. The orientation
target therefore does not by itself close that entire application.
