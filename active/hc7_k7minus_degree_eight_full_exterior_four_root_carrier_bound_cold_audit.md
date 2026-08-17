# Independent cold audit: full-exterior four-root carrier bound

**Verdict:** GREEN.

Audited source:

```text
eda80d79ddc7fd917a6e8fad38fd1ee3b1b0bb8b934812fbbb374383f5541e2a  active/hc7_k7minus_degree_eight_full_exterior_four_root_carrier_bound.md
```

The shortest-path enlargement of four disjoint carriers is valid: the
internal vertices of a shortest path between distinct contact components
meet no current carrier, and absorption preserves connectivity,
disjointness and all four root contacts.  A connected four-vertex contact
graph has a vertex with two neighbours, giving the stated relabelling.

I checked all seven branch sets in Theorem 1.  The bag
`{v,x,y,t_3}` is connected through `v`; `{t_4} union Q_0` is connected;
and all bags are disjoint.  The first bag sees the three boundary-bearing
bags through `v` and the last three carriers through `t_3`.  The next
three bags form a clique using the literal edge `t_1t_2` and the
`t_1,t_2` contacts of `Q_0`.  Every one of them sees each of the last
three carriers through its root, while the carrier contact graph misses at
most one of its three pairs.  The quotient therefore has at least twenty
of the twenty-one contacts, exactly as required for `K_7^-`.

When `alpha(G[J])<=3`, every one of the seventy four-subsets of the
eight-vertex boundary contains an edge.  Summing the capacity-three bound
and reversing incidences gives
`sum_c binom(a(c),4)<=3 binom(8,4)=210`.  Division by
`1,5,15,35,70` yields the displayed bounds `210,42,14,6,3`.

The proof uses no edge between `v` and the exterior and no virtual
boundary edge.  Its application to the connected full exterior of the
critical degree-eight centre therefore has exactly the stated scope.
`git diff --check` passes.
