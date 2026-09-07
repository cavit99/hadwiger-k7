# Two insufficient induction hypotheses for the companion target

**Status:** explicit counterexamples with written proofs. The adjacent audit
records its separate internal verdict at an exact source hash.
Neither construction refutes Conjecture 19, Conjecture 21 or HC7.
Write `Q=K_7^=` for the complete seven-vertex graph minus two independent
edges. All minor exclusions below allow arbitrary connected branch sets.

## 1. Density without connectivity does not force the target

**Refuted assertion.** Every `Q`-minor-free graph with no literal
`K_5^-` has fewer than `4n` edges.

For each `k>=16`, join an independent four-set `A` to `k` disjoint
edges. The resulting graph has

```text
n=2k+4,    e=9k>=4n,    delta=5,    kappa=4.
```

A five-set with `r` vertices in `A` spans at most
`r(5-r)+floor((5-r)/2)<=7` edges, so contains no `K_5^-`.
In any proposed seven-bag model at most four bags meet `A`. At least
three bags therefore lie entirely in the matching. Such connected bags
have at most one pairwise contact among any three: each is contained in
one matching edge, which cannot accommodate three nonempty disjoint bags.
But every three vertices of `Q` span at least two edges. Thus the graph
has no `Q` minor, independently of the choice of model.

The first false inference was replacing the critical host by a merely
dense graph with the two exclusions. Its minimum-degree-eight and
seven-connectivity hypotheses are absent from this family; retaining
either is not refuted here.

## 2. Local exclusions do not ensure a degree-preserving contraction

**Refuted assertion.** Seven-connectivity, minimum degree eight, literal
`K_5^-` exclusion and neighbourhood independence number at most three
ensure an edge whose contraction retains minimum degree eight.

Let `H=K_3 square K_4 square K_4`: vertices are triples, with two
adjacent exactly when they differ in one coordinate. Every vertex has
degree eight and its neighbourhood is `K_2 dot-union K_3 dot-union K_3`.
Thus every neighbourhood has independence number three and contains no
diamond. A literal `K_5^-` would put a diamond in a universal vertex's
neighbourhood, so none exists.

Here is an elementary connectivity check. In `K_4 square K_4`, a
component separated from another surviving vertex uses `r` rows and `c`
columns with `1<=r,c<=3`. All cells in those rows outside those columns,
and in those columns outside those rows, must have been deleted. There
are `r(4-c)+c(4-r)>=6` such cells. Consequently five deletions leave each
such layer connected. After at most seven deletions from `H`, at most
one of its three layers has lost six or more vertices. The other layers
are connected and their matching edges still link them. A surviving
vertex in the remaining layer has a neighbour in a good layer, since
at most one deletion lies outside its layer. Hence `H` is eight-connected.

Every edge belongs to a coordinate triangle. Its third vertex has degree
eight and loses one neighbour on contraction, becoming degree seven.
Thus no edge has the proposed degree-preserving property.

**Unaffected scope.** This graph contains a `K_7` minor. In a
`K_4 square K_4` layer take one column's four vertices as singleton bags
and the other three whole columns as three bags. All seven bags are
connected, disjoint and pairwise adjacent. The target-free hypothesis
therefore remains a possible source of a terminal construction when
degree-preserving contraction fails. The first unsupported induction
step is dropping that hypothesis, or claiming that a quotient remains
in the minimum-degree-eight class merely because its order decreases.
