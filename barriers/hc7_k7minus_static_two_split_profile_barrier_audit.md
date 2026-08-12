# Separate internal audit: static two-split profile barrier

## Verdict and exact revisions

**Verdict: GREEN.**  The explicit graph refutes the stated static
two-split profile assertion, the `K_7^-`-minor argument is exact, and the
deterministic exhaustive verifier reproduces all displayed counts.
This is a separate internal mathematical and computational audit, not
external peer review.

The audited files and their SHA-256 hashes are:

```text
3c331150a4b95a814c7ef5f6aa35bba049996470d22cf75ad28ffa81a3185117  barriers/hc7_k7minus_static_two_split_profile_barrier.md
b2b65ccf1a47a7e9baeeccec68babc08a08845a45cd27222fd690b3f2d33f991  barriers/hc7_k7minus_static_two_split_profile_barrier_verify.py
```

The source differs from the initially audited revision
`c162f2447fb6297b56bac1176c7eabb905be51677d9906d20c5aa3d3dc622671`
only by removal of two trailing spaces in quoted blank lines.  Its
mathematical content is unchanged.

## 1. Explicit construction and split scores

The construction is `Q=K_{2,2,2,2}=K_8-4K_2`, with nonedges

```text
06, 17, 24, 35.
```

The two root bags `R={0,1}` and `S={2,3}` are edges.  Together with the
four singleton bags `{4},{5},{6},{7}`, they are connected, disjoint and
pairwise adjacent, so they form the claimed labelled `K_6` model.

For the `R`-split, `S,{4},{5}` meet both singleton sides, while `{6}`
misses `0` and `{7}` misses `1`.  Its double-contact score is therefore
three.  For the `S`-split, `R,{6},{7}` meet both sides, while `{4}` misses
`2` and `{5}` misses `3`; its score is also three.  Thus neither root
split has the four double-contacting foreign bags required by the refuted
assertion.

The complete four-partite graph has clique number four, so the asserted
absence of a literal `K_5` is immediate.

## 2. Exact exclusion of a `K_7^-` minor

Any seven nonempty branch sets in an eight-vertex graph use either seven
vertices as singleton branch sets or all eight vertices with exactly one
two-vertex branch set.

In the singleton case, omitting one vertex destroys only one of the four
part-nonedges.  The remaining seven vertices still contain the other three
nonadjacent pairs, whereas a `K_7^-` model permits at most one nonadjacent
pair of branch sets.

In the second case the two-vertex branch set must be connected, so its
vertices lie in two different parts.  It is adjacent to every remaining
singleton branch set.  The two parts not met by it each retain both of
their vertices as singleton branch sets, yielding two distinct
nonadjacent pairs.  Again this is too many for `K_7^-`.

These are all possible branch-set-size patterns, so the argument excludes
the minor exactly.  In the source sentence about the second case, “the two
parts not met twice” is understood as the two parts not met by the
connected pair; the displayed construction and the exhaustive check both
implement this exact argument.

## 3. Audit of the exhaustive verifier

The profile generator covers the advertised labelled class exactly:

- each of four singleton foreign bags chooses one of the three nonempty
  incidence patterns at each root edge, giving `9^4` choices;
- a nonempty subset of the four possible `R`--`S` edges makes the two root
  bags adjacent, giving `15` choices; and
- hence the total is `9^4*15=98,415`.

The two split scores correctly include the opposite root bag precisely
when that bag has a neighbour at both singleton sides.  The foreign
singleton bags are made a clique, and the root edges are always present,
exactly as required by the labelled `K_6` profile.

The `K_7^-` test is exhaustive on eight vertices.  It checks every
seven-singleton model by omitting one vertex and every remaining possible
model by contracting each adjacent pair and using the other six vertices
as singleton bags.  For each candidate it counts missing branch-set
adjacencies and accepts exactly when at most one is missing.  These are
the only possible partitions of at most eight vertices into seven
nonempty connected branch sets.

The `K_5` test checks all five-vertex subsets.  The connectivity routine
checks deleted vertex sets in increasing order and returns six for the
explicit graph, as expected from `kappa(K_{2,2,2,2})=8-2=6`.

Running

```text
python3 barriers/hc7_k7minus_static_two_split_profile_barrier_verify.py
```

reproduced:

```text
GREEN static two-split profile barrier
graph=K_8-4K_2 connectivity=6 omega=4 split_scores=(3,3)
K7_minus_minor=false PP_signature=true
total=98415
blocked=84928
target_free=79768
omega_at_most_four=30652
maximal_blocked_omega_four=384
degree_six_maximal=24
```

For every minimum-degree-six survivor counted on the last line, the
verifier additionally checks that the complement consists of four edges
covering all eight vertices.  Hence each is isomorphic to `K_8-4K_2`,
which justifies the stated unique unlabelled saturated obstruction.

## 4. Scope

The construction has the forbidden all-proper signature, is only
six-connected, and is not a critical host.  It therefore does not refute
the cross-signature root-bag theorem, `HC_7`, or the `K_7^-` six-colour
conjecture.  It refutes only an uncoloured static-contact implication and
correctly establishes that the absent all-proper signature must be used
through literal colouring or Kempe data rather than appended to a contact
profile as a label.

There are no unresolved assumptions in the stated barrier or its finite
profile count.
