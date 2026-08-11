# Internal audit: common rainbow contact-triangle elimination

Audited file:
`active/hc7_k7minus_five_centre_common_rainbow_triangle_elimination.md`

Audited SHA-256:

```text
d58f12af5f0f929e46c0e3bea838094335d97ec3d98f4d498f25380f396fdd97
```

**Verdict:** **GREEN** for Theorem 2.1 and its stated scope.

This is a hash-pinned internal mathematical audit, not external peer
review.  The theorem eliminates one unbounded subcase of the all-rainbow
`t=5` row.  It does not close the full five-centre two-cut branch.

## 1. Audited dependencies

| input | source SHA-256 | audit SHA-256 |
|---|---|---|
| global five-root palette alternative | `b26f9f0d12822f93af55e3aa566fc75b985dcb5a17daa4ea2b329c8efea274c3` | `765df0db1168001a212c77e5f871abe4725d4c92cc4e11ae8d887ff808f92e6a` |
| synchronized five-centre paths | `5db1bcb4715b1d83c894f3a79450f029fb726b153b2db375d850bd477e116192` | `696c3e0acd224184c660c9d75ea67d3f7c898b4a55d49fe685d4e20b4e495e6d` |
| five-centre two-cut reduction | `1917b5e3d183d44a2d905d2628272d10e4bc6f7ae0768b43cab0e9462b83332a` | `d01183c936d79ea2e07f956c2e89f7291df9cc28a5dab3dda6b093c8a69c4ea3` |
| terminal-respecting tree contraction | `012e98da1403fb72e303c294e403b2b82a4cc8d2a411287268e8de08d505a5d2` | `5cc78f8103df07c799fdf5301eea63829539c2932b0935bf5abfc3ba6158a858` |

The palette theorem supplies the exact profile `(4,3,1)` for every
pole-incident rainbow centre and puts the three colours on each
`D`-contact triangle outside the root and pole colours.  The two-cut
reduction supplies rooted infeasibility and a bichromatic pole-to-pole
path in the distinct-response shore.  Lemma 3.3 of the synchronized-path
theorem applies to any such path and any prescribed triangle in one
component left by its interior.  The tree-contraction lemma applies to
arbitrary disjoint connected marked sets in the connected graph `C`.

## 2. The triangle is disjoint from the selected path

Under the fixed distinct-response colouring, `p,q` have colours
`beta,delta`, while the common contact triangle uses precisely the three
colours in

\[
                  [6]-\{\alpha,\beta,\delta\}.
\]

A `beta`--`delta` path therefore contains no triangle vertex.  This is the
point at which the all-rainbow hypothesis is essential.  Since the three
triangle vertices remain pairwise adjacent after deleting the path
interior, they lie in one residual component.  All hypotheses of the
prescribed-triple fan lemma are consequently met.

The three returned paths have distinct path endpoints and are pairwise
vertex-disjoint.  Deleting the endpoint on the pole path leaves three
nonempty connected bags.  They are pairwise adjacent through the three
literal triangle edges and are each adjacent to the path bag through the
deleted last edge.  Thus the four right-hand bags in the source are a
literal `K_4` minor model.

## 3. The three enlarged centre bags

Each of the three centres has four `C`-contacts.  For any subfamily of
the three contact sets, its union has order at least four, hence at least
the order of that subfamily.  Hall's theorem therefore gives distinct
representatives `x_1,x_2,x_3`.

Applying terminal-respecting tree contraction to the three singleton
marked sets inside connected `C` gives disjoint connected sets
`Q_1,Q_2,Q_3` whose contact graph contains a spanning tree.  Adding
`z_i` to `Q_i` preserves connectivity through `z_ix_i` and preserves
disjointness because the centres are distinct boundary vertices.  A tree
on three labels has two edges, so at most one pair of these enlarged bags
can be nonadjacent.

## 4. Complete branch-set audit

The seven bags are pairwise disjoint: the three enlarged centre bags use
only `Z union C`, the three fan bags use `D-V(R)`, and the path bag is
`V(R) subseteq D union {p,q}`.

Their adjacencies are:

- fan bag--fan bag: the common triangle edges;
- fan bag--path bag: the last fan edge;
- centre bag--fan bag: every selected centre is complete to the common
  triangle;
- centre bag--path bag: the centre's unique pole edge, with both poles in
  the path bag; and
- centre bag--centre bag: the spanning tree in the contact graph of the
  `Q_i`.

Thus at most one of the 21 branch-set adjacencies is absent.  This is an
explicit `K_7^-` minor model and contradicts the standing host
hypothesis.  The proof does not require the centres to have a common pole.

## 5. Scope

The conclusion bounds the multiplicity of each literal `D`-contact
triangle among pole-incident rainbow centres by two.  It makes no claim
about two centres sharing a triangle, pole-free centres, or three centres
with different triangles.  No unresolved assumption or proof gap remains
inside Theorem 2.1 at the audited revision.
