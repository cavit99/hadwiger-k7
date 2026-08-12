# Singleton-coordinate localisation at a lifted six-cut

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_six_cut_coordinate_localisation_audit.md).
This note sharpens the six-connected case of the
[six-coordinate induced-forest reduction](hc7_k7minus_six_coordinate_forest_reduction.md).
It does not prove the `K_7^-` six-colour conjecture or `HC_7`.

## 1. Abstract lifted-cut setting

Let `G` be a seven-connected graph such that

\[
 \chi(G)=7,\qquad
 \chi(J)\leq6\text{ for every proper minor }J\text{ of }G,
 \qquad K_7^-\npreccurlyeq G.                       \tag{1.1}
\]

Let `F` be a componentwise-induced forest and put `X=G-F`.  Assume that
every nonempty `J subseteq F` is the exact monochromatic-edge signature of
a proper six-colouring `c_J` of `X`.

Suppose

\[
             V(G)=A\mathbin{\dot\cup}T\mathbin{\dot\cup}B,
             \qquad A,B\ne\varnothing,\qquad E_G(A,B)=\varnothing. \tag{1.2}
\]

Assume that there are two forest edges

\[
             e_A=u_Av_A,\qquad e_B=u_Bv_B             \tag{1.3}
\]

with `u_A in A`, `u_B in B` and `v_A,v_B in T`.  The edges need not be
distinctly oriented in `F`; what matters is that one singleton signature
has its restored defect entering each open side.

For `Y subseteq V(G)`, write `Pi_Y(c)` for the equality partition induced
by `c` on `Y`.

### Theorem 1.1 (coordinate localisation)

For `W in {A,B}`, take the corresponding edge `e_W=u_Wv_W`, and let
`K_W` be the component of `G[W]` containing `u_W`.  Put

\[
                              Q_W=N_G(K_W).             \tag{1.4}
\]

Then:

1. `Q_W subseteq T` and `7<=|Q_W|<=|T|`;
2. `c_{\{e_W\}}` restricts to a proper six-colouring of `G-K_W`;
3. the partition `Pi_{Q_W}(c_{\{e_W\}})` does not extend through
   `G[K_W union Q_W]`.

Consequently either one of `Q_A,Q_B` is a strict response-bearing
separator of order between seven and `|T|-1`, retaining the specified
singleton-signature exterior colouring, or `K_A,K_B` are two anticomplete
connected subgraphs full to `T`.

In the latter case:

4. `G[T]` has no `K_5` minor and is four-colourable;
5. the extension languages of the aggregate closed sides `G[A union T]`
   and `G[B union T]` each meet every exact-block cylinder on `T`;
6. `G[T]` is nonsplit.

#### Proof

Every neighbour of a component of `G[A]` lies in `A union T`, and there is
no edge from that component to another component of `G[A]`.  Hence
`Q_A subseteq T`; the argument for `Q_B` is symmetric.  The opposite open
side is nonempty, so each `Q_W` is an actual separator.  Seven-connectivity
gives `|Q_W|>=7`, proving item 1.

The colouring `c_{\{e_W\}}` is proper on `X`, and after restoring `F` its
only monochromatic edge is `e_W`.  Deleting `K_W` removes the endpoint
`u_W` and therefore removes that sole defect.  This proves item 2.  If the
induced partition on `Q_W` extended through the intact `K_W`-side, a
permutation of colour names would align the two colourings on `Q_W`.
They would then glue to a proper six-colouring of `G`, contrary to (1.1).
This proves item 3 and the first alternative.

Suppose now that `Q_A=Q_B=T`.  The two displayed components are connected,
anticomplete and full to `T`.  A `K_5`-minor model in `G[T]`, together
with `K_A,K_B`, would give seven branch sets with the sole possible missing
adjacency between `K_A` and `K_B`.  This is a `K_7^-` model.  Thus `G[T]`
has no `K_5` minor, and the established case `HC_5` makes it
four-colourable.  This proves item 4.

Let `I` be any nonempty independent set of `G[T]`.  Contract the connected
set `K_B union I` and six-colour the resulting proper minor.  Expand the
contraction colour over `I` and restrict the colouring to `G[A union T]`.
Every vertex of `T-I` is adjacent to `K_B`, so the contraction colour
occurs on `T` exactly at `I`.  Thus the `A`-side extension language meets
the exact-block cylinder indexed by `I`.  Contracting `K_A union I` proves
the symmetric statement for the `B`-side.

The two aggregate extension languages are disjoint, since a common
boundary partition would align and glue across the anticomplete sets
`A,B`.  Item 4 gives `chi(G[T])<=4=6-2`.  The audited
[split-boundary synchronisation theorem](hc7_split_boundary_synchronization.md)
therefore says that `G[T]` cannot be split.  This proves items 5--6.
`\square`

## 2. Application to the six-coordinate lifts

### Corollary 2.1 (all crossing allocations)

Theorem 1.1 applies to every separator in Theorems 2.1 and 3.1 of the
[complementary-cube lift](hc7_k7minus_six_cut_complementary_cube_lift.md).
More precisely:

1. in the matching case, choose one edge from each nonempty part
   `E_C,E_D` of the crossing matching;
2. in the induced-path case, choose one edge of `E_0` for the `C'`-side
   and either one of `rx,ry` for the `D'`-side.

Thus every displayed complementary-cube separator either has a strict
singleton-coordinate localisation, or its boundary is nonsplit and
`K_5`-minor-free and it has a full coordinate-bearing component on each
side.

#### Proof

In the matching construction, an edge in `E_C` has its `C`-end in `C'`
and its other end in `T`; an edge in `E_D` has its `D`-end in `D'` and its
other end in `T`.  Both sets are nonempty.  These are (1.3).

In the induced-path construction, every edge of `E_0` has its `C`-end in
`C'` and its selected `D`-end in `T`.  Both leaves `x,y` remain in `D'`,
whereas their common neighbour `r` lies in `T`.  Hence `rx` or `ry`
supplies the opposite orientation.  Apply Theorem 1.1. `\square`

The strict localisation retains one fixed forest-coordinate response.  It
does not automatically remain inside a previously chosen minimum-side or
model-labelled comparison class.  That distinction is essential: this is
a genuine smaller separator, but not yet a terminal recursive descent.

## 3. Large boundaries and fresh response descent

### Corollary 3.1 (orders at least ten)

In the full-component outcome of Corollary 2.1, if `|T|>=10`, there is a
vertex `v in A union B` such that

\[
                         7\le d_G(v)<|T|.              \tag{3.1}
\]

Its neighbourhood is the boundary of a strict singleton-side separation.
For every edge `vx`, a six-colouring of `G-vx` gives an exterior-realised,
intact-singleton-side-rejected boundary partition on `N_G(v)`.

Consequently a residue admitting neither a coordinate-preserving strict
localisation nor a fresh strict response has only the following crossing
counts:

\[
\begin{array}{c|c|c}
\text{forest type}&\text{crossing count}&|T|\\ \hline
6K_2&q=3&9,\\
4K_2\mathbin{\dot\cup}P_3&k\in\{1,2\}&8\text{ or }9.
\end{array}                                           \tag{3.2}
\]

#### Proof

Theorem 1.1 gives `K_5 not preccurlyeq G[T]`.  Apply the audited
[large-boundary singleton-response theorem](hc7_large_boundary_singleton_response_descent.md)
to the decomposition (1.2).  Its hypotheses hold because `K_7^-`-minor
exclusion implies `K_7`-minor exclusion.  The theorem gives (3.1) and the
stated edge-deletion response.

In the matching lift, `|T|=6+q` and the present range has `q>=3`; avoiding
order at least ten leaves `q=3`.  In the induced-path lift,
`|T|=7+k`; avoiding order at least ten leaves `k=1,2`. `\square`

The response in Corollary 3.1 is deliberately called fresh.  Its deleted
edge need not be a member of the six-coordinate forest, so it cannot be
substituted silently for the coordinate-preserving outcome of Theorem 1.1.

## 4. Component count after all strict responses are excluded

### Lemma 4.1 (financing one common partition)

Suppose every component of `G-T` is full to `T`, and let their number be
`r`.  If `G[T]` has a proper equality partition into `k` independent
blocks and

\[
                              r\ge k+1,                \tag{4.1}
\]

then `G` is six-colourable.

#### Proof

Fix a component `C` of `G-T`.  Assign the `k` boundary blocks injectively
to `k` other components.  For each block `I`, contract the connected set
formed by `I` and its assigned component.  The `k` contraction images are
pairwise adjacent: each assigned component is full to every vertex in
every other block.  Six-colour this proper minor and pull the colouring
back to `G[C union T]`.  The equality partition induced on `T` is exactly
the prescribed partition.

Repeat for every component `C`.  After permuting colour names, all these
closed-component colourings agree on `T`.  Components of `G-T` are
pairwise anticomplete, so the colourings glue to a six-colouring of `G`.
`\square`

### Theorem 4.2 (only two or three full components survive)

Assume `|T|>=6`, every component of `G-T` is full to `T`, and there are at
least two components.  Then a graph satisfying (1.1) has exactly two or
three components of `G-T`.  If there are three, then

\[
                              \chi(G[T])\in\{3,4\}.     \tag{4.2}
\]

#### Proof

Two full components and a `K_5` model in `G[T]` would form a `K_7^-`
model, so `chi(G[T])<=4` by `HC_5`.

If `r>=5`, use an optimal boundary partition with `k<=4` in Lemma 4.1.
This six-colours `G`, a contradiction.

Suppose `r=4`.  If three boundary vertices span at least two edges, choose
three further distinct boundary vertices, absorb one into each of three
full components, retain the fourth component, and retain the original
three vertices as singleton bags.  These seven connected bags have every
adjacency except possibly one among the three singleton bags, and hence
form a `K_7^-` model.  Therefore every three vertices of `T` span at most
one edge.  It follows that `Delta(G[T])<=1`, so `G[T]` is a matching and is
two-colourable.  Lemma 4.1 again six-colours `G`.

Thus `r` is two or three.  When `r=3`, a one- or two-colouring of `G[T]`
would satisfy Lemma 4.1, proving (4.2). `\square`

### Corollary 4.3 (exact no-descent residue)

In Corollary 2.1, either some component `K` of `G-T` has

\[
                    7\le |N_G(K)|<|T|,                \tag{4.3}
\]

and a six-colouring of the proper minor `G-K` gives a rejected boundary
partition on `N_G(K)`, or all components are full to `T`.  If all strict
responses, including Corollary 3.1, are excluded, then `|T|` is eight or
nine and `G-T` has exactly two or three full components.  In the
three-component case the boundary is three- or four-chromatic.

#### Proof

For any component `K` of `G-T`, its neighbourhood is contained in `T` and
has order at least seven.  If it is not all of `T`, (4.3) holds.  A proper
six-colouring of `G-K` cannot induce a boundary partition extending through
the intact `K`-side, since the two colourings would glue to colour `G`.
If every component is full, apply Theorem 4.2, and apply Corollary 3.1 to
exclude boundary order at least ten. `\square`

## 5. Exact remaining obstruction

The proof has reduced the complementary-cube residue to a sharp choice.
A strict coordinate-labelled separator is available immediately unless a
coordinate-bearing component is full.  Refusing fresh response descent as
well leaves only boundaries of order eight or nine with two or three full
components.  The common partition in Lemma 4.1 eliminates four or more
components, but it does not eliminate three components when the boundary
requires three or four colours.

The adjacent-pair shortcut for that last case is false even at order eight.
The separate
[three-component boundary barrier](../barriers/hc7_k7minus_three_full_component_partition_barrier.md)
uses `2K_3 dotcup 2K_1`.  Thus the next positive theorem must use the
literal singleton-coordinate colourings or the two seven-connected
restorations; component fullness, target exclusion and boundary
colourability alone have reached their exact limit.

## Dependencies and scope

The nontrivial imported inputs are the audited complementary-cube lift,
the split-boundary synchronisation theorem, the large-boundary
singleton-response theorem, and the established case `HC_5`.  All other
arguments are elementary contractions and gluing.

The result is unbounded in the sizes of the open shores.  No finite
enumeration is used.
