# Internal audit: high triangle-misser elimination

**Verdict:** **GREEN** for the pinned source revision.  This is a separate
internal mathematical audit, not external peer review.

**Audited source:**
`active/hc7_k7minus_e5_s3_high_misser_elimination.md`

**SHA-256:**
`6c881f87026f3116fa01749a1dc665dd93642a482a90ba37d404b83e2976db8e`

No mathematical correction is required at this revision.  The theorem is
computation-free.  Its conclusion is only the elimination of high
triangle-missing components in the selected exact `s=3` residue; it does
not eliminate the remaining six-full-component class or prove `(E5)`.

Relative to the originally audited revision
`038c6511515cfd6ec5c72451a8b017e6fcf74c457175eb4b69b09cca5702af69`,
the source change is status-only: it replaces the pending-audit wording by
a link to this adjacent audit.  The theorem statements, proofs,
dependencies, and mathematical endpoint are unchanged.

## 1. Global selection and the complement-excess identity

For any five-cut `Q`, exact `E5` accounting gives

```text
sum_D delta_Q(D)=13-|E(G[Q])|.
```

Consequently, for a nominated component `C`,

```text
Phi(Q,C)=delta_Q(C)+|E(G[Q])|
        =13-sum_{D != C} delta_Q(D).
```

The lexicographic choice which first minimises component order, then
maximises `Phi`, and finally minimises the number `rho` of opposite
components is therefore well-founded.  In the original two-singleton row,
the two singleton components each have excess one and the boundary has
three edges.  Hence

```text
delta_S(A)=8,                Phi(S,A)=11,             rho(S,A)=2.
```

The structural reductions invoked before the companion-cut comparison use
only minimum component order.  The only former maximum-excess comparisons
needed on the route used by the audited theorem occur in the companion-cut
and edge-atom terminal subcases, and Sections 2 and 3 below verify their
replacement.  The upper excess inequalities stated in the triangle-cut
refinement are not used in the new high-misser arguments; only its
minimum-order dichotomy, exact swaps, and normal forms are imported.

Thus the revised secondary coordinates are compatible with the precise
branch claimed in the source.  As the source correctly notes, this does
not install the revised choice in unrelated branches of the `E5`
programme.

## 2. Companion-cut replay

The structural companion-cut proof produces

```text
Sigma={b,c,q,x,y},          |E(G[Sigma])|=2,
```

with exactly two complementary components: a component `L` of order
`|A|` and a low edge.  Their excesses are nine and two.  Thus

```text
Phi(Sigma,L)=9+2=11=Phi(S,A),
rho(Sigma,L)=1<2=rho(S,A).
```

The candidate component has the same minimum order and excess at least
four.  The third coordinate of the revised selection therefore excludes
the four-separator normal form exactly as asserted.  No step producing
`Sigma` or classifying its two sides uses the former excess tie-break.

## 3. Edge-atom replay

For adhesion count `k=2`, the cited edge-atom proof directly gives the
degree-five singleton cut at `p`; no secondary choice is involved.

For `k=3`, the returned cut is

```text
Sigma={b,p,q,x,y},          |E(G[Sigma])|=3,
```

with a component `K` of order `|A|` and one low edge `L`.  When the
selected leaf is not in `L`, the explicit rooted six-bag construction in
the edge-atom proof gives `K_7^-` independently of any tie-break.  In the
remaining row `L={t,u_t}`, exact accounting gives

```text
delta_Sigma(L)=1+epsilon,
delta_Sigma(K)=9-epsilon.
```

If `epsilon=0`, then `Phi(Sigma,K)=9+3=12>11`.  If
`epsilon=1`, then `Phi(Sigma,K)=8+3=11` and
`rho(Sigma,K)=1<2`.  In both cases the component order is `|A|`, so the
revised selection supplies the required contradiction.  The edge atom
therefore still reduces precisely to the `k=2` singleton atom.

## 4. High misses at `p` and `q`

For a high component `C` missing `p`, the triangle-cut swap gives the
five-cut

```text
Q_p=R union {t,q}
```

with exactly the two components `C` and `{p,d}`.  The latter edge has
excess `k` in `{1,2}`.  The complement-excess identity therefore gives

```text
Phi(Q_p,C)=13-k.
```

For `k=1` this is twelve; for `k=2` it is eleven and the candidate has
only one opposite component.  Since `|C|=|A|`, the second or third
selection coordinate excludes both cases.  The `q`-misser swap has the
same hypotheses and arithmetic.

## 5. The adjacent high miss at `t`

In the adjacent normal form, `d=u_t`, `R={x,y,r}`, and

```text
beta=|N_G(u_t) intersect {p,q}| in {1,2}.
```

Deleting `Q_t=L-{t}` leaves exactly `C` and the edge `{t,u_t}`.  Its edge
count is one internal edge, four boundary incidences at `t`, and
`3+beta` incidences at `u_t`; hence its excess is exactly `beta`.
Accordingly

```text
Phi(Q_t,C)=13-beta.
```

The values `beta=1,2` are excluded respectively by larger `Phi` and by
equal `Phi` with `rho=1`.  Again the high component has order `|A|`.

## 6. The central `W`-cut

In the nonadjacent normal form, use the source notation

```text
S=(t-u-d) disjoint union (r-s),
P={p,q},                    X={x,y},
B=A-P,                      W=P union {u,r,s}.
```

The imported bound `|A|>=8` makes `B` nonempty.  The exact reorientation
has

```text
N_G(t)=N_G(d)=X union {u} union P,
```

and `x,y` have no neighbours in `A`.  Therefore every component `K` of
`G[B]` has all its external neighbours in `W`.  Vertices in
`X union {t,d}` survive deletion of that neighbourhood, so
five-connectivity forces

```text
N_G(K)=W.
```

Let `c` be the number of components of `G[B]` and
`m=|E_G(P,{r,s})|`.  Each of `p,q` has exactly the three fixed neighbours
consisting of its mate and `t,d`, and has no neighbour in `X union {u}`.
Its remaining two neighbours lie in `B union {r,s}`.  Fullness of each
`B`-component to `W` then gives

```text
c<=2,                       m<=4-2c.
```

After deleting `W`, the other component is

```text
D=G[X union {t,d}]=K_{2,2}.
```

It has four internal edges and twelve boundary incidences: six from
`x,y` to `u,r,s`, and six from `t,d` to `u,p,q`.  Thus

```text
delta_W(D)=4+12-16=0.
```

The only edges of `G[W]` are `pq`, `rs`, and the `m` edges between these
two pairs; the vertex `u` has no further edge in `W`.  Hence

```text
|E(G[W])|=2+m,
sum_{K in components of G[B]} delta_W(K)=11-m.
```

If `c=1`, then `m<=2` and the unique component has excess at least nine.
If `c=2`, then `m=0`, and one component has integer excess at least six.
Every such component has order at most

```text
|B|=|A|-2<|A|.
```

This contradicts the first coordinate of the global selection.  The
five-cut property, component list, edge count, and all inequalities in
the `W`-cut argument are therefore valid.

## 7. Conclusion

The three high-misser normal forms are exhausted: misses at `p` or `q`,
the adjacent miss at `t`, and the nonadjacent reorientation.  The
triangle-cut dichotomy then genuinely leaves a component adjacent to all
six vertices of the lifted cut.  No root-preserving model is inferred
from that contact, so the stated remaining obstruction and the theorem's
scope are accurate.
