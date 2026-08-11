# Retained-centre local quotient probe

**Status:** computer-assisted finite diagnostic; not an unbounded theorem,
not a counterexample to the five-centre theorem, and not part of the active
proof spine.

The probe enumerates seven-vertex graphs `Y` from the NetworkX graph atlas
with `alpha(Y)<=2` and no `K_4` subgraph.  It adjoins a retained centre, a
pole vertex, and one or two exterior quotient vertices, then searches
directly for a `K_7^-` minor model.

For the first two completed phases, there are nine candidate graphs `Y`.
Among the 81 one-exterior cases, 25 quotient patterns remain target-free.
Adding a second exterior vertex in every possible continuation produces
225 cases and no survivor.  This finite observation motivates a
second-donor connector lemma; it does not prove that two compatible donor
pieces exist in an unbounded host.

The final two-ear phase is exploratory and is not used as a recorded claim.

Run:

```text
.venv/bin/python active/experiments/five_centre_two_cut_local_quotient/probe.py --skip-ears
```
