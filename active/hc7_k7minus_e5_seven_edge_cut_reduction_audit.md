# Audit: seven-edge five-cut reduction

**Verdict:** GREEN for the stated reduction.

**Audited source:**
`active/hc7_k7minus_e5_seven_edge_cut_reduction.md`

**SHA-256:**
`a0f26f2c57a00f7e4d238bf68a4f2d824e3c90f100f47ebe2697e6be42f73461`

This is an internal mathematical audit, not external peer review.  The
source does not prove `(E5)`: one exact seven-edge boundary row remains.

## 1. Setting and dependencies

For a two-component five-cut with seven boundary edges, direct accounting
gives

```text
delta_S(C)+delta_S(D)=q+6.
```

The source chooses `C` with minimum order among every component behind a
five-cut having excess at least `q+4`.  Consequently every strictly smaller
such component has excess at most `q+3`.  All uses of minimality respect
this global choice.

The audited internal dependencies are pinned at:

```text
dense five-cut reductions       81306114489449f1bd2d8521c4aefc216411f81bf6721c7763412d4a7a87c6c0
eight-edge descent              afe8754937317dcd47b40d2ee2e3e921ea8e22fd5a309c7b6601b289d76a309e
four-component elimination     c2709e5a1b69cc0ce205d5b79bfdeb9e14790b0c30997137bf8cdf416d521c6c
K_{2,3} (3,3,1) elimination    33ff2125cafdfdc75b28e3a4ae7d24e4299e6e77cec946d674b7f2875a6e15c1
```

In particular, the proof legitimately uses: no five-component cut; no
four-component cut; a three-component cut has triangle-free boundary; an
eight-edge boundary has two independent missing edges; and the displayed
`K_{2,3}` equality row is impossible.

## 2. Star and triangle complements

For a missing three-edge star, one full connected opposite component can
realise all missing edges by absorption into the centre.  Completing the
five boundary bags therefore gives an actual proper minor, not merely an
abstract augmented graph.

For a missing triangle, let `H` be the high closed side with its boundary
completed.  Deleting any one added triangle edge leaves two added edges
with a common end, so the opposite component realises them simultaneously.
Each deleted graph is thus an actual dense proper minor and cannot be
five-connected.  Mader's critical-cycle theorem applies to the three
critical edges in the five-connected graph `H` and gives a boundary vertex
with one neighbour `p` in `C`.

After replacing that vertex by `p`, every new inside component is full to
the new five-set.  The boundary triangle excludes two such components;
the established four- and five-component results exclude the next two
counts; six full components give the displayed `K_7^-` quotient.  Hence
the inside is connected.  Deleting the old boundary vertex removes exactly
three edges, and the identity

```text
delta_Q(C-p)=delta_S(C)+8-|E(G[Q])|
```

is correct.  Complete and `K_5^-` five-boundaries are unavailable, so the
new excess is at least the old excess, contradicting global minimality.

## 3. Path complement

Adding either adjacent pair of missing path edges gives a dense actual
proper minor with boundary `K_5^-`.  A separator of order at most four must
contain the other three boundary vertices and one vertex of `C`; this
gives the two stated one-vertex obstructions.

The rooted Two Paths application is at the correct four roots.  In its
disc outcome the closed graph without `t` has

```text
4|C|+delta_S(C)-p_t+3 <= 3(|C|+4)-6,
```

and `p_t<=|C|`, so `delta_S(C)<=3`.  The path outcome makes the two
obstruction vertices distinct.  Five-connectivity then gives exactly the
neighbourhoods used in the proof, and each deletion leaves a connected
inside.  A two-vertex `C` has excess at most three, so the residual `R` is
nonempty.

In each of the three non-crossed orientations, deleting the two missed
boundary vertices removes exactly six old-side edges.  Since the new
boundary has at most eight edges, its excess increases.  The sole crossed
orientation removes seven edges and gives

```text
sum delta_Q(R_i)=delta_S(C)+8-|E(G[Q])|.
```

If `q>0`, edge-minimality makes every edge connectivity-critical.  Mader's
theorem on the literal triangle `adt` gives `a` or `d` degree five; replacing
it by its unique `C`-neighbour produces a smaller high-excess component
behind a boundary with at most seven edges.  Thus `q=0`.

In the crossed residue, disconnectedness gives exactly two inside
components.  Triangle-freeness and Mantel's theorem force

```text
G[Q]=K_{2,3},   (delta_Q(R_1),delta_Q(R_2),delta_Q(O))=(3,3,1).
```

The pinned independent theorem eliminates exactly this row.  Hence the
entire path-complement case is closed.

## 4. Disjoint star-and-edge complement

Realising `ab,ac` through the opposite component leaves a `K_5-de`
boundary.  Its non-five-connectivity gives the separator `{a,b,c,p}`.
Every component of `C-p` has one of the two displayed five-neighbour sets.

The proof that both types occur is necessary and valid.  If, for example,
no component meets `e`, then `e` has the unique `C`-neighbour `p`.
Replacing `e` by `p` leaves a boundary containing `bcd`, hence a connected
new inside.  The boundary has at most seven edges, and deleting `e` removes
exactly four old-side edges, so the new excess is at least
`delta_S(C)`.  This contradicts minimality.  The symmetric argument handles
`d`.  Two components of one type would give a three-component cut with a
boundary triangle.  Thus there is exactly one component `A` and one `B`.

The edge decomposition is exact:

```text
alpha+beta=delta_S(C)+4-d_S(p).
```

The two new boundaries contain four fixed edges.  Eight boundary edges
would leave the adjacent missing pair `ab,ac`, so both boundaries have at
most seven edges.

If `q>0`, the critical triangle `bcd` contains a degree-five vertex.
Vertices `b,c` each see both `A,B`, three boundary neighbours, and `D`, so
their degrees are at least six.  Therefore `d` has degree five and a unique
neighbour in `C`.  The recentering at that neighbour gives the same strict
order contradiction as recorded in the source.  Hence `q=0`.

If `p` sees both `d,e`, the seven displayed branch sets are connected and
pairwise adjacent except possibly for `B,D`; this is an explicit
`K_7^-` model.  Thus `p` sees at most one of them.  Combining this with the
two seven-edge boundary inequalities gives `d_S(p)<=3`.  The three exact
numerical rows then follow directly from `alpha,beta<=3` and the global
excess identity.

Finally, disjoint connected subgraphs `T,P` inside `D` with the stated root
contacts really do complete the five boundary branch sets: absorb `T` into
the `a`-bag and split a minimal `d`--`e` subtree of `P` between those two
root bags.  The latter also works when the subtree is one vertex.  The
completed high closed side would be a dense, five-connected, proper minor.
Therefore such supports cannot exist.

## 5. Exact nonclosure and literature scope

The surviving assertion is not ordinary two--three linkage.  Ordinary
feasibility allows one of `b,c` to be an internal terminal of the
three-root tree, whereas the minor construction needs one connected
interior subgraph adjacent to all of `a,b,c`.  Xie's official dissertation
states ordinary feasibility for six-connected graphs and records a stronger
tripod-type property as part of Conjecture 7.0.2.  Neither statement closes
this five-cut side.  The source therefore stops at the correct first
unsupported inference rather than promoting the rooted-support condition
to a theorem.

Before promotion beyond `active/`, the Two Paths citation should be given
with its exact primary theorem identifier.  This is a bibliographic task,
not a mathematical gap in the reduction.
