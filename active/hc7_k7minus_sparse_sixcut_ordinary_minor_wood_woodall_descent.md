# Ordinary near-five minors and the Wood--Woodall descent

**Status:** proved unbounded structural fork; independently audited.  An
ordinary `K_5^-` minor is reduced either to a legal exact-six fragment or to
a low-visibility bag with strictly surplus internal portals.  In the
ordinary-minor-free branch, every three-connected lobe is either separated
by an exact-six singleton or has order at most `31` and excess at most `62`.
Small-separator leaves are bounded by the four-root carrier capacity.  These
results do not prove the desired sharp bound `eta<=5`.

## 1. Setup

Let `G` be a six-connected graph with no `K_7^-` minor.  Let `S` be a cut of
order six such that `G-S` has at least three components, and fix one component
`C`.  Every component of `G-S` is adjacent to every vertex of `S`.

For a nonempty connected set `X subseteq C`, put

```text
T(X)=N_{G[C]}(X),       R(X)=N_G(X) intersect S,
t(X)=|T(X)|,            r(X)=|R(X)|.                 (1)
```

Thus `N_G(X)=T(X) union R(X)`.  The coefficient-four excess is

```text
eta_S(C)=|E(G[C])|+|E_G(C,S)|-4|C|.                 (2)
```

We use two previously audited consequences of the other two full
components:

* a punctured `S`-rooted `K_5^-` model in the closed `C`-shore is terminal;
* for every four-set `Z subseteq S`, at most two pairwise disjoint connected
  subgraphs of `C` are adjacent to every vertex of `Z`.  Consequently,

```text
sum_{v in C} binom(|N_S(v)|,4)<=30.                  (3)
```

## 2. The ordinary-minor fork

### Lemma 2.1 (spanning normalisation)

Every ordinary `K_5^-` model in `G[C]` can be enlarged to a model whose five
branch bags partition `C`.

### Proof

For every component `K` of the vertices outside the five old bags,
connectedness of `C` gives an edge from `K` to at least one old bag.  Absorb
all of `K` into one such bag.  The enlarged bag is connected, the five bags
remain disjoint, and no old quotient adjacency is lost.  Doing this for every
component gives the asserted partition. `\square`

### Theorem 2.2 (low visibility gives the exact portal alternative)

Suppose that `G[C]` has an ordinary `K_5^-` minor.  There is a spanning model
with a branch bag `B` for which

```text
r=|N_G(B) intersect S|<=2.                           (4)
```

Put

```text
P=N_{G[C]}(B).                                       (5)
```

Then exactly one of the following numerical rows holds.

1. `|P|=6-r`, and `P union (N_G(B) intersect S)` is an exact six-separator
   with open side `B`.
2. `|P|>=7-r`; all these portal vertices lie in the other four branch bags.

### Proof

Apply Lemma 2.1 and then the audited balanced two-pole composition theorem.
If every branch bag met at least three boundary vertices, a three--three
partition of `S`, together with two other full components, would complete
the five bags to a `K_7^-` model.  Hence (4) holds.

The bag `B` is connected and proper because the other four branch bags are
nonempty.  Six-connectivity applied to the singleton shore `B` gives

```text
|P|+r=|N_G(B)|>=6.                                   (6)
```

If equality holds, (5) and the fact that `C` is a component of `G-S` show
that the displayed union is the full external neighbourhood of `B`, so it
is an exact six-separator.  Otherwise integrality gives `|P|>=7-r`.  The
spanning partition puts every member of `P` in one of the other four bags.
`\square`

### Corollary 2.3 (the equality row is a legal hereditary descent)

In row 1, let

```text
U=P union (N_G(B) intersect S).
```

After completing `S` to a clique, `B` is a component behind the exact
six-cut `U`, remote from the nonempty set `S-U`.  Punctured-rooted-model
exclusion therefore reroots to `(G[B union U],U)`, and

```text
eta_S(C)=eta_U(B)+eta_S(C-B).                        (7)
```

### Proof

Completing `S` adds no edge incident with `B`, so its full neighbourhood
remains `U`.  Since (4) leaves at least four vertices of `S` outside `U`, the
fragment has the orientation required by the audited exact-six rerooting
theorem.  Its hereditary-exclusion corollary and exact edge partition give
the two assertions. `\square`

The strict row is the exact obstruction to this argument.  It gives at least
five internal portals when `r=2`, at least six when `r=1`, and at least seven
when `r=0`, but it does not place them in distinct branch bags.  Several
portals may be concentrated in a single one of the four other bags.

There is a complementary audited contraction normalisation when `S` is
stable.  A literal five-vertex `K_5^-` roots at arbitrary shore order by five
disjoint boundary-to-core paths.  A minimum counterexample using a genuinely
nonliteral ordinary model has order at least seven, and every edge internal
to a chosen branch bag is blocked by an exact six-fragment containing both
ends on its boundary.  Thus a nonsingleton low-visibility bag already returns
an exact fragment governed by the same rerooting and additivity mechanism as
Corollary 2.3.  The unresolved stable row is the two-copy packet-transfer
problem across those exact fragments.

## 3. What every small internal separator returns

### Lemma 3.1 (relative-six separator fork)

Let `X` be a nonempty proper connected subset of `C` with `t(X)<=2`.  Then

```text
t(X)+r(X)>=6.                                        (8)
```

If equality holds, `N_G(X)` is an exact six-separator.  If equality does not
hold, then

```text
r(X)>=7-t(X).                                        (9)
```

In particular, a strict two-separator shore sees at least five roots, and a
strict cutvertex shore is adjacent to all six roots.

### Proof

The other components of `G-S` give a nonempty far side after `N_G(X)` is
deleted.  Thus `N_G(X)` is a genuine cut, and six-connectivity gives (8).
Equality is exactly the first assertion because (1) is the full external
neighbourhood.  Otherwise its order is at least seven, which is (9).
`\square`

### Lemma 3.2 (at most six disjoint strict two-shores)

Let `X_1,...,X_q` be pairwise disjoint connected proper subsets of `C`, each
with `t(X_i)<=2`, and suppose none gives equality in (8).  Then

```text
sum_i binom(r(X_i),4)<=30,       and hence q<=6.      (10)
```

### Proof

For every four-set `Z subseteq S`, the members `X_i` with
`Z subseteq R(X_i)` are pairwise disjoint `Z`-carriers.  There are at most
two of them by the audited carrier theorem.  Sum this bound over the fifteen
choices of `Z`.  This gives the first inequality in (10).  Lemma 3.1 gives
`r(X_i)>=5`, so every summand is at least five and `q<=6`. `\square`

### Corollary 3.3 (the cutvertex branch closes)

If `C` has a cutvertex, then at least one of the following holds:

1. a leaf-block shore gives an exact six-fragment;
2. `C` contains two disjoint `S`-full packets.

Consequently, in the packet-one regime with no nested exact-six fragment,
`C` is a single block; if `|C|>=3`, it is two-connected.

### Proof

The block--cutvertex tree has two leaf blocks.  From each, delete its unique
attachment cutvertex and call the remaining connected set `X_i`.  The two
sets are disjoint and satisfy `T(X_i)` equal to that one cutvertex.  If neither
shore is exact, Lemma 3.1 says `r(X_i)=6`.  They are then two disjoint
`S`-full packets. `\square`

Lemma 3.2 also bounds by six every family of pairwise disjoint open shores
whose external internal neighbourhoods are the two-vertex adhesions of a
two-separation decomposition.  It does not by itself bound a nested chain of
two-separations; that chain is the remaining decomposition obstruction.

## 4. The three-connected ordinary-minor-free core

### Theorem 4.1 (exact singleton or bounded exceptional core)

Suppose that `G[C]` is three-connected and has no ordinary `K_5^-` minor.
Then either a singleton of `C` lies behind an exact six-separator, or

```text
|C|<=31,                  eta_S(C)<=62.              (11)
```

If `G[C]` is the triangular prism or `K_{3,3}`, the second bound improves to

```text
eta_S(C)<=15.                                         (12)
```

### Proof

Wood and Woodall's Lemma 4.2.1 says that a three-connected
`K_5^-`-minor-free graph is a wheel, the triangular prism, or `K_{3,3}`.

First let `C` be a wheel with rim length `m` and hub `h`.  Every rim vertex
has three neighbours in `C`.  Relative six-connectivity gives it at least
three neighbours in `S`.  If it has exactly three, its full neighbourhood
has order six and gives the exact singleton fragment.  Otherwise every rim
vertex `v` has

```text
a(v)=|N_S(v)|>=4.
```

Equation (3) then gives `m<=30`, and hence `|C|=m+1<=31`.  For
`a in {4,5,6}`,

```text
a-2 <= 2 binom(a,4).
```

Since a wheel has `2m` internal edges,

```text
eta_S(C)
 =a(h)+sum_(v on rim)(a(v)-2)-4
 <=6+2(30)-4=62.                                    (13)
```

Now let `C` be the triangular prism or `K_{3,3}`.  Both have six vertices,
nine edges, and internal degree three at every vertex.  Again, a vertex with
exactly three boundary neighbours gives an exact singleton fragment; in the
remaining row every `a(v)>=4`.  For `a in {4,5,6}`,

```text
a-4 <= (binom(a,4)-1)/4.
```

Using (3) over the six vertices gives

```text
sum_v(a(v)-4) <= (30-6)/4=6,
sum_v a(v)<=30.
```

Therefore

```text
eta_S(C)=9+sum_v a(v)-24<=15.                        (14)
```

This proves (11)--(12). `\square`

The theorem is an unbounded reduction: no arbitrarily large
three-connected ordinary-minor-free core survives without returning an
exact six-fragment.

### Corollary 4.2 (a terminal three-connected two-shore is bounded)

Suppose that `C` is two-connected and ordinary-`K_5^-`-minor-free.  Let `X`
be a connected set with

```text
N_{G[C]}(X)={u,v},
```

and suppose that `C-(X union {u,v})` is nonempty and

```text
J=G[C][X union {u,v}]+uv
```

is three-connected.  Then either a vertex of `X` gives an exact singleton
fragment, or `|X|<=31`.

### Proof

Two-connectivity makes every component of `C-{u,v}` adjacent to both `u`
and `v`.  The nonempty far side therefore contains a `u`--`v` path whose
internal vertices avoid `X`.  Contracting that path to the edge `uv` and
deleting the rest shows that `J` is a minor of `C`; hence `J` has no
`K_5^-` minor.

Apply Wood--Woodall to `J`.  In a wheel, every rim vertex belonging to the
open side `X` has the same three internal neighbours in `C` as in `J`; unless
it gives an exact singleton, it has at least four boundary neighbours.  At
most thirty such vertices exist by (3), and at most one further vertex of
`X` is the hub.  Thus `|X|<=31`.  In the prism and `K_{3,3}` rows,
`|X|<=|V(J)|-2=4`. `\square`

Together with Lemma 3.2, this bounds both the number and size of disjoint
terminal three-connected leaf shores.  A nested chain can still reuse its
two-vertex adhesions and is not bounded by this counting argument.

## 5. Additivity does not imply strict excess descent

The exact equality (7) cannot be strengthened to `eta_U(B)<eta_S(C)` from
relative connectivity alone.  Here is a sharp arithmetic guardrail.

Let `S={s_1,...,s_6}` be stable and let `C=K_6`, partitioned into a four-set
`L` and a two-set `T`.  Join every vertex of `L` to
`s_1,s_2,s_5,s_6`, and every vertex of `T` to `s_3,s_4`.  The pair is
relatively six-connected: a set contained in `L` sees four roots and all
outside clique vertices, a set contained in `T` sees two roots and all
outside clique vertices, and a set meeting both parts sees all six roots.

The set

```text
U=T union {s_1,s_2,s_5,s_6}
```

is an exact six-separator for `L`, but direct counting gives

```text
eta_S(C)=15+20-24=11,
eta_U(L)=6+24-16=14,
eta_S(T)=1+4-8=-3.                                  (15)
```

Thus `11=14+(-3)`: the smaller exact fragment has larger excess.  This local
pair can be embedded in a genuinely six-connected three-lobe host: take a
second component `A=K_6` complete to `S` and a singleton component complete
to `S`.  Deleting at most five vertices leaves a vertex of `S`, a vertex of
`A`, and a surviving attachment from `C` to `S`; the last assertion follows
because the attachment graph is the disjoint union of `K_{4,4}` and
`K_{2,2}`.  Separating its two sides requires a vertex cover of order at least
`4+2=6`.  The construction is deliberately target-rich, so it does not
refute a target-sensitive induction.  It does refute every proposed
strict-drop argument using only six-connectivity, side minimisation, and
additivity.

## 6. Exact remaining barrier

This branch does not establish `eta<=5`.  Within this route, the unresolved
mechanisms are:

* the strict row of Theorem 2.2, where a low-visibility ordinary-model bag
  has surplus portals concentrated in up to four other bags;
* a nested chain of strict two-separation shores, each seeing at least five
  original roots; and
* bounded wheel, prism and `K_{3,3}` incidence instances.  The present
  inequalities allow excess up to `62`, even though punctured-rooted-model
  exclusion may remove all high-excess instances.

Any closure must use that target-sensitive exclusion (or transfer two
derived-boundary packets).  Neither Wood--Woodall structure nor exact
additivity alone supplies the missing sharp bound.

## Pinned dependencies and primary source

* balanced two-pole gate: source SHA-256
  `9a7a6923764094b588319ed9e683091ce3a6b27fe0cd32b4f871d4a4a83d098d`,
  GREEN audit SHA-256
  `c6b5777570f623610e9a4f703851950a49c6ced5247baf56d72e2ba74f336d96`;
* four-root carrier packing: source SHA-256
  `adfcc70aca8543e15bcf7e94e1fb310492535f8155f02cb5a5430adba4ce8372`,
  GREEN audit SHA-256
  `4a185697d20ed73c358703eb7d433c3555bca6474497a011630d3805dc493e97`;
* exact-six rerooting and additivity: source SHA-256
  `53c91cee74ae8b1f5251e13c14095f8abc65f05625eedb401d3d53173996da15`,
  GREEN audit SHA-256
  `c30aa69b6919edd2cfba80d6df1f02e2c75d38d9544bd87e4332ba4d823526a3`;
* stable-boundary ordinary-model contraction gate: source SHA-256
  `0e078226085a494413fac157ca4de6cc4ebcb0fb5eb855a2f8738d141b59776a`,
  GREEN audit SHA-256
  `237cecba16fe7fa03b382892b3e2289dd338a4b975d32cfd7e19451fadb5c386`.

The only external structural input is R. G. Wood and D. R. Woodall,
*Defective Choosability of Graphs without Small Minors*, Electronic Journal
of Combinatorics **16** (2009), R92, Lemma 4.2.1,
[DOI 10.37236/181](https://doi.org/10.37236/181).  The published statement
was checked directly: the only three-connected `(K_5-e)`-minor-free graphs
are wheels, the triangular prism, and `K_{3,3}`.
