# A three-part partition need not split every boundary neighbourhood

**Status:** explicit counterexample with a direct written check; no
separate internal audit. This refutes an intermediate construction, not
the critical-host target or HC7.

## Statement refuted

Suppose A is connected, contains a triangle P, and has a six-vertex
boundary T. Even if every nonempty proper U subset A has at least seven
outside neighbours, there need not be a partition of A into three
connected sets rooted at the three P vertices such that every t in T
has neighbours in at least two parts.

## Construction and check

Let A be the four-clique on `p1,p2,p3,x`, with `P={p1,p2,p3}`. Let
`T={t1,...,t6}` be independent, with precisely these A-neighbourhoods:

- `N_A(ti)={x,pi}` for i=1,2,3;
- `N_A(t4)=A`;
- `N_A(t5)=N_A(t6)=P`.

Every singleton in A has three A-neighbours and four T-neighbours.
A pair of P vertices has two outside A-neighbours and five T-neighbours;
a pair containing x has two outside A-neighbours and all six T-neighbours.
Every triple in A sees the remaining A vertex and all six T vertices.
Thus the required boundary bound holds for every nonempty proper U.

In any three-part P-rooted partition, x belongs to the part containing
some pi. Both neighbours of ti then lie in that part. This disproves
the proposed conclusion, independently of connectivity choices.

## Unaffected target

The required two-set construction does exist here: `{p1,x}` and
`{p2,p3}` are connected and share five T-neighbours. No opposite shore
or chromatic-critical host is specified. The example therefore does not
refute the [simultaneous two-set target](../active/hc7_split_clique_global_colour_lifts.md#the-simultaneous-construction-still-needed)
or imply failure of the complete six-cut case.
