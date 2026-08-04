# Internal audit: refinement of the lifted triangle cut

**Verdict:** GREEN for the pinned source revision.  This is a separate
internal mathematical audit, not external peer review.

**Audited source:**
`active/hc7_k7minus_e5_s3_triangle_cut_refinement.md`

**SHA-256:**
`870e6d41c3d0f0e0e69c2a410ff6543bb2127ead3fd6cc371a1a1f148a123495`

No mathematical correction is required at this revision.

The change from the previously audited source revision
`1e989666db2fa71544fecee2c31e67b2dd77d256323765a0193130c59a822614`
is status-only: the source now links this adjacent audit.  Its theorem
statements, proofs, identities, and mathematical endpoint are unchanged.

## 1. Imported setup and orders

The singleton-triangle contraction supplies a four-cut `{z} union R` in
the quotient, with `|R|=3`, and its lift

```text
L={p,t,q} union R
```

is an order-six cut of `G`.  Components of `G-L` are full to `R` and meet
the triangle in aggregate.  Since the exact two-singleton host has
`|V(G)|=a+7`, exactly `a+1` vertices lie outside `L`.

The exact singleton neighbourhoods give three exterior neighbours for
each triangle vertex:

```text
P_p=N_G(p)-{p,t,q},
P_t={x,y,u_t},
P_q={b} union R_0.
```

The singleton endpoint for `p` includes the fact that deleting `N_G(p)`
leaves exactly `{p}` and one connected exterior.  The leaf-cut
classification gives the analogous fact for `q`.  The refined standing
choice first minimises `a` and then maximises lobe excess; it is inherited
through the singleton endpoint from the companion-cut reduction.  In the
original `P_3` disjoint union `K_2` row,
`delta_S(A)=11-3=8`.  Thus every imported hypothesis used later is
available and the maximum-excess comparison is legitimate.

## 2. Triangle contacts and component capacity

If a component `C` of `G-L` met only one triangle vertex `u`, its complete
external neighbourhood would be contained in `R union {u}`.  Fullness to
`R` and the assumed contact with `u` make this set its exact neighbourhood.
Another component of `G-L` survives its deletion because `L` is a cut.
This would be a cut of order four in `G`, contradicting
five-connectivity.  Every component therefore meets at least two triangle
vertices.

Consequently, a component missing `u` has exact neighbourhood

```text
R union (Delta-{u}),
```

which is a five-cut.  No possible external neighbour is omitted: the set
is a component after deleting `L`, it is full to `R`, and the two-of-three
lemma supplies precisely the other two triangle contacts.

For a triangle vertex `u`, distinct complementary components require
distinct members of its three-set `P_u`; neighbours in `R` consume further
distinct members of the same set.  Hence

```text
c_u+|R intersect P_u|<=3.
```

Summing over the triangle and using two contacts per component gives
`2m<=9`, so `m<=4`.  Multiple neighbours of `u` in one component only
strengthen this inequality.

There are no edges between distinct components of `G-L`.  Grouping every
edge outside `G[L]` by its complementary component therefore gives

```text
sum_C eta_L(C)
  =|E(G)|-|E(G[L])|-4(|V(G)|-6)
  =17-|E(G[L])|.
```

Since `Delta` induces a triangle,

```text
|E(G[L])|=3+|E(G[R])|+|E_G(Delta,R)|,
```

which yields the second form
`14-|E(G[R])|-|E_G(Delta,R)|`.  Thus both constants and both equalities
in the exact six-cut identity (3) are correct.

## 3. Exact misser dichotomy and six-full consequence

For a component `C` missing `u`, apply the universal high-excess lemma to
its exact five-cut.  If `C` has excess at least four, minimum lobe order
gives `|C|>=a`.  There are only `a+1` vertices outside `L` and at least
one other component, so equality holds and the entire remainder is one
singleton component.

If `C` has excess at most three, a different component behind the same
five-cut has excess at least four and hence order at least `a`.  A
five-cut leaves `a+2` vertices, so `|C|<=2`.  These integer excess cases
are exhaustive and mutually exclusive.

If there is neither a high misser nor a component meeting all three
triangle vertices, every component is a low misser of order at most two.
At most four such components contain at most eight vertices.  This
contradicts

```text
|V(G-L)|=a+1>=9.
```

Thus the six-full conclusion follows exactly as stated.

## 4. Connected-exterior swap for a high `p`-misser

Suppose the order-`a` component `C` misses `p` and the other component of
`G-L` is `{d}`.  The sets `P_p` and
`E_p=V(G)-N_G[p]` partition the vertices outside the triangle and have
orders three and `a+1`, respectively.  Since `C` misses `p`, it contains
no member of `P_p` and is a subset of `E_p`.

The partition outside the triangle is

```text
R disjoint union C disjoint union {d}.
```

After the `a` vertices of `C` have been counted in `E_p`, exactly one of
the four vertices in `R union {d}` lies in `E_p` and the other three form
`P_p`.  There are exactly two placements:

1. `R=P_p` and `d in E_p`; or
2. `d in P_p`, two vertices of `R` are `P_p-{d}`, and the third is a
   vertex `r in E_p`.

In the first placement `N_G[p]=L`, so its exterior is the disconnected
union `C disjoint union {d}`, contradicting the imported connectedness of
`E_p`.  The second placement is therefore forced and gives equation (4)
of the source.

The singleton `{d}` is full to `R` and meets at least two triangle
vertices.  Since `d in P_p`, one is `p`; hence its number `k` of contacts
with `{t,q}` is one or two.  Deleting

```text
Q_p=R union {t,q}
```

leaves exactly the two components `C` and `{p,d}`.  Indeed, `pd` is an
edge, `p` misses `C`, and `d` has no edge to `C` because those vertices
were in distinct components of `G-L`.

## 5. Excess identities and the tie-break

The low edge `{p,d}` has one internal edge.  The vertex `p` has four
incidences with `Q_p`: two to `P_p-{d}` and the edges to `t,q`.  The
vertex `d` has three incidences with `R` and `k` with `{t,q}`.  Therefore

```text
delta_Q_p({p,d})=1+4+(3+k)-8=k.
```

Inside the lifted six-set, `p` has exactly those same four neighbours, so
`Q_p=L-{p}` gives

```text
|E(G[Q_p])|=|E(G[L])|-4.
```

For a five-cut in the exact `4n-7` graph, the component excesses sum to
`13-|E(G[Q_p])|`.  Since the cut has precisely the two components above,

```text
delta_Q_p(C)=13-(|E(G[L])|-4)-k
            =17-|E(G[L])|-k.
```

The component is the assumed high misser, giving the lower bound four.
It has order exactly `a`, so the maximum-excess tie-break against the
selected lobe of excess eight gives the upper bound eight.  Rearranging
the upper bound yields `|E(G[L])|+k>=9`.  All directions and constants in
equation (5) are correct.

For a high `q`-misser, the exact singleton cut `N_G(q)` has one connected
exterior by the leaf-cut classification.  Replacing `p,P_p,{t,q}` by
`q,P_q,{p,t}` repeats the partition count verbatim.  The vertex `q` also
has four neighbours in `L` after the forced swap, so every symmetric
identity is valid.

## 6. The two high `t`-misser normal forms

Suppose that the order-`a` component `C` misses `t`, and write `{d}` for
the other component of `G-L`.  The exact exterior neighbourhood of `t`
is

```text
P_t={x,y,u_t}.
```

If `td` is absent, none of these three vertices can lie in `C` or equal
`d`, so all three belong to `R`.  Hence `R={x,y,u_t}`.  Fullness of the
singleton `{d}` makes it adjacent to `x,y,u_t`, and the two-contact lemma
makes it adjacent to both `p,q`.  It cannot lie in `A`, because vertices
of `A` have no edge to `x` or `y`; as `x,y,u_t` already lie in `R`, it
therefore lies in `S`.  The edges `tu_t,u_td` place `t,u_t,d` in the
three-vertex path component of `G[S]`.  Component separation and fullness
now give the exact equal neighbourhoods

```text
N_G(t)=N_G(d)={x,y,u_t,p,q}=Q_t.
```

Deleting `Q_t` leaves exactly `C,{t},{d}`.  The pair `(Q_t,C)` is another
minimum-order high-lobe instance of the proved two-singleton
classification, so its boundary is `P_3` disjoint union `K_2`.  The
already forced edges orient it uniquely as

```text
G[Q_t]=(x-u_t-y) disjoint union (p-q).
```

The two singleton excesses are one, and the five-cut excess sum is
`13-3=10`; consequently `delta_Q_t(C)=8`.  This is indeed a same-order
reorientation, not a descent.

If `td` is an edge, then `d` is one of `x,y,u_t`.  Taking `d=x` or `d=y`
would put the other twin in `R`, and fullness of `{d}` to `R` would force
the forbidden edge `xy`.  Thus `d=u_t` and

```text
R={x,y,r}.
```

Fullness gives `u_tr`.  The remaining triangle contacts of `u_t` number

```text
beta=|N_G(u_t) intersect {p,q}| in {1,2}.
```

Write `alpha=|N_G(r) intersect {p,q}|` and let `sigma` indicate
`r in S`.  The vertex `r` is either in `S`, when it has both edges to
`x,y`, or in `A`, when it has neither.  There are no other possible edges
inside

```text
L={p,t,q,x,y,r}.
```

Its edges are therefore exactly the three triangle edges, `tx,ty`, the
`alpha` edges from `r` to `{p,q}`, and the `2 sigma` twin incidences.  This
checks

```text
|E(G[L])|=5+alpha+2 sigma.
```

The singleton `u_t` has precisely the four incidences to `t,x,y,r` and
the `beta` incidences to `{p,q}`, so `eta_L({u_t})=beta`.  The exact
six-cut identity then gives

```text
eta_L(C)=17-|E(G[L])|-beta
        =12-alpha-2 sigma-beta.
```

Because `C` misses `t`, this is also its excess behind the exact five-cut
`L-{t}`.  It is a high component of the globally minimum order `a`, so
the maximum-excess tie-break against `delta_S(A)=8` yields precisely

```text
alpha+2 sigma+beta>=4.
```

Thus both cases in Theorem 5 are exhaustive, and every asserted edge and
excess identity is exact.

## 7. Dependencies and remaining scope

The source revisions checked were:

```text
singleton-triangle contraction:
52e321c3c46a267663de3584d1a628f8a3c9044369071328f619df704129d242

singleton endpoint and refined lobe choice:
63e9087752b66a0334d28ea555e40dbde9a7f4dad60d016c04329470e89e9a3a

companion-cut refinement:
6acfe24187c99c5da3439e72ebdee4c72b32a38eeae0df08116689237d6bc22e

singleton-contraction theorem:
e4720b2641033396aabf333cc97d9f401df4577f8a6f337a44d7ca6aba0ac1c2

anchored order bound:
b22556c8dc6fa22bbd950d53356c6dc46826e755173ca4a36b3fb5425c0995d8

leaf-cut classification:
cd69a799e80385f0182b08eb6bed3d5e6954d3169ec8437378dfd1e490cb2edd

atomic six-boundary setup:
3f2084f172183f38b91aa5a9ef402d2c60095579dda915fa6fcadaabfe94edff

lifted-triangle contact barrier:
cf0fef6c5fb1824f08683bb7451745499dabce9fcd87702ce800d1046ad28d83
```

The high `t`-misser does not admit the connected-exterior swap used for
`p,q`; Theorem 5 instead gives the exact reorientation and edge-low-side
normal forms above.  Neither is claimed to be a strict descent.  A
six-full component also remains nonterminal: the cited barrier excludes a
contact-only implication but does not encode internal component structure.
The source correctly records these points as nonclosures and does not infer
`K_7^-`, `(E5)`, or the primary theorem from them.
