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
