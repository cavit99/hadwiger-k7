# Internal audit: limits of rooted helper completion

**Verdict: GREEN for all three counterexamples.** This is a separate
internal mathematical audit, not external peer review.

Audited [source](five_root_helper_completion.md), SHA-256:

```text
0ab6ea87d6bf0bf0debf55307c2dfe9cfdd8d4bdea97819071ce0bacb27dc67b
```

## Density one

Each of the three nonempty nonroot sets in the seven-vertex example has
exactly five external neighbours. The nine edges incident with the two
nonroots give rooted density one. A model with five prescribed root bags
and two helpers must use all seven vertices as singleton bags, leaving
the two absent helper contacts unrepaired. The extra root edge is not
counted as a helper contact. Contracting that edge merges two boundary
vertices and leaves density one on the resulting four-boundary fragment.
This last observation illustrates the local split-boundary pattern; it
does not assert a root-preserving contraction of five original roots.

## Opposite helper placement

The specified graph has nineteen edges. Its four-root helper model uses
the connected bag `{x,y}` and the singleton `{w}`. Each meets all four
root bags, and they are adjacent. The six-root internal connectivity and
ordinary five-connectivity checks are valid.

If `x,y` must instead belong to distinct helpers, the four roots and
these two vertices force six distinct bags. Only `w` can enlarge a bag.
The missing contacts `xa` and `yb` have disjoint pairs of prescribed
bags. An enlargement of one bag can repair at most one of these pairs;
leaving `w` unused repairs neither. The required model therefore does
not exist. The six-root boundary has thirteen edges and singleton
interior excess two, so this example does not meet the sparse boundary
and excess-seven conditions distinguished in the source.

## Unbounded density

For every integer `m>=4`, the bipyramid has `m+2` vertices, `3m` edges,
and a planar embedding with the stated facial triangle. Deleting at most
three vertices leaves it connected: a surviving pole joins all surviving
cycle vertices and any other pole; if neither pole survives, the cycle
has lost at most one vertex. At least one cycle vertex survives in the
former case because `m>=4`.

Adding the two adjacent universal vertices gives six-connectivity: after
at most five deletions, a surviving universal vertex connects what
remains; if both are deleted, at most three bipyramid vertices were
deleted. Root-free fragments with at most four neighbours are therefore
impossible, since at least one of the five roots survives outside each
such fragment and its boundary. This establishes 4-lightness.

The nonroots are the other pole and the remaining cycle vertices, hence
connected. The five roots induce `K5`. The edge count `5m+5` and nonroot
count `m-1` give density `m-1`, without a bound on `m`.

In a hypothetical `K7` model, at least five branch sets avoid the two
universal vertices. Those five bags and their mutual contacts all lie
in the planar bipyramid, yielding an impossible planar `K5` minor.
Eleven helper contacts, together with the literal root clique, would
give precisely such a model. Deleting root--root edges changes neither
root-free fragment data nor nonroot connectedness; any helper model
after deletion would remain one before deletion. The independent-root
variant is consequently valid as well.

No calculation gap or unresolved assumption was found. The first two
examples are explicit finite constructions; the third is an unbounded
family. None refutes the density-two target allowing one missing contact,
Conjecture 21 or HC7. No computational extrapolation is used.
