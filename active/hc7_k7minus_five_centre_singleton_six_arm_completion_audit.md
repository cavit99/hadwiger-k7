# Internal audit: six equality-shore arms at a singleton contact

**Verdict:** **GREEN**.

**Audited theorem:**
[`hc7_k7minus_five_centre_singleton_six_arm_completion.md`](hc7_k7minus_five_centre_singleton_six_arm_completion.md)

**Audited SHA-256:**
`534fb93d2785332d4fa775f2e273f32a4d6d77bb70242489963f743a146480c6`

This is a hash-pinned internal mathematical audit, not external peer review.
The proof is computation-free.  The verdict covers Theorem 2.1, its
six-vertex contact-graph bound, and the terminal reinterpretation in Section
3 of the scalar witness from the singleton-shift note.

## 1. Input normal form

The only project-specific input is the audited
[`singleton-shift normal form`](hc7_k7minus_five_centre_singleton_shift.md),
whose checked source hash is
`c42ecd8d8f198c4f8b6d53b0341d9c7a01ea9f8702e665e1d3d6d5a125145e04`.
It gives exactly the facts used here:

\[
 B=(Z-\{z\})\mathbin{\dot\cup}\{p,q\},\quad |B|=6,
 \qquad H=G-zx,
\]

`H` is six-connected, `H-B` has precisely the connected components `C` and
`E=D\cup\{z\}`, both components are adjacent to every literal vertex of
`B`, `x\in C`, `z\in E`, and `xz\in E(G)`.  In particular, the last edge is
available for the eventual minor model even though it is absent from `H`.

## 2. The six first-hit arms

The ordinary Fan Lemma applies in the six-connected graph `H` from
`x\notin B` to the six-set `B`.  It gives six paths sharing only `x` and
having distinct ends in `B`.  Since `B` itself has order six, every member
of `B` is one of those ends.  Consequently no path can contain a second
member of `B`: that vertex is the end of another path and would violate
disjointness away from `x`.  The stated truncation at first boundary hits is
therefore harmless and, more generally, preserves six distinct hits.

Before its first hit in `B`, each path remains in the component `C` of
`H-B` containing `x`; it cannot enter `E` without first meeting `B`.
Deleting `x` therefore gives six nonempty, connected, pairwise disjoint sets
`A_b\subseteq C\cup\{b\}` with `A_b\cap B=\{b\}`.  The first edge of the
corresponding path joins `x` to `A_b`.  Fullness of `E` at the literal
boundary gives an `E`--`A_b` edge through `b` for every label.  This checks
all three assertions preceding the definition of the contact graph.

## 3. Lifting a contact-graph minor

Let `R_1,\ldots,R_5` be the disjoint connected label sets of a `K_5^-`
model in the contact graph `J`.  For each `i`, the vertex union

\[
                        \bigcup_{b\in R_i}A_b
\]

is connected: the witnessing `G`-edges for a spanning tree of `J[R_i]`
join its constituent arm sets.  The five unions are pairwise disjoint
because the label sets and all six arms are pairwise disjoint.  Every model
adjacency between two `R_i` is witnessed by an edge between the
corresponding lifted unions.  Thus these five unions have all but at most
one mutual adjacency.

The additional sets `{x}` and `E` are disjoint from one another and from all
five lifted unions: `x\in C` was deleted from every arm, while
`E\cap(C\cup B)=\varnothing`.  They are connected and adjacent to each
other through the literal edge `xz` of `G`.  The first arm edges make
`{x}` adjacent to every lifted union, and fullness at the boundary makes
`E` adjacent to every lifted union.  Hence the seven displayed sets are
literal branch sets of a `K_7^-` model in `G`.  Extra adjacencies cause no
problem.

The source phrase about adjoining witnessing edges to a branch set is
understood in the standard sense that those edges establish connectivity
of the displayed vertex union; no additional vertices or overlaps are
introduced.

## 4. Six-vertex extremal bound

The assertion that every six-vertex graph `F` with at least twelve edges
has a `K_5^-` minor is correct.

- If `e(F)>=13`, a minimum-degree vertex has degree at most
  `floor(e(F)/3)`.  Deleting it leaves at least nine edges on five vertices,
  hence a spanning `K_5^-` subgraph (possibly with its missing edge also
  present).
- If `e(F)=12` and some vertex has degree at most three, the same deletion
  leaves at least nine edges.
- Otherwise the degree sum is 24 and every vertex has degree four.  Hence
  `F=K_6-3K_2`.  Contract an edge whose ends lie in two different missing
  pairs.  The contracted branch set is adjacent to all four remaining
  vertices; among those four, only the third missing pair remains absent.
  The resulting five branch sets form exactly a `K_5^-` model.

Applying this exhaustive argument to `J` proves that a target-free host has
`e(J)<=11`.

## 5. The old scalar witness

The six arms displayed in equation (3.2) are valid first-hit arms.  Their
initial paths use, respectively,

\[
 xp,\quad xaq,\quad xby_1,\quad xc'y_2,\quad xd'y_3,
 \quad xegw.
\]

All required edges occur in the incidence table and in
`K_8-\{xg,ab,c'd',ef\}`.  After deleting `x`, the six arm sets are nonempty,
connected and pairwise disjoint.

Omit the arm ending at `q`.  Among the remaining arms:

- the `p`-arm meets the `w`-arm through `pw` and the three `y_i`-arms
  through the listed `p`--`C` incidences;
- the arms ending at `y_1,y_2,y_3,w` have every mutual contact supplied by
  the core except the `y_2`--`y_3` contact, whose possible core edge
  `c'd'` is one of the deleted matching edges;
- the boundary vertices in question are independent apart from the
  displayed `w`--pole edges, and the incidence table supplies no alternative
  `y_2`--`y_3` edge.

Their contact graph is therefore exactly `K_5^-`.  Adding `{x}` and `E`
gives the seven branch sets checked in Section 3 of this audit.  Thus any
actual singleton-shift host realizing the old local data is terminal.
The source correctly retains the table only as an arithmetic and local
incidence witness; it does not reinterpret that table alone as the existence
of a global critical host.

## 6. Exact scope

The theorem does not show that an arbitrary six-arm contact graph has twelve
edges or a `K_5^-` minor, and it does not synchronize the critical-edge
Kempe paths with the fan.  Therefore it does not eliminate the complete
singleton-contact branch.  Its surviving conclusion---that every applicable
six-arm contact graph is `K_5^-`-minor-free and hence has at most eleven
edges---is exactly supported by the proof.
