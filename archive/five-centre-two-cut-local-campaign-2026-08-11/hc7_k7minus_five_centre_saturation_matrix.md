# Five-centre saturation certificates and the two-shore composition matrix

**Status:** archived written proof; not separately audited.  The
results below give an exact global colouring obstruction for the five-centre
two-cut branch.  They do not eliminate the branch.

## 1. Setting and terminology

Let `G` satisfy

\[
 \chi(G)=7,
 \qquad
 \chi(M)\le 6\quad\hbox{for every proper minor }M\hbox{ of }G.
 \tag{1.1}
\]

Let

\[
                         Z=\{z_1,\ldots,z_5\}
\tag{1.2}
\]

be an independent set and put `F=G-Z`.  In the two-cut application,
`p,q\in V(F)` are nonadjacent and

\[
 F-\{p,q\}=C\mathbin{\dot\cup}D,
 \qquad E_F(C,D)=\varnothing .
\tag{1.3}
\]

For a proper six-colouring `phi` of `F`, define its set of **saturated
centres** by

\[
 \Sigma(\phi)=
 \{z\in Z:\phi(N_F(z))=\{1,\ldots,6\}\}.
\tag{1.4}
\]

Thus `phi` extends independently over all of `Z` if and only if
`Sigma(phi)` is empty.

## 2. The global minimal-saturation theorem

### Theorem 2.1 (every singleton is an exact saturation set)

One has

\[
                              \chi(F)=6.              \tag{2.1}
\]

More generally, for every nonempty set `A\subseteq Z`, there is a proper
six-colouring `phi_A` of `F` such that

\[
             \varnothing\ne\Sigma(\phi_A)\subseteq A.\tag{2.2}
\]

In particular, for every `i\in\{1,\ldots,5\}` there is a proper
six-colouring `phi_i` of `F` satisfying

\[
                         \Sigma(\phi_i)=\{z_i\}.       \tag{2.3}
\]

#### Proof

The graph `F` is a proper minor of `G`, so it is six-colourable.  If it
were five-colourable, the five independent vertices of `Z` could all be
given one new sixth colour.  This would six-colour `G`, proving (2.1).

Fix nonempty `A\subseteq Z`.  The graph `G-A` is a proper minor and hence
is six-colourable.  It is not five-colourable: a five-colouring of `G-A`,
together with one new colour on the independent set `A`, would again
six-colour `G`.  Restrict a proper six-colouring of `G-A` to `F`, and call
the restriction `phi_A`.

For every `z\in Z-A`, the colour assigned to `z` in `G-A` is absent from
`phi_A(N_F(z))`.  Hence no member of `Z-A` belongs to
`Sigma(phi_A)`.  If no member of `A` were saturated either, assign to each
vertex of `A` an independently chosen colour missing from its neighbourhood.
Together with the original colours on `Z-A`, this would extend `phi_A` to
a six-colouring of `G`.  Therefore (2.2) holds.  Taking `A={z_i}` gives
(2.3). \(\square\)

### Corollary 2.2 (degree-eight multiplicities)

If every member of `Z` has degree eight, then in the colouring `phi_i` the
six colour multiplicities on `N_F(z_i)=N_G(z_i)` are either

\[
                  3,1,1,1,1,1
       \qquad\hbox{or}\qquad
                  2,2,1,1,1,1.                       \tag{2.4}
\]

In particular, at least four colours have a unique representative in that
neighbourhood.

#### Proof

Independence of `Z` gives `N_F(z_i)=N_G(z_i)`.  Saturation makes all six
multiplicities positive, and they sum to eight.  These are the only two
partitions of eight into six positive parts. \(\square\)

Theorem 2.1 is stronger than merely knowing that every colouring of `F`
saturates some centre: the five proper-minor colourings realize every
singleton as the *only* saturated centre.  They are nevertheless five
potentially unrelated colourings.

## 3. The exact permutation-cover obstruction

Fix a proper six-colouring `phi` of `F`.  Globally rename its colours so
that the colours on `p,q` are fixed labels.  Let `Gamma_phi` be the group
of permutations of the six colours which fixes those pole labels
pointwise.  Thus

\[
 \Gamma_\phi\cong
 \begin{cases}
  S_5,&\phi(p)=\phi(q),\\
  S_4,&\phi(p)\ne\phi(q).
 \end{cases}                                         \tag{3.1}
\]

For `z\in Z`, put

\[
 \begin{aligned}
 A_z&=\phi\bigl(N_F(z)\cap(C\cup\{p,q\})\bigr),\\
 B_z&=\phi\bigl(N_F(z)\cap D\bigr),\\
 \mathcal B_z&=\{\sigma\in\Gamma_\phi:
                 A_z\cup\sigma(B_z)=\{1,\ldots,6\}\}.
 \end{aligned}                                      \tag{3.2}
\]

Here `A_z,B_z` are sets of colours, not multisets.

### Theorem 3.1 (five containment cylinders cover the pole stabilizer)

For every `phi`,

\[
                         \Gamma_\phi
                  =\bigcup_{z\in Z}\mathcal B_z.     \tag{3.3}
\]

If `phi=phi_i` is chosen as in Theorem 2.1, then the identity permutation
belongs to `mathcal B_{z_i}` and to no other member of the cover.

#### Proof

For `sigma\in\Gamma_phi`, retain `phi` on `C\cup\{p,q\}` and apply
`sigma` to all colours on `D`.  Because `sigma` fixes the pole colours and
there are no `C-D` edges, this gives a proper six-colouring `phi^sigma` of
`F`.  By (3.2), a centre `z` is saturated under `phi^sigma` exactly when
`sigma\in\mathcal B_z`.

If `sigma` belonged to none of the five sets, every centre would miss a
colour and could be coloured independently.  This would six-colour `G`.
Thus (3.3) holds.  The assertion about the identity is exactly (2.3).
\(\square\)

The sizes of the five covering sets are explicit.  Let `P_0` be the set
of the one or two fixed pole colours, put `R_0=[6]-P_0`, and write

\[
 m=|R_0|,\qquad
 R_z=[6]-A_z,\qquad
 r_z=|R_z\cap R_0|,\qquad
 b_z=|B_z\cap R_0|.                                  \tag{3.4}
\]

### Lemma 3.2 (exact cylinder size)

If

\[
 R_z\cap P_0\nsubseteq B_z\cap P_0
 \quad\hbox{or}\quad r_z>b_z,                        \tag{3.5}
\]

then `mathcal B_z` is empty.  Otherwise

\[
 |\mathcal B_z|
   =m!\,\frac{\binom{b_z}{r_z}}{\binom{m}{r_z}}.     \tag{3.6}
\]

Consequently every surviving two-cut satisfies the necessary cover
inequality

\[
 \sum_{z\in Z}
   \frac{\binom{b_z}{r_z}}{\binom{m}{r_z}}
 \ge1,                                               \tag{3.7}
\]

where a term is zero when (3.5) holds.

#### Proof

The fixed-colour condition in (3.5) is plainly necessary, as is
`r_z\le b_z`.  Subject to those conditions, `sigma(B_z\cap R_0)` is a
uniformly distributed `b_z`-set in the `m` free colours.  It contains the
specified `r_z`-set `R_z\cap R_0` for

\[
 \binom{m-r_z}{b_z-r_z}\,b_z!\,(m-b_z)!
 =m!\,\frac{\binom{b_z}{r_z}}{\binom{m}{r_z}}
\]

permutations.  This proves (3.6).  The union bound applied to (3.3) gives
(3.7). \(\square\)

## 4. Three singleton witnesses of one pole type

Among the five colourings `phi_1,\ldots,phi_5`, at least three give the
same equality type on `p,q`.  Fix three such indices `I={i,j,k}`.  Rename
colours globally in each colouring so that the colours on `p,q` agree
pointwise.  For ordered `a,b\in I`, define `theta_ab` by using `phi_a` on
`C\cup\{p,q\}` and `phi_b` on `D`, and put

\[
                         \Sigma_{ab}=\Sigma(\theta_{ab}).
\tag{4.1}
\]

### Lemma 4.1 (the cross-composition matrix)

Every entry of the `3 by 3` matrix `(Sigma_ab)` is nonempty, while

\[
                         \Sigma_{aa}=\{z_a\}
                    \qquad(a\in I).                  \tag{4.2}
\]

#### Proof

The two restrictions used to define `theta_ab` agree at `p,q`, and (1.3)
makes their union a proper colouring of `F`.  An empty saturation set would
extend over the independent set `Z` and six-colour `G`.  This proves
nonemptiness.  The diagonal entry is the original colouring `phi_a`, so
(4.2) follows from (2.3). \(\square\)

The following elementary consequence records exactly what three equal-type
witnesses force, without identifying their colourings.

### Lemma 4.2 (persistence, external ownership, or a directed cycle)

Choose one centre `o_ab\in Sigma_ab` for each ordered pair of distinct
indices `a,b\in I`.  At least one of the following holds.

1. **External ownership:** `o_ab\notin\{z_a,z_b\}` for some ordered pair.
2. **One-shore persistence:** for some distinct `a,b,c\in I`, either

   \[
                  o_{ab}=o_{ac}=z_a
       \quad\hbox{or}\quad
                  o_{ba}=o_{ca}=z_a.                 \tag{4.3}
   \]

3. **Directed three-cycle:** after cyclically naming the indices `a,b,c`,

   \[
   o_{ab}=o_{ba}=z_a,
   \qquad
   o_{bc}=o_{cb}=z_b,
   \qquad
   o_{ca}=o_{ac}=z_c.                                \tag{4.4}
   \]

#### Proof

Assume outcomes 1 and 2 fail.  Every `o_ab` is one of `z_a,z_b`.  Draw
the directed arc `a\to b` when `o_ab=z_a`.  Failure of the first alternative
in (4.3) says that every vertex has outdegree at most one.  Failure of the
second says that at most one of the two entries in column `a` is owned by
`z_a`; equivalently, the indegree of `a` in the directed graph is at least
one.

There are three vertices.  The sum of the outdegrees is at most three,
while the sum of the indegrees is at least three; the two sums are equal.
Hence every vertex has indegree and outdegree one.  The directed arcs form
a three-cycle.  If `a\to b` is an arc, the reverse arc `b\to a` is absent,
so both matrix entries indexed by the unordered pair `{a,b}` are owned by
`z_a`.  This is exactly (4.4). \(\square\)

For a centre `x\in Z` and an index `a\in I`, write

\[
 \begin{aligned}
 A_a^x&=\phi_a\bigl(N_F(x)\cap(C\cup\{p,q\})\bigr),\\
 B_a^x&=\phi_a\bigl(N_F(x)\cap D\bigr).
 \end{aligned}                                      \tag{4.5}
\]

The directed-cycle alternative contains a literal three-corner palette
obstruction, not just an ownership table.

### Lemma 4.3 (the missing fourth corner has a named colour)

Suppose the directed cycle in (4.4) contains the arc `a\to b`.  There is a
colour `lambda_ab` such that

\[
 \lambda_{ab}\in A_a^{z_a}\cap B_a^{z_a},
 \qquad
 \lambda_{ab}\notin A_b^{z_a}\cup B_b^{z_a}.        \tag{4.6}
\]

Thus `lambda_ab` occurs on both shores of `N_F(z_a)` in `phi_a` and is
absent from the whole neighbourhood in `phi_b`.  If `z_a` is adjacent to
at least one pole, then `lambda_ab` is not a fixed pole colour.

#### Proof

The centre `z_a` is saturated in the three entries

\[
                         (a,a),\quad(a,b),\quad(b,a),
\]

by (4.2) and (4.4), but it is not saturated in `(b,b)` because
`Sigma_bb={z_b}`.  Choose

\[
             \lambda_{ab}\notin A_b^{z_a}\cup B_b^{z_a}.
\]

Saturation in `(a,b)` forces `lambda_ab\in A_a^{z_a}`, while saturation
in `(b,a)` forces `lambda_ab\in B_a^{z_a}`.  This proves (4.6).  If
`z_a` is adjacent to a pole, the fixed colour of that pole belongs to
`A_b^{z_a}` in every normalized colouring, so it cannot be
`lambda_ab`. \(\square\)

## 5. Exact nonclosure

The saturation theorem and the matrix lemmas do not synchronize shore
colourings.  In (4.3), the repeated centre is saturated in two different
colourings of the other shore.  In (4.4), the three repeated centres occur
around three different pairs of colourings.  Lemma 4.3 names one missing
fourth-corner colour, but its three instances still belong to different
centres and different pairs of colourings.  None of these conclusions gives
one colouring with an empty saturation set, a common missing colour, or
common bichromatic paths.

The containment cover itself admits the sharp contact sizes appearing in
the shared-pole row.  For example, in the equal-pole case the free group is
`S_5`.  Five abstract cylinders with `r_z=1` and `b_z=3` can cover `S_5`
while the identity belongs only to the first.  Label free colours
`1,\ldots,5`; let the complements of the five three-element domain sets be

\[
 \{2,3\},\ \{2,3\},\ \{2,3\},\ \{2,4\},\ \{2,5\},   \tag{5.1}
\]

and let the five demanded image colours be `1,2,3,4,5`, respectively.
Every permutation violates at least one demand because all five complement
sets have union `{2,3,4,5}` and therefore admit no system of distinct
representatives.  The identity violates only the first demand.  These are
exactly the cylinder parameters allowed by the contact profile
`(c_z,d_z,rho_z)=(4,3,1)`.  This is an abstract palette certificate, not a
graph counterexample; it proves that cardinalities and the private identity
alone do not eliminate that profile.

There is an even simpler obstruction in the distinct-pole four-contact
profile.  If a centre adjacent to both poles sees all four free colours on
its four `C`-contacts, then it is saturated on `C\cup\{p,q\}` alone.  Its
set `mathcal B_z` is the whole pole stabilizer, independently of the
`D`-shore permutation.

The first unsupported inference is therefore precise:

> infer from five separately obtained singleton-saturation colourings, or
> from the persistence/cycle alternatives in Lemma 4.2, one common relative
> shore permutation under which no centre is saturated.

That inference is false at the level of the exact palette-cover data above.
A terminal theorem must use additional graph structure to couple the
different colourings--for example common Kempe components, a prescribed
rooted minor, or an actual smaller separation retaining one fixed boundary
partition.

The classical Dirac--Gallai two-cut theorem for critical graphs does not
remove this obstruction.  The graph `F` is six-chromatic but is not known
to be critical, whereas the critical graph `G` has the seven-vertex cut
`Z\mathbin{\dot\cup}\{p,q\}`, not the two-cut `{p,q}`.  Passing to an
unspecified six-critical subgraph of `F` need not retain both shores or any
of the five degree-eight neighbourhoods.
