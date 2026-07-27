# Independent audit of the incident-bypass conflict split

## Verdict

**GREEN** for the exact source revision

```text
4b3f0eea1436d1337da1b842aaf07e56a4f81f888ed596b4bc8f03915bb1c297  results/hc7_order8_incident_bypass_conflict_split.md
```

This is a separate internal mathematical audit, not external peer review.
The intersection-safe recolouring, conflict-component structure,
edge-response signatures, same-colouring list obstruction and simultaneous-
contraction argument are valid under the stated hypotheses.  The theorem
does not align palette colours with the seven column labels or close the
order-eight two-full-component branch.

The direct dependency revisions checked were

```text
f1c9bb1131d2ea406c6e2d77395a0c45e3446adf43792aa986507427cd9642be  results/hc7_order8_unified_incident_pair_normal_form.md
5d5a5eda08701262a1bf6b821194aacd7192a41f0ecf997134764b5b59c80961  results/hc7_shared_interface_bichromatic_bypass.md
69044ccf85ccd3ec32ca118f11ddb1e673dade7fa7f7ac9d980b6b430ee5e228  results/hc7_near_k7_bipartite_total_contraction.md
```

## 1. Bypass hypotheses and intersection recolouring

The audited incident-edge bypass theorem supplies distinct alternate
colours `i,j` and the two named components `A,B` with exactly the exclusions
stated in (1.4).  Their palettes intersect only in colour zero, so every
vertex of `R=A cap B` has colour zero.  The named-vertex exclusions also
ensure that `R` contains none of the endpoints of the two deleted edges.

The revised proof correctly treats the assignments on `A-B` and `B-A` as
pointwise restrictions of the two named component switches, not as separate
Kempe interchanges.  Every colour-`i` neighbour of `R` lies in `A-B` and
every colour-`j` neighbour lies in `B-A`; all relevant edges occur in the
common deletion graph because the two omitted edges have only colour-zero
ends.  Those neighbours change to zero when `R` changes to `i`.

For an edge between `A-B` and `B-A`, the only possible new equality has an
old colour-`i` end and an old colour-`j` end.  These are exactly the edges
of `F=E_G(X,Y)`, and both ends become zero.  The outer endpoints change away
from zero while the common endpoint remains zero, so both incident edges
are restored properly.  If `F` were empty, the resulting assignment would
colour `G`, proving `F` is nonempty.

## 2. Induced conflict components

Although `kappa` colours the common deletion rather than `G`, the omitted
edges have only colour-zero endpoints and are not incident with `X` or `Y`.
Thus `X` and `Y` are independent in `G`.  Every `X-Y` edge is in `F` by
definition.  It follows that each nontrivial conflict component is an
induced connected bipartite subgraph of `G`, and distinct conflict
components are anticomplete.

## 3. Edge-response signatures

The constructed colouring makes every edge of `F` monochromatic.  For each
`f in F`, a colouring of the proper minor `G-f` makes the ends of `f`
equal; otherwise it would colour `G`.  Every other edge of `F` remains
present and proper, giving the singleton signature `{f}` on `G-F`.  An
empty signature would restore all of `F` and colour `G`.

Consequently restoring all of `F` is the unique noncolourable restoration
set: for any proper restoration subset, choose an omitted edge `f` and use
its singleton-signature colouring.

For any colouring of `G-f`, the ends of `f` must have one colour.  If they
were separated in a bichromatic graph using that colour and an alternate
one, switching the component containing only one end would make `f` proper
and hence colour `G`.  Thus every unit edge is linked in all `q-1`
alternate bichromatic graphs in its own unit colouring.  No common unit
colouring or boundary partition for different edges is inferred.

## 4. Same-colouring bilateral split

Let `U` contain all ends of conflict edges.  The restriction of `psi` to
`G-U` is proper.  For every conflict component, the displayed lists contain
zero because every edge from that component to the core is proper under
`psi`.

If every component were colourable from its lists, pairwise
anticompleteness would let those colourings combine with `psi|G-U` to
colour `G`.  Hence one fixed component is list-uncolourable.  The audited
poor-edge lemma applies to that component for every selected spanning tree.
Its two returned tree sides are nonempty, connected and adjacent, and
taking palette complements of their singleton list intersections proves
that both see every colour other than zero in the same fixed colouring
`psi`.

## 5. Simultaneous contraction and scope

All vertices of every conflict component have colour zero under `psi`, and
the only monochromatic edges are internal conflict edges.  Contracting
every component therefore produces a proper minor coloured by `psi`.

If that minor were `(q-1)`-colourable, each conflict component could be
expanded using its contraction colour on one bipartition class and one
common fresh colour on the other.  Outside neighbours avoid the contraction
colour, the fresh colour is absent outside `U`, and different components
are anticomplete.  This would `q`-colour `G`.  Thus the contracted minor has
chromatic number exactly `q`.

The qualification about contracting all components is essential and is
stated correctly: contracting only one component need not preserve `psi`
while other conflict edges remain monochromatic.

In a displayed two-shore separation, a unit edge with an end in one open
shore is absent only from that closed shore.  Its unit colouring therefore
extends through the intact opposite shore.  If the same boundary equality
partition extended through the intact operated shore, the two extensions
could be relabelled and glued to colour `G`.  Unit edges on opposite shores
with a common boundary partition would therefore give the terminal common-
partition outcome.  The source correctly does not assert that both shore
classes are nonempty or that their independently selected partitions meet.

The order-eight application matches its audited dependency exactly.  The
result retains the selected incident edges, common contraction colouring,
named components, individual switches and the derived conflict colouring.
It does not assign the five exposed palette colours to five distinct latent
columns, construct a labelled rooted `K_5`, produce a common boundary
partition, or force an order-seven or nested order-eight restart.  No
unresolved assumption remains within the theorem's stated scope.
