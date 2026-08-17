# Low-endpoint pair-deletion interface

Deleting an adjacent degree-eight vertex and a degree-eight or degree-nine
neighbour leaves enough density for a spanning `K_7^vee` minor.  This
experiment tests whether the resulting branch-set contact pattern closes
from the degree and codegree data alone.

It does not.  Start with `K_7^vee` on

```text
P,B,C,U1,U2,U3,U4,
```

where `PB` and `PC` are absent.  Add adjacent roots `v,x`, each adjacent
to exactly `B,C,U1,U2`.  The resulting graph has graph6 code `HN~~zpx` and
has no `K_7^-` minor.  Multiplicities within those four branch sets can
give the roots degrees `(8,8)` or `(8,9)` and codegree three.

This is not a counterexample to the critical-host theorem: the quotient is
only four-connected, and the multiplicity table is not an actual host.  It
shows precisely that a proof must use internal branch-set structure or a
model-transfer argument; static contacts, degrees and codegree do not force
the required alignment.

Run from the repository root:

```text
UV_CACHE_DIR=/tmp/uv-cache uv run python \
  active/experiments/pair_deletion_low_endpoint_interface/verify.py
```
