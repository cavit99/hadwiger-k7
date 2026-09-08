# A rooted four-clique reserving three neighbourhood vertices

**Status:** written proof; a separate internal audit is recorded beside it.
This is a structural rooted-model conclusion, not closure of the
two-triangle case, Conjecture 19, or HC7.

Graphs are finite and simple. Write `Q=K_7-2K_2`, with the two missing
edges independent; set neighbourhoods are external.

**Theorem.** Let `G` be seven-connected, with `delta(G)>=8`, no `Q`
minor, and a degree-eight vertex `v`. Suppose
`N(v)=A dotcup B dotcup {x,y}`, where `A,B` are triangles and `xy` is
an edge. Choose `a in A,b in B` so that
`R={a,b,x,y}` induces only the edge `xy`, and put
`T=(A-{a}) union (B-{b})` and `W=G-N[v]`.
Such a choice exists. For every such choice, some `r in R` satisfies:

`G-v-(R-{r})` contains a `T`-rooted `K_4` model.

Thus the four prescribed triangle roots survive separately, and the
model avoids `v` and three of the four reserved neighbours. No colouring
assumption is used.

## Inputs and the choice of roots

We use these exact separately audited revisions:

- [Connected-set contraction closure](../active/hc7_companion_contraction_closure.md),
  SHA-256 `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`:
  contracting a connected set of at most three vertices cannot create
  a literal `K_5^-`.
- [The two-triangle exterior theorem](hc7_degree8_two_triangle_exterior.md),
  SHA-256 `e51564c9ffd857d15eb3d1de9c5cfa4ce9b9bfac514ac3188ac5379e2a745776`:
  `W` is nonempty, connected, and full to `N(v)`.
- [The exact rooted-four alternative recorded in the exterior-helper source](hc7_two_triangle_exterior_helpers.md),
  SHA-256 `b3fe07ea52e0e553c61edb59cd5b7da3719ae834d8803f21afb9bde90fc410a8`.
  Norin--Totschnig, Theorem 8, gives a rooted `K_4`, an order-two
  trisection with two open parts each containing a root, a separation
  of order at most three whose open side contains at least two vertices
  and no prescribed root, or a plane drawing with all four roots on
  one face. The exact extra conditions in its separation alternative
  are retained in the cited record; only the stated weaker consequences
  are needed here.
- [Jakobsen's density input as recorded in the triangle-poor-edge source](hc7_k7minus_degree_eight_triangle_poor_edge_packing.md),
  SHA-256 `2ffeb857f4c999abc14bc28cd4650332d9397a140c601929117376f38f637449`;
  its [audit](hc7_k7minus_degree_eight_triangle_poor_edge_packing_audit.md)
  has SHA-256 `bfc73f1df0cd965054d434f2e7afe7fbc3f3d6629f0ce643a07854583e7c0e4d`.
  In the required order range, `m>=9n/2-12` forces a `K_7^-` minor
  or a `(K_{2,2,2,2},K_6,4)`-cockade. The primary formulation was
  inspected for the cited record; no fresh primary inspection is claimed.

Contracting `xy` leaves the literal four-clique `{v} union A` intact.
The merged vertex is adjacent to `v`, so it has at most one A neighbour,
or there is a literal `K_5^-`. Similarly `x,y` collectively see at most
one B vertex. There are therefore at least two choices in each triangle
avoiding both `x,y`. There is at most one A--B edge: two edges with
different A ends are forbidden by contracting the B triangle; two with
the same A end have different B ends and are forbidden symmetrically.
Among the available choices of `a,b`, avoid that possible edge. This
proves the asserted existence of `R`.

## 1. Four full regions are terminal

**Lemma 1.** In the theorem's setting, four pairwise disjoint nonempty
connected subsets of `W`, each contacting every vertex of `R`, give a
`Q` minor.

**Proof.** Extend the four sets to a connected partition of `W`, by
successively assigning an unassigned vertex adjacent to an assigned set
to that set. Connectedness of `W` ensures the process reaches every
vertex. Every part retains all four R contacts. The contact graph of
the four parts is connected, so three parts can be labelled to have
contacts `C_1--C_2--C_3`; call the remaining part `C_4`.

Use the seven bags

`{v,x}, {y} union C_4, {a}, {b}, C_1, C_2, C_3`.

The first two are connected and adjacent. They are full to the other
five: the first uses `v` for `a,b` and `x` for the three C parts; the
second uses `C_4` for `a,b` and `y` for those parts. The last five have
all six contacts between `{a,b}` and `{C_1,C_2,C_3}`, together with
`C_1C_2,C_2C_3`. These form a wheel with centre `C_2` and rim
`a,C_1,b,C_3`. Its double cone is `Q`. All bags are disjoint actual
connected sets, and no contact between `C_4` and another C part is used.
QED

## 2. Four-vertex deletions are nonplanar

**Lemma 2.** Under the theorem's host hypotheses, deleting any four
vertices leaves a nonplanar graph.

**Proof.** A `K_7^-` minor contains `Q`. Seven-connectivity excludes
the two cockade bases and every nontrivial four-clique sum. Jakobsen's
strict bound and integrality therefore give `2m<=9n-25`.
Put `q=m-4n`. Minimum degree eight gives `q>=0`,
`sum_z(d(z)-8)=2q`, and hence `q<=(n-25)/2` and `n>=25`.
For any four-set `S`, its degree sum is at most `32+2q`, so

`e(G-S)>=4n-32-q+e(G[S])`.

This exceeds the planar upper bound `3(n-4)-6`: their difference is
at least `n-14-q>=(n-3)/2>0`. QED

## 3. The four failures cannot coexist

**Proof of the theorem.** Put `F=G-v`, which is six-connected. Suppose
that for every `r in R`, the graph `J_r=F-(R-{r})` has no `T`-rooted
`K_4`. It is three-connected and, by Lemma 2, nonplanar. The rooted-four
alternative must therefore give an open root-free side of order at
least two with at most three neighbours in `J_r`.

Every component of this open side must contain `r`. Otherwise it lies
in `W`, has no neighbour `v`, and has at most six neighbours in `G`:
the three separator vertices and the three deleted R vertices. This
contradicts seven-connectivity, with `v` surviving outside its boundary.
Thus the open side is one connected set `D_r subseteq W union {r}`,
contains `r`, and has at least two vertices. Write
`S_r=N_{J_r}(D_r)`. Its G boundary is contained in
`{v} union (R-{r}) union S_r`. Since `|S_r|<=3`, a T root survives
outside this boundary. Seven-connectivity forces `|S_r|=3` and

`N_F(D_r)=(R-{r}) union S_r`.

The four sets `D_r` are pairwise disjoint. Indeed, let
`f(X)=|N_F(X)|=|N_F[X]|-|X|`. Closed-neighbourhood cardinality is a
coverage function, so `f` is submodular. A nonempty intersection
`D_r intersect D_s`, for distinct `r,s`, lies in `W` and has at least
seven F neighbours: it has no v contact, and seven-connectivity applies
in `G`. Their union avoids all four T roots and the other two R roots,
so six-connectivity of `F` gives at least six neighbours. Submodularity
would then give `12=f(D_r)+f(D_s)>=7+6`, a contradiction.

For each `r`, choose one component `C_r` of `D_r-{r}`. It is nonempty,
connected, and lies in `W`. Its G boundary is contained in the seven
vertices `R union S_r`: no edge joins different components of
`D_r-{r}`, and no W vertex sees `v`. Since `v` survives outside this
boundary, seven-connectivity forces equality. In particular every
`C_r` contacts every R root. The four chosen components are disjoint,
so Lemma 1 gives `Q`, a contradiction. At least one root deletion
therefore succeeds. QED

The successful model may use `r` and other vertices of `W`. This proof
does not provide a five-connected quotient after pairing its A and B
bags, establish the required quotient density, or close the remaining
two-triangle case.
