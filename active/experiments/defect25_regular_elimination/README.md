# Exact-defect regular elimination: finite verification

Run from the repository root with the retained virtual environment:

```text
.venv/bin/python active/experiments/defect25_regular_elimination/verify.py
```

The script uses only NetworkX.  It obtains every order-eight graph by
adjoining one vertex in all `128` ways to each of the `1,044` unlabelled
order-seven graphs in NetworkX's graph atlas.  This may repeat isomorphism
types, but cannot omit one.

It checks two statements by exact connected-branch-set minor search.

1. For all `352` eligible extension representations of minimum degree at
   least four, all `36` unordered equal-or-distinct pairs of exact misses
   give a `K_7^-` minor after adding the centre and two component images.
   This is `12,672` checked profiles.  A full component attachment is a
   supergraph of one of the tested distinct-miss profiles.
2. Among those eligible representations, precisely two are
   `K_5`-minor-free, and both are isomorphic to
   `C_6 join overline(K_2)`.  They are two atlas-extension presentations
   of the same unlabelled graph.

The final assertion records the exact limit of this finite step.  At
minimum neighbourhood degree three, the cubic graph `GMs`KK` with misses
`3,5` gives an eleven-vertex quotient with no `K_7^-` minor.  Thus the
two-exterior inference used at defect 25 does not survive unchanged at
defect 26.
