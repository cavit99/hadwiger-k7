# The contact-only `7,6,7` three-piece quotient is not terminal

**Status:** explicit barrier/counterexample to the intermediate claim below;
[separate internal audit GREEN](hc7_k7minus_three_piece_767_quotient_barrier_audit.md)
and deterministically verified by
[`probe_three_piece_terminal.py`](../active/experiments/feedback_forest_boundary_gate/probe_three_piece_terminal.py).
It is not a counterexample to the `K_7^-` six-colour conjecture or to the
critical-host three-piece composition problem.

## Refuted claim

The following finite quotient assertion is false.

> Let `T` be a graph of order at most fourteen with `chi(T)>=5`.  Add three
> vertices `a,b,c` which induce the path `a-b-c`, where
>
> \[
>   |N_T(a)|\geq7,\qquad |N_T(b)|\geq6,
>   \qquad |N_T(c)|\geq7.
> \]
>
> If the resulting graph has no `K_5` subgraph, then it contains a
> `K_7^-` minor.

The counterexample has a connected boundary of order eleven and fourteen
vertices in total.  Each of the three added vertices has degree exactly
eight.

## Construction

Let `p,q` span a `K_2`, let

\[
                         r_0r_1r_2r_3r_4r_0
\]

be a `C_5`, and take their join.  Add four further boundary vertices
`l_1,...,l_4`, each adjacent within the boundary only to `p`.  Thus

\[
 T=(K_2\vee C_5)+\{pl_i:1\leq i\leq4\},             \tag{2.1}
\]

where the four `l_i` are otherwise independent.

Add an induced path `a-b-c` and prescribe

\[
 \begin{aligned}
 N_T(a)=N_T(c)&=\{p,q,r_0,l_1,l_2,l_3,l_4\},\\
 N_T(b)&=\{p,q,l_1,l_2,l_3,l_4\}.
 \end{aligned}                                      \tag{2.2}
\]

There are no other edges.  Call the resulting graph `Q`.

The boundary is connected and has order eleven.  Since
`chi(K_2\vee C_5)=2+3=5` and the four added boundary vertices are pendant,

\[
                              \chi(T)=5.              \tag{2.3}
\]

Equation (2.2) gives the exact contact sequence `7,6,7`; together with the
two path edges it also gives

\[
                         d_Q(a)=d_Q(b)=d_Q(c)=8.       \tag{2.4}
\]

## No literal `K_5`

The largest clique in `T` has order four.  A clique using `a` or `c` has
order at most four because the corresponding open neighbourhood has clique
number three.  For example, its only triangles are of the forms

\[
        \{p,q,r_0\},\qquad \{p,q,b\},\qquad
        \{p,b,l_i\},                                  \tag{3.1}
\]

with the symmetric list at `c`.  The open neighbourhood of `b` also has
clique number three: `a,c` are nonadjacent, `q` misses every `l_i`, and the
`l_i` are pairwise nonadjacent.  Hence

\[
                              \omega(Q)=4.             \tag{3.2}
\]

In particular, `Q` contains no `K_5` subgraph.

## Width-four certificate

The following bags form a tree decomposition.  First take the path

\[
 \begin{aligned}
 K_3&=\{p,q,r_0,r_3,r_4\},\\
 K_2&=\{p,q,r_0,r_2,r_3\},\\
 K_1&=\{p,q,r_0,r_1,r_2\},\\
 E&=\{p,q,r_0,a,c\},\\
 D&=\{p,q,a,b,c\},
 \end{aligned}
 \qquad
 K_3-K_2-K_1-E-D.                                   \tag{4.1}
\]

For each `i`, attach the leaf bag

\[
                         L_i=\{p,a,b,c,l_i\}          \tag{4.2}
\]

to `D`.  Every edge of `Q` lies in a displayed bag, and the bags containing
any fixed vertex induce a connected subtree.  All bags have order five, so

\[
                              \operatorname{tw}(Q)\leq4.          \tag{4.3}
\]

The graph `K_7^-` contains a `K_6` subgraph and therefore has treewidth at
least five.  Treewidth is minor-monotone, so (4.3) proves

\[
                              K_7^-\npreccurlyeq Q.    \tag{4.4}
\]

This is a structural certificate, not an inference from a failed minor
search.

## Reproduction

From the repository root, run

```text
python3 -B \
  active/experiments/feedback_forest_boundary_gate/probe_three_piece_terminal.py
```

The deterministic script reconstructs the graph, verifies its chromatic
number, clique number, contact sizes and tree-decomposition axioms, and
prints

```text
boundary_order=11
host_order=14
pendant_count=4
outer_core=(0, 1, 2)
middle_core=(0, 1)
pendants=(7, 8, 9, 10)
contacts=(7, 6, 7)
maximum_clique=4
treewidth_upper_bound=4
graph6=M~vNKA?_C?[No^w]_
COUNTEREXAMPLE_TO_CONTACT_ONLY_767_QUOTIENT
```

## Exact scope and next useful hypothesis

The construction shows that boundary order, five-chromaticity, absence of
a literal `K_5`, the induced exterior path and even exact degree eight at
the three contracted pieces do not force the target minor.

It does not satisfy seven-connectivity and carries none of the labelled
six-coordinate colouring responses, the common cycle through the selected
edges, or the co-bagged spanning `K_6` model available in the critical
host.  It therefore does not refute a host-level theorem using those data.
The next viable composition statement must spend at least one of them; a
larger census of contact-only quotients cannot prove the desired theorem.
