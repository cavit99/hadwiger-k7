# A triangle and a four-cycle on a seven-separator

**Status:** written proof; a [separate exact-source audit](hc7_triangle_four_cycle_separator_audit.md) is recorded beside it.
This closes a separator case, not Conjecture 19 or HC7.

All graphs are finite and simple. Put `Q=K7-2K2`. Minor bags are
nonempty, connected and pairwise disjoint; extra contacts are harmless.

**Theorem.** Let G be seven-connected, and let Z be a seven-vertex cut.
Suppose Z contains a triangle T and a four-cycle on `S=Z-T`, and every
vertex outside Z has degree at least eight. Then G contains Q as a minor.

We use the [five-root degree-six theorem](../results/hc7_five_root_degree_six.md),
source SHA-256 `289c5ad015b6c392ea69e8e26e15eba54b4eba7cb155789edd76b3dbb5c9f9a4`,
and its [audit](../results/hc7_five_root_degree_six_audit.md), SHA-256
`6f13ffd37126c78a697b5752574fe06b6fd13b68dabb0d63e4e39d76a8f1d065`.
For five roots containing a triangle, nonroot degree at least six and
boundary at least five for every nonempty nonroot subset give a rooted
K5-minus-edge. At least two triangle roots are admissible as the triangle
endpoint of its sole possible hole; the other endpoint is a helper root.

**Proof.** Partition the components of `G-Z` into two nonempty unions
C,E. Partition S into the opposite pairs P,U of its four-cycle. All
four P--U edges are present. Apply the five-root theorem to the actual
induced graphs

```text
G[C union T union P]       and       G[E union T union U].
```

Each nonroot loses at most the two omitted S vertices, so retains
degree at least six. For a nonempty `X subseteq C`, E is nonempty and
anticomplete to X; thus seven-connectivity gives `|N_G(X)|>=7`.
Deleting U leaves boundary at least five. The same argument applies to
subsets of E, with C as the surviving opposite side. These checks apply
even if C or E is disconnected.

Choose different admissible triangle endpoints in the two models; each
offers at least two choices. For each root of T, unite its two bags.
These unions are connected through their common root. The models share
only the three prescribed T roots, so the resulting three unions and
four separate S-rooted bags are pairwise disjoint. All three triangle
contacts survive. The four S bags form a K4: their within-pair contacts
come from the models, and their cross-pair contacts are literal cycle
edges. The only possibly missing contacts join different triangle bags
to helper bags in different pairs. They are therefore independent.
The seven bags give Q. No induction or choice of compatible interiors
across an overlapping side is used. QED

## Application to a four-cut of the critical complement

Use the [four-cut theorem](../results/hc7_four_cut_components.md),
source SHA-256 `2986fb1f55c2cbaa4572b7c88e287ed5aa4230f34ab3b63dabe4d840e247e03f`,
and its [audit](../results/hc7_four_cut_components_audit.md), SHA-256
`7a9d05d3874f6a6da0fabda90493660ee893fb0fd7e29ab5afe8ef42ae3fa437`.
Under its hypotheses,
write `R={v} union B`, `F=G-R`, and let `F-S` have components C,D.
If C misses `r in R`, then `(R-{r}) union S` separates C from
`D union {r}`. Consequently S cannot contain a spanning four-cycle.
This includes all choices of r, including v; r need not remain singleton.

There is a second direct construction. Suppose a connected set
`K subseteq S`, with `1<=|K|<=2`, contacts r and both vertices of a pair
`{s1,s2} subseteq S-K`. Apply the five-root theorem on
`C union (R-{r}) union {s1,s2}`. Its degree and boundary conditions
are verified in the pinned four-cut source. Add bags `K union {r}`
and D. The first is connected and full to the five packet bags.
D sees s1,s2 and at least two roots of the triangle `R-{r}`, and
contacts `K union {r}` through K. Choose an admissible triangle endpoint
contacted by D. Its possible missing triangle contact then has a different
endpoint from the packet's possible hole. These seven bags give Q.

The four-cut theorem already gives `|N(r) intersect S|<=1`. If this
intersection is `{w}`, the component of `G[S]` containing w is a path
with w at an endpoint. Indeed, w cannot have two S-neighbours; if it
has one neighbour z, the choice `K={w,z}` excludes two further neighbours
of z. On four vertices the only remaining cycle could be a triangle
disjoint from w. Thus the remaining S graphs are linear forests with w
at an endpoint, or a triangle plus isolated w. When r has no S-neighbour,
the four-cycle exclusion still applies but these sharper restrictions
need not hold.

The theorem combines two independently chosen models on a common
triangle, whose rooted bags can be united safely. The missed-root
application does not cover a cut whose two components both meet all of R.
The remaining cut shapes and the more connected complement remain open.

The simultaneous construction and the connected-K construction arose
in the separate boundary-allocation analysis. The seven-separator statement
is the same argument with only its necessary hypotheses retained.
