# The fresh induced path at an eight-coordinate singleton

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_singleton_induced_path_common_deletion_audit.md);
and recorded route nonclosure.  This note does not prove the `K_7^-`
six-colour conjecture or `HC_7`.

The singleton-coordinate localisation theorem produces an induced path

\[
                         v-u-w
\]

unless the mate `v` dominates `N_G(u)-\{v\}`.  This note compares that
positive alternative with the audited common-model machinery for an induced
`P_3`.  The comparison has one new terminal consequence: every failure of
seven-connectivity gives an original-labelled response of order seven or
eight carrying the whole punctured two-edge response square.  If neither
response occurs, the surviving seven-connected case still has the old
branch-set allocation obstruction.  The singleton trace adds colour
saturation, not an allocation of those colours among the branch sets.

## 1. Setting

Let `G` be a minor-minimal seven-chromatic graph with no `K_7^-` minor.  Thus
`G` is seven-connected, `delta(G)>=8`, and every proper minor of `G` is
six-colourable.  Let `F_8` be the induced eight-edge forest supplied by the
eight-coordinate reduction, and assume that `G-F_8` is seven-connected.

Let `e=uv` be an edge of `F_8` whose endpoint `u` is an actual singleton
response side.  Assume that there is

\[
              w\in N_G(u)-\{v\},\qquad vw\notin E(G),              \tag{1.1}
\]

and put

\[
              f=uw,\qquad Q=G-\{e,f\}.                             \tag{1.2}
\]

The singleton two-edge theorem proves that `Q` is exactly six-chromatic and
that its equality signatures on `\{e,f\}` are exactly

\[
                 \{e\},\qquad \{f\},\qquad \{e,f\}.                \tag{1.3}
\]

All three colourings restrict to proper colourings of `G-u` and induce
rejected partitions on the one boundary `N_G(u)`.  The graph
`G/\{e,f\}` is exactly six-chromatic and supplies a spanning `K_6`-minor
model whose lift co-bags the induced path `v-u-w`.  The graph `Q` also has
a spanning exact `K_7^vee`-minor model.

Since `e\in F_8`, the graph `G-e` contains the spanning seven-connected
subgraph `G-F_8`.  Hence

\[
                         Q+f=G-e\quad\hbox{is seven-connected}.     \tag{1.4}
\]

This single seven-connected restoration is enough to classify every
six-separation of `Q`.

## 2. Exact terminalisation of the low-connectivity case

### Theorem 2.1 (fresh-path common deletion)

In the setting of Section 1, at least one of the following holds.

1. `Q` is seven-connected.
2. There is a connected set `A` containing `u`, and a six-set `T`, such
   that

   \[
          N_G(A)=T\mathbin{\dot\cup}\{w\}
          \quad\hbox{or}\quad
          N_G(A)=T\mathbin{\dot\cup}\{v,w\}.                     \tag{2.1}
   \]

   The opposite open side `G-(A\cup N_G(A))` is nonempty.  Every colouring
   in (1.3) restricts to a proper colouring of `G-A`, and its partition of
   the one boundary `N_G(A)` is rejected by the intact closed `A`-side.
   Thus (2.1) is an actual response of order seven or eight retaining the
   original coordinate `e`, the fresh coordinate `f`, and all three fixed
   proper-minor colourings.  The edge `f=uw` crosses from `A` to its
   boundary, so its signature-`\{f\}` colouring is also a generic selected
   response on that boundary.  If `A=\{u\}`, then necessarily

   \[
                         N_G(u)=T\mathbin{\dot\cup}\{v,w\}.         \tag{2.2}
   \]

#### Proof

Deleting two incident edges from a seven-connected graph gives a
six-connected graph unless their common endpoint has degree seven and is
isolated by a five-cut in the common deletion.  The latter alternative is
excluded by `delta(G)>=8`.  Therefore `Q` is six-connected.

Suppose that `Q` is not seven-connected, and let `T` be a six-vertex cut.
The graph `Q+f=G-e` is seven-connected by (1.4), so the restored edge `f`
must join different components of `Q-T`.  In particular

\[
                     u,w\notin T.                                  \tag{2.3}
\]

Since one edge reconnects `Q-T`, that graph has exactly two components;
write them as `A,B`, with `u\in A` and `w\in B`.  Six-connectivity makes
both components full to `T`.

If `A=\{u\}`, then `N_Q(u)=T`.  The vertex `v` cannot belong to `T`,
since `uv` is absent in `Q` whereas the component `\{u\}` is full to
`T`.  Together with (2.3), this gives

\[
                       N_G(u)=T\mathbin{\dot\cup}\{v,w\}.          \tag{2.4}
\]

In general no edge of `Q` joins `A` to `B`.  Restoring `f` adds only the
edge `uw`, while restoring `e` adds only `uv`.  Both restored edges have
their endpoint `u` in `A`.  Consequently

\[
 N_G(A)=
 \begin{cases}
   T\mathbin{\dot\cup}\{w\},&v\in A\cup T,\\
   T\mathbin{\dot\cup}\{v,w\},&v\in B.
 \end{cases}                                                       \tag{2.5}
\]

The set `B-(\{w\}\cup(\{v\}\cap B))` is nonempty.  Indeed, if `v` is not
in `B` and `B=\{w\}`, then fullness gives `N_Q(w)=T`, while restoring the
two selected edges adds only the neighbour `u` at `w`; this would give
`d_G(w)=7`, contrary to `delta(G)>=8`.  If `v\in B`, then the connected
component `B` contains a vertex other than `v,w`, since `vw` is not an
edge.  Hence (2.5) is the boundary of an actual separation in both cases.

Finally, `A` contains the common endpoint `u`, so it meets every
monochromatic deleted edge in each of the three signatures (1.3).  Each
colouring therefore restricts to a proper colouring of `G-A`.  If its
induced boundary partition extended through `G[A\cup N_G(A)]`, alignment
of colour names on the boundary would six-colour `G`.  All three partitions
are rejected by the intact `A`-side, proving outcome 2.  \(\square\)

Theorem 2.1 spends all of the connectivity information which is special to
the fresh edge.  In particular, after order-seven and order-eight labelled
responses carrying the entire two-edge square have been excluded, the graph
`Q` itself is seven-connected.  No unbounded separation remains hidden in
this alternative.

## 3. What the common contraction adds

The double contraction supplies more than the three signatures, but its
additional conclusion is still a colour statement.

### Lemma 3.1 (path-contraction saturation)

Let `c_{ef}` be a proper six-colouring obtained by expanding a colouring of
`G/\{e,f\}`; thus

\[
                       c_{ef}(v)=c_{ef}(u)=c_{ef}(w)=alpha.          \tag{3.1}
\]

Then `u` has neighbours of all five colours different from `alpha` outside
`\{v,u,w\}`.  At least one of `v,w` also has neighbours of all those five
colours outside the path.

#### Proof

Every outside neighbour of a path vertex avoids `alpha`, because it is
adjacent to the contracted path vertex before expansion.  If an alternate
colour `beta` were absent from the outside neighbourhood of `u`, assigning
`beta` to `u` while leaving `v,w` coloured `alpha` would restore both path
edges and give a six-colouring of `G`.

If both leaves missed an alternate colour in their respective outside
neighbourhoods, recolour `v` and `w` with such missing colours and leave `u`
coloured `alpha`.  The leaves are nonadjacent by (1.1), so this again gives a
six-colouring of `G`.  Thus at least one leaf sees all five alternate
colours.  \(\square\)

Now lift a spanning `K_6`-minor model of `G/\{e,f\}` and let `R` be the
branch set containing the path.  Split `R` into three connected pieces

\[
                          R_v,\quad R_u,\quad R_w                    \tag{3.2}
\]

containing `v,u,w`, respectively, and retaining the two path adjacencies.
If four of the five foreign branch sets meet all three pieces in (3.2), the
three pieces together with those four branch sets give a `K_7^-` minor: the
only possibly absent adjacency is between the two leaf pieces.  Consequently
every target-free configuration has at most three foreign branch sets meeting
all three pieces.

Lemma 3.1 does not contradict that obstruction.  The five colour witnesses
at `u`, and the five witnesses at one leaf, may be concentrated in one or a
few foreign branch sets.  A proper colouring has no canonical relation to
the labels of a separately chosen minor model.

## 4. Comparison with the audited induced-path case

The positive singleton alternative is stronger than the deferred
six-separation induced-`P_3` case in three respects:

1. all three nonempty equality signatures live on the same singleton
   boundary;
2. the boundary trace is an actual rejected trace, not merely a potential
   operation; and
3. Theorem 2.1 terminalises every failure of seven-connectivity by a labelled
   response of order seven or eight which retains the entire two-edge square.

It is weaker in the one respect needed for the branch-set construction.  The
six-separation induced-path case has an opposite matching coordinate, two
seven-connected restorations, and two complete linkage systems which may be
chosen with a common fan on one shore.  The fresh singleton alternative has
only the incident two-edge response square.  Its three singleton traces say
that every corresponding exterior colouring uses all six colours on
`N_G(u)`; they do not assign the five alternate colours to five foreign model
bags.

Thus, after outcome 2 of Theorem 2.1 is terminalised by the existing labelled
small-boundary machinery, the exact remaining inference is

\[
\begin{gathered}
 Q\text{ seven-connected},\quad
 \Sigma_{\{e,f\}}(\operatorname{Col}_6 Q)
      =\{\{e\},\{f\},\{e,f\}\},\\
 \text{one co-bagged spanning }K_6\text{ model},\quad
 \text{path-contraction saturation}
 \quad\Longrightarrow\quad
 \text{four foreign bags meet all three pieces}.                  \tag{4.1}
\end{gathered}
\]

No proved result in the repository establishes (4.1).  Proving it directly
would duplicate the unresolved branch-set allocation theorem in the audited
induced-`P_3` programme, with fewer linkage labels.  The singleton trace does
not supply the missing allocation.

Accordingly this route should be used as follows:

- accept Theorem 2.1 as the new low-connectivity terminalisation;
- send its labelled order-seven and order-eight outcome to the existing
  bounded-interface machinery while retaining `e,f` and all three colourings;
- do not open a separate fresh-path allocation campaign; and
- use any eventual response-sensitive induced-`P_3` allocation theorem for
  both configurations.

This is a route nonclosure, not a counterexample to (4.1).  The smallest
repair lemma is precisely a response-sensitive induced-path model-allocation
theorem which converts the forbidden empty signature, rather than merely the
three exhibited colourings, into four triple-contacting foreign branch sets
or a common boundary partition.

## 5. Dependencies

- [coordinate responses at a singleton side](hc7_k7minus_singleton_coordinate_localisation.md);
- [incident-pair common-deletion connectivity](../results/hc7_order8_incident_pair_common_deletion_connectivity.md);
- [induced-path common-model theorem](../results/hc7_k7minus_p3_opposite_coordinate_common_model.md); and
- [eight-coordinate forest host](../results/hc7_k7minus_seven_removable_matching_reduction.md).
