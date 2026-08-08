# Full-lobe contraction does not preserve seven-connectivity

**Status:** barrier/counterexample to an intermediate claim; computation-free
written verification.  This construction contains a `K_7^-` minor and therefore
does **not** refute the `4n-2` extremal target.  It refutes any argument which
deduces seven-connectivity of a full-lobe contraction from seven-connectivity,
boundary fullness, density, and the marked safe-edge cut geometry alone.

## Refuted assertion

The following assertion is false.

> Let `G` be seven-connected, let `Q` be an order-seven cut, and suppose
> `G-Q` has exactly two components `C,D`, each adjacent to every vertex of
> `Q`.  Then contracting `C`, or contracting `C` together with a suitable
> vertex of `Q`, preserves seven-connectivity.

It remains false if `G` is far above the `4|G|-2` density threshold, all the
displayed contractions preserve that density, and `Q` is obtained by lifting
an exact six-cut after a density-safe edge contraction at a degree-seven
vertex.

## Construction

Let

\[
 Q=\{v,s,t_1,t_2,t_3,t_4,t_5\}.
\]

The only edge of `G[Q]` is `vs`.  Let `C` and `D` induce respectively
`K_{12}` and `K_{35}`, with no edge between `C` and `D`.  Choose pairwise
disjoint sets

\[
 A_v,A_s,A_{t_1},\ldots,A_{t_5}\subseteq C,
 \qquad
 B_v,B_s,B_{t_1},\ldots,B_{t_5}\subseteq D
\]

which partition their respective cliques and satisfy

\[
 |A_v|=|A_s|=1,
 \qquad |A_{t_i}|=2,
 \qquad |B_z|=5\quad(z\in Q).
\]

For each `z in Q`, join `z` precisely to every member of
`A_z \cup B_z`, in addition to the edge `vs`.  There are no other edges.

Plainly `G-Q` has exactly the two connected components `C,D`, and both are
adjacent to every vertex of `Q`.  Also

\[
 |V(G)|=54,
 \qquad
 |E(G)|=\binom{12}{2}+\binom{35}{2}+12+35+1=709.
\tag{1}
\]

In particular `|E(G)|>4|V(G)|-2`.

## Seven-connectivity

Let `X` be a set of at most six vertices.  Both `C-X` and `D-X` are
nonempty connected graphs.  A surviving vertex `z in Q` meets both of
them unless `X` contains all of `A_z` or all of `B_z`.

To prevent every member of `Q` from joining `C-X` to `D-X`, for each
`z in Q` the set `X` must contain one of

\[
 \{z\},\qquad A_z,\qquad B_z.
\]

These candidate sets belonging to distinct `z` are pairwise disjoint and
each is nonempty.  Blocking all seven boundary vertices therefore costs at
least seven deletions.  Hence some surviving `z` joins `C-X` to `D-X`.

Every other surviving boundary vertex meets at least one of the two
cliques: deleting both `A_z` and `B_z` costs at least six vertices.  Equality
is possible only for `z in {v,s}`; in that case its boundary mate survives
and joins it to one of the cliques, since deleting the mate as well would
cost seven vertices.  Thus `G-X` is connected.

It follows that `G` is seven-connected.  Deleting `Q` separates `C` from
`D`, so in fact

\[
 \kappa(G)=7. \tag{2}
\]

Moreover `d_G(v)=d_G(s)=7` and

\[
 N_G(v)\cap N_G(s)=\varnothing. \tag{3}
\]

Consequently `vs` is density-safe in the strongest possible common-neighbour
sense.  If `w` is its contraction image in `G/vs`, then

\[
 \{w,t_1,t_2,t_3,t_4,t_5\}
\]

is an exact six-cut with complementary components `C,D`.  The quotient is
six-connected because contracting one edge of a seven-connected graph
cannot lower connectivity by more than one.

## Failure of every full-lobe contraction

Let `c` be the image of `C` in `G/C`.  For every `i`,

\[
 N_{G/C}(t_i)=\{c\}\mathbin{\dot\cup}B_{t_i}.
\]

Thus the six-set `\{c\}\cup B_{t_i}` isolates `t_i`; in particular

\[
 \kappa(G/C)\le6. \tag{4}
\]

Now fix any `z in Q` and contract the connected set `C union {z}` to a
vertex `c_z`.  Choose `t_i \ne z`.  Again

\[
 N_{G/(C\cup\{z\})}(t_i)=\{c_z\}\mathbin{\dot\cup}B_{t_i},
\]

so the same type of six-set isolates `t_i`.  Therefore

\[
 \kappa(G/(C\cup\{z\}))\le6
 \qquad\text{for every }z\in Q.                       \tag{5}
\]

All these contractions remain well above the target density.  More
generally, if

\[
 q(G)=|E(G)|-(4|V(G)|-2),
 \qquad
 \delta_C=|E(G[C])|+|E_G(C,Q)|-4|C|,
\]

then exact simple-edge accounting gives

\[
 q(G/C)=q(G)+3-\delta_C,                              \tag{6}
\]

and, for `z in Q`,

\[
 q(G/(C\cup\{z\}))
   =q(G)+6-\delta_C-d_{G[Q]}(z).                      \tag{7}
\]

Here `q(G)=495` and `delta_C=30`, so (6)--(7) are positive for every
choice of `z`.

## Singleton-lobe variant

The same obstruction persists when one lobe is a singleton, so it cannot be
removed merely by contracting the singleton onto a boundary vertex.

Let `Q={q_0,...,q_6}` induce a seven-cycle, let `C={x}`, and let
`D` induce `K_{28}`.  Partition `D` into disjoint four-sets
`B_0,...,B_6`.  Join `x` to every vertex of `Q`, and join `q_i` to every
member of `B_i`; there are no other edges between the displayed parts.
Then

\[
 d_G(x)=d_G(q_i)=7,
 \qquad |V(G)|=36,
 \qquad |E(G)|=420.                                  \tag{8}
\]

Again `Q` is an exact order-seven cut with the two boundary-full components
`{x}` and `D`.  To see that `G` is seven-connected, delete at most six
vertices.  If `x` survives, separating it from `D` requires, independently
for every `i`, deleting `q_i` or all four vertices of `B_i`, and therefore
requires at least seven deletions.  If `x` is deleted, at most five further
vertices are deleted.  A surviving `q_i` whose entire `B_i` is deleted has
a surviving cycle neighbour with an intact `D`-attachment, since deleting
`x`, `B_i`, and both cycle neighbours would require seven vertices.  Thus
all surviving vertices still lie in one component.  Deleting `Q` separates
`x` from `D`, so `\kappa(G)=7`.

For every `i`,

\[
 |N_G(x)\cap N_G(q_i)|=2.                             \tag{9}
\]

Hence every `xq_i` is density-safe.  Nevertheless, after contracting
`xq_i`, either cycle neighbour, say `q_{i-1}`, has precisely the six
neighbours

\[
 \{xq_i,q_{i-2}\}\mathbin{\dot\cup}B_{i-1}.
\]

Its neighbourhood is a cut of order six in the quotient.  Therefore no
singleton-to-boundary contraction is seven-connected.

## Failure mechanism and exact scope

When the contracted lobe vertex is deleted, all distinct attachments from a
boundary vertex into that lobe disappear simultaneously.  Boundary fullness
only guarantees one edge from each boundary vertex into the lobe; it gives no
robust attachment after the contracted vertex is deleted.  Adding a boundary
vertex to the contracted set generally cannot repair this: it deletes still
more of the original graph whenever the contracted vertex belongs to a cut.

The construction does not satisfy `K_7^-`-minor exclusion.  Accordingly it
does not rule out a theorem whose proof makes essential use of target
exclusion or of a special consequence of minimum counterexample status.  It
does show that those hypotheses must enter the connectivity proof explicitly;
the usual cut-lifting argument alone is insufficient.
