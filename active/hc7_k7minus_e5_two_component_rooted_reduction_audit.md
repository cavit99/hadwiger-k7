# Internal audit: two-component rooted reduction

**Verdict:** GREEN for the pinned source revision.

The audited source is
[`hc7_k7minus_e5_two_component_rooted_reduction.md`](hc7_k7minus_e5_two_component_rooted_reduction.md),
with SHA-256

```text
e77dded1d9459f167f1f636832f9c4b46633172f8f8272b478cdf3f834fbc940
```

The audit checks an unbounded reduction in a minimum exact-density `E5`
enemy.  It does not certify `(E5)` itself.

## 1. Accounting and inherited rooted model

For two components `A,B` behind a five-cut `S`, the edge partition is

```text
|E(G)|=|E(J)|+4|A|+delta_A+4|B|+delta_B,
|V(G)|=|A|+|B|+5.
```

Substitution of `|E(G)|=4|V(G)|-7` gives

```text
delta_A+delta_B=13-|E(J)|.
```

Lemma 1 is a legitimate reuse of the rooted six-bag supply theorem.  The
proof of that theorem uses only the internally five-connected pair formed
by one lobe and `S`; no third component enters either its density count or
its fifth-root augmentation.

## 2. Cross-root branch-set check

In the `A`-model, the five boundary-bearing bags are the four root bags
and the helper `U_x` containing `x`; the residual helper `V_A` contains no
boundary vertex.  The analogous statement holds in the `B`-model.  Since
the open lobes are disjoint and anticomplete, corresponding
boundary-bearing bags intersect exactly in their named boundary vertex.
Thus the five unions `M_s` are connected, disjoint, and disjoint from
`V_A,V_B`.

All twenty required adjacencies of a `K_7^-` model were checked by type:

| pairs | number | source |
|---|---:|---|
| among the five `M_s` | 10 | `U_x` supplies the four pairs at `M_x`, `U_y` the three new pairs at `M_y`, and the literal triangle the remaining three |
| `V_A` to the five `M_s` | 5 | one helper edge and four root--helper incidences |
| `V_B` to the five `M_s` | 5 | symmetric |

The sole unrequired pair is `V_A V_B`.  No virtual root edge is used in
this composition.  Theorem 2 is therefore terminal and correct.

## 3. Star completion

If every missing boundary edge has common end `t`, one connected subgraph
of the opposite full lobe can be absorbed into `t` and can meet every
other missing-edge end.  This realises all missing edges simultaneously;
it does not require disjoint paths.

The completed closed shore is five-connected.  Any component after
deleting at most four vertices which avoided the surviving boundary clique
would be a nonempty subset of the selected open lobe with at most four
neighbours in `G`.  Every component therefore meets the nonempty surviving
clique and all are joined.

The completed minor has order `c+5` and size

```text
4c+delta_C+10>=4(c+5)-7
```

when `delta_C>=3`.  It is proper and target-free because it is a minor of
`G`.  The minimum-enemy contradiction is valid.  For
`J=K_4 dotunion K_1`, the excess sum is seven, so the stated application
has a lobe of excess at least four.

## 4. Whole-component contraction

Contracting a full connected lobe `B` replaces all its internal and
boundary edges by the five edges from the contracted vertex to `S`.
Using the excess identity gives

```text
|V(G/B)|=|A|+6,
|E(G/B)|=4|A|+18-delta_B.
```

Thus `delta_B<=1` places the contraction at or above the `E5` threshold.
When `|B|>=2`, it is a proper target-free minor and so cannot remain
five-connected.

Every cut of order at most four in the contraction contains the contracted
vertex: otherwise it would lift unchanged to a cut of `G`.  Deleting that
vertex leaves a set `T` of order at most three, and the remaining graph is
exactly `G[A union S]-T`.  A component avoiding `S-T` would lie in `A`
and have all its neighbours in `T`, contradicting five-connectivity.
Theorem 4 follows.  If `B` is a singleton, simplicity and fullness give
exactly five incident boundary edges and excess one.

## 5. Two--three linkage at excess at least two

For missing boundary edges `ab,ac,de`, Du--Li--Xie--Yu Theorem 1.2 is
applied with the triple `{a,b,c}` and pair `{d,e}`.  A nonempty obstruction
set lies in the open lobe `D` and has at most four neighbours there; because
`D` has no neighbours outside its closed shore, this would contradict
five-connectivity of `G`.  In the empty-obstruction case the theorem's
completed root graph has at most `4v-10` edges if it is infeasible.

The source's competing count is exact:

```text
|E(G[D union S]+{ab,ac})|=4|D|+delta_D+9.
```

Since the closed shore has `|D|+5` vertices, `delta_D>=2` exceeds the
infeasible bound by at least one edge.  Feasibility therefore gives a
`d`--`e` path disjoint from `{a,b,c}` and, in its complement, a path from
`a` to one of `b,c`.  Contracting the initial segments specified in the
source creates two distinct missing boundary edges by disjoint branch
sets.

The retained opposite shore has boundary `K_5^-` and size

```text
4|C|+delta_C+9>=4|C union S|-7
```

when `delta_C>=4`.  Its five-connectivity argument is sound.  Every
component after deleting at most four vertices meets the surviving
boundary.  The only disconnected residual of `K_5^-` consists of the two
ends of its missing edge; separating those ends would, after adding one of
them to the deleted set, isolate a nonempty subset of `C` by at most four
vertices in `G`.  Thus the constructed proper minor is a smaller `E5`
enemy, giving the claimed contradiction.

The threshold is sharp for this method.  If `D` is a path whose vertices
all see `a,b,c`, with its ends additionally seeing `d,e`, then
`delta_D=1`.  The completed shore has exactly `4v-10` edges, and any
connected support meeting all of `a,b,c` intersects the unique
`d`--`e` route.  This verifies the recorded diagnostic obstruction but
does not construct an `E5` enemy.  The source correctly leaves the
high-lobe coupling at excess one open and does not invoke the conjectural
leafified-tripod strengthening of Xie's theorem.

## 6. Scope and unresolved inference

The source correctly stops at the three-separation returned by a failed
whole-lobe contraction.  Such a component contains boundary roots; its
interior need not remain connected after those roots are removed, and the
excess need not stay on the smaller side.  The claimed five-root reserve
lemma is therefore an open repair, not an inferred theorem.

The source also correctly distinguishes its cross-root theorem from the
existing one-terminal composition, whose seventh bag is a third singleton
component, and from three-packet quotient results, which likewise require
a third full component.
