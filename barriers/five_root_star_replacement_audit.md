# Internal audit: boundary-star replacement

**Verdict: GREEN for the stated counterexample.** This is a separate
internal mathematical audit, not external peer review.

Audited [construction](five_root_star_replacement.md), SHA-256:

```text
cf158c177800e7b75b70bd7fa5b11ad081f60adf21e34235aba17e18449f469d
```

The claim concerns one graph with nine vertices and five prescribed roots.
Its proof is an explicit calculation, without an external theorem or a
computer-assisted premise.

The three edge lists are disjoint and have sizes `6,7,5`, giving eighteen
edges. All edges have a nonroot end, so the global density is two. The
five neighbours of `y` are exactly the stated boundary; its singleton
density is one.

The lightness proof exhausts all fifteen nonempty subsets of the four
nonroots. Any subset containing `v` has all five roots as neighbours.
Among subsets avoiding `v`, those containing `y` together with `a` or `b`
also see every root. The remaining sets are `{y}`, `{a}`, `{b}`, `{a,b}`,
whose boundary orders are respectively `5,5,6,5`. Thus no nonempty
root-free fragment has at most four neighbours. The five external paths
are present, pairwise vertex-disjoint and avoid `y`; their ends cover the
entire boundary of that singleton.

Contracting `vy` preserves all original roots and adds only `va` to
`G-y`: the three other star edges already exist. The edge count becomes
fourteen on three nonroots, so the global density remains two. In the
quotient, `{a,b}` has exactly the boundary `{r1,r2,r3,v}` and exactly nine
incident edges. Its fragment density is one, violating 4-lightness.
This tests the new four-boundary fragment explicitly, rather than inferring
lightness from the unchanged global density.

The limitation in the final paragraph is necessary and correct. Before
contraction, `{a,b}` has boundary `{r1,r2,r3,v,y}` and ten incident edges,
so its density is two. Its closed side omits `r4,r5`, giving a proper root
five-separation with that positive-density right-hand side. The example
therefore does not belong to a class excluding such separations.

No unresolved assumption or calculation gap was found. The example refutes
unqualified preservation of 4-lightness under the stated replacement,
even with the exhibited linkage and unchanged global density. It does not
refute preservation with all proposed minimal-counterexample restrictions,
the stronger helper target, Conjecture 21 or HC7.
