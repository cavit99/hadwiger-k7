# Second internal audit: the one-missing-contact helper theorem

**Verdict: GREEN for the stated rooted theorem and the checked implication
chain.** This is an independent internal mathematical reconstruction, not
external peer review. The first audit's verdict was not used as a proof
input. No finite search or extrapolation establishes the conclusion.

Audited [theorem](five_root_one_missing_contact.md), SHA-256:

```text
078ba860d4cdde187cdc6e618a4e1842dd623523dbefbe3ead06544c7d8afa18
```

The inspected upstream sources have these exact hashes:

| Source | SHA-256 |
|---|---|
| [Minimal-counterexample reductions](hc7_c21_rooted_density_low_degree_reduction.md) | `431bd7d7d2b5bcb59e385781234c6d7ed6824f62ee50eb8ddf49e69da792cef2` |
| [Degree-five elimination](hc7_c21_helper_degree_six.md) | `85927a0f7d1af6229930fd67f7144eac35b934c54ad504539a34d39e209020ee` |
| [Degree-five rooted dart](rooted_dart_nonroot_degree_five.md) | `37dcf256f64fca7c49a1bd4ec66021371fba9a7863bf9523597ba4b898ecfad2` |

The first of these sources received only introductory and historical-status
changes during this audit; its proof text was unchanged. All final hashes
were read again after those changes.

## Exact conclusion and external atom input

The conclusion covers every finite 4-light graph with five prescribed
distinct roots and density at least two. Its seven bags are disjoint,
connected and nonempty, retain the five individual roots, and realise
at least ten of the eleven pairs involving a helper. Root--root contacts
are not asserted.

I inspected the rendered printed page 5 of Kriesell--Schmidt,
[*More on foxes*, arXiv:1610.09093v1](https://arxiv.org/pdf/1610.09093v1),
as well as the surrounding definitions. Their Theorem 5 allows an
arbitrary family of vertex sets. It has no unstated requirement that
every edge be noncontractible, or that the graph be contraction-critical.
The overbar in its local condition denotes the complementary fragment;
it cannot be replaced by the atom itself. The proof applies this exact
condition, not a variant restricted to positive-density fragments.

The external atom theorem and the explicitly cited Dvořák--Norin--Rahman
inputs are accepted as literature inputs. This audit verifies their
stated use; it does not reconstruct all proofs in those papers.

## The padded atom inference

Completing the roots and adjoining the large clique gives connectivity
exactly five. Deleting at most four vertices leaves a surviving original
root in the large clique; an additional component would violate internal
five-connectivity in the original graph. Deleting all five original roots
does disconnect the padding from the nonempty original nonroot set.

No new vertex is adjacent to an original nonroot. Thus boundaries and
fragment densities of original root-free sets are unchanged. Common
neighbours of every original edge having a nonroot end are unchanged as
well. The established blockers are consequently genuine fragments of the
padded graph at minimum separating sets, and the family of eligible
fragments is nonempty.

The atom is chosen among all fragments whose five-boundary contains an
eligible edge, including fragments of nonpositive density. An existing
blocker bounds its order by the number of original nonroots. If it met
the padded root clique, it would contain that entire clique outside its
five-boundary, exceeding this bound. Hence it lies entirely among the
original nonroots. Its closed side is also proper in the original graph:
otherwise its five-boundary would be the original root set, which cannot
contain an eligible edge having a nonroot end. The previously proved
proper-side bound therefore gives atom density at most one.

Minimum nonroot degree six rules out an atom of order one or two. For
an atom `A` of order at least three, the exact weighted identity is

```text
sum_{v in A}(deg_G(v)+deg_{N(A)}(v))
    =8|A|+2rho_G(A)<=8|A|+2.
```

Integrality supplies a vertex of weight at most eight. Its original-root
weight is no larger, so the local star construction supplies an eligible
incident edge `f`. One endpoint of `f` is in `A`, and both lie in
`A union N(A)`. Its blocker cut `T` contains both endpoints. Thus

```text
V(f) subset T-barA,       T intersect A != empty.
```

These are both required local conditions of the atom theorem. Its order
bound is at most `5/2`, contradicting the atom's order at least three.
Neither positivity of the chosen atom nor closure of positive fragments
under intersection is assumed anywhere in this inference.

## The weighted-neighbourhood construction

For a nonroot `v` of original-root weight at most nine, assuming every
incident edge has at least four common neighbours in the completed-root
graph gives the exact degree hypotheses of the rooted star lemma on
`G[N(v)]`. Root completion contributes `r-1` extra common neighbours only
at a neighbouring root, where `r=|N(v) intersect X|`; the proof subtracts
precisely this quantity.

Internal five-connectivity gives five disjoint paths from the original
roots to `N(v)` in `G-v`. A separator of size at most four otherwise
isolates a root-free component containing `v`. First-entry truncation
keeps all path interiors outside the neighbourhood and preserves trivial
paths at the roots already in that neighbourhood.

The central star bag avoids original roots. Trimming just its own linkage
path leaves a nonempty prescribed-root bag, since the star centre is a
nonroot. The other four paths remain intact. The two helpers have five
and four root contacts respectively, and are adjacent, giving the claimed
ten contacts without reusing a linkage endpoint. The averaging argument
that establishes the first eligible edge also checks: there are at least
four nonroots and their total original-root weight is `8m+4`.

## Independent challenge of the degree-five reduction

I rederived the local contraction lemma from its separation grid, rather
than importing contraction-criticality from the stated external lemma.
For the two five-cuts, use the source's notation `p,r,s,u,w`. A nonempty
`A`-corner has a boundary omitting the distinguished vertex `x`, because
its only neighbour in `A` is already in the crossing cut. This gives
`u>r` and `p>w` for one corner, with the symmetric inequalities for the
other. If both corners exist, the opposite shore lies in the cut and
the resulting inequalities exceed the five available cut positions.
If neither exists, `p>=3` forces the opposite crossing side to have
order at most one. If exactly one exists, the same corner bounds force
the original opposite shore to have order at most one. Each contradicts
the stated size hypotheses. No assumption about an atom or global edge
criticality enters this derivation.

For deletion of a degree-five nonroot and addition of the missing edge
`ab`, the incident-density identity for a violating fragment is

```text
rho_G(Y)=rho_H(Y)+e_G(v,Y)-1_{ab incident with Y}.
```

Internal five-connectivity and the proper-side density bound force all
four relevant quantities to equal one. Exactly one endpoint, say `a`,
lies inside the fragment, and the other endpoint `b` must already be
among its four remaining boundary vertices. A singleton fragment would
then assert the missing edge `ab`. A two-vertex fragment would consist
of adjacent degree-five vertices with three common neighbours, exactly
the separately excluded configuration. The other open shore has at
least two vertices: a singleton would be an original root with degree
at most one. Thus the local contraction lemma applies with its full
hypotheses.

After contracting the two nonroot endpoints `v,a`, quasi
five-connectivity gives rooted 4-lightness. The only dangerous opposite
singleton would be an original root, but root completion makes its
degree at least five. The nonedge `ab` limits the common-neighbour count
of `va` to three, preserving density at least two. This is a strictly
smaller admissible rooted graph with a valid fixed-preimage lift.

I also checked the two-vertex-blocker rerooting used in this argument.
Removing `pu,qv` and rerooting at `{u,v} union D` gives density
`7-delta-a0`, exactly the number of missing edges in the required
seven-edge rooted graph. Every value from zero to seven is covered by
the stated universality table; its exceptional four-edge target at
density three is irrelevant. The constructed helpers avoid all
original roots. The subsequent root linkage either attaches five
distinct boundary bags or makes a reducible smaller-boundary side;
the helper vertices are not reused as linkage roots.

## Assumptions and scope

No unresolved inference was found in the padded atom proof or in the
upstream degree-five and two-vertex reductions checked here. The rooted
dart input retains its explicitly identified external terminal
construction. All invoked induction steps decrease the finite
lexicographic parameter and lift through disjoint connected preimages.
Padding is only an auxiliary fragment-selection device.

This verdict certifies the stated rooted helper theorem subject to its
explicit literature inputs. It does not certify a global composition
proving Conjecture 21 or HC7, an originality claim, or attainment of the
user's comparable-significance criterion.
