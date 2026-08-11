# Synchronized Kempe paths at a five-centre two-cut

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_five_centre_distance_one_paths_audit.md`](hc7_k7minus_five_centre_distance_one_paths_audit.md).
This note synchronizes the two opposite shore responses in the
five-centre two-cut reduction.  It produces four induced odd cycles sharing
one literal opposite-shore path, and it proves an exact attachment bound for
every component left by any of the five selected paths.  It does not
eliminate the order-at-least-eight branch and does not prove the
`K_7^-` six-colour conjecture.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting

Use the hypotheses and notation of the audited
[five-centre two-cut reduction](../results/hc7_k7minus_five_centre_two_cut_reduction.md).
Thus `G` is seven-connected and seven-chromatic, every proper minor of `G`
is six-colourable, and

\[
 S=Z\mathbin{\dot\cup}\{p,q\},\qquad |Z|=5,
 \qquad pq\notin E(G),
\tag{1.1}
\]

where `Z` is independent.  The graph `G-S` has exactly two connected
components `C,D`, both adjacent to every literal vertex of `S`.  The
permitted response on the closed `C`-shore has `Z` monochromatic and
`p=q`; the permitted response on the closed `D`-shore has `Z`
monochromatic and `p!=q`.

Contracting `D union Z` to a vertex `x` gives the proper minor `M_C` from
the two-cut reduction.  The graph `M_C+pq` is exactly seven-chromatic and
`pq` is a critical edge.  Choose one proper six-colouring `phi_C` of
`M_C`, pull it back to `G[C union S]`, and name the colours so that

\[
 \phi_C(Z)=\alpha,
 \qquad \phi_C(p)=\phi_C(q)=\beta.
\tag{1.2}
\]

Here `x` has colour `alpha`.  Put

\[
                    \Gamma=[6]-\{\alpha,\beta\}.
\tag{1.3}
\]

When minimum-side descent is discussed, choose `C` with minimum order
among the equality-response components obtained from all two-cuts of
`F=G-Z`.  This convention is legitimate because every such two-cut has
exactly one equality-response component.  It only controls another actual
two-cut of `F` whose equality-response component has smaller order.

## 2. Four distance-one transitions with one common opposite path

### Theorem 2.1 (synchronized odd paths)

There are paths

\[
                         P_\gamma\quad(\gamma\in\Gamma)
       \qquad\hbox{and}\qquad R                         \tag{2.1}
\]

with all of the following properties.

1. Each `P_gamma` is an induced `p`--`q` path with nonempty interior in
   `C`.  Under the one fixed colouring `phi_C`, it uses only
   `beta,gamma`.
2. The path `R` is an induced `p`--`q` path with nonempty interior in
   `D`.  For every `gamma in Gamma`, there is a permitted colouring of the
   closed `D`-shore under which this same literal path `R` uses only
   `beta,gamma`, with `p` coloured `beta` and `q` coloured `gamma`.
3. For each `gamma`, the two boundary traces differ by exactly the
   `beta`--`gamma` interchange on the singleton boundary component
   `{q}`.  The two full shore components containing `{q}` also contain
   `{p}`; `P_gamma` and `R` are the two corresponding obstruction paths.
4. Distinct paths `P_gamma,P_lambda` are edge-disjoint.  Every vertex in
   their intersection is `beta`-coloured under `phi_C`.
5. Each

   \[
                              O_\gamma=P_\gamma\cup R
   \tag{2.2}
   \]

   is an induced odd cycle.  The four cycles have the same literal
   `D`-shore segment `R`.

#### Proof

Fix `gamma in Gamma`.  Criticality of `pq` in `M_C+pq` implies that `p,q`
belong to one `beta`--`gamma` component of `M_C`: otherwise interchanging
the two colours on the component containing `p` would give the ends of
`pq` different colours and restore that edge.  The component avoids `x`,
whose colour is `alpha`, and it avoids `Z` after pullback.  Choose a
shortest `p`--`q` path in it and call it `P_gamma`.  Its internal vertices
lie in `C`, and shortestness makes it induced.

Now fix one permitted colouring `phi_D` of `G[D union S]`.  Align the
colours on `Z` and at `p` with `alpha,beta`.  The colour at `q` is some
`gamma_0 in Gamma`.  The response theorem says that the
`beta`--`gamma_0` component containing `p` also contains `q`; equivalently,
otherwise a Kempe interchange at one pole would change the distinct
response into the forbidden equal response.  Choose a shortest such path
`R`.  It has nonempty interior in `D` and is induced.

For any `gamma in Gamma`, permute the four colour names in `Gamma` in
`phi_D`, fixing `alpha,beta` and sending `gamma_0` to `gamma`.  This is
again a permitted `D`-shore colouring, and the same literal path `R` is
now a `beta`--`gamma` path.

On the boundary `S`, the equal trace has `p,q` both coloured `beta`, while
the corresponding distinct trace has `p` coloured `beta` and `q` coloured
`gamma`.  No other boundary vertex has either colour: every member of `Z`
has colour `alpha`, and `pq` is absent.  Hence the boundary two-colour
graph has precisely the two singleton components `{p},{q}`, and the traces
differ by interchanging the colours on `{q}`.  The obstruction in each
closed shore therefore joins these same two singleton components.  This is
also the two-parallel-edge case of the audited
[two-shore incidence theorem](../results/hc7_two_shore_kempe_incidence_cycle.md).

For distinct `gamma,lambda`, a common vertex of `P_gamma,P_lambda` has a
colour in

\[
       \{\beta,\gamma\}\cap\{\beta,\lambda\}=\{\beta\}.
\]

A common edge is impossible, since its other end would have to receive
both `gamma` and `lambda`.  This proves item 4.

The ends of `P_gamma` have the same colour, so its length is even.  The
ends of `R` have different colours, so its length is odd.  Since `pq` is
absent, both paths have nonempty interiors.  Their interiors lie in the
anticomplete sets `C,D`, respectively.  Thus their union is an odd cycle.
Each constituent path is induced, there is no edge between their
interiors, and `pq` is absent, so the cycle itself is induced.  This proves
item 5 and the theorem. \(\square\)

The point of Theorem 2.1 is literal synchronization: the four equality-side
paths use one colouring, and all four are paired with one and the same
opposite-shore path.  No permutation of path labels or boundary vertices
remains.

## 3. Rooted infeasibility forces three path attachments

The next lemma is independent of the colouring construction.

### Lemma 3.1 (path-deletion attachment inequality)

Let `X` be one of `C,D`, let `X'` be the other component, and let `P` be a
`p`--`q` path whose nonempty interior `P^circ` lies in `X` and which avoids
`Z`.  Suppose the rooted instance `(G[X union S],Z,p,q)` is infeasible.
For every component `A` of

\[
                              G[X-P^\circ],             \tag{3.1}
\]

put

\[
 a(A)=|N_G(A)\cap Z|,
 \qquad h(A)=|N_G(A)\cap V(P)|.                        \tag{3.2}
\]

Then

\[
 N_G(A)=(N_G(A)\cap Z)\mathbin{\dot\cup}
        (N_G(A)\cap V(P)),                            \tag{3.3}
\]

and

\[
                   a(A)+h(A)\ge7,
          \qquad   a(A)\le4,
          \qquad   h(A)\ge3.                         \tag{3.4}
\]

#### Proof

The only neighbours of `X` outside `X` are in `S`, and `X` is
anticomplete to `X'`.  Different components of (3.1) are anticomplete.
The deleted vertices are precisely `P^circ`, while the two poles are the
ends of `P`.  This proves the exact neighbourhood identity (3.3).

The nonempty opposite component `X'` lies beyond this neighbourhood, so
`N_G(A)` separates `A` from `X'`.  Seven-connectivity gives

\[
                              a(A)+h(A)\ge7.            \tag{3.5}
\]

If `a(A)=5`, then every root in `Z` has a neighbour in the connected set
`A`.  After deleting all vertices of `P`, the set `A union Z` therefore
lies in one connected component.  The path `P` would witness feasibility
of the rooted instance, a contradiction.  Thus `a(A)<=4`, and (3.5)
gives `h(A)>=3`. \(\square\)

### Corollary 3.2 (the five selected paths)

Assume the full rooted instance is infeasible on both shores.  Every
component left in `C` by the interior of any `P_gamma`, and every component
left in `D` by the interior of `R`, misses at least one centre and has at
least three distinct neighbours on the corresponding path.

At most one of the four paths `P_gamma` spans all of `C`.  Consequently at
least three of them leave a nonempty component, and every such component
satisfies (3.4).

#### Proof

The first assertion is Lemma 3.1.  If two distinct paths `P_gamma` and
`P_lambda` both had interior vertex set `C`, every vertex of `C` would lie
on both paths and hence would be `beta`-coloured by Theorem 2.1(4).  But
`P_gamma` has a `gamma`-coloured internal vertex adjacent to `p`, a
contradiction.  Thus at most one path spans `C`. \(\square\)

This strengthens the bare fact that each selected path separates the five
roots.  A component with only two path neighbours is impossible: seven-
connectivity would force it to be adjacent to all five roots, which would
make the path feasible.

The same calculation gives a prescribed three-fan inside every residual
component.

### Lemma 3.3 (a prescribed triple reaches the path disjointly)

Retain the hypotheses and notation of Lemma 3.1.  Let `A` be one of the
components in (3.1), and let `T subseteq A` have order three.  There are
three pairwise vertex-disjoint paths from the three distinct vertices of
`T` to three distinct vertices of `N_G(A) cap V(P)`, with every internal
vertex in `A`.

Consequently, if `T` induces a triangle, then `T` and `P` support four
pairwise adjacent connected branch sets: three disjoint sets containing
the respective vertices of `T`, and the path `P` itself.

If, in addition, a vertex `z` outside these four sets is adjacent to all
three vertices of `T`, then adjoining the singleton branch set `{z}` gives
a `K_5^-` minor model: its only possibly missing adjacency is from `{z}`
to the path branch set.  If `z` has a neighbour on `P`, the model is a
`K_5` model.

#### Proof

Apply Menger's theorem in the graph induced by

\[
                         A\cup(N_G(A)\cap V(P))
\tag{3.6}
\]

between `T` and `N_G(A) cap V(P)`.  Suppose a separator `K` of order at
most two existed.  At least one vertex of `T` survives.  Let `W` be the
union of the components of `A-K` which contain surviving vertices of `T`
and do not meet the path-neighbour set after deleting `K`.  Then `W` is
nonempty and

\[
                         N_G(W)\subseteq K\cup N_Z(A).
\tag{3.7}
\]

Indeed, different components of `A-K` are anticomplete, every edge from
`A` to `V(P)` ends in the target set in (3.6), and `A` has no other
neighbours outside `A` except its centre neighbours.  Lemma 3.1 gives
`|N_Z(A)|<=4`, so (3.7) would be a separator of order at most six between
`W` and the nonempty opposite shore.  This contradicts seven-connectivity.
Menger's theorem therefore gives the three disjoint paths with distinct
ends.

When `T` is a triangle, delete each path endpoint on `P` from its path and
use the remaining connected set as the corresponding branch set (a
singleton is allowed).  The triangle edges make these three sets pairwise
adjacent, and their three last edges make each adjacent to the disjoint
branch set `P`. \(\square\)

In the all-five-root row, where a centre's three contacts in one shore form
a triangle disjoint from the selected pole path, Lemma 3.3 supplies a
shore-confined three-fan from that literal triangle to the same synchronized
path.  This is still only one connected completing set; it does not produce
the two disjoint pole-labelled completing sets required for a terminal
`K_7^-` model.

## 4. The odd-cycle connector alternative

### Lemma 4.1

Fix `gamma in Gamma` and let `O_gamma` be the induced odd cycle from
Theorem 2.1.  Exactly one of the following holds.

1. Some component of `G-V(O_gamma)` contains all five vertices of `Z`.
2. The vertices of `Z` lie in at least two components of
   `G-V(O_gamma)`, and every component meeting `Z` has at least seven
   distinct neighbours on `O_gamma`.

In particular, if `|O_gamma|=5`, outcome 1 holds.  If `|O_gamma|=7` and
outcome 1 fails, then `O_gamma` is an exact order-seven cut and
`G-V(O_gamma)` has exactly two components, both adjacent to every vertex
of the cycle.

#### Proof

If no component contains all of `Z`, the five roots occupy at least two
components.  Let `K` be one which meets `Z`.  Its neighbourhood is
contained in `V(O_gamma)`, and another root lies outside
`K union N_G(K)`.  Thus `N_G(K)` is a genuine separator.  Seven-
connectivity gives `|N_G(K)|>=7`, proving the dichotomy and the order-five
consequence.

Suppose now that the cycle has order seven and outcome 1 fails.  Every
component of its deletion is full to the cycle by seven-connectivity.  The
audited
[critical seven-cut capacity theorem](../results/hc7_k7minus_critical_seven_cut_capacity.md)
says that there are at most three components.  There cannot be three:
that theorem would require every proper three-colouring of the boundary
cycle to have class sizes `3,2,2`, whereas a seven-cycle has a proper
three-colouring with class sizes `3,3,1`.  Hence there are exactly two
components, both full to the cycle. \(\square\)

The connector in outcome 1 is allowed to use both original shores.  It
therefore does not contradict rooted infeasibility on either one closed
shore.

## 5. What minimum-side descent can and cannot use

### Lemma 5.1 (exact two-cut descent criterion)

Adopt the minimum choice of `C` from Section 1.  Fix `gamma in Gamma`.
Suppose there is a nonempty connected set `L subsetneq C` and two distinct
vertices `u,v in V(P_gamma)` such that

\[
                         N_F(L)=\{u,v\},               \tag{5.1}
\]

and `phi_C(u)=phi_C(v)`.  Then this configuration is impossible.

#### Proof

The set `{u,v}` is an actual two-cut of `F`, and `L` is a component after
its deletion.  Moreover,

\[
                         N_G(L)=\{u,v\}\cup N_Z(L).
\]

Seven-connectivity forces `N_Z(L)=Z`.  Restricting `phi_C` to
`G[L union Z union {u,v}]` gives a permitted response in which `Z` is
monochromatic and `u,v` have one common different colour.  The
unconditional two-cut reduction makes `L` the equality-response component
for this new two-cut.  Since `|L|<|C|`, this contradicts the minimum choice
of `C`. \(\square\)

Because `P_gamma` alternates `beta,gamma`, the equal-colour condition in
Lemma 5.1 says exactly that `u,v` have the same parity along the path.  A
two-cut whose ends have opposite colours produces a distinct-response
component and is not a descent.  Likewise, Lemma 3.1 gives at least three
attachments for each individual residual component, so it does not by
itself produce the two-vertex boundary in (5.1).  A terminal descent must
therefore combine path intervals and residual components while proving
that no third attachment crosses the proposed interval.

## 6. Exact gain and remaining obstruction

The equal and distinct responses are now synchronized at their actual
distance-one boundary transition.  The result is stronger than merely
having four paths on one shore and an unrelated path on the other:

* one fixed equality-side colouring supplies all four `P_gamma`;
* one literal opposite-shore path `R` works for every colour coordinate;
* the resulting four cycles are induced and odd;
* full rooted infeasibility forces every residual component to miss a
  centre and attach to its path at least three times;
* any prescribed triple in such a component has a disjoint three-fan to
  the synchronized path; and
* a length-seven cycle either has a two-shore root connector or gives an
  exact two-component order-seven separation.

None of these conclusions is terminal.  A component with three or more
path attachments need not have a two-vertex neighbourhood in `F`, the
two-shore connector need not lie in either original closed shore, and the
order-seven cycle cut is not of the form `Z union {u,v}`.  Thus neither the
minimum choice of `C` nor the existing rooted-minor completion theorem can
be invoked without an additional interval-uncrossing or labelled
branch-set allocation theorem.

The next exact task is consequently:

> For the four paths `P_gamma` and their common opposite path `R`, either
> combine the three-or-more attachment sets into the prescribed rooted
> `K_6^-` model, or find a path interval whose closure has a same-colour
> two-vertex neighbourhood in `F`.

The first conclusion combines with the opposite full side to give the
forbidden `K_7^-` minor; the second is the strict equality-side descent in
Lemma 5.1.  The present note proves the synchronized input to that task,
not the task itself.

## Dependencies

- [five independent centres at a two-cut](../results/hc7_k7minus_five_centre_two_cut_reduction.md);
- [one opposite-shore Kempe transition](../results/hc7_opposite_shore_single_kempe_transition.md);
- [the exact two-shore incidence cycle](../results/hc7_two_shore_kempe_incidence_cycle.md); and
- [critical seven-cut capacity](../results/hc7_k7minus_critical_seven_cut_capacity.md).
