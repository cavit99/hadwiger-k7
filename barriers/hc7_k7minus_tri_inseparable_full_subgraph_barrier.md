# A tri-inseparable side need not contain two boundary-full connected subgraphs

**Status:** written barrier to an intermediate structural claim; separate
internal audit GREEN in
[`hc7_k7minus_tri_inseparable_full_subgraph_barrier_audit.md`](hc7_k7minus_tri_inseparable_full_subgraph_barrier_audit.md).
The proof is computation-free.  This graph contains a `K_7` minor and is
not a counterexample to the `K_7^-` six-colour conjecture.

## 1. The claim refuted

The following implication is false without using minor-criticality or the
exclusion of a `K_7^-` minor.

> Let `G` be a seven-connected, `K_5`-free graph of minimum degree at least
> eight.  Suppose an independent seven-set
> `S=U dotcup T`, with `|U|=4` and `|T|=3`, separates connected sets `C,D`
> which are each adjacent to every vertex of `S`.  Put `H=G-U`.  If every
> member of `T` has at least two neighbours in `C` and no mixed separation
> of `H` of order at most three splits `C`, then `C` contains two disjoint
> connected subgraphs which are each adjacent to every vertex of `S`.

The construction below satisfies all the hypotheses and not the conclusion.
It shows that the canonical tri-separation residue does not by itself supply
the two connected subgraphs needed by boundary-colouring reflection.

## 2. Construction

Let

\[
 C=K_{2,2,2,1}
\]

with vertex set `c_0,...,c_6` and nonedges

\[
 c_0c_1,\qquad c_2c_3,\qquad c_4c_5.                 \tag{2.1}
\]

Thus all other pairs in `C` are adjacent.  Let `D` be the five-cycle
`d_0d_1d_2d_3d_4d_0`, and let

\[
 S=\{s_0,\ldots,s_6\}
\]

be independent.  There are no edges between `C` and `D`.  Make every
vertex of `S` adjacent to every vertex of `D`.

The neighbours in `C` of the seven vertices of `S` are the lines of the
Fano plane:

\[
\begin{array}{c|c}
s_0&\{c_0,c_1,c_2\}\\
s_1&\{c_0,c_3,c_4\}\\
s_2&\{c_0,c_5,c_6\}\\
s_3&\{c_1,c_3,c_5\}\\
s_4&\{c_1,c_4,c_6\}\\
s_5&\{c_2,c_3,c_6\}\\
s_6&\{c_2,c_4,c_5\}.
\end{array}                                           \tag{2.2}
\]

Finally put

\[
 U=\{s_0,s_1,s_2,s_3\},\qquad
 T=\{s_4,s_5,s_6\},\qquad H=G-U.                     \tag{2.3}
\]

Deleting `S` leaves exactly the two components `C,D`, and each is adjacent
to every vertex of `S`.  Deleting `T` from `H` likewise leaves exactly
`C,D`.

## 3. Degree, clique and connectivity checks

Every vertex in a part of order two in `C` has five neighbours in `C` and
belongs to three lines in (2.2), so it has degree eight in `G`.  The
singleton-part vertex `c_6` has degree nine.  Every vertex of `D` has its
two cycle neighbours and all seven neighbours in `S`, while every vertex
of `S` has three neighbours in `C` and five in `D`.  Hence

\[
                         \delta(G)=8,                  \tag{3.1}
\]

and every member of `U` has degree eight.  In particular, every member of
`T` has three neighbours in `C`, which is stronger than the two-neighbour
hypothesis in Section 1.

The graph has no `K_5` subgraph.  A clique cannot meet both `C` and `D`,
and it contains at most one vertex of the independent set `S`.  The largest
clique in `C` has order four.  A vertex `s_i` has only three neighbours in
`C`, so a clique meeting both `S` and `C` has order at most four.  A clique
in `D union S` has order at most three.

We next prove that `G` is seven-connected.  Let `X` have order at most six.
Since `|S|=7`, at least one vertex of `S-X` remains.

Suppose first that `D-X` is nonempty.  The graph on `(D union S)-X` is
connected because every remaining vertex of `D` is adjacent to every
remaining vertex of `S`.  If `|X cap C|<=4`, then `C-X` is connected since
`K_{2,2,2,1}` is five-connected.  At least one edge from `C-X` to `S-X`
also remains: the incidence graph in (2.2) has 21 edges, while deleting
`|X cap C|+|X cap S|<=6` of its vertices covers at most 18 incidences.
Thus `C-X` meets the connected graph `(D union S)-X`.

If `|X cap C|>=5`, then `|X cap S|<=1`.  Every remaining vertex of `C`
therefore retains at least two neighbours in `S-X`, so all remaining
vertices again lie in one component.

It remains that `D subseteq X`.  Deleting the five vertices of `D` leaves
room for at most one further deleted vertex.  The graph `C-X` is connected,
and every remaining vertex of `S` has a neighbour in it.  Hence `G-X` is
connected in this case as well.  Therefore `kappa(G)>=7`.  The set `S`
separates `C` from `D`, so

\[
                         \kappa(G)=7.                  \tag{3.2}
\]

It follows in particular that `H=G-U` is three-connected.

## 4. No mixed separation of order three splits `C`

We prove a stronger fact inside `C`.  Delete `k<=3` vertices from
`K_{2,2,2,1}`.  The remaining graph is complete multipartite, has order
`7-k`, and has no part larger than two.  Its edge-connectivity is its
minimum degree, which is at least

\[
                         (7-k)-2=5-k.                  \tag{4.1}
\]

Consequently, a mixed cut of `C` using `k` vertices and some crossing edges
has order at least

\[
                         k+(5-k)=5.                   \tag{4.2}
\]

Now let `(A,B)` be a mixed separation of `H` whose two open sides both meet
`C`.  The vertices of `C cap A cap B`, together with the edges of `C`
joining the two open sides, form a mixed cut of `C`.  Their number is at
most the order of `(A,B)`.  Equations (4.1) and (4.2) show that `(A,B)`
has order at least five.  In particular, no tri-separation of `H` splits
`C`.

## 5. The Fano obstruction

Suppose that `P,Q` were disjoint vertex sets in `C`, each adjacent to every
vertex of `S`.  Then every line in (2.2) would meet both `P` and `Q`.
Colour the vertices of `P` red and those of `Q` blue, and colour any
remaining vertices arbitrarily.  Every Fano line would contain both
colours.

The Fano plane has no such two-colouring.  For completeness, one colour
has at least four points.  If it has more than four, its pairs determine
more than the seven lines unless three of its points lie on one line.  If
it has exactly four and has no monochromatic line, its six pairs lie on six
distinct lines of type `2+1`.  The three pairs of the other colour would
then require three further lines of the opposite type, although the Fano
plane has only seven lines.  This is impossible.

Thus no two disjoint subsets of `C` are both adjacent to every vertex of
`S`.  In particular, there are no two disjoint connected subgraphs of `C`
with that property.

## 6. Scope

This example blocks only the passage from tri-inseparability and local
degree conditions to two boundary-full connected subgraphs.  It does not
rule out a theorem that uses the fixed boundary-colouring partition,
proper-minor colouring responses, or the exclusion of a `K_7^-` minor.

Indeed, the graph contains a `K_7` minor.  For `0<=i<=4`, put

\[
                         B_i=\{d_i,s_i\}.
\]

The five sets `B_i` are connected and pairwise adjacent.  The two sets

\[
 P=\{c_0,c_1,c_6\},\qquad Q=\{c_2,c_3,c_4,c_5\}
\]

are connected, adjacent to each other, and each adjacent to every `B_i`.
These seven sets form a `K_7` minor model.  The construction is therefore
not a counterexample to the target conjecture and makes no claim of
minor-criticality.

The remaining positive question is partition-specific.  For the fixed
one-sided boundary partition, one must either construct disjoint connected
branch sets which absorb its colour classes and form the clique minor used
by exact colouring reflection, obtain a mixed separation that splits `C`,
or construct the target minor directly.
