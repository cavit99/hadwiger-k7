# The exact Kempe consequence of the forbidden all-proper signature

**Status:** written unbounded proof;
[separate internal audit GREEN](hc7_k7minus_matching_forbidden_signature_kempe_coupling_audit.md).
Theorems 2.1 and 3.1 isolate what the absent fourth signature
really forces for two vertex-disjoint critical edges.  Section 4 records the
first remaining unsupported inference.  This note does not prove the
`K_7^-` six-colour conjecture or `HC_7`.

## 1. Setting

Let `q>=2`, let `G` be a graph with `chi(G)>q`, and let

\[
                     e=ab,\qquad f=cd                         \tag{1.1}
\]

be vertex-disjoint edges.  Put

\[
                     H=G-\{e,f\}.                              \tag{1.2}
\]

Suppose `phi` is a proper `q`-colouring of `H` with signature
`(equal,proper)`:

\[
  \phi(a)=\phi(b)=i,
  \qquad \phi(c)=r\ne s=\phi(d).                               \tag{1.3}
\]

No proper `q`-colouring of `H` has signature `(proper,proper)`, since such
a colouring would remain proper after restoring both edges.  This is the
only global colouring prohibition used in Section 2.

For `j ne i`, call `ab` **`i`--`j` locked** when `a,b` lie in one component
of the subgraph of `H` induced by colours `i,j`.

## 2. An unlocked palette couples both critical edges

### Theorem 2.1 (unique unlocked palette and crossed components)

In the setting of Section 1:

1. `ab` is locked for every colour `j ne i`, with at most one exception;
2. if `ab` is not `i`--`j` locked, then

   \[
                         \{r,s\}=\{i,j\};                       \tag{2.1}
   \]

3. in that exceptional palette, let `D_a,D_b` be the two distinct
   `i`--`j` components containing `a,b`, respectively.  Then each of
   `D_a,D_b` contains exactly one of `c,d`;
4. both restored edges `e,f` run between `D_a` and `D_b`; and
5. interchanging `i,j` on either one of `D_a,D_b` changes the signature
   directly from `(equal,proper)` to `(proper,equal)`.

The symmetric statement holds starting from a `(proper,equal)` colouring.

#### Proof

Fix `j ne i` and suppose `a,b` lie in distinct `i`--`j` components.  Switch
the component `D_a` containing `a`.  This preserves properness of `H` and
makes the ends of `e` different.  The resulting colouring cannot make the
ends of `f` different, because that would be the forbidden all-proper
signature.  Thus the switch makes `c,d` equal.

A switch on colours `i,j` can turn two initially different colours into
one colour only when those initial colours are exactly `i,j` and the
switched component contains exactly one of the two vertices.  Hence
(2.1) holds and `D_a` contains exactly one of `c,d`.

Return to the original colouring `phi` and apply the same argument to the
component `D_b` containing `b`.  Switching it also makes `e` proper, so it
too contains exactly one of `c,d`.  The
components are disjoint and there are only two endpoints of `f`; therefore
each component contains one endpoint and together they contain both.  The
edge `e` has one end in each by definition, and `f` has one end in each by
the preceding conclusion.  Switching either component changes exactly one
end of each pair and produces `(proper,equal)`.

For fixed `phi`, the unordered pair `\{r,s\}` is fixed.  Equation (2.1)
therefore permits at most one exceptional colour `j`.  Every other palette
locks `ab`, proving item 1.  Symmetry proves the final assertion. `\square`

For `q=6`, every one-edge response therefore gives its equal pair at least
four common-host bichromatic locks.  The theorem strengthens that numerical
count: if the fifth palette is unlocked, its two components contain the
four literal endpoints in a crossed allocation and either component is an
actual one-step transition between the two singleton responses.

## 3. What a direct transition returns in the critical host

Assume now that

\[
 \chi(G)=7,
 \qquad \chi(J)\le6\text{ for every proper minor }J\text{ of }G,
 \qquad \kappa(G)\ge7,
 \qquad K_7\npreccurlyeq G,                                  \tag{3.1}
\]

and put `q=6`.  Retain the exceptional case of Theorem 2.1 and choose
`D` to be either of `D_a,D_b`.  Put

\[
                              S=N_G(D).                         \tag{3.2}
\]

### Theorem 3.1 (direct transition separation or five-chromatic complement)

Exactly one of the following holds.

1. `D` is not dominating.  Then `S` is the boundary of an actual
   separation, `|S|>=7`, and the two opposite singleton-response
   colourings agree literally on `G-D`.  Their common equality partition
   on `S` is realised by a proper colouring of `G-D` and is rejected by
   the intact `D`-side.
2. `D` is dominating.  Then

   \[
                     \chi(G-D)=5,
                     \qquad K_6\npreccurlyeq G-D.               \tag{3.3}
   \]

#### Proof

The subgraph `H[D]` is a connected component of a two-colour graph and is
bipartite.  Each restored edge has exactly one endpoint in `D`, by
Theorem 2.1.  Hence neither restored edge lies inside `D`, and

\[
                              G[D]=H[D]                          \tag{3.4}
\]

is bipartite.

Let `phi'` be obtained from `phi` by switching `D`.  The colourings
agree on every vertex outside `D`.  Theorem 2.1 says that their signatures
are the two opposite singleton signatures.  Removing `D` removes one end
of each restored edge, so their common restriction is a proper colouring
of the intact graph `G-D`.

If `D` is not dominating, a vertex outside `N_G[D]` and the nonempty set
`D` lie on opposite sides of `S`, so `S` is an actual separator.
Seven-connectivity gives `|S|>=7`.  If a proper six-colouring of
`G[D union S]` induced exactly the same equality partition on `S`, align
colour names and glue it to the common exterior colouring.  This would
six-colour `G`.  Thus that partition is rejected by the intact side,
proving outcome 1.

Suppose instead that `D` dominates.  If `G-D` were four-colourable, use
two disjoint new colours on the bipartite graph `G[D]`.  The disjoint
palettes make every edge between the two parts proper and would six-colour
`G`.  Hence `chi(G-D)>=5`.

If `G-D` contained a `K_6` model, the connected dominating set `D` would
be adjacent to all six branch sets and would complete them to a `K_7`
model in `G`.  Thus `G-D` is `K_6`-minor-free.  The established case
`HC_6` gives `chi(G-D)<=5`, proving (3.3). `\square`

The argument in outcome 1 supplies no upper bound on the separator order.
Seven-connectivity supplies the lower bound but does not turn it into an
order-seven or order-eight separation.

### Theorem 3.2 (crossed pair, low-colour boundary, and domination exclusion)

Let

\[
                             U=D_a\cup D_b.                       \tag{3.5}
\]

Then `G[U]` is connected and three-colourable, every vertex of
`N_G(U)` has one of the four colours outside `\{i,j\}`, and the following
statements hold.

1. If `U` is not dominating, then `N_G(U)` is the boundary of an actual
   separation of order at least seven.  Its displayed colouring uses at
   most four boundary colours, is realised on the exterior, and is
   rejected by the intact `U`-side.
2. If `U` is dominating, then

   \[
                  \chi(G-U)=4,
                  \qquad K_6\npreccurlyeq G-U.                    \tag{3.6}
   \]

3. The components `D_a,D_b` cannot both be dominating.

Consequently, every direct singleton-to-singleton interchange yields a
response-bearing separator from Theorem 3.1.

#### Proof

Distinct `i`--`j` components have no edge between them in `H`.  Theorem
2.1 says that both omitted edges have one endpoint in each component.
Thus `G[U]` is obtained from the two connected bipartite graphs
`H[D_a],H[D_b]` by adding the two independent edges `e,f`.  Colour both
components with two colours, orienting their bipartitions so that `e` is
proper.  If `f` is then proper, this is a two-colouring of `G[U]`.  If
not, its ends have one colour; recolour either end of `f` with a third
colour.  That vertex is incident with only one of the two added edges,
because `e,f` are vertex-disjoint, and its neighbours inside its original
bipartite component all have the other old colour.  This is a proper
three-colouring of `G[U]`.  The two added edges also make `G[U]`
connected.

Let `x in U` and `y notin U` be adjacent in `G`.  Neither omitted edge
leaves `U`, so `xy` belongs to `H`.  If `phi(y)` belonged to `\{i,j\}`,
then this proper bichromatic edge would place `y` in the same `i`--`j`
component as `x`, contrary to the definition of `U`.  Thus every boundary
vertex has one of the other four colours.

If `U` is not dominating, its neighbourhood is an actual separator and
has order at least seven.  The restriction of `phi` to `G-U` is proper,
because both omitted edges lie inside `U`.  The usual alignment-and-gluing
argument shows that its boundary partition cannot extend through
`G[U union N_G(U)]`.  This proves item 1.

If `U` dominates, every vertex of `G-U` is a boundary vertex, so the same
restriction four-colours `G-U`.  A three-colouring of `G-U`, together
with the three-colouring of `G[U]` on a disjoint palette, would six-colour
`G`.  Hence `chi(G-U)=4`.  A `K_6` model in `G-U`, completed by the
connected dominating set `U`, would be a `K_7` model in `G`.  This proves
item 2.

Finally suppose both components dominate.  Every vertex of `D_b` must
then be incident with an edge to `D_a`.  The only such edges are `e,f`,
and their endpoints are distinct, while Theorem 2.1 already puts both
endpoints in `D_b`.  Hence `D_b` consists of precisely those two vertices;
symmetrically, so does `D_a`.  Connectedness supplies one `H`-edge inside
each pair, there are no `H`-edges between the pairs, and restoring `e,f`
supplies exactly the other two edges.  Thus the four endpoints induce a
four-cycle `C` whose opposite edges are `e,f`.

Contract `C` to one vertex and call the resulting proper minor `L`.  If
`L` had a five-colouring, expand the contraction vertex by giving one
independent pair of `C` its old colour and the other pair a fresh sixth
colour.  This would six-colour `G`; hence `chi(L)=6`.  By `HC_6`, take a
spanning `K_6` model in `L` and lift its contraction bag.  The other five
bags are disjoint from `D_a,D_b`.  Since both components dominate, each
is adjacent to all five bags, and the two components are adjacent through
`e,f`.  They and the five foreign bags form a `K_7` model, contrary to
(3.1).  This proves item 3. `\square`

### Theorem 3.3 (the endpoint cycle gives one four-rooted common model)

Assume the opposite-shore placement

\[
 V(G)=A\mathbin{\dot\cup}T\mathbin{\dot\cup}B,\qquad
 E_G(A,B)=\varnothing,\qquad
 e=up,\quad f=vq,                                    \tag{3.7}
\]

where `u in A`, `v in B` and `p,q in T`.  If the four endpoints induce
the cycle

\[
                         u-p-v-q-u,                    \tag{3.8}
\]

then contracting that cycle gives a graph `L` satisfying

\[
                         \chi(L)=6,qquad \kappa(L)\ge4. \tag{3.9}
\]

The graph `L` has a spanning `K_6` model.  On lifting it to `G`, one
branch bag contains all four endpoints.  That bag admits connected
splittings extending each of

\[
                  \{u,p\}\mid\{v,q\},qquad
                  \{u,q\}\mid\{p,v\}.                 \tag{3.10}
\]

If an order-four cut of `L` exists, it contains the contraction vertex
and lifts to an actual order-seven separation of `G` carrying a rejected
proper-minor colouring partition.

#### Proof

Let `w` be the vertex obtained by contracting the cycle.  The proper
minor `L` is six-colourable.  If it had a colouring with at most five
colours, give the independent pair `\{p,q\}` the old colour of `w` and
the independent pair `\{u,v\}` one fresh sixth colour.  Every neighbour
outside the cycle avoided the old colour at `w`, and all four cycle edges
go between the two displayed pairs.  This would six-colour `G`, proving
`chi(L)=6`.

A cut of `L` not containing `w` would also disconnect `G`, so it has order
at least seven.  A cut `Q` containing `w` lifts to

\[
                         (Q-\{w\})\cup\{u,p,v,q\},     \tag{3.11}
\]

whose order is `|Q|+3`.  Seven-connectivity therefore excludes
`|Q|<=3`, proving `kappa(L)>=4`.  When `|Q|=4`, (3.11) is an actual
order-seven separator.  Every component behind it is full by
seven-connectivity, and deleting any edge between a component and the
separator gives the standard exterior-realised, intact-side-rejected
proper-minor partition.

The established case `HC_6` gives a `K_6` model in `L`; connectedness
allows it to be made spanning.  Lift `w` inside its branch bag, replacing
it by the whole cycle.  To obtain either split in (3.10), begin with its
two connected cycle edges.  Every component of the rest of that branch
bag has a neighbour in the cycle and may be assigned wholly to a side it
meets.  The two resulting sets are connected and partition the bag.
`\square`

Combining Theorems 2.1--3.2 gives the exact host-level dichotomy for one
singleton response in the matching row:

\[
 \boxed{
 \begin{array}{c}
   \text{all five alternate palettes lock the equal coordinate;}\\
   \text{or an actual response-bearing separator is returned.}
 \end{array}}                                             \tag{3.12}
\]

Indeed, an unlocked palette invokes Theorem 3.2.  Its two crossed
components cannot both dominate, so Theorem 3.1 applies to one of them.

## 4. Exact nonclosure at a blocked common model split

In the live matching row, additional proved data coexist with the setting
above:

* `H` is six-connected;
* all three nonempty edge signatures occur and the all-proper signature is
  absent;
* `G/e/f` is exactly six-chromatic; and
* one spanning `K_6` model lifted from `G/e/f` co-bags both endpoint pairs.

Theorems 2.1--3.2 record direct consequences of spending the absent
signature through Kempe switching.  They eliminate every unlocked palette
unless it returns an actual response-bearing separator.  When all five
palettes are locked, however, they do not allocate a lock path to a
branch-set label of the independently selected model.

This is a literal mismatch of vertex partitions.  The sets `D_a,D_b` are
components defined by one pair of colour classes.  A branch bag may meet
both components, one component may traverse several bags, and a path
between the endpoints may pass from a bag meeting only the first side to a
different bag meeting only the second.  Since the five foreign bags are
pairwise adjacent, such a path does not force any one foreign bag to meet
both sides of the selected root-bag split.

Consequently the following inference is unsupported:

\[
 \begin{gathered}
   \text{four palette locks or one crossed response transition}\
   +\text{ one common co-bagged }K_6\text{ model}
 \end{gathered}
 \quad\Longrightarrow\quad
 \text{four foreign bags adjacent to both split sides}.        \tag{4.1}
\]

Nor does Theorem 3.1 by itself produce the other desired terminal output.
Its separator has order at least seven, but this argument supplies no upper
bound.  Applying it to only one of the two crossed components can also
return a dominating component with a five-chromatic `K_6`-minor-free
complement; Theorem 3.2 shows that the other crossed component then returns
the separator.

There is a second independent reconfiguration obstruction.  The exact
signature set does not imply that a Kempe component of the six-colouring
reconfiguration graph meets both singleton-response families.  Even when
one does, a shortest route may pass through a double-equality colouring
rather than contain a direct singleton-to-singleton interchange.  The
switches on the two sides of that intermediate colouring need not use the
same palette component.

Thus these uses of the forbidden signature do not by themselves close the
model exchange.  A positive repair could add one of the following genuinely
new conclusions:

1. a branch-bag-respecting version of Theorem 2.1;
2. an upper bound `|N_G(D)|<=8` for one crossed transition component; or
3. a theorem which turns the low-colour separator partition of Theorem 3.2
   into a common original-shore partition or an anchored descent.

Additional unlabelled fans or another count of locked palettes would not
prove any of these three statements.

## 5. Relation to the matching common-state theorem

The corrected
[`matching common-state theorem`](hc7_k7minus_matching_square_common_state.md)
uses connector paths only to obtain a cycle through the two coordinates;
it correctly declines to contract that arbitrary cycle.  Its Theorem 2.6
incorporates Theorems 2.1 and 3.1 above with the both-dominating exclusion
from Theorem 3.2, giving the concise conclusion that an unlocked singleton
response always returns a separator.  The rigorous common minor model used
elsewhere in that theorem remains the double-contraction model, which co-bags
the two coordinate pairs but need not co-bag all four endpoints in one bag.

## Dependencies and scope

Theorem 2.1 is elementary Kempe-component switching.  Theorems 3.1--3.2 use
seven-connectivity, `K_7`-minor exclusion and the established case `HC_6`,
due to Robertson, Seymour and Thomas,
[*Hadwiger's conjecture for `K_6`-free graphs*](https://doi.org/10.1007/BF01202354).
It is unbounded and computation-free.  Section 4 is a recorded route
nonclosure, not a counterexample to a theorem using further labelled
critical-host structure.
