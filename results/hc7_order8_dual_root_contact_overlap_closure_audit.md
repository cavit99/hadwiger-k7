# Independent audit: dual-root contact overlap closure

## Verdict

**GREEN** for the exact source revision

```text
d42eb35b88280f98a062c2c231a9e0fac7fe47de8e05bb4e0edac80af35845e6  results/hc7_order8_dual_root_contact_overlap_closure.md
```

The pole/rim classification, both explicit `K_5`-minor models and the lift
through the dual-root latent-column construction are correct.  This is an
internal cold audit, not external peer review.

The direct audited dependencies were checked at

```text
bb78ac1cc61c501a5f871ab9b69a402f765ee333dabe0c9deeff5805bc94a323  results/hc7_order8_dual_free_root_response_star.md
b48e19642347571a713f60d2b045be85907bfe6a07052465ba09d2446d516859  results/hc7_seven_column_contact_structure.md
```

Their adjacent audits record GREEN verdicts for those revisions.

## 1. Exhaustive overlap classification

Deleting a pole from the pentagonal bipyramid leaves `K_1 join C_5`, with
degree multiset

```text
(5,3,3,3,3,3).
```

Deleting a rim vertex leaves `overline(K_2) join P_4`, with degree multiset

```text
(4,4,4,4,3,3).
```

The common six-vertex induced graph `(K-a)-b=(K-b)-a` therefore determines
whether the two deleted vertices are poles or rim vertices.  Mixed roles
are impossible, so the proof's two cases are exhaustive.

In the pole case the common graph has one universal pole over one literal
five-cycle.  Both deleted vertices have exactly the stated rim contacts and
miss that common pole.  In the rim case the common graph is
`overline(K_2) join P_4`; its pole pair is the unique nonadjacent pair among
the degree-four vertices, so both representations identify the same two
poles and the same path up to reversal.  Restoring either rim vertex gives
exactly its two pole contacts and its two endpoint contacts.  The edge `ab`
is immaterial in both cases.

## 2. The two explicit `K_5` models

In the pole case, after deleting `x_5`, the sets

```text
{a,x_1}, {b,x_2}, {p}, {x_3}, {x_4}
```

are disjoint and connected.  The deleted pole vertices supply every
otherwise missing rim adjacency, `p` contacts the rim vertices contained in
the two nonsingleton bags, and `x_3x_4` supplies the last singleton contact.
All ten pairs are adjacent.

In the rim case, after deleting `x_2`, the sets

```text
{a}, {x_1}, {p}, {b,x_4}, {q,x_3}
```

are disjoint.  The last two are connected through `bx_4` and `qx_3`.
Pole--path contacts, the restored rim contacts and `x_3x_4` verify all ten
pairwise adjacencies.  Neither model uses its displayed deleted label.

## 3. Lift to the host graph

For either free label `r in {a,b}`, a `K_5` minor in `K-r` would lift
through the seven surviving connected columns.  Consuming `K_r` supplies
two disjoint adjacent connected roots, each adjacent to every surviving
column, so those roots complete an explicit `K_7`-minor model.

Consequently `K-a` and `K-b` are both `K_5`-minor-free in a surviving host.
The seven-column theorem applies separately to them.  If neither has a
vertex of degree at most three, both are pentagonal bipyramids.  The
abstract overlap theorem then gives some label `r` for which `K-r` has a
`K_5` minor.  The arbitrary-label consumption construction is available
for this `r`, and the same lift gives the forbidden `K_7` minor.  This
proves the host-level conclusion exactly as stated.

## Trust boundary

The theorem eliminates simultaneous pentagonal-bipyramid alternatives and
therefore guarantees one low-degree free-root choice.  It does not:

- turn a degree bound in the column-contact graph into a bounded separator
  of the host;
- identify the low-degree column as the target or a response source;
- split a path which encounters a root or an old column;
- synchronize the two shore colourings; or
- produce an exact-seven response or a strict order-eight response-side
  descent.

No unresolved assumption or gap remains in the stated theorem.
