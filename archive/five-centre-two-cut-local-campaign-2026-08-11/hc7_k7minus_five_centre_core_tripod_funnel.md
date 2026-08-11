# A rooted-tripod funnel for the shared-pole core

**Status:** archived written derivation; not separately audited.  This note
records a route nonclosure, not a counterexample.  It identifies the
first literal separation exposed by applying the Robertson--Seymour--Thomas
tripod theorem to a pole-clean `K_5^-` core.  It does not anchor the two
tripod interiors at the two poles and therefore does not close the
five-centre two-cut branch.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting and relative seven-connectivity

Use the two-shore notation of the audited
[five-centre two-cut reduction](../../results/hc7_k7minus_five_centre_two_cut_reduction.md):

\[
 S=Z\mathbin{\dot\cup}\{p,q\},\qquad |Z|=5,
\]

and `G-S` has connected components `C,D`, with no edge between `C` and
`D`.  Let `z,w in Z` be distinct centres.  Put

\[
                         Q=S-\{z,w\}.                  \tag{1.1}
\]

Thus `|Q|=5`.

For a nonempty set `X subseteq D`, let

\[
 \Lambda(X)=\{s\in S:N_D(s)\cap X\ne\varnothing\}.
\tag{1.2}
\]

### Lemma 1.1 (relative-seven inequality on `D`)

Every nonempty `X subseteq D` satisfies

\[
                      |N_D(X)|+|\Lambda(X)|\ge7.       \tag{1.3}
\]

#### Proof

There is the disjoint decomposition

\[
                     N_G(X)=N_D(X)\mathbin{\dot\cup}\Lambda(X).
\]

The nonempty opposite component `C` is disjoint from `X union N_G(X)`, so
`N_G(X)` separates `X` from `C`.  Seven-connectivity gives (1.3).
\(\square\)

## 2. Contracting a pole-clean core

Assume that `D` contains three pairwise disjoint connected sets

\[
                         B_1,B_2,B_3                   \tag{2.1}
\]

which are pairwise adjacent and each adjacent to both `z` and `w`.
Assume moreover that they exhaust the two centres' `D`-contacts:

\[
 N_D(z)\cup N_D(w)\subseteq B_1\cup B_2\cup B_3.     \tag{2.2}
\]

In the shared-pole saturated row this last condition is automatic for a
pole-clean `K_5^-` core: both centres have exactly three `D`-neighbours,
and the three disjoint non-centre bags must use one contact of each centre.

Let `J` be the simple graph obtained from `D` by contracting each `B_i` to
a vertex `b_i`.  The vertices `b_1,b_2,b_3` induce a triangle.  Call a
separation `(A,B)` of `J` **outward** when

\[
 b_1,b_2,b_3\in A,\qquad |B-A|\ge2.                  \tag{2.3}
\]

### Lemma 2.1 (the first exact separator)

Let `(A,B)` be an outward separation of `J` of order at most two, and let
`K=A cap B`.

1. If `K` contains a contracted root `b_i`, then every component of
   `J-K` in `B-A` is adjacent to a contracted root in `K`.  The lift of
   any such component may be absorbed into one of those root bags,
   producing a strictly larger pole-clean core.
2. If `K` contains no contracted root, then

   \[
                         |K|=2,                        \tag{2.4}
   \]

   and, for every component `X` of `J-K` in `B-A`, its lift
   `tilde X subseteq D` satisfies

   \[
                N_D(\widetilde X)=K,
                \qquad \Lambda(\widetilde X)=Q.       \tag{2.5}
   \]

   In particular, `K union Q` is an exact order-seven separator of `G`.

#### Proof

Fix a far-side component and write `X` for its lift to `D`.

Suppose first that `K` contains a contracted root.  If `X` had no edge to
any root bag represented in `K`, then all its `D`-neighbours would be the
at most one ordinary vertex of `K`.  It has no neighbour in a root bag
outside `K`, since the corresponding contracted vertex lies in `A-K`.
By (2.2), `X` consequently misses both `z` and `w`, so

\[
             |N_D(X)|+|\Lambda(X)|\le1+|Q|=6,
\]

contrary to Lemma 1.1.  Thus `X` meets a root bag represented in `K`.
Adding `X` to that bag preserves connectivity, disjointness, all three
root-bag adjacencies, and both centre contacts.  It strictly enlarges the
core.

Now suppose that `K` contains no root.  No vertex of `X` is adjacent to
any root bag, because all three contracted roots lie in `A-K`.  Condition
(2.2) again gives

\[
                         z,w\notin\Lambda(X).           \tag{2.6}
\]

Moreover `N_D(X) subseteq K`.  Lemma 1.1 therefore gives

\[
 7\le |N_D(X)|+|\Lambda(X)|
   \le |K|+|Q|\le7.                                    \tag{2.7}
\]

Equality holds throughout.  Hence `|K|=2`, both vertices of `K` meet
`X`, and every member of `Q` meets `X`, proving (2.4)--(2.5).  Since
`C` lies on the other side, `K union Q` is an exact seven-cut in `G`.
\(\square\)

The second outcome is not a smaller two-cut of `F=G-Z`.  Indeed, after
deleting `Z`, equation (2.5) becomes

\[
                         N_F(\widetilde X)
                         =K\cup\{p,q\},                \tag{2.8}
\]

an exact order-four boundary.  The old poles bypass `K`, and the two
vertices of `K` bypass the old pole cut.

## 3. What the tripod theorem gives

Robertson, Seymour, and Thomas, statements (3.4)--(3.5) in
[*Hadwiger's conjecture for `K_6`-free graphs*](https://thomas.math.gatech.edu/PAP/hadwiger.pdf),
show that, in the absence of an outward separation of order at most two,
either

1. `J` has a tripod on `b_1,b_2,b_3`; or
2. `J` has a disc drawing with `b_1,b_2,b_3` on the boundary.

The first outcome lifts cleanly even when the tripod has nontrivial legs.
Assign the three common feet and the three mutually disjoint legs to the
corresponding root bags.  Removing those feet from the two triads leaves
two disjoint nonempty connected sets `X_1,X_2`, each adjacent to every
enlarged root bag.  Thus the tripod gives a rooted `K_{3,2}` model on the
three non-centre bags.

Lemma 2.1 shows exactly what can prevent this application.  A
root-containing quotient separation permits a literal bag enlargement;
an ordinary quotient separation is the exact order-seven cut (2.5).

Neither tripod outcome is terminal here.  By (2.2), every `D`-neighbour
of `z` or `w` is already in a root bag.  Hence the two clean tripod
interiors, being disjoint from those bags, are adjacent to neither centre.
To complete the `K_5^-` core they must be extended disjointly so that one
contains `p` and the other contains the connected component `C` (or an
equivalent connected set meeting both centres).  The edge from `p` to
`C` would then supply the helper--helper adjacency.  The unlabelled
tripod theorem contains no such placement clause.

## 4. The exact placement theorem that would be terminal

There is a stronger Robertson--Seymour--Thomas statement which isolates
the remaining placement issue exactly.  Their statement (3.6) says that,
for a literal triangle `b_1b_2b_3` in a four-connected simple nonplanar
graph `H`, if a nominated set `W` containing the triangle induces a graph
which is not *triangular* in their precisely defined sense, then `H` has a
five-bag clique model

\[
                 \{\{b_1\},\{b_2\},\{b_3\},X_1,X_2\}
\tag{4.1}
\]

in which both `X_1,X_2` meet `W`.

Put

\[
                 Y=C\cup\bigl(S-\{z,w,p\}\bigr).       \tag{4.2}
\]

The set `Y` is connected, because `C` is connected and full to `S`.
Contract `Y` to `c`, contract the three core bags to
`b_1,b_2,b_3`, and delete `z,w`; call the resulting simple minor
`bar G`.  None of the four contracted sets contains `p`, and `pc` is an
edge because `p` has a neighbour in `C`.  Apply (3.6) with

\[
                         W=\{b_1,b_2,b_3,p,c\}.         \tag{4.3}
\]

### Lemma 4.1 (RST placement is terminal)

If `bar G` is four-connected and nonplanar and `bar G[W]` is not
triangular with respect to `b_1,b_2,b_3`, then `G` contains `K_7^-` as a
minor.

#### Proof

Statement (3.6) gives (4.1), with both non-root bags meeting `W`.  The
three singleton root bags already contain the three members of `W` on the
triangle.  Since all five bags are disjoint, the two remaining bags
contain `p` and `c`, one each.  Relabel them as `X_p,X_C`.

Lift the contractions.  The five bags remain pairwise adjacent; their
three root bags contain `B_1,B_2,B_3`, `X_p` contains `p`, and `X_C`
contains the connected set `Y`, in particular `C`.  Each of the singleton
bags `{z},{w}` is adjacent to all three root bags by the core hypothesis, to
`X_p` through the common pole `p`, and to `X_C` because `C` is full to
`S`.  Thus

\[
          \{z\},\{w\},B_1,B_2,B_3,X_p,X_C
\]

lift to seven pairwise adjacent connected bags except possibly for the
pair `\{z\},\{w\}`.  They form a `K_7^-` model.  \(\square\)

The last RST hypothesis has a particularly small literal form here.  Put

\[
 A=\{i:p\sim B_i\},\qquad
 B=\{i:Y\sim B_i\}.                                   \tag{4.4}
\]

### Lemma 4.2 (the five-vertex triangular table)

The graph `bar G[W]` is not triangular with respect to
`b_1,b_2,b_3` if and only if at least one of the following holds:

1. `A=\{1,2,3\}`;
2. `B=\{1,2,3\}`; or
3. `A=B` and `|A|=2`.

#### Proof

The induced graph consists of the root triangle, the edge `pc`, the
`p`--root edges indexed by `A`, and the `c`--root edges indexed by `B`.
The third case in the RST definition of triangularity is impossible,
because only the two vertices `p,c` lie outside the root triangle.

If `A` is the full three-set, then `p` has degree four.  Deleting any root
leaves the triangle formed by `p` and the other two roots together with
the additional neighbour `c`; hence the remaining graph is neither a
circuit nor acyclic.  The first two RST cases both fail.  The argument for
full `B` is symmetric.

If `A=B` is a two-set, then `p,c` both have degree three and the two common
root neighbours have degree four.  Deleting the third root leaves a
`K_4`; deleting either common root leaves a triangle with a pendant
vertex.  Again neither of the first two RST cases applies.

Conversely, assume neither set is full and they are not the same
two-set.  If `A cap B` is empty, every vertex has degree at most three and
at most one of `p,c` has degree three, so the second RST case applies.  If
the sets are equal singletons, delete their common root; the remainder is
a forest of maximum degree at most two.  If one is a singleton contained
in the other two-set, delete the singleton root; the remainder is again
such a forest.  The only remaining possibility is that `A,B` are distinct
two-sets.  Deleting their common root leaves a four-vertex circuit.  These
are precisely the alternatives in the first RST case.  \(\square\)

Consequently the shared-pole row would close if one could verify the
connectivity and nonplanarity hypotheses of Lemma 4.1 and one of the three
incidence patterns in Lemma 4.2.  The first unsupported inference is not
the final branch-set assembly; it is preservation of four-connectivity and
nonplanarity through the four contractions, together with one of those
literal incidence patterns.

## 5. Why `chi(D)>=5` does not remove the planar quotient

It is invalid to exclude the disc alternative merely from
`chi(D)>=5`: contracting the three root bags can destroy the chromatic
obstruction.

For a concrete sharpness check, let

\[
                         D=K_2\mathbin\vee C_5,
\]

with universal adjacent vertices `a,b` and cycle
`v_0v_1v_2v_3v_4v_0`.  Then `chi(D)=5` and `D` has no literal `K_5`.
The disjoint triangles

\[
 T_z=\{a,v_0,v_1\},\qquad T_w=\{b,v_2,v_3\}
\]

are joined by the three pairwise adjacent connected bags

\[
 B_1=\{a,b\},\qquad
 B_2=\{v_0,v_4,v_3\},\qquad
 B_3=\{v_1,v_2\}.                                     \tag{5.1}
\]

They cover `D`, and their contraction is the planar triangle.  This graph
is not a counterexample to the shared-pole theorem--in particular it does
not realize the full saturated palette and proper-minor response data.
It proves only that high chromaticity of the uncontracted shore cannot by
itself discharge the Robertson--Seymour--Thomas planar alternative.

## 6. Exact nonclosure

The rooted-tripod attack therefore reaches the following exhaustive
local funnel for any chosen pole-clean core:

1. enlarge one non-centre core bag;
2. obtain the exact cut `K union Q` of Lemma 2.1;
3. obtain two clean but unanchored tripod interiors; or
4. obtain a planar three-root quotient.

The first literal separation in this route is fully identified: it is an
order-seven cut in `G` and an order-four cut in `F`, not a new two-cut of
`F`.  The remaining useful theorem would have to spend the proper-minor
colouring response to place `p` and `C` in different tripod interiors, or
show that the planar quotient lifts to a compatible shore colouring.
Neither conclusion follows from connectivity or `chi(D)>=5` alone.
