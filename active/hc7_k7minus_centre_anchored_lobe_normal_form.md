# A centre-bearing anchored response bypasses the unbounded side

**Status:** active written proof; internal self-audit adjacent; and recorded
route nonclosure.  This is a conditional reduction in the critical host.  It
does not prove the `K_7^-` six-colour conjecture or `HC_7`.

The centre-preserving visibility theorem puts an original degree-eight
centre in the model-anchored response side.  Two different questions then
need to be separated.

First, the centre itself already has an actual boundary of order eight.  No
connected-complement assertion inside its model bag is needed to use that
boundary as a colouring interface.  The other four centre operations give a
punctured response cube on the opposite closed shore, and at least two of
them localise on one exterior component boundary of order seven or eight.
Thus an unbounded centre-bearing side can be bypassed by a bounded,
operation-labelled interface.

Second, deleting the centre need not leave its containing branch set
connected.  If connectedness of both parts of that branch set is retained,
a globally minimum centre-bearing side has an exact cutvertex-lobe normal
form.  Degree eight and the exceptional-neighbourhood identity reduce it to
at most two lobes, but do not remove them.  This note records the exact
remaining obstruction and the quantifier loss in calling those lobes
coordinate-free.

## 1. Setting

Let `G` satisfy

\[
 \chi(G)=7,\qquad
 \chi(J)\leq6\text{ for every proper minor }J\text{ of }G,
 \qquad \kappa(G)\geq7,
 \qquad K_7^-\npreccurlyeq G.                         \tag{1.1}
\]

Fix five independent degree-eight centres

\[
                         Z_0=\{z_1,\ldots,z_5\}.       \tag{1.2}
\]

Use the common-matching theorem to choose independent triples
`I_z subseteq N_G(z)`, representatives `x_z in N_G(z)-I_z`, and the
matching

\[
             M=\{e_z=zx_z:z\in Z_0\}.                 \tag{1.3}
\]

For every nonempty `J subseteq M`, let `c_J` be a proper six-colouring of
`G-M` whose equality signature on `M` is exactly `J`.  After restoring
`M`, its monochromatic edges are precisely the members of `J`.  For
`J={e_z}`, take the canonical colouring from the star contraction at `z`
and abbreviate it to `c_z`.  Its equality partition on `N_G(z)` has shape

\[
                         3+1+1+1+1+1.                 \tag{1.4}
\]

Retain a labelled exact `K_7^vee`-minor model

\[
                     P,B,C,U_1,U_2,U_3,U_4,           \tag{1.5}
\]

where `B,C,U_1,...,U_4` form a `K_6` model, `P` is
anticomplete to `B,C`, and `P` is adjacent to every `U_i`.

A **centre-anchored response configuration** consists of a choice of
`z in Z_0`, one universal branch set `R=U_i`, a nonempty proper connected
set `Y subset R`, and a named foreign branch set `D`, such that

\[
 z\in Y,\qquad R-Y\ne\varnothing\text{ is connected},
 \qquad E_G(Y,D)=\varnothing.                         \tag{1.6}
\]

The edge `e_z` and colouring `c_z` give a rejected exterior trace on `Y`:
deleting `Y` removes the only monochromatic restored edge, and a matching
closed-side boundary partition would glue to a six-colouring of `G`.

## 2. The centre-side bypass

### Theorem 2.1 (bounded multi-coordinate interface)

Suppose a centre-anchored response configuration exists.  Put

\[
                              S=N_G(z).                \tag{2.1}
\]

Then all of the following hold without changing the model in (1.5).

1. `S` is an actual separator of order eight.  The colouring `c_z` is
   proper on `G-z`, its six-block partition on `S` is rejected by the
   singleton closed shore `G[N_G[z]]`, and the same edge `e_z`, colouring
   `c_z`, containing model bag `R`, and named far bag `D` are retained.
2. For every nonempty `J subseteq M-{e_z}`, the restriction of `c_J` to
   `G[N_G[z]]` is proper.  Its boundary partition on `S` is rejected by
   `G-z`.  Thus all fifteen nonempty signatures on the other four centre
   edges occur in the opposite orientation on the same order-eight
   boundary.
3. Some component `Q` of `G-N_G[z]` contains at least two centres of
   `Z_0-{z}`.  With

   \[
       T=N_G(Q),\qquad
       M_Q=\{e_w:w\in (Z_0-\{z\})\cap V(Q)\},          \tag{2.2}
   \]

   one has

   \[
             T\subseteq S,\qquad 7\leq |T|\leq8,
             \qquad |M_Q|\geq2.                       \tag{2.3}
   \]

   The colouring `c_z` is proper on `G[Q union T]`, while every
   `c_J`, for nonempty `J subseteq M_Q`, is proper on `G-Q`.  The induced
   boundary partitions extend through the displayed shore and are rejected
   by the opposite shore.

In particular, reaching a side which contains an original centre never
requires further side-order descent merely to obtain a bounded labelled
response interface.  This conclusion does not require `R-z` to be
connected.

#### Proof

The far branch set `D` is nonempty, disjoint from `R`, and anticomplete to
`z in Y`.  Hence it lies outside `N_G[z]`, so `S` is an actual separator.
Its order is eight because `d_G(z)=8`.

After restoring `M`, the sole monochromatic edge under `c_z` is `e_z`.
Deleting `z` removes it, so `c_z|G-z` is proper.  If its partition on `S`
extended through `G[N_G[z]]`, align the six colour names on the equality
blocks and glue the two colourings.  This would six-colour `G`.
The construction of `c_z` gives (1.4).  No branch set has been altered,
and `D` is still anticomplete to the singleton.  This proves item 1.

Fix nonempty `J subseteq M-{e_z}`.  Every monochromatic restored edge under
`c_J` has its centre end in `Z_0-{z}`.  The centres are independent, so

\[
                         Z_0-\{z\}\subseteq G-N_G[z]. \tag{2.4}
\]

Consequently no such monochromatic edge has both ends in `N_G[z]`, and
`c_J|G[N_G[z]]` is proper.  If its boundary partition also extended
through `G-z`, the same alignment-and-gluing argument would colour `G`.
This proves item 2.

For completeness, the two boundary languages in items 1 and 2 are
automatically disjoint by block count.  Every six-colouring of `G-z` uses
all six colours on `S`, since a missing colour could be assigned to `z`.
Every colouring of `G[N_G[z]]` uses at most five colours on `S`, because
the colour of `z` is absent there.

The graph `G-N_G[z]` is nonempty because it contains `D`.  The audited
degree-eight exterior-component theorem says that it has at most two
components.  All four centres in (2.4) lie in those components, so one
component `Q` contains at least two.  Every neighbour of `Q` belongs to
`S`, and `T` separates `Q` from `z`.  Seven-connectivity gives
`|T|>=7`, while `|S|=8` gives the upper bound in (2.3).

Neither end of `e_z` lies in `Q`: its ends are `z` and
`x_z in N_G(z)=S`.  Hence `c_z` is proper on `G[Q union T]`.  If
`emptyset ne J subseteq M_Q`, every monochromatic restored edge under
`c_J` has its centre end in `Q`; deleting `Q` removes all of them.  Thus
`c_J|G-Q` is proper.  An extension of either displayed partition through
the opposite shore would again glue to a six-colouring of `G`.  This proves
item 3. `\square`

### Corollary 2.2 (unconditional use after centre visibility)

In the target-free outcome of the five-centre model-anchored visibility
theorem, Theorem 2.1 applies immediately.  It is unnecessary to assume that
the subsequent anchored descent ends at the singleton centre.

#### Proof

The visibility theorem returns either the target, an exact order-eight
singleton at a centre already lying in `P,B` or `C`, or a configuration
satisfying (1.6) in a universal bag.  The target is terminal.  In the
universal-bag case Theorem 2.1 applies verbatim.  In the `P,B,C` case the
proof of Theorem 2.1 applies directly with the named anticomplete bag
supplied by visibility; its bounded conclusions never use that the
containing bag is universal or that its complement after deleting `z` is
connected. `\square`

## 3. What remains if the branch-set complement must stay connected

Choose a centre-anchored response configuration with `|Y|` minimum,
globally over the five centres, the exact model and its labels.  Ordinary
minor models, rather than only spanning models, are allowed in this
minimum.

Let `W` be the component of `G[R-z]` containing the connected set `R-Y`.
Every other component of `G[R-z]` lies in `Y-z`.  Denote them by
`A_1,...,A_t`.

### Theorem 3.1 (centre-lobe normal form)

Unless `G` contains a `K_7^-` minor, the minimum configuration has

\[
                   Y=R-W=\{z\}\mathbin{\dot\cup}
                         A_1\mathbin{\dot\cup}\cdots
                         \mathbin{\dot\cup}A_t,
                   \qquad 0\leq t\leq2.              \tag{3.1}
\]

Moreover:

1. every `A_i` is a component of `G[R-z]`, attaches to `z`, and contains
   no centre of `Z_0`;
2. if `mathcal F` is the set of the six foreign model labels and

   \[
      \Lambda(A_i)=\{L\in\mathcal F:
         N_G(L)\cap R\ne\varnothing\text{ and }
         N_G(L)\cap R\subseteq A_i\},                \tag{3.2}
   \]

   then `|Lambda(A_i)|>=2`; these sets are pairwise disjoint and none
   contains `D`;
3. if `t=2`, choose

   \[
      a_i\in N_G(z)\cap A_i,qquad w\in N_G(z)\cap W. \tag{3.3}
   \]

   The set `{a_1,a_2,w}` is a maximum independent set in `G[N_G(z)]`.
   Consequently every other neighbour of `z` is adjacent to at least one
   of `a_1,a_2,w`;
4. for every lobe `A=A_i`, put `B_A=N_G(z)\cap A` and
   `A_L=N_G(L)\cap A` for `L in Lambda(A)`.  Either the target occurs, or
   there are `I subseteq Lambda(A)` and `S_A subseteq A` such that

   \[
       2\leq |I|\leq5,\qquad |S_A|=|I|-1,             \tag{3.4}
   \]

   and `S_A` meets every path in `G[A]` from `B_A` to
   `bigcup_{L in I}A_L`.  Every proper subfamily of `I` has its full
   labelled linkage.

Thus the centre-bearing minimum is the singleton exactly when `R-z` is
connected.  The stated critical-host data reduce failure of that
connectedness to one or two centre-free, multi-owner lobes with a small
owner circuit; they do not eliminate those lobes.

#### Proof

The set

\[
                             Y_z=R-W                  \tag{3.5}
\]

contains `z` and is contained in `Y`.  It is connected: every component of
`G[R-z]` other than `W` has an edge to `z`, because `G[R]` is connected.
Its complement in `R` is the connected nonempty set `W`, and the named far
bag `D` is anticomplete to `Y_z subseteq Y`.  Deleting `Y_z` removes the
centre end of the only monochromatic edge under `c_z`, so the same fixed
response is rejected on `Y_z`.  Hence (3.5) is another centre-anchored
configuration.  Minimality gives `Y_z=Y`, proving the decomposition in
(3.1).

Choose one neighbour of `z` in every component of `G[R-z]`.  Vertices
chosen in distinct components are pairwise nonadjacent and all belong to
`N_G(z)`.  The exceptional-neighbourhood theorem gives

\[
                         \alpha(G[N_G(z)])=3,          \tag{3.6}
\]

so `G[R-z]` has at most three components and `t<=2`.  When `t=2`, the
three vertices in (3.3) attain equality in (3.6).  A further neighbour of
`z` anticomplete to all three would create an independent four-set, proving
item 3.

Fix a lobe `A`.  Both `R-A` and `Y-A` are connected: they consist of `z`
together with the remaining components of `G[R-z]`.  If
`Lambda(A)=empty`, omit `A` from the branch set `R`.  All required model
adjacencies remain, and `Y-A` with the same centre operation is a smaller
configuration.  If `Lambda(A)={L}`, move `A` into the branch set `L`.
The new `L`-bag is connected, an `A-z` edge restores its adjacency to
`R-A`, and every other required adjacency survives.  If this creates one
of `PB,PC`, the seven bags miss at most the other and form an explicit
`K_7^-` model; otherwise they remain an exact `K_7^vee` model.  The far
label cannot be `L`, since `D` is anticomplete to `A`.  In the target-free
case, `Y-A` is again a smaller configuration.  Both possibilities
contradict minimality, so `|Lambda(A)|>=2`.

One foreign label cannot be monopolised by two disjoint lobes, and the
required `R-D` contact lies in `W` because `D` is anticomplete to `Y`.
This proves the remaining assertions in item 2.  If a lobe contained a
centre `z' in Z_0`, then the same model, the connected split `A,R-A`, the
far bag `D`, and the response at `e_{z'}` would make `A` a smaller
centre-anchored configuration.  Thus the lobes are centre-free, proving
item 1.

Finally suppose the full family `Lambda(A)` had pairwise vertex-disjoint
paths in `G[A]` from distinct vertices of `B_A` to the respective sets
`A_L`.  Enlarge those paths to a connected partition of `A`, one part for
each label.  Move each part into its owner bag and replace `R` by `R-A`.
The endpoint in `B_A` restores the owner's adjacency to `R-A` through
`z`, and the endpoint in `A_L` attaches the part to its owner bag.  As
above, this gives the target or a smaller centre-anchored configuration.
Thus the full labelled linkage does not exist.

Apply Rado's independent-transversal theorem to the strict gammoid of sets
linkable to distinct vertices of `B_A`.  Choose an inclusion-minimal
deficient family `I`.  A singleton is not deficient because `G[A]` is
connected and both endpoint sets are nonempty.  Minimality gives rank
`|I|-1`, and vertex Menger supplies a separator `S_A` of that order.
Every proper subfamily is linkable by the choice of `I`.  This proves
item 4. `\square`

## 4. Exact quantifier boundary

The lobes in Theorem 3.1 are centre-free, but the restricted minimum does
not make them free of all matching-coordinate endpoints.  A lobe may
contain a mate `x_w` while the corresponding centre `w` lies outside it.
The singleton-signature colouring at `e_w` then gives a response on the
lobe, but that smaller side no longer contains a centre.  Enlarging the
minimisation class to all matching-endpoint response sides would remove
such a lobe, at the price of losing the centre whose degree-eight boundary
enabled Theorem 2.1.

Therefore the two useful statements have incompatible minimisation
classes:

\[
\begin{array}{c|c|c}
 \text{minimum class}&\text{retains}&\text{does not force}\\ \hline
 \text{centre-bearing sides}&z, d_G(z)=8&
                    A_i\cap V(M)=\varnothing\\
 \text{all matching-endpoint sides}&
                    A_i\cap V(M)=\varnothing&
                    \text{a centre in the minimum side}.
\end{array}                                             \tag{4.1}
\]

This is a recorded route nonclosure, not a counterexample to a stronger
host theorem.  The owner-circuit reduction does not repair it: owner bags
are precisely the bags with no contact from `R-A`, so neither the centre
nor its fixed matching edge supplies any of the monopolised adjacencies.

Theorem 2.1 makes this nonclosure less damaging than the former unbounded
side problem.  The remaining implication is now bounded but still
unsupported:

\[
 \begin{gathered}
  \text{the exact model, the canonical six-block centre response, and an
  opposite}\\
  \text{punctured response square on one order-seven/eight component
  boundary}
 \end{gathered}
 \Longrightarrow
 \begin{gathered}
  K_7^-\preccurlyeq G,\quad\text{or a strict labelled model split or
  component descent}.
 \end{gathered}                                        \tag{4.2}
\]

A common partition cannot close the full singleton boundary: every
colouring of `G-z` has six boundary blocks, while the singleton closed
shore has at most five.  What remains is to turn an operation label on the
component boundary into a prescribed exact-model contact.  Further
side-order minimisation is unnecessary for obtaining a bounded interface
and does not perform that allocation.

## Dependencies

- [the common five-centre matching and punctured response cube](../results/hc7_k7minus_five_centre_common_matching_reduction.md);
- [centre-preserving exact-model visibility](hc7_k7minus_five_centre_model_anchored_visibility.md);
- [the exceptional-neighbourhood independent triple](../results/hc7_k7minus_exceptional_neighbourhood_completion.md);
- [the degree-eight exterior-component bound](../results/hc7_low_degree_exterior_component_bounds.md); and
- [model ownership and coordinate avoidance](../results/hc7_k7minus_model_anchored_appendage_ownership.md).

The proof is unbounded and computation-free.  It replaces the unbounded
centre-bearing side by a fully labelled bounded interface and gives the
exact normal form of any retained connected-complement obstruction.  It
does not terminalise that bounded interface, eliminate the one- or
two-lobe normal form, prove Conjecture 21, or prove `HC_7`.
