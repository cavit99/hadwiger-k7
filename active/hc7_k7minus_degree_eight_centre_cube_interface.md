# A degree-eight centre exposes an opposite four-coordinate response interface

**Status:** active written proof; internal self-audit adjacent.  This is a
conditional reduction in the eight-coordinate exact-model campaign.  It does
not prove the `K_7^-` six-colour conjecture or `HC_7`.

The centre-preserving visibility theorem ensures that a model-anchored
response side contains one of the five original degree-eight centres.  If the
anchored reduction ends at the singleton centre, its boundary has order eight.
The other four centres then give considerably more than one additional
operation: all fifteen nonempty signatures on their matching edges induce
proper colourings of the singleton closed shore.  On a component outside the
closed neighbourhood, the centres in that component give a punctured response
cube in the opposite orientation on a boundary of order seven or eight.

This converts the singleton endpoint into a bounded, multi-operation
interface.  It also identifies a rigid obstruction: the two shore-colouring
languages at the full singleton boundary have different numbers of boundary
blocks, so a common boundary partition is impossible there.  Any closure must
therefore use the minor-model geometry or pass to one of the component
boundaries; colour gluing alone cannot eliminate the singleton.

## 1. Setting

Let `G` satisfy

\[
 \chi(G)=7,\qquad
 \chi(J)\leq 6\text{ for every proper minor }J\text{ of }G,
 \qquad \kappa(G)\geq7,
 \qquad K_7^-\npreccurlyeq G,                         \tag{1.1}
\]

and retain the critical-host conclusions

\[
 |V(G)|\geq25,\qquad K_5\not\subseteq G.              \tag{1.2}
\]

Fix five independent degree-eight centres

\[
                         Z=\{z,z_1,z_2,z_3,z_4\}.      \tag{1.3}
\]

For every `w in Z`, use the choices in the audited five-centre common
matching theorem: an independent triple `I_w subseteq N_G(w)`, the
five-set

\[
                         R_w=N_G(w)-I_w,               \tag{1.4}
\]

a representative `x_w in R_w`, and the matching edge

\[
                         e_w=wx_w.                     \tag{1.5}
\]

The five edges

\[
                         M=\{e_w:w\in Z\}              \tag{1.6}
\]

form a matching.  For every nonempty `J subseteq M`, fix a proper
six-colouring `c_J` of `G-M` with equality signature exactly `J`.  When
all edges of `M` are restored, the only monochromatic edges under `c_J`
are the members of `J`.

For `J={e_z}`, choose the particular colouring supplied by the star
contraction at `z`; abbreviate it to `c_z`.  Its equality partition on

\[
                              S=N_G(z)                 \tag{1.7}
\]

has the exact shape

\[
                         I_z\mid\{r\}\ (r\in R_z),
\qquad                         3+1+1+1+1+1.           \tag{1.8}
\]

In the model-anchored application, also retain the exact spanning
`K_7^vee` model, its branch set containing `z`, the named branch set
anticomplete to `z`, and, when supplied by the anchored-hull reduction,
connectedness of the complement of `{z}` inside its containing branch
set.  None of those objects will be reselected below.

For an induced closed shore `L` with boundary `T`, write
`Part_6(L,T)` for the equality partitions of `T` induced by proper
six-colourings of `L`.

## 2. The full singleton boundary has disjoint block-count languages

### Lemma 2.1 (six blocks outside, at most five inside)

The two boundary languages at `S=N_G(z)` satisfy

\[
 \begin{aligned}
  \Pi\in\operatorname{Part}_6(G-z,S)
       &\Longrightarrow |\Pi|=6,\\
  \Pi\in\operatorname{Part}_6(G[N_G[z]],S)
       &\Longrightarrow |\Pi|\leq5.
 \end{aligned}                                        \tag{2.1}
\]

Consequently the two languages are disjoint.  In particular, a common
boundary partition cannot be the terminal mechanism at the singleton
centre.

#### Proof

Let `a` be a proper six-colouring of `G-z`.  If at most five colours
occurred on `S`, a missing colour could be assigned to `z`, producing a
proper six-colouring of `G`.  Thus all six colours occur on `S`, proving
the first line.

In every proper six-colouring of `G[N_G[z]]`, the colour of `z` is absent
from all of `S`, since `z` is adjacent to every member of `S`.  At most
five colours, and hence at most five equality blocks, occur on `S`.  This
proves the second line and disjointness. `\square`

The conclusion is stronger than the rejection of the one displayed
partition (1.8): it separates the complete shore languages.

## 3. The other four centre edges give an opposite response cube

Put

\[
                         M_z=M-\{e_z\}.                \tag{3.1}
\]

### Theorem 3.1 (opposite four-coordinate singleton interface)

For every nonempty `J subseteq M_z`, the restriction

\[
                         c_J|G[N_G[z]]                 \tag{3.2}
\]

is a proper six-colouring.  Let `Pi_J` be its equality partition on `S`.
Then

\[
 \Pi_J\in\operatorname{Part}_6(G[N_G[z]],S)
      -\operatorname{Part}_6(G-z,S).                  \tag{3.3}
\]

On the other hand, the canonical partition `Pi_z` induced by `c_z` obeys

\[
 \Pi_z\in\operatorname{Part}_6(G-z,S)
      -\operatorname{Part}_6(G[N_G[z]],S),            \tag{3.4}
\]

and has the exact shape (1.8).

Thus the exact order-eight boundary `S` retains the original coordinate
`e_z`, its fixed colouring `c_z`, and all fifteen nonempty operation
signatures on the other four centre edges, in the opposite shore
orientation.  The fifteen boundary partitions in (3.3) are operation
labelled; they are not asserted to be pairwise distinct.

#### Proof

Independence of `Z` gives

\[
                         Z-\{z\}\subseteq G-N_G[z].    \tag{3.5}
\]

After restoring `M`, every monochromatic edge under `c_J` belongs to `J`.
Every edge of `J subseteq M_z` has its centre end in `Z-{z}`, and hence
outside `N_G[z]` by (3.5).  Deleting those four possible centre ends
removes every monochromatic restored edge.  This proves that (3.2) is
proper.

If `Pi_J` also extended through `G-z`, permute the six colour names in
one of the two shore colourings to align their common equality partition
on the literal boundary `S`.  Gluing would give a proper six-colouring of
`G`, contrary to (1.1).  This proves (3.3).  It also follows directly from
Lemma 2.1, since `Pi_J` has at most five blocks.

The only monochromatic restored edge under `c_z` is `e_z`, and deleting
`z` removes it.  Hence `c_z|G-z` is proper.  Its boundary partition is
(1.8), so it has six blocks and Lemma 2.1 excludes it from the singleton
closed-shore language.  This proves (3.4). `\square`

Theorem 3.1 uses the complete punctured cube rather than four unrelated
centre-deletion colourings: for every nonempty subset of the four named
coordinates, the corresponding operation colouring occurs on the same
literal boundary and on the same singleton shore.

## 4. A square survives on one exterior component boundary

Let

\[
                         O=G-N_G[z].                  \tag{4.1}
\]

It is nonempty by (1.2).  The audited low-degree exterior-component theorem
gives at most two components of `O`.  Every member of `Z-{z}` lies in
`O`, so one component `C` contains at least two of the four other centres.
Put

\[
 W_C=(Z-\{z\})\cap V(C),\qquad
 M_C=\{e_w:w\in W_C\},\qquad
 T=N_G(C).                                             \tag{4.2}
\]

### Theorem 4.1 (component-localised opposite response square)

The boundary `T` is an actual separator and

\[
                         T\subseteq S,\qquad
                         7\leq|T|\leq8,
 \qquad                   |M_C|\geq2.                 \tag{4.3}
\]

The canonical colouring `c_z` is proper on the closed `C`-side
`G[C union T]`.  For every nonempty `J subseteq M_C`, the colouring
`c_J` is proper on the opposite closed shore `G-C`.  If `Pi_z^T` and
`Pi_J^T` denote their respective boundary partitions on `T`, then

\[
 \begin{aligned}
  \Pi_z^T&\in\operatorname{Part}_6(G[C\cup T],T)
              -\operatorname{Part}_6(G-C,T),\\
  \Pi_J^T&\in\operatorname{Part}_6(G-C,T)
              -\operatorname{Part}_6(G[C\cup T],T).  \tag{4.4}
 \end{aligned}
\]

In particular, one boundary of order seven or eight carries the original
coordinate and colouring in one orientation and at least the three
nonempty signatures of a two-coordinate response square in the other.

If `|T|=8`, then `Pi_z^T` has shape `3+1+1+1+1+1`.  If
`T=S-{t}`, then its shape is

\[
 \begin{cases}
  2+1+1+1+1+1,&t\in I_z,\\
  3+1+1+1+1,&t\in R_z.
 \end{cases}                                          \tag{4.5}
\]

Every `Pi_J^T` has at most five blocks.  Hence the displayed partitions
are separated automatically by block count unless `|T|=7` and the unique
missed vertex lies in `R_z`.

#### Proof

The component `C` has no neighbour outside `S`, because it is a component
of `G-N_G[z]`.  Thus `T subseteq S`.  Its boundary separates `C` from the
nonempty singleton `{z}`, so seven-connectivity gives `|T|>=7`; degree
eight gives the upper bound.  The low-degree component theorem and the
four centres in `O` give `|M_C|=|W_C|>=2`.

The edge `e_z=zx_z` has neither end in `C`: its centre end is `z`, while
`x_z in S`.  Hence the restriction of `c_z`, whose sole monochromatic
restored edge is `e_z`, is proper on `G[C union T]`.

Now let `emptyset ne J subseteq M_C`.  Every monochromatic restored edge
under `c_J` has its centre end in `C`.  Deleting `C` therefore removes all
of them, and `c_J|G-C` is proper.  If either partition in (4.4) extended
through the opposite shore, alignment on `T` and gluing would six-colour
`G`.  This proves (4.4).

The shapes in (4.5) are the restrictions of (1.8).  Finally, `z` belongs
to `G-C`, every edge at `z` is proper under `c_J` because `e_z notin J`,
and consequently the colour of `z` is absent from `T subseteq N_G(z)`.
Thus `Pi_J^T` has at most five blocks. `\square`

### Corollary 4.2 (exact bounded return at a terminal centre)

Suppose the centre-preserving model-anchored descent terminates at
`{z}`.  Then, without changing the exact `K_7^vee` model or any of its
labels, one obtains both:

1. the exact order-eight opposite four-coordinate interface of
   Theorem 3.1; and
2. an actual order-seven or order-eight interface of Theorem 4.1 retaining
   `e_z,c_z` and at least two further original centre coordinates.

If the containing branch-set complement was connected and a named far bag
was retained before reaching `{z}`, those facts remain literally true:
the construction changes no branch set and no vertex of the model.

#### Proof

The singleton has boundary `N_G(z)` of order eight because `d_G(z)=8`.
Apply Theorems 3.1 and 4.1.  They only restrict already fixed colourings to
induced shores and do not modify the model. `\square`

## 5. Exact gain and first unsupported inference

Corollary 4.2 proves the bounded multi-coordinate outcome sought from a
terminal degree-eight centre.  In particular, the full punctured response
cube does not collapse to a lone fixed-edge trace at this singleton: the
other four actual centres place a four-coordinate family on the original
boundary, and at least a two-coordinate family on one component boundary.

It does **not** eliminate the singleton.  There are two precise reasons.

1. Lemma 2.1 proves that the original singleton boundary can never be
   closed by a common partition: the exterior language has six blocks and
   the singleton language has at most five.
2. The operation signatures in Theorems 3.1 and 4.1 need not be visible in
   the equality partition of the boundary.  Several or all of the
   operation-labelled colourings may induce the same boundary partition,
   and no palette colour is thereby identified with a branch-set label of
   the fixed exact model.

Thus the inference

\[
 \begin{gathered}
  \text{an exact model-anchored degree-eight centre, the canonical
  six-block response,}\\
  \text{and an opposite punctured response cube on an order-seven/eight
  boundary}
 \end{gathered}
 \Longrightarrow
 \begin{gathered}
  K_7^-\npreccurlyeq G,\quad\text{or a strict labelled model split}
 \end{gathered}                                       \tag{5.1}
\]

is the first unsupported step.  This is a route nonclosure, not a
counterexample to (5.1).  A positive continuation must use the exact-model
contacts to turn at least one of the operation labels into a branch-set
allocation, or must turn the component interface of Theorem 4.1 into a
non-singleton response side.  Further comparison of boundary palettes
alone cannot close the full singleton boundary.

## Dependencies and scope

- [five-centre common matching and its punctured response cube](../results/hc7_k7minus_five_centre_common_matching_reduction.md);
- [centre-preserving exact-model visibility](hc7_k7minus_five_centre_model_anchored_visibility.md);
- [the low-degree exterior-component bound](../results/hc7_low_degree_exterior_component_bounds.md); and
- [the model-anchored response hull](../results/hc7_k7minus_model_anchored_response_hull.md).

The proof is unbounded and computation-free.  It closes the side-order
descent at a singleton centre by a fully labelled bounded interface, not by
an explicit forbidden minor.  It does not terminalise the resulting
order-seven/eight model-allocation problem or prove Conjecture 21 or
`HC_7`.
