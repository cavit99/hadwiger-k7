# E5 six-boundary density localisation after `ff363c1`

**Status:** imported working artefact, preserved from commit `756ccf9`.  It is
not part of the authoritative proof spine.  Its sound finite statements and
unbounded deductions have been restated, independently checked and audited in
the promoted
[finite screen](../../../results/hc7_k7minus_e5_six_boundary_extension_screen.md)
and the corrected
[localisation reduction](../../hc7_k7minus_e5_six_boundary_localisation.md).
Section 10 below is not exhaustive: it omits the one-six-full kernel rows and
the both-endpoints cases with at most ten boundary edges.  This note does not
prove `(E5)` and must not be cited instead of the corrected reduction.

This note starts from the promoted six-boundary kernel reduction and finite
kernel theorem at commit

```text
ff363c1f078f6ef45fe772f0cb9c0d5a6f459b8d
```

and sharpens the three remaining branches.  Its main positive conclusion is:

> **Localisation endpoint.** Every labelled `P3` or `K3` kernel shore either
> returns the self-similar singleton exterior or has exactly one six-full
> opposite component and no other opposite component.  A shore containing two
> or more six-full components forces a `K_7^-` minor.  For the `K2` kernel, the
> only multi-six-full survivor has exactly two six-full components, no other
> opposite component, and at most seven boundary edges.

Thus the formerly unlocalised shore is no longer arbitrary.  The remaining
multi-component density-sensitive split is the exact `K2` two-six-full row.
There is also one sparse `K2` one-six-full/full-edge equality family.  The
self-similar and both-endpoints branches are sharpened separately below.

## 1. Imported setting and notation

Let `G` be the minimum `E5` enemy in the promoted `s=3` branch.  Thus

```text
|V(G)|=a+7,                 |E(G)|=4|V(G)|-7,          a>=8.
```

A second-contraction failure supplies a labelled six-set `P` and a low
kernel `T`, where

```text
T is K2, P3, or K3.
```

Every component of the opposite shore which is not six-full misses a unique
root of `P` and is one of the following promoted objects:

1. a singleton complete to the other five roots; or
2. an edge whose two ends are each complete to the other five roots.

For `r in P`, let `M_r` be the family of opposite components which miss `r`,
and put

```text
sigma_r=sum_{K in M_r}|K|.
```

The labelled kernel contacts are as follows.

### `K2` kernel

Use boundary labels

```text
P={0,1,2,3,4,5},                    0=u, 1=v,
T={d,w},                            dw in E(G),
N_P(d)={0,1,2,3},                   N_P(w)={0,1,4,5}.
```

The opposite shore has order `a-1`.  The vertex `u=0` has degree five.

### `P3` and `K3` kernels

Use boundary labels

```text
P={0,1,2,3,4,5},
T={d,f_1,f_2},
N_P(d)={0,1,2},
N_P(f_1)=N_P(f_2)={0,3,4,5}.
```

The low graph is the path `f_1-d-f_2` in the `P3` row and the triangle
`d f_1 f_2` in the `K3` row.  The opposite shore has order `a-2`.

There are two orientations:

```text
favourable:     0=u,
unfavourable:   1=u.
```

The literal boundary edge `01` is always present.

## 2. Aggregate missed-root mass

### Theorem 1 (two-vertex missed-root mass)

For every root `r in P`,

```text
sigma_r<=2.                                             (1)
```

### Proof

Delete the five-set

```text
Q_r=P-{r}.
```

Every member of `M_r` remains a separate component of `G-Q_r`.  All other
vertices outside `Q_r` lie in one connected central component:

- `r` is joined to the low kernel, because every boundary root has a low
  neighbour in each of the three labelled kernels;
- every six-full component meets `r`; and
- a component missing another root `s!=r` is complete to `P-{s}` and hence
  meets `r`.

The central component has at least three vertices.  Since exactly `a+2`
vertices lie outside a five-cut, no member of `M_r` can have order at least
`a`: such a component together with the central component would already use
at least `a+3` vertices.

The universal five-cut theorem supplies a component of excess at least four.
By the minimum choice of `a`, that component has order at least `a`.  It must
therefore be the central component.  The remaining components have total
order at most

```text
(a+2)-a=2.
```

This is (1).  \(\square\)

This is stronger than the promoted componentwise statement: all components
missing the same root have aggregate order at most two.

## 3. A six-full component is unavoidable

### Theorem 2 (forced six-full component)

Every kernel shore contains a six-full component.

### Proof

Assume that all opposite components are non-six-full.  By the promoted
classification, every vertex in a component which does not miss `u` is
adjacent to `u`.  Equation (1) bounds the total order of components which do
miss `u` by two.  The degree-five capacity at `u` bounds the remaining
vertices.

In the `K2` row, `u` already sees `v,d,w`.  At most two opposite vertices can
therefore lie in components which do not miss `u`.  The whole opposite shore
would have order at most

```text
2+sigma_u<=4,
```

whereas it has order `a-1>=7`.

In the favourable `P3/K3` orientation, `u=0` already sees `1,d,f_1,f_2`.
At most one opposite vertex does not miss `u`, so the opposite shore has
order at most three, whereas it has order `a-2>=6`.

In the unfavourable orientation, `u=1` already sees `0,d`.  At most three
opposite vertices do not miss `u`, so the opposite shore has order at most
five, again below `a-2>=6`.

All three alternatives are impossible.  \(\square\)

### Immediate capacity consequences

The same degree count gives:

```text
K2:                         one or two six-full components;
favourable P3/K3:           exactly one six-full component;
unfavourable P3/K3:         at most three six-full components.
```

The finite extension screen below eliminates three six-full components in
the last row and sharply classifies the two-six-full cases.

## 4. Exact extension screen

The verifier

```text
e5_six_boundary_extension_screen.cpp
```

uses only the C++ standard library and directly enumerates every partition of
an arbitrary host subset into seven nonempty connected branch sets.  It then
checks whether the branch-set quotient has at most one missing pair.

The checked partition-universe sizes are

```text
order 10:       11,880
order 11:      159,027
order 12:    1,899,612.
```

The exact new outputs are:

1. In the favourable `P3` row, one six-full representative plus one
   singleton missing `u` forces `K_7^-` at `e(P)>=5`; the maximum negative
   boundary size is four.
2. In the favourable `K3` row, the corresponding threshold is `e(P)>=4`;
   the maximum negative boundary size is three.
3. In either favourable row, two tied singleton components or one full edge
   missing `u` always force the target.
4. In the unfavourable one-six-full row, every degree-compatible pair of
   singleton components with a common missed root forces the target.  The
   same conclusion holds for a full edge, since adding its internal edge
   cannot destroy a minor model.
5. Three six-full representatives force the target in both `P3` and `K3`,
   for every boundary graph.
6. With two six-full representatives and `d_P(u)<=2`, the only negative
   `P3/K3` boundary graphs have at most four edges.  In the exact
   `d_P(u)=2` subrow they are precisely

   ```text
   01,12,
   optionally 02,
   optionally one of 34,35,45.
   ```

7. Adding any degree-compatible non-six-full singleton component to that
   two-six-full row forces the target.
8. In the `K2` two-six-full row, the boundary has at most seven edges.  At
   seven edges the unique labelled negative graph is

   ```text
   01,12,13,14,15,23,45.
   ```

9. Adding any non-six-full component to the `K2` two-six-full row forces the
   target: it is enough to retain one singleton minor of that component.
10. In the `K2` one-six-full row, the tied two-singleton case is positive.
    The sole full-edge equality family has boundary

    ```text
    01, with either, both, or neither of 23 and 45,
    ```

    and no other boundary edge.

The verifier also performs two contact-interface screens used in the
unbounded proof of the next section.

## 5. Elimination of every `P3/K3` multi-six-full shore

### Theorem 3

A target-free `P3` or `K3` kernel shore has exactly one six-full component.

### Proof

Three six-full components are excluded by the exact screen.  Suppose that
there are exactly two, called `C,D`.  The screen excludes every additional
opposite component.  It remains to eliminate the exact two-component shore.

There are two degree rows.

### 5.1 Boundary degree one at `u`

Suppose `d_P(u)=1`.  Since `u` also sees the low centre `d` and has degree
five, one of `C,D`, say `C`, contains exactly two neighbours `x,y` of `u`.

Put

```text
M=N_C({3,4,5}),
```

the set of vertices of `C` adjacent to at least one of the three leaf-side
roots.  The fullness of `C` makes `M` nonempty.

There are two vertex-disjoint paths in `C` from `x,y` to two distinct
members of `M`.  Otherwise the two-set-to-set form of Menger's theorem gives
a separator of order at most one.  After deleting that separator, some
component containing one of `x,y` has no vertex of `M`.  Its external
neighbourhood in `G` is contained in

```text
{the separator vertex, u, 0, 2},
```

which has order at most four.  This contradicts five-connectivity.

Enlarge the two disjoint paths inside the connected graph `C` to two
adjacent connected parts which partition `C`.  Both parts meet `u`, and the
union of portals to `{3,4,5}` meets both parts.

The exact 243-pattern split screen says that, for every one of the eight
possible negative boundary graphs and for both low kernels, a target-free
split must put **all** portals to roots `3,4,5` exclusively in one part.
The constructed split violates that condition.  Hence it gives an explicit
`K_7^-` model, a contradiction.

### 5.2 Boundary degree two at `u`: rooted `K4` reduction

Now `d_P(u)=2`.  The degree-five count gives

```text
|E_G({u},C)|=|E_G({u},D)|=1.                           (2)
```

Choose `C` with maximum six-cut excess.  If `k=e(P)`, then

```text
eta_P(C)>=ceil((16-k)/2)       in the P3 row,
eta_P(C)>=ceil((15-k)/2)       in the K3 row.          (3)
```

For `j in P-{u}`, put

```text
Z_j=P-{u,j}.
```

A `Z_j`-rooted `K4` model in `G[C union Z_j]` composes with the low kernel
and `D` to give `K_7^-`.  The construction is explicit.  For example, when
`j=2`, use outside bags

```text
{u,2,d,f_1},       {f_2},       D;
```

when `j` is one of `3,4,5`, use

```text
{u,d,f_1},         {j,f_2},     D;
```

and when `j=0`, use

```text
{0,u,f_1},         {d,f_2},     D.
```

Together with the four rooted bags these have at most one missing
adjacency.  Extra boundary edges and the leaf edge in the `K3` row only
help.

Assume that `(G[C union Z_j],Z_j)` is internally four-connected.  Since a
rooted `K4` is forbidden by the preceding composition, the rooted density
bound gives

```text
e(C)+e(C,P)-p_C(u)-p_C(j)+e(P[Z_j]) <= 3|C|+5.
```

Using `p_C(u)=1` from (2) and `p_C(j)<=|C|`, this yields

```text
eta_P(C)<=6-e(P[Z_j]).                                (4)
```

If internal four-connectivity fails, add the omitted roots `{u,j}` to a
rooted separator of order at most three.  Five-connectivity makes the result
an exact five-cut.  In the absence of strict descent, its small component
has order at most two.  A two-vertex component has excess at most two,
because only one of its vertices can see `u`; the global
`(minimum order, maximum Phi, minimum rho)` selection excludes it.  Hence
the small component is a singleton `c_j`, complete to the five-cut.  It is
the unique neighbour of `u` in `C`.

#### `P3`

For every one of the eight possible boundaries and every choice of `j`,
the right side of (4) is strictly smaller than the lower bound (3).
Therefore all five rooted pairs fail internal four-connectivity.  Their
singletons are all the unique `u`-neighbour in `C`, so they are one vertex
`c`.  That vertex is adjacent to `u` and to all five choices of `j`, giving
degree at least six.  This contradicts its degree-five singleton cut.

#### `K3`: boundary sizes two and four

The same strict argument works for every `j` when `k=2` or `k=4`, again
giving the degree contradiction.

#### `K3`: boundary size three

There are two types.

1. `P` contains the triangle `012` and no other boundary edge.  The strict
   choices are `j=3,4,5`.
2. `P` has edges `01,12` and one edge among `34,35,45`.  If that edge is
   `34`, the strict choices are `j=0,2,5`, with the other cases obtained by
   permuting `3,4,5`.

The strict failures give one degree-five singleton `c` adjacent to `u` and
the three displayed roots.  Of the two remaining choices of `j`, at least
one rooted pair is internally four-connected; otherwise `c` would again
have degree at least six.  Equality in (3)--(4) then gives

```text
eta_P(C)=6,
```

and some remaining root `j` is adjacent to **every** vertex of `C`.

The final 162-pattern split screen now closes the equality.  Split any
spanning tree edge of `C` into two adjacent connected parts.  In the
triangle type, a target-free split must put all portals to roots `3,4,5`
exclusively in one part.  Hence, if two distinct vertices of `C` met those
roots, a tree edge separating them would give the target.  All such portals
therefore lie at a single vertex.  The singleton `c` meets all three, so it
is that vertex.  It is also adjacent to `u` and to the root universal on
`C`, giving five boundary neighbours and no available internal neighbour.
But `eta_P(C)=6` forces `|C|>=3`, contradicting connectedness of `C`.

In the one-`U`-edge type, the screen says that all portals to

```text
{u,0,2,the isolated member of {3,4,5}}
```

must be concentrated at one vertex.  Again that vertex is `c`; the
universal endpoint of the `U`-edge is its fifth boundary neighbour, leaving
no internal neighbour in the nontrivial connected component `C`.  This is
the same contradiction.

Thus two six-full components are impossible in both `P3` and `K3`.
\(\square\)

## 6. Complete localisation of `P3/K3` opposite shores

### Corollary 4

In a target-free `P3` or `K3` kernel row, exactly one of the following
holds.

1. The opposite shore is one six-full connected component.
2. Some five-cut `P-{r}` has exactly one singleton component missing `r`
   and one connected central component.  This is the self-similar singleton
   exterior.

### Proof

Theorem 3 gives exactly one six-full component.  If there are additional
non-six-full components, Theorem 1 gives at most two vertices for each
missed root.

A pair of singleton components with the same missed root, or a full edge,
is excluded by the extension screen in both orientations.  Hence every
surviving missed root occurs for only one singleton component.  Deleting
`P-{r}` then leaves that singleton and the connected central component from
the proof of Theorem 1.  \(\square\)

In the favourable orientation the finite screen additionally gives the
sharp boundary bounds

```text
P3 self-similar singleton:      e(P)<=4,
K3 self-similar singleton:      e(P)<=3.
```

## 7. Exact `K2` endpoint

### Theorem 5

A target-free `K2` kernel shore is one of the following.

1. One six-full component and no other opposite component.
2. A self-similar singleton exterior obtained from `P-{r}`.
3. One six-full component and one full edge missing `u`, with

   ```text
   E(P)={01} union X,              X subseteq {23,45}.  (5)
   ```

4. Exactly two six-full components, no other opposite component, and

   ```text
   e(P)<=7.                                            (6)
   ```

At equality in (6), the boundary is uniquely

```text
01,12,13,14,15,23,45.                                 (7)
```

### Proof

The degree-five root allows one or two six-full components.

If there are two, it has no remaining degree slot for any boundary edge
other than `01` or for a non-six-full vertex which sees `u`.  Any component
missing `u` contains a singleton minor; the extension screen shows that
adding such a singleton to two six-full representatives gives `K_7^-`.
Thus there are no additional components, and the exact screen gives
(6)--(7).

Suppose that there is one six-full component.  Any singleton component
whose missed root occurs only once gives the self-similar cut `P-{r}`.
Two singleton components with the same missed root produce a selected
five-cut tie; the boundary induced by the five roots is `P3` disjoint union
`K2`, and the exact tied-twin screen gives the target.

A two-vertex component not missing `u` would use two unavailable neighbours
of the degree-five root.  Thus the only remaining two-vertex component is a
full edge missing `u`.  The exact screen leaves precisely the four boundary
graphs in (5).  \(\square\)

The edge family (5) has a useful exact density identity.  If `C` is the
six-full component, then

```text
eta_P(C)=13-e(P),
|E_G({u},C)|=2.
```

Putting `Q=P-{u}` gives

```text
|E(G[C union Q])|=4|C|+10
                  =4|C union Q|-10.                   (8)
```

Thus the residual is exactly at the rooted two-helper equality, not merely
an uncontrolled sparse case.

## 8. Anchor-preserving peel rank for the self-similar quotient

The self-similar branch admits a well-founded rank which preserves the
original anchor `z` and the labels `u,v` at the quotient level.

Let `H_0=H`.  Whenever `H_i` has the anchored singleton normal form, choose
a returned degree-four singleton `d_i` and put

```text
H_{i+1}=H_i-d_i.
```

Deleting `d_i` removes exactly four edges and one vertex, so

```text
e(H_{i+1})>=4|H_{i+1}|-7.                             (9)
```

It also leaves a target-free minor and preserves the literal anchor `z`.
Moreover `H_{i+1}` is at least three-connected.

A maximal peel sequence terminates in one of the following ways.

1. A five-connected graph is obtained.  By (9), this is a smaller `E5`
   enemy, a contradiction.
2. Connectivity drops to three.  A three-cut lifts with the last deleted
   singleton to a four-cut of the preceding graph.  The anchored normal
   form then gives two adjacent degree-four singleton shores, the quotient
   `K2` terminal.
3. Four-connectivity remains, but a four-cut is no longer an anchored
   singleton-plus-connected-remainder cut.  This is exactly the nontrivial
   separation needed for the second-contraction kernel mechanism.

The process cannot continue indefinitely because order strictly decreases;
at order seven the density in (9) would force `K7`.

This removes the logical possibility that the self-similar quotient is a
terminal abstract object.  It does **not** yet close the host-specific
branch: after several deletions, earlier singleton vertices may have supplied
extra neighbours in `G`, so the final quotient `K2` does not automatically
have the original degree-five labelled lift.  The next invariant must retain
that incidence history, for example by recording which peeled vertices use
`u`, which use only `v`, and the rooted elimination forest among them.

## 9. Both-endpoints separation: improved boundary bound

Suppose a nontrivial four-separation after contracting `dz` has both original
endpoints `u,v` meeting both open sides.  Its lift has six-boundary

```text
R={u,d,v} union U,                   |U|=3.
```

Both `u` and `d` have degree five.  They are adjacent to one another and to
`v`, and each has a neighbour in each open side.  Consequently each has at
most one neighbour in `U`.  The four vertices `{v} union U` span at most six
edges, so

```text
e(G[R])<=6+3+1+1=11.                                (10)
```

This improves the previous twelve-edge bound.

Equality in (10) is rigid:

```text
G[{v} union U]=K4,
e_G({u},U)=e_G({d},U)=1,
```

and each of `u,d` has exactly one neighbour in each open side.  The six-cut
excess identity then leaves total opposite excess exactly six.  Thus the
both-endpoints branch has reduced to a two-anchor rooted model-or-small-atom
problem over a `K4` core; it is not an arbitrary twelve-edge boundary.

## 10. Exact remaining obligations

The new endpoint has three parts.

### A. Exact `K2` two-six-full split

```text
G-P=T(K2) dotunion C dotunion D,
C,D six-full,
e(P)<=7,
u has exactly one neighbour in each of C,D.
```

At `e(P)=7`, the unique boundary is (7).  This is now the sole
multi-six-full kernel shore.

### B. Exact `K2` one-six-full equality

```text
G-P=T(K2) dotunion C dotunion K2,
C six-full,
the second K2 misses u,
E(P)={01} union X, X subseteq {23,45},
|E(G[C union (P-{u})])|=4|C union (P-{u})|-10.
```

This asks for an equality-sensitive rooted model, not another boundary
census.

### C. Incidence-stable self-similar peel or both-endpoints atom

The deletion rank proves termination at the quotient level, but the final
step must preserve the original endpoint incidence history.  In the
both-endpoints row, (10) reduces the task to placing both degree-five anchors
inside one rooted two-helper system or exposing a new order-at-most-two
atom.

The best next theorem is therefore no longer a broad quasi-five splitter.
It is the following exact statement.

> **Anchored `K2` split-or-ranked-peel lemma.** In either the exact `K2`
> configuration A/B or the boundary-eleven both-endpoints configuration,
> either construct `K_7^-`, return a five-cut component of order below `a`
> and excess at least four, or delete/contract one returned singleton while
> strictly decreasing an endpoint-incidence rank which records the original
> `u,v` preimages.

Pure contact quotients cannot prove this statement; the repository barriers
show that density and internal component structure are essential.  The
advance above isolates exactly where that internal structure must now enter.

## 11. Reproduction

Compile and execute:

```bash
g++ -O3 -std=c++20 -Wall -Wextra -pedantic -fopenmp \
  e5_six_boundary_extension_screen.cpp \
  -o e5_six_boundary_extension_screen

OMP_NUM_THREADS=5 ./e5_six_boundary_extension_screen
```

Expected final line:

```text
ALL CHECKS PASSED
```

Pinned local hashes at the time of this note:

```text
source:
f4705afa63fd4653549726927fefdb25efbeae57763ab52e4319e978f5e8e3ef

compiled Linux binary:
aa80e35b47687f174d9670e6568993ee9daeb25afe8225110acf3b2b01e7f126

recorded output:
3cd13e6d330dccf072cc6103fd237b528ca9093679a80507cf7775e19d63b03c
```

The compiled binary hash is environment-specific; the source and exact
stdout are the durable artefacts.
