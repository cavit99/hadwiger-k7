# Two helpers with at most one missing contact

**Status, 21 September 2026:** written proof with a separate GREEN
internal audit, recorded in the [adjacent audit](five_root_one_missing_contact_audit.md).
This proves the stated rooted helper theorem subject to the cited
minimal-counterexample reductions, including the new degree-six
reduction. It does not by itself prove Conjecture 21 or HC7, or establish
the user's requested comparison in significance with Norin–Totschnig.

## Statement and exact inputs

For a finite simple graph `G` and five distinct roots `X`, put

`rho4(G,X)=|E(G)-E(G[X])|-4|V(G)-X|`.

For `Y subset V(G)-X`, let `N_G(Y)` be its external neighbourhood and
let `rho_G(Y)` count all edges with at least one end in `Y`, minus
`4|Y|`. Say `(G,X)` is **4-light** if `rho_G(Y)<=0` whenever
`|N_G(Y)|<=4`.

**Theorem.** Every 4-light five-rooted graph with `rho4(G,X)>=2` has
five disjoint nonempty connected bags, each containing its prescribed
root and no other root, and two further disjoint nonempty connected
bags containing no root, such that at least ten of the eleven possible
helper–root and helper–helper pairs are adjacent. No root–root contact
is required.

The proof uses the following separately written inputs.

1. The [audited minimal-counterexample reduction](hc7_c21_rooted_density_low_degree_reduction.md),
   including its rooted star lemma and its exact contraction obstruction.
2. The [degree-five elimination](hc7_c21_helper_degree_six.md),
   which upgrades the nonroot minimum degree to six. The mathematical
   text has a separate GREEN internal audit; the promoted source hash is
   `85927a0f7d1af6229930fd67f7144eac35b934c54ad504539a34d39e209020ee`.
3. Mader's atom theorem, in the precise form reproduced as Theorem 5 of
   Kriesell–Schmidt, [*More on foxes*, arXiv:1610.09093v1, printed page 5](https://arxiv.org/pdf/1610.09093v1).
   Its overbar and set difference were checked in the rendered primary
   PDF, rather than inferred from the extracted text.

Here is the exact atom input with its notation defined. For a graph `Q`
of connectivity `k`, let `T(Q)` be its separating sets of order `k`.
A `T`-fragment is a nonempty union of components of `Q-T` other than
their entire union. Given a family `Sfam` of vertex sets, an
`Sfam`-fragment is a `T`-fragment for which some member of `Sfam` is
contained in `T`. An `Sfam`-atom is an `Sfam`-fragment of minimum
cardinality. If `A` is such an atom, write `T_A=N_Q(A)` and
`barA=V(Q)-(A union T_A)`. If there are `S in Sfam` and `T in T(Q)`
such that

`S subset T-barA` and `T intersect A` is nonempty,

then Mader's theorem gives

`A subset T` and `|A|<=|T-T_A|/2`.

No assumption that every edge is noncontractible is part of this
statement. We will verify its two local hypotheses for the entire
family of relevant fragments, not merely for positive-density sides.

## 1. The minimum counterexample and its low-triangle edges

Suppose the theorem is false and minimize `(|V(G)|,|E(G)|)`
lexicographically over counterexamples. The first two inputs give:

- `X` is independent, `rho4(G,X)=2`, and `G-X` is nonempty;
- `(G,X)` is internally five-connected: every nonempty root-free set
  has at least five external neighbours;
- every nonroot has degree at least six and at most three neighbours
  in `X`;
- every proper root-free five-boundary side `Y` has `rho_G(Y)<=1`.

The last condition means that `Y` is nonempty, `|N_G(Y)|=5`, and
`Y union N_G(Y)` is a proper subset of `V(G)`.

Let `Q0=G+K_X`, and for each original edge `e` let `t(e)` be its number
of common neighbours in `Q0`. Define `E0` to consist of the original
edges with at least one nonroot end and `t(e)<=3`. Thus virtual
root–root edges are never members of `E0`.

For every `e in E0`, the rooted quotient satisfies

`rho4(G/e)=rho4(G)+3-t(e)>=2`.

If it were 4-light, minimum order would give the desired model in
`G/e`. Replacing its contracted vertex by the fixed connected preimage
of `e` lifts every bag and contact; if the edge has a root end, its
preimage belongs only to that root's prescribed bag. Thus the quotient
is not 4-light. The audited contraction-obstruction lemma consequently
supplies a proper root-free fragment `Y_e` with

`|N_G(Y_e)|=5`, `rho_G(Y_e)=1`, and `V(e) subset N_G(Y_e)`.

We need the existence of these cuts, rather than an assertion that all
five-fragments have positive density.

## 2. A small weighted neighbourhood always meets a low-triangle edge

**Claim.** If a nonroot `v` satisfies
`deg_G(v)+|N_G(v) intersect X|<=9`, then some edge incident with `v`
belongs to `E0`.

**Proof.** Suppose all incident edges have `t(e)>=4`. Set
`H=G[N_G(v)]`, `X0=N_G(v) intersect X`, and `r=|X0|`. Each vertex
`u in V(H)-X0` has `deg_H(u)=t(uv)>=4`. Each `u in X0` has
`deg_H(u)=t(uv)-(r-1)>=5-r`. The set `X0` is independent, is a proper
subset of `V(H)`, and `|V(H)|+r<=9`. Properness also follows from
`deg_G(v)>=6` and `r<=3`.

There are five disjoint paths from `X` to `N_G(v)` in `G-v`. Otherwise
Menger's theorem supplies a separator of at most four vertices between
these sets; in `G` the component containing `v` after deleting that
separator has no original root, contradicting internal
five-connectivity. Truncate each path when it first reaches `N_G(v)`.
Their five distinct endpoints form a set `Z` containing `X0`; each
original root already in `N_G(v)` has its trivial path. No other path
vertex belongs to `N_G(v)`.

The rooted star lemma gives a connected bag `C` at some
`z in Z-X0`, containing no other vertex of `Z`, adjacent to all four
singleton bags in `Z-{z}`. Explicitly it gives
`C=(V(H)-Z) union {z}`, so `C` avoids all original roots.

Take `{v}` and `C` as helpers. For the four paths ending in
`Z-{z}`, take the whole path as its root bag. For the path ending at
`z`, take the path with `z` removed. This last bag is nonempty because
`z` is not an original root; its last edge reaches `C`. The five root
bags are connected and retain exactly their prescribed roots. They
avoid both helpers because path interiors avoid `N_G(v)` and `v`.
The helper `C` meets all five root bags, `{v}` meets the four other
root bags, and the helpers are adjacent through `vz`. These are ten
required contacts, a contradiction. This proves the claim.

In particular `E0` is nonempty. Indeed, write `m=|V(G)-X|`.
A nonroot has degree at most `m-1+3=m+2`, so the minimum degree six
implies `m>=4`. Double-counting incident edges gives

`sum_{v outside X}(deg_G(v)+deg_X(v))=8m+4`.

Some nonroot therefore has weight at most nine, and the claim applies.

## 3. Padding makes the minimum atom avoid the roots

Introduce a new set `W` of `|V(G)|+1` vertices. Let `Q` be obtained
from `G` by making `X union W` a clique and adding no edges between
`W` and `V(G)-X`. This is only an auxiliary graph used to select a
fragment. No minor model or density induction is performed in `Q`.

The graph `Q` is five-connected. After removing at most four vertices,
the remaining vertices of `X union W` form one connected set containing
an original root. A different component would be root-free and would
have boundary of order at most four in `G`. Also `Q-X` separates the
nonempty set `G-X` from `W`, so `kappa(Q)=5` exactly.

Adding `W` changes neither the neighbourhood nor the incident edges
of a subset of `G-X`. It also changes no common-neighbour count of an
original edge with a nonroot end: no vertex of `W` is adjacent to
that end. In particular the family `E0` still has its original meaning.

Set `Sfam={V(e):e in E0}`. Every previously obtained `Y_e` remains
a fragment of `Q`, with the same five-neighbour boundary containing
`V(e)`. Hence `Sfam`-fragments exist. Choose an `Sfam`-atom `A` in
`Q`, minimizing cardinality over **all** such fragments. Since one
of the `Y_e` is available,

`|A|<=|Y_e|<=|V(G)-X|`.

The atom contains no vertex of `X union W`. Otherwise, with
`T_A=N_Q(A)` of size five, connectedness of the clique
`(X union W)-T_A` forces all its vertices into `A`. This gives

`|A|>=|X union W|-5=|W|>|V(G)-X|`,

a contradiction. Thus `A subset V(G)-X`, and its neighbourhood in
`Q` equals its neighbourhood in `G`.

Moreover `A union N_G(A)` is proper in `G`. If it were all of `G`,
the five-element boundary, being disjoint from the root-free set
`A`, would contain all five original roots and hence equal `X`.
It could not then contain a member of `Sfam`, each of which has a
nonroot vertex. This would contradict the definition of an
`Sfam`-fragment. We therefore have `rho_G(A)<=1`.

## 4. The atom meets a new low-triangle edge

The atom has at least three vertices. If `a=|A|` were one or two,
the minimum nonroot degree six would give

`rho_G(A)=sum_{v in A}deg_G(v)-e(G[A])-4a`
`>=2a-binomial(a,2)>=2`,

contrary to `rho_G(A)<=1`.

Write `S_A=N_G(A)`. Since every neighbour of a vertex in `A` lies
in `A union S_A`, double-counting gives

`sum_{v in A}(deg_G(v)+deg_{S_A}(v))=8|A|+2rho_G(A)`
`<=8|A|+2`.

As `|A|>=3`, some `v in A` has the displayed summand at most eight.
Every original-root neighbour of `v` lies in `S_A`, so
`deg_G(v)+deg_X(v)<=8`. Section 2 supplies an incident edge
`f=vu in E0`. Its other endpoint lies in `A union S_A`.

Take the blocker `Y_f` from Section 1 and put `T=N_Q(Y_f)`. This
is a separating set of size five in `Q`, hence `T in T(Q)`, and
`V(f) subset T`. Furthermore `v in A intersect T`, while

`V(f) subset A union T_A=V(Q)-barA`.

Consequently `V(f) subset T-barA`. These are exactly the two local
hypotheses of Mader's atom theorem, with `S=V(f) in Sfam`.
It follows that

`|A|<=|T-T_A|/2<=5/2`,

so the integer `|A|` is at most two. This contradicts Section 4's
lower bound. The minimum counterexample does not exist, proving the
rooted helper theorem.

## Audit scope and the remaining global obligation

The new inference requiring independent challenge is the padded
`Sfam`-atom application: padding must exclude all root-containing
minimum atoms, and the selected low edge must meet the atom while its
two endpoints stay outside the complementary fragment. Sections 3–4
verify both facts explicitly. The atom minimizes over every eligible
fragment, so no positive-density closure under intersection is assumed.

The only inductive reductions used by the cited inputs decrease the
finite lexicographic parameter `(|V|,|E|)` and lift through fixed
disjoint connected preimages. Padding is neither a reduction nor a
graph claimed to inherit chromatic criticality. The final argument
constructs the helper model in the original graph or contradicts the
existence of its minimum counterexample.

The global composition needed for Conjecture 21, and the user's HC7
or comparable-theorem criterion, are separate obligations. They are
not established by this rooted statement alone.
