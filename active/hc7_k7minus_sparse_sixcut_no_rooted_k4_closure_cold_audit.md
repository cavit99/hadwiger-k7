# Independent cold audit: sparse six-cut no-rooted-`K_4` closure

**Verdict:** GREEN.

This audit pins

```text
23ee073a1df5ccca13dfab57e0307e152bb49183b72315554e298f0d9aaade49  active/hc7_k7minus_sparse_sixcut_no_rooted_k4_closure.md
13767ebc7a583eb77c51c86cc42c19b495aee5c959670e3441c4b68c7a9931cc  active/experiments/sparse_sixcut_no_rooted_k4/verify.py
```

The source proves exactly the stated branch closure: in a returned
three-component six-cut satisfying the `4n` density identity, some closed
lobe contains a four-rooted `K_4` model.  It does not claim that this model
already composes to `K_7^-`.

## Analytic check

For a component `C` and omitted pair `{p,q}`, the separator lift to
`(G[C union Z],Z)`, `Z=S-{p,q}`, is valid: a rooted separation of order at
most three, together with `p,q`, would be a cut of the host of order at most
five, with either other full component on the far side.  Norin--Totschnig
Lemma 9 therefore gives the displayed inequality whenever the rooted model
is absent.

Summing over all fifteen pairs is exact.  Each attachment count occurs ten
times and each boundary edge six times, giving

```text
15e_C+10P+6b <= 45c+75.
```

Substitution of `eta=e_C+P-4c` and `e_C>=c-1` gives
`10eta(C)+6b<=80`.  Summing this over the three components contradicts
`b+sum eta=24+sigma` for every `b>0`.  At `b=0`, equality forces
`sigma=0`, `eta=8`, `e_C=c-1` and `P=3c+9` in every component.  The fifteen
pair inequalities then all have equality, so all six attachment counts are
`(c+3)/2`.  The minimum-degree sum gives `c<=7`; simplicity excludes
`c=1`, and the audited carrier bound excludes `c=3`.  Thus only the finite
orders five and seven remain.

## Finite lemma

I reran the standard-library verifier.  It reproduced all pinned counts and
digests:

```text
order 5: 3 tree shapes, 36 profiles, 540 four-sets
order 7: 11 tree shapes, 1149 profiles, 17235 four-sets
order-5 digest c78743f57d3a36bf6ca87f1a9e339e1f2f09cd53832ad6805f73e9f606ecacf7
order-7 digest a5d70b88bfb125047b3cb2d3b3a9f0acfdfd5d7741c5aaac11ec66390c76ae1d
```

The enumeration is complete.  At order five, a profile is determined up to
root permutation by the counts of the six single missed vertices, bounded
by the tree degrees.  At order seven, the six missed pairs form a loopless
multigraph whose degree sequence equals that of the tree; recursive stub
pairing enumerates every such multigraph, with duplicates removed.  Prüfer
sequences and the canonical centre code give all unlabelled trees.  Root
permutations need not be repeated because the conclusion quantifies over
all four-subsets of the six roots.

For every profile and four-set, the checker tests every injection of the
four roots into four distinct tree vertices.  Its acceptance conditions are
exactly that each two-vertex rooted bag is connected and that the four bags
are pairwise adjacent.  Thus every accepted witness is a literal rooted
`K_4` model.

`py_compile`, `git diff --check`, and a fresh verifier run passed.  I found
no arithmetic, separator, enumeration, labelling, or scope defect.
