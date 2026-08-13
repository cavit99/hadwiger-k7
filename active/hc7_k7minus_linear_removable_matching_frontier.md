# Linear removable-matching frontier

**Status:** current structural frontier on branch
`feature/linear-removable-matching`.  The promoted theorem is
[`../results/hc7_k7minus_linear_removable_matching.md`](../results/hc7_k7minus_linear_removable_matching.md).
It does not prove Conjecture 21 or `HC_7`.

## 1. Global entrance

Let `G` be a hypothetical minor-minimal non-six-colourable
`K_7^-`-minor-free graph of order `n`.  There is a matching `M` such that

\[
 G-M\text{ is seven-connected},\qquad
 |M|\ge\left\lceil\frac{5n+59}{28}\right\rceil,
\]

and `V(M)` is a feedback vertex set.  On the common graph `G-M`, every
nonempty equality signature on `M` occurs and the empty signature does not.

Since `n>=25`, every hypothetical counterexample therefore has a
seven-edge submatching `N` for which

\[
 G-N\text{ is seven-connected},\qquad
 |E(G-N)|\ge4|V(G)|-7,
\]

the complete punctured seven-cube occurs, and a spanning exact
`K_7^vee` model is present.

This supersedes the former need to enter through a six-coordinate forest
whose deletion might have connectivity six.  The old matching and induced
`P_3` six-cut rows remain valid conditional theorems but are no longer an
exhaustive entrance for a hypothetical counterexample.

## 2. Operation-labelled separator abundance

Partition a maximal removable matching into five-edge blocks.  Every block
has a seven-connected deletion host at the Norin--Totschnig threshold.
Endpoint-visibility optimisation in an exact `K_7^vee` model gives either
`K_7^-` or one actual separator retaining a literal matching edge and its
singleton-signature rejected trace.

Thus a target-free critical host has linearly many distinct coordinate
edges carried by response-bearing actual separations.  The exact models
and separators returned by different blocks need not coincide.

## 3. Immediate global target

The next theorem should use this abundance rather than restart a bounded
kernel classification.

> **Multi-response separator coupling target.**  Let `e_1,...,e_s` be
> distinct edges from disjoint five-edge blocks of one maximal
> seven-removable matching, and let `Y_i` be their operation-labelled
> response sides.  Then either:
>
> 1. `G` contains `K_7^-`;
> 2. two exterior traces induce one common boundary partition and colour
>    `G`; or
> 3. an exact model can be selected for two blocks so that the two
>    coordinate responses yield a common labelled split.

A successful theorem of this kind would spend a genuinely new resource:
many independent proper-minor operations on one fixed feedback endpoint
set.  One-donor minimisation, fixed-lock transfer and static ownership have
already been exhausted and should not be reused as the engine.

## 4. Scope

The linear matching theorem is a global, computation-free structural result.
It does not bound the response separators from above, synchronize their
traces, or eliminate the critical host.  Those remain the proof obligation.
