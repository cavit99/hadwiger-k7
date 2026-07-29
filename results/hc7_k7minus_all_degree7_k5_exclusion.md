# All-degree-seven `K_5` exclusion by Kempe-component allocation

**Status:** written proof; separate internal audit GREEN for this revision.

Here `K_7^-` denotes `K_7` with one edge deleted.  The principal theorem
below isolates the exact private-triangle hypotheses used by the earlier
critical-equality argument; no density equality is assumed.

## Theorem 1 (private-triangle Kempe allocation)

Let `G` be a finite simple graph such that

\[
 \chi(G)=7,
 \qquad
 \text{every proper minor of `G` is six-colourable}.
                                                               \tag{1}
\]

Suppose `A` is a literal `K_5` in `G` and, for every `a\in A`,

\[
                    T_a=N_G(a)-A                              \tag{2}
\]

is a triangle.  Suppose also that the five triangles `T_a` are pairwise
vertex-disjoint, each `T_a` is anticomplete to `A-\{a\}`, and `G-A` is
connected.  Then `G` contains an explicit `K_7^-`-minor model.

### Proof

Put `H=G-A`.  Fix `a_i\in A` and `x\in T_{a_i}`.  Since `G-a_ix` is a
proper minor, choose a proper six-colouring `phi` of it.  Necessarily

\[
                         \phi(a_i)=\phi(x)=p,                  \tag{3}
\]

since otherwise `phi` would colour `G`.  The clique `A` uses five distinct
colours.  Let `q` be the unique sixth colour, put

\[
                         S_a=\phi(T_a),                        \tag{4}
\]

and write

\[
                         S_{a_i}=\{p,q,r\}.                    \tag{5}
\]

Indeed, `q` must occur on `T_{a_i}`: otherwise recolouring `a_i` with `q`
would restore the deleted edge and six-colour `G`.  Let `a_h` be the member
of `A-\{a_i\}` coloured `r`, and put

\[
 J=A-\{a_i,a_h\},
 \qquad c_j=\phi(a_j)\quad(a_j\in J).                         \tag{6}
\]

Thus the six colours are

\[
                         \{p,q,r\}\cup\{c_j:a_j\in J\}.       \tag{7}
\]

For every `a\in A`, let

\[
                         L_a=[6]-S_a                           \tag{8}
\]

be the colours available at `a` over the fixed colouring of `H`.

#### Claim 2 (edge-critical Kempe fork)

For each `a_j\in J`, let `P_j` be the component of `H[p,c_j]` containing
`x`.  Then:

1. both `p` and `q` occur on `T_{a_j}`;
2. `P_j` meets `T_{a_j}`;
3. either `p,q` occur on all five private triangles, or

   \[
                 S_{a_j}=S_{a_i}=\{p,q,r\}
                 \quad\text{for every `a_j\in J`};            \tag{9}
   \]

4. in the second outcome of part 3, every `P_j` meets all four triangles

   \[
                 T_{a_i},\qquad T_{a_t}\quad(a_t\in J).       \tag{10}
   \]

##### Proof of Claim 2

The four vertices of `A-\{a_i\}` use the four colours outside `\{p,q\}`,
and (5) gives

\[
                         L_{a_i}=\{c_j:a_j\in J\}.              \tag{11}
\]

Fix `a_j\in J`.  If `p\in L_{a_j}`, assign `c_j` to `a_i`, assign `p` to
`a_j`, and retain the original colours on the other three vertices of `A`.
If `q\in L_{a_j}`, use `q` at `a_j` in the same assignment.  Either choice
would extend the colouring of `H` to a six-colouring of `G`.  Hence both
`p,q` occur on `T_{a_j}`, proving part 1.

Suppose `P_j` misses `T_{a_j}` and interchange `p,c_j` on `P_j`.  The
triangle `T_{a_i}` contains `p` only at `x` and contains no `c_j`, so the
interchange removes `p` from `T_{a_i}`.  Assign `p` to `a_i` and retain the
original colours on `A-\{a_i\}`.  The colour `c_j` remains available at
`a_j` because `P_j` misses its private triangle, and all other retained
colours lie outside the interchanged pair.  The restored edge has colours
`p,c_j`.  This six-colours `G`, a contradiction, proving part 2.

By part 1, write

\[
                         S_{a_j}=\{p,q,s_j\}\quad(a_j\in J).   \tag{12}
\]

Suppose `p,q` do not both occur on `T_{a_h}`.  Choose
`t\in\{p,q\}\cap L_{a_h}`.  If some `s_j\ne r`, then `r\in L_{a_j}`.
Assign `t` to `a_h`, `r` to `a_j`, `c_j` to `a_i`, and retain the two
original colours on `J-\{a_j\}`.  These are five distinct available
colours, and the restored edge has colours `c_j,p`, again a contradiction.
Therefore every `s_j=r`, proving part 3.

Finally assume (9), fix `a_j\in J`, and let `a_t\in J-\{a_j\}`.  If the
component of `H[p,c_j]` containing the `p`-coloured vertex of `T_{a_t}`
were different from `P_j`, it would miss both `T_{a_i}` and `T_{a_j}`:
their unique `p`-coloured vertices lie in `P_j`, and neither triangle
contains `c_j`.  Interchange `p,c_j` on that different component, assign
`p` to `a_t`, assign `c_t` to `a_i`, and retain the other three clique
colours.  This is a proper six-colouring of `G`, a contradiction.  Hence
every `P_j` meets all four triangles in (10).  This proves part 4 and the
claim.  \(\square\)

For every `a\in A` on whose triangle `p` or `q` occurs, write `p_a` or
`q_a` for the uniquely coloured vertex.  Put `y=q_{a_i}`.  For `a_j\in J`,
let `Q_j` be the component of `H[q,c_j]` containing `y`.

#### Claim 3 (symmetric component reach)

Every `Q_j` meets `T_{a_j}`.  In the second outcome of Claim 2(3), every
`Q_j` meets all four triangles in (10).

##### Proof of Claim 3

If `Q_j` missed `T_{a_j}`, interchange `q,c_j` on `Q_j`.  This removes `q`
from `T_{a_i}`, leaves the list at `a_j` unchanged, and permits the
assignment `q` to `a_i` while retaining the original colours on the other
four clique vertices.  The restored edge has colours `q,p`, a
contradiction.

Now assume (9).  If `a_t\in J-\{a_j\}` and the component of `H[q,c_j]`
containing `q_{a_t}` differed from `Q_j`, it would miss `T_{a_i}` and
`T_{a_j}` and all three relevant triangles would contain no `c_j`.
Interchanging on that component, assigning `q` to `a_t`, assigning `c_t`
to `a_i`, and retaining the other clique colours would six-colour `G`.
Thus every `Q_j` has the stated reach.  \(\square\)

We now exclude the two outcomes of Claim 2(3).

#### Claim 4 (common four-triangle outcome)

The second outcome of Claim 2(3) yields a `K_7^-` minor.

##### Proof of Claim 4

Choose distinct `a_j,a_l\in J` and put

\[
                            X=P_j,
 \qquad                     Y=Q_l.                    \tag{13}
\]

The sets `X,Y` are connected and vertex-disjoint because their colour sets
`\{p,c_j\}` and `\{q,c_l\}` are disjoint.  Claims 2 and 3 show that both
sets meet the same four triangles in (10), and an edge `p_aq_a` in any one
of those triangles makes them adjacent.

If `T_{a_h}` misses `X\cup Y`, take a shortest path in the connected graph
`H` from `T_{a_h}` to `X\cup Y`, stopped at its first vertex in that union,
and add the path to the set containing its final vertex.  If `T_{a_h}`
already meets the union, no path is needed.  We obtain disjoint connected
sets `X',Y'`, one meeting all five private triangles and the other meeting
the four triangles in (10), with an edge between them.

The five singleton sets `\{a\}`, `a\in A`, together with `X',Y'`, are seven
pairwise disjoint connected branch sets.  Every required adjacency is
present except possibly the adjacency between `a_h` and the set not meeting
`T_{a_h}`.  They form an explicit `K_7^-`-minor model.  \(\square\)

It remains to treat the first outcome of Claim 2(3), in which `p,q` occur
on all five triangles.  Write

\[
                         S_a=\{p,q,s_a\}\quad(a\in A).          \tag{14}
\]

Then

\[
 s_{a_i}=r,
 \qquad s_{a_h}\in\{c_j:a_j\in J\},
 \qquad s_{a_j}\ne c_j\quad(a_j\in J).                       \tag{15}
\]

The first equality is (5).  For every `a\ne a_i`, all edges from `a` to
`T_a` remain present in `G-a_ix`, so the colour on `a` is absent from
`S_a`; this gives the other two assertions.

Claim 4 excludes (9), so some `a_u\in J` satisfies `s_{a_u}\ne r`.

#### Claim 5 (all-five-triangle component reach)

Fix `a_j\in J`.  If `a_t\in A` and `s_{a_t}\ne c_j`, then

\[
                         p_{a_t}\in P_j,
 \qquad                  q_{a_t}\in Q_j.                      \tag{16}
\]

##### Proof of Claim 5

The assertion follows from the definitions for `a_t=a_i` and from Claims 2
and 3 for `a_t=a_j`.

Let `a_t\in J-\{a_j\}`.  If the component of `H[p,c_j]` containing
`p_{a_t}` differed from `P_j`, it would miss `T_{a_i}` and `T_{a_j}`.
The hypothesis `s_{a_t}\ne c_j` says that `T_{a_t}` also contains no
`c_j`.  Interchange `p,c_j` on that component, assign `p` to `a_t`, assign
`c_t` to `a_i`, and retain the other clique colours.  This six-colours `G`,
a contradiction.  The same argument with `q,c_j` proves the assertion for
`Q_j`.

Finally let `a_t=a_h`.  Suppose the relevant `p,c_j` component through
`p_{a_h}` differs from `P_j`.  It misses `T_{a_i}` and `T_{a_j}`, and the
hypothesis makes `T_{a_h}` free of `c_j`; its interchange therefore removes
`p` from `T_{a_h}`.  Assign

\[
                p\text{ to }a_h,
 \qquad          c_u\text{ to }a_i,
 \qquad          r\text{ to }a_u,                            \tag{17}
\]

and retain the original colours on the other two vertices of `J`.  The
choice `s_{a_u}\ne r` makes `r` available.  If `a_u=a_j`, no clique vertex
retains `c_j`; otherwise the interchanged component misses `T_{a_j}`.
Every other retained colour lies outside the interchanged pair, and the
restored edge has colours `c_u,p`.  This is again a six-colouring of `G`.
Replacing `p` by `q` gives the same conclusion for `Q_j`, proving (16).
\(\square\)

#### Claim 6 (all-five-triangle outcome)

The first outcome of Claim 2(3) yields a `K_7^-` minor.

##### Proof of Claim 6

For `a_j\in J`, put

\[
              n_j=|\{a\in A:s_a=c_j\}|.                       \tag{18}
\]

Only `a_h` and the three vertices of `J` can contribute, so

\[
                         \sum_{a_j\in J}n_j\le4.               \tag{19}
\]

Choose `a_l\in J` with `n_l\le1`, and write
`J=\{a_j,a_k,a_l\}`.  Define

\[
                         X=P_j\cup P_k,
 \qquad                  Y=Q_l.                                \tag{20}
\]

The set `X` is connected because both components contain `x`; `Y` is
connected.  They are vertex-disjoint because their colour sets are
`\{p,c_j,c_k\}` and `\{q,c_l\}`.

For every `a\in A`, the colour `s_a` cannot equal both `c_j` and `c_k`, so
Claim 5 puts `p_a` in `X`.  Thus `X` meets all five triangles.  Claim 5 puts
`q_a` in `Y` except possibly when `s_a=c_l`, which occurs on at most one
triangle.  Every nonexceptional triangle contains an edge between `X` and
`Y`.  The five singleton vertices of `A`, together with `X,Y`, consequently
form an explicit `K_7^-`-minor model.  \(\square\)

Claims 4 and 6 exhaust Claim 2(3), proving Theorem 1.  \(\square\)

## Theorem 7 (all-degree-seven clique exclusion)

Let `G` satisfy

\[
 \kappa(G)\ge7,
 \qquad \chi(G)=7,
 \qquad \text{every proper minor of `G` is six-colourable},
 \qquad K_7^-\npreccurlyeq G.                                 \tag{21}
\]

Then no literal `K_5` in `G` has all five vertices of degree seven.

### Proof

Suppose `A` is such a clique.  Fix `a\in A`.  If `a` belonged to a second
literal `K_5`, the exact degree-seven neighbourhood theorem would make the
two cliques meet in exactly `\{a,w\}` for some `w\in A`.  Their union has
eight vertices.  Both `a` and `w` have all seven neighbours in that union,
and the two three-vertex exclusive parts are anticomplete.  If a vertex lay
outside the union, the six exclusive vertices would be a cut of order six.
If no vertex lay outside, seven-connectivity would force the eight-vertex
graph to be complete.  Both alternatives are impossible.  Thus every
member of `A` lies in no other literal `K_5`.

The exact neighbourhood theorem now gives, for each `a\in A`, a triangle
`T_a=N(a)-A` anticomplete to `A-\{a\}`.  These triangles are pairwise
disjoint: a common vertex of `T_a,T_b` would be both adjacent and
nonadjacent to `a`.  Finally, deleting the five vertices of `A` from a
seven-connected graph leaves a connected graph.  Theorem 1 therefore gives
a `K_7^-` minor, contradicting (21).  \(\square\)

## Corollary 8 (degree count and the tight layer)

Under (21), let `n_i` be the number of degree-`i` vertices and put

\[
                         s=\sum_{i\ge9}(i-8)n_i.                \tag{22}
\]

Then

\[
                         n_7\le8,
 \qquad                  |E(G)|\ge4|V(G)|-4.                  \tag{23}
\]

If equality holds in (23), then

\[
                         n_7=8,
 \qquad                  s=0,                                 \tag{24}
\]

so the degree sequence is

\[
                         7^8 8^{|V(G)|-8}.                     \tag{25}
\]

Exactly two literal `K_5`s cover the eight degree-seven vertices.  Each
contains four degree-seven vertices and one degree-eight vertex, and the two
cliques are disjoint or meet in their common degree-eight vertex.  Moreover,

\[
                         |V(G)|\ge21.                           \tag{26}
\]

### Proof

Every degree-seven vertex lies in a literal `K_5`, while the audited global
clique theorem gives at most two literal `K_5`s in `G`.  Theorem 7 allows at
most four degree-seven vertices in either clique, proving `n_7\le8`.
Degree summation gives

\[
 2|E(G)|=8|V(G)|-n_7+s\ge8|V(G)|-8,                           \tag{27}
\]

which proves (23).

If equality holds, (27) gives `n_7-s=8`; hence `n_7=8` and `s=0`.  The two
literal `K_5`s are both needed to cover the degree-seven vertices, and each
contains exactly four.  Their degree-seven subsets are disjoint.  Since
each clique has only one remaining vertex, any intersection consists of
their common degree-eight vertex, proving the structural assertion.

Choose one clique `A` and let `z` be its degree-eight vertex.  Its four
degree-seven vertices lie in no other literal `K_5`, so their four private
triangles are pairwise disjoint and occupy twelve vertices outside `A`.
They are anticomplete to `z`.  The vertex `z` has four further neighbours
outside `A`, all outside those triangles.  Therefore

\[
                         |V(G)|\ge5+12+4=21.
\]

This proves (26).  \(\square\)

## Dependencies and scope

The local dependency is the audited
[exact degree-seven neighbourhood theorem](hc7_k7minus_degree7_clique_incidence.md).
The global count uses the audited
[three-literal-`K_5` exclusion](hc7_k7minus_three_clique_bound.md); its
non-two-apex hypothesis follows from `chi(G)=7`.

The proof is unbounded and uses no finite enumeration.  It strengthens the
structure behind the existing critical-host bound but does not prove a bare
seven-connected `4n-4` extremal theorem, the `K_7^-` six-colour conjecture,
or `HC_7`.  Theorem 1 constructs two disjoint connected branch sets of which
one may miss one private triangle; it does not prove a bond meeting all five
triangles or two full connected transversals.
