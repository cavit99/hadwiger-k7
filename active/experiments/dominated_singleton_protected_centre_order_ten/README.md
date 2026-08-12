# Protected-centre order-ten kernel composition

This self-contained verifier checks the finite quotient lemma used to
eliminate the two-nonterminal branch of the exact eight-terminal kernel at
a dominated degree-eight centre.

Labels `0,...,6` are the seven common neighbours `Q`; label `7` is one
other exceptional centre.  The script generates every labelled exact
order-ten normal form

```text
terminal C8 + two complementary AABBAABB four-neighbour sets,
```

tries all sixteen legal nonterminal-owner pairs, then absorbs the bag rooted
at terminal `7` into every neighbouring `Q`-rooted bag.  It tests the union
of the resulting seven-bag quotient with the literal edges of each of the
three surviving graphs `Q` for a `K5-minus` minor by exact
deletion/contraction recursion.

Run from the repository root:

```text
python3 active/experiments/dominated_singleton_protected_centre_order_ten/verify.py
```

Pinned output:

```text
FCQ`_ templates=10080 failures=0
FCQb_ templates=10080 failures=0
FCp`_ templates=10080 failures=0
protected-centre order-ten composition templates=10080 q_types=3 failures=0
witness_digest bacd9ed98b08a1a0a60829250f852e54763e6fc812404e807f2cebf2cdc62202
```

The normal-form template digest is also asserted internally:

```text
78217d8621685a5839aa55172a51e3470297e6f989516c0455a4884471923418
```

## Trust boundary

The analytic order-ten kernel classification and the legality of all
sixteen nonterminal-owner pairs are proved and independently audited in
[`active/hc7_eight_terminal_exact_bundle.md`](../../hc7_eight_terminal_exact_bundle.md)
and its adjacent audit.  This verifier checks only the downstream finite
composition.  Its minor routine is exact on the resulting seven-vertex
quotients: deletion handles unused vertices and contraction handles branch
sets containing more than one vertex.

The script does not enumerate the order-eight or order-nine exact kernels.
Their current residual counts remain discovery diagnostics, not part of
this promoted conclusion.
