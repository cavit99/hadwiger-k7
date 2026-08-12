# Three forest pieces and a well-distributed `K_5` model

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_three_piece_k5_composition_audit.md).
This is an unbounded host-level composition theorem.  It is conditional on
the stated incidence with a `K_5`-minor model and does not prove the
`K_7^-` six-colour conjecture or `HC_7`.

## Theorem 1 (four-of-five composition)

Let `G` be a graph.  Let

\[
                         Q_1,Q_2,Q_3,Q_4,Q_5                 \tag{1.1}
\]

be pairwise disjoint connected branch sets of a `K_5`-minor model in `G`.
Let `A,B,C` be three further pairwise disjoint nonempty connected sets,
disjoint from the five model bags, such that `A` is adjacent to `B` and
`B` is adjacent to `C`.  Suppose each of `A,B,C` is adjacent to at least
four of the five sets in (1.1).

Then `G` contains a `K_7^-` minor.

### Proof

For `Y in {A,B,C}`, let `m(Y)` be the unique model-bag index missed by
`Y`, if such an index exists, and put `m(Y)=*` if `Y` is adjacent to all
five bags.

First suppose `m(A) ne m(B)`, where `*` differs from every ordinary
index.  The connected set `A union B` is adjacent to every `Q_i`: two
sets which each miss at most one member of a five-set and have different
missed members have full union contact.  Hence

\[
                         A\cup B,\ C,\ Q_1,\ldots,Q_5       \tag{1.2}
\]

are seven disjoint connected branch sets.  They are pairwise adjacent
except possibly for `C` and the single bag `Q_{m(C)}`.  Thus (1.2) is a
`K_7^-`-minor model.

We may therefore assume

\[
                         m(A)=m(B)=j                         \tag{1.3}
\]

for an ordinary index `j`; equality cannot hold with `*` unless both sets
have full contact, in which case `A union B` again has full contact and
(1.2) applies.

If `m(C) ne j`, the connected set `B union C` is adjacent to every
`Q_i`.  The seven sets

\[
                         A,\ B\cup C,\ Q_1,\ldots,Q_5       \tag{1.4}
\]

are then pairwise adjacent except for `A,Q_j`, and again form a
`K_7^-`-minor model.

It remains that

\[
                         m(A)=m(B)=m(C)=j.                    \tag{1.5}
\]

Delete `Q_j` from consideration.  The seven sets

\[
                         A,\ B,\ C,\ (Q_i:i ne j)            \tag{1.6}
\]

are pairwise adjacent except possibly for `A,C`: the three exterior sets
form a path, and each is adjacent to all four retained model bags.  Thus
(1.6) is a `K_7^-`-minor model. `\square`

## Corollary 2 (the exact three-piece target in the feedback branch)

In the three-piece outcome of the bounded-feedback forest reduction, it is
enough to find a `K_5`-minor model in `G[T]` such that each of the three
connected forest pieces is adjacent to at least four model bags.

The conclusion is the forbidden minor itself; no colouring
synchronisation or separator descent is then required.

## The remaining incidence problem

The cardinality bounds

\[
 |N_T(A)|\ge7,\qquad |N_T(B)|\ge6,\qquad |N_T(C)|\ge7       \tag{2.1}
\]

do not by themselves say how those literal neighbours are distributed
among the five branch sets of a `K_5` model.  Seven neighbours may all lie
in one large branch set.  The common cycle through the six selected
boundary-crossing edges does not repair this directly: when `A` and `C`
are singleton selected leaves, the cycle may traverse the segment

\[
                         y_A-A-B-C-y_C,                       \tag{2.2}
\]

and therefore certifies only one literal `T`-contact for each end piece.
The cycles obtained after prescribing one further vertex are chosen
separately, so using four such choices would be an unsupported exchange of
quantifiers.

Consequently the first missing positive implication is precisely:

> under the critical-host hypotheses, the common six-edge cycle and the
> co-bagged spanning `K_6` model either produce a `K_5` model in `T` with
> four-bag contact from each of `A,B,C`, or return a labelled separation
> carrying one of the six matching-edge responses.

Theorem 1 proves that the first outcome is terminal.  It does not assert
the displayed implication.
