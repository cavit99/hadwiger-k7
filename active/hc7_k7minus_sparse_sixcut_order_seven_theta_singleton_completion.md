# The order-seven theta singleton closes by one misaligned incidence

**Status:** proved analytic finite lemma; the accompanying portable verifier
checks every labelled copy and every directed nonedge incidence.  Independently
cold-audited.

Write `K_5^-` for `K_5` with one edge deleted.  A model rooted at five
specified vertices has five disjoint connected bags, one containing each
root, and at most one missing pair of bag contacts.

## 1. Statement

Let `S` be a stable six-set and let `W` be a disjoint six-set, labelled

```text
S={s_0,...,s_5},       W={w_0,...,w_5}
```

in a graph `H`.  Let `u` be a further vertex.  Suppose

1. `u` is adjacent to every vertex of `W` and to no vertex of `S`;
2. `s_i w_i` is an edge for every `i`;
3. `H[W]` is one of `Theta(2,2,3)`, `Theta(1,2,4)`, or
   `Theta(1,3,3)`; and
4. there are at least `21` edges between `S` and `W`.

Then, for some `o`, the graph

```text
H[{u} union W union (S-{s_o})]
```

contains an `(S-{s_o})`-rooted `K_5^-` model.

In particular, the conclusion uses neither relative five-connectivity nor
the packet-one hypothesis occurring in the order-seven `i=1` return.

## 2. A directed-incidence reduction

Give the six vertices of `W` the labels supplied by the matching in item 2.
Write

```text
i -> j    when s_i w_j is an edge and i!=j.
```

Call this arc **aligned** when `w_i w_j` is an edge of `H[W]`.  A theta in
the statement has seven edges, so there are only fourteen possible aligned
arcs.  The six diagonal matching edges together with all fourteen of them
account for at most twenty boundary incidences.  Item 4 therefore gives an
arc `i -> j` for which `w_i w_j` is not an edge.

The next lemma closes every such arc.  Its proof is an explicit symmetry
table rather than an exhaustive search through incidence systems.

### Lemma 2.1 (one misaligned arc completes the model)

Under items 1--3, one arc `i -> j` on a nonedge `w_iw_j` already forces a
punctured rooted `K_5^-` model.

### Proof

We use two bag templates.  In both, `s_o` is omitted and every root not
displayed separately uses its diagonal bag `{s_i,w_i}`.

For distinct `o,b`, let `P(o;b)` denote the five bags

```text
{s_b,w_b,u,w_o},       {s_i,w_i}  (i notin {o,b}).       (2.1)
```

The first bag is connected and is adjacent through `u` to all four other
bags.  Thus it remains only to find five of the six contacts among the four
diagonal bags.

For distinct `o,a,b`, let `F(o;a;b)` denote

```text
{s_a,w_a,w_o},  {s_b,w_b,u},  {s_i,w_i} (i notin {o,a,b}). (2.2)
```

The table below uses `F(o;a;b)` only when the first displayed bag is
connected.  The `u`-bag is adjacent to all four other bags, so again only
the six contacts among those four need checking.

Here are canonical edge sets for the three theta graphs:

```text
223: 02 03 04 12 13 15 45
124: 01 02 03 12 15 34 45
133: 01 02 04 13 15 23 45.                              (2.3)
```

In the following table an entry in the second column is the complete orbit
of directed nonedges under the automorphism group of the corresponding
labelled theta.  The bags and possible missing contact are written for the
first arc in that orbit; for another arc, apply an automorphism taking the
first arc to it.  An ordinary pair in the last column is the only possible
missing contact between two diagonal bags.  An entry `[ao]-j` is the only
possible missing contact between the folded bag `{s_a,w_a,w_o}` and the
bag rooted at `s_j`.

| theta | directed-nonedge orbit | bags | possible missing contact |
|---|---|---|---|
| 223 | `0>1, 1>0` | `P(4;5)` | `23` |
| 223 | `0>5, 1>4` | `F(1;2;3)` | `[21]-4` |
| 223 | `2>3, 3>2` | `P(4;5)` | `01` |
| 223 | `2>4, 2>5, 3>4, 3>5` | `F(0;3;5)` | `14` |
| 223 | `4>1, 5>0` | `F(0;2;3)` | `[20]-5` |
| 223 | `4>2, 4>3, 5>2, 5>3` | `F(0;3;5)` | `14` |
| 124 | `0>4, 1>4` | `F(1;0;2)` | `35` |
| 124 | `0>5, 1>3` | `P(3;4)` | `25` |
| 124 | `2>3, 2>5` | `P(4;5)` | `13` |
| 124 | `2>4` | `F(0;3;5)` | `14` |
| 124 | `3>1, 5>0` | `P(4;5)` | `23` |
| 124 | `3>2, 5>2` | `P(4;5)` | `13` |
| 124 | `3>5, 5>3` | `F(0;1;2)` | `[10]-4` |
| 124 | `4>0, 4>1` | `F(0;1;2)` | `35` |
| 124 | `4>2` | `F(0;3;5)` | `14` |
| 133 | `0>3, 0>5, 1>2, 1>4` | `P(4;5)` | `12` |
| 133 | `2>1, 3>0, 4>1, 5>0` | `P(4;5)` | `03` |
| 133 | `2>4, 3>5, 4>2, 5>3` | `F(0;1;3)` | `25` |
| 133 | `2>5, 3>4, 4>3, 5>2` | `F(0;1;3)` | `24` |

For each representative arc, (2.3), the one directed incidence in the
second column, and the diagonal incidences show directly that the indicated
four non-universal bags have all contacts except possibly the one in the
last column.  They also show that every folded bag is connected.  Applying
an automorphism simultaneously to the roots and their matched vertices
proves the same assertion for every arc in that row.  The listed orbits are
disjoint and contain all sixteen directed nonedges in each theta graph.
Consequently (2.1) or (2.2) is the required punctured rooted model. \(\square\)

The theorem now follows from the counting argument preceding Lemma 2.1.
\(\square\)

## 3. Exact returned-six-cut consequence

In the exact order-seven `i=1` Hall return, the unmatched vertex `u` is
universal to the other six shore vertices and has no boundary neighbour.
The other six shore vertices have a perfect matching to the six boundary
roots.  When their internal graph is one of the three theta graphs and the
boundary incidence total is at least `21`, the theorem gives a punctured
five-rooted `K_5^-` model.  The standard two-other-full-components
completion then gives a `K_7^-` minor in the host.

Thus all three order-seven theta rows are terminal.  No relative-five
inequality or packet criterion is needed for this closure.

## 4. Reproduction

The checker

[`experiments/sparse_sixcut_order_seven_theta_singleton/verify.py`](experiments/sparse_sixcut_order_seven_theta_singleton/verify.py)

uses only the Python standard library.  It reconstructs each theta and its
automorphism group, checks that the nineteen displayed directed-nonedge
orbits are disjoint and exhaustive, and verifies connectivity, disjointness,
root placement, and every bag contact.  It repeats the check for all `6!`
simultaneous relabellings of each theta, thereby covering every labelling
induced by the perfect matching.

Run

```text
python active/experiments/sparse_sixcut_order_seven_theta_singleton/verify.py
```

The expected terminal line is

```text
order-seven theta singleton completion: PASS
```
