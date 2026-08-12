# Prescribing a five-centre matching edge and the exact-kernel limitation

**Status:** active written lemma; self-audit adjacent; and computer-assisted
finite route diagnostic.  The lemma is unbounded and computation-free.  The
diagnostic is not a promoted theorem because the exact order-eight catalogue
has not received an independent audit.  Neither result closes the dominated
degree-eight case, the eight-coordinate branch, or `HC_7`.

This note separates two facts.  A supported neighbour of one exceptional
centre may be prescribed as that centre's representative without losing the
common five-edge response cube.  However, even granting the strongest
possible rooted-bag adjacency from such a representative does not eliminate
all exact order-eight protected-centre quotient residues.

## 1. A prescribed representative

Let `G` satisfy the critical-host hypotheses used by the audited
[common five-centre matching theorem](../results/hc7_k7minus_five_centre_common_matching_reduction.md),
and let `Z` be its five independent degree-eight centres.  For `z in Z`, put

\[
 \mathcal I_z=\{I\subseteq N_G(z):|I|=3\text{ and }I\text{ is independent}\},
 \qquad K_z=\bigcap_{I\in\mathcal I_z}I.              \tag{1.1}
\]

The exceptional-neighbourhood theorem gives
\(\mathcal I_z\ne\varnothing\).

### Theorem 1.1 (prescribed matching representative)

Fix `w in Z` and

\[
                         y\in N_G(w)-K_w.              \tag{1.2}
\]

The independent triples and representatives in the common-matching theorem
may be chosen so that

\[
                         x_w=y.                        \tag{1.3}
\]

In particular the five edges

\[
                         M=\{zx_z:z\in Z\}             \tag{1.4}
\]

still form a matching, and the proper six-colourings of `G-M` have precisely
the nonempty equality signatures on `M`.  The singleton signature at `wy`
may be taken from the star contraction at `w`, so `wy` is its sole
monochromatic restored edge.

#### Proof

Because \(y\notin K_w\), choose \(I_w\in\mathcal I_w\) with
\(y\notin I_w\) and put \(R_w=N_G(w)-I_w\).  Then \(|R_w|=5\) and
\(y\in R_w\).  For each other centre `z`, choose any
\(I_z\in\mathcal I_z\) and put \(R_z=N_G(z)-I_z\); again
\(|R_z|=5\).

Prescribe `x_w=y`.  For the four remaining centres consider the sets

\[
                         R_z-\{y\}\qquad(z\in Z-\{w\}). \tag{1.5}
\]

Each has order at least four.  Hence the union of every nonempty subfamily
of `k<=4` such sets has order at least four, and therefore at least `k`.
Hall's theorem gives distinct representatives for the four sets, all
different from `y`.  Together with (1.3) these are distinct representatives
of all five `R_z`.

The centres are independent, so no representative is a centre and the five
edges in (1.4) form a matching.  The proof of the common-matching theorem
uses no further property of the representatives.  Contracting any nonempty
subset of `M` gives every nonempty equality signature, while the empty
signature would six-colour `G`.  For the singleton at `w`, contract the star
on \(\{w\}\cup I_w\); the five vertices of `R_w` receive five distinct
colours other than the colour on `I_w`.  Assigning `w` the colour of `y`
makes `wy` the unique monochromatic restored edge. `\square`

The exclusion of `K_w` is exact for this proof method: a vertex in `K_w`
belongs to every available independent triple, so it cannot lie in the
corresponding five-set `R_w`.

## 2. Application to a protected eight-terminal kernel

Retain the connected dominated degree-eight configuration with adjacent
vertices `u,v`, seven common neighbours

\[
                         Q=N_G(u)-\{v\},               \tag{2.1}
\]

and one of the other exceptional centres `w` in the five-connected graph
`G-\{u,v\}`.  Apply the exact eight-terminal kernel construction to the
eight roots `Q union \{w\}`.  Label `w` by `7` and the members of `Q` by
`0,...,6`.

If a prescribed representative `y` lies in the bag rooted at `q in Q`, the
edge `wy` gives an actual adjacency between the `w`-bag and the `q`-bag.
When that adjacency is absent from the retained kernel quotient, restoring
it adds the rooted edge `wq`.  Thus the strongest conclusion obtainable
from the representative edge at quotient level is to add one arbitrary
missing edge incident with root `w`.

The deterministic diagnostic
[`probe.py`](experiments/dominated_singleton_exact_eight_kernel_absorption/probe.py)
tests exactly this generous implication after the protected `w`-bag is
absorbed into an adaptive neighbouring `Q`-bag.

### Diagnostic 2.1 (an extra protected-root edge is insufficient)

The exact order-eight screen has 425 failed protected-centre compositions,
distributed over the three surviving graphs on `Q` as

\[
                         210,\qquad74,\qquad141.       \tag{2.2}
\]

For each failure, add in turn every missing edge from root `w` to a member
of `Q`.  The number of additions which close the quotient has the following
distribution:

```text
Q type                         0    1    2    3    4
C5 disjoint union K2          30    0   80   40   60
C5 with a pendant 2-path       6    0   24   18   26
C7                             15   28   35   14   49
```

Consequently 51 of the 425 failures resist every possible extra
protected-root edge.  They have precisely two degree profiles:

```text
carrier degree sequence       degree of w       count
(3,3,3,3,3,3,3,5)                 5              38
(3,3,3,3,3,3,3,7)                 7              13
```

For the second profile there is no missing edge at `w`; for the first,
neither of the two missing edges closes.  Exact deletion-contraction minor
search verifies each `K_5^-` decision.

This is a **recorded negative finding / route nonclosure**, not a graph
counterexample to a host theorem.  The quotient records do not assert
seven-chromaticity, minor-criticality or the full response family.  The
underlying exact order-eight catalogue is a deterministic discovery census
whose generator has not received an independent audit; only the analytic
order-ten part of that catalogue has an independent GREEN audit.  The
counts in Diagnostic 2.1 must therefore not be cited as a promoted
computer-assisted result.

## 3. Exact first unsupported inference

Theorem 1.1 resolves the matching-selection quantifier: once a literal
neighbour `y in N(w)-K_w` is identified, it can be made the matching mate of
`w` while retaining all 31 nonempty five-edge signatures.

It does not identify the branch-set location of `y`.  For any one exact
kernel lift, all of `N(w)-K_w` may lie in the `w`-bag, or may lie only in
rooted bags whose adjacency to the `w`-bag is already represented.  Even if
one such neighbour produces a new rooted edge, Diagnostic 2.1 shows that
this operation cannot close the 51 resistant quotient records.

Nor may one simply change the protected centre.  For the four available
centres the rooted theorem gives the quantifiers

\[
             \forall w\in Z-\{u\}\quad
             \exists\text{ an exact kernel model rooted at }Q\cup\{w\}.
                                                               \tag{3.1}
\]

Those four models need not have common branch sets, so their matching mates
cannot be compared as four placements in one quotient.

The first unsupported positive inference is therefore

\[
 \begin{gathered}
  \text{a protected centre }w,\text{ its selectable neighbours, and an exact}\\
  \text{kernel model rooted at }Q\cup\{w\}
 \end{gathered}
 \Longrightarrow
 \begin{gathered}
  \text{a supported matching mate in a useful foreign bag, or a}\\
  \text{response-preserving internal split of the }w\text{-bag}.
 \end{gathered}                                        \tag{3.2}
\]

For 374 of the 425 diagnostic failures at least one missing protected-root
edge would close, so a branch-set-location theorem of the first kind would
settle those finite records.  The 51 resistant records require more than
one representative adjacency: a response-sensitive split, another
simultaneously rooted operation endpoint, or a labelled response
separation.  Matching re-choice alone cannot eliminate the protected-centre
order-eight residue, and the 803 order-nine records have not been tested by
this extra-edge refinement.

## Dependencies and scope

- [the common five-centre matching and response cube](../results/hc7_k7minus_five_centre_common_matching_reduction.md);
- [direct star visibility and the sets `K_z`](../results/hc7_k7minus_dense_branch_rotation_visibility.md);
- [the eight-terminal rooted-carrier theorem](../results/hc7_eight_terminal_rooted_carrier_trichotomy.md); and
- [the exact eight-terminal catalogue draft](hc7_eight_terminal_exact_bundle.md).

Theorem 1.1 may be used independently of the finite diagnostic.  The latter
only prevents repetition of a representative-only quotient attack.
