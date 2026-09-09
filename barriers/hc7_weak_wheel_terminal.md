# Two weaker wheel terminals fail

**Status:** explicit counterexamples, with a separate exact-source internal audit.
These refute abstract contact patterns, not the actual critical-host target.

Write `Q=K7-2K2`, with the omitted edges independent. The positive
[two-double-contact construction](../results/hc7_sealed_wheel_terminal.md)
specifies the nine-set pattern used in the first example.

## 2. One single-contact port does not suffice

Replace `qr,qt` by just `qt`. Use singleton sets and exactly the required
contacts, with wheel hub `v` and rim `p-b-q-c-p`. The edge `vq` is already
present. This nine-vertex graph has 23 edges; `b,c,q` have degree four, every
other vertex has degree at least five, and `bc` is absent. It has no `Q` minor.

Indeed, a seven-bag model requires exactly two vertex reductions. Any unused
vertex costs at least four edges, and the remaining reduction costs at least
one, leaving fewer than the 19 edges of `Q`. Thus all vertices are used.
A singleton of degree four cannot have the five contacts required in `Q`,
so all of `b,c,q` belong to non-singleton bags. If there is one three-vertex
bag, it is `{b,c,q}`: contraction loses its two internal edges, two duplicate
contacts to `v`, and one each to `p,d`, leaving 17 edges. Otherwise there are
two edge bags. By symmetry one is `{b,q}`, and the other is `{c,z}` for
`z` in `{p,d,v}`. Contracting `bq` loses two edges; the second contraction
loses three edges for `z=p,d`, and four for `z=v`. Again fewer than 19 remain.
These cases exhaust arbitrary connected branch sets, including root mergers.

## 3. A root port and a double-contact port do not suffice

Consider eight singleton vertices `v,s,q,b,c,u,t,d`. On the first five take
the wheel with hub `v` and rim `s-b-q-c-s`. Add the contacts

```
ut;  uv, us, uq, tv, ts, tq;
du, dt, dv, ds, db, dc.
```

The literal edge `vs` and also `vq` are present. Here `b,c` are nonadjacent
vertices of degree four, each with neighbourhood `{v,s,q,d}`. A seven-bag
`Q` model would use one edge contraction or one vertex deletion. A deletion
leaves at least one of `b,c` singleton with degree at most four. A contraction
can absorb both only if `bc` is an edge, which it is not. Hence no `Q` model
exists. This refutes the stated eight-set contact pattern, even with `vq`.

The two negative graphs refute only the corresponding abstract terminals.
Neither is an actual seven-connected, minimum-degree-eight critical host.
No claim is made that its remaining structure can realise either example.

## 4. Completing the wheel and exterior bag still fails

In the first pattern, add every missing edge on `{v,p,q,b,c,d}`, retaining
exactly the stated contacts to the triangle `{r,s,t}`. The completed graph
still has no Q minor. It is the union of a K6 on `{v,p,q,b,c,d}` and the
seven-vertex graph on `{v,p,q,d,r,s,t}`, intersecting in the literal K4
`{v,p,q,d}`. The latter graph has 18 edges: its only holes are `pt,qr,qs`.
Neither side has Q, the first by its order and the second by its edge count.

In the second pattern, complete `{v,s,q,b,c,d}` to K6, retaining exactly
the stated contacts to `{u,t}`. The completed graph is the union of two
K6 graphs, on `{v,s,q,b,c,d}` and `{v,s,q,d,u,t}`, intersecting in the
literal K4 `{v,s,q,d}`. Again neither side has Q.

For completeness, the following projection proves Q-exclusion in both
unions without an unexamined clique-sum theorem. Suppose two graphs
intersect in a clique K of order four, with no edges between their open
sides, and their union has a Q model. At most four bags meet K. Deleting
their corresponding Q vertices leaves a nonempty connected graph:
deleting at most four vertices from Q leaves at least three vertices,
and a complete graph minus a matching on at least three vertices is
connected. Each bag avoiding K lies wholly in one open side, so all
such bags lie in the same side. Retain that side together with K and
restrict every K-meeting bag to it. Each restricted bag is nonempty;
any pieces previously joined through the discarded side contain K
vertices and reconnect through literal clique edges. A lost contact
between two K-meeting bags is restored between their distinct K vertices.
Contacts involving a bag avoiding K already lie in the retained side.
The restricted bags therefore give Q in one original side, a contradiction.

Thus extra wheel diagonals, contacts from d to either port, or any other
edges confined to the six indicated vertices cannot repair these terminals.
No extra triangle contacts are allowed in these counterexamples. In the
actual application, a repair must use resources beyond extra edges in
this fixed six-bag core. Additional bags, changed triangle contacts,
or a construction inside or splitting the original preimages remain
possible; the unused separator edge is one available resource.
The actual seven-connected critical host remains outside their scope.
