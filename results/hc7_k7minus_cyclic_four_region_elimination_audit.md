# Internal audit: cyclic four-region elimination

**Verdict:** **GREEN.**

**Audited source:**
[`hc7_k7minus_cyclic_four_region_elimination.md`](hc7_k7minus_cyclic_four_region_elimination.md)

**Audited source SHA-256:**

```text
f5794395173655892c55c1d2965eb816e36c0532a493b4dc212f7734dcb16156
```

This hash identifies the exact revision checked.  The audit is a separate
internal mathematical audit, not external peer review.

## 1. Rooted triangle in the doubly replaced component

For distinct `u,v in W_P`, the simultaneous-replacement theorem gives the
exact boundary

```text
S_uv=(U-{u,v}) union T_P union {x,y}
```

and a connected `S_uv`-full component `R=P-{x,y}` with at least two
vertices.  Its opposite open side is nonempty.  Thus the closed-shore
rooted-connectivity lemma applies to every subset of `S_uv`, in particular
to `Q={x,y,r}` for either remaining centre `r`.  Consequently

```text
J=G[R union Q]
```

is internally three-connected relative to `Q`.

The proof correctly excludes the cutvertex obstruction to a `Q`-rooted
triangle.  If the obstruction vertex `z` were a root, connectedness of `R`
and fullness to the other two roots would put those roots in one component
of `J-z`, contrary to the obstruction.  Hence `z in R`.  Since `|R|>=2`,
some component `A` of `J-z` contains a vertex of `R-{z}`.  It contains at
most one root.  With `W=A cap Q`, the displayed sets

```text
X=(V(J)-A) union {z} union W,
Y=A union {z}
```

form a separation: their intersection is `{z} union W`, of order at most
two; `Q subseteq X`; and `Y-X=A-W` is nonempty.  No edge joins the open
sides because `A` is a component of `J-z`.  This contradicts internal
three-connectivity.  Lemma 2.1 therefore supplies three disjoint connected,
pairwise adjacent bags rooted at `x,y,r`.

## 2. Seven-bag model

Write `U={u,v,r,s}`.  Adding `u` to the `x`-bag and `v` to the `y`-bag is
legitimate through the literal edges `ux` and `vy`.  The three enlarged
bags remain disjoint and pairwise adjacent.  They contain the three centres
`u,v,r`, respectively, so each has an edge to every piece in
`mathcal P-{P}`.

The four outer piece bags are disjoint from the inner bags: their original
pieces are pairwise disjoint and avoid `P`, while the only centres used by
the inner bags are `u,v,r`.  Absorbing `s` into one outer piece preserves
disjointness and makes that bag connected and adjacent to the other three,
because every centre has a neighbour in every piece.

The case choices are exhaustive and give the claimed outer `K_4^-` model:

| interaction | base piece `P` | bag receiving `s` | other three bags |
|---|---|---|---|
| `C_4` | `C` | any region of `mathcal B` | `C_4` minus one vertex, hence `P_3` |
| `C_4` | a region of `mathcal B` | `C` | `C_4-P=P_3` |
| `P_4` | `C` | an endpoint region | `P_4` minus that endpoint, hence `P_3` |
| `P_4` | an endpoint region | `C` | `P_4-P=P_3` |

In each row the bag containing `s` is universal among the four outer bags,
and the other three induce a path.  Thus exactly one outer adjacency may be
missing.  The inner bags form a triangle and are complete to the outer
bags, so the seven bags form an explicit `K_7^-`-minor model.  No adjacency
between `x` and `y` is assumed or needed.

## 3. Counting consequences

The incidence inequality

```text
sum_P |W_P| >= 8
```

over five pieces guarantees a piece with at least two unique-centre
incidences.  Every possible base piece is covered by one of the first two
rows when `Gamma=C_4`, so that interaction graph is eliminated.

For `Gamma=P_4`, the last two rows show that `C` and both endpoint regions
have `|W_P|<=1`.  They contribute at most three incidences, leaving at least
five on the two internal regions.  Since each `W_P` is contained in the
four-set `U`, both internal sets are nonempty and one has order at least
three.  These deductions match Theorem 3.1 exactly.

## 4. Scope and unresolved cases

There is no unresolved assumption or proof gap in the stated theorem.  Its
scope is intentionally limited: it does not eliminate replacement squares
based at the two internal regions of `P_4`, does not treat `2K_2`, and does
not synchronize proper-minor colourings.  The proof uses only the audited
simultaneous-replacement/fullness conclusions, closed-shore rooted
connectivity, and the audited rooted-triangle obstruction; Proposition 6.1
of the Boolean edge-coupling theorem is not required.
