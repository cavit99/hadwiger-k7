# Author-side audit: full-exterior four-root carrier packing

**Verdict:** **GREEN** for the theorem at SHA-256

```text
eda80d79ddc7fd917a6e8fad38fd1ee3b1b0bb8b934812fbbb374383f5541e2a.
```

This is an adversarial self-audit, not an independent or external review.

## Carrier connection and labels

The shortest-path enlargement is valid even when a path meets a carrier in
a third contact component: the initial or final subpath would otherwise be
a shorter path between two contact components.  Hence its internal
vertices avoid all current carriers.  Absorption preserves disjointness,
connectedness and all four root contacts, and strictly reduces the number
of contact components.

In the resulting connected four-vertex contact graph, a vertex of degree
at least two and two of its neighbours can be labelled
`Q_1,Q_2,Q_3`; the remaining carrier is `Q_0`.  This supplies the two
carrier--carrier edges required in the last row of the model and assumes
no third such edge.

## The seven bags

The bags in (1) are disjoint because the four carriers lie in `C`, the six
used boundary roots are distinct, and `v` lies outside both sets.  The bag
`{v,x,y,t_3}` is a connected star and `{t_4} union Q_0` is connected by
the carrier contact at `t_4`.

All twenty-one contacts have literal sources:

- the first bag meets `{t_1},{t_2},{t_4} union Q_0` through `v` and meets
  `Q_1,Q_2,Q_3` through `t_3`;
- the three boundary-bearing bags form a clique through `t_1t_2` and the
  `t_1-Q_0,t_2-Q_0` contacts;
- each boundary-bearing bag meets every last carrier through its root in
  `T`; and
- at least two of the last three carrier pairs are edges of their contact
  graph.

Thus twenty contacts are guaranteed and at most one is absent.  The two
unused vertices of the eight-set `J` cause no problem because a minor model
need not span the host.  No edge from `v` to `C` or between distinct open
shores is used.

The same construction at a six-vertex boundary has an independent cold
audit at SHA-256
`b4f50b6e48c2ed3d4cee75995138c76964b6a99884c75c719da046929485a30a`;
the frozen six-boundary source is
`49f2056d05c2c9550dbfdbc3429fc09ed55da0e5acbba2209ecc153b7b8a851f`.

## Incidence count and scope

Independence number at most three makes every one of the seventy four-sets
edge-containing.  Four common neighbours would be four singleton carriers,
so each four-set has at most three common neighbours in `C`.  Double
counting gives exactly `70*3=210`.  The thresholds in (3) are the floors of
`210/binom(k,4)` for `k=4,5,6,7,8`, namely `210,42,14,6,3`.

The sum contains no contribution from a vertex with at most three boundary
neighbours.  The source therefore correctly makes no order, internal-edge,
or full-exterior elimination claim.  No branch-set, quantifier or counting
defect was found.
