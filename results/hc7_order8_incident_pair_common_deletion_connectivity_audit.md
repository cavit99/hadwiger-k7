# Independent audit of the incident-pair common-deletion connectivity theorem

## Verdict

**GREEN** at the exact source revision

```text
fca23a393c3b912fabef6164a111244359f4ab72bc933676ba934d9ea0a1a283  results/hc7_order8_incident_pair_common_deletion_connectivity.md
```

This is a separate internal audit, not external peer review.

## 1. Connectivity dichotomy

If a set `T` of at most five vertices separates the common two-edge
deletion `H`, then `v` cannot lie in `T`, since otherwise `H-T=G-T`.
Moreover

\[
 H-(T\cup\{v\})=G-(T\cup\{v\})
\]

is connected by seven-connectivity.  Hence the only possible separated
component is `{v}`, so `N_H(v) subseteq T`.  Minimum degree seven in `G`
and deletion of exactly two incident edges force

\[
 5\le d_H(v)\le |T|\le5.
\]

Thus every inequality is equality and the displayed degree-seven
alternative is exact.

## 2. Chromatic and response conclusions

The graph `H` is a proper edge-deletion minor and hence is at most
six-colourable.  A five-colouring of `H`, followed by recolouring `v` with a
fresh sixth colour, would permit both deleted edges to be restored and would
six-colour `G`.  Therefore `chi(H)=6`.

In the low-connectivity branch, the opposite old full component supplies a
nonempty opposite open shore.  The `(=,not equal)` response from the unified
incident-pair theorem is proper on that shore and is rejected by the intact
singleton shore; otherwise the boundary partition would glue to a global
six-colouring.  The old operated component cannot itself be `{v}`, since it
is full to an eight-vertex boundary while `d_G(v)=7`.  The exact-seven
response is consequently a strict smaller-shore restart.

The six-connected conclusion does not keep a standard linkage disjoint from
the latent roots and columns.  The theorem correctly leaves that labelled
allocation open.

## 3. Root-provenance corollary

The named bypass support is connected, contains both outer endpoints and
avoids the operated centre `v`.  If deleting the opposite centre `w` leaves
an endpoint path in that support, the alternative free-root realization
turns every noncentral first root hit into a hit on the restored latent
column without changing either endpoint response label.  In the clean case,
truncating between the last visit to the first endpoint column and the first
subsequent visit to the second justifies the stated contact augmentation.

If no such path remains in the named support, `w` separates its endpoints.
Six-connectivity of the common deletion implies connectivity after deleting
`v,w`, and therefore supplies a centre-free endpoint path.  The proof
correctly does not assign the named bichromatic switches to this replacement
path.  Thus the only unresolved root-first case is the fixed-centre
provenance bottleneck, not an arbitrary root encounter.
