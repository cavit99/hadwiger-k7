# Complete seven-terminal kernel composition

This deterministic verifier composes the three surviving dominated
degree-eight common-neighbour graphs with the complete audited
seven-terminal irreducible-kernel catalogue.

It enforces the catalogue's exact quantifiers:

* every one of the 5,495 labelled edge-minimal three-connected carriers on
  the seven roots; and
* every one of the 30,600 labelled order-eight templates, accepting a
  template when at least one legal owner of the extra vertex closes.

Run from the repository root:

```text
python3 active/experiments/dominated_singleton_complete_seven_terminal_kernel/verify.py
```

Pinned output:

```text
complete seven-terminal dominated-centre composition order7_carriers=5495 order7_failures=21 order8_templates=30600 order8_failures=89
order7_failure_counts [('FCQ`_', 10), ('FCQb_', 4), ('FCp`_', 7)]
order8_failure_counts [('FCQ`_', 50), ('FCQb_', 10), ('FCp`_', 29)]
order7_failure_degree_profiles [((3, 3, 3, 3, 3, 3, 6), 21)]
order8_failure_chord_contact_profiles [((0, 7), 13), ((1, 5), 19), ((1, 6), 38), ((1, 7), 19)]
FCQ`_ order7_failure_orbits=1 order8_failure_orbits=4
FCQb_ order7_failure_orbits=2 order8_failure_orbits=5
FCp`_ order7_failure_orbits=1 order8_failure_orbits=4
kernel_failure_orbits order7=4 order8=13
order8_closing_owner_histogram [(0, 89), (3, 428), (4, 9013), (5, 31336), (6, 36201), (7, 14733)]
four_contact_refinement_screen order7_tests=735 order7_failures=0 order8_tests=3115 order8_failures=0
```

Thus the complete catalogue does not by itself close the branch.  Its
residue is nevertheless exact:

* every order-seven survivor is a labelled six-wheel
  `K_1\vee C_6` (21 placements, four fixed-`Q` orbits); and
* every order-eight survivor is a wheel or one-chord template (89
  placements, thirteen fixed-`Q` orbits).  No two-chord template survives.

Every residual placement becomes terminal after one further connected
augmentation meeting any four rooted bags, provided it can be absorbed at
a contacted owner while preserving the original rooted carrier.  The
order-eight check chooses both the extra-vertex owner and a distinct owner
for the four-contact augmentation.

The terminal-kernel lift used in the host is spanning.  Consequently this
finite augmentation should be read as the adjacency increment required
from a controlled split and transfer inside one existing branch set, not as
evidence that a component outside the model exists.

## Trust boundary

The five unlabelled minimal three-connected carriers are generated from
`geng`, then relabelled and deduplicated.  The order-eight templates are
generated directly from the three audited exact families and deduplicated.
Assertions enforce the catalogue sizes, residue counts, orbit counts and
four-contact closure.

The finite theorem concerns only the seven-bag adjacency quotient.  It
does not prove that five-connectivity or the four operation-labelled
colourings supply a movable connected subgraph meeting four distinct bags,
nor that removing such a subgraph preserves the source bag and its carrier
adjacencies.  That response-sensitive branch-set split is the remaining
unbounded step.
