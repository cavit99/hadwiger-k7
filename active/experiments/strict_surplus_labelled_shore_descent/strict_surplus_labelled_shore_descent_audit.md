# Audit of the corrected eligible-shore descent

**Audited file:**
`strict_surplus_labelled_shore_descent.md`, Theorem 2.1  
**Status:** internal hostile audit GREEN for the theorem stated below;
external audit still required before promotion.

## 1. Statement audited

Let `G` be seven-connected, let

\[
\mathcal M=(D,Q_1,\ldots,Q_5)
\]

be a `K_6` model, and let `U` be one foreign bag.  Suppose
`C subseteq D` is connected, has order at least two, contains at most one
prescribed root, is anticomplete to `U`, and satisfies

\[
\eta(C)\le q(G)+|N(C)|-4.
\]

Then contracting `C` yields a threshold-preserving proper minor.  If that
minor is not seven-connected, one obtains an exact order-seven cut, a legal
model reroute, or a strict smaller connected shore with the same missed bag
and no additional root.

## 2. Density accounting

Contracting `C` removes `|C|-1` vertices.  The

\[
4|C|+\eta(C)
\]

edges internal to or leaving `C` are replaced by exactly `|N(C)|` simple
edges.  Hence

\[
q(G/C)=q(G)+|N(C)|-4-\eta(C)\ge0.
\]

This part is exact.

## 3. Pullback of a quotient cut

Every cut of `G/C` of order at most six contains the contracted vertex:
a cut avoiding it would lift unchanged because expanding one connected
vertex inside one quotient component cannot join two quotient components.
Writing the cut as `{c} union Z` gives `|Z|<=5` and

\[
\mathcal K=\mathcal C(G-C-Z)
\]

with at least two members.

The proof must partition **all** of `mathcal K` into two nonempty terminal
families.  Selecting only two components is insufficient, because a path
could use a third component as an excursion.  With the all-component
partition, any terminal-to-terminal path can be truncated after its last
vertex in the first terminal union and before its first vertex in the
second; every internal vertex of the truncated path lies in `C`.

## 4. Correct Menger form

Use the vertex-capacitated set-to-set version of Menger:

- every vertex of `C` has capacity one;
- terminal vertices have unbounded capacity and are not separator
  candidates.

Let `lambda` be the minimum capacity of a `C`-set separating the two
terminal unions in `G-Z`.  If `K subseteq C` had

\[
|K|<7-|Z|,
\]

then `Z union K` would be a cut of `G` of order at most six.  Thus

\[
lambda\ge7-|Z|=:p\ge2.
\]

Equality produces an actual order-seven cut.  Strict inequality gives at
least `p+1>=3` paths whose nonempty internal `C`-segments are pairwise
disjoint connected sets.  Nonemptiness follows because distinct components
of `G-C-Z` are anticomplete.

## 5. Ownership count

For a path interior `P`, a foreign duty `Q_i` is owned when every
`D-Q_i` edge has its `D`-end in `P`.  A model duty is nonempty, so two
disjoint interiors cannot own the same duty.  The named missed bag `U`
cannot be owned by any `P subseteq C`, because `C` is anticomplete to
`U`.  Hence at least three disjoint ownership sets lie inside a four-label
set; one has order at most one.

## 6. Model moves

Let `P` be the selected interior.

- If `D-P` is disconnected, `N(P)` separates the nonempty connected set
  `P` from the nonempty anticomplete bag `U`.
- If `D-P` is connected and `P` contains the possible root, it is a strict
  smaller one-root shore.
- If `P` is root-free and owns no duty, omit it from `D`; the remaining
  branch sets still form the same, not necessarily spanning, `K_6` model.
- If it owns exactly `Q_i`, move `P` into `Q_i`.  An actual `P-Q_i` edge
  makes the enlarged target connected, an edge across `P|(D-P)` restores
  the donor-target adjacency, and every other donor duty survives by the
  definition of ownership.

All prescribed roots and contacted-bag labels are retained in the two
model moves.

## 7. Scope

The theorem does not by itself eliminate a singleton shore.  It also does
not claim that an exact cut is genuinely crossing another cut.  Those are
separate terminal obligations.

The former attempted proof that every six-cut quotient failure was
impossible remains rejected; the corrected theorem makes no such claim and
works uniformly for quotient cuts of every order at most six.
