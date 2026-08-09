# Operation-coupled reduction at the four-centre web cut

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_four_centre_operation_cut_reduction_audit.md`](hc7_k7minus_four_centre_operation_cut_reduction_audit.md).
This note refines the rooted-web outcome of the audited
[four-centre theorem](hc7_k7minus_four_centre_web_cut_lattice.md).  It gives
a strict response-carrying descent or a colour-indexed fan, and it identifies
the exact packet-rich residue.  It does not eliminate the web outcome or
prove the `K_7^-` six-colour conjecture.

Throughout, a connected subgraph is **full at** a vertex set `S` if it is
adjacent to every literal vertex of `S`.

## 1. Setting

Let `G` satisfy

\[
 \chi(G)=7,\qquad
 \text{every proper minor of `G` is six-colourable},\qquad
 \kappa(G)\ge7,\qquad K_7^-\npreccurlyeq G.              \tag{1.1}
\]

Let `U` be an independent set of four degree-eight vertices, put `H=G-U`,
and assume that `H` is nonplanar, as supplied by the four-centre theorem.
Fix `r in U` and a six-colouring `phi` of `G-r`.  Choose four colours
which occur exactly once on `N_G(r)`, with representatives
`x_1,x_2,x_3,x_4 in H`.

Assume the rooted-web outcome of the four-centre theorem.  Thus there is a
three-set `T subseteq V(H)` such that, with

\[
                              S=U\mathbin{\dot\cup}T,    \tag{1.2}
\]

the graph `G-S` has two components `C,D`, both full at `S`.  All four
`x_i` avoid `C`, and some `x_j` belongs to `D`.  Fix such an index `j` and
write

\[
                         x=x_j,\qquad \gamma=\phi(x).   \tag{1.3}
\]

For a component `X in {C,D}`, let `nu_X` be the maximum number of pairwise
vertex-disjoint connected subgraphs of `G[X]` which are full at `S`.

## 2. The selected edge response

### Lemma 2.1 (the cross-edge colouring)

Extend `phi` to `r` by assigning `r` the colour `gamma`.  The resulting
map `d` is a proper six-colouring of `G-rx`.  Its restriction to
`G[C union S]` is proper in the original graph `G`.

For every colour `beta ne gamma`, the vertices `x,r` lie in one
`gamma,beta`-component of `G-rx`.

#### Proof

The vertex `x` is the unique neighbour of `r` having colour `gamma`.
Consequently `rx` is the only monochromatic edge after restoring `r`, and
it is absent from `G[C union S]` because `x in D`.

If `x` and `r` lay in distinct `gamma,beta`-components, interchange the two
colours on the component containing `x`.  This makes the edge `rx` proper
and changes no other edge from `r`, producing a six-colouring of `G`, a
contradiction.  \(\square\)

For each `beta ne gamma`, choose a simple `gamma,beta` path from `x` to
`r` in `G-rx`, orient it from `x`, and stop it at its first vertex
`t_beta in S`.  Its internal vertices lie in `D`.  Put

\[
                   T_0=\{r\}\cup\{t_\beta:\beta\ne\gamma\}. \tag{2.1}
\]

The first edge of the stopped `beta`-path after `x` has a `beta`-coloured
other endpoint.  These five first endpoints, and hence these five first
edges, are distinct.

### Theorem 2.2 (five-spoke packing or strict response descent)

At least one of the following alternatives is guaranteed.

1. There is a set `Q subseteq S` of order at most six containing `T_0` and
   five `x`--`Q` paths which preserve the five colour-indexed first edges
   above and are pairwise vertex-disjoint outside `\{x\} union Q`.  Their
   ends in `Q` need not be distinct.
2. There are a five-set `Q subseteq S` containing `T_0`, a four-set
   `Z subseteq D-\{x\}`, and a nonempty connected set
   `A subseteq D-(\{x\} union Z)` such that

   \[
             N_G(A)=(S-Q)\mathbin{\dot\cup}\{x\}
                         \mathbin{\dot\cup}Z.           \tag{2.2}
   \]

   Thus `N_G(A)` is an actual order-seven cut and `|A|<|D|`.  The
   restriction of `d` to `G[A union N_G(A)]` is proper in `G`, and its
   exact `gamma`-coloured boundary block has order at least two.  A proper
   six-colouring of the opposite closed shore attains the same exact block.

The separator in outcome 2 is not asserted to contain `U`; it is a strict
generic exact-seven descent, not automatically a member of the
four-centre cut lattice.

#### Proof

Suppose first that `|T_0|<=5`, and enlarge `T_0` to a five-set `Q subseteq S`.
Apply the audited critical-edge fan-descent theorem with boundary `S`,
operated component `D`, boundary endpoint `r`, internal endpoint `x`, edge
`rx`, and colouring `d`.  Its two conclusions are exactly the two outcomes
above, including (2.2), strict decrease, and the common exact boundary
block.

It remains that `|T_0|=6`; put `Q=T_0`.  Some of the prescribed first
edges may already end in `Q`.  Let there be `q` such direct paths, retain
them, and let `W` be the other `5-q` first endpoints in `D-\{x\}`.  In

\[
                         G[(D-\{x\})\cup Q],            \tag{2.3}
\]

seek `5-q` paths from `W` to `Q`, using every member of `W`, with unit
capacity in `D-\{x\}` and unlimited capacity at `Q`.  Failure gives a set
`Z subseteq D-\{x\}` of order at most `4-q` meeting every such path.
Choose a member of `W-Z` and let `A` be its component in
`G[D-(\{x\} union Z)]`.  It has no neighbour in `Q`, and hence

\[
                    N_G(A)\subseteq(S-Q)\cup\{x\}\cup Z.
\]

The right side has order at most `1+1+(4-q)<=6`.  The set `Q` and the
other component `C` lie outside `A`, so this is a genuine separator,
contrary to seven-connectivity.  The required routing exists.  Prepending
the five prescribed first edges and restoring the direct paths gives
outcome 1.  \(\square\)

## 3. The distinct-ended fan has a contact deficit

### Theorem 3.1 (five-limb contact bound)

There is a fan in `G[D union S]` from `x` to six distinct vertices of `S`
which consists of the edge `xr` and five other paths preserving the five
colour-indexed first edges.  Delete `x` from the five non-direct paths and
call the resulting disjoint connected sets `L_beta`, `beta ne gamma`.
Let their contact graph have these five sets as vertices, with two adjacent
exactly when the corresponding sets have an edge between them in `G`.
This contact graph has at most eight edges.

#### Proof

The distinct-ended fan is Theorem 2.1 of the audited critical-edge
fan-descent result, applied with the same literal data as in Theorem 2.2.
Each `L_beta` is nonempty, and its boundary end lies in `S-\{r\}`.

Suppose the five-set contact graph had at least nine of its ten possible
edges.  Then the seven disjoint connected bags

\[
       \{x\},\qquad C\cup\{r\},\qquad
       L_\beta\quad(\beta\ne\gamma)                   \tag{3.1}
\]

would form a `K_7^-` model.  The first bag meets every limb at its
prescribed first edge.  The second is connected because `C` is full at
`r`, meets `\{x\}` through `rx`, and meets every limb through its distinct
boundary end because `C` is full at `S`.  Among the last five bags at most
one adjacency is missing.  This contradicts (1.1), proving the bound.
\(\square\)

Thus a clean fan is not itself terminal: at least two limb contacts are
missing, and Theorem 2.2 does not allocate the limbs to existing rooted
minor bags.

## 4. The packet-rich residue

### Theorem 4.1 (independent auxiliary boundary)

Up to interchanging `C,D`, one has

\[
                         (\nu_C,\nu_D)=(1,1)
                         \quad\text{or}\quad(1,2).     \tag{4.1}
\]

In the second case `G[T]` is independent.  More strongly,

\[
 \alpha(G[S])=4,                                      \tag{4.2}
\]

and the complement in `S` of every independent four-set is independent.

#### Proof

The audited critical seven-cut capacity theorem gives (4.1).  Suppose
`(nu_C,nu_D)=(1,2)`, with `C` the thin component.  The set `U` is an
independent four-set.  If `G[T]` had an edge, the robust independent-block
closure for an exact `(1,2)` cut, applied with `I=U`, would give a
six-colouring of `G` or a `K_7` minor.  Both contradict (1.1).  Hence `T`
is independent.

The same closure applies to every independent set of order at least five,
and to every independent four-set whose three-vertex complement contains
an edge.  Neither can occur.  Since `U` itself has order four, (4.2) and
the final assertion follow.  \(\square\)

### Theorem 4.2 (one fixed colouring carries all three pair paths)

Assume `(nu_C,nu_D)=(1,2)` with `C` thin.  There is a proper six-colouring
of `G[D union S]` whose equality partition on `S` is

\[
                         U\mid\{t_1\}\mid\{t_2\}
                           \mid\{t_3\},                \tag{4.3}
\]

where `T=\{t_1,t_2,t_3\}`.  In this one fixed colouring, for every
`i ne j` the vertices `t_i,t_j` lie in one bichromatic component on their
two colours.  A corresponding path has all internal vertices in `D`.

#### Proof

Let `Q subseteq C` be connected and full at `S`.  Contract a spanning tree
of the connected set `Q union U` and six-colour the resulting proper minor.
Keep this colouring on `G[D union T]` and assign every member of `U` the
colour of the contraction image.  This is proper, and `U` is one exact
boundary colour block because `Q` is full at every vertex of `T`.

Read the complete equality partition on `S`.  Since `T` is independent,
if its block sizes are `3` or `2,1`, the exact packet demand is two.  The
two disjoint full connected subgraphs in `D` then reflect that partition
onto `G[C union S]`; after permuting colour names, the two shore colourings
glue to a six-colouring of `G`.  Therefore the three vertices of `T` have
distinct colours, proving (4.3).

Fix `i ne j`.  If `t_i,t_j` lay in different components of the subgraph on
their two colours, interchange those colours on the component containing
`t_i`.  On `S` this replaces the two singleton blocks by the independent
block `\{t_i,t_j\}`.  The new partition

\[
                         U\mid\{t_i,t_j\}\mid\{t_k\}
\]

has packet demand two and is again reflectable through the two full
subgraphs in `D`, giving the same contradiction.  Hence the component, and
therefore a path, exists.  The other five boundary vertices use none of
the two path colours, so every internal vertex of a simple such path lies
in `D`.  All three conclusions concern the same initial colouring.
\(\square\)

The three paths in Theorem 4.2 are not asserted to be mutually internally
disjoint or disjoint from the two full subgraphs in `D`.

## 5. Every other centre repairs the rooted obstruction

### Proposition 5.1 (one-centre crossing repair)

Relabel `x_1,x_2,x_3,x_4` in their cyclic order on the outer face of the
web.  For every `s in U-\{r\}`, the graph `H+s` contains an
`\{x_1,x_2,x_3,x_4\}`-rooted `K_4` model, and every such model uses `s`.
Equivalently, `H+s` contains disjoint paths joining the two alternating
pairs `x_1,x_3` and `x_2,x_4`, and exactly one of those paths uses `s`.

#### Proof

Deleting the three vertices `U-\{s\}` from the seven-connected graph `G`
leaves the four-connected graph `H+s`.  It is nonplanar because it contains
the nonplanar subgraph `H`.  The four-connected rooted-`K_4`
theorem of Fabila-Monroy and Wood therefore supplies the rooted model: its
only alternative is a planar graph with all four roots on one face.

The graph `H` has no such rooted model, so every model in `H+s` uses `s`.
The Two Paths characterization gives the displayed alternating linkage.
If neither path used `s`, the linkage would lie in `H`; vertex-disjointness
prevents both paths from using `s`.  Thus exactly one does.  \(\square\)

## 6. Exact remaining obligation

The promoted deductions leave two genuinely dynamic outcomes.

1. A strict response-carrying order-seven descent may replace some of the
   four centres by the operated neighbour and four internal vertices.  Its
   exact colour block is retained, but it cannot be inserted into the
   four-centre lattice without an additional label-preservation theorem.
2. In the clean-packing branch, at least two contacts among the five limbs
   are missing.  In the packet-rich subcase, all three pairwise `T` Kempe
   paths coexist, but they need not avoid the two full packets.

The next accepted theorem must turn one of these into a common boundary
partition, a rooted augmentation, or a strict descent that retains the four
named centres.  Boundary density or unlabelled uncrossing alone does not do
so.

## Dependencies

- [Four-centre rooted model or exact-cut lattice](hc7_k7minus_four_centre_web_cut_lattice.md).
- [Critical boundary-edge fan descent](hc7_exact7_critical_edge_fan_descent.md),
  Theorems 2.1 and 3.1 and Corollary 3.2.
- [Critical seven-cut capacity](hc7_k7minus_critical_seven_cut_capacity.md),
  Lemma 1 and Theorem 3.
- [Adaptive `(1,2)` boundary closure](hc7_exact7_adaptive_12_boundary_closure.md),
  Lemma 2.1.
- R. Fabila-Monroy and D. R. Wood, *Rooted `K_4`-Minors*, Electronic
  Journal of Combinatorics 20(2) (2013), Paper P64, Lemma 2 and Theorems 6
  and 8, <https://doi.org/10.37236/3476>.
