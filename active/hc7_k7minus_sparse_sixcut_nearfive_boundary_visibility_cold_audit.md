# Independent cold audit: boundary visibility of a spanning near-five model

**Verdict:** **GREEN** for the hash-pinned revision below.  The set-system
lemma, the seven-bag composition, and the external-neighbourhood counts are
correct.  This is an independent internal audit, not external peer review.

## Audited revision and reproducible check

The audited source is
[`hc7_k7minus_sparse_sixcut_nearfive_boundary_visibility.md`](hc7_k7minus_sparse_sixcut_nearfive_boundary_visibility.md)
at SHA-256

```text
36a196529df143dc0d06464bad122b3478f37e748ab122dd42779e670192b0f4
```

The current source SHA-256 is
`f860157875b2503b0ab9d056d4e2f2d11afc56ca937f401b4a3ce67147cf2bd9`.
The only post-audit change marks the source as independently audited; the
mathematical text is unchanged.

The adversarial verifier is
[`experiments/sparse_sixcut_nearfive_boundary_visibility_verify.py`](experiments/sparse_sixcut_nearfive_boundary_visibility_verify.py)
at SHA-256

```text
276b1202e242d8cb26ceb81763715cdd870ed00b9a198ca32d0f4551decbce6b
```

It enumerates unordered five-multisets of subsets of a labelled six-set, so
repeated sets are included.  Among the `5,194,959` multisets with set order
at least two and at most two order-two occurrences, `4,619,110` cover the
six-set.  Their counts by number of order-two occurrences are

```text
1,279,600,  2,008,605,  1,330,905.
```

Testing all complementary bipartitions found no counterexample.  A clean
rerun printed

```text
GREEN: exhaustive Property-B census; eligible=5194959,
covering=4619110,
by_two_occurrences=[1279600, 2008605, 1330905], counterexamples=0
```

## Audit of Lemma 1

For balanced three-versus-three partitions, an order-three set forbids
exactly its two complementary orientations, whilst a set of order at least
four forbids none.  This proves the case with no order-two set.

For one distinct order-two set `P`, exactly twelve balanced choices split
`P`; each of the at most four other sets forbids at most two.  If `P` is
repeated, there are only three other sets, so repetition causes no gap.

For two distinct disjoint pairs, eight balanced choices split both pairs.
The other three sets forbid at most six choices in total.  For the shared-end
case `{a,b},{a,c}`, the six balanced choices form the three complementary
lines displayed in the source.  A remaining set can forbid such a choice
only when it is one of those triples.  Unless the three remaining sets
represent all three lines, a choice survives; repetitions cannot create a
missing line.  If all lines occur, the union is the full six-set precisely
when exactly one chosen triple is on the `{b,c}` side.  After relabelling,
the five sets are

```text
{a,b}, {a,c}, {b,c,f}, {a,d,f}, {a,e,f},
```

and `{b,c,d,e} | {a,f}` splits each of them.  Thus the exceptional equality
case, including its union hypothesis, is handled correctly.

## Audit of the seven branch sets

Because the near-five model spans `C` and `C` is `S`-full, the five boundary
sets `H_i=N_G(B_i) intersect S` cover `S`.  Negating both displayed outcomes
of Theorem 2 says exactly that every `H_i` has order at least two and at most
two of them have order two, so Lemma 1 applies.

The resulting parts `X,Y` are nonempty.  The sets `A union X` and `D union
Y` are connected because `A,D` are connected `S`-full components.  They are
disjoint from one another and from all five model bags.  Their contacts are:

- `A union X` meets every `B_i` through a vertex of `X intersect H_i`;
- `D union Y` meets every `B_i` through a vertex of `Y intersect H_i`;
- the two enlarged component bags meet through any `X`--`D` edge.

The original five bags have every contact except possibly the one missing
edge of the `K_5^-` model.  Hence the seven displayed bags are connected,
disjoint, and have at most one missing pair: they are a `K_7^-` model.  A
spanning `K_5` model is the easier special case.

## External-neighbourhood count and scope

Each `B_i` has at least six external neighbours.  If it does not dominate
its complement, its external neighbourhood is a vertex cut and
six-connectivity applies; if it does, the six boundary vertices already
give the same bound.  No edge joins `B_i subseteq C` to `A` or `D`, and the
model spans `C`, so every external neighbour outside `S` lies in another
model bag.  Therefore the exact lower bound there is

```text
6-|H_i|.
```

Outcome 1 gives at least five such neighbours.  Outcome 2 gives at least
four for each of three branch sets, exactly as stated in the audited
revision.  The theorem remains conditional on the existence of a spanning
ordinary `K_5^-` model; it does not supply that model or finish the sparse
three-component case.
