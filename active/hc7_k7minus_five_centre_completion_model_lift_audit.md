# Internal audit of the five-centre completion-model lift

Audited file:
`active/hc7_k7minus_five_centre_completion_model_lift.md`

Audited SHA-256:

```text
09ea5813b843a17e667d3f8cd4cebbf8094f2bceb39955d2ed873638e4f9afbf
```

**Verdict:** **GREEN** for Lemmas 2.1, 2.2 and 3.1, Theorem 4.1,
Corollary 4.2, Theorem 4.3, and the stated conditional scope.

This is a hash-pinned internal mathematical audit, not external peer
review.  The theorem is unbounded.  It is conditional on the minimally
infeasible five-root row: the full `D`-side instance is infeasible and
deleting any one centre makes it feasible.  It does not eliminate the final
unique-owner configuration whose sole branch-set nonedge joins two
`C`-only bags.

## 1. Exact inputs and hypotheses checked

The exact repository revisions used in checking the setting are:

| input | source SHA-256 | audit SHA-256 |
|---|---|---|
| five-centre two-cut reduction | `1917b5e3d183d44a2d905d2628272d10e4bc6f7ae0768b43cab0e9462b83332a` | `d01183c936d79ea2e07f956c2e89f7291df9cc28a5dab3dda6b093c8a69c4ea3` |
| four-root transfer | `1f91f4396e090497a576fd63c1462762b5ab5f95151a06632a8f63584caee1a9` | `b366bbd22bd3b37db844db80d14c80b909a49e4ee2c3681767ac0b1c916ce668` |
| global five-root palette setting | `b26f9f0d12822f93af55e3aa566fc75b985dcb5a17daa4ea2b329c8efea274c3` | `765df0db1168001a212c77e5f871abe4725d4c92cc4e11ae8d887ff808f92e6a` |

The two-cut theorem gives two connected full shores, `pq` absent, and the
proper contraction minor `M_C` obtained by contracting `D union Z`.  It
also proves that `M_C+pq` is exactly seven-chromatic.  Since the source
chooses `G` globally vertex-minimal among all counterexamples, the smaller
graph `M_C+pq` must contain a `K_7^-` minor; otherwise it would itself be a
smaller counterexample.

The audit treats four-root feasibility and full five-root infeasibility on
`D` as explicit standing hypotheses, exactly as the source does.  No
unbounded conclusion is inferred from a finite search.

## 2. The feasible path and omitted-root absorption

For a four-root witness `L,K`, the component `K` contains four independent
centres and therefore contains a vertex of `D`.  If `R` is a component of
`G[K cap D]`, then all its external neighbours lie in `Z union V(L)`.
The opposite shore `C` lies beyond that set, so seven-connectivity gives at
least two distinct neighbours on `L`.  Splitting between two such
attachments gives two pole subpaths, each adjacent to `K`.  This verifies
Lemma 2.1.

For Lemma 2.2, put `A=Z-{z}`.  If the omitted centre `z` had a neighbour in
`K`, adding `z` to the graph after deleting the same path `L` would put all
five centres in one component, contrary to full five-root infeasibility.
Thus `z` is anticomplete to `K`.

The path `L` avoids all four members of `A`, since those roots lie in `K`
after `L` is deleted.  Because `pq` is absent, `L` has a nonempty interior
in `D`.  Hence every component of `G[D-V(L)]` is adjacent to `L`, by
connectedness of `D`.  If `z` has no neighbour on `L`, adjoining `z` and
all off-path `D`-components met by it therefore gives a connected set.
None of those components meets `K`, since such a component is wholly
contained in `K` and would give a `z`--`K` edge.  The constructed set
`W_z` is consequently connected, contains `L` and `z`, and is disjoint
from `K`, as claimed.

## 3. Four-centre expansion and distinct pole bags

After deleting `x` from its branch set, every remaining component is
adjacent to `x`.  Inclusion-minimal retention gives each retained component
a distinct private `C`-only bag.  Choosing one centre to reconnect each
retained component and one centre for every still-required direct
`x`--bag edge uses at most four centres in Lemma 3.1.  Duplicate choices
only reduce this number.  A connected expansion containing the selected
centres reconnects the pruned branch set and preserves every required
adjacency.

If `p,q,x` lie in distinct bags, the two pole subpaths replace the
artificial edge, the complementary four-root component expands `x`, and
Lemma 2.1 supplies both new adjacencies between these three bags.  All sets
are disjoint because the old material lies in `C union {p,q}`, while the
new open-path and component material lies in `D union A`.  This verifies
the nontrivial case of Theorem 4.1; the cases avoiding `x` or placing `x`
in a pole bag lift directly as stated.

When `p,q` lie in one bag, the literal contraction edges `xp,xq` make the
`x`-bag adjacent to it.  A complete branch-set contact graph, or a sole
nonedge incident with the `x`-bag, allows one `xR_i` adjacency to be
declared missing.  Only four `xR_i` adjacencies then require preservation,
and the same four-centre lift is terminal.  Thus Corollary 4.2 correctly
leaves exactly one nonedge away from the `x`-bag and forces all five
`xR_i` adjacencies to be required.

## 4. Unique-owner normalization

Let `k` be the number of inclusion-minimal retained components of
`X-{x}`, and let `m` be the number of `R_i` contacted by them.  Private-bag
minimality gives `m at least k`, while the expansion cover has nominal
order

```text
k + (5-m) <= 5.
```

Corollary 4.2 excludes an actual cover of order at most four.  Hence the
nominal count is five and all selected centres are distinct.  In
particular `m=k`; the `k` private bags exhaust the contacted bags, so each
retained component contacts only its own private `R_i` among the five
`R`-bags.

Moving such a component into its private bag preserves connectivity and
all old adjacencies.  Its old edge to `x` makes the enlarged bag adjacent
to the singleton `{x}`.  If a moved component filled the sole branch-set
nonedge, the resulting contact graph would be complete; declaring one
`xR_j` edge missing and applying the four-centre same-bag lift would be
terminal.  The target-free hypothesis therefore preserves the unique
nonedge through this normalization.

For the normalized model, each owner set

```text
O_i = N_G(R_i) cap Z
```

is nonempty, because every contraction edge `xR_i` is represented by a
centre--`R_i` edge.  If one centre belonged to two owner sets, that centre
together with one choice from each of the other three nonempty sets would
give a cover of order at most four.  The same-bag lift would be terminal.
Thus the five nonempty owner sets are pairwise disjoint subsets of the
five-set `Z`; each is a singleton and together they exhaust `Z`.  This
verifies the owner bijection without assuming the desired conclusion.

## 5. Elimination of a pole-bag nonedge

Suppose the sole nonedge were `BR_i`, and omit its owner `z_i` from the
four-root witness.  Lemma 2.2 gives disjoint connected sets `K` and
`W_{z_i}`, with the latter containing a genuine `p`--`q` path and `z_i`.
The seven sets

```text
B union W_{z_i},  K,  R_1,...,R_5
```

are pairwise disjoint.  The first is connected because the genuine path
replaces the internal artificial edge `pq` of `B`.  Lemma 2.1 gives its
adjacency to `K`.  For every `j!=i`, the owner `z_j in K` gives the
`K`--`R_j` adjacency.  The edge from `z_i` to `R_i` fills the old
`B`--`R_i` nonedge.  All other old adjacencies persist.  Hence only
`K`--`R_i` may be absent, yielding a `K_7^-` model.  This proves that the
sole surviving nonedge must join two `R`-bags.

## 6. Spanning absorption and scope

Every component of the uncovered part of connected `G[C]` has an edge to
the current bag union and can be absorbed into an adjacent bag.  Absorption
only adds vertices, so it cannot destroy connectivity, a model edge, or an
existing owner contact.  If it fills the sole nonedge, the complete contact
graph is terminal by declaring an `xR_j` edge missing and using four-root
expansion.  If it makes one centre adjacent to two distinct `R_i`, that
centre and three further owner choices give the terminal four-centre cover.
Otherwise the unique nonedge and singleton owner sets persist.  Iteration
therefore gives the spanning partition claimed in Theorem 4.3.

No unresolved proof gap remains in the conditional conclusions of this
revision.  The source correctly leaves one case open: a spanning
unique-owner model whose sole nonedge joins two `C`-only bags.  Proving
that this normal form cannot occur still requires a branch-set exchange or
a compatible replacement of the artificial pole edge; it is not supplied
by the audited theorem.
