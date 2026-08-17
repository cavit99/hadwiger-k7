# Four stable roots give a tripod configuration or an exact-six fragment

**Status:** written unbounded reduction, pending separate audit.  The
separator outcome is a strict nested six-boundary fragment with exact
coefficient-four additivity and hereditary punctured-model exclusion.  The
subdivision outcome is not, by itself, a five-rooted near-clique or a pair
of six-full packets; the final section gives an exact low-excess guardrail.
This note does not prove the sparse-six-cut packet inequality,
Conjecture 21, or `HC_7`.

## 1. Input from the rooted-subdivision theorem

We use Theorem 1.2 of Hayashi, Kawarabayashi and Yoo.  In the form needed
here, it says the following.  Let `F` be a graph with a stable four-set
`Z`.  Suppose that

1. `|F-Z|>=2` and `F-Z` is connected;
2. no separation of order at most three has `Z` on one side and a
   nonempty open part on the other;
3. no separation of order at most two puts two vertices of `Z` in each
   open side; and
4. every vertex of `Z` has at least two neighbours outside `Z`.

Then `F` contains, for a suitable ordering of `Z`, at least one of

* a nondegenerate diamond on the four roots;
* a `K_{2,3}^+`-subdivision with three of the roots as feet and avoiding
  the fourth; or
* a `K_5^-`-subdivision whose two degree-three branches have legs ending
  at two roots.

The feet in the last two outcomes are exactly as stated: the theorem does
not say that all four roots are branches of the subdivision.

Primary source: Koyo Hayashi, Ken-ichi Kawarabayashi and Youngho Yoo,
[*Chasing Tripods to Obtain a Rooted Subdivision*](https://doi.org/10.1137/23M157082X),
SIAM J. Discrete Math. **39** (2025), 1683--1711, Theorem 1.2 and the
definitions immediately preceding it.

## 2. The exact shore fork

Let `G` be a six-connected graph.  Let `S` be a six-set and let `C` be a
component of `G-S` with

```text
N_G(C)=S.
```

Fix a four-set `Z subseteq S`, put `R=S-Z`, and form

```text
F=G[C union Z]-E(G[Z]).                              (2.1)
```

Thus the four roots are made stable using edge deletion only.  For a
nonempty `X subseteq C` whose external neighbourhood is a six-set `U`, put

```text
eta_U(X)=|E(G[X])|+|E_G(X,U)|-4|X|.                 (2.2)
```

### Theorem 2.1 (tripod configuration or density-neutral exact-six peel)

Assume

```text
|C|>=3,
|N_G(z) intersect C|>=2  for every z in Z.           (2.3)
```

Then one of the following holds.

1. `F` contains one of the three Hayashi--Kawarabayashi--Yoo
   configurations listed in Section 1.
2. There are a partition

   ```text
   Z=Z_X disjoint union Z_Y,   |Z_X|=|Z_Y|=2,
   ```

   a two-set `T subseteq C`, and a nonempty connected set
   `X subseteq C-T` such that

   ```text
   N_G(X)=U:=T union Z_X union R.                    (2.4)
   ```

   In particular, `U` is an actual six-cut, `X` is a proper nested
   fragment, and

   ```text
   eta_S(C)=eta_U(X)+eta_S(C-X).                     (2.5)
   ```

   The second term in (2.5) is the same edge expression as (2.2); no
   connectedness of `C-X` is asserted.

#### Proof

The graph `F-Z=G[C]` is connected and has at least three vertices.  The
set `Z` is stable by construction, and (2.3) is the required root-degree
condition.

We first verify the rooted separation hypothesis of the source theorem.
Suppose `(A,B)` is a separation of `F` of order at most three, with
`Z subseteq A` and `B-A` nonempty.  Choose a component `X_0` of
`F[B-A]`.  Since `B-A subseteq C`, deletion of the root--root edges in
(2.1) has deleted no edge incident with `X_0`.  Moreover, `C` has no
neighbour outside `C union S`.  Consequently

```text
N_G(X_0) subseteq (A intersect B) union R,
```

which has order at most five.  The vertices of `Z` ensure that
`X_0` is a proper side.  This contradicts six-connectivity of `G`.

It remains to inspect the two--two separation hypothesis.  If it holds,
all hypotheses of Hayashi--Kawarabayashi--Yoo are verified and outcome 1
follows.

Otherwise let `(A,B)` be a separation of `F` of order at most two such
that

```text
Z_X=Z intersect (A-B),  Z_Y=Z intersect (B-A),
|Z_X|=|Z_Y|=2.
```

Put `T=A intersect B`.  The four displayed roots exhaust `Z`, so
`T intersect Z` is empty and hence `T subseteq C`.  Since `|C|>=3>|T|`,
at least one of `(A-B) intersect C` and `(B-A) intersect C` is nonempty.
Interchange `A,B` if necessary, and choose a component `X` of
`G[(A-B) intersect C]`.

There is no edge in `F` from `A-B` to `B-A`.  The deleted edges in (2.1)
have both ends in `Z`, while `C` has no neighbour outside `C union S`.
It follows that

```text
N_G(X) subseteq T union Z_X union R.                 (2.6)
```

The right side has order at most six.  On the other hand `Z_Y` is
disjoint from it and anticomplete to `X`, so `X` is a proper side and
six-connectivity gives `|N_G(X)|>=6`.  Equality holds throughout (2.6).
Thus `|T|=2` and (2.4) follows.

Every edge counted in `eta_S(C)` which is incident with `X` either lies
inside `X` or joins `X` to `U`.  These are exactly the edge terms in
`eta_U(X)`; every other counted edge belongs to the second term of (2.5).
The vertex sets also partition `C`.  This proves (2.5).  \(\square\)

### Corollary 2.2 (the exact-six outcome is a legal rooted induction)

In outcome 2, complete `S` to a clique in `G[C union S]`.  Then `X` is a
component behind the order-six cut `U` and does not contain `S-U=Z_Y`.
If every original punctured shore

```text
G[C union (S-{s})],   s in S,
```

has no `(S-{s})`-rooted `K_5^-` model, then every derived punctured shore

```text
G[X union (U-{u})],   u in U,
```

has no `(U-{u})`-rooted `K_5^-` model.

#### Proof

Adding edges inside `S` creates no new edge incident with `X`, so (2.4)
makes `X` a component behind `U` in the completed torso.  Apply Corollary
3 of the audited six-boundary fragment-rerooting theorem.  \(\square\)

The rerooting source is
[`hc7_k7minus_six_boundary_fragment_rerooting.md`](hc7_k7minus_six_boundary_fragment_rerooting.md),
SHA-256

```text
53c91cee74ae8b1f5251e13c14095f8abc65f05625eedb401d3d53173996da15.
```

Its independent GREEN audit has SHA-256

```text
c30aa69b6919edd2cfba80d6df1f02e2c75d38d9544bd87e4332ba4d823526a3.
```

## 3. The exact three-contact decoder in the rooted-`K_4` branch

The rooted-`K_4` hypothesis in the live branch gives one further
normalisation which is independent of the three subdivision shapes.

### Lemma 3.1 (spanning rooted model and three-contact terminal)

Suppose `G[C union Z]` has a `Z`-rooted `K_4` model.  There is such a
model with branch bags `B_1,...,B_4` which partition `C union Z`.  For
`r in R`, put

```text
I(r)={i in {1,2,3,4}: N_G(r) intersect B_i is nonempty}.
```

If `|I(r)|>=3`, then `G[C union Z union {r}]` contains a
`(Z union {r})`-rooted `K_5^-` model.  Consequently, under the punctured
five-rooted-model exclusion,

```text
|I(r)|<=2  for both r in R                            (3.1)
```

for every spanning rooted model obtained in this way.

#### Proof

Choose a `Z`-rooted `K_4` model whose branch-bag union has maximum order.
If a vertex is uncovered, let `D` be a component of the uncovered graph.
The graph `G[C union Z]` is connected, so `D` has an edge to some branch
bag, say `B_i`.  Replacing `B_i` by `B_i union D` preserves connectedness,
disjointness, all four roots and every old bag adjacency, while enlarging
the union.  This is a contradiction.  The bags therefore partition
`C union Z`.

If `|I(r)|>=3`, the four old bags together with the singleton bag `{r}`
are connected and pairwise adjacent with at most one exception: the old
four bags form a clique and `{r}` misses at most one of them.  They are
rooted at the five distinct vertices `Z union {r}`, proving the asserted
`K_5^-` model.  The model uses no vertex of the other member of `R`, so it
is a legal punctured-shore model.  This proves (3.1).  \(\square\)

Lemma 3.1 is the exact **incidence-only three-augmented-bag certificate**.
Its failure is also exact: it says only that each omitted root is
concentrated on at most two branch bags.  It does not bound the number of
edges inside those bags, make their `C`-parts connected, or produce two
disjoint six-full subgraphs.  Those are the density-sensitive obligations
left after the decoder.

### Proposition 3.2 (what the three tripod outputs actually decode)

Each source configuration has the following exact branch-bag content.

1. A diamond on `(v_1,v_2;v_3,v_4)` contains a
   `Z`-rooted `K_4^-` model whose possible missing pair is the pair of
   bags rooted at `v_3,v_4`.  Hence, for distinct `r,s in R`, a connected
   `r`-rooted augmentation in `G-s`, disjoint from the four bags and
   adjacent to all four, gives a punctured rooted `K_5^-`.  If the possible
   missing pair is already adjacent in the host, three contacts from the
   same augmentation suffice.
2. A `K_{2,3}^+`-subdivision with feet `v_1,v_2,v_3` has five disjoint
   connected bags with quotient `K_{2,3}^+`: the three degree-two bags
   contain the three feet, and the two branch bags are unrooted.  If at
   least two of the three possible contacts among the foot bags are
   present, and, for some `s in S-{v_1,v_2,v_3}`, the other two roots in
   that three-set have disjoint connected augmentations in `G-s` which
   can be appended to the two branch bags, the five bags give a punctured
   rooted `K_5^-` model.
3. A `K_5^-`-subdivision with feet `v_1,v_2` gives five branch bags whose
   two degree-three bags contain `v_1,v_2`.  If, for some
   `s in S-{v_1,v_2}`, the five bags avoid `s` and the other three branch
   bags have pairwise disjoint connected augmentations in `G-s` containing
   the three distinct roots of `S-{v_1,v_2,s}`, the result is a punctured
   five-rooted `K_5^-` model.

#### Proof

For item 1, orient the three diamond paths from branch `a` to branch `b`.
On the path containing `v_3`, cut immediately before and after `v_3`;
put the first part in the bag containing the `v_1`-leg, the middle part in
the `v_3`-bag, and the last part in the bag containing the `v_2`-leg.
Do the same with `v_4` on the second path.  Split one edge of the third
path between the first two bags.  The resulting four connected bags have
all six adjacencies except possibly the `v_3v_4` bag pair.  The two stated
augmentations then give at most one missing pair among five bags.

For item 2, perform the same prefix--middle--suffix split on each of the
three paths containing a foot, and split one edge of the fourth path
between the two branch bags.  This is precisely the five-bag
`K_{2,3}^+` quotient.  It has seven of the ten possible bag adjacencies;
two contacts among the three foot bags raise this to nine.  Appending the
two distinct root augmentations to the two branch bags preserves all those contacts
and roots the five bags distinctly.

For item 3, contract each subdivided edge towards one of its ends and
include each leg in its incident degree-three branch bag.  This gives the
five stated bags.  The three disjoint augmentations preserve their
connectedness and all nine required adjacencies while supplying the three
missing root labels.  In every item, the explicit `G-s` confinement keeps
the unused sixth boundary root out of all five bags.
\(\square\)

The qualifications in Proposition 3.2 are necessary.  In item 1 a
three-contact fifth bag leaves two missing pairs when the original
`K_4^-` miss remains.  In item 2 the bare source quotient is three edges
short of `K_5`, and its two unrooted branch bags still need distinct root
labels.  In item 3 the source theorem controls only two feet and does not
say that the other two members of `Z` avoid the subdivision.  Thus none of
the three rows silently supplies the required augmentation.

## 4. A sharp guardrail on the subdivision outcome

The following three-vertex atom shows that a raw configuration from
outcome 1, even together with a spanning four-rooted clique model, does
not imply either local terminal.  Its excess is only four, so it does not
refute the density-sensitive target at `eta>=6`.

Let `S={0,1,2,3,4,5}` be stable, let `C={a,b,c}` induce a triangle, and
give the three vertices the boundary neighbourhoods

```text
N_S(a)={0,2,3,4,5},
N_S(b)={0,1,4,5},
N_S(c)={0,1,2,3}.                                   (4.1)
```

Every nonempty `Y subseteq C` satisfies

```text
|N_C(Y)-Y|+|N_S(Y)|>=6.                             (4.2)
```

Indeed, the values for a singleton are `7,6,6`, every pair sees the
remaining triangle vertex and all six roots, and `C` sees all six roots.

The coefficient-four excess is

```text
eta_S(C)=3+(5+4+4)-4*3=4.                           (4.3)
```

Every two vertices of `C` together see all six roots, whereas no singleton
does.  Hence every six-full connected set has at least two vertices and

```text
mu_S(C)=1.                                          (4.4)
```

There is no punctured five-rooted `K_5^-` model.  Such a model has only
three internal vertices available, so at least two of its five rooted bags
are singleton boundary roots.  Since `S` is stable, those two bags already
account for the one permitted missing adjacency.  Each would therefore
have to be adjacent to all three bags containing `a,b,c`, and hence each
singleton root would have to be adjacent to all of `a,b,c`.  In (4.1)
only root `0` has that property, so two such singleton bags do not exist.

For `Z={0,1,2,4}`, the four bags

```text
{0},  {1,b},  {2,c},  {4,a}
```

form a spanning `Z`-rooted `K_4` model.  The same four roots satisfy all
hypotheses of the Hayashi--Kawarabayashi--Yoo theorem.  The only possible
two-vertex cut consists of two triangle vertices; according to the one
triangle vertex left, it isolates exactly one of roots `1,2,4`, never a
two--two split.  Finally, the theorem's diamond outcome is present
literally.  With branches `a,b`, use

```text
P_1=a-2-c-b,   P_2=a-4-b,   P_3=a-b,
Q_1=a-0,       Q_2=b-1.
```

This is a nondegenerate diamond on `(0,1;2,4)`.  The same atom also
contains a `K_{2,3}^+`-subdivision with feet `0,2,4`,
avoiding root `1`: use the four internally disjoint `a`--`b` paths

```text
a-0-b,   a-2-c-b,   a-4-b,   a-b.
```

Equations (4.3)--(4.4) and the preceding model check prove that neither a
raw diamond, a raw `K_{2,3}^+`-subdivision, nor a raw spanning rooted
`K_4` supplies the missing fifth rooted bag or a second six-full packet.
Any decoder for outcome 1 must use the excess threshold, an additional
host-level composition, or both.

## 5. Exact scope

Theorem 2.1 removes every low-order separator failure from the proposed
tripod route without losing density or punctured-model exclusion.  What
remains is the inseparable outcome of the primary theorem.  Its three
subdivisions are only partially rooted, and Section 3 shows why treating
any of them as the desired five-rooted model would be invalid.  A complete
proof of the local inequality must still turn `eta_S(C)>=6` into the
additional disjoint attachment needed by one of those subdivisions, or
into two connected `S`-full packets.
