# Generalized Kempe paths at a rainbow degree-eight centre

**Status:** written derivation; separate hash-pinned internal audit
**GREEN** in
[`hc7_k7minus_five_centre_rolek_scheme_reduction_audit.md`](hc7_k7minus_five_centre_rolek_scheme_reduction_audit.md).
The rooted-minor and separator reductions below are unbounded.  They do not
close the all-rainbow five-centre row or prove the `K_7^-` six-colour
conjecture.

Throughout, `K_t^-` denotes `K_t` with one edge deleted.

## 1. The exact generalized-chain input

Use the hypotheses and notation of the audited
[global five-root palette alternative](hc7_k7minus_five_centre_t5_global_palette.md),
and assume its all-rainbow outcome.  Thus `G` is
seven-contraction-critical, every centre `z` has degree eight,
`G[N(z)]` is `K_4`-free, and

\[
 |N_D(z)|=3,\qquad N_D(z)\cong K_3,
 \qquad |N_C(z)|=5-\rho_z,
 \qquad \rho_z\in\{0,1\}.
\tag{1.1}
\]

We use Rolek--Song--Thomas, Lemma 1.7, in the following exact form.  If
`x` is a degree-`k+s` vertex of a `k`-contraction-critical graph,
`alpha(G[N(x)])=s+2`, and `I` is an independent `(s+2)`-set in `N(x)`,
then for every set `M` of missing edges of `G[N(x)-I]` there are paths

\[
                         P_{uv}\qquad(uv\in M)          \tag{1.2}
\]

whose ends are `u,v` and whose internal vertices lie outside `N[x]`.
Moreover, `P_{uv}` and `P_{wz}` are vertex-disjoint whenever
`u,v,w,z` are distinct.  This arbitrary-`M` statement is the one printed
as [Lemma 1.7 in Rolek--Song--Thomas](https://arxiv.org/abs/2208.07335).

The following conversion records exactly what this disjointness buys.

### Lemma 1.1 (a rooted `K_{1,1,3}` from five remaining neighbours)

Let `z` be a degree-eight centre and let `I` be an independent triple in
`N(z)`.  Put `R=N(z)-I`, and suppose

\[
                         R=X\mathbin{\dot\cup}Y,
             \qquad |X|=3,\quad |Y|=2,                \tag{1.3}
\]

where the two vertices of `Y` are adjacent.  Then `G-z-I`
contains an `R`-rooted `K_{1,1,3}` minor whose singleton parts are the two
vertices of `Y` and whose three-vertex part is `X`.

Consequently:

1. if `G[X]` has at least two edges, the same five rooted bags form an
   `R`-rooted `K_5^-` model; and
2. if `G[X]` is a triangle, they form an `R`-rooted `K_5` model.

#### Proof

The displayed independent triple proves
`alpha(G[N(z)])>=3`; Dirac's contraction-critical neighbourhood bound
gives the reverse inequality.  Hence the Rolek--Song--Thomas lemma applies
with `k=7` and `s=1`.

For every pair with one end in `X` and the other in `Y`, use its literal
edge when it is present and
otherwise use the path (1.2).  Use the literal edge inside `Y` for the
seventh edge of `K_{1,1,3}`.  Every nontrivial path has its interior
outside `N[z]`, so it contains no other root.  Paths belonging to two
nonincident missing pairs are disjoint.  A nontrivial path and a
nonincident literal root edge are also disjoint.

It remains only to check the multiple-intersection clause in the
definition of a scheme.  Any pairwise incident family of edges in the
triangle-free graph `K_{3,2}` has one common endpoint: three pairwise
incident edges without a common endpoint would form a triangle.  A family
also using the literal edge inside `Y` can meet at only one of that edge's
ends, which is again a common endpoint of all its demand edges.  Thus the
seven selected paths form a `K_{1,1,3}`-scheme on the five roots.

Kuendgen--Pelsmajer--Ramamurthi, Theorem 6.2, says that
`K_{1,1,3}` is contractible.  It therefore gives the asserted rooted
minor model.  Literal edges inside `X` join the corresponding rooted bags.
Two edges on a three-set contain a spanning `P_3`, so they leave at most
one of the ten bag adjacencies absent; three edges leave none. \(\square\)

The external conversion used in the last paragraph is
[Theorem 6.2 of Kuendgen, Pelsmajer, and Ramamurthi](https://arxiv.org/abs/1207.6141).

## 2. The pole-free profile

Let `z` be pole-free and put

\[
                         A=N_C(z),\qquad T=N_D(z).     \tag{2.1}
\]

Then `|A|=5`, `T` is a triangle, and `A` is anticomplete to `T`.
Since `G[N(z)]` is `K_4`-free and has independence number three,

\[
                         \alpha(G[A])=2,
             \qquad G[A]\text{ is `K_4`-free}.        \tag{2.2}
\]

### Theorem 2.1 (pole-free local alternative)

One of the following two mutually exclusive local configurations holds.

1. There are a nonedge `ab` of `G[A]` and a vertex `t_0` in `T` such that
   `G[A-\{a,b\}]` has at least two edges and, with

   \[
        I=\{a,b,t_0\},\qquad
        X=A-\{a,b\},\qquad Y=T-\{t_0\},               \tag{2.3}
   \]

   the graph `G-z-I` contains an `R`-rooted `K_5^-` model, where
   `R=X\mathbin{\dot\cup}Y`.  If `G[X]` is a triangle, the model
   is a rooted `K_5`.
2. The equality-shore contact graph is one of the two exact residues

   \[
                         G[A]\cong C_5
               \quad\hbox{or}\quad
                         G[A]\cong K_3\mathbin{\dot\cup}K_2.  \tag{2.4}
   \]

   For every choice in (2.3), `G[X]` has exactly one edge.  Lemma 1.1
   still gives five rooted bags with all the adjacencies of a
   `K_5` with two adjacent edges deleted.  Additional bag adjacencies are
   not excluded.

#### Proof

Choose any nonedge `ab` in `A` and any `t_0` in `T`.  The set in (2.3) is
independent, `Y` is an edge, and Lemma 1.1 applies.  Its first conclusion
gives outcome 1 whenever `e(G[A-\{a,b\}])>=2`.

Suppose no nonedge has that property, and put `L=overline{G[A]}`.  By
(2.2), `L` is triangle-free and `alpha(L)<=3`.  For every edge `ab` of
`L`, the three-vertex graph `G[A-\{a,b\}]` has at most one edge, so
`L-\{a,b\}` has at least two edges.

We claim `delta(L)>=2`.  If `v` were isolated, choose an edge `ab` of
`L`; one exists because `alpha(L)<=3`.  The graph `L-\{a,b\}` would
contain the isolated vertex `v` and hence at most one edge, a
contradiction.  If instead `v` had the unique neighbour `u`, then
`L-\{u,v\}` would have to be a three-vertex path, say `x-y-z`.  Applying
the same two-edge requirement to `xy` and `yz` forces `uz` and `ux`,
respectively.  But `L-\{u,x\}` then has only the edge `yz`, again a
contradiction.

Thus `5<=e(L)<=6`, where the upper bound is Mantel's theorem.  If
`e(L)=5`, every vertex has degree two and `L=C_5`.  If `e(L)=6`, the
triangle-free equality case gives `L=K_{2,3}`.  Taking complements gives
(2.4).  In either graph, deleting the ends of any complement edge leaves
exactly one edge in `G[A]`, proving the last assertion. \(\square\)

## 3. The pole-incident profile

Suppose instead that `z` is adjacent to one pole `r`.  Put again
`A=N_C(z)` and `T=N_D(z)`.  Now

\[
 N(z)=A\mathbin{\dot\cup}T\mathbin{\dot\cup}\{r\},
 \qquad |A|=4,\quad T\cong K_3,\quad A\text{ anticomplete to }T.
\tag{3.1}
\]

As above, `alpha(G[A])=2`.  Choose a nonedge `ab` of `G[A]` and
`t_0` in `T`, and put

\[
 I=\{a,b,t_0\},\qquad
 X=(A-\{a,b\})\cup\{r\},\qquad
 Y=T-\{t_0\}.                                        \tag{3.2}
\]

The cross pairs from the two `A`-vertices to `Y` are missing, while the
two `r`--`Y` pairs may be either edges or missing edges.  Lemma 1.1
therefore gives the following exact conclusion.

### Corollary 3.1 (pole-rooted local alternative)

For every choice in (3.2), `G-z-I` contains an
`R`-rooted `K_{1,1,3}` minor, where `R=X\mathbin{\dot\cup}Y`, in which the
pole `r` is one of the
three roots in the size-three part.  If `G[X]` has at least two edges, it
is a rooted `K_5^-` model; if `G[X]` is a triangle, it is a rooted `K_5`
model.

This conclusion does not refer to the contact triangle of another centre.
In particular, for two same-pole centres with distinct rainbow triangles,
it does not place the second triangle one vertex per rooted bag.

## 4. Terminal model-separator alternatives

The next two consequences apply to any rooted `K_5^-` model supplied by
Lemma 1.1; they do not depend on the exact pole profile.  Assume here that
`G` is seven-connected.  Let `mathcal B=(B_r:r in R)` be such a model,
put

\[
                         W=\bigcup_{r\in R}V(B_r),
             \qquad      H=G-z,
\tag{4.1}
\]

and recall that `I` is an independent triple, `R=N(z)-I`, and every
vertex of `R` has a neighbour in `I`.

### Theorem 4.1 (terminal minor or a full model separator)

Either `G` contains a `K_7^-` minor, or there is a separator `Q subseteq W`
of `H` with `|Q|>=6` such that two components of `H-Q` are `Q`-full and
each contains a vertex of `I`.  Those same components are full to
`Q union {z}` in `G-(Q union {z})`.  In particular, if `|Q|=6`, then
`Q union {z}` is an exact order-seven separator of `G` with two full
sides.

#### Proof

The graph `H` is six-connected.  If one component `K` of `H-W` contains
all of `I`, then `K` is adjacent to every rooted bag: for each `r in R`,
maximality of the independent triple `I` gives an edge from `r` to `I`.
The seven bags

\[
                             \{z\},\quad K,\quad
                             (B_r:r\in R)
\]

are pairwise adjacent except for at most the one missing pair in the
rooted `K_5^-` model.  They form a `K_7^-` minor.

Otherwise two vertices `i,j in I` lie in different components of `H-W`.
Choose an inclusion-minimal `i`--`j` separator `Q subseteq W`.  Six-
connectivity gives `|Q|>=6`.  The components of `H-Q` containing `i` and
`j` are both `Q`-full: if a member of `Q` missed either component, it
could be deleted from the separator.  In `G`, each component is also
adjacent to `z` through its displayed member of `I`, and it has no other
new neighbour.  Its exact neighbourhood is therefore `Q union {z}`.
\(\square\)

### Corollary 4.2 (exterior avoidance is terminal)

Suppose `G` has no `K_7^-` minor.  Then `W` meets every component of
`G-N[z]`.

#### Proof

Suppose that `W` avoids a component `F` of `G-N[z]`.  Seven-connectivity
gives

\[
                         |N_G(F)|\ge7,
             \qquad      N_G(F)\subseteq N(z),
\tag{4.2}
\]

so `F` misses at most one vertex of `N(z)`.  If `F` sees all of `N(z)`,
choose any `i in I`.  If its unique missed vertex `x` is not in `R`, choose
any `i in I` seen by `F`.  If `x in R`, choose `i in I` adjacent to `x`;
such an `i` exists because `I` is a maximum independent set in `N(z)`,
and `F` sees every member of `I`.  In every case `F union {i}` is connected,
is adjacent to every rooted bag, and is adjacent to `{z}`.  Together with
`{z}` and the five rooted bags, it gives a `K_7^-` minor, a contradiction.
\(\square\)

Thus a surviving generalized-path model cannot be localized by simply
avoiding a component outside `N[z]`: avoidance is already terminal.  If
its union separates the independent triple, Theorem 4.1 instead exposes
a full separator contained in the model itself.

## 5. Why the arbitrary-demand form is still nonterminal

The positive outcome of Theorem 2.1 or Corollary 3.1 is genuinely rooted.
Adjoining the singleton bag `{z}` gives six bags: a `K_6^-` model in the
near-clique case and a `K_6` model in the clique case.  It does not give a
seventh bag.

There are three independent reasons the generalized paths do not supply
the two pole-reserved completing bags required by the shared-pole attack.

1. **The colouring is different.**  The proof of the generalized-chain
   lemma six-colours the proper minor obtained by contracting the star on
   `\{z\}\cup I`.  Its five remaining neighbours receive five distinct
   colours.  That colouring need not coincide with, and has not been
   identified with, the fixed all-rainbow colouring of the `D`-shore.
   Hence the paths in (1.2) are not the three fixed
   `beta`--`gamma_i` or `delta`--`gamma_i` coordinates.
2. **There is no shore confinement.**  In the two-cut geometry, a path
   from an `A`-root to a `T`-root must cross
   the six-set `(Z-\{z\})\cup \{p,q\}`.  Lemma 1.7 does not prescribe which boundary
   vertex it uses.  The rooted model may therefore consume either pole,
   other centres, and vertices of both open shores.
3. **Contractibility preserves roots, not a reserved complement.**  The
   `K_{1,1,3}` conversion supplies five disjoint rooted bags, but it has no
   clause leaving two connected subgraphs containing `p` and `q` and
   adjacent to all three non-centre core bags.  In the pole-incident case
   the incident pole is itself a root of the model, while the opposite
   pole may occur internally on a generalized path.

Thus arbitrary-demand disjointness solves a local rooted-minor packaging
problem but not the labelled placement problem.  In the pole-free row the
first local incidence residue is exactly (2.4); even outside that residue,
the first global unsupported inference is the existence of a connected
seventh bag, or of two prescribed pole-rooted helper bags, disjoint from
the rooted model.  A terminal continuation still needs a shore-reserving
conversion, a compatible boundary colouring, or a response-preserving
strict separation.

## Dependencies and claim status

- The all-rainbow profiles and critical-host hypotheses come from the
  separately audited global five-root palette alternative.
- The arbitrary-missing-edge path family is an established external input:
  Rolek--Song--Thomas, Lemma 1.7.
- Contractibility of `K_{1,1,3}` is an established external input:
  Kuendgen--Pelsmajer--Ramamurthi, Theorem 6.2.
- The scheme verification, the rooted-minor and model-separator
  corollaries, and the five-vertex classification are written proofs in
  this note.  No
  shore-confined rooted `K_5`, pole-reserved two-helper model, `K_7^-`
  minor, or closure of the five-centre branch is claimed.
