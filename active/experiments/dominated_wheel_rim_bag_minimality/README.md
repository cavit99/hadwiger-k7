# Dominated wheel rim-bag quotient check

This deterministic check refines the 21 order-seven failures in the
complete seven-terminal dominated-centre composition.

Run from the repository root:

```text
python3 active/experiments/dominated_wheel_rim_bag_minimality/verify.py
```

Expected output:

```text
GREEN dominated wheel rim-bag quotient residues=21 missing_edge_tests=189 vulnerable=[('FCQ`_', 20), ('FCQb_', 4), ('FCp`_', 0)]
```

It verifies three exact finite facts.

1. In every failed order-seven composition, every literal edge of `Q` is
   already an edge of the labelled six-wheel.
2. Adding any one of the 189 missing labelled quotient edges produces a
   `K_5^-` minor.
3. A rim root has two nonliteral carrier adjacencies only when it has
   degree one in `Q`.  Across all labelled failures, this occurs twenty
   times for `C_5 dotcup K_2`, four times for the pendant-path type, and
   never for `C_7`.

The script imports the exact minor routine, eligible `Q` graphs, and
minimal three-connected carrier generator from the adjacent complete
kernel experiment.  It requires `geng` from nauty.  It is a finite quotient
calculation, not an unbounded host proof.
