# A wheel terminal with two double-contact ports

**Status:** written proof; a separate exact-source internal audit accompanies
this conditional construction. It does not close the actual critical-host case.

Write `Q = K_7 - 2K_2`, where the omitted edges are independent. All graphs
are finite and simple. Adjacent sets have an actual edge between them.

## 1. The positive terminal

Suppose nine nonempty, pairwise disjoint connected sets are labelled
`v,p,q,b,c,r,s,t,d`. The first five sets support a `W_4`, with arbitrary hub
and rim order. The remaining required contacts are

```
rs, rt, st;  vr, vs, vt;
dr, ds, dt, dv, db, dc;
pr, ps;  qr, qt.
```

Then their union contains a `Q` minor. Additional contacts are permitted.
This includes the variant `p -> {r,s}`, `q -> {s,t}`, by exchanging `r,s`.

The symmetries exchanging `b,c` and simultaneously exchanging `p,q` and
`s,t` give the following six orbits of the fifteen labelled wheels. A rim
word specifies its cyclic order. In every row contract the two displayed
edges and retain all other sets; the two possible holes are displayed.

| Hub | Rim | Orbit size | Contract | Possible holes |
| --- | --- | ---: | --- | --- |
| `v` | `p b q c` | 1 | `bd`, `cp` | `(c+p)t`, `qs` |
| `v` | `p b c q` | 2 | `bd`, `cq` | `(c+q)s`, `pt` |
| `p` | `v b q c` | 2 | `bd`, `cq` | `(c+q)s`, `pt` |
| `p` | `v c b q` | 4 | `bd`, `cp` | `(c+p)t`, `qs` |
| `b` | `v p c q` | 2 | `bd`, `cp` | `(c+p)t`, `qs` |
| `b` | `v c p q` | 4 | `bd`, `cp` | `(c+p)t`, `qs` |

Here `c+p` means the union of the original sets, joined by the displayed
wheel edge. The orbit count is complete: a hub `v` has two rim types; a hub
in either two-element pair has two types according as the other member of
that pair is adjacent or opposite to `v` on the rim.

There is also a direct check of all contacts. After the indicated symmetries,
the wheel has edges `vq,qb,pc`. Such a choice always exists: if `v` is the
hub, the rim has a matching between `{p,q}` and `{b,c}`; if a port is the hub,
retain that port as `q` and match the other port to a rim helper; if a helper
is the hub, the four-cycle on `v,p,q` and the other helper has disjoint edges
joining `v` and that helper to the two ports. Since every wheel vertex has
degree at least three, both `v` and `q` meet `{p,c}`. Consequently the seven
fixed preimages

```
d+b, p+c, v, q, r, s, t
```

are connected and pairwise disjoint, and every required `Q` contact is
present except possibly `(p+c)t` and `qs`. These holes are independent.
This proves the construction for arbitrary original connected sets, without
assuming any connectivity property of a quotient.

The [weaker contact patterns](../barriers/hc7_weak_wheel_terminal.md)
have explicit counterexamples. Both double-contact ports and the exterior
bag contacts are hypotheses of this construction.
