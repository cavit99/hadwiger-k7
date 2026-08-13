# The exact protected-centre kernel residue

## Status and scope

**Frozen route note; new written lemmas and finite normal-form diagnostics
are not independently audited.**  The host reductions cited below are
written and audited, but Lemmas 4.1 and 7.1 have only the proofs given here.  The
order-eight and order-nine exact terminal catalogues have not yet received
an independent implementation audit.  Consequently the finite propositions
below are conditional computer-assisted statements, not promoted results.

This note does not prove the `K_7^-` six-colour conjecture or `HC_7`.  It
identifies the exact finite objects left by the protected-centre reduction.
The proposed fan-to-root continuation is now frozen at a separately recorded
path/model quantifier mismatch; the note must not be read as an active claim
that one further host lemma is likely to eliminate the residue.

## 1. Host setting

Let `G` be a seven-connected graph with no `K_7^-` minor.  Let `u` be a
degree-eight vertex and let `v` be adjacent to all seven vertices of

\[
                         Q=N_G(u)-\{v\}.
\]

Assume the proved dominated-centre reductions.  Thus

\[
 H=G-\{u,v\}\text{ is five-connected},
\]

`u` belongs to an independent set of five degree-eight centres, and

\[
 Q\cong C_5\mathbin{\dot\cup}K_2,
 \quad C_5\text{ with a pendant path of length two},
 \quad\text{or}\quad C_7.                            \tag{1.1}
\]

Choose another centre `w`.  Protect `T=Q\cup\{w\}` and reduce `H` by
terminal-legal contractions to a `T`-irreducible kernel.  The audited
terminal-kernel theorem bounds its order by ten, and the protected-centre
order-ten theorem excludes order ten.  The current residue therefore has
order eight or nine.

## 2. Exact one-centre normal form

For a graph `L` with two vertices of degree three and all other vertices of
degree two, write `theta(a,b,c)` when its three internally disjoint paths
between the degree-three vertices have lengths `a,b,c`.

### Proposition 2.1 (conditional finite classification)

Assume the current exact order-eight and order-nine catalogue is complete.
After adding the literal edges of `Q` and allowing every legal absorption of
a nonterminal or of the protected-centre bag, the following statements hold.

1. There are 425 failed labelled order-eight compositions in 66 fixed-`Q`
   automorphism orbits.
2. Granting one arbitrary new contact from the `w`-rooted bag to a
   `Q`-rooted bag leaves 51 labelled cases in nine fixed-`Q` orbits.  Their
   unlabelled terminal quotients are exactly:

   \[
   w\vee C_7,
   \qquad
   w\text{ joined to all degree-two vertices of }
   \theta(1,2,5),\theta(1,3,4),\theta(2,3,3).        \tag{2.1}
   \]

3. There are 803 failed exact order-nine owner families in 88 fixed-`Q`
   orbits.  In every corresponding nine-vertex kernel `K`, with unique
   nonterminal `x`,

   \[
   d_K(w)=3,\qquad wx\in E(K),\qquad
   |N_K(w)\cap Q|=2,qquad d_K(x)\in\{6,7,8\}.       \tag{2.2}
   \]

   The only degree sequences are

   \[
   3^8 6,qquad 3^7 4 7,qquad 3^8 8,qquad 3^6 4^2 8. \tag{2.3}
   \]

4. Every failed order-nine family is eliminated by one suitably placed new
   `w`--`Q` rooted-bag contact.  The set of forcing `Q` bags has order five
   for the two `C_5`-based graphs, and order three, four or five for `C_7`.

The exact counts, fixed-`Q` orbit representatives, universal missing-edge
profiles, source hashes and result digests are recorded in the adjacent
[classifier report](experiments/dominated_singleton_exact_eight_kernel_absorption/README.md).

The conclusion is deliberately conditional: the classifier exhausts the
current catalogue, but does not independently establish that catalogue.

## 3. What a second centre would finish

Call the four graphs in (2.1) the **resistant quotients**.  The following two
finite implications have exact rooted-minor lifts.

### Proposition 3.1 (common `Q` bags are terminal)

Let `B_0,...,B_6,W,W'` be pairwise disjoint connected sets in `H`, with
`q_i\in B_i`.  Suppose the quotient on

\[
                         B_0,...,B_6,W
\]

contains a resistant quotient rooted at `Q,w`, and the quotient on

\[
                         B_0,...,B_6,W'
\]

contains a resistant quotient rooted at `Q,w'`.  Then `H` contains a
`Q`-rooted `K_5^-` model and `G` contains a `K_7^-` model.

#### Conditional computer-assisted proof

The verifier checks all ordered pairs of labelled resistant quotients on the
same seven fixed `Q` bags.  The numbers of pairs are 900, 36 and 225 for the
three graphs in (1.1), and none fails.  A `K_5^-` model in the quotient lifts
to five branch sets in `H`, each meeting `Q`.  The adjacent vertices `u,v`,
both complete to `Q`, supply the other two branch sets. `\square`

### Proposition 3.2 (four contacts from a second centre-bearing set)

Let `B_0,...,B_6,W` be a resistant rooted model in `H`.  Let `A` be a
connected set disjoint from those eight bags.  If `A` is adjacent to four of
the seven `Q`-rooted bags, then `G` contains a `K_7^-` minor.

For the two `C_5`-based choices of `Q`, and for the `C_7`--`theta(1,3,4)`
case, three contacts already suffice.

#### Conditional computer-assisted proof

Contract `A` to one vertex and test the resulting nine-vertex rooted
quotient.  The verifier enumerates every subset of the seven `Q` bags.
Every four-subset closes.  The failed three-subsets occur only for the
`C_7`--`theta(1,2,5)` and `C_7`-wheel quotients.  The same rooted lift as in
Proposition 3.1 applies. `\square`

## 4. Two prescribed representatives

For a centre `z`, let

\[
 \mathcal I_z=\{I\subseteq N_G(z):|I|=3\text{ and }I\text{ is independent}\},
 \qquad K_z=\bigcap_{I\in\mathcal I_z}I.             \tag{4.1}
\]

The exceptional-neighbourhood theorem gives
\(\mathcal I_z\ne\varnothing\).

### Lemma 4.1 (two prescribed matching representatives)

Let `w_1,w_2` be distinct members of the five-centre set.  For `i=1,2`,
choose

\[
                  y_i\in N_G(w_i)-K_{w_i},
                  \qquad y_1\ne y_2.                 \tag{4.2}
\]

The common five-centre matching may be chosen with matching edges
`w_1y_1,w_2y_2`, while retaining every nonempty equality signature on the
five matching edges.

#### Proof

For `i=1,2`, choose `I_{w_i}` avoiding `y_i`, and put
`R_{w_i}=N_G(w_i)-I_{w_i}`.  For each of the other three centres `z`, choose
any `I_z in \mathcal I_z` and put `R_z=N_G(z)-I_z`.  Every `R_z` has order
five.

Prescribe `y_1,y_2`.  Each of the three remaining sets

\[
                         R_z-\{y_1,y_2\}              \tag{4.3}
\]

has order at least three.  Hence every subfamily of \(k\le3\) such sets
has union of order at least three, and therefore at least `k`.  Hall's
theorem supplies three further distinct representatives, all different
from `y_1,y_2`.  The centres are independent, so the five selected edges
form a matching.  The proof of the common-matching theorem now gives the
complete punctured response cube exactly as before. `\square`

This lemma settles simultaneous matching selection once two literal
neighbours are known.  It says nothing about the branch bags containing
those neighbours.

### Proposition 4.2 (conditional two-contact relation)

Assume the all-terminal exact order-nine catalogue is complete, and fix one
of its failed compositions on common `Q`-rooted bags and two protected
centres.  For each ordered pair `(q,r) in Q times Q`, add the two rooted-bag
contacts from the first centre to `q` and from the second centre to `r`.
Then:

1. for `Q=C7`, every product of two five-subsets of `Q` contains a pair
   which forces a `Q`-rooted `K_5^-` model or the target minor; and
2. for either `C5`-based graph, the only nonforcing products of two
   five-subsets omit, in opposite coordinates, one edge of the `C5` and
   the two vertices outside that `C5`.

There are four labelled exceptional products in three fixed-`Q` orbits for
`C5` disjoint union `K2`, and eight labelled products in five fixed-`Q`
orbits for the pendant graph.

#### Conditional computer-assisted proof

For each static failed quotient, the verifier constructs its exact
`7 by 7` forcing relation by deletion-and-contraction minor search.  The
maximum common nonforcing-column profiles for row-set orders one through
seven are

\[
 (7,7,6,5,5,3,0),\quad(7,7,6,5,5,3,0),\quad
 (7,7,7,7,4,3,0),                                \tag{4.4}
\]

in the order of (1.1).  Fixed-`Q` canonicalisation gives the asserted
omitted pairs in every `5 by 5` exception. `\square`

Proposition 4.2 is a conditional allocation theorem, not a host closure.
The five vertices of `R_z` need not lie in five distinct `Q` bags.  They may
be concentrated in one bag or remain inside the centre-rooted bag.

## 5. Why neighbourhood structure does not remove the exceptions

In the two `C5`-based cases, the exceptional five-sets induce the following
graphs on the literal vertices of `Q`:

\[
 \begin{array}{c|cc}
 Q & \text{omit a cycle edge} & \text{omit the off-cycle pair}\\ \hline
 C_5\mathbin{\dot\cup}K_2 & P_3\mathbin{\dot\cup}K_2 & C_5\\
 C_5\text{ with a pendant }P_2 & P_5 & C_5.
 \end{array}                                                   \tag{5.1}
\]

If `N_G(w)-K_w` had order five and consisted of five literal vertices of
`Q`, then `K_w` would be the unique independent triple in `N_G(w)`.  The
remaining five vertices would have independence number at most two.  Thus
the first column in (5.1) cannot equal `N_G(w)-K_w` under this literal-root
hypothesis.

The observation is exact but does not lift through arbitrary branch bags.
Moreover the second column is locally feasible.  An exhaustive eight-vertex
test finds 315 `K_4`-free, `K_6^-`-minor-free neighbourhoods of independence
number three for which the displayed `C5` is exactly `N_G(w)-K_w`.  The
other two graphs in (5.1) can occur as `N_G(w)-I` for a selected independent
triple `I`; the corresponding local extension counts are 8,904 and 10,296.
Connected witnesses of minimum degree four survive in every case.

Consequently degree-eight neighbourhood structure alone does not eliminate
the exceptional products.  A successful host proof must control where the
selectable neighbours lie in one common rooted model.

## 6. Rooted-suffix absorption does not close the residue

Suppose the matching mate of a protected centre `w` has been swallowed by
the `w`-rooted branch bag.  In an ordinary minimum rooted tree for that bag,
split off a suffix `P` which contains the mate.  Let `O` be the set of
quotient adjacencies owned by `P`, where \(|O|\ge2\), and choose an
owned `Q` bag `B_q` into which `P` is absorbed.

This has an exact quotient operation.  Delete the edges from the retained
`w` part to every label in `O`; retain all nonowned source edges; add the
edges from `q` to `O-{q}`; and restore `wq` through the matching edge between
the root part and `P`.

### Diagnostic 6.1 (rooted-suffix route nonclosure)

In the all-terminal order-nine catalogue, even an existential choice of
protected centre, ownership set and absorption bag leaves

\[
                  256,\qquad 1022,\qquad 256           \tag{6.1}
\]

failed labelled compositions for the three graphs in (1.1).  These form
66, 230 and 66 fixed-`Q` orbits.  The failure set is unchanged if `O` is
restricted to `Q` neighbours or is allowed also to contain the other
protected centre.

There is a stronger negative finding.  For every one of the original 427,
1,446 and 379 static failures, each protected centre has some legal
ownership set for which no choice of owned absorption bag closes.  Thus
bare minimum-bag ownership cannot give an ownership-independent theorem.

Every existential failure has, up to exchanging the centres, one of only
three protected-root incidence profiles:

\[
\begin{array}{c|c|c}
(d_K(w_1),d_K(w_2)) &
(|N_K(w_1)\cap Q|,|N_K(w_2)\cap Q|) & w_1w_2\\ \hline
(3,3)&(2,2)&\text{present}\\
(3,3)&(3,3)&\text{absent}\\
(4,3)&(3,2)&\text{present}.
\end{array}                                                \tag{6.2}
\]

Only four full carrier degree sequences occur:

\[
3^8 4,\qquad 3^8 6,\qquad 3^7 4 5,\qquad 3^8 8.          \tag{6.3}
\]

This is a route nonclosure, not a counterexample to a host theorem.  The
finite quotient does not encode the singleton-signature colouring of the
swallowed matching edge or the bichromatic components forced by that
colouring.

## 7. The response-labelled supply problem

Let `w'` be another exceptional centre and let `e_{w'}` be its selected
matching edge.  The complete punctured response cube supplies all nonempty
endpoint-equality signatures involving `e_{w'}` on the common deletion
host.  Its uncoloured structural shadow is only the one physical edge
`e_{w'}`.  At branch-set level that edge supplies one contact, and the finite
screen has a failure for every possible single contact in every resistant
quotient.  Thus the equality signatures alone do not imply either
Proposition 3.1 or Proposition 3.2.

Diagnostic 6.1 shows that a static rooted suffix is insufficient.  The
smallest remaining source of genuinely new structure is the fixed
singleton-signature colouring of its matching edge.  If the endpoints have
colour `alpha`, then for each other colour `beta` they lie in one
`alpha,beta` component of the edge-deletion graph; otherwise a Kempe switch
would make the restored edge proper and six-colour `G`.  This does not by
itself prove that a corresponding path leaves the protected branch bag: the
chosen branch tree may have an internal bypass in the host graph.  The
response-sensitive lemma must either use such a bypass to reduce the bag or
produce a bichromatic path which leaves it.

The complete matching deletion gives a sharper dichotomy before the branch
bags are considered.

### Lemma 7.1 (five-coordinate component alternative)

Let `M` be the five-edge common matching, put `H_M=G-M`, and let `c` be a
proper six-colouring of `H_M` whose exact equality signature is `{e}`, where
`e=wx`.  Put `alpha=c(w)=c(x)`.  For every \(\beta\ne\alpha\), let
`C_beta` be the `alpha,beta` component of `H_M` containing `w`.  Then exactly
one of the following holds.

1. `x in C_beta`; hence `C_beta` contains a `w`--`x` path which avoids all
   five matching edges.
2. Interchanging `alpha,beta` on `C_beta` produces another proper
   six-colouring of `H_M`, with a nonempty exact equality signature

   \[
                     \varnothing\ne J_\beta
                         \subseteq M-\{e\}.           \tag{7.1}
   \]

   Moreover `C_beta` contains exactly one endpoint of every matching edge
   in `J_beta`, while the other endpoint lies outside `C_beta` and both
   endpoint colours belong to `{alpha,beta}`.

#### Proof

Let `U_beta` be the set of matching edges which have exactly one endpoint
in `C_beta` and whose two endpoint colours both belong to
`{alpha,beta}`.  A Kempe interchange toggles precisely the equality status
of the edges in `U_beta`.  This is the audited matching-signature toggle
formula.

If `x in C_beta`, item 1 holds.  Otherwise `e in U_beta`, because its two
ends both have colour `alpha` and only `w` lies in `C_beta`.  The new exact
signature is therefore

\[
             \{e\}\mathbin{\triangle}U_\beta
                        =U_\beta-\{e\}=:J_\beta.      \tag{7.2}
\]

It cannot be empty: an empty signature would make every restored matching
edge proper and six-colour `G`.  The final endpoint statement is the
definition of `U_beta`. `\square`

Thus every alternate colour supplies either a matching-free bypass of the
swallowed edge or one connected subgraph which carries a nonempty set of
other matching-coordinate endpoints.  This is stronger than the bare
existence of the other response signatures: the transition and its endpoint
set come from one named Kempe component in the singleton colouring.

The smallest host statement which uses this information is the following.

> **Response-aligned protected-bag split target.**  In a resistant rooted
> model, some centre operation either:
>
> 1. yields a connected operation-labelled piece `A` whose removal leaves
>    its containing rooted bag connected and which is adjacent to four
>    `Q`-rooted bags; or
> 2. yields a second protected-centre rooted model using the same seven
>    `Q`-rooted bags; or
> 3. for a swallowed matching mate, localises one of its forced
>    bichromatic paths to a connected piece outside the protected root bag
>    which can be moved together with the suffix and produces a forcing
>    pair of named `Q`-bag contacts.

Either conclusion is terminal by Section 3.  This statement is not proved.
It is narrower than a generic branch-set split theorem: the source is one of
the three other actual degree-eight centres, its selected matching edge and
its fixed response colouring must survive, and the destination labels are
the seven literal vertices of `Q`.

There is a useful exact reformulation.  In outcome 1 of Lemma 7.1, if the
bypass lies wholly inside the protected branch bag, the selected edge is not
needed for internal connectivity.  If the edge is a bridge of the induced
branch bag, every bypass has a consecutive subpath outside the bag joining
the two sides of that bridge.  In outcome 2, `C_beta` itself is a connected
operation-labelled subgraph carrying other coordinate endpoints.  Neither
outcome says which named `Q` bags the new subpath or component meets.

Thus the exact first unsupported implication is

\[
 \begin{gathered}
  \text{a protected rooted bag containing }e=wx,\\
  \text{its singleton-signature colouring, and}\\
  \text{the five component alternatives of Lemma 7.1}
 \end{gathered}
 \Longrightarrow
 \begin{gathered}
  \text{one component-localised movable piece whose owned-label transfer}\\
  \text{is a forcing rooted-suffix operation, or a common}\\
  \text{second-centre model}
 \end{gathered}                                      \tag{7.1}
\]

The word *forcing* in (7.1) refers to the exact finite relation checked by
the verifier; it is not inferred from the existence of a Kempe component.
The component may revisit the same branch bag, several colours may use the
same external piece, and a first external piece may contact only one named
bag.  Any proof of (7.1) must exclude these three failures using the
critical host or the second protected centre.

The full response information may plausibly supply the missing contacts via
the component-localised response square on the exact boundary
`N_G(u)=Q\cup\{v\}`.  What remains unsupported is the conversion from those
colouring labels to four named branch-set contacts.  Replacing the operation
by an arbitrary extra edge cannot do this: the 51 order-eight cases in
Proposition 2.1 survive every such one-contact refinement.

## 8. Reproduction and trust boundary

Run:

```text
python3 active/experiments/dominated_singleton_exact_eight_kernel_absorption/classify.py --all
python3 active/experiments/dominated_singleton_exact_eight_kernel_absorption/second_centre.py
python3 active/experiments/dominated_singleton_exact_eight_kernel_absorption/two_coordinate_contacts.py
python3 active/experiments/dominated_singleton_exact_eight_kernel_absorption/candidate_set_gate.py
python3 active/experiments/dominated_singleton_exact_eight_kernel_absorption/swallowed_mate_split.py
```

The checked script revisions and every catalogue/result digest are listed in
the classifier report.  The minor test is exact deletion-and-contraction,
and the scripts assert the displayed counts.  No independent implementation
has yet replayed the order-eight/order-nine catalogue or these two new
compositions.  Accordingly this note must not be cited as a promoted result
until that audit exists.

## Dependencies

- [the exact connected dominated exterior](hc7_k7minus_dominated_degree_eight_exterior_connectivity.md);
- [the three surviving graphs `Q`](hc7_k7minus_dominated_degree_eight_rooted_seven_carrier.md);
- [the protected order-ten exclusion](hc7_k7minus_dominated_protected_centre_order_ten_elimination.md);
- [the terminal-kernel theorem](../results/hc7_five_terminal_rooted_fan.md); and
- [the opposite four-coordinate boundary interface](hc7_k7minus_degree_eight_centre_cube_interface.md).
