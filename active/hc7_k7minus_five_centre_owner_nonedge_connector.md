# A terminal connector for the unique-owner completion residue

**Status:** written proof; separate hash-pinned internal audit **GREEN** in
[`hc7_k7minus_five_centre_owner_nonedge_connector_audit.md`](hc7_k7minus_five_centre_owner_nonedge_connector_audit.md).
The results are unbounded.  This note identifies the exact
`D`-shore model which repairs both the artificial pole edge and the sole
owner-bag nonedge.  It uses the separately audited theorem that every four
boundary vertices root a `K_4` model on the `D`-shore to force at least
three one-sided owners with no opposite-side neighbour.  A contracted-shore
pole--owner merge eliminates six further deficiency patterns.  A second
composition with the universal four-boundary rooted `K_4` reduces every
remaining pattern to a forbidden minor or an actual nested separator.  The
latter separator is not yet trace-preserving, so the present five-centre
inputs do not yet force the full terminal connector.

Throughout, `K_t^-` denotes `K_t` with one edge deleted.

## 1. The unique-owner residue

Use the target-free normal form from the active
[critical-completion lift](hc7_k7minus_five_centre_completion_model_lift.md).
Thus

\[
 S=Z\mathbin{\dot\cup}\{p,q\},\qquad
 Z=\{z_1,\ldots,z_5\},
\]

and `G-S` has connected full components `C,D`.  There are pairwise
disjoint connected sets

\[
                         B,R_1,\ldots,R_5
\tag{1.1}
\]

which partition `C union {p,q}` and have the following properties.

1. The set `B` contains `p,q` and is connected after the artificial edge
   `pq` is added; that edge is essential to its connectivity.
2. For distinct indices other than one fixed pair `a,b`, all sets in
   (1.1) are adjacent.  The sole nonadjacent pair is `R_a,R_b`.
3. The centre ownership is bijective:

   \[
                         N_G(R_i)\cap Z=\{z_i\}
                         \qquad(1\le i\le5).
   \tag{1.2}
   \]

The earlier lift already eliminates a sole nonedge of the form `BR_i`.
Thus (1.1)--(1.2) are the exact completion-model residue, not an extra
case split introduced here.

## 2. Splitting the artificial-edge bag

Let `B_p,B_q` be the two components of `G[B]`, labelled by their pole.
They are exactly two: in the completion graph the sole added edge `pq` is
an essential edge of the connected branch set `B`.  Since `B` is adjacent
to every `R_i`, each owner bag is adjacent to at least one of `B_p,B_q`.
Call `R_i` **one-sided** if it is adjacent to exactly one of `B_p,B_q`,
and **two-sided** otherwise.  In the orbit codes below, `P,Q,B` mean
`B_p`-only, `B_q`-only, and both, respectively.  The letter `B` in a code
does not denote the pole-pair branch set.

Let `J` be the eight-vertex branch-contact graph on

\[
                    x,B_p,B_q,R_a,R_b,R_c,R_d,R_e,              \tag{2.1}
\]

where `x` is universal and `B_pB_q` is the artificial edge.  The only
possible owner-bag nonedge is `R_aR_b`.

### Lemma 2.1 (a pole component meets at most three owner bags)

If one of `B_p,B_q` is adjacent to at least four of the owner bags, then
`G` contains a `K_7^-` minor.

#### Proof

Suppose first that `B_p` is adjacent to all five owner bags.  In `J`,
merge `x` with `B_q`.  The resulting seven bags are pairwise adjacent
except possibly for `R_aR_b`, and `p,q` lie in distinct bags.  The
critical-completion lift is terminal.

Suppose instead that `B_p` has exactly four owner-bag neighbours, and let
`R_j` be the fifth.  Then `R_j` is adjacent to `B_q`.  In `J`, merge
`B_q` with `R_j`.  This merged bag is adjacent to `B_p` through the
artificial edge.  If `j` is outside `\{a,b\}`, it is adjacent to all four
remaining owner bags, whose only possible nonedge is `R_aR_b`.  If
`j\in\{a,b\}`, it is adjacent to the three owner bags outside the missing
pair; its possible nonadjacency to the other endpoint of that pair is the
only missing edge.  The bag `B_p` sees all four remaining owner bags in
either case.  Together with the universal singleton `\{x\}`, these are
seven bags with at most one nonedge and with the poles in distinct bags.
The critical-completion lift again gives the required minor in `G`.
\(\square\)

### Theorem 2.2 (exact three-orbit split classification)

If `G` has no `K_7^-` minor, then, up to interchanging the poles,
interchanging `a,b`, and permuting `c,d,e`, its pole-side incidence code
is exactly one of

\[
                         \boxed{PQBPQ},\qquad
                         \boxed{PQPPQ},\qquad
                         \boxed{PPPQQ}.               \tag{2.2}
\]

Thus at least four owner bags are one-sided, at most one is two-sided,
and the missing-edge owners `R_a,R_b` are one-sided.

#### Proof

If `m` owner bags are two-sided, the total number of incidences with
`B_p,B_q` is `5+m`.  Lemma 2.1 bounds both pole-side degrees by three, so
`m\le1`.

The remaining possibilities have six orbits.  The table uses the index
order `a,b,c,d,e`; the displayed contraction is performed in `J`.

| two-sided bags | position of `R_a,R_b` | code | quotient outcome |
|---|---|---|---|
| none | opposite sides | `PQPPQ` | survives |
| none | together on the degree-three side | `PPPQQ` | survives |
| none | together on the degree-two side | `PPQQQ` | contract `B_pR_a` |
| one ordinary bag | opposite sides | `PQBPQ` | survives |
| one ordinary bag | same side | `PPBQQ` | contract `B_pR_a` |
| one missing-edge owner | — | `BPPQQ` | contract `B_pR_b` |

The six rows are exhaustive: with no two-sided bag the pole-side degrees
are `3,2`, and the missing pair is split, together on the larger side, or
together on the smaller side.  With one two-sided bag both degrees are
three, and that bag is either outside the missing pair with the pair split,
outside it with the pair together, or itself an endpoint of the pair.

For each of the three terminal rows, the indicated contraction leaves a
six-vertex contact graph with exactly one possible nonedge.  Explicitly,
the six bags besides `\{x\}` are, respectively,

\[
\begin{array}{c|c}
 PPQQQ & B_p\cup R_a,\ B_q,\ R_b,R_c,R_d,R_e,\\
 PPBQQ & B_p\cup R_a,\ B_q,\ R_b,R_c,R_d,R_e,\\
 BPPQQ & B_p\cup R_b,\ B_q,\ R_a,R_c,R_d,R_e.
\end{array}                                                   \tag{2.3}
\]

Their possible missing edges are `B_qR_b`, `B_qR_b`, and `B_qR_c`,
respectively.  The artificial edge joins the merged bag to `B_q`, and
all other adjacencies follow from the code and the owner-bag clique minus
`R_aR_b`.  Hence all three rows lift terminally by the distinct-pole
critical-completion theorem.

For completeness, the three surviving rows really have no other
distinct-pole `K_7^-` model in the eight-vertex graph `J`.  Let `K=J-x`.
Any seven-bag model in `J` either omits one vertex or contracts one edge.
If it omits `x`, it would require at least `20` edges in `K`.  If it merges
`x` with a vertex `v`, or omits `v`, it would require at least `14` edges
in `K-v`.  If it keeps `x` singleton and contracts an edge other than the
forbidden same-pole-bag contraction `B_pB_q`, it would require at least
`14` edges after that contraction.  Direct inspection gives

\[
\begin{array}{c|c|c|c}
 \text{code} & |E(K)| & \max_v |E(K-v)|
              & \max_{uv\ne B_pB_q}|E(K/uv)|\\ \hline
 PQBPQ &16&12&13\\
 PQPPQ &15&12&13\\
 PPPQQ &15&12&13.
\end{array}                                                   \tag{2.4}
\]

These bounds exclude every such model.  Contracting `B_pB_q` merely
reconstructs the original same-pole-bag residue.  This proves both the
necessity and exactness of (2.2). \(\square\)

### Corollary 2.3 (four one-sided owner bags)

Every target-free split has four or five one-sided owner bags.  If it has
four, its code is `PQBPQ`; if it has five, its code is `PQPPQ` or
`PPPQQ`.

## 3. Opposite-side owner contacts

For a one-sided owner bag `R_i`, call `z_i` **opposite-side adjacent** if
`z_i` has a neighbour in the pole component not adjacent to `R_i`.  An
edge from `z_i` to the opposite pole itself counts, since that pole belongs
to the opposite component.

### Theorem 3.1 (two absent opposite-side owner contacts)

Assume every pair of centres is feasible on `D`.  If all but at most one
one-sided owner bag have opposite-side-adjacent owners, then `G` contains
a `K_7^-` minor.  Consequently a target-free residue has at least two
one-sided bags whose owners have no neighbour in the opposite pole
component.

#### Proof

Use pair feasibility for `\{z_a,z_b\}`.  Choose a `p`--`q` path `L` on
the `D`-side and a component of its deletion containing `z_a,z_b`; inside
that component choose a `z_a`--`z_b` path `T`.  Split `L` across an edge
into connected subpaths `L_p,L_q` containing `p,q`, and split `T` across
an edge into connected subpaths `T_a,T_b` containing `z_a,z_b`.

Use the seven branch sets

\[
\begin{aligned}
 B_p'&=B_p\cup V(L_p),&
 B_q'&=B_q\cup V(L_q),\\
 R_a'&=R_a\cup V(T_a),&
 R_b'&=R_b\cup V(T_b),\\
 R_k'&=R_k\cup\{z_k\}&&
       (k\notin\{a,b\}).
\end{aligned}                                                 \tag{3.1}
\]

They are pairwise disjoint.  The witness path and its complementary
component are disjoint, and the pair-feasibility instance contains no
centre outside `\{z_a,z_b\}`.  Ownership edges make all five enlarged
owner bags connected.  The split edge of `L` repairs `B_pB_q`, and the
split edge of `T` repairs `R_aR_b`.

Every two-sided owner bag retains both pole-component adjacencies.  A
one-sided bag retains its original adjacency, and its owner supplies the
opposite adjacency exactly when that owner is opposite-side adjacent.
All other owner-bag pairs retain their old edges.  Thus the seven bags in
(3.1) have at most the one missing adjacency belonging to the possible
exceptional one-sided bag.  They form a `K_7^-` model in `G`.

Corollary 2.3 gives at least four one-sided bags.  Target exclusion
therefore forces at least two of their owners to lack an opposite-side
neighbour. \(\square\)

The pair-feasibility hypothesis is the separately audited conclusion
available on `D` in the no-singleton-contact row.  Theorem 3.1 is invoked
only in that row.

### Lemma 3.2 (every four boundary vertices root a `K_4` on `D`)

Assume the opposite component satisfies

\[
                            \chi(G[D])\ge5.
\tag{3.2}
\]

For every four-set `Q subseteq S`, the graph `G[D union Q]` contains a
`Q`-rooted `K_4` minor model.

#### Proof

This is the separately audited
[universal four-boundary rooted-`K_4` theorem](../results/hc7_k7minus_five_centre_universal_boundary_rooted_k4.md),
applied with the same distinct-response component `D` and boundary `S`.
Its hypotheses are inherited from the five-centre two-cut reduction; in
particular, that reduction supplies (3.2). `\square`

For a one-sided bag `R_i`, call `i` **opposite-side deficient** when
`z_i` has no neighbour in the pole component not adjacent to `R_i`.
Equivalently, these are exactly the exceptional indices not repaired by
adjoining the owner singleton `\{z_i\}` to `R_i`.

### Theorem 3.3 (three opposite-side-deficient owners)

Assume (3.2).  If `G` has no `K_7^-` minor, then at least three one-sided
bags are opposite-side deficient.  If exactly three are deficient, their
index set does not contain both `a` and `b`.

#### Proof

Let `T` be the set of opposite-side-deficient indices.  First suppose
`|T|<=2`.  Choose distinct indices `i,j` such that `T subseteq {i,j}`.
By Lemma 3.2, the graph

\[
                   G[D\cup\{p,q,z_i,z_j\}]
\]

has four pairwise adjacent disjoint connected bags `H_p,H_q,H_i,H_j`,
rooted at `p,q,z_i,z_j`, respectively.  Enlarge the seven split bags by

\[
\begin{aligned}
 B_p'&=B_p\cup H_p,&
 B_q'&=B_q\cup H_q,\\
 R_i'&=R_i\cup H_i,&
 R_j'&=R_j\cup H_j,\\
 R_k'&=R_k\cup\{z_k\}&&
       (k\notin\{i,j\}).
\end{aligned}                                                \tag{3.3}
\]

These seven sets are pairwise disjoint and connected.  The rooted clique
repairs `B_pB_q` and every pole-component deficit at `R_i,R_j`.
For `k notin {i,j}`, the ownership edge connects `z_k` to `R_k`; if
`R_k` is one-sided, the definition of `T` says that `z_k` also repairs
its opposite pole-component adjacency.  All old owner-bag adjacencies
remain.  Thus the only possible missing edge among the sets in (3.3) is
`R_aR_b`, unless both `a,b` belong to `{i,j}`, in which case the rooted
clique repairs that edge as well.  In either case (3.3) is a `K_7^-`
model, a contradiction.  Hence `|T|>=3`.

Now suppose `|T|=3` and `{a,b} subseteq T`.  Apply the same construction
with `i=a` and `j=b`.  The rooted clique repairs `B_pB_q`, both selected
pole-component deficits, and `R_aR_b`.  Adjoining each remaining owner
repairs every nondeficient one-sided bag.  The third member of `T`
therefore contributes the sole possible missing edge.  Again the seven
sets form a `K_7^-` model, a contradiction.  Thus an exact three-set `T`
cannot contain both `a,b`. `\square`

Theorem 3.3 strictly strengthens the numerical conclusion of Theorem 3.1
whenever (3.2) is available.  Its model uses the rooted `K_4` to repair
two prescribed owner deficits simultaneously; it does not require a
rooted model disjoint from a prescribed `p`--`q` path.

### Theorem 3.4 (contracted-shore pole--owner merge)

Let `T` again denote the set of opposite-side-deficient indices.  Choose
an index `j`, and choose a pole side `s in {p,q}` to which `R_j` is
adjacent.  If `R_j` is one-sided, take `s` to be its unique side; if it
is two-sided, either side may be used.  Write `t` for the other pole.

Then `G` has seven pairwise disjoint connected sets

\[
 D,\qquad B_s\cup R_j\cup\{z_j\},\qquad B_t,
 \qquad R_i\cup\{z_i\}\quad(i\ne j).                 \tag{3.4}
\]

Every set in (3.4) is adjacent to all the others except precisely for the
following possible pairs:

1. the merged set and `B_t` if `j in T`;
2. `B_t` and `R_i union {z_i}` for every deficient owner `i ne j` on side
   `s`;
3. `R_a union {z_a}` and `R_b union {z_b}` if
   `j notin {a,b}`; and
4. if `j in {a,b}`, writing `h` for the other member of `{a,b}`, the
   merged set and `R_h union {z_h}` when `h in T` lies on side `t`.

Consequently (3.4) is a `K_7^-` model whenever this list contains at most
one pair.

#### Proof

Put

\[
 X=D,
 \qquad M=B_s\cup R_j\cup\{z_j\},
 \qquad R_i'=R_i\cup\{z_i\}\quad(i\ne j).
\]

The seven sets `X,M,B_t,(R_i':i ne j)` are disjoint.  They are connected:
`B_s` and `R_j` are adjacent, the ownership edge joins `z_j` to `R_j`,
and every other ownership edge joins `z_i` to `R_i`.

The set `X` is adjacent to every other set.  It meets `B_t` and `M`
through the fullness edges at the two poles, and it meets every enlarged
owner bag through an edge from `z_i` to `D`.

The merged set `M` is adjacent to `B_t` through an old
`R_j`--`B_t` edge when `R_j` is two-sided, and through `z_j` when `R_j`
is one-sided and nondeficient.  The only failure is item 1.  For
`i ne j`, the bag `R_i'` is adjacent to `B_t` unless it is a deficient
owner on side `s`.  This gives exactly the pairs in item 2.

All enlarged owner bags retain the old owner-bag adjacencies.  If
`j notin {a,b}`, the sole possible missing pair among them remains
`R_a'R_b'`, giving item 3, while `R_j` makes `M` adjacent to every
`R_i'`.  Suppose instead that `j in {a,b}` and let `h` be its former
nonneighbour.  For every `i ne h,j`, the edge `R_jR_i` joins `M` to
`R_i'`.  The set `M` is also adjacent to `R_h'` if `h` lies on side `s`,
through `B_sR_h`, or if `h` is nondeficient on side `t`, through an edge
from `z_h` to `B_s`.  The only remaining case is exactly item 4.

No pair listed above is duplicated, and all other contacts have been
verified.  At most one listed pair therefore makes (3.4) a `K_7^-`
minor model. `\square`

The following table is the exact finite evaluation of Theorem 3.4 on the
three codes in (2.2), subject to Theorem 3.3.  An entry `U:r` means that
`T=U` and the best permitted choice of `(j,s)` leaves exactly `r`
missing pairs in (3.4).  The symbol `n/a` means that the column cannot
occur.

This evaluation is a direct count, not a computational assumption.  Write
`sigma(i)` for the set of pole sides met by `R_i`, and, when
`j in {a,b}`, write `h` for the other endpoint of the owner nonedge.  The
four pair types in Theorem 3.4 are disjoint, so for every permitted
`s in sigma(j)` their exact number is

\[
\begin{aligned}
 m(j,s;T)={}&\mathbf 1_{j\in T}
   +|\{i\in T-\{j\}:\sigma(i)=\{s\}\}|\\
 &+\mathbf 1_{j\notin\{a,b\}}
   +\mathbf 1_{j\in\{a,b\},\ h\in T,\ \sigma(h)=\{t\}}.
\end{aligned}                                                \tag{3.5}
\]

Here `j` is allowed to be deficient; its contribution is then the first
term.  Substitution of the three five-letter codes into (3.5), followed by
minimization over the five choices of `j` (and both choices of `s` for a
two-sided owner), gives the displayed entries.

| code | three deficient | four deficient | five deficient |
|---|---|---|---|
| `PQBPQ` | `ade:2`, `bde:2` | `abde:3` | `n/a` |
| `PQPPQ` | `acd:1`, `ace:2`, `ade:2`, `bcd:1`, `bce:2`, `bde:2`, `cde:1` | `abcd:2`, `abce:3`, `abde:3`, `acde:2`, `bcde:2` | `abcde:3` |
| `PPPQQ` | `acd:2`, `ace:2`, `ade:1`, `bcd:2`, `bce:2`, `bde:1`, `cde:1` | `abcd:2`, `abce:2`, `abde:2`, `acde:2`, `bcde:2` | `abcde:3` |

For example, in code `PQPPQ` with `T={a,c,d}`, choose `j=b` and
`s=q`.  The merged bag is `B_q union R_b union {z_b}`.  It repairs the
deficits at `R_c,R_d`; only its adjacency to `R_a union {z_a}` can be
absent.  Thus (3.4) is terminal.

For the other five entries equal to one, witnesses `(j,s)` are

\[
\begin{array}{c|c|c}
 \text{code}&T&(j,s)\\ \hline
 PQPPQ&\{b,c,d\}&(b,q)\\
 PQPPQ&\{c,d,e\}&(b,q)\\
 PPPQQ&\{a,d,e\}&(b,p)\\
 PPPQQ&\{b,d,e\}&(a,p)\\
 PPPQQ&\{c,d,e\}&(a,p).
\end{array}
\]

Together with (3.4), these choices are explicit seven-bag minor models;
the single absent pair is respectively `MB_p`, `B_pR_e'`, `B_qR_a'`,
`B_qR_b'`, and `B_qR_c'`.

The entries equal to one give the following unconditional exclusions:

\[
\begin{array}{c|c}
 PQPPQ & T\notin\{\{a,c,d\},\{b,c,d\},\{c,d,e\}\},\\
 PPPQQ & T\notin\{\{a,d,e\},\{b,d,e\},\{c,d,e\}\}.
\end{array}                                                   \tag{3.6}
\]

Entries at least two record only the exact limit of this particular
pole--owner merge.  They are not asserted to be realizable host
configurations.

### Corollary 3.5 (all but four patterns give a minor or nested separator)

For every admissible pair consisting of a code in (2.2) and a deficiency
set `T`, except

\[
 \begin{array}{c|c}
  PQBPQ&\{a,b,d,e\},\\
  PQPPQ&\{a,b,c,e\},\ \{a,b,d,e\},\ \{a,b,c,d,e\},
 \end{array}                                                   \tag{3.7}
\]

at least one of the following holds:

1. `G` contains a `K_7^-` minor; or
2. some bag `U` in a spanning seven-bag model of the form (3.4) contains
   a nonempty proper connected set `Y` such that `U-Y` is connected and
   `N_G(Y)` is an actual vertex separator.

In outcome 2, `|N_G(Y)|>=7`; if equality holds, every component of
`G-N_G(Y)` is adjacent to every vertex of `N_G(Y)`.

#### Proof

The six entries excluded in (3.6) give outcome 1 directly.  For every
other nonexceptional entry, choose `(j,s)` from the following table.  The
number `r` is the number of absent pairs in (3.4), and the last column is
their common endpoint.

| code | `T` | `(j,s)` | `r` | common endpoint |
|---|---|---|---|---|
| `PQBPQ` | `ade` | `(a,p)` | 2 | `B_q` |
|  | `bde` | `(b,q)` | 2 | `B_p` |
| `PQPPQ` | `ace`, `ade` | `(a,p)` | 2 | `B_q` |
|  | `bce`, `bde` | `(b,q)` | 2 | `B_p` |
|  | `abcd` | `(b,q)` | 2 | `M` |
|  | `acde` | `(a,p)` | 3 | `B_q` |
|  | `bcde` | `(b,q)` | 2 | `B_p` |
| `PPPQQ` | `acd`, `ace`, `bcd`, `bce` | `(a,p)` | 2 | `B_q` |
|  | `abcd`, `abce` | `(a,p)` | 3 | `B_q` |
|  | `abde`, `acde`, `bcde` | `(a,p)` | 2 | `B_q` |
|  | `abcde` | `(a,p)` | 3 | `B_q` |

Formula (3.5) verifies every row directly.  Thus the absent-pair graph is
an edge-star with at least two leaves.  The seven sets in (3.4) partition
`V(G)`: the sets `B_p,B_q,R_a,...,R_e` partition `C union {p,q}`, all
five centres are adjoined to their owner bags, and `D` is the remaining
bag.  Taking the common endpoint of the star as `X`, the other six bags
are pairwise adjacent.  The separately audited
[multiple-missing-adjacencies separator dichotomy](../results/hc7_k7minus_multiple_missing_adjacencies_separator_dichotomy.md)
therefore gives outcome 1 or outcome 2, including the assertions about
the separator order and fullness. `\square`

The four sets in (3.7) are exact exceptions to this argument: substitution
in (3.5) shows that no choice of `(j,s)` leaves at most one absent pair or
makes all absent pairs share an endpoint.  This says only that the present
single pole--owner merge does not reach the separator dichotomy there.
It does not assert that those configurations exist.

### Proposition 3.6 (a near-clique spanning model gives a minor or separator)

Let `G` be seven-connected, and let

\[
                            X,U_1,\ldots,U_6                 \tag{3.8}
\]

be pairwise disjoint nonempty connected sets which partition `V(G)`.
Suppose that at most one pair among `U_1,...,U_6` is nonadjacent.  If `X`
is nonadjacent to at least one `U_i`, then either

1. `G` contains a `K_7^-` minor; or
2. for some `j` there is a nonempty proper connected set `Y subset U_j`
   such that `U_j-Y` is connected and `N_G(Y)` is an actual vertex
   separator.

Every separator in outcome 2 has order at least seven.  If it has order
seven, every component of its deletion is adjacent to every separator
vertex.

#### Proof

Let `M` be the nonempty set of indices of bags missed by `X`.  For any
`m in M`, the bag `U_m` lies beyond `N_G(X)`, so seven-connectivity gives

\[
                              |N_G(X)|\ge7.                    \tag{3.9}
\]

Those neighbours lie in at most five contacted bags.  Hence one contacted
bag, relabelled `U_1`, contains distinct vertices `p,q` adjacent to `X`.
For every `i in {2,...,6}` for which `U_1,U_i` are adjacent, put

\[
                         P_i=N_G(U_i)\cap U_1.                 \tag{3.10}
\]

Each such `P_i` is nonempty.  Call a connected subset of `U_1` containing
`p` and meeting every set in (3.10) a `p`-retaining core.

Suppose first that a `p`-retaining core `T` avoids `q`.  Let `Y` be the
component of `G[U_1-T]` containing `q`, and put `W=U_1-Y`.  Every other
component of `G[U_1-T]` has an edge to `T`, so `W` is connected and
retains every adjacency of `U_1` except its possible one original
nonadjacency among the six `U`-bags.

If `Y` is adjacent to every `U_m` with `m in M`, then

\[
                         X\cup Y,\quad W,\quad U_2,\ldots,U_6  \tag{3.11}
\]

are seven connected branch sets with at most one nonadjacent pair.  The
edge from `X` to `q` connects the first set, the cut between `Y` and `W`
joins the first two, `Y` repairs every adjacency missed by `X`, and `W`
retains all old contacts from `U_1`.  Thus (3.11) is a `K_7^-` model.
If instead `Y` is anticomplete to some `U_m`, then `U_m` is a nonempty
far side of `N_G(Y)`.  The set `Y` and its complement `W` in `U_1` are
connected, giving outcome 2.  The same argument applies with `p,q`
interchanged.

It remains to suppose that every `p`-retaining core contains `q` and every
`q`-retaining core contains `p`.  Let `C_q` be the component of
`G[U_1-q]` containing `p`, and set `Z_q=U_1-C_q`; define `C_p,Z_p`
symmetrically.  Each `Z_s` is nonempty and connected, its complement in
`U_1` is connected, and

\[
                              Z_p\cap Z_q=\varnothing.          \tag{3.12}
\]

Indeed, a vertex in the intersection would force every `p`--vertex path
through `q` and every `q`--vertex path through `p`; the suffix of a simple
path gives a contradiction.

Let `I` be the set of indices occurring in (3.10), and define

\[
                  \Omega(Z)=\{i\in I:P_i\subseteq Z\}.         \tag{3.13}
\]

Both `Omega(Z_p)` and `Omega(Z_q)` are nonempty.  Otherwise the connected
complement of the relevant set would meet every `P_i` and would be a
retaining core avoiding the opposite marked vertex.  Choose
`i in Omega(Z_p)`.  Equations (3.12)--(3.13) show that `Z_q` is
anticomplete to `U_i`, so `U_i` is a far side of `N_G(Z_q)`.  Taking
`Y=Z_q` gives outcome 2.

Seven-connectivity bounds every returned separator below by seven.  If a
separator of order seven had a vertex missing one component of its
deletion, the other six separator vertices would separate that component,
contrary to seven-connectivity. `\square`

Proposition 3.6 differs from the multiple-missing-adjacencies theorem used
in Corollary 3.5 only in permitting one nonedge among the six bags outside
`X`.  That one edge is exactly the sole nonedge allowed in (3.11).

### Theorem 3.7 (universal nested-separator reduction)

In the unique-owner residue, at least one of the following holds:

1. `G` contains a `K_7^-` minor; or
2. a bag in a spanning seven-bag model contains a nonempty proper connected
   set `Y` whose complement in that bag is connected and whose open
   neighbourhood is an actual separator of order at least seven.

If the separator in outcome 2 has order seven, every component of its
deletion is full at that separator.

#### Proof

Apply Lemma 3.2 to the four roots `p,q,z_a,z_b`.  Enlarge its four rooted
bags, without losing connectedness or pairwise adjacency, so that they
partition `D union {p,q,z_a,z_b}`.  Explicitly, contract the four rooted
bags, take a spanning forest rooted at their four images in the resulting
connected graph, and assign each remaining vertex to the rooted tree which
contains it.  Name the enlarged bags `H_p,H_q,H_a,H_b` by their roots.
The following seven sets are connected and partition `V(G)`:

\[
\begin{aligned}
 U_p&=B_p\cup H_p,& U_q&=B_q\cup H_q,\\
 U_a&=R_a\cup H_a,& U_b&=R_b\cup H_b,\\
 U_i&=R_i\cup\{z_i\} &&(i\in\{c,d,e\}).
\end{aligned}                                                 \tag{3.14}
\]

The rooted clique repairs `U_pU_q`, every pole adjacency at `U_a,U_b`,
and `U_aU_b`.  All owner-bag adjacencies other than the latter were already
present.  Consequently every possible nonedge in (3.14) is an
opposite-pole deficit at one of `U_c,U_d,U_e`.

In code `PQBPQ`, these candidate nonedges are `U_qU_d` and `U_pU_e`.
In code `PQPPQ`, they are `U_qU_c,U_qU_d,U_pU_e`; in code `PPPQQ`, they
are `U_qU_c,U_pU_d,U_pU_e`.  Thus they form the union of two pole-centred
edge-stars, one of which has at most one leaf.

If at most one candidate pair is actually absent, (3.14) is a `K_7^-`
model.  Otherwise choose as `X` a pole bag incident with at least one
absent pair and with the other pole incident with at most one absent pair.
The remaining six bags then have at most one nonadjacent pair, so
Proposition 3.6 applies and gives outcome 1 or outcome 2, including the
separator assertions. `\square`

Unlike Corollary 3.5, Theorem 3.7 has no exceptional deficiency pattern.
It uses the rooted `K_4` to repair the artificial pole edge and the
owner-bag nonedge simultaneously, and then spends the permitted nonedge in
`K_7^-` on the smaller of the two remaining pole-centred stars.

## 4. The terminal rooted connector

Call four connected subgraphs `L,Q_a,Q_b,W` of
`G[D union Z union {p,q}]` an **owner-nonedge connector** when all of the
following hold.

1. They are pairwise vertex-disjoint.
2. Their intersections with the seven boundary vertices are

   \[
   V(L)\cap S=\{p,q\},\qquad
   V(Q_a)\cap S=\{z_a\},\qquad
   V(Q_b)\cap S=\{z_b\},\qquad
   V(W)\cap S=\varnothing.
   \tag{4.1}
   \]

3. The subgraphs `Q_a,Q_b` are adjacent.
4. Among the six sets

   \[
             L,Q_a,Q_b,\{z_k\}\quad
             (k\in\{1,\ldots,5\}-\{a,b\}),
   \tag{4.2}
   \]

   the set `W` is adjacent to at least five.

The definition allows exactly one missing adjacency at `W`.  A stronger
but convenient sufficient form consists of a `p`--`q` path `L`, a
vertex-disjoint `z_a`--`z_b` path split across one edge into `Q_a,Q_b`,
and a connected residual set `W` adjacent to all six sets in (4.2).

### Theorem 4.1 (owner-nonedge connector completion)

If the unique-owner residue (1.1)--(1.2) has an owner-nonedge connector,
then `G` contains a `K_7^-` minor.

#### Proof

For `k` outside `{a,b}`, put

\[
                         R_k'=R_k\cup\{z_k\},
\]

and put

\[
 B'=B\cup V(L),\qquad
 R_a'=R_a\cup V(Q_a),\qquad
 R_b'=R_b\cup V(Q_b).
\tag{4.3}
\]

These six sets and `W` are pairwise disjoint.  They are connected:
`L` replaces the artificial edge `pq` inside `B`, while the ownership
edges from `z_i` to `R_i` connect each enlarged owner bag.  Every pair
among the five enlarged owner bags is adjacent.  The only old missing
pair `R_aR_b` is supplied by the `Q_a`--`Q_b` edge.  The bag `B'` is
adjacent to all five owner bags because `B` was adjacent to every `R_i`.

Finally, `W` is adjacent to at least five of the other six bags by
(4.2).  Hence the contact graph of

\[
                         B',R_1',\ldots,R_5',W
\]

is `K_7` with at most one edge deleted.  These seven bags form a
`K_7^-` minor model in `G`.  \(\square\)

The proof spends the two scarce resources separately: `L` restores the
internal connectivity of the pole-pair bag, and `Q_a,Q_b` restore the
missing adjacency between its two owner bags.  The seventh bag `W`
replaces the contracted universal vertex.

## 5. What the synchronized rainbow path actually gives

Assume now the all-rainbow outcome.  Fix the common proper colouring of
the closed `D`-shore, with pole colours `beta,delta` and three remaining
contact colours `Gamma`.  Let `R` be the synchronized `beta`--`delta`
`p`--`q` path, and put

\[
                         T_i=N_D(z_i).
\]

Each `T_i` is a triangle whose vertices have the three colours in
`Gamma`.

### Lemma 5.1 (component partition along the synchronized path)

Every triangle `T_i` is disjoint from `R` and lies in one component
`A_i` of `G[D-V(R)^\circ]`.  If `A` is a component meeting at least one
contact triangle and

\[
                         Z_A=N_G(A)\cap Z,
\]

then

\[
 |Z_A|\le4,
 \qquad
 |N_G(A)\cap V(R)|\ge7-|Z_A|\ge3.                 \tag{5.1}
\]

Moreover, the nonempty sets `Z_A`, over the components which meet contact
triangles, partition `Z`; equivalently,

\[
                         z_i\in Z_A
             \quad\Longleftrightarrow\quad T_i\subseteq A.
\tag{5.2}
\]

#### Proof

The path `R` uses only `beta,delta`, whereas every vertex of `T_i` has a
colour in `Gamma`.  Thus `T_i` is disjoint from `R`.  Its three literal
triangle edges put it in one component of `D-V(R)^\circ`.

Apply the path-deletion attachment inequality from the active
[synchronized-path theorem](hc7_k7minus_five_centre_distance_one_paths.md)
to `R` on the rooted-infeasible `D`-shore.  It gives exactly (5.1).
Since `N_D(z_i)=T_i`, a centre is adjacent to `A` precisely when its
whole contact triangle lies in `A`.  Every centre has one such triangle,
so (5.2) follows and the displayed nonempty sets partition `Z`.
\(\square\)

### Corollary 5.2 (the first linkage obstruction)

If `A_a` and `A_b` are distinct, every `z_a`--`z_b` path whose open
interior lies in `D` meets `V(R)^\circ`.  Consequently the synchronized
path `R` cannot be used as the `L`-bag of the convenient two-path form of
Theorem 4.1.

#### Proof

After deleting `V(R)^\circ`, the only `D`-neighbours of `z_a,z_b` lie in
the distinct components `A_a,A_b`, respectively.  A path between them
with open interior in `D` must therefore use a deleted vertex.  \(\square\)

If `A_a=A_b`, a `z_a`--`z_b` path with open interior in that component
does exist.  This still does not produce Theorem 4.1: one must choose it
so that a disjoint connected residual set remains adjacent to at least
five of the six prescribed sets in (4.2).

## 6. Exact route nonclosure

The contracted-shore analysis first restricts the deficiency set to

\[
 |T|\ge3,
 \qquad
 |T|=3\Longrightarrow \{a,b\}\nsubseteq T,             \tag{6.1}
\]

and excludes the six triples in (3.6).  Corollary 3.5 gives a nested
separator outside four exact quotient patterns.  Theorem 3.7 then removes
that four-pattern exception: in a target-free unique-owner residue, every
remaining configuration has a nonempty proper connected set `Y` inside
one bag of (3.14), with connected complement in that bag, such that
`N_G(Y)` is an actual separator of order at least seven.

This nested separator is not terminal with the current data.  Its order
can exceed seven, its boundary need not be the neighbourhood of a named
degree-eight centre, and neither shore is known to retain the required
boundary-colouring response.  In particular, it is not yet the
trace-preserving strict descent required by the minimum-side argument.

The failure is visible inside the proof of Proposition 3.6.  An avoidable
donor piece which meets every bag missed by `X` is absorbed into `X` and
immediately gives the forbidden minor.  A separator is returned only when
such a piece misses a required foreign bag, or when the two opposite
retaining cores are unavoidable and one monopolizes all donor contacts to
a foreign bag.  The proof supplies no legal iteration across that missed
contact: after one donor piece is selected, no second disjoint piece is
known whose simultaneous deletion leaves a connected donor complement
retaining all of its other branch-set adjacencies.  Assuming such a second
piece would be a new linkage statement, not a consequence of the retaining-
core argument.

Nor does unique ownership force the returned boundary to be
`Z union {r,s}`.  The donor bag is not controlled.  For example, if the
returned set lies in one of the ordinary bags
`U_i=R_i union {z_i}` from (3.14), then (1.2) and the independence of `Z`
give

\[
                         N_G(Y)\cap Z\subseteq\{z_i\}.          \tag{6.2}
\]

Thus that separator misses at least four centres and cannot be the desired
seven-vertex boundary.  The present argument neither excludes an ordinary
owner bag as donor nor relocates its separator to the original five
centres.  The smallest repair is therefore a rooted donor theorem: either
the near-clique absorption is terminal, or it returns an exact separator
`Z union {r,s}` with the equal/distinct boundary partition retained.

The four-rooted `K_4` in Lemma 3.2 can repair `B_pB_q` and the deficits
of two selected owners.  It does not also provide a disjoint residual bag
adjacent to the six repaired bags, nor can it be assumed disjoint from a
prescribed pole path.  Thus (6.1) is a genuine remaining simultaneous
allocation obstruction rather than a failure to find rooted clique bags.

Four-root feasibility supplies a `p`--`q` path and one complementary
component containing four centres.  It does not split those four centres
into their four owner bags while preserving a fifth, disjoint connected
bag adjacent to them.  Conversely, using a path through two different
components of `D-V(R)^\circ` to repair `R_aR_b` consumes the synchronized
pole path and destroys the connectivity supplied to `B`.

Thus the first unsupported inference is not the existence of another
ordinary path.  It is the following simultaneous allocation statement.

> **Owner-nonedge connector-or-descent target (not proved).**  In the
> all-rainbow unique-owner residue, either there is an owner-nonedge
> connector, or there is a proper equality-response component
> `C' subsetneq C` with an actual two-vertex boundary in `G-Z` and the
> retained equal boundary-colouring trace.

The first conclusion is terminal by Theorem 4.1.  The second would be the
strict minimum-side descent already proved terminal in the synchronized-
path theorem.  Current attachment inequalities give at least three
neighbours on a pole path, not an exact two-vertex boundary, so they do
not establish the second conclusion.

## Dependencies and claim status

- the spanning unique-owner normal form and elimination of a `BR_i`
  nonedge are the separately audited conclusions of the
  critical-completion lift;
- pair feasibility on `D`, when Theorem 3.1 is invoked, is the separately
  audited conclusion of the
  [three-root palette reduction](hc7_k7minus_five_centre_t3_palette_gluing.md);
- `chi(G[D])>=5` is a separately audited conclusion of the
  [five-centre two-cut reduction](../results/hc7_k7minus_five_centre_two_cut_reduction.md),
  and Lemma 3.2 is the separately audited
  [universal four-boundary rooted-`K_4` theorem](../results/hc7_k7minus_five_centre_universal_boundary_rooted_k4.md);
- Corollary 3.5 invokes the separately audited
  [multiple-missing-adjacencies separator dichotomy](../results/hc7_k7minus_multiple_missing_adjacencies_separator_dichotomy.md);
- the all-rainbow contact triangles and common pole path are separately
  audited inputs of the global-palette and synchronized-path results; and
- Lemmas 2.1, 3.2, and 5.1, Proposition 3.6, Theorems 2.2, 3.1, 3.3,
  3.4, 3.7, and 4.1, and Corollaries 2.3, 3.5, and 5.2 are proved here.

Theorem 3.7 gives an unconditional minor-or-separator dichotomy in the
unique-owner residue.  It does not identify the separator as
`Z union {r,s}`, retain either boundary-colouring response, or close the
five-centre two-cut branch.  No such terminal descent is claimed here.
