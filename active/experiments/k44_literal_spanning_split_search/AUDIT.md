# Independent internal audit: literal-`K_{4,4}` spanning-split screen

**Verdict: GREEN at the exact revisions below.**  The symbolic encoding,
authenticated host corpora, recorded bounded results, and two solver-free
adjunct checks support exactly the finite claims made in the README.  They do
not prove an unbounded spanning-split theorem or the literal `K_{4,4}` case of
T44.

This is a separate internal mathematical and finite-encoding audit, not
external peer review.

## Audited revisions

| file | SHA-256 |
|---|---|
| [`README.md`](README.md) | `c65a77dc89cf5ef38c414dd86a2869031b3c05720d350e65a49b7be79680a626` |
| [`search.py`](search.py) | `1a7ba1ff5de6a54a93e9cfc29f44e8ac4a06f46b91f2f2db5e20f7bdb7865839` |
| [`verify.py`](verify.py) | `2776688cfdeaf36c7f98a45ea0b8595d6eae3eac390a88df07ea2d8e42768a23` |
| [`output.txt`](output.txt) | `298eb4db2c5e85841713acc902441d81dc521485d678d8c34bc4d5fed3044e84` |
| [`verify_minimum_kfull_bond_route_nonclosure.py`](verify_minimum_kfull_bond_route_nonclosure.py) | `42195c818ba2d59284df05a9c1c5516e7a061d781b1250b4e0a0bdaad7f404de` |
| [`verify_icosahedral_seed_nonextension.py`](verify_icosahedral_seed_nonextension.py) | `94a00b974fb57c7adcef6c3693d513f6274e33c411db6037a905d05b5f742eeb` |

## Corpus and reproduction checks

The complete reproduction harness was rerun with Z3 `4.16.0`, NetworkX
`3.6.1`, and nauty `2.9.3`.  It terminated GREEN with the output retained in
`output.txt`.  The harness now checks the generated count, sorted graph6
digest, and post-filter eligible-host count before accepting each case.
Consequently an empty, truncated, or changed generator stream cannot report
the published GREEN result.

The authenticated corpora are:

| host family | generated | eligible | graph6 SHA-256 |
|---|---:|---:|---|
| all connected order-eight hosts of minimum degree at least four | 424 | 422 | `79043a58646d5fc086e54b33c75f77e9935221dcf00245e2781ad234eb288ad5` |
| connected order-nine 4-regular hosts | 16 | 16 | `9e851692305a2c9b565cdb6e4ff4644c34b02c796dbc7b53db416a2afb2260bd` |
| planar order-nine hosts of minimum degree at least four | 14 | 10 four-connected | `08048d0e52435765946d241d35ddf08617b4b35f3c8c4aca2bedbff69dc32f9c` |
| canonical `K_3*(3K_2)` zero-, one-, and two-edge perturbations | 6 | 6 | `ae62a05e285f00fafebda2b36776d8074136d419a8e679eec67caf2949964821` |

The first line is exhaustive at order eight for the stated host conditions.
The three order-nine lines are targeted families, not an exhaustive
order-nine search.  Independent regeneration also confirmed the raw counts,
digests, connectivity distributions, inclusion of `2K_1*C_7` in the planar
family, and the reduction of 79 labelled join perturbations to six
isomorphism types.

## Encoding checks

For each fixed host, `search.py` enumerates every nonempty subset, its exact
external vertex boundary, every three-vertex deletion and its components,
and both orientations of every spanning connected bipartition.  The symbolic
incidences impose:

1. nonempty support for all seven boundary resources and
   `|N_X(W)|+|N_D(W)|>=7` for every nonempty `W`, including `W=V(X)`;
2. the strict order-eight inequality for every proper connected `W` meeting
   both distinguished supports;
3. multiplicity at least two for each of the five `K`-supports,
   `1<=|R_a|<=5`, and existence of an eligible vertex `p`;
4. at most three components after a three-vertex deletion and, when there
   are exactly three, precisely one of the two audited incidence profiles;
5. the universal anchored negation over every eligible `p` and every
   oriented spanning connected partition containing it; and
6. the full negation with split bound two when the second side sees `b` and
   split bound three when it does not.

The nondecreasing binary values of the five `K`-supports break only their
permutation symmetry: the value is injective on supports, repeated supports
remain allowed, and all other constraints are invariant under that
permutation.  A SAT answer is reconstructed and checked by exhaustive
solver-free set computations.  This direct check protects the interpretation
of any reported survivor; because every audited instance is UNSAT, it is not
an independent certificate of the UNSAT answers.

## Solver-free adjunct checks

The minimum-side checker is GREEN on the displayed order-eight graph.  It
verifies four-connectivity, all boundary and strict blocker inequalities,
support multiplicities, all five eligible choices of `p`, and the absence of
three-cuts.  It then exhausts every bond.  The unique minimum `K`-full side is
`{0,3,4}`; it is a three-vertex path with cutvertex `0` and splits only three
supports.  The same side is nevertheless already a closing partition, and
the checker finds 182 anchored witnesses and 95 full witnesses.  Thus the
example refutes only the proposed two-connectivity and four-split
consequences of lexicographic minimum-side selection, not the spanning-split
target.

The fixed-seed checker is GREEN on the exact labelled graph6 graph
`JhfwEDbKgs_` and the five supports used in the adjacent rooted-extension
barrier.  It verifies the graph6 encoding, four-connectivity, the complete
connected-set score histogram, all 467 bonds, and the absence of a
four-support split.  It exhausts all 1,023 nonempty `a`-supports of order at
most five.  For each, the intersection of all sides forced by the oriented
three-split bonds is the maximal possible region for `R_b`; monotonicity
makes this a valid elimination of every nonempty subset of that region.
Only 12 maximal regions are nonempty and none meets the 32 remaining
boundary-six obligations.  This excludes the full `a,b` extension only for
that one fixed labelled seed.

## Trust boundary and exact scope

The finite trust boundary is the disclosed Python, Z3, NetworkX, and nauty
semantics, successful assertions, and the audited translation above.  Z3 is
version-recorded but is not locked by the repository environment, and no
DRAT-style independently checkable UNSAT certificate is retained.  The
`__debug__` guards prevent running the verification entry points with Python
assertions disabled.

Accordingly, the audit certifies bounded hostile evidence and the two exact
finite adjunct statements only.  It does not infer the minimum-blocker
bisection lemma, weighted splitter theorem, literal T44 branch, T44,
Conjecture 21, or `HC_7`.
