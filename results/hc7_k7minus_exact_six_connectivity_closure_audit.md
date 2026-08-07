# Audit of the exact-six-connectivity closure

**Audit verdict:** **GREEN** for the theorem file with SHA-256

```text
c17ea01e3d4f1aad159ca66a75c2b1f0ab7bc589b3473d302dba0c31d4712be0
```

namely
[`hc7_k7minus_exact_six_connectivity_closure.md`](hc7_k7minus_exact_six_connectivity_closure.md).

The finite verifier has SHA-256

```text
f9fde5e2c7a40b9411665a79933f2391478417ea6c44d5b46c47a2ea1042e0a4
```

and its recorded output has SHA-256

```text
d732563c507e7c7cb6055238fadcefd68ecd0e4951eb0434062c5f7dfcff408e
```

This is an internal hostile audit, not external peer review.  The verdict is
restricted to the pinned files and the imported results named below.

---

## 1. Scope of the audit

The audited note makes three claims.

1. If
   \[
      \kappa(H)=6,\qquad |E(H)|\ge4|V(H)|-2,
   \]
   then `H` has a `K_7^-` minor.
2. Every seven-connected graph at the same density has a `K_7^-` minor.
3. Together with the repository's established critical-host entrance, every
   `K_7^-`-minor-free graph is six-colourable.

The first claim is the new mathematical core.  The second uses the audited
safe degree-seven contraction.  The third uses Mader's connectivity theorem
and three previously audited repository results.

The audit checked the proof independently from the proposed
labelled-separator-shore rank.  No statement from the unmerged terminalisation
experiment is needed.

---

## 2. Imported statements

### 2.1 Rooted `K_4` bound

Norin--Totschnig, Lemma 9, states exactly:

> If `|Q|=4`, `(F,Q)` is internally four-connected, and `F` has no
> `Q`-rooted `K_4` model, then
> \[
>                         |E(F)|\le3|V(F)|-7.
> \]

The proof uses this only through the displayed contrapositive bound.  It
works when `|V(F)|=5`; no omitted order-six hypothesis is present.

### 2.2 Rooted diamond theorem

Norin--Totschnig, Lemma 10, quotes Jørgensen's result:

> If `|V(F)|\ge6`, `|Q|=4`, and `(F,Q)` is internally four-connected,
> then `F` has a `Q`-rooted `K_4^-` model.

The theorem note invokes this only after identifying a non-singleton cut
component, so the rooted graph has at least six vertices.

### 2.3 Safe degree-seven contraction

The audited theorem
[`hc7_k7minus_degree7_safe_contraction.md`](hc7_k7minus_degree7_safe_contraction.md)
proves that in a seven-connected `K_7^-`-minor-free graph at nonnegative
`4n-2` surplus, a degree-seven vertex has an incident edge `vs` with

\[
                         |N(v)\cap N(s)|\le3,
\]

and therefore contraction does not reduce the surplus.  Its corollary
proves that a minimum-order, then minimum-size enemy has a degree-seven
vertex.  The current proof neither strengthens nor re-proves its local
neighbourhood classification.

### 2.4 Critical-host entrance

The six-colour corollary uses the already audited facts that:

- every degree-seven vertex lies in a literal `K_5`;
- a target-free six-connected graph contains at most one literal `K_5`;
- the unique literal `K_5` cannot have all five vertices of degree seven.

The linked theorem files in the audited note have the required hypotheses.
Mader's standard theorem supplies seven-connectivity of a
seven-contraction-critical graph.

No imported result assumes the new `4n-2` extremal theorem, so the dependency
graph is acyclic.

---

## 3. Six-cut accounting

Let `S` be a six-cut in a six-connected target-free graph `H`, and let
`C_1,...,C_r` be the components of `H-S`.

For every `i`,

\[
                         N_H(C_i)=S.                    \tag{3.1}
\]

If a component missed one boundary vertex, its neighbourhood would be a cut
of order at most five.  This verifies the repeated use of literal fullness.

With

\[
 \delta_i=|E(H[C_i])|+|E_H(C_i,S)|-4|C_i|
\]

and

\[
 q_H=|E(H)|-(4|V(H)|-2),
\]

the vertex and edge partitions give

\[
 \begin{aligned}
  |V(H)|&=6+\sum_i|C_i|,\\
  |E(H)|&=|E(H[S])|+\sum_i(4|C_i|+\delta_i).
 \end{aligned}
\]

Therefore

\[
                         q_H=|E(H[S])|+\sum_i\delta_i-22. \tag{3.2}
\]

The constant is `22=4\cdot6-2`; the audit found no coefficient shift.

---

## 4. Component-count branch-set templates

The following table records the literal bags used before any rooted theorem.
In every row, component fullness supplies all component-to-boundary edges.

| row | branch sets | only possible defects |
|---|---|---|
| `r\ge5` | four `C_i\cup\{s_i\}`, one bare component, two boundary singletons | the singleton pair |
| `r=4`, rich triple | three `C_i\cup\{s_i\}`, one bare component, three selected singletons | missing pairs inside the selected triple |
| `r=3`, rich four-set | two `C_i\cup\{s_i\}`, one bare component, four selected singletons | missing pairs inside the selected four-set |
| `r=2`, rich five-set | one `C_i\cup\{s\}`, one bare component, five selected singletons | missing pairs inside the selected five-set |

The absorbed boundary vertices are essential: they create the adjacencies
between otherwise anticomplete cut components.  Each construction has exactly
seven disjoint connected nonempty branch sets.

Consequences:

1. `r\ge5` is impossible.
2. For `r=4`, every boundary triple spans at most one edge.  This makes
   `H[S]` a matching.  Fullness gives each boundary vertex four exterior
   neighbours and minimum degree six gives boundary degree at least two,
   contradiction.
3. For `r=3`, every boundary four-set spans at most four edges.
4. For `r=2`, every boundary five-set spans at most eight edges.

Thus `r\in\{2,3\}`.

---

## 5. Two-component boundary audit

There are six five-subsets of a six-set.  Each boundary edge belongs to
exactly four of them.  Therefore

\[
                         4e_S\le6\cdot8=48,
 \qquad e_S\le12.                                      \tag{5.1}
\]

Two full components give every boundary vertex at least two exterior
neighbours, while minimum degree is at least six.  Hence every boundary
degree is at least four and `e_S\ge12`.

Equality in both bounds gives a four-regular six-vertex graph.  Its
complement is one-regular, so

\[
                         H[S]=K_6-3K_2.                 \tag{5.2}
\]

The finite verifier independently finds exactly fifteen labelled survivors,
the number of perfect matchings on six labelled vertices.

### Rooted composition

For a missing pair `pq`, the remaining four roots induce `K_4-2K_2`, a
four-cycle with four edges.  The rooted pair on one component and those
four roots is internally four-connected: adding `p,q` to a rooted separator
of order at most three would give a cut of `H` of order at most five.

A rooted `K_4` model would combine with:

- the other full component;
- singleton `p`;
- singleton `q`.

The vertices `p,q` are adjacent to every one of the four roots, and the only
possibly absent pair is `pq`.  The model would therefore be `K_7^-`.
The application of the rooted edge bound is valid.

### Excess arithmetic

Writing `c,e_C,P,\delta` as in the theorem, the rooted bound gives

\[
 p(p)+p(q)\ge c+\delta-1.                              \tag{5.3}
\]

The three missing pairs partition `S`, so summing gives

\[
                         P\ge3c+3\delta-3.              \tag{5.4}
\]

Connectedness gives `e_C\ge c-1`, and hence

\[
                         P=4c+\delta-e_C
                           \le3c+\delta+1.              \tag{5.5}
\]

Thus `2\delta\le4`, so `\delta\le2`.  Applying this to both components
contradicts (3.2), which requires their total excess to be at least ten.

The audit checked the inequality direction in (5.3): the omitted attachment
counts move to the right-hand side with positive sign.

---

## 6. Three-component boundary audit

Every boundary edge belongs to exactly six four-subsets, so the four-set
bound gives

\[
                         6e_S\le15\cdot4=60,
 \qquad e_S\le10.                                      \tag{6.1}
\]

All three components cannot be singletons: that would give order nine and
at most `18+10=28` edges, below `4\cdot9-2=34`.

Choose a non-singleton component.  If a boundary vertex `z` has four
boundary neighbours, the rooted pair on that component and four selected
neighbours is internally four-connected.  The rooted diamond theorem
applies.  Its four bags combine with:

- the second component plus the sixth boundary vertex;
- the third component;
- singleton `z`.

The singleton `z` meets all four rooted bags by the selected literal edges.
The only possible defect is the one inside the rooted `K_4^-` model.  Hence
maximum boundary degree is at most three.

Three full components give every boundary vertex at least three exterior
neighbours, so minimum degree six gives boundary degree at least three.
Thus the boundary is cubic and

\[
                              e_S=9.                    \tag{6.2}
\]

### Ordered-nonedge composition

A cubic graph on six vertices has two nonneighbours at every vertex and
therefore twelve ordered nonedges `(q,p)`.

For one ordered nonedge, delete `q,p` from the boundary and use the other
four vertices as roots.  A rooted `K_4` model would combine with:

- one other component plus `p`;
- the third component;
- singleton `q`.

Since `p` is one nonneighbor of the cubic-boundary vertex `q`, exactly one
of the four remaining roots can also be nonadjacent to `q`.  Thus the seven
bags have at most one missing pair.  The rooted model is correctly excluded.

### Incidence sum

In the twelve ordered nonedges:

- every boundary vertex occurs twice as the first entry and twice as the
  second, so omitted attachment counts have total coefficient four;
- the initial `12P` therefore becomes `8P`;
- the complement of a cubic six-vertex graph is two-regular;
- for a boundary edge `uv`, the four complement edges incident with `u` or
  `v` are distinct, leaving two complement edges among the other four
  vertices, i.e. four ordered nonedges;
- hence every boundary edge is counted in exactly four root graphs and the
  total root-edge term is `4e_S=36`.

Summing gives

\[
                         3e_C+2P\le9c+6.                \tag{6.3}
\]

Using `e_C\ge c-1`,

\[
                         2\delta\le7,
 \qquad \delta\le3.                                    \tag{6.4}
\]

The total component excess is at most nine, whereas (3.2) requires at least
thirteen.  This is the final contradiction.

The finite verifier checks all seventy labelled cubic six-vertex graphs and
confirms every coefficient in this sum.

---

## 7. Contraction closure audit

Let `G` be a minimum-order, then minimum-size counterexample to the
seven-connected `4n-2` statement.  The audited safe-edge theorem gives an
edge `vs` at a degree-seven vertex with at most three common neighbours.
For `H=G/vs`,

\[
                         q(H)=q(G)+3-|N(v)\cap N(s)|\ge0. \tag{7.1}
\]

The connectivity lower bound is exact.

- If a cut `X` of `H` avoids the contracted vertex, splitting that vertex
  back into the adjacent pair `v,s` inside its component cannot join two
  components of `H-X`; `X` is also a cut of `G`.
- If `X` contains the contracted vertex, replacing it by `v,s` increases
  the cut order by one and leaves exactly the same remainder.

Thus a cut of `H` of order at most five would lift to a cut of `G` of order
at most six.  Hence `\kappa(H)\ge6`.

If `\kappa(H)\ge7`, then `H` is a smaller counterexample.  Otherwise
`\kappa(H)=6`, and the new exact-six theorem applies.  There is no omitted
connectivity value.

The contraction is a proper minor and cannot create target-freeness failure
in the wrong direction: if `H` has a `K_7^-` minor, so does `G`.

---

## 8. Six-colour corollary audit

Let `G` be minor-minimal non-six-colourable and `K_7^-`-minor-free.
Mader gives `\kappa(G)\ge7`.  The three audited clique results put every
degree-seven vertex in the unique possible literal `K_5`, while excluding
five degree-seven vertices in that clique.  Therefore `n_7\le4`.

Minimum degree is seven, so

\[
                         2e(G)\ge7n_7+8(n-n_7)
                              =8n-n_7\ge8n-4.           \tag{8.1}
\]

Integrality gives `e(G)\ge4n-2`, exactly the hypothesis of the new extremal
theorem.  No parity improvement or exceptional-degree count is needed.

This proves the `K_7^-` six-colour consequence, not `HC_7`.

---

## 9. Verifier reproduction

Command:

```bash
python3 results/hc7_k7minus_exact_six_connectivity_verify.py
```

Expected output:

```text
six_vertex_graphs=32768
four_component_survivors=0
two_component_boundaries=15
two_component_edge_counts=[12]
three_component_cubic_boundaries=70
ordered_nonedge_checks=PASS
summary_sha256=2282b0fa6a51fd9318bd67126defec4a41e27957e32cdc0381a53c571945280c
ALL CHECKS PASSED
```

The script uses only the Python standard library.  It exhausts all labelled
six-vertex boundary graphs and contains no random choices.

---

## 10. Hostile checks and nonclaims

The audit specifically checked the following common failure modes.

1. **Absorbed-root omission.**  Every branch-set template includes the
   boundary vertices needed to create adjacencies between anticomplete cut
   components.
2. **Rooted model leakage.**  The omitted boundary vertices are outside the
   rooted graph, so all seven final bags are disjoint.
3. **Two missing defects.**  In the three-component ordered-nonedge model,
   the orientation ensures the singleton `q` misses at most one of the four
   roots; `p` is deliberately chosen as one of its two nonneighbours.
4. **Wrong rooted threshold.**  Lemma 9 is used with `3|V|-7`, not with the
   `4|V|-10` rooted-helper bound.
5. **Order-five base case.**  Lemma 9 permits five-vertex rooted graphs.
6. **Circularity.**  The safe contraction, degree-seven clique incidence,
   two-clique exclusion and all-degree-seven clique exclusion predate and do
   not use the new extremal theorem.
7. **Hadwiger overclaim.**  A `K_7^-` minor is not a `K_7` minor; `HC_7`
   remains open.

No unsupported global shore rank is used.

## Final verdict

For the pinned theorem and verifier, the proof of the exact-connectivity-six
statement, the reduction to the seven-connected `4n-2` theorem, and the
six-colour corollary are internally **GREEN**.
