# Four-root feasibility gives a one-centre palette transfer

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_five_centre_four_root_transfer_audit.md`](hc7_k7minus_five_centre_four_root_transfer_audit.md).
This note eliminates two unbounded rows in the five-centre two-cut attack.  It
does not eliminate minimal bad-root sets of order four, or the remaining
order-five rows described in Section 5.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting

Let `G` satisfy

\[
 \kappa(G)\ge7,
 \qquad \chi(G)=7,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G.
 \tag{1.1}
\]

Let `Z` be an independent set of five degree-eight vertices.  Let `p,q`
be nonadjacent vertices outside `Z`, put

\[
                         S=Z\mathbin{\dot\cup}\{p,q\},
\tag{1.2}
\]

and suppose that `G-S` has exactly two connected components `C,D`, both
adjacent to every vertex of `S`.  Assume that the closed sides have the
opposite response colourings supplied by the five-centre two-cut theorem:

* `G[C union S]` has a proper six-colouring in which `Z` is monochromatic
  and `p,q` have one common different colour; and
* `G[D union S]` has a proper six-colouring in which `Z` is monochromatic
  and `p,q` have two distinct colours, both different from the colour on
  `Z`.

For `z in Z`, write

\[
 c_z=|N_G(z)\cap C|,
 \qquad d_z=|N_G(z)\cap D|,
 \qquad \rho_z=|N_G(z)\cap\{p,q\}|.
\tag{1.3}
\]

Since `z` has degree eight and `Z` is independent,

\[
                         c_z+d_z+\rho_z=8.           \tag{1.4}
\]

For `A subseteq Z`, call the `C`-rooted graph on
`C union A union {p,q}` feasible when it contains a `p`--`q` path `P`
such that all vertices of `A` belong to one component of the graph after
deleting `P`.  Define `D`-feasibility symmetrically.

## 2. Absorbing the omitted root's components

### Lemma 2.1 (equal-response transfer)

Let `z in Z` and put `A=Z-{z}`.  If the `C`-rooted graph with root set
`A` is feasible while the one with root set `Z` is infeasible, then the
closed `D`-side has a proper six-colouring in which

1. `A` is monochromatic;
2. `p,q` have one common colour different from the colour on `A`; and
3. `z` avoids the common colour on `p,q`.

#### Proof

Choose a `p`--`q` path `P` witnessing feasibility and let `K` be the
component after deleting `P` which contains `A`.  The vertex `z` has no
neighbour in `K`.  Otherwise adding `z` to `K` would leave all five roots
in one component after deleting the same path, contrary to the assumed
infeasibility for `Z`.

Every neighbour of `z` in `C` therefore lies on `P` or in a component of
the rooted graph minus `P` other than `K`.  Let `W` be the union of `P`
and all components of the latter kind which contain a neighbour of `z`.
Every such component has a neighbour on `P`, so `W` is connected.  The
sets `K,W` are disjoint and adjacent, and `W` contains `p,q` and a
neighbour of `z`.

Contract spanning trees of `K` and `W`, delete the unused vertices of
`C`, and retain `D` and `z`.  This is a proper minor.  In any proper
six-colouring of it, the two contraction images have distinct colours,
and `z` avoids the colour of the image of `W`.  Expand only the literal
vertices of `A` from the first image and `p,q` from the second.  The roots
in `A` are independent and `pq` is absent, so this gives the required
proper colouring of `G[D union S]`.  All edges from the expanded vertices
to `D` were represented by edges incident with the corresponding
contraction image.  \(\square\)

The absorption into `W` is important.  In particular, no centre--pole
edge at `z` is required to force item 3.

### Lemma 2.2 (distinct-response transfer)

Let `z in Z` and put `A=Z-{z}`.  If the `D`-rooted graph with root set
`A` is feasible while the one with root set `Z` is infeasible, then the
closed `C`-side has a proper six-colouring in which

1. `A` is monochromatic; and
2. the three blocks `A,{p},{q}` have three distinct colours.

#### Proof

Choose a feasible `p`--`q` path `P` and let `K` be the component after
deleting `P` which contains `A`.  Some component `R` of `K cap D` is
nonempty.  Indeed, `A` has four independent vertices and `K` is
connected, so its connections between the roots use vertices of `D`.

The neighbourhood of `R` in `G` is contained in

\[
                         Z\cup V(P).                  \tag{2.1}
\]

There is no edge from `R` to `C`; and a vertex of `D-P` outside the
component containing `R` has no edge to `R`.  Since `C` is nonempty,
`N_G(R)` separates `R` from `C`.  Seven-connectivity and `|Z|=5` imply
that `R` has at least two distinct neighbours on `P`.

Split `P` across an edge between two such neighbours into connected
subpaths `P_p,P_q` containing `p,q`, respectively.  Then `K,P_p,P_q` are
three pairwise adjacent connected sets.  Contract a spanning tree of each,
delete unused vertices of `D`, and retain `C` and `z`.  The three images
form a triangle and hence have three distinct colours in every proper
six-colouring of the resulting proper minor.  Expanding `A` from the
`K`-image and `p,q` from the other two images gives the asserted colouring
of `G[C union S]`.  \(\square\)

## 3. The terminal equality-side row

### Theorem 3.1 (a small equality-shore contact is impossible)

Suppose that the `C`-rooted graph with root set `Z` is infeasible and
every proper subset of `Z` is feasible.  Then

\[
                              c_z\ge4
                    \qquad\text{for every }z\in Z.   \tag{3.1}
\]

#### Proof

Suppose `c_z<=3` for some `z`, and put `A=Z-{z}`.  Fix the permitted
equal-response colouring `phi_C` of `G[C union S]`.  Name the colour of
`Z` by `alpha` and the common colour of `p,q` by `beta`.  Lemma 2.1 gives
a proper colouring `phi_D` of `G[D union S]` in which `A` is monochromatic,
`p,q` have a common different colour, and `z` avoids that pole colour.
Permute colour names so that the colours of `A` and `{p,q}` in `phi_D`
are `alpha,beta`, respectively.

Regard

\[
 C,qquad A\cup\{p,q\},qquad D\cup\{z\}
\tag{3.2}
\]

as the left open side, common boundary, and right open side.  The two
colourings agree on the boundary.  The only edges between the open sides
are the `c_z` edges from `z` to `C`.

Every vertex of `N_C(z)` avoids `alpha` under `phi_C`, because the full
closed-side colouring `phi_C` assigns `alpha` to `z`.  If `phi_D(z)` is
`alpha`, all crossing edges are already proper.  It is not `beta` by
Lemma 2.1.  Otherwise it is one of the four colours outside
`{alpha,beta}`.  At most three of those four colours occur on `N_C(z)`.
Permute the four free colour names on the `D`-side so that the colour of
`z` is sent to an absent one.  The two colourings then glue to a proper
six-colouring of `G`, contrary to (1.1).  This proves (3.1).  \(\square\)

### Corollary 3.2 (the opposite contacts are small cliques)

Assume in addition that every exceptional centre has a `K_4`-free
neighbourhood of independence number three.  Under the hypotheses of
Theorem 3.1,

\[
                              d_z\le3
                    \qquad\text{for every }z\in Z,   \tag{3.3}
\]

and `N_D(z)` is a clique.

#### Proof

The two contact sets `N_C(z),N_D(z)` are anticomplete.  Hence

\[
 \alpha(G[N_C(z)])+\alpha(G[N_D(z)])
 \le \alpha(G[N(z)])=3.                              \tag{3.4}
\]

The first contact set has at least four vertices by Theorem 3.1 and cannot
be a clique because `G[N(z)]` is `K_4`-free.  Its independence number is
therefore at least two, so the second contact set has independence number
one and is a clique.  `K_4`-freeness bounds that clique by three vertices.
\(\square\)

## 4. One terminal distinct-side row

### Theorem 4.1 (two pole contacts and at most two shore contacts)

Suppose that the `D`-rooted graph with root set `Z` is infeasible and
every proper subset of `Z` is feasible.  If some `z in Z` satisfies

\[
                         \rho_z=2,
                         \qquad d_z\le2,               \tag{4.1}
\]

then `G` is six-colourable.

#### Proof

Put `A=Z-{z}`.  Fix the permitted distinct-response colouring `phi_D` of
`G[D union S]`, naming the colours on `Z,p,q` by `alpha,beta,delta`,
respectively.  Lemma 2.2 gives a colouring `phi_C` of `G[C union S]` in
which `A,{p},{q}` have three distinct colours.  Align those three colours
with `alpha,beta,delta`.

Use `C union {z}` and `D` as the two open sides and
`A union {p,q}` as their common boundary.  The only crossing edges are
the `d_z` edges from `z` to `D`.  Under `phi_D`, their `D`-ends avoid
`alpha`, since the full closed-side colouring assigns `alpha` to `z`.
Under `phi_C`, the vertex `z` avoids `beta,delta` because it is adjacent
to both poles.  If it has colour `alpha`, every crossing edge is proper.
Otherwise it has one of the three colours outside
`{alpha,beta,delta}`.  At most two of those three colours occur on
`N_D(z)`, so permute the three free colours on the `C`-side to send the
colour of `z` to an absent one.  The two partial colourings glue to a
proper six-colouring of `G`.  \(\square\)

### Corollary 4.2

If both shores have a minimal infeasible root set of order five, then no
centre has two pole neighbours.

#### Proof

For `rho_z=2`, identity (1.4) gives `c_z+d_z=6`.  If `c_z<=3`, Theorem
3.1 is terminal.  Otherwise `d_z<=2`, and Theorem 4.1 is terminal.
\(\square\)

## 5. Exact remaining rows

Theorems 3.1 and 4.1 are unbounded in `|C|,|D|`.  After the already proved
three-root equality-side closure, they leave the following cases.

1. A minimal infeasible equality-side root set has order four.
2. The equality side has minimal bad-root order five, every centre has at
   least four `C`-neighbours, and every `D`-contact set is a clique of
   order at most three.
3. If the distinct side also has minimal bad-root order five, every centre
   has at most one pole neighbour.  For a centre with one pole neighbour,
   the unresolved palette obstruction is exact: the transferred colour
   of the centre can equal the colour of the nonadjacent pole, or a
   three-vertex `D`-contact clique can use all three freely permutable
   colours.

The last obstruction is not removed by an abstract Hall count.  Its
geometric repair requires a feasible `p`--`q` path whose two contracted
halves both meet the omitted centre and both meet the retained four-root
component, or a terminal separation/minor when that alternating path does
not exist.
