# A maximum-visibility normal form after Lo deletion

**Status:** written proof of an unbounded reduction, awaiting a separate
internal audit, with a scoped finite barrier.  This does not prove the
six-connected `4n` target, Conjecture 21, or `HC_7`.

Write `K_t^-` for `K_t` with one edge deleted.  A **near-six model** is a
family of six pairwise disjoint connected bags whose contact graph has at
most one missing edge.  For a vertex `v` outside the model, a bag is
**visible** if it meets `N(v)`.

## Theorem 1 (maximum-visibility dichotomy)

Let `G` be a six-connected graph with `n>=8` and

```text
|E(G)|>=4|V(G)|.
```

For every vertex `v`, either `G` contains a `K_7^-` minor, or `G-v` has a
spanning near-six model `M=(B_1,...,B_6)` with the following properties.

1. `M` maximises the number `p` of `v`-visible bags over all near-six
   models in `G-v`, and `p<=5`.
2. No **visibility-increasing transfer** is possible: one cannot move a
   nonempty set from a visible bag to an invisible bag so that both altered
   bags remain nonempty and connected, both remain visible, and the six
   altered bags remain a near-six model.
3. Every invisible bag `B` satisfies

   ```text
   |N_G(B)|>=6.
   ```

   Its boundary lies in the other five bags, it meets at least four of
   them, and some one of them contains at least two vertices of `N_G(B)`.
   Moreover `B` lies in one component `C` of `G-N[v]`, and
   `|N_G(C)|>=6`.
4. Exactly one of the following two rooted residues occurs.

   - **Low visibility:** `p<=4`.
   - **Exact two-defect quotient:** `p=5`; the six model bags have exactly
     one missing adjacency.  If `B_0` is the unique invisible bag, then
     contracting the six bags and retaining `v` gives exactly `K_7` with
     two edges deleted: `vB_0` and the internal model defect.  These two
     edges may be incident or independent.

In the exact two-defect residue, none of the five visible bags has a
**safe split**: there is no partition of one visible bag into two nonempty
connected sets, both meeting `N(v)`, such that those two sets and the other
four visible bags form a near-six model.

### Proof

The elementary-minor robustness theorem gives a near-six model in `G-v`.
Choose one with maximum visibility and, subject to that, covering the
maximum possible number of vertices.  It is spanning.  Indeed, let `D` be
a component of the uncovered graph.  Since `G-v` is connected, `D` has an
edge to a model bag `B`.  Suppose first that `D` contains a neighbour of
`v`.  If `B` is invisible, absorbing `D` into `B` increases the number of
visible bags; if `B` is visible, the same absorption preserves that number
and increases the covered set.  Both alternatives contradict the choice of
the model.  If `D` contains no neighbour of `v`, absorbing it into any
adjacent model bag preserves the visibility score and increases the covered
set, again a contradiction.  Every absorption preserves connectedness and
all old model contacts.  Hence the model is spanning.

If all six bags were visible, adjoining the singleton `{v}` would give a
`K_7^-` model.  Hence `p<=5`.  A visibility-increasing transfer would
produce another near-six model with larger score, proving item 2.

Let `B` be invisible.  The set `B` is connected, `v` has no neighbour in
`B`, and the other five model bags are nonempty.  Thus `N_G(B)` separates
`B` from `v`, so six-connectivity gives `|N_G(B)|>=6`.  Spanningness puts
this boundary in the other five bags.  The near-six model makes `B`
adjacent to at least four of them, and six boundary vertices in five bags
force a repeated bag.  Since `B` is a connected subgraph of `G-N[v]`, it
lies in one exterior component.  The boundary of that component is a
subset of `N(v)` separating it from `v`, and again has order at least six.

It remains to analyse `p=5`.  If the six model bags were pairwise adjacent,
then `{v}` would miss only the unique invisible bag and would complete a
`K_7^-` model.  Therefore the model has exactly one missing adjacency, and
the asserted two-defect quotient follows.  Finally, a safe split, together
with the other four visible bags, would be a near-six model all six of whose
bags meet `N(v)`; adjoining `{v}` would again give the target.  This proves
the theorem.  \(\square\)

## Theorem 2 (minimum-enemy specialisation)

Suppose the statement

> every six-connected graph `G` with `|E(G)|>=4|V(G)|` contains a
> `K_7^-` minor

is false.  Choose an enemy first with minimum order and then with minimum
size, and put

```text
q=|E(G)|-4|V(G)|.
```

There is a vertex `v` of degree `d in {6,7,8}` to which Theorem 1 applies.
If `q>0`, one may take `d=6`.  For a spanning maximum-visibility model put
`R=N(v)`.  If its visible bags contain respectively `r_1,...,r_p` vertices
of `R`, then

```text
sum_i (r_i-1)=d-p.                                    (1)
```

Thus the exact two-defect residue has at least `d-5` root collisions in
its visible bags, whilst the low-visibility residue has at least `d-4`.

Let `C_1,...,C_s` be the components of `G-N[v]` and define

```text
eta_i=|E(G[C_i])|+|E_G(C_i,R)|-4|C_i|.
```

Then every `|N_G(C_i)|>=6`, and exact accounting gives

```text
|E(G[R])|+sum_i eta_i=q+3d+4.                         (2)
```

When `d=6`, every component is full to `R`, `s in {1,2}`, and (2) becomes

```text
|E(G[R])|+sum_i eta_i=q+22.                           (3)
```

Every invisible model bag lies wholly in one of these one or two full
components.

### Proof

The two base graphs in Jakobsen's exceptional cockade family have fewer
than `4n` edges, while every nontrivial cockade has a four-vertex cut.
Thus `G` is not exceptional, and Jakobsen's strict bound gives average
degree less than nine.  Six-connectivity gives minimum degree at least six,
so a minimum-degree vertex has degree six, seven, or eight.  If `q>0`,
deletion of any edge would leave the density threshold intact.
Size-minimality therefore makes `G` minimally six-connected, and Halin's
theorem supplies a degree-six vertex.

Spanningness assigns all `d` roots to the `p` visible bags, proving (1).
The component boundary bound is six-connectivity.  Partitioning all edges
over `v`, `R`, and the exterior components gives

```text
|E(G)|=d+|E(G[R])|+sum_i(4|C_i|+eta_i),
|V(G)|=1+d+sum_i|C_i|,
```

which is (2).  If `d=6`, `R` is an order-six cut.  The exact six-cut
localisation theorem says that `G-R` has two or three full components.
One is `{v}`, so there are one or two full exterior components, proving
(3) and the final assertion.  \(\square\)

## Sharp obstructions to visibility-only augmentation

The adjacent
[`K_1`-icosahedron barrier](../barriers/hc7_k7minus_lo_low_visibility_apex_barrier.md)
is six-connected and target-free.  After deleting a base vertex, every
near-six model has at most four visible bags, and an explicit model has
exactly four.  The example has `4n-10` edges, just below the `4n-9`
elementary-minor entrance, although the particular deletion graph itself
satisfies Lo's hypotheses.

The adjacent
[`K_{2,2,2,2}` barrier](../barriers/hc7_k7minus_lo_five_visible_bags_barrier.md)
is six-connected, target-free, and already satisfies the `4n-9` entrance
for the elementary-minor theorem.  At every vertex its deletion graph has
maximum visibility exactly five, with one internal model defect; the two
quotient defects are independent.  Thus “five visible bags” is not enough.
The example has `4n-8` edges, so it does not refute a theorem using the full
eight-edge surplus at `4n`.

Together, the examples show that neither `p>=5` nor augmentation from
`p=5` follows from connectivity, target exclusion and the local Lo
hypotheses.  The unresolved alternatives above are consequently exact:
use the full density surplus to eliminate low visibility, force a
visibility-increasing transfer, or prove that one of the forced root
collisions admits a safe split.  No such step is claimed here.

## Inputs

- [Lo elementary-minor robustness](../active/hc7_k7minus_lo_elementary_minor_robustness.md).
- [Exact order-six-cut localisation](hc7_k7minus_exact_six_cut_localisation.md).
- I. T. Jakobsen, *On a certain homomorphism properties of graphs II*,
  Mathematica Scandinavica **52** (1983), 229--261.
- R. Halin, *A theorem on n-connected graphs*, Journal of Combinatorial
  Theory **7** (1969), 150--154.
