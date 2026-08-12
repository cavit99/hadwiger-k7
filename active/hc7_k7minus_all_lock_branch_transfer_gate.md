# The all-lock branch-set transfer gate

**Status:** written model-transfer lemmas and a recorded route nonclosure;
[separate internal audit GREEN](hc7_k7minus_all_lock_branch_transfer_gate_audit.md).
This note does not prove the matching row, the `kappa(X)=6` branch, the
`K_7^-` six-colour conjecture, or `HC_7`.

## 1. Setting

Use the opposite-coordinate matching setting of the audited
[common-state theorem](../results/hc7_k7minus_matching_square_common_state.md).
Thus

\[
 e=up,\qquad f=vq,\qquad H=G-\{e,f\},
\]

and fix a proper six-colouring `phi` of `H` for which `e` has
monochromatic ends and `f` has differently coloured ends.  Write

\[
                 \phi(u)=\phi(p)=\alpha .             \tag{1.1}
\]

Assume that the bounded response outcomes of the audited
[lock-boundary reduction](../results/hc7_k7minus_matching_lock_boundary_reduction.md)
have been excluded.  For each `beta ne alpha`, the component

\[
 K_\beta\quad\text{of}\quad H[\phi^{-1}(\{\alpha,\beta\})]
 \quad\text{containing }u                             \tag{1.2}
\]

also contains `p`, is connected and dominating in `G`, and satisfies

\[
 \chi(G[K_\beta])=3,
 \qquad 4\leq\chi(G-K_\beta)\leq5,
 \qquad K_6\npreccurlyeq G-K_\beta .                 \tag{1.3}
\]

There is one useful strengthening of (1.3) which is easy to miss.

### Lemma 1.1 (four exact four-chromatic complements)

For all but at most one colour `beta ne alpha`, the component `K_beta` is
the entire subgraph of `H` induced by the colours `alpha,beta`.  For each
such `beta`,

\[
                  \chi(G-K_\beta)=4.                  \tag{1.4}
\]

#### Proof

Suppose a vertex `x outside K_beta` has colour `alpha` or `beta`.  Since
`K_beta` dominates `G`, the vertex `x` has an edge into `K_beta`.  No such
edge lies in `H`, because it would join `x` to the connected
`alpha-beta` component `K_beta`.  The edge is not `e`, whose two ends lie
in `K_beta`; therefore it is `f`.  Its other endpoint lies in `K_beta` and
also has colour `alpha` or `beta`.  Since `f` is proper under `phi`, the
unordered pair of its fixed endpoint colours is exactly `{alpha,beta}`.
This equality can hold for at most one choice of `beta`.  For every other
choice no `alpha`- or `beta`-coloured vertex lies outside `K_beta`, so
`K_beta` is the whole two-colour induced subgraph.

For such a `beta`, the restriction of `phi` colours `G-K_beta` with the
four remaining colours.  The edge `e` has both ends in `K_beta`, and the
only other edge omitted from `H` is the edge `f`, which is proper under
`phi`.  Hence `chi(G-K_beta)<=4`.  The lower bound in (1.3) gives equality.
`\square`

The conclusion is chromatic rather than rooted.  `HC_4` supplies a `K_4`
minor somewhere in `G-K_beta`, but gives no prescription that its four
branch sets be adjacent to both sides of a connected `u-p` split inside
`K_beta`, or that they coincide with four foreign bags of the common
model.  Since `K_beta` dominates, every one of those `K_4` bags has some
neighbour in `K_beta` as a whole; domination does not decide on which side
of the split that neighbour lies.  This is the same allocation obstruction
with four rather than five foreign labels.

More precisely, let `D_1,...,D_4` be any `K_4` model in `G-K_beta` and
split `G[K_beta]` across the restored edge `e` into connected sets
`L_beta dotcup P_beta` containing `u,p`.
To obtain the desired six-bag clique model from these objects one needs

\[
 E_G(D_i,L_\beta)\ne\varnothing\ne E_G(D_i,P_\beta)
                    \qquad(i=1,\ldots,4).              \tag{1.5}
\]

The hypotheses imply only

\[
 E_G(D_i,L_\beta\cup P_\beta)\ne\varnothing
                    \qquad(i=1,\ldots,4).              \tag{1.6}
\]

Indeed, every vertex of every `D_i` has a neighbour in `K_beta`, because
`K_beta` is dominating, but all such neighbours may lie in one split side.
The failure of (1.5) therefore does not even expose a vertex separator:
paths between `D_i` and the other side may run through the other `D_j` or
through vertices of `(G-K_beta)-union D_j`.  Turning (1.6) into (1.5), a
small actual response boundary, or a common shore partition is the first
additional theorem required by the four-chromatic strengthening.

The double contraction `G/e/f` supplies a `K_6` model.  After lifting it,
write its branch sets as

\[
                         R,B_1,\ldots,B_5,             \tag{1.7}
\]

where `u,p in R`.  If the pair `v,q` has the same model label as `u,p`,
it also lies in `R`; otherwise it is co-bagged in one of the `B_i`.
The model can be made spanning, but the first lemma deliberately permits
unused vertices because spanningness is irrelevant to a minor model and
would only obscure the elementary transfer.

Choose connected sets

\[
                         R=L\mathbin{\dot\cup}P,
 \qquad u\in L,\quad p\in P,                           \tag{1.8}
\]

with an edge between them.  The usual tree split across `e` is one such
choice.  A foreign label is **double-contacting** when its bag is adjacent
to both `L` and `P`.

The model in (1.7) and the four-bag model furnished by Lemma 1.1 are
generally different.  In particular, no proved statement places four
foreign bags of (1.7) inside `G-K_beta`.  This is a second reason why
Lemma 1.1 does not immediately improve the existing common-model split.

## 2. What minimum branch bags actually force

The following observation is the exact model-theoretic content of
minimising the co-bagged branch set.  It is independent of colours.

### Lemma 2.1 (two-owner floor)

Fix a set `Z subseteq R` of protected vertices, including `u,p` and every
other coordinate endpoint whose model label is required to remain `R`.
Among all labelled `K_6` models

\[
                         R,B_1,\ldots,B_5              \tag{2.1}
\]

with `Z subseteq R`, choose one with `|R|` minimum; the models need not be
spanning.  Let `W` be a nonempty subset of `R-Z` such that both `G[W]` and
`G[R-W]` are connected.  Put

\[
 \Omega(W)=\{i\in[5]:E_G(R-W,B_i)=\varnothing\}.       \tag{2.2}
\]

Then

\[
                              |\Omega(W)|\geq2.         \tag{2.3}
\]

#### Proof

If `Omega(W)` is empty, omit `W` and replace `R` by `R-W`.  The residual
root bag is nonempty and connected, contains every protected vertex, and
retains its adjacency to all five foreign bags.  This is a smaller model
in the comparison class.

Suppose `Omega(W)={i}`.  Replace

\[
                         R\longmapsto R-W,
 \qquad B_i\longmapsto B_i\cup W.                     \tag{2.4}
\]

The enlarged foreign bag is connected because the definition of
`Omega(W)` and the old `R-B_i` model edge give an edge from `W` to `B_i`.
The two connected sides `W,R-W` of the old connected bag have an edge
between them; after (2.4) that edge restores the required adjacency
between the new root bag and the enlarged `B_i`.  Every other root--foreign
adjacency survives by (2.2), and enlarging `B_i` cannot destroy a
foreign--foreign adjacency.  Again the protected vertices remain in the
strictly smaller root bag.  Both cases contradict the choice of `R`, and
(2.3) follows. `\square`

This lemma gives a two-**label** obstruction.  It does not give a
two-vertex cut.  Each owner `B_i` is an arbitrary connected branch set,
and the set of its vertices adjacent to `W` is not bounded.

There is also a mismatch between this minimum and the proposed
double-contact maximum.  If `W subseteq L`, define

\[
 \Delta_L(W)=\{i:\ E_G(B_i,L)\ne\varnothing,
                       E_G(B_i,L-W)=\varnothing,
                       E_G(B_i,P)\ne\varnothing\}.     \tag{2.5}
\]

Every label in `Delta_L(W)` ceases to be double-contacting when `W` is
removed from the root bag, even when `Omega(W)` is empty and the six-bag
model remains valid.  Consequently, maximising the number of double
contacts first does not permit the transfer used in Lemma 2.1.  Reversing
the priorities gives Lemma 2.1, but supplies no reason for the minimum-root
model to maximise double contacts.  The two extremal choices are not one
monotone potential.

## 3. The exact inward transfer and its obstruction

The transfer envisaged for a lock path moves a piece of a foreign bag into
one side of the split.  Its valid model-local form is as follows.

### Lemma 3.1 (foreign-piece absorption)

Fix `i in [5]` and a nonempty proper set `W subset B_i`.  Suppose

1. `G[W]` and `G[B_i-W]` are connected;
2. `W` is adjacent to `L` and to `B_i-W`; and
3. `B_i-W` remains adjacent to every `B_j` with `j ne i`.

Then

\[
 R'=R\cup W,\qquad B_i'=B_i-W,
 \qquad B_j'=B_j\ (j\ne i)                           \tag{3.1}
\]

is another labelled `K_6` model.  Moreover

\[
                         L'=L\cup W,\qquad P'=P        \tag{3.2}
\]

is a connected split of its root bag with the same protected poles.

#### Proof

The set `R'` is connected through an `L-W` edge and `B_i'` is connected
by hypothesis.  The `W-(B_i-W)` edge restores the `R'-B_i'` adjacency.
All `B_i'-B_j` adjacencies survive by item 3, all other old model
adjacencies are unchanged, and enlarging `R` cannot lose an adjacency.
Finally `L'` is connected, `P'` is connected, and their old adjacency
survives. `\square`

Thus failure of this inward move has an exact certificate: either the
residual foreign bag is disconnected, or some foreign label has all of
its `B_i-B_j` model edges incident with the proposed piece.  Neither
certificate bounds the full neighbourhood of a residual component by
seven or eight.  Seven-connectivity gives a lower bound on any actual
separator it exposes, not the required upper bound.  Nor does either
certificate carry a boundary colouring.

## 4. A locked Kempe component cannot label a proper transfer piece

The missing all-proper signature does not repair the obstruction in
Section 3 for one fixed lock component.

### Lemma 4.1 (Kempe indivisibility of a lock)

Fix `beta ne alpha` and put `K=K_beta`.  Let `U` be any vertex set which
contains some but not all vertices of `K`.  Interchanging `alpha,beta` on
`U` does not give a proper colouring of `H`.

In contrast, interchanging the colours on the whole component `K` is
proper, but leaves the two ends of `e` equal-coloured.  Hence the forbidden
all-proper signature imposes no further condition on this whole-component
switch.

#### Proof

The graph `H[K]` is connected.  Therefore an edge `xy` of `H[K]` crosses
the nontrivial partition `U cap K, K-U`.  The endpoints have the two
different colours `alpha,beta` under the proper colouring `phi`.
Interchanging those colours at exactly one endpoint makes `x,y`
monochromatic, so the partially switched assignment is not proper.

Switching the whole bichromatic component is a valid Kempe interchange.
Both `u` and `p` belong to `K`, so they are switched together and remain
equal-coloured.  The resulting signature is therefore still of the form
`(=,*)`, never the forbidden all-proper signature `(ne,ne)`. `\square`

Lemma 4.1 is the first failed inference in the proposed all-lock transfer.
A proper initial segment of a lock path may be an excellent connected set
for Lemma 3.1, but it is not a Kempe component and carries no proper
six-colouring.  Conversely, the only switchable piece containing the lock
path is the whole component; it contains both sides of the coordinate and
cannot be absorbed into one side of the split.

In particular, changing ownership of vertices between branch bags does
not itself change `phi` and cannot turn a lost model adjacency into the
opposite singleton response.  The critical implication

\[
 \text{every move repairing `e` must make `f` monochromatic}             \tag{4.1}
\]

applies only after a **proper** Kempe interchange has separated the ends
of `e`.  In the all-lock case no `alpha-beta` interchange does so.

## 5. Route verdict and smallest repair

The proposed lexicographic branch-set transfer does not presently prove
the all-lock edge case.  Its first unsupported implication is

\[
 \begin{gathered}
 \text{a lock-path prefix cannot be absorbed without disconnecting a bag}\
 \text{or losing a model adjacency}
 \end{gathered}
 \quad\Longrightarrow\quad
 \begin{gathered}
 \text{an original-coordinate response boundary of order seven or eight,}\
 \text{or a common shore partition.}
 \end{gathered}                                      \tag{5.1}
\]

The left side of (5.1) is model ownership.  The right side is colouring
data on a vertex boundary.  Lemmas 2.1 and 3.1 expose the ownership
certificate exactly; Lemma 4.1 shows why the fixed lock colouring cannot
convert it into the required response.  The universal absence of the
all-proper signature has already been spent in proving that the palette is
locked and supplies no second use on a partial lock segment.

This is a route nonclosure, not a counterexample to a response-sensitive
co-bagged forest-split theorem.  A repair must add genuinely new content,
for example the following narrower statement.

> **Blocked-transfer response theorem (open).**  In the seven-connected
> common matching host, if every foreign-piece absorption along all five
> lock components is blocked, then the family of all three realised
> signatures—not one fixed lock colouring—either produces a boundary
> partition extending through both original shores, produces an
> original-coordinate response boundary of order seven or eight, or
> forces four foreign bags to meet both sides of one co-bagged split.

Proving that theorem would require comparing different signature
colourings or different lock palettes while retaining one model.  It is
not a consequence of a branch-set move inside one fixed `K_beta`.

## 6. Scope

The proved inputs used here are the common matching state and the
lock-boundary reduction cited in Section 1.  The model-transfer lemmas are
elementary and unbounded.  The existing
[static multi-owner barrier](../barriers/hc7_multi_owner_static_first_hit_barrier.md)
independently shows that seven-connectivity, minor exclusion and an
optimised labelled model do not turn a two-owner obstruction into a small
separator without a critical colouring response.  That barrier is
six-colourable and does not satisfy the present critical-host hypotheses;
it supports only the stated route diagnosis.
