# Returned order-two dense-lobe elimination: exact verification

This directory contains two independent exact verifiers for the finite
nine-vertex quotient in the adjacent
[theorem note](../../hc7_k7minus_returned_order_two_dense_lobe_elimination.md).

Run the recursive minor-operation search with:

```text
python3 active/experiments/returned_order_two_dense_lobe_elimination/recursive_verify.py
```

Run the independent direct branch-partition search with:

```text
g++ -O3 -std=c++20 \
  active/experiments/returned_order_two_dense_lobe_elimination/partition_verify.cpp \
  -o /tmp/returned_order_two_dense_lobe_partition_verify
/tmp/returned_order_two_dense_lobe_partition_verify
```

Both programs exhaust exactly the equality profiles

```text
e(S)=9:     5,005
e(S)=10:   36,036
e(S)=11:   81,900
total:    122,941
```

The Python program recursively enumerates all sequences of connected-bag
contractions and vertex deletions.  The C++ program instead directly
enumerates the 750 partitions of a 7-, 8-, or 9-vertex subset into seven
nonempty bags.  Thus they do not share a search implementation.

Profiles with more than the minimum number of component-to-boundary edges
are covered by monotonicity, as proved in the theorem note; neither verifier
silently replaces the inequality by equality.

The source hashes are

```text
recursive_verify.py
  SHA-256 929ca03af1c5404b659b0391b9fe089acd414dfebe8f93117fe3ac02d1c682df
partition_verify.cpp
  SHA-256 1c44627c6ec673efefd38d9b31584b68f8e36defb3b77530c58761ab4337407c
```

The recursive verifier additionally prints the certificate digest

```text
c90f0ffb52a2ee94b30d0d249e048b5501f97d4f34fdf291874780fab968370c
```
