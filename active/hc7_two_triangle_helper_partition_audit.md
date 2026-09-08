# Internal audit: the two-triangle helper partition

**Verdict: GREEN.**

**Source:** [the helper-partition reduction](hc7_two_triangle_helper_partition.md).

**Whole-source SHA-256:**
`dc3101172b266bbe69f02ef0ded4b1219cc0ec73930b137387710a8ee7f2def1`.

This separate internal mathematical audit covers the theorem, its explicit
terminal construction and its stated nonclosure. The final change from the
cold-read draft only replaces the pending-audit status. No finite enumeration
or external peer review is a premise.

The two input files were read at the hashes displayed in the source:
contraction closure `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`
and helper construction `0c1ac8052f7734d8d0267381c030e177bd70010eded63d15fdca8c0db6d1f375`.
Their adjacent GREEN audits pin those same bytes. The inherited
Norin--Totschnig input was not freshly inspected for this audit.

Deleting the literal four-clique `{v} union B` leaves a three-connected
graph. Every surviving vertex loses at most two neighbours by contraction
closure, so its degree remains at least six. For `F=G-v`, the exact degree
eight deletion gives `e(F)>=4|F|-4`; six-connectivity supplies the internal
four-connectivity hypothesis. Singleton normalization applies in this same
host. Adjoining `x` to either initial helper preserves connectivity through
its actual contact with that helper.

The fan proof does not require three distinct endpoints in `Y`. A cut of
capacity at most two deletes at most two vertices or source roots from `P`;
three-connectivity leaves a surviving source connected to the untouched
nonempty `Y`. Saturation of the three source arcs and unit vertex capacities
prevent another `A` root from being internal. Truncating at the first `Y`
vertex gives disjoint nonempty seeds in `P`. Connected growth partitions
all of `P`, retaining each seed's contact with `Y`. Literal `A` edges give
all three region-region contacts.

In the perfect-matching case, contracting one selected cross-edge makes
its bag adjacent to all four remaining core bags. Those four retain the
two triangle edges and two other matching edges, forming a four-cycle.
Thus the five core bags contain `W_4`, not merely a graph with the same
edge count. Both `Y` and `{v}` are full to these bags: use the fan for
`Y`-region contacts, actual `A` roots for `v`-region contacts and the
original root contacts for `B`. The edge `vx` joins the two apices.
Their union with the wheel is exactly the required `Q` subgraph of the
quotient, with independent missing pairs.

Absence of a perfect matching implies that some region has no private
`B` root. Donating it therefore preserves all three `B` contacts of the
two retained regions. Their literal `A` edge preserves connectivity;
the donated region's fan contact preserves connectivity of `Y`. The
result has exactly the claimed two-plus-one distribution of `A`, with
`x` still in `Y`, and disjoint ownership throughout.

For the final sufficient criterion, each of the two regions misses at
most one `B` root. Full combined support prevents a common missed root,
so the possible two omissions are independent and the five bags contain
the rooted wheel. This does not prove the required split exists.
Private supports can obstruct donation from an articulation branch of
`U`; no actual separator of `H` or decreasing exchange follows. The
remaining two-triangle case, Conjecture 19 and HC7 are still unresolved.
