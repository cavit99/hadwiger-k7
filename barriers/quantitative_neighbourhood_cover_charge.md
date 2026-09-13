# Maximum stars do not control neighbourhood-cover drift

**Status:** explicit counterexample to a uniform charge for arbitrary
maximum-star choices. This does not refute reduction R or a globally chosen
sequence of chromatic-preserving contractions.

For a graph F, write `tau_F(z)=d_F(z)-alpha(F[N_F(z)])`. The refuted claim
is that an absolute C bounds the total positive change of tau at surviving
singleton vertices by `Cr` times the order loss whenever a star with a
maximum independent neighbourhood is contracted in the small-order,
all-minor independence class. The example also defeats that bound for the
increase in the sum of tau over all vertices.

## Construction and class membership

For an integer `m>=1`, let H have distinct vertices

```text
u, a, b, x_1, y_1, ..., x_m, y_m
```

and exactly the edges `ua, ub, ax_i, x_i y_i, y_i b`, for `1<=i<=m`.
Put `n=2m+3` and `r=ceil(n^(2/3))`. Then `r>=3` and `n<=r^(3/2)`.

A width-two tree decomposition has central bag `{a,b,u}`, joined to
`{a,b,x_i}` for each i, with `{b,x_i,y_i}` attached to that bag. These
bags cover every edge and satisfy the connectedness condition for every
vertex. Deletion preserves such a decomposition; contracting an edge
replaces its two labels by one, whose bag subtrees remain connected because
some bag contained both endpoints. Thus every minor still has width at most
two. Removing a vertex confined to a leaf bag gives a vertex of degree at
most two, after redundant bags are discarded; induction gives a proper
three-colouring. Consequently every minor F satisfies
`alpha(F)>=|F|/3>=|F|/r`. The cycle `u,a,x_1,y_1,b,u` shows `chi(H)=3`.

## The failed charge and an alternative choice

The entire neighbourhood `S=N_H(u)={a,b}` is independent, hence maximum.
Contract `B={u,a,b}` to w. The quotient has exactly the m triangles
`w,x_i,y_i`, sharing only w, and the order loss is two.

H is triangle-free, so every original neighbourhood is independent and
every original tau is zero. In the quotient, each x_i and y_i has two
adjacent neighbours, giving tau one. The neighbourhood of w is a matching
of m edges, giving tau m. Hence the total positive singleton drift is
`2m`, and the increase in the sum over all vertices is `3m`.
Since `m/r` is unbounded, neither is bounded by `Cr` times the loss two
for an absolute C.

The same host admits a much larger maximum star: centre a and all its
neighbours `{u,x_1,...,x_m}` as independent leaves. It removes `m+1`
vertices. Its quotient has triangles `w,b,y_i`, so retains chromatic
number three. The obstruction therefore concerns arbitrary choices, not
the existence of a favourable choice.

The examples have no chromatic gap above r and do not satisfy R's critical
high-chromatic hypotheses. They also fail the positive low-tau threshold
needed for the proposed chromatic-preserving repair operation. What remains
possible is a global choice or exchange using those additional hypotheses;
maximum leaves and the all-minor independence bound alone do not prove it.
