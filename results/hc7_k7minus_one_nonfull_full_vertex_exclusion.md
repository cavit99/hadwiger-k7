# Full-side vertices exclude minimum-shore recentering

**Status:** written proof; separate internal audit GREEN for this revision.
The proof is unbounded but inherits the computer-assisted trust boundary of
the cited degree-eight exterior-component and uniform defect-two reflection
theorems.  It does not prove that every exceptional anti-neighbourhood is
connected or settle the `K_7^-` six-colour conjecture.

Throughout, let `G` satisfy

\[
 \kappa(G)\ge7,
 \qquad \chi(G)=7,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G,
 \qquad K_7^-\npreccurlyeq G.                         \tag{H}
\]

## Theorem 1 (no full-side vertex sees the common seven-set)

Let `u` be an exceptional vertex of degree eight, put `X=N_G(u)`, and
suppose that `G-N_G[u]` has components `D,F`, where `D` misses
`x\in X` and `F` is adjacent to every vertex of `X`.  Put

\[
                              S=X-\{x\}.
\]

No vertex of `F` is adjacent to every vertex of `S`.

### Proof

Suppose that `v\in F` is adjacent to every vertex of `S`.  The singleton
`P=\{v\}` is then an `S`-full connected subgraph of `F`.  Apply the
[tight nested-cut theorem](hc7_k7minus_one_nonfull_k5_and_nested_cut.md#theorem-4-tight-nested-cut-reduction)
to this choice of `P`.  If `K` is the component containing `x` in

\[
                         G[(F\cup\{x\})-\{v\}],
\]

and

\[
 A=N_G(K)\cap S,
 \qquad
 B=N_G(K)\cap\{v\},
\]

that theorem gives

\[
                         |A|\le4,
 \qquad
                         |A|+|B|\ge6.                 \tag{1}
\]

But `B\subseteq\{v\}`, so `|B|\le1`.  The second inequality in (1)
therefore gives `|A|\ge5`, contradicting the first.  In the proof of the
cited theorem, the case `|A|\ge5` invokes the audited uniform defect-two
connected-subgraph reflection theorem and produces a six-colouring of `G`.
Thus the contradiction has the required colouring terminal. \(\square\)

## Theorem 2 (minimum exceptional exterior)

Suppose that some exceptional degree-eight vertex has disconnected
anti-neighbourhood.  Choose an exceptional degree-eight vertex `u` and a
component `E` of `G-N_G[u]` with minimum order among all components of all
disconnected exceptional degree-eight anti-neighbourhoods.  Then every
degree-eight vertex in `E` has connected anti-neighbourhood.

### Proof

Put `X=N_G(u)`.  The audited degree-eight exterior-component theorem gives

\[
                         G-N_G[u]=E\mathbin{\dot\cup}F               \tag{2}
\]

for one other component `F`.  The two-component literal-clique exclusion
implies that `G` has no literal `K_5`.  The exact degree-seven
neighbourhood theorem then gives `\delta(G)\ge8`, and every degree-eight
vertex is exceptional.

The component `E` is not a singleton.  Indeed, if `E=\{e\}`, then
minimum degree gives `N_G(e)=X`.  A six-colouring of the proper minor
`G-u` assigns to `e` a colour absent from `X`; assigning the same colour
to the nonadjacent vertex `u` would six-colour `G`, a contradiction.

Let `v\in E` have degree eight and suppose, for a contradiction, that
`G-N_G[v]` is disconnected.  Since `E` is connected and has at least two
vertices, `v` has a neighbour in `E`.  Consequently

\[
 |N_X(v)|\le7,
 \qquad
 Y:=X-N_G(v)\ne\varnothing.                           \tag{3}
\]

The set `\{u\}\cup Y` is connected in `G-N_G[v]`.  If `F` had a
neighbour in `Y`, it would lie in that same component.  Every other
component would then be contained in

\[
                         E-(\{v\}\cup N_E(v))
\]

and would have order at most `|E|-2`, contrary to the minimum choice of
`E`.  Hence `F` has no neighbour in `Y`.

Seven-connectivity gives `|N_X(F)|\ge7`, while

\[
                         N_X(F)\subseteq X-Y=N_X(v).
\]

Together with (3), this forces

\[
 Y=\{y\},
 \qquad
 N_X(F)=N_X(v)=S:=X-\{y\}.                            \tag{4}
\]

The two exterior components at `u` cannot miss the same neighbour of `u`.
Since `F` misses `y`, the component `E` has a neighbour at `y`.  It is
therefore adjacent to every vertex of `X`: the vertex `v\in E` sees every
vertex of `S`, and some vertex of `E` sees `y`.

Thus, relative to `u`, the component `F` is the unique nonfull component,
it misses `y`, and `E` is the full component.  But `v\in E` is adjacent
to every vertex of `S`, contradicting Theorem 1.  Therefore
`G-N_G[v]` is connected. \(\square\)

## Exact scope

Theorem 2 eliminates the complete exact order-seven/eight minimum-shore
rotation: its only putative recentering vertex is forbidden by Theorem 1,
and the underlying reflection produces a six-colouring.  It is stronger
than an isolated boundary-graph exclusion and uses no new finite census.

It does not eliminate the originally selected disconnected centre `u`.
The minimum component `E` may contain no degree-eight vertex, or may contain
degree-eight vertices whose own anti-neighbourhoods are connected.  The
general one-nonfull, distinct-adjacent-miss, and both-full configurations
therefore remain open.

## Inputs

- [one-nonfull tight nested-cut theorem and uniform defect-two reflection](hc7_k7minus_one_nonfull_k5_and_nested_cut.md)
- [degree-eight exterior-component upper bound](hc7_low_degree_exterior_component_bounds.md)
- [exact degree-seven neighbourhoods](hc7_k7minus_degree7_clique_incidence.md)
- [same-miss exclusion](hc7_k7minus_nonfull_attachment_reduction.md)
