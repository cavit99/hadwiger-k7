# Seven exceptional degree-eight vertices: live technical frontier

**Status:** active conditional frontier.  The lower bound and the local
neighbourhood and exterior-completion reductions in Sections 1--2 are
written and separately audited GREEN.  The list-core calculation in Section
3 is a written live derivation without a separate audit.  The upper bound is
open.  This file is not a second status ledger.

## 1. Exact finishing target

Let `G` satisfy

\[
 \kappa(G)\ge7,
 \qquad \chi(G)=7,
 \qquad \text{every proper minor of `G` is six-colourable},
 \qquad K_7^-\npreccurlyeq G.                              \tag{H}
\]

Call a degree-eight vertex exceptional when its neighbourhood is
`K_4`-free.  The proved
[degree-defect theorem](../results/hc7_k7minus_seven_exceptional_vertices_corollary.md)
gives

\[
 b\ge15-n_7+\sum_{i\ge10}(i-9)n_i
  \ge7+\sum_{i\ge10}(i-9)n_i,                           \tag{1}
\]

where `b` is the number of exceptional vertices.  Therefore the theorem

> every graph satisfying (H) has at most six exceptional vertices

would prove that every `K_7^-`-minor-free graph is six-colourable.  It is a
headline-equivalent finishing theorem, not a routine intermediate lemma.

The equality `b=7` branch is already rigid: `n_7=8`, `n_8=9`, all other
vertices have degree nine, `2m=9n-25`, and the two literal `K_5`s are
disjoint copies with degree pattern `7^4 8^1`.  Parity gives odd order, and
private-triangle capacity gives `n\ge21` in this exact branch.

## 2. What the present attack proved

The new
[exceptional-neighbourhood and exterior-completion theorem](../results/hc7_k7minus_exceptional_neighbourhood_completion.md)
proves two facts.

1. Every exceptional vertex `u` has `alpha(G[N(u)])=3`.  Thus every one of
   the at least seven centres has an independent triple; the former
   independence-number-two branch is absent.
2. For an independent triple `I\subseteq N(u)` and
   `R=N(u)-I`, any `R`-rooted `K_5` model in `G-({u}\cup I)` that avoids an
   exterior component completes immediately to a `K_7^-` model.

The audited
[low-degree exterior-component theorem](../results/hc7_low_degree_exterior_component_bounds.md)
gives at most two components of `G-N[u]`.
Consequently every surviving rooted model is bilateral when there are two
components.  In the one-component case every residual connected subgraph
outside the rooted bags either has no neighbour in `I` or contacts at most
three of the five bags.

These are positive host-level reductions.  They do not yet coordinate six
or seven different centres.

## 3. Seven-root list reduction

**Status:** written live derivation; not separately audited or promoted to
`results/`.

Choose seven exceptional vertices and call their set `B`.  Six-colour
`G-B` with a colouring `phi`.  Put `H=G[B]`; the degree-defect theorem gives
that `H` is `K_5`-free.  For each `v\in B`, let

\[
 \begin{aligned}
 E_v&=N(v)-B,\\
 \rho(v)&=|E_v|-|\phi(E_v)|,\\
 L(v)&=[6]-\phi(E_v).
 \end{aligned}                                           \tag{2}
\]

Then `G[B]` is not `L`-colourable; otherwise the colouring extends to all
of `G`.  Since `|E_v|=8-d_H(v)`, the exact list identity is

\[
                         |L(v)|=d_H(v)+\rho(v)-2.         \tag{3}
\]

Let `C\subseteq B` be inclusion-minimal such that `G[C]` is not colourable
from the restricted lists.  It is connected, since otherwise minimality
colours each component separately.  Colouring `C-v` and then attempting to
extend at `v` also gives `d_{H[C]}(v)>=|L(v)|`.  For `v\in C`, define

\[
 c(v)=|N_H(v)-C|,
 \qquad
 \varepsilon(v)=d_{H[C]}(v)-|L(v)|.                     \tag{4}
\]

Minimality gives `\varepsilon(v)>=0`, and substitution in (3) gives the
exact budget

\[
                  \boxed{c(v)+\rho(v)+\varepsilon(v)=2}
                  \qquad(v\in C).                        \tag{5}
\]

Thus each core vertex has exactly two units divided among contacts with the
other exceptional vertices, repeated exterior colours, and list-degree
excess.  For the tight set

\[
                         T=\{v\in C:\varepsilon(v)=0\},
\]

the graph `H[T]` is a Gallai forest.  Indeed, after colouring outside a
block `Q`, each vertex of `Q` retains at least `d_Q(v)` colours.  The
Borodin--Erdos--Rubin--Taylor degree-choosability theorem forces `Q` to be a
complete graph or an odd cycle; `K_5`-freeness bounds the complete blocks by
`K_4`.  This is the same audited argument as Theorem 2.1(4) of
[`hc7_boundary_list_critical_transfer.md`](../results/hc7_boundary_list_critical_transfer.md).

It does not finish.  The explicit
[`C_7\vee C_6` mechanism barrier](../barriers/hc7_k7minus_seven_root_list_count_barrier.md)
has seven exceptional degree-eight vertices and is eight-connected.  One
colouring of the `C_6` produces empty lists and singleton cores; another
produces the tight odd-cycle core `C=B=C_7` with common list `\{1,2\}`.
The witness is only five-chromatic and is not a counterexample to (H), but
it shows that one static colouring state cannot close the theorem.

There is, however, genuine adaptive information.  For each `x\in B`, a
six-colouring of the proper minor `G-x` restricts to a colouring of `G-B`
for which `H-x` is list-colourable but `H` is not.  Consequently every
minimal core for that response contains `x`.  The seven anchored cores may
differ; synchronizing them is the exact multi-centre colouring target.

## 4. Exact remaining obstruction

The most concrete current gate is the following allocation statement.

> **Rooted shore-allocation target.** Among the at least seven exceptional
> centres, find `u`, an independent triple `I\subseteq N(u)`, and an
> `(N(u)-I)`-rooted `K_5` model such that either:
>
> 1. the model avoids one component of `G-N[u]`; or
> 2. a connected subgraph disjoint from the star and all five bags is
>    adjacent to the star and to at least four bags.

Either outcome gives an explicit `K_7^-` model.  With two exterior
components, a one-shore rooted model is terminal.  With one component, the
second residual-contact outcome is necessary: a model avoiding the whole
component would be confined to its five roots and would make them a literal
`K_5`, impossible at an exceptional centre.

The existing one-pair seven-path argument cannot supply this allocation;
its exact failure is recorded in the
[seven-path barrier](../barriers/hc7_k7minus_bad_pair_seven_paths_barrier.md).

## 5. Recommended next attack

Attack two complementary gates in this order.

1. **Two-component shore allocation.**  Its win condition is sharply bounded:
use the proper-minor colouring responses to construct one rooted `K_5`
model confined to either closed shore.  The current bilateral
`P_3\mathbin{\dot\cup}K_2` inputs are already audited in the
[two-independent-triples theorem](../results/hc7_degree8_two_independent_triples.md),
[polarized-response theorem](../results/hc7_degree8_p3k2_polarized_response.md),
and [concentrated-reserve elimination](../results/hc7_low_degree_concentrated_reserve_elimination.md).
What remains unproved is their shore-avoidance refinement.
2. **Anchored-core synchronization.**  Compare the seven list states coming
from `G-x`, not arbitrary static lists.  The first accepted outcome should
eliminate either saturated singleton cores or common-two-colour odd-cycle
cores by a Kempe swap or an explicit rooted minor.

If the shore lemma succeeds, isolate the one-component residual-contact
theorem.  Further enumeration of arbitrary degree-compatible lists is
blocked by the mechanism witness and should not be repeated.

Before that attack, split the two-component case by its actual attachment
type.  A nonfull exterior component misses exactly one boundary vertex `x`,
and `S=N(u)-\{x\}` is an order-seven cut.  If both exterior components miss
the same `x`, then `G-S` has the three components consisting of the two
exterior components and `\{u,x\}`; the audited
[critical seven-cut theorem](../results/hc7_k7minus_critical_seven_cut_capacity.md)
therefore gives `chi(G[S])=3` and colour-class sizes `3,2,2`.  If the misses
differ, or only one component is nonfull, the other component joins
`\{u,x\}` and this is the structured two-component cut case.  Only the case
in which both exterior components meet all eight neighbours belongs in the
two-full-shore `P_3\mathbin{\dot\cup}K_2` analysis.

An exploratory order-eight census suggests a useful second split: most
`K_4`-free, independence-three neighbourhood types appear to admit an
independent triple leaving at most six missing root adjacencies, within the
range of Kriesell--Mohr Theorem 7, while a small residue remains.  This is
not a promoted finite result and is not used above.  Before relying on exact
counts, retain an independent verifier and write the unbounded host
reduction explicitly.
