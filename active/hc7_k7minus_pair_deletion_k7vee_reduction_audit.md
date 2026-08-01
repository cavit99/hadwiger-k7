# Internal audit: degree-eight pair deletion and `K_7^\vee`

**Verdict:** GREEN for the theorem and scope actually stated.

**Audited source:**
`active/hc7_k7minus_pair_deletion_k7vee_reduction.md`

**SHA-256:**

```text
8852762aa81749443a92849606296401e3a21073c7f6d7245911fdd2058903ea
```

This is a separate internal mathematical audit, not external peer review.

## 1. Density and external theorem matching

For degree-eight vertices `a,b`, deletion removes exactly

\[
                         16-\mathbf 1_{ab\in E(G)}
\]

edges.  The established disconnected-centre density bound `m>=4n` therefore
gives

\[
 |E(G-\{a,b\})|\ge4|V(G-\{a,b\})|-8
                    +\mathbf 1_{ab\in E(G)}.
\]

Deleting two vertices from a seven-connected graph leaves a
five-connected graph.  The hypotheses of Norin--Totschnig, Theorem 6,
therefore match: every four-connected graph with at least `4n-8` edges has
a `K_7^\vee` minor unless it is `K_{2,2,2,2}`.  The established
`n_8>=25+tau` gives `|V(G)|>=25`, so the deletion has at least 23 vertices
and cannot be the eight-vertex exception.

The checked density dependency is

```text
e1b54acdd971831786c0d8912d5e4189aaeedd84184540ed438e594aadb9b2e4  results/hc7_k7minus_one_nonfull_k5_and_nested_cut.md
```

## 2. Spanning enlargement and contact restrictions

Every component outside the initial model union has an edge to that union,
because the deletion graph is connected.  Assigning each whole component
to one adjacent branch set preserves connectedness, disjointness, and every
required model adjacency.  If this creates either nominally missing
adjacency at the deficient branch set, the seven enlarged bags already
contain a `K_7^-` model.  Thus in the target-free host the spanning model
retains both missing pairs.

The six nondeficient bags form a literal clique in the branch-set contact
graph.  A retained root meeting five of them completes a `K_7^-` model.
If a root meets the deficient bag and either missed twin, absorbing the
root into the deficient bag repairs that adjacency and leaves at most the
other one missing.  Finally, if both roots meet the deficient bag and all
four universal bags, those five bags and the two singleton roots have at
most the root--root adjacency missing.  These constructions verify all
three contact restrictions.

## 3. Localization and scope

At most nine degree-eight vertices lie in `N[u]`; hence

\[
                         n_8(E)+n_8(F)\ge16+\tau
\]

for the two exterior components.  This is only a sum.  Neither the degree
identity nor seven-connectivity gives a positive lower bound for either
summand separately.

The four-bag concentration in the source is explicitly an abstract contact
pattern not excluded by the proved restrictions, not a constructed graph
satisfying the critical hypotheses.  The theorem does not split a model
bag, return a boundary equal to `N(z)` for a named degree-eight vertex,
eliminate an attachment regime, construct a `K_7^-` minor, or produce a
six-colouring.  No finite computation is used.
