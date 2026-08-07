# The remaining `K_7^-`-to-`K_7` upgrade

**Status:** sole active mathematical target.  The `K_7^-` six-colour
conjecture and the seven-connected `4n-2` extremal theorem are proved in this
repository with a separate internal GREEN audit.  `HC_7` remains open.

Here `K_7^-` is `K_7` with one edge deleted.  Internal audit is not external
peer review.

## 1. New entrance

Let `G` be a hypothetical minor-minimal non-six-colourable graph with no
`K_7` minor.  Standard contraction-critical theory makes `G`
seven-connected.  The proved
[exact-six-connectivity closure](../results/hc7_k7minus_exact_six_connectivity_closure.md)
and its six-colour corollary imply that `G` contains a `K_7^-` minor.

Choose a spanning labelled model

\[
                         A,B,R_1,R_2,R_3,R_4,R_5       \tag{1.1}
\]

whose only unrequired adjacency is `AB`.  Enlargement to a spanning model
preserves every existing model edge.  Since `G` has no `K_7` minor, the
bags `A,B` are genuinely anticomplete in every terminal labelled model of
this form.

The density programme is therefore complete.  The remaining problem is
purely label-sensitive: repair the single missing branch-set adjacency, or
use the obstruction to six-colour the host.

## 2. Active target

> **Labelled missing-edge repair theorem.**  In the setup above, at least
> one of the following occurs:
>
> 1. the labelled model can be rerouted or split to produce a `K_7` minor;
> 2. an actual order-seven separation is exposed together with one exact
>    boundary equality partition realised by both closed shores;
> 3. there is a proper-minor operation with a label-faithful response which
>    gives a strict same-host descent in a declared literal shore or carrier
>    parameter; or
> 4. a two-vertex set meets every `K_5` minor, which directly yields a
>    six-colouring by the known `t=5` case of Hadwiger's Conjecture.

The first outcome is the desired clique minor.  Each of the other three
outcomes contradicts the choice of a minor-minimal seven-chromatic host.

The theorem is deliberately stated over a **spanning labelled** model and
requires proper-minor response data.  Connectivity and static branch-set
contacts alone admit sharp six-colourable two-apex and planar-web
architectures.

## 3. Selected audited inputs

The decisive proved entrance is:

- [exact-six-connectivity closure and `K_7^-` six-colour theorem](../results/hc7_k7minus_exact_six_connectivity_closure.md).

Reusable frozen toolkits include:

- the [bounded-interface synchronization frontier](hc7_bounded_interface_synchronization_frontier.md);
- the [degree-seven model/separator frontier](hc7_degree7_model_separator_frontier.md);
- the audited labelled near-clique and exact-seven results indexed from
  those frontiers.

## 4. Immediate barriers

The active target must retain contraction-critical operation states because:

- reversible labelled rotations need not admit a size-only rank;
- a separator supported by five branch bags can have unbounded order under
  geometry alone;
- static exact boundary traces need not synchronize across the two shores.

These are methodological barriers, not counterexamples to the active theorem.
They are preserved in [`../barriers/`](../barriers/).

## 5. Acceptance criterion

Progress on this frontier must close the missing adjacency in the full
minor-critical host.  Additional unrooted near-clique models, local contact
counts, or finite boundary lists do not count unless they produce one of the
four active-target outcomes above.

The next proof should start from the guaranteed spanning `K_7^-` model and
choose a lexicographically minimal deficient pair of bags.  A blocked
label-preserving split should be converted into an actual exact-seven
response interface or a strict carrier descent.  The old density-safe shore
machinery is now optional: density is no longer the obstruction.
