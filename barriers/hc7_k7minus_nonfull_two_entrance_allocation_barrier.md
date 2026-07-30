# Two entrances do not force the third connected subgraph

**Status:** explicit barrier to a topology-only intermediate claim;
deterministic verifier retained.  This graph contains an explicit
`K_7`-minor model and is exactly five-chromatic.  It is therefore not a counterexample to
the critical-host hypotheses `(H)` or to the `K_7^-` six-colour conjecture.

## 1. The refuted shortcut

The following implication is false without using `K_7^-`-minor exclusion
or operation-specific proper-minor colourings:

> At the one-nonfull order-seven cut, seven-connectivity, packing vector
> `(1,2)`, four boundary neighbours of the missed vertex, and two distinct
> neighbours entering the full exterior component force two disjoint
> boundary-full connected subgraphs together with a third disjoint
> connected subgraph adjacent to at least five boundary vertices.

The boundary and exceptional-neighbourhood conditions from the live
one-nonfull reduction do not repair this static inference.

## 2. Construction

Let

\[
 S=\{s_0,\ldots,s_6\},\qquad A=\{s_1,s_2,s_3,s_4\},
\]

and put the following eight edges in `G[S]`:

\[
 s_0s_3,s_0s_4,s_0s_6,s_1s_5,s_1s_6,s_2s_5,s_3s_4,s_5s_6.
                                                               \tag{1}
\]

Thus `G[S]` has graph6 code `FCdeG`, one of the 28 exact one-nonfull
boundary types.

Add vertices `u,x,e_0,e_1,a,b`.  Their remaining adjacencies are:

\[
\begin{aligned}
 N(u)&=S\cup\{x\},\\
 N(x)-\{u\}&=A\cup\{a,b\},\\
 N(e_0)\cap S&=S, & N(e_1)\cap S&=S-\{s_1\},\\
 N(a)\cap S&=A\cup\{s_0\},
 &N(b)\cap S&=A\cup\{s_5,s_6\}.
\end{aligned}                                               \tag{2}
\]

Add the edges `e_0e_1` and `ab`, and no other edges.

The vertex `u` has degree eight and

\[
 X=N(u)=S\cup\{x\}.
\]

The graph `G[X]` is `K_4`-free and has independence number three.  Moreover,

\[
 G-N[u]=E\mathbin{\dot\cup}F,
 \qquad E=G[\{e_0,e_1\}],\quad F=G[\{a,b\}].             \tag{3}
\]

The component `E` misses `x`, while `F` is adjacent to every vertex of
`X`.  Relative to the seven-boundary `S`, the two components of `G-S` are
`E` and `F\cup\{u,x\}` and their boundary-full packing numbers are exactly
`(1,2)`.

## 3. Exact obstruction

The only boundary-full connected subgraph contained in `F` is all of
`F`: the label `s_0` requires `a`, while `s_5,s_6` require `b`.  The
vertex `x` sees only the four vertices of `A`.  Adding `a` gives five
boundary contacts and adding `b` gives six, but either choice takes a
vertex required by every boundary-full connected subgraph of `F`.

More strongly, there are no three pairwise disjoint connected subgraphs in
`F\cup\{u,x\}` of which two are boundary-full and the third meets at least
five vertices of `S`.  Any two disjoint full subgraphs must use `u` for one
and both `a,b` for the other, leaving at most the four-contact singleton
`x`.

This is a compact local mechanism behind the failure: the three labels
outside `N_S(x)` are split between indispensable entrance vertices.  Two
entrances supply attachment multiplicity, not a removable connected
subgraph preserving all seven contacts in the remainder.

## 4. Why the terminal disjunction survives

The whole graph is seven-connected.  The verifier checks all 4,096 vertex
deletions of order at most six; none disconnects the graph.  Deleting the
seven neighbours of `x` isolates it, so the connectivity is exactly seven.

Nevertheless the following seven bags form an explicit `K_7`-minor model:

\[
 \{s_0\},\ \{s_3\},\ \{s_4\},\ \{u\},\
 \{s_1,e_0\},\ \{s_5,e_1\},\
 \{s_2,s_6,x,a,b\}.                                    \tag{4}
\]

The graph is exactly five-chromatic: `\{s_0,s_3,s_4,e_0,e_1\}` is a
literal `K_5`, and the verifier supplies a five-colouring.  Thus the graph
violates both `K_7^-`-minor exclusion and the seven-chromatic
proper-minor-critical response.  It does not refute a theorem with the
accepted conclusion

\[
 \text{third connected subgraph}\quad\text{or}\quad K_7^-\text{ minor}.
\]

Its exact conclusion is that the positive branch cannot be deduced from
connectivity, connected-subgraph packing numbers, exceptional boundary
structure, and the two entrance edges alone.  A valid proof must use the
terminal-minor exclusion or compatible proper-minor colouring responses to
eliminate this indispensable-entrance configuration.

## 5. Verification

Run

```text
python3 barriers/hc7_k7minus_nonfull_two_entrance_allocation_barrier_verify.py
```

The script uses only the Python standard library.  It checks every claimed
incidence, all small vertex cuts, the exact connected-subgraph packing and
allocation failure, the five-colouring and `K_5`, and every contact in the
displayed `K_7` model.
