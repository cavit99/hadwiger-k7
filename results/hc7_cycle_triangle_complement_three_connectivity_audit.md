# Internal audit of the cycle-complement three-connectivity theorem

**Verdict: GREEN.**

Date: 8 September 2026. This is a separate internal mathematical review,
not external peer review. The reviewer checked the complete final proof
and previously suggested its uniform formulation of the three flow cases;
the adjacent second audit separately checks that formulation.

Audited source: [three-connectivity theorem](hc7_cycle_triangle_complement_three_connectivity.md).
Whole-file SHA-256:
`4e2b5b0b7b7294c30bdcdd1b4f147d12ba535dc3513508981160c5173d519228`.

The theorem holds with exactly its structural hypotheses: seven-connectivity,
minimum degree eight, exclusion of `Q`, the specified degree-eight vertex,
and the cycle/triangle decoration with at most one cross-edge. Chromatic
criticality is not assumed. Its conclusion is three-connectivity of `G-v-C`,
not completion of the cycle case.

## Inputs and strongest checks

The two invoked sources match their adjacent GREEN audits:
the exterior theorem at
`6c5196ea71f77a1426d8bc24ef040e7fe85805ac0cb784d2d62d152a67303eb3`,
and the designated-root almost-clique theorem at
`de183e350c412739c05a744e811304454ba90856efee9e097813c70617bba9cd`.
The latter permits an arbitrary advance choice of the triangle root at
which its sole possible missing contact occurs. No finite test is used.

- **Actual cut sides.** At a putative cutvertex, any component avoiding
  the surviving triangle has boundary in the five cycle vertices and that
  cutvertex; `v` survives outside. At a two-cut `T`, every other component
  than `K` lies in `B`, and `C union T` is an actual seven-cut. All its
  components are full to the cut. If there are two exterior components,
  the displayed three connected bags are disjoint, pairwise adjacent and
  full to the cycle, including when `T` meets the triangle.
- **Uniform flow bound.** For `k=|T-A|`, deleting all `k+1` source roots
  costs `2k+2`. A smaller weighted vertex separator leaves a source in a
  reachable set with no sink terminal. Its original neighbourhood lies
  in the separator plus `v` and `T cap A`, at most `k+4<=6` actual vertices;
  `L` survives on the other side. Source or terminal cuts in the standard
  split network correspond to deleting those same vertices. This proves
  the required integral flow bound for all three values of `k`.
- **Prescribed endpoints survive augmentation.** The initial `k` paths
  lie in `K union (T-A)` and can be shortened at their last source roots.
  A simple residual augmenting path cannot leave the sink, so it never
  reverses an occupied terminal-to-sink arc. All required endpoints remain.
  At full flow every source vertex's capacity two is saturated by its own
  starts; another path cannot traverse it internally. Sink-only terminals
  exclude internal cycle or cut roots. Integer augmentation terminates.
- **The shared-source repair stays on the correct side.** When both cut
  paths start at `a_1`, their tails include both vertices of `T`. The four
  other paths are truncated before their cycle endpoints, so both bridge
  endpoint sets lie in `J-a_1`. A shortest bridge avoids all six paths
  internally. An excursion into `L` would require an internal encounter
  with `T`, already in its first endpoint set; hence the bridge stays in
  `K union T`. The new source prefix, bridge and cut-path suffix avoid the
  retained other cut path and the untouched family's two cycle paths.
- **Root preservation and terminal contacts.** The chosen matching of
  two cycle edges keeps the two `D` contacts in distinct pieces. On the
  `L` side each set boundary loses at most two vertices, while each degree
  loses at most one; the exact almost-clique hypotheses therefore hold.
  The additions to the `T` bags lie in `K`, are mutually disjoint, and
  avoid both the side model and `D`. The three triangle roots are allocated
  separately to those two bags and `D`. Their literal edges supply both
  `D` contacts, and `v` contacts all six other bags. Choosing the designated
  cycle root among the two contacted by `D` makes the two possible missing
  pairs independent. Extra contacts do not impair the `Q` model.

## Remaining obligations

No substantive gap was found. The fixed cycle contractions have explicit
disjoint original-host preimages; no quotient criticality or recursive
connectivity assumption is used. The result excludes every two-cut of `J`.
It does not supply the simultaneous full-contact helper partition splitting
the triangle, settle the other neighbourhood configuration, or prove a
global six-colouring conjecture.
