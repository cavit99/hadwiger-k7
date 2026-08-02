# Internal audit: exact `K_7^\vee` separator dichotomy

**Verdict:** GREEN for Theorem 1 and Corollary 2.  The proof gives either an
explicit `K_7^-` minor model or an actual nested separator, and the corollary
preserves the named two-edge response.  It does not terminalize the separator.

**Audited source:**
`results/hc7_k7minus_exact_k7vee_separator_dichotomy.md`

**SHA-256:**

```text
4845f5375581971aca7397bbac0e3eb930dd2943c9dca71f6264a24e2fa31c6e
```

This is a separate internal mathematical audit, not external peer review.
The proof was also cold-checked independently against the retained-core and
opposite-gate antecedents.  No finite computation is involved.

## 1. Initial separator and duplicate portal

Because the seven branch sets span the graph and `X` is anticomplete to
`B,C`, every neighbour of `X` lies in one of the four universal bags.  The
connected bag `B` lies outside `X` and its open neighbourhood, so
`N_G(X)` is an actual separator.  Seven-connectivity gives at least seven
boundary vertices and hence two distinct `X`-portals in one universal bag.

## 2. Avoidable retaining core

Let `T` be a retaining core through one selected portal and let `Y` be the
component of the donor minus `T` containing the other.  Every other
component of the donor minus `T` attaches to `T`, so `U-Y` is connected.
It retains all five foreign adjacencies.

If `Y` meets a missed twin, adjoining `Y` to that twin and retaining `U-Y`
gives six mutually adjacent foreign branch sets.  The deficient bag meets
the enlarged twin, `U-Y`, and the other three universal bags.  Together
these are seven disjoint connected branch sets with only the other deficient
bag--twin pair possibly absent.  This is an explicit `K_7^-` model.

If `Y` misses both twins, either twin is a nonempty far side of `N_G(Y)`.
Thus the returned neighbourhood is an actual separator, and the donor
complement remains connected as claimed.

## 3. Opposite unavoidable gates

When every retaining core based at either selected portal contains the
other, the two canonical opposite gates are nonempty, connected, have
connected complements, and are disjoint.  If a gate had empty monopoly set,
its connected complement would itself be a retaining core avoiding the
opposite portal.  Hence both monopoly sets are nonempty.  A portal set cannot
be contained in two disjoint gates, so the monopoly sets are disjoint.

If a gate misses a twin, its open neighbourhood is again an actual
separator.  Otherwise both gates meet both twins.  Their disjointness then
prevents either twin label from belonging to either monopoly set.  The two
nonempty disjoint monopoly sets lie among only three neutral universal
labels, so one has order one.

For that gate `Z`, the branch sets

```text
U-Z,  X union Z,  B,  C,  and the three other universal bags
```

are disjoint and connected.  The first two meet across the donor cut; the
enlarged deficient bag meets both twins through `Z` and the neutral bags
through `X`; and `U-Z` loses at most the unique monopolized adjacency.
Thus at most one of the twenty-one branch-set adjacencies is absent.

## 4. Separator order and fullness

Every returned open neighbourhood has order at least seven by
seven-connectivity.  At exact order seven, if a boundary vertex missed a
component of the deletion, the other six boundary vertices would separate
that component.  Hence every component is adjacent to every boundary
vertex.

## 5. Fixed-response corollary

The surviving labelled model supplies at least one retained portal in each
universal bag, and five retained portals force a duplicate.  Repeating the
theorem with those retained edges makes every minor-model construction lie
in the edge-deleted graph.  In a separator outcome, restoring the two
incident edges can add only `r` to the selected donor piece's boundary.
The piece already meets `X`, and a missed twin remains a far side, so its
open neighbourhood in the original graph is still an actual separator.
No recolouring occurs; the fixed six-colouring remains attached to the
outcome.

## 6. Exact scope

The separator can have order greater than seven.  Its boundary need not be
the neighbourhood of a degree-eight exceptional vertex, and the deleted
edge endpoints need not lie in opposite open shores.  The result therefore
does not itself give a six-colouring, a smaller exceptional
anti-neighbourhood, Conjecture 21, or `HC_7`.
