# Seven-edge five-cut reduction

**Status:** written computation-free unbounded reduction; separate internal
audit.  The result eliminates three complement types and reduces the last
one to an exact rooted-support obstruction.  It does not eliminate every
seven-edge five-cut or prove `(E5)`.

Let `G` be a minimum `E5` enemy and put

```text
q=|E(G)|-(4|V(G)|-7).
```

Let `S` be a cut of order five such that `G-S` has exactly two components
`C,D` and `|E(G[S])|=7`.  For a component `L` behind a five-cut `Q`, write

```text
delta_Q(L)=|E(G[L])|+|E_G(L,Q)|-4|L|.
```

Assume that

```text
delta_S(C)>=q+4                                      (1)
```

and that `C` has minimum order among all components behind order-five cuts
satisfying the same inequality.  The complement of `G[S]` has three
edges, and hence is one of

```text
K_{1,3},       K_3,       P_4,       P_3 disjoint union K_2.
```

## Theorem 1 (the star and triangle types are impossible)

The complement of `G[S]` is neither `K_{1,3}` nor `K_3`.

### Proof

If the complement is a three-edge star, the full connected component `D`
contains a connected subgraph meeting its centre and all three leaves.
Absorbing this subgraph into the centre realises all three missing boundary
edges.  Thus the graph obtained from `G[C union S]` by completing `S` to a
clique is a proper minor of `G`.  It is five-connected and has

```text
4|C|+delta_S(C)+10 >= 4(|C|+5)-7
```

edges.  It would be a smaller `E5` enemy, a contradiction.

Suppose instead that the three missing edges form a triangle on
`a,b,c`; call the other boundary vertices `d,e`.  Put

```text
H=G[C union S]+E(K_5[S]).
```

The graph `H` is five-connected.  For any edge of the added triangle,
the other two added edges form a star and can be realised through `D`.
Consequently deleting any edge of that triangle from `H` gives an actual
proper minor of `G` at the `E5` density threshold.  Such a graph cannot be
five-connected, so all three edges of the added triangle are critical for
five-connectivity in `H`.

Mader's critical-cycle theorem gives a vertex, say `a`, of that triangle
with `d_H(a)=5`.  Four neighbours lie in the completed boundary and
fullness supplies a neighbour in `C`; hence `a` has a unique neighbour
`p` in `C`.

Put

```text
R=C-{p},             Q={p,b,c,d,e}.
```

The set `R` is nonempty, since a singleton `C` has excess at most one.
Every component of `G[R]` has neighbourhood exactly `Q`, and all remaining
vertices lie in one component containing `D` and `a`.  The graph `G[R]`
is connected: two of its components would give a three-component cut whose
boundary contains the triangle `bde`; three and four components give the
already eliminated four- and five-component cases; at least five give an
explicit `K_7^-` quotient using six full components.

Let `k=|E(G[Q])|`.  A complete boundary gives the target immediately and
a `K_5^-` boundary has already been eliminated, so `k<=8`.  Deleting `a`
from the old closed side removes its two original boundary edges and its
edge to `p`.  Therefore

```text
delta_Q(R)=delta_S(C)+8-k >= delta_S(C)>=q+4.
```

This contradicts the minimum order of `C`.  \(\square\)

## Theorem 2 (the four-edge path type is impossible)

The complement of `G[S]` is not the path

```text
a-b-c-d
```

with fifth vertex `t`.

### Proof

Add the missing edges `ab,bc` to `G[C union S]`.  They form a star and are
simultaneously realised through `D`.  The resulting proper minor is at the
`E5` threshold, but is not five-connected.  Its boundary is
`K_5-cd`; the same separator argument as in the eight-edge descent gives
a vertex `p in C` such that every `c`--`d` path through `C` contains `p`.
Adding `bc,cd` instead gives `q' in C` meeting every `a`--`b` path.

The vertices `p,q'` are distinct.  Indeed, apply the Two Paths Theorem in
`G[C union S]-t` to the cyclically ordered roots `a,c,b,d`.  In the disc
outcome, writing `p_t=|E_G({t},C)|`, planarity gives

```text
4|C|+delta_S(C)-p_t+3 <= 3(|C|+4)-6,
```

and hence `delta_S(C)<=3`, contrary to (1).  Thus `C` contains disjoint
`a`--`b` and `c`--`d` paths, on which `q'` and `p` respectively lie.

Every component of `C-p` is adjacent to `a,b,t,p` and exactly one of
`c,d`.  Since `q'` meets every `a`--`b` path, `C-p` is connected.
Similarly `C-q'` is connected.  Let `u` be the member of `{c,d}` met by
`C-p`, let `v` be the other member, let `r` be the member of `{a,b}` met
by `C-q'`, and let `s` be the other member.  Then

```text
N_C(v)={p},             N_C(s)={q'}.
```

Put

```text
R=C-{p,q'},             Q={p,q',u,r,t}.
```

The set `R` is nonempty: a component `C` of order two has at most one
internal edge and at most ten boundary edges, and hence excess at most
three, contrary to (1).

Every component of `G[R]` is full to `Q`, and all other vertices lie in
one component containing `D,v,s`.

If `ur` is an edge, then `G[Q]` contains the triangle `urt`, so the known
component-count reductions make `R` connected.  Deleting `v,s` removes
six edges from the old closed side, and therefore

```text
delta_Q(R)=delta_S(C)+9-|E(G[Q])|
              >=delta_S(C)+1.
```

This is a strict high-excess descent, a contradiction.  Hence the only
orientation which can survive has `u=c` and `r=b`, so `ur` is the middle
missing edge.

If `q>0`, every edge of `G` is critical for five-connectivity: deleting an
edge otherwise gives a same-order smaller `E5` enemy.  The literal triangle
`adt` therefore contains a degree-five vertex by Mader's theorem.  The
vertex `t` has four boundary neighbours and neighbours in both `C,D`, so
that vertex is `a` or `d`.  It has exactly one neighbour in `C`.
Let that neighbour be `h`, replace the degree-five boundary vertex by `h`,
and take `C-{h}` as the new inside.  Every component of this inside is
full to the new boundary, while the other vertices form one outside
component.  The new boundary contains a triangle, so the component-count
theorems make the inside connected.  Its boundary has at most seven edges:
eight edges would retain the adjacent missing pair `ab,bc` or `bc,cd`,
contrary to the eight-edge theorem.  Exact edge accounting then gives the
new component excess at least `delta_S(C)`, contradicting the minimum
order of `C`.  Thus `q=0`.

In the surviving orientation, if `R` were connected then deleting `a,d`
would give

```text
delta_Q(R)=delta_S(C)+8-|E(G[Q])|>=delta_S(C),
```

again contradicting minimality.  Hence `R` is disconnected.  The
component-count reductions force it to have exactly two components
`R_1,R_2`, and the three-component theorem makes `G[Q]` triangle-free.
Thus `|E(G[Q])|<=6`.  Each `R_i` is smaller than `C`, so its excess is at
most three.  Exact accounting gives

```text
delta_Q(R_1)+delta_Q(R_2)
  =delta_S(C)+8-|E(G[Q])|>=6.
```

Equality is forced throughout.  Hence both excesses are three,
`delta_S(C)=4`, and `|E(G[Q])|=6`.  Equality in Mantel's theorem gives
`G[Q]=K_{2,3}`.  Finally the global excess identity at `Q` gives
`delta_Q(O)=1`.  This is precisely the separately eliminated
`K_{2,3}` three-component equality row, a contradiction.  \(\square\)

## Theorem 3 (the disjoint star-and-edge type)

Suppose that the missing boundary edges are

```text
ab, ac, de.
```

Then there is a vertex `p in C` such that `C-p` has exactly two components
`A,B`, where

```text
N_G(A)={p,a,b,c,d},        N_G(B)={p,a,b,c,e}.          (2)
```

Put

```text
Q_d={p,a,b,c,d},       Q_e={p,a,b,c,e},
alpha=delta_{Q_d}(A),  beta=delta_{Q_e}(B).
```

Then

```text
alpha,beta<=q+3,
alpha+beta=delta_S(C)+4-d_S(p),                         (3)
|E(G[Q_d])|,|E(G[Q_e])|<=7.                            (4)
```

In fact `q=0`, the vertex `p` is adjacent to at most one of `d,e`, and

```text
4<=delta_S(C)<=5,        delta_S(D)=6-delta_S(C),
alpha,beta<=3.                                             (5)
```

More precisely, the remaining numerical rows are

```text
delta_S(C)=5:  d_S(p)=3 and (alpha,beta)=(3,3);
delta_S(C)=4:  d_S(p)=2 and (alpha,beta)=(3,3),
               or d_S(p)=3 and {alpha,beta}={2,3}.        (6)
```

Moreover, there do not exist vertex-disjoint connected subgraphs `T,P` of
`G[D]` such that

```text
{a,b,c} subseteq N_G(T),       {d,e} subseteq N_G(P).       (7)
```

### Proof

Adding `ab,ac` through `D` gives a proper minor at the `E5` threshold with
boundary `K_5-de`.  It is not five-connected.  Its separator has the exact
form

```text
{a,b,c,p}
```

for some `p in C`, and separates `d` from `e`.  Every component of `C-p`
has one of the two neighbourhoods in (2).  There is exactly one of each
type.  To see first that both types occur, suppose for example that no
component meets `e`.  Then `p` is the unique neighbour of `e` in `C`.
Replace `e` in the old boundary by `p` and take `C-{p}` as the new inside.
The new boundary contains the triangle `bcd`, so the component-count
theorems make this inside connected.  It has at most seven boundary edges,
because eight would retain the adjacent missing pair `ab,ac`.  Deleting
`e` from the old closed side removes its three boundary edges and its edge
to `p`; exact accounting therefore gives new excess at least
`delta_S(C)`, contradicting the minimum order of `C`.  The argument with
`d` and the triangle `bce` is symmetric.  Finally, two components of
either type would give a three-component five-cut whose boundary contains
`bcd` or `bce`; larger numbers are excluded by the four- and
five-component theorems or by the six-component `K_7^-` quotient.

Both `A` and `B` are smaller than `C`, so their excesses are at most
`q+3`.  Decomposing all internal and boundary edges of `C` across
`A,p,B` gives (3).  The four old boundary vertices in `Q_d` induce
`K_4-{ab,ac}`, so

```text
|E(G[Q_d])|=4+|N_G(p) intersect {a,b,c,d}|.
```

Eight edges would leave the two adjacent missing edges `ab,ac`, contrary
to the eight-edge theorem.  This proves (4), and the same argument applies
to `Q_e`.  In particular `d_S(p)<=4`.

We next prove that `q=0`.  If `q>0`, deletion of every edge destroys
five-connectivity, since otherwise it gives a same-order smaller `E5`
enemy.  The boundary contains the triangle `bcd`.  Both `b` and `c` have
a neighbour in each of `A,B`, as well as three boundary neighbours and a
neighbour in `D`, so they have degree at least six.  Mader's
critical-cycle theorem therefore makes `d` a degree-five vertex.  It has
three boundary neighbours and neighbours in both `C,D`; hence it has a
unique neighbour `h` in `C`.  Replace `d` in the boundary by `h` and take
`C-{h}` as the new inside.  The new boundary contains the triangle `bce`,
so the component-count theorems make the inside connected.  It has at most
seven edges, because eight would retain the adjacent missing pair
`ab,ac`.  Deleting `d` from the old closed side removes its three boundary
edges and its edge to `h`, so exact accounting gives new excess at least
`delta_S(C)`.  This contradicts the minimum order of `C`.  Thus `q=0`.

If `p` were adjacent to both `d,e`, the seven connected branch sets

```text
A union {a},  {p,d},  {b},  {c},  {e},  B,  D
```

would be pairwise adjacent except possibly for `B,D`, and would form a
`K_7^-` model.  Hence `p` meets at most one of `d,e`.  The two bounds in
(4) then give `d_S(p)<=3`.  Now (3), minimality, and the global identity

```text
delta_S(C)+delta_S(D)=6
```

give (5).  Since `alpha+beta<=6`, equation (3) also gives
`d_S(p)>=delta_S(C)-2`; the alternatives in (6) follow.

Finally suppose that `T,P` as in (7) exist.  Absorb `T` into the branch set
rooted at `a`; its contacts with `b,c` realise the missing edges `ab,ac`,
while the literal edge `bc` supplies the third adjacency.  In a minimal
subtree of `P` joining a neighbour of `d` to a neighbour of `e`, split one
edge to obtain adjacent branch sets rooted at `d,e`; if that subtree is a
single vertex, absorb it into either root bag and retain the other root as
a singleton.  The two constructions are disjoint, so they complete `S` to
a `K_5` model through `D`.  After
contraction, the completed closed side at `C` is an actual proper minor of
`G`.  It is five-connected and has at least

```text
4|C|+delta_S(C)+10 >= 4(|C|+5)-7
```

edges, contradicting the choice of `G`.  Thus the rooted instance is
infeasible.  \(\square\)

## Exact remaining obligation

The path-complement row reduces to, and is closed by, the independently
proved `K_{2,3}` equality-cut elimination.  The sole survivor among the
seven-edge boundary complements is the exact `q=0` configuration of
Theorem 3, including the absence of the star-and-path support (7).

Condition (7) is stronger than ordinary two--three linkage.  A connected
subgraph through `a,b,c` need not contain one connected interior part
adjacent to all three roots: in a minimal rooted tree, `b` or `c` may lie
between the other two terminals.  Xie's general two--three-linkage
characterisation therefore does not directly supply (7), and in any event
retains reducible, planar, apex, and order-four-separation outcomes.  The
theorem that every six-connected graph is two--three linked also does not
apply to this five-cut side.  A single interior vertex adjacent to all five
roots already shows that boundary fullness alone need not provide two
disjoint supports as in (7).

This is not a routine strengthening hidden in the cited theorem: the
closely related demand that the three-root subgraph contain an interior
tripod is recorded as property (P1) in Xie's Conjecture 7.0.2, even under
six-connectivity and a non-apex hypothesis.

Therefore the first unsupported inference is:

> the low-excess opposite component `D` must supply the star-and-path
> support (7).

Neither five-connectivity nor the present excess bounds prove it.  To close
the row, the planar or separation outcome of the rooted obstruction must
be coupled to the high-excess component `C` so as to produce an explicit
`K_7^-` model or another strict high-excess descent.

## External inputs

- Wolfgang Mader, *Ecken vom Grad n in minimalen n-fach
  zusammenhängenden Graphen*, Archiv der Mathematik 23 (1972), 219--224,
  Theorem 1.
- Neil Robertson, Paul Seymour, and Robin Thomas, the Two Paths Theorem in
  the four-terminal disc form used by Norin and Totschnig.
- Shijie Xie, *6-connected graphs are two-three linked*, PhD dissertation,
  Georgia Institute of Technology (2019), Theorem 7.0.1, Conjecture 7.0.2,
  and the principal six-connectivity theorem,
  <http://hdl.handle.net/1853/62273>.

## Internal dependency

- [Elimination of the `K_{2,3}` three-component equality
  row](hc7_k7minus_e5_k23_331_elimination.md), written computation-free
  unbounded theorem with separate internal audit.
