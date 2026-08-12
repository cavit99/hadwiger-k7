# Internal audit: dominated-singleton saturated five-root reduction

## Verdict

**GREEN.**  The proof in
[`hc7_k7minus_dominated_singleton_rooted_five_reduction.md`](hc7_k7minus_dominated_singleton_rooted_five_reduction.md),
source SHA-256
`c7a8ae5457fef4925aaed616889a8aaab6fc6db92f5798c4a2af1387e96f0433`,
correctly proves the five-chromatic saturated-set reduction and the two
rooted-model completions.  Its discussion of the unrooted inputs is also
correctly scoped as a route nonclosure, not as a counterexample or a proof
of the missing rooted theorem.

## 1. Colour-class deletion

Let `c` be a proper six-colouring of `G-uv` with `c(u)=c(v)=0`, and let
`Gamma=c^{-1}(0)`.  Since `uv` is the sole deleted edge, `Gamma` is
independent in `G-uv`, and the only edge of `G[Gamma]` is `uv`.  In
particular:

- `Gamma-{u}` is independent;
- `u` has no neighbour in `Gamma-{u,v}`; and
- `Q=N_G(u)-{v}` is disjoint from `Gamma` and hence is a subset of
  `K=G-Gamma`.

If `K` were four-colourable, four colours on `K`, a fifth colour on
`Gamma-{u}` and a sixth colour on `u` would properly colour `G`.  The edge
`uv` is proper because `v` receives the fifth colour.  Thus `chi(K)>=5`.
The fixed colouring `c` restricted to `K` uses at most the five colours
different from `0`, so `chi(K)=5`.

## 2. Universal saturation, not one-colouring saturation

The source correctly starts with an arbitrary proper five-colouring of
`K`.  If one colour is absent from `Q`, it assigns that colour to `u` and
one fresh sixth colour to every vertex of `Gamma-{u}`, including `v`.
This is proper because:

- all neighbours of `u` other than `v` lie in `Q`;
- `Gamma-{u}` is independent; and
- `u` and `v` receive different colours.

Hence the argument applies to every five-colouring of `K`; it does not
reuse or assume uniqueness of the original colouring `c`.

The definitions are consistent:

\[
 K=G-\Gamma=(G-\{u,v\})-(\Gamma-\{u,v\})
            =H-(\Gamma-\{u,v\}).
\]

Thus `K` is precisely the common-colour-free induced subgraph of the
five-connected graph `H=G-{u,v}`.

## 3. Minor-model completions

Every vertex of `Q` is adjacent to both `u` and `v`, and `uv` is an edge.
Therefore five pairwise adjacent branch sets each meeting `Q`, together
with the singleton bags `{u},{v}`, give a `K_7` model.  If the five rooted
bags have at most one missing adjacency, the same seven bags give a
`K_7^-` model.  Items 3 and 4 of Theorem 2.1 follow exactly.

The target-free conclusion is conditional: a hypothetical target-free host
would yield a five-chromatic saturated pair `(K,Q)` without a `Q`-rooted
`K_5` model.  The source does not claim that such a host exists, nor does it
claim an unconditional counterexample to Holroyd's conjecture.

## 4. Five-connectivity and the direct inputs

Deleting `u,v` from a seven-connected graph leaves `H` five-connected.
A four-colouring of `H` extends with two fresh colours on the adjacent
vertices `u,v`, so `chi(H)>=5`; the Four-Colour Theorem then makes `H`
nonplanar.  Kelmans--Seymour supplies an unrooted subdivision of `K_5`, and
the Dominating 4-Colour Theorem supplies an unrooted dominating `K_5`
model.  Neither result says that every branch set meets `Q`.

The universal five-terminal theorem supplies a rooted
`F_5=K_1\vee P_4` model.  Its guaranteed seven edges are two short of the
nine edges of `K_5^-`.  The source now explicitly allows additional actual
bag adjacencies; it says only that the universal theorem does not guarantee
the two repairs.

## 5. Trust boundary

The exact proved gain is the saturated-set reduction and its terminal
rooted-model criterion.  The following remain unproved:

- the order-five case of Holroyd's conjecture;
- a `Q`-rooted `K_5^-` model in the five-connected graph `H`;
- a clean five-root linkage into the branch vertices of an arbitrary
  Kelmans--Seymour subdivision; and
- a conversion of the fixed exact model or the second edge response into
  such a rooted model.

The existing double-saturation barrier lacks the present
seven-connectivity, contraction-criticality and dominated common-neighbour
structure.  The source correctly uses it only to rule out an inference from
colour saturation alone.
