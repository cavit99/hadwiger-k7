# Pure `C_7` true-twin seam: a sharp portal normal form

**Status.**  Human proof with an exact 841-case boundary check.  This note
proves a local normal form and reduces every target-free exterior to a
three-connected graph.  It does **not** settle the three-connected exterior
case.

## 1. Setting and lift

Let `G` be a seven-connected graph with adjacent true twins `a,b` of degree
eight.  Put

\[
 T=N_G(a)-\{b\}=N_G(b)-\{a\},\qquad H=G-\{a,b\},
 \qquad D=H-T,
\]

and assume that `G[T]` is the chordless cycle
`t_0t_1...t_6t_0`.  Thus `a` and `b` are anticomplete to `D`, and
`H` is five-connected.

Five pairwise-disjoint connected bags in `H`, each meeting `T`, whose
contact graph is `K_5^-`, lift to a `K_7^-` model in `G`: add the singleton
bags `\{a\}` and `\{b\}`.  The twins see all five old bags through their
`T` vertices and see one another through `ab`.

We use the following elementary rooted fact.

**Four-root diamond lemma.**  If `J` is three-connected and
`r_1,r_2,r_3,r_4` are distinct vertices, then `J` has four disjoint
connected bags rooted at those vertices whose contact graph contains
`K_4^-`.

One direct proof takes a cycle through `r_1,r_2,r_3` and a three-fan from
`r_4` to that cycle.  Split the cycle into three connected rooted arcs.
The split points may be chosen so that two distinct fan ends lie in two
different arcs (if all fan ends lie between the same consecutive pair of
roots, put a split point between two of them).  The three arcs form a
triangle and the union of the fan paths, rooted at `r_4`, sees at least two
of them.

## 2. Portal lemma

For `x in D`, write `S=N_T(x)`.  For `t in S`, let

\[
 M_t=(S-\{t\})\mathbin\cup\{t^-,t^+\},
\]

where `t^-` and `t^+` are the two neighbours of `t` on the fixed
seven-cycle.

**Lemma 2.1 (four augmented portals are terminal).**  If
`|M_t|>=4` for some `x in D` and `t in N_T(x)`, then `G` contains a
`K_7^-` minor.

**Proof.**  Deleting `x,t` from the five-connected graph `H` leaves a
three-connected graph.  Choose four distinct vertices of `M_t` and apply
the four-root diamond lemma in `H-\{x,t\}`.  The bag `\{x,t\}` is connected
and sees each of the four rooted bags: a chosen root in `S-\{t\}` is
adjacent to `x`, while a chosen root in `\{t^-,t^+\}` is adjacent to `t`.
We have therefore obtained a `T`-hitting rooted `K_5^-` in `H`, which
lifts as above.  `square`

**Corollary 2.2 (sharp target-free portal classification).**  If `G` has
no `K_7^-` minor, then every `x in D` satisfies

\[
 |N_T(x)|\le 2,
 \quad\hbox{or}\quad
 N_T(x)=\{t_{i-1},t_i,t_{i+1}\}\text{ for some }i.
\]

**Proof.**  In a target-free graph Lemma 2.1 gives `|M_t|<=3` for every
`t in S`.  Since

\[
 |M_t|=|S|+1-d_{C_7[S]}(t),
\]

we have `d_{C_7[S]}(t)>=|S|-2` for every `t in S`.  As the cycle has
maximum degree two, `|S|<=4`.  Equality `|S|=4` would give degree two at
every vertex of `C_7[S]`, forcing a nonempty proper subset of a cycle to be
closed under both cyclic neighbours, which is impossible.  If `|S|=3`,
then `C_7[S]` has minimum degree at least one.  It is triangle-free, so it
is a three-vertex path, and its vertices are three consecutive cycle
vertices.  The alternatives of size at most two remain.  `square`

If the ambient reduction additionally supplies `delta(G)>=8`, then this
normal form implies `d_D(x)>=5` for every `x in D`, because `x` has no
neighbour in `\{a,b\}` and at most three neighbours in `T`.  This degree
conclusion is not being inferred from seven-connectivity alone.

## 3. Disconnected exterior

**Lemma 3.1.**  If `D` is disconnected, then `G` contains a `K_7^-`
minor.

**Proof.**  Let `X` be any component of `D`.  Its neighbourhood is
contained in `T`.  Since `G` is seven-connected, `N_G(X)` cannot have
order below seven.  Hence `N_T(X)=T`; every component of `D` is `T`-full.

Choose distinct components `X,Y` and adjacent vertices `t_0,t_1` of the
cycle.  Use the two connected bags

\[
 X\cup\{t_0\},\qquad Y\cup\{t_1\}.
\]

The remaining five cycle vertices induce a path.  Partition that path
into three nonempty consecutive intervals and use the intervals as three
more bags.  The first two bags are adjacent through `t_0t_1`; each sees
all three interval bags because `X` and `Y` are `T`-full.  Consecutive
interval bags are adjacent, so among the ten pairs of bags only the two
outer intervals may be nonadjacent.  Thus the contact graph contains
`K_5^-`.  Every bag meets `T`, and the lift from Section 1 finishes.
`square`

**Lemma 3.2.**  If `D` is connected and has a cut vertex, then `G` contains
a `K_7^-` minor.

**Proof.**  Let `z` be a cut vertex of `D`, and choose two distinct
components `X,Y` of `D-z`.  For either such component `Q`,

\[
                         N_G(Q)\subseteq T\cup\{z\}.
\]

Seven-connectivity therefore gives `|N_T(Q)|>=6`.  Put
`A=N_T(X)` and `B=N_T(Y)`.  Thus each of `A,B` misses at most one cycle
vertex and `|A cap B|>=5`.

Choose an oriented cycle edge `t_0t_1` with `t_0 in A` and `t_1 in B`.
Such an edge exists: the possible missing vertex of `A` forbids at most its
two outgoing orientations, and the possible missing vertex of `B` forbids
at most its two incoming orientations, among fourteen oriented cycle
edges.  Use the connected bags

\[
                         X\cup\{t_0\},\qquad
                         Y\cup\{t_1\}.
\]

They are adjacent through `t_0t_1`.  The residual five cycle vertices form
a path and contain at least

\[
                         |A\cap B|-2\ge3
\]

vertices supported by both `X` and `Y`.  Partition the residual path into
three nonempty consecutive intervals, each containing one of three such
common vertices (cut between successive chosen common vertices).  Both of
the first two bags see every interval, consecutive intervals see each
other, and again only the two outer intervals may fail to be adjacent.
These five `T`-hitting bags form `K_5^-` and lift with the twins.
`square`

## 4. Two-cuts

We first isolate the only finite cycle fact needed for a two-cut.

**Lemma 4.1 (two support sets on `C_7`).**  Let `A,B subseteq V(C_7)` with
`|A|,|B|>=5`.  The cycle vertices can be partitioned into five nonempty
sets

\[
                         P,Q,I_1,I_2,I_3
\]

such that

1. `P subseteq A` and `Q subseteq B`;
2. every `I_i` induces a connected subgraph of the cycle; and
3. the following abstract five-bag contact graph has at least nine edges:
   declare `P,Q` adjacent; retain every cycle edge between distinct parts;
   join `P` to every `I_i` meeting `A`, and join `Q` to every `I_i`
   meeting `B`.

**Proof.**  There is a short restricted construction except in two orbits.
Choose adjacent `p in A,q in B`, put `P={p},Q={q}`, and partition the
residual five-vertex path into three consecutive nonempty intervals, each
meeting both `A` and `B`.  Since `A` and `B` each miss at most two cycle
vertices, checking the positions of those two missing sets, up to a
dihedral symmetry and interchange of `A,B`, leaves precisely the following
two failures of this restricted construction:

| `V(C_7)-A` | `V(C_7)-B` |
|---|---|
| `\{0,1\}` | `\{3,4\}` |
| `\{0,1\}` | `\{3,5\}` |

For the first row use

\[
 P=\{6\},\quad Q=\{5\},\quad
 I_1=\{0,1\},\ I_2=\{2,3\},\ I_3=\{4\};
\]

the sole absent contact is `I_1I_3`.  For the second row use

\[
 P=\{2,3\},\quad Q=\{4\},\quad
 I_1=\{0,1\},\ I_2=\{5\},\ I_3=\{6\};
\]

the sole absent contact is `I_1I_2`.

For auditability, `verify_c7_twocut_fivebag_partition.cpp` independently
enumerates all `29^2=841` ordered support pairs, all five-label assignments
of the seven cycle vertices, and all stated connectivity and contact
conditions.  Its exact output is

```text
support_pairs 841 failures 0
```

The two-orbit restricted-construction classification is also obtained by
`verify_c7_twocut_restricted_orbits.py`, which enumerates the complements
of size at most two under the fourteen dihedral maps and swapping `A,B`.
It finds 28 restricted failures, split into exactly the two displayed
orbits with fourteen ordered members each.  `square`

**Lemma 4.2.**  If `D` is two-connected but not three-connected, then `G`
contains a `K_7^-` minor.

**Proof.**  Let `\{u,v\}` be a two-cut of `D` and choose distinct
components `X,Y` of `D-\{u,v\}`.  Since `D` is two-connected, each of
`u,v` has a neighbour in each of `X,Y`; otherwise the other cut vertex
would already disconnect that component from `D`.

For either component `W`,

\[
                         N_G(W)\subseteq T\cup\{u,v\}.
\]

Seven-connectivity gives `|N_T(W)|>=5`.  Apply Lemma 4.1 to
`A=N_T(X)` and `B=N_T(Y)`, obtaining `P,Q,I_1,I_2,I_3`.  Form the five
bags

\[
 X\cup\{u\}\cup P,\qquad
 Y\cup\{v\}\cup Q,\qquad I_1,I_2,I_3.
\]

The first bag is connected because `u` has a neighbour in `X` and every
vertex of `P subseteq A` has a neighbour in `X`; the second is symmetric.
They are adjacent because `u` has a neighbour in `Y`.  Their contacts with
the interval bags are exactly the support contacts allowed in Lemma 4.1,
and contacts among interval bags include all retained cycle edges.
Consequently the five bags have at least nine of ten contacts.  They are
disjoint and all meet `T`, so they lift with the twins to `K_7^-`.
`square`

## 5. Trust boundary

The portal classification uses only five-connectivity of `H`, the literal
induced `C_7` boundary, and the four-root diamond lemma.  The exterior
reductions use seven-connectivity of `G` and the fact that the twins have no
neighbours in `D`.  The remaining exterior is three-connected.  No
st-numbering split may be used as a branch bag without first absorbing
suitable `T` anchors.
