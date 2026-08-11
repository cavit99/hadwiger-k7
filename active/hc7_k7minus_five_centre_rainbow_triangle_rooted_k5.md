# A rainbow contact triangle gives a shore-confined rooted `K_5`

**Status:** written proof; separate hash-pinned internal audit **GREEN** in
[`hc7_k7minus_five_centre_rainbow_triangle_rooted_k5_audit.md`](hc7_k7minus_five_centre_rainbow_triangle_rooted_k5_audit.md).
The theorem is unbounded.  Its pole-incident corollary eliminates every
all-rainbow configuration in which all three contacts of some
pole-incident centre are shared by other centres.  It does not eliminate
the surviving private-contact configurations.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting

Use the hypotheses and notation of the separately audited
[global five-root palette alternative](hc7_k7minus_five_centre_t5_global_palette.md),
and assume its all-rainbow outcome.  Thus

\[
 S=Z\mathbin{\dot\cup}\{p,q\},\qquad |Z|=5,
\]

`G-S` has connected full components `C,D`, and one fixed proper
six-colouring `phi_D` of `G[D union S]` satisfies

\[
 \phi_D(Z)=\alpha,\qquad
 \phi_D(p)=\beta,\qquad
 \phi_D(q)=\delta.
\tag{1.1}
\]

Put

\[
                    \Gamma=[6]-\{\alpha,\beta,\delta\}.
\tag{1.2}
\]

For every centre `z in Z`, its `D`-contact set is a triangle

\[
 T_z=N_D(z)=\{t_1,t_2,t_3\},
 \qquad \phi_D(t_i)=\gamma_i,
 \qquad \Gamma=\{\gamma_1,\gamma_2,\gamma_3\}.
\tag{1.3}
\]

Lemma 5.1 of the global palette alternative gives, for every `i`, a
`beta`--`gamma_i` path from `p` to `t_i` and a
`delta`--`gamma_i` path from `q` to `t_i`.  The distinct-response
obstruction also gives a `beta`--`delta` path from `p` to `q`.  All open
interiors of these seven paths lie in `D`.

## 2. The rooted model

### Theorem 2.1 (shore-confined rooted `K_5`)

For every rainbow centre `z`, the graph `G[D union {p,q}]` contains a
rooted `K_5` minor with five pairwise disjoint connected branch sets

\[
                         B_p,B_q,B_1,B_2,B_3,
\tag{2.1}
\]

where `p in B_p`, `q in B_q`, and `t_i in B_i` for `i=1,2,3`.

#### Proof

Let `H=K_{1,1,3}` with singleton parts `p,q` and stable part
`{t_1,t_2,t_3}`.  For each of its seven edges, choose one of the paths
specified at the end of Section 1.  These paths form an `H`-scheme in
`G[D union {p,q}]`.

Indeed, a selected path for the edge `uv` uses only the two colours
`phi_D(u),phi_D(v)`.  The five roots have pairwise distinct colours, so
the path contains no other root.  If a vertex `x` belongs to every path
in a nonempty family, its colour belongs to every corresponding
two-element endpoint-colour set.  The unique root having colour
`phi_D(x)` is therefore a common endpoint of all the corresponding edges
of `H`.  This is exactly the multiple-intersection condition in the
definition of an `H`-scheme.

Kuendgen--Pelsmajer--Ramamurthi, Theorem 6.2, states that
`K_{1,1,3}` is contractible.  The scheme therefore yields a rooted
`K_{1,1,3}` minor with the five branch sets in (2.1).  The three literal
edges of the triangle `t_1t_2t_3` make `B_1,B_2,B_3` pairwise adjacent.
All ten pairs of branch sets are now adjacent, so they form the asserted
rooted `K_5` model. \(\square\)

The external conversion used here is
[Theorem 6.2 of Kuendgen, Pelsmajer, and Ramamurthi](https://arxiv.org/abs/1207.6141).

## 3. The pole-incident terminal consequence

Call a contact `t in T_z` **private to `z` among the five centres** when

\[
                             N_Z(t)=\{z\}.
\tag{3.1}
\]

### Corollary 3.1 (private-contact necessity)

Suppose `G` has no `K_7^-` minor and `z` is pole-incident.  Then `T_z`
contains a contact private to `z` among the five centres.

#### Proof

By symmetry, suppose `zp` is an edge.  Take the five rooted branch sets
from Theorem 2.1 and put

\[
                             Y=C\cup(Z-\{z\}).
\tag{3.2}
\]

The set `Y` is connected: `C` is connected, and every centre in
`Z-{z}` has a neighbour in `C`.  It is disjoint from the five branch sets
and from `{z}`.  Fullness of `C` makes `Y` adjacent to `B_p` and `B_q`,
and a `C`-contact of `z` makes `Y` adjacent to `{z}`.

If (3.1) failed for all three contacts, then for every `i` some centre in
`Z-{z}` would be adjacent to `t_i`.  Hence `Y` would also be adjacent to
every `B_i`.  The seven disjoint connected sets

\[
               \{z\},\quad Y,\quad
               B_p,B_q,B_1,B_2,B_3
\tag{3.3}
\]

would then be pairwise adjacent except possibly for `{z}` and `B_q`:
the edge `zp` joins `{z}` to `B_p`, and the three edges `zt_i` join it to
the three triangle bags.  Thus (3.3) would be a `K_7^-` minor model, a
contradiction. \(\square\)

### Corollary 3.2 (pairwise triangle uniqueness)

If `z` is pole-incident, no other centre `w in Z-{z}` has
`T_w=T_z`.

#### Proof

Equality would make `w` adjacent to every vertex of `T_z`, contrary to
Corollary 3.1. \(\square\)

## 4. Exact scope

Theorem 2.1 is stronger than six unrelated pole--triangle connections:
all seven demand paths use one colouring, satisfy the full scheme
intersection condition, and yield one common rooted model confined to the
closed `D`-shore.  Corollary 3.1 is terminal whenever a pole-incident
triangle has no centre-private contact.

The conclusion does not by itself close the all-rainbow row.  A surviving
pole-incident centre may have one private contact, and a pole-free centre
is adjacent to neither pole, so its singleton bag cannot be added to the
rooted `K_5` with only one missing adjacency.  In particular, the theorem
does not reserve or absorb the contact triangle of a second centre.

## Dependencies and claim status

- The two-cut geometry, full-shore contacts, and distinct-response
  `p`--`q` path come from the separately audited
  [five-centre two-cut reduction](../results/hc7_k7minus_five_centre_two_cut_reduction.md).
- The common fixed colouring and six pole--triangle Kempe connections are
  Lemma 5.1 of the separately audited
  [global five-root palette alternative](hc7_k7minus_five_centre_t5_global_palette.md).
- Contractibility of `K_{1,1,3}` is an established external input:
  Kuendgen--Pelsmajer--Ramamurthi, Theorem 6.2.
- The scheme verification, rooted `K_5` conversion, and private-contact
  consequence are written proofs in this note.  No elimination of the
  private-contact or pole-free residues is claimed.
