# Eliminating degree-five nonroots in the stronger-helper construction

**Status:** written proof with a separate hash-pinned internal audit.
This degree restriction is an input to the stronger helper construction,
not a standalone completion of that theorem, Conjecture 21, HC7, or the
requested theorem of comparable significance to Norin–Totschnig.

## Setting and retained inputs

Let `(G,X)` be a lexicographically minimum counterexample, by
`(|V(G)|,|E(G)|)`, to the stronger helper target `P`: five prescribed-root
bags and two disjoint root-free helper bags, all connected and nonempty,
with at least ten of the eleven helper–root and helper–helper contacts.
The graph is finite and simple, `|X|=5`, and

```text
rho4(G)=e(G)-e(G[X])-4|V(G)-X|.
```

For a root-free set `Y`, its fragment density counts all edges with at
least one endpoint in `Y`, minus `4|Y|`. A graph is 4-light when this is
nonpositive whenever `|N(Y)|<=4`.

Use the proved restrictions from the
[degree and connectivity reduction](hc7_c21_rooted_density_low_degree_reduction.md):
`X` is independent; `rho4(G)=2`; `(G,X)` is internally five-connected;
every root has degree at least two; every nonroot has degree at least five
and at most three root neighbours; no proper root five-separation has
right-side density at least two; and no adjacent degree-five nonroots
have exactly three common neighbours. These inputs are not reproved here.

Complete `X` to a clique and call the resulting graph `Q`. It is
five-connected: after deletion of at most four vertices the surviving
roots form one nonempty clique; another component would be a nonempty
root-free set with boundary at most four in `G`. Root-free boundaries and
fragment densities are the same in `G` and `Q`.

## 1. A local contraction fact

A graph is **quasi five-connected** if it is four-connected and has no
four-separation whose two open sides both have at least two vertices.

**Lemma.** Let `Q` be five-connected. Let `A` have five external
neighbours `S`, with `|A|>=3` and `|V(Q)-(A union S)|>=2`. If `x in S`
has exactly one neighbour `a` in `A`, then `Q/xa` is quasi five-connected.

This is the local assertion established by the proof of Kou, Qin, Yang,
Zhang and Zhao, [Lemma 1, arXiv:2509.25809v1](https://arxiv.org/html/2509.25809v1#S2).
Their stated lemma assumes global contraction criticality. The following
local form uses only the hypothetical cut obstructing `xa`; no atom or
minimal-fragment assumption is needed. The primary proof and definitions
were inspected on 21 September 2026.

**Proof.** Contraction in a five-connected graph preserves
four-connectivity. A nontrivial four-cut in `Q/xa` would lift to a five-cut
`T` containing `x,a`, with open sides `B,D` of orders at least two.
Write `C=V(Q)-(A union S)` and

```text
p=|A intersect T|, r=|C intersect T|, s=|S intersect T|,
u=|S intersect B|, w=|S intersect D|.
p+r+s=u+w+s=5,  s>=1.
```

If `A intersect B` is nonempty, its corner boundary omits `x`, so
`p+s+u>=6`. Hence `p>w`, `u>r`, and `C intersect D` is empty.
Symmetrically, `A intersect D` nonempty implies `p>u`, `w>r`, and
`C intersect B` empty.

If both A-corners are nonempty, `|C|=r>=2` and
`u+w>=2r+2>=6>5-s`, impossible. If neither is nonempty, `p=|A|>=3`
and `r<=1`; assume `C intersect B` nonempty. Its corner bound gives
`u>=p`, hence `w<=1` and `C intersect D` empty, contradicting `|D|>=2`.
If only `A intersect B` is nonempty, then `D=S intersect D`, so `w>=2`.
Now `p>w` gives `r<=1`, while the corner boundary of `C intersect B`
has order `r+s+u=5+r-w<=4`. Thus that corner is empty, leaving
`|C|=r<=1`. Every case is impossible. QED

## 2. Quasi connectivity is enough for rooted lightness

**Lemma.** Suppose `u,v` are nonroots and `Q/uv` is quasi five-connected.
Then `(G/uv,X)` is 4-light.

**Proof.** Write `J=Q/uv` and `H=G/uv`. Their root-free boundaries and
fragment densities agree. Every original root has degree at least five
in `J`: its at least two nonroot neighbours in `G` merge to at least one,
and it also has the four other roots as neighbours.

Let `Y` be a nonempty root-free set with boundary of order at most four.
All five roots lie outside `Y`, so at least one vertex lies outside its
closed side. Four-connectivity of `J` therefore forces boundary order
exactly four. Quasi five-connectivity now forces one open side to be a
singleton. If `Y` is a singleton, its degree is four and its fragment
density is zero. If the opposite open side is a singleton, it must be an
original root: all five roots lie outside `Y`, and only four vertices
are in the boundary. That root would have degree at most four in `J`, a
contradiction. These cases exhaust all fragments, proving lightness. QED

## 3. Removing a degree-five vertex and adding one edge

**Theorem.** Every nonroot of the minimum counterexample has degree at
least six.

**Proof.** Suppose a nonroot `v` has degree five. First assume `Q[N(v)]`
is not complete. Choose a nonedge `ab` of that graph. It is also a
nonedge of `G`, and its ends cannot both be original roots. Set

```text
H0=G-v,  H=H0+ab.
rho4(H0)=1,  rho4(H)=2.
```

The graph `H` is a rooted minor of `G`: contract `va` and delete the
unwanted newly created edges, retaining `ab`. Its fixed nontrivial
preimage is `{v,a}`, which contains at most one original root.
Thus if `H` were 4-light, minimality would give `P(H,X)` and lifting
those bags would give `P(G,X)`. All five roots and bag ownership survive.

Suppose instead that a nonempty root-free `Y` violates lightness in `H`.
Let `k=e_G(v,Y)`, and let `c` be one if the added edge `ab` is incident
with `Y`, zero otherwise. Its original boundary satisfies

```text
N_G(Y) subseteq N_H(Y) union {v},
rho4(G,Y)=rho4(H,Y)+k-c.
```

Internal five-connectivity gives `|N_G(Y)|=5` and `k>=1`. The resulting
root five-separation is proper: its boundary contains the nonroot `v`,
so it cannot contain all five original roots. The retained density bound
therefore gives

```text
1 >= rho4(G,Y) = rho4(H,Y)+k-c >= 1+k-c.
```

Consequently `rho4(H,Y)=rho4(G,Y)=k=c=1`. Exactly one of `a,b` lies in
`Y`; rename so it is `a`. Then `a` is a nonroot and

```text
N_G(v) intersect Y={a},
N_G(Y)=S union {v},  |S|=4,  b in S,
rho4(H0,Y)=0.
```

The assertion `b in S` follows because removing `v` leaves four original
boundary vertices; adding `ab` cannot introduce a fifth boundary vertex
of `H`. If `|Y|=1`, membership `b in S` would assert the missing edge
`ab`, impossible. If `|Y|=2`, minimum nonroot degree five and density one
force its two vertices to be adjacent, both of degree five, and to have
three common neighbours. This is excluded by the retained input. Thus
`|Y|>=3`.

The opposite open side of this five-separation has at least two vertices
in `Q`. Otherwise it is one original root `z`; the boundary is then
`(X-{z}) union {v}`. Independence of `X` would give `deg_G(z)<=1`,
contrary to its degree at least two.

Apply Section 1 to `A=Y`, `x=v`, and its unique neighbour `a`. It gives
quasi five-connectivity of `Q/va`. Since both `v,a` are nonroots,
Section 2 gives 4-lightness of `G/va`. Moreover `v` has degree five and
its neighbour `b` is not adjacent to `a`, so `v,a` have at most three
common neighbours. Completing the roots does not change this count,
because both ends are nonroots. Therefore

```text
rho4(G/va)=rho4(G)+3-|N_G(v) intersect N_G(a)| >= 2.
```

This is a smaller admissible five-rooted graph. Minimality gives its
`P` model, and replacing the contracted vertex by `{v,a}` lifts that
model with disjoint root-free helper bags. This contradiction settles
the noncomplete-neighbourhood case.

It remains that `Q[N(v)]` is a clique on five vertices. Internal
five-connectivity and Menger's theorem give five disjoint paths from
`X` to `N(v)` with interiors outside `N[v]`. For precision, use the root
separation `(V(G)-{v},N[v])`: an isolator of order at most four would
have the nonroot `v` on its open far side, contrary to internal
five-connectivity. Truncate a maximum root linkage at its first entry
to `N[v]`; every entry is in `N(v)`. Original roots already in `N(v)`
have trivial linkage paths.

Choose `z in N(v)-X`, possible because `v` has at most three root
neighbours. Keep `{v}` and `{z}` as the two helpers. For the root whose
linkage path ends at `z`, remove the final vertex `z` and keep the
remaining path as its root bag; this path is nonempty because `z` is
not an original root. Keep the other four linkage paths as root bags.
All seven bags are connected, disjoint and have their proper ownership.

The helper `z` contacts the four other root bags through their ends in
`N(v)`, since all edges from the nonroot `z` in the completed clique
are actual edges of `G`. It contacts the trimmed root bag through the
last edge of its linkage path. The helper `v` contacts the other four
root bags and the helper `z`. Only its contact with the trimmed root
bag may be absent. This is `P(G,X)`, the final contradiction. QED

## Scope

Both reductions strictly decrease vertex count and retain all five
original roots. No quotient is assumed contraction-critical. The original
root clique is used only to prove connectivity properties; every edge in
the final model is an actual original edge or has its specified rooted
minor preimage. The result rules out degree-five nonroots of arbitrary
ambient order, including arbitrary-sized density-one sides blocking the
one-edge deletion operation. This source does not handle degree six and
above; subsequent steps of the stronger helper construction require
separate proofs.
