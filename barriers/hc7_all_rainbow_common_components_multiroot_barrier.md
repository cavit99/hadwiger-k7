# Barrier to a simultaneous five-triangle rooted model

**Status:** explicit barrier/counterexample to an intermediate claim, with
a deterministic exhaustive checker in
[`hc7_all_rainbow_common_components_multiroot_barrier_verify.py`](hc7_all_rainbow_common_components_multiroot_barrier_verify.py).

This construction shows that the six common bichromatic components in the
all-rainbow row do not, even together with seven-connectivity of the
closed shore, force one rooted `K_5` model whose three non-pole bags all
meet every contact triangle.  It also has no separator of order at most
six.  The construction is not a five-centre critical host and does not
satisfy the later private-contact conclusions.

Throughout, `K_t^-` denotes `K_t` with one edge deleted.

## 1. The refuted intermediate claim

The following implication is false.

> Let `H` be a seven-connected graph with nonadjacent nominated vertices
> `p,q` and a proper colouring with colour classes labelled
> `beta,delta,gamma_1,gamma_2,gamma_3`.  Let
> `T_1,...,T_5` be rainbow triangles, each having one vertex of every
> `gamma` colour.  Suppose that, for every `i`,
>
> - the `beta`--`gamma_i` component containing `p` contains the
>   `gamma_i`-vertex of every `T_j`; and
> - the `delta`--`gamma_i` component containing `q` contains the
>   `gamma_i`-vertex of every `T_j`.
>
> Then either `H` has a `p,q`-rooted `K_5` model whose three remaining
> branch sets each meet every `T_j`, or `H` has a separator of order at
> most six.

The counterexample below has neither conclusion.  Thus neither ordinary
connectivity nor the literal common-component data can provide the
simultaneous rooted model or a small separator.

## 2. Construction

Take five independent colour pairs

\[
\begin{aligned}
 B&=\{p,v\},&D&=\{q,u\},\\
 A&=\{a_0,a_1\},&X&=\{b_0,b_1\},&Y&=\{c_0,c_1\}.
\end{aligned}                                                   \tag{2.1}
\]

Give these pairs the colours

\[
 B:\beta,\qquad D:\delta,\qquad
 A:\gamma_1,\quad X:\gamma_2,\quad Y:\gamma_3.
\tag{2.2}
\]

Start with the complete five-partite graph with the five parts in (2.1),
and delete the single edge `pq`.  Call the resulting graph `H`.  In
particular,

\[
                         p-u-v-q                         \tag{2.3}
\]

is a `beta`--`delta` path.

Nominate the five rainbow triangles

\[
\begin{array}{lll}
 T_1=\{a_0,b_0,c_0\},&
 T_2=\{a_0,b_0,c_1\},&
 T_3=\{a_0,b_1,c_0\},\\
 T_4=\{a_0,b_1,c_1\},&
 T_5=\{a_1,b_0,c_0\}.&
\end{array}                                                   \tag{2.4}
\]

All three vertices of each displayed set belong to different parts, so
each set induces a triangle and is rainbow.

## 3. Connectivity and common components

### Lemma 3.1

The graph `H` is seven-connected.

#### Proof

The vertices `p,q` have degree seven, so `kappa(H)<=7`.  Delete at most
six vertices and let `R` be the remaining set.  Then `|R|>=4`, so `R`
contains a vertex `r` outside `{p,q}`.  The vertex `r` is adjacent to
every vertex except its unique colour-pair mate.  Hence it reaches every
vertex of `R` directly except possibly that mate.  If the mate remains,
choose a third vertex `t`.  The edges from `t` to the pair are present
unless that pair contains one of `p,q` and `t` is the other pole.  At most
one choice of `t` is therefore exceptional; since `|R|>=4`, another choice
exists and gives a path of length two.  Thus `H[R]` is connected.
Therefore `kappa(H)>=7`, proving equality. \(\square\)

### Lemma 3.2

For each `i in {1,2,3}`, the `beta`--`gamma_i` component containing `p`
contains every `gamma_i` contact in (2.4), and the
`delta`--`gamma_i` component containing `q` does likewise.

#### Proof

For a fixed `gamma_i`, the subgraph induced by its two-vertex colour part
and either `B` or `D` is a complete bipartite graph.  It is connected and
contains both vertices of the `gamma_i` part.  These two vertices include
all contacts of that colour occurring in (2.4). \(\square\)

The expected one-triangle conclusion is also present.  For each `T_j`,
the five bags

\[
                         \{p,u\},\quad\{v,q\},
                 \quad (\{t\}:t\in T_j)             \tag{3.1}
\]

form a `p,q,T_j`-rooted `K_5` model: the first two bags are connected and
adjacent through `uv`, and the three singleton bags form the displayed
triangle and are adjacent to both pole bags.

## 4. No simultaneous rooted model

### Theorem 4.1

There is no `p,q`-rooted `K_5` model in `H` with three further branch
sets `S_1,S_2,S_3` such that

\[
                         S_i\cap T_j\ne\varnothing
                    \qquad(1\le i\le3,\ 1\le j\le5).     \tag{4.1}
\]

#### Proof

The three sets `S_1,S_2,S_3` are pairwise disjoint.  Since each `T_j`
has order three, (4.1) forces its three vertices to occur one per stable
bag.

Compare `T_1` and `T_2`.  Their common vertices `a_0,b_0` occupy two
stable bags, so `c_0,c_1` must both occupy the third.  Comparing `T_1`
with `T_3` similarly puts `b_0,b_1` in one stable bag, and comparing
`T_1` with `T_5` puts `a_0,a_1` in one stable bag.  Consequently, up to
permuting the stable bags,

\[
            A\subseteq S_1,\qquad X\subseteq S_2,
            \qquad Y\subseteq S_3.                   \tag{4.2}
\]

Each pair in (4.2) is independent.  To be connected, each `S_i` must
therefore contain another vertex.  All six vertices in `A union X union
Y` already belong to the three stable bags.  The vertices `p,q` belong
to the two nominated pole bags and cannot be used.  Only `u,v` remain,
but two vertices cannot supply a distinct connecting vertex to each of
three disjoint stable bags.  At least one `S_i` is disconnected, a
contradiction. \(\square\)

Together with Lemma 3.1, this also proves that failure of the simultaneous
model does not force a separator of order at most six.

## 5. Exact scope

This barrier retains all of the data used by the proposed static
inference:

- one proper colouring;
- nonadjacent poles and a literal bichromatic pole path;
- five rainbow contact triangles;
- all six common pole--contact bichromatic components;
- an individual rooted `K_5` model for every contact triangle; and
- connectivity stronger than the relative connectivity available on a
  general shore.

It does **not** realize a hypothetical counterexample to the main
conjecture.  In particular, if abstract centres are attached to the five
triangles in (2.4), most triangles do not have the private contacts forced
by the later five-centre theorems.  Nor is `H` asserted to arise as a
shore of a seven-contraction-critical graph with the opposite colouring
response or the unique-owner completion model.

Thus the barrier does not refute a theorem using private-contact
allocation, proper-minor criticality, or the coupled `C`-shore model.  It
does refute any attempt to obtain the simultaneous rooted model, or a
small separator, solely from the common bichromatic components and
connectivity.

## Verification

Run

```text
python3 barriers/hc7_all_rainbow_common_components_multiroot_barrier_verify.py
```

The checker verifies the colouring, the five triangles, all six common
components, exact vertex-connectivity seven, the five individual rooted
models, and exhaustively excludes the simultaneous rooted model.
