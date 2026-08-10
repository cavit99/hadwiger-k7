# Internal audit: Boolean coordinates at the minimum exact cut

**Verdict:** **GREEN** for the exact source revision below.

**Audited source:**
[`hc7_k7minus_boolean_minimum_separator_linkage.md`](hc7_k7minus_boolean_minimum_separator_linkage.md)

**Audited source SHA-256:**

```text
271549bf40b825aee557bfcaf47ee713215030dfe1ea55870340c22e14b7a024
```

This is a separate internal mathematical audit, not external peer review.
Independent passes reconstructed the minimum-separator linkage, the
lifted-order corner calculation, the endpoint-language classification and
both Kempe-lock arguments.  An adversarial pass separately searched for an
unsupported colour synchronization and produced the scoped odd-wheel
barrier cited by the source.  No unresolved gap remains in the stated
results.

## Pinned inputs

The proof uses these audited local sources at the displayed revisions:

- common colouring and simultaneous replacement cuts:
  `8c1c27b99edbd5b73ccc6254eafb10dfddeed62d3b271e4e8ba527783a08412a`;
- Boolean linkage coordinates and one-edge deletion:
  `c155030145a46a70c789302188a3220af2bf8ca5c537ad1c78d2325fa33946da`;
- fixed-trace minimum-side descent:
  `04d4585b25ce9fbd8f3392b715eb28caa7e4b008e45072ede2b08cbbf0bfecff`;
- lifted-order submodularity and exact uncrossing:
  `e7fcf00c9bdbd2fcbab78bb13d4244a659f4f7db0ae45a97cfbd9a8d599a0ee3`;
- the two-component normal form for order-seven cuts:
  `1041988a33b749bef5802dd21d3cd9419b5afc754735a20174bf5a13c0a56c96`;
- the clean paired-trace fan:
  `ad8a30f5e316fccdbc9319aa8788a00096c599656310ab10498246cdb2c0043c`.

The source repeats all new deductions rather than importing an unstated
strengthening of these inputs.

## 1. Centre-fixed linkage

For `P in mathcal B`, the exact-cut comparison gives `P subset D` and
`C subset O_P`.  Thus the chosen vertices `a in P-X(P,R)` and `b in C`
lie on opposite sides of every Boolean separator.  The Boolean linkage
theorem applies to any seven internally disjoint `a`--`b` paths and places
each literal edge `x_{uP}u` on its named path.

The old set `U dotcup T` is a second order-seven `a`--`b` separator.
Every one of the seven paths must meet it; internal disjointness gives seven
distinct intersections, so each path meets it exactly once and the paths
exhaust the separator.  The coordinate path already contains `u`, making
`u` its unique old-separator vertex.  The unreplaced-centre paths are
trivial between the two cuts, leaving the three `T_P` paths to meet the
three distinct vertices of `T`.

Before its old-separator hit, a truncated segment cannot enter `C`; after
the hit at `u`, the coordinate path cannot return to `D` without meeting
the old separator again.  This verifies both the `D`-interior assertion and
the suffix wholly inside `C`.  Different suffixes inherit internal
disjointness from the original path family.  First-hit truncation at a
connected support `Y` proves Corollary 2.2.  In the paired case the
`p`--`p'` path has nonempty interior because `pp'` is a nonedge, so its
interior is a legitimate choice of `Y`.

## 2. Entering-separator corner calculation

The old separation `p_0` has ordinary separator order three and is crossed
by all four centres.  The proposed separation `q` has ordinary order four
and is crossed by exactly three centres.  Hence both have lifted order
seven.  The vertices `c in C cap L_q` and `x_j in D cap R_q` are common
opposite anchors, so fixed-anchor uncrossing makes the meet and join proper
and of lifted order seven.

The three centres in `U-{w}` cross both inputs and therefore both corners.
For `w`, the input crossing indicators sum to one.  Equality in
lifted-order submodularity holds, so rootwise equality makes `w` cross
exactly one corner.  The ordinary corner-separator orders sum to
`3+4=7`; consequently the corner crossed by `w` has ordinary order three
and the other has order four.

If `w` has no neighbour in `R_q`, it cannot cross the join, whose right
open side is `D cap R_q`; hence the meet is the all-four-centre
three-separation.  Its selected open side is the nonempty proper set
`C cap L_q`, its selected closed side lies in the old closed `C`-side, and
`x_j` remains opposite.  The fixed trace therefore restricts and gives
strict trace-admissible descent.

If `w` has no neighbour in `L_q`, it cannot cross the meet.  The meet then
has a four-vertex ordinary separator crossed by the other three centres.
The root `w` belongs on the opposite open side of its minimum lift: it has
no left neighbour and has a neighbour in `D` because it crosses `p_0`.
The lifted boundary is exactly `(U-{w}) dotcup S_m`.  In both cases, the
critical-host two-component theorem turns the proper order-seven lift into
two full connected components.  This verifies all exactness and strictness
claims in Proposition 2.3.

## 3. Endpoint response language

For one coordinate, `x` has no neighbour in the opposite open side except
`u`.  Once the colours on `Q` are aligned, a right-shore colouring extends
over `x` precisely when its type at `u` can be assigned a palette colour
different from the coherent type of `x`.

If the type of `x` is a named boundary block, only that block is
incompatible.  If it is unused and `Q` uses five colours, the single unused
palette colour is incompatible.  If at least two palette colours are
unused, they can be permuted to make the endpoints different, so no type is
incompatible.  Since the intact coherent colouring makes `u,x` different,
its `u`-type is compatible.  Rejection at the `x`-boundary therefore
already implies rejection at the `u`-boundary; the two rejections are not
independent.  The five-block shape in the sole unused-colour case is
exactly the audited endpoint-type conclusion of the Boolean theorem.

## 4. Normalization and two-sided locks

Every six-colouring `kappa` of `G-ux` makes `u,x` equal, or it would extend
to `G`.  On `A_emptyset=P union T_P union U`, the neighbours of `u` are
contained in its unique `P`-neighbour `x` together with at most three
vertices of `T_P`; the other centres are independent.  At most four colours
are forbidden.  Recolouring `u` with an available colour different from
`alpha` gives a proper intact-side colouring `theta`.  Since `u` is absent
from `Q`, the two colourings agree on `Q`.  Restricting `theta` across the
Boolean family proves coherence and removes the empty-language case.

On `S_u`, the two traces differ only by the `alpha`--`beta` interchange at
`u`.  The singleton `{u}` is its own boundary two-colour component: properness
of `kappa` excludes an `alpha`-neighbour in `Q`, and the choice of `beta`
excludes a `beta`-neighbour there.  If the full left-shore two-colour
component met no other boundary component, switching it would reproduce the
`kappa` trace and glue to the right shore, contradicting `chi(G)=7`.
Therefore it contains an `u`--`Q` path with nonempty `L`-interior.  The
unique neighbour of `u` in `L` is `x`, so the first edge is literally
`ux`.  The symmetric switching argument under `kappa` gives the right-shore
lock.  Their interiors lie in disjoint open sides.

For `P subset D`, reversing the left lock and appending the centre-to-`C`
suffix is simple: the first part lies in `P subset D`, the second in `C`,
and they meet only at `u`.  Its possible `Q`-endpoint is the only reason the
source does not claim that `u` is the unique old-separator vertex on the
entire prefix.

## Scope and unresolved obligation

The source proves path anchoring, an exact entering-separator criterion, a
complete one-coordinate type language, one aligned order-six partition and
two local Kempe locks.  It does not identify the normalized edge-deletion
colouring with the fixed exact-`U` colouring trace used to choose `C`.
Nor does it prove `u in W_C`, root the spanning `K_6` model, orient the
component excess into `C`, synchronize two different edge-deletion
colourings, eliminate any of `2K_2,P_4,C_4`, or prove the conjecture.

The next valid target is therefore fixed-trace and composable.  No audit
claim promotes the local normalization or the uncoloured suffix to that
missing synchronization.
