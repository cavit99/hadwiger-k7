# Singleton-contraction uncrossing in the exact three-component residue

**Status:** written computation-free unbounded reduction; separate internal
audit.  This note verifies the singleton-contraction cut family and reduces
its no-descent outcome to one boundary graph with at least three prescribed
degree-five roots.  It does not prove `(E5)`.

Write `K_7^-` for `K_7` with one edge deleted.  Let `G` be a minimum
`E5` enemy, chosen first with minimum order and then with minimum size.  The
existing reductions give

```text
|E(G)|=4|V(G)|-7,                    kappa(G)=5.
```

For a component `D` behind a five-cut `Q`, put

```text
delta_Q(D)=|E(G[D])|+|E_G(D,Q)|-4|D|.
```

Choose a pair `(S,A)` with `S` a five-cut, `A` a component of `G-S`,
`delta_S(A)>=4`, and `|A|` minimum over all such pairs.  This note treats
the exact surviving three-component case

```text
components of G-S: A, {x}, {y};
N_G(x)=N_G(y)=S;                    xy notin E(G).
```

Put

```text
H=G[A union S],                    J=G[S],
a=|A|.
```

The three-component concentration theorem makes `J` triangle-free and
excludes `K_{1,4}`.  Since the two singleton lobes have excess one, exact
accounting gives

```text
|E(H)|=4|V(H)|-9,                  delta_S(A)=11-|E(J)|>=5.       (1)
```

## Lemma 1 (every five-cut has a high-excess component)

For every five-cut `Q` of `G`, some component `D` of `G-Q` satisfies

```text
delta_Q(D)>=4.                                               (2)
```

### Proof

Write `k=|E(G[Q])|`.  The existing component-count and dense-boundary
theorems show that `G-Q` has two or three components and `k<=8`.

If `k=8`, the eight-edge theorem gives a component of excess at least four.
If there are three components, the concentration theorem gives one of
excess at least five.  If there are two components and `k<=6`, their
excesses sum to `13-k>=7`, proving (2).

It remains to consider two components and `k=7`.  Their excesses sum to
six.  If neither reaches four, both equal three.  The three-edge complement
of `G[Q]` is one of

```text
K_{1,3},            K_3,            P_4,
P_3 disjoint union K_2.                                    (3)
```

The first type is impossible by the star-completion theorem.  In each
other type choose two vertices `u,v` covering the three missing edges so
that `Q-{u,v}` is a triangle: choose two vertices of the missing triangle,
the two internal vertices of the missing `P_4`, or the middle vertex of
the missing `P_3` together with one end of the missing `K_2`, respectively.
Then

```text
d_{G[Q]}(u)>=2,                    d_{G[Q]}(v)>=2.
```

The two-shore cross-root theorem applies, one nominated vertex to each
excess-three lobe, and constructs a `K_7^-` minor.  This contradicts the
choice of `G`.  Hence (2) holds in every case.  \(\square\)

## Lemma 2 (singleton-contraction cuts)

For every `s in S` there is a two-set `R_s` such that

```text
Q_s={x,y,s} union R_s                                      (4)
```

is a five-cut of `G`,

```text
H-({s} union R_s) is disconnected,
|R_s intersect S|<=1.                                     (5)
```

### Proof

Triangle-freeness and the exclusion of `K_{1,4}` give `d_J(s)<=3`: a
vertex of degree four would have four independent neighbours and make `J`
exactly `K_{1,4}`.  Contract `xs` and call the new vertex `z`.  The
contraction loses the edge `xs` and one duplicate edge for each neighbour
of `s` in `J`, so

```text
|E(G/xs)|=4|V(G)|-8-d_J(s)
          >=4|V(G/xs)|-7.                                (6)
```

The quotient is a proper target-free minor.  Minimality of `G` therefore
implies that it is not five-connected.  Let `W` be a cut of `G/xs` of
order at most four.  The vertex `z` belongs to `W`; otherwise `W` lifts
unchanged to a cut of `G`.  Replacing `z` by `x,s` gives a cut

```text
Q=(W-{z}) union {x,s}
```

of `G` of order at most five.  Five-connectivity forces `|Q|=5`.

We claim that `y in Q`.  Otherwise `S-Q` is nonempty, and `y` joins all
its vertices in one component of `G-Q`.  Any other component lies in `A`
and has all its neighbours in `Q-{x}`, a set of order four.  This
contradicts five-connectivity.  Thus `Q` has the form (4) for a two-set
`R_s`.  Since deleting `Q` from `G` is the same as deleting
`{s} union R_s` from `H`, the first part of (5) follows.

If both members of `R_s` belonged to `S`, then `A`, together with the two
surviving vertices of `S`, would be connected: `A` is connected and full
to `S`.  This would make `H-({s} union R_s)` connected, a contradiction.
Hence `|R_s intersect S|<=1`.  \(\square\)

For the rest of the note write

```text
C_s={s} union R_s.                                        (7)
```

Thus `|C_s|=3`, `s in C_s`, and `|C_s intersect S|<=2`.

## Theorem 3 (root-only small sides)

For every `s in S`, the graph `H-C_s` has a unique component `D_s` of
excess at least four behind the lifted cut `Q_s`.  Moreover,

```text
|D_s| in {a,a+1}.                                         (8)
```

All other components have total vertex set `L_s`, where

```text
L_s subseteq S,                 1<=|L_s|<=2,
N_H(L_s)=C_s.                                             (9)
```

Every component of `H-C_s` is adjacent to all three vertices of `C_s`
and contains a member of `S-C_s`.  Finally,

```text
|E(G[Q_s])|<=6.                                           (10)
```

### Proof

Every component behind a minimum cut is full to that cut.  Hence every
component of `G-Q_s=H-C_s` is adjacent to all of `Q_s`, and in particular
to all of `C_s`.  Its adjacency to `x` forces it to contain a surviving
member of `S`, because `N_G(x)=S`.

Lemma 1 supplies a component `D_s` with excess at least four.  The choice
of `A` gives `|D_s|>=a`.  Since

```text
|H-C_s|=a+2
```

and `H-C_s` is disconnected, (8) follows and all other components together
have order one or two.  A component of order at most two has excess at
most three, so `D_s` is the unique high-excess component.

Every vertex outside `D_s` is a root.  Indeed, each low component contains
a surviving root.  If a low component of order two also contained a
vertex of `A`, that vertex would have at most one neighbour in its
component and three in `C_s`, and none in `{x,y}`.  Its degree in `G`
would be at most four, contrary to five-connectivity.  This proves the
first two assertions of (9).  The low components have no neighbours
outside their union and `C_s`, and each is full to `C_s`; hence
`N_H(L_s)=C_s`.

It remains to prove (10).  The vertices `x,y` are nonadjacent and have no
neighbours in `A`, while each is adjacent to every root in `C_s`.  Thus
`|E(G[Q_s])|<=7`, with equality only when `C_s` contains two roots and one
vertex of `A`, and `H[C_s]` is a triangle.

Suppose equality holds.  If `|D_s|=a`, then `D_s` is a minimum-order
high-excess component behind a seven-edge cut.  The triangle `H[C_s]`
also forces `G-Q_s` to have two components, since a three-component
five-cut has triangle-free boundary.  The complement of `G[Q_s]` is the
triangle on `x,y` and the member of `A` in `C_s`, which is an already
eliminated seven-edge type.  If `|D_s|=a+1`, the other component is a
singleton root.  Fullness makes that root adjacent to both roots in
`C_s`; together with their edge in `H[C_s]` this is a triangle in `J`.
Both alternatives are impossible, proving (10).  \(\square\)

Two refinements of (9) will be used repeatedly.

- If `L_s` is an edge of `J`, each endpoint has at least two neighbours
  in `C_s`, since it already has only `x,y` and its mate outside `C_s`.
- If the two members of `L_s` are nonadjacent, they are separate singleton
  components of `H-C_s`.  Each is full to `Q_s`, so they have the same
  neighbourhood `C_s` in `H`.

## Theorem 4 (classification of the boundary graph)

The boundary graph is one of

```text
J is P_3 disjoint union K_2,       P_5,       or C_5.      (11)
```

### Proof

For every `s`, equation (9) gives

```text
s in N_J(L_s)-L_s,                |N_J(L_s)-L_s|<=2.       (12)
```

Thus `J` has no isolated vertex.  It is triangle-free, and it has maximum
degree at most three because a vertex of degree four would make it
`K_{1,4}`.  The triangle-free graphs on five vertices with these degree
conditions are

```text
P_3 disjoint union K_2,       P_5,       subdivided K_{1,3},
C_5,                         C_4 with a pendant edge,       K_{2,3}.
                                                               (13)
```

We eliminate three entries.

For `K_{2,3}`, choose `s` in the part of order three.  The set `L_s` must
contain one of the two vertices in the other part.  Such a singleton has
three external neighbours.  An adjacent pair has three external
neighbours as well.  A nonadjacent pair either misses both neighbours of
`s`, has at least three external neighbours, or fails the identical-
neighbourhood condition following Theorem 3.  This contradicts (12).

For a four-cycle with a pendant edge, take the pendant vertex as `s`.
Its degree-three neighbour must lie in `L_s`.  Alone it has three external
neighbours; paired with either adjacent cycle neighbour it still has three;
paired with the opposite cycle vertex it fails the identical-neighbourhood
condition.  Again (12) is impossible.

Finally consider a subdivided claw and take as `s` a leaf joined directly
to its degree-three centre `c`.  The set `L_s` contains `c`.  The only
allowed set in (12) is the edge consisting of `c` and the other direct
leaf `u`; every other choice has three external neighbours or fails the
identical-neighbourhood condition.  Here `C_s` contains the two remaining
external roots and one vertex of `A`.  The root `u` is adjacent in `G`
only to `x,y,c` and possibly that one vertex of `A`, so it has degree at
most four.  This contradicts five-connectivity and proves (11).  \(\square\)

## Theorem 5 (Yuan fragments and degree-five roots)

The graph `H` has four distinct fragments whose intersections with `S`
are nonempty and pairwise disjoint.  At least three of those intersections
are singletons.  For a fragment `F` with

```text
F intersect S={t},                                        (14)
```

exactly one of the following holds.

1. `F={t}` and `d_G(t)=5`.
2. `F` is the unique high-excess component behind the five-cut
   `N_H(F) union {x,y}`.  Its anti-fragment consists of two roots, its
   three-vertex separator consists of two roots and one vertex of `A`,
   and

   ```text
   A-{one vertex} subseteq F.                             (15)
   ```

Consequently the following lower bounds hold:

```text
J=P_3 disjoint union K_2:       at least three roots have degree five;
J=P_5:                          at least two roots have degree five;
J=C_5:                          at least one root has degree five.       (16)
```

### Proof

First, `H` is three-connected.  A cut of order at most two in `H`,
together with `x,y`, would be a cut of `G` of order at most four.  Lemma 2
also shows that

```text
kappa(H)=3,                       kappa(H-s)=2
                                   for every s in S.       (17)
```

Indeed, `C_s` is a three-cut of `H`, and `R_s` is a two-cut of `H-s`;
the lower bounds in (17) follow from three-connectivity.

Every fragment of `H` meets `S`.  Otherwise it lies in `A` and its
three-vertex neighbourhood is also its neighbourhood in `G`, contrary to
five-connectivity.  Similarly, every fragment of `H-s` meets `S-{s}`:
one which did not would lie in `A` and would have at most its two-vertex
neighbourhood in `H-s`, together with `s`, as neighbours in `G`.

Thus `H` is a noncomplete `S`-locally `1`-critical three-connected graph
in Yuan's exact convention.  Yuan's fragment theorem supplies four
fragments with pairwise disjoint `S`-traces.  The traces are nonempty, so
at least three are singletons.

Fix a fragment satisfying (14) and put `T=N_H(F)`.  The fragment is one
component of `H-T`: every component behind the minimum three-cut `T` is
itself a fragment and hence meets `S`, while (14) leaves only one root
available in `F`.  The set

```text
T union {x,y}
```

is a five-cut of `G`.  Lemma 1 and the minimum choice of `A` give the same
high-component and root-only small-side conclusion as in Theorem 3.  If
`F` is on the low side, all its vertices are roots; (14) then gives
`F={t}`.  Since
`|T|=3`, the two further neighbours `x,y` give `d_G(t)=5`.

Suppose that `F` is the high component.  Its anti-fragment has order one
or two and consists entirely of roots.  It cannot have order one: the
other three roots would then all lie in `T`, making the lone anti-root
have degree three in `J`, whereas every graph in (11) has maximum degree
two.  Hence the anti-fragment consists of two roots.  The remaining two
roots and one vertex of `A` form `T`, proving (15).  Notice that `a>=3`,
since a component of order at most two has excess at most three.

We use the standard fragment-uncrossing fact that for two fragments
`F_1,F_2` with disjoint `S`-traces,

```text
F_1 intersect F_2 is empty
or their anti-fragments are disjoint.                     (18)
```

If both intersections in the two opposite corners were nonempty,
separator submodularity would make `F_1 intersect F_2` a fragment.  Its
`S`-trace would be empty, contrary to the local criticality just proved.
By (15), any two high singleton-trace fragments meet in at least
`a-2>=1` vertices of `A`.  Their two-root anti-fragments must therefore
be disjoint by (18).

It remains only to inspect the three graphs in (11).  A high singleton-
trace fragment has a two-root anti-fragment `L` whose external
neighbourhood in `J` consists of the other two separator roots.

- In `P_3` disjoint union `K_2`, no such two-root anti-fragment is
  compatible with the connected-edge or identical-neighbourhood
  alternatives following Theorem 3.  All three singleton-trace fragments
  are therefore literal degree-five roots.
- Label `P_5` as `1-2-3-4-5`.  The only high orientations have trace `1`
  and anti-root set `{3,4}`, or trace `5` and anti-root set `{2,3}`.
  Those anti-root sets intersect, so at most one such fragment is high.
  At least two singleton-trace fragments are literal degree-five roots.
- In `C_5`, the anti-root set for a high trace is the edge opposite that
  trace.  Pairwise high anti-root sets must be disjoint, and a five-cycle
  has matching number two.  At most two singleton-trace fragments are
  high, leaving at least one literal degree-five root.

This proves (16).  \(\square\)

## Theorem 6 (a degree-two boundary root gives strict descent)

No root `t in S` can satisfy

```text
d_G(t)=5,                         d_J(t)=2.              (19)
```

Consequently neither `C_5` nor `P_5` can occur.  The sole surviving
boundary graph satisfies

```text
J=P_3 disjoint union K_2:       at least three of its four
                                degree-one roots have degree five in G.   (20)
```

### Proof

Suppose (19) holds.  The two neighbours `x,y` leave exactly three
neighbours of `t` in `H`.  Two are its neighbours in `J`, so `t` has a
unique neighbour `p in A`.  Put

```text
Q=(S-{t}) union {p},             X={x,t,y}.
```

The set `Q` is a five-cut.  Indeed, `X` is a connected component of
`G-Q`, while every other component lies in the nonempty graph `A-p`.
Here `A-p` is nonempty because `a>=3`.  Exact accounting gives

```text
|E(G[X])|=2,
|E_G(X,Q)|=4+4+3=11,
delta_Q(X)=2+11-4(3)=1.                                  (21)
```

Lemma 1 supplies a component of `G-Q` with excess at least four.  By
(21) it lies in `A-p`, and hence has order strictly less than `a`.  This
contradicts the minimum choice of `A` and proves the first assertion.

Every vertex of `C_5` has degree two, so the degree-five root forced in
Theorem 5 excludes that graph.  Now consider `P_5`.  The proof of Theorem 5
shows that a high fragment with singleton trace can be rooted only at an
endpoint.  By the first part of this theorem, a literal degree-five
singleton trace can also occur only at an endpoint.  Yuan supplies at
least three singleton traces, and they are pairwise disjoint, whereas
`P_5` has only two endpoints.  This excludes `P_5`.

In `P_3` disjoint union `K_2`, no singleton-trace fragment is high by
Theorem 5.  At least three are therefore literal degree-five roots.  The
degree-two centre of the path is unavailable, so these are three of the
four degree-one roots.  This is (20).  \(\square\)

## Theorem 7 (distinct leaf representatives and further exact cuts)

Let `T` be the set of degree-one roots which have degree five in `G`, and
for `t in T` put

```text
P_t=N_G(t) intersect A.
```

Then

```text
3<=|T|<=4,                         |P_t|=2,              (22)
```

the family `(P_t:t in T)` has a system of distinct representatives, and

```text
a>=7.                                                       (23)
```

Moreover, for every `t in T` and `p in P_t`, the edge `tp` lies in an
exact five-cut `Q_{t,p}`.  Behind that cut there is a unique component of
excess at least four, and its order is `a` or `a+1`.

### Proof

Equation (22) follows from (20): a degree-five leaf root has the two
neighbours `x,y`, its unique neighbour in `J`, and exactly two neighbours
in `A`.  There are only four degree-one roots.

We first obtain the order bound.  Since `J` has three edges, exact
accounting at the original cut gives

```text
|E(G[A])|+|E_G(A,S)|=4a+8.                              (24)
```

Three roots in `T` contribute six edges to `E_G(A,S)`, while the other two
roots contribute at most `2a`.  Hence

```text
4a+8<=binom(a,2)+2a+6,
```

which gives `a>=6`.

Suppose `a=6`.  Four roots in `T` are impossible, since then the left side
of (24) is 32 while its two terms have sum at most

```text
15+(8+6)=29.
```

Thus `|T|=3`.  The three leaf roots contribute six boundary edges, so
(24) and the bounds

```text
|E(G[A])|<=15,                    |E_G(A,S)|<=18
```

leave only

```text
(|E(G[A])|,|E_G(A,S)|)=(14,18) or (15,17).              (25)
```

In the first case `G[A]=K_6-e` and both remaining roots are adjacent to
all of `A`; in the second `G[A]=K_6` and at least one remaining root is
adjacent to all of `A`.  That root together with `A` induces a `K_7^-` or
`K_7`, respectively.  Both contradict the choice of `G`, proving (23).

We next verify Hall's condition for `(P_t:t in T)`.  It is automatic for
one or two of the two-sets.  If three sets indexed by `R subseteq T` had
union `P` of order at most two, all three would equal `P`.  Deleting

```text
P union (S-R)
```

would remove at most four vertices and separate the connected set
`{x,y} union R` from the nonempty set `A-P`.  This contradicts
five-connectivity.  If `|T|=4` and the union of all four sets had order at
most three, deleting that union together with the one root of `S-T` would
give the same contradiction.  Hall's theorem now supplies distinct
representatives.

Finally fix `t in T` and `p in P_t`.  If `u_t` is the unique neighbour of
`t` in `J`, then

```text
N_G(t) intersect N_G(p)
  subseteq {u_t} union (P_t-{p}).                         (26)
```

Indeed, vertices of `A` are adjacent to neither `x` nor `y`.  Thus `tp`
has at most two common neighbours, and contracting it gives a proper
target-free graph with at least

```text
4|V(G)|-10=4|V(G/tp)|-6
```

edges.  Minimality makes the quotient non-five-connected.  Edge
contraction lowers connectivity by at most one, so the quotient is
four-connected.  Every four-cut contains the contracted vertex; otherwise
it lifts unchanged to a four-cut of `G`.  Replacing the contracted vertex
by `t,p` therefore gives an exact five-cut `Q_{t,p}` of `G`.

Lemma 1 supplies a component of excess at least four behind this cut.  Its
order is at least `a` by the choice of `A`, while only `a+2` vertices
remain after deleting the cut.  Since the cut disconnects the graph, the
high component has order `a` or `a+1`; all other components together have
order at most two and hence excess at most three.  The high component is
unique.  \(\square\)

## Exact nonclosure and repair lemma

Theorems 3--7 replace the vague five-root obstruction by a sharply
structured one, but they do not finish `(E5)`.  In the sole surviving
boundary graph, each `t in T` has

```text
N_H(t)={u_t} union P_t,
```

so this neighbourhood is a three-cut of `H` isolating `t`.  Theorem 7
allows distinct representatives `p_t in P_t` and returns an exact five-cut
through each connected pair `{t,p_t}`.  It does not give disjoint
extensions of those pairs or the ten pairwise adjacencies required for an
`S`-rooted `K_5` model.  The high component behind each returned cut has
order at least `a`, so the cuts also do not individually give strict
descent.

The first unsupported inference is therefore:

> the distinct leaf pairs supplied by Theorem 7 extend simultaneously to
> an `S`-rooted `K_5` model, or two of their exact five-cuts uncross to a
> strict high-excess descent.

A smallest useful repair is the following special statement.

> **Distinct leaf-pair repair.**  In the setting of Theorem 7, choose
> distinct representatives `p_t in P_t`.  The connected pairs `{t,p_t}`
> either extend to disjoint branch sets of an `S`-rooted `K_5` model in
> `H`, or two of the cuts `Q_{t,p_t}` yield a component `D` behind a
> five-cut `Q` with `|D|<a` and `delta_Q(D)>=4`.

The first outcome, together with the singleton branch sets `{x},{y}`,
is an explicit `K_7^-` model.  The second contradicts the choice of `A`.
This repair is strictly narrower than an arbitrary five-root reserve
theorem.  A smaller arbitrary side, a family of trace-disjoint fragments,
or an unrooted `K_6` model does not prove it.

## Dependencies

- The exact-density, exact-connectivity, component-count and dense-boundary
  reductions collected in
  [`hc7_k7minus_e5_frontier.md`](hc7_k7minus_e5_frontier.md).
- The [two-shore cross-root theorem](hc7_k7minus_e5_two_component_rooted_reduction.md)
  and the [complete seven-edge elimination](hc7_k7minus_e5_star_edge_cut_elimination.md).
- The [three-component concentration theorem](hc7_k7minus_e5_three_component_concentration.md).
- Xudong Yuan, *A Note on Fragments in a Locally `k`-Critical
  `n`-Connected Graph*, Ars Combinatoria **93** (2009), 25--31,
  Theorem 3.
