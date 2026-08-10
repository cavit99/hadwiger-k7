# Internal audit of the order-six equality-shore elimination

**Verdict:** **GREEN.**

**Audited theorem:**
[`hc7_k7minus_order_six_equality_shore_elimination.md`](hc7_k7minus_order_six_equality_shore_elimination.md)

**Audited theorem SHA-256:**
`96e7b99fda8c2e4584066fd3855f412072a4d6513962cf05e4e842f62e0a7983`

**Audited verifier:**
[`hc7_k7minus_order_six_equality_shore_elimination_verify.py`](hc7_k7minus_order_six_equality_shore_elimination_verify.py)

**Audited verifier SHA-256:**
`54c95f5bf5a5440129547e3242774851fa7286a2b4450c694d3d2a2c8cd7fee9`

This is a separate internal mathematical and computational audit, not
external peer review.

The mathematical proof and finite reduction were frozen and audited at
SHA-256
`1769b6e5059578593325acf3b50cf68924436c009fdc4658d8b22e650079bb87`.
The promoted revision pinned above changes only the status paragraph and
the two reproduction paths from `active/` to `results/`.  That exact diff
was inspected; the theorem statement, proof, finite encoding description,
hashes, and scope are unchanged.

## 1. Host-to-incidence reduction

For a vertex `v` of the six-vertex component `C`, all its neighbours
outside `C` lie in the seven-set `S`.  With
`J=overline{G[C]}`, minimum degree eight therefore gives exactly the lower
bound used by the finite lemma:

```text
|A_v| >= 8-d_G[C](v) = 3+d_J(v).
```

For every nonempty `X subseteq C`, the open neighbourhood of `X` separates
`X` from the other component `D`.  Its internal and boundary parts are
disjoint, so seven-connectivity gives

```text
|N_G[C](X)| + |union_{v in X} A_v| >= 7.
```

Taking `X=C` also proves that every boundary vertex meets `C`.  A boundary
vertex complete to a literal `K_4` in `G[C]` would form a literal `K_5`, so
the fourth incidence hypothesis is valid.  No fullness, degree-equality,
or unstated boundary-edge assumption is used in this reduction.

## 2. Six-vertex orbit enumeration

The verifier represents `J` by the fifteen-bit mask of its edges.  The
eleven-edge lower bound on `G[C]` is exactly `|E(J)|<=4`.  The functions
`core_has_k5` and `core_is_three_colourable` respectively test whether the
core contains a literal `K_5` and whether it has a proper colouring with at
most three colours.  Quotienting the surviving labelled masks by all
`6!` vertex permutations is therefore exact.

The independent audit run reproduced ten canonical orbits and the pinned
orbit digest

```text
d9d88730ab2cd9712f1131aca905e15241e06cb790e63f25d64e71344b598c9e
```

matching the ten complement types listed in the theorem.  In particular,
no unbounded conclusion is inferred from a bounded census: the theorem has
already reduced the component literally to six vertices before invoking
the enumeration.

## 3. CNF semantics

The formula has one variable `x_(v,s)` for each of the 42 possible
`C`--`S` incidences.  Each group of clauses was checked directly.

1. `Formula.at_least` uses every subset of size `n-r+1`, which is exactly
   the positive-clause encoding of at least `r` true literals.  It correctly
   encodes every row-degree lower bound.
2. For fixed nonempty `X`, the connectivity clauses forbid any
   `|N_K(X)|+1` boundary columns from all being empty on `X`, where `K` is
   the six-vertex core.  This is
   equivalent to the required union-neighbourhood inequality.
3. Each negative four-literal clause says that a boundary vertex is not
   complete to a literal core `K_4`.
4. The adjacent-column clauses forbid precisely a decreasing pair of
   six-bit incidence columns.  Sorting the seven columns loses no set
   system because boundary labels play no role in the lemma or its
   conclusion.
5. For each of the `5040` injections, the six negative assignment literals
   make every clause vacuous unless the injection respects all incidences.
   For every set of `|E(J)|-1` missing core edges, the distributed
   `2^(|E(J)|-1)` clauses are the CNF expansion of the assertion that those
   edges are not all repaired.  Consequently the conjunction says exactly
   that no valid injection repairs all but at most one core nonedge.

Thus a satisfying assignment would be exactly a counterexample to Lemma
2.1, not merely a relaxation or a stronger auxiliary object.  The
deterministic CNF corpus digest reproduced as

```text
8540146081d94bc2779d3049e1c5fba807748cb3a6052e8a4b770c6ec854a354.
```

## 4. Independent certificate reproduction

The full verifier was run with CaDiCaL 3.0.1 and `drat-trim` at revision
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985`.  The audit invocation supplied
the checker explicitly through `--checker`; it regenerated every formula
from the audited verifier, regenerated all ten DRAT proofs, and checked
each proof independently of the SAT solver.

The reproduced terminal line was

```text
UNSAT_cases=10/10 DRAT_verified=10/10 generated_proof_bytes=10339951
```

The proof-byte total may depend on the solver build, as the theorem notes;
the orbit and CNF hashes are deterministic and matched exactly.  The
audited local executables had SHA-256 values

```text
CaDiCaL:  601c9fa8ba5d09fd81bb00c89b3e54832f138bccc3422bd8652e8cda4d74d1fa
drat-trim: f58f63b0f76945d4c4c9ff6e87afaf870f579e67c0f7cca589492df8fc7ebd47
```

The stated trust boundary is accurate: CPython and the explicit generator
remain trusted, CaDiCaL is only the proof producer, and `drat-trim` checks
the emitted refutations.

## 5. Minor-model reconstruction

For the injection supplied by the finite lemma, the six sets
`B_v={v,f(v)}` are connected and pairwise disjoint.  A core edge joins its
two bags directly.  For every but at most one core nonedge, one of the two
literal cross-incidences in the lemma joins the corresponding bags.  They
therefore form a `K_6^-` model, allowing additional adjacencies.

Seven-connectivity forces `N_G(D)=S`: omitting any boundary vertex would
make a separator of order at most six between the nonempty components
`C` and `D`.  If `s_0` is the unique boundary vertex unused by the
injection, then `D union {s_0}` is connected, is disjoint from the six
earlier bags, and is adjacent to each of them through the literal vertex
`f(v)`.  It is the seventh universal branch set, giving the claimed
explicit `K_7^-` minor model.

## 6. Verdict and scope

The proof establishes Theorem 1.1 under exactly its stated hypotheses, and
Corollary 3.1 correctly eliminates only the order-six equality-response
component in the audited five-centre two-cut reduction.  It raises that
component's surviving lower bound to seven.  It does not eliminate larger
components, the three-connected branch after deleting the five centres, or
prove the global conjecture.

No unresolved assumption, encoding discrepancy, certificate failure, or
proof gap was found.
