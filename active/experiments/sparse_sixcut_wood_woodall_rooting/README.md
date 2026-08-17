# Wood--Woodall exceptional-core rooting verifier

This verifier exhausts the six-root attachment masks in the finite decoder
used by
[`hc7_k7minus_sparse_sixcut_threeconnected_minorfree_exact_singleton.md`](../../hc7_k7minus_sparse_sixcut_threeconnected_minorfree_exact_singleton.md).

Run from the repository root:

```text
cc -std=c11 -O2 -Wall -Wextra -pedantic \
  active/experiments/sparse_sixcut_wood_woodall_rooting/verify.c \
  -o /tmp/sparse_sixcut_wood_woodall_rooting
/tmp/sparse_sixcut_wood_woodall_rooting
```

Expected output:

```text
W3 tested=234256 decoder_failures=15 carrier_admissible_failures=0
W4 tested=9838752 decoder_failures=75 carrier_admissible_failures=0
long-wheel tested=5153632 decoder_failures=15 carrier_admissible_failures=0
prism tested=5153632 decoder_failures=15 carrier_admissible_failures=0
K33 tested=5153632 decoder_failures=15 carrier_admissible_failures=0
```

A mask is one of the `22` subsets of a six-set having order at least four;
the `W4` hub also uses the `42` subsets of order at least three.  For each
row the verifier tries every injection of the five bag roots into the six
boundary roots and checks the exact missing core pairs recorded in the
proof.  The `W3` row separately tries the fifth singleton-root bag.

The middle count records failure of the displayed sufficient decoder, not
absence of every conceivable rooted model.  The last column retains such a
failure only if it obeys the audited carrier guard: no four-set of roots is
contained in three masks.  It is zero in every row.  Thus all raw decoder
failures are forbidden by three singleton four-root carriers; no
probabilistic or solver heuristic is used.
