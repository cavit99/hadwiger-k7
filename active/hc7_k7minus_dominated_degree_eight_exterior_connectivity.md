# Exterior connectivity at a dominated degree-eight centre

**Status:** active written host reduction with one computer-assisted finite
lemma; internal self-audit adjacent.  This is a conditional theorem in the
eight-coordinate campaign.  It does not prove the `K_7^-` six-colour
conjecture or `HC_7`.

The dominated alternative at a terminal degree-eight centre has only one
exterior component.  Two components already complete the forbidden minor,
uniformly over all nine possible common-neighbour graphs and all 729
attachment profiles.

## 1. Finite quotient lemma

### Lemma 1.1 (two contracted exterior components)

Let `Q` be a graph of order seven satisfying

\[
 \alpha(Q)\leq3,\qquad Q\text{ is triangle-free},\qquad
 K_5^-\npreccurlyeq Q,                                \tag{1.1}
\]

and suppose that `Q` has a vertex cut of order at most two.  Add adjacent
vertices `u,v`, each complete to `Q`.  Add two further vertices `c_1,c_2`
such that

\[
 c_1c_2,uc_1,uc_2\notin E,
 \qquad
 |N(c_i)\cap(\{v\}\cup V(Q))|\geq7\quad(i=1,2).       \tag{1.2}
\]

Then the resulting graph contains a `K_7^-` minor.

#### Computer-assisted proof

The deterministic verifier
[`verify.py`](experiments/dominated_singleton_two_exterior_completion/verify.py)
enumerates every unlabelled triangle-free graph of order seven using
`geng -t`.  It independently checks the independence bound, excludes a
`K_5^-` minor by exact deletion and contraction, and retains only graphs
with a cut of order at most two.  Exactly nine graphs remain.

For each graph, each of `c_1,c_2` independently misses either no vertex or
one of the eight vertices in `\{v\} union V(Q)`.  The verifier checks all

\[
                              9\cdot9^2=729           \tag{1.3}
\]

attachment profiles.  The same exact minor routine finds a `K_7^-` minor
in every one.  Assertions enforce the graph count, profile count and every
minor conclusion before the script prints

```text
GREEN dominated degree-eight singleton two-exterior completion eligible_Q=9 profiles=729 one_component_survivors=46 survivor_graphs=6 live_profile_survivors=10 live_graphs=5
```

The adjacent experiment README records the reproduction command and finite
trust boundary. `\square`

## 2. Host lift

### Theorem 2.1 (dominated degree-eight exterior connectivity)

Let `G` be seven-connected and suppose that `K_7^-` is not a minor of
`G`.  Let `u` have degree eight and let `v in N_G(u)` dominate

\[
                              Q=N_G(u)-\{v\}.          \tag{2.1}
\]

Assume that

\[
 \alpha(G[Q])\leq3,\qquad G[Q]\text{ is triangle-free},\qquad
 K_5^-\npreccurlyeq G[Q],                             \tag{2.2}
\]

and that `G[Q]` has a vertex cut of order at most two.  If
`G-N_G[u]` is nonempty, then it is connected.

#### Proof

Suppose that `G-N_G[u]` has two distinct components `C_1,C_2`.  For each
`i`, its full neighbourhood is contained in `N_G(u)=\{v\} union Q` and
separates `C_i` from `u`.  Seven-connectivity gives

\[
        |N_G(C_i)|\geq7.                              \tag{2.3}
\]

Contract each connected component `C_i` to one vertex `c_i`, delete every
other vertex outside `N_G[u]`, and suppress parallel edges.  The two
component vertices are nonadjacent to one another and to `u`; each has at
least seven neighbours in `\{v\} union Q`.  The vertices `u,v` are
adjacent and complete to `Q` by the definition of `Q` and the domination
hypothesis.  Lemma 1.1 therefore gives a `K_7^-` minor in this quotient,
and hence in `G`, a contradiction.  Thus there is at most one exterior
component.  Nonemptiness makes it connected. `\square`

### Corollary 2.2 (the live dominated centre has one exterior component)

In the dominated alternative of the centre-singleton theorem, when the
terminal centre has degree eight, all hypotheses of Theorem 2.1 hold.
Consequently

\[
                         G-N_G[u]\text{ is connected}.             \tag{2.4}
\]

#### Proof

The dominated-singleton reduction gives that `G[Q]` is triangle-free and
has no `K_5^-` minor.  Exceptionalness and the degree-eight neighbourhood
theorem give `alpha(G[N(u)])=3`; since `v` is complete to `Q`, every
independent triple lies in `Q`, so `alpha(G[Q])=3`.  The Wood--Woodall
classification used in the dominated two-cut theorem gives a cut of order
at most two in `G[Q]`.  The critical host has order at least 25, so the
exterior is nonempty.  Apply Theorem 2.1. `\square`

## 3. Exact consequence for the five-centre response cube

Retain the five independent centres and common matching from the
centre-singleton interface theorem, with `u=z`.  The four other centres are
nonadjacent to `z`, and hence all lie in the unique component

\[
                              C=G-N_G[z].              \tag{3.1}
\]

Put `T=N_G(C)`.  Then

\[
                              7\leq|T|\leq8.           \tag{3.2}
\]

### Theorem 3.1 (exact full-shore response interface)

The graph `G-T` has exactly two components, both full at `T`.  They are

\[
 C\quad\hbox{and}\quad
 A=N_G[u]-T=
 \begin{cases}
  \{u\},&|T|=8,\\
  \{u,s\},&T=N_G(u)-\{s\}.
 \end{cases}                                          \tag{3.3}
\]

On this exact separation, the canonical `u`-coordinate colouring is proper
on `G[C union T]`, while every nonempty signature on the other four centre
edges is proper on `G[A union T]=G-C`.  Each displayed boundary partition
is rejected by the opposite shore.  Thus all fifteen opposite responses
occur on one exact order-seven/eight cut with two full connected shores.

#### Proof

Since `C=G-N_G[u]`, every vertex outside `C union T` belongs to
`N_G[u]-T`.  If `T=N_G(u)`, this set is `{u}`.  Otherwise the bounds in
(3.2) give `T=N_G(u)-{s}`, and the remaining set is the edge `{u,s}`.
There is no edge from this set to `C`: `u` has none by the definition of
the exterior, and `s notin N_G(C)`.  Hence these are exactly the two
components of `G-T`.

The component `C` has neighbourhood `T` by definition.  The vertex `u` is
adjacent to every member of `T`, so the other component also has full
neighbourhood `T`.  The colouring and rejection assertions are the
component-localised response theorem, now with all four other centres in
`C`; equality of a displayed partition with one extending through the
opposite shore would glue to a six-colouring of `G`. `\square`

The component-localised interface therefore retains the complete punctured
four-coordinate family, not merely a two-coordinate square: the canonical
`z`-coordinate colouring is proper on `G[C union T]`, while every nonempty
signature on the other four centre edges is proper on `G-C=G[N_G[z]]`.
All fifteen opposite responses occur on the one actual boundary `T`.

### Proposition 3.2 (static one-component completion is insufficient)

The finite hypotheses of Lemma 1.1 with only one component vertex do not
force a `K_7^-` minor.  Among the 81 quotients obtained from the nine
eligible graphs `Q` and their nine possible near-complete attachments,
exactly 46 are `K_7^-`-minor-free.  They arise from six eligible graphs;
five retain all nine attachment profiles and one retains one profile.

#### Computer-assisted proof

The final loop in the same deterministic verifier performs this exact
screen and asserts both the total count and the distribution

\[
                              46=9+9+9+9+9+1.         \tag{3.4}
\]

The deletion-and-contraction routine is the same as in Lemma 1.1.
`\square`

Proposition 3.2 is a negative diagnostic, not a counterexample to the live
host theorem.  Its quotients need not be seven-connected,
seven-chromatic, or retain the exact model and punctured response cube.
It establishes the first unsupported inference precisely: connectedness
and one near-complete contracted exterior attachment do not by themselves
yield the `Q`-rooted `K_5^-` model required by the dominated five-root
reduction.  Any closure of the connected residue must spend at least one of
the critical-host inputs discarded by the quotient—most naturally the
four-coordinate response family or the exact-model labels.

### Corollary 3.3 (five exact common-neighbour types remain)

In the target-free live dominated degree-eight state, if `|T|=7` then

\[
                              T=Q,\qquad
                              N_G(C)=Q;                \tag{3.5}
\]

equivalently, the unique boundary vertex missed by `C` is the dominating
vertex `v`.  After contracting `C`, target exclusion leaves exactly five
possibilities for `G[Q]`:

1. `C_5 dotunion K_2`;
2. `C_5` with a pendant path of length two attached at a cycle vertex;
3. the theta graph with path lengths `2,3,3`;
4. `C_7`; or
5. `C_7` with a chord whose resulting cycles have orders four and five.

The same five types, and no others, survive when `|T|=8`.

#### Proof

Suppose `|T|=7` and write `N_G(u)-T={s}`.  The vertex `s` has no neighbour
in `C`.  Since `delta(G)>=8`, its neighbours must be `u` and all seven
vertices of `T`.  If `s in Q`, it is adjacent to all six vertices of
`Q-s`; triangle-freeness of `Q` would make `Q-s` independent, contrary to
`alpha(Q)<=3`.  Hence `s=v`, proving (3.5).

Contract the connected component `C` to one vertex.  When `|T|=8`, that
vertex sees the whole interface `\{v\} union Q`; when `|T|=7`, it sees all
of `Q` and misses only `v`.  The final assertions in the deterministic
verifier screen precisely these two profiles.  Of the nine eligible
unlabelled graphs, exactly the five displayed types are target-free in
either profile. `\square`

### Corollary 3.4 (the complete shore languages are disjoint)

Let `Part_6(L,T)` denote the equality partitions of `T` induced by proper
six-colourings of a closed shore `L`.  In either surviving boundary order,

\[
 \operatorname{Part}_6(G[C\cup T],T)
 \cap
 \operatorname{Part}_6(G-C,T)=\varnothing.           \tag{3.6}
\]

More precisely:

1. if `|T|=8`, every partition from the `C`-shore has six blocks, while
   every partition from the singleton `u`-shore has at most five;
2. if `|T|=7`, every partition from the `C`-shore has at least five blocks,
   while every partition from the edge `uv`-shore has at most four.

Consequently no common boundary partition can eliminate the dominated
degree-eight residue.  Its terminal mechanism must use the rooted-minor or
exact-model structure.

#### Proof

If `|T|=8`, the two shores are `G-u` and `G[N_G[u]]`.  A six-colouring of
`G-u` must use all six colours on `T=N_G(u)`, or a missing colour could be
assigned to `u`.  In a colouring of the singleton closed shore, the colour
of `u` is absent from `T`, giving at most five blocks.

If `|T|=7`, Corollary 3.3 gives `T=Q` and the other component is the edge
`uv`.  In every colouring of `G[\{u,v\}\cup Q]`, the adjacent vertices
`u,v` use two distinct colours, both absent from `Q` because each is
complete to `Q`; thus at most four blocks occur on `Q`.  Conversely, if a
colouring of `G[C\cup Q]` induced at most four blocks on `Q`, assign two
unused colours to `u,v`.  They are adjacent to each other, complete to `Q`,
and have no neighbours in `C`, so this would six-colour `G`.  Hence the
exterior shore uses at least five blocks.  This proves (3.6). `\square`

This is the strongest bounded conclusion currently available in the
dominated degree-eight case.  The single remaining component may have
arbitrary order, and the operation labels need not determine distinct
boundary partitions or distinct branch-set contacts.

## Dependencies and scope

- [dominated-singleton localisation](../results/hc7_k7minus_singleton_coordinate_localisation.md);
- [the dominated common-neighbour two-cut](../results/hc7_k7minus_dominated_singleton_twocut_response.md);
- [exceptional-neighbourhood independence](../results/hc7_k7minus_exceptional_neighbourhood_completion.md); and
- [the degree-eight centre cube interface](hc7_k7minus_degree_eight_centre_cube_interface.md).

The finite lemma is exhaustive only because the host reduction fixes
`|Q|=7`; no unbounded statement is inferred from a search bound.  The host
lift is unbounded in the orders of the exterior components.  The theorem
eliminates the disconnected dominated degree-eight exterior, not the
connected residue or the whole eight-coordinate branch.
