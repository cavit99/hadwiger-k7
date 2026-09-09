# A barrier to density extraction with bounded branch sets

**Status:** written counterexample with a separate internal audit.
It refutes the bounded-branch-set formulation below, including its
small-order restriction. It does not refute the density conjecture
`e(G) <= C h(G)^2 alpha(G)`, the critical star-contraction target, or HC7.

For an integer `b>=1`, let `k_b(G)` be the maximum of `|J|/alpha(J)` over
nonempty minors J having a model in G whose every branch set has at most
b vertices. Put `t(G)=sqrt(e(G)/alpha(G))`.

**Claim.** For every fixed b there are finite graphs G with `t(G)`
arbitrarily large, `|G| <= t(G) ln t(G)`, and `k_b(G)/t(G)` arbitrarily
small. These also satisfy `|G|<=t(G)^(3/2)` for large t. Thus no
absolute positive c guarantees a minor of independence
ratio at least `c t(G)` using branch sets of any fixed bounded size.

In particular, for a matching M delete unmatched vertices and contract
its edges. The quotient has independence number `nu_s(M)`, the maximum
number of pairwise anticomplete edges in M. Its bags have size two, so
the claim refutes `|M|/nu_s(M)>=c sqrt(e(G)/alpha(G))` for every constant
c, even with the stated order restriction.

## 1. An elementary triangle-free independence bound

If Q is triangle-free and has maximum degree at most `D>=16`, then

```text
alpha(Q) >= |Q| log_2(D)/(16D).                         (1)
```

Choose an independent set I uniformly among all independent sets of Q.
For a vertex u, condition on I outside its closed neighbourhood. Its
neighbours form an independent set. Let Z be the number of neighbours
not forbidden by the conditioned vertices. The remaining possibilities
are `{u}` or an arbitrary subset of these Z neighbours, so conditionally

```text
Pr(u in I) = 1/(1+2^Z),
E |I intersect N(u)| = Z 2^(Z-1)/(1+2^Z).
```

If `Z <= (log_2 D)/2`, the first quantity is at least
`1/(1+sqrt(D)) >= log_2(D)/(8D)`. Here `sqrt(D)>=log_2(D)` for `D>=16`
justifies the last inequality. Otherwise the second quantity divided by
D is greater than `log_2(D)/(8D)`, since `2^Z/(1+2^Z)>=1/2`.
Average and sum `Pr(u in I)+D^(-1) E|I intersect N(u)|` over u.
This sum is at most `2 E|I|`, because every vertex has degree at most D.
This proves (1).

## 2. Sparse graphs of prescribed girth

Fix b. For every sufficiently large integer d there is a graph B
satisfying, with `N=d^(3b+4)`,

```text
|B| <= N,  Delta(B) <= 2d,  girth(B) > 3b,
e(B) >= Nd/4,  alpha(B) <= 5N ln(d)/d.                (2)
```

To prove existence, choose the binomial random graph X on N vertices,
with edge probability `d/N`. Its edge count is at least `Nd/3` with
probability tending to one, by the elementary binomial variance bound.
For `a=ceil(4N ln(d)/d)`, the expected number of independent a-sets is at
most

```text
(eN/a)^a exp(-d a(a-1)/(2N)) = o(1).
```

Indeed, its logarithm divided by a is at most
`ln(ed/(4 ln d))-2 ln d+o(1)`, which tends to minus infinity.
Thus `alpha(X)<a<=5N ln(d)/d` with probability tending to one.

Let T be the sum of the degrees of vertices of degree greater than 2d.
For `Y~Bin(N-1,d/N)`, the identity

```text
E[Y 1_(Y>2d)]
 = (N-1)(d/N) Pr(Bin(N-2,d/N)>=2d)
 <= d (e/4)^d
```

follows from the binomial moment-generating-function bound at parameter
`ln 2`. Hence `E T <= Nd(e/4)^d`, and Markov's inequality gives
`T<=Nd/24` with probability tending to one. The expected number of
cycles of lengths three through 3b is at most
`sum_(j=3)^(3b) d^j/(2j) <= d^(3b)` for large d. Thus there are at most
`d^(3b+1)` such cycles with probability tending to one. These four
events hold simultaneously for some X.

Delete every vertex of degree greater than 2d; this removes at most T
edges. From what remains, delete one vertex from every surviving cycle
of length at most 3b. At most `d^(3b+1)` vertices are deleted in this
second step, removing at most `2d^(3b+2)` further edges. For large d,
this is at most `Nd/24`, so the remaining B has at least `Nd/4` edges.
Its other properties in (2) follow immediately. For a deterministic family,
choose the first labelled graph of order at most N satisfying (2), in
order of vertex count and then adjacency string. The proof above ensures
that this finite search succeeds; no running-time bound is claimed.

## 3. All bounded branch-set models after a clique blow-up

For a positive integer s, replace every vertex of B by an s-clique,
with complete joins exactly along the edges of B. Denote the resulting
graph by `G_s=B[K_s]`. Then

```text
|G_s|=s|B|,
alpha(G_s)=alpha(B),
e(G_s)>=s^2 e(B),
t(G_s)>=sd/sqrt(20 ln d).                            (3)
```

Fix ANY model with k disjoint nonempty connected branch sets in G_s,
each of size at most b. Let J be its full contact graph, retaining every
edge between the bags. Edge deletions only increase independence
number, so it suffices to bound `k/alpha(J)` for these full contact
graphs.

Project each bag onto the base vertices whose cliques it meets. Its
support is connected in B and has at most b vertices. At any base
vertex, at most s bag supports occur, since the original bags are
disjoint. Hence each support conflicts, by overlap, with at most
`b(s-1)` other supports. Greedy colouring partitions the supports into
at most `b(s-1)+1<=bs` classes whose supports are pairwise disjoint.
For b=2 this also handles matching edges within a clique: their
projected supports are singleton loops, not ordinary edges of B.

For one class, the corresponding induced subgraph of J is the contact
graph of its disjoint connected supports in B. Its maximum degree is
at most `b Delta(B)<=2bd`. It is triangle-free: three pairwise adjacent
supports would give three cross-edges; inside each support, join their
incidences by a simple path of length at most `b-1`, using a length-zero
path when they coincide. Their union is a cycle in B of length at most
3b, contradicting its girth. Supports are disjoint, so the cycle has no
repeated vertices apart from its initial/final vertex.

A largest class has at least `k/(bs)` supports. Apply (1) to its contact
graph with `D=2bd`. Its independent set is also independent in J, giving

```text
alpha(J) >= k log_2(2bd)/(32 b^2 s d),
k_b(G_s) <= 32 b^2 s d/log_2(2bd).                   (4)
```

These bounds hold for every such model. Combining (3) and (4) yields,
for each fixed b,

```text
k_b(G_s)/t(G_s) <= 32 b^2 sqrt(20 ln d)/log_2(2bd) -> 0.
```

Finally choose the integer `s=2^(2N)`. For large d, (3) gives `t(G_s)>=s`,
and therefore

```text
ln t(G_s) >= ln s = 2N ln 2 >= N,
|G_s| <= sN <= t(G_s) ln t(G_s).
```

Also `ln t<=sqrt(t)` for sufficiently large t, giving the stated
power bound. This proves the claim.

## Scope

The obstruction concerns density extraction through minor models with
a fixed bound on branch-set size. It leaves unbounded connected bags
available. No upper bound on the Hadwiger number of these graphs is
asserted, and no violation of `e<=C h^2 alpha` is established. The
proof supplies neither the minor-critical chromatic hypotheses nor the
density surplus `e >> r^2 alpha` required by the quantitative
star-contraction campaign. The argument is an existence proof, not a
finite computation. Its only probabilistic ingredients were proved or
displayed above; no external triangle-free independence theorem or
random-regular existence theorem is needed.
