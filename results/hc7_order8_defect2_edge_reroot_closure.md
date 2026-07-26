# Rerooting closes the aligned order-eight edge-component case

**Status:** written proof; separate internal audit **GREEN** in
[`hc7_order8_defect2_edge_reroot_closure_audit.md`](hc7_order8_defect2_edge_reroot_closure_audit.md).
This theorem eliminates one complete aligned small-shore branch.  It does
not prove `HC_7`.

## 1. Setting

Let `G` be seven-connected and satisfy

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G.
\tag{1.1}
\]

Let `u` have degree eight, put

\[
                              S=N_G(u),
\tag{1.2}
\]

and suppose that `G-N_G[u]` has exactly two components `E,F`, each
`S`-full.  Assume

\[
V(E)=\{v,w\},\qquad vw\in E(G).
\tag{1.3}
\]

Here a connected subgraph disjoint from `S` is **`S`-full** when it has a
neighbour at every vertex of `S`.

For `x in {v,w}`, define its boundary defect by

\[
                         \Delta_x=S-N_G(x).
\tag{1.4}
\]

Since the component `E` is collectively `S`-full,

\[
                         \Delta_v\cap\Delta_w=\varnothing.
\tag{1.5}
\]

## 2. Defect-two rerooting

### Theorem 2.1

Neither endpoint of `E` has boundary defect of order two.

### Proof

Suppose, by symmetry, that

\[
                            \Delta_v=\{r,s\}.
\tag{2.1}
\]

Collective `S`-fullness of `E` forces

\[
                              wr,ws\in E(G).
\tag{2.2}
\]

The component property gives no edge from `v` to `F`, and `v` is not
adjacent to `u` because `v` lies outside `N_G[u]`.  Hence

\[
                  N_G(v)=\{w\}\mathbin{\dot\cup}(S-\{r,s\}),
\tag{2.3}
\]

so `d_G(v)=7`.  Put

\[
                         T=N_G(v),\qquad R=G-N_G[v].
\tag{2.4}
\]

The original vertex partition gives the exact identity

\[
                       V(R)=V(F)\mathbin{\dot\cup}\{u,r,s\}.
\tag{2.5}
\]

The graph `R` is nonempty and connected: `F` is connected and has a
neighbour at `r`, while `ur` and `us` are edges.

Choose any proper six-colouring of the proper minor `G-vw`.  The partition

\[
                    V(G)=\{v\}\mathbin{\dot\cup}T
                              \mathbin{\dot\cup}V(R),
\tag{2.6}
\]

together with the selected edge `vw`, is a generic exact-seven response
interface with singleton operated shore `{v}`.  Indeed, `T=N_G(v)`,
`|T|=7`, the two open shores are nonempty and anticomplete, and the selected
edge joins `v` to the boundary vertex `w`.  The automatic-response lemma
then supplies the rejected intact-shore boundary partition; no inherited
order-eight labels are required.

The promoted singleton exact-seven terminal theorem therefore applies to
the new boundary `T`.  It says that the maximum number `nu_T(R)` of
pairwise vertex-disjoint connected subgraphs of `R` adjacent to every
literal vertex of `T` is

\[
                              \nu_T(R)=1.
\tag{2.7}
\]

Now consider the two induced subgraphs

\[
                  P_1=G[V(F)\cup\{r\}],\qquad
                  P_2=G[\{u,s\}].
\tag{2.8}
\]

They lie in `R`, are vertex-disjoint, and are connected: `F` has a
neighbour at `r`, and `us` is an edge.  Both are `T`-full.  For every
`t in S-{r,s}`, the component `F` supplies a `P_1`--`t` edge and `u`
supplies a `P_2`--`t` edge.  At the remaining boundary vertex `w`, the
edges `wr` and `ws` supply the two contacts.  Consequently

\[
                              \nu_T(R)\ge2,
\tag{2.9}
\]

contradicting (2.7).  Thus \(|\Delta_v|\ne2\).  Interchanging `v,w`
proves \(|\Delta_w|\ne2\). \(\square\)

## 3. Complete aligned edge-component closure

### Corollary 3.1

Under the setting of Section 1, no component `E` satisfying (1.3) exists.

### Proof

For either endpoint `x` of `E`, componenthood gives

\[
                          d_G(x)=1+(8-|\Delta_x|)
                                =9-|\Delta_x|.
\tag{3.1}
\]

Seven-connectivity gives minimum degree at least seven, so
\(|\Delta_x|\le2\).  If both endpoint defects have order at most one, the
promoted near-full edge-component theorem gives a contradiction.  If at
least one has order two, Theorem 2.1 gives a contradiction.  These cases
are exhaustive. \(\square\)

## 4. Exact gain and limitation

Corollary 3.1 eliminates every aligned order-eight two-vertex exterior
component, including all mixed defect profiles of orders zero, one and two.
The defect-two branch uses the host's global minor-criticality and
seven-connectivity through the generic exact-seven response and singleton
packing-one theorems; it requires no further order-eight enumeration.

The result does not force either aligned exterior component to have order
two.  It does not close another small-shore shape, the minimum-boundary
interface with exactly two full components, the general bounded-interface
composition theorem, or `HC_7`.

## 5. Direct dependencies

- [generic exact-seven selected responses](hc7_generic_exact7_response_restart.md), Definition 1.1 and Lemma 1.1;
- [singleton exact-seven packing-one theorem](hc7_singleton_exact7_terminal_normal_form.md), Theorem 2.1; and
- [near-full edge-component closure](hc7_order8_nearfull_edge_triangle_closure.md), Corollary 6.2.
