# Owner circuits at a model-anchored response appendage

**Status:** written proof; internal self-audit adjacent; and recorded route
nonclosure.  This conditional theorem does not prove the `K_7^-`
six-colour conjecture or `HC_7`.

The model-anchored terminal form has at most two coordinate-free appendages,
each monopolising at least two labelled adjacencies of its containing branch
set.  A simultaneous linkage from those labelled contacts to the retained
part of the branch set would remove the appendage while preserving the fixed
forest-coordinate response.  Consequently every surviving appendage has a
small Rado--Menger owner circuit.  The circuit produces either two
owner-labelled edge responses at one vertex, an actual response side, or two
separately model-persistent edge responses.

The theorem also identifies the precise limitation of this reduction.  The
model used in the global anchored minimum need not span the host.  Neighbours
outside its seven branch sets prevent the circuit separator from having a
bounded full host boundary.  Moreover, visibility of both ends of the fixed
coordinate cannot repair an adjacency monopolised by the appendage.

## 1. Setting

Use a globally minimum anchored response configuration from
[the model-ownership theorem](../results/hc7_k7minus_model_anchored_appendage_ownership.md).
Thus `G` is a minor-minimal non-six-colourable graph, every proper minor of
`G` is six-colourable, `G` is seven-connected, and it has a labelled exact
`K_7^vee`-minor model

\[
                  P,B,C,U_1,U_2,U_3,U_4.              \tag{1.1}
\]

Let `R` be the universal branch set containing the terminal side `Z`, let
`D` be a named foreign branch set anticomplete to `Z`, and let

\[
                  Z=K\mathbin{\dot\cup}A_1
                       \mathbin{\dot\cup}\cdots
                       \mathbin{\dot\cup}A_t,
                  \qquad 0\le t\le2,                 \tag{1.2}
\]

be its terminal decomposition.  Here `K` is boundary-list-critical for the
singleton-signature colouring `c_e` of one fixed edge `e in F_8`.  It
contains every end of `e` which lies in `Z`.  Each appendage is connected,
is disjoint from `V(F_8)`, and is a component of `G[R-K]`.

Fix one appendage `A`.  Put

\[
        R_0=R-A,
        \qquad B_A=N_G(R_0)\cap A.                    \tag{1.3}
\]

Both `R_0` and `B_A` are nonempty and `G[R_0]` is connected.  Let
`Lambda(A)` be the model-monopoly set of `A`, as in the cited theorem.  For
each `Q in Lambda(A)`, put

\[
                       A_Q=N_G(Q)\cap A.               \tag{1.4}
\]

Every `A_Q` is nonempty, and

\[
                       2\le |\Lambda(A)|\le5.          \tag{1.5}
\]

The upper bound uses the fact that the far label `D` does not belong to
`Lambda(A)`.

Let `U_0` denote the set of vertices which lie in none of the seven branch
sets in (1.1).  It may be nonempty because the anchored minimisation uses
ordinary, not necessarily spanning, minor models.

## 2. A full owner linkage removes the appendage

### Theorem 2.1 (model-anchored multi-owner transfer)

Suppose that `G[A]` contains pairwise vertex-disjoint paths

\[
                         (P_Q:Q\in\Lambda(A))          \tag{2.1}
\]

such that `P_Q` has one end in `A_Q` and its other end in `B_A`.  Trivial
paths are allowed.  Then either `G` contains a `K_7^-` minor or there is an
anchored response configuration with the same edge `e`, colouring `c_e`,
far label `D` and list-critical core `K`, but with the strictly smaller side
`Z-A`.  In particular, (2.1) is impossible in the globally minimum
target-free configuration.

#### Proof

Let `L_Q` initially be the vertex set of `P_Q`.  Every component of

\[
                 G\left[A-\bigcup_QV(P_Q)\right]
\]

has an edge to at least one path, because `G[A]` is connected.  Assign each
such component to one adjacent path.  The resulting sets `(L_Q)` partition
`A`; they are nonempty and connected, and each meets both `A_Q` and `B_A`.

Replace the branch sets by

\[
               R'=R-A,
       \qquad Q'=Q\cup L_Q\quad(Q\in\Lambda(A)),       \tag{2.2}
\]

and leave every other branch set unchanged.  Each `Q'` is connected through
its `A_Q` end.  Its `B_A` end gives an edge to `R'`.  Thus (2.2) restores
every adjacency which `A` monopolised.  Every non-monopolised adjacency of
`R` already has an end in `R'`, and enlarging the owner bags destroys no
other model adjacency.  The branch sets remain pairwise disjoint; vertices
of `U_0` remain unused.

The only absent pairs in the original exact model are `PB` and `PC`.  If
the transfer creates either adjacency, the seven displayed sets miss at
most the other one and give an explicit `K_7^-` model.  Otherwise they are
another exact `K_7^vee` model.

The label `D` is not an owner, so it is unchanged and remains anticomplete
to `Z-A`.  The sets `R-A` and `Z-A` are connected, and

\[
                         (R-A)-(Z-A)=R-Z               \tag{2.3}
\]

is connected.  The core `K` remains inside `Z-A` and contains the required
end or ends of `e`.  Its new boundary lists under the same colouring `c_e`
are no larger than its old lists, so it remains list-uncolourable.  Hence
the fixed exterior trace is still rejected on the strictly smaller side
`Z-A`.  This is the second outcome. `\square`

This is a specialisation of the labelled portal-linkage transfer principle
to an exact `K_7^vee` model.  The new points needed here are preservation of
the fixed `F_8` coordinate and list-critical core, allowance for an
ordinary nonspanning model, and the `K_7^-` conclusion when one of the two
exactly missing adjacencies appears.

## 3. The owner circuit

For `I subseteq Lambda(A)`, put `A_I=bigcup_{Q in I}A_Q` and let `r(I)` be
the maximum number of pairwise vertex-disjoint paths in `G[A]` from distinct
vertices of `B_A` to distinct vertices of `A_I`.  Endpoint intersections
and trivial paths are allowed in the standard strict-gammoid convention.

### Theorem 3.1 (Rado--Menger owner circuit)

In the globally minimum target-free configuration there are an
inclusion-minimal set `I subseteq Lambda(A)` and a set `S subseteq A` such
that

\[
              2\le |I|\le5,
       \qquad r(I)=|I|-1,
       \qquad |S|=|I|-1,                              \tag{3.1}
\]

and `S` meets every path in `G[A]` from `B_A` to

\[
                         A_I=\bigcup_{Q\in I}A_Q.      \tag{3.2}
\]

Every proper subfamily of `I` has its full labelled linkage.

#### Proof

The vertex sets linkable by disjoint paths to distinct vertices of `B_A`
form a strict gammoid.  Rado's independent-transversal theorem says that
the full linkage in Theorem 2.1 exists exactly when

\[
                              r(J)\ge |J|              \tag{3.3}
\]

for every `J subseteq Lambda(A)`.  Theorem 2.1 excludes that linkage, so
choose `I` inclusion-minimal subject to failure of (3.3).  A singleton is
not deficient because `G[A]` is connected and `A_Q,B_A` are nonempty.
For every `Q in I`, minimality and monotonicity give

\[
                    |I|-1\le r(I-\{Q\})\le r(I)<|I|.
\]

Thus `r(I)=|I|-1`, and every proper subfamily satisfies all the Rado
inequalities.  Vertex Menger, with endpoints permitted in the separator,
supplies `S` of order `r(I)` meeting every `B_A`--`A_I` path. `\square`

### Theorem 3.2 (operation-sensitive circuit outcomes)

For `I,S` as in Theorem 3.1, at least one of the following holds.

1. **Concentrated owner responses.**  There are distinct labels
   `Q_1,Q_2 in I`, a vertex `s in S`, and edges

   \[
                         sq_1,\ sq_2,
                  \qquad q_i\in Q_i.                  \tag{3.4}
   \]

   Each edge deletion gives a rejected response on the actual singleton
   side `{s}`.  For each edge in (3.4), comparison with the fixed
   coordinate `e` gives the exact three signatures `EP,PE,EE` on their
   common deletion.
2. **A component response.**  There is a nonempty connected component
   `C` of `G[A-S]` such that

   \[
       N_G(C)\cap R\subseteq S,
       \qquad D\cap N_G(C)=\varnothing,                \tag{3.5}
   \]

   and an edge `g=cs`, with `c in C` and `s in S`.  The common deletion
   `G-{e,g}` has exactly the signatures `EP,PE,EE`.  Its `PE` colouring
   gives a rejected exterior trace on the actual side `C`.  If

   \[
                              V(e)\not\subseteq N_G(C), \tag{3.6}
   \]

   then an `EP` colouring is proper on the intact closed `C`-side, and its
   boundary-partition language is disjoint from the nonempty `PE` exterior
   language unless `G` is six-colourable.
3. **Repeated model contact.**  There is a component `C` satisfying
   (3.5), a named branch set `Q ne R,D`, and distinct vertices `x,y in Q`
   adjacent to `C`.  Choosing one `C-Q` edge at each of `x,y` gives two
   edge operations which are separately persistent for the original exact
   model and which each give a rejected exterior trace on `C`.

In outcomes 2 and 3, `N_G(C)` is an actual separator and

\[
  7\le |N_G(C)|
     \le |I|+4+|N_G(C)\cap U_0|\le9+|N_G(C)\cap U_0|                 \tag{3.7}
\]

whenever outcome 3 does not occur.  Thus a spanning anchored model would
return an actual response boundary of order seven, eight or nine.

#### Proof

Suppose first that `A_I subseteq S`.  Choose one portal in `A_Q` for every
`Q in I`.  There are `|I|` chosen occurrences in the set `S` of order
`|I|-1`; hence two distinct owner labels have a common chosen vertex `s`.
This gives (3.4).  The far bag `D` is anticomplete to `s`, so `N_G(s)` is
an actual boundary.  A colouring of either edge-deleted proper minor makes
its ends equal and restricts properly outside `{s}`; an extension through
the singleton side would six-colour `G`.  The vertex `s` is not a forest
endpoint.  Nor can an end of `e` lie in either owner bag: the end of `e`
in the fixed core belongs to `R-A`, so `e` would itself be an
`(R-A)`--owner contact, contrary to ownership.  Thus both edges in (3.4)
are disjoint from `e`.  Contraction of each disjoint pair supplies `EE`,
the two single-edge colourings supply `EP` and `PE`, and `PP` would colour
`G`.  This proves outcome 1.

Now suppose `A_I` is not contained in `S`.  Let `C` be a component of
`G[A-S]` meeting `A_I-S`.  It contains no vertex of `B_A-S`, since a path
inside `C` would avoid the transversal `S`.  By (1.3), `C` is therefore
anticomplete to `R-A`.  Its neighbours inside `A` lie in `S`, proving the
first part of (3.5); the second follows from the choice of the far bag.
Connectivity of `G[A]` supplies an edge `g=cs` as stated.

The edges `e,g` are disjoint.  The singleton-signature colouring of `G-e`
gives `EP`, and a colouring of `G-g` gives `PE`.  A six-colouring after
contracting both disjoint edges expands to `EE`, while `PP` would colour
`G`; these are exactly the three signatures.  In a `PE` colouring, deleting
`C` removes the sole monochromatic edge `g`, so the exterior restriction is
proper and its trace is rejected by gluing.  In an `EP` colouring, the
closed `C`-side is proper exactly when it does not contain both ends of
`e`, which is (3.6).  A common partition from that closed-side language and
the `PE` exterior language would glue to a six-colouring of `G`.  This
proves all the response assertions in outcome 2 directly; it does not
require `s` to belong to the list-critical core.

Every neighbour of `C` lies in `S`, one of the six foreign branch sets, or
`U_0`.  The far bag `D` contributes no neighbour.  If one of the other five
named bags contributes two distinct vertices, the corresponding two
external edges give outcome 3: deleting either edge leaves the other to
witness the same required `R-Q` model adjacency, and the branch set `R`
stays connected.  Each deletion colouring restricts properly outside `C`
and is rejected on the intact side.

Otherwise each of those five bags contributes at most one boundary vertex,
so

\[
 |N_G(C)|\le |S|+5+|N_G(C)\cap U_0|
             =|I|+4+|N_G(C)\cap U_0|.
\]

The nonempty far bag lies outside `N_G[C]`, so the boundary is actual;
seven-connectivity gives its lower bound.  This proves (3.7). `\square`

## 4. Why fixed-coordinate visibility does not release an owner

### Proposition 4.1 (coordinate--owner orthogonality)

No endpoint of the fixed edge `e` outside `R` lies in a branch set belonging
to `Lambda(A)`.  Consequently, even the stronger condition

\[
                              V(e)\subseteq N_G(A)      \tag{4.1}
\]

does not supply any of the model adjacencies monopolised by `A`.

#### Proof

The fixed-coordinate core `K subseteq R-A` contains every end of `e` which
lies in `Z`, and in particular contains an end of `e`.  If the other end
lay in a foreign branch set `Q`, then the edge `e` itself would be an
`(R-A)-Q` contact.  By definition, `Q` could not belong to `Lambda(A)`.
If the other end lies in `R` or in `U_0`, it supplies no foreign model
adjacency at all.  Thus no owner label can be repaired by `e`, irrespective
of (4.1). `\square`

## 5. Exact nonclosure

Theorems 2.1--3.2 are an operation-sensitive, model-anchored reduction:
they use target exclusion in the multi-owner transfer and retain the
list-critical core and fixed forest response.  They do not eliminate the
owner circuit.

Two exact obstacles remain.

1. The operation comparison does not force (4.1).  If (4.1) fails, it
   gives two nonempty but disjoint boundary-partition languages on
   `N_G(A)` or `N_G(C)`; list-criticality of `K` supplies no theorem making
   those languages intersect.
2. The globally minimum exact model need not span `G`.  Formula (3.7) has
   the uncontrolled term `|N_G(C) cap U_0|`.  The older spanning
   multi-owner portal theorem has no such term, but imposing spanningness
   here invalidates the omission step which proved that every appendage has
   at least two owners.

Therefore the first unsupported inference is

\[
 \begin{gathered}
   \text{a fixed-coordinate list-critical core and a coordinate-free owner
   circuit}\\
   \text{with the response alternatives of Theorem 3.2}
 \end{gathered}
 \Longrightarrow
 \begin{gathered}
   K_7^-\preccurlyeq G,\quad\text{a common boundary partition, or}\\
   \text{a bounded response boundary retaining the original model labels.}
 \end{gathered}                                        \tag{5.1}
\]

This is a recorded route nonclosure, not a counterexample to (5.1).

## Dependencies

- [model ownership and coordinate avoidance](../results/hc7_k7minus_model_anchored_appendage_ownership.md);
- [changing the deleted edge at an anchored side](../results/hc7_k7minus_operation_provenance_exchange.md); and
- [the general spanning multi-owner portal theorem](../results/hc7_multi_owner_portal_linkage_transfer.md).
