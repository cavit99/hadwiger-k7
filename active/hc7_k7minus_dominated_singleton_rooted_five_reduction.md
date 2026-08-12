# The dominated singleton produces a saturated five-root obstruction

**Status:** written proof and recorded route nonclosure;
[separate internal audit GREEN](hc7_k7minus_dominated_singleton_rooted_five_reduction_audit.md).
This is a conditional reduction inside the eight-coordinate campaign.  It
does not prove the `K_7^-` six-colour conjecture or `HC_7`.

The dominated-singleton state admits a direct formulation which does not
refer to the fixed exact `K_7^\vee` model.  Deleting the common colour class
of the operated edge leaves a five-chromatic graph and a set which uses all
five colours in every five-colouring.  A `K_5` model rooted at that set would
give a `K_7` model immediately.  Thus a target-free dominated singleton is
a restricted obstruction to the still-open order-five case of Holroyd's
rooted Hadwiger conjecture.

This identifies the exact limit of the direct five-connectivity,
Kelmans--Seymour and universal five-terminal arguments.  They supply an
unrooted `K_5` model or a rooted triangulated pentagon, but not the required
five branch sets meeting the common-neighbour set.

## 1. Setting

Let `G` be seven-connected and seven-chromatic, and suppose every proper
minor of `G` is six-colourable.  Let `uv` be an edge, and let `c` be a
proper six-colouring of `G-uv` with

\[
                              c(u)=c(v)=0.              \tag{1.1}
\]

Assume that `v` is adjacent to every member of

\[
                         Q=N_G(u)-\{v\}.                \tag{1.2}
\]

In the dominated-singleton application, `|Q|>=7`, the graph `G[Q]` is
triangle-free and has no `K_5^-` minor.

Put

\[
 \Gamma=c^{-1}(0),\qquad K=G-\Gamma,\qquad H=G-\{u,v\}. \tag{1.3}
\]

The edge `uv` is the only edge of `G` with both ends in `Gamma`.
In particular,

\[
                 K=H-(\Gamma-\{u,v\}),                 \tag{1.4}
\]

so `K` is exactly the common-colour-free induced subgraph of `H`.

## 2. The exact five-colour obstruction

### Theorem 2.1 (saturated common-neighbour set)

In the setting above:

1. `chi(K)=5`;
2. every proper five-colouring of `K` uses all five colours on `Q`;
3. if `K` has a `K_5`-minor model every branch set of which meets `Q`, then
   `G` has a `K_7` minor; and
4. if `H` has a `K_5^-`-minor model every branch set of which meets `Q`,
   then `G` has a `K_7^-` minor.

Consequently, if `G` has no `K_7^-` minor, then `(K,Q)` is a
five-chromatic instance in which `Q` uses every colour in every
five-colouring but no `K_5` model has all five branch sets meeting `Q`.

#### Proof

The restriction of `c` to `K` uses at most five colours.  If `K` were
four-colourable, use four colours on `K`, one fresh colour on
`Gamma-\{u\}`, and a sixth fresh colour on `u`.  The set
`Gamma-\{u\}` is independent, and its only possible conflict with `u` in
the original graph is `uv`; that edge now has differently coloured ends.
This would six-colour `G`, a contradiction.  Hence `chi(K)=5`.

Every vertex of `Q` lies in `K`, since it is adjacent to `u` and therefore
does not have colour `0` in (1.1).  Suppose that a proper five-colouring
of `K` omits one colour on `Q`.  Give `u` that omitted colour and give all
of `Gamma-\{u\}` one fresh sixth colour.  This is proper: `u` has no
neighbour in `K-Q`, the edge `uv` has differently coloured ends, and
`Gamma-\{u\}` is independent and anticomplete to `u` apart from `v`.
Again this would six-colour `G`.  Thus every five-colouring of `K` uses
all five colours on `Q`.

Let `B_1,...,B_5` be pairwise disjoint connected pairwise adjacent branch
sets, each meeting `Q`.  Both `u` and `v` are adjacent to every `B_i`, and
`uv` is an edge.  Therefore

\[
                         \{u\},\{v\},B_1,\ldots,B_5    \tag{2.1}
\]

are seven pairwise adjacent connected branch sets.  This proves item 3.
The same construction applied to a `K_5^-` model has exactly its one
allowed missing adjacency among `B_1,...,B_5`, proving item 4. `\square`

### Corollary 2.2 (the direct capstone is a rooted-model theorem)

The dominated-singleton case is eliminated by either of the following
statements.

1. The order-five case of Holroyd's conjecture: if a set uses all five
   colours in every five-colouring of a five-chromatic graph, then the
   graph has a `K_5` model every branch set of which meets the set.
2. The narrower ambient statement: in the present host, `H` has a
   `K_5^-` model every branch set of which meets `Q`.

The second statement is strictly the smaller conclusion needed here.  It
may use five-connectivity of `H`, the triangle-free `K_5^-`-minor-free
structure of `G[Q]`, the second edge response and the fixed exact model.

#### Proof

Apply Theorem 2.1(3) or (4), respectively. `\square`

## 3. What the direct global inputs do and do not supply

### Proposition 3.1 (five-connected nonplanar remainder)

The graph `H` is five-connected, has chromatic number at least five, and is
nonplanar.  It therefore contains both a subdivision of `K_5` and a
dominating `K_5` model.  In a `K_7^-`-minor-free host, every such `K_5`
model has a branch set disjoint from `Q`.

#### Proof

Deleting two vertices from a seven-connected graph leaves a
five-connected graph.  A four-colouring of `H`, followed by two fresh
colours on the adjacent vertices `u,v`, would six-colour `G`; hence
`chi(H)>=5`.  The Four-Colour Theorem makes `H` nonplanar.

The Kelmans--Seymour theorem supplies a subdivision of `K_5`; alternatively,
the Dominating 4-Colour Theorem supplies a dominating `K_5` model from
`chi(H)>=5`.  If all five branch sets of either model met `Q`, (2.1) would
be a `K_7` model. `\square`

This is the exact failure of the unrooted approach.  Neither theorem
prescribes even one `Q`-vertex in each branch set.  Five-connectivity gives
disjoint set-to-set paths, but an arbitrary linkage into a selected
subdivision may meet its subdivided edges before reaching the five branch
vertices.  Turning those first contacts into five distinct rooted branch
sets is an additional rooted-minor theorem, not a consequence of Menger's
theorem or Kelmans--Seymour.

### Proposition 3.2 (the universal five-terminal model is two edges short)

Choose any five vertices of `Q`.  Since `H` is three-connected, the audited
universal five-terminal theorem gives a model rooted at them whose quotient
contains

\[
                              F_5=K_1\vee P_4.          \tag{3.1}
\]

Adding the singleton bags `{u},{v}` guarantees the quotient subgraph
`K_2\vee F_5`.  The graph `F_5` has seven edges, whereas `K_5^-` has nine.
Thus the guaranteed model is two branch-set adjacencies short of a
`K_7^-` model.  Extra adjacencies in the actual quotient may close that
gap; the universal five-terminal theorem itself does not supply them.

#### Proof

Only the edge count needs verification: the hub of `F_5` contributes four
edges and the path contributes three.  The two universal singleton bags
already have every required adjacency, so the remaining deficit is exactly
the two edges separating `F_5` from a nine-edge `K_5^-`. `\square`

Likewise, applying the rooted `K_4` theorem in the five-connected
nonplanar graph `H` to four vertices of `Q` gives only six branch sets after
adjoining `u,v`.  A fifth vertex of `Q` is not guaranteed to avoid the
rooted model or to meet four of its bags.  This is the same missing rooted
allocation in a different form.

## 4. Exact nonclosure and smallest repair

The direct route has therefore reached a precise boundary:

\[
 \boxed{
 \begin{gathered}
  K\text{ is five-chromatic};\\
  Q\text{ uses all five colours in every five-colouring of }K;\\
  H\text{ is five-connected and nonplanar};\\
  \text{every unrooted }K_5\text{ model misses }Q\text{ in some bag}.
 \end{gathered}}
                                                               \tag{4.1}
\]

The existing double-saturation counterexample does not refute the live
statement: it is only six-colourable at the ambient level, is not
seven-connected or contraction-critical, and its two root sets are not the
present common-neighbour set with the dominated inclusion.  Conversely,
proving the generic implication from the first two lines of (4.1) would
settle the still-open order-five case of Holroyd's conjecture.  The project
should not silently assume that theorem.

The smallest direct repair is therefore:

> **Dominated common-neighbour rooted-model theorem.**  In the full aligned
> dominated-singleton state, `H` contains a `K_5^-` model all five of whose
> branch sets meet `Q`, or one boundary partition extends through both
> original sides.

The first outcome is terminal by Theorem 2.1(4); the second six-colours
`G`.  A proof must use information absent from a generic saturated-set
instance: the fixed exact `K_7^\vee` model, the exclusive two-edge response,
or the actual response component.  This is a global alternative to the
component-to-bag capture theorem, not a consequence of unrooted
five-connectivity alone.

## Dependencies and scope

- the audited
  [dominated-singleton localisation](../results/hc7_k7minus_singleton_coordinate_localisation.md)
  and
  [all-degree alignment](../results/hc7_k7minus_dominated_singleton_low_degree_terminal.md);
- the audited
  [universal five-terminal rooted-`F_5` theorem](../results/hc7_five_terminal_rooted_fan.md);
- Kelmans--Seymour for five-connected nonplanar graphs;
- the Dominating 4-Colour Theorem; and
- Holroyd's rooted Hadwiger conjecture, used only to identify the scope of
  the missing generic implication, not as a proved input.
