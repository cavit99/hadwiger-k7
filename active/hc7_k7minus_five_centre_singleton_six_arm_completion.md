# Six equality-shore arms at a singleton contact

**Status:** active computation-free written proof; separate internal audit
[`GREEN`](hc7_k7minus_five_centre_singleton_six_arm_completion_audit.md).
The theorem below is an unbounded terminal criterion in the singleton-contact
branch.  It does not eliminate every singleton-contact configuration and does
not prove the `K_7^-` six-colour conjecture.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting

Use the notation and conclusions of the audited
[singleton-shift normal form](hc7_k7minus_five_centre_singleton_shift.md).
Thus

\[
 B=(Z-\{z\})\mathbin{\dot\cup}\{p,q\},\qquad |B|=6,
 \qquad E=D\cup\{z\},\qquad H=G-zx,
\tag{1.1}
\]

where `H` is six-connected and

\[
                         H-B=C\mathbin{\dot\cup}E.     \tag{1.2}
\]

Both displayed components are connected and adjacent to every literal
vertex of `B`; moreover `x\in C`, `z\in E`, and `xz\in E(G)`.

The palette fan in the singleton-shift note preserves the deleted edge
`xz` and therefore leaves only five arms on the `C`-side.  Here we use a
different fan: all six arms lie on the `C`-side, while the connected set
`E` is retained as a separate branch set.

## 2. The six-arm completion theorem

### Theorem 2.1

There are six pairwise vertex-disjoint connected sets

\[
                              A_b\qquad(b\in B)         \tag{2.1}
\]

such that

1. `A_b\subseteq C\cup\{b\}` and `A_b\cap B=\{b\}`;
2. `{x}` is adjacent to every `A_b`; and
3. `E` is adjacent to every `A_b`.

Let `J` be their contact graph: its vertices are the six labels in `B`,
and `bb'\in E(J)` exactly when `E_G(A_b,A_{b'})` is nonempty.  If `J`
contains a `K_5^-` minor, then `G` contains an explicit `K_7^-` minor.
Consequently, in a surviving target-free host,

\[
                  K_5^-\npreccurlyeq J,
                  \qquad |E(J)|\le 11.                \tag{2.2}
\]

#### Proof

Apply the Fan Lemma in the six-connected graph `H` to the vertex `x` and
the six-set `B`.  It gives six paths from `x` to the six distinct vertices
of `B`, pairwise disjoint away from `x`.  Truncate every path at its first
vertex of `B`.  Before that first visit a path cannot leave `C`: by (1.2),
every route from `C` to `E` meets `B`.  For the path ending at `b`, delete
`x` and call the remaining connected set `A_b`.  This proves assertions
1 and 2.  Fullness of `E` at `B` proves assertion 3.

Let five pairwise disjoint connected branch sets of a `K_5^-` model in
`J` be `R_1,\ldots,R_5`, where each `R_i` is a connected set of arm
labels.  Replace `R_i` by the union of the corresponding literal sets
`A_b`, together with one witnessing edge for each edge of a spanning tree
of `J[R_i]`.  These are five pairwise disjoint connected branch sets in
`G`, with all but at most one of their mutual adjacencies.

The two additional branch sets

\[
                              \{x\},\qquad E            \tag{2.3}
\]

are disjoint, connected, and adjacent through the edge `xz`.  Assertions
2 and 3 make both of them adjacent to every lifted branch set.  The seven
sets therefore form a `K_7^-` minor model in `G`.

It remains only to justify the numerical bound.  Let `F` be a graph on six
vertices with at least twelve edges.  If `|E(F)|\ge13`, a minimum-degree
vertex `v` satisfies

\[
 d_F(v)\le\left\lfloor {|E(F)|\over3}\right\rfloor,
 \qquad |E(F-v)|\ge9,
\]

so `F-v` contains `K_5^-` as a subgraph.  If `|E(F)|=12` and some vertex
has degree at most three, the same conclusion holds.  Otherwise `F` is
four-regular, hence `F\cong K_6-3K_2`.  Contracting an edge whose ends
belong to different missing pairs gives five branch sets with exactly one
missing adjacency.  Thus `F` again contains a `K_5^-` minor.  Applied to
`J`, this proves (2.2). `\square`

## 3. The displayed sharp scalar witness is terminal under this fan

The local realization in Section 7 of the singleton-shift note does show
that the *five-arm palette fan* can have exactly eight contacts.  It does
not obstruct Theorem 2.1.

Retain the notation of equations (7.3)--(7.6) there.  Thus

\[
 V(C)=\{x,a,b,c',d',e,f,g\},
\]

`G[C]` is `K_8` minus the matching

\[
                         xg,\quad ab,\quad c'd',\quad ef,
\tag{3.1}
\]

and `G[B]` consists of the two edges `wp,wq`.  The following are six
pairwise disjoint first-hit arms from `x` to the six vertices of `B`:

\[
 \begin{array}{c|c}
 \text{end}&A_b\\ \hline
 p&\{p\}\\
 q&\{a,q\}\\
 y_1&\{b,y_1\}\\
 y_2&\{c',y_2\}\\
 y_3&\{d',y_3\}\\
 w&\{e,g,w\}.
 \end{array}                                          \tag{3.2}
\]

The relevant initial paths are `xp`, `xaq`, `xby_1`, `xc'y_2`,
`xd'y_3`, and `xegw`.  Omit the `q`-arm.  Among the other five arms every
pair is adjacent except the pair ending at `y_2,y_3`: the `p`-arm meets
the `w`-arm through `pw` and meets the other three through the displayed
`p`--`C` incidences, while (3.1) supplies every remaining adjacency except
`c'd'`.  Hence those five arms already have contact graph `K_5^-`.

Together with `{x}` and `E`, they give the seven branch sets in the proof
of Theorem 2.1.  Thus any actual normal-form host realizing the data of
Section 7 contains the forbidden minor.  The table remains an exact scalar
identity check, but it is not a surviving obstruction to the six-arm
completion.

## 4. Exact scope

The theorem replaces the five-vertex edge-count test by a six-vertex
minor test.  It is terminal whenever one equality-shore six-fan has a
contact graph containing `K_5^-`, and it eliminates the concrete sharp
incidence realization previously used to illustrate nonclosure.

What remains is exact: in every surviving singleton-contact host, **every
chosen six-arm system to which Theorem 2.1 is applied has a
`K_5^-`-minor-free contact graph**, hence at most eleven distinct arm
contacts.  The present proof does not derive twelve contacts from
`e(C)\ge3|C|-2`, and it does not synchronize the critical-edge Kempe paths
with a choice of the six arms.  Either conclusion would finish the
singleton-contact branch.
