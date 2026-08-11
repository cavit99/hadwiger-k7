# Lifting a `K_7^-` model from the five-centre critical completion

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_five_centre_completion_model_lift_audit.md`](hc7_k7minus_five_centre_completion_model_lift_audit.md).
The theorem is unbounded.  It makes every model in the smaller critical
completion terminal when the two poles lie in distinct branch sets.  If
the poles lie in one branch set, the same proof works unless expansion of
the contracted branch set genuinely requires all five centres.  The
surviving all-five placement is reduced here to a spanning unique-owner
normal form, but that normal form is not eliminated.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting

Assume the `K_7^-` six-colour conjecture is false, and choose `G`
lexicographically minimizing `(|V(G)|,|E(G)|)` among all its
counterexamples.  Thus `G` is both globally vertex-minimal and
proper-minor-minimal subject to being non-six-colourable and
`K_7^-`-minor-free.  Use the five-centre two-cut notation

\[
 S=Z\mathbin{\dot\cup}\{p,q\},\qquad |Z|=5,
\]

where `G-S` has connected full components `C,D`, and `C` is the
equal-response side.  Contract the connected set `D\cup Z` to one vertex
`x`, retaining `C,p,q`, and call the resulting proper minor `M_C`.  The
five-centre two-cut theorem gives

\[
                    \chi(M_C+pq)=7.                 \tag{1.1}
\]

The graph in (1.1) has fewer vertices than `G`.  If it were
`K_7^-`-minor-free, (1.1) would make it a smaller counterexample.
Therefore it contains a `K_7^-` minor.

Assume in addition the four-root feasibility conclusion on the `D`-side:
for every four-set `A\subset Z`, the graph

\[
                         G[D\cup A\cup\{p,q\}]       \tag{1.2}
\]

has a `p`--`q` path `L` such that one component `K` after deleting `L`
contains all four vertices of `A`.  This is the hypothesis available in
the minimal five-root row before the all-rainbow alternatives are split.
Assume also the other half of that row: the full five-root instance on
`D` is infeasible.  Thus there is no `p`--`q` path in
`G[D\cup Z\cup\{p,q\}]` for which one component after deleting the path
contains all five vertices of `Z`.

The only edge of `M_C+pq` which need not be an edge of the contraction
minor is `pq`.  Every edge from `x` to `C` is represented in `G` by an
edge from a centre in `Z` to `C`, because `C` and `D` are anticomplete.

## 2. Four roots leave a two-sided path

### Lemma 2.1 (two attachments to a feasible path)

Let `A\subset Z` have order four, and let `L,K` witness (1.2).  Then `K`
has neighbours at two distinct vertices of `L`.  Consequently an edge of
`L` splits it into connected subpaths `L_p,L_q`, containing `p,q`
respectively, such that `K` is adjacent to both subpaths.

#### Proof

The four roots in `A` are independent and belong to the connected graph
`K`, so `K\cap D` is nonempty.  Let `R` be a component of `G[K\cap D]`.
There are no `C`--`D` edges, and distinct components after deleting `L`
are anticomplete.  Hence

\[
                         N_G(R)\subseteq Z\cup V(L). \tag{2.1}
\]

The nonempty component `C` lies beyond this neighbourhood.  Seven-
connectivity gives `|N_G(R)|\ge7`; since `|Z|=5`, at least two distinct
vertices of `L` have neighbours in `R`, and hence in `K`.  Splitting `L`
at any edge between two such attachments gives the last assertion.
\(\square\)

### Lemma 2.2 (absorbing an omitted root into the path side)

Let `z\in Z`, put `A=Z-\{z\}`, and let `L,K` be a four-root witness for
`A`.  Then `z` has no neighbour in `K`.  Moreover, there is a connected
set `W_z`, disjoint from `K`, which contains `V(L)\cup\{z\}`.

#### Proof

If `z` had a neighbour in `K`, then in
`G[D\cup Z\cup\{p,q\}]-V(L)` the component containing `K\cup\{z\}`
would contain all five vertices of `Z`.  This contradicts full five-root
infeasibility.

The full component `D` gives `z` a neighbour in `D`.  If `z` has a
neighbour on `L`, take `W_z=V(L)\cup\{z\}`.  Otherwise, add to `V(L)`
the vertex `z` and every component of `G[D-V(L)]` met by `z`.  None of
those components meets `K`, by the first paragraph.  Each is adjacent to
`L` because `D` is connected, and at least one is adjacent to `z`.
The resulting set `W_z` is connected and disjoint from `K`. \(\square\)

## 3. The contracted bag needs at most four roots

Fix a `K_7^-` model `mathcal M` in `M_C+pq`.  Suppose that `p,q,x` lie in
three distinct branch sets, denoted `P,Q,X`, respectively.  The other four
branch sets lie wholly in `C`; denote them by

\[
                         R_1,R_2,R_3,R_4.             \tag{3.1}
\]

Only adjacencies which are edges of the chosen labelled copy of `K_7^-`
are called required below.

### Lemma 3.1 (four-root expansion cover)

The `x`-bag may be pruned so that there is a set `A_0\subseteq Z`, with
`|A_0|\le4`, having the following property.  If `W` is any connected set
in the original graph which contains `A_0`, then replacing `x` in `X` by
`W`:

1. makes the lifted `X`-bag connected; and
2. preserves every required adjacency from `X` to the four bags in
   (3.1).

Here `W` is assumed disjoint from `C`; adjacencies from the old
`C`-vertices of `X` to the other bags are left unchanged.

#### Proof

Every component `J` of `(M_C+pq)[X-\{x\}]` is adjacent to `x`, since `X`
is connected.  Choose an inclusion-minimal subfamily `mathcal J` of these
components such that

\[
                   \{x\}\cup\bigcup_{J\in\mathcal J}V(J)       \tag{3.2}
\]

retains every required adjacency from `X` to the bags `R_i`.  Replace `X`
by (3.2).  No adjacency to `P` or `Q` is lost: the literal contraction
edges `xp,xq` join `x` to those two bags.

Minimality assigns to every `J\in\mathcal J` a distinct bag `R_i` which
is contacted by `J` but by neither `x` nor any other member of
`mathcal J`.  Hence, if `k=|mathcal J|`, at least `k` of the four bags are
contacted by retained components.

For every `J\in\mathcal J`, choose a centre `z_J\in Z` adjacent in `G` to
`J`.  Such a centre exists because the edge from `x` to `J` in `M_C`
comes from `D\cup Z`, while `D` is anticomplete to `C`.  For each required
bag `R_i` not contacted by a retained component, its adjacency to (3.2)
is an edge `xy` with `y\in R_i`; choose a centre `z_i\in Z` adjacent to
`y` in `G`.  Put

\[
 A_0=\{z_J:J\in\mathcal J\}
       \cup\{z_i:R_i\text{ is not contacted by a retained component}\}.
\tag{3.3}
\]

There are at most `k+(4-k)=4` choices in (3.3), so `|A_0|\le4`.
If `W` contains `A_0`, every component in `mathcal J` is joined to `W`
through its selected centre edge.  Each required `X`--`R_i` adjacency is
either an unchanged edge from a retained component or the selected edge
`z_i y`.  This proves both assertions. \(\square\)

## 4. The distinct-pole-bag placement is terminal

### Theorem 4.1 (critical-completion model lift)

Under the setting of Section 1, if `M_C+pq` has a `K_7^-` model in which
`p` and `q` lie in distinct branch sets, then `G` contains a `K_7^-`
minor.

#### Proof

If the model avoids `x`, choose a `p`--`q` path with open interior in the
connected full component `D`.  If `p,q` lie in distinct bags, split this
path across an edge and add its two halves to the corresponding bags.
This replaces the only possible use of the artificial edge `pq`.  All
other model edges already belong to `G`.

Suppose next that `x` lies in the `p`-bag or the `q`-bag.  Replace `x` by
the whole connected set `D\cup Z`.  This reconnects every component of
the old bag through the centre edge which represented its edge to `x`,
and it preserves every old adjacency incident with `x`.  If, say, `x`
lies in the `p`-bag, an edge from `q` to `D` replaces the artificial
`p`--`q` bag adjacency.  The other orientation is symmetric.

It remains that `p,q,x` lie in distinct bags.  Apply Lemma 3.1 and extend
its set `A_0` to a four-set `A\subset Z`.  Choose a feasible pair `L,K`
for `A` on the `D`-side, and split `L` into `L_p,L_q` as in Lemma 2.1.
Make the following replacements:

\[
 \begin{aligned}
 P'&=P\cup V(L_p),\\
 Q'&=Q\cup V(L_q),\\
 X'&=(X-\{x\})\cup V(K).
 \end{aligned}                                      \tag{4.1}
\]

The four other bags are unchanged.  The sets in (4.1) are pairwise
disjoint: the old bags outside `x` lie in `C\cup\{p,q\}`, while `K` and
the open parts of `L` lie in `D\cup A`, and `K\cap L=\varnothing`.
They are connected.  This is clear for `P',Q'`; Lemma 3.1 makes `X'`
connected because `A_0\subseteq A\subseteq K`.

The splitting edge of `L` supplies the `P'`--`Q'` adjacency.  The two
attachments in Lemma 2.1 supply the `X'`--`P'` and `X'`--`Q'`
adjacencies.  Lemma 3.1 preserves every required adjacency from `X'` to
the four unchanged bags.  Every remaining required model adjacency is an
old edge not involving `x` or the artificial edge `pq`, and is unchanged.
Thus the seven lifted bags form a `K_7^-` model in `G`. \(\square\)

### Corollary 4.2 (the exact surviving placement)

Suppose `G` has no `K_7^-` minor.  Then every `K_7^-` model in
`M_C+pq` which genuinely uses the artificial edge has all of the following
properties:

1. `p,q` lie in one branch set `B`;
2. `x` lies in a different branch set `X`; and
3. the other five branch sets lie wholly in `C`; and
4. the branch-set contact graph has exactly one nonedge, with neither end
   at `X`.

Moreover, after pruning `X-\{x\}` as in Lemma 3.1, no set of four centres
can both connect all retained components to the expansion of `x` and
preserve every required adjacency from `X` to the five `C`-only bags.

#### Proof

Theorem 4.1 proves item 1.  If the model avoided `x`, a `p`--`q` path
through `D` could replace `pq` inside `B`.  If `x` belonged to `B`,
expanding it to `D\cup Z` would connect `p` to `q` and preserve every
edge incident with `x`.  Both cases would lift the model to `G`, proving
items 2 and 3.

The literal edges `xp,xq` make `X` adjacent to `B`.  If the contact graph
were complete, declare any one edge `XR_j` to be the missing edge of the
desired `K_7^-` model.  If its unique nonedge were incident with `X`, it
would therefore be some `XR_j`; use that edge as the missing edge.  In
either case only four of the five `X`--`R_i` adjacencies remain required.
The proof of Lemma 3.1 gives a four-centre expansion cover for those four
requirements.  Replacing `x` by the corresponding feasible component `K`
and the internal artificial edge `pq` of `B` by the whole feasible path
`L` then lifts a `K_7^-` model to `G`, as below.  Thus the contact graph is
not complete and its unique nonedge lies outside `X`, proving item 4.

Now prune `X` exactly as in Lemma 3.1, with five rather than four
`C`-only bags.  The same argument produces a centre set of order at most
five which connects the retained components and preserves all required
`X`-bag adjacencies.  If some such set had order at most four, extend it
to a four-set `A`, choose a feasible `p`--`q` path `L` with complementary
component `K` containing `A`, replace `x` by `K`, and replace the internal
edge `pq` of `B` by the whole path `L`.  Lemma 2.1 supplies the required
`K`--`L` adjacency, and the proof of Theorem 4.1 verifies every other
adjacency.  This would again lift the model to `G`.  Therefore all five
centres are genuinely required. \(\square\)

### Theorem 4.3 (all-five unique-owner normal form)

Suppose `G` has no `K_7^-` minor.  Then `M_C+pq` has a `K_7^-` model
whose branch sets can be written

\[
                         B,\{x\},R_1,\ldots,R_5       \tag{4.2}
\]

and labelled so that all of the following hold.

1. The vertices `p,q` belong to `B`, and

   \[
             B,R_1,\ldots,R_5
   \quad\hbox{partition}\quad C\cup\{p,q\}.
   \tag{4.3}
   \]

2. The singleton branch set `\{x\}` is adjacent to each of the other six
   branch sets.
3. The branch-set contact graph has exactly one nonedge, and that nonedge
   has both ends in `\{R_1,\ldots,R_5\}`.
4. After relabelling `Z=\{z_1,\ldots,z_5\}`, one has

   \[
                         N_G(R_i)\cap Z=\{z_i\}
                         \qquad(1\le i\le5).          \tag{4.4}
   \]

Consequently every neighbour in `C` of `z_i` lies in `R_i\cup B`.
Thus each centre has one unique `C`-only owner bag; contacts with the
pole-pair bag `B` remain unrestricted.

#### Proof

Start with a model supplied by (1.1).  In a target-free `G`, its
artificial edge `pq` must be essential to the model, and Corollary 4.2
gives bags `B,X,R_1,\ldots,R_5` with `p,q\in B`, `x\in X`, and
`R_i\subseteq C`.

By item 4 of Corollary 4.2, the contact graph has exactly one nonedge,
outside `X`, and every edge from `X` to another bag is required.

Prune `X-\{x\}` inclusion-minimally while retaining all five
`X`--`R_i` adjacencies.  Let `\mathcal J` be the retained components,
put `k=|\mathcal J|`, and let `m` be the number of bags `R_i` contacted
by at least one member of `\mathcal J`.  Minimality gives each member of
`\mathcal J` a distinct private bag, so `m\ge k`.  As in (3.3), one
centre for each retained component and one centre for each bag not
contacted by a retained component give an expansion cover of order at
most

\[
                             k+(5-m)\le5.             \tag{4.5}
\]

Corollary 4.2 excludes a cover of order at most four.  Equality must
therefore hold throughout (4.5), including after duplicate selected
centres are removed.  In particular `m=k`.  The `k` distinct private
bags exhaust the `m` contacted bags; hence every retained component
contacts exactly its own private bag and no other `R_i`.

Move each retained component into its private bag.  That bag remains
connected, and its old edge to `x` makes it adjacent to the now-singleton
bag `\{x\}`.  Bags contacted directly by `x` are unchanged.  Thus we
obtain (4.2), with `\{x\}` adjacent to every `R_i`.  If this move filled
the sole nonedge, the resulting contact graph would be complete; declare
any edge `\{x\}R_j` missing and apply the four-centre same-bag lift.
Target-freeness therefore ensures that the sole nonedge persists.

For each `i`, put

\[
                              O_i=N_G(R_i)\cap Z.
\]

The set `O_i` is nonempty: an `x`--`R_i` edge in the contraction is
represented by a centre--`R_i` edge because `C` and `D` are
anticomplete.  If one centre belonged to both `O_i` and `O_j`, choose it
for those two bags and choose one member of each of the other three
nonempty owner sets.  These at most four centres would preserve all five
`x`--`R_i` adjacencies when `x` is expanded.  Four-root feasibility and
the same-bag lift would again give a `K_7^-` model in `G`.  Hence the five
nonempty subsets `O_1,\ldots,O_5` of the five-set `Z` are pairwise
disjoint.  Each is therefore a singleton, and their elements exhaust
`Z`.  This proves (4.4) after relabelling.

The sole nonedge cannot be `BR_i`.  Suppose it were.  Apply Lemma 2.2 to
the omitted owner `z_i`, obtaining a four-root witness `L,K` for
`Z-\{z_i\}` and a connected set `W_{z_i}` containing
`V(L)\cup\{z_i\}` and disjoint from `K`.  In the original graph use the
seven bags

\[
              B\cup W_{z_i},\quad K,\quad R_1,\ldots,R_5.       \tag{4.6}
\]

The first bag is connected because `W_{z_i}` replaces the internal
artificial edge `pq` of `B`.  Lemma 2.1 makes `K` adjacent to that bag.
For `j\ne i`, the owner `z_j\in K` preserves the `K`--`R_j`
adjacency.  The edge from `z_i\in W_{z_i}` to `R_i` repairs the old
nonedge `BR_i`.  All other bag adjacencies are inherited from the model.
Thus (4.6) is a `K_7^-` model whose only possibly missing edge is
`KR_i`, a contradiction.  The unique nonedge is therefore between two
of the five `R_i`.

It remains only to make the model spanning on `C`.  Repeatedly absorb a
component of the as-yet uncovered part of the connected graph `G[C]`
into an adjacent one of `B,R_1,\ldots,R_5`.  Such a bag always exists,
and absorption preserves its connectivity and every old model edge.  If
an absorption filled the sole missing branch-set adjacency, the contact
graph would become complete; declaring an edge `\{x\}R_j` missing and
using the four-centre lift above would be terminal.  If an absorption
made one centre adjacent to two distinct `R_i`, the preceding
four-centre cover would likewise be terminal.  Since `G` is assumed
target-free, neither event occurs.  After all vertices of `C` have been
absorbed, (4.3), the unique nonedge assertion, and (4.4) all still hold.
The final consequence follows immediately from (4.3)--(4.4). \(\square\)

## 5. Exact nonclosure

The smaller critical completion always supplies a `K_7^-` model, and the
four-root witness now lifts every distinct-pole-bag placement.  The only
remaining placement is therefore not an arbitrary branch-set problem.
It has the spanning normal form (4.2)--(4.4): one pole-pair bag, a
singleton contracted bag adjacent to the other six bags, and five
`C`-only bags in bijection with the five centres.  The sole quotient
nonedge lies between two of the `C`-only bags.  Every `C`-neighbour of a
centre lies in its unique owner bag or in the common pole-pair bag.

If one centre can serve two owner bags, the proof above is already
terminal.  The exact residue is instead a bijective all-five allocation.
Full five-root feasibility is unavailable by hypothesis, so replacing
`pq` through `D` cannot presently be made disjoint from the expansion of
`x`.  The theorem does, however, remove every component-connectivity
ambiguity from that obstruction: the contracted bag is a singleton and
the five roots are needed only for its five owner-bag adjacencies.

No assertion is made that this last unique-owner placement exists.
Eliminating it requires a branch-set exchange which makes one centre
serve two owner bags, or a same-bag replacement of `pq` through `C`
which avoids the contracted bag.  This is the first unsupported
composition step.

## Dependencies and claim status

- exact seven-chromaticity of `M_C+pq` comes from the separately audited
  five-centre two-cut reduction;
- existence of a `K_7^-` model in that smaller graph uses the global
  vertex-minimality coordinate in the choice of `G`;
- four-root feasibility on `D` is an explicit standing hypothesis of the
  minimal five-root row; and
- all branch-set pruning, root counting, and lifting arguments are proved
  here.

The theorem closes every distinct-pole-bag placement and reduces the
all-five same-bag residue to Theorem 4.3.  It does not eliminate that
unique-owner normal form or close the complete five-centre two-cut
branch.
