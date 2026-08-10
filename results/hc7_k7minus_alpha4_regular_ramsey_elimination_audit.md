# Independent audit: independence-four exceptional-centre elimination

**Verdict:** GREEN.

**Audited theorem:**
[`hc7_k7minus_alpha4_regular_ramsey_elimination.md`](hc7_k7minus_alpha4_regular_ramsey_elimination.md)

**Audited theorem SHA-256:**

```text
90d47de90eebeec12c806d3e33dff74f56bdabcfcf448a46453bd3eadfb954f6
```

After this verdict, the opening status was changed to link this audit and a
bibliographic citation was added for `R(4,5)=25`; neither change alters the
audited mathematics.  The promoted theorem SHA-256 is

```text
8838868b67a46aa611ee3f7c3a2b522c7ba559e5bc320d4ff1b0284bce8988de
```

**Audited verifier:**
[`hc7_k7minus_alpha4_regular_ramsey_elimination_verify.py`](hc7_k7minus_alpha4_regular_ramsey_elimination_verify.py)

**Audited verifier SHA-256:**

```text
f85b1787b46a5052f92731c2b88911b030c0813e54bb238d66f6c8ad95a635b5
```

This is a separate internal mathematical and computational audit, not
external peer review.  No unresolved mathematical or encoding gap was
found.

## 1. Audit of the host reduction

Let `B` be the degree-eight vertices and assume `alpha(G[B])=4`.  For a
maximum independent set `U` of order four, every vertex of `B-U` has a
nonempty `U`-neighbourhood.  If `A_u` denotes the vertices whose unique
`U`-neighbour is `u`, then `A_u` is a clique: two nonadjacent members,
together with `U-{u}`, would be an independent five-set.  Since
`{u} union A_u` is also a clique and the host has no literal `K_5`,
`|A_u|<=3`.  Hence `a=sum |A_u|<=12`.

Writing `b=|B|`, the four vertices of `U` have at most 32 incident edges in
total.  Every nonsingleton mask contributes at least two incidences, so

```text
32 >= a + 2((b-4)-a) = 2b-8-a.
```

Thus `a>=2b-40`; together with `b>=25` and `a<=12`, this gives
`25<=b<=26`.

The step from `B` to the whole host is valid and essential.  Since
`alpha(G[B])=4`, one has `chi(G[B])>=ceil(b/4)=7`.  If `B` were proper,
deleting `V(G)-B` would make `G[B]` a proper minor, contrary to the
six-colourability of every proper minor.  Therefore `B=V(G)` and `G` is
8-regular.  If `b=26`, then `G-v` has 25 vertices, while each class in any
six-colouring has order at most four; six classes cover at most 24
vertices.  Hence `b=25`.

This justifies the exact degree equations used in the finite calculation;
the computation is not incorrectly applying equality to an arbitrary
25-vertex subset of `B`.

## 2. Independent incidence enumeration

For the 21 vertices outside `U`, let `n_S` count the nonempty masks
`S subseteq U`.  The four centre degrees give

```text
sum_S n_S = 21,             sum_{S containing u_i} n_S = 8.
```

The singleton bounds are `0<=n_{u_i}<=3`.  I independently enumerated the
vectors using a different parametrization from the verifier.  The total
incidence excess over one per outside vertex is

```text
32-21=11.
```

I enumerated only the six doubleton, four triple and one four-element mask
counts with weighted excess respectively `1`, `2`, and `3`.  Their four
coordinate loads then determine the singleton counts uniquely as
`8-load_i`; retaining precisely the values in `[0,3]` gives 505 vectors.
Canonicalization under all 24 permutations of `U` gives 40 orbits.  The
canonical orbit text independently reproduced

```text
8841a5f22d526efdc5b24c889dc40b6d01ea57b186ecca664435756ccd308f31.
```

Thus the enumeration is exhaustive and the `S_4` quotient loses no
labelled case.

## 3. CNF encoding audit

For each orbit representative, the fixed centre incidences and the six
centre-centre nonedges leave exactly `binom(21,2)=210` unknown edge
variables.  The encoding has the following exact semantics.

1. For an outside vertex with mask `S`, the formula requires exactly
   `8-|S|` incident outside edges.  The prefix variable at position `i`
   and threshold `j` is constrained equivalently to “at least `j` of the
   first `i` literals are true”: the `and` and `or` gates are encoded in
   both directions.  Requiring threshold `k` and forbidding threshold
   `k+1` is therefore an exact-`k` constraint.
2. For each five-set, a fixed nonedge makes the nonclique condition
   automatic; otherwise the formula inserts the disjunction of the
   negated unknown edges.  A fixed edge similarly makes the
   non-independent condition automatic; otherwise it inserts the
   disjunction of the positive unknown edges.  If every pair is fixed with
   the forbidden value, the resulting empty clause correctly makes that
   case unsatisfiable.
3. The four centre degrees are already exactly eight by the mask equations,
   while every outside degree is exactly eight by item 1.  Items 2 and 3
   exclude precisely `K_5` and independent five-sets.  Conversely, the
   outside-edge assignment of any graph satisfying the finite theorem
   extends uniquely at the semantic level to the prefix thresholds and
   satisfies the CNF.

The 40 deterministic formulas all have 6,492 variables and between 62,925
and 63,055 clauses.  Their ordered digest corpus independently regenerated
as

```text
a34b94ffa30e693806a83b32bdbacff036c8c091fa7f03e84835530d1a3bc48a.
```

## 4. Independent certificate replay

I reran the pinned verifier in full with CaDiCaL 3.0.1 and `drat-trim` at
commit

```text
2e3b2dc0ecf938addbd779d42877b6ed69d9a985
```

using a checker binary of SHA-256

```text
f58f63b0f76945d4c4c9ff6e87afaf870f579e67c0f7cca589492df8fc7ebd47.
```

The independent run returned

```text
incidence_vectors=505 orbits=40
orbit_sha256=8841a5f22d526efdc5b24c889dc40b6d01ea57b186ecca664435756ccd308f31
cnf_corpus_sha256=a34b94ffa30e693806a83b32bdbacff036c8c091fa7f03e84835530d1a3bc48a
cnf_variables=6492..6492 cnf_clauses=62925..63055
UNSAT_cases=40/40 DRAT_verified=40/40 generated_proof_bytes=283582854
```

CaDiCaL is used only as the proof producer.  Every binary DRAT refutation
was accepted by the separate `drat-trim` checker.  The proofs were generated
in temporary storage and removed after checking; retaining roughly 284 MB
of reproducible proof data in Git is not necessary for replay and would
conflict with the repository rule against generated bulk data.

## 5. Consequence and scope

The finite result therefore eliminates `alpha(G[B])=4` in the critical
host.  Symmetry of the established equality `R(4,5)=R(5,4)=25`, together
with the absence of a literal `K_5`, first gives `alpha(G[B])>=4`; the
elimination upgrades this to at least five independent degree-eight
centres.

This is terminal for the independence-four branch, not for the full
conjecture.  The rooted-model and exact-separator outcomes arising from five
independent centres still require treatment.
