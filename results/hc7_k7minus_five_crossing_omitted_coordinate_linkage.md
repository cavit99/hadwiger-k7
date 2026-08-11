# Omitted-coordinate linkages in the five-crossing row

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_five_crossing_omitted_coordinate_linkage_audit.md`](hc7_k7minus_five_crossing_omitted_coordinate_linkage_audit.md).
This is an unbounded, computation-free reduction of the five-crossing
three-cut residue in the five-centre common host.  It does not prove the
`K_7^-` six-colour conjecture or `HC_7`.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting

Assume the hypotheses and notation of the audited
[five-centre common-matching theorem](hc7_k7minus_five_centre_common_matching_reduction.md).
Thus `G` satisfies

\[
 \chi(G)=7,\qquad
 \chi(J)\leq6\text{ for every proper minor }J\text{ of }G,
 \qquad K_7^-\npreccurlyeq G,
\]

and

\[
 \kappa(G)\geq7,\qquad |E(G)|\geq4|V(G)|,
 \qquad \delta(G)\geq8,\qquad K_5\not\subseteq G,
 \qquad |V(G)|\geq25.
\]

There are five independent degree-eight centres
`Z={z_1,\ldots,z_5}` and distinct selected neighbours `x_i` such that

\[
                         \alpha(G[N_G(z_i)])=3
                         \qquad(1\leq i\leq5),
\]

and

\[
 M=\{e_i=z_ix_i:1\leq i\leq5\},\qquad H=G-M                 \tag{1.1}
\]

is a matching deletion with the punctured Boolean signature property:
for every nonempty `I\subseteq M`, there is a proper six-colouring of `H`
in which the ends of precisely the edges in `I` have equal colours.
Suppose that `H` has a three-cut `S`, that `H-S` has exactly two components
`A,D`, and that all five edges of `M` cross between them.  Write

\[
                         e_i=a_id_i,
 \qquad a_i\in A,\quad d_i\in D.                    \tag{1.2}
\]

The centre end may be `a_i` or `d_i`, independently for each `i`.  The
common-host theorem gives `|A|,|D|\geq6`.

For a transversal `X` choosing one end of every edge of `M`, call `X`
**mixed** when it meets both `A` and `D`.  We work in the no-descent row:
for every mixed `X`, the graph

\[
                         G-(S\mathbin{\dot\cup}X)                 \tag{1.3}
\]

has exactly the two components `A-(X\cap A)` and `D-(X\cap D)`, and both
are adjacent to every vertex of `S\mathbin{\dot\cup}X`.

An **`e_i`-anchored exact order-seven response** consists of a seven-set
`T`, a component `C` of `G-T`, and a proper six-colouring `c_i` of
`G-e_i` such that:

1. `G-T` has exactly two components, both full at `T`;
2. `T` contains one end of `e_i` and `C` contains the other;
3. `c_i` is proper on `G-C`; and
4. `c_i|_T` does not extend to a proper six-colouring of `G[C\cup T]`.

Thus the operation is tied to the literal selected edge of the named
centre, not merely to an unlabelled boundary partition.

## 2. The omitted-coordinate alternative

### Theorem 2.1

For every `i\in\{1,\ldots,5\}`, at least one of the following holds.

1. **Exact response.**  There is an `e_i`-anchored exact order-seven
   response.  The centre `z_i` lies either in its boundary or in its
   response component.
2. **Complete omitted-coordinate linkage.**  The graph `G-e_i` is
   seven-connected and contains seven internally vertex-disjoint
   `z_i`--`x_i` paths with the following common coordinate assignment:

   - for every `j\ne i`, a different path contains `e_j=a_jd_j` as a
     literal consecutive edge;
   - the remaining three paths meet the three different vertices of `S`;
   - for every choice of one end of each edge in `M-\{e_i\}`, the seven
     paths meet the resulting set together with `S` exactly once each;
     the path assigned to `e_j` meets its selected end, and each of the
     other paths meets its assigned vertex of `S`.

   These paths leave `z_i` through all seven vertices of
   `N_G(z_i)-\{x_i\}`.  Together with the edge `e_i`, they form eight
   internally vertex-disjoint `z_i`--`x_i` paths in `G`.

In outcome 2, `G` contains a minor

\[
                    K_2\vee G[N_G(z_i)-\{x_i\}],                  \tag{2.1}
\]

whose two `K_2` branch sets are rooted at `z_i,x_i` and whose other seven
branch sets retain the literal vertices of `N_G(z_i)-\{x_i\}`.  Hence

\[
                    K_5^-\npreccurlyeq G[N_G(z_i)-\{x_i\}].       \tag{2.2}
\]

Consequently, if no selected edge gives outcome 1, all five selected
edges give the complete linkage and rooted-join conclusions in outcome 2.

#### Proof

Fix `i` and put `J_i=G-e_i`.  For each transversal `X` of the other four
edges, put

\[
                         Q_X=S\mathbin{\dot\cup}X.                 \tag{2.3}
\]

There is no edge of `J_i-Q_X` between

\[
                 A_X=A-(X\cap A),\qquad
                 D_X=D-(X\cap D):                                \tag{2.4}
\]

the edges of `M-\{e_i\}` are covered by `X`, the edge `e_i` was deleted,
and `H-S` has components `A,D`.  Both displayed sets are nonempty because
`|A|,|D|\geq6`.

Extend `X` first by `d_i`.  Unless this is the all-`D` transversal, (1.3)
shows that `A_X` is connected; in the exceptional choice `A_X=A`, which
is connected by definition.  Extending instead by `a_i` proves in the
same way that `D_X` is connected.  A mixed extension also shows that every
vertex of `S` has a neighbour in each displayed set.  For a vertex of
`X`, its matching mate gives its contact with the opposite set, while
fullness in a mixed extension gives its contact with its home set.  Thus
`Q_X` is an order-seven separator of `J_i` with exactly the two full
components in (2.4).  The sixteen choices of `X` form a literal
four-dimensional separator cube.

Deleting one edge from a seven-connected graph lowers vertex connectivity
by at most one in the present setting.  Indeed, if a set `R` of at most
five vertices separated `J_i`, then the single restored edge `e_i` would
have to join the components of `J_i-R`.  There would be exactly two such
components, with the ends of `e_i` in different components.  At least one
would be nonsingleton because `|V(G)|\geq25`; adding its incident end of
`e_i` to `R` would give a proper separator of `G` of order at most six.
Therefore

\[
                          6\leq\kappa(J_i)\leq7,                   \tag{2.5}
\]

where the upper bound comes from (2.3).

Suppose first that `\kappa(J_i)=6`, and let `R` be a six-cut of `J_i`.
Since `G-R` is connected, `J_i-R` has exactly two components and the ends
`p,q` of `e_i` lie in different components.  Choose `p` in a nonsingleton
one and put `T=R\cup\{p\}`.  The set `T` is an actual seven-vertex cut of
`G`.  The audited
[three-component seven-cut exclusion](hc7_k7minus_three_component_seven_cut_exclusion.md)
upgrades it to exactly two full complementary components.  Let `C` be
the component containing `q`.

A proper six-colouring `c_i` of `G-e_i` exists by minor-criticality.  Its
two deleted-edge ends have the same colour, since otherwise it would also
colour `G`.  Its only possible improper edge after `e_i` is restored is
`pq`, and `q\in C`; hence `c_i` is proper on `G-C`.  If `c_i|_T` extended
through `G[C\cup T]`, that extension would glue to `c_i` outside `C` and
six-colour `G`.  This proves outcome 1.  Since one end of `e_i` is `z_i`,
the centre lies in `T` or `C` as asserted.

It remains that `\kappa(J_i)=7`.  Menger's theorem gives seven internally
vertex-disjoint paths between the ends `a_i,d_i` of `e_i`.  Every `Q_X`
separates those ends.  Its order is seven, so the seven paths meet `Q_X`
once each and exhaust it.

Start with the choice `X=\{d_j:j\ne i\}`.  For fixed `j\ne i`, replace
`d_j` by `a_j`.  Six boundary vertices are unchanged, so the path through
`d_j` in the first cut is the path through `a_j` in the second.  Traversed
from `A` to `D`, it meets `a_j` before `d_j`.  A vertex strictly between
them would belong to the `A`-side of the first cut and the `D`-side of the
second, which is impossible.  Thus `a_jd_j` is a literal consecutive edge
of that path.  Distinct coordinates lie on distinct paths.  The remaining
three paths meet the three vertices of `S`, and comparison with arbitrary
endpoint choices proves the stated common assignment over all sixteen
cuts.

The paths are also internally disjoint when viewed as `z_i`--`x_i` paths.
Since `d_{J_i}(z_i)=7`, their first vertices are precisely
`N_G(z_i)-\{x_i\}`.  Restoring `e_i` gives the eighth path.

For each `y\in N_G(z_i)-\{x_i\}`, delete the initial vertex `z_i` from
the corresponding path and absorb all remaining internal vertices except
`y` into one branch set rooted at `x_i`.  Internal disjointness shows that
no such path contains a second vertex of `N_G(z_i)-\{x_i\}`.  The union is
connected and adjacent to every retained singleton `y`.  Together with
the singleton branch set `\{z_i\}`, it gives (2.1), retaining every edge
of the displayed induced graph.  A `K_5^-` minor in that induced graph
would join the two rooted branch sets to form a `K_7^-` minor in `G`.
Target exclusion therefore proves (2.2). `\square`

## 3. Exact scope

The theorem removes the one-unit connectivity slack after any selected
coordinate is omitted.  It gives either a literal centre-edge response at
an exact seven-boundary or a complete seven-path coordinate system in the
corresponding one-edge-deleted graph.

In the all-linkage outcome, however, the quantifiers are only

\[
        \text{for every }i\text{ there exists a path family }\mathcal P_i.
\]

The five families belong to five different graphs `G-e_i` and may
intersect one another arbitrarily.  Neither this theorem nor the signed
four-coordinate Boolean theorem supplies simultaneous path families,
pairwise-adjacent branch sets, or a common equality partition on one
seven-boundary.  Exchanging these quantifiers would therefore be an
unsupported composition step.  The all-linkage outcome is a rigid
host-level residue, not yet a `K_7^-` model or a six-colouring of `G`.

## Dependencies

The five-edge matching, component-size bound and no-descent row come from
the audited common-matching theorem cited in Section 1.  The only other
promoted input is the audited order-seven two-component theorem cited in
the proof.  The coordinate comparison is the one used in the audited
[signed four-coordinate Boolean theorem](hc7_k7minus_four_crossing_signed_boolean_reduction.md),
but it is proved directly above because the present four-cube lies in
`G-e_i` rather than in the four-crossing row of `G`.
