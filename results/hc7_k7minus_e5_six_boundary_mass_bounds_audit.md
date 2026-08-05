# Internal audit: missed-root mass and both-endpoints boundary bounds

**Verdict:** **GREEN** for the pinned source revision.  This is a separate
internal mathematical audit, not external peer review.

## 1. Audited revision and imported endpoint

**Audited source:**
`results/hc7_k7minus_e5_six_boundary_mass_bounds.md`

**SHA-256:**

```text
3311e4640584e8223fc9c71c2cd22d7e06aabd7f65efa6ebd017fc1adc4d29e8
```

The imported second-contraction reduction was checked at SHA-256

```text
3218c292213fbf7e9cf6e7e6a38b2c3cef0c05801a4359cbd956a28daf3ef93e.
```

Its adjacent GREEN audit is pinned to that revision.  It supplies exactly
the hypotheses used here:

- `|V(G)|=a+7`, `|E(G)|=4|V(G)|-7` and `a>=8`;
- the three labelled six-boundary kernels and the opposite-shore orders
  `a-1` for `K_2` and `a-2` for `P_3,K_3`;
- the degree-five endpoint and its displayed fixed low-kernel neighbours;
- the universal high-excess conclusion for a five-cut and the minimum
  choice of the order `a`; and
- Proposition 5.2: every non-six-full opposite component misses one root
  and is either a full singleton or a full edge of order two.

The both-endpoints setting in Section 4 is also exactly the unclosed branch
of Section 4 of the imported reduction.  Its lifted boundary is
`R={u,d,v} union U`, where `|U|=3`, the three edges among `u,d,v` are
present, `u,d` have degree five, and each meets both open sides.

## 2. Missed-root mass

If `M_r` is nonempty, `Q_r=P-{r}` is a five-cut.  After deleting it, every
component missing `r` remains separate.  All other vertices form one
connected component through `r`: every boundary root has a neighbour in
the connected low kernel, a six-full component meets `r`, and every full
singleton or full edge missing a different root is adjacent to `r`.

This central component contains `r` and at least the two vertices of the
low kernel, so it has order at least three.  Since exactly `a+2` vertices
lie outside the five-cut, no component missing `r` has order at least `a`.
The universal five-cut theorem supplies a high-excess component, whose
order is at least `a` by the selected minimum-lobe choice.  It must be the
central component, leaving at most two vertices in all components missing
`r`.  Thus `sigma_r<=2`.  The source separately handles `M_r` empty, so it
does not apply the five-cut theorem to a non-cut.

## 3. Forced six-full component and multiplicity

Proposition 5.2 makes every vertex of a non-six-full component which does
not miss `u` adjacent to `u`; Theorem 2.1 bounds the total order of the
components which do miss `u` by two.  The fixed neighbours of the
degree-five endpoint number respectively three, four and two in the
`K_2`, favourable `P_3/K_3`, and other `P_3/K_3` cases.  The resulting
upper bounds on an all-non-six-full shore are `4`, `3` and `5`, strictly
below the imported shore orders `a-1>=7` and `a-2>=6`.

Hence a six-full component exists.  Distinct six-full components contain
distinct neighbours of `u`, so the same residual degree capacities give
the asserted upper bounds two, one and three.  No internal structure or
order bound for a six-full component is inferred.

## 4. Both-endpoints boundary

The six-set `R` has at most six edges inside `{v} union U`, the three
triangle edges `ud,uv,dv`, and at most one edge from each of `u,d` to
`U`.  The last bounds follow because each degree-five vertex already sees
the other two triangle vertices and both open sides.  Therefore

```text
|E(G[R])|<=6+3+1+1=11.
```

Equality forces `{v} union U` to induce `K_4` and both one-edge bounds to
be tight.  Each of `u,d` then has exactly two neighbours outside `R`, and
meeting both open sides places exactly one in each.

The components of `G-R` have total order `a+1`.  Partitioning all edges
between the boundary, the components and their interiors gives

```text
4a+21
 = |E(G[R])| + 4(a+1) + sum_K eta_R(K),
```

which is precisely `sum_K eta_R(K)=17-|E(G[R])|`.  The source correctly
restricts the literal `K_4` core to equality and leaves every boundary
with at most ten edges open.

## 5. Scope

The source proves three computation-free consequences only within the
selected minimum-`E5` kernel setting: aggregate missed-root mass at most
two, existence and multiplicity bounds for six-full components, and the
eleven-edge both-endpoints boundary bound with its exact excess identity.
It does not eliminate a large six-full component, the connected
one-six-full kernel rows, the self-similar quotient, or a both-endpoints
case with at most ten boundary edges.  It does not prove `(E5)` or the
principal seven-connected theorem.

There are no unresolved assumptions or gaps inside the statements actually
proved at the pinned source hash.
