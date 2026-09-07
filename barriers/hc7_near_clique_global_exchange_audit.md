# Independent audit: near-clique transfers and centroid weakenings

**Verdict: GREEN.** The propositions and counterexamples in the checked
source are sound. This is a separate internal audit, not external peer review.

**Audited source:** [hc7_near_clique_global_exchange.md](hc7_near_clique_global_exchange.md)

**Source SHA-256:**
`6e48f030621358a37d99a963dc2125999a1decabed31bb6921df30e6a396e076`

The cold audit first checked revision
`e5f1deb7d5e6936f7746896aa6b92172209ca3ceef335bd4faa686bcf0bcc6ad`.
Replacing only the final revision's status wording reproduces that exact
hash; its mathematical content is unchanged.

## Transfer construction

The path interior avoids every original bag, so its union with `D,X`
is connected and disjoint from `Y` and the five unchanged foreign bags.
The actual `X`--`Y` edge retains the recipient--donor contact. All old
`D`--`U_i` contacts and all contacts between unchanged core bags survive.
Consequently the displayed `2-g+l` count lists every missing contact,
without assuming that colours or contact labels determine ownership.

The strongest inference, the `g=l=1` case, is valid. If the recipient's
missing bag `H` were also the donor remainder's sole missing neighbour,
the original `T`--`H` edge would have its `T` end in `X`. That edge
would make `D'` adjacent to `H`, a contradiction. Thus `H,V` are distinct
foreign bags, and the two missing edges have four distinct ends.

Since `0<=g<=2`, the cases with `l<=g` are exhaustive. Strict inequality
leaves at most one missing edge; equality leaves either the two stated
incident-edge patterns or the independent-edge pattern just checked.
A `K_7^-` model contains `K_7^=` after deleting an additional suitable
edge. No root of the donor is silently retained: the source explicitly
allows it to leave `Y`. No decreasing parameter or induction is claimed.

## First centroid example

The six displayed bags are disjoint, connected and form a `K_6` model.
The selected witnesses put three contact ends at `c,d` and two at
`u_1,u_2`, respectively. Deleting each nominated centroid from its bag
tree therefore leaves components of contact weight at most two.
The other four bags are singletons. The complement of the six centroids
is `K_2`, and restoring any one centroid gives `K_3`, as required.

The clique-separation exclusion is sound. A five-connected seven-vertex
minor has at most four branch sets meeting the four-clique separator.
All other bags must lie on one side. Restricting the crossing bags to
that closed side retains a separator vertex in each; the separator clique
connects their retained pieces and replaces contacts lost on the other
side. Thus the minor would lie in one of the two six-vertex cliques.
`K_7^=` is five-connected, so this proves its exclusion. The spanning
model leaves no disjoint deficient bag, exactly as the source states.

## Variant and retained global constraint

In the variant, `d` contacts precisely the four indicated core bags.
The centroid complement is the path `d-u_1-v`. Each centroid has the
two claimed outside neighbours: `c,u_2,u_3,u_4` see `u_1,d`, and `a,b`
see `u_1,v`. Adding the four-clique along `u_1ab` preserves target
exclusion by the same argument across its three-clique separator.
This variant claims only the weaker connected-complement condition.

For a seven-connected host and six centroids, deleting `6-|I|` vertices
leaves connectivity at least `|I|+1`. In the first example, choosing
`I={a,c}` leaves a graph disconnected by deleting `u_1,u_2`, so the
stated stronger condition fails. Both examples are six-colourable and
do not realize the critical host.

## Unresolved obligations

No mathematical gap was found in the checked claims. They do not prove
that a useful transfer exists, handle `l>g`, or produce a well-founded
continuation in either nonterminal case. The centroid counterexamples
do not refute the full seven-connected allocation statement. Conjectures
19 and 21 and `HC_7` remain unproved here. No external source or finite
enumeration is required for this audit.
