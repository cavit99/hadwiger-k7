# Three augmented bags do not capture the density-six rooted certificate

**Status:** exact order-five barrier with an elementary model and a
deterministic verifier.  The graph satisfies the live connectivity, excess,
and packet-one hypotheses and has the required rooted `K_5^-`; it shows that
the uniform three-row certificate found at internal order four cannot be the
unbounded proof mechanism by itself.

## 1. Construction

Let the six roots `0,...,5` be independent.  Let `C` have vertices
`v_0,...,v_4`, internal edges

```text
01,03,04,12,13,14,23,24
```

and boundary labels

```text
v_0:124,   v_1:034,   v_2:124,   v_3:01234,   v_4:0345.    (1)
```

For every nonempty `X subseteq C`,

```text
|N_C(X)-X|+|N_S(X)|>=6.                                 (2)
```

Root `5` has the unique neighbour `v_4`.  Consequently every `S`-full
packet contains `v_4`, so the full-packet packing number is one.  Direct
counting gives

```text
eta(C)=8+18-4*5=6.                                      (3)
```

## 2. Why the three-row mechanism fails

A model with exactly three augmented one-vertex root bags and two singleton
root bags would require three internal vertices having the singleton pair
in their common boundary neighbourhood.  The only triples with common
neighbourhood of order at least two are

```text
{v_0,v_2,v_3}, with common roots {1,2,4},
{v_1,v_3,v_4}, with common roots {0,3,4}.               (4)
```

In the first triple, after choosing two singleton roots, both `v_0` and
`v_2` have only the same remaining root available, so the three augmented
bags cannot receive distinct roots.

In the second triple, `v_1` must receive the remaining common root, `v_4`
must receive root `5`, and `v_3` receives one of `1,2` while the other is
omitted.  The first two required contacts exist, but the `v_3`--`v_4`
contact does not: `34` is not an internal edge, `v_3` does not see `5`, and
`v_4` sees neither `1` nor `2`.  Thus no three-augmented literal certificate
exists.

## 3. The correct four-augmented certificate

Omit root `0` and take the rooted bags

```text
{1,v_2}, {2,v_3}, {3,v_1}, {4}, {5,v_4}.              (5)
```

They are pairwise adjacent except for the bags rooted at `2` and `5`.
Hence (5) is a punctured five-rooted `K_5^-` model.  The density-gated
dichotomy survives; only the proposed uniform certificate normal form is
false.

## 4. Reproduction

Run

```text
python3 -B barriers/hc7_three_augmented_incidence_certificate_barrier_verify.py
```

The standard-library verifier exhausts all nonempty internal shores, all
full packets, and every choice of three vertices, singleton pair, omitted
root, and root assignment.  It then checks (3) and the explicit model (5).
