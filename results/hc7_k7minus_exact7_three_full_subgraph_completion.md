# Exact three-full-subgraph `K_7^-` completion at a seven-vertex boundary

**Status:** written proof; separately internally audited in the adjacent
[`_audit.md`](hc7_k7minus_exact7_three_full_subgraph_completion_audit.md) note.
The quotient characterization is computation-free.  The host-level section
gives explicit terminal constructions and reduces every detached complete
support in the first paired response to a minor or an actual separator.
Such a support is not yet forced in every exact `(1,2)` separation.

Write `K_4^-` for the graph obtained from `K_4` by deleting one edge.  Let
`H` be a graph on a literal seven-set `S`.  Form `J_0(H)` by adjoining three
pairwise nonadjacent vertices `p_0,p_1,p_2`, each adjacent to every vertex of
`S`.  Form `J_1(H)` in the same way and add the single edge `p_1p_2`.

## 1. Exact static characterization

### Theorem 1 (three independent universal vertices)

The following are equivalent:

1. `J_0(H)` contains a `K_7^-` minor;
2. there are distinct vertices `x,y in S` such that

   \[
                         K_4^-\preccurlyeq H-\{x,y\}.  \tag{1}
   \]

#### Proof

Suppose first that (1) holds, with branch sets `B_1,...,B_4`.  The seven
sets

\[
 \{p_0,x\},\quad \{p_1,y\},\quad \{p_2\},
 \quad B_1,B_2,B_3,B_4                              \tag{2}
\]

are connected and pairwise disjoint.  The first three are pairwise
adjacent through the two anchors, every one of them is adjacent to every
`B_i`, and at most one adjacency is absent among the four `B_i`.  Thus (2)
is a `K_7^-` model.

Conversely, take a `K_7^-` model in `J_0(H)`.  Since `J_0(H)` is connected,
we may enlarge its branch sets so that they cover every vertex.  Let `r` be
the number of branch sets containing an added universal vertex `p_i`.  The remaining
`7-r` branch sets lie wholly in `S`; call them boundary branch sets.  Any
four boundary branch sets form a `K_4^-` model because the original seven
branch sets have at most one missing adjacency.

If `r=0` or `r=1`, select four boundary branch sets.  At least two nonempty
unselected boundary branch sets remain, and vertices chosen from them give
the required `x,y`.

Suppose `r=2`.  There are five boundary branch sets.  One universal branch
set contains at least two of the three pairwise nonadjacent added vertices,
so its connectedness forces it to contain a boundary vertex.  Select four
boundary branch sets and take `x` in the fifth and `y` in that universal
branch set.

It remains to consider `r=3`.  There are exactly four boundary branch sets.
If the universal branch sets contain at least two boundary vertices, choose two
of them as `x,y`.  They cannot contain none: three singleton universal branch
sets would have three mutually missing adjacencies.  The only remaining
case is that exactly one boundary vertex `x` lies in the universal branch
sets.  The two unanchored universal branch sets are then the unique nonadjacent
pair in the model.  Consequently the four boundary branch sets are pairwise
adjacent and partition the other six vertices of `S`.

We use the following elementary observation.  If four disjoint connected
pairwise adjacent branch sets cover six vertices, some vertex `y` can be
deleted while the four sets, with its own set reduced, remain a `K_4^-`
model.  Their sizes are `3,1,1,1` or `2,2,1,1`.  Choose a nonsingleton set
`B`.  It has at least two vertices whose deletion leaves `B` nonempty and
connected.  For such a vertex `v`, call another branch set exclusive to
`v` when every edge from `B` to that set is incident with `v`.  The
exclusive families belonging to different vertices of `B` are disjoint,
and there are only three other branch sets.  Hence one of the two eligible
vertices is exclusive to at most one other branch set.  Deleting it loses
at most one of the six required adjacencies.

Apply the observation and call its deleted vertex `y`.  The four reduced
boundary branch sets give a `K_4^-` model in `H-{x,y}`.  This completes the
proof. \(\square\)

### Theorem 2 (one adjacent pair of full subgraphs)

The following are equivalent:

1. `J_1(H)` contains a `K_7^-` minor;
2. there is a vertex `x in S` such that

   \[
                              K_4^-\preccurlyeq H-x.   \tag{3}
   \]

#### Proof

Given the model in (3), use

\[
 \{p_0,x\},\quad\{p_1\},\quad\{p_2\},
 \quad B_1,B_2,B_3,B_4.                              \tag{4}
\]

The anchor `x` supplies both adjacencies incident with the first universal
branch set, while `p_1p_2` supplies the third.  At most one adjacency is
absent among the four boundary branch sets, so (4) is a `K_7^-` model.

For the converse, again take a spanning `K_7^-` model and let `r` count its
universal branch sets.  If `r<=2`, select four of at least five boundary branch
sets and choose `x` in another.  If `r=3`, the four boundary branch sets
already form a `K_4^-` model.  At least one universal branch set contains a
boundary vertex `x`, because otherwise the two nonedges from `p_0` to
`p_1,p_2` would both remain missing.  The four boundary branch sets avoid
that `x`, proving (3). \(\square\)

## 2. Lift to an exact `(1,2)` separation

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
 \qquad E_G(L,R)=\varnothing,                         \tag{5}
\]

where `G[L]` and `G[R]` are connected.  Suppose `L` contains a connected
subgraph `Q` adjacent to every vertex of `S`, and `R` contains two disjoint
connected subgraphs `P_1,P_2`, each adjacent to every vertex of `S`.

A shortest `P_1`--`P_2` path in `G[R]` has no internal vertex in either
subgraph.  Add all its vertices except its endpoint in `P_2` to `P_1`.
The enlarged `P_1` remains connected, disjoint from `P_2`, and full at `S`,
and it is adjacent to `P_2`.  Replacing `p_0,p_1,p_2` in Theorem 2 by
`Q,P_1,P_2` therefore gives the following exact quotient consequence:

> If `G` has no `K_7^-` minor, then
> \[
>                         K_4^-\npreccurlyeq G[S]-x
>                         \qquad(x\in S).              \tag{6}
> \]

The implication (6) was already available as the connected-rich diamond
deletion lemma in the exceptional-centre programme.  Theorems 1 and 2 add
the converse statement at the contracted three-subgraph level: no other
static `K_7^-` model is hidden in either three-vertex quotient.

If, in addition, `G` is seven-connected, is not six-colourable, and every
proper minor of `G` is six-colourable, then the critical seven-cut theorem
and (6) give

\[
              2\le\chi(G[S])\le3,
              \qquad |E(G[S])|\le9.                  \tag{7}
\]

Indeed, three disjoint full connected subgraphs give the nine-edge bound,
and the critical theorem says that `G[S]` has an edge.  Equation (6)
excludes a literal `K_4`: one of the other three boundary vertices could be
deleted while retaining it.  A `K_4`-free graph on seven vertices with at
most nine edges is three-colourable by the elementary four-critical
argument recorded in the critical seven-cut theorem.

## 3. A terminal one-defect construction

The difficult returned partitions in the exact `(1,2)` programme include

\[
 S=M\mathbin{\dot\cup}\{x,y\}\mathbin{\dot\cup}K,
 \qquad M=\{m_1,m_2\},
 \qquad G[K]\cong K_3.                               \tag{8}
\]

Retain three pairwise disjoint connected subgraphs `Q,P_1,P_2` of `G-S`,
each full at `S`.

### Lemma 3 (one nontriangle contact and two triangle contacts)

Suppose a connected subgraph `X` is disjoint from
`S,Q,P_1,P_2`, is adjacent to some

\[
                           o\in M\cup\{x,y\},          \tag{9}
\]

and `X union {o}` is adjacent to at least two vertices of `K`.  Then `G`
contains a `K_7^-` minor.

#### Proof

Assign the other three vertices of `M union {x,y}` bijectively to
`Q,P_1,P_2`.  Enlarge each full subgraph by its assigned vertex, use
`X union {o}` as a fourth branch set, and retain the three vertices of `K`
as singleton branch sets.

All seven sets are connected and disjoint.  Any two of the first four are
adjacent because each full-subgraph-derived set is full at the boundary
vertex contained in the other set.  Each full-subgraph-derived set is
adjacent to all three singleton vertices of `K`, and those vertices form a
triangle.  The set
`X union {o}` is adjacent to at least two of them.  Thus at most one of the
21 branch-set adjacencies is absent. \(\square\)

### Lemma 4 (a complete operated `x`--`y` support)

Suppose a connected subgraph `W`, disjoint from `S,Q,P_1,P_2`, has an edge
to each of `x,y`, and `W union {x,y}` is adjacent to at least two vertices
of `K`.  Then `G` contains a `K_7^-` minor.

#### Proof

Use the seven branch sets

\[
 Q\cup\{m_1\},\quad P_1\cup\{m_2\},\quad P_2,
 \quad W\cup\{x,y\},\quad \{k\}\ (k\in K).          \tag{10}
\]

The first three are mutually adjacent: boundary fullness supplies the
cross-edges through `m_1,m_2`.  They are each adjacent to the fourth set
through `x` or `y`, and to every singleton in `K`.  The fourth set is
adjacent to at least two of those singletons, which are mutually adjacent.
Again at most one adjacency is absent. \(\square\)

### Lemma 5 (two operated supports when the retained clique has order two)

Suppose instead that

\[
 S=M\mathbin{\dot\cup}\{x,y\}\mathbin{\dot\cup}K,
 \qquad M=\{m_1,m_2,m_3\},
 \qquad G[K]\cong K_2.                               \tag{11}
\]

Let `X,Y` be disjoint connected subgraphs, also disjoint from
`S,Q,P_1,P_2`, such that `X` is adjacent to `x`, `Y` is adjacent to `y`,
and `X` is adjacent to `Y`.  If at most one of the four possible
adjacencies from `X union {x}` and `Y union {y}` to the two vertices of
`K` is absent, then `G` contains a `K_7^-` minor.

#### Proof

Use the seven branch sets

\[
 Q\cup\{m_1\},\quad P_1\cup\{m_2\},\quad
 P_2\cup\{m_3\},\quad X\cup\{x\},\quad Y\cup\{y\},
 \quad\{k\}\ (k\in K).                              \tag{12}
\]

Boundary fullness supplies every adjacency involving one of the first
three sets.  The fourth and fifth sets are adjacent by hypothesis, the two
singletons in `K` are adjacent, and at most one adjacency from the fourth
or fifth set to those singletons is absent.  Thus (12) is a `K_7^-` model.
\(\square\)

## 4. Complete supports with several missing clique contacts

The preceding lemmas give a minor immediately when enough retained-clique
contacts are present.  The opposite contact extreme does not require a
three-target linkage.

### Lemma 6 (a complete support gives a minor or a nested separator)

Assume `G` is seven-connected and retain the `2+1+1+3` setting (8).  If a
connected subgraph `W` satisfies the hypotheses of Lemma 4 apart from its
two-contact requirement, then either `G` contains a `K_7^-` minor or there
is a nonempty proper connected part of a branch set in a spanning extension
of the displayed model whose complement in that branch set is connected
and whose open neighbourhood is an actual separator of `G`.

#### Proof

Put

\[
 A_0=Q\cup\{m_1\},\qquad A_1=P_1\cup\{m_2\},\qquad A_2=P_2,
 \qquad X=W\cup\{x,y\}.                               \tag{13}
\]

The six sets `A_0,A_1,A_2` and the three singleton members of `K` form a
`K_6`-minor model.  The set `X` is adjacent to each `A_i`.  If it is
adjacent to at least two members of `K`, Lemma 4 applies.

Otherwise enlarge these seven branch sets to a spanning model, assigning
each unused connected component to an adjacent branch set.  If this fills
all but at most one missing `X`--`K` adjacency, the resulting seven sets
are themselves a `K_7^-` model.  If at least two remain absent, apply the
audited
[multiple-missing-adjacency separator dichotomy](hc7_k7minus_multiple_missing_adjacencies_separator_dichotomy.md),
Theorem 1.  It gives exactly the asserted alternative. \(\square\)

### Lemma 7 (one complete support in the retained-edge response)

Assume `G` is seven-connected and retain the `3+1+1+2` setting (11).  If
one of `X union {x}` and `Y union {y}` is adjacent to both members of `K`,
then `G` contains a `K_7^-` minor or the nested-separator outcome of Lemma 6
holds.

#### Proof

Suppose `Y union {y}` is adjacent to both members of `K`.  If
`X union {x}` meets either one, Lemma 5 gives `K_7^-`.  Otherwise use
`X union {x}` as the centre and use

\[
 Q\cup\{m_1\},\quad P_1\cup\{m_2\},\quad P_2\cup\{m_3\},
 \quad Y\cup\{y\},\quad\{k\}\ (k\in K)               \tag{14}
\]

as the six pairwise adjacent foreign branch sets.  The centre is adjacent
to the first four sets and misses the two `K` singletons.  Extend the model
to span `G`.  It either acquires all but at most one missing adjacency or
Theorem 1 of the cited multiple-missing-adjacency dichotomy applies.
\(\square\)

## 5. Exact scope and remaining inference

Lemmas 3--5 are explicit terminal constructions, not connectivity
heuristics.  In a `K_7^-`-minor-free host they imply, respectively,

\[
 |N_K(X\cup\{o\})|\le1,
 \qquad
 |N_K(W\cup\{x,y\})|\le1.                            \tag{15}
\]

Lemma 5 gives the corresponding conclusion for the `3+1+1+2` response:
any two adjacent operated supports rooted at `x,y` have at least two
missing adjacencies to the retained boundary edge.

Thus an operation-generated support which meets one of the four vertices in
`M union {x,y}` must miss at least two common vertices of `K`.  This is
stronger than the earlier conclusion allowing only one unspecified missing
boundary contact.

Lemmas 6--7 remove the former need to force two named contacts in `K` once
a complete operated support has been separated from the two rich full
subgraphs.  In the `2+1+1+3` response every such support now gives either
`K_7^-` or an actual nested separator.  In the `3+1+1+2` response the same
holds whenever one support has both retained-edge contacts; the crossed
one-miss-at-each orientation remains outside that near-clique reduction.

The separator is not yet terminal: its boundary need not be the
neighbourhood of a named exceptional vertex, and the fixed colouring need
not be proper on either new closed shore.  In the direct-entry case there
may also be no complete operated support disjoint from the two rich full
subgraphs at all.  The first unsupported inference is therefore:

> split one rich full subgraph, while retaining one full connected
> remainder and the fixed proper-minor colouring, so that either a complete
> operated support is disjoint from both retained full subgraphs or the
> returned separator carries a legal common trace or is literally
> `N_G(z)` for a named exceptional degree-eight vertex `z`.

A gate-edge deletion supplies five bichromatic bypasses, but their colours
belong to that second operation, not to the original attained duties.
Treating them as duty labels is an unsupported operation-provenance swap.
The required two-operation trace-alignment theorem must instead return a
complete support, a common exact boundary partition, an explicit `K_7^-`
model, or a component of `G-N[z]` strictly smaller than the selected
component for a named exceptional degree-eight vertex `z`.  Neither
ordinary connectivity nor the current unlabelled full-subgraph rotations
supplies this conclusion.  Accordingly this theorem does not eliminate
every exact `(1,2)` separation.

## Dependencies and antecedents

- [exact static `K_7` three-full-subgraph characterization](hc7_exact7_three_packet_quotient_characterization.md)
- [connected-rich diamond deletion](hc7_k7minus_nonfull_attachment_reduction.md), Lemma 1
- [critical seven-cut capacity](hc7_k7minus_critical_seven_cut_capacity.md)
- [connected-subgraph capacity at a seven-vertex boundary](hc7_k7minus_seven_boundary_component_descent.md)
- [selected-response preservation and partition-specific connected-subgraph criterion](hc7_exact7_selected_response_preservation.md)
- [multiple missing centre adjacencies give a minor or separator](hc7_k7minus_multiple_missing_adjacencies_separator_dichotomy.md)
