# A minimum disconnected exceptional exterior and exact recentering

**Status:** active written unbounded proof;
[separate internal audit GREEN](hc7_k7minus_minimal_exterior_recentring_audit.md).
No new finite computation is used, but the deduction depends on audited inputs,
including the computer-assisted degree-eight exterior-component bound.
The results below do not prove that exceptional anti-neighbourhoods are
connected or settle the `K_7^-` six-colour conjecture.  They identify the
only way in which a second degree-eight centre inside a minimum exterior
component can itself have disconnected anti-neighbourhood.

Throughout, let `G` satisfy

\[
 \kappa(G)\ge7,
 \qquad \chi(G)=7,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G,
 \qquad K_7^-\npreccurlyeq G.                         \tag{H}
\]

Suppose some exceptional degree-eight vertex has disconnected
anti-neighbourhood.  Choose an exceptional degree-eight vertex `u` and a
component `E` of `G-N[u]` so that

\[
 |E|=\min\{|C|: C\text{ is a component of }G-N[z],
 \ z\text{ is exceptional of degree eight, and }G-N[z]
 \text{ is disconnected}\}.                         \tag{1}
\]

Put `X=N(u)`.  The proved low-degree exterior-component theorem gives

\[
                         G-N[u]=E\mathbin{\dot\cup}F  \tag{2}
\]

for one other component `F`.

## 1. Global consequences and nonsingleton shores

The proved two-component literal-clique exclusion applies at `u`.  Hence

\[
 \begin{gathered}
  G\text{ has no literal }K_5,
  \qquad \delta(G)\ge8,
  \qquad |E(G)|\ge4|V(G)|,\\
  n_8\ge25+\tau,
  \qquad \tau=\sum_{i\ge10}(i-9)n_i.                 \tag{3}
 \end{gathered}
\]

In particular every degree-eight vertex is exceptional.

### Lemma 1 (both exterior components are nonsingleton)

One has `|E|,|F|>=2`.

#### Proof

Suppose, for example, that `E={e}`.  Every neighbour of `e` belongs to
the eight-set `X`.  Minimum degree eight therefore gives

\[
                             N(e)=X.                  \tag{4}
\]

Take a six-colouring of the proper minor `G-u`.  The colour on `e` is
absent from `X=N(e)`.  Assigning that same colour to the nonadjacent
vertex `u` gives a six-colouring of `G`, contrary to (H).  The argument
for `F` is identical. \(\square\)

## 2. The minimum-component theorem

### Theorem 2 (minimum-shore rotation)

Let `v` be a degree-eight vertex in `E`.  Then exactly one of the following
holds.

1. `G-N[v]` is connected.
2. There are vertices `y\in X` and `w\in E` such that

   \[
    N_X(v)=X-\{y\},
    \qquad N_E(v)=\{w\},
    \qquad N_X(F)=X-\{y\},                            \tag{5}
   \]

   and `G-N[v]` has exactly the two components

   \[
        F,
        \qquad
        E'=(E-\{v,w\})\cup\{u,y\}.                   \tag{6}
   \]

   The second displayed set induces a connected graph and

   \[
                              |E'|=|E|.                \tag{7}
   \]

#### Proof

Because `E` is connected and nonsingleton, `v` has a neighbour in `E`.
All neighbours of `v` outside `E` belong to `X`; there are no edges from
`E` to `F\cup\{u\}`.  Consequently

\[
  |N_X(v)|\le7,
  \qquad Y:=X-N(v)\ne\varnothing.                    \tag{8}
\]

In `G-N[v]`, the vertex `u` and every vertex of `Y` survive, and the
edges from `u` to `Y` put them in one component, call it `K`.

Suppose first that `F` has a neighbour in `Y`.  Since `F` is connected
and every one of its vertices survives, all of `F` lies in `K`.  Every
component of `G-N[v]` other than `K` is therefore contained in

\[
                         E-(\{v\}\cup N_E(v)).        \tag{9}
\]

Such a component has order at most `|E|-2`, because `v` has an
`E`-neighbour.  If it existed, it would contradict the minimum choice
(1), since `v` is itself exceptional of degree eight.  Thus `G-N[v]` is
connected in this case.

It remains that `F` has no neighbour in `Y`.  Seven-connectivity gives
`|N_X(F)|>=7`, while

\[
                         N_X(F)\subseteq X-Y=N_X(v).  \tag{10}
\]

Together with (8), this forces equality throughout:

\[
 |N_X(v)|=|N_X(F)|=7,
 \qquad Y=\{y\},
 \qquad N_X(v)=N_X(F)=X-\{y\}.                       \tag{11}
\]

The degree equation at `v` now gives `N_E(v)={w}` for one vertex `w`.
All neighbours of `F` are deleted in `G-N[v]`, so `F` is one component.
The set `{u,y}` is connected and lies in a second component.  The proved
degree-eight exterior-component theorem allows at most two components of
`G-N[v]`.  Every surviving vertex of `E-\{v,w\}` is anticomplete to `F`
and hence belongs to the component containing `{u,y}`.  This proves (6)
and its connectedness.  Finally,

\[
                |E'|=(|E|-2)+2=|E|,
\]

which proves (7). \(\square\)

### Corollary 3 (one common exact `(1,2)` seven-cut)

Outcome 2 of Theorem 2 has the following additional structure.  Put

\[
                              S=X-\{y\}.               \tag{12}
\]

Then `S` is an order-seven cut, `G-S` has exactly two components

\[
                         F,
              \qquad E\cup\{u,y\},                   \tag{13}
\]

and their maximum numbers of pairwise disjoint connected `S`-full
subgraphs are respectively one and two.  The rich component contains the
two `S`-full singleton subgraphs `{u}` and `{v}`.

Moreover, relative to the centre `v`, the component `F` misses the unique
neighbour `w\in N(v)`, while the other component `E'` from (6) is full to
`N(v)=S\cup\{w\}`.  Thus the same graph has a second one-nonfull
description at `v`, with the minimum component order unchanged.

#### Proof

Equation (11) says that `F` has neighbourhood exactly `S`, so `S` is a
cut.  The two exterior components `E,F` at `u` cannot miss the same
neighbour of `u`, by the proved same-miss exclusion.  Hence `E` has a
neighbour at `y`.  Since `E` is connected and `uy` is an edge, (13) is
the exact component decomposition of `G-S`.

The connected subgraphs `F`, `{u}`, and `{v}` are pairwise disjoint and
each is adjacent to every vertex of `S`.  Hence their total `S`-full
packing number is at least three.  The critical seven-cut capacity theorem
bounds it above by three.  Thus the packing number of `F` is one and that
of the other component is two.

Finally, `F` is anticomplete to `w\in E`, so it misses `w` relative to
`N(v)=S\cup\{w\}`.  The set `E'` contains `u`, so it is adjacent to every
vertex of `S`.  If `E'` also missed `w`, the two exterior components at
`v` would have the same missed neighbour, again contradicting the same-miss
exclusion.  Therefore `E'` has an edge to `w` and is full to
`N(v)=S\cup\{w\}`. \(\square\)

### Corollary 4 (at most one recentering vertex)

At most one degree-eight vertex of `E` satisfies outcome 2 of Theorem 2.
Consequently all but at most one degree-eight vertex in the minimum
component `E` have connected anti-neighbourhood.

#### Proof

If two distinct vertices `v,v'\in E` satisfied outcome 2, their missed
vertices would be equal: in each case that vertex is the unique member of
`X-N_X(F)`.  Thus both singleton subgraphs `{v}` and `{v'}` would be
`S`-full for the same cut `S=N_X(F)`.  Together with `{u}` and `F`, they
would give four pairwise disjoint connected `S`-full subgraphs, contrary
to the critical seven-cut capacity bound of three. \(\square\)

## 3. The exact proper-minor responses at the recentered pair

Retain outcome 2, and write

\[
                         J=G-\{u,v\}.                  \tag{14}
\]

The vertices `u,v` are nonadjacent and have the common seven-neighbour
set `S`; their remaining neighbours are respectively `y,w`:

\[
                         N(u)=S\cup\{y\},
               \qquad N(v)=S\cup\{w\}.               \tag{15}
\]

### Lemma 5 (the two vertex-deletion boundary responses)

Every six-colouring `c_u` of `G-u` satisfies

\[
 c_u(v)=c_u(y),
 \qquad c_u(S)\text{ uses exactly the other five colours}.     \tag{16}
\]

Symmetrically, every six-colouring `c_v` of `G-v` satisfies

\[
 c_v(u)=c_v(w),
 \qquad c_v(S)\text{ uses exactly the other five colours}.     \tag{17}
\]

#### Proof

The two-singleton common-host theorem applies to the nonadjacent vertices
`u,v`.  In the restriction of `c_u` to `J`, the retained vertex `v` is not
colour-dominating: its own colour is absent from
`N_J(v)=S\cup\{w\}`.  Therefore `u` is colour-dominating in that
restriction.

Put `alpha=c_u(v)`.  Properness makes `alpha` absent from `S`.  On the
other hand `u` sees all six colours on `N_J(u)=S\cup\{y\}`.  It follows
that `S` uses the other five colours and that `c_u(y)=alpha`, proving
(16).  Interchanging `u,v` proves (17). \(\square\)

Thus the sole minimum-component recentering residue already carries two
operation-specific five-colour boundary responses, with the two private
equalities oriented in opposite directions.  The missing step is to
synchronize those two partitions through the connected graph

\[
                       G[E-\{v\}\cup\{y\}],           \tag{18}
\]

which is connected because `v` is a leaf of `G[E]` and `y` has an
`E`-neighbour distinct from `v`.  The remaining task is to turn their first
incompatible Kempe transition into an explicit
`K_7^-` model or a strict smaller actual separation.  Neither conclusion
follows from Lemma 5 alone.

The two responses can nevertheless be placed in one common proper minor,
and all of its unavoidable bichromatic paths can be localized on the same
middle subgraph.

### Lemma 6 (common two-edge response and localized locks)

Let

\[
 e=uy,\qquad f=vw,\qquad H=G-\{e,f\},
 \qquad C=G[(E-\{v\})\cup\{y\}].                     \tag{19}
\]

Then `C` is connected and `chi(H)=6`.  In generally different proper
six-colourings of the same graph `H`, all three possible edge-equality
patterns occur: both `e,f` are
monochromatic, only `e` is monochromatic, and only `f` is monochromatic.
No proper six-colouring makes both edges bichromatic.

More precisely:

1. every six-colouring of `G-e` has
   `c(u)=c(v)=c(y)`, while `c(w)` is different and `S` uses exactly the
   other five colours;
2. every six-colouring of `G-f` has
   `c(u)=c(v)=c(w)`, while `c(y)` is different and `S` uses exactly the
   other five colours;
3. in every six-colouring `kappa` of `H` obtained by expanding a
   six-colouring of `G/e/f`,

   \[
        \kappa(u)=\kappa(y)=\kappa(v)=\kappa(w)=i,    \tag{20}
   \]

   the set `S` uses exactly the five colours different from `i`, and
   `yw` is a nonedge of `G`.

For each colour `j` different from `i`, at least one of the following
literal paths exists in `H`:

\[
  \begin{array}{ll}
   \text{an }i\text{-}j\text{ path from }u\text{ to }y,
      &\text{or}\quad
   \text{an }i\text{-}j\text{ path from }v\text{ to }w.
  \end{array}                                         \tag{21}
\]

One fixed pair, `uy` or `vw`, has such paths for at least three of the five
colours.  Each `u-y` path in (21) contains a subpath from a `j`-coloured
vertex of `S` to `y` whose open interior lies in `C`; each `v-w` path has
the analogous subpath ending at `w` with open interior in `C`.

#### Proof

The vertex `v` is a leaf of the connected graph `G[E]`, so `E-v` is
connected.  The component `E` has a neighbour at `y`, while `vy` is absent
by (15); hence `y` has a neighbour in `E-v` and `C` is connected.

The graph `H` is a proper minor and is therefore six-colourable.  If it
were five-colourable, recolour the nonadjacent vertices `u,v` with a fresh
sixth colour and restore `e,f`.  This would six-colour `G`, so
`chi(H)=6`.

The common-host double-contraction theorem, applied to the disjoint edges
`e,f`, gives the three asserted equality patterns and excludes the pattern
in which both are bichromatic.  Consider a six-colouring of `G-e`.  Its
restriction to `G-u` satisfies Lemma 5, so `v` and `y` have one colour and
`S` uses the other five.  The missing edge `e` must be monochromatic,
because otherwise it could be restored; hence `u,v,y` have one colour.
The retained edge `f` makes the colour of `w` different.  This proves
clause 1, and clause 2 is symmetric.

Now let `kappa` be a double-contraction colouring.  In `H` one has

\[
                         N_H(u)=N_H(v)=S,
                         \qquad uv\notin E(G).          \tag{22}
\]

Write

\[
 \kappa(u)=\kappa(y)=a,
 \qquad \kappa(v)=\kappa(w)=b.                       \tag{23}
\]

Both `u` and `v` are adjacent to every vertex of `S`, so `S` uses neither
`a` nor `b`.  If `a` and `b` were different, recolouring `u` with `b` and
`v` with `a` would remain proper in `H` and would make both deleted edges
bichromatic.  Restoring them would six-colour `G`.  Thus `a=b=i`, proving
(20).  Properness then shows that `yw` is absent.  If some colour different
from `i` were absent from `S`, recolouring both nonadjacent vertices `u,v`
with that colour and restoring `e,f` would again six-colour `G`.  Therefore
`S` uses all five other colours.

The same-colour lock-allocation theorem now says that, for every alternate
colour `j`, at least one of `uy,vw` is locked in the `i-j` subgraph of `H`.
It also assigns at least three of the five locks to one fixed pair.  This
proves (21).

It remains to localize a lock.  The graph `H-S` has exactly the four
components

\[
                         F,\quad \{u\},\quad \{v\},\quad C.     \tag{24}
\]

Indeed, deleting `e` and `f` isolates `u` and `v` from the old rich side,
and the preceding paragraph proves that the remainder `C` is connected.
Choose a shortest locked `u-y` path and let `s` be its last vertex in `S`
before `y`.  Since `S` contains no vertex of colour `i`, the vertex `s`
has colour `j`.  The subpath from `s` to `y` has no internal vertex in `S`;
by (24), its open interior lies in `C`.  The argument for a locked `v-w`
path is identical. \(\square\)

The one-restoration part of the same common-host theorem supplies two
further, generally different, colourings of `H`.  Restricting any
six-colouring of `G-e` to `H` leaves at least four alternate-colour locks
on `uy`; restricting any six-colouring of `G-f` leaves at least four on
`vw`.  Each surviving lock has a last-`S` subpath with open interior in
`C`, by the argument using (24).  These two four-lock systems need not use
the same palette or the same colouring of `H`.

Lemma 6 is the exact gain obtainable from the existing common-host
machinery: all three proper-minor responses now live in one graph, and
every alternate boundary colour has a literal connector into the same
connected subgraph `C`.  The first unavailable implication is a
**set-rooted absorption step**: from these five colour-indexed connectors,
one must either construct five pairwise disjoint, pairwise adjacent
connected branch sets, each meeting `S` and avoiding `u,v`, or return an
operation-preserving order-seven separation with open side properly inside
`C`.  The first outcome, together with the singleton branch sets `{u}` and
`{v}`, is an explicit `K_7^-`-minor model.  Existing lock allocation does
not imply it, because connectors for different colours may share
`i`-coloured vertices.  Existing seven-cut capacity does not imply the
second outcome, because it controls disjoint `S`-full connected subgraphs,
not these one-ended connectors.  To contradict the minimum choice (1), a
returned separation would additionally have to identify its smaller side
as an actual anti-neighbourhood component of an exceptional degree-eight
vertex; an abstract smaller separator side is insufficient.

### Corollary 7 (exact order-seven or order-eight two-shore interface)

Put

\[
                         T=N_S(C),
                         \qquad B=T\cup\{u,v\}.         \tag{25}
\]

Then

\[
                         5\le |T|\le6.                 \tag{26}
\]

Moreover, `B` is a vertex cut of order seven or eight, and `G-B` has
exactly the two components

\[
                         C,
                 \qquad D=F\cup(S-T).                 \tag{27}
\]

Both components are adjacent to every vertex of `B`.  The boundary graph
has the exact form

\[
                         G[B]=\overline{K_2}\vee G[T], \tag{28}
\]

where the independent pair is `\{u,v\}`, and

\[
                         \Delta(G[T])\le1.             \tag{29}
\]

If `|T|=5`, the maximum numbers of pairwise disjoint connected `B`-full
subgraphs in `C` and `D` are exactly one and one.

#### Proof

For each of the five colours `j` different from `i`, Lemma 6 supplies a
subpath from a `j`-coloured vertex of `S` into `C`.  These five initial
vertices are distinct, so `|T|>=5`.  If `T=S`, then

\[
                         F,\quad \{u\},\quad \{v\},\quad C
\]

would be four pairwise disjoint connected subgraphs adjacent to every
vertex of the order-seven cut `S`, contrary to the critical seven-cut
capacity bound.  Hence `|T|<=6`, proving (26).

The only neighbours of `C=(E-\{v\})\cup\{y\}` outside `C` are its
neighbours in `T`, the edge `uy`, and the edge `vw`.  Thus

\[
                         N_G(C)=B.                     \tag{30}
\]

Since `S-T` is nonempty and `F` is adjacent to every vertex of `S`, the
set `D` in (27) is connected.  There are no edges from `C` to `D`, and
together they contain every vertex outside `B`; hence they are the two
components of `G-B`.  The component `C` is full to `B` by the definition
of `T` and the two private edges.  The component `D` is full to `T`
through `F` and to `u,v` through any vertex of `S-T`.  This also proves
(28).

Suppose that `G[T]` contains a path `a-b-c`.  Choose distinct
`p,q\in T-\{a,b,c\}`, which is possible by (26).  The seven sets

\[
 C\cup\{p\},\quad D,\quad \{u,q\},\quad \{v\},
                   \quad \{a\},\quad \{b\},\quad \{c\}             \tag{31}
\]

are disjoint and connected.  The first four are pairwise adjacent and
each is adjacent to the last three; among the last three only the
`a`--`c` adjacency may be absent.  Thus (31) is a `K_7^-`-minor model,
contrary to (H).  This proves (29).

Finally suppose `|T|=5`.  Every connected `B`-full subgraph of `C` must
contain `y`, the only neighbour of `u` in `C`, and `w`, the only neighbour
of `v` in `C`.  Hence the full-subgraph packing number of `C` is one.  If
the corresponding number for `D` were at least two, the total capacity at
the order-seven cut `B` would be three.  The seven-boundary capacity theorem
would then give `|E(G[B])|<=9`.  But `u` and `v` already contribute the
ten distinct edges joining them to the five vertices of `T`, a
contradiction.  The packing number in `D` is therefore also one. \(\square\)

When `|T|=6`, Corollary 7 is a boundary-full order-eight separation.  The
audited operation-coupled order-eight theorem applies to either private
edge and returns a clean five-path response or an actual order-seven
response side inside `C`.  That alternative is not terminal: the returned
side need not be an anti-neighbourhood component of an exceptional vertex,
so it does not contradict the minimum choice (1).  When `|T|=5`, the exact
packing vector `(1,1)` likewise does not synchronize the two proper-minor
boundary colourings.  Thus Corollary 7 is a strict unbounded reduction of
the rotation residue, not its elimination.

## 4. What the global count adds

### Corollary 8 (an independent four-set of degree-eight centres)

At least sixteen degree-eight vertices lie in `E\cup F`.  Among them are
three pairwise nonadjacent vertices.  Together with `u`, they form an
independent four-set of exceptional degree-eight vertices.

#### Proof

The closed neighbourhood `N[u]` has nine vertices.  Equation (3) therefore
puts at least

\[
                             25-9=16                  \tag{32}
\]

degree-eight vertices in `E\cup F`.  The graph induced by those vertices
contains no `K_5`, because `G` contains no literal `K_5`.  The standard
Ramsey equality `R(5,3)=14` therefore supplies an independent three-set.
Every exterior vertex is nonadjacent to `u`, so adjoining `u` gives the
claimed independent four-set. \(\square\)

The independent set supplies several legitimate pairs to which the
two-singleton common-host theorem and the proper vertex-deletion responses
apply.  It does not force any of the three exterior centres to have
disconnected anti-neighbourhood, nor does it align their spanning minor
models or boundary colour partitions.  Hence the count does not by itself
eliminate the original disconnected centre.

## 5. Exact scope

Theorem 2 and Corollaries 4 and 7 form an unbounded minimum-component
result.  They show that the global `25+tau` branch cannot contain
uncontrolled repeated minimum-shore failures: within a selected minimum
component, every degree-eight centre except possibly one has connected
anti-neighbourhood,
and the exception is the exact two-centre configuration of Corollary 3 and
Lemmas 5--6.  Corollary 7 further reduces that exception to a full
two-shore separation of order seven or eight whose remaining boundary
graph is a matching plus isolated vertices.

This is not exceptional-centre connectivity.  A hypothetical host may
still have one disconnected centre while its many other degree-eight
centres have connected anti-neighbourhoods, and the current count theorem
does not contradict that possibility.

## Inputs

- [two-component literal-clique exclusion and density jump](../results/hc7_k7minus_one_nonfull_k5_and_nested_cut.md)
- [degree-eight exterior-component bound](../results/hc7_low_degree_exterior_component_bounds.md)
- [same-miss exclusion](../results/hc7_k7minus_nonfull_attachment_reduction.md)
- [critical seven-cut capacity](../results/hc7_k7minus_critical_seven_cut_capacity.md)
- [two nonadjacent singleton roots over a common host](../results/hc7_two_singleton_common_host.md)
- [common-host double-contraction lock allocation](../results/hc7_common_host_double_contraction_lock_allocation.md)
- [operation-coupled order-eight response](../results/hc7_operation_coupled_order8_response.md)
- the standard Ramsey equality `R(5,3)=14`
