# Literal-`K_{4,4}` spanning-split hostile screen

**Status:** deterministic computer-assisted bounded evidence.  Both the
anchored strengthening and the full exact spanning-partition statement survive
the complete order-eight screen and three targeted order-nine families.  This
is not an unbounded theorem, an independently checkable UNSAT certificate, a
proof of the minimum-blocker bisection lemma, or a proof of the literal
`K_{4,4}` case of T44.

## Question and exact hypotheses

The screen uses the audited minimum-blocker normal form

```text
D={a,b,k1,k2,k3,k4,k5},  H=D-{a},  K=H-{b}.
```

For a fixed finite simple host `X`, all incidences between `V(X)` and `D` are
symbolic.  The encoding imposes every currently proved local hypothesis:

1. `X` is three-connected and has minimum degree at least four;
2. every boundary resource has a neighbour in `X`, and every nonempty
   `W subseteq X`, including `W=X`, satisfies

   ```text
   |N_X(W)|+|N_D(W)| >= 7;
   ```

3. every proper connected `W` seeing both `a` and `b` has boundary order at
   least eight, as required by the minimal choice of the blocker;
4. every `k in K` has at least two neighbours in `X`;
5. `1 <= |N_X(a)| <= 5`, and at least one vertex `p in N_X(a)` satisfies

   ```text
   X-p is full to H,  and  |N_K(p)| <= 2;
   ```

6. deleting any three vertices leaves at most three components; whenever
   exactly three components remain, their `K`-supports satisfy one of the two
   exact profiles in item 4 of the audited minimum-blocker theorem.

The upper bound in item 5 is the omitted singleton-atom algebra from the
preceding bounded screen: in the notation of Proposition 7.1 of the atom
theorem, `|P|+|O|=6` and `|O|>=1`, while `P=N_X(a)`.

For an ordered spanning connected partition `X=U dotunion V`, let `s(U,V)`
be the number of `K`-supports meeting both sides.  The two separately tested
negations are:

- **anchored:** every vertex `p` satisfying item 5 fails every partition with
  `p in U`, `V` seeing `b`, and `s(U,V)>=3`;
- **full:** every partition with `U` seeing `a` fails the exact criterion

  ```text
  s(U,V)>=3  if V sees b;
  s(U,V)>=4  if V misses b.
  ```

The quantifier over `p` in the anchored negation is universal over all
eligible vertices.  Thus a SAT model cannot arise merely by selecting one bad
eligible vertex while another eligible vertex has a good partition.

## Bounded results

No SAT survivor was found.

| order | host family before structural filtering | generated | tested | anchored | full |
|---:|---|---:|---:|---|---|
| 8 | all connected unlabelled hosts with minimum degree at least four | 424 | 422 | UNSAT | UNSAT |
| 9 | connected 4-regular hosts | 16 | 16 | UNSAT | UNSAT |
| 9 | planar hosts of minimum degree at least four, retaining only four-connected hosts | 14 | 10 | UNSAT | UNSAT |
| 9 | `K_3` joined to `3K_2`, with zero, one, or two added edges between distinct matching edges | 6 | 6 | UNSAT | UNSAT |

The two excluded order-eight hosts have vertex-connectivity two.  The four
excluded planar order-nine hosts have vertex-connectivity three; the retained
ten form the deliberately targeted four-connected planar family.  The planar
family includes the nine-vertex bipyramid `2K_1` joined to `C_7`.  The six
join-family counts are isomorphism types after canonical labelling.

The sorted graph6 digests are:

| family | SHA-256 |
|---|---|
| order-eight minimum-degree-four hosts | `79043a58646d5fc086e54b33c75f77e9935221dcf00245e2781ad234eb288ad5` |
| order-nine 4-regular hosts | `9e851692305a2c9b565cdb6e4ff4644c34b02c796dbc7b53db416a2afb2260bd` |
| order-nine planar minimum-degree-four hosts | `08048d0e52435765946d241d35ddf08617b4b35f3c8c4aca2bedbff69dc32f9c` |
| order-nine join perturbations | `ae62a05e285f00fafebda2b36776d8074136d419a8e679eec67caf2949964821` |

Order eight is exhaustive for the displayed local hypotheses: `geng`
enumerates all unlabelled connected minimum-degree-four hosts, after which
the proved connectivity conditions are checked.  Order nine is intentionally
not exhaustive.  Its three families test the minimum-degree equality case,
the four-connected planar regime, and the sharp three-cut host
`K_3` joined to `3K_2` together with its smallest edge perturbations.  No
inference is made about other order-nine hosts or any larger order.

## Encoding and independent SAT-model check

[`search.py`](search.py) fixes each host and makes only the seven boundary
supports symbolic.  Connected subsets and spanning connected partitions are
enumerated directly.  It breaks only the harmless permutation symmetry of
the five `K`-resources.  For every SAT answer it reconstructs the seven
supports and runs solver-free exhaustive checks of the inequalities,
minimality, attachment and anchor conditions, three-cut profiles, and absence
of the requested partitions before printing the survivor.  The reproduction
harness also asserts the published host counts, graph6 digests and eligible
host counts, so a truncated or empty generator output is rejected.

No SAT survivor of either spanning-split negation occurred in the recorded
runs, so there is no such counterexample to validate or promote to
`barriers/`.

## Scoped nonclosure: internal structure of a minimum `K`-full side

A separate hostile query falsified two proposed structural consequences of
minimum-side selection, while leaving both the selection and the bisection
target intact.  Choose a `K`-full bond side `U` first with minimum order and
then with maximum split count.  The following local model has a **unique**
minimum side, that side has a cutvertex, and its split count is only three:

```text
graph6: GCxvf{
a ={1,2,3,4,5}       b ={6}
k1={0,3}             k2={0,4}
k3={1,2,4}           k4={3,5}
k5={0,1,2,5,6}
```

The host has order eight, 18 edges, vertex-connectivity four, and degree
sequence `(4,4,4,4,4,4,5,7)`.  Consequently it has no three-cut, so the
three-cut-profile condition is vacuous.  Every vertex `1,2,3,4,5` is an
eligible choice of `p`.

The unique minimum `K`-full bond side is

```text
U={0,3,4},  E(X[U])={03,04}.
```

It has articulation vertex `0`, its two lobes are the singletons `{3}` and
`{4}`, its boundary within `U` is all of `U`, and exactly `k3,k4,k5` split.
Thus even the lexicographic choice “minimum `|U|`, then maximum split count”
does not supply a two-connected side or a fourth split support.

This is not a counterexample to the anchored or full spanning-split
statement.  The selected minimum bond itself is closing: `U` sees `a`, its
complement sees `b`, it splits `k3,k4,k5`, and `p=3` (or `p=4`) is eligible
and belongs to `U`.  Another closing partition is

```text
U'={1,4},  V'={0,2,3,5,6,7},  p=1
```

It is an anchored closing partition splitting `k2,k3,k5`.  Exhaustion finds 182
anchored witnesses when eligible choices of `p` are counted and 95 full
oriented partitions.  The model therefore refutes only the claims that a
lexicographically minimum `K`-full side must be two-connected or must split
four supports.  It shows why the correct `a,b` orientation, rather than the
internal shape of that side alone, has to remain in the argument.

The dependency-free checker
[`verify_minimum_kfull_bond_route_nonclosure.py`](verify_minimum_kfull_bond_route_nonclosure.py)
exhaustively verifies all boundary inequalities, blocker minimality, support
multiplicity, eligible vertices, connectivity, the unique minimum side, and
the displayed closing partition.

## The four-support shortcut is false, but its planar seed is excluded

The separate [six-connected rooted-extension
barrier](../../../barriers/hc7_k44_sixconnected_k5_rooted_extension_barrier.md)
gives a four-connected exterior satisfying the derived five-support
inequality but having no bond which splits four supports.  Thus the two
distinguished supports `a,b` cannot be discarded from the proof.

That fixed planar seed does not extend to the exact blocker data.  A
solver-free exhaustion checks all 1,023 nonempty possible `a`-supports of
order at most five.  Only 12 leave any nonempty region in which a
`b`-support could avoid every forbidden oriented three-split bond, and none
of those regions meets all 32 remaining boundary-six obligations.  This is
a finite fact about one fixed labelled seed, not an unbounded exclusion of
the planar obstruction.  It is verified by
[`verify_icosahedral_seed_nonextension.py`](verify_icosahedral_seed_nonextension.py).

## Reproduction and trust boundary

NetworkX `3.6.1` is pinned by the repository lock.  The recorded run used Z3
`4.16.0` and nauty `2.9.3` (`geng`, `planarg`, and `labelg`).  On the current
local toolchain, use the Homebrew Python carrying `z3-solver`; the scripts
locate NetworkX in the repository environment when necessary, and the nauty
executables must be on `PATH`.  From the repository root run:

```text
python3 active/experiments/k44_literal_spanning_split_search/verify.py
```

The expected output is retained in [`output.txt`](output.txt).  A single mode
or family can instead be rerun with `search.py --help`.

To verify the scoped selection-route failure, run:

```text
python3 active/experiments/k44_literal_spanning_split_search/verify_minimum_kfull_bond_route_nonclosure.py
```

To verify that the fixed planar barrier has no full `a,b` extension, run:

```text
python3 active/experiments/k44_literal_spanning_split_search/verify_icosahedral_seed_nonextension.py
```

The finite trust boundary is Python and Z3 Boolean/pseudo-Boolean semantics,
Z3's `UNSAT` answers, NetworkX connectivity and graph6 parsing, nauty's
unlabelled generation/canonical labelling, `planarg`'s planarity filter, and
successful assertion execution.  No DRAT-style or independently checkable
UNSAT certificate is retained.  The two negations share the host and
incidence encodings, although their partition clauses are implemented
separately.

## Mathematical reading

The decisive negative outcome of this falsification gate is that the first
previously untested order does not expose either an anchoring obstruction or
a full two-helper obstruction, even after all sharp three-cut profiles are
enforced.  In particular, finite evidence now favours proving the stronger
anchored statement: find an eligible `p` and a connected spanning partition
with `p` on the first side, a `b`-neighbour on the second, and three split
`K`-supports.  This remains a conjectural unbounded lemma, not a conclusion of
the computation.  The written [five-support bond
reduction](../../../results/hc7_k44_five_support_bond_reduction.md) narrows
any counterexample further to three minimum-side block structures and a
weakly-linkable parity-bond obstruction.

## Proved inputs

- [tight-boundary and minimum-blocker theorem](../../../results/hc7_k44_tight_boundary_and_minimum_blocker.md)
- [spanning-extension and exact split-count theorem](../../../results/hc7_k44_spanning_two_helper_split_count.md)
- [singleton-atom algebra](../../../results/hc7_k44_positive_atom_elimination.md)
