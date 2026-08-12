# Endpoint visibility in the eight-coordinate exact model

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_eight_coordinate_endpoint_visibility_audit.md).
This is a conditional reduction inside a hypothetical critical host.  It
does not prove the `K_7^-` six-colour conjecture or `HC_7`.

## 1. Setting

Let `G` be seven-connected, seven-chromatic, and minor-minimal subject to
not being six-colourable, and suppose that `K_7^-` is not a minor of `G`.
Let `F_8` be the eight-edge componentwise-induced forest supplied by the
audited forced-growth corollary, and put

\[
                              H=G-F_8.                \tag{1.1}
\]

Thus `H` is seven-connected and its proper six-colourings realise precisely
the nonempty equality signatures on `F_8`.  Retain a spanning exact
`K_7^\vee`-minor model

\[
                       P,B,C,U_1,U_2,U_3,U_4,          \tag{1.2}
\]

where `B,C,U_1,...,U_4` form a `K_6`-minor model, `P` is anticomplete to
`B,C`, and `P` is adjacent to every `U_i`.  Exactness means that `P`
remains anticomplete to `B,C` after all edges of `F_8` are restored.

A proper six-colouring of `G-Y` gives a **rejected exterior trace on `Y`**
when its equality partition on `N_G(Y)` is not induced by any proper
six-colouring of `G[Y\cup N_G(Y)]`.

For an exact model as in (1.2), define its **endpoint-visibility score** by

\[
            s(P)=\bigl|(P\cup N_G(P))\cap V(F_8)\bigr|. \tag{1.3}
\]

The inclusion of endpoints already in `P` is essential.  Moving an old
endpoint portal into `P` need not increase the number of endpoints in
`N_G(P)`, but it does not decrease (1.3).

## 2. Direct coordinate traces

### Lemma 2.1 (singleton-coordinate trace)

Every nonempty proper vertex set `Y` satisfying

\[
                         Y\cap V(F_8)\ne\varnothing    \tag{2.1}
\]

carries a rejected exterior trace obtained from a singleton signature on
`F_8`.

#### Proof

Choose an endpoint `v in Y` of an edge `e in F_8`.  The full punctured
signature cube supplies a proper six-colouring `c` of `H` in which `e` is
the unique edge of `F_8` with equal-coloured ends.  After restoring `F_8`,
the only monochromatic edge is therefore `e`.  Since deleting `Y` removes
the endpoint `v`, the restriction of `c` to `G-Y` is proper.

If its equality partition on `N_G(Y)` extended through
`G[Y union N_G(Y)]`, a permutation of colour names would align the two
boundary colourings.  Gluing them would give a proper six-colouring of
`G`, a contradiction.  Hence the exterior trace is rejected. `\square`

## 3. Moving an endpoint towards the deficient branch set

For a universal branch set `U=U_i`, call the other five members of the
`K_6` model

\[
                    B,C,U_j\quad(j\ne i)              \tag{3.1}
\]

its **foreign branch sets**.  For `A subseteq U`, put

\[
 \Omega_U(A)=\{D\text{ in (3.1)}:
                 E_G(U-A,D)=\varnothing\}.            \tag{3.2}
\]

Thus `Omega_U(A)` records precisely the foreign adjacencies monopolised by
`A`.

### Theorem 3.1 (endpoint-visibility transfer)

Let `v in U_i cap V(F_8)` and suppose

\[
                              v\notin N_G(P).           \tag{3.3}
\]

Then at least one of the following holds.

1. `G` contains a `K_7^-` minor.
2. There is a nonempty proper connected set `Y` meeting `V(F_8)` such that
   `N_G(Y)` is an actual separator.  It has order at least seven and `Y`
   carries a rejected exterior trace from a singleton `F_8` signature.
3. There is another spanning exact `K_7^vee` model whose deficient branch
   set `P'` satisfies

   \[
                              s(P')>s(P).              \tag{3.4}
   \]

#### Proof

Write `U=U_i`.  Choose a vertex `q in U cap N_G(P)`, which exists because
`P` and `U` are adjacent branch sets.  Take a spanning tree `T` of `G[U]`
and, if necessary, replace it by a spanning tree containing a fixed
`q`--`v` path.  Let `xv` be the edge of that path incident with `v`.
Deleting `xv` from `T` gives two connected vertex sets.  Let `A` be the
one containing `q` and put

\[
                              W=U-A.                   \tag{3.5}
\]

Then `A,W` are nonempty and connected, `v in W`, and `xv` is an edge
between them.

Suppose first that `Omega_U(A)` is nonempty.  For every
`D in Omega_U(A)`, the connected set `W` is anticomplete to the nonempty
connected branch set `D`.  Hence `N_G(W)` is an actual separator, with
`W` on one side and `D` on another.  Seven-connectivity gives
`|N_G(W)|>=7`.  Since `v in W cap V(F_8)`, Lemma 2.1 attaches the original
singleton-coordinate rejected trace.  This is outcome 2.

We may therefore assume

\[
                              \Omega_U(A)=\varnothing. \tag{3.6}
\]

Replace `P,U` by

\[
                              P'=P\cup A,
                       \qquad U'=W.                    \tag{3.7}
\]

The set `P'` is connected through the `Pq` edge, `U'` is connected, and
the edge `xv` joins them.  Equation (3.6) says that `U'` retains an edge
to every foreign branch set.  All other adjacencies in the foreign
`K_6` model are unchanged.  The old set `P` retains its edges to the
three universal branch sets other than `U`.

  If `A` is adjacent to `B` or `C`, the seven sets after (3.7) have at most one
missing adjacency and give a `K_7^-` model.  We may therefore suppose
that `A` is anticomplete to both `B,C`.  Then the sets after (3.7) form
another spanning exact `K_7^vee` model, with the same two missing pairs
`P'B,P'C`.

If `A` contains an endpoint of `F_8`, then `P'` carries a singleton-
coordinate rejected trace by Lemma 2.1.  Moreover `P'` is anticomplete to
the nonempty branch set `B`, so `N_G(P')` is an actual separator; its order
is at least seven.  This is outcome 2.

It remains that `A cap V(F_8)=empty`.  Every endpoint counted by `s(P)`
is still counted by `s(P')`: endpoints in `P` remain in `P'`, while every
endpoint outside `P'` adjacent to `P` remains adjacent to the subset
`P subseteq P'`.  The endpoint `v` was not counted by `s(P)` under (3.3),
but the edge `xv`, with `x in P'`, makes it a member of `N_G(P')`.
Therefore (3.4) holds, giving outcome 3. `\square`

### Remark 3.2 (why literal portal count is not monotone)

The score in (1.3) cannot in general be replaced by
`|N_G(P) cap V(F_8)|`.  If the only old `P`--`U` portal is itself a
coordinate endpoint, the transfer may absorb that endpoint into `P'` and
expose `v` as the new endpoint portal.  The literal portal count then stays
constant.  Endpoint visibility strictly increases because the absorbed
endpoint remains counted inside `P'`.

## 4. Two endpoint portals in one universal branch set

### Theorem 4.1 (endpoint-support capture)

Suppose that for some `i` the universal branch set `U_i` contains two
distinct vertices

\[
                  p,q\in N_G(P)\cap U_i\cap V(F_8).   \tag{4.1}
\]

Then either `G` contains a `K_7^-` minor, or there is a nonempty proper
connected set `Y subset U_i` such that `U_i-Y` is connected,
`N_G(Y)` is an actual separator of order at least seven, `Y` contains
`p` or `q`, and `Y` carries a singleton-coordinate rejected exterior
trace.  If `|N_G(Y)|=7`, every component of `G-N_G(Y)` is adjacent to
every vertex of `N_G(Y)`.

#### Proof

Apply the audited exact-`K_7^vee` separator dichotomy to (1.2), using
`p,q` as its two selected neighbours of `P` in `U_i`.  Its retaining-core
and opposite-gate proof has the following labelled form: either its
branch-set transfer constructs a `K_7^-` model, or the connected set
returned inside `U_i` contains one of the two selected vertices.  In the
latter case its complement in `U_i` is connected and its open
neighbourhood is an actual separator of order at least seven.  Lemma 2.1
attaches a singleton-coordinate rejected trace.  The order-seven fullness
statement is the final conclusion of the same dichotomy. `\square`

## 5. The eight-coordinate consequence

### Theorem 5.1 (target or original-coordinate response separation)

In the setting of Section 1, either `G` contains a `K_7^-` minor, or there
is a nonempty proper connected set `Y` meeting `V(F_8)` such that
`N_G(Y)` is an actual separator of order at least seven and `Y` carries a
rejected exterior trace from a singleton `F_8` signature.

#### Proof

Among all spanning exact models of the form (1.2), choose one maximising
`s(P)`.  Such a choice exists because `G` is finite.

If one of `P,B,C` meets `V(F_8)`, use that branch set as `Y`.  It is
connected and carries a singleton-coordinate trace by Lemma 2.1.  Its open
neighbourhood is an actual separator: `P` is anticomplete to each of
`B,C`, while each of `B,C` is anticomplete to `P`.  Seven-connectivity
gives the boundary lower bound.

We may therefore suppose that all coordinate endpoints lie in
`U_1 union ... union U_4`.  If an endpoint `v in U_i` is not adjacent to
`P`, Theorem 3.1 gives the target, the required separator, or another
exact model with a larger score.  The last outcome contradicts the choice
of the model.  Hence every coordinate endpoint in every `U_i` is adjacent
to `P`.

The forest `F_8` has sixteen vertices when it is a matching and fifteen
vertices when its only nonsingle-edge component is an induced `P_3`.
Four universal branch sets therefore cannot each contain at most one
coordinate endpoint.  Some `U_i` contains two endpoint portals, and
Theorem 4.1 gives the target or the required response-bearing separator.
`\square`

### Corollary 5.2 (bounded response separation)

In the setting of Section 1, either `G` contains a `K_7^-` minor, or there
is a nonempty proper connected set `Z` such that `N_G(Z)` is an actual
separator,

\[
                         7\le |N_G(Z)|\le9,             \tag{5.1}
\]

and a proper six-colouring of an edge-deleted proper minor induces on
`N_G(Z)` a boundary partition which extends through `G-Z` and is rejected
by the intact closed `Z`-side.

If the separator supplied by Theorem 5.1 already has order at most nine,
the trace retains its original `F_8` coordinate.  Otherwise the bounded
trace in this corollary may come from a fresh edge deletion and need not
retain the forest or model labels.

#### Proof

Apply Theorem 5.1.  There is nothing to prove if it gives the target or a
response separator of order at most nine.  Starting from a response
separator of order at least ten, apply the audited large actual-boundary
singleton descent and iterate.  Every step strictly lowers the positive
integer boundary order and produces an actual singleton-side response;
the iteration therefore stops at order seven, eight or nine. `\square`

## 6. Scope and first remaining obstruction

Theorem 5.1 is unbounded and uses no finite enumeration.  It makes the
forced eight-coordinate exact-model case produce one separator retaining
a literal coordinate and its singleton-signature colouring data.  That
coordinate-preserving result does not control the separator order beyond
the lower bound

\[
                              |N_G(Y)|\ge7.             \tag{6.1}
\]

This is the exact first unsupported label-preserving strengthening.
Seven-connectivity provides (6.1), not an upper bound.  Neither spanning
of the exact model nor the punctured signature cube bounds the number of
neighbours that the transferred connected set may have in the six other
branch sets.  Corollary 5.2 bounds the interface numerically, but it may
spend a fresh singleton operation and lose the coordinate and model labels
just preserved.

The remaining theorem must therefore terminalise the generic order-seven,
order-eight and order-nine response interfaces, or compress the
original-coordinate separator while retaining enough of its colouring and
model data to do so.  Static contact quotients do not encode that
information.

## Dependencies

The forced eight-coordinate host is Corollary 2 of
[`hc7_k7minus_bounded_feedback_degree_elimination.md`](../results/hc7_k7minus_bounded_feedback_degree_elimination.md).
The labelled branch-set argument used in Theorem 4.1 is
[`hc7_k7minus_exact_k7vee_separator_dichotomy.md`](../results/hc7_k7minus_exact_k7vee_separator_dichotomy.md).
The numerical response compression in Corollary 5.2 is Theorem 2.1 and
Corollary 2.2 of
[`hc7_k7minus_matching_lock_boundary_reduction.md`](../results/hc7_k7minus_matching_lock_boundary_reduction.md).
