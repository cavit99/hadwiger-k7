# GREEN: audit of the odd-cycle attachment counterexamples

**Status:** separate internal mathematical audit, 5 September 2026.
This is an internal agent audit, not external peer review. The auditor
participated in the earlier proof discussion and then checked the complete
recorded source separately; this was not a blind review.

**Audited source:** [the uniform counterexamples and canonical-model
lemma](triangle_free_bipartite_attachment_counterexample.md), whole-file
SHA-256
`252e475a4e4dba5867ae25101dac4b5f18fed5b3a174e6399fa1228e9c568f41`.

**Verdict: GREEN.**

No unresolved mathematical assumption or gap was
found in Theorems 1--2 or Lemma 3 at this revision. The proofs quantify
over every odd `ell>=5` and every subgraph, respectively. Neither theorem
depends on the finite verifier.

## Corrections checked before the verdict

Two stronger intermediate assertions were rejected during development
and source review. The audited revision uses the following valid repairs.

- When `C_v` is a singleton, its six host neighbours occupy its six
  target-neighbour bags. Two of these are cycle bags, so this alone does
  not place all four `T` vertices in `B` bags. What follows, and suffices,
  is that none lies in `C_p` or `C_q`. These two bags then cannot leave
  their roots. This correction was requested after reading the previous
  source revision, SHA-256
  `27be9e00eebf50b55b78b37e2ee6175b8a3d9bb50478c25bb2b3b848e055d4b4`.
- With one singleton `B` pair, an arbitrary left-port `A` bag can contact
  a small right `B` bag through a right port; such contact need not use a
  right `T` vertex. The proof instead assumes that the `A` bag has only
  two nonroots. Connectivity then restricts its second nonroot to `T_L`,
  or to `y_1` in the stated exceptional case. None supplies the contact.
  Thus the required lower bound of three holds without restricting larger
  bags or choosing their contact edges in advance.

## Uniform obstruction and unrestricted branch sets

The displayed paths have the prescribed distinct endpoints, alternate
their endpoint colours, and contain no other root. Consequently every
actual path-membership set has a common endpoint, including sets of more
than two paths. The vertex counts are `ell+6` roots and `ell+8` nonroots.

The nonroot graph is exactly the two stated `K_{3,2}` graphs, sharing
`z`, with the length-`ell` path between `v_L,v_R`. Every odd cycle must
use that entire path and a path of length at least four in the bipartite
portion. Hence its odd girth is `ell+4`. Target-adjacent roots have
distance exactly three: the supplied path gives the upper bound, and
triangle-freeness excludes a common neighbour.

The cycle count is valid for arbitrary bags. Nonempty singleton-index
sets have strictly more cycle neighbours; if no bag is singleton, using
only `ell` nonroots forces one per bag and a forbidden `C_ell` in the
nonroot graph. This yields `ell+1` without assuming colour-respecting
ownership or confinement to the cycle side.

The strongest inference is the ten-nonroot bound for the seven
bipartite-block bags. The singleton-pair reduction follows from the
identical three-element neighbourhoods and disjointness of the three
required `A` bags. With both pairs singleton the shared `z` belongs to
one `A` bag, and the other two contain left and right ports with neither
a root adjacency nor a common nonroot neighbour. The lower bound
`2+4+4` is therefore necessary. The corrected one-pair argument gives
`3+3+2+1+1`.

With no singleton pair, all seven bags are nonsingleton, so their total
excess over seven is nonnegative. Under the assumed budget of nine,
the three cases `b=0,1,2` are exhaustive. In the `b=1` case, the two
small `A` bags consume both vertices of one `T_D`; the small `B` bag
containing `p_D` has its entire neighbourhood in the other `B` bags and
those two `A` bags. It cannot contact the third `A` bag, regardless of
that bag's size or location. The other two cases follow from the exact
port-neighbourhood intersections. Extra cycle vertices create no
exception to these neighbourhood statements.

Finally, the perfect matching on `c_1,...,c_(ell-1)` forces `ell-1`
nonroots in bags disjoint from these seven bags. Both final counting
contradictions demand `ell+9` where only `ell+8` exist. Unused host
vertices, larger bags and arbitrary redistribution of nonroots are all
allowed by the argument. This is a direct construction, not a reduction
requiring an induction parameter or an unverified lift.

Every cycle and theta lies within a block. The cycle block has no theta,
and the bipartite block has no skewed theta. Thus the examples satisfy
the exact target conditions whose proposed sufficiency they refute.

## Canonical models for every subgraph

The primary [Kündgen--Pelsmajer--Ramamurthi
paper](https://arxiv.org/pdf/1207.6141), Definition 7.4, Proposition 7.5
and Corollary 7.6, was inspected. The source reproduces the sufficient
matching-and-shift construction with all prescribed roots preserved.
Its stated use of Theorem 4.2 for cycles also matches the primary source.

The matching-cover argument in Lemma 3 checks in both cases. If a maximum
matching leaves `v` unmatched, every minimum cover avoids `v`: equality
of cover and matching sizes forces each cover vertex to occupy exactly
one matching edge. Therefore each cover vertex is matched into the
specified `S`, and `N_H(S)=C`; precisely the odd cycle remains.

If every maximum matching saturates `v`, removing `v` decreases the
matching number by exactly one. The cover `C' union {v}` is minimum,
and the matching covers it from its complement. Adding the displayed
alternating cycle vertices gives exactly the stated neighbourhood, with
disjoint additional matching edges, and leaves precisely one edge.
The cyclic shift or endpoint swap supplies the respective remainder.

A subgraph omitting a cycle edge is bipartite; one retaining the whole
cycle is covered by Lemma 3. This includes nonspanning subgraphs,
disconnected bipartite components and isolated vertices. Thus the result
concerns every subgraph, not a finite list of canonical tests.

## Separate verification of the smallest example

The [retained verifier](triangle_free_bipartite_attachment_verify.py)
was read at whole-file SHA-256
`245f9645d4cb7761e749cfd3ffca0d76a46a359df14f2aeac636d1063d42a74d`.
Its pruning is complete for the checked inputs, for these reasons:

1. It enumerates every subset of nonroots for every prescribed root and
   retains exactly those connected to that root. Singleton subsets are
   included, other roots are excluded, and vertices may remain unused.
2. Every possible singleton-index set is considered. Stability and the
   distance-three lower bounds are necessary. Exact equality of host
   root degree and target degree, explicitly checked by `prepare`, forces
   exactly one neighbour of each singleton root into each adjacent
   target bag and none into any other bag. The singleton-domain filter
   therefore discards no model of these inputs.
3. Recursive filters enforce only disjointness, already required contacts,
   and necessary remaining-vertex budgets. Each domain stays compatible
   with all previously chosen bags. Its minimum-size and maximum-size
   bounds follow by summing necessary sizes of the other disjoint bags;
   they are not assumptions on branch-set shape.

The contact predicate checks root-to-nonroot and nonroot-to-nonroot
edges; there are no root-to-root edges. Returned positive certificates
receive an additional direct graph-traversal and contact check.

Running

```text
uv run python3 barriers/triangle_free_bipartite_attachment_verify.py
```

with the permitted temporary uv cache reproduced the positive canonical
`C_5` and attachment calibrations, the negative skewed-theta calibration,
and no rooted model for the 24-vertex example: 27 surviving singleton
cases and 1768 recursion nodes. The code and its pruning were checked
separately from the mathematical proof; this run is only a finite
diagnostic, not evidence from which the unbounded theorem is inferred.

## Scope of the verdict

The source refutes the two proposed sufficiency statements and
unrestricted attachment of a bipartite block to a contractible graph.
The necessity theorem and universal bipartite theorem remain intact.
No unrooted obstruction, Hadwiger result, T44 result or consequence for
spectral theorems is established. The audit supplies no external peer
review, novelty certification, or completion of the user's significance
objective.
