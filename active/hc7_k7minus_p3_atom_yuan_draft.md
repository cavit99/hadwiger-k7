# The four-distinct-miss `P_3` atom

**Status:** active draft; written reduction with a computer-assisted finite
lemma and a separate internal audit.  This result is conditional on the
generalised-atom entrance stated below.  It is not a proof of the `4n-2`
extremal target.

Here `K_7^-` denotes `K_7` with one edge deleted.  For a graph `G` of order
`n`, put

\[
                   q(G)=|E(G)|-(4n-2).
\]

For an edge `xy`, write `c(xy)=|N(x)\cap N(y)|`.  Since

\[
                   q(G/xy)=q(G)+3-c(xy),                 \tag{1}
\]

call `xy` **density-safe** when `c(xy)<=q(G)+3`, and put

\[
 \mathcal X=\{\{x,y\}:xy\in E(G)\text{ is density-safe}\}.
\]

An `\mathcal X`-fragment and `\mathcal X`-atom have Mader's standard
meanings: the relevant minimum separator contains a member of `\mathcal X`,
and an atom is a fragment of minimum order among all such fragments.

## 1. Statement

### Theorem 1.1 (the four-distinct-miss path is impossible)

Let `G` be a finite seven-connected `K_7^-`-minor-free graph with
`q(G)>=1`.  Suppose that `G` is `\mathcal X`-critical and let `A` be an
`\mathcal X`-atom of order three.  It is impossible that

\[
                         G[A]=a-b-c,                       \tag{2}
\]

all three vertices have degree seven, and, writing `S=N(A)`, there are four
distinct vertices `alpha,beta,gamma,delta in S` such that

\[
\begin{aligned}
 N(a)\cap S&=S-\{\alpha\},\\
 N(b)\cap S&=S-\{\beta,\delta\},\\
 N(c)\cap S&=S-\{\gamma\}.
\end{aligned}                                               \tag{3}
\]

The theorem eliminates one complete non-singleton atom type.  It does not
eliminate a singleton atom or the associated nested root-swap obstruction.

## 2. The finite boundary lemma

For a graph `B` on the labelled set `S` and distinct labels
`alpha,beta,gamma,delta`, form two graphs.

- `J_2(B)` adds two nonadjacent vertices, each complete to `S`.
- `J_P(B)` adds the path `a-b-c` with the incidences in (3), and one
  further vertex complete to `S` and anticomplete to the path.

For `s in S`, call `s` **good** if one of its incident edges to the path in
`J_P(B)` has at most four common neighbours.  These common-neighbour counts
are determined by `B`:

\[
\begin{aligned}
 c(as)&=d_B(s)-[s\alpha\in E(B)]+[s\notin\{\beta,\delta\}],
       &&s\ne\alpha,\\
 c(bs)&=d_B(s)-[s\beta\in E(B)]-[s\delta\in E(B)]
       +[s\ne\alpha]+[s\ne\gamma],
       &&s\notin\{\beta,\delta\},\\
 c(cs)&=d_B(s)-[s\gamma\in E(B)]+[s\notin\{\beta,\delta\}],
       &&s\ne\gamma.
\end{aligned}                                               \tag{4}
\]

Here `[P]` is one when `P` holds and zero otherwise.

### Lemma 2.1 (finite path-boundary alternative)

For every `B` and every choice of the four distinct labels, at least one of
the following holds:

1. `J_2(B)` contains a `K_7^-` minor;
2. at most two vertices of `S` are not good; or
3. `J_P(B)` contains a `K_7^-` minor.

### Verification

The retained verifier is
[`hc7_k7minus_p3_atom_yuan_verify.py`](hc7_k7minus_p3_atom_yuan_verify.py).
It enumerates the 1,044 unlabelled seven-vertex graphs in the NetworkX graph
atlas and all `7P4=840` role assignments.  Its minor test is an exact search
over spanning partitions into seven nonempty connected branch sets, accepting
only partitions with at most one missing pair of branch-set adjacencies.  It
therefore tests `K_7^-`, not `K_7^\vee`.  Every minor model in a connected
graph can be enlarged to a spanning model, so the spanning restriction loses
nothing.

Run

```text
uv run --with networkx==3.6.1 python \
  active/hc7_k7minus_p3_atom_yuan_verify.py
```

Expected output:

```text
networkx_version=3.6.1
atlas_boundaries=1044
role_assignments_per_boundary=840
two_packet_target_free_boundaries=700
non_good_distribution=(451944, 121820, 14128, 108)
three_non_good_cases=108
three_non_good_graph6=FD^Ww
expanded_P3_K7minus_certificates=108
expanded_P3_survivors=0
triangle_q1_static_survivors=('J???B}~r~{?', 'J???B}nr~{?')
exceptional_digest=3945e33ab729bfd1c709fcc3a326620f222de6a178a93dec60bae6cbdcd183ec
certificate_digest=1538af1f3ad9c958dc6411c2bbfb346b762ddacbaa8115f0478a90bf1a8e03d4
```

The checker regenerates and independently validates an explicit branch-set
certificate for each of the 108 exceptional labelled cases.  All 108 have
the same unlabelled boundary `FD^Ww`, of degree sequence
`(5,5,5,3,2,2,2)`, and none survives after the path is restored.  This proves
Lemma 2.1.

## 3. From a good boundary vertex to a critical vertex

Put `H=G-A`.  We first record two consequences of the atom hypotheses.

Because `G` is `\mathcal X`-critical, the defining crossing separator for
the `\mathcal X`-fragment `A` meets `A` and contains a member of
`\mathcal X` inside `A\cup S`.  Mader's atom crossing lemma therefore puts
all of `A` in that order-seven separator.  Deleting `A` from it gives a
four-vertex separator of `H`.  Deleting three vertices from a
seven-connected graph lowers connectivity by at most three, and hence

\[
                            \kappa(H)=4.                 \tag{5}
\]

The edges `ab` and `bc` each have exactly four common neighbours: in (3)
their common boundary neighbourhoods are respectively

\[
 S-\{\alpha,\beta,\delta\},\qquad
 S-\{\beta,\gamma,\delta\}.
\]

Thus both edges are density-safe because `q(G)>=1`.

Let `F` be any fragment of `H`, and put `T=N_H(F)`, so `|T|=4`.  If some
vertex of `A` had no neighbour in `F`, then

\[
                         T\cup N_G(F)\cap A
\]

would be a separator of `G` of order at most six.  Therefore every vertex
of `A` has a neighbour in `F`, and

\[
                         N_G(F)=T\cup A.                 \tag{6}
\]

The separator in (6) contains the density-safe edge `ab`; hence `F` is an
`\mathcal X`-fragment of `G`, with `A\subseteq N_G(F)`.  Mader's atom trace
lemma gives

\[
                         |F\cap S|\ge |A|=3.             \tag{7}
\]

This applies to every fragment of `H`, including its complementary
fragment.

Now let `s in S` be good.  Choose `x in A` such that `xs` has at most four
common neighbours.  Equation (1) and `q(G)>=1` show that `xs` is
density-safe.  The first condition in `\mathcal X`-criticality supplies an
order-seven separator `Q` containing `x` and `s`.  It meets the atom and its
intersection with `A\cup S` contains the member `\{x,s\}` of `\mathcal X`.
Mader's atom crossing lemma therefore gives `A\subseteq Q`.  Consequently
`Q-A` is a four-vertex separator of `H` containing `s`.  It follows that

\[
                           \kappa(H-s)=3.                \tag{8}
\]

The lower bound in (8) follows by deleting one vertex from the
four-connected graph `H`.  Thus every good boundary vertex is a critical
vertex of `H`.

## 4. Yuan's fragment theorem and the final uncrossing

Choose any component `D` of `G-S` other than `A`.  Seven-connectivity makes
both `A` and `D` adjacent to every vertex of `S`.  Contracting each component
to one vertex gives `J_2(G[S])` as a minor.  If outcome 1 of Lemma 2.1 holds,
then `G` contains `K_7^-`.  If outcome 3 holds, retain the path `A` and
contract only `D`; the resulting minor contains `J_P(G[S])`.  Both outcomes
contradict the hypothesis on `G`.

We may therefore assume that the set `Z` of non-good boundary vertices has
order at most two.  Put

\[
                              W=S-Z.
\]

By (7), every fragment of `H` meets `W`.  By (5) and (8),

\[
 \kappa(H)=4,
 \qquad
 \kappa(H-w)=3\quad\text{for every }w\in W.
\]

We also verify the local fragment condition after deleting `w`.  Let `D`
be a fragment of `H-w`, and put `K=N_{H-w}(D)`, so `|K|=3`.  Suppose that
`D` misses `W-\{w\}`.  Its neighbourhood in `G` is contained in

\[
                              K\cup A\cup\{w\}.
\]

Seven-connectivity forces equality: omitting any member of `A\cup\{w\}`
would give a separator of order at most six.  Choose the density-safe edge
`xw` witnessing that `w` is good.  The exact seven-separator
`K\cup A\cup\{w\}` contains `xw`, so `D` is an `\mathcal X`-fragment and
`A\subseteq N_G(D)`.  Mader's trace lemma gives `|D\cap S|>=3`.  But
`w\notin D` and `D` misses `W-\{w\}`, so `D\cap S\subseteq Z`, contrary to
`|Z|<=2`.  Hence every fragment of `H-w` meets `W-\{w\}`.

Thus `H` is a noncomplete `W`-locally `1`-critical four-connected graph in
Yuan's terminology.  Yuan's fragment theorem gives four fragments
`F_1,F_2,F_3,F_4` of `H` for which

\[
                  F_1\cap W,\ldots,F_4\cap W
        \quad\text{are pairwise disjoint}.              \tag{9}
\]

The graph `H` is noncomplete.  Otherwise (5) gives `H=K_5`, so `G` has eight
vertices; seven-connectivity would then give `G=K_8`, which contains
`K_7^-`.

If `|Z|<=1`, then (7) gives `|F_i\cap W|>=2` for every `i`, contrary to
(9), since `|W|<=7`.

It remains that `|Z|=2`.  Each of the four sets in (9) is nonempty and they
are contained in the five-set `W`.  At least three therefore have order one.
For each such fragment, (7) forces both vertices of `Z` to lie in the
fragment.  Choose two of them, say `F` and `F'`.  Then

\[
                           F\cap F'\ne\varnothing.       \tag{10}
\]

Write `\widetilde F=V(H)-(F\cup N_H(F))`, and similarly for `F'`.  If
`\widetilde F` and `\widetilde F'` were disjoint, then their intersections
with `S` would be disjoint.  Each has order at least three by (7), and both
are contained in the five-set `W`, because the two vertices of `Z` lie in
`F\cap F'`.  This is impossible.  Hence

\[
               \widetilde F\cap\widetilde F'\ne\varnothing. \tag{11}
\]

The standard fragment uncrossing lemma applied to (10)--(11) says that
`F\cap F'` is again a fragment of `H`.  But (9) gives

\[
                         (F\cap F')\cap W=\varnothing,
\]

contrary to the defining property of the `W`-locally critical graph `H`.
This proves Theorem 1.1.  `\square`

## External inputs and trust boundary

- The atom crossing and trace results are Mader's generalised atom lemmas,
  in the explicit formulation of T. L. Chan, *Contractible edges*, doctoral
  dissertation, University of Hamburg (2016), Lemmas 7.7 and 7.19.  Chan
  cites W. Mader, *Generalizations of critical connectivity of graphs*,
  Discrete Mathematics **72** (1988), 267--283.
- The fragment theorem is X. Yuan, *A note on fragments in a locally
  k-critical n-connected graph*, Ars Combinatoria **93** (2009), 25--31,
  Theorem 3.  Its definition uses `|W'|<=k`; in the present `k=1` application
  both `W'=emptyset` and all singleton deletions are checked in (5) and (8).
- Lemma 2.1 is computer-assisted.  Its unbounded use is justified by the
  written contraction to the literal seven-vertex boundary in Section 4.
  The verifier uses NetworkX only for its fixed graph atlas; the minor search,
  model generation and certificate validation are implemented directly.

## Scope

The proof does not use a finite order bound for `G`; only the boundary in
Lemma 2.1 has fixed order.  The result removes the last four-distinct-miss
degree-seven path atom.  It does not by itself prove that a density-safe edge
is seven-contractible.  The remaining atom/root-swap case must still yield an
explicit `K_7^-` model, a density-preserving seven-connected contraction, or
an exact contradiction among the singleton cut certificates.

The analogous order-three triangle atom is not closed by the same static
quotient argument.  At `q(G)=1`, absence of a density-safe internal triangle
edge leaves, up to relabelling, the two miss patterns

\[
 (\{0\},\{1\},\{2,3\}),\qquad
 (\{0\},\{1,3\},\{2,3\}).
\]

With an edgeless seven-vertex boundary and one opposite boundary-full vertex,
both expanded quotients are `K_7^-`-minor-free; the verifier checks these two
explicit constructions.  More importantly, without a fixed density-safe
edge in the lifted seven-separator, an ordinary fragment of `G-A` need not be
an `\mathcal X`-fragment, so the trace bound (7) cannot be invoked.  This
refutes only quotient-only or unlabelled-fragment closure of the triangle
case.  It does not refute a dynamic proof using the protecting separators of
boundary edges or a different eligible-family argument.
