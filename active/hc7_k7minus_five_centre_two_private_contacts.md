# A retained-pole four-root witness forces two private triangle contacts

**Status:** written proof; separate hash-pinned internal audit **GREEN** in
[`hc7_k7minus_five_centre_two_private_contacts_audit.md`](hc7_k7minus_five_centre_two_private_contacts_audit.md).
The theorem is unbounded.  It forces two private contacts for every centre
whose deletion leaves both pole labels among the other four centres.  It
applies in particular to every pole-free centre.  It does not by itself
eliminate configurations in
which the resulting two private contacts are different for different
centres.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting

Use the hypotheses and notation of the separately audited
[global five-root palette alternative](hc7_k7minus_five_centre_t5_global_palette.md)
in its all-rainbow outcome.  Thus

\[
 S=Z\mathbin{\dot\cup}\{p,q\},\qquad |Z|=5,
\]

`G-S` has connected full components `C,D`, the full rooted instance on
`C` is infeasible, and deleting any one centre makes it feasible.  Every
centre `z` has a contact triangle

\[
                         T_z=N_D(z)=\{t_1,t_2,t_3\}.
\tag{1.1}
\]

The separately audited
[rainbow-triangle theorem](hc7_k7minus_five_centre_rainbow_triangle_rooted_k5.md)
gives a rooted `K_5` minor in `G[D union {p,q}]` with pairwise disjoint
connected branch sets

\[
                         B_p,B_q,B_1,B_2,B_3,
\tag{1.2}
\]

where `p in B_p`, `q in B_q`, and `t_i in B_i`.

A vertex `t in T_z` is **private to `z` among the five centres** when

\[
                              N_Z(t)=\{z\}.
\tag{1.3}
\]

## 2. The connected branch set from a four-root witness

Fix `z in Z`, put `A=Z-{z}`, and choose a `p`--`q` path `P` in

\[
                         H=G[C union A union {p,q}]
\tag{2.1}
\]

such that one component `K` of `H-P` contains all of `A`.  Full five-root
infeasibility gives

\[
                              E_G(z,K)=\varnothing.
\tag{2.2}
\]

Let `mathcal B` be the set of components of `H-P`, other than `K`, which
have a neighbour at `z`, and put

\[
 X=\{z\}\mathbin{\cup}(V(P)-\{p,q\})
       \mathbin{\cup}\bigcup_{B\in\mathcal B}V(B).
\tag{2.3}
\]

### Lemma 2.1 (connected witness branch set)

The set `X` is connected and is adjacent to `K`.

#### Proof

The permitted equal-pole colouring of the closed `C`-shore gives
`phi_C(p)=phi_C(q)`, so `pq` is not an edge.  Hence the open part
`P-{p,q}` is nonempty and connected.  Since every vertex of `A` belongs
to `K`, each member `B` of `mathcal B` is a subgraph of `C`.  Distinct
components of `H-P` are anticomplete, and there are no `C`--`D` edges.
Consequently

\[
                              N_G(B)\subseteq\{z\}\cup V(P).
\tag{2.4}
\]

The nonempty component `D` lies outside `B union N_G(B)`.  Seven-connectivity
therefore gives `|N_G(B)|>=7`, so `B` has at least six distinct neighbours
on `P`.  In particular, it has a neighbour in `P-{p,q}`.  Thus the union
of the open path and all members of `mathcal B` is connected.

Fullness gives `z` a neighbour in `C`.  By (2.2), every such neighbour
lies either on the open part of `P` or in a member of `mathcal B`.
Therefore adjoining `z` preserves connectedness, and `X` is connected.

It remains to prove adjacency to `K`.  The connected graph `K` contains
the four pairwise nonadjacent vertices of `A`, so `K cap C` is nonempty.
Let `R` be a component of `G[K cap C]`.  Equation (2.2), the absence of
`C`--`D` edges, and the definition of `K` give

\[
                              N_G(R)\subseteq A\cup V(P).
\tag{2.5}
\]

Again `D` lies beyond this neighbourhood.  Seven-connectivity and
`|A|=4` imply that `R` has at least three distinct neighbours on `P`.
At least one is different from `p,q`, and hence belongs to `X`.  Since
`R subseteq K`, the sets `K,X` are adjacent. \(\square\)

The deletion of the two pole vertices in (2.3) is essential: it keeps
`X` disjoint from the rooted model (1.2).  Lemma 2.1 shows that
seven-connectivity supplies both the lost connectivity and an internal
`K`--`X` edge.

## 3. Terminal composition

### Theorem 3.1 (two-private-contact necessity)

Suppose `G` has no `K_7^-` minor.  Let `z in Z`, and suppose that
`A=Z-{z}` contains a centre adjacent to `p` and a centre adjacent to `q`.
Then at least two vertices of `T_z` are private to `z` among the five
centres.

#### Proof

Take the rooted `K_5` model (1.2) and the disjoint connected sets `X,K`
from Lemma 2.1.  These seven sets are pairwise vertex-disjoint: the five
rooted bags lie in `D union {p,q}`, while `X` lies in `C union {z}` and
`K` lies in `C union A`.

The set `X` is adjacent to all five rooted bags.  Its open path has one
edge to `p in B_p` and one edge to `q in B_q`, while the three edges
`zt_i` join it to `B_i` for `i=1,2,3`.  Lemma 2.1 also gives the
`X`--`K` adjacency.

By hypothesis there are `a_p,a_q in A subseteq K` with
`a_pp,a_qq in E(G)`.  Hence `K` is adjacent to `B_p` and `B_q`.  If a
contact `t_i` is not private to `z`, some member of `A subseteq K` is
adjacent to `t_i`, and consequently `K` is adjacent to `B_i`.

If at least two contacts of `T_z` were not private, `K` would be adjacent
to at least four of the five rooted bags.  The seven branch sets

\[
                         X,K,B_p,B_q,B_1,B_2,B_3
\tag{3.1}
\]

would then be pairwise adjacent with at most one missing pair.  They would
form a `K_7^-` minor model, contrary to the hypothesis.  Thus at most one
contact is nonprivate, proving the theorem. \(\square\)

### Corollary 3.2 (centres which do not carry a unique pole label)

Suppose both pole labels occur among the pole-incident centres.  Every
pole-free centre, and every pole-incident centre whose own pole label
occurs at least twice, has at least two private vertices in its contact
triangle.

#### Proof

Deleting a pole-free centre leaves both pole labels.  Deleting a centre
whose pole label occurs at least twice leaves another centre at its pole
and leaves a centre at the opposite pole.  Theorem 3.1 applies in either
case. \(\square\)

In particular, in every all-rainbow row all centres except possibly a
pole-incident centre which is the unique centre at its pole have two
private contacts.  In the order-eleven equality case of the audited
five-root atom theorem, all five centres are pole-incident.  If their pole
multiplicities are `3+2`, the conclusion holds for all five centres; if
they are `4+1`, it holds for the four centres in the larger class.

## 4. Exact scope

The theorem gives a two-private-contact conclusion whenever deleting the
chosen centre retains both pole labels.  It uses one literal `C`-shore
four-root witness and the
one common rooted `K_5` model on the `D`-shore; no finite bound on either
shore is used.

The argument does not constrain a pole-incident centre which is the unique
centre at its pole, or the identities of private contacts belonging to
different triangles.  Consequently it is a strict unbounded reduction of
the all-rainbow branch, not a proof of the full five-centre two-cut theorem.

## Dependencies and claim status

- The two full shores, seven-connectivity, independent centres, permitted
  response colourings, and four-root feasibility come from the separately
  audited five-centre two-cut and global-palette theorems.
- The shore-confined rooted `K_5` model is the separately audited
  rainbow-triangle theorem.
- Lemma 2.1, Theorem 3.1, and Corollary 3.2 are written proofs in this
  note.  No full branch closure is claimed.
