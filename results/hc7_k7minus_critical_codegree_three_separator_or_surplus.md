# A critical codegree-three edge forces a two-root separator

**Status:** proved; two independent cold audits are GREEN.  This theorem
removes the degree bound on the second endpoint from the preceding
low-endpoint split theorem.  It gives a global separator-or-positive-surplus
dichotomy for every hypothetical critical counterexample, but it does not
eliminate either outcome.

Write `K_7^-` for `K_7` with one edge deleted.

## Theorem 1 (degree-free codegree-three/four split)

Let `G` satisfy

```text
kappa(G)>=7,
chi(G)=7,
every proper minor of G is six-colourable,
K_7^- is not a minor of G.
```

Let `vx` be an edge with

```text
3<=|N_G(v) cap N_G(x)|<=4.                            (1)
```

Put `H=G-{v,x}`.  Then:

1. `chi(H)=6`, and `H` is five-connected;
2. `H` has a spanning `K_6`-minor model;
3. the palette-permutation theorem applies to `vx`: a six-colouring of
   `G-vx` saturates the five non-pole colours at both ends, and `H`
   contains five pairwise vertex-disjoint paths between corresponding
   five-colour neighbour sets, up to a permutation of the colours; and
4. in every spanning `K_6` model `F_1,...,F_6` of `H`, some branch set
   `F_h` contains distinct vertices

   ```text
   a in N_G(v) cap F_h,   b in N_G(x) cap F_h.          (2)
   ```

For any partition

```text
F_h=X_v dot_union X_x                                    (3)
```

into nonempty connected adjacent sets with `a in X_v` and `b in X_x`, at
least two of the ten possible adjacencies from

```text
{v} union X_v,   {x} union X_x
```

to the five foreign branch sets are absent.  Consequently at least one
of `X_v,X_x`, say `X_p`, has the property that the pole-piece
`{p} union X_p` is anticomplete to a foreign branch set.  Both

```text
N_G(X_p)   and   N_G({p} union X_p)                     (4)
```

are actual separators.  The first contains `p`, and the second contains
the other pole.  In particular, one of the two separators contains the
specified endpoint `v`.  Every displayed separator has order at least
seven; if its order is seven, every component behind it is full to all
seven boundary vertices.

### Proof

Deleting two vertices lowers chromatic number by at most two, while `H`
is a proper subgraph.  Hence

```text
5<=chi(H)<=6.                                           (5)
```

Suppose that `H` has a proper five-colouring.  Fix one colour.  If no
vertex of that colour is adjacent to both `v` and `x`, recolour every
vertex of that colour adjacent to `v` with a new sixth colour, give `v`
the old colour, and give `x` the new colour.  The recoloured vertices are
independent and none is adjacent to `x`, so this is a proper six-colouring
of `G`.  Therefore each of the five colours occurs on a common neighbour
of `v,x`, contradicting (1).  Thus `chi(H)=6`.

Deleting two vertices from a seven-connected graph leaves a
five-connected graph.  The proved `t=6` case of Hadwiger's conjecture now
gives a `K_6` minor in `H`.  Since `H` is connected, successively absorb
every unused component into an adjacent branch set.  This makes the model
spanning.  Notice that no density hypothesis and no bound on `d_G(x)` is
used here.

The equality `chi(H)=6`, together with the standing critical hypotheses,
is exactly the input of the audited palette-permutation theorem.  It gives
the colouring and the five disjoint paths in item 3.

Fix a spanning `K_6` model `F_1,...,F_6` and put

```text
C_v={i:N_G(v) cap F_i is nonempty},
C_x={i:N_G(x) cap F_i is nonempty}.
```

The connected set `{v,x}`, together with the six branch sets, would be a
`K_7^-` model if it met at least five of them.  Hence

```text
|C_v union C_x|<=4.                                    (6)
```

Let `W=N_G(v) cap N_G(x)`.  If two vertices of `W` lie in one branch set,
they give (2).  We may therefore assume that the members of `W` lie in
distinct common-contact branch sets.

Suppose that no common-contact branch set contains distinct pole
neighbours.  In each of these common branch sets the nonempty `v`- and
`x`-neighbourhoods are then the same singleton.  Those three or four
singletons are precisely the vertices of `W`.

Take the six-colouring of `G-vx` supplied by the palette theorem, and call
the common pole colour `alpha`.  The vertices of `W` use at most four of
the five other colours.  Choose a colour `beta` absent from `W`.
Palette saturation supplies a `beta`-coloured neighbour of each pole in
`H`.  They cannot occupy the same branch set: such a branch set would be
a further common-contact set containing distinct pole neighbours.  Nor can
either lie in one of the three old common-contact branch sets, for it would
be distinct from that set's common singleton.  Thus the two neighbours lie
in distinct exclusive branch sets.  Together with the common branch sets
they give

```text
|C_v union C_x|>=|W|+2>=5,
```

contrary to (6).  This proves (2).

Take a spanning tree of `G[F_h]` and delete any edge of its `a-b` path.
The two resulting vertex sets give a partition (3).  Consider the seven
connected branch sets

```text
{v} union X_v,   {x} union X_x,   F_i  (i ne h).       (7)
```

The first two are adjacent through `vx`, and the five foreign branch sets
are pairwise adjacent.  The only possibly absent pairs in (7) are the ten
pole-piece--foreign-set pairs.  If at most one were absent, (7) would be a
`K_7^-` model.  Target exclusion therefore forces at least two absences.
In particular, one of the two pieces, say `X_p`, is anticomplete to a
foreign branch set even after its corresponding pole `p` is adjoined.

Both `X_p` and `{p} union X_p` are connected and anticomplete to that
foreign branch set.  Their external neighbourhoods are therefore actual
separators.  The pole `p` belongs to `N_G(X_p)` because `X_p` contains its
nominated pole-neighbour.  The other pole belongs to
`N_G({p} union X_p)` through the edge `vx`.  Thus one of these two
separators contains `v`, regardless of which pole-piece contact was absent.

Seven-connectivity gives order at least seven for both separators.  If one
has order seven and a component behind it misses a boundary vertex, that
component has a separating neighbourhood of order at most six.  This is
impossible.  Hence equality forces every component to be full. `\square`

## Theorem 2 (critical separator-or-surplus dichotomy)

Let `G` be minor-minimal subject to being non-six-colourable and having no
`K_7^-` minor.  Then one of the following holds.

1. There is an edge `vx` with `d_G(v)=8` and
   `|N_G(v) cap N_G(x)|<=2`.  The contraction `Q=G/vx` is
   six-connected, exactly six-chromatic and target-free, and

   ```text
   |E(Q)|>=4|V(Q)|+1.                                  (8)
   ```

   If `w` is the contracted vertex and `T=N_G(v)-{x}`, then every proper
   six-colouring of `Q` gives `w` one colour and uses all other five
   colours on the seven-set `T`.

2. There is an edge `vx` satisfying (1), and every spanning `K_6` model
   of `G-{v,x}` has a branch-set split producing an actual separator as in
   Theorem 1.  The separator can be chosen to contain the degree-eight
   endpoint `v`; it has order at least seven and is full when its order is
   seven.

### Proof

The audited critical-host theorems give

```text
kappa(G)>=7,   delta(G)>=8,   chi(G)=7,
|E(G)|>=4|V(G)|,
```

and a degree-eight vertex `v`.  The generic six-connected degree-eight
theorem supplies an incident edge `vx` having at most three common
neighbours.

If the codegree is three, Theorem 1 gives outcome 2.  Suppose it is at most
two and contract `vx`.  Edge contraction lowers vertex connectivity by at
most one, so `Q` is six-connected; it is target-free because it is a minor
of `G`.  With `c=|N_G(v) cap N_G(x)|`, exact contraction accounting gives

```text
|E(Q)|=|E(G)|-1-c
      >=4|V(G)|-3
       =4|V(Q)|+1,
```

which is (8).  Proper-minor minimality makes `Q` six-colourable.  If it had
a five-colouring, split its contracted vertex into `v,x`, give both the old
colour, and give `v` a new sixth colour.  This would six-colour `G`.
Therefore `chi(Q)=6`.

Finally, expand any six-colouring of `Q` to a colouring of `G-vx` in which
both ends receive the colour of `w`.  No member of `T` has that colour.  If
one of the other five colours were absent from `T`, recolouring `v` with
that colour would properly six-colour `G`.  Hence all five occur on `T`.
`\square`

## Why the degree bound mattered before, and why it does not here

The earlier low-endpoint theorem used `d_G(x)<=9` only to show

```text
|E(G-{v,x})|>=4|V(G-{v,x})|-8
```

and then invoked Norin--Totschnig's extremal theorem to obtain an unrooted
near-clique model.  Once `chi(G-{v,x})=6` is established, the known
`t=6` case of Hadwiger gives the exact `K_6` model directly.  Every later
palette, contact and branch-splitting argument is independent of
`d_G(x)`.

The conclusion is nevertheless not terminal.  Although the returned
separator can always be chosen to contain the degree-eight endpoint `v`,
the argument does not bound its order above by seven.  Outcome 1 leaves the
still-open positive-surplus six-connected extremal problem.  These are the
two exact remaining interfaces.

## Frozen repository inputs and external source

```text
2b0c30b9d8566f6da4959df145bf0f527249bf887dfa844d19a98e524080a9f2
  results/hc7_adjacent_pair_palette_linkage.md
06d35e4059848517e65e48b04c592e948bbc8e4407501de75520cfa3e9d22844
  results/hc7_k7minus_sixconnected_degree_eight_low_codegree.md
6ffee04cf9ff66275f9674c24bc2b9c669b1e108b76e5b1d2a18ec7d0106fe67
  results/hc7_k7minus_degree7_rooted_helper_closure.md
f0e129b30bb9f1c0d8cf8257b39bb70cbc573d15e7231de90c52de62aa33ad79
  active/hc7_k7minus_low_endpoint_joint_two_root_split.md
```

The first input supplies the palette and five-path theorem.  The next two
supply the generic low-codegree edge and the critical-host density and
degree facts.  The last source is the independently audited bounded-endpoint
version whose argument is strengthened here.

The external input is the proved `t=6` case of Hadwiger's conjecture:
N. Robertson, P. Seymour and R. Thomas, *Hadwiger's conjecture for
`K_6`-free graphs*, Combinatorica **13** (1993), 279--361,
<https://doi.org/10.1007/BF01202354>.
