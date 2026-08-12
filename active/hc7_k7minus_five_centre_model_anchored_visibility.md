# Centre-preserving visibility in an exact `K_7^vee` model

**Status:** written proof; internal self-audit adjacent.  This is a
conditional reduction in the critical host.  It does not prove the
`K_7^-` six-colour conjecture or `HC_7`.

The endpoint-visibility argument can be strengthened for the original
five-centre matching.  One should maximise visibility of the five degree-
eight centres themselves, rather than visibility of all ten matching
endpoints.  The branch-set transfer then either exposes a response side
which still contains the nominated centre or strictly increases that
centre score.  At a maximum, two centres in one universal bag can be fed
as the two prescribed portals into the exact near-clique dichotomy, which
returns a side containing one of those same literal centres.

Consequently the model-anchored response reduction may start with an
original centre edge and a side containing its degree-eight centre.  The
subsequent fixed-coordinate core and anchored-hull reductions preserve that
centre.

## 1. Setting and direct centre responses

Let `G` satisfy

\[
 \chi(G)=7,\qquad
 \chi(J)\le6\text{ for every proper minor }J\text{ of }G,
 \qquad \kappa(G)\ge7,
 \qquad K_7^-\npreccurlyeq G.                       \tag{1.1}
\]

Fix five independent degree-eight vertices

\[
                         Z=\{z_1,\ldots,z_5\}.       \tag{1.2}
\]

Use the matching and common colouring host supplied by the audited
[five-centre common-matching theorem](../results/hc7_k7minus_five_centre_common_matching_reduction.md):

\[
 M=\{e_z=zx_z:z\in Z\},\qquad H=G-M.                \tag{1.3}
\]

The edges in `M` form a matching.  For every `z in Z`, fix a proper
six-colouring `c_z` of `H` whose matching signature is exactly `{e_z}`.
After the other four matching edges are restored, `c_z` is a proper
six-colouring of `G-e_z`.

Let

\[
                         P,B,C,U_1,U_2,U_3,U_4       \tag{1.4}
\]

be a spanning exact `K_7^vee`-minor model in `G`: the six bags
`B,C,U_1,...,U_4` form a `K_6` model, `P` is anticomplete to `B,C`, and
`P` is adjacent to every `U_i`.

### Lemma 1.1 (literal centre response)

If a nonempty proper connected set `Y` contains `z in Z` and some nonempty
set `D` is disjoint from `Y` and anticomplete to it, then `N_G(Y)` is an
actual separator and `c_z|G-Y` is proper.  Its equality partition on
`N_G(Y)` is rejected by the intact closed `Y`-side.  In particular,

\[
                             |N_G(Y)|\ge7.            \tag{1.5}
\]

#### Proof

After restoration of `M`, the only monochromatic edge under `c_z` is
`e_z`.  Deleting `Y` removes its centre end `z`, so the exterior
restriction is proper.  If the same boundary partition extended through
`G[Y union N_G(Y)]`, a permutation of the six colours would align the two
boundary colourings and glue them to a six-colouring of `G`.

The nonempty anticomplete set `D` lies outside `N_G[Y]`, so the boundary is
actual.  Seven-connectivity gives (1.5). `\square`

For an exact model `mathcal M` as in (1.4), define its **centre-visibility
score** by

\[
               s_Z(\mathcal M)
                 =|(P\cup N_G(P))\cap Z|.            \tag{1.6}
\]

Centres already absorbed into `P` remain visible.  This is essential for
monotonicity under the transfer below.

## 2. A centre-preserving endpoint transfer

For `A subseteq U_i`, let

\[
 \Omega_i(A)=\{D\in\{B,C,U_j:j\ne i\}:
                         E_G(U_i-A,D)=\varnothing\}. \tag{2.1}
\]

Thus `Omega_i(A)` is exactly the set of foreign adjacencies which would be
lost by replacing `U_i` with `U_i-A`.

### Theorem 2.1 (centre-visibility transfer)

Let `z in Z cap U_i` and suppose that `z notin N_G(P)`.  Then at least one
of the following holds.

1. `G` contains a `K_7^-` minor.
2. There are a nonempty proper connected set `Y subset U_i` and a named
   foreign branch set `D` such that

   \[
       z\in Y,\qquad U_i-Y\text{ is connected},
       \qquad E_G(Y,D)=\varnothing.                  \tag{2.2}
   \]

   The same edge `e_z` and colouring `c_z` give the rejected actual
   response of Lemma 1.1 on `Y`.
3. There is another spanning exact `K_7^vee` model `mathcal M'` with

   \[
                         s_Z(\mathcal M')
                               >s_Z(\mathcal M).      \tag{2.3}
   \]

#### Proof

Write `U=U_i`.  Choose `q in U cap N_G(P)`.  In a spanning tree of `G[U]`
containing a fixed `q`--`z` path, delete the path edge `xz` incident with
`z`.  Let `A` be the resulting connected vertex set containing `q` and
put

\[
                              W=U-A.                  \tag{2.4}
\]

Then `A,W` are nonempty and connected, `z in W`, and `xz` joins them.

If `Omega_i(A)` is nonempty, choose `D in Omega_i(A)`.  The definition
gives `E_G(W,D)=empty`.  Taking `Y=W`, equation (2.2) holds, and Lemma 1.1
attaches the original centre-edge response.  This is outcome 2.

Assume now that `Omega_i(A)=empty`.  Replace `P,U` by

\[
                              P'=P\cup A,
                     \qquad U'=W.                    \tag{2.5}
\]

The set `P'` is connected through a `P`--`q` edge, `U'` is connected, and
`xz` joins the two new bags.  The empty monopoly set says that `U'`
retains all five foreign adjacencies.  All other required adjacencies are
unchanged.  If `A` meets `B` or `C`, the seven new bags miss at most the
other one of `P'B,P'C`, and hence form an explicit `K_7^-` model.

Otherwise `A` is anticomplete to both `B,C`, and (2.5) is another spanning
exact `K_7^vee` model.  No centre counted by the old score is lost:
centres in `P` remain in `P'`, and every centre outside `P'` adjacent to
old `P` is still adjacent to the subset `P subseteq P'`.  Any centre in
`A` is now counted inside `P'`.  The nominated centre `z` was not counted
before, but `z in U'` is adjacent to `x in P'`.  It is counted after the
transfer.  Thus (2.3) holds.

Unlike the all-endpoint transfer, this proof does not stop when `A`
contains a noncentre endpoint `x_w`.  Such an endpoint is irrelevant to
the score in (1.6), and the centre `z` still gives the strict increase.
`\square`

## 3. Maximal visibility and two-centre capture

### Theorem 3.1 (five-centre model-anchored visibility)

Under the hypotheses of Section 1, at least one of the following holds.

1. `G` contains a `K_7^-` minor.
2. Some centre `z` lies in one of `P,B,C`.  The singleton `{z}` has the
   exact order-eight response boundary `N_G(z)`, retains the edge `e_z`
   and colouring `c_z`, and has a named anticomplete branch set: take `B`
   when `z in P`, and take `P` when `z in B union C`.
3. There are a centre `z`, a universal branch set `U_i`, a nonempty proper
   connected set `Y subset U_i`, and a named foreign branch set `D` such
   that

   \[
       z\in Y,\qquad U_i-Y\text{ is connected},
       \qquad E_G(Y,D)=\varnothing.                  \tag{3.1}
   \]

   The fixed centre edge `e_z` and singleton-signature colouring `c_z`
   give a rejected exterior trace on this actual model-anchored side.

#### Proof

Among all spanning exact models of the form (1.4), choose one maximising
`s_Z`.  If a centre lies in `P,B` or `C`, exactness supplies the named far
bag stated in outcome 2.  Lemma 1.1 applied to `{z}` gives the fixed
response, and `d_G(z)=8` makes its boundary have order eight.

We may therefore assume

\[
                              Z\subseteq
                       U_1\cup U_2\cup U_3\cup U_4.  \tag{3.2}
\]

If a centre `z in U_i` is not adjacent to `P`, Theorem 2.1 gives the
target, outcome 3, or a model with strictly larger centre score.  The last
possibility contradicts maximality.  Hence every centre is a literal
`P`-neighbour in its universal branch set.

Five centres lie in four universal bags, so one bag `U_i` contains two
distinct centres

\[
                         p,q\in N_G(P)\cap U_i.       \tag{3.3}
\]

Rerun the audited exact-`K_7^vee` separator dichotomy with `p,q` as its two
prescribed portals.  In its retaining-core case, the returned component
contains the nominated portal avoided by the core.  In its opposite-gate
case, the two gates contain `p,q` separately.  Whenever a returned set
misses one of `B,C`, that twin is a named far branch set and (3.1) holds.
If no such set misses a twin, the branch-set transfer in the dichotomy
constructs a `K_7^-` minor.  Thus the separator alternative contains one
of the same literal centres `p,q`, and Lemma 1.1 attaches that centre's
original matching-edge response. `\square`

### Corollary 3.2 (the centre survives anchored reduction)

In outcome 3 of Theorem 3.1, apply the fixed-coordinate list-critical core
reduction and the model-anchored hull reduction while retaining `e_z,c_z`,
the containing bag `U_i` and the named far bag `D`.  Every resulting
list-critical core and every anchored hull contains `z`.  Consequently the
entire well-founded anchored reduction preserves the same degree-eight
centre, not merely an unspecified endpoint of a selected edge.

#### Proof

The side contains `z`, which is one end of `e_z`.  If `x_z` is outside the
side, the rooted list-critical core theorem forces its unique contained end
`z` into the core.  If `x_z` also lies in the side, that theorem forces both
ends into the core.  The anchored hull contains the core.  The same
argument applies at every subsequent step. `\square`

## 4. Exact scope

Theorem 3.1 repairs the endpoint-label issue: the response side in the
universal-bag outcome contains a degree-eight centre, and the operation is
its original edge in the five-centre matching.  Corollary 3.2 shows that
the existing list-critical and anchored-hull descents cannot discard that
centre.

The theorem does not itself prove that `U_i-z` is connected.  Thus one
cannot automatically replace the model-anchored side by the singleton
`{z}` while retaining a connected complement inside `U_i`.  The singleton
still has its exact order-eight response boundary, but that separate move
may lose the branch-set split.  Nor does the theorem terminalise the
resulting order-eight boundary, produce a compatible boundary partition,
or construct the forbidden minor in every case.

The degree-eight hypothesis is used in the exact bounded conclusion of
outcome 2 and remains available throughout outcome 3.  It is not needed
for the score monotonicity itself.

## Dependencies

- [the common five-centre matching and its singleton signatures](../results/hc7_k7minus_five_centre_common_matching_reduction.md);
- [the exact spanning near-clique separator dichotomy](../results/hc7_k7minus_exact_k7vee_separator_dichotomy.md);
- [fixed-coordinate response-core reduction](../results/hc7_k7minus_fixed_coordinate_response_core_reduction.md); and
- [the model-anchored response hull](../results/hc7_k7minus_model_anchored_response_hull.md).
