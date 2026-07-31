# Internal audit: contracted-star and fan-tree elimination

**Verdict:** GREEN for the exact theorem revision identified below.  This is
an internal mathematical and computational audit, not external peer review.

## Audited revisions

- [theorem](hc7_k7minus_distinct_miss_fan_tree_elimination.md), SHA-256
  `012e98da1403fb72e303c294e403b2b82a4cc8d2a411287268e8de08d505a5d2`;
- [retained verifier](hc7_k7minus_distinct_miss_fan_tree_completion_verify.py),
  SHA-256
  `15c14433076527c173d7b12afe4c2ff88313236be38f16ee2e1f9a9a16889b0a`;
- [exceptional-neighbourhood input](hc7_k7minus_exceptional_neighbourhood_completion.md),
  SHA-256
  `fc1e88c28b1f4d0dc7a1cbdeefa19fecfd5e969b986c64e11eb1990615f5dfbd`;
- [distinct-miss boundary input](hc7_k7minus_nonfull_attachment_reduction.md),
  SHA-256
  `2b269e7ecea09f695991689e2a6db64d928aedb141ea8cfbf85d14f84fc70617`.

The two inputs have their own adjacent GREEN audits.  No dependency uses the
new theorem, so the proof chain is acyclic.

## 1. Dynamic-colouring argument

The contracted-star proof is valid.  The independent set `J` is explicitly
nonempty, so contracting `\{u\}\cup J` produces a proper minor.  Pulling its
colouring back only to `G-u` gives `J` one common colour.  The other
`q-1` neighbours must use all remaining colours exactly once, since any
absent colour extends to `u`.

For a nonedge `rs`, a Kempe interchange on the bichromatic component
containing only one endpoint would remove the old colour of `r` from
`N(u)`, again colouring `u`.  Hence the endpoints are joined
bichromatically.  On a shortest such path, no internal neighbour of `u`
can occur: `J` uses the contracted colour, while `r,s` are the unique
vertices of `N(u)-J` using the two path colours.  The open interior is
therefore contained in one component of `G-N[u]`.

Applying this with an independent triple in `Z` would give a nontrivial
`x`--`y` path through `E` or `F`.  This is impossible because `E` misses
`x` and `F` misses `y`.  Thus `\alpha(G[Z])\le2`, dynamically eliminating
the exact `3K_2` parity boundary and every other independence-three case.

## 2. Boundary classification

The six-vertex classification is computation-free.  Ramsey's
`R(3,3)=6` theorem supplies one triangle.  The vertex-deleted
`K_4^-` exclusion bounds each remaining vertex to one neighbour in that
triangle, and the independence bound forces the other three vertices to
form a triangle.  Symmetry makes the cross edges a matching.  Two cross
edges, followed by one deletion and one contraction, give the forbidden
vertex-deleted `K_4^-` model.  The only possibilities are therefore
`2K_3` and `2K_3` plus one joining edge.

## 3. Fan-tree reduction

The connectivity and shore-confinement claims check.  A separator of order
at most five in `G-u`, together with `u`, would contradict
`\kappa(G)\ge7`; hence `G-u` is six-connected.  A six-fan from `x` uses all
six vertices of `Z` as distinct ends.  After replacing an adjacent-end limb
by its literal edge, a nontrivial limb has no internal vertex in `Z`.
Its first internal vertex is in `F`: it cannot be in `E`, which misses `x`,
or be `y`, since `xy` is absent.  Once in `F`, it cannot enter `E`, `y`,
another boundary vertex, `u`, or `x` again.  Its open interior is therefore
wholly in `F`.  The argument for the `y`-fan and `E` is symmetric.

Each missed-neighbour set meets both boundary triangles; otherwise its
portal is complete to one triangle and creates a literal `K_4`.  Thus the
marked sets are nonempty.  After contracting the disjoint marked limb
interiors, choose a tree joining them.  Contracting only edges with an
unmarked endpoint, while propagating at most one marked label, never merges
two markers.  The expanded preimages are disjoint connected bags and their
contact graph contains the resulting labelled tree.  The original
portal-to-limb and limb-to-root edges survive.

## 4. Rooted certificates and host lift

For each side state, every bag labelled by `z` is connected and contains
the literal root `z`.  Combining the `E`-side and `F`-side pieces with that
label remains connected through `z`; pieces with different labels remain
disjoint.  The two contact masks therefore combine literally.  Fourteen of
the fifteen possible contacts give a rooted `K_6^-` model.  The singleton
`\{u\}` meets every bag through its root and completes it to `K_7^-`.

When the whole-component quotient is terminal, its connected branch sets
lift through the contractions of `E` and `F`.  Otherwise the actual two
fans yield some pair of the labelled trees covered by the finite theorem,
so the corresponding rooted certificate lifts.  Both outcomes are
explicit minor-model constructions in the unbounded host.

## 5. Retained and independent finite checks

Running

```text
python3 results/hc7_k7minus_distinct_miss_fan_tree_completion_verify.py
```

reproduced:

```text
GREEN: distinct-miss fan-tree completion verified
bridge=0 labelled_valid=1032 valid_orbits=21 quotient_survivor_orbits=3 tree_pair_counts=(2000, 256, 256)
bridge=1 labelled_valid=1113 valid_orbits=109 quotient_survivor_orbits=6 tree_pair_counts=(2000, 2000, 256, 256, 256, 256)
mask_orbit_digest=1d653544a19aed2fac36589f1d113583fe29f7a2af58679e90b574558d9f3203
quotient_certificate_digest=cb251c5518e05b5b1ba79a9149600226777cee5e8677f6bf9a8af90b18b626c3
fan_tree_certificate_digest=5c19a21365f7380afef89b6164dcbee3752db001198cb04aa9270bc4aad33785
```

The retained verifier regenerates all valid portal masks, their exact
symmetry orbits, and all quotient certificates.  It enumerates labelled
trees by Prüfer sequences, constructs six rooted bags, and rechecks their
connectivity, disjointness, and contacts.  Its dominance pruning is safe:
replacing a side state by a contact superset cannot invalidate a completion,
and there is no bag-capacity constraint between the two disjoint shores.

A separate deterministic checker did not use side states, rooted contact
masks, dominance pruning, or their combination logic.  It built every full
sparse fan-tree graph and contracted actual edges directly to seven
spanning connected bags, then rechecked at least twenty quotient edges.
It found models in all

\[
 2{,}512+5{,}024=7{,}536
\]

labelled tree pairs, with zero failures.  Its independently serialized
certificate stream has SHA-256

```text
339e124717b0ad46b2eca4374bb1dd61f20ae952e14a045152b726597e961bde
```

and a separate mask/orbit regeneration reproduced all nine survivor
orbits.  The independent checker used symmetry-equivalent representatives
in the bridged case, providing an additional convention check.

The scripts rely on Python assertions; the documented ordinary invocation,
not `python -O`, is the verification command.

## Scope

The theorem closes exactly the two-component distinct nonadjacent-miss case
at an exceptional degree-eight centre.  It does not eliminate distinct
adjacent misses, the one-nonfull case, the both-full case, or the
one-component exceptional-centre residue.  It proves neither the global
`K_7^-` six-colour conjecture nor `HC_7`.  The finite step is
computer-assisted, and the review remains internal.
