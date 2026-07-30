# Seven exceptional degree-eight vertices: live technical frontier

**Status:** active conditional frontier.  The lower bound and the local
neighbourhood, exterior-completion, and two-component reductions in Sections
1--2 are written and separately audited GREEN; the finite boundary claims
have retained independently checked verifiers.  The accompanying scoped
barriers are also separately audited GREEN.  The list-core calculation in
Section 3 is a written live derivation without a separate audit.  The upper
bound is open.  This file is not a second status ledger.

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

The focused two-component attack now goes substantially further.  Its
[nonfull-attachment theorem](../results/hc7_k7minus_nonfull_attachment_reduction.md)
proves that the two exterior components cannot miss the same neighbour of
`u`.  If exactly one component is nonfull, deleting its unique missed
neighbour from `X=N(u)` gives an order-seven cut with connected-subgraph
packing vector exactly `(1,2)`.  Its boundary has independence number
three, at most nine edges, connectivity at most three, no `K_5` minor, no
vertex deletion with a `K_4^-` minor, and no robust independent triple.
The audited uniform defect-two carrier theorem then forces the missed
vertex to have at most four neighbours on that boundary and at least two
neighbours entering the full exterior component.  A retained exact census
leaves 28 possible seven-vertex boundary types; all are three-chromatic, 25
have a clique odd-cycle transversal, and three do not.
If the two components have distinct misses, the two overlapping
order-seven cuts are connected-rich `(1,2)` cuts when the missed vertices
are adjacent; when they are nonadjacent, each cut is `(1,1)` or `(1,2)`
and their common six-vertex boundary satisfies the explicit `K_4` and
`K_4^-` minor exclusions in that theorem.

In the both-full case, the
[shore reduction](../results/hc7_k7minus_both_full_shore_reduction.md)
starts with all 2,076 exceptional order-eight neighbourhoods.  An
unbounded diamond-deletion lift leaves 15 boundary types; the audited
three-full-component theorem removes eight, leaving seven exact graph6
types.  Every surviving exterior component has `X`-full connected-subgraph
packing number one, so the full packing vector outside `X` is exactly
`(1,1,1)` for `\{u\},E,F`.  For the reserve types with six or seven
missing root adjacencies, every fixed star-contraction colouring still
supports at least two demands through each shore; concentration of all but
one demand in one shore would already give a rooted `K_5^-` and hence a
`K_7^-` model.

These results are strict positive reductions, not shore allocation.  The
[accompanying barriers](../barriers/hc7_k7minus_shore_allocation_barrier.md)
show that all 15 boundary types admit balanced abstract shore labels under
every independent-triple rotation, and that fullness plus minor exclusion
alone does not force a one-shore rooted model.  The latter witness is only
three-connected and four-chromatic, so it does not refute the critical-host
target; it identifies exactly where seven-connectivity and compatible
proper-minor colouring responses must enter.

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

In the both-full two-component cell, a third accepted outcome is an
`(N(u)-I)`-rooted `K_5^-` model confined to one closed shore; the unused
full component completes it to `K_7^-`.

Each accepted outcome gives an explicit `K_7^-` model.  With one exterior
component, the residual-contact outcome is necessary: a model avoiding the
whole component would be confined to its five roots and would make them a
literal `K_5`, impossible at an exceptional centre.

For two exterior components, the target is no longer an undifferentiated
allocation problem.  The nonfull theorem eliminates the common-miss case
and exposes only connected-rich `(1,2)` boundaries or a pair of overlapping
cuts with packing vector `(1,1)`.  In the both-full case, the boundary is
one of seven exact types and both exterior packing numbers are one.  On
that cell a shore-confined rooted `K_5^-`, rather than a full rooted `K_5`,
is already terminal.  These are the exact local obligations; none is
presently closed.

The existing one-pair seven-path argument cannot supply this allocation;
its exact failure is recorded in the
[seven-path barrier](../barriers/hc7_k7minus_bad_pair_seven_paths_barrier.md).

## 5. Recommended next attack

Attack the two normalized local gates in this order.

1. **Nonfull carrier extraction and overlapping-cut synchronization.**
   In the one-nonfull cell, the missed vertex has at most four boundary
   neighbours and at least two neighbours entering the full exterior
   component.  Use those entrances to split off a connected subgraph
   missing at most two boundary vertices while preserving a disjoint full
   packet; the audited defect-two carrier theorem would then six-colour the
   host.  For distinct nonadjacent misses, use the two overlapping `(1,1)`
   cuts simultaneously rather than reflecting either cut in isolation.
2. **Dynamic allocation on the seven both-full types.**  For the six- and
   seven-demand reserves, compare operation-related star-contraction
   colourings until one shore supports all but one demand, or extract a
   disjoint residual connected subgraph meeting the star and four rooted
   bags.  The two eight-demand types require a separate conversion beyond
   the six-demand Kriesell--Mohr theorem.  Any proof must use compatibility
   of actual responses or packet-one topology; the balanced-label barrier
   rules out static counting and independent-triple rotation alone.

In parallel, the multi-centre route should compare the seven list states
coming from `G-x`, not arbitrary static lists.  Its first accepted outcome
is a Kempe or explicit-minor exclusion of saturated singleton cores or
common-two-colour odd-cycle cores.  If the two-component gates close, the
remaining local problem is the one-component residual-contact theorem.
Further enumeration is useful only when attached to an unbounded host lift;
the relevant order-eight and order-seven boundary splits are now exact.
