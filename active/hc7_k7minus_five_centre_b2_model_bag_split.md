# A terminal split criterion for the concentrated `b=2` model

**Status:** written proof; separate internal audit GREEN at the revision
recorded in the adjacent audit.
This note extracts a terminal consequence from the stable-bag concentration
theorem.  In a target-free configuration, no bag of the rooted `K_5` model
contains two disjoint connected subgraphs each adjacent to all four other
bags.  The two centre-clean bags therefore have internal boundary at least
six but packing number one for this four-bag adjacency requirement.  The
three remaining bags contain at least eight distinct vertices adjacent to
the retained-centre component.  These conclusions sharpen the exact
unbounded residue but do not prove the required split.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting

Use the notation and conclusions of the separately audited
[stable-bag concentration theorem](hc7_k7minus_five_centre_b2_stable_bag_concentration.md).
Thus

\[
                         \mathcal M=\{P,Q,B_1,B_2,B_3\}          \tag{1.1}
\]

is a spanning rooted `K_5`-minor model in
\(G[D\cup\{p,q\}]\).  Its bags
are connected, pairwise disjoint and pairwise adjacent.  The connected set
`X`, disjoint from all five bags, is adjacent to every member of
\(\mathcal M\).  The connected retained-centre set `K` is disjoint from these
six sets and adjacent to `X`.

After relabelling,

\[
 N_D(Z-\{z\})\subseteq P\cup Q\cup B_1,
 \qquad N_Z(B_2)=N_Z(B_3)=\{z\},                              \tag{1.2}
\]

and

\[
 |N_{G[D\cup\{p,q\}]}(B_i)|\ge6\qquad(i=2,3).                 \tag{1.3}
\]

The union \(P\cup Q\cup B_1\) contains at least six distinct contacts
private to centres of \(Z-\{z\}\).

For a fixed bag \(U\in\mathcal M\), call a connected subgraph of `G[U]`
*four-adjacent* if it has an edge to every bag in
\(\mathcal M-\{U\}\).

## 2. The terminal split

### Theorem 2.1 (two four-adjacent subgraphs are terminal)

If some \(U\in\mathcal M\) contains two vertex-disjoint four-adjacent
connected subgraphs, then `G` contains a `K_7^-` minor.

#### Proof

Let the two subgraphs be `R_0,R_1`.  Because `G[U]` is connected, there is
a partition

\[
                         U=U_0\mathbin{\dot\cup}U_1             \tag{2.1}
\]

such that each `G[U_i]` is connected, \(R_i\subseteq U_i\), and `U_0,U_1`
are adjacent.  To see this, contract `R_0,R_1`, take a spanning tree of the
contracted graph, and delete an edge on the path between the two contracted
vertices.  Expanding the contractions gives (2.1).

Each of `U_0,U_1` is adjacent to every member of
\(\mathcal M-\{U\}\), because it contains `R_0` or `R_1`.  Hence

\[
                         U_0,U_1,\quad\mathcal M-\{U\}           \tag{2.2}
\]

are six pairwise adjacent connected branch sets.  The set `X` is adjacent
to the four unchanged bags.  It is adjacent to at least one of `U_0,U_1`,
because it was adjacent to `U` and the two sets partition `U`.  Thus `X`
and the six sets in (2.2) are pairwise adjacent with at most one exception,
namely the possible nonadjacency of `X` to the other part of `U`.  They form
a `K_7^-` minor. \(\square\)

### Corollary 2.2 (four-adjacent packing number one)

If `G` has no `K_7^-` minor, every bag in \(\mathcal M\) contains at most one
member of any family of pairwise vertex-disjoint four-adjacent connected
subgraphs.

In particular, each centre-clean bag `B_i`, \(i\in\{2,3\}\), has at least six
distinct neighbours in the other four model bags by (1.3), with at least
one neighbour in each of those bags, but it has no two disjoint connected
subgraphs which each reach all four bags.

#### Proof

The first assertion is the contrapositive of Theorem 2.1.  Because the
model in (1.1) is spanning, every neighbour counted in (1.3) belongs to one
of the other four bags.  Model adjacency makes all four corresponding
classes nonempty.  The final assertion follows. \(\square\)

## 3. Eight retained-component contacts in three bags

### Proposition 3.1

The union \(P\cup Q\cup B_1\) contains at least eight distinct vertices
adjacent to `K`.  Consequently, one of these three bags contains at least
three distinct vertices adjacent to `K`.

#### Proof

The stable-bag concentration theorem supplies six pairwise distinct private
contacts of centres in \(Z-\{z\}\) inside \(P\cup Q\cup B_1\).  Every one is
adjacent to its centre in `K`.  In addition, `p in P` is adjacent to the
pole-incident centre `z_p in K`, and `q in Q` is adjacent to
`z_q in K`.  The vertices `p,q` lie outside `D` and hence are distinct from
the six private contacts and from one another.  This gives eight distinct
vertices of `N_G(K)` in the displayed three-bag union.  The last conclusion
is the pigeonhole principle. \(\square\)

## 4. Exact remaining inference

The data now have two complementary forms:

- each of `B_2,B_3` has at least six internal-boundary vertices distributed
  among all four other model bags, but no two disjoint connected subgraphs
  can each meet all four adjacency classes; and
- one of `P,Q,B_1` has at least three distinct contacts with `K`, while all
  eight known `K`-contacts are concentrated in these three bags.

Neither count forces the split in Theorem 2.1.  Several boundary contacts
may all depend on one cutvertex inside a connected bag, and the distinct
contacts with `K` need not lie in connected subgraphs which separately
retain all four model adjacencies.  The first unsupported inference is
therefore

\[
 \begin{gathered}
 \text{six external boundary vertices, or three contacts with `K`,}\\
 \text{inside one connected model bag}
 \end{gathered}
 \quad\Longrightarrow\quad
 \text{two disjoint four-adjacent connected subgraphs}.          \tag{4.1}
\]

No such implication follows from connectivity and the numerical counts
alone.  A terminal continuation must use a host-specific rerouting or
separation theorem which either produces the two four-adjacent subgraphs,
or turns their failure into a strict exact separation compatible with the
proper-minor colouring data.

## Dependencies and claim status

The spanning rooted model, the sets `X,K`, concentration, clean-bag
boundary bound, and six private contacts are conclusions of the separately
audited stable-bag concentration theorem and its audited dependencies.
The terminal split theorem, packing consequence, and eight-contact count
are proved here.  The rerouting/separation statement described in Section 4
is an explicit open step.
