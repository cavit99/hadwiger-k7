# A deficient near-clique bag can be reduced to a vertex or an edge

**Status:** written proof; separate internal audit at the source hash
recorded beside this file. This is a model reduction, not a proof of
Conjecture 21, T44 or `HC_7`.

Write `K_7^vee` for `K_7` with two adjacent edges deleted, and `K_7^-`
for `K_7` with one edge deleted. All graphs are finite and simple.

## Theorem

Let `G` be three-connected and contain no `K_7^-` minor. Suppose
`(D_0,T_1^0,T_2^0,T_3^0,T_4^0,B,C)` is a `K_7^vee` model: the six
core bags form a clique, and `D_0` contacts the four `T_i^0` bags.
There is another such model `(D,T_1,T_2,T_3,T_4,B,C)` with

```text
D subseteq D_0,  T_i^0 subseteq T_i for every i,  1 <= |D| <= 2.
```

Thus both `B,C` stay fixed and every original core bag is retained inside
its corresponding bag. No prescribed vertex of `D_0` is required to
remain in `D`.

If `|D|=2` is the minimum possible subject to these requirements, write
`D={x,y}` and permute the four `T_i` labels. In the component `Q` of
`G-W`, where `W=T_1 union ... union T_4 union B union C`, the edge `xy`
is a bridge. Its two sides `Q_x,Q_y` satisfy

```text
N_G(Q_x)-{y} subseteq T_1 union T_2,
N_G(Q_y)-{x} subseteq T_3 union T_4,
```

and each side contacts both of its indicated core bags. The edge `xy`
lies in no triangle of `G`. If `G` is seven-connected, each displayed
neighbourhood has at least six vertices.

## Proof

Choose a model satisfying the stated containment requirements with `|D|`
minimum. Such a model exists by the original hypothesis. No vertex of
`D` contacts `B` or `C`, since that would give `K_7^-` immediately.

Select one actual contact edge from `D` to each `T_i`, and a smallest
tree in `G[D]` containing their ends in `D`. Its vertex set can replace
`D`, so minimality makes it span `D`. Each label `i` marks its selected
end in this tree. If the tree has more than one vertex, every leaf has
at least two labels. A leaf with no label could be deleted. A leaf with
one label `i` could instead be absorbed into `T_i`: this enlarges a
connected core bag, and the leaf's tree edge replaces the lost `D-T_i`
contact. All other contacts and all core containments survive.

There are only four labels. Consequently the tree is a path, with two
labels at each end. Call the ends `x,y`; after permutation their labels
are respectively `{1,2}` and `{3,4}`. There are no extra contacts from
an internal path vertex to the core. Indeed, a contact to `T_i` would
let us select its witness there, leaving the end formerly carrying `i`
with only one selected label; absorbing that end as above shrinks `D`.
Likewise `x` cannot contact `T_3,T_4`, and `y` cannot contact `T_1,T_2`.
A chord of the path would permit a shorter connected `D` retaining its
four end contacts, so the path is induced.

Consider a component `Z` outside all seven model bags with a neighbour
on the path interior. If it contacts some `T_i`, absorb all of `Z` into
that bag; the new internal contact permits the same strict shortening.
If it contacts `B` or `C`, adjoining `Z` to `D` instead supplies a
`K_7^-` model. Thus such a component contacts no core bag. If the path
has an internal vertex, its interior together with all these components
is therefore separated from the six nonempty core bags by `{x,y}`.
This contradicts three-connectivity. Hence `|D|<=2`.

Now assume the minimum is two. A component `Z` outside the model that
contacts `x` cannot contact `T_3,T_4`: absorbing it there would give `x`
a third label, after which `y` is absorbed into its remaining labelled
bag and `D` shrinks to `{x}`. It cannot contact `B,C` either, by the
terminal construction above. The symmetric assertion holds at `y`.
If `Z` contacts both ends, it consequently has no core contact. Its
entire neighbourhood then lies in `{x,y}`, contradicting
three-connectivity. Thus no such component meets both ends. These are
all possible connections in `G-W`, proving the bridge and the two
neighbourhood inclusions. The original end contacts ensure that each
side meets both indicated bags. A common neighbour of `x,y` would belong
either to a core bag or to an outside component meeting both ends. Both
possibilities were excluded, so `xy` lies in no triangle.

Finally `N_G(Q_x)` contains `y` and vertices of `T_1 union T_2` only.
Deleting it separates `Q_x` from `B,C,T_3,T_4`, so seven-connectivity
gives `|N_G(Q_x)|>=7`. Removing `y` leaves at least six neighbours.
The argument for `Q_y` is identical. QED

## Exact remaining obligation

The decreasing quantity is `|D|` in a fixed finite host; no quotient is
asserted to retain criticality or connectivity. Every modification has
explicit disjoint bags and retains the entire original core. The
deficient bag's original vertices are movable, which is essential.

Seven-connectivity does not turn six attachment vertices in two core
bags into six distinct bag contacts. The singleton case and the two
connected sides above still need a simultaneous construction through
the core interiors. This theorem supplies no such construction or
well-founded continuation, and does not achieve the user's objective.
