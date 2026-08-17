# A codegree-three or excess-eighteen dichotomy

**Status:** written proof with a computer-assisted finite lemma and an
adjacent author-side audit.  The theorem gives a new global trichotomy in a
hypothetical critical host.  It does not eliminate the low-endpoint branch
or the `tau>=18` branch.

Write `K_7^-` for `K_7` with one edge deleted and put

```text
c(xy)=|N_G(x) cap N_G(y)|.
```

Thus `c(xy)` is the number of triangles containing the edge `xy`.

## Lemma 1 (the two-universal-vertex census)

Let `J` be a graph on eight vertices satisfying

```text
delta(J)>=3,   K_6^- is not a minor of J,
K_4 is not a subgraph of J,   alpha(J)=3.
```

Form `Q(J)` by adding two nonadjacent vertices, each complete to `J`.  If
`Q(J)` has no `K_7^-` minor, then at least four vertices of `J` have degree
three.

Up to isomorphism, exactly `56` graphs `J` satisfy these hypotheses and
have target-free `Q(J)`.  Their numbers of degree-three vertices have the
distribution

```text
number of degree-three vertices       4   5   6   7   8
number of graphs                       8  13  25   6   4.       (1)
```

### Verification

The retained verifier generates every unlabelled graph of order eight by
extending the complete graph-atlas list of order seven and then taking
isomorphism representatives.  It obtains `27,529` minimum-degree-three
extensions, `2,590` representatives and `542` graphs satisfying the four
local hypotheses.  An exact contraction--deletion search for `K_7^-`
leaves `56` two-universal-vertex quotients and verifies (1).

The script pins explicit models for all `486` positive quotients, the full
negative classification and their degree sequences.  Run

```text
UV_CACHE_DIR=/tmp/uv-cache uv run python \
  active/experiments/sevenconnected_full_exterior_profiles/verify.py
```

The exact verifier revision is recorded under **Frozen inputs** below.

## Theorem 2 (low codegree, low endpoint or large excess)

Let `G` satisfy

```text
kappa(G)>=7,
chi(G)=7,
every proper minor of G is six-colourable,
K_7^- is not a minor of G.
```

For `i>=8`, let `n_i` be the number of degree-`i` vertices and put

```text
tau=sum_{i>=10}(i-9)n_i.
```

Then at least one of the following holds.

1. Some degree-eight vertex `v` has a neighbour `x` with `c(vx)<=2`.
2. Some degree-eight vertex `v` has a neighbour `x` with
   `c(vx)=3` and `d_G(x)<=9`.
3. `tau>=18`.

### Proof

Suppose that the first two conclusions fail.  The audited critical-host
results give

```text
delta(G)>=8,
G has no literal K_5,
alpha(G[N_G(v)])=3 for every degree-eight vertex v,
n_8>=26+tau.                                           (2)
```

In particular, `|V(G)|>=26`.  Fix a degree-eight vertex `v` and write
`J=G[N_G(v)]`.  Since conclusion 1 fails, `delta(J)>=3`.  The absence of a
literal `K_5` makes `J` `K_4`-free, and target exclusion prevents a
`K_6^-` minor in `J`.

The exterior `G-N_G[v]` is nonempty because `|V(G)|>=26`.  The audited
full-exterior reduction shows that it is connected and its unique component
`C` has a neighbour at every vertex of `J`.  Contract `C` to one vertex.
Together with `v` and `J`, the resulting minor is exactly `Q(J)` from
Lemma 1.  It remains target-free, so at least four vertices `x in J` have
`d_J(x)=3`.  For each such vertex,

```text
c(vx)=d_J(x)=3.
```

Conclusion 2 fails, so all four have degree at least ten in `G`.

Let `B` be the set of degree-eight vertices and count ordered pairs `(v,x)`
such that `v in B`, `vx` is an edge, `c(vx)=3` and `d_G(x)>=10`.  Call the
number of pairs `I`.  The preceding paragraph, applied at every member of
`B`, gives

```text
4n_8 <= I.                                             (3)
```

A vertex of degree `i>=10` is the second entry of at most `i` such pairs.
If `h=sum_{i>=10}n_i`, then `h<=tau`, and hence

```text
I <= sum_{i>=10} i n_i = 9h+tau <=10tau.              (4)
```

Combining (2)--(4) yields

```text
4(26+tau) <=10tau.
```

Thus `6tau>=104`, and integrality gives `tau>=18`. `\square`

## Corollary 3 (exact full-exterior residue)

In the proof of Theorem 2, `27` of the `56` possible local graphs admit a
four-set `T subseteq V(J)` with the following property.  For every possible
missing edge of a `T`-rooted `K_4^-` model, completing the other five pairs
of `T` in `J+v` gives a `K_7^-` minor.  Consequently those `27` profiles
cannot occur when `G[C union T]` contains the corresponding `T`-rooted
model.

Exactly `29` graph6 codes resist every completion of this form:

```text
GhCKN{ GhEJC{ GhEJE{ GjSKLK GjSKNK GjSKL[ GjSKN[ GhdM@k GxaGis Gpq_is
GhEM`W GhEMdW GhEMbW GhEM`w GhEMdw GlO[PK GMs`KK GMs`Kk GhEMLo GhEMNo
GhEMJw GhEMNw GlgGiK GlgGik GhMIMc GhEK~_ GhEKzW GhEK~c GhEJ]o.
```

### Proof

The same exact verifier tests all seventy choices of `T` in every one of
the `56` profiles and every nonedge that may remain in the rooted
`K_4^-`.  It pins explicit `K_7^-` models for one canonical completion of
each eliminated profile and checks the displayed residue.  A rooted model
in the exterior realizes the tested edge additions by contraction.  If its
missing pair was already an edge of `J[T]`, the result is only stronger.
`\square`

## Proposition 4 (what the low-endpoint branch supplies)

Suppose outcome 2 of Theorem 2 holds, and let `H=G-{v,x}`.  Then
`d_G(x)` is eight or nine, `H` is five-connected, and `H` has a spanning
`K_7^vee` minor model, where `K_7^vee` is `K_7` with two incident edges
deleted.  It may be labelled

```text
P,B,C,U_1,U_2,U_3,U_4,
```

with only `PB` and `PC` nonadjacent.  For each retained root
`r in {v,x}`:

1. `r` meets at most four of `B,C,U_1,U_2,U_3,U_4`;
2. if `r` meets `P`, it meets neither `B` nor `C`; and
3. the two roots do not both meet all of `P,U_1,U_2,U_3,U_4`.

### Proof

The critical-host density theorem gives

```text
|E(G)|>=4|V(G)|.
```

Since `vx` is an edge and `d_G(v)=8`, exact deletion accounting gives

```text
|E(H)|=|E(G)|-8-d_G(x)+1
      >=4|V(G)|-16
       =4|V(H)|-8.                                    (5)
```

Deleting two vertices from a seven-connected graph leaves a five-connected
graph.  Norin--Totschnig, Theorem 6, now gives a `K_7^vee` minor unless
`H` is `K_{2,2,2,2}`.  The latter has order eight, whereas (2) gives
`|V(H)|>=24`.  Enlarge the seven branch sets to a partition of `V(H)`.
Target exclusion ensures that the two nominally absent adjacencies remain
absent.

If a root met five of the six pairwise adjacent bags, adjoining its
singleton would give a `K_7^-` model.  If it met both `P` and `B`, absorb
the root into `P`; only the adjacency to `C` could then be absent.  The same
argument applies with `B,C` interchanged.  Finally, if both roots met
`P,U_1,U_2,U_3,U_4`, those five bags and the two adjacent singleton roots
would give a `K_7` model.  This proves the three restrictions. `\square`

## The pair-deletion alignment does not close statically

Proposition 4 extends the spanning-near-clique gateway from two
degree-eight roots to the `(8,9)` endpoint case.  It does not produce a new
terminal class.  The following exact quotient isolates the obstruction.

Start with the seven labelled vertices of `K_7^vee`, add adjacent roots
`v,x`, and make both roots adjacent precisely to

```text
B,C,U_1,U_2.
```

The resulting nine-vertex graph has graph6 code `HN~~zpx` and no
`K_7^-` minor.  It obeys all three contact restrictions in Proposition 4.
Moreover the following multiplicities inside the four contacted branch
sets are arithmetically compatible with the exact root data:

```text
bag             B   C   U_1   U_2
common          1   1    1     0
v-only          0   0    2     2
x-only          0   0    2   2 or 3.
```

Thus the table gives `v` seven neighbours in `H`, `x` seven or eight, and
exactly three vertices adjacent to both.  After restoring `vx`, these are
numerically the degree pairs `(8,8)` or `(8,9)` and codegree three.  The
exact verifier is

```text
active/experiments/pair_deletion_low_endpoint_interface/verify.py.
```

This is a route nonclosure, not a counterexample to Proposition 4 or to the
critical-host conjecture: the quotient has connectivity four and the
multiplicity display is not itself a host graph.  It proves that degrees,
codegree and static branch-set contacts do not force the missing alignment.
The available next step is only the existing branch-set transfer and its
nested-separator normal form; closing this branch requires a genuinely
joint two-root transfer or further use of the five-connectivity inside the
uncontracted branch sets.

## Frozen inputs and exact scope

The proofs use the following revisions:

```text
993278e07663ee5cd10df67917037ff784a743e4b3806813b6ddd8ad0c1e46a3
  active/experiments/sevenconnected_full_exterior_profiles/verify.py
c7cb794dd0298b1cbe98ac4ee1bdbbf04f1e5c546ae26f195fcbb034602b0c0d
  active/hc7_k7minus_critical_degree_eight_full_exterior_reduction.md
2ffeb857f4c999abc14bc28cd4650332d9397a140c601929117376f38f637449
  results/hc7_k7minus_degree_eight_triangle_poor_edge_packing.md
6ffee04cf9ff66275f9674c24bc2b9c669b1e108b76e5b1d2a18ec7d0106fe67
  results/hc7_k7minus_degree7_rooted_helper_closure.md
fc1e88c28b1f4d0dc7a1cbdeefa19fecfd5e969b986c64e11eb1990615f5dfbd
  results/hc7_k7minus_exceptional_neighbourhood_completion.md
2421f7b00b263ad3ee5f4f747252d7bee23f6ff7bdfd73247033ff2012f2fb76
  active/experiments/pair_deletion_low_endpoint_interface/verify.py
7541a7f0f20ad1f407acd9158cfef5f76eb48d39ea528e57d943c1d1fec8b17e
  active/hc7_k7minus_pair_deletion_k7vee_reduction.md
```

The first script is a computer-assisted finite result, not an unbounded
enumeration.  Theorem 2 is unbounded because the audited full-exterior
theorem reduces every degree-eight centre to one of those finite quotients
before Lemma 1 is invoked.  The theorem does not prove that outcome 1 must
hold: it leaves the explicitly stated low-endpoint and `tau>=18` branches.

The external density-to-model input in Proposition 4 is S. Norin and
A. Totschnig, *Every graph with no `K_7^vee`-minor is 6-colorable*,
Theorem 6, arXiv:2507.03244.
