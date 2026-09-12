# Independence resilience obstructs a uniformly cheap contraction

**Status:** written counterexample; a separate internal audit accompanies this source.
All graphs are finite and simple. Contractions are simplified, and `h(G)`
denotes the largest order of a complete minor. No computation is a premise.

**Theorem.** For every constant `D>0` there are an integer `r>=2` and a
connected noncomplete graph G such that

```text
|G| <= r^(3/2),
alpha(F) >= |F|/r for every minor F of G,
```

but every nonempty connected set B with `alpha(G/B)<alpha(G)` satisfies
`e(G)-e(G/B)>Dr^2`. In the family below the loss is uniformly
`Omega(r^2 log r)`. Moreover `chi(G)=o(r)`.

## Probability input and parameters

We use [Janson--Warnke, arXiv:1406.1248v1, p. 1, equation (2)](https://arxiv.org/pdf/1406.1248v1),
whose primary statement was inspected on 12 September 2026. For containment
indicators in independent ground elements, put `X=sum I_A`, `mu=E X`, and
let Delta sum `E(I_A I_B)` over **ordered distinct** pairs with overlapping
ground sets. Its `epsilon=1` case gives

```text
P(X=0) <= exp(-mu^2/(mu+Delta)).
```

We take independent nonedges as the ground elements. The inequality has
no fixed-size restriction on the sets indexing the indicators.
All asymptotics below are as the integer `k>=3` tends to infinity. Set

```text
n = ceil((k! 2^(k(k-1)/2))^(1/(k-3/2))),
m = ceil(99n/100),       G0 ~ G(n,1/2),
mu_M = binom(M,k) 2^(-k(k-1)/2).
```

Stirling's formula and `k^2/n=o(1)` give

```text
n/(k 2^(k/2)) -> 2^(1/4)/e,
mu_n = (1+o(1)) n^(3/2),        2^(-k) = Theta(k^2/n^2),
mu_m = n^(3/2 + 2 log_2(99/100) + o(1)) >= n^(7/5).
```

The expected number of independent `(k+1)`-sets is
`mu_n (n-k) 2^(-k)/(k+1)=Theta(k sqrt(n))`. Markov's inequality therefore
puts their number at most `n^(3/4)` with probability tending to one.

## A uniform independent-set estimate

Fix a set U of size m, and count its independent k-sets. Two indicators
depend on common ground elements exactly when their vertex sets overlap
in at least two vertices. For overlap `2<=j<=k-1`, the exact contribution is

```text
Delta_j/mu_m^2
 = binom(k,j) binom(m-k,k-j) 2^(j(j-1)/2) / binom(m,k).
```

For `2<=j<=floor(k/2)` this is at most

```text
A_j = (k^2/(m-k))^j 2^(j(j-1)/2).
```

Indeed, the overlap probability is at most
`binom(k,j) (k)_j/(m)_j <= (k^2/(m-k))^j`.
The logarithm of A_j is convex in j. Its first endpoint is
`A_2=O(k^4/n^2)` and its endpoint nearest `k/2` is
`exp(-Omega(k^2))`, using `log_2 n=k/2+O(log k)`.
This half of the sum is consequently `O(k^5/n^2)`.

For `j>k/2`, write `s=k-j`. The exact ratio is

```text
mu_m^(-1) binom(k,s) binom(m-k,s) 2^(-ks+s(s+1)/2)
 <= mu_m^(-1) Q_s,
Q_s = (km)^s 2^(-ks+s(s+1)/2).
```

Again the logarithm is convex. Here `Q_1=O(k^3/n)`, while the endpoint
nearest `k/2` is `exp(-Omega(k^2))`. Thus

```text
Delta/mu_m^2 = O(k^5/n^2 + k^4/(n mu_m)),
Delta/mu_m = O(mu_m k^5/n^2 + k^4/n) = o(1).
```

Janson's inequality gives `P(X_U=0)<=exp(-mu_m/2)` for sufficiently
large k. A union bound over at most `2^n` choices proves that, with
probability tending to one, **every subset of at least m vertices
contains an independent k-set**.

We also record a smaller-set version to control chromatic number. Put
`m0=ceil(sqrt(n))` and `s0=floor((log_2 n)/2)`.
For independent s0-sets in a fixed m0-set, their expectation nu satisfies
`nu>=m0^3`. The same A_j estimate now applies over the entire overlap
range: `s0~log_2 m0`, so its last endpoint is
`exp(-Omega(s0^2))`. Consequently
`Delta/nu^2=O(s0^5/m0^2)`, and the failure probability is at most
`exp(-Omega(m0^2/s0^5))`. Since
`binom(n,m0)<=exp(O(sqrt(n) log n))`, another union bound proves that
every subset of at least m0 vertices contains an independent s0-set.

## Other simultaneous properties

For `X~Bin(N,p)`, exponential Markov gives
`P(X<=Np/2)<=2^(Np/2) E[2^(-X)]
=2^(Np/2)(1-p/2)^N<=exp(-pN/8)`.
Every pair of vertices of G0 has a binomial `Bin(n-2,1/4)` common-neighbour
count. Thus a union bound shows that, with probability tending to one,
every pair has at least `(n-2)/8` common neighbours.
Also every set B of size at least `n/200` satisfies

```text
e(G0[B]) >= |B|(|B|-1)/8.
```

For each B this is half the expected edge count; the failure probability
is `exp(-Omega(|B|^2))`. Summing over at most `2^n` sets proves the assertion.

Put `t=ceil(4n/sqrt(log_2 n))`. We show `h(G0)<t` with probability
tending to one, allowing arbitrary branch sets. Among t disjoint
nonempty bags, at least `floor(t/2)` have size at most `2n/t`.
For a fixed assignment of vertices to the bags or to an unused class,
the contact events between these small bags use disjoint sets of edges
and are independent. Each contact fails with probability at least

```text
2^(-4n^2/t^2) >= n^(-1/4).
```

Ignoring internal connectivity only increases the probability of a model.
There are at most `(t+1)^n<=(n+1)^n` assignments, so

```text
P(h(G0)>=t)
 <= exp(n log(n+1) - Omega(n^(7/4)/log n)) = o(1).
```

All the preceding properties hold simultaneously with probability tending
to one. Fix such a graph G0. Delete one chosen vertex from each of its
independent `(k+1)`-sets, and call the resulting graph G. The deleted union
has size at most `n^(3/4)`. Thus `|G|>=n-n^(3/4)>=m`, and the large-set
property gives `alpha(G)=k`. Every pair of surviving vertices still has
a common neighbour, so G is connected; `k>=3` makes it noncomplete.

## All minors and every eligible contraction

For completeness, every nonempty graph H satisfies
`|H|<=h(H)(2 alpha(H)-1)`. Here is a short proof by induction on order.
In a connected H, grow a connected dominating set C from one vertex by
repeatedly adding a path of length two from C to a vertex at distance two.
The second added vertices, together with the initial vertex, are independent.
Hence `|C|<=2 alpha(H)-1`. If H-C is nonempty, C can be added to any
complete minor there as a universal bag. Induction gives

```text
h(H) >= 1 + h(H-C)
     >= 1 + (|H|-|C|)/(2 alpha(H-C)-1)
     >= |H|/(2 alpha(H)-1).
```

If H-C is empty the bound is immediate. For disconnected H, sum the
inductive bounds on its components and use their largest Hadwiger number;
the sum of their `2 alpha-1` terms is at most `2 alpha(H)-1`.

Set `r=2t`. For every nonempty minor F of G, minor monotonicity and the
preceding inequality yield

```text
alpha(F) >= |F|/(2 h(F)) >= |F|/(2t) = |F|/r.
```

The empty minor satisfies the assertion too. Moreover
`|G|<=n<=r^(3/2)` for sufficiently large k.

Now let B be any nonempty connected set with `alpha(G/B)<k`.
The induced graph G-B is a subgraph of G/B. If `|G-B|>=m`, the uniform
large-set property would give an independent k-set there. Therefore

```text
|B| > |G|-m >= n/200
```

for sufficiently large k. This conclusion includes clique bags and
does not require any choice or minimality of B. Exact simplification gives

```text
e(G)-e(G/B)
 = e(G[B]) + sum_(z outside B) max(0, |N(z) intersect B|-1)
 >= e(G[B]) >= |B|(|B|-1)/8 = Omega(n^2).
```

Since `r^2=Theta(n^2/log n)` and `log r~log n`, the lower bound is
`Omega(r^2 log r)`, uniformly over every eligible B. Taking k sufficiently
large proves the theorem for any prescribed D. If a deterministic choice
is desired, take the first labelled G0 satisfying the displayed properties
and always select the first vertex of each independent `(k+1)`-set.

## Scope

The smaller-set property permits greedy removal of independent s0-sets
until fewer than m0 vertices remain, then singleton colour classes. Thus
`chi(G)<=n/s0+m0=O(n/log n)=o(r)`. This family fails the high-chromatic
premise `q>=Kr` of the critical reduction R, for every fixed `K>0`.

It also satisfies `e(G)<=r^2 alpha(G)` for large k: the right side is
`(128+o(1))n^2`, while `e(G)<=n^2/2`. Thus this counterexample refutes
the absolute cost per independence-decreasing contraction, not the density
inequality, critical reduction R, proposed improved colouring bound, C19
or HC7. An edge-loss allowance proportional to the actual independence
decrease is not refuted: contracting all of G loses `O(n^2)` edges and
lowers independence number by `k-1=Theta(log n)`.
