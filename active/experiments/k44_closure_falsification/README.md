# T44 exact falsification checkpoint (22 August 2026)

This directory preserves exact finite-search sources and checkable output
from the first falsification pass on

> every seven-connected graph with a `K_{4,4}` minor has a `K_7^-` minor.

No conclusion about arbitrary T44 hosts is inferred here.  The only
unbounded statement below is the written-unaudited reduction for the
seven-connected members of one specified full-attachment family.

The primary order-eleven generator needs `pynauty`; the seven-sum and
orders-eight-to-ten scripts need `z3-solver`.  Those two research-only
packages are intentionally not added to the project's locked runtime.  The
retained order-eleven certificate verifier itself uses only the locked
`networkx` dependency.

## Exact order-eleven census

`n11_exact_search.py` generates every unlabelled graph of maximum degree at
most three.  Complementation therefore covers every graph of order eleven
and minimum degree at least seven, hence every seven-connected graph of that
order.  It then tests vertex connectivity exactly and calls the independent
spanning-forest engine in `k7minus_minor11.c`.

Expected census:

```text
unlabelled max-degree-three graphs: 10,946
seven-connected complements:       9,940
with a literal K4,4:                9,844
literal-core K7^- subgraphs:        3,871
literal-core proper-minor cases:    5,973
K7^- certificate quotient edges:   {20: 9,398, 21: 542}
certificate digest:
08b284abc580718e87d2c5561d04b334f47064e5b46254d37440f12c87576ce2
```

The generator's counts through order seven are checked independently
against the NetworkX graph atlas.  `verify_n11_certificates.py` reads the
emitted certificate file without loading the C library or nauty and checks
all 9,940 graphs for exact seven-connectivity, seven nonempty disjoint
connected spanning bags, and at least twenty quotient contacts.

`orders8_10_exact.py` independently covers the smaller orders by using the
fact that the relevant complements have maximum degree at most two and are
therefore disjoint unions of paths and cycles.  Its seven-connected counts
are 1, 5, and 87 at orders 8, 9, and 10.  Thus the combined finite statement
really is for every order at most eleven, not merely order eleven.

Reproduce the order-eleven run from this directory with

```bash
cc -O3 -shared -fPIC k7minus_minor11.c -o /tmp/k7minus_minor11.so
python3 n11_exact_search.py /tmp/k7minus_minor11.so /tmp/n11_certificates.tsv
UV_CACHE_DIR=/tmp/t44-uv-cache uv run python \
  verify_n11_certificates.py /tmp/n11_certificates.tsv
```

The generation command requires an environment containing `pynauty`; the
last command is the independent locked-runtime certificate check.

## Exact full-attachment seven-sums

`full_attachment_seven_sum.py` checks the edge-minimal representatives of
the seven-connected members of

`G = S join (L disjoint-union R)`, `|S|=7`,

where `L,R` are nonempty connected graphs and there are no `LR` edges.
For two outside vertices, seven-connectivity forces `S` to be
five-connected, so the audited double-cone theorem applies.  For three
outside vertices it forces `S` to be four-connected and hence to have
minimum degree at least four, so the audited seven-vertex double-cone
theorem applies.  For four through seven outside vertices, reduce the
shores to spanning trees and `S` to an edge-minimal
`(7-|L|-|R|)`-connected graph.  There are respectively 10, 18, 66, and 11
representative cases, and every case has a validated `K_7^-` model.  For at
least seven outside vertices, delete down to connected subgraphs with seven
total vertices; hence the finite `q=7` case covers every larger order.  This
written reduction plus exact computer-assisted family result covers only
seven-connected members of this full-attachment family; it does not cover
arbitrary non-full seven-sums.

The solver-independent graph6 corpus digest for the
`10+18+66+11=105` minimal cases is

```text
915f0faf4a8dc6ef28a007289acccf5835cfe945a9555f970c6ef92eadd614be
```

The script validates one `K_7^-` model for every case but deliberately does
not hash the Z3-selected witnesses, whose presentation can vary with solver
version.

The finite reduction is monotone: delete each shore to a spanning tree and
delete separator edges until its connectivity is edge-minimal.  The formula

```text
kappa(S join (L disjoint-union R))
  = min(7, |L|+|R|+kappa(S))
```

shows that the retained separator connectivity is exactly what is needed.
When the outside has at least seven vertices, connected subgraphs of the two
shores can be reduced to seven vertices in total, so the order-seven row
also covers every larger member of this full-attachment family.

## Existing sharp local survivors

The retained
[`fat-triangle`](../../../barriers/hc7_k44_fat_triangle_certificate_barrier_verify.c)
and
[`one-split-theta`](../../../barriers/hc7_k44_one_split_theta_certificate_barrier_verify.c)
programs are source-audited.  Their spanning-forest enumeration is
complete.  The former has fifteen target-free profiles with best seven-bag
quotient density 18; the latter has eighteen target-free profiles with best
density 15.  None of those graphs is seven-connected, so they are barriers
to shortcut certificates rather than counterexamples to the global target.
