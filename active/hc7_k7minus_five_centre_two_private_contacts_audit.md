# Internal audit: two private contacts from a retained-pole witness

**Verdict:** **GREEN** for Lemma 2.1, Theorem 3.1, Corollary 3.2, and the
stated scope at the exact source revision below.  This is a separate
internal mathematical audit, not external peer review.

## 1. Exact revisions checked

The audited theorem source
`hc7_k7minus_five_centre_two_private_contacts.md` has SHA-256

```text
a7470e97b209418be8d27a55b48370b1348b83ae4389432cd2a416f308947213
```

The direct theorem dependencies were checked at these revisions:

| dependency | SHA-256 |
|---|---|
| `hc7_k7minus_five_centre_t5_global_palette.md` | `b26f9f0d12822f93af55e3aa566fc75b985dcb5a17daa4ea2b329c8efea274c3` |
| its audit | `765df0db1168001a212c77e5f871abe4725d4c92cc4e11ae8d887ff808f92e6a` |
| `hc7_k7minus_five_centre_rainbow_triangle_rooted_k5.md` | `891aed883d8082c18e0c502cd7be7c67760daec8ad973b8eefa8477a2f8c4a19` |
| its audit | `4a161fa0e113ba93d21170263781de76abc41ca0b819483b826afe8942e0f05a` |
| `../results/hc7_k7minus_five_centre_two_cut_reduction.md` | `1917b5e3d183d44a2d905d2628272d10e4bc6f7ae0768b43cab0e9462b83332a` |
| its audit | `d01183c936d79ea2e07f956c2e89f7291df9cc28a5dab3dda6b093c8a69c4ea3` |

## 2. Four-root witness and the two connected sets

Deleting the witness path `P` leaves a component `K` containing all four
retained centres.  Full five-root infeasibility correctly implies that the
omitted centre `z` has no neighbour in `K`: otherwise the same path and
`K+z` would witness feasibility for all five roots.

Every other component `B` of `H-P` met by `z` lies in `C`.  Its only
possible neighbours are `z` and vertices of `P`: the retained centres are
in the different component `K`, distinct components of `H-P` are
anticomplete, and `C` is anticomplete to `D`.  Since the nonempty component
`D` lies beyond this neighbourhood, seven-connectivity gives

```text
|N_G(B)| >= 7.
```

At most one of those neighbours is `z`, so `B` has at least six neighbours
on `P`, including an internal path vertex.  This verifies that all such
components attach to the connected open path.  Fullness at `z`, together
with `E(z,K)=emptyset`, then attaches `z` to that same union.  The set `X`
in (2.3) is therefore connected and, because its definition deletes both
literal poles, remains disjoint from the opposite-shore rooted model.

For the asserted `K-X` edge, the connected component `K` must meet `C`:
after deleting `P`, its four independent retained centres cannot form a
connected subgraph by themselves.  If `R` is a component of `K cap C`,
then

```text
N_G(R) subseteq A union V(P).
```

The omitted centre misses `K`, different residual components are
anticomplete, and there are no `C-D` edges.  Seven-connectivity therefore
gives at least three neighbours of `R` on `P`; one is internal and belongs
to `X`.  This proves the final assertion of Lemma 2.1.

## 3. The seven-bag composition

The five rooted bags lie in `D union {p,q}`.  The set `X` lies in
`C union {z}`, and `K` lies in `C union A`; their construction makes all
seven sets disjoint.

Every required adjacency is literal:

- the first and last edges of `P` join `X` to the bags rooted at `p,q`;
- the three edges `zt_i` join `X` to the triangle-rooted bags;
- Lemma 2.1 supplies `X-K`;
- retained centres at the two pole labels join `K` to the `p`- and
  `q`-rooted bags; and
- every nonprivate `t_i` has a retained-centre neighbour in `K`, joining
  `K` to `B_i`.

The five rooted bags already form a clique model.  If two triangle
contacts were nonprivate, `K` would meet at least four of those five bags,
so among the seven displayed bags only the remaining `K-B_i` adjacency
could be absent.  This is an explicit `K_7^-` model, establishing
Theorem 3.1 by contradiction.

Corollary 3.2 is the exact incidence reformulation of the theorem:
deleting a pole-free centre preserves both pole labels, as does deleting a
centre whose own label has another carrier.  No extra profile or finite
shore-order assumption enters the proof.

## 4. Scope and unresolved cases

The source correctly does not claim closure when the omitted centre is the
unique carrier of one pole label.  It also does not relate the private
contacts of different triangles, place them in common rooted bags, or
derive a forbidden minor from the private-contact census alone.

In the `b=2` row the theorem gives two private contacts to each of the
three pole-free centres, but it gives no new conclusion for the two
pole-incident centres.  That is a genuine unbounded reduction, not a
closure of the `b=2` row or of the five-centre two-cut branch.
