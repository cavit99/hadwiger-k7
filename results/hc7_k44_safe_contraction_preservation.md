# What a safe literal-core contraction preserves

**Status.** Written proof with a separate hash-pinned internal audit.
Sections 1–3 contain
unbounded elementary deductions; Section 4 records a route nonclosure in a
conditional induction claim. Section 5 gives a counterexample only to
unconditional ambient-connectivity preservation. None closes a literal
residue, proves T44 or Conjecture 21, or proves `HC_7`.

Let `S=S_0 dotcup S_1` induce `K_{4,4}` in a finite simple graph `G`, and
put `C=G-S`. For nonempty `W subseteq V(C)`, define

\[
 \lambda(W)=|N_C(W)|+|N_G(W)\cap S|.
\]

Safety has its existing meaning: a union-labelled exterior edge contraction
preserves three-connectivity of the exterior and all inequalities
`lambda(W)>=7`, including the full-set inequality.

## 1. A connectivity criterion

**Lemma 1.** Suppose `C` is three-connected, every nonempty exterior set
satisfies `lambda(W)>=7`, and every vertex of `S` has degree at least seven
in `G`. Then `G` is seven-connected.

**Proof.** Suppose a set `Z` of at most six vertices disconnects `G`.
Every component of `G-Z` meets `S`: otherwise its vertex set `W` is an
exterior set with `lambda(W)=|N_G(W)|<=6`. If both literal shores have
surviving vertices, all surviving core vertices lie in one component by
the complete cross-shore adjacency, a contradiction. Thus `Z` contains
an entire four-vertex shore. It deletes at most two exterior vertices, so
the surviving exterior is nonempty and connected. Every other component
consists entirely of vertices of the opposite core shore. That shore is
independent, so each such component is a singleton `s`. All neighbours of
`s` then lie in `Z`, contradicting `d_G(s)>=7`. \(\square\)

**Theorem 2.** Let `G` be seven-connected and `K_7^-`-minor-free, with an
induced literal `K_{4,4}` on `S`. Suppose every core vertex has degree at
least eight. If `e` is a safe exterior edge, then `G/e` is seven-connected,
is target-free, and retains the same induced literal core.

**Proof.** The core is untouched by an exterior contraction. Each core
degree falls by at most one, so its new degree is at least seven. Safety
supplies the other hypotheses of Lemma 1 in the quotient. Minor exclusion
is preserved by taking a minor. \(\square\)

## 2. The critical-host consequence

Call `G` seven-contraction-critical when `chi(G)=7` and every proper minor
is six-colourable. The audited
[degree-seven exclusion](../results/hc7_k7minus_degree7_rooted_helper_closure.md)
gives `delta(G)>=8` for a target-free such graph.

**Lemma 3.** If a target-free graph has a literal `K_{4,4}` on `S`, its
exterior is connected, and every core vertex has an exterior neighbour,
then `G[S]` is exactly the displayed `K_{4,4}`.

**Proof.** Suppose `xy` is an additional edge in one shore. Contract two
disjoint cross-shore edges incident with the other two vertices of that
shore. The six resulting core bags form a `K_6^-` model: the mixed bags are
universal, `x,y` are adjacent, and the sole possible missing contact is between the
two remaining vertices of the opposite shore. Use the whole connected
exterior as a seventh bag. It meets every core bag, giving `K_7^-`.
\(\square\)

**Corollary 4.** In the hypotheses of the audited
[critical safe-contraction theorem](../results/hc7_k44_critical_safe_contraction.md),
every core vertex has degree at least nine, and every safe exterior
contraction is seven-connected.

**Proof.** The audited exterior theorem makes `C` three-connected. Since
`delta(G)>=8` and `|S|=8`, every core vertex has an exterior neighbour.
Lemma 3 makes the core induced. For each `s in S`, the opposite shore is
an independent four-set in `N_G(s)`. Dirac's neighbourhood inequality,
quoted as Theorem 15 in
[Norin--Totschnig](https://arxiv.org/html/2507.03244v1), gives
`4<=alpha(G[N_G(s)])<=d_G(s)-5`, so `d_G(s)>=9`.
Apply Theorem 2. \(\square\)

This adds a conclusion to the existing theorem; its proof of one safe edge
and its six-colouring corollary are unchanged. The quotient is still
six-colourable and therefore is not seven-contraction-critical.

## 3. A second safe edge, with an explicit stopping point

**Lemma 5.** If `G` is seven-contraction-critical with `delta(G)>=8`, no
single-edge contraction `H=G/uv` has a degree-seven vertex whose
neighbourhood is bipartite with class orders three and four.

**Proof.** Write `z` for the contracted vertex. Suppose first that the
degree-seven vertex is `x!=z`. Its original degree is at most eight, hence
exactly eight. An independent four-set in `H[N_H(x)]` lifts to an
independent four-set in `G[N_G(x)]`: if it contains `z`, replace `z` by
either adjacent original endpoint. No edge to the other three vertices
can appear, since such an edge would have survived contraction. Dirac's
inequality gives `alpha(G[N_G(x)])<=d_G(x)-5=3`, a contradiction.

If the vertex is `z`, each of `u,v` has all its neighbours among the other
endpoint and the seven vertices of `N_H(z)`. Minimum degree eight forces
both degrees to equal eight and both endpoints to meet all seven vertices.
The independent four-set in that unchanged seven-vertex graph again
contradicts Dirac's inequality at `u`. \(\square\)

**Corollary 6.** Under Corollary 4, if the original exterior has order at
least eight, the quotient after a first safe edge contains a second safe
exterior edge. Contracting any such second safe edge again gives a
seven-connected target-free graph with the same induced literal core.

**Proof.** Corollary 4 gives a seven-connected target-free quotient with
the same literal core and exterior order at least seven. If it had no safe
edge, the audited
[singleton-atom theorem](../results/hc7_k44_positive_atom_elimination.md),
Theorem 1.1(6), would produce the vertex excluded by Lemma 5. Every core
vertex originally had degree at least nine by Corollary 4, so its degree
after the first contraction is at least eight. Theorem 2 therefore applies
to any second safe edge and proves the preservation claim. \(\square\)

This does not supply arbitrary iteration. After the second contraction the
proved lower bound on core degrees is only seven, and Lemma 5 treats one original edge,
not an arbitrary connected branch set or two disjoint contracted edges.
Neither a third safe edge nor a closed inductive class is proved here.

## 4. The separate pure-labelled induction gap

**Status: recorded negative finding / route nonclosure, not a
counterexample.** The [small-atom reduction](../results/hc7_k44_weighted_splitter_small_atom_reduction.md)
is stated for purely labelled exteriors. Its conditional completion lemma
at lines 592–598 has those same hypotheses, so the induction at lines
600–605 is correctly conditional on a purely labelled completion theorem.
Its terminal-lifting lemma, lines 109–124, preserves the three specified
labelled configurations.

The [later singleton-atom theorem](../results/hc7_k44_positive_atom_elimination.md)
instead assumes a seven-connected target-free ambient literal host.
For example, its lines 603–608 use ambient seven-connectivity to obtain
seven disjoint boundary-to-core paths. Its open completion lemma at lines
1100–1104 retains those host hypotheses, but lines 1107–1111 then propose
safe contraction and induction to close the literal case.

The first unsupported inference is reapplying that ambient-host completion
after a merely safe labelled contraction: safety preserves neither ambient
seven-connectivity by definition nor a purely labelled version of the
later completion theorem. Conversely, absence of the three labelled
terminal configurations does not, as a proved input, imply absence of every
`K_7^-` model in an arbitrary reconstructed host.

The smallest repair is either a completion theorem with the original
purely labelled hypotheses and one of the three labelled conclusions, or
an ambient induction theorem preserving its full hypothesis class at every
step. The critical one- and two-step statements above provide neither.
This does not refute any displayed proved atom theorem, either literal
residue, the labelled trichotomy, the literal case, or T44.

## 5. Why unconditional connectivity preservation is false

The [explicit connectivity barrier](../barriers/hc7_k44_safe_contraction_connectivity_barrier.md)
has a seven-connected literal host and a safe exterior edge whose quotient
has connectivity six. It contains `K_7` and all three labelled terminal
configurations. It refutes only unconditional preservation, not a
target-free or terminal-free refinement and not Theorem 2.
