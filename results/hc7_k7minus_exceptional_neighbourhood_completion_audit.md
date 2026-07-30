# Internal audit: exceptional neighbourhood and exterior completion

Audited file:
`results/hc7_k7minus_exceptional_neighbourhood_completion.md`

Promoted source SHA-256:

```text
fc1e88c28b1f4d0dc7a1cbdeefa19fecfd5e969b986c64e11eb1990615f5dfbd
```

**Verdict:** **GREEN** for the promoted exact revision.

The mathematical content was cold-audited at

```text
9da656d9f8963cac2fa0e63c15b513c6cce56f4d8cc8ec07ee35ac6056bbce9d
```

and promotion changed only the status paragraph from audit pending to audit
GREEN.

This is a separate internal mathematical and computational audit, not
external peer review.

## Exact dependencies and verifier

| Item | SHA-256 |
|---|---|
| Minimum-order and density theorem | `604d11d4276ce6a3c57a8375d702624a1c364b5123f122b7e9e3dc18d11bf8f4` |
| Low-degree exterior-component bound | `4ee48c6d71c994b166b29dcd969d64c3526e6b6b75fa8a849fae834cf95eea29` |
| Retained finite verifier | `5eb316169563208269c887775376dea9d4b853201a2458f9b604b23ea6017ad0` |

The external order-eight input is Rolek--Song--Thomas, *Properties of
8-contraction-critical graphs with no `K_7` minor*, arXiv:2208.07335v2,
Lemma 2.1.  Its unrestricted finite statement says that an eight-vertex
graph with independence number two contains a literal `K_4` or their graph
`H_8`; the displayed `H_8` is isomorphic to the cycle square
`C_8^{1,2}`.  The theorem uses only this local statement, not the paper's
ambient contraction-critical hypotheses.

## Order-eight cross-check

The verifier was rerun under CPython 3.14.6 with nauty 2.9.3:

```text
order-eight graphs=12346; K4-free alpha<=2=3; spanning C8^1,2=3
near-full exterior K7-minus certificates=9/9
```

It parses all unlabelled order-eight graphs returned by `geng`, tests the
literal `K_4` and independent-triple conditions, and directly searches all
cyclic orderings for a spanning cycle square.  A separate NetworkX decoder
cross-check agreed on all 12,346 graph6 records and independently recovered
all three spanning copies.  The verifier also reconstructs the nine
quotients in which the exterior component misses no boundary vertex or one
of the eight vertices, and checks branch-set disjointness, connectivity and
at most one absent adjacency.

The published written lemma is the proof input; the finite verifier is an
independent reproducibility cross-check.  The computational trust boundary
contains CPython, nauty, the graph6 decoder and the short exhaustive tests,
but it is not the only support for the order-eight classification.

## Exceptional-neighbourhood theorem

The star-contraction argument gives `alpha(N(u))<=3`: an independent
four-set contracts to one colour in a proper six-colourable minor, leaving
at most four other colours on the remaining neighbours and a sixth colour
for `u`.

If an exceptional neighbourhood had independence number at most two, the
external lemma supplies a spanning `C_8^{1,2}`.  The minimum-order theorem
ensures that `G-N[u]` is nonempty.  For any component `C` there,
`N(C) subseteq N(u)` separates `C` from `u`; seven-connectivity therefore
gives at least seven boundary neighbours.  After cyclic relabelling, the
seven bags

\[
 \{0,7,2\},\ \{3\},\ \{4\},\ \{1,u\},\ \{6\},\ \{5\},\ C
\]

are disjoint and connected.  The audit checked every adjacency directly.
The only pair that may be nonadjacent is `\{3\},\{6\}`; the component bag
sees every other bag even when it misses vertex zero.  Hence these bags form
an explicit `K_7^-` model, proving `alpha(N(u))=3`.

## Exterior-component completion

For `A={u} union I`, the star is connected and sees every rooted bag.  A
component of `G-N[u]` is adjacent to at least seven boundary vertices, so it
sees at least two members of the three-set `I` and at least four of the five
roots.  If the rooted model avoids that component, `A`, the component, and
the five rooted bags are seven disjoint connected branch sets with at most
one missing adjacency.  No independence assumption on `I` is needed for
this lemma, though the application uses an independent triple.

In a `K_7^-`-minor-free host every rooted model must consequently meet every
exterior component.  If a residual exterior component after deleting the
rooted bags had an `I`-neighbour and contacted at least four bags, the same
seven-bag construction would apply.  This proves all three statements of
the allocation corollary.  The audited low-degree theorem supplies the
separate at-most-two-components assertion.

## Unresolved assumptions and scope

No mathematical defect, hypothesis mismatch, branch-set error, verifier
encoding defect, or overclaim was found.  The result does not construct an
exterior-avoiding rooted `K_5` model, synchronize different exceptional
centres, prove the upper bound of six exceptional vertices, prove the
`K_7^-` six-colour conjecture, or prove `HC_7`.
