# Two failed operations under the full augmentation hypotheses

**Status:** written counterexamples; separate internal audit alongside this
source. The linked finite experiment has an independent reconstruction.
Neither example refutes the augmentation theorem, C19 or HC7.

Write Q7=K7−2K2, with independent missing edges. The augmentation target
concerns finite simple five-connected six-chromatic graphs of minimum
degree at least six and order at least seven. Both constructions below
satisfy every hypothesis and have explicit Q7 models.

## 1. Every single-edge contraction can lose the sixth colour

Let X have vertices Z_11 and edge differences ±2, ±3, ±5. Its complement
T has differences ±1, ±4. It is triangle-free, so alpha(X)=2. Thus X needs
six colours; the following classes supply them:

    {0}, {1,2}, {3,7}, {4,8}, {5,9}, {6,10}.

The graph X is six-regular and six-connected. Indeed, the common-neighbour
counts in T for cyclic distances 1,2,3,4,5 are respectively 0,1,3,0,2.
Thus T contains no K2,4. A K3,3 would require three vertices pairwise at
distance three, impossible because those pairs form an eleven-cycle.
A cut of X of order at most five would leave at least six vertices in
exactly two components, since alpha(X)=2. Their cross-pairs would form a
complete bipartite subgraph of T. Maximum degree four excludes a singleton
side; the other possibilities contain K2,4 or K3,3. This proves connectivity
six. There is no literal K6: its vertices would be an independent six-set
in the eleven-cycle contained in T.

Translations and reflections reduce the edges to 02,03,05. With w denoting
the contracted vertex, their quotient five-colourings are:

| Edge | Independent colour classes in the quotient |
| --- | --- |
| 02 | {w,1}, {3,4}, {6,10}, {5,9}, {7,8} |
| 03 | {w,4}, {1,2}, {6,10}, {5,9}, {7,8} |
| 05 | {w,1}, {6,10}, {2,9}, {3,4}, {7,8} |

Each quotient still contains nine original vertices of independence
number at most two, so its chromatic number is exactly five. The three
edge types have 2,4,3 common neighbours in X. These vertices acquire degree
five; the other singleton degrees remain six and w has degree 8,6,7,
respectively. Hence every quotient has minimum degree five. Its connectivity
is five: a cut of order at most four would lift to at most five vertices
in X, while a degree-five vertex gives the upper bound.

Expanding w in the displayed colouring colours X−e with five colours.
Deleting the singleton class {0} above, then translating, also shows that
every vertex deletion is five-colourable. Thus the obstruction survives
both vertex- and edge-criticality.

**First unsupported inference.** No single-edge contraction preserves the
augmentation class in this host. Retaining a K6 *minor model* does not
preserve chromatic number; chromatic number can increase under contraction.
No claim about larger contractions follows from the single-edge failure.

**A simultaneous repair in the same graph.** Contract 02 and 1–10. Both
resulting vertices are universal: the common non-neighbour sets of the
endpoint pairs are {1} and {0}, absorbed by the opposite bag. The quotient
is K2 joined to R=X[{3,4,5,6,7,8,9}]. Its seven vertices require four
colours, supplied by {3,7},{4,8},{5,9},{6}; the quotient is six-chromatic.
The deleted four-set induces P4, so its bipartiteness also gives
chi(R)≥chi(X)−2=4. The quotient still has minimum degree five.

The seven original bags

    {0,2}, {1,10}, {3,5,8}, {4}, {6}, {7}, {9}

form Q7. The first two are universal bags; the last five form a wheel
with hub {9} and rim {3,5,8},{6},{4},{7}. The only omissions are
{3,5,8}–{4} and {6}–{7}. Connectivity, disjointness and all contacts are
in the original graph. This repairs the example, not the general
selection of simultaneous contractions or a preserved induction class.

## 2. Balancing bags can prohibit every strict local improvement

For seven nonempty connected bags partitioning the host, let m count
missing contacts, o count pairs of omissions sharing a bag, and s be the
sum of squared bag orders. A move splits one bag into two connected
nonempty parts and merges any adjacent two resulting parts. All connected
splits are allowed; the choice of spanning trees is unrestricted.

There is a full-hypothesis host and a nonterminal partition from which no
move strictly decreases (m,o,s) lexicographically.

**Construction.** On Z_7 let B be K7 with pairs {1,6},{2,5},{3,4} omitted.
Colour its edge ij by i+j modulo seven, which lies in {1,...,6}. This is
a proper six-edge-colouring. B has a proper four-vertex-colouring f with
those three pairs and singleton {0} as classes, labelled 1,2,3,0.

Replace each vertex i by a disjoint copy X_i of X. Choose ports 0,1,3,4,5,6,
one in each of X's six colour classes, labelled 0,...,5. For each B edge
of edge-colour t, join the port labelled t−1 in its two copies. There
are no other cross-edges. Each port is used at most once.

Shift every colour in X_i by f(i) modulo six. The endpoints of a cross-edge
had the same original colour and have different shifts, so this properly
six-colours H. Each copy requires six colours; hence chi(H)=6. Its order
is 77 and minimum degree six. Deleting at most four vertices leaves each
copy connected and removes at most four cross-edges. Every cut of B with
smaller side k≤3 has at least k(7−k)−k≥5 edges. The surviving copies
therefore remain connected, proving five-connectivity of H. Each copy
already contains the displayed Q7 model.

**Failure of strict descent.** Use the seven copies as bags. Their contact
graph is B, so (m,o)=(3,0), and s=7·11²=847 is the absolute minimum.
Splitting a bag distributes every old contact to exactly one child,
because each pair of original bags has just one cross-edge. The children
are adjacent, so the split produces exactly 19 contacts. Merging adjacent
parts deletes their mutual contact and may identify others, leaving at
most 18. Thus m cannot decrease below three. The value o cannot improve
from zero, and s cannot improve from its absolute minimum. This proves
the claimed obstruction for every allowed move.

A port can nevertheless move into the adjacent copy without changing the
contact graph: its old bag remains connected and retains an edge to the
moved port. The sizes 11,11 become 10,12, increasing s by two. Balancing
can therefore reject a useful equal-defect move.

**Unaffected scope.** This does not refute larger exchanges, other initial
partitions, or moves allowing the balancing term to increase. The host is
not six-vertex-critical. Each bag is itself a smaller full-hypothesis host,
so induction on order also handles this example immediately. Neither that
smaller instance nor a Q7-containing subgraph has been forced in a general
local minimum. A six-chromatic bag alone need not retain the required
connectivity; replacing the host by a critical core still needs a proof.

## Finite exchange comparison

The [retained probe](../active/hc7_chromatic_exchange_probe.py) checks X and
a second explicit eleven-vertex full-hypothesis host. It enumerates all
63,987 seven-part partitions of each, then all connected split-and-merge
moves. The second host has 24 nonterminal local minima for (m,o); a displayed
one escapes in two moves with scores (3,0),(3,0),(2,0). Adding s removes
all local minima on these two graphs. Section 2 disproves the universal
inference from that finite success. No finite computation is a premise
of the written counterexamples in Sections 1 and 2.
