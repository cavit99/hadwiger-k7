# Extending four clique roots to a five-root wheel

**Status:** written proof; separate internal audits accompany this source.
All graphs are finite and simple. No priority or comparative-significance
claim is made here.

## Theorem

Let F be three-connected and let T be five distinct vertices. If F has a
K4 minor rooted at some four members of T, then it has a W4 minor rooted
at all five members of T, where W4 is the four-cycle with a universal hub.
The hub is not prescribed. The omitted member of T may belong to the
initial K4 model; it need not be unused.

A model consists of disjoint nonempty connected vertex sets, called bags,
with the required adjacencies. Rooted bags contain their respective roots.

## 1. Contractions and the terminal triangle

An edge is contractible if contracting it and simplifying leaves a
three-connected graph. It is T-legal if its ends are not both in T.
All contractions below retain the five distinct labels. A model in a
quotient lifts by replacing each quotient vertex by its fixed connected
contraction preimage. This preserves disjointness, roots and contacts.

We use Wu's theorem: in a simple three-connected graph of order at least
five, a vertex incident with no contractible edge has at least four
degree-three neighbours, each incident with exactly two contractible edges.
See H. Wu, *Contractible Elements in Graphs and Matroids*,
Combinatorics, Probability and Computing **12** (2003), 457–465,
[published statement](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/contractible-elements-in-graphs-and-matroids/5556F945B4E534D2A8F017DE7E82BD5B).

Two elementary contraction facts will be used, with F of order at least five.

**Clique-neighbour contraction.** If rs is an edge and N(r)-{s} is a
clique, then rs is contractible. Indeed, a cut of order at most two in
F/rs must contain the contracted vertex. In F-{s,z}, the remaining
neighbours of r form a clique, so removing r cannot disconnect the other
vertices. This excludes the corresponding cut {rs,z}; the one-vertex
case is identical.

**Boundary contraction.** Suppose {u,v,w} is a three-cut, D is a component of
F-{u,v,w}, and uv is an edge. Contract D together with w. The quotient is
F-D with wu and wv added, and is three-connected. Cuts avoiding the new
vertex lift immediately. For a cut containing it, start in F-{w,z};
paths through D can be replaced by uv, or by its surviving endpoint when
z is u or v. Here every component of a three-cut has all three boundary
neighbours, by three-connectivity.

**Terminal triangle.** If F[T] contains a triangle, F has a T-rooted W4.
To see this, contract T-legal contractible edges until none remains.
Each step reduces the order. For each remaining nonterminal h, Wu supplies
four degree-three neighbours whose two contractible edges must join
terminals. These neighbours are terminals and cannot serve two different
nonterminals. Thus at most one nonterminal remains.

With no nonterminal, the five-vertex graph has minimum degree three; its
complement is a matching, so it contains W4. With one nonterminal h,
at least four terminals have precisely two terminal neighbours and are
adjacent to h. The remaining terminal has terminal degree two or four,
by parity and minimum degree three. In the first case the terminal graph
is C5. In the second it is a universal terminal joined to a matching on
the other four, and deleting h and that terminal disconnects the graph.
Thus the only possible six-vertex case has terminal graph C5, which cannot
retain the original terminal triangle. All resulting models lift.

## 2. A minimum counterexample

Suppose the theorem fails, and choose a counterexample (F,T) of minimum
order. It has at least six vertices. A T-legal contraction that preserves
three-connectivity and *some* four-of-five rooted K4 contradicts this
choice. In particular every T-legal edge internal to any such K4 bag is
noncontractible. A noncontractible edge uv belongs to a three-cut
{u,v,w}: a two-cut in F/uv must contain the contracted vertex.

For a chosen K4 model, write R for its four selected roots and t for the
remaining terminal. Changing R is allowed. The terminal-triangle argument
shows that F[T] has no triangle.

**Every nonterminal is used by every four-of-five K4 model.** Suppose x
is unused. Every edge incident with x preserves the model on contraction,
so none is contractible. Let Y be the four degree-three neighbours supplied
by Wu. Each y in Y has precisely one noncontractible incident edge, xy.
A nonterminal y is impossible: if unused, its incident contractions
preserve the model; if used, an edge to its own bag is T-legal and
noncontractible, contrary to Wu. Thus Y is contained in T. A selected
root y in Y cannot be a singleton bag, since its unused neighbour x
leaves only two possible clique contacts. An edge to its own bag must
therefore join y to t; any other such edge would be T-legal. Only one
selected-root bag can contain t. There are consequently at most two
possibilities for y, that selected root and t itself, a contradiction.

Fix a T-legal internal edge uv of a bag A and a three-cut {u,v,w}.
We next control its small components. Put U={u,v}.

## 3. A component with no selected root

**Claim.** If a component X of F-{u,v,w} avoids R, then X={t} and w is
a selected root.

The boundary contraction preserves a four-root K4. If w is in a different
bag B, A-X remains connected through uv and B-X through w; assigning the
contracted vertex to B restores the only possibly lost contact, A–B.
If w belongs to A, the added edges reconnect its pieces; if w is unused,
only A can meet X and uv reconnects it. Other bags and contacts are
unchanged. Thus the contraction contradicts minimality whenever
X together with w contains at most one terminal. The only remaining case
has t in X and w in R. The selected root w may belong to A or to a
different bag B.

Any w–U path with interior in X supplies a replacement: put its interior
in A, remove the rest of X, and keep the outside bags. If w belongs to A,
this path reconnects its pieces; otherwise it supplies A–B. Therefore every
nonterminal p in X lies on every such path. In F[X+{w}]-p, the component
of w cannot contain another vertex: otherwise its vertices other than w
have actual boundary contained in {p,w}. Hence N(w) intersect X={p}.
There is at most one nonterminal, and if it exists then X={p,t}.
Connectedness and minimum degree give pt,tu,tv.

Every edge incident with p preserves a K4 model. If w belongs to A, put
p,t in A. If w belongs to B, do this for all edges except pw; for pw,
put p in B and t in A, using pt for A–B.
All these edges are T-legal and thus noncontractible. Wu cannot supply
four suitable neighbours of p: any neighbour u or v already has the two
noncontractible incident edges to p and along uv, while the only other
possible neighbours are t,w. This contradiction proves the claim.

## 4. A component containing the other bag's root

Suppose w belongs to B, a bag different from A, and X contains precisely
the selected root r of B. We prove that X has no nonterminal.

Let L=F[X+{w}]. If a nonterminal p in X can be avoided by an r–w path
in L, take the component of L-p containing r,w. Its vertices in X meet U;
otherwise their actual boundary is contained in {p,w}. Assign this
component to B, discard the rest of X, and retain A-X joined by uv.
Its U contact restores A–B. All contacts with the other two bags survive
outside X. This would omit p. Thus every nonterminal in X separates r
from w in L, and belongs to B in the original model.

We record the cut argument along these mandatory vertices. Let ef be an
edge on an r–w path in L, with e,f in X-{r}, e preceding f and e
separating r from w in L. Both ends are in B; assume the edge is T-legal. Let P be the
r-component of L-e. Then N_F(P) is contained in {e,u,v}, and P meets
both u and v. If {e,f,z} is a three-cut, every surviving component of P-z
meets U: otherwise {e,z} is an actual cut of order at most two. The
surviving U vertices are joined by uv. Let Y be their component in
F-{e,f,z}. Then every surviving vertex of P belongs to Y, and
N_F(X union Y) is contained in {w,z}, with any deleted U endpoint included
in this bound. If z lies in X the boundary is smaller. Three-connectivity
therefore puts every surviving selected root in Y; any selected root
equal to z is, of course, deleted. Every other cut-component is consequently
{t}, by Section 3.

If t belongs to X and also separates r from w in L, an edge joining t to an adjacent
nonterminal on this path gives a contradiction: the preceding argument
leaves only a singleton t component, although t was deleted. Such an edge
exists whenever X has a nonterminal, as r and t are its only terminals.
We may therefore choose an r–w path whose interior avoids t. Write it as

    r,p1,...,pm,w,

where p1,...,pm are all nonterminals of X. For each consecutive pair
pi,pi+1, the internal edge must have an obstructing three-cut isolating t,
so N(t)={pi,pi+1,z}. Whenever such a pair exists, t lies in X: a terminal at u or v is
in Y or deleted, one at w would shortcut a mandatory vertex, and other
vertices outside X cannot meet its interior. By Section 3, z is a selected
root. It therefore lies in U or is r; adjacency to r would shortcut a
mandatory vertex.
Two consecutive such edges are impossible. Hence m is at most two.

If m=2, t has neighbours p1,p2 and one member of U. Thus
N(r)={p1,u,v}, and rp1 is a T-legal internal contraction by the
clique-neighbour fact. This is impossible.

Suppose m=1, writing p=p1. If t is outside X or rt is absent,
N(r)={p,u,v} and rp contracts. If rt is present but tp is absent, t has
neighbours r,u,v, so N(r)-{p} is again a clique. Otherwise r,t,p form a
triangle and neither r nor t sees w. Put

    R_U=N(r) intersect U,    T_U=N(t) intersect U.

Both sets are nonempty. If one contains the other, rp or tp has its
other neighbours in a clique. For tp we may first assign all X to B;
this keeps the selected root and an actual A–B contact through U.
If the sets are incomparable, they are {u} and {v}, after relabelling.
Then ru and tv are contractible, since the other two neighbours of each
root are adjacent. For ru use bags (A-X) union {r} and (B-X) union {t,p},
selecting r,t as their roots and omitting A's former selected root.
They are connected through ru and tpw, and rt supplies their mutual
contact. Both retain their outside contacts to the other two bags.
For tv reverse r,t. At most one of u,v is a terminal, so one of these
contractions is T-legal. This is the final contradiction.

## 5. Cuts through a selected root

Take an internal edge ap, where a is the selected root of A and p is a
nonterminal. In an obstructing cut {a,p,z}, the two K4 bags containing
none of these three vertices lie in one component. Every other component
has at most one selected root. If it has one, its bag must contain z:
otherwise it cannot meet the two untouched outside bags. Sections 3–4
therefore make every such component a subset of T.

We first exclude a component {b,t} with two terminals. Its selected root
b has a bag B containing z. In particular z is a nonterminal. The roots
b,t are adjacent, and each has at least two neighbours in {a,p,z}.
Initially put both in B; A remains connected through ap and B through z.

When both neighbour sets have two elements, their union is {a,p,z}; write them
as {s,i} and {s,j}. The edges bi and tj are contractible, since each
endpoint's other two neighbours are adjacent. At least one of i,j is
not the terminal a. If that port is z, the contraction is internal to B.
If it is p, move its incident root into A and keep the other root in B;
the latter sees z, and bt supplies A–B. Select b,t instead of a,b.

If one root sees all three boundary vertices, and the other misses z,
contract the full root to z: its other neighbours form the triangle on
a,p and the other root. If the other root sees z, its edge to z is
contractible instead. When both see all three, either edge to z works.
All selected edges have a nonterminal end and preserve a four-of-five
K4 model. Thus two-terminal components are impossible.

Every remaining small component is consequently a singleton s. It has

    N(s)={a,p,z}.

The edge sz is contractible because ap is an edge. If s is a selected
root, its bag must extend through z: a singleton bag meeting only the
owners of a,p and of z cannot have three clique contacts. Thus z is in
its bag and, by minimality, must be the other terminal there. If s=t,
Section 3 already gives z in R.

## 6. The final contradiction

First suppose a K4 model leaves its omitted terminal t unused. Any
nonsingleton bag has an edge ap as in Section 5. Its singleton obstruction
cannot be a selected root, since no bag contains a second terminal.
It is therefore t, whose degree-three neighbourhood has two terminals
and a unique nonterminal p. Two different nonsingleton bags would require
this same p. At least three bags are singleton terminals, giving a
triangle in F[T]. Hence every K4 model uses its omitted terminal.

Choose such a model, with selected root b and omitted root t in the same
bag B. For a nonsingleton outside bag A, Section 5 supplies a singleton
obstruction s. If s is selected, it must be b and its opposite port is t.
If s is omitted, it is t; its only possible neighbour within B is z,
so z is b. Thus, writing {s,s'}={b,t},

    N(s)={a,p,s'},    p in A-T.

In particular s has only the neighbour s' within B. Two nonsingleton
outside bags would need different obstructions, because p is the unique
nonterminal neighbour of s. Then b,t both have degree one within B,
forcing B={b,t}. Their displayed neighbourhoods meet only those two
outside bags, so B misses the fourth bag. This is impossible.

There cannot be zero nonsingleton outside bags, since their three selected
roots would form a triangle. There is therefore exactly one, A; call
the other singleton bags C,D. Change B's selected root to s', omitting s.
The connected set B-{s} retains both its contacts to C,D. If it consists
only of s', those three terminals form a triangle. Otherwise s' has a
nonterminal neighbour q in B-{s}.

Apply Section 5 to the internal edge s'q. A selected singleton obstruction
would require a second terminal in its own bag, but none of the outside
bags has one. The omitted singleton s cannot be isolated either: its two
distinct neighbours a,p are both in A, whereas the cut already uses
s',q in B and has only one further vertex. Two-terminal components were
excluded above. Thus s'q has no obstructing three-cut and is contractible.
It is T-legal and preserves the current K4 model, contradicting minimum
order. This proves the theorem.

## 7. Colourful sets and the double-critical branch

A set C is *colourful in every k-colouring* if every colour class of every
proper k-colouring meets C. We use Martinsson–Steiner,
[Theorem 1.3](https://arxiv.org/html/2209.00594v1): a set colourful in
every four-colouring of a four-chromatic graph roots a K4 minor, with one
member of the set in each bag. Its representatives are not prescribed.

**Corollary.** If H is three-connected and five-chromatic, and C is
colourful in every five-colouring, H has a W4 model with all five bags
meeting C.

Fix a five-colouring and a whole class I. The graph H-I is four-chromatic,
and C-I is colourful in every four-colouring: otherwise adjoining I as
a fifth class contradicts the hypothesis on C. Martinsson–Steiner gives
four C-I-rooted K4 bags. Choose c in C intersect I. The theorem applied
to these four representatives and c gives the required wheel.

**Corollary.** Let G be five-connected and seven-chromatic. If xy is an
edge and chi(G-{x,y})=5, then G has a K7-2K2 minor.

Put H=G-{x,y} and C=N_G(x) intersect N_G(y). The graph H is
three-connected. In every five-colouring of H, C meets every class.
Indeed, if class i misses C, recolour its x-neighbours with a fresh sixth
colour, give x colour i and y colour six. The recoloured vertices are
independent and miss y, giving a forbidden six-colouring of G.
The preceding corollary gives five wheel bags in H, each meeting C.
The adjacent singleton bags x,y are full to all five, yielding
K2 join W4 = K7-2K2.

This closes the chi(G-{x,y})=5 branch in the current two-triangle
critical-host campaign. The alternative value six, Conjecture 19,
Conjecture 21 and HC7 remain unproved.
