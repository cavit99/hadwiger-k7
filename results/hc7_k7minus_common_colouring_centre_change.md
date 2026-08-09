# A common colouring at several degree-eight vertices

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_common_colouring_centre_change_audit.md`](hc7_k7minus_common_colouring_centre_change_audit.md).

This note recolours four selected colour classes in the common graph
`H=G-U`.  It either changes the vertex deleted by the critical colouring
without changing the colouring of `H`, or places several degree-eight
vertices in one common saturated colouring.  A separate comparison theorem
shows that every new exact four-centre cut is either the old minimum cut or
a strict cut inside its opposite component.

The ordinary rooted-model-or-web dichotomy used below is not new.  The new
data are the common colouring and the exact comparison of the resulting
cuts.

## 1. Recolouring the selected classes

Use the setting of the audited
[four-centre rooted-web theorem](hc7_k7minus_four_centre_web_cut_lattice.md).
Thus `G` is seven-connected, every proper minor of `G` is six-colourable,
`chi(G)=7`, `G` has no `K_7^-` minor, `U` is an independent set of four
degree-eight vertices, and `H=G-U` is three-connected, nonplanar, and
six-chromatic.

Fix `r in U` and a proper six-colouring `phi` of `G-r`.  Choose four
colours `c_1,...,c_4` which occur exactly once on `N_G(r)`, let their
representatives be `X={x_1,...,x_4}`, and suppose that `H` has no
`X`-rooted `K_4` model.  Let `Delta` be the other two colours and put

\[
 J=H[\phi^{-1}(\{c_1,c_2,c_3,c_4\})].                \tag{1.1}
\]

### Theorem 1.1 (a common saturated colouring)

The graph `J` is four-chromatic.  It has a proper four-colouring `psi`
which uses at most three colours on `X`.  Combining `psi` with the two
unchanged `Delta`-colour classes of `phi` gives a proper six-colouring
`theta` of `H`.

Define

\[
 \Sigma(\theta)=
 \{u\in U:\theta(N_H(u))=\{1,\ldots,6\}\}.            \tag{1.2}
\]

Then

\[
                 \varnothing\ne\Sigma(\theta)
                 \subseteq U-\{r\}.                  \tag{1.3}
\]

Every `s in Sigma(theta)` has at least four colours which occur exactly
once on `N_H(s)`.

#### Proof

The restriction of `phi` four-colours `J`.  A three-colouring of `J`,
together with the two untouched colour classes, would five-colour `H`.
Thus `chi(J)=4`.

Martinsson and Steiner's colourful-set theorem says that if four nominated
vertices receive four different colours in every proper four-colouring of
a four-chromatic graph, then the graph contains a rooted `K_4` at those
vertices.  Their rooted convention asks each of four disjoint branch sets
to meet the four-set; with four roots this places one root in each branch
set.  The contrapositive gives `psi`.  The palettes used on `J` and on the
two untouched classes are disjoint, so their union is the asserted
colouring `theta` of `H`.

The selected representatives are the only neighbours of `r` in their four
old colour classes.  They use at most three colours under `psi`; the other
neighbours of `r` use the two untouched colours.  Hence `r` misses a colour
under `theta` and is not in `Sigma(theta)`.

If `Sigma(theta)` were empty, assign to each vertex of the independent set
`U` a colour missing from its neighbourhood.  This would extend `theta` to
a six-colouring of `G`.  Thus (1.3) holds.  Finally, six positive colour
multiplicities on the eight neighbours of a saturated degree-eight vertex
have total excess two.  At least four of them are therefore one.  \(\square\)

## 2. Changing the deleted vertex

For `s in Sigma(theta)`, choose representatives

\[
                         Y_s=\{y_1,y_2,y_3,y_4\}       \tag{2.1}
\]

of any four singleton colour classes on `N_H(s)`.

### Theorem 2.1

If `Sigma(theta)={s}`, then `theta` extends over `U-{s}` to a proper
six-colouring `widehat theta` of `G-s`.  For every choice (2.1), the
four-centre rooted-web theorem applied with deleted vertex `s` gives one
of the following:

1. `H` contains a `Y_s`-rooted `K_4` model.  Its four branch sets together
   with `{s}` form an `s`-rooted `K_5` model in `G-(U-{s})`.
2. There is an exact cut `U dotcup T_s` with two full connected components
   and the one-sided colouring trace induced by `widehat theta`.

The restriction of `widehat theta` to `H` is exactly `theta`.  In
particular, the graph `J` and the two original `Delta`-colour classes are
retained as vertex sets.  The four singleton classes chosen at `s` need not
be the original four classes chosen at `r`.

If `|Sigma(theta)|>=2`, the same colouring need not extend to `G-s` for a
saturated vertex `s`.  Nevertheless, for every such `s` and every choice
(2.1), one of the following holds:

1. there is an `s`-rooted `K_5` model as above; or
2. there is a three-set `T_s` such that

   \[
    H-T_s=E_s\mathbin{\dot\cup}F_s,
    \qquad
    N_G(E_s)=N_G(F_s)=U\mathbin{\dot\cup}T_s.          \tag{2.2}
   \]

   The two components are connected and full to the displayed boundary.
   All four vertices of `Y_s` avoid the component behind the facial
   three-set, and at least one belongs to the other component.

No one-sided colouring trace is asserted in the second part.  If
`kappa(G)=8`, the cut alternative is impossible.

#### Proof

In the unique-saturation case, each vertex of the independent set
`U-{s}` misses a colour on its neighbourhood under `theta`.  Assign these
missing colours independently.  This gives `widehat theta`, and the first
assertion is the four-centre rooted-web theorem with `s` and `Y_s` in place
of `r` and `X`.

For the multiple-saturation statement, apply the rooted `K_4` theorem of
Fabila-Monroy and Wood directly to the three-connected graph `H` and the
four nominated vertices `Y_s`.  A rooted model gives the first outcome.
Otherwise `H` is a spanning subgraph of a `Y_s`-web.  Since `H` is
nonplanar, a nonempty component lies behind a facial three-set `T_s` of the
web.  Three-connectivity gives its full neighbourhood `T_s` in `H`, and
seven-connectivity gives full neighbourhood `U union T_s` in `G`.  The
two-component theorem for seven-vertex cuts gives (2.2).  Vertices in the
component behind the facial three-set avoid all four outer roots, and at
least one root lies outside the three-set.  Eight-connectivity excludes
(2.2).  \(\square\)

## 3. Comparing exact four-centre cuts

Let

\[
 H-T=C\mathbin{\dot\cup}D                              \tag{3.1}
\]

be the minimum trace-admissible cut, oriented toward its selected component
`C`.  The following theorem applies to every exact four-centre cut, not
only to those obtained in Theorem 2.1.

### Theorem 3.1 (opposite-side boundary replacement)

Let `T'` be a three-set and let

\[
 H-T'=A\mathbin{\dot\cup}B,
 \qquad
 N_G(A)=N_G(B)=U\mathbin{\dot\cup}T'.                 \tag{3.2}
\]

After exchanging `A,B` if necessary, either (3.2) is the old cut (3.1), or

\[
                         C\subseteq A,
 \qquad
                         \varnothing\ne B\subsetneq D. \tag{3.3}
\]

In the second case, put

\[
 R=T\cap T',
 \qquad
 Z=T'\cap D.                                          \tag{3.4}
\]

Then

\[
 T'=R\mathbin{\dot\cup}Z,
 \qquad
 1\le |Z|\le3,
 \qquad
 Z=N_D(B),                                            \tag{3.5}
\]

and `B` is anticomplete to `T-R`.  Thus a distinct non-descending cut
replaces `|Z|` vertices of the old three-vertex boundary by the same number
of vertices internal to `D`.

#### Proof

First observe that every component behind an exact four-centre cut has at
least three vertices.  A singleton would have degree at most seven.  If a
component had two vertices, both would be adjacent to each other and to all
seven boundary vertices, by minimum degree eight.  Either vertex would
then have the independent four-set `U` in its degree-eight neighbourhood,
contrary to the degree-eight neighbourhood theorem.

Neither `C` nor `D` is contained in `T'`.  Otherwise it would equal `T'`,
while deleting it would leave the opposite old closed shore connected,
contrary to (3.2).

Suppose first that both open components in (3.2) meet `C`.  Choose a vertex
of `D-T'`, orient (3.2) so that it lies on the opposite side from some
vertex of `C-T'`, and take the meet with the old separation.  The
fixed-anchor exact uncrossing theorem returns an exact four-centre cut whose
selected open side is a nonempty proper subset of `C`.

Assume the first case does not hold.  The same conclusion follows if `T'`
meets `C`.  After exchanging `A,B`, all of `C-T'` lies in `A`.  The
component `B` must meet `D`.  Otherwise `B subseteq T`; the
three-vertex lower bound forces `B=T`, and `A` would contain nonempty
anticomplete parts of `C` and `D`, contrary to its connectedness.  Orient
the cut with `C-T'` in `A` and a vertex of `B cap D` in `B`, and take the
same exact meet.  Its selected side omits `T' cap C` and is again a
nonempty proper subset of `C`.

In either paragraph the new selected closed side lies inside
`C union U union T`.  The old colouring therefore restricts to it, every
nominated root still avoids the selected component, and the fixed opposite
root remains in the opposite open side.  This is a strict trace-admissible
descent, contradicting the choice of `C`.

It follows that `T' cap C` is empty and all of `C` lies in one component,
say `A`.  Every vertex of `T` has a neighbour in `C`, so the other component
`B` contains no vertex of `T`.  Hence `B subseteq D`.  If `B=D`, then
`T'=N_H(D)=T`, and (3.2) is (3.1).  Otherwise (3.3) holds.

Now `T' subseteq D union T`.  The set `Z` is nonempty, since `Z=emptyset`
would give `T'=T` and hence `B=D`.  Fullness in (3.2) gives
`N_D(B)=T' cap D=Z`.  Every vertex of `T-R` lies with `A`, so it is
anticomplete to `B`.  Equations (3.4)--(3.5) follow.  \(\square\)

The component `B` in (3.3) is not full to the old boundary and carries no
old selected-side trace.  The theorem therefore identifies the exact
remaining geometry; it does not turn the new cut into a second strict
descent.

## 4. The minimal opposite-side cut family

Let \(\mathcal B\) be the inclusion-minimal family of nonempty sets which occur
as the component on the `D`-side of an exact four-centre cut oriented away
from `C`.  Include `D` itself, from the old cut, before taking the minimal
members.  For \(B\in\mathcal B\), write `T_B=N_H(B)` and define a graph
\(\Gamma\) on \(\mathcal B\) by joining two members when they are adjacent in
`H`.

### Corollary 4.1

Distinct members of \(\mathcal B\) are disjoint, and

\[
 \Delta(\Gamma)\le3,
 \qquad
 \alpha(\Gamma)\le2,
 \qquad
 |\mathcal B|\le4.                                    \tag{4.1}
\]

If \(|\mathcal B|=4\), then

\[
                         \Gamma\in\{2K_2,P_4,C_4\}.   \tag{4.2}
\]

#### Proof

Suppose that distinct \(B_1,B_2\in\mathcal B\) meet at a vertex `b`.  Choose
`c in C`.  The two exact separations are oriented with `c` on their common
left side and `b` on their common right side.  Fixed-anchor exact
uncrossing makes their join another exact four-centre separation, whose
right open side is `B_1 cap B_2`.  The two-component theorem makes this set
connected.  It is a nonempty member of the family contained in both
`B_1,B_2`, contrary to inclusion-minimality unless `B_1=B_2`.  Thus the
members are pairwise disjoint.

If `B_i,B_j` are adjacent, some vertex of `B_j` belongs to
`N_H(B_i)=T_{B_i}`.  The members of \(\mathcal B\) are disjoint, so different
neighbours of `B_i` in \(\Gamma\) use different vertices of `T_{B_i}`.
Therefore \(d_\Gamma(B_i)\le3\).

Suppose that three members `B_1,B_2,B_3` are pairwise nonadjacent.  For any
`u in U`, choose one neighbour of `u` in each `B_i` and one in `C`.
Fullness of the four exact cuts supplies these four vertices.  They are
pairwise nonadjacent because `C` is anticomplete to `D` and the three
members are pairwise nonadjacent.  This contradicts
`alpha(G[N(u)])=3`, so \(\alpha(\Gamma)\le2\).

If \(\Gamma\) contains a triangle `B_1B_2B_3B_1` and has a fourth vertex
`B_4`, write `U={u_1,u_2,u_3,u_4}`.  The seven disjoint connected sets

\[
 B_1,\ B_2,\ B_3,\ B_4\cup\{u_1\},\
 C\cup\{u_2\},\ \{u_3\},\ \{u_4\}                   \tag{4.3}
\]

are pairwise adjacent except possibly for the last two.  Adjacencies among
the first three come from the triangle; every other required adjacency
comes from the fact that `C,B_1,...,B_4` are adjacent to every vertex of
`U`.  Thus (4.3) is a `K_7^-` model, a contradiction.  Consequently
\(\Gamma\) is triangle-free whenever it has at least four vertices.

Suppose now that `|mathcal B|>=5` and choose five members.  Their induced
interaction graph is triangle-free and has independence number at most two,
so it is a five-cycle.  Label it cyclically as
`B_1B_2B_3B_4B_5B_1`.  Then

\[
 B_1,\ B_2,\ B_3,\ B_4\cup\{u_1\},\
 B_5\cup\{u_2\},\ C\cup\{u_3\},\ \{u_4\}            \tag{4.4}
\]

are disjoint connected branch sets.  They are pairwise adjacent except
possibly for `B_1,B_3`: the cycle supplies the required adjacencies among
the first five sets, and boundary fullness supplies every adjacency using
a member of `U`.  This is again a `K_7^-` model.  Hence
`|mathcal B|<=4`.

In the equality case, both \(\Gamma\) and its complement are triangle-free:
the first by (4.3), the second because \(\alpha(\Gamma)\le2\).  The three
graphs on four vertices with this property are `2K_2`, `P_4`, and `C_4`.
This proves (4.2).  \(\square\)

The corollary bounds the inclusion-minimal opposite-side cut family, not
the orders of its members or the number of nonminimal exact cuts.

The equality case forces a second family of minimum cuts.  Put

\[
 \mathcal P=\{C\}\cup\mathcal B,
 \qquad
 T_C=T,
 \qquad
 T_B=N_H(B)\quad(B\in\mathcal B).                    \tag{4.5}
\]

### Corollary 4.2 (simultaneous centre replacement)

Suppose that `|mathcal B|=4`.  For `P in mathcal P`, put

\[
 W_P=\{u\in U:|N_G(u)\cap P|=1\},                    \tag{4.6}
\]

and denote the unique neighbour of `u in W_P` in `P` by `x_{uP}`.  These
vertices are distinct for distinct members of `W_P`.

For every nonempty set `W subseteq W_P`, let

\[
 X(P,W)=\{x_{uP}:u\in W\},
 \qquad
 Z(P,W)=(U-W)\cup T_P\cup X(P,W).                    \tag{4.7}
\]

Then `Z(P,W)` is an exact order-seven cut, and `P-X(P,W)` is one of its
two full connected components and has at least two vertices.  All cuts
`Z(P,W)`, over all eligible pairs `(P,W)`, are distinct.

Moreover,

\[
 \sum_{P\in\mathcal P}|W_P|\ge8,                     \tag{4.8}
\]

so the five pieces give at least eleven simultaneous-replacement cuts.
Together with their five original four-centre cuts, the equality case
`|mathcal B|=4` therefore forces at least sixteen distinct exact
order-seven cuts.

#### Proof

Every centre is adjacent to each of the five pairwise disjoint connected
sets in `mathcal P`.  For `u in U`, put

\[
 m_{uP}=|N_G(u)\cap P|,
 \qquad
 r_u=8-\sum_{P\in\mathcal P}m_{uP}\ge0.              \tag{4.9}
\]

Since `|mathcal P|=5` and `d_G(u)=8`,

\[
       \sum_{P\in\mathcal P}(m_{uP}-1)+r_u=3.         \tag{4.10}
\]

At most three of the five nonnegative terms `m_{uP}-1` are positive.
Thus every centre has a unique neighbour in at least two members of
`mathcal P`, proving (4.8).

Fix `P`.  Two centres in `W_P` cannot have the same unique neighbour `x`.
Otherwise `P-x` is nonempty and has neighbourhood contained in

\[
                       (U-\{u,v\})\cup T_P\cup\{x\},
\]

a set of order six, while the old opposite component survives.  This
contradicts seven-connectivity.

We next prove the assertion about `Z(P,W)` by induction on `|W|`.  For a
singleton `W={u}`, the set `P-x_{uP}` has at least two vertices because
`|P|>=3`.  In the inductive step, assume the conclusion for a proper
nonempty subset of `W` and remove one further unique neighbour.  Distinctness
of the unique neighbours and the inductive lower bound of two ensure that
the new remainder is nonempty.

Let `O_P` be the component opposite `P` in its original four-centre cut.
For the singleton base case and each inductive step,

\[
 V(G-Z(P,W))=
 \bigl(P-X(P,W)\bigr)
 \mathbin{\dot\cup}
 \bigl(O_P\cup W\bigr).                              \tag{4.11}
\]

The second set is connected because `O_P` is connected and adjacent to
every centre.  Every component `A` of the first set has all its neighbours
in the seven-set `Z(P,W)`: the old cut gives
`N_G(P)=U union T_P`, and each centre in `W` has had its only neighbour in
`P` removed.  Seven-connectivity makes `N_G(A)=Z(P,W)`.  The two-component
theorem then makes `P-X(P,W)` connected and full to the displayed boundary.
It cannot be a singleton, since such a vertex would have degree seven.
This completes the induction and proves the cut assertion.

The replacement cuts are distinct.  Their intersections with `U` determine
`W`.  If the same `W` and distinct pieces `P,Q` gave the same cut, the two
nonempty remainders would be distinct components after deleting that cut.
Any vertex of the nonempty set `W` survives and is anticomplete to both
remainders, so it lies in a third component, contrary to the two-component
theorem.

Finally, if `k_P=|W_P|`, the number of replacement cuts is

\[
                    \sum_{P\in\mathcal P}(2^{k_P}-1). \tag{4.12}
\]

Subject to five nonnegative integer values with sum at least eight, this is
minimized at `2,2,2,1,1`, and is then eleven.  The four minimal members of
`mathcal B` give distinct cuts by the two-component theorem, and none is
the old `C`-cut: otherwise it would be the whole old opposite component
`D`, which is not inclusion-minimal in a four-member family.  These five
original cuts have all four vertices of `U` in their boundaries, whereas
every cut in (4.12) has fewer.  The total is therefore at least sixteen.
\(\square\)

The simultaneous replacements also have an exact lattice structure.  Use
the usual order on oriented separations:
`(A,B) <= (A',B')` when `A subseteq A'` and `B supseteq B'`.

### Corollary 4.3 (Boolean sublattices of replacement cuts)

Retain the equality case of Corollary 4.2 and fix `P in mathcal P`.  For
every `W subseteq W_P`, including the empty set, let

\[
 A_W=P\cup T_P\cup(U-W),
 \qquad
 B_W=O_P\cup T_P\cup U\cup X(P,W),                  \tag{4.13}
\]

where `O_P` is the component opposite `P` in its original four-centre cut.
Then `(A_W,B_W)` is a proper separation of order seven, with open sides

\[
 A_W-B_W=P-X(P,W),
 \qquad
 B_W-A_W=O_P\cup W.                                  \tag{4.14}
\]

For all `W_1,W_2 subseteq W_P`,

\[
 \begin{aligned}
 (A_{W_1},B_{W_1})\wedge(A_{W_2},B_{W_2})
   &=(A_{W_1\cup W_2},B_{W_1\cup W_2}),\\
 (A_{W_1},B_{W_1})\vee(A_{W_2},B_{W_2})
   &=(A_{W_1\cap W_2},B_{W_1\cap W_2}).             \tag{4.15}
 \end{aligned}
\]

Thus these separations form a sublattice anti-isomorphic to the Boolean
lattice on `W_P`.  At least one member of `mathcal P` has `|W_P|>=2`, so
the equality case contains a four-element Boolean sublattice.  A proper
six-colouring of `G[A_emptyset]` restricts to every `G[A_W]`; in particular,
the resulting boundary partitions on `Z(P,W)`, for all `W subseteq W_P`,
come from one common colouring.

#### Proof

For `W=emptyset`, (4.13) is the original exact four-centre separation of
`P`.  For nonempty `W`, Corollary 4.2 gives (4.14), and its boundary is

\[
 A_W\cap B_W=(U-W)\cup T_P\cup X(P,W)=Z(P,W).
\]

This has order seven and both open sides are nonempty.  The meet and join
identities in (4.15) follow directly from (4.13) and
`X(P,W_1) cap X(P,W_2)=X(P,W_1 cap W_2)`.  Finally,
(4.8) and `|mathcal P|=5` give `|W_P|>=2` for some `P`.  The graph
`G[A_emptyset]` is a proper minor of `G`, since `O_P` is nonempty, and is
therefore six-colourable.  The colouring assertion follows from
`A_W subseteq A_emptyset`.  \(\square\)

## External input and internal dependencies

- A. Martinsson and R. Steiner, *Strengthening Hadwiger's conjecture for
  4- and 5-chromatic graphs*, J. Combin. Theory Ser. B **164** (2024),
  1--16,
  <https://doi.org/10.1016/j.jctb.2023.08.009>, Theorem 1.3.
- R. Fabila-Monroy and D. R. Wood, *Rooted `K_4`-Minors*, Electron. J.
  Combin. **20**(2) (2013), Paper P64,
  <https://doi.org/10.37236/3476>, Theorem 8.
- [Four-centre rooted-web theorem and exact cut lattice](hc7_k7minus_four_centre_web_cut_lattice.md).
- [Trace-preserving minimum four-centre cut](hc7_k7minus_four_centre_trace_descent.md).
- [Two-component normal form for seven-vertex cuts](hc7_k7minus_three_component_seven_cut_exclusion.md), Corollary 2.
- [Degree-eight neighbourhood structure](hc7_k7minus_exceptional_neighbourhood_completion.md), Theorem 2.
