# Literal near-clique exclusion under connected-set contractions

**Status:** written proof; a separate internal audit is recorded at the exact
source hash in the adjacent audit. The global six-colouring conjectures remain open.

Write `Q=K_7^=` for `K_7` with two independent edges deleted. All graphs
are finite and simple. We use
[the five-connected rooted-helper closure, Theorem 2](hc7_five_connected_helper_closure.md#3-the-closure-theorem):
if a five-connected graph `F` has a vertex `z` of degree `d` whose
neighbourhood contains `K_4^-`, and `e(F)>=4|V(F)|+d-13`, then `F`
contains a `Q` minor. Its proof and external input are recorded there;
the deduction below introduces no additional literature input.

## 1. Every edge has a literal-exclusion-preserving quotient

**Theorem 1 (written proof).** Let `G` be six-connected,
`delta(G)>=8`, and `Q`-minor-free. For every edge `uv`, the simple quotient
`G/uv` contains no `K_5^-` subgraph. Consequently `G` itself contains no
`K_5^-` subgraph.

**Proof.** Put `n=|V(G)|`, `e(G)=4n+q`, where `q>=0`, and
`c=|N_G(u) intersect N_G(v)|`. Write `w` for the contracted vertex and
`F=G/uv`. Then

```text
|V(F)|=n-1,     e(F)=e(G)-1-c,
e(F)-4|V(F)|=q+3-c.
```

The quotient is five-connected. Indeed a cut of at most four vertices
avoiding `w` lifts unchanged to a cut of `G`, and one containing `w`
lifts by replacing `w` with `u,v`, still using at most five vertices.
It is also `Q`-minor-free: replace `w` in its unique owning branch set
by the connected pair `{u,v}` to lift any proposed minor. Finally every
unmerged vertex loses at most one neighbour, while
`d_F(w)=| (N_G(u) union N_G(v)) minus {u,v} |>=7`.
Thus `delta(F)>=7`.

Suppose five vertices of `F` span `K_5^-`. Three of them contact all
four others. Choose two such vertices `x,y` different from `w`.
Their neighbourhoods contain `K_4^-`. The contrapositive of the cited
helper theorem, including integrality, gives

```text
d_F(x), d_F(y) >= (e(F)-4|V(F)|)+14 = q+17-c.
```

The four original vertices `u,v,x,y` are distinct. Their degrees in `G`
satisfy `d_G(u),d_G(v)>=c+1` and `d_G(x)>=d_F(x)`,
`d_G(y)>=d_F(y)`. Therefore

```text
d_G(u)+d_G(v)+d_G(x)+d_G(y) >= 2q+36.
```

These four vertices contribute at least `2q+4` to
`sum_z (d_G(z)-8)=2q`. Every other summand is nonnegative, a contradiction.

For completeness, the original literal exclusion follows directly from
the same helper theorem: three universal vertices of a `K_5^-` subgraph
would each have degree at least `q+14`, contributing at least
`3(q+6)>2q` to the same degree sum. QED

There is no bound on `c`, endpoint degrees, graph order or excess `q`.
No colouring or contraction-critical hypothesis is used.

## 2. Exact information retained by the quotient

**Proposition 2 (written proof).** Under Theorem 1, every unmerged
degree-seven vertex of `F` was a degree-eight common neighbour of `u,v`
in `G`. These vertices induce a matching and isolated vertices. The
merged vertex has degree seven exactly when
`d_G(u)=d_G(v)=8` and `c=7`.

**Proof.** Only common neighbours lose a neighbour, and the loss is one.
If three vertices in `N_G(u) intersect N_G(v)` span two edges, those
three vertices together with `u,v` span `K_5^-`: they have six contacts
to `u,v`, the edge `uv`, and the two indicated edges. Theorem 1's original
literal exclusion forbids this. Hence the common-neighbour graph has
maximum degree at most one. The assertion about `w` follows because its
neighbourhood is the union of two sets, each of size at least seven;
their union has size seven exactly when both sets coincide and have
size seven. QED

**Recorded route nonclosure.** The quotient need not remain six-connected
or have minimum degree eight. It is not asserted to retain chromatic
criticality or any original branch-set roots at `u,v`. Hence Theorem 1
does not authorize iteration on arbitrary returned quotients. Host order
decreases by one and minor lifting is valid, but closure of an induction
class remains unproved.

## 3. A contact restriction beside a literal four-clique

**Corollary 3 (written proof).** Under Theorem 1, let `R` span a `K_4`
and put `J=G-R`. Every vertex of `J` has at most two neighbours in `R`.
For an edge `ux` of `J`, if `x` has two neighbours in `R`, then
`N_G(u) intersect R` is contained in `N_G(x) intersect R`.

In particular, if `R={v,a,b,c}`, no edge `ux` of `J` has
`u in N_G(v)` and `|N_G(x) intersect {a,b,c}|>=2`.
This includes the degree-eight case without requiring that degree bound
at the particular clique vertex `v`.

**Proof.** Three contacts from an outside vertex to the four-clique give
a literal `K_5^-`, already excluded. If the asserted containment fails,
choose `v in (N_G(u) intersect R) minus N_G(x)` and contract `vu`.
The four-clique remains a four-clique, with its `v` vertex replaced by
the merged vertex. The vertex `x` now meets that merged vertex and its
two old neighbours in `R`, giving a `K_5^-` subgraph of `G/vu`.
This contradicts Theorem 1. All other clique vertices are untouched;
no simultaneous reuse of a branch set occurs. QED

## 4. A certificate for contracting an arbitrary connected set

**Proposition 4 (written proof).** Under the hypotheses of Theorem 1, let
`C` be a nonempty connected vertex set such that the simple quotient
`F=G/C` is five-connected. Put

```text
b=|N_G(C)|,
D=sum_{z in N_G(C)} (|N_G(z) intersect C|-1).
```

Here `N_G(C)` is the open neighbourhood outside `C`. If `D<=b+3`, then
`F` contains no `K_5^-` subgraph.

**Proof.** Put `k=|C|`, `m_C=e(G[C])` and `e(G)=4n+q` as before. If `w`
is the contracted vertex, then

```text
|V(F)|=n-k+1,
e(F)=e(G)-m_C-D,
q_F=e(F)-4|V(F)|=q+4(k-1)-m_C-D.
```

The quotient remains `Q`-minor-free, using the connected set `C` as the
fixed preimage of `w`. Suppose it contains a `K_5^-` subgraph, and choose
two universal vertices `x,y` different from `w`. Five-connectivity permits
the helper theorem, which gives `d_G(x),d_G(y)>=q_F+14`.

The number of edges from `C` to its complement is `b+D`, so
`sum_{z in C} d_G(z)=2m_C+b+D`. Consequently the distinct original vertices
in `C union {x,y}` contribute at least

```text
(2m_C+b+D-8k) + 2(q_F+6) = 2q+4+b-D
```

to `sum_z(d_G(z)-8)=2q`. All remaining contributions are nonnegative.
The hypothesis makes this lower bound strictly greater than `2q`, a
contradiction. The minor lift uses disjoint fixed preimages and makes no
claim to preserve multiple prescribed roots inside `C`. QED

**Corollary 5 (written proof).** The conclusion of Proposition 4 holds
whenever every outside vertex has at most two neighbours in `C`, provided
`G/C` is five-connected. It also holds for every triangle `C` whose quotient
is five-connected.

**Proof.** In the first case each summand in `D` is at most one, so
`D<=b`. For a triangle let `n_i` count outside vertices with exactly `i`
neighbours in it. There is at most one vertex with three such neighbours:
two of them together with the triangle would span `K_5^-` in `G`.
Hence `b-D=n_1-n_3>=-1`, so again `D<=b+3`. QED

## 5. Automatic closure for every connected three-set

**Corollary 6 (written proof).** Let `G` be seven-connected,
`delta(G)>=8`, and `Q`-minor-free. For every connected nonempty set `C`
with `|C|<=3`, the simple quotient `G/C` contains no `K_5^-` subgraph.

**Proof.** First `G` contains no `K_{1,2,3}` subgraph. Contract an edge
between its parts of orders two and three: the six-vertex subgraph
becomes a five-vertex `K_5^-`, whose sole missing edge
joins the two uncontracted vertices of the part of order three. This
contradicts Theorem 1; extra edges do not affect this argument.

Suppose `|C|=3`, and choose a vertex of `C` adjacent to its other two
vertices. Three outside vertices adjacent to all of `C` would, together
with these three vertices, contain `K_{1,2,3}`: its parts are the chosen
centre, the other two vertices of `C`, and the three outside vertices.
Thus, writing `n_i` for the number of outside vertices with exactly `i`
neighbours in `C`, we have `n_3<=2`. Consequently

`D-b=n_3-n_1<=2`.

The quotient is five-connected. A cut of at most four vertices avoiding
the merged vertex lifts unchanged, and one containing it lifts by
replacing that vertex with the three vertices of `C`, giving at most six
vertices in `G`. Proposition 4 now applies. The cases `|C|=1,2` are
Theorem 1. QED

The connectivity of the returned quotient remains an explicit hypothesis
for larger sets in Proposition 4. Nor does the multiplicity inequality
preserve minimum degree eight or chromatic criticality. These are
contraction certificates, not a closed induction.
