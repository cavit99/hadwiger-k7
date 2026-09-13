# Limits of an order-and-edge potential

**Status:** written proof of a scalar obstruction, with a
[separate GREEN internal audit](quantitative_order_edge_potential_audit.md).
No graph realisation is
asserted. This refutes the inference specified below, not the critical
reduction R in the [quantitative frontier](../active/quantitative_star_contraction_frontier.md).

## Exact scalar claim refuted

Consider integer sequences indexed by descending colour levels p, satisfying

```text
p <= n_p <= r^(3/2),       0 < m_p <= binom(n_p,2),
2m_p/n_p >= 2p-2r+1,
n_p-n_(p-1) >= m_p/r^2,   m_p-m_(p-1) >= m_p/r.
```

These inequalities alone do not imply any bound

`q^3/r^3 <= A + B log(n_q/r)`

with fixed positive constants A,B, even when they hold at every step from
q down to 2r and q/r tends to infinity. They also do not force the first
step to remove a fixed positive multiple of `n_q q^2/r^3` vertices.

## Integer construction

Let r tend to infinity through integers, use the natural logarithm, and set

```text
q = floor((r/2) sqrt(log r)),
n_q = 2 floor(r^(3/2)/2),
n_(p-1) = 2 floor(n_p(1-p/r^2)/2)       (p=q,...,2r+1),
m_p = n_p(p-r+1/2)                    (p=q,...,2r).
```

For sufficiently large r, `q>=2r+1` and `0<p/r^2<=1/2` throughout.
Every n_p is even, so every m_p is an integer. Writing
`D_p=n_p-n_(p-1)`, the rounding gives

`n_p p/r^2 <= D_p < n_p p/r^2+2`.

We first verify positivity and the order and edge capacities, so these
properties are not assumptions about the recurrence. Expanding it yields

`n_p >= n_q product_(j=p+1)^q(1-j/r^2)-2(q-p)`.

Since `log(1-x)>=-2x` for `0<=x<=1/2`, uniformly over these levels,

```text
product_(j=p+1)^q(1-j/r^2) >= exp(-q(q+1)/r^2)
                          = r^(-1/4-o(1)),
n_p >= (r^(3/2)-2)r^(-1/4-o(1))-2q
     = r^(5/4-o(1)) >> 2q.
```

Thus all n_p are positive, `p<=n_p<=n_q<=r^(3/2)`, and
`n_p>=2p-2r+2`. The last inequality is exactly the condition
`m_p<=binom(n_p,2)`. Moreover `m_p>0`, and the required density bound
holds at equality: `2m_p/n_p=2p-2r+1`.

## Both loss inequalities hold

The rounding bound immediately gives `D_p>=n_p p/r^2>=m_p/r^2`.
The exact edge-count difference is

`m_p-m_(p-1)=n_p+D_p(p-r-1/2)`.

Its coefficient of D_p is positive. Substituting the lower bound on D_p,
and subtracting `m_p/r`, gives a lower bound of

`(n_p/r^2)[p^2-2pr+2r^2-(p+r)/2]`.

The bracket increases with p for `p>=2r`; at `p=2r` it is
`2r^2-3r/2>0`. This proves the second loss inequality at every step.

## Failure of the proposed conclusions

Here `q^3/r^3 ~ (log r)^(3/2)/8`, whereas
`log(n_q/r) ~ (log r)/2`. Hence every fixed-constant cubic bound above
eventually fails. At the first step the rounding estimate also gives

`D_q/(n_q q^2/r^3) <= r/q + 2r^3/(n_q q^2) -> 0`.

These are integer order and edge counts only. No graphs, minor relations,
independent star packings, all-minor independence bounds or chromatic
criticality are certified. Actual graph structure may impose additional
constraints beyond these scalar inequalities. Consequently neither R nor
its intended colouring consequence is refuted. A proof through these
counts requires further information linking the contractions, their edge
losses and the degrees of the surviving vertices.
