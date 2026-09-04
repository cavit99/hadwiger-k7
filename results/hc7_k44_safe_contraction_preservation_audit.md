# Internal audit: safe literal-core contractions

**Verdict:** GREEN for Lemmas 1, 3, 5, Theorem 2 and Corollaries 4, 6.
Sections 4 and 5 correctly distinguish a missing induction implication from
a counterexample to unconditional preservation. This is separate internal
review, not external peer review.

**Audited source:** [safe literal-core contractions](hc7_k44_safe_contraction_preservation.md).
**Whole-file SHA-256:**

```text
b62fe795c22992858da26ca5eba12e3886b960d782edcf4e5dbaf9cf40ca8ac5
```

## Proof checks

- In Lemma 1, a component missing the core has its full neighbourhood in
  the deleted set, contradicting the labelled inequality. If both shores
  survive they lie in one component. Otherwise four deletions remove a
  whole shore and at most two meet the exterior; three-connectivity leaves
  the exterior connected. Independence of the other shore reduces any
  further component to an isolated vertex, excluded by its degree.
- An exterior contraction changes a core degree by at most one and keeps
  the induced core unchanged. These facts prove Theorem 2 using Lemma 1.
- Lemma 3's two disjoint mixed core pairs and four singleton core vertices
  have every required `K_6^-` adjacency. The connected exterior is adjacent
  to each bag through a core vertex's exterior neighbour. Extra core edges
  can only add adjacencies.
- In the critical application, minimum degree eight ensures all core
  vertices have exterior neighbours. The resulting induced core gives an
  independent four-set in every core neighbourhood. Dirac's inequality
  raises the core degree bound to nine. Thus core degrees remain at least
  eight after the first contraction and at least seven after the second.
- Lemma 5's uncontracted vertex originally has degree exactly eight; any
  independent four-set lifts, replacing the contracted vertex by an
  adjacent endpoint if necessary. At the contracted vertex, both endpoints
  must have degree eight and see the whole seven-set. Either case
  contradicts Dirac. This argument is only for one original edge.
- The first quotient has every ambient hypothesis of the singleton-atom
  theorem. Lemma 5 excludes its no-safe-edge conclusion. This supplies a
  second safe edge, and the core-degree bound permits Theorem 2 again.

A separate internal check found and corrected an overly pessimistic draft
stopping point: it used only core degree eight initially and left the
second quotient's connectivity open. The audited revision uses degree nine
and proves preservation after both steps. It makes no third-step claim.

## Induction scope and dependencies

The purely labelled small-atom source has whole-file SHA-256
`bc4f7d38d94beed2d86b9858a2290fd1cb85af398653b5b16a5d3231f80eb2db`.
The ambient singleton-atom source has whole-file SHA-256
`775a4f5a6cf2f455a2ca54a232146fd2f4b22a1c88e7e38770b26bfb83df8e07`.
Their stated hypothesis classes differ exactly as Section 4 describes.
Neither labelled terminal lifting nor the two contractions proved here
supplies an unbounded ambient induction. The example linked in Section 5 refutes
unconditional preservation, but has targets and so does not refute a
target-free preservation theorem. Its proof is preserved in `barriers/`, at
whole-file SHA-256
`eeac0df204de1977bbc5f1cbf3e0cdc2b703785eed4f9132c5a9811e72289c3b`.
Moving that example and linking it did not change the mathematical claims.

The critical-host minimum-degree, exterior-connectivity, safe-edge and
singleton-atom results are imported at their audited scopes; the last
includes its previously recorded finite lemma. No new finite enumeration
is a proof input. Dirac's inequality is the cited classical input.
No unresolved gap was found in the new stated deductions. Literal terminal
completion, a closed induction class, nonliteral rotation, T44, Conjecture
21 and `HC_7` all remain unproved.
