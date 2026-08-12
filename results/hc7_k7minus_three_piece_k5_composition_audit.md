# Internal audit: three-piece `K_5` composition

**Verdict:** GREEN for Theorem 1, Corollary 2, and the stated remaining
incidence problem.  The four-of-five hypothesis is sufficient exactly as
claimed.  This is a separate internal mathematical audit, not external peer
review.

## 1. Exact revision

The audited source is
[`hc7_k7minus_three_piece_k5_composition.md`](hc7_k7minus_three_piece_k5_composition.md),
with SHA-256

```text
9790e806b1ece317808670efd0219497b77b00a30cf1db466e800622c8f7bb41
```

## 2. Branch-set verification

Promotion changed only the status paragraph and audit link.  A mechanical
diff check found no mathematical change.

For each of `A,B,C`, adjacency to at least four of the five model bags
means that it has either one uniquely missed bag or no missed bag.  Thus the
notation `m(Y)` used in the proof is exhaustive.

If `m(A)` and `m(B)` differ, including the case in which exactly one is `*`,
then `A union B` meets every model bag.  It is connected because `A` is
adjacent to `B`.  It is adjacent to `C` through the edge between `B` and
`C`; `C` misses at most one model bag; and the five `Q_i` are mutually
adjacent.  Hence the seven sets in (1.2) have at most the one missing pair
`C,Q_{m(C)}`.  If both missed symbols are `*`, the same conclusion follows
because `A union B` again has full model-bag contact.

The remaining unequal case is symmetric.  When
`m(A)=m(B)=j` and `m(C) ne j`, the connected union `B union C` meets every
model bag, is adjacent to `A` through `A B`, and leaves only the possible
missing pair `A,Q_j` in (1.4).

Finally, if all three missed indices equal `j`, removing `Q_j` leaves four
mutually adjacent model bags.  Each of `A,B,C` meets all four.  Their two
prescribed adjacencies are `A B` and `B C`, so the only possibly absent pair
among the seven sets in (1.6) is `A,C`.

In every case the displayed branch sets are nonempty, connected and
pairwise disjoint.  A seven-bag model with at most one nonadjacent pair is a
`K_7^-`-minor model (and a complete seven-bag model is stronger).  This
checks every required branch-set adjacency.

## 3. Exact scope of the four-of-five condition

The proof uses the condition in two precise ways:

1. two different missed indices make the union of two adjacent exterior
   sets meet all five model bags; and
2. one common missed index can be discarded while retaining four model
   bags met by all three exterior sets.

Thus four-of-five is a sufficient incidence threshold.  The source does not
claim that it is necessary, nor that the numerical neighbour bounds in
`T` force this distribution among arbitrary branch sets.  Its warning that
several neighbours may lie in one branch set is correct.

## 4. Why this does not yet cover the six-component outcome

The two forest edges `A B` and `B C` are essential to the displayed
composition.  Six distinct components of `G-T` have no such edges between
them.  Even four-of-five incidence for every component is not enough by
itself.

For a sharp quotient example, take

```text
K_4 join I_7,
```

write the four clique vertices as `q_1,...,q_4`, and choose one independent
vertex `q_5` and six further independent vertices `x_1,...,x_6`.  The five
singletons `q_1,...,q_5` form a `K_5` model, and every `x_i` meets exactly
four of its bags.  Nevertheless the graph has tree-width four: a central
bag `{q_1,...,q_4,q_5}` and the six bags
`{q_1,...,q_4,x_i}` form a width-four tree-decomposition.  Since
`K_7^-` contains a `K_6` and has tree-width five, minor-monotonicity of
tree-width excludes a `K_7^-` minor in this example.

Accordingly Theorem 1 cannot be transferred to the six-component case from
bag incidence alone.  The stronger critical-host hypotheses, the eight
literal boundary contacts per selected component, or additional disjoint
linkages could still yield a separate theorem; this audit neither proves
nor refutes such a strengthening.

## 5. Trust boundary

Corollary 2 is an immediate conditional application of Theorem 1.  Neither
statement constructs the required well-distributed `K_5` model in `G[T]`,
aligns the common cycle with a separately chosen spanning minor model, or
returns a response-bearing separation.  Those are exactly the unsupported
steps isolated in the final section of the source.  Consequently this
result does not by itself eliminate the bounded-feedback branch, prove the
`K_7^-` six-colour conjecture, or prove `HC_7`.
