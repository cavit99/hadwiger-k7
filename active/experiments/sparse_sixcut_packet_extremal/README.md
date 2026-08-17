# Sparse six-cut packet extremal falsifier

**Status:** deterministic finite falsifier and development search.  It is
evidence only, not a proof of the unbounded statement.

For an independent six-vertex boundary `S` and an internal graph `C`, the
program represents each internal vertex by its internal adjacency mask and
its boundary-neighbourhood label.  It tests exactly:

```text
|N_C(X)-X|+|N_S(X)| >= 6             for every nonempty X subseteq C,
eta(C)=e(C)+e(C,S)-4|C|,
mu_S(C)=1,
```

and absence of every punctured five-rooted `K_5^-` model.  The rooted-model
test enumerates every assignment of internal vertices to the five rooted
bags or to no bag; it is not restricted to singleton contractions.

## Reproducible exact screens

Run:

```text
python active/experiments/sparse_sixcut_packet_extremal/search.py --mode self-test
python active/experiments/sparse_sixcut_packet_extremal/search.py --mode exact-small --order 1
python active/experiments/sparse_sixcut_packet_extremal/search.py --mode exact-small --order 2
python active/experiments/sparse_sixcut_packet_extremal/search.py --mode exact-small --order 3
python active/experiments/sparse_sixcut_packet_extremal/search.py --mode exact-clique-four
```

The exact labelled census gives:

| `|C|` | internally six-connected | packet-one | rooted-model-free | maximum `eta` |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 2 |
| 2 | 44 | 42 | 42 | 4 |
| 3 | 12,128 | 10,572 | 1,710 | 4 |

The independent order-four census covers all six connected unlabelled
internal graphs.  It is compiled and run with:

```text
cc -O3 -std=c17 -Wall -Wextra -pedantic \
  active/experiments/sparse_sixcut_packet_extremal/exact_order_four.c \
  -o /tmp/sparse_sixcut_exact4
/tmp/sparse_sixcut_exact4
```

Among the instances satisfying `eta>=6`, relative six-connectivity and
`mu_S(C)=1`, the exact counts are:

| internal graph | instances tested | punctured-model-free |
|---|---:|---:|
| `P_4` | 4,074 | 0 |
| `K_{1,3}` | 5,004 | 0 |
| `C_4` | 24,204 | 0 |
| paw | 24,564 | 0 |
| `K_4-e` | 113,724 | 0 |
| `K_4` | 414,924 | 0 |

Thus all `586,494` threshold instances contain a punctured five-rooted
`K_5^-` model.  The final line is

```text
GREEN exact independent-six-root order-four dichotomy
```

This is an exact order-four result only.  It does not imply the unbounded
statement below.

**Verifier maintenance:** automation must require exit status zero and the
final `GREEN` line.  Any avoiding instance prints `COUNTEREXAMPLE` and
immediately calls `exit(1)`; do not replace that exit with continued
counting unless `main` is also changed to return nonzero when the avoiding
count is positive.

The random mode is a seeded adversarial supplement:

```text
python active/experiments/sparse_sixcut_packet_extremal/search.py \
  --mode random --order 7 --trials 100000 --seed 20260817
```

It must not be cited as exhaustive.

## Exact low-order witnesses and rejected shortcuts

The edge with both internal vertices adjacent to all six roots has
`eta=5` and no punctured rooted model.  It has two singleton full packets,
so it is the sharp rooted-model-free atom rather than a packet-one
counterexample.

The triangle with boundary labels

```text
0123, 0145, 02345
```

is internally six-connected, packet-one and rooted-model-free, with
`eta=4`.  Its full packets need not share a common vertex.  Thus a
Helly-vertex induction is invalid.

The clique `K_4` with labels

```text
0134, 0124, 013, 012345
```

has `eta=7` and packet number one.  It refutes a pure carrier-packing
strengthening, but it has the required punctured rooted model.  The rooted
alternative cannot be discarded.

Nor can ordinary Mader augmentation align the roots.  Add nine virtual
edges forming a `K_5^-` on five boundary roots to the preceding triangle
atom.  For omitted root `5` and virtual missing edge `01`, the augmented
graph has the literal `K_6` minor with bags

```text
{2}, {3}, {0,4}, {v_0}, {1,5,v_1}, {v_2}.
```

The atom still has no punctured rooted `K_5^-` and has packet number one.
Hence an unrooted `K_6` obtained after a nine-edge completion does not by
itself decode to either desired local outcome; a density-sensitive
alignment argument would still be required.

## Unbounded gate

No counterexample was found to

```text
eta(C)>=6
  => a punctured five-rooted K_5^- model or mu_S(C)>=2.
```

The computation does not settle that implication.  The accompanying
exact-six-fragment rerooting theorem supplies hereditary rooted-model
exclusion for a separator induction; two derived full packets still need
two disjoint opposite-side linkages, whereas six-connectivity supplies
only one.
