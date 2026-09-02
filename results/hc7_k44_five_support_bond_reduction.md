# Five-support bond reductions for a literal `K_{4,4}` blocker

**Status.** Written unbounded theorem; separate hash-pinned internal audit
GREEN.  The
results below reduce the nonsingleton literal-core partition problem to three
block structures and to a standard parity-bond obstruction.  They do not
prove that the required bond exists, and they do not prove the weighted
splitter theorem, the literal case of T44, T44, Conjecture 21, or `HC_7`.

## 1. Abstract setting

Let `X` be a finite simple graph.  Let

\[
 R_a,R_b,R_1,\ldots,R_5\subseteq V(X)
\]

be the supports of seven boundary vertices.  For a nonempty set
`W subseteq V(X)`, put

\[
 \lambda(W)=|N_X(W)|+
   |\{d\in\{a,b,1,\ldots,5\}:R_d\cap W\ne\varnothing\}|
\]

and

\[
 q(W)=|N_X(W)|+
   |\{i\in\{1,\ldots,5\}:R_i\cap W\ne\varnothing\}|.       \tag{1}
\]

A **bond** below means an ordered partition

\[
                       V(X)=U\mathbin{\dot\cup}V             \tag{2}
\]

into two nonempty sets such that both `X[U]` and `X[V]` are connected.
Write

\[
 s(U,V)=|\{i:R_i\cap U\ne\varnothing\ne R_i\cap V\}|.       \tag{3}
\]

Call (2) **closing** if, after orienting it so that `U` meets `R_a`,

\[
 s(U,V)\ge
 \begin{cases}
 3,&R_b\cap V\ne\varnothing,\\
 4,&R_b\cap V=\varnothing.
 \end{cases}                                                \tag{4}
\]

By the audited two-helper theorem and split-count identity, a closing bond
in the minimum blocker gives an explicit `K_7^-` minor in the original
graph.

## 2. Eliminating the two distinguished supports

### Lemma 2.1 (six-boundary inequality)

Suppose

1. `lambda(W)>=7` for every nonempty proper connected `W subset V(X)`; and
2. `lambda(W)>=8` whenever such a set `W` meets both `R_a` and `R_b`.

Then

\[
                              q(W)\ge6                        \tag{5}
\]

for every nonempty proper connected `W subset V(X)`.

#### Proof

The two distinguished supports contribute at most two to `lambda(W)`.  If
`q(W)<=4`, then `lambda(W)<=6`, contrary to the first hypothesis.  If
`q(W)=5`, the first hypothesis forces `W` to meet both distinguished
supports, but then `lambda(W)=7`, contrary to the second hypothesis.  Hence
(5) holds.  \(\square\)

This is the exact point at which minimum-blocker strictness is used.  It
turns the seven-boundary system with two distinguished supports into a
six-boundary system involving only the five supports that must be split.

## 3. A six-connected augmentation and its exact rooted meaning

Let `Q={q_1,...,q_5}` be disjoint from `V(X)`.  Form `J` from `X` by making
`Q` a clique and joining `q_i` precisely to the vertices of `R_i`.

### Theorem 3.1 (augmentation equivalence)

The graph `J` is six-connected if and only if all of the following hold:

1. `X` is connected;
2. `|R_i|>=2` for every `i`; and
3. (5) holds for every nonempty proper connected `W subset V(X)`.

When these equivalent conditions hold, moreover, the following statements
are equivalent.

1. `X` has a bond which splits at least four of `R_1,...,R_5`.
2. `J` has a `K_7^-` minor model in which the five vertices of `Q` are five
   singleton branch sets.

#### Proof

Suppose first that `J` is six-connected.  Deleting `Q` shows that `X` is
connected.  Since each `q_i` already has four neighbours in `Q`, minimum
degree six gives `|R_i|>=2`.  For a proper connected `W subset V(X)`,

\[
 N_J(W)=N_X(W)\mathbin{\dot\cup}
        \{q_i:R_i\cap W\ne\varnothing\}.                    \tag{6}
\]

If this set had order at most five, then `N_X(W)` would be nonempty and at
least one vertex of `Q` would remain outside it.  Thus (6) would separate
`W` from that vertex, contrary to six-connectivity.  This proves (5).

Conversely, let `T` have order at most five.  If `Q subseteq T`, then
`T=Q` and `J-T=X` is connected.  Otherwise all surviving vertices of `Q`
lie in one component of `J-T`.  If another component exists, its vertex set
`W` lies in `X-T`, is connected, and satisfies `N_J(W) subseteq T`.  It is
proper in `X`: if `W=X`, a surviving `q_i` meets its nonempty support and
joins `W` to the component containing `Q`.  Equation (6) now gives
`q(W)<=|T|<=5`, contrary to (5).  Hence `J-T` is connected, and `J` is
six-connected.

For a bond `(U,V)`, use `U,V` and the five singleton vertices of `Q` as
branch sets.  There are ten contacts inside `Q`, one between `U,V`, and
`5+s(U,V)` contacts from the two exterior sets to `Q`.  Thus the quotient
has

\[
                             16+s(U,V)                         \tag{7}
\]

contacts, at least twenty exactly when `s(U,V)>=4`.

For the converse, let the two branch sets other than the five `Q` singletons
be `A,B subseteq V(X)`.  If they are not adjacent, the twenty-contact
condition forces both to meet all five supports.  Since `X` is connected,
grow them along a shortest path until they become adjacent.  Once they are
adjacent, assign every component of the unused part of `X` wholly to a side
which it meets.  This gives a bond and does not destroy any contact with
`Q`.  Its quotient still has at least twenty contacts, so (7) gives
`s(U,V)>=4`.  \(\square\)

The six-connected reformulation is exact, but it is not by itself a
solution: the generic rooted conclusion in Theorem 3.1 is false.  An
explicit counterexample is recorded in the adjacent
[rooted-extension barrier](../barriers/hc7_k44_sixconnected_k5_rooted_extension_barrier.md).
In particular, one must retain the additional minimum-blocker structure.

## 4. Minimum support-full sides

Assume for this section that

1. `X` is three-connected and `delta(X)>=4`;
2. a specified vertex `p` belongs to `R_a`, and `|R_i|>=2` for
   `1<=i<=5`; and
3. (5) holds for every nonempty proper connected set.

A side `U` of a bond `(U,V)` is **support-full** if it meets every `R_i`.
Such a bond with `p in V` exists: three-connectivity makes
`(X-p,{p})` a bond, and support multiplicity makes its first side
support-full.  Among the bonds with support-full first side and `p in V`,
choose one with `|U|` minimum, and put

\[
 B=N_X(V)\cap U,
 \qquad
 M=\{x\in B:X[U-x]\text{ is connected}\}.                  \tag{8}
\]

When `|U|>=2`, the vertices of `M` are precisely the non-cutvertices of
`X[U]` which have a neighbour in `V`.  The singleton case is excluded at
the start of the proof below.

### Theorem 4.1 (minimum-side block reduction)

If `X` has no closing bond, then `X[U]` has a cutvertex.  Its block-cut tree
has one of the following three forms.

1. It has two leaf blocks, both with a singleton lobe.  The graph `X[U]` is
   a path, possibly with one path edge replaced by a triangle.
2. It has two leaf blocks, one with a singleton lobe and the other a
   triangle whose two non-cutvertices form its lobe.  The graph `X[U]` is
   that triangle with a pendant path attached at its cutvertex.
3. It has three leaf blocks, each with a singleton lobe.  The graph `X[U]`
   is a subdivided claw, possibly with its central vertex replaced by a
   triangle.

In every case `2<=|M|<=s(U,V)<=3`.  In outcome 1 there are two members of
`M`; there may be a third exactly when one internal path edge is replaced by
a triangle.  In outcomes 2 and 3, `|M|=s(U,V)=3`.  Each `x in M` is the
unique vertex of `U` in a distinct split support.  A singleton leaf-lobe
vertex has at least three neighbours in `V`.  More generally, every vertex
`u in U` has a neighbour in `V`, and

\[
                         |N_X(u)\cap V|\ge4-d_{X[U]}(u).       \tag{11}
\]

If `U` meets `R_b`, only the triangle-free instance of outcome 1 is
possible: `X[U]` is a path and `|M|=s(U,V)=2`.

#### Proof

Put `s=s(U,V)`.  The side `V` meets `R_a` at `p`.  If `s>=4`, orient the
bond with `V` first; it is closing regardless of the `R_b` incidence on
`U`.  Thus `s<=3`.  If `U` meets `R_b`, the same orientation is already
closing when `s>=3`, so in that case `s<=2`.

If `|U|=1`, support multiplicity makes all five supports split, contrary to
the assumption.  Thus `|U|>=2`.

For each `x in M`, the partition `(U-x,V union {x})` is a bond with a
smaller first side.  Minimality says that this side misses some support,
say `R_{i(x)}`.  Consequently

\[
                         R_{i(x)}\cap U=\{x\}.                \tag{9}
\]

Support multiplicity makes `R_{i(x)}` meet `V`, so it is split by `(U,V)`.
Different vertices of `M` give different supports in (9).  Therefore

\[
                              |M|\le s\le3.                   \tag{10}
\]

Suppose first that `X[U]` has no cutvertex.  Then `M=B`.  If `U-B` is
nonempty, `B` separates it from `V`, so three-connectivity and (10) give
`|B|=s=3`.  The three supports in (9) are then all the split supports.  A
component `W` of `X[U-B]` meets none of them and at most the two supports
contained wholly in `U`, while `N_X(W) subseteq B`.  This gives `q(W)<=5`,
contrary to (5).  Hence `U=B`, and (10) gives `|U|<=3`.

If `|U|=2`, the total number of incidences of the five supports with `U` is at
least

\[
                            2(5-s)+s=10-s\ge7.
\]

One vertex of `U` therefore lies in at least four supports, and its
singleton bond splits those supports.  If `|U|=3`, the absence of a
cutvertex makes `X[U]` a triangle.  Now `B=U` and `s=3`; the three split
supports have the three distinct vertices of `U` as their unique
`U`-vertices.  The other two supports have order at least two inside the
three-set `U`, so they intersect at a vertex `x`.  The bond
`(V union {x},U-x)` splits those two supports and the two split supports
whose unique `U`-vertices are different from `x`.  It therefore splits four
supports.  Every possibility contradicts the assumption.  Thus `X[U]` has
a cutvertex.

Use the standard block-cut tree of `X[U]`, with bridges included as
two-vertex blocks.  Every leaf block with attachment cutvertex `c` has an
edge from its lobe to `V`; otherwise `c` separates that lobe in `X`.  Its
endpoint in the lobe belongs to `M`.  Therefore the number of leaf blocks is
at most three.

We next show that every non-cutvertex of `X[U]` belongs to `M`.  Let `Q` be
a block, let `C_Q` be the set of cutvertices of `X[U]` which lie in `Q`, put
`t=|C_Q|`, and put

\[
 I_Q=V(Q)-C_Q,
 \qquad M_Q=M\cap I_Q.
\]

Every component of the block-cut tree incident with `Q` contains a leaf
block and hence a member of `M` outside `I_Q`.  Thus

\[
                              t+|M_Q|\le|M|.                  \tag{12}
\]

If `I_Q-M_Q` is nonempty, take a component `W` of its induced subgraph.
It has no neighbour in `V`, and block structure gives

\[
                       N_X(W)\subseteq C_Q\cup M_Q.           \tag{13}
\]

The `|M|` distinct supports selected in (9) avoid `W`, so `W` meets at most
`5-|M|` supports.  Equations (12)--(13) give

\[
             q(W)\le t+|M_Q|+5-|M|\le5,
\]

again contradicting (5).  Hence `I_Q=M_Q` for every block.

There are at least two leaf blocks.  Together with (10), the last conclusion
leaves only the following possibilities.  With two leaf blocks, the
block-cut tree is a path.  Each leaf lobe is a singleton, except that one of
them may have two vertices; in the latter case its block is a triangle.
Every internal block is a bridge, except that when both leaf lobes are
singletons there may be one triangle with one non-cutvertex.  These are
outcomes 1 and 2.  With three leaf blocks, each lobe is a singleton and the
block-cut tree has a unique node of degree three.  If that node is a
cutvertex, the graph is a subdivided claw.  If it is a block, that block has
three cutvertices and no other vertex, so it is a triangle.  This is outcome
3.

Finally, each of the three displayed graphs has maximum degree at most three.
Minimum degree four in `X` therefore gives (11), and in particular every
vertex of `U` has a neighbour in `V`.  A singleton leaf-lobe vertex has only
its attachment cutvertex as a neighbour in `U`, so it has at least three
neighbours in `V`.  All remaining assertions follow from (9)--(10).  If
`U` meets `R_b`, then `s<=2`; since there are at least two leaf blocks,
`2<=|M|<=s` forces `|M|=s=2`.  The classification then leaves only a path
with no replaced edge.
\(\square\)

The theorem does not say that examining one chosen minimum side is enough.
The [bounded spanning-split experiment](../active/experiments/k44_literal_spanning_split_search/README.md)
contains a four-connected order-eight instance whose unique minimum
support-full side is a three-vertex path with split count three, even though
that same side is already closing by the correct `a,b` orientation.  Thus
minimum-side structure alone does not force two-connectivity or four split
supports; the three block forms must be analysed together with the full
incidence and orientation data.

## 5. Parity bonds from rainbow support paths

We use Chen--Ding--Yu--Zang,
[*Bonds with Parity Constraints*](https://www.math.lsu.edu/~ding/bonds.pdf),
Journal of Combinatorial Theory, Series B 102 (2012), 588--609.  Their
Theorem 1.2 says that a nontrivial acyclic triple of even vertex sets in a
two-connected graph either has a bond meeting all three sets oddly on both
sides or is weakly linkable in their precise sense.  Their Theorem 1.1
specializes in a four-connected graph to a facial-cycle obstruction.

### Theorem 5.1 (rainbow support path)

Suppose `X` is two-connected.  Let `x_0,...,x_4` be distinct vertices with
`x_0 in R_a` and `x_4 in R_b`.  Suppose four distinct indices
`i_1,...,i_4` satisfy

\[
             \{x_{j-1},x_j\}\subseteq R_{i_j}
             \quad(1\le j\le4).                              \tag{14}
\]

Then either `X` has a closing bond, or the parity quadruple

\[
 (X;\{x_0,x_1\},\{x_1,x_2\},\{x_2,x_3\})                   \tag{15}
\]

is weakly linkable in the sense of Chen--Ding--Yu--Zang.  In particular, if
`X` is four-connected and nonplanar, (14) always gives a closing bond.

#### Proof

The three two-element sets in (15) are nonempty, and their symmetric
difference is `{x_0,x_3}`.  Thus the quadruple is nontrivial and acyclic.
By Theorem 1.2 of the cited paper, it is weakly linkable or has a feasible
bond.

In a feasible bond, `x_0,x_1,x_2,x_3` alternate sides.  If `x_4` is opposite
`x_3`, all four supports in (14) split.  If `x_4` is on the same side as
`x_3`, then `x_0,x_4` are opposite; orient the `x_0` side first.  It meets
`R_a`, the other side meets `R_b`, and the first three supports in (14)
split.  The bond is closing in either case.

When `X` is four-connected, the specialization of Theorem 1.1 in the cited
paper says that an infeasible nontrivial acyclic quadruple has a plane
representation in which the triple is linked by a facial cycle.  This is
impossible when `X` is nonplanar.  Hence the feasible outcome holds.
\(\square\)

### Corollary 5.2 (rainbow support cycle)

Let `X` be two-connected.  Suppose distinct vertices `x_0,...,x_3` and
distinct indices `i_1,...,i_4` satisfy

\[
 \{x_0,x_1\}\subseteq R_{i_1},\quad
 \{x_1,x_2\}\subseteq R_{i_2},\quad
 \{x_2,x_3\}\subseteq R_{i_3},\quad
 \{x_3,x_0\}\subseteq R_{i_4}.                              \tag{16}
\]

Then either a bond splits all four displayed supports, or the quadruple
(15) is weakly linkable.  In particular, the splitting bond exists whenever
`X` is four-connected and nonplanar.

#### Proof

Apply the same parity theorem to the first three pairs.  A feasible bond
makes `x_0,x_1,x_2,x_3` alternate sides and therefore also separates
`x_3,x_0`.  The rest follows exactly as in Theorem 5.1.  \(\square\)

### Lemma 5.3 (a facial obstruction must have an off-cycle support)

Let `X` be a finite simple four-connected plane graph, let `C` be a facial
cycle, and suppose (5) holds.  Then the five supports are not all contained
in `V(C)`.

#### Proof

Make the face bounded by `C` the outer face.  Put `n=|V(X)|`, `h=|V(C)|`,
and `e=|E(X)|`, and let `f` be the number of bounded faces.  Every bounded
face has length at least three, so

\[
                         2e-h\ge3f.
\]

Euler's formula gives `f=e-n+1`, and hence `e<=3n-h-3`.  Consequently

\[
 \sum_{v\notin V(C)}(6-d_X(v))+
 \sum_{v\in V(C)}(4-d_X(v))
       =6n-2h-2e\ge6.                                      \tag{17}
\]

Four-connectivity gives `delta(X)>=4`, so every summand in the second sum
is nonpositive.  Equation (17) first shows that there is a vertex outside
`C`, and then shows that some such vertex `v` has `d_X(v)<=5`.  If every
support were contained in `V(C)`, the singleton `{v}` would meet no support,
and therefore `q({v})=d_X(v)<=5`, contrary to (5).  \(\square\)

Thus the four-connected planar alternative is not an arbitrary planar
residue.  In any facial-cycle obstruction compatible with (5), at least one
of the five supports extends away from the obstructing face.

### Corollary 5.4 (a mixed three-support parity certificate)

Suppose `X` is two-connected.  Let `i,j,k` be three distinct indices and
choose two-element sets

\[
 A_i\subseteq R_i,\qquad A_j\subseteq R_j,\qquad A_k\subseteq R_k.
\]

Suppose `A_i={x,y}`, where `x in R_a`, `y in R_b`, and `x ne y`.  If

\[
                         A_i\mathbin{\triangle}A_j
                         \mathbin{\triangle}A_k\ne\varnothing,             \tag{18}
\]

then either `X` has a closing bond or the quadruple
`(X;A_i,A_j,A_k)` is weakly linkable.  In particular, if `X` is
four-connected and nonplanar, it has a closing bond.

#### Proof

Condition (18) makes the nontrivial parity quadruple acyclic.  If it is not
weakly linkable, Theorem 1.2 of Chen--Ding--Yu--Zang gives a feasible bond.
That bond separates the two vertices of each `A`-set, so it splits the three
distinct supports.  It also separates `x` from `y`; orienting the `x`-side
first makes the first side meet `R_a` and the second meet `R_b`.  Hence the
bond is closing.  In a four-connected nonplanar graph, Theorem 1.1 excludes
the weakly-linkable facial alternative.  \(\square\)

### Corollary 5.5 (mixed-support exclusion in the nonplanar case)

Suppose `X` is four-connected and nonplanar, all five supports have order at
least two, and `X` has no closing bond.  Then no support `R_i` contains
distinct vertices

\[
                         x\in R_a\cap R_i,
                         \qquad y\in R_b\cap R_i.             \tag{19}
\]

#### Proof

Suppose (19) holds and put `A_i={x,y}`.  Choose three indices other than
`i`, and from each corresponding support choose an arbitrary two-element
set `B_1,B_2,B_3`.  Some pair `B_r,B_s` satisfies
\(A_i\mathbin{\triangle}B_r\mathbin{\triangle}B_s\ne\varnothing\).
Otherwise
\(B_1\mathbin{\triangle}B_2=A_i=B_1\mathbin{\triangle}B_3\), so
`B_2=B_3`, contradicting
\(B_2\mathbin{\triangle}B_3=A_i\).  Corollary 5.4 applied to
`A_i,B_r,B_s` gives a closing bond.  \(\square\)

## 6. Exact remaining statement

For the nonsingleton literal blocker, Theorems 4.1 and 5.1 leave one precise
unbounded task:

> **Leaf-block completion lemma.**  Under the full hypotheses and exact
> three-cut profiles of the audited minimum-blocker theorem, eliminate the
> three block forms in Theorem 4.1 by producing a closing bond.  One possible
> route is to find a rainbow support path as in Theorem 5.1 and exclude its
> weakly-linkable obstruction using those block and three-cut profiles.  In
> the four-connected planar case, Lemma 5.3 guarantees an off-face support
> which the completion argument may exploit; in the nonplanar case,
> Corollary 5.5 forbids every mixed support of the form (19).

This is strictly narrower than the former arbitrary spanning-partition
problem.  It still requires a global argument involving the complementary
side `V`: the explicit order-eight minimum-side example shows that the
internal block structure of `U` alone cannot finish the proof.
