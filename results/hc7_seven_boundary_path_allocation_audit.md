# Internal audit of the seven-boundary path normalization

**Verdict: GREEN.** The complete [source](hc7_seven_boundary_path_allocation.md)
was checked at SHA-256
`db1d76d5d3330bca5bae82fa3f76a6a09a20a1d5098527f247ee2983283af1b8`.
No gap was found in the abstract normalization or its stated application.
This is an internal audit, not external peer review or a global closure.

## Provenance and inputs

The reviewer developed the four interchangeable central-root responses
and the root-switching step before this independent whole-file read.
That prior collaboration is disclosed. The first complete read was at
`c920493414e136f10853b8097a63b7e4c28749c153c688b19a3f966d9cd8f630`.
The next revision only defines Q and spells out the neighbourhood
configuration; reversing those two clarifications exactly recovers that hash.
Promotion changes only the status sentence and two relative input links;
reversing them exactly recovers the fully audited draft
`c735382ea8f417958cdec2793ccd8e650efac90e9e5b12d643c482b55a1b36bc`.

Both invoked statements and their adjacent audits were reread and the
following four hashes checked against disk:

| Input | Source SHA-256 | Audit SHA-256 |
| --- | --- | --- |
| [Four-root packet, Lemma 1](hc7_two_triangle_exterior_helpers.md) | `b3fe07ea52e0e553c61edb59cd5b7da3719ae834d8803f21afb9bde90fc410a8` | `e9bc147d6c0e48bba395dc5fe590ef8a8cc778914804e3c1f5d33c48e2eec628` |
| [Contraction closure, Corollary 3](../active/hc7_companion_contraction_closure.md) | `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4` | `26b2f5ad7226c7bb3f194cac8523f043d7ae6ca955036249f04ddc9fb6d94394` |

No fresh literature inspection or finite mathematical computation is used.

## Strongest inference checks

Deleting three C roots loses at most three boundary vertices and at most
two neighbours per nonroot. The four-root packet therefore applies for
each central root separately. Finiteness permits the stated extremum over
all four choices; no independent models are united.

A nonroot leaf that exclusively supplies at most one P contact can be
donated to that bag, with its old tree edge restoring the contact from
the remaining central bag. Two nonroot leaves would require four distinct
exclusive labels, so the minimal central tree is a path. Chord shortcuts
either increase the P union or decrease the central bag without losing
the endpoint or a required contact.

An unused component has no P-bag neighbour. Bracketing an internal marked
vertex permits a reroute through that component and donation of the old
segment, strictly increasing the P union even when unused reroute vertices
enter the central bag. For each remaining closed gap, its internal path
vertices and all components attached within it form an actual nonroot set
with boundary at most two. A component meeting the gap interior cannot
cross a mark. The internal-four condition excludes every nonempty gap and
every singleton-attachment component, proving the spanning assertion.

For the central-root switch, the new C root lies outside all old bags.
The donated prefix contains an M1 contact, and the old cut edge preserves
the new central--M1 contact even when the switch occurs at q. The old
central root is excluded, every original P root stays in its own bag,
and all other C roots remain unused. The P union grows strictly.

The singleton-path case needs no nonroot count. For length one, q loses
at most two neighbours to C and has at least six P-bag neighbours. For
longer paths, z1 has only its two path neighbours and at most one further
C neighbour outside M1, giving five M1 neighbours. Later internal vertices
have six, and q has seven neighbours in the P union. These count actual
vertices, including all edges of F, rather than distinct bag labels.

## Application and remaining scope

In the actual host, v survives outside every closed nonroot subset, so
seven-connectivity supplies the required boundary bound. The closed side
retains all nonroot degrees. Corollary 3 gives at most two B contacts,
and an r-neighbour cannot have two B contacts; hence the C bound holds.
No chromatic-criticality or induced-neighbourhood assumption is imported.

The audit does not supply a matching of B contacts among the P bags or a
nonseparating transfer through M1. The central root remains a choice from
C, and different root responses are not simultaneous. The compatible
extra helper, the two-triangle case, and Conjecture 19 remain open.
