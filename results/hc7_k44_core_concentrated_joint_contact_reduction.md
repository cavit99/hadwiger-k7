# Joint contact and an actual separator in the core-concentrated trace

**Status.** Written unbounded theorem; the adjacent audit identifies the exact
checked revision.  No finite computation is used in the theorem.  Section 7
records an abstract finite graph only as a route nonclosure; it is not a
counterexample to any host theorem.

Here `K_7^-` denotes `K_7` with one edge deleted.

## 1. Theorem

Let `G` be a finite simple seven-connected graph with no `K_7^-` minor.
Suppose that

\[
                    E=\{a,p\}\mathbin{\dot\cup}T,
                    \qquad |T|=5,                         \tag{1}
\]

is a vertex cut such that `G-E` has exactly two components `D,R`, each
adjacent to every vertex of `E`.  Suppose that `ap` is an edge, that `a,p`
have degree seven, and that they have a unique common neighbour `b`, where

\[
                          b\notin T.                       \tag{2}
\]

Assume that `G[D union T]` has a `T`-rooted `K_5`-minor model.  For such a
model

\[
                         \mathcal B=(B_t:t\in T),           \tag{3}
\]

put

\[
 \begin{split}
 C_a(\mathcal B)&=\{t\in T:E_G(\{a\},B_t)\ne\varnothing\},\\
 C_p(\mathcal B)&=\{t\in T:E_G(\{p\},B_t)\ne\varnothing\}.
 \end{split}                                                \tag{4}
\]

Then the following conclusions hold.

1. Every `T`-rooted `K_5` model in `G[D union T]` satisfies

   \[
                    |C_a(\mathcal B)\cup C_p(\mathcal B)|\le3. \tag{5}
   \]

2. For every such model,

   \[
   |C_p(\mathcal B)|=3\ \Longrightarrow\
   C_a(\mathcal B)\subseteq C_p(\mathcal B),             \tag{6}
   \]

   and the symmetric implication holds.  In particular, if both contact
   sets have order three, then they are equal.

3. There is a nonempty connected set `Y` which is either a proper subset of
   `R` or a proper subset of one branch set of a spanning `T`-rooted `K_5`
   model in `G[D union T]`, such that `N_G(Y)` is an actual vertex
   separator.  Consequently

   \[
                            |N_G(Y)|\ge7.                \tag{7}
   \]

   If equality holds, every component of `G-N_G(Y)` is adjacent to every
   vertex of `N_G(Y)`.

Conclusion 3 is the precise positive reduction supplied here.  In the first
case it is a new separator crossing the original component `R`, rather than
the original cut `E=N_G(R)`.  The conclusion does not assert that the
returned separator has order seven.

## 2. The joint contact bound

Fix a model (3).  If

\[
                    |C_a(\mathcal B)\cup C_p(\mathcal B)|\ge4,
\]

use the following seven branch sets:

\[
                 (B_t:t\in T),\qquad R,\qquad\{a,p\}.    \tag{8}
\]

The five rooted bags contribute the ten contacts of a `K_5`.  Fullness of
`R` to `E` makes `R` adjacent to every rooted bag through its root in `T`,
and also adjacent to the connected bag `\{a,p\}`.  The last bag is adjacent
to at least four rooted bags by assumption.  Thus (8) has at least

\[
                              10+5+1+4=20               \tag{9}
\]

contacts, and is a `K_7^-`-minor model.  This contradiction proves (5).

Suppose now that `|C_p(\mathcal B)|=3` and choose

\[
                         h\in C_a(\mathcal B)-C_p(\mathcal B).
\]

Enlarge `B_h` by `a`, retain the other four rooted bags, and use `R` and
the singleton bag `\{p\}`.  The five enlarged rooted bags still form a
`K_5` model.  The bag `R` is adjacent to all five and to `\{p\}`.  The
singleton `p` is adjacent to its three old contact bags and, through `ap`,
to the enlarged `h`-bag.  The contact count is again

\[
                              10+5+1+4=20.              \tag{10}
\]

This contradiction proves (6), and symmetry proves the other implication.

Because the two roots `a,p` have no common neighbour in `T`, (5) also gives
the useful boundary consequence

\[
                         |N_G(a)\cap T|+|N_G(p)\cap T|\le3. \tag{11}
\]

Indeed, each root in either boundary neighbourhood belongs to the
corresponding contact set, and the two boundary neighbourhoods are disjoint.

## 3. An exact sufficient split inside the remote component

The following formulation records exactly what is needed from `R`.  Fix a
model (3).  Let `U,V` be disjoint nonempty connected subsets of `R` such
that

\[
             E_G(\{a\},U)\ne\varnothing,
             \qquad E_G(\{p\},V)\ne\varnothing.        \tag{12}
\]

If

\[
 \begin{split}
 &|T-(C_a(\mathcal B)\cup N_T(U))|\\
 &\qquad +|T-(C_p(\mathcal B)\cup N_T(V))|\le1,        \tag{13}
 \end{split}
\]

then `G` contains a `K_7^-` minor.

To prove this, use the five bags in (3) together with

\[
                            U\cup\{a\},
                            \qquad V\cup\{p\}.          \tag{14}
\]

They are disjoint and connected, and the two new bags are adjacent through
`ap`; they need not be adjacent through an edge of `U-V`.  A rooted bag
`B_t` contains exactly the one vertex `t` of `T`.  Since `R` has no edge to
`D`, the first new bag meets `B_t` exactly when `t` belongs to
`C_a(\mathcal B) union N_T(U)`, and similarly for the second new bag.
Therefore the seven bags have at least

\[
                              10+1+(10-1)=20            \tag{15}
\]

contacts.  This proves the sufficient condition.

Notice that (13) does not require `U union V=R`.

## 4. Splitting the remote component

Choose a spanning `T`-rooted `K_5` model in `G[D union T]`.  Such a model
exists: starting from any rooted model, assign each component of the
uncovered subgraph to an adjacent branch bag, one component at a time.
The graph `G[D union T]` is connected because `D` is connected and is
adjacent to every root in `T`.

Suppose first that there are distinct vertices

\[
                         x\in N_G(a)\cap R,
                         \qquad y\in N_G(p)\cap R.      \tag{16}
\]

Take a spanning tree of `G[R]` and delete an edge of its `x`--`y` path.
Let `X_a,X_p` be the two resulting vertex sets, indexed so that they
contain `x,y`, respectively.  They are nonempty, connected, disjoint, and
partition `R`.  Put

\[
 \begin{split}
 d={}&|T-(C_a(\mathcal B)\cup N_T(X_a))|\\
    &+|T-(C_p(\mathcal B)\cup N_T(X_p))|.             \tag{17}
 \end{split}
\]

The five rooted bags together with `X_a union {a}` and
`X_p union {p}` have exactly the following guaranteed contacts:

\[
               \underbrace{10}_{\text{rooted }K_5}
               +\underbrace{1}_{\text{edge }ap}
               +\underbrace{10-d}_{\text{new bags to rooted bags}}
               =21-d.                                  \tag{18}
\]

If `d<=1`, this is a `K_7^-` model.  Target-freeness therefore gives
`d>=2`.  At least one of `X_a,X_p`, say `Y`, is anticomplete to one rooted
bag after allowing the corresponding endpoint contacts in (17).  In
particular, `Y` itself is anticomplete to that rooted bag.  The connected
set `Y` and the nonempty rooted bag lie in different components of
`G-N_G(Y)`.  Hence `N_G(Y)` is an actual separator.

If `b in D`, fullness of `R` to `a,p` supplies the two vertices in (16),
and their distinctness follows from the uniqueness of the common neighbour
`b`.  The same proof applies when `b in R` unless both endpoint
neighbourhoods in `R` are the singleton `\{b\}`.

## 5. The last location of the common neighbour

It remains to consider

\[
                         N_G(a)\cap R=N_G(p)\cap R=\{b\}. \tag{19}
\]

In particular `b in R`.  Since `d_G(a)=7`, the other five neighbours of
`a` besides `p,b` all lie in `D union T`.  The spanning model fixed in
Section 4 contains all five.  By (5), some branch bag `B_h` contains at
least two distinct neighbours of `a`.

We need an elementary tree partition.  Take a spanning tree of `G[B_h]`
and its minimal subtree containing `t_h` and all members of
`N_G(a) cap B_h`.  This minimal subtree has a leaf
`ell in (N_G(a) cap B_h)-\{t_h\}`.  Let `e` be the unique edge of the
minimal subtree incident with `ell`, delete `e` from the full spanning
tree, and let

\[
                            B_h=Z\mathbin{\dot\cup}W   \tag{20}
\]

be the resulting partition, with `ell in Z` and `t_h in W`.  Both parts
are nonempty, connected, and adjacent.  Every path in the tree from `ell`
to another specified terminal starts with `e`; hence all the other
specified terminals lie in `W`.  Thus `Z` contains the chosen neighbour of
`a`, while `W` contains another neighbour of `a`.

Use the following seven bags:

\[
       Z\cup\{a\},\qquad W,\qquad R\cup\{p\},
       \qquad (B_t:t\in T-\{h\}).                    \tag{21}
\]

The first three bags form a triangle.  The edge deleted in (20) joins the
first two, `ap` joins the first and third, and fullness of `R` at `t_h`
joins the second and third.  The four foreign rooted bags form a `K_4`,
and `R union {p}` is adjacent to all four through their roots.

Let `d'` be the total number of missing contacts from `Z union {a}` and
`W` to those four foreign rooted bags.  The guaranteed contact count for
(21) is

\[
                    \underbrace{3}_{\text{first triangle}}
                    +\underbrace{6}_{\text{foreign }K_4}
                    +\underbrace{4}_{R\cup\{p\}\text{ to the }K_4}
                    +\underbrace{8-d'}_{Z\cup\{a\},W\text{ to the }K_4}
                    =21-d'.                            \tag{22}
\]

If `d'<=1`, this is a `K_7^-` model.  Otherwise at least one of `Z,W` is
anticomplete to a foreign rooted bag.  That connected part is a set `Y`
for which `N_G(Y)` is an actual separator, exactly as in Section 4.

Sections 4 and 5 exhaust the two possible locations of `b` and prove
conclusion 3.

Finally, seven-connectivity gives (7).  If `|N_G(Y)|=7` and a component
of `G-N_G(Y)` missed a vertex `s` of the separator, then its neighbourhood
would be contained in the six-set `N_G(Y)-\{s\}`, contradicting
seven-connectivity.  This proves the equality-fullness assertion and the
theorem.  \(\square\)

## 6. A common-branch-set refinement

There is a useful local version of the preceding proof.  Suppose one common
contact bag `B_h` contains distinct vertices

\[
              x\in N_G(a)\cap B_h,
              \qquad y\in N_G(p)\cap B_h.             \tag{23}
\]

Split a spanning tree of `B_h` along its `x`--`y` path into connected
adjacent parts `X_a,X_p`.  Use

\[
 X_a\cup\{a\},\quad X_p\cup\{p\},\quad R,
 \quad (B_t:t\in T-\{h\}).                            \tag{24}
\]

If `d` is the total number of missing contacts from the two split parts,
with their attached endpoints, to the four foreign rooted bags, then the
seven bags in (24) have

\[
                               21-d                     \tag{25}
\]

guaranteed contacts: the four foreign bags contribute six, the two split
bags are adjacent, the split-to-foreign contribution is `8-d`, and `R` is
adjacent to the four foreign bags and to both endpoint bags.  Thus `d<=1`
gives the target, while `d>=2` gives an actual separator from a deficient
connected part.

Consequently, if neither the target nor this separator outcome occurs, a
common branch bag can contain only the single common neighbour `b` as both
of its endpoint contacts.  Since branch bags are disjoint, there is at most
one such common bag.  If `b in R`, there is none.

This refinement is conditional only on excluding the explicitly stated
separator outcome; the main theorem itself shows that some separator
outcome always occurs in the target-free core-concentrated profile.

## 7. Abstract contact data do not close the profile

The bound (5) alone cannot produce the target.  Let `Q` be the graph on

\[
                         \{q_1,\ldots,q_5,r,a,p\}
\]

in which the `q_i` form a `K_5`, the vertex `r` is adjacent to every other
vertex, `ap` is an edge, and the remaining endpoint contacts are

\[
                         N_Q(a)\cap\{q_i\}=\{q_1\},
 \qquad N_Q(p)\cap\{q_i\}=\{q_2,q_3\}.                \tag{26}
\]

Thus the joint contact set has order three.  The graph `Q` has 21 edges,
but it has no `K_7^-` minor.  Indeed, deleting any vertex leaves at most
18 edges.  Every edge of `Q` lies in a triangle, so contracting any edge
deletes that edge and creates at least one pair of parallel edges which is
then simplified; the resulting seven-vertex graph has at most 19 edges.
Any seven-branch minor model in an eight-vertex graph is obtained either by
using seven singleton vertices or by putting the ends of one edge in the
only branch set of order two.  These are exactly the deletion and
edge-contraction cases just checked.

This is only an abstract quotient obstruction to a contact-counting
argument.  It does not have the degree-seven multiplicity, literal-core
geometry, internal rooted structure, or seven-connectivity required in the
theorem.  It is not a counterexample to the theorem, the weighted splitter
theorem, the literal `K_{4,4}` case, or T44.

## 8. Exact scope

In the adjacent-singleton application, all hypotheses above are supplied
by the audited exact contraction trace and the audited singleton-neighbourhood
theorem: the two components are full, `a,p` are adjacent degree-seven
exterior vertices, their common neighbour is unique and lies outside `T`,
and the core-containing component has a `T`-rooted `K_5` model.

The theorem strengthens the previous separate three-contact bounds to the
joint bound (5), gives the containment restriction (6), and proves that the
remaining core-concentrated case necessarily returns an actual separator
from a connected part of one of the two relevant structures.  Its precise
remaining issue is quantitative: the proof supplies no upper bound on the
order of that separator.  Seven-connectivity supplies a lower bound of
seven, not equality.  Therefore this result does not by itself close the
adjacent-singleton case, the literal `K_{4,4}` case, T44, Conjecture 21, or
`HC_7`.
