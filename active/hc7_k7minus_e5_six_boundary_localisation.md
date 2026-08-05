# Density localisation across the labelled six-boundary kernels

**Status:** active written reduction using a computer-assisted finite theorem;
separate internal audit GREEN for the pinned revision in the
[adjacent audit](hc7_k7minus_e5_six_boundary_localisation_audit.md).  This
reduction does not prove `(E5)`.

Write `K_7^-` for `K_7` with one edge deleted.

## 1. Imported endpoint

Use the selected minimum-`E5` kernel setting of the audited
[second-contraction reduction](hc7_k7minus_e5_s3_second_contraction_kernel_reduction.md).
Thus

```text
|V(G)|=a+7,                    |E(G)|=4|V(G)|-7,
a>=8,
```

and a six-set `P={0,1,2,3,4,5}` exposes one of the labelled low kernels
`T=K_2,P_3,K_3`.  A component of `G-P` is **`P`-six-full** when its
neighbourhood is `P`.  The componentwise classification in the imported
reduction and the audited
[missed-root mass theorem](../results/hc7_k7minus_e5_six_boundary_mass_bounds.md)
give the following facts.

1. A `P`-non-six-full opposite component misses one root and is a full
   singleton or a full edge of order two.
2. All components missing any fixed root have total order at most two.
3. Every kernel shore has a `P`-six-full component.  Their numbers are at
   most two in the `K_2` case, one in the favourable `P_3,K_3` orientation,
   and three in the other orientation.

For a component `C` of `G-P`, put

```text
eta_P(C)=|E(G[C])|+|E_G(C,P)|-4|C|.
```

If `k=|E(G[P])|`, the exact opposite-shore identities are

\[
 \sum_{C\ne T}\eta_P(C)=
 \begin{cases}
  16-k,&T=K_2,\\
  16-k,&T=P_3,\\
  15-k,&T=K_3.
 \end{cases}                                           \tag{1.1}
\]

We also use the computer-assisted
[extension screen](../results/hc7_k7minus_e5_six_boundary_extension_screen.md).

## 2. Multiple six-full components in the `P_3,K_3` kernels

### Theorem 2.1

A target-free `P_3` or `K_3` kernel shore has exactly one `P`-six-full
component.

### Proof

The finite screen excludes three six-full components.  The favourable
orientation already has at most one by the degree-five bound.  It remains to
consider the other orientation with exactly two six-full components `C,D`.
Here the degree-five endpoint is `u=1`.  The screen excludes every additional
opposite component and restricts a target-free boundary to

\[
 E(G[P])=\{01\}\mathbin\cup X\mathbin\cup Y,          \tag{2.1}
\]

where `X` is a subset of `{02,12}` and `Y` is empty or one of
`{34},{35},{45}`.

### Boundary degree one

Suppose first that `d_{G[P]}(u)=1`.  Besides its boundary neighbour and the
low centre `d`, the vertex `u` has three neighbours in `C union D`.  One of
the two components, say `C`, contains two of them, denoted by `x,y`.

Let `M` be the set of vertices of `C` adjacent to at least one of roots
`3,4,5`.  There are two vertex-disjoint paths in `C` from `x,y` to two
distinct vertices of `M`.  Otherwise the two-set version of Menger's theorem
gives a separator of order at most one.  A component behind it which contains
one of `x,y` and no member of `M` has its entire external neighbourhood in

```text
{the separator vertex,u,0,2},
```

contrary to five-connectivity.

Extend the two paths to two adjacent connected parts which partition `C`.
Both parts meet `u`, and the portals to roots `3,4,5` meet both parts.
Contracting the parts and `D` gives one of the 243-pattern split hosts in
Theorem 2.1(1) of the finite screen.  Target-freeness would put all portals
to roots `3,4,5` exclusively in one part, a contradiction.

### Boundary degree two

Now suppose `d_{G[P]}(u)=2`.  Degree five gives

\[
 |E_G(\{u\},C)|=|E_G(\{u\},D)|=1.                    \tag{2.2}
\]

Choose `C` with maximum `eta_P`.  Equation (1.1) gives

\[
 \eta_P(C)\ge
 \begin{cases}
  \lceil(16-k)/2\rceil,&T=P_3,\\
  \lceil(15-k)/2\rceil,&T=K_3.
 \end{cases}                                           \tag{2.3}
\]

For `j in P-{u}`, put `Z_j=P-{u,j}`.  A `Z_j`-rooted `K_4` model in
`G[C union Z_j]` composes with the low kernel and `D` to give `K_7^-`.
Indeed, the three additional bags may be chosen as follows:

```text
j=2:          {u,2,d,f_1}, {f_2}, D;
j in 3,4,5:   {u,d,f_1}, {j,f_2}, D;
j=0:          {0,u,f_1}, {d,f_2}, D.
```

Together with the four rooted bags, each list has at most one missing
adjacency.  In the last list the edge from `u` to root `2` is present by
`d_{G[P]}(u)=2` and (2.1).

Suppose `(G[C union Z_j],Z_j)` is internally four-connected.  The preceding
composition forbids a rooted `K_4`.  Norin--Totschnig Lemma 9, in the exact
form already used in the audited
[sparse three-component reduction](hc7_k7minus_e5_three_component_sparse_elimination.md#lemma-1-two-lobe-models),
therefore gives

\[
 e(G[C])+|E_G(C,P)|-p_C(u)-p_C(j)+|E(G[Z_j])|
 \le3|C|+5.
\]

Using `p_C(u)=1` and `p_C(j)<=|C|`, this yields

\[
                  \eta_P(C)\le6-|E(G[Z_j])|.          \tag{2.4}
\]

If internal four-connectivity fails, add `u,j` to a rooted separator of
order at most three.  Five-connectivity makes an exact five-cut.  Its
connected far component has order at most two unless it gives a strict
high-excess descent.  An edge component has excess at most two because only
one of its vertices can see `u`; the selected
`(minimum order, maximum Phi, minimum rho)` comparison excludes it.  Thus
the far component is a degree-five singleton `c_j` complete to the cut.  By
(2.2), it is the unique neighbour of `u` in `C`.

For `P_3`, direct substitution of all eight boundaries (2.1) makes (2.3)
strictly larger than the right side of (2.4) for every `j`.  All five rooted
pairs therefore fail internal four-connectivity.  Their singletons coincide
with the unique `u`-neighbour `c`, making `c` adjacent to `u` and all five
other roots.  This contradicts `d_G(c)=5`.

For `K_3`, the same argument applies to every `j` when `k=2` or `k=4`.  If
`k=3`, there are two boundary types.

1. If `G[P]` is the triangle on `{0,1,2}`, the strict choices are
   `j=3,4,5`.
2. If `E(G[P])={01,12,34}`, the strict choices are `j=0,2,5`; the other
   two cases follow by permuting roots `3,4,5`.

The strict choices again give one degree-five singleton `c`.  At least one
of the two remaining rooted pairs is internally four-connected, since a
second failed pair would give `c` a sixth neighbour.  Equality throughout
(2.3)--(2.4) then gives

```text
eta_P(C)=6,
some remaining root is adjacent to every vertex of C.  (2.5)
```

Split a spanning tree of `C` at any edge and contract its two parts.  The
equality split screens say that target-freeness concentrates all portals to
`{3,4,5}` at one part in the triangle case, and all portals to
`{u,0,2,5}` at one part in the `34` case.  Applying this to every spanning
tree edge shows that all the relevant portal vertices are one vertex.  The
strict failed pairs identify that vertex as `c`.  The universal root in
(2.5) is its fifth boundary neighbour, so the degree-five vertex `c` has no
neighbour inside `C`.  But `eta_P(C)=6` forces `|C|>=3`, contradicting the
connectedness of `C`.

Thus two six-full components are impossible.  \(\square\)

## 3. Localisation of `P_3,K_3` opposite shores

### Corollary 3.1

In a target-free `P_3` or `K_3` kernel configuration, exactly one of the
following holds.

1. The opposite shore is one `P`-six-full connected component.
2. For some `r in P`, the five-cut `P-{r}` has one degree-five singleton
   component missing `r` and one connected central component.

### Proof

Theorem 2.1 gives exactly one six-full component.  Suppose there is another
opposite component.  The missed-root mass theorem leaves only singleton
components or one full edge for each missed root.

A full edge is excluded by the finite screen in both orientations.  The
same is true of two singleton components with a common missed root.  In the
favourable orientation, such a pair makes `P-{r}` another cut tied with the
selected data `(a,Phi,rho)=(a,11,2)`; the prior exact three-component
classification therefore makes its boundary `P_3` disjoint union `K_2`,
which is precisely the tied-twin finite screen.  In the other orientation
the unrestricted degree-compatible twin screen applies.

Thus any surviving missed root belongs to one singleton only.  Deleting
`P-{r}` leaves that singleton and the connected central component from the
proof of the missed-root mass theorem.  \(\square\)

In the favourable orientation the finite screen also gives

```text
P_3 singleton exterior:       |E(G[P])|<=4,
K_3 singleton exterior:       |E(G[P])|<=3.
```

## 4. Exact `K_2` alternatives

### Theorem 4.1

A target-free `K_2` kernel configuration has at least one of the following
forms.

1. The opposite shore is one `P`-six-full component.
2. For some `r`, the cut `P-{r}` has one full singleton component and one
   connected central component.
3. The opposite shore is one `P`-six-full component `C` and one full edge
   missing `u=0`, with

   \[
      E(G[P])=\{01\}\mathbin\cup X,
      \qquad X\subseteq\{23,45\}.                    \tag{4.1}
   \]

4. The opposite shore consists of exactly two `P`-six-full components,
   `|E(G[P])|<=7`, and `u` has exactly one neighbour in each.  At seven
   boundary edges the unique labelled boundary is

   ```text
   01,12,13,14,15,23,45.                             (4.2)
   ```

### Proof

The missed-root mass and degree-five bounds permit one or two six-full
components.

With two, the degree of `u` leaves no boundary edge at `u` except `01` and
no extra component which meets `u`.  Any remaining component must miss `u`;
retaining one endpoint gives the singleton extension excluded by the finite
screen.  Thus no extra component exists, and the two-six-full screen gives
(4.2) and the seven-edge bound.

Now suppose there is one six-full component.  A singleton whose missed root
occurs only once gives outcome 2.  Two singleton components with a common
missed root can only miss `u`; their tied five-cut has boundary `P_3`
disjoint union `K_2`, and the tied-twin screen excludes it.  A two-vertex
component which meets `u` would exceed the degree of `u`.  The only remaining
non-six-full component is therefore one full edge missing `u`, and the exact
finite screen gives (4.1).  \(\square\)

In outcome 3, equation (1.1) and the full edge's excess three give

```text
eta_P(C)=13-|E(G[P])|,
|E_G({u},C)|=2.
```

For `Q=P-{u}` this is the exact equality

\[
 |E(G[C\cup Q])|=4|C|+10=4|C\cup Q|-10.             \tag{4.3}
\]

## 5. Exact scope and remaining obstruction

The result removes every `P_3,K_3` shore with multiple six-full components
and every shore made only from non-six-full components.  It does not close
the remaining single-six-full components.

Within the three kernel families, a target-free host is now confined to:

1. one unbounded `P`-six-full component in a `K_2,P_3` or `K_3` kernel;
2. a self-similar singleton exterior as in Corollary 3.1 or Theorem 4.1;
3. the `K_2` one-six-full/full-edge equality (4.1)--(4.3); or
4. the `K_2` two-six-full family of Theorem 4.1(4), with at most seven
   boundary edges.

Two branches preceding the kernel construction also remain:

- the four-connected quotient may repeat the anchored
  singleton-plus-connected-remainder normal form; deleting returned
  singletons preserves density and terminates at the quotient level, but
  later cuts need not lift to `G` with the original endpoint labels or
  selected-lobe data; and
- every eligible nontrivial separation may be met on both sides by both
  original endpoints.  The audited boundary theorem gives only
  `|E(G[R])|<=11`; the literal `K_4` core occurs at equality, and all rows
  with at most ten boundary edges remain open.

Consequently the next proof must use internal density in an unbounded
six-full component or preserve the original endpoint-incidence history
through a singleton reduction.  The existing contact-quotient barriers rule
out replacing either task by boundary incidence alone.
