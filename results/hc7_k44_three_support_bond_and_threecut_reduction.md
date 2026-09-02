# Three-support bonds and the exact three-cut residue in a literal `K_{4,4}` blocker

**Status.** Written unbounded theorem; separate hash-pinned internal audit
GREEN.  The
finite check in Section 2 is corroboration only.  The results eliminate every
four-connected nonsingleton minimum blocker and every three-component
three-cut in a surviving nonsingleton blocker.  They do not eliminate the
remaining two-component three-cuts or the singleton-blocker branch, and they do not prove
the literal `K_{4,4}` case of T44, T44, Conjecture 21, or `HC_7`.

## 1. Setting

Let `G` be a finite simple seven-connected graph with no `K_7^-` minor.
Suppose that `G` contains a specified literal `K_{4,4}` with vertex set `S`
and shores `S_0,S_1`, and put `C=G-S`.

Use the minimum crossing-blocker normal form from the audited
[tight-boundary theorem](hc7_k44_tight_boundary_and_minimum_blocker.md).
Thus `ab` is a three-contractible edge crossing a singleton tight atom, `X`
is a minimum connected tight blocker of `ab`, and in the nonsingleton case

\[
 D:=\partial X=\{a,b\}\mathbin{\dot\cup}K,
 \qquad |K|=5.                                             \tag{1}
\]

For `d in D`, put

\[
 R_d=N_G(d)\cap X.                                         \tag{2}
\]

The theorem supplies seven mutually disjoint connected `D`-rooted bags,
disjoint from `X`, ending at seven distinct vertices of `S`; the remaining
vertex of `S` is unused.  The representatives properly two-colour `G[D]`
by their literal shores.  In particular, the representatives of `a,b` lie
on opposite shores because `ab in E(G)`.

For a bond `X=A dotcup Z`, meaning a partition into two nonempty connected
induced subgraphs, let

\[
 s(A,Z)=|\{k\in K:R_k\cap A\ne\varnothing\ne R_k\cap Z\}|. \tag{3}
\]

Minimum-blocker strictness and the audited
[five-support bond reduction](hc7_k44_five_support_bond_reduction.md) give

\[
 q(W):=|N_X(W)|+|\{k\in K:R_k\cap W\ne\varnothing\}|\ge6   \tag{4}
\]

for every nonempty proper connected `W subset V(X)`.  Every `R_k` has at
least two vertices, `X` is three-connected, and `delta(X)>=4`.

## 2. A direct literal-core completion for three split supports

The old two-helper count closes a three-support bond when its two shores
separate suitable occurrences of `R_a` and `R_b`.  The following direct
minor model removes that orientation restriction.  It is the step which
makes three, rather than four, the universal threshold.

### Lemma 2.1 (rooted three-support completion)

Let a graph contain a literal `K_{4,4}` with shores `S_0,S_1`.  Suppose
there are seven mutually disjoint connected bags

\[
 B_a,B_b,B_{j_1},B_{j_2},B_{j_3},B_k,B_l                 \tag{5}
\]

whose intersections with the literal core are distinct singleton
representatives.  Let `f` be the eighth core vertex, and suppose the
representatives of `a,b` lie on opposite shores.

Let `A,Z` be disjoint connected sets, disjoint from the bags and from the
literal core, with an edge between them.  Suppose

1. `A` is adjacent to `B_a,B_b,B_{j_1},B_{j_2},B_{j_3}`;
2. `Z` is adjacent to `B_{j_1},B_{j_2},B_{j_3}`; and
3. each of `B_k,B_l` is adjacent to at least one of `A,Z`.

Then the graph contains a `K_7^-` minor.  More precisely, it has seven
disjoint connected branch sets whose quotient has at least twenty of the
twenty-one possible contacts.

#### Proof

Write a rooted-bag name without `B`, and write juxtaposition inside brackets
for a union.  Thus `[j_1f]` means `B_{j_1}` joined to the unused singleton
`{f}` by a literal-core edge, `[kl]` means `B_k union B_l` joined by a
literal-core edge, and `[j_2Z]` means `B_{j_2} union Z` joined by a support
edge.  Every bracketed set below is therefore connected, and the seven sets
in each row are disjoint.

Call the shore containing the representative of `a` left.  After
permuting `j_1,j_2,j_3`, permuting `k,l`, and, when necessary,
interchanging `a,b` together with the two shores, the core representatives
have one of the following three types:

\[
\begin{array}{c|c|c}
 &S_0&S_1\\ \hline
T_1&a,k,l,f&b,j_1,j_2,j_3\\
T_2&a,j_1,k,f&b,j_2,j_3,l\\
T_3&a,j_1,k,l&b,j_2,j_3,f.
\end{array}                                                \tag{6}
\]

Indeed, if `r` of the three `j`-representatives, `c` of the two remaining
representatives, and `e in {0,1}` copies of `f` lie with `a`, then
`1+r+c+e=4`.  The six possibilities are paired by the `a,b` shore
symmetry and give exactly (6).

Choose for each of `k,l` one adjacent helper as its **owner**.  Extra
helper adjacencies can only add quotient contacts.  In types `T_1,T_3` the
two vertices have the same core colour, so in the mixed-owner case rename
them so that `k` is owned by `A`.  The following table gives the required
branch sets.

\[
\begin{array}{c|c|l|c}
\text{type}&\text{owners of }k,l&\text{seven branch sets}
   &\text{only possibly missing contact}\\ \hline
T_1,T_3&AA&
 [j_3],[l],[A],[a],[j_1f],[j_2Z],[kb]&[l]\!-[a]\\
T_1,T_3&AZ&
 [j_3],[A],[Z],[a],[j_1f],[j_2k],[lb]&[Z]\!-[a]\\
T_1,T_3&ZZ&
 [j_3],[A],[Z],[a],[j_1f],[j_2l],[kb]&[Z]\!-[a]\\
T_2&AA&
 [j_3],[k],[A],[a],[j_1b],[j_2Z],[lf]&[k]\!-[a]\\
T_2&AZ\text{ or }ZA&
 [j_3],[A],[Z],[a],[j_1b],[j_2f],[kl]&[Z]\!-[a]\\
T_2&ZZ&
 [j_1],[j_3],[A],[Z],[j_2f],[kb],[la]&\text{none}.
\end{array}                                                \tag{7}
\]

Every merger of two core-rooted bags in (7) uses opposite shores.  A branch
set containing representatives of both shores contacts every other branch
set containing a core representative.  The remaining contacts follow from
the specified helper adjacencies and the edge `AZ`.  Row by row, this leaves
only the displayed pair in the first five rows and no missing pair in the
last.  Thus the quotient has respectively twenty or twenty-one contacts.
\(\square\)

The dependency-free script
[`hc7_k44_three_support_bond_completion_verify.py`](hc7_k44_three_support_bond_completion_verify.py)
independently enumerates all forty proper `3`-by-`4` placements with `a,b`
opposite and all four owner assignments.  This is a bounded check of the
finite table, not an input to the proof.

### Corollary 2.2 (every three-support bond is terminal)

In the nonsingleton minimum-blocker setting of Section 1, every bond with
`s(A,Z)>=3` gives an explicit `K_7^-` minor in `G`.

#### Proof

Orient the bond so that `A` meets `R_a`.  If `Z` meets `R_b`, the audited
[spanning split-count theorem](hc7_k44_spanning_two_helper_split_count.md)
and two-helper construction give the target from any three split supports.

Suppose instead that `Z` misses `R_b`.  Boundary fullness makes `A` meet
`R_b`.  Choose three split resources and name them `j_1,j_2,j_3`; name the
other two `k,l`.  Use the seven boundary-rooted bags from Section 1.  The
sets `A,Z` are adjacent because `X` is connected.  Both meet every selected
support, while each remaining support meets at least one of them.  All
hypotheses of Lemma 2.1 hold, so it gives the target. \(\square\)

Consequently, in the target-free setting,

\[
                         s(A,Z)\le2                         \tag{8}
\]

for every bond of `X`.

## 3. An abstract four-connected three-support bond theorem

The next theorem uses only the five-support boundary system.  It is stated
separately so that its unbounded content is not confused with the literal-
core construction above.

### Theorem 3.1 (four-connected three-support bond theorem)

Let `Y` be a finite simple four-connected graph, and let
`R_1,...,R_5 subseteq V(Y)` have order at least two.  Suppose that

\[
 |N_Y(W)|+|\{i:R_i\cap W\ne\varnothing\}|\ge6             \tag{9}
\]

for every nonempty proper connected `W subset V(Y)`.  Then `Y` has a bond
which splits at least three of `R_1,...,R_5`.

#### Proof

Assume to the contrary that every bond splits at most two supports.  Choose
any vertex `p`.  Since `Y-p` is connected and every support has order at
least two, `(Y-p,{p})` has a support-full first shore.  Among all bonds
`Y=U dotcup V` with `p in V` and `U` meeting all five supports, choose one
with `|U|` minimum.

Apply Theorem 4.1 of the audited
[five-support bond reduction](hc7_k44_five_support_bond_reduction.md),
taking both auxiliary distinguished supports there to be `{p}`.  There is
no closing bond in its sense, because such a bond would split at least
three supports.  If `M` is the movable boundary set of that theorem, its
conclusion and the present assumption give

\[
                         2\le |M|\le s(U,V)\le2.             \tag{10}
\]

The block classification therefore has only its triangle-free first
outcome: a replaced path edge would contribute a third non-cutvertex and
hence a third member of `M`, while the other two outcomes also have three
members of `M`.  Thus

\[
                         Y[U]=u_1u_2\cdots u_m              \tag{11}
\]

is an induced path.  Exactly two supports, call them `E_L,E_R`, split the
bond, with

\[
 E_L\cap U=\{u_1\},\qquad E_R\cap U=\{u_m\}.                \tag{12}
\]

The other three supports, call them `F_1,F_2,F_3`, lie wholly in `U`, and
every vertex of `U` has a neighbour in `V`.

Every nonempty subpath `P` of `U` is one shore of a bond: every component
of `U-P` has a neighbour in the connected graph `Y[V]`.  Hence

\[
\begin{split}
 s(P,Y-P)={}&\mathbf1_{\{u_1\in P\}}+
                \mathbf1_{\{u_m\in P\}}\\
 &+|\{i:\varnothing\ne F_i\cap P\ne F_i\}|\le2.           \tag{13}
\end{split}

For each `i`, let `I_i` be the minimal subpath of `U` containing `F_i`.
It has positive length because `|F_i|>=2`.  For every edge of `U`, one of
the two end-subpaths already splits `E_L` or `E_R`; by (13), at most one
`I_i` uses that edge.  Thus `I_1,I_2,I_3` are pairwise edge-disjoint.

Let `A_i` be the pair of ends of `I_i`.  The union of the three nontrivial
edge-disjoint paths `I_i` is a nonempty forest whose odd-degree vertex set
is

\[
                         A_1\mathbin\triangle A_2
                         \mathbin\triangle A_3\ne\varnothing.             \tag{14}
\]

Theorem 1.1 of Chen--Ding--Yu--Zang,
[*Bonds with Parity Constraints*](https://www.math.lsu.edu/~ding/bonds.pdf),
in the form recorded and audited in Section 5 of the five-support bond
reduction, now gives one of two outcomes.  Either there is a feasible bond,
which separates the two vertices of each `A_i` and hence splits
`F_1,F_2,F_3`, or `Y` has a plane representation in which a facial cycle
`C` links the three pairs.

It remains to exclude the facial outcome.  Lemma 5.3 of the five-support
bond reduction, applied to (9), says that at least one of the five supports
has a vertex outside `C`.

If some `F_i` has a vertex `z` outside `C`, replace `A_i` by any two-element
subset of `F_i` containing `z` and retain the two extreme pairs belonging
to the other internal supports.  Otherwise all three `F_i` lie on `C`, and
one of `E_L,E_R`, say `E`, has a vertex outside `C`.  Replace one internal
pair by a pair consisting of the unique vertex of `E cap U` and a vertex of
`E cap V`, chosen so that the pair contains a vertex outside `C`: if the
unique `U`-vertex is outside, any `V`-vertex works, and otherwise choose an
off-cycle `V`-vertex.  Retain two internal extreme pairs.

In either case the new triple of pairs has nonempty symmetric difference:
the selected off-cycle vertex occurs in the new pair and in neither retained
pair.  It is therefore acyclic.  The two retained extreme pairs contain at
least three distinct vertices of `C`, since their positive-length path
hulls are edge-disjoint.  Apply the parity-bond theorem again.  A feasible
bond splits the three corresponding supports.  An infeasible triple would
give another facial cycle `C'` containing those at least three vertices of
`C` and the selected vertex outside `C`.  Four-connectivity gives a unique
spherical embedding.  In a three-connected plane graph, the intersection
of two distinct facial cycles is empty, one vertex, or one edge.  Hence
`C'=C`, contrary to the off-cycle vertex on `C'`.

Both alternatives produce a bond splitting three supports, the desired
contradiction. \(\square\)

### Lemma 3.2 (three components give a three-pair bond)

Let `Y` be a three-connected graph, let `T={r,s,t}` be a three-cut, and let
`W_1,W_2,W_3` be distinct components of `Y-T`.  For each `i`, choose distinct
vertices `x_i,y_i in W_i`.  Then `Y` has a bond which separates `x_i` from
`y_i` for all `i=1,2,3`.

#### Proof

The graph `Y-r` is two-connected.  For each `i`, set-Menger in `Y-r` gives
two vertex-disjoint paths from `{x_i,y_i}` to `{s,t}`, saturating both end
sets.  Choose the paths minimally and trim them at their first vertex of
`{s,t}`.  Their interiors lie in `W_i`, one ends at `s`, and the other ends
at `t`.

Let `A_0` be the union of the three paths ending at `s`, and let `Z_0` be
the union of the three paths ending at `t`.  Paths belonging to distinct
components have disjoint interiors, while the two paths in any one component
are disjoint.  Hence `A_0,Z_0` are disjoint connected sets, and each contains
exactly one of `x_i,y_i`.

If they are not already adjacent, take a shortest `A_0`--`Z_0` path and
assign its internal vertices between the two sets so that the enlarged sets
are connected and adjacent.  Every component of the still unused graph has
an edge to their union; assign it whole to a side which it meets.  This gives
a bond of `Y` and preserves all three separations. \(\square\)

## 4. The exact nonsingleton residue

### Theorem 4.1 (reduction to two-component three-cuts)

In the nonsingleton target-free minimum-blocker setting of Section 1, choose
the vertex `p in R_a` supplied by the tight-boundary theorem.  Among all
bonds `X=U dotcup V` with `p in V` and `U` meeting all five `K`-supports,
minimize `|U|`.  Then all of the following hold.

1. The graph `X[U]` is an induced path `u_1...u_m`, with `m>=4`.
   Exactly two supports, denoted `E_L,E_R`, split across `U,V`, and
   \[
      E_L\cap U=\{u_1\},\qquad E_R\cap U=\{u_m\}.            \tag{15}
   \]
   The other three supports `F_1,F_2,F_3` lie wholly in `U`.

2. Every nonempty subpath `P` of `U` is a bond shore and satisfies the
   exact formula (13).  The three support hulls of `F_1,F_2,F_3` have
   positive length and are pairwise edge-disjoint.  If
   \[
      \rho(u)=|\{k\in K:u\in R_k\}|,
   \]
   then `rho(u)<=2` and
   \[
      |N_X(u)\cap V|\ge6-d_{X[U]}(u)-\rho(u).                \tag{16}
   \]
   In particular each path end has at least three neighbours in `V`, and
   each internal path vertex has at least two.

3. For any two distinct vertices `x,z` of `X`, there is a bipolar order
   \[
                         x=x_1,x_2,\ldots,x_n=z              \tag{17}
   \]
   in which every proper prefix and suffix induces a connected subgraph.
   If
   \[
      \alpha_i=\min\{j:x_j\in R_i\},\qquad
      \omega_i=\max\{j:x_j\in R_i\},
   \]
   the five gap intervals
   \[
                         [\alpha_i,\omega_i)                 \tag{18}
   \]
   have depth at most two, and their interval-intersection graph is a
   forest.  If `L_j,R_j` count the supports lying wholly before and wholly
   after the `j`th gap, respectively, then, for the prefix `P_j` and suffix
   `Q_j`,
   \[
             |N_X(P_j)|\ge1+R_j,
             \qquad |N_X(Q_j)|\ge1+L_j.                     \tag{19}
   \]

4. The graph `X` has a three-cut.  For every three-cut `T`, every component
   of `X-T` meets `U-T`, and `X-T` has exactly two components.

Thus a surviving nonsingleton blocker has connectivity exactly three.  Its
remaining three-cut has exactly two components; no complete support profile
for those two components is yet proved.

#### Proof

Corollary 2.2 gives (8).  Apply Theorem 4.1 of the five-support bond
reduction to the displayed minimum choice.  Its inequalities become

\[
                         2\le |M|\le s(U,V)\le2,
\]

so its classification gives the path and support placement in item 1;
the argument establishing (13) in Theorem 3.1 applies verbatim.  Three
positive-length edge-disjoint support hulls require at least three path
edges, so `m>=4`.  At most two hulls contain any path vertex, including the
possible meeting of two hulls at a common end.  At a path end, its endpoint
support and at most one internal hull occur.  Hence `rho(u)<=2`.  The
singleton instance of (4) is

\[
                         d_X(u)+\rho(u)\ge6,
\]

and subtracting the path degree proves (16).

For item 3, use the standard bipolar-order theorem for two-connected graphs.
Every proper prefix and suffix is a bond shore, so (8) says that at most two
support intervals cross each gap.  This is exactly depth at most two.  An
interval graph with a cycle has a triangle, whereas depth two excludes a
triangle; hence the interval-intersection graph is a forest.  The prefix
`P_j` meets exactly `5-R_j` supports, so (4) gives the first inequality in
(19); the suffix argument is identical.

If `X` were four-connected, Theorem 3.1 and (4) would give a bond splitting
three supports, contrary to (8).  Since `X` is three-connected and has at
least five vertices, it therefore has a three-cut.

Let `T` be any three-cut and `W` a component of `X-T`.  Three-connectivity
gives `N_X(W)=T`.  If `W subseteq V`, then `W` misses the three supports
contained in `U` and can meet only `E_L,E_R`, so (4) would give
`q(W)<=3+2=5`.  Thus every component meets `U-T`.  If there are three
components, deleting `T cap U` from the path `U` leaves at least three
components, so `|T cap U|>=2`.

The tight-boundary theorem already says that `X-T` has at most three
components and classifies the three-component case into two profiles.  In
its second profile, one component `W_1` meets each of the three
non-component-exclusive supports, and each such support has a vertex
outside `W_1`.  The complement of `W_1` is connected because it consists
of `T` and the other two components, each adjacent to every vertex of `T`.
Thus `(W_1,X-W_1)` is a bond splitting those three supports, contrary to
(8).

In the first profile, each of three distinct supports is contained wholly
in one distinct component.  Every such support has order at least two.
Choose two of its vertices in that component and apply Lemma 3.2.  The
resulting bond splits all three component-exclusive supports, again
contrary to (8).  Hence three components are impossible.  The
tight-boundary theorem gives at most three components, and a cut has at
least two, so every three-cut leaves exactly two.  This completes item 4.
\(\square\)

## 5. Exact remaining lemma

The four-connected nonsingleton branch and both three-component profiles
are now closed.  The exact nonsingleton residue is:

> **Three-cut completion lemma (open).**  Under the hypotheses and path
> structure of Theorem 4.1, eliminate a three-cut with exactly two
> components.  Every component meets the minimum support-full path, but no
> complete support profile across the two components is yet proved.

A proof may choose the three-cut; it need not work for every three-cut.
The global restriction (8), the exact subpath formula (13), and the bipolar
interval forest (18) remain available.  The adjacent
[minimum-path internal-transversal barrier](../barriers/hc7_k44_minimum_path_internal_transversal_barrier.md)
shows only that a fixed internal triple of supports need not have a
prescribed local transversal.  It does not refute the two-component
three-cut completion lemma, because the successful bond may change the three
supports or use vertices on both sides of the cut.

This is a strict unbounded reduction of the literal-core nonsingleton
problem.  The singleton-blocker branch remains separate.
