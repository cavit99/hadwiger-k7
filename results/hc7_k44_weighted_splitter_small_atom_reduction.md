# Safe contraction or a three-vertex tight atom in a labelled exterior

**Status.** Written unbounded reduction theorem.  Its adjacent audit records
the exact checked revision.  The theorem does not prove the weighted splitter
theorem, the literal case of T44, T44 itself, Conjecture 21, or `HC_7`.

## 1. Setting

Let `C` be a finite simple three-connected graph of order at least seven.
Let `Omega` be a set of eight labels disjoint from `V(C)` and assign a set

\[
                         L(v)\subseteq\Omega
\]

to every `v in V(C)`.  For nonempty `X subseteq V(C)`, put

\[
 L(X)=\bigcup_{x\in X}L(x),\qquad
 \lambda(X)=|N_C(X)|+w(X),\qquad w(X)=|L(X)|.         \tag{1}
\]

Throughout the theorem, assume

\[
                         \lambda(X)\ge 7              \tag{2}
\]

for every nonempty `X subseteq V(C)`, including `X=V(C)`.  Thus the
full-set instance of (2) is `w(C)>=7`.

An edge `uv` is **three-contractible** when simplifying `C/uv` leaves a
simple three-connected graph.  It is **safe** when, after giving the
contracted vertex the label set `L(u) union L(v)`, both three-connectivity
and every inequality (2) are preserved.

A **four-label triangle model** is a family of three pairwise disjoint
connected vertex sets which are pairwise adjacent in `C` and each have
weight at least four.

A **three-label spanning `K_4` model** is a partition of `V(C)` into four
nonempty connected bags which are pairwise adjacent and each have weight
at least three.

A **positive `K_6^-` quotient model** is a family of six pairwise disjoint
connected positive-weight bags, not necessarily spanning, whose quotient
has at least fourteen of the fifteen possible bag adjacencies.

Call a nonempty set `A subseteq V(C)` a **contractible-boundary tight set**
if

\[
 \lambda(A)=7
 \quad\hbox{and}\quad
 N_C(A)\hbox{ contains both ends of a three-contractible edge}. \tag{3}
\]

The vertex and label members of the boundary will be treated as formally
different resources:

\[
 \partial A=N_C(A)\mathbin{\dot\cup}L(A).             \tag{4}
\]

Equation (3) says exactly that `|partial A|=7` and that its vertex part
contains a three-contractible edge.

## 2. Exact contraction obstruction

### Lemma 2.1

Let `uv` be a three-contractible edge of `C`.  The contraction `C/uv`, with
the union label at the contracted vertex, violates (2) if and only if there
is a nonempty set

\[
                    X\subseteq V(C)-\{u,v\}            \tag{5}
\]

such that

\[
            u,v\in N_C(X)\qquad\hbox{and}\qquad
            \lambda(X)=7.                              \tag{6}
\]

Thus `uv` is safe if and only if no tight set has both ends of `uv` in its
vertex boundary.

#### Proof

Let `z` be the contracted vertex and let `q:V(C)-->V(C/uv)` be the quotient
map.  If `z in Y`, then the preimage `q^{-1}(Y)` contains both `u,v`.
The vertex boundary, label union and hence the value in (1) are unchanged.

If `z notin Y`, identify `Y` with the same subset of
`V(C)-{u,v}`.  Its label union is unchanged and its boundary is the image
of `N_C(Y)`.  The boundary loses one vertex precisely when both `u` and
`v` belong to `N_C(Y)`; otherwise its order is unchanged.  Since the old
value is at least seven, the new inequality fails precisely in (6).  The
full-set inequality is preserved because contraction does not change the
global label union.  This proves both directions.  \(\square\)

The lemma deliberately includes co-spanning sets.  For example,
`X=V(C)-{u,v}` may have boundary `{u,v}` and weight five.  Such a set can
block the weighted inequality even though it is not a fragment of `C` in
the usual separator sense.

### Lemma 2.2 (terminal lifting)

Each of the three terminal configurations defined in Section 1 lifts
from the union-labelled contraction `C/uv` to `C`.

#### Proof

If the contracted vertex is unused by a nonspanning quotient model, leave
all its bags unchanged.  Otherwise replace the unique bag containing the
contracted vertex by its full preimage, which contains the edge `uv`, and
leave every other bag unchanged.  The replacement bag is connected, its
label union is the old union label, and every quotient adjacency lifts to
an original edge between the corresponding preimage bags.  Disjointness is
preserved.  In the four-bag case the preimage bags still partition `V(C)`.
Thus all bag weights, all required quotient adjacencies, and the spanning
requirement when present are preserved.  \(\square\)

## 3. Tight-set algebra

### Lemma 3.1

The following assertions hold.

1. The function `lambda` is submodular.
2. If tight sets `X,Y` intersect, then both `X intersect Y` and
   `X union Y` are tight.
3. Every component `D` of `C[X]`, for a tight set `X`, is tight and has
   exactly the same boundary resources as `X`.

#### Proof

The function `|N_C[X]|` is a coverage function, hence is submodular.
Subtracting the modular function `|X|` shows that `|N_C(X)|` is
submodular.  The label-union cardinality is another coverage function, so
their sum `lambda` is submodular.

If `X intersect Y` is nonempty, submodularity gives

\[
 14=\lambda(X)+\lambda(Y)
 \ge \lambda(X\cap Y)+\lambda(X\cup Y)\ge14.          \tag{7}
\]

The last inequality uses (2); it also applies when `X union Y=V(C)` because
the full-set inequality is among the hypotheses.  Equality holds
throughout.

Finally, if `D` is a component of `C[X]`, then no vertex of another
component is adjacent to `D`, and therefore

\[
 \partial D\subseteq\partial X.
\]

By (2), `|partial D|>=7=|partial X|`, so the two resource sets are equal.
This proves assertion 3.  \(\square\)

In particular, every blocker in Lemma 2.1 can be replaced by any one of
its components while retaining both ends of the blocked edge in its
boundary.

### Lemma 3.2 (seven distinct labelled vertices)

There are seven distinct labels `omega_1,...,omega_7` and seven distinct
vertices `v_1,...,v_7` such that `omega_i in L(v_i)` for every `i`.

#### Proof

Let `Omega_0` be the set of labels used on `C` and put
`m=|Omega_0|=w(C)`, so `7<=m<=8`.  In the bipartite incidence graph
between `Omega_0` and `V(C)`, let `P(U)` be the vertex neighbourhood of a
set `U subseteq Omega_0`.

We claim

\[
                 |P(U)|\ge |U|-(m-7)                 \tag{H}
\]

for every `U`.  Put `X=V(C)-P(U)`.  If `X` is nonempty, then
`N_C(X) subseteq P(U)` and `X` uses no label of `U`.  Hence (2) gives

\[
 7\le |N_C(X)|+w(X)\le |P(U)|+m-|U|,
\]

which is (H).  If `X` is empty, then `|P(U)|=|V(C)|>=7`, while the
right side of (H) is at most seven, so (H) still holds.

The deficiency form of Hall's theorem now gives a matching of size at
least `m-(m-7)=7`.  Its seven edges give the asserted labels and
vertices.  \(\square\)

### Lemma 3.3 (spanning contractible tree)

If `C` has no four-label triangle model, then `C` has a spanning tree all
of whose edges are three-contractible.

#### Proof

First, no two degree-three vertices are adjacent.  Indeed, if `x,y` were
adjacent degree-three vertices, then three-connectivity would make
`C-{x,y}` connected.  The singleton inequalities give
`w({x}),w({y})>=4`, while

\[
 N_C(C-\{x,y\})=\{x,y\},
 \qquad w(C-\{x,y\})\ge5.
\]

Thus `\{x\}`, `\{y\}`, and `C-\{x,y\}` would be a four-label triangle
model.

We translate a theorem of Costalonga to graphs.  Let `M(C)` be the cycle
matroid of `C`.  It is a three-connected binary matroid of rank
`|V(C)|-1>=6`.  A triangle of `M(C)` is a graph triangle.  Binary
circuit--cocircuit parity says that a triad meeting the graph triangle
`abc` meets it in exactly two edges, say `ab,ac`.  A graphic triad is a
three-edge bond, so write it as the edge boundary of a connected shore
containing `a` and not `b,c`.  If the third boundary edge is incident
with `a`, any further vertex on that shore would make `a` a cut vertex.
Otherwise let `d` be
the inside end of the third boundary edge.  If the shore has another
vertex besides `a,d`, deleting `a,d` disconnects `C`; if the shore is
exactly `\{a,d\}`, then `d` has degree at most two.  Three-connectivity
therefore forces the shore to be `\{a\}`.  In particular, the triad is the
three-edge star of the degree-three vertex `a`.

Since no graph triangle contains two adjacent degree-three vertices, each
triangle of `M(C)` meets at most one triad.  Costalonga's Theorem 1.5 now
gives a spanning set of `M(C)` consisting of vertically contractible
elements.  It contains a basis, hence a graph spanning tree `F`.  For an
edge `e of F`,

\[
 \operatorname{si}(M(C)/e)=M(\operatorname{si}(C/e)).
\]

Whitney's graphic connectivity equivalence therefore says that vertical
contractibility is precisely three-connectivity of the simplified graph
`C/e`.  Thus every edge of `F` is three-contractible.  \(\square\)

## 4. Small-atom reduction

### Theorem 4.1 (safe contraction or a small transverse atom)

Under the hypotheses of Section 1, at least one of the following holds.

1. `C` has a four-label triangle model.
2. `C` has a safe three-contractible edge.
3. There is a spanning tree `F` of `C` every edge of which is
   three-contractible, and there is a contractible-boundary tight set `A`
   chosen with minimum order among those whose boundary contains an edge
   of `F`.  Put

   \[
        r=|A|,\qquad B=N_C(A),\qquad Q=\bigcup_{a\in A}L(a).
   \]

   Then:

   - `C[A]` is connected and `1<=r<=3`;
   - `4<=|B|<=7`, `|Q|=7-|B|<=3`;
   - the boundary `B` contains an edge `xy of F`; fix one such edge;
   - for every nonempty proper `Y subset A`,

     \[
      |B-(N_C(Y)\cap B)|+|Q-L(Y)|
      \le |N_{C[A]}(Y)|;                              \tag{8}
     \]

   - if `Y` is adjacent to both `x,y`, then the right side of (8) can be
     decreased by one;
   - for every edge `ab in E(F)` incident with `A`, oriented with
     `a in A` and `b in A union B`, and every connected tight blocker `X`
     of `ab`,

     \[
       A\subseteq N_C(X),\qquad
       |\partial A\cap\partial X|\le 7-2r.            \tag{9}
     \]

     At least one such tree edge crosses from `A` to `B`.  For every
     blocker of a crossing edge `ab`, the intersection in (9) contains
     `b`; in particular, if `r=3`, then

     \[
                  \partial A\cap\partial X=\{b\}.     \tag{10}
     \]

Here intersections in (9) use the common resource universe
`V(C) dotcup Omega`.

#### Proof

Assume that outcome 1 does not hold.  A vertex of degree three has weight
at least four by its singleton inequality.  Lemma 3.3 supplies a spanning
tree `F` all of whose edges are three-contractible.

Assume also that outcome 2 does not hold.  Lemma 2.1 now says that every
three-contractible edge has a tight blocker.

We translate the weighted system to ordinary connectivity.  Add the eight
label vertices `Omega`, make them a clique, and join `v in V(C)` to
`omega in Omega` exactly when `omega in L(v)`.  Add a further set `R` of
`|V(C)|` vertices disjoint from `V(C) union Omega`, make `Omega union R`
a clique, and add no edge from `R` to `C`.  Call the resulting graph `J`.

The graph `J` is seven-connected.  Indeed, after deleting at most six
vertices, the large clique still has a surviving vertex.  A component
`X` of the remaining graph which misses that clique would be a nonempty
subset of `V(C)` with all resources in `partial X` deleted, contradicting
(2).  Conversely, every tight set in `C` has its seven resources as a
separator in `J`, with the ballast clique on the opposite side.
Because the contractible spanning tree is nonempty and every one of its
edges has a tight blocker, such a separator exists.  Hence
`kappa(J)=7`.

Let `\mathcal S` be the family of endpoint pairs of the edges of `F`.
Every member of `\mathcal S` lies in a minimum separator of `J`: use a
tight blocker and Lemma 2.1.  A minimum-order
`\mathcal S`-fragment of `J` lies wholly in `C`.  To see this, first note
that a blocker contained in `C` supplies such a fragment of order at most
`|V(C)|-2`.  If a fragment met the clique `Omega union R`, clique adjacency
would put every clique vertex outside its seven-vertex boundary on the
same side.  That fragment would contain at least

\[
              |Omega union R|-7=|V(C)|+1
\]

vertices and could not be minimum.  Denote a minimum fragment in `C` by
`A`.  Lemma 3.1 shows that it is connected.  In the direct language of
Section 1, it is precisely a minimum contractible-boundary tight set among
those whose boundary contains an edge of `F`.

We apply Mader's generalized atom theorem to `A`.  Fix an edge `ab of F`
incident with `A`, orient it so that `a in A`, and fix an arbitrary
connected tight blocker `X` of `ab`.  Adjacency gives
`b in A union N_J(A)`, while `T=partial X=N_J(X)` is a minimum separator
containing `a,b` and therefore meeting `A`.  Mader's theorem gives

\[
          A\subseteq T,
          \qquad
          |A|\le {1\over2}|T-N_J(A)|.                 \tag{11}
\]

Since `|T|=7`, (11) gives `r<=3` and

\[
                   |T\cap N_J(A)|\le7-2r.             \tag{12}
\]

The chosen connected set `X` is a component of `J-T` away from the ballast
clique.  The inclusion `A subseteq T` places every member of `A` in
`N_C(X)`, and (12) is exactly (9).  Since the blocker was arbitrary, this
proves the universal assertion in (9).

Because `F` is a spanning tree and `A` is a nonempty proper subset of
`V(C)`, some edge `ab of F` crosses from `A` to `B`.  For a blocker of
this edge, `b` belongs both to `partial A` and to `T=partial X`.  Combining
this with (12) proves (10) when `r=3`.

The boundary `B` contains the fixed edge `xy of F`.  If `|B|<=3`, then
`|A union B|<=6<|V(C)|`; hence `B` separates `A` from a nonempty part of
`C`.  Contracting the displayed edge in `B` leaves a separator of order at
most two, contrary to three-contractibility.  Thus `|B|>=4`, and tightness
gives `|Q|=7-|B|<=3`.

It remains to prove the local resource statements.  For
`emptyset ne Y subsetneq A`, every boundary resource of `Y` either belongs
to `partial A` and is seen by `Y`, or is a vertex of `A-Y` adjacent to
`Y`.  Applying (2) to `Y` gives (8).  If `Y` sees both `x,y` and equality
held in its boundary inequality, then `Y` would be a smaller tight set
whose boundary contains the fixed edge `xy of F`, contrary to the choice
of `A`.  Hence its boundary has order at least eight, which decreases the
right side of (8) by one.  This completes the proof.  \(\square\)

### Corollary 4.2 (exact transverse pair for a three-vertex atom)

Suppose outcome 3 of Theorem 4.1 holds with `|A|=3`.  Let
`ab in E(F)` cross from `a in A` to `b in B`, and let `X` be any connected
tight blocker of `ab`.  Put

\[
                     P=X\cap B,
 \qquad B_0=B-(P\cup\{b\}).
\]

Then

\[
\begin{gathered}
 A\cap X=\varnothing,\qquad A\subseteq N_C(X),\qquad
 L(A)\cap L(X)=\varnothing,\\
 N_C(X)\cap B=\{b\},\qquad 1\le |P|\le3,qquad |X|\ge3.       \tag{13}
\end{gathered}
\]

The set `P` collectively dominates `A`, while `X` is anticomplete to
`B_0`.
As resource sets,

\[
       \partial X=(A\mathbin{\dot\cup}\{b\})
                     \mathbin{\dot\cup} Z,
       \qquad |Z|=3.                                  \tag{14}
\]

Finally,

\[
                         \lambda(A\cup X)=10-|P|.     \tag{15}
\]

In particular, the four bags consisting of the three atom vertices and
`X` form a `K_4` model when `C[A]` is a triangle and a `K_4^-` model when
`C[A]` is a path.  If `|X|=3`, then `|P|>=2`.  If in addition `|P|=2`,
both vertices of `P` are adjacent to both vertices of `A-{a}`; when
`C[X]` is a path, the two vertices of `P` are its endpoints.

#### Proof

The blocker definition makes `X` disjoint from `a,b`, and Theorem 4.1
strengthens this to `A subseteq N_C(X)`, so all of `A` is disjoint from
`X`.  Equation (10) says `partial A intersect partial X={b}`.  Separating
vertex and label resources gives

\[
                  L(A)\cap L(X)=\varnothing,
        \qquad N_C(X)\cap B=\{b\}.
\]

Since `A union {b}` consists of four vertex resources in the seven-set
`partial X`, the remaining resource set `Z` has order three, proving
(14).  Every member of `A` has a neighbour in `X`; any such neighbour
belongs to `X cap N_C(A)=P`.  Thus `P` dominates `A` and is nonempty.
The displayed boundary intersection also says that no edge joins `X` to
`B_0`.

Let `D=N_C(X)-(A union {b})`.  The vertex and label parts of (14) give

\[
                         |D|+w(X)=3.                  \tag{16}
\]

Moreover `D cap B=emptyset`, and direct boundary accounting gives

\[
 N_C(A\cup X)=(B-P)\mathbin{\dot\cup}D.
\]

The label unions of `A` and `X` are disjoint.  Using
`|B|+w(A)=7` and (16) now proves (15).  The boundary inequality for
`A union X` gives `|P|<=3`.

The set `X` is itself a tight set whose boundary contains the fixed tree
edge `ab`.  Minimality of `A` among such sets gives `|X|>=|A|=3`.

Suppose `|X|=3`.  Then `X` is another minimum tight set for the fixed tree
and satisfies the local resource inequality (8), with `a,b` as its
distinguished boundary edge.  Every two-set of `X` sees every boundary
resource other than possibly one of `a,b`: if it missed any other
resource, its one-resource allowance would force it to see both `a,b`,
and the sharpened form of (8) would remove that allowance.  If `|P|=1`,
the two-set `X-P` has no neighbour in `A`, so it misses both vertices of
`A-{a}`.  But every
two-set of a connected three-vertex atom misses at most one boundary
resource, a contradiction.  If `P={p_1,p_2}`, apply the same two-set
inequality to `\{p_i\} union (X-P)`.  The vertex in `X-P` has no neighbour
in `A`, so each `p_i` must see both vertices of `A-{a}`.  If the vertex in
`X-P` were an endpoint of a path `C[X]`, its singleton inequality would
force it to see all boundary resources except possibly one of `a,b`, again
contrary to its two misses in `A-{a}`.  Thus `P` consists of the path
endpoints.

Finally, `X` is adjacent to every atom vertex.  Together with the internal
path or triangle on `A`, this gives the asserted four-bag quotient.
\(\square\)

### Corollary 4.3 (component reduction for three-vertex atoms)

In a labelled instance with none of the three terminal configurations,
let `A` be a three-vertex atom from Theorem 4.1 and let `m` be the number
of components of `C-A`.  Then `m<=2`.

If `C[A]` is a triangle, put

\[
             d=|\{a\in A:w(\{a\})<3\}|.
\]

Then `m<=d`.  If `C[A]=u-v-w` is a path, put

\[
                    q=|Q|,\qquad s=w(\{v\}).
\]

The only possibilities are

\[
 m=1,
 \qquad\hbox{or}\qquad
 m=2\ \hbox{ with }\ q<3\ \hbox{ or }\ s<3.          \tag{17}
\]

#### Proof

Every component `H` of `C-A` has `N_C(H)=A`: a smaller boundary would be a
separator of order at most two.  Its boundary inequality therefore gives
`w(H)>=4`.

If `m>=3`, choose distinct components `H_1,H_2,H_3` and distinct atom
vertices `a_1,a_2,a_3`.  The three bags

\[
                       H_i\cup\{a_i\}
\]

are connected and have weight at least four.  They are pairwise adjacent
because each `H_i` is adjacent to every atom vertex.  This is the first
terminal configuration, so `m<=2`.

Suppose first that `A` is a triangle.  Reserve one component as a fourth
bag and attach a different component to each atom vertex of weight below
three.  The remaining atom singletons already have weight at least three.
The triangle edges and the fact that every component has boundary `A`
make the four bags pairwise adjacent.  Any leftover component may be
attached to an atom bag, preserving connectivity.  Thus `m>=d+1` would
give a spanning three-label `K_4` model, and terminal-freeness gives
`m<=d`.

Now let `A=u-v-w` be a path.  Both endpoints carry all `q` labels of `Q`.
Reserve a component `H_0` as the fourth bag and attach a second component
`H_1` to `u`.  The edge from `H_1` to `w` supplies the missing contact
between the endpoint bags.  If `q<3`, attach one further component to
`w`; if `s<3`, attach one further component to `v`.  These four bags are
connected, pairwise adjacent and all have weight at least three; arbitrary
leftover components can again be attached to an atom bag.  Consequently a
spanning three-label `K_4` model exists whenever

\[
              m\ge2+\mathbf1_{q<3}+\mathbf1_{s<3}.
\]

Combining its failure with `m<=2` gives exactly (17).  \(\square\)

## 5. The four exact atom shapes

Theorem 4.1 leaves only the following cases.

1. `A` is a singleton `a`, with `N_C(a)=B` and `L(a)=Q`.
2. `C[A]` is one edge.  Each endpoint carries every label in `Q` and is
   adjacent to every vertex of `B` except possibly one of `x,y`.
3. `C[A]` is a three-vertex path.  Every two-set in `A`, and each endpoint
   separately, carries every label in `Q` and is adjacent to every vertex
   of `B` except possibly one of `x,y`.  The middle vertex misses at most
   two resources of `B dotcup Q`, and at most one if it sees both `x,y`.
4. `C[A]` is a triangle.  Every two-set in `A` carries every label in `Q`
   and is adjacent to every vertex of `B` except possibly one of `x,y`.
   Each singleton misses at most two resources of `B dotcup Q`, and at
   most one if it sees both `x,y`.

For example, in case 2, (8) says that either singleton misses at most one
of the seven resources in `B dotcup Q`.  If it missed a label, or a
boundary vertex other than `x,y`, it would see both `x,y`, and the sharpened
form of (8) would say that it misses no resource.  This proves case 2.
The same argument applied to a two-set in case 3 or 4, and to an endpoint
of the path in case 3, proves the other assertions.

In addition, every edge of the fixed contractible spanning tree incident
with the atom has a companion tight blocker satisfying (9).  The old and
new seven-resource boundaries overlap in at most five, three, or one
resources when `|A|` is one, two, or three, respectively.  A tree edge
crossing from `A` to `B` always exists; for a three-vertex atom its
companion boundary meets the atom boundary in exactly its endpoint in
`B`.

## 6. Exact remaining lemma and consequence

The weighted splitter theorem is reduced to the following statement.

> **Small transverse-atom completion lemma (open).**  In a labelled
> three-connected graph satisfying (2) and avoiding all three terminal
> configurations of the literal-core trichotomy, none of the four atom
> shapes in Section 5 can occur together with the companion blockers (9)
> for the fixed spanning tree of three-contractible edges, including the
> exact transverse-pair structure (13)--(16) and the component restrictions
> (17) when `|A|=3`.

Indeed, if the small transverse-atom lemma holds and none of the three
terminal configurations is present, outcome 1 of Theorem 4.1 is absent and
outcome 3 is excluded by the lemma.  Outcome 2 supplies a safe contraction.
Lemma 2.2 lifts whichever terminal configuration occurs.  Induction from
the computation-free base through order six would then prove the full
labelled trichotomy and close the literal `K_{4,4}` branch of T44.

The remaining lemma is unbounded: although its atom has at most three
vertices, its boundary and companion blockers live in an exterior of
arbitrary order.  In the three-vertex case, terminal-freeness leaves only
one or two components of `C-A`, with the deficiencies in Corollary 4.3.
The one-resource overlap does not imply `|P|=3`, does not create additional
components, and does not split the component containing `X` into two
connected label-rich pieces.  The precise missing mechanism there is a
rooted positive-weight partition inside that one component (or the two
components in (17)); further cut counting alone does not supply it.  No
finite census is used to infer this unbounded residue.

## 7. External inputs and scope

The two external inputs are used at their exact stated strengths.

- J. P. Costalonga, *A splitter theorem on 3-connected binary matroids and
  inner fans*, Journal of Combinatorial Theory, Series B **173** (2025),
  204--245, doi:`10.1016/j.jctb.2025.03.004`, Theorem 1.5: a
  three-connected binary matroid of rank at least four in which every
  triangle meets at most one triad has a spanning set of vertically
  contractible elements.  Lemma 3.3 supplies the graphic translation,
  including the triad check.
- W. Mader, *Generalizations of critical connectivity of graphs*, Discrete
  Mathematics **72** (1988), 267--283,
  doi:`10.1016/0012-365X(88)90216-6`: the generalized atom theorem used in
  (11).  The exact formulation used here is also Lemma 5.1 of M. Kriesell,
  *Minimal Connectivity*, arXiv:`1101.2357`: for an `\mathcal S`-atom `A`
  and a minimum separator `T` meeting `A` and containing a member of
  `\mathcal S` inside `A union N(A)`, it gives
  `A subseteq T` and `|A|<=|T-N(A)|/2`.

This result formalizes the exact safe-contraction obstruction and replaces
an arbitrary complete system of tight witnesses by one of four small atom
normal forms, a spanning tree of contractible edges, and sharply transverse
companion cuts.  It does not eliminate those normal forms and therefore
does not prove the weighted splitter theorem or any of the larger
conjectures listed at the start.
