# The order-seven `i=2` Hall return is terminal

**Status:** proved by a direct pole-and-tree completion with a fifteen-row
orbit table and independently cold-audited.  Neither the excess nor the
packet hypothesis is needed.

## 1. Normalised return

Let `U={p_0,p_1}` be the two singleton bags in an inclusion-minimal
Hall-deficient family.  Put

```text
R=N_S(U)={q},        W=C-U,        T=S-{q}.
```

The order-seven Hall profile gives a perfect matching

```text
w -> t_w       (w in W)
```

from the five vertices of `W` to the five roots of `T`.  Minimality matches
`U-{p_j}` to `q` for either choice of `j`.  Thus `q` is adjacent to both
poles, and these are the only boundary neighbours of either pole.  The same
profile gives the collective domination

```text
N_C(U)=W.                                           (1.1)
```

The three complementary bags of the original spanning `K_5^-` model
partition `W`.  At most one of their three quotient pairs is absent, so
their quotient is connected.  Since each bag is connected, `C[W]` is
connected.

Relative six-connectivity applied to either singleton pole gives

```text
d_C(p_j)+d_S(p_j)>=6,
```

and `d_S(p_j)=1`.  Hence

```text
d_C(p_j)>=5.                                        (1.2)
```

## 2. Direct completion lemma

Delete edges of `C[W]` down to a spanning tree.  There are three unlabelled
trees on five vertices: the path, the star, and the fork with edges
`01,02,03,14`.

If `p_0p_1` is absent, (1.2) says that both poles are complete to `W`.  This
gives three cases, one for each tree.

Suppose instead that `p_0p_1` is present.  Each pole then misses at most one
vertex of `W`.  If both miss a vertex, their misses are distinct by (1.1).
If a pole is complete to `W`, delete one of its incident edges so that its
new miss is distinct from the other miss; if both are complete, choose two
distinct misses.  The reduced graph is therefore specified by one of the
three trees and an ordered pair of distinct missing vertices.  This gives
`3*5*4=60` cases.

Only the seven boundary edges `qp_0,qp_1` and `t_ww` are retained.  Two
certificate templates suffice.

* **A(`x,y`)** omits `q`.  Its five bags are initially
  `{t_w,w}` for `w in W`; insert `p_0` into the `x`-bag and `p_1` into the
  distinct `y`-bag.
* **B(`z,h,p`)** uses the `q`-rooted bag `{q,p}` and omits `t_z`.  Its other
  four bags are initially `{t_w,w}` for `w != z`; enlarge the `h`-bag to
  contain `w_z` and the other pole, where `h != z`.

For the nonadjacent-pole case, template A succeeds for each of the three
tree types.  In the adjacent-pole case, exchange of the poles and tree
automorphisms reduce the sixty labelled cases to the following fifteen
rows.  The middle column is the ordered pair of pole misses.  Here `u=p_0`
and `v=p_1`.

| tree | misses | orbit size | certificate |
|---|---:|---:|---|
| path | `(0,1)` | 4 | `A(1,0)` |
| path | `(0,2)` | 4 | `B(0,1,u)` |
| path | `(0,3)` | 4 | `B(0,4,u)` |
| path | `(0,4)` | 2 | `A(4,0)` |
| path | `(1,2)` | 4 | `A(0,1)` |
| path | `(1,3)` | 2 | `A(0,4)` |
| star | `(0,1)` | 8 | `A(1,2)` |
| star | `(1,2)` | 12 | `A(2,1)` |
| fork | `(0,1)` | 2 | `A(1,4)` |
| fork | `(0,2)` | 4 | `A(2,3)` |
| fork | `(0,4)` | 2 | `B(1,4,v)` |
| fork | `(1,2)` | 4 | `B(2,4,v)` |
| fork | `(1,4)` | 2 | `A(4,1)` |
| fork | `(2,3)` | 2 | `A(3,2)` |
| fork | `(2,4)` | 4 | `A(4,2)` |

The orbit sizes sum to twenty for each tree.  Direct inspection of every
displayed certificate shows that its five bags are pairwise disjoint and
connected, use five distinct roots, and have at least nine of the ten bag
contacts.  The accompanying verifier checks those conditions from the bag
sets themselves.  It also checks all three nonadjacent-pole cases and all
sixty adjacent-pole cases without quotienting: template A closes forty-six
of the latter, and template B closes the remaining fourteen.  This proves
the completion lemma.

## 3. Consequence

The completion lemma produces a punctured `S`-rooted `K_5^-` model in the
edge-deleted graph, hence also in the original shore.  Therefore every
order-seven Hall return with `i=2` is terminal.  The argument uses only the
order-seven Hall profile and relative six-connectivity; no lower bound on
`eta(C)` and no packet assumption is required.

## 4. Reproduction

Run the standard-library verifier with

```text
python3 \
  active/experiments/sparse_sixcut_order_seven_i2_completion/verify.py
```

Its terminal line is

```text
order-seven i=2 direct completion: PASS
```
