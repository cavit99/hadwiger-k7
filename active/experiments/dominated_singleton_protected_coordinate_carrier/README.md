# Protected-coordinate eight-terminal carrier probe

This discovery probe tests a literal second-coordinate refinement of the
dominated degree-eight singleton residue.  Let `Q` be one of the three
surviving seven-vertex common-neighbour graphs, let `w` be another exceptional
centre, and let `x` be its selected matching mate outside `Q`.  Delete one
vertex `q_0` of `Q`.  The graph `G-{u,v,q_0}` is four-connected, so the eight
terminals

```text
(Q-{q_0}) union {w,x}
```

root one of the audited `C8`, `K3,5`, or `F8` carriers.  The probe restores
`q_0`, all literal edges of `Q`, and the coordinate edge `wx`.  It then asks
for a `K5-minus` model all five bags of which meet `Q`.

This is a bounded falsification screen, not a proof.  A positive universal
screen would still require a written rooted-quotient lift.  A survivor records
the precise carrier geometry on which the protected-coordinate idea needs
additional exact-kernel or response information.

Run:

```text
python3 active/experiments/dominated_singleton_protected_coordinate_carrier/verify.py
```
