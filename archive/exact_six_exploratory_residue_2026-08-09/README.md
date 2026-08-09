# Exact-six exploratory residue, 9 August 2026

**Status:** archived computational evidence.  Nothing in this directory is a
written proof or part of the current proof spine.  The negative conclusions
below concern only the stated finite quotient or arithmetic mechanism.

## Provenance and disposition

These ten scripts were recovered from stash commit
`a8a6ec161d0e4acbaaf12612569be8a1e905a01f`, whose base is
`ce2c89fa30464075e2ec8a7cc736573965c59d84` and whose untracked-file parent is
`08b5c8e9572bc767fcf64ecf4391fe89661a0a4b`.  The comparison snapshot of
`main` was `7f364d0a56d42edc313a1cef923d9c07f6f3a693`.

The stash also contained five tracked status-document changes and five
untracked promoted artifacts.  The latter are byte-for-byte present on
`main`, introduced by commit `820d46a908eefe44ec63517126300157e0831941`.
The status-document changes are older versions of the current ledger,
navigation, technical frontiers, and research manifest and must not be
restored.

A focused second pass retained three scripts beyond the original seven-file
minimum.  The remaining 84 exploratory files are listed below.  No one of
them supplies a result that should be promoted independently of the ten
retained mechanisms.

## Reproduction environment

The recorded rerun used Python 3.14.6, NetworkX 3.6.1, Z3 5.0.0, Apple clang
21.0.0 with C++20, and the `geng` executable from nauty.  Run commands from
the repository root.  Z3 is an optional audit dependency and is not added to
the project dependency lock.  `tmp_atom_rooted_diamond_probe.py` also uses
`active/hc7_k7minus_p3_atom_yuan_verify.py`; the dependency used for this run
has SHA-256
`0be573df800d1c35d3ea740ea08ab0e5d30335bcfccf363b1c725a2655d257cf`.

```sh
uv run --frozen python archive/exact_six_exploratory_residue_2026-08-09/tmp_internal4_avoidable_diamond.py
uv run --frozen python archive/exact_six_exploratory_residue_2026-08-09/tmp_seven_terminal_avoidable_diamond.py
uv run --frozen python archive/exact_six_exploratory_residue_2026-08-09/tmp_three_mark_private_root_quotient.py
uv run --frozen python archive/exact_six_exploratory_residue_2026-08-09/tmp_atom_rooted_diamond_probe.py
uv run --with z3-solver python archive/exact_six_exploratory_residue_2026-08-09/tmp_threecut_triple_z3.py
uv run --with z3-solver python archive/exact_six_exploratory_residue_2026-08-09/tmp_exact6_r3_valid.py

clang++ -std=c++20 -O2 archive/exact_six_exploratory_residue_2026-08-09/tmp_internal4_gate_terminal.cpp -o /tmp/internal4_gate_terminal
clang++ -std=c++20 -O2 archive/exact_six_exploratory_residue_2026-08-09/tmp_cross_triangle_cut_screen.cpp -o /tmp/cross_triangle_cut_screen
clang++ -std=c++20 -O2 archive/exact_six_exploratory_residue_2026-08-09/tmp_two_nearfull_split_screen.cpp -o /tmp/two_nearfull_split_screen
clang++ -std=c++20 -O2 archive/exact_six_exploratory_residue_2026-08-09/tmp_atom_two_cut_random.cpp -o /tmp/atom_two_cut_random

/tmp/internal4_gate_terminal
/tmp/cross_triangle_cut_screen
/tmp/two_nearfull_split_screen
/tmp/atom_two_cut_random 0 0 200
/tmp/atom_two_cut_random 1 0 200
/tmp/atom_two_cut_random 2 0 200
```

`SHA256SUMS` pins the recovered sources.  The SHA-256 digests of complete
standard output in the command order above are:

```text
tmp_internal4_avoidable_diamond.py       bf170c865e5a5cb49b0e06ccb8d7665e0d2a003188c93e6a206f4d981e2f2a94
tmp_seven_terminal_avoidable_diamond.py  172217685418a010ccfa05bba68c91685a731f8218a43f26110c97512b825715
tmp_three_mark_private_root_quotient.py   500292656eb6ef7de76cb9d78d5d4377e5b6f7c5d28b51cc51f2f6f8d94257f5
tmp_atom_rooted_diamond_probe.py          2bc0a78eb1809d40bc3b88ba9dc859243e084cee1211df6080518109966e4f3e
tmp_threecut_triple_z3.py                 d385ec634dbe3bc761ac1d7059860e24fdbf70d207b34ca0ff64e869725efc2f
tmp_exact6_r3_valid.py                    997dcf74e660ee2468cbe80b5ccc768262633f886b23d0bd11f9447e20d5fd40
tmp_internal4_gate_terminal.cpp           137f36e56ab224962565e18952bad8fbad070db6cf6d0dc1d1dde5c68f82dbcb
tmp_cross_triangle_cut_screen.cpp         41b0d1752adeec383925891f4dcd31601117f89e6826a9078a4940aadcefc5a8
tmp_two_nearfull_split_screen.cpp         4dda774e413b374812fca42323bd1c03a191216415d8c4a08659f78797aa88b6
tmp_atom_two_cut_random.cpp, kind 0       8b0805616fde0dd4855dca16714d49ef2750241343b27e1b4f82357569c4833c
tmp_atom_two_cut_random.cpp, kind 1       4de4e0b69822800e0bd2d40a0bb291ea0fe012ef9d31d31580475ee16da08ef5
tmp_atom_two_cut_random.cpp, kind 2       bcad756aa0ae50e3f0f969a3128229dae985d4ebe46c5c53e93b9dcdab681700
```

The final three digests cover standard output; their one-line survivor counts
are written to standard error.

## Recorded findings

### Avoiding a rooted `K_4^-` model after one marked deletion

**Status:** barrier/counterexample to an intermediate claim.

`tmp_internal4_avoidable_diamond.py` refutes the claim that internal
four-connectivity relative to four roots alone guarantees a marked vertex
whose deletion leaves a rooted `K_4^-` model.  It returns graph6 code
`F?qkw`, roots `(0,1,2,3)`, and the edge set

```text
{(0,4),(0,5),(0,6),(1,4),(2,5),(3,6),(4,5),(4,6),(5,6)}.
```

Deleting any of the marked vertices `4,5,6` leaves no such rooted model.
This does not refute the three-connected terminal construction used in the
positive-surplus atom reduction.  The smallest repair is to retain that
exact three-connected terminal hypothesis rather than replace it with the
tested relative-connectivity condition.

The companion exhaustive catalogue screen
`tmp_seven_terminal_avoidable_diamond.py` reports:

```text
order7_carriers=5
order8_presentations=13
root_assignments=630
assignments_with_avoidable_diamond=630
failures=0
```

The two scripts therefore delimit the failed generalisation without
challenging the narrower catalogue result.

### Static boundary augmentations do not close the seven both-full types

**Status:** recorded negative findings / route nonclosures.

`tmp_internal4_gate_terminal.cpp` checks every triangle in each of the seven
promoted boundary types.  Every type has an explicit presentation surviving
both the one- and two-auxiliary-vertex augmentations; its summary has
`one=0 two=0` for every code.

`tmp_cross_triangle_cut_screen.cpp` adds two boundary-full vertices and one
vertex adjacent to the complement of every boundary triangle.  It closes
only `GCOcbW` and `GCOebW`; the other five types survive.

`tmp_two_nearfull_split_screen.cpp` adds two adjacent vertices, each adjacent
to at least six boundary vertices.  Six types close, but `GCOcaO` has 99
surviving attachment pairs, beginning with hexadecimal masks `3f,3f`.

These are finite failures of particular augmentation mechanisms.  They do
not construct a critical host and do not refute an unbounded completion
theorem.  A repair must use host-level support allocation, colouring data,
or interaction between actual separations; another isolated boundary
augmentation is insufficient.

### Private-root incidence is insufficient

**Status:** computer-assisted finite route nonclosure.

`tmp_three_mark_private_root_quotient.py` examines the fixed nine-vertex
contact-only quotient.  It reports 750 candidate seven-bag partitions, 36
valid incidence patterns, and 28 patterns without a `K_7^-` minor model.
Thus the private-root incidence conditions alone do not force the target.
This says nothing about a host with the required connectivity, density, and
shore structure.  Any repair must add one of those host-level invariants.

### Fixed three-cut skeleton

**Status:** computer-assisted finite positive evidence, not a theorem.

`tmp_threecut_triple_z3.py` reports 206 connected bipartitions, of which 150
split the three marked vertices, followed by `UNSAT`.  This applies only to
the encoded nine-vertex skeleton and incidence inequalities.  Promotion
would require a written reduction from the unbounded host problem and an
independent checker.

### Atom and two-separation quotient failures

**Status:** deterministic heuristic route nonclosures.

`tmp_atom_rooted_diamond_probe.py`, with fixed random seed `847221`, returns
explicit surviving quotients for edge, three-vertex-path, and triangle
atoms.  It shows that inserting one guaranteed rooted `K_4^-` model into
these simplified quotients does not by itself force `K_7^-`.  The samples do
not satisfy the full minimum-host hypotheses and hence are not host
counterexamples.

`tmp_atom_two_cut_random.cpp`, with fixed seeds and 200 trials per atom type,
returns five explicit target-free quotient presentations for each of the
edge, path, and triangle atoms.  The presentations enforce the script's
component-fullness and atom-contact conditions but not the complete
connectivity, density, colouring, or minimality hypotheses.  This is a
warning against closing the atom reduction by those static contacts alone.

### Sound-inequality arithmetic remains feasible

**Status:** computer-assisted finite route nonclosure; encoding not
independently audited.

`tmp_exact6_r3_valid.py` enumerates 50 six-vertex boundary types allowed by
its stated inequalities and finds 31 satisfiable arithmetic profiles.  In
particular, replacing the earlier unsupported internal-boundary degree
assumption by the script's rooted inequalities does not close the
three-component exact-six arithmetic mechanism.  The output is a list of
integer profiles, not graphs and not counterexamples to the six-connected
or seven-connected target statement.

## Focused second-pass disposition of the other 84 files

The following files are not retained.  This is a disposition of the stash,
not a claim that every experiment was mathematically valueless when first
written.

### Exact-six and returned-cut variants

These are overlapping LP/SMT variants, input-driven graph filters, or
specialisations of the same exact-six arithmetic mechanism.  Direct reruns
of `tmp_degree6_lp_sound.py` and `tmp_exact6_r3_sound_z3.py` left respectively
34 and 216 encoded survivors.  `tmp_r3_sound_lp.py` and
`tmp_seven_cut_rooted_disjunct_lp.py` exceeded the bounded audit run while
the former was already producing feasible profiles; the latter had not
completed its first reported result.  None supplies a closure or a graph
counterexample.  The representative standalone survivor screen retained
above captures the reusable conclusion.

```text
tmp_degree6_k6_extension_scan.cpp
tmp_degree6_lp.py
tmp_degree6_lp_sound.py
tmp_degree6_neighbour_screen.py
tmp_degree6_one_lobe_lp.py
tmp_degree6_r2_lp.py
tmp_degree7_boundary_scan.cpp
tmp_degree7_failed_contraction_z3.py
tmp_degree7_neighbour_screen.py
tmp_degree7_quotient_classify.py
tmp_degree7_returned_boundary.py
tmp_edge_atom_lobe_z3.py
tmp_exact6_lightcut_probe.py
tmp_exact6_lp_probe.py
tmp_exact6_lp_sound2.py
tmp_exact6_minimal_r3_lp.py
tmp_exact6_r2_composition.py
tmp_exact6_r3_general_z3.py
tmp_exact6_r3_high_lobe.py
tmp_exact6_r3_sound_z3.py
tmp_exact_six_r3_linear.py
tmp_exact_six_scan.cpp
tmp_high_lobe_large_z3.py
tmp_high_lobe_sixcut_z3.py
tmp_lifted_q_critical_screen.py
tmp_lifted_r3_global_lp.py
tmp_lifted_r3_lp.py
tmp_marked_safe_r2_kstar_lp.py
tmp_marked_safe_r3_lp.py
tmp_min7_boundary_diamond.py
tmp_min7_sixcut_z3.py
tmp_order8_k7minus_threefull.py
tmp_order8_r3_rooted_lp.py
tmp_order8_r3_rooted_quotient.py
tmp_r3_k4_forcing_lp.py
tmp_r3_rooted_assembly.py
tmp_r3_sound_lp.py
tmp_realise_empty_boundary.py
tmp_seven_cut_rooted_disjunct_lp.py
tmp_sixconn_k6_implies_target.cpp
tmp_sixconn_k7vee_obstructions.py
```

### Degree-eight and both-full boundary variants

The promoted Rolek--Song verifier on `main` preserves the audited matching
nonclosure.  The three retained boundary-augmentation scripts preserve the
additional reproducible conclusions.  The files below are raw census or
augmentation variants without a distinct audited result.  Five Python files
also import the absent module `tmp_degree8_rolek_matching_screen`, and the
C++ path-quotient program did not finish a bounded audit run.

```text
tmp_adjacent_degree8_k7vee_masks.py
tmp_alpha3_diamond.py
tmp_degree8_boundary_scan.cpp
tmp_degree8_diamond_target_scan.cpp
tmp_degree8_lobe_lp.py
tmp_degree8_returned_cut_boundary_screen.py
tmp_degree8_rolek_star_screen.py
tmp_degree8_rooted_lp.py
tmp_degree8_two_exterior_scan.cpp
tmp_degree8_two_full_one_path.py
tmp_degree8_two_full_path_quotients.cpp
tmp_degree8_two_full_path_quotients.py
tmp_diamond_star_host.py
tmp_dual_k42_quotient.py
tmp_exceptional_k4minus_profile.py
tmp_exceptional_one_component_screen.cpp
tmp_exceptional_rooted_k4_family.py
tmp_k7vee_augmentation_scan.cpp
tmp_neighbourhood_diamond_scan.py
tmp_rolek_matching_screen.cpp
```

### Other atom probes

The retained pair supplies explicit examples for the reusable static
nonclosure.  `tmp_expand_atom_survivor.cpp` reached only connectivity three
or four in the bounded rerun, and `tmp_inspect_atom_survivor.py` instead
exhibited a near-clique minor model in its fixed presentation.  The remaining
two screens have neither a documented exhaustive input set nor a separately
checkable output certificate.

```text
tmp_atom_cross_screen.py
tmp_atom_diamond_screen.py
tmp_expand_atom_survivor.cpp
tmp_inspect_atom_survivor.py
```

### Rooted-helper, marked-root, and augmentation searches

These are searches or bounded classifications without retained input
catalogues, output digests, or written reductions.  A deterministic rerun of
`tmp_k5minus_random_counterexample.cpp` completed 200,000 trials with `NONE`;
the built-in example in `tmp_two_mark_helper_screen.cpp` checked 1,260 root
choices with no failure.  `tmp_fixed_mark_h3_z3.py` also contains a
device-specific absolute dependency path.  The promoted rooted-helper
theorem and its hash-pinned audit are already on `main`.

```text
tmp_anchored_k6minus_scan.cpp
tmp_fixed_mark_h3_z3.py
tmp_four_root_k42_search.cpp
tmp_low_vertex_augmentation_search.cpp
tmp_marked_k42_dense_scan.cpp
tmp_marked_realise.py
tmp_marked_single.py
tmp_rooted_k42_eq.py
tmp_rooted_k6minus_dense_scan.cpp
tmp_rooted_k6minus_fixed_scan.cpp
tmp_spare_u_exhaust.cpp
tmp_two_apex_rooted_search.cpp
tmp_two_mark_helper_screen.cpp
```

### Miscellaneous construction probes and helper modules

These are heuristic constructions, narrow combinatorial utilities, or an
unpromoted solver helper.  They have no retained successful certificate or
written reduction and do not change the present proof frontier.

```text
tmp_icosahedral_six_sum_search.py
tmp_join_planar_probe.py
tmp_k4free_six_highdegree.py
tmp_k5minus_cycle_transversal.py
tmp_k5minus_random_counterexample.cpp
tmp_k7minus_z3.py
```

## Final stash assessment

After preserving the ten scripts and this scope-and-reproduction record, the
stash contains no remaining unique claim or certificate that warrants
retention.  It is safe to drop only after the commit containing this archive
has been integrated or otherwise retained by a durable branch reference.
