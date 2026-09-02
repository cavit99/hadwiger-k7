# Support normal form at the remaining two-component three-cut

**Status.** Written unbounded theorem; separate hash-pinned internal audit
GREEN.  This
result classifies the five support sets at a two-component three-cut under
the six-boundary inequality and the prohibition on bonds splitting three
supports.  It does not eliminate the two-component cut, the nonsingleton or
singleton literal-core residues, the literal `K_{4,4}` case of T44, T44,
Conjecture 21, or `HC_7`.

## 1. Abstract statement

Let `X` be a finite simple three-connected graph, and let
`R_1,...,R_5` be five indexed subsets of `V(X)`, each of order at least two.
For a nonempty proper connected set `W subset V(X)`, put

\[
 q(W)=|N_X(W)|+|\{i:R_i\cap W\ne\varnothing\}|.
\]

Assume

\[
 q(W)\ge6                                                     \tag{1}
\]

for every such `W`, and assume that every bond of `X` splits at most two of
the five supports, where a bond `X=A dotcup Z` splits `R_i` when both
`R_i cap A` and `R_i cap Z` are nonempty.

### Lemma 1.1 (three separated pairs give a bond)

Let `T={r,s,t}` be a three-cut of `X`, and let `P,Q` be distinct components
of `X-T`.  If

\[
 x_P,y_P\in P,\qquad x_Q,y_Q\in Q
\]

are two pairs of distinct vertices, then there is a bond of `X` which
simultaneously separates `x_P` from `y_P`, `x_Q` from `y_Q`, and `s` from
`t`.

#### Proof

The graph `X-r` is two-connected.  Set-Menger in `X-r` gives two
vertex-disjoint paths from `{x_P,y_P}` to `{s,t}` which saturate both end
sets.  Trim them at their first vertex of `{s,t}`.  Their interiors then lie
in `P`, one ends at `s`, and the other ends at `t`.  The same construction in
`Q` gives a second pair of paths whose interiors lie in `Q`.

Let `A_0` be the union of the two paths ending at `s`, and let `Z_0` be the
union of the two paths ending at `t`.  These are disjoint connected sets.
They put opposite members of each of the three specified pairs on opposite
sides.  If they are not adjacent, split the internal vertices of a shortest
`A_0`--`Z_0` path between its two ends so that the enlarged sets remain
disjoint, connected, and become adjacent.  Every component of the remaining
unused graph has an edge to their union; assign that component wholly to a
side which it meets.  The resulting spanning partition is a bond and still
separates all three pairs. \(\square\)

### Theorem 1.2 (two-component support normal form)

Let `T` be a three-cut of `X` for which `X-T` has exactly two components
`P,Q`.  Put

\[
 I_P=\{i:R_i\cap P\ne\varnothing\},\qquad
 I_Q=\{i:R_i\cap Q\ne\varnothing\},\qquad
 B=I_P\cap I_Q.                                             \tag{2}
\]

Then all of the following hold.

1. `N_X(P)=N_X(Q)=T`.  For every `J subseteq T`,
   \[
      X=(P\cup J)\mathbin{\dot\cup}(Q\cup(T-J))             \tag{3}
   \]
   is a bond.
2. Every support meets `T` in at most one vertex.
3. The number of supports meeting both components satisfies
   \[
                              1\le |B|\le2.                  \tag{4}
   \]
4. If `|B|=2`, each of the other three supports is contained wholly in one
   component, and they have a `1+2` distribution between `P` and `Q`.
5. If `|B|=1`, exactly two of the other supports meet `P` and not `Q`, and
   exactly two meet `Q` and not `P`.  On either component side at most one
   of its two supports meets `T`, so each component contains a whole
   support.  If a `P`-side support and a `Q`-side support both meet `T`,
   their unique vertices in `T` are equal.

#### Proof

Three-connectivity gives `N_X(P)=N_X(Q)=T`.  Every vertex of `T` has a
neighbour in each component.  Consequently both sets in (3) are nonempty
and connected for every `J subseteq T`, proving item 1.

By (1),

\[
                         |I_P|\ge3,\qquad |I_Q|\ge3.         \tag{5}
\]

The component bond `(P,X-P)` splits at most two supports.  Since `P` meets
at least three supports, some support `E_P` is contained wholly in `P`.
Likewise, there is a support `E_Q` contained wholly in `Q`.  Choose two
distinct vertices in each; support multiplicity makes this possible.

Suppose that some support `R_i` contains distinct vertices `s,t in T`, and
write `T={r,s,t}`.  Lemma 1.1 applied to the chosen pairs in `E_P,E_Q`
gives a bond separating both pairs and `s,t`.  That bond splits
`E_P,E_Q,R_i`, a contradiction.  Thus every support meets `T` in at most
one vertex, proving item 2.  In particular, no support can be contained in
`T`, since every support has order at least two.

The lower bound in (4) follows from (5) and inclusion-exclusion:

\[
             |B|=|I_P\cap I_Q|
                  \ge |I_P|+|I_Q|-5\ge1.
\]

Every member of `B` is split by the component bond, so the global bond
restriction gives `|B|<=2`.  This proves item 3.

Suppose first that `|B|=2`.  Those two supports exhaust the split allowance
of each component bond.  Hence every other support meeting `P` is wholly
contained in `P`, and the analogous statement holds for `Q`.  No support is
contained in `T`, so the other three supports all belong to one component.
Equation (5) forces at least one on each side, giving the `1+2`
distribution in item 4.

Now suppose that `|B|=1`.  The four remaining supports cannot meet both
components and cannot be contained in `T`.  Equation (5) requires at least
two of them on each component side, so exactly two meet `P` and not `Q`, and
exactly two meet `Q` and not `P`.  If both `P`-side supports met `T`, then
they and the member of `B` would all be split by `(P,X-P)`, a contradiction.
Thus at most one does, and the other is wholly contained in `P`; the same
argument applies to `Q`.

Finally suppose that a `P`-side support meets `T` at `t_P` and a `Q`-side
support meets `T` at `t_Q`.  These vertices are unique by item 2.  If they
were distinct, use `J={t_Q}` in (3).  The resulting bond splits the member
of `B`, the `P`-side support because `t_P` lies opposite `P`, and the
`Q`-side support because `t_Q` lies opposite `Q`.  This contradiction gives
`t_P=t_Q` and completes item 5. \(\square\)

## 2. Application to the literal blocker

In the target-free nonsingleton minimum-blocker setting, the audited
[three-support bond theorem](hc7_k44_three_support_bond_and_threecut_reduction.md)
supplies all hypotheses of Theorem 1.2: the five non-atom supports have
order at least two, satisfy (1), and no bond splits three of them.  It also
shows that every surviving three-cut has exactly two components.  Therefore
every such cut has precisely one of the two support-incidence types in items
4 and 5.

The remaining nonsingleton problem is now narrower than an arbitrary
two-component cut.  It is enough to eliminate these two types while also
using the sequential minimum support-full path, its exact subpath formula,
and the distinguished `a,b` incidence retained by the blocker theorem.

## 3. The simultaneous parity obstruction

The support normal form also identifies the exact global obstruction which
any remaining example must realize.  We use Theorem 1.2 of
Chen--Ding--Yu--Zang, [*Bonds with Parity
Constraints*](https://www.math.lsu.edu/~ding/bonds.pdf), in the form recorded
and audited in the [five-support bond
reduction](hc7_k44_five_support_bond_reduction.md): a nontrivial acyclic
quadruple on a two-connected graph either has the prescribed parity bond or
is weakly linkable in their precise sense.

### Lemma 3.1 (small torso separations contain three supports)

Retain a component `P` of `X-T`, and let `S_P` be the indexed supports which
meet `P`.  Form the torso `Y=X[P union T]+K_T`.  Suppose `|Z|<=3`, the set
`W subseteq P` is the vertex set of a component of `Y-Z`, and
`Y-(Z union W)` is nonempty.  Then

\[
 |N_X(W)|=3
 \quad\hbox{and}\quad
 |\{i:R_i\cap W\ne\varnothing\}|\ge3.                     \tag{6}
\]

In particular, when `|S_P|=3`, the set `W` meets every support in `S_P`.

#### Proof

The set `W` has no neighbour in `Q`, and its neighbours in `P union T` all
belong to `Z`.  Hence `N_X(W) subseteq Z`.  Three-connectivity gives
`|N_X(W)|>=3`, so equality holds.  Now (1) gives the support lower bound in
(6).  Every support meeting `W` belongs to `S_P`, which proves the final
assertion. \(\square\)

### Theorem 3.2 (a smallest three-support side has a four-connected torso)

Assume now the target-free nonsingleton minimum-blocker setting of Section 2.
Among all pairs `(T,P)` in which `T` is a three-cut and `P` is a component
of `X-T` meeting exactly three supports, choose one with `|P|` minimum.  Such
a pair exists.  Then the torso

\[
                         Y=X[P\cup T]+K_T                        \tag{7}
\]

is four-connected.  If `S_P` denotes the three supports meeting `P`, then
either exactly one member of `S_P` is contained wholly in `P` and the other
two have vertices outside `P`, or exactly two are contained wholly in `P`
and the third meets both components of `X-T`.  Moreover, for every nonempty
connected `W subseteq P`,

\[
 |N_Y(W)|+|\{i\in S_P:R_i\cap W\ne\varnothing\}|\ge6.          \tag{8}
\]

#### Proof

The preceding audited three-support theorem gives a three-cut, and says that
every such cut has exactly two components.  Existence now follows from
Theorem 1.2: in the two-bridge type, the component which contains only one of
the other three supports meets exactly three, while in the one-bridge type
both components meet exactly three.

First, `Y` is three-connected.  Delete at most two vertices.  Some vertex of
`T` remains, and the surviving vertices of `T` form a clique in `Y`.  Every
component of `P` after the deletion has a neighbour in `T` outside the
deleted set; otherwise at most two vertices would separate that component
in `X`.  Hence all surviving vertices of `Y` lie in one component.

Suppose that `Z` is a three-cut of `Y`.  It is not `T`, since `Y-T=P` is
connected.  The clique on `T` puts all vertices of `T-Z` in one component
`C_0` of `Y-Z`.  Every other component `W` lies in `P`.  Its neighbourhood
in both `Y` and `X` is `Z`.  In `X-Z`, the other original component of
`X-T` attaches to `T-Z` and hence joins `C_0`.  Thus the components of
`Y-Z` other than `C_0` are also precisely the remaining components of
`X-Z`.  The audited three-support theorem says that every three-cut of `X`
has exactly two components.  Consequently there is exactly one such `W`.

Lemma 3.1 says that `W` meets at least three supports.  Only the three
members of `S_P` can meet a subset of `P`, so `W` meets all three.  Since
`Z ne T`, at least one vertex of `P` lies in `Z` or in `C_0`; hence
`|W|<|P|`.  The pair `(Z,W)` contradicts the choice of `P`.  Therefore `Y`
has no three-cut.  A singleton component `P` would have degree three in
`X`, contrary to `delta(X)>=4`; thus `|V(Y)|>=5`, and `Y` is
four-connected.

The two support alternatives follow directly from Theorem 1.2.  On a
three-support side of the two-bridge type, one support is wholly inside and
the two bridge supports have vertices outside.  On a side of the one-bridge
type, the bridge support has vertices outside, while at least one of the two
side supports is wholly inside; according as the other side support meets
`T` or not, exactly one or exactly two supports are wholly inside.  Finally,
for `W subseteq P`, no support outside `S_P` meets `W`, and adding the edges
of `K_T` does not change `N_X(W)`.  Thus (8) is exactly (1). \(\square\)

### Corollary 3.3 (a Cartesian family of weakly linkable triples)

Choose any supports `E_P subseteq P` and `E_Q subseteq Q`, any support `H`
which meets both components, arbitrary two-element sets

\[
 A_P\subseteq E_P,\qquad A_Q\subseteq E_Q,
\]

and arbitrary vertices `x in H cap P`, `y in H cap Q`.  Then the quadruple

\[
                    (X;A_P,A_Q,\{x,y\})                    \tag{9}
\]

is weakly linkable.  Thus this conclusion holds simultaneously for every
choice in the full Cartesian family of two local support pairs and one
bridge-support pair.

#### Proof

The three displayed two-element sets belong to three distinct indexed
supports.  Their symmetric difference is nonempty: its intersection with
`P` is `A_P` symmetric-differenced with `{x}`, which has odd order whether
or not `x` lies in `A_P`.  Hence (9) is nontrivial and acyclic.

A feasible parity bond would separate both vertices of all three sets and
therefore split `E_P,E_Q,H`.  The universal three-support bond prohibition
excludes this.  Since `X` is three-connected, it is two-connected, so the
Chen--Ding--Yu--Zang theorem forces (9) to be weakly linkable. \(\square\)

Consequently the remaining nonsingleton theorem can be stated precisely as
a **simultaneous weak-linkability exclusion**: prove that the complete family
(9) cannot all be weakly linkable in either incidence type of Theorem 1.2
when the six-boundary inequality, the small-torso restriction (6), and the
sequential minimum-path data hold.  It is not enough to make one fixed
choice of the three pairs; the obstruction is universal over all such
choices.

## 4. Exact localized completion lemma

Use the minimum pair `(T,P)` and four-connected torso `Y` from Theorem 3.2.
Call a member of `S_P` **whole** if it is contained in `P`, and **external**
if it has a vertex outside `P`.  There are either one whole and two external
supports, or two whole and one external support.

> **Triangle-boundary torso bisection lemma (open).**  There is a nonempty
> connected set `A subset P` such that `Y-A` is connected, `A` meets every
> external support, and
> \[
>        A\cap E\ne\varnothing\ne(P-A)\cap E
> \]
> for every whole support `E`.

This is exactly a component-side three-support bond.  Indeed, the displayed
conditions split every whole support, while `A` meets each external support
and its vertex outside `P` lies in the other shore.  The graph `X-A` is
connected: start from the connected graph `Y-A` and replace every added
edge of the triangle `K_T` by a path through the connected component `Q`,
which is adjacent to every vertex of `T`.  Thus `(A,X-A)` is a bond splitting
all three members of `S_P`, contrary to the global restriction.

Conversely, if a bond with one shore `A subset P` splits all three members
of `S_P`, then `A` has exactly the displayed support properties, and
connectivity of `X-A` implies connectivity of `Y-A` after the component `Q`
is replaced by the triangle on `T`.  Hence the open lemma is equivalent to
finding a three-support bond whose one shore stays inside the selected
minimum component.  Proving it would eliminate every nonsingleton blocker.

The lemma is not a consequence of four-connectivity and (8) alone.  The
adjacent [stripped-torso
barrier](../barriers/hc7_k44_three_support_torso_bisection_barrier.md) is a
`K_5` torso with one whole and two external supports, all local scores equal
to six, but no such set `A`.  It lacks the complementary component, the two
other supports, their exact global provenance, and the minimum-path data.
At least one of those retained global inputs must therefore enter the proof.
