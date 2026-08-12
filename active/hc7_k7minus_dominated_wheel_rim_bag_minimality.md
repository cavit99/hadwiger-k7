# Root-preserving minimisation of a wheel rim branch set

**Status:** active written theorem and recorded route nonclosure; internal
audit adjacent.  The theorem is model-theoretic.  It identifies the exact
two-owner obstruction left by minimising a rooted rim bag, but does not
eliminate that obstruction, close the dominated-centre case, or prove the
`K_7^-` six-colour conjecture.

## 1. Setting

Let `J` be a graph with seven prescribed roots.  Fix a labelled six-wheel

\[
                   W=K_1\vee C_6
\]

on those root labels.  A rooted `W`-model is a family

\[
                    (B_t:t\in V(W))                  \tag{1.1}
\]

of pairwise disjoint connected branch sets, with the root labelled `t` in
`B_t`, and with every edge of `W` represented between the corresponding
branch sets.  The model need not span `J`.

Fix a rim label `s`.  Its three neighbours in `W` are the hub and its two
rim neighbours; write this set of labels as `D_W(s)`.

For a nonempty connected set `P\subseteq B_s` such that `B_s-P` is
connected and contains the root labelled `s`, define the labels whose
required adjacency is owned by `P` to be

\[
 \Omega(P)=\{t\in D_W(s):E_J(B_s-P,B_t)=\varnothing\}.       \tag{1.2}
\]

Every member of `Omega(P)` is an actual owner: the old rooted model has an
edge between `B_s` and `B_t`, so that edge has its end in `B_s` inside
`P`.

Choose a rooted `W`-model with `|B_s|` minimum among all rooted `W`-models
with the same root-to-label assignment.  This is an **ordinary**, not a
spanning, minimum.  That distinction is essential below.

## 2. The detachable-piece owner rule

### Theorem 2.1

Every set `P` admitted in (1.2) satisfies

\[
                              |\Omega(P)|\geq2.         \tag{2.1}
\]

### Proof

Suppose first that `Omega(P)` is empty.  Delete `P` from the branch set
`B_s` and leave its vertices outside the model.  The source branch set
remains connected and rooted, and every required adjacency incident with
it is still represented.  All other branch sets are unchanged.  This is a
rooted `W`-model with a smaller `s`-bag, a contradiction.

Suppose instead that `Omega(P)={t}`.  Unite `P` with `B_t`.  The enlarged
`t`-bag is connected because `P` has an edge to `B_t`.  The reduced
`s`-bag is connected and rooted.  It is adjacent to the enlarged `t`-bag
through an edge between `P` and `B_s-P`, which exists because `B_s` is
connected and both displayed parts are nonempty.  Every other required
adjacency at `s` survives by the definition of `Omega(P)`.  Enlarging
`B_t` destroys no model adjacency.  The resulting rooted `W`-model again
has a smaller `s`-bag, a contradiction.  This proves (2.1). `\square`

The proof does not require the quotient to be induced.  Any unrecorded
edge between branch sets is harmless: moving `P` may add quotient
adjacencies, but cannot destroy one except at the source, and (1.2) records
exactly those required source adjacencies.

It also does not minimise the orders of all bags.  The owner bag can grow.
Only the strict decrease of the fixed source bag is used.

There is a different, weaker conclusion when spanningness is retained.

### Theorem 2.2 (spanning comparison)

Suppose instead that (1.1) spans `J`, and minimise `|B_s|` only among
spanning rooted `W`-models with the fixed root labels.  For every set `P`
admitted in (1.2), at least one of the following holds:

1. `|Omega(P)|>=2`; or
2. `Omega(P)` is empty, `P` has no edge to any foreign branch set, and
   `N_J(P)=N_{J[B_s]}(P)` has order at least `kappa(J)`.

In particular, if

\[
                       |N_{J[B_s]}(P)|<\kappa(J),       \tag{2.2}
\]

then `P` owns at least two required foreign labels.

### Proof

The unique-owner transfer in the proof of Theorem 2.1 preserves the union
of all branch sets, so a unique owner again contradicts minimality.  If
there is no owner but `P` meets a foreign branch set, unite `P` with any
such branch set.  All required source adjacencies already survive in the
remainder, while the internal edge between the two source pieces keeps the
reduced source adjacent to the enlarged bag.  This too is a smaller
spanning model.

The only remaining owner-free case has no foreign contact.  Since the
model spans, every neighbour of `P` lies in `B_s-P`.  Its full
neighbourhood separates `P` from the six nonempty foreign branch sets, so
its order is at least `kappa(J)`.  This proves the dichotomy and (2.2).
`\square`

For a five-connected host, every root-free connected piece with connected
rooted complement and at most four attachment vertices inside the source
bag therefore owns at least two foreign labels.  Every nontrivial source
bag has such a piece: if its induced graph is two-connected, take all
vertices except the root; otherwise take the vertices of a leaf block,
apart from its attachment cutvertex, choosing a leaf block not containing
the root as a non-cutvertex.

This yields a rooted **block-chain** constraint, not a rooted path.  If the
source graph has more than one block, distinct root-free leaf-block pieces
have disjoint owner sets.  Since each has at least two owners among three
labels, there is only one such leaf block.  The root is a non-cutvertex in
the other leaf block and the block-cut tree is a path.  Individual blocks
may nevertheless be arbitrarily large and highly connected.

## 3. Exact shape of a minimum rim bag

### Theorem 3.1

Either `B_s` is a singleton, or the induced graph `J[B_s]` is a path whose
root is one endpoint.  If `x` is the other endpoint, then

\[
 \left|\{t\in D_W(s):
 E_J(B_s,B_t)\ne\varnothing\text{ and every such edge has its }B_s
 \text{-end }x\}\right|\geq2.                         \tag{3.1}
\]

More generally, every nonempty terminal subpath `P` not containing the
root owns at least two of the three required foreign labels in the sense
of (1.2).

### Proof

Suppose `|B_s|>1`.  If `x\in B_s` is not the root and `J[B_s]-x` is
connected, Theorem 2.1 applied to `P={x}` says that `x` is the sole
`B_s`-end of the required contacts to at least two labels in `D_W(s)`.

Two distinct such non-root vertices cannot exist.  Indeed, their owner
sets would be disjoint: a nonempty required adjacency cannot have all its
`B_s`-ends contained in each of two different singletons.  But two
disjoint subsets of a three-element set cannot both have order at least
two.

Every nontrivial connected graph has at least two vertices whose deletion
leaves it connected.  Thus the root is one of them and precisely one other
vertex has this property.  We now use the elementary block-tree fact that
a connected graph with exactly two non-cutvertices is a path.  Indeed,
every leaf block contains a non-cutvertex.  A leaf block of order at least
three contains at least two vertices which are not its possible attachment
cutvertex, so it would already contribute at least two.  Hence there are
exactly two leaf blocks and both are edges.  A branch in the block-cut tree
would give a third leaf block.  Finally, an internal block of order at
least three has at most two attachment cutvertices along this block-tree
path and therefore contains another non-cutvertex.  Thus every block is an
edge and the block-cut tree is a path.  Therefore `J[B_s]` itself is a
path, with the two non-cutvertices as its endpoints.

Equation (3.1) is Theorem 2.1 for the non-root endpoint.  Every terminal
subpath has connected rooted complement, so its final assertion follows
from the same theorem. `\square`

The conclusion is a rooted path, not a branch set of order two.  A path of
arbitrary order is consistent with (3.1): attach two required foreign
labels only at its non-root endpoint and the third only at its root.
Thus root-preserving bag minimisation has spent all of its force at (3.1).

## 4. Specialisation to the dominated-centre residue

In the dominated degree-eight centre reduction, put

\[
                         H=G-\{u,v\}.
\]

The exact seven-terminal kernel supplies a spanning `Q`-rooted residual
model in the five-connected graph `H`.  In the order-seven branch its
carrier is a six-wheel.  There are now two legitimate but inequivalent
choices.

* Forget spanningness and minimise a chosen rim bag among all rooted
  models with the same root labels.  Theorems 2.1 and 3.1 give the rooted
  path and endpoint ownership.
* Retain spanningness.  Theorem 2.2 gives only the rooted block-chain and
  a terminal leaf-block piece owning at least two labels.

The following exact quotient refinement makes the second choice sharper.

### Lemma 4.1 (finite order-seven refinement)

In every one of the 21 failed labelled order-seven compositions:

1. every literal edge of `Q` is already an edge of the labelled
   six-wheel `W`;
2. adding any one missing labelled edge to `W` produces a `K_5^-` minor;
   and
3. a rim root has at least two carrier neighbours not joined to it by a
   literal `Q` edge only when it has degree one in `Q`.

There are exactly two such rim roots in every `C_5 dotcup K_2` residue,
one in every pendant-path residue, and none in a `C_7` residue.

#### Computer-assisted proof

The deterministic
[`verify.py`](experiments/dominated_wheel_rim_bag_minimality/verify.py)
regenerates the 21 failures from the complete kernel catalogue.  It tests
all 189 missing labelled edges by exact deletion-and-contraction minor
recursion and checks the nonliteral carrier contacts at every rim label.
It reports

```text
GREEN dominated wheel rim-bag quotient residues=21 missing_edge_tests=189 vulnerable=[('FCQ`_', 20), ('FCQb_', 4), ('FCp`_', 0)]
```

Assertions enforce the per-residue counts as well as these totals.
`\square`

In a target-free host, part 2 also shows that the actual bag-adjacency
quotient of this order-seven model has no unrecorded edge: any such edge,
together with the seven rooted bags, would lift the displayed `K_5^-`
minor and then extend through `u,v` to `K_7^-`.

### Corollary 4.2 (one fixed rim label)

Fix one rim label `s` of one order-seven residual placement, and minimise
its bag among **spanning** rooted models with this fixed labelled wheel.
If `d_Q(s)>=2`, then `B_s={s}`.  If `d_Q(s)=1`, then either `B_s={s}` or
its block-cut tree is a path rooted in one end block, while its opposite
leaf-block piece owns exactly the two carrier adjacencies which are not
literal `Q` edges.

#### Proof

A root-free piece cannot own a wheel adjacency which is already the
literal edge between its retained root and another root.  A rim label has
only three wheel neighbours.  Thus `d_Q(s)>=2` leaves at most one possible
owner label.

If `B_s` were nontrivial, the construction following Theorem 2.2 would
give a root-free connected piece with connected rooted complement and one
internal attachment vertex.  Since `H` is five-connected, Theorem 2.2
forces that piece to own at least two labels, a contradiction.  This proves
the singleton assertion.  When `d_Q(s)=1`, the same argument and the
block-chain conclusion following Theorem 2.2 force the opposite leaf piece
to own both and only the two nonliteral carrier adjacencies. `\square`

Corollary 4.2 has a strict quantifier limit.  It minimises one fixed rim
bag.  Repeating it for another label may use a different spanning model:
the transfer which shrinks the new source is allowed to enlarge the first
owner bag.  Hence it does not put all six `C_7` rim roots into singleton
bags in one common model.

The rooted-path conclusion and the canonical spanning partition cannot be
retained simultaneously.  In the owner-free case, the proof of Theorem
2.1 leaves `P` outside the model.  Theorem 2.2 records exactly what replaces
that step: a piece with no foreign contact may have at least five internal
attachment vertices.  A non-cutvertex of a large source bag can likewise
have every neighbour inside that bag, so five-connectivity does not supply
a bag into which it can be moved.

Nor does five-connectivity make the rooted path short.  For a root-free
terminal interval `P`, its full neighbourhood separates `P` from every
vertex outside `P\cup N_H(P)`.  If such a far-side vertex exists, then
five-connectivity gives

\[
                            |N_H(P)|\geq5.              \tag{4.1}
\]

This is a lower bound.  If no far-side vertex exists, `N_H(P)` is not a
proper separator at all and connectivity says nothing.  Each of the two
owner labels can contribute arbitrarily many boundary vertices, and
further boundary vertices can lie in the third required neighbour bag, in
bags joined by additional actual quotient edges, or outside a nonspanning
minimum model.  Hence neither `|N_H(P)|<5` nor any fixed upper bound
follows.

The order-eight residual templates are weaker still for this particular
argument.  After the nonterminal branch set is absorbed, their owner
quotients are wheel or one-chord templates, but in general are not
six-wheels.  The source bag can have a different set of required neighbour
labels, and the catalogue only records a required spanning subgraph of the
actual bag-adjacency quotient.  Unrecorded interbag edges therefore cannot
be assumed absent.  One may apply the detachable-piece argument with the
full required neighbour set of a fixed quotient, but the special
three-label pigeonhole which forces a rooted path is then unavailable.

## 5. Precise nonclosure and smallest repair

The first unsupported inference in the proposed branch-bag transfer is

\[
 \begin{gathered}
  |\Omega(P)|\geq2,\quad \kappa(H)\geq5,\quad
  K_7^-\npreccurlyeq G
 \end{gathered}
 \Longrightarrow
 \begin{gathered}
  \text{a movable four-bag split, an order-at-most-eight labelled}\\
  \text{separation, or a source bag of order two.}
 \end{gathered}                                      \tag{5.1}
\]

The owner rule supplies labels, not distinct portal vertices.  Two owned
adjacencies may be concentrated at the same endpoint of the rooted path.
Such a vertex cannot be divided between two owner bags.  Five-connectivity
only supplies (4.1), and target exclusion by itself gives no rule carrying
the proper-minor colouring response onto `N_H(P)`.

The smallest useful repair is therefore an **operation-labelled two-owner
split theorem** for the exact residual quotient:

> Let a root-free connected and co-connected piece of one rooted residual
> branch set monopolise two required foreign adjacencies.  Using one of the
> retained proper-minor operations, either link those two owner contacts to
> distinct attachment vertices and split the piece between the owners, or
> return an actual bounded separation carrying that same operation's
> boundary partition, or construct a `Q`-rooted `K_5^-` model.

The need for distinct attachment vertices is substantive.  Static
multi-owner transfer, even under stronger connectivity, is already known
not to turn owner labels into a bounded separator.  The response label is
the missing input; another unlabelled minimum will reproduce (3.1).

## Dependencies and scope

- [the spanning residual wheel/one-chord normal form](hc7_k7minus_dominated_degree_eight_rooted_seven_carrier.md);
- [the general multi-owner portal-linkage transfer](../results/hc7_multi_owner_portal_linkage_transfer.md); and
- [the static first-hit obstruction](../barriers/hc7_multi_owner_static_first_hit_barrier.md).

This note deliberately makes no claim about the protected-centre
order-eight or order-nine kernel comparison.  Those reductions may supply
the operation label required in Section 5, but protecting one centre at a
time does not itself produce the two distinct owner portals needed here.
