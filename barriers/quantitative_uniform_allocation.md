# Fixed uniform capacities can be diluted

**Written counterexample; separate internal audit accompanies this source.**
The failure concerns the
proposed allocation, including capacities computed separately for each
original connected component. It does not refute density surplus extraction.

**Claim refuted.** Let `r>=2` be an integer, `n=|G|<=r^(3/2)` and
`b=r^2 alpha(G)/n`. Suppose every minor of G has independence ratio at
most r. In every retained history of minimum-codegree edge contractions
and retirements of degree at most r, allocate merge demand
`max(0,c+1-b)` to original vertices in the two private-neighbour preimages,
with total capacity b per original vertex.

This allocation can fail even when G is connected. It still fails if both
child preimages are added to each merge's eligible vertices. Replacing b
by any fixed constant multiple in both demands and capacities does not
repair it.

## Closure under a one-vertex sum

For integer r, the property `|J|<=r alpha(J)` for every induced subgraph J
is closed under gluing graphs at one common vertex x. To see this, it is
enough to check a subgraph containing x. Let its components after deleting
x have orders `n_i` and independence numbers `a_i`. Each lies in one of the
original pieces, so `n_i<=r a_i`. If
`1+sum n_i>r alpha(J)`, then `alpha(J)>=sum a_i` forces every nonnegative
integer `r a_i-n_i` to be zero. Applied to each component together with x,
the original property now supplies an independent set of size `a_i+1`,
necessarily containing x. Their union has size `1+sum a_i`, contradicting
the assumed inequality. Subgraphs omitting x are disjoint unions.

Consequently the all-minor independence-ratio property is also closed under
one-vertex sums. A minor with no bag containing x is a disjoint union of
minors of the pieces with x removed. If one bag contains x, its intersection
with each piece is connected whenever nonempty: excursions outside the
piece can only return through x. Projecting this bag onto the pieces writes
the full contact graph as a one-vertex sum of minors of those pieces.
Deleting contacts can only increase independence number. These arguments
also justify disjoint unions.

## The connected construction

For arbitrarily large N choose a graph H on N vertices such that

```text
0.4N <= d_H(u) <= 0.6N,
0.2N <= |N_H(u) intersect N_H(v)| <= 0.3N  (u != v),
alpha(H) <= 3 log_2 N,
h(H) < t = ceil(4N/sqrt(log_2 N)).
```

Such graphs exist. In `G(N,1/2)`, the degree and common-neighbour conditions
hold simultaneously by binomial tail bounds and a union bound over pairs.
The expected number of independent `ceil(3 log_2 N)`-sets tends to zero.
For the last condition, among t disjoint bags at least `floor(t/2)` have
size at most `2N/t`. Each pair of these small bags fails to touch with
probability at least `2^(-4N^2/t^2)>=N^(-1/4)`. Their contact events are
independent for a fixed assignment. Taking the union over at most
`(t+1)^N` assignments gives probability at most
`exp(N log(N+1)-Omega(N^(7/4)/log N))=o(1)` for a K_t model.
This is the same minor-model count as in the existing independence-cost
barrier; it permits arbitrary bags and ignores connectivity only to obtain
an upper bound.
For a deterministic family, take the first labelled H satisfying the
displayed properties; the probability argument guarantees its existence
for every sufficiently large N.

Add a universal vertex x to H. Put `r=2(t+1)`, and attach q copies of K_r
by identifying one vertex of each with x, where

```text
q = floor((r^(3/2)-N-1)/(r-1)).
```

Call the resulting connected graph G. Each attached clique otherwise has
its own vertices. Then

```text
n=N+1+q(r-1)<=r^(3/2),
alpha(G)=alpha(H)+q,
q~sqrt(r),     b=r^2 alpha(G)/n~r=o(N).
```

Also `e(G)=e(H)+N+q binom(r,2)`, so
`e(G)/(r^2 alpha(G))->1/2`. These graphs do not have density surplus
for any fixed `D>=1`.

Every minor of the core `H+x` has independence ratio at most r: its
Hadwiger number is at most `t+1`, and the independently proved bound
`|F|<=h(F)(2alpha(F)-1)` applies. Every minor of K_r has ratio at most r.
The one-vertex-sum argument therefore gives the required bound for every
minor of G. In particular no forest-antichain selection can succeed.

## A permissible history with an allocation deficit

First retire all vertices of the attached cliques except x. Each such
vertex has current degree at most `r-1`, so these retirements are allowed.
The active graph is now `H+x`. Contract minimum-codegree edges, considering
the first `L=floor(N/100)` contractions.

Throughout these L steps, the bag containing x remains a singleton. Indeed,
after j non-x contractions any core bag has degree at least `0.4N-j`.
Consequently any edge incident with x has codegree at least `0.4N-j-1`.
There are at least `N-2j` untouched H vertices. Each has at least
`0.4N-2j` neighbours among them, so some two are adjacent;
an edge between two such vertices has codegree at most `0.3N+j+1`.
The former bound is larger for `j<=L` and large N, so a minimum-codegree
edge avoids x. The same degree bound is greater than r, so no core
retirement is possible during this interval.

Every contracted edge in this interval has codegree at least `0.2N-2j`.
Choose one original edge between its two preimages. Of its original common
neighbours, at most j can have been absorbed into those two bags, and at
most j more are lost by identifying other bags. Thus each merge loses at
least `0.18N` edges. The L demands have total

```text
sum max(0,c+1-b) >= L(0.18N-b) = Omega(N^2).
```

Their eligible original vertices all belong to H. Retired vertices are
absent from the active quotient; x is adjacent to both endpoints and is
therefore never a private neighbour, and neither endpoint contains x.
This remains true when both endpoint preimages are eligible. Hence total
available capacity is at most `bN=o(N^2)`, a strict deficit. The same
argument permits any fixed constant multiple of b. Continue the history
to the empty graph in any permitted way; later steps cannot repair this
already deficient collection of merges.

The first invalid inference is that a deficit for uniform capacities forces
a successful forest selection. These connected hosts have a deficit and
no successful minor at all. Choosing budgets separately for original
connected components cannot repair the example. Recomputing or transferring
budgets after retirements, or choosing nonuniform capacities jointly with
the allocation, remains possible. So does a construction using the density
surplus itself. No such repair or existential choice of a successful
history is settled here.
