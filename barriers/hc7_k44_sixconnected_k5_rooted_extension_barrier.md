# A six-connected `K_5` need not have the canonical rooted `K_7^-` extension

**Status.** Explicit counterexample to the intermediate four-support bond
claim, with a deterministic exhaustive verifier.  This is not a
counterexample to the literal `K_{4,4}` partition theorem, T44,
Norin--Totschnig Conjecture 21, or `HC_7`.

## 1. Claim refuted

The following tempting strengthening of the literal-blocker residue is
false.

> Let `X` be four-connected with minimum degree at least four.  Let
> `R_1,...,R_5 subseteq V(X)` have order at least two, and suppose every
> nonempty proper connected `W subset V(X)` satisfies
> \[
>   |N_X(W)|+|\{i:R_i\cap W\ne\varnothing\}|\ge6.             \tag{1}
> \]
> Then `X` has a bond which splits at least four of the five supports.

Equivalently, make five new vertices into a `K_5` and join its `i`th vertex
precisely to `R_i`.  Condition (1) and support multiplicity make the
augmentation six-connected, but they do not force a `K_7^-` model whose five
new clique vertices are singleton branch sets.

## 2. Construction

Let `X` be the graph obtained from the icosahedral graph by deleting one
vertex.  Relabel its remaining vertices as `0,...,10`; its graph6 code is

```text
JhfwEDbKgs_
```

The deleted vertex exposes the facial cycle

\[
                              0,4,10,6,7,0.                  \tag{2}
\]

Take

\[
\begin{aligned}
 R_1&=\{0,1,2,3,4,5,8,9\}, & R_2&=\{4,10\},\\
 R_3&=\{10,6\},             & R_4&=\{6,7\},\\
 R_5&=\{7,0\}.&&
\end{aligned}                                                   \tag{3}
\]

Thus `R_2,...,R_5` are four consecutive edges of the facial cycle (2),
while `R_1` contains the remaining edge `04` and all six vertices off that
face.

The graph `X` is planar and four-connected, and its degree sequence is

```text
4,4,4,4,4,5,5,5,5,5,5.
```

Direct exhaustion gives

\[
 \min_{\varnothing\ne W\subsetneq V(X),\ X[W]\text{ connected}}
 \left(|N_X(W)|+|\{i:R_i\cap W\ne\varnothing\}|\right)=6.    \tag{4}
\]

There are 32 oriented sets attaining equality.  For example `W={1}` has
five neighbours and meets only `R_1`.

## 3. Why four supports cannot split

In a plane graph, a bond crosses the boundary of a face at most twice.
Otherwise two arcs of each connected side occur alternately on that facial
cycle, and connected subgraphs joining the same-side arcs cross in the disk
outside the face.

Splitting one of the two-element supports `R_2,...,R_5` is exactly crossing
its edge on (2).  A bond therefore splits at most two of those four
supports.  It can split `R_1` only once as a counted support, so every bond
splits at most three supports in total.

The exhaustive bond histogram, counting an unordered bipartition once, is

| number of split supports | bonds |
|---:|---:|
| 1 | 52 |
| 2 | 172 |
| 3 | 243 |

There are no bonds with zero, four, or five split supports.

## 4. Six-connected augmentation and exact scope

Add `Q={q_1,...,q_5}`, make `Q` a clique, and join `q_i` precisely to
`R_i`.  The resulting 16-vertex, 51-edge graph has vertex-connectivity six.
Nevertheless it has no `K_7^-` model in which all five members of `Q` are
singleton branch sets: by the spanning-extension argument, such a model is
equivalent to a bond of `X` splitting four supports.

This construction retains the two most tempting generic hypotheses:
`X` itself is four-connected of minimum degree four, and the augmentation is
six-connected.  It shows that a proof of the literal blocker lemma cannot
discard the distinguished supports `R_a,R_b` and aim only for four split
`K`-supports.  The three-support mode with the correct `a,b` orientation is
essential.  The example realizes the facial-cycle obstruction in the
Chen--Ding--Yu--Zang parity-bond theorem exactly.

In fact the augmentation does contain an unrooted `K_7^-` minor.  Number the
new roots `q_1,...,q_5` according to (3).  The seven branch sets

\[
\begin{gathered}
 \{0,5,q_3,q_5\},\quad \{10\},\quad \{6\},\quad
 \{1,9,q_1\},\\
 \{2,3,8\},\quad \{7\},\quad \{4,q_2,q_4\}
\end{gathered}                                                \tag{5}
\]

are connected and have twenty contacts; the sole missing pair is
`{10}`--`{7}`.  Thus the example does not refute the still-possible unrooted
statement that every six-connected graph containing a `K_5` has a `K_7^-`
minor.

The construction also does not include supports `R_a,R_b`, the strict
minimum-blocker inequality, the distinguished eligible vertex, or the exact
three-cut incidence profiles.  It therefore does not refute the exact
nonsingleton blocker lemma.

Indeed, a solver-free finite exhaustion shows that the fixed supports (3)
cannot be extended by any nonempty `R_a,R_b` satisfying the full boundary
inequalities, `|R_a|<=5`, and failure of the exact oriented closing-bond
criterion.  Of the 1,023 possible `R_a`, only 12 leave a nonempty allowed
region for `R_b`, and none covers all 32 remaining boundary-six sets.  This
seed-specific fact is checked by the
[nonextension verifier](../active/experiments/k44_literal_spanning_split_search/verify_icosahedral_seed_nonextension.py);
it is not an unbounded theorem about facial obstructions.

## 5. Verification

Run

```text
python3 barriers/hc7_k44_sixconnected_k5_rooted_extension_barrier_verify.py
```

The verifier uses no third-party package.  It checks four-connectivity and
minimum degree of `X`, all connected-set inequalities in (4), all 467 bonds,
six-connectivity of the augmentation, absence of every rooted model of the
stated canonical form, and the unrooted model in (5).
