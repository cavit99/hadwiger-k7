# Colour-saturated common neighbours and a rooted five-fan

**Status:** written elementary lemmas and recorded negative finding / route
nonclosure; separate internal audit pending.  This note identifies the first
unsupported inference in a proposed composition inside the dominated
degree-eight case.  It is not a counterexample and does not close that case,
the eight-coordinate branch, Conjecture 21, or `HC_7`.

## 1. Exact setting

Let `G` be seven-connected and seven-chromatic, and suppose that every
proper minor of `G` is six-colourable.  Let `uv` be an edge and let `c` be a
proper six-colouring of `G-uv` with `c(u)=c(v)=0`.  Assume that `v` is
adjacent to every member of

\[
                         Q=N_G(u)-\{v\}.
\]

Put

\[
 \Gamma=c^{-1}(0),\qquad H=G-\{u,v\},\qquad K=G-\Gamma.
                                                               \tag{1.1}
\]

The audited saturated-set reduction proves that `chi(K)=5` and that every
proper five-colouring of `K` uses all five colours on `Q`.  It does **not**
prove that `H` is five-colourable: the established bounds are

\[
                         5\leq\chi(H)\leq6.                    \tag{1.2}
\]

Thus the colour-guided argument below must use a five-colouring of `K`, not
of `H`.  The universal rooted-five-fan theorem is instead applied in the
five-connected graph `H`.

## 2. What colour saturation really gives

Fix a proper five-colouring `eta` of `K`.  For each colour `i`, write

\[
                         Q_i=Q\cap\eta^{-1}(i).
\]

Every `Q_i` is nonempty.

### Lemma 2.1 (set-rooted bichromatic connectivity)

For every two distinct colours `i,j`, some component of

\[
                  K[\eta^{-1}(\{i,j\})]
\]

meets both `Q_i` and `Q_j`.

#### Proof

Suppose that no bichromatic component meets both sets.  Interchange `i` and
`j` on the union of all bichromatic components which meet `Q_i`.  This is a
proper five-colouring.  Every member of `Q_i` changes from `i` to `j`, and
no member of `Q_j` changes, so colour `i` is now absent from `Q`.  This
contradicts the saturated-set theorem. `\square`

### Corollary 2.2 (two disjoint set-rooted components)

For four distinct colours `a,b,c,d`, there are vertex-disjoint connected
subgraphs `D_ac,D_bd` such that

\[
 D_{ac}\cap Q_a\ne\varnothing,\quad
 D_{ac}\cap Q_c\ne\varnothing,
 \qquad
 D_{bd}\cap Q_b\ne\varnothing,\quad
 D_{bd}\cap Q_d\ne\varnothing.                               \tag{2.1}
\]

#### Proof

Choose the two components supplied by Lemma 2.1.  Their colour sets are
disjoint, so their vertex sets are disjoint. `\square`

This is a set-rooted Kempe conclusion.  It does not prescribe which member
of a non-singleton `Q_i` lies in the selected component.

## 3. The exact positive composition

Choose a rainbow transversal of the five sets `Q_i`.  The universal
five-terminal theorem gives a rooted model of

\[
                           F_5=K_1\vee P_4
\]

in `H`; the bijection between the five terminals and the roles of `F_5` is
not prescribed.  Label the returned bags by the colours of their roots.
Write `h` for the colour on the universal bag and

\[
                             a-b-c-d                           \tag{3.1}
\]

for the colour order on the four path bags.  The three adjacencies missing
from the guaranteed quotient are `ac,ad,bd`.  Adding `ac` and `bd` gives
`K_5-ad`, hence a `K_5^-` quotient.

Let `W` be the union of the five rooted bags.  A path has a **consecutive
endpoint-bag interval** for bags `B_i,B_j` if some subpath has one end in
each of those bags and all its internal vertices outside `W`.

### Proposition 3.1 (clean two-component composition)

Suppose that the components in Corollary 2.2 can be chosen so that

1. `D_ac` contains a consecutive endpoint-bag interval for `B_a,B_c`; and
2. `D_bd` contains a consecutive endpoint-bag interval for `B_b,B_d`.

Then `G` contains a `K_7^-` minor.

#### Proof

For the first interval, add all vertices except its `B_c` end to `B_a`.
This preserves connectivity and disjointness and creates the adjacency
`B_aB_c`.  Do the analogous operation from `B_b` towards `B_d`.  The two
operations are disjoint because `D_ac,D_bd` are vertex-disjoint and their
four endpoint bags are distinct.

The resulting five-bag quotient contains `F_5+ac+bd=K_5-ad`.  Each bag
still contains its selected member of `Q`.  Since both `u` and `v` are
complete to `Q` and `uv` is an edge, adjoining the singleton bags
`{u},{v}` gives a `K_7^-` model. `\square`

This is the same valid absorption mechanism as the audited consecutive-bag
interval theorem for a fixed-colouring `P_5` certificate.

## 4. The two unsupported quantifier exchanges

Corollary 2.2 does not establish the hypotheses of Proposition 3.1.

### 4.1. A set contact is not a contact with the colour-labelled bag

The component `D_ac` meets *some* vertices of `Q_a,Q_c`.  The rooted model
contains one selected vertex from each set, but the component need not meet
those selected vertices or their bags.  Choosing the component endpoints
first does not repair this: the universal rooted-five-fan theorem does not
prescribe which selected terminal is its hub or any of the four path
positions.  Contracting a connector before invoking that theorem would
identify two distinct terminal labels and is therefore invalid.

Since `|Q|=7` and five colours occur, at least three of the five sets `Q_i`
are singletons.  This improves some endpoint contacts, but it does not make
both missing matching pairs singleton-rooted for every unprescribed fan
labelling.  In the distribution `2,2,1,1,1`, for example, the two
non-singleton colours can occupy path positions paired separately with the
two singleton positions in `ac,bd`.

The adjacent set-endpoint barrier makes this failure explicit on nine
vertices.  It uses `Q=C_5\mathbin{\dot\cup}K_2`, a proper five-block
partition, a rainbow rooted `F_5`, and two disjoint connected subgraphs
meeting the two missing colour-block pairs.  The resulting graph has no
`K_5^-` minor.  Thus the set-to-selected-bag inference is false even before
dirty intersections with the model arise.

### 4.2. Disjoint components need not be clean relative to the model

Even if `D_ac` and `D_bd` meet the intended endpoint bags, they may run
through foreign fan bags.  Their disjointness from one another says nothing
about these model intersections.  Absorbing a segment through a foreign bag
can disconnect that bag or remove one of its indispensable adjacencies.

This is not merely a missing sentence.  The audited dirty-path barrier
starts from the stronger quotient `K_5-\{ae,bc\}` and supplies two
vertex-disjoint bichromatic paths for the missing matching edges.  An
exhaustive reassignment of every non-root vertex in the displayed support
still cannot obtain a rooted quotient with at most one missing adjacency.
That construction is target-rich and is neither seven-chromatic nor
contraction-critical, so it does not refute a theorem using the full host.
It does refute the purely local inference from two disjoint Kempe paths and
a five-root model.

## 5. Exact remaining theorem

The smallest positive repair is a protected, colour-rooted fan exchange in
the full dominated-centre host:

> For some five-colouring of `K`, choose a rainbow transversal of `Q` and
> an `F_5` model rooted at it.  Then either the two missing-matching colour
> pairs have bichromatic components with consecutive endpoint-bag intervals,
> or `H` already has a `Q`-meeting `K_5^-` model, or a labelled separation
> preserves the colouring and the five root roles.

The first two conclusions are terminal after adjoining `{u},{v}`.  A useful
separation conclusion must retain the colour-labelled roots and the same
Kempe components; an unlabelled smaller boundary repeats the earlier
quantifier loss.

Any proof of this theorem must spend information absent from the local
barrier, such as `K_7^-`-minor exclusion, contraction-criticality, the exact
order-eight two-shore response, or the additional bichromatic components
for the other colour pairs.  Set-valued Kempe completeness and the
black-box rooted-five-fan theorem alone do not prove it.

## Dependencies and scope

- [the saturated five-colour common-neighbour reduction](hc7_k7minus_dominated_singleton_rooted_five_reduction.md);
- [the universal five-terminal rooted-fan theorem](../results/hc7_five_terminal_rooted_fan.md);
- [the consecutive-bag absorption theorem](../results/hc7_degree8_simultaneous_p5_certificate.md);
- [the set-endpoint fan barrier](../barriers/hc7_dominated_colour_fan_set_endpoint_barrier.md); and
- [the dirty-path local uncrossing barrier](../barriers/hc7_degree8_dirty_path_local_uncrossing_barrier.md).
