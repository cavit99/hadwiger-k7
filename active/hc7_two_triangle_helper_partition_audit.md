# Internal audit: the two-triangle helper partition

**Verdict: GREEN.**

**Source:** [the helper-partition reduction](hc7_two_triangle_helper_partition.md).

**Whole-source SHA-256:**
`5cdd75943fe3dd690986e699e69c24f585febfab78ed7d633df824d13f75b4c3`.

The original separate internal audit by `route_assessment`, retained below,
covered the theorem, its terminal construction and its stated nonclosure at
`dc3101172b266bbe69f02ef0ded4b1219cc0ec73930b137387710a8ee7f2def1`.
That revision differed from its cold-read draft only in the pending-audit
status. Its entire 90-line content is a byte-identical prefix of the current
source, checked against Git `2e2ba11`. A separate cold audit by
`literature_repair` covers the appended propositions at the current whole-source
hash; its verdict and scope follow the original review. No finite enumeration
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

## Separate audit of the coupled response

**Verdict: GREEN.** The new propositions and their final nonclosure were
read in full at the current source hash. Both imported sources and their
adjacent hash pins were rechecked; the helper normalization proof was reread.
No fresh primary-source inspection or independent external review is claimed.

The synchronized choice uses four distinct vertices and nonnegative degree
excesses: twice the sum of the two chosen excesses is at most the total
`2q`. The independent pair `a0,x` permits expansion of the actual star
contraction colouring to `G-v`. Exactly six other neighbours must use all
five remaining colours, so precisely one pair repeats. The two triangle
constraints give exactly the stated five- or six-colour alternative. Deleting
the three chosen vertices removes precisely two internal edges and gives the
asserted `4|F|-10` bound and actual four-connectivity.

Completing the four prescribed roots adds at least two edges. In the returned
rooted model, each added edge has its ends in two different prescribed root
bags. It can neither connect a bag internally nor witness any required helper
contact. Removing all added edges therefore leaves the model in the original
deletion graph; no minor relation for the augmented graph is needed.

The maximal-union, minimal-root-bag argument precedes the five-connectivity
step of the imported normalization. Two distinct helper-contact vertices in
a root bag permit a nonroot leaf transfer that enlarges a helper while
retaining both contacts. Hence each root bag has one actual port, shared by
both helpers; no unassigned component contacts their union. If any one of
`v,a0,x` missed the union, its entire original boundary would lie in the four
ports and the other two deleted vertices. The union and that missing vertex
survive this actual separator of order at most six. Thus all three deleted
vertices contact the union. Its required `v` contact places a remaining `A`
root in a helper; the literal `A` edge puts the other root, if outside, at
the unique port of its own root bag. Root singletonness is never inferred.

The second proposition quantifies over the absence of any rainbow triangle
colouring, then works in the single colouring just constructed. A swap on
one of two distinct `alpha,zeta` components makes the triangles rainbow;
swapping their common component when it omits `y` removes `alpha` from the
whole neighbourhood. Both contradictions are valid. The resulting component
contacts the five retained roots through the stated literal edges. The two
singleton-colour paths avoid both that component and the entire zero-colour
class. Removing their distinct terminal roots leaves one connected `a2` bag,
and the literal `b1b2` edge completes its disjoint rooted triangle.

These conclusions do not identify a Kempe component with a structural helper
or preserve its reserved vertices in an independently returned model. A
completion with two further root bags requires their mutual contact as well
as the specified triangle contacts; nonadjacent same-colour roots do not
supply it. Both the global allocation and the six-colour triangle alternative
remain open. No conclusion proving the two-triangle case, Conjecture 19,
HC7 or comparable mathematical significance is asserted by this audit.
