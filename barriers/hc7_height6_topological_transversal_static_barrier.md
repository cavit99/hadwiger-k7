# Static barrier to the height-six topological-transversal exchange

**Status:** computer-assisted finite barrier with a deterministic verifier;
separately audited in
[`hc7_height6_topological_transversal_static_barrier_audit.md`](hc7_height6_topological_transversal_static_barrier_audit.md).
This is not a counterexample to the proposed height-six theorem or to
`HC_7`.

## 1. The inference ruled out

For a graph `G`, let `T_{<=6}(G)` be the family of supports of all
subdivisions of `K_5` using at most six vertices.  For a two-set `P`, put

\[
 \theta_G(P)=\min\{|V(T)|:T\subseteq G-P\text{ is a subdivision of }K_5\},
 \tag{1.1}
\]

with value infinity if no such subdivision exists, and let `Theta_5(G)`
be the maximum over all two-sets.

The height-six programme hoped that the following static data might force
a global pair exchange:

- `G` has no `K_7` minor;
- `tau(T_{<=6}(G))>2` and `Theta_5(G)=6`;
- a relative-minimal family of six-vertex topological `K_5` supports has
  globally maximizing private pairs; and
- every selected support has one of the three topological deficiency
  types `(1,1,2)`, `(1,2,1)`, `(1,3,0)`.

The graph below satisfies all of this static information.  Thus the
topological restriction and the complete small-support family do not by
themselves produce a two-vertex transversal.  At least one additional
full-host input absent from the example, such as seven-connectivity or
operation-specific critical responses, must be used essentially.

## 2. The graph and complete topological family

Let `J` be the graph on vertices `0,...,14` with graph6 encoding

```text
Nwf_POKE?sdkR~KV|VW
```

It has 15 vertices and 50 edges.  Exact enumeration gives

\[
 \begin{array}{c|r}
 \text{literal `K_5` supports}&3\\
 \text{six-vertex `TK_5` supports}&48\\
 |T_{\le6}(J)|&51.
 \end{array}                                           \tag{2.1}
\]

Every vertex pair misses one of these 51 supports, while

\[
                              \{0,4,12\}               \tag{2.2}
\]

meets all of them.  Hence

\[
                       \tau(T_{\le6}(J))=3.             \tag{2.3}
\]

The adjacent verifier constructs the family from the definition rather
than reading a stored list.

## 3. A relative-minimal topological kernel

The following table gives six members `A_i` of the complete six-vertex
family, one subdivided segment in each, its deficiency type when the first
half-edge is used as the two-vertex branch set, and a private pair `P_i`.

\[
\begin{array}{c|c|c|c}
i&A_i&\text{subdivided segment}&P_i\\ \hline
1&\{0,1,2,5,8,14\}&5-8-14&\{3,12\}\\
2&\{0,4,5,8,11,12\}&4-0-5&\{13,14\}\\
3&\{2,5,7,11,12,13\}&2-5-12&\{4,14\}\\
4&\{3,4,9,10,11,13\}&4-11-13&\{0,12\}\\
5&\{4,7,9,10,12,13\}&4-7-13&\{11,14\}\\
6&\{4,9,11,12,13,14\}&4-11-13&\{5,10\}
\end{array}                                            \tag{3.1}
\]

The first, second and fourth supports have type `(1,3,0)`; the other three
have type `(1,2,1)`.
No selected support has the non-topological type `(2,2,0)`.
For each selected six-set, the displayed subdivided segment is its unique
spanning `TK_5` witness, up to reversing the two branch endpoints; none of
the six-sets contains a literal `K_5`.

Let `F_5(J)` be the three literal `K_5` supports and put

\[
                         C=\{A_1,\ldots,A_6\}.         \tag{3.2}
\]

Exact enumeration also gives

\[
                    \tau(F_5(J)\cup C)=3.             \tag{3.3}
\]

For every `i`, the pair `P_i` is disjoint from `A_i` and meets every
member of

\[
                         F_5(J)\cup(C-\{A_i\}).        \tag{3.4}
\]

Equations (3.3)--(3.4) show that `C` is inclusion-minimal relative to the
full literal-clique family with transversal number greater than two.
They also give

\[
                       \theta_J(P_i)=6=\Theta_5(J)     \tag{3.5}

\]

for every `i`: each `P_i` meets every literal `K_5`, its avoided `A_i`
supplies a six-vertex subdivision, and every pair avoids some member of
the complete family in (2.1).  The chosen private pairs include disjoint
pairs, so this example enters the separated private-pair branch of the
existing support-six machinery rather than a bounded star or triangle
shortcut.

## 4. `K_7`-minor exclusion

The following are bags of a tree decomposition of `J`:

```text
B0 = 3 4 9 10 13
B1 = 4 6 10 12 14
B2 = 4 10 12 13 14
B3 = 0 1 2 5 12 14
B4 = 0 2 4 5 12 14
B5 = 2 4 5 11 12 14
B6 = 2 4 7 11 12 13
B7 = 2 4 11 12 13 14
B8 = 4 5 8 11 12 14
B9 = 4 9 10 12 13 14
```

The decomposition tree has edges

```text
B7B5 B5B4 B5B8 B4B3 B7B6 B7B2 B2B9 B2B1 B9B0.
```

Every bag has order at most six.  The verifier checks edge coverage and
the running-intersection property, so `tw(J)<=5`.  Since treewidth is
minor-monotone and `tw(K_7)=6`, the graph has no `K_7` minor.

For completeness, `J` is exactly five-chromatic.  It contains a literal
`K_5`, and the following are five independent colour classes:

\[
 \{2,3,12\},\quad \{4,5,13\},\quad \{11,14\},\quad
 \{1,7,8,10\},\quad \{0,6,9\}.                       \tag{4.1}
\]

Deleting `{4,9,10,13}` isolates vertex `3`, so the graph is not
seven-connected.

## 5. Exact scope

This graph proves that all of the following can coexist without yielding a
two-vertex transversal:

- the **complete**, rather than sampled, family of topological `K_5`
  supports through order six;
- global pair height exactly six;
- a relative-minimal family with private maximizing pairs;
- only topological split types; and
- global `K_7`-minor exclusion.

It does not refute the first-rung topological-transversal theorem for a
hypothetical minimal counterexample.  The graph is five-chromatic, is not
seven-connected, and does not satisfy the seven-chromatic
contraction-critical hypotheses from which the required operation responses
are derived.

The missing positive input is therefore not another static classification
of six-vertex subdivisions.  One credible continuation is a whole-family
composition of the operation-coupled responses supplied, for one selected
support, by the
[clean-bypass theorem](../results/hc7_height6_topological_clean_bypass.md);
a genuinely global seven-connectivity or bridge argument could serve the
same role.  Until some host-level theorem produces a pair meeting the
complete family, further static or one-support height-six work should remain
frozen.

## 6. Verification

Run

```text
uv run barriers/hc7_height6_topological_transversal_static_barrier_verify.py
```

The script independently reconstructs all 51 supports, verifies their
transversal number, checks the relative kernel and deficiency types, and
checks the tree decomposition and five-colouring.
