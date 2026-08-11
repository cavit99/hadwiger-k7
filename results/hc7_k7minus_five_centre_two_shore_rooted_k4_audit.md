# Internal audit: universal rooted `K_4` models on both two-cut shores

**Verdict:** **GREEN.**

**Audited source:**
[`hc7_k7minus_five_centre_two_shore_rooted_k4.md`](hc7_k7minus_five_centre_two_shore_rooted_k4.md)

**Audited source SHA-256:**

```text
f2178d7bd01b1b59a72f74a9cae9c253eac7eca87856c5c0c9f48875bb89c144
```

This is a hash-pinned internal mathematical audit, not external peer
review.  The theorem is unbounded and computation-free.

## 1. Common-matching orientation

The audited
[five-centre common-matching theorem](hc7_k7minus_five_centre_common_matching_reduction.md),
at SHA-256

```text
d0d3aa3574d747a3164f29febff1fa8fd6f37b0899415cd97a515005c5de5f43
```

supplies the asserted orientation.  In its two-cut outcome, the five
selected matching edges cross the two components of the deleted-matching
host.  For each centre `z`, the selected end `x_z` lies in one component
of `F-{p,q}` and is the unique neighbour of `z` in that component; all
seven other neighbours of `z` lie in the opposite closed shore.  The
audited two-cut theorem then orients these components as the equal-response
shore `C` and the distinct-response shore `D`.

Consequently the definition

\[
                         U=\{z\in Z:x_z\in C\}
\]

has exactly the meaning used in the source: every member of `U` has one
`C`-neighbour, namely `x_z`.  If `U` is empty, every `x_z` lies in `D` and
is the unique `D`-neighbour of its centre.  No stronger assertion about
the unselected centre contacts is used.

## 2. The distinct-response shore

The audited
[universal boundary rooted-`K_4` theorem](hc7_k7minus_five_centre_universal_boundary_rooted_k4.md),
at SHA-256

```text
0a2511508c313e06c47cf7837e823299be4dc665d0572a4a3b53fdde4a44191f
```

applies verbatim to `D`.  It proves that `G[D union Q]` contains a
`Q`-rooted `K_4` minor for every four-set `Q subseteq S`.  This part of
Theorem 2.1 does not depend on the orientation of any selected matching
edge.

## 3. Singleton shift and equality-shore density

Suppose `U` is nonempty and choose `z in U`.  The preceding orientation
gives precisely the hypothesis `|N_C(z)|=1` of the audited
[singleton-shift theorem](../active/hc7_k7minus_five_centre_singleton_shift.md),
at SHA-256

```text
6398ef32f17ba1174031b2c99fd5985b60a61b7ffcd48ccc5b2b00686fcff5c1
```

with its unique neighbour equal to `x_z`.  That theorem is stated in the
same equal/distinct response orientation and yields

\[
                         |E(G[C])|\geq 3|C|-2,
                         \qquad |C|\geq 8.
\]

The selected-neighbour provenance of `x_z` is more information than the
singleton-shift theorem requires, so there is no hidden compatibility
hypothesis here.

## 4. Relative connectivity and the obstruction theorem

For each four-set `Q subseteq S`, apply the audited
[closed-shore rooted-connectivity lemma](hc7_closed_shore_rooted_connectivity.md),
at SHA-256

```text
ba6dbfe1ca9e89041b1a77174844c24598984cbe76349a55c41f15b2e997cc03
```

with `A=C` and opposite component `R=D`.  It excludes every separation of
`J=G[C union Q]` of order at most three having all four roots on one
closed side and a nonempty root-free open side.  Ordinary
four-connectivity is neither asserted nor needed.

The published primary source was checked directly: Ruy Fabila-Monroy and
David R. Wood, *Rooted `K_4`-Minors*, *Electronic Journal of
Combinatorics* **20** (2013), P64, Theorem 15,
<https://doi.org/10.37236/3476>.  Under the contrary assumption, it gives
exactly that `J` is a spanning subgraph of a graph `J^+` in one of classes
`A`--`F`.  In every class:

1. all four nominated vertices lie in the planar base graph;
2. every vertex outside the base lies in a clique assigned to one base
   triangle; and
3. that clique has no neighbour outside itself and the assigned triangle.

If an assigned clique is nonempty, take a component `W` of its intersection
with the spanning subgraph `J`.  Then

\[
                         N_J(W)\subseteq T
\]

for its assigned triangle `T`.  All roots lie outside `W`, and

\[
       (V(J)-W,\;W\cup N_J(W))
\]

is a separation of order at most three with a nonempty root-free open
side.  This is precisely the separation excluded by the relative
connectivity lemma.  The use of a component of the intersection is
essential and correctly handles edges of `J^+` omitted from `J`.

Thus every added clique is empty and `J` is a subgraph of the planar base.
The induced subgraph `G[C]` is planar, so, since `|C|>=8`,

\[
                         |E(G[C])|\leq3|C|-6,
\]

contradicting the singleton-shift lower bound.  This proves the
equality-shore assertion for every four-set `Q`.

## 5. Exact seven-bag accounting

In the `U nonempty` alternative, choose two boundary four-sets whose
intersection is one root.  The two rooted models lie respectively in
`C` plus its four roots and `D` plus its four roots, so their only possible
common vertex is that literal root.  Merging the two bags containing it
therefore gives seven pairwise disjoint connected bags.

The merged bag is adjacent to the other six.  The three unmerged bags on
each shore form a clique, contributing all six within-shore pairs.  The
only unaccounted adjacencies are the `3 times 3=9` pairs between unmerged
bags on opposite shores.  A `K_7^-` model requires at least eight of these
nine pairs, because all other twelve pairs are already present.

Since `C` and `D` are anticomplete, every such cross-pair must be supplied
by an edge incident with literal boundary vertices, including selected or
unselected centre contacts.  The two existence theorems do not prescribe
which rooted bag contains the relevant interior endpoint.  This remains
true after making the models spanning: fullness gives an opposite-shore
neighbour to each exclusive boundary root, but that neighbour may be
absorbed into the bag merged at the common root and hence need not fill an
entry of the `3 by 3` matrix.

The source therefore identifies the first unsupported simultaneous
selection statement accurately.  It does **not** claim that compatible
models cannot exist, only that their existence is not supplied by the two
separate rooted-model theorems.  In the `U=empty` alternative, the missing
input is even earlier: no universal rooted-`K_4` theorem has been obtained
on `C`.

## 6. Trust boundary and scope

This audit accepts the GREEN, hash-pinned proofs of the common-matching
theorem, the two-cut reduction, the universal distinct-shore theorem, the
singleton-shift theorem and the closed-shore connectivity lemma.  Their
relevant source hashes were checked against the adjacent audits.  The
Fabila-Monroy--Wood classification and its six obstruction definitions
were checked in the published primary source.

No unresolved inference was found.  The theorem proves universal rooted
`K_4` supply on `D`, and on `C` whenever at least one selected matching
edge has its non-centre end in `C`.  It does not synchronize branch sets,
fill eight entries of the cross-shore adjacency matrix, eliminate the
`U=empty` orientation, produce a six-colouring, or prove a `K_7^-` minor.
