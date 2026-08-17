# A codegree-three low endpoint forces a two-root branch-set separation

**Status:** computation-free written proof with an adjacent author-side
audit.  The theorem strengthens the low-endpoint branch of the
codegree-three trichotomy.  It forces a genuine separator from every
spanning `K_6` model, but does not bound that separator above by seven.

Write `K_7^-` for `K_7` with one edge deleted.

## Theorem 1 (joint two-root split)

Let `G` satisfy

```text
kappa(G)>=7,
chi(G)=7,
every proper minor of G is six-colourable,
K_7^- is not a minor of G.
```

Suppose `vx` is an edge such that

```text
d_G(v)=8,   d_G(x)<=9,   |N_G(v) cap N_G(x)|=3.        (1)
```

Put `H=G-{v,x}`.  Then the following statements hold.

1. `d_G(x)` is eight or nine and `chi(H)=6`.
2. `H` is five-connected and has a spanning `K_6`-minor model.
3. The audited palette-permutation theorem applies to `vx`: one
   six-colouring of `G-vx` saturates all five non-pole colours at both
   ends, and `H` contains five pairwise vertex-disjoint paths between
   corresponding complete five-colour neighbour sets, up to a permutation
   of the colours.
4. Let `F_1,...,F_6` be any spanning `K_6` model in `H`.  Some branch set
   `F_h` contains distinct vertices

   ```text
   a in N_G(v) cap F_h,   b in N_G(x) cap F_h.          (2)
   ```

   Split a spanning tree of `G[F_h]` across any edge of its `a-b` path,
   obtaining nonempty connected adjacent sets

   ```text
   F_h=X_v dot_union X_x,   a in X_v,   b in X_x.      (3)
   ```

   Among the ten possible adjacencies from
   `{v} union X_v` and `{x} union X_x` to the five foreign branch sets,
   at least two are absent.  Consequently at least one of `X_v,X_x` has
   an actual external neighbourhood which separates it from a foreign
   branch set.  Every such separator has order at least seven; if its
   order is seven, every component behind it is full to all seven boundary
   vertices.

### Proof

Minimum degree eight in the audited critical host gives
`d_G(x) in {8,9}`.

We first prove that `chi(H)=6`.  Deleting two vertices lowers chromatic
number by at most two, while `H` is a proper subgraph, so

```text
5<=chi(H)<=6.
```

Suppose that `H` has a proper five-colouring.  Fix one colour.  If no
vertex of that colour is adjacent to both `v` and `x`, recolour every
vertex of that colour adjacent to `v` with a new sixth colour, give `v`
the old colour and give `x` the new colour.  The recoloured vertices are
independent, and none is adjacent to `x`; this properly six-colours `G`.
Thus every one of the five colours occurs on a common neighbour of `v,x`,
contrary to (1).  Hence `chi(H)=6`.  This also proves directly that `vx`
is not a double-critical edge.

Deleting two vertices from a seven-connected graph leaves a five-connected
graph.  The critical-host density theorem gives

```text
|E(G)|>=4|V(G)|.
```

Exact deletion accounting and `d_G(x)<=9` give

```text
|E(H)|=|E(G)|-8-d_G(x)+1
      >=4|V(H)|-8.                                    (4)
```

Norin--Totschnig, Theorem 6, supplies a `K_7^vee` minor in `H`, unless
`H` is `K_{2,2,2,2}`.  The audited degree-eight count gives
`|V(G)|>=26`, so the eight-vertex exception is impossible.  Absorbing the
deficient branch set of the `K_7^vee` model into a universal branch set
gives a `K_6` model.  Since `H` is connected, enlarge its branch sets to a
partition of `V(H)`.  This proves item 2.  The equality `chi(H)=6` and the
standing critical hypotheses are exactly the assumptions of the audited
palette-permutation linkage theorem, proving item 3.

Fix any spanning `K_6` model `F_1,...,F_6`.  Let

```text
C_v={i:N_G(v) cap F_i is nonempty},
C_x={i:N_G(x) cap F_i is nonempty}.
```

The connected set `{v,x}` together with the six branch sets would be a
`K_7^-` model if it met at least five of them.  Therefore

```text
|C_v union C_x|<=4.                                   (5)
```

Let `W=N_G(v) cap N_G(x)`, so `|W|=3`.  If two members of `W` lie in one
branch set, they give the distinct vertices in (2).  We may therefore
assume that the three vertices of `W` lie in three distinct common-contact
branch sets.

Suppose no common-contact branch set contains distinct vertices as in
(2).  In each such branch set the nonempty `v`- and `x`-neighbourhoods
must then be the same singleton.  Consequently the three branch sets
containing `W` are the only common-contact branch sets, and their three
portals are precisely the vertices of `W`.

Take the six-colouring of `G-vx` from the palette theorem, with common pole
colour `alpha`.  The three vertices of `W` use at most three of the five
other colours.  Choose a colour `beta` absent from `W`.  Palette saturation
gives a `beta`-coloured neighbour of `v` and a `beta`-coloured neighbour of
`x` in `H`.  They cannot lie in one branch set, since that would be another
common-contact branch set with distinct pole neighbours.  They therefore
lie in distinct exclusive branch sets.  Together with the three common
branch sets, these make `|C_v union C_x|>=5`, contradicting (5).  This
proves (2).

Now take any rooted split (3).  Use the seven connected branch sets

```text
{v} union X_v,   {x} union X_x,   F_i (i ne h).        (6)
```

The first two are adjacent through `vx`, and the five foreign branch sets
are pairwise adjacent.  Thus the only possibly absent pairs in (6) are
the ten pole-piece--foreign-set pairs.  If at most one were absent, (6)
would be a `K_7^-` model.  Target exclusion proves that at least two are
absent.

In particular one of the two pieces, say `Y`, is anticomplete to some
foreign branch set `F_j` even after its pole is adjoined.  Hence `Y` itself
is anticomplete to `F_j`.  The set `Y` is connected and `F_j` lies outside
`Y union N_G(Y)`, so `N_G(Y)` is an actual vertex separator.
Seven-connectivity gives `|N_G(Y)|>=7`.  If equality holds and a component
of `G-N_G(Y)` misses one boundary vertex, its neighbourhood has order at
most six and separates it from the component containing `F_j`.  This is
impossible.  Every component is therefore full to the seven-vertex
boundary. `\square`

## Corollary 2 (strengthened low-endpoint alternative)

In outcome 2 of the codegree-three trichotomy, every spanning `K_6` model
of `G-{v,x}` contains a branch set whose two-root split produces an actual
separator as in Theorem 1.  Thus the branch does not stop at a static
`K_7^vee` contact pattern: it always enters the host's separation
structure.

The remaining issue is exact.  The proof gives no upper bound on
`|N_G(Y)|`.  An order-seven output is a full exact seven-boundary interface;
an output of larger order still requires a density, colouring or
minimality argument before it is terminal.

## Adversarial scope checks

The known static quotient `HN~~zpx` has two adjacent roots with coincident
four-branch-set contacts and no `K_7^-` minor.  It does not refute Theorem
1: its connectivity is four, and the rooted split exposes the separator
alternative rather than eliminating it.

The two-apex icosahedral example from the ordinary `K_7`-minor contact
theory also does not refute the theorem.  Its two apex vertices have twelve
common neighbours, not three, and the graph is not a critical host under
the displayed hypotheses.  These checks show why both the exact codegree
and the proper-minor palette are used.

## Frozen inputs and scope

```text
2b0c30b9d8566f6da4959df145bf0f527249bf887dfa844d19a98e524080a9f2
  results/hc7_adjacent_pair_palette_linkage.md
6bce1f570c12a93a7d1830f53905cb1e033bd2e40abed948a70a21ce5100c03d
  results/hc7_atomic_two_pole_contact_trichotomy.md
6ffee04cf9ff66275f9674c24bc2b9c669b1e108b76e5b1d2a18ec7d0106fe67
  results/hc7_k7minus_degree7_rooted_helper_closure.md
891f937237eff6eb3dd1a111ea6a68611c4b5d3ee7b4c2b4ef0465ff684b0b3e
  active/hc7_k7minus_critical_degree_eight_codegree_three_dichotomy.md
```

The proof uses the first source for the edge-deletion palette and five-path
linkage.  The branch-set split is reproved with the stronger `K_7^-`
contact count, rather than inferred from the ordinary `K_7` statement in
the second source.  The last two sources supply the critical-host density,
order and the entrance into the low-endpoint branch.

The external density-to-model input is S. Norin and A. Totschnig,
*Every graph with no `K_7^vee`-minor is 6-colorable*, Theorem 6,
arXiv:2507.03244.
