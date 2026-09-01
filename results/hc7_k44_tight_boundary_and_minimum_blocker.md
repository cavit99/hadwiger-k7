# Tight boundary colouring and minimum blockers in a literal `K_{4,4}` exterior

**Status.** Written unbounded reduction; the adjacent audit identifies the
exact checked revision.  The finite hostile screen mentioned in Section 8 is
evidence only and is not used in any proof.  This result does not prove the
weighted splitter theorem, the literal case of T44, T44, Conjecture 21, or
`HC_7`.

## 1. Setting and main statement

Let `G` be a finite simple seven-connected graph with no `K_7^-` minor.
Suppose that `G` contains a specified literal `K_{4,4}` with vertex set `S`
and shores `S_0,S_1`, and put `C=G-S`.  For nonempty `Y subseteq V(C)`, put

\[
 L(Y)=N_G(Y)\cap S,\qquad
 \partial Y=N_C(Y)\mathbin{\dot\cup}L(Y),\qquad
 \lambda(Y)=|\partial Y|.                            \tag{1}
\]

Seven-connectivity gives

\[
                         \lambda(Y)\ge 7             \tag{2}
\]

for every nonempty `Y subseteq V(C)`, including `Y=V(C)`.

### Theorem 1.1 (tight boundaries and minimum crossing blockers)

The following statements hold.

1. If `Y subseteq V(C)` is nonempty and connected and
   `lambda(Y)=7`, then `partial Y` is an actual seven-vertex cut.  The graph
   `G[partial Y]` has a bipartition of orders three and four which extends
   the literal-shore colouring on `L(Y)`.

2. Let `A={a}` be the singleton all-edge atom supplied by the audited
   [singleton-atom reduction](hc7_k44_positive_atom_elimination.md).  Let
   `ab` be a three-contractible edge crossing from `a` to its exterior
   vertex boundary, and choose a connected tight blocker `X` of `ab` with
   minimum order.  Then either

   \[
                              |X|=1,                 \tag{3}
   \]

   or `G[X]` is three-connected and

   \[
                         \delta(G[X])\ge4.           \tag{4}
   \]

3. In the nonsingleton outcome, write the exact boundary normal form from
   the singleton-atom theorem as

   \[
       D:=\partial X=\{a,b\}\mathbin{\dot\cup}K,
       \qquad |K|=5,
       \qquad H=\{b\}\mathbin{\dot\cup}K,           \tag{5}
   \]

   and put `P=N_X(a)`.  Every resource `k in K` has at least two neighbours
   in `X`.  There is a vertex `p in P` such that

   \[
       N_D(X-p)\cap H=H,
       \qquad |N_D(p)\cap K|\le2.                   \tag{6}
   \]

   Here `N_D(U)` denotes the members of the actual boundary `D` having a
   neighbour in `U`; this includes literal-core resources in `D cap S`.
   For `d in D`, write `N_X(d)=N_G(d) cap X`.

4. If `T` is a three-cut of `G[X]`, then `G[X]-T` has at most three
   components.  If it has exactly three components, their `K`-contacts have
   exactly one of the following forms.

   - Two resources of `K` meet all three components, while each of the
     remaining three resources has all its neighbours in one distinct
     component.
   - After indexing the components as `W_1,W_2,W_3`, the component `W_1`
     contains every neighbour in `X` of both `a` and `b`.  Exactly three
     resources of `K` are not supported wholly inside a single component,
     and all three meet `W_1`.  Each of `W_2,W_3` contains every
     `X`-neighbour of one distinct remaining resource and meets at least two
     of the three non-component-exclusive resources.

Thus an inclusion-minimal nonsingleton crossing blocker is not an arbitrary
connected set: it is a minimum-degree-four three-connected shore, all five
non-atom boundary resources are multiply attached, and deleting a specified
atom-neighbour leaves all six resources in `H` represented while that
neighbour sees at most two members of `K`.  Every three-cut has the sharply
bounded component profiles in item 4.

The proof first establishes a general exact-boundary theorem and then uses
an explicit two-helper `K_7^-` construction to eliminate every cut of order
at most two and every degree-three vertex in a minimum blocker.

## 2. Every tight connected set has a bipartite `3`-by-`4` boundary

Let `Y` be as in item 1 and put

\[
                 D=\partial Y,\qquad
                 D_S=D\cap S,\qquad D_C=D-S.         \tag{7}
\]

The connected graph `G[Y]` is a component of `G-D`: every exterior
neighbour of `Y` lies in `D_C`, and every literal-core neighbour lies in
`D_S`.  Also `S-D_S` is nonempty because `|D|=7<|S|`.  Hence `D` is an
actual cut.  Every component of `G-D` is adjacent to every member of `D`,
since otherwise six vertices of `D` would still separate that component.

The audited
[seven-cut component theorem](hc7_k7minus_seven_cut_three_component_bound.md)
says that `G-D` has at most three components.  Besides `Y`, denote them by
`W_1,...,W_h`, where `1<=h<=2`.  Put `S_*=S-D_S`.  Since `|D|=7`,

\[
                         |S_*|=|D_C|+1.              \tag{8}
\]

Every member of `S_*` belongs to one of the `W_i`.  Partition

\[
                         D_C=D_1\mathbin{\dot\cup}\cdots
                                   \mathbin{\dot\cup}D_h             \tag{9}
\]

so that `|D_i|<=|S_* cap W_i|`.  Such a partition exists by (8).

For each nonempty `D_i`, apply the audited
[closed-shore rooted-connectivity lemma](hc7_closed_shore_rooted_connectivity.md)
to the component `W_i`, the separator `D`, and root set `D_i`.  The pair
`(G[W_i union D_i],D_i)` is internally `|D_i|`-connected.  The set form of
Menger's theorem therefore gives `|D_i|` disjoint paths from the distinct
roots in `D_i` to distinct vertices of `S_* cap W_i`.  Indeed, a smaller
linkage separator would define a rooted separation of order below
`|D_i|`.  Trim the paths at their first literal-core vertices.

Use those paths as bags rooted at `D_C`, and use the singleton bag `{s}`
for each `s in D_S`.  This gives seven disjoint connected `D`-rooted bags,
avoiding `Y`, which end at seven distinct vertices of the literal core.
Let `s_*` be the one unused core vertex.  Colour each member of `D` by the
shore of its representative.  The two colour classes have orders three
and four, and the colouring agrees with the literal shores on `D_S`.

This colouring is proper on `G[D]`.  Otherwise two rooted bags joined by an
edge of `G[D]` have representatives on the same shore.  Add `s_*` to a
rooted bag ending on the opposite shore, chosen away from the two chord
bags when necessary.  The other six representatives induce a `K_{3,3}`
and retain a same-shore chord.  Contracting a suitable cross-shore edge
gives a five-bag `K_5^-` model; the enlarged rooted bag is universal to
those five bags.  The connected set `Y` is a seventh bag adjacent to all
six through the roots in `D`.  The quotient has

\[
                              9+5+6=20               \tag{10}
\]

contacts, a `K_7^-` minor.  This contradiction proves item 1.

## 3. A prescribed-core-vertex cut dichotomy

The preceding construction has the following general companion, which is
useful when exact boundaries are compared.  Retain `Y,D` and put

\[
        Q=D\cap S,\qquad B=D-S,\qquad q=|Q|.
\]

Assume `B` is nonempty.  For `s in S-Q`, put

\[
        k=7-q=|B|,
        \qquad T_s=S-(Q\cup\{s\}).                   \tag{11}
\]

Exactly one of the following holds.

1. In `G-(Y union Q union {s})` there are `k` pairwise vertex-disjoint
   `B`--`T_s` paths saturating both end sets.
2. There is a `B`--`T_s` separator `W_s`, disjoint from `Y union Q union
   {s}`, of order `k-1` such that

   \[
                              Q\cup\{s\}\cup W_s     \tag{12}
   \]

   is an exact seven-cut.

To prove this, apply Menger's theorem after deleting `Y union Q union
{s}`.  A separator of order at most `k-1`, together with `Q union {s}`,
separates the nonempty set `Y` from a surviving vertex of `T_s` because
every path leaving `Y` first meets `B`.  Seven-connectivity makes every
bound an equality.  The linkage and separator alternatives are mutually
exclusive by Menger.

If both shores contain a choice `s_i in S_i-Q` and every such choice gives
the linkage outcome, then `G[D]` has a component disjoint from `Q` whose
two colour classes have nonzero odd difference in order.  Indeed, add the
trivial bags at `Q` to the linkages obtained by omitting `s_0` and `s_1`.
The argument in Section 2 gives two proper colourings of `G[D]`, agreeing
on `Q`, whose shore-zero class orders are respectively three and four.
Components meeting `Q` cannot flip.  The sum of the signed class
differences over the flipped `Q`-free components is one, so one summand is
nonzero and odd.

In particular, both omitted-shore choices exist whenever `G[D]` contains
an exterior edge.  If `Q` contained an entire literal shore, its four
vertices would fill the order-four colour class from Section 2; all three
remaining boundary vertices would have the other colour, contradicting
the exterior edge.

## 4. The two-helper completion

We now use the normal form (5).  Section 2 supplies seven disjoint
`D`-rooted bags avoiding `X`, with distinct literal-core representatives
and one unused core vertex.

### Lemma 4.1 (two-helper criterion)

Let `U,V subseteq X` be disjoint connected sets with an edge between them,
and suppose `a` has a neighbour in `U`.  If some `h_0 in H` satisfies

\[
 \begin{split}
 &|H-(N_D(U)\cup\{b,h_0\})|\\
 &\qquad +|H-(N_D(V)\cup\{h_0\})|\le1,              \tag{13}
 \end{split}
\]

then `G` contains a `K_7^-` minor.

#### Proof

Discard the rooted bags at `a` and `h_0`.  The five retained bags end at
five distinct core vertices.  Any five vertices of a literal `K_{4,4}`
root a `K_5` minor using the other three core vertices: if `ell` selected
vertices lie in `S_0`, add the `ell-1` unused vertices of `S_1` to distinct
`S_0`-rooted bags and the `4-ell` unused vertices of `S_0` to distinct
`S_1`-rooted bags.  Exactly one pure rooted bag remains on each shore, so
the five enlarged bags are pairwise adjacent.

The connected bag `U union {a}` meets the `b`-rooted bag through `ab` and
all other retained bags counted by the first term of (13).  The bag `V`
meets the bags counted by the second term, and the two helper bags are
adjacent.  Thus the seven bags have at least

\[
                              10+5+5+1-1=20          \tag{14}
\]

contacts.  \(\square\)

For a set `R subseteq X`, write

\[
                         \Delta_R=D-N_D(R).          \tag{15}
\]

If `R` is nonempty and proper, (2) says

\[
                         |\Delta_R|\le |N_X(R)|.     \tag{16}
\]

If equality holds, `R` is connected, and `a,b notin Delta_R`, then `R`
is a smaller tight blocker of `ab`, contrary to the choice of `X`.

## 5. A minimum nonsingleton blocker is three-connected

Suppose first that `|X|=2`.  Its two singleton sides have defect at most
one by (16).  Orient them as `U,V` so that `U` sees `a`.  Before deleting
`h_0`, each term in (13) has order at most one; choose `h_0` in their union
when it is nonempty.  Lemma 4.1 gives the target.

Suppose that `G[X]` has a cutvertex `x`, and let `A_1,...,A_t` be the
components of `X-x`.  For every `i`,

\[
             N_X(A_i)=\{x\},\qquad |\Delta_{A_i}|\le1.
\]

Minimality implies `Delta_{A_i} subseteq {a,b}`: a one-element defect
outside `{a,b}` would make `A_i` a smaller blocker.  Choose a lobe `A_i`
and split `X` into `A_i` and its connected complement.  Each side contains
a lobe, so each has defect contained in `{a,b}`.  Orient the split so that
the first side sees `a`.  After the `a,b` allowances in (13), at most one
residual `H`-defect remains on either side; choose `h_0` to erase one of
the at most two residual defects.  Equation (13) holds.

The only two-connected graph of order three is a triangle.  Choose
`p in P`, put `U={p}` and `V=X-p`.  Then

\[
 |Delta_U|\le2,\qquad |\Delta_V|\le1,
 \qquad |\Delta_U-\{a,b\}|\le1.                     \tag{17}
\]

The last inequality follows from blocker minimality if the first defect has
order two.  Again a suitable `h_0` removes one of the at most two remaining
defects, and Lemma 4.1 applies.

It remains to exclude a two-cut `{x,y}` in a two-connected graph `G[X]` of
order at least four.  Let `A_1,...,A_t` be the components of
`X-{x,y}`.  Two-connectivity makes every `A_i` adjacent to both `x,y`.
Put

\[
 \Delta_i=D-N_D(A_i),
 \qquad
 E_i=D-N_D\left(\{x,y\}\cup\bigcup_{j\ne i}A_j\right).             \tag{18}
\]

Then `|Delta_i|<=2`.  If equality holds, `Delta_i` meets `{a,b}`, by
minimality.  Moreover

\[
 E_i=\left(\bigcap_{j\ne i}\Delta_j\right)-N_D(\{x,y\}),           \tag{19}
\]

so `|E_i|<=2`; if equality holds, every `Delta_j`, `j ne i`, equals
`E_i`, and therefore `E_i` also meets `{a,b}`.

The two defects `Delta_i,E_i` are disjoint: a boundary resource missed by
both sides would have no neighbour in `X`, contrary to fullness at `D`.

Split `X` into

\[
 U=A_i,
 \qquad
 V=\{x,y\}\cup\bigcup_{j\ne i}A_j.                \tag{20}
\]

Both sets are connected and adjacent.  If only one side sees `a`, orient
it as `U`.  Its defect, after supplying `a` and `b`, has order at most one;
the other defect, after ignoring `a`, also has order at most one.  A choice
of `h_0` gives (13).

Suppose both sides see `a`.  First attach `a` to `A_i`.  Put

\[
                 R=\Delta_i-\{b\},\qquad T=E_i.
\]

Here `|R|<=1`, while `|T|<=2` and an order-two `T` has the form `{b,s}`.
Condition (13) can fail only when

\[
                       R=\{r\},\qquad T=\{b,s\},
                       \qquad r\ne s.                \tag{21}
\]

In that case the second side misses `b,s`.  Fullness of `X` at `D` makes
`A_i` see both, so `Delta_i={r}`.  Attach `a` to the second side instead.
The two remaining defects are `{s}` and `{r}`; deleting either one as
`h_0` leaves (13).  Thus every two-cut also gives the target.

We have proved that a target-free minimum blocker is a singleton or is
three-connected.

## 6. Multiple attachment and minimum degree four

Assume from now on that `G[X]` is three-connected.

First, every `k in K` has at least two neighbours in `X`.  If `k` had the
unique neighbour `z`, then `X-z` would be connected.  Its only internal
boundary resource is `z`.  Inequality (2) says that at most one member of
`D` is supported only at `z`.  Since `k` is one such member, both `a` and
`b` remain represented on `X-z`, and

\[
                         \lambda(X-z)=1+6=7.
\]

This is a smaller connected blocker, a contradiction.

Next choose `p` for (6).  If `P={p}`, then the inequality for `X-p` shows
that at most one boundary resource is supported only at `p`.  The resource
`a` is one, so `X-p` sees all of `H`.  If `|P|>=2`, choose `p in P` which
is not the unique neighbour of `b`, if such a unique neighbour belongs to
`P`.  The set `X-p` still sees `a`.  It cannot miss a member of `K`, since
then it would be a smaller tight blocker; by the choice of `p` it also sees
`b`.  Thus `X-p` is `H`-full in both cases.

Apply Lemma 4.1 with `U={p}` and `V=X-p`.  The second term of (13) is zero,
and the first term before deleting `h_0` has order

\[
                         5-|N_D(p)\cap K|.
\]

If `p` saw at least three members of `K`, a choice of `h_0` would make
(13) hold.  Target-freeness proves the second assertion in (6).

Finally suppose, for a contradiction, that some `x in X` has degree three
in `G[X]`.  Put

\[
 \alpha=\mathbf 1_{ax\in E(G)},\qquad
 \beta=\mathbf 1_{bx\in E(G)},\qquad
 k=|N_D(x)\cap K|.                                  \tag{22}
\]

Let `e_a,e_b` indicate that `x` is respectively the unique neighbour in
`X` of `a,b`, and let

\[
 e_K=|\{z\in K:N_X(z)=\{x\}\}|,
 \qquad e=e_a+e_b+e_K.                              \tag{23}
\]

The inequalities for `{x}` and `X-x` give

\[
                         \alpha+\beta+k\ge4,
                         \qquad e\le1.               \tag{24}
\]

If `alpha=1`, applying the two-helper exclusion to `{x},X-x` gives

\[
                         5-k+e_b+e_K\ge3.            \tag{25}
\]

If `e_a=0`, applying it in the reverse orientation to `X-x,{x}` gives

\[
                         e_K+6-\beta-k\ge3.          \tag{26}
\]

There are three cases.

- If `alpha=0`, (24) and (26) give `e_K>=1`.  Hence (24) forces
  `e_a=e_b=0` and `e=1`.  The connected set `X-x` sees `a,b` and has
  boundary order seven, contradicting minimality.
- If `alpha=beta=1`, the singleton `{x}` sees `a,b`; minimality and (24)
  give `k>=3`.  Equation (25) gives `e_b+e_K>=1`, so `e_a=0`.  If
  `e_b=0`, then `X-x` is again a smaller blocker.  If `e_b=1`, (24) gives
  `e_K=0`, while (26) gives `k<=2`, a contradiction.
- If `alpha=1` and `beta=0`, (24)--(25) give `k>=3` and `e_K>=1`.
  Therefore `e_a=e_b=0` and `e=1`, so `X-x` is again a smaller blocker.

All cases are impossible, proving (4).

## 7. Three-cut component capacity

Let `T` be a three-cut of `G[X]`, and let `W_1,...,W_s` be the components
of `X-T`.  Three-connectivity makes every `W_i` adjacent to all three
members of `T`.  Put

\[
 K_i=N_D(W_i)\cap K,
 \qquad
 e_i=|\{k\in K:N_X(k)\subseteq W_i\}|.              \tag{27}
\]

The boundary inequality for `W_i`, strengthened by blocker minimality when
`W_i` sees both `a,b`, gives

\[
                              |K_i|\ge3.              \tag{28}
\]

Indeed, a component seeing neither of `a,b` needs at least four members of
`K`; one seeing exactly one needs at least three; and one seeing both needs
at least three because boundary order seven is forbidden.

The complement `X-W_i` is connected: it contains `T` and another component,
which is adjacent to every member of `T`.  Consider the spanning connected
bipartition `W_i, X-W_i`.  Orient it with a side seeing `a` first; when both
sides see `a`, choose the orientation for which the exceptional indicator
below is zero.  Let `c_i` be the number of resources in `K` which meet both
sides.  In the notation of Lemma 4.1, the defect sum before choosing `h_0`
is

\[
            5-c_i+\mathbf 1_{\{b\text{ has neighbours only on the
                                      side seeing }a\}}.           \tag{29}
\]

Target-freeness therefore gives `c_i<=2`, except that `c_i<=3` when the
displayed exceptional indicator is unavoidable.  This happens exactly when
only one side sees `a` and every neighbour of `b` in `X` lies on that same
side.

Since

\[
                              c_i=|K_i|-e_i,          \tag{30}
\]

an equality `e_i=0` is possible only when every neighbour in `X` of both
`a` and `b` lies in `W_i`, and `|K_i|=3`.  Indeed, if the forced side in the
exceptional orientation were `X-W_i`, then `W_i` would miss both `a,b`, so
`|K_i|>=4` and `c_i>=4`, contradicting even the exceptional bound.  Thus the
forced side is `W_i`; every other orientation has no exceptional allowance
in (29).  There is at most one such component.

Suppose `s>=4` and put `E=sum_i e_i`.  If the exceptional component exists,
then `E>=s-1`, so at most `5-E<=2` resources of `K` are nonexclusive; but
the exceptional component needs three such resources by (30), a
contradiction.  Hence every `e_i>=1`, so `E>=s` and at most one resource is
nonexclusive.  Equation (28) then forces `e_i>=2` for every `i`, giving
`E>=2s>5`.  This is impossible and proves `s<=3`.

Finally let `s=3`.  First suppose there is no exceptional component.  Then
every `e_i>=1`.  If `t=5-E` is the number of nonexclusive `K`-resources,
then (28) gives

\[
                         e_i+t\ge3\quad(i=1,2,3).
\]

Thus `E>=9-3t`, while `E=5-t`.  It follows that `t>=2`; the reverse
inequality follows from `E>=3`.  Hence `t=2`, `E=3`, every `e_i=1`, and
both nonexclusive resources meet every component.  This is precisely the
first profile in item 4.

If an exceptional component exists, index it as `W_1`.  Then `e_1=0` and
its three `K`-contacts are nonexclusive, so `t>=3`.  On the other hand
`e_2,e_3>=1`, whence `E>=2` and `t<=3`.  Therefore

\[
                         t=3,\qquad E=2,
                         \qquad e_2=e_3=1.            \tag{31}
\]

The component `W_1` meets exactly the three non-component-exclusive
resources and contains every neighbour in `X` of both `a` and `b`.  Each
other component contains every `X`-neighbour of its one exclusive resource
and, by (28), meets at least two of the three non-component-exclusive
resources.  This is the second profile and completes
Theorem 1.1.  \(\square\)

## 8. Finite falsification and exact remaining lemma

A targeted symbolic screen, separate from the proof, imposes exactly the
relative inequalities (2), blocker minimality, boundary fullness, and the
negation of Lemma 4.1 for every connected spanning bipartition of a
three-connected `X`.  It finds no survivor for any three-connected graph
of order four through seven: the unlabelled host counts are

\[
                         1,\ 3,\ 17,\ 136.            \tag{32}
\]

The screen is bounded evidence without an independently checkable UNSAT
certificate.  No unbounded conclusion in this file depends on it.

The exact nonsingleton residue is now the following boundary-bisection
problem.

> **Minimum-degree-four boundary-bisection lemma (open).**  Under the
> hypotheses of items 2--4, prove that a nonsingleton minimum blocker has
> disjoint adjacent connected sets `U,V` satisfying (13).

By Sections 5--7, a counterexample to this lemma must be three-connected,
have minimum degree at least four, have every `K`-resource attached at least
twice, and contain the vertex `p` in (6).  Lemma 4.1 would immediately turn
a positive bisection into a `K_7^-` model.  The separate singleton-blocker
outcome (3) remains the adjacent degree-seven pair from the preceding
audited theorem.

This is a strict reduction of the complete tight-witness system, not a
counterexample to the weighted splitter theorem or to T44.
