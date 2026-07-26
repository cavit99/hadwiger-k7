# Spanning normalization for the eight latent response columns

**Status:** written proof;
[separately audited GREEN](hc7_order8_latent_column_spanning_normalization_audit.md).

This note replaces the earlier nine-set spanning argument by a normalization
which keeps the two fan centres and all eight latent column seeds fixed.
It therefore remains compatible with either free-root choice.  It also
shows exactly how a first root encounter changes when the other nonresponse
label is consumed.

## 1. Seed-preserving latent-column systems

Use outcome 3 of Lemma 2.1 in the audited
[dual-free-root response-star theorem](hc7_order8_dual_free_root_response_star.md).
Thus `v,w` are the two fan centres and

\[
                         K_s\qquad(s\in S)              \tag{1.1}
\]

are eight pairwise disjoint connected latent columns, where `|S|=8`.
For each `r in S`, the original fan limbs give adjacent connected roots

\[
                  R_C^r=P_r^C,
                  \qquad R_D^r=P_r^D-\{r\},            \tag{1.2}
\]

which are disjoint from the seven columns with labels different from `r`
and are each adjacent to all seven.

A **seed-preserving enlargement** is a family of pairwise disjoint connected
sets

\[
                         \widehat K_s\supseteq K_s      \tag{1.3}
\]

contained in `V(G)-{v,w}`.  The original roots in (1.2) are retained when
one label is consumed; vertices added to the consumed column need not be
assigned to either root.

Let `Khat` be the contact graph of the eight enlarged columns.  Choose a
seed-preserving enlargement first maximizing `|E(Khat)|` and then maximizing
the number of covered host vertices.

## 2. The maximum system spans outside the two centres

### Theorem 2.1

Assume `G` is seven-connected and has no `K_7` minor.  Every lexicographically
maximum seed-preserving enlargement satisfies

\[
             V(G)=\{v,w\}\mathbin{\dot\cup}
                    \bigcup_{s\in S}\widehat K_s.       \tag{2.1}
\]

Moreover, for every `r in S`, the graph `Khat-r` is `K_5`-minor-free.

#### Proof

If `Khat-r` had a `K_5` model, its five branch sets would lift through the
seven surviving enlarged columns.  The original roots `R_C^r,R_D^r` are
disjoint from those columns, adjacent to one another and adjacent to every
one of them.  They would complete an explicit `K_7`-minor model.  Hence
every `Khat-r` is `K_5`-minor-free.

Suppose a component `Z` remains outside the two centres and the eight
enlarged columns.  Let `A` be the set of column labels having a neighbour
in `Z`.  The set `A` is nonempty.  Otherwise

\[
                              N_G(Z)\subseteq\{v,w\},
\]

contrary to seven-connectivity.

If two labels in `A` are nonadjacent in `Khat`, connectedness of `Z` gives
a path between their columns whose internal vertices lie in `Z`.  Absorb
the path interior into one endpoint column.  This preserves all seeds,
connectedness, disjointness and old contacts while adding the missing
contact, contrary to maximality of `|E(Khat)|`.

Thus `A` is a clique in `Khat`.  Choose `a in A` and absorb all of `Z` into
`widehat K_a`.  The enlarged set is connected.  Every other column newly
met through `Z` has label in `A` and therefore already contacted
`widehat K_a`.  No old contact is lost, while the number of covered vertices
strictly increases.  This contradicts the second maximization and proves
(2.1). \(\square\)

### Corollary 2.2 (no unclassified bypass interior)

In a maximum system, every path avoiding `v` whose endpoints lie in two
columns has all its vertices in the eight columns together with `w`.
After truncating at two noncontacting endpoint columns, its first old object
is therefore either `w` or another latent column.  There is no additional
outside component to classify.

## 3. Changing the consumed free label

Let `a,b` be the two nonresponse labels.  Suppose `r` is one of them and
the system currently consumes `r`, so its roots are `R_C^r,R_D^r` and its
other seven latent columns survive.

### Lemma 3.1 (first root encounter becomes column dirt)

Let `P` be a path between response-labelled columns which avoids `v`.
Suppose that, after leaving its initial column, its first encounter with an
old root or column is a vertex `z` of `R_C^r union R_D^r`.

If `z ne w`, then after consuming the other nonresponse label instead:

1. both endpoint columns of `P` still survive;
2. `z` belongs to the restored latent column `K_r`; and
3. in the original, unenlarged latent-column system, `z` is the first old
   root-or-column encounter of `P` in the new system.

Thus the only root encounter which cannot be converted in this way is the
fixed opposite fan centre `w`.

For a seed-preserving enlargement from Section 1, the correct conclusion is
slightly weaker: the path meets the restored enlarged column `widehat K_r`
at or before `z`.  It can do so earlier through a vertex added to the
consumed column which was not assigned to either old root.

#### Proof

The path avoids `v`.  From the literal definitions

\[
 R_C^r-\{v\}\subseteq K_r,
 \qquad
 R_D^r-\{w\}\subseteq K_r.                            \tag{3.1}
\]

Hence `z ne w` belongs to the restored column `K_r`.  The response endpoint
labels are the target or sources, never `a` or `b`, so consuming the other
nonresponse label preserves both endpoint columns.

Before reaching `z`, the path met neither current root nor current column.
In particular it did not meet the other nonresponse column.  The new roots
are contained in that former column together with the fixed centres `v,w`;
the path avoids `v` and, because `z` was the first old-root encounter and
`z ne w`, did not meet `w` earlier.  It therefore meets no new root before
`z`.  All other surviving seed columns are unchanged, so in the unenlarged
system `z` remains the first old-object encounter and now lies in `K_r`.

Under a seed-preserving enlargement, the same argument excludes every new
root and every enlarged column other than `widehat K_r` before `z`.  The
path may already meet an added vertex of `widehat K_r`; hence its first
column encounter is at or before `z`, as asserted. \(\square\)

## 4. Exact gain and trust boundary

Theorem 2.1 permits a finite lexicographic rank on the eight latent columns
without enlarging or reassigning the native fan centres.  Lemma 3.1 converts
every first-root case except a hit on `w` into a column hit, possibly at an
earlier vertex after seed-preserving enlargement.  Neither statement
supplies the needed exchange at a first old column or at `w`.

Changing the consumed label replaces one seven-vertex contact graph by
another.  It need not preserve which column has low degree, the number of
contacts in that seven-vertex graph, or a later encounter sequence on the
same path.  The lemma concerns only the first encounter and does not claim
a rank improvement.  The remaining dirty-bypass theorem must still use the
coupled proper-minor responses, `K_7`-minor exclusion or a literal bounded
separation to justify any reassignment.

## 5. Dependency

- [two free root choices in the critical-edge response star](hc7_order8_dual_free_root_response_star.md).
