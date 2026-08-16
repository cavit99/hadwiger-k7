# Internal audit: contractibility of every `K_{2,n}`

Audited file:
`results/k2n_contractibility_via_matroid_packing.md`

Audited SHA-256:

```text
c8784e5d244c0e07a2d78a9a0ccb005a0c5d7dcb2f83b5d05404aaae1316249b
```

Audited Git blob: `cd0c6deb3fa26d0cda1c8d7a905029ded4b3abe6`.

**Verdict:** **GREEN** for Theorem 1.1 and its stated scope.  No unresolved
mathematical assumption or proof gap remains at the pinned revision.

This is a separate internal mathematical audit, not external peer review.

## 1. Exact external inputs

The proof uses the following results.

1. Kündgen--Pelsmajer--Ramamurthi, [*Finding minors in graphs with a given
   path structure*](https://arxiv.org/abs/1207.6141), Lemma 3.3: an
   `H`-scheme yields a coloured `H`-scheme in a rooted minor of its
   underlying graph.
2. Remark 3.2(1), (2), (6), and (7) of the same paper: colours alternate on
   a scheme path; every underlying edge belongs to exactly one scheme path;
   every non-root vertex lies on at least two scheme paths; and, if `u` has
   degree two in `H`, every vertex of colour `u` lies on each path
   `P_{uv}` incident with `u`.
3. Corollary 3.5 of the same paper: forests are contractible.  This covers
   the separately dispatched case `n=1`.
4. Edmonds' matroid-union rank formula

   \[
   r_{M_1\vee M_2}(E)
      =\min_{X\subseteq E}\bigl(|E-X|+r_1(X)+r_2(X)\bigr).
   \]

The question answered by the source is Section 8, Question 2: whether
`K_{2,4}` or `K_{3,3}` is contractible.

## 2. Projection check

Let `a,b` be the two hub roots and `t_i` a degree-two root.  Applying
Remark 3.2(7) to `P_{at_i}` and `P_{bt_i}` shows that every vertex in the
colour class `L_i` lies on both paths.  Thus every
`x\in E_i=L_i-\{t_i\}` has two distinct `a`-coloured neighbours on the
first path and two distinct `b`-coloured neighbours on the second.  The
two abstract projection edges labelled `x` are therefore well-defined.
They may be parallel to other projected edges, but neither is a loop.

On the `a` side, alternation shows that the projected path `Q_i^a` has
edge set exactly `E_i`; the same argument gives
`E(Q_i^b)=E_i`.  Since the sets `E_i` partition `E`, both path families
partition the same labelled ground set.  Every hub-coloured vertex occurs
on a scheme path incident with that hub, so the paths also cover all
vertices of their projection.  Both projection multigraphs are connected.

If an incident scheme path is the single edge from a hub to `t_i`, then
Remark 3.2(7) forces `E_i` to be empty, and the corresponding projected
path is correctly interpreted as trivial.  If `E` itself is empty, both
projections have one vertex and their empty edge sets are spanning trees.

For a non-root `a`-coloured vertex, every containing scheme path contributes
two distinct incident edges, and Remark 3.2(2) prevents double counting.
Its degree is therefore `2k` when it lies on `k` paths.  The coloured-scheme
minimum degree, equivalently Remark 3.2(6), gives `k\geq2`.  The identical
statement holds on the `b` side.

## 3. Component count and matroid union

For `X\subseteq E`, components are counted in the spanning subgraph, so
isolated projection vertices are included.  The component containing the
hub meets all `n` projected paths.  Every other component contains a
non-root projection vertex and hence meets at least two paths.  This proves
the lower incidence bound

\[
 n+2(c_a(X)-1).
\]

Deleting `Y=E-X` cuts `Q_i^a` into at most
`|E(Q_i^a)\cap Y|+1` segments.  Components of the full spanning subgraph
can only identify such segments, not create more of them.  Summing over the
edge partition gives the upper bound `n+|Y|`.  Consequently

\[
 c_a(X)\leq |Y|/2+1,
 \qquad
 c_b(X)\leq |Y|/2+1.
\]

For the two connected graphic matroids this is exactly

\[
 |E-X|+r_a(X)+r_b(X)\geq r_a(E)+r_b(E).
\]

Edmonds' formula makes the union rank equal to the sum of the two ranks.
If independent sets `I_a,I_b` realize that union rank, equality in

\[
 |I_a\cup I_b|\leq |I_a|+|I_b|
                 \leq r_a(E)+r_b(E)
\]

forces them to be disjoint bases.  Thus the conclusion really is a pair
of edge-disjoint spanning trees, not merely two spanning edge sets.

## 4. Rooted-model and trust-boundary checks

Lifting an `a`-tree edge labelled `x` to its two-edge path through `x`
makes the proposed `a`-bag connected and includes every `a`-coloured
vertex.  The `b`-bag is connected for the same reason.  Disjoint tree-label
sets and disjoint colour classes make the two bags disjoint.  Each root
`t_i` is a singleton bag, and the two scheme-path edges incident with it
join it to the corresponding hub bags.  These are precisely all required
adjacencies of a rooted `K_{2,n}` model.  Composing this model with the
root-preserving contractions from Lemma 3.3 preserves every named root.

The proof is unbounded and does not rely on finite computation.  It proves
the stated theorem conditional only on the cited published inputs.  The
audit confirms that the theorem answers the question posed in the cited
2012 paper; it does **not** establish publication priority, certify that no
later source resolved the question, or replace independent expert review.
It also leaves `K_{3,3}` and general bipartite contractibility untouched.
