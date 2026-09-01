# Safe contraction or a tight singleton in a literal `K_{4,4}` exterior

**Status.** Written unbounded reduction with one computer-assisted finite
lemma.  The adjacent audit identifies the exact checked revisions and the
finite trust boundary.  This result does not prove the weighted splitter
theorem, the literal case of T44, T44, Conjecture 21, or `HC_7`.

## 1. Setting and statement

Let `G` be a finite simple seven-connected graph with no `K_7^-` minor.  Let
`G` contain a specified literal `K_{4,4}` on vertex set `S`, put `C=G-S`,
and assume `|V(C)|>=7`.  Extra edges inside the displayed core are allowed.
For `v in V(C)`, put

\[
                 L(v)=N_G(v)\cap S,
\]

and, for every nonempty `X subseteq V(C)`, put

\[
 L(X)=\bigcup_{x\in X}L(x),\qquad
 w(X)=|L(X)|,\qquad
 \lambda(X)=|N_C(X)|+w(X).                           \tag{1}
\]

Seven-connectivity gives

\[
                         \lambda(X)\ge7              \tag{2}
\]

for every nonempty `X`, including `X=V(C)`.  The promoted exterior theorem
makes `C` three-connected.  An edge of `C` is **three-contractible** if its
contraction, after simplifying parallel edges, is three-connected.  It is
**safe** if the union-labelled contraction also preserves every inequality
(2).

A nonempty set `A subseteq V(C)` is an **all-edge tight atom** if

1. `lambda(A)=7`;
2. `N_C(A)` contains both ends of a three-contractible edge; and
3. `A` has minimum order among all sets satisfying 1 and 2.

The minimum is taken over the ends of every three-contractible edge, not over
the edges of one preselected spanning tree.

### Theorem 1.1 (all-edge atom reduction to a singleton)

If `C` has no safe three-contractible edge, then it has an all-edge tight atom
`A`.  Put

\[
        r=|A|,\qquad B=N_C(A),\qquad Q=L(A),\qquad q=|Q|.
\]

It may be chosen so that all of the following hold.

1. `C[A]` and `C-A` are connected,

   \[
       1\le r\le3,\qquad 4\le|B|\le7,\qquad
       q=7-|B|\le3.                                  \tag{3}
   \]

2. Fix any three-contractible edge `xy` in `B`.  For every nonempty proper
   `Y subset A`,

   \[
    |B-(N_C(Y)\cap B)|+|Q-L(Y)|
       \le |N_{C[A]}(Y)|,                             \tag{4}
   \]

   and the right side may be decreased by one when `Y` is adjacent to both
   `x` and `y`.

3. Let `ab` be any three-contractible edge crossing from `a in A` to
   `b in B`, and let `X` be any connected tight blocker of `ab`; that is,

   \[
       X\subseteq V(C)-\{a,b\},\qquad
       a,b\in N_C(X),\qquad \lambda(X)=7.
   \]

   Then

   \[
      A\subseteq N_C(X),\qquad
      |\partial A\cap\partial X|\le7-2r,\qquad
      |X\cap B|\ge r,                                \tag{5}
   \]

   where `partial Z=N_C(Z) dotcup L(Z)` in the common resource universe
   `V(C) dotcup S`.

4. If `r=3`, put `P=X cap B` for a blocker in item 3.  Then

   \[
       |P|=3,\qquad \partial A\cap\partial X=\{b\}.   \tag{6}
   \]

   With

   \[
       B_0=B-(P\cup\{b\}),\qquad
       D=N_C(X)-(A\cup\{b\}),
   \]

   one has

   \[
   \begin{gathered}
      |B_0|=3-q,\qquad |D|+w(X)=3,\\
      N_C(A\cup X)=(B-P)\mathbin{\dot\cup}D,
      \qquad \lambda(A\cup X)=7.                    \tag{7}
   \end{gathered}
   \]

5. In fact,

   \[
                              r=1.                   \tag{8}
   \]

6. If `r=1`, then for every three-contractible edge `xy` in `B` there is a
   spanning partition of `C` into three connected pairwise adjacent bags
   rooted at `A,x,y` with the exact portal restrictions in Corollary 5.1
   below.

   Moreover, `Z=B dotcup Q=N_G(A)` is an exact seven-cut.  It has a
   bipartition of orders three and four which extends the two literal-core
   shores on `Q`; in particular,

   \[
                              \delta(G[Z])\le3.       \tag{16}
   \]

7. Let `ab` be a three-contractible edge from the singleton `A=\{a\}` to
   `b in B`, and let `X` be a connected tight blocker.  The resources of
   `Z=B dotcup Q` and `partial X` have the exact decomposition in
   Proposition 7.1.  In particular, the portions of `Z` lying in `X` and on
   the opposite side of `partial X` are both nonempty, and the overlap of
   `Z` with `partial X` is exactly the single exterior vertex `b`.  The
   blocker boundary is itself a bipartite exact seven-cut with shore orders
   three and four.  If `X cap B` has at least two vertices, at least two of
   them are non-cutvertices of `G[X]`.

8. If a blocker in item 7 is itself a singleton `X=\{p\}`, then the two
   exact neighbourhoods have the overlap form in Proposition 7.2.  Their
   unique common resource is the exterior vertex `b`, and the two singleton
   atoms have disjoint label sets.  This common neighbour satisfies the two
   three-portal union bounds in (26).

9. Every prescribed omitted portal satisfies the linkage-or-exact-cut
   dichotomy in Proposition 7.3.  If `q>=1`, either such a new exact
   seven-cut occurs or `G[Z]` has a component disjoint from `Q` whose two
   bipartition classes have nonzero odd difference in order.

Consequently, failure of a safe contraction has been reduced to a singleton
atom with an exact spanning three-bag portal profile.  Its complement is
connected, and its seven-vertex neighbourhood is bipartite with shore orders
three and four.

The new conclusions relative to the preceding small-atom reduction are the
trace lower bound in (5), connectedness of `C-A`, the exact equality
`|P|=3`, the elimination of every positive-weight two- or three-vertex atom,
the literal-core linkage which eliminates the remaining unlabelled
non-singleton atoms, the exact singleton profile in Corollary 5.1, and the
reduction of every crossing blocker to one-resource overlap together with a
bipartite exact boundary in Proposition 7.1.  Proposition 7.3 further
converts every failed prescribed portal omission into an exact seven-cut.

## 2. Selecting the atom over all contractible edges

For clarity, the exact obstruction to safety is recalled first.  If `uv` is
three-contractible, its union-labelled contraction violates (2) exactly when
there is a nonempty

\[
                     X\subseteq V(C)-\{u,v\}
\]

with `u,v in N_C(X)` and `lambda(X)=7`.  Sets containing the contracted
vertex preserve the boundary and label union of their preimage; a set
avoiding it loses one boundary vertex exactly when both `u,v` were in its
old boundary.  This includes co-spanning blockers.

We use the augmented graph from the audited small-atom theorem.  Add the
eight label vertices, make them a clique, join them to `C` according to the
labels, and add a clique of `|V(C)|` ballast vertices adjacent to every label
vertex and to no vertex of `C`.  Call the resulting graph `J`.  Inequality
(2) says that `J` is at least seven-connected, and every tight blocker is a
seven-separator fragment on the `C` side.  The blockers below therefore make
`kappa(J)=7`.

Let `mathcal E` be the family of endpoint pairs of all three-contractible
edges of `C`.  Since `G` is target-free, the audited four-portal triangle
theorem excludes a triangle of three disjoint connected exterior bags of
weight at least four.  The Costalonga argument in the preceding reduction
therefore gives a spanning tree of three-contractible edges.  In particular,
the graph with edge set `mathcal E` is connected.  The no-safe-edge
hypothesis puts every member of `mathcal E` in a minimum separator of `J`.

Choose a minimum `mathcal E`-fragment of `J`.  The ballast comparison in the
preceding theorem puts it wholly in `C`, and the tight-component lemma makes
it connected; call it `A`.  It is precisely an all-edge tight atom in the
language of Section 1.

For any contractible edge `ab` incident with `A` and any connected blocker
`X`, Mader's generalized atom lemma, applied in `J`, gives

\[
              A\subseteq N_C(X),\qquad
              |\partial A\cap\partial X|\le7-2|A|.  \tag{9}
\]

Because the contractible-edge graph is connected and `A` is nonempty and
proper, at least one such edge crosses `A`.  Applying (9) to that edge gives
`r<=3`.  The boundary of `A` contains a contractible edge `xy`.  If
`|B|<=3`, then `|A union B|<=6<|V(C)|`; after contracting `xy`, the image of
`B` would be a separator of order at most two.  Thus `|B|>=4`, which proves
(3).

The resource count for a proper nonempty subset of `A` proves (4), exactly as
in the preceding theorem.  If equality held for a set seeing `x,y`, that set
would be a smaller all-edge tight set whose boundary contains `xy`.

We now use the extra strength of minimising over all contractible edges.
Mader's trace lemma says that if `A` is a `mathcal E`-atom and `F` is a
`mathcal E`-fragment with `A subseteq N_J(F)`, then

\[
                         |F\cap N_J(A)|\ge|A|.        \tag{10}
\]

Apply (10) to the connected blocker `X`.  Since `X subset C` and
`N_J(A) cap C=B`, it gives `|X cap B|>=r`, completing (5).

Suppose `r=3`.  For a crossing edge, its outside end `b` lies in the
intersection in (9), so that intersection is exactly `{b}`.  Put
`P=X cap B`.  The boundary calculation from the preceding reduction gives

\[
                         \lambda(A\cup X)=10-|P|.    \tag{11}
\]

Inequality (2) and (10) give `|P|<=3` and `|P|>=3`, respectively.  Thus
`|P|=3`; separating the vertex and label resources in the two seven-element
boundaries gives every equality in (7).

It remains to prove that `C-A` is connected.  This is immediate from
three-connectivity when `r<=2`.  Let `r=3`, and let `H` be a component of
`C-A`.  A contractible spanning tree has an edge `ab` from `A` to `H`.
Every connected blocker `X` of this edge lies in `H`: it is disjoint from
`A`, connected, adjacent to `b in H`, and `b` itself is not in `X`.  By
(6), the component `H` contains the three vertices of `P=X cap B` and the
distinct vertex `b`.  Thus every component of `C-A` contains at least four
vertices of `B`.  Since `|B|<=7`, there is only one.  This completes all
claims of Theorem 1.1 except (8).

The trace lemma used here is Lemma 7.19 of Chan's dissertation
[*Contractible edges*](https://ediss.sub.uni-hamburg.de/bitstream/ediss/7445/1/Dissertation.pdf),
where it is attributed to Mader.  The generalized atom estimate (9), the
Costalonga input, and the full augmented-graph translation are pinned in the
adjacent audit of the preceding small-atom theorem.

## 3. An exact rooted marked partition

### Lemma 3.1 (exact marked rooted partition)

Let `D` be a `k`-connected graph, let `s_1,...,s_k` be distinct roots, let
`M subseteq V(D)`, and let `t_1,...,t_k` be positive integers with sum
`|M|`.  There is a partition

\[
                         V(D)=V_1\mathbin{\dot\cup}\cdots
                                  \mathbin{\dot\cup}V_k
\]

such that every `D[V_i]` is connected, `s_i in V_i`, and

\[
                             |V_i\cap M|=t_i
\]

for every `i`.

#### Proof

Replace every edge of `D` by its two orientations, delete the arcs leaving
the roots, and take the roots as sinks.  The Fan Lemma says that this digraph
is `k`-connected to the sink set in the sense of
Chen--Kleinberg--Lovasz--Rajaraman--Sundaram--Vetta.  Give demand one to each
vertex of `M` and zero to every other vertex.  Their Theorem 23 supplies a
confluent flow routing all demand to the sinks with

\[
                         C(s_i)<t_i+1.
\]

Delete any cyclic circulation.  Confluence then sends every unit-demand
origin along a unique path to one sink.  Each sink load is therefore the
integer number of marked origins assigned to it, including the sink itself
when that root is marked.  Hence it is at most `t_i`.  The loads sum to
`|M|=sum_i t_i`, so every load is exactly `t_i`.

For each sink, take the vertices on its positive-flow paths together with the
sink itself.  This is a connected set, and confluence makes the `k` sets
disjoint.  They contain every marked vertex, with the required counts.  Each
component of the unused vertices is mark-free.  Attach it wholesale to any
adjacent flow set.  Connectivity of `D` guarantees such an adjacency, and
these attachments give the required spanning partition without changing a
mark count.  \(\square\)

The external input is Theorem 23 of J. Chen, R. D. Kleinberg, L. Lovasz,
R. Rajaraman, R. Sundaram and A. Vetta,
[* (Almost) tight bounds and existence theorems for single-commodity
confluent flows*](https://www.cs.cornell.edu/~rdk/papers/conflu.pdf),
Journal of the ACM **54** (2007).  Its demand function is nonnegative, so
the zero demands used above are part of the stated theorem.

### Lemma 3.2 (representatives outside a labelled set)

Let `T` be a nonempty subset of `V(C)`, put `Q_0=L(T)` and `q_0=|Q_0|`, and
suppose `q_0<=7`.  There are `7-q_0` distinct vertices outside `T` carrying
`7-q_0` distinct labels outside `Q_0`.

#### Proof

Let `Omega_0=L(C)` and `m=|Omega_0|`.  In the incidence graph between
`Omega_0-Q_0` and `V(C)-T`, let `P(U)` be the vertex neighbourhood of a set
of labels `U`.  The set `Z=V(C)-P(U)` is nonempty because it contains `T`,
its graph boundary is contained in `P(U)`, and it uses no label of `U`.
Thus (2) gives

\[
                     |P(U)|\ge |U|-(m-7).
\]

The deficiency form of Hall's theorem gives a matching of size at least

\[
                  (m-q_0)-(m-7)=7-q_0,
\]

which is the required system of representatives.  \(\square\)

## 4. The finite seven-portal triangle theorem

### Lemma 4.1 (seven-portal triangle profile)

Let `H` be a literal `K_{4,4}` with vertex set `S`, and add three vertices
`z_1,z_2,z_3` which form a triangle.  Let `Q subset S`, where
`1<=q=|Q|<=3`, and suppose every vertex of `Q` is adjacent to at least two
of the `z_i`.  Choose `7-q` further vertices of `S-Q` and partition them
into three sets `R_1,R_2,R_3` whose sizes, in some order, are

\[
                             1,\quad1,\quad5-q.
\]

If `z_i` is adjacent to every member of `R_i`, then the resulting graph has
a `K_7^-` minor.

#### Computer-assisted proof

It suffices by monotonicity to retain only the displayed incidences.  For
each `q`, the verifier chooses `Q`, the one unused vertex of `S-Q`, the
ordered partition into the three prescribed group sizes, and independently
one of the four incidence sets

\[
             \{z_1,z_2\},\ \{z_1,z_3\},\
             \{z_2,z_3\},\ \{z_1,z_2,z_3\}
\]

for every member of `Q`.  It then quotients by
`Aut(K_{4,4}) times S_3`.  The exact counts are

| `q` | labelled profiles | after `S_3` | full orbits |
|---:|---:|---:|---:|
| 1 | 20,160 | 3,360 | 20 |
| 2 | 161,280 | 26,880 | 77 |
| 3 | 645,120 | 107,520 | 198 |

For every one of the 295 full-orbit representatives, the verifier enumerates
all 63,987 spanning partitions of the eleven vertices into seven nonempty
bags in restricted-growth order.  It records the first partition whose bags
are connected and whose quotient has at least twenty of the twenty-one
possible adjacencies.  Each recorded partition is therefore an explicit
`K_7^-` minor model.  The SHA-256 digest of the ordered 295 certificate
records is

```text
48afac546bfa7bb92768b77581a774eeb735faf477a870886ea03f02b3a2c3f5
```

The dependency-free verifier is
[`hc7_k44_positive_atom_elimination_verify.py`](hc7_k44_positive_atom_elimination_verify.py).
It regenerates the profiles, symmetry quotient and certificates and checks
the displayed counts and digest.  No bounded-order exterior enumeration is
used.  \(\square\)

### Lemma 4.2 (distinguished `5,1,1` profile)

Let `H` be a literal `K_{4,4}` and let `z_0,z_1,z_2` form a triangle.  Choose
seven distinct vertices of `H`.  Join five of them to `z_0`, one of the
remaining two to `z_1`, and the other to `z_2`.

Up to `Aut(K_{4,4})` and interchange of `z_1,z_2`, there are exactly three
profiles.  Two contain a `K_7^-` minor.  In the third, the singleton portals
belong to opposite shores of the `K_{4,4}`; this profile is target-free.
Moreover, in that third profile, adding an edge from either `z_1` or `z_2`
to any of the five portals assigned to `z_0` creates a `K_7^-` minor.

#### Computer-assisted proof

With the five-portal bag distinguished, there are 168 profiles after
interchanging the singleton bags and three full symmetry orbits.  Their
canonical representatives, written as eight-bit portal masks, are

```text
(31,32,64), (55,8,64), (55,64,128).
```

The first and third representatives have exact spanning seven-bag models;
the middle representative has none among all 63,987 spanning partitions and
is the opposite-shore singleton profile.  The compact certificate-record
digest is

```text
a0812a66b38384445f877fa4cac909b4bea11a13d36364643cf9e1100ae2c6e8
```

For `(55,8,64)`, the verifier separately checks all ten ways to add one of
the five bits of `55` to either singleton mask.  Every addition has an exact
spanning model; their record digest is

```text
ce2f0641c454480ccd151d3d4679cc320b7a15abfd7a559622273240893e8565
```

The same retained verifier as in Lemma 4.1 regenerates and checks this
classification.  The negative assertion is exact because every seven-bag
minor model in a connected eleven-vertex graph can be made spanning by
attaching each unused component to a neighbouring bag.  \(\square\)

## 5. Eliminating every positive atom of order two or three

Assume `r>=2` and, for a contradiction, `q>=1`.  Lemma 3.2 gives a set `M`
of `7-q` distinct vertices outside `A` which represent `7-q` distinct labels
of `S-Q`.

First let `A=\{u,v\}`.  Inequality (4) says that both `u` and `v` carry every
label of `Q` and each is adjacent to every vertex of `B` except possibly one
of `x,y`.  Since `|B|>=4`, they have a common neighbour `p in B`.  Apply
Lemma 3.1 in `C` with roots `u,v,p`, marked set `M`, and quotas

\[
                              1,\quad1,\quad5-q.
\]

The resulting three spanning connected bags are pairwise adjacent through
the triangle `uvp`.  Every label of `Q` occurs in both the `u`- and `v`-bags,
and the represented labels outside `Q` are split into groups of the displayed
sizes.  Contracting the three bags and applying Lemma 4.1 inside the literal
core gives a `K_7^-` minor in `G`, a contradiction.

Now let `r=3`.  If `C[A]` is a triangle, root the marked partition at its
three vertices.  Every two-set of atom vertices carries all of `Q` by (4),
so each label in `Q` occurs in at least two rooted bags.  Lemma 4.1 again
applies.

It remains only to check the contact between the endpoint bags when
`C[A]=u-v-w` is a path.  The local form of (4) says that both endpoints carry
all of `Q` and that each endpoint is adjacent to every member of `B` except
possibly one of `x,y`.  Apply Lemma 3.1 with roots `u,v,w` and the same
quotas, obtaining bags `U,V,W`.  The path edges give the `UV` and `VW`
contacts.  Every quota is positive, so `U` and `W` each contain a marked
vertex outside `A`.  On a path in `U` from `u` to such a vertex, let `b_u` be
the first vertex after leaving `A`; define `b_w in W` symmetrically.  Both
vertices lie in `B`.  If `u b_w` or `w b_u` is an edge, then `U` and `W`
touch.  Otherwise `b_u,b_w` are the two distinct exceptional vertices
`x,y`, and the edge `xy` again makes `U` and `W` touch.  The three bags
therefore form a triangle, each label of `Q` occurs in both endpoint bags,
and Lemma 4.1 gives the same contradiction.

Thus every atom of order at least two which survives this section is
unlabelled.  \(\square\)

### Corollary 5.1 (exact singleton enclosure profile)

Let `A=\{a\}` be the singleton atom in Theorem 1.1, and let `xy` be any
three-contractible edge in `B=N_C(a)`.  There is a spanning partition

\[
                      V(C)=V_a\mathbin{\dot\cup}V_x
                                  \mathbin{\dot\cup}V_y              \tag{12}
\]

into connected pairwise adjacent bags rooted respectively at `a,x,y`.
There are seven distinct selected portals split as

\[
                 R_a\mathbin{\dot\cup}\{s_x\}
                    \mathbin{\dot\cup}\{s_y\},\qquad |R_a|=5,       \tag{13}
\]

such that `R_a subseteq L(V_a)`, `s_x in L(V_x)`, and
`s_y in L(V_y)`.  In a target-free host, `s_x,s_y` lie on opposite shores
of the literal `K_{4,4}` and

\[
                 L(V_x)\cap R_a=L(V_y)\cap R_a=\varnothing.         \tag{14}
\]

In particular,

\[
                         L(V_x)\cap Q=L(V_y)\cap Q=\varnothing.     \tag{15}
\]

#### Proof

Lemma 3.2 gives `7-q` distinct representatives outside `A` for labels
outside `Q`.  Apply Lemma 3.1 with roots `a,x,y` and quotas

\[
                             5-q,\quad1,\quad1.
\]

These are positive because `q<=3`.  The three bags are pairwise adjacent
through the triangle `axy`.  Let `R_a` consist of `Q` together with the
`5-q` representative labels placed in `V_a`, and let `s_x,s_y` be the two
remaining representative labels.  This proves (12)--(13).  Lemma 4.2 says
that target-freeness forces `s_x,s_y` onto opposite shores.  Its ten
single-edge completion checks say that neither small bag can see any member
of `R_a`, proving (14).  Since `Q subseteq R_a`, equation (15) follows.
Finally, `Z=B dotcup Q=N_G(a)` is a seven-vertex separator between `a` and
the rest of `G`.  The promoted exact-seven-cut theorem gives
`delta(G[Z])<=3`, proving (16).  \(\square\)

### Corollary 5.2 (bipartite singleton neighbourhood)

Let the two shores of the displayed literal core be `S_0,S_1`.  The exact
neighbourhood

\[
                              Z=B\mathbin{\dot\cup}Q
\]

of the singleton atom has a bipartition `Z_0,Z_1` such that

\[
       Q\cap S_i\subseteq Z_i\quad(i=0,1),
       \qquad \{|Z_0|,|Z_1|\}=\{3,4\}.               \tag{17}
\]

#### Proof

Delete the `q` vertices of `Q`.  The graph `G-Q` is
`(7-q)`-connected, and `|B|=7-q`.  Menger's theorem gives `|B|` pairwise
vertex-disjoint paths from `B` to `S-Q`, with distinct ends and with their
interiors outside `B union (S-Q)`.  Every vertex of `B` is an end.  These
paths avoid `a`: in `G-Q` the only neighbours of `a` are the vertices of
`B`, all of which are already distinct path ends, so a path entering `a`
could not leave it without meeting a second path end.

Add the trivial one-vertex path at each member of `Q`.  We obtain seven
disjoint connected path bags indexed by `Z`, each adjacent to `a`, with
seven distinct ends in `S`.  Exactly one core vertex `s_0` is unused.  Give
`z in Z` the colour of the literal-core shore containing the end of its path
bag.  On `Q` this is the original shore colouring, and the two colour-class
orders are three and four.

Suppose an edge `zz'` of `G[Z]` has same-coloured ends.  Assume, after
exchanging the shores, that `s_0 in S_0`; the seven path ends then have shore
orders three and four.  Choose a path bag `D` ending in `S_1`, distinct from
the two chord-end bags if the chord also lies on the `S_1` side, and enlarge
`D` by `s_0`.  This enlarged bag is connected, adjacent to `a`, and universal
to the other six path bags.

The remaining six ends form a `K_{3,3}` and retain the same-shore chord
`zz'`.  On the shore of that chord there is a unique third vertex.  Contract
an edge from it to the opposite shore.  The five resulting path bags form a
`K_5^-`: the contracted bag is universal, while the other four bags induce
a `K_{2,2}` plus the chord.  Together with `\{a\}` and `D union \{s_0\}`,
which are adjacent to each other and universal to those five bags, the
quotient has `9+10+1=20` contacts.  This is a `K_7^-` minor, a contradiction.

Every edge of `G[Z]` therefore crosses the displayed colouring, proving
(17).  The smaller shore has order three, so (16) follows as well.
This completes item 6.  \(\square\)

## 6. Eliminating the unlabelled non-singleton atoms

It remains to prove (8).  Suppose `r>=2`.  Section 5 gives `q=0`, and hence

\[
                            B=N_G(A),\qquad |B|=7.    \tag{18}
\]

The set `B` separates the connected set `A` from the literal core `S`.
Seven-connectivity and Menger's theorem give seven pairwise vertex-disjoint
`B`--`S` paths with distinct ends.  Trim each path at its first vertex of
`S`; it may be taken internally disjoint from `B union S`.  All seven
vertices of `B` are path ends, while the ends in `S` are seven distinct core
vertices.

No path meets `A` internally.  Indeed, (18) says that a path entering `A`
from its end in `B` must leave through a second vertex of `B`; that vertex is
already the end of another path, contrary to disjointness.  Contract each
path to a bag `Z_b` indexed by its end `b in B`.  The seven ends in the
literal core induce a graph containing `K_{3,4}`, so the seven bags have a
`K_{3,4}` quotient.  We identify each `b` with its bag and hence with the
shore of the corresponding core end.

Contracting two disjoint edges of this `K_{3,4}` produces five bags with a
`K_5^-` quotient.  Both contracted bags are universal, and the three
singleton bags consist of one vertex on the three-vertex shore and two on
the four-vertex shore; only the edge between the latter two may be absent.
We choose the two-edge matching so that the five bags also have the required
contacts with two connected atom bags.

If `A=\{u,v\}`, put

\[
               M_u=B-N_C(u),\qquad M_v=B-N_C(v).
\]

The local inequality (4) gives `|M_u|,|M_v|<=1`.  A two-edge matching in
`K_{3,4}` can be chosen to cover `M_u union M_v`.  Consequently every one of
the resulting five bags contains a neighbour of each of `u,v`.  Together
with the adjacent singleton bags `\{u\},\{v\}`, their quotient has

\[
                            9+10+1=20
\]

contacts and is a `K_7^-` model.

If `C[A]=u-v-w`, use the two atom bags `\{u\}` and `\{v,w\}`.  The two miss
sets relevant to them are

\[
             M_u=B-N_C(u),\qquad
             T=B-N_C(\{v,w\}).
\]

Again (4) gives `|M_u|,|T|<=1`.  Cover their union by a two-edge matching.
The five `K_5^-` bags are complete to both atom bags, and the edge `uv`
joins those two bags.  The same count gives a `K_7^-` model.

Finally suppose `C[A]` is a triangle on `a_1,a_2,a_3`.  For
`\{i,j,k\}=\{1,2,3\}`, define

\[
       M_i=B-N_C(a_i),\qquad
       T_i=M_j\cap M_k=B-N_C(A-\{a_i\}).              \tag{19}
\]

The local and strict forms of (4) give

\[
 \begin{gathered}
    |M_i|\le2,\qquad |T_i|\le1,\\
    |M_i|=2\Longrightarrow M_i\cap\{x,y\}\ne\varnothing,\\
    T_i\ne\varnothing\Longrightarrow T_i\subseteq\{x,y\}.
                                                               \tag{20}
 \end{gathered}
\]

Moreover, `M_1 cap M_2 cap M_3` is empty because `B=N_C(A)`, and hence
`M_i cap T_i` is empty.

For some `i`, the set `U_i=M_i union T_i` is not a three-set contained in
one shore of the `K_{3,4}`.  Otherwise every `M_i` would have order two and
every `T_i=\{t_i\}` would be nonempty.  By (19), all three `t_i` would belong
to `\{x,y\}`.  They are pairwise distinct: equality of, say,
`t_1 in M_2 cap M_3` and `t_2 in M_1 cap M_3` would put their common value in
all three `M_i`.  Three distinct vertices cannot lie in `\{x,y\}`.

For this `i`, a two-edge matching of the `K_{3,4}` can be chosen whose four
ends cover `U_i` and neither of whose edges has both ends in `M_i`.  Indeed,
`|U_i|<=3` and `U_i` has at most two vertices on either shore.  If it has
three vertices, first match the lone-shore vertex so as to avoid the sole
possible cross-shore pair inside `M_i`, and match the other covered vertex
to a fresh vertex.  The cases of at most two prescribed vertices are
immediate by matching them separately when necessary; the shore orders
three and four leave the required fresh ends.

After contracting this matching, every one of the five `K_5^-` bags meets
`N_C(a_i)`: every missed singleton was covered, and no contracted edge lies
wholly in `M_i`.  Every bag also meets `N_C(A-\{a_i\})`: the latter miss set
is `T_i`, which has order at most one and was covered by a matching edge.
The connected atom bags `\{a_i\}` and `A-\{a_i\}` are adjacent and complete
to the five quotient bags.  Again the contact count is `9+10+1=20`.

All three possible unlabelled non-singleton atoms therefore give the
forbidden minor.  Hence `r=1`, proving (8).  \(\square\)

## 7. Exact singleton companion algebra

### Proposition 7.1 (exact one-resource overlap)

Let `A=\{a\}` be the atom, let `ab` be a three-contractible edge with
`b in B`, and let `X` be a connected tight blocker of `ab`.  Define the
following disjoint resource sets:

\[
\begin{aligned}
 P&=X\cap B, & R&=N_C(X)\cap B, & T&=Q\cap L(X),\\
 O&=(B-(P\cup R))\mathbin{\dot\cup}(Q-T),
 &K&=\partial X-(\{a\}\cup R\cup T).
                                                               \tag{21}
\end{aligned}
\]

Then

\[
\begin{gathered}
 \partial X=\{a\}\mathbin{\dot\cup}R\mathbin{\dot\cup}T
                    \mathbin{\dot\cup}K,\\
 Z=P\mathbin{\dot\cup}R\mathbin{\dot\cup}T
                    \mathbin{\dot\cup}O,\\
 |P|\ge1,\qquad R=\{b\},\qquad T=\varnothing,
       \qquad |K|=5,\qquad |O|\ge1,\\
                         \lambda(A\cup X)=6+|O|.       \tag{22}
\end{gathered}
\]

Thus `A union X` is tight exactly when `|O|=1`.  If `P=\{p\}`, then every
component `Y` of `X-p` is tight and

\[
                 \partial Y=(\partial X-\{a\})\cup\{p\}.
\]

Put `D=partial X` and `H=D-\{a\}`.  The graph `G[D]` has a bipartition of
orders three and four.  This bipartition is obtained from seven disjoint
`D`-rooted path bags, each meeting the literal core in exactly one distinct
representative and all disjoint from `X`; one literal-core vertex is unused.

If `P=\{p\}`, then either `X=\{p\}` or `X-p` is connected.
If `|P|>=2`, then at least two distinct vertices `p in P` satisfy that
`X-p` is connected.

#### Proof

The atom trace bound gives `|P|>=1`.  The endpoint `b` belongs to `R`, and
the atom estimate (5) gives `|R|+|T|<=5`.  Since `X` is tight and its
boundary contains `a`, the definition (21) partitions its seven resources as

\[
                        7=1+|R|+|T|+|K|.
\]

Direct boundary accounting gives

\[
 \partial(A\cup X)=R\mathbin{\dot\cup}T
                         \mathbin{\dot\cup}O\mathbin{\dot\cup}K,
\]

and hence

\[
 \lambda(A\cup X)=|R|+|T|+|O|+|K|=6+|O|.
\]

Inequality (2) gives `|O|>=1`, proving (21).  If `P=\{p\}` and `Y` is a
component of `X-p`, then `Y` has no neighbour in `a`: the only neighbour of
`a` inside `X` is `p`.  Therefore

\[
                 \partial Y\subseteq(\partial X-\{a\})\cup\{p\}.
\]

The resource set on the right has order seven, while (2) gives
`|partial Y|>=7`; equality follows.

It remains to improve the atom estimate.  Put `M=R dotcup T` and
`m=|M|`.  The exact boundary of `X` is

\[
          D:=\partial X=\{a\}\mathbin{\dot\cup}M
                            \mathbin{\dot\cup}K,
          \qquad |K|=6-m.                             \tag{23}
\]

Put `H=D-\{a\}=M dotcup K`, so `|H|=6`.  The connected set `X` is a
component of `G-D`.  By the audited
[seven-cut component theorem](hc7_k7minus_seven_cut_three_component_bound.md),
`G-D` has at most three components.  Write its other components as
`W_1,...,W_h`, where `1<=h<=2`.  Seven-connectivity makes every `W_i` full
to `D`.

Let `D_S=D cap S`, `D_C=D-S`, and `S_*=S-D`.  Since `a notin S`,

\[
                         |S_*|=8-|D_S|=|D_C|+1.       \tag{23a}
\]

Every vertex of `S_*` lies in one of the `W_i`.  Partition
`D_C=D_1 dotcup ... dotcup D_h` so that

\[
                         |D_i|\le |S_*\cap W_i|.      \tag{23b}
\]

For each nonempty `D_i`, apply the audited
[closed-shore rooted-connectivity lemma](hc7_closed_shore_rooted_connectivity.md)
to the order-seven separation with shore `W_i`, separator `D`, and root set
`D_i subseteq D`.  The pair `(G[W_i union D_i],D_i)` is internally
`|D_i|`-connected.  Menger's theorem and (23b) give `|D_i|` pairwise
vertex-disjoint paths from the distinct roots in `D_i` to distinct vertices
of `S_* cap W_i`.  Indeed, a smaller set-linkage separator would leave a
target vertex and, after placing any deleted roots in the separator, its
target-side components would give a separation of
`(G[W_i union D_i],D_i)` of order below `|D_i|`.  Trim each path at its
first literal-core vertex.  Paths belonging to different components `W_i`
are disjoint.

Use these paths as rooted bags for the vertices of `D_C`, and use the
singleton bag `\{s\}` for every `s in D_S`.  We now have seven disjoint
connected bags rooted at `D`, each meeting `S` in exactly one of seven
distinct representatives.  They avoid `X`, and one core vertex `s_0` is
unused.

The representative-shore colouring is proper on `G[D]`.  Otherwise an
edge of `G[D]` joins two rooted bags whose representatives lie on the same
shore.  Suppose `s_0` lies on shore zero.  Choose a rooted bag ending on
shore one, distinct from the two chord bags if the chord also lies on shore
one, and add `s_0` to it.  The enlarged bag is connected and universal to
the other six rooted bags.  Their six representatives form a `K_{3,3}`
and retain the same-shore chord.  Contracting a suitable cross-shore edge
gives five bags with a `K_5^-` quotient, exactly as in the proof of
Corollary 5.2.  The connected bag `X` is adjacent to all six resulting
bags through the seven roots in `D`.  The quotient therefore has

\[
                              9+5+6=20
\]

contacts, a contradiction.  Thus `G[D]` is bipartite with colour-class
orders three and four.

Every member of `M` is adjacent to `a`, so properness puts all `M`-rooted
representatives on the shore opposite the representative of `a`.  Suppose
`m>=2`, and delete the entire `a`-rooted path bag.  The remaining six bags
are rooted at `H`, avoid `X union \{a\}`, meet `S` exactly in their six
representatives, and leave two core vertices unused.  Extend them to a
rooted quotient containing `K_6` minus a two-edge matching as follows.

Any six selected vertices of a literal `K_{4,4}` extend, using the two
unused core vertices, to a rooted quotient containing `K_6` minus a
two-edge matching.  If `ell` selected representatives lie on one shore, the
unused shore counts are `4-ell` and `ell-2`.  Add each unused vertex to a
distinct selected bag whose core representative lies on the opposite shore.
The two enlarged bags are universal, and precisely two pure bags remain on
each shore; all pairs are adjacent except possibly the two same-shore pure
pairs.  The two pure bags on either shore may be prescribed arbitrarily.

Prescribe two `M`-rooted bags as one shore's pure pair, and add `a` to one
of them.  This enlargement is connected because its root lies in
`M subseteq N_G(a)`, and `a` supplies the formerly missing contact to the
other `M`-rooted bag.  The six bags now have at least fourteen contacts.
Finally, `X` is a disjoint connected seventh bag adjacent to all six
through their roots in `H subseteq \partial X`.  The resulting quotient
has at least twenty contacts, a `K_7^-` minor.

This contradiction proves `m<=1`.  Since `b in R subseteq M`, equality
holds: `M=R=\{b\}` and `T` is empty.  Equation (23) gives `|K|=5`,
completing the resource assertions in (22).

Suppose now that `|P|>=2`.  Choose a spanning tree of `G[X]`, and in it
the minimal subtree containing `P`.  Every leaf of this minimal subtree
belongs to `P`, and there are at least two leaves.  Fix such a leaf `p`.
All vertices of `P-\{p\}` lie in one component `Y_0` of `X-p`.  If another
component `Y_1` existed, it would be disjoint from `P`.  Consequently

\[
                       \partial Y_1=H\cup\{p\}.
\]

Indeed, the left side is contained in the seven-resource set on the right,
and (2) forces equality.  The component `Y_0` is adjacent to both `a` and
`p`, and its boundary is contained in the eight-resource set
`D union \{p\}`.  Inequality (2) therefore makes it adjacent to at least
five of the six roots in `H`.

Delete the `a`-rooted bag from the seven-root system above.  Among the five
rooted bags whose roots meet `Y_0`, two representatives lie on the same
core shore.  Prescribe those two bags as a pure pair in the six-bag
extension, and add all of `Y_0` to one of them.  This repairs that missing
contact.  The disjoint connected bag `Y_1` is adjacent to all six bags
through `H`, so the quotient again has `14+6=20` contacts.  This
contradiction proves that `X-p` is connected.  Applying the argument to
two leaves gives the asserted two distinct choices of `p`.

Finally suppose `P=\{p\}` and `X-p` has two distinct components
`Y_1,Y_2`.  The endpoint `b in R` makes `m>=1`.  In the six-root system,
choose the unique `M`-rooted bag and a `K`-rooted bag whose core
representatives lie on the same shore.  Such a `K`-rooted bag exists
because each shore contains at least two of the six representatives.
Prescribe these two bags as one pure same-shore pair.

By the component identity preceding (23),

\[
                         N_G(Y_i)=H\cup\{p\}
\]

for `i=1,2`.  In `G[Y_2 union \{p,k\}]`, where `k in K` is the root of
the chosen pure bag, take a `p`--`k` path whose internal vertices lie in
`Y_2`.  Enlarge the `k`-rooted bag by this path minus `k` and by `a`.
It stays connected through `ap`, and `a` supplies the missing contact to
the chosen `M`-rooted bag.  The six rooted bags now have at least fourteen
contacts.  The disjoint connected bag `Y_1` is adjacent to all six through
their roots in `H`, giving a `K_7^-` model.  This contradiction shows that
`X-p` has at most one component.  This completes item 7 and
Proposition 7.1.  \(\square\)

### Proposition 7.2 (adjacent singleton blockers)

In Proposition 7.1, suppose `X=\{p\}` and put

\[
                 M=R\mathbin{\dot\cup}T,\qquad m=|M|.
\]

Then

\[
\begin{aligned}
 N_G(a)&=\{p,b\}\mathbin{\dot\cup}O,\\
 N_G(p)&=\{a,b\}\mathbin{\dot\cup}K,\\
 |O|&=|K|=5,\qquad N_{G[Z]}(p)=\{b\}.              \tag{24}
\end{aligned}
\]

Thus `a,p` have the unique common neighbour `b`.

Moreover,

\[
                              L(a)\cap L(p)=\varnothing.           \tag{25}
\]

For their common neighbour,

\[
             |L(a)\cup L(b)|\le3,
             \qquad |L(p)\cup L(b)|\le3.             \tag{26}
\]

In particular, if `|L(a)|=|L(p)|=3`, then `b` is unlabelled.

#### Proof

Equation (24), including `M=R=\{b\}` and the fact that `T` is empty, is
the specialization of (21)--(22) to `X=\{p\}`.

The set `\{p\}` is another all-edge tight atom because its exact boundary
contains the ends `a,b` of a three-contractible edge.  More explicitly,
`C-p` is connected by three-connectivity.  If `|N_C(p)|<=3`, then after
contracting `ab` the image of `N_C(p)` would be a separator of order at
most two, contrary to the three-connectivity of `C/ab`.  Thus
`|N_C(p)|>=4` and `|L(p)|<=3`, so Corollaries 5.1 and 5.2 apply uniformly
with `p` as the atom.

Finally apply Corollary 5.1 with `p` as the singleton atom and `ab` as
the three-contractible edge in its vertex boundary.  The resulting small
bag rooted at `a` has label set disjoint from `L(p)` by (15).  Since
that bag contains `a`, equation (25) follows.

The vertices `a,p,b` form a triangle.  Repeat the proof of
Corollary 5.1 with `a` as the large-bag root and `p,b` as the unit-bag
roots; only the triangle is used in that proof, not contractibility of its
opposite edge.  Lemmas 3.2 and 3.1 produce the `5,1,1` profile, and Lemma
4.2 says that the two small bags avoid its selected five-set, which contains
`L(a)`.  Hence `|L(p) union L(b)|<=3`.  Recentring the same construction at
`p` gives `|L(a) union L(b)|<=3`, proving (26).

If both singleton label sets have order three, (25) makes them disjoint.
The two bounds in (26) put `L(b)` inside each of them, so `L(b)` is empty.
This completes item 8.  \(\square\)

### Proposition 7.3 (prescribing the omitted literal-core vertex)

Let `S_0,S_1` be the two shores of the displayed literal core.  For
`s in S-Q`, put

\[
                  k=7-q,\qquad T_s=S-(Q\cup\{s\}).
\]

Exactly one of the following conclusions holds.

1. There are `k` pairwise vertex-disjoint `B`--`T_s` paths in
   `G-(Q union \{s\})`.  They saturate both end sets, may be taken internally
   disjoint from `B union T_s`, and avoid `a`.
2. There is a `B`--`T_s` separator
   `W_s subseteq V(G)-(Q union \{s\})` of order `6-q` such
   that

   \[
                              Q\cup\{s\}\cup W_s       \tag{27}
   \]

   is an exact seven-cut.  It may be chosen with `a notin W_s`; the vertex
   `a` and every member of `B-W_s` lie in one component on the same side of
   this cut.

If `q>=1`, then either conclusion 2 holds for some `s in S-Q`, or `G[Z]`
has a connected component disjoint from `Q` whose two bipartition classes
have nonzero odd difference in order.

#### Proof

The sets `B` and `T_s` both have order `k`.  Apply the set form of Menger's
theorem in `H_s=G-(Q union \{s\})`.  If there are `k` disjoint paths, they
saturate both sets.  Replacing each path by the segment from its last
`B`-vertex to its first subsequent `T_s`-vertex makes its interior disjoint
from `B union T_s`.  The paths avoid
`a` because `N_{H_s}(a)=B`: a path through `a` would have an internal
vertex in `B`.

Otherwise Menger gives a `B`--`T_s` separator `W_s` of order at most
`k-1`.  Both `B-W_s` and `T_s-W_s` are nonempty, so
`Q union \{s\} union W_s` separates `G` and has order at most seven.
Seven-connectivity forces `|W_s|=k-1=6-q` and makes (27) an exact
seven-cut.

Choose `W_s` inclusion-minimal.  If `a in W_s` and `W_s-\{a\}` did not
separate `B` from `T_s`, a path avoiding `W_s-\{a\}` would have to use
`a`.  Immediately after its occurrence of `a`, the path has a vertex of
`B`; the suffix from that vertex to `T_s` avoids all of `W_s`, a
contradiction.  Thus `a notin W_s`.  Since `a` is adjacent to every
surviving member of `B`, they lie in one component of the indicated side.

It remains to prove the last assertion.  Suppose `q>=1` and choose
`s_i in S_i-Q` for `i=0,1`; both choices exist because `q<=3`.  If either
choice gives conclusion 2, there is nothing to prove.  Otherwise add the
trivial one-vertex paths at `Q` to the two linkages from conclusion 1.
For each `i` this gives seven disjoint path bags indexed by `Z` and ending
at precisely `S-\{s_i\}`.  Colour a vertex of `Z` by the literal-core shore
of its path end.  The proof of Corollary 5.2 applies verbatim: a
same-coloured edge of `G[Z]` would combine with the unused vertex `s_i` to
give a `K_7^-` minor.  Hence both are proper bipartite colourings of
`G[Z]`, and both agree with the fixed shore colouring on `Q`.

In the colouring obtained by omitting `s_0`, the colour-zero class has
order three; in the colouring obtained by omitting `s_1`, it has order
four.  On every connected component meeting `Q` the two colourings have
the same orientation.  They can differ only by flipping components
disjoint from `Q`.  Fix the first colouring and, for each flipped component
`D`, let

\[
 d(D)=|\{z\in D:c(z)=0\}|-|\{z\in D:c(z)=1\}|.
\]

The change in the total colour-zero class is one, so the sum of `-d(D)`
over the flipped components is one.  At least one of these integers is
nonzero and odd.  This proves item 9, Proposition 7.3, and Theorem 1.1.
\(\square\)

## 8. Exact unresolved scope

The theorem leaves one atom alternative when no safe edge exists: `A` is a
singleton with `0<=w(A)<=3`.  Its complement is connected, every
three-contractible edge in its vertex boundary admits the exact spanning
enclosure profile (12)--(15), and its full seven-vertex neighbourhood is a
`3`-by-`4` bipartite graph extending the literal-core shore colouring.
Every blocker of a crossing contractible edge has the exact resource split
(21)--(23); its overlap with the atom neighbourhood is exactly the exterior
vertex `b`, and the blocker boundary is another `3`-by-`4` bipartite exact
seven-cut.  If `|X cap B|>=2`, at least two vertices of `X cap B` are
non-cutvertices of `G[X]`.  A singleton blocker has the paired exact
neighbourhoods (24): the adjacent degree-seven vertices have the unique
common neighbour `b`, have disjoint label sets by (25), and satisfy the
label-union bounds (26).  If `X cap B=\{p\}`, then a nonsingleton `X` has
`X-p` connected.  Proposition 7.3 adds a second exact
residue: prescribing the omitted literal-core vertex either succeeds or
returns the exact seven-cut (27); when `q>=1`, absence of all such cuts
forces a `Q`-free component of `G[Z]` with odd bipartition imbalance.

The restriction `q>=1` in Lemma 4.1 is essential to the positive-atom proof
mechanism.
For `q=0`, the marked partition theorem controls only the three mark counts,
not the identities of the labels assigned to the bags.  With quotas
`1,1,5`, the profile consisting of singleton labels on opposite shores of
the `K_{4,4}` and the other five represented labels in the third bag is
genuinely `K_7^-`-minor-free.  The seven-linkage argument of Section 6 avoids
that obstruction for every non-singleton atom, but it does not supply two
atom bags when `A` is a singleton.  The precise remaining lemma is therefore:

> **Singleton all-edge atom completion lemma (open).**  In the setting of
> Theorem 1.1, exclude the singleton atom together with the complete system
> of tight blockers of all three-contractible edges, the spanning enclosure
> profiles (12)--(17), and the exact crossing-cut restrictions
> (21)--(27).

This is a route nonclosure for the present partition argument, not a
counterexample to the weighted splitter theorem or to T44.  Proving the
singleton completion lemma would give a safe edge whenever no terminal
configuration is present; terminal lifting and induction from the
computation-free base through order six would then close the literal
`K_{4,4}` branch of T44.
