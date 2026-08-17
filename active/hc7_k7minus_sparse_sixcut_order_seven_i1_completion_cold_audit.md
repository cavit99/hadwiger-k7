# Cold audit: full order-seven `i=1` completion

**Verdict:** **GREEN** at the pinned revisions below.  This is an independent
internal audit, not external peer review.

## Pinned artefacts

```text
7384cdbbd16b0370aa171fad767975f043bddf873eecc235d2d1a552249a911f
  active/hc7_k7minus_sparse_sixcut_order_seven_i1_completion.md
67fb9b60e5272288c534791cf90866236648f6b9d1e6ea2de9b565f7d2315005
  active/experiments/sparse_sixcut_order_seven_i1_classification/verify.py
```

The audited dependencies were also checked at these revisions:

```text
a81cb9476890fe0d373ecdc8aecebf5a40996d7d44ba15f16faf076dd5b581d8
  active/hc7_k7minus_ordinary_k5minus_rooting_contraction_gate.md
23db844015f8f38619e164453b1049b9c16468fe6677d3337d5b5bf63d33a0d8
  active/hc7_k7minus_ordinary_k5minus_rooting_contraction_gate_cold_audit.md
093c25e97ff5e5d627d12915c551418cd0039f5fb1f745dc03bdeb64148d7d75
  active/hc7_k7minus_sparse_sixcut_order_seven_theta_singleton_completion.md
f24ef3026763a595f4fc3cd9f61fc482b05d9ed281e99fe48f02b987746f51ff
  active/experiments/sparse_sixcut_order_seven_theta_singleton/verify.py
b8dc456fb995e382478884bc3bc55531ae1797d59f3c8d7eee739adb0de335ae
  active/hc7_k7minus_sparse_sixcut_order_seven_theta_singleton_completion_cold_audit.md
8778331e60c4655aab12e0fc8e3b4e875121eca12d7a6f3cb10c3f36e982bfdf
  active/hc7_k7minus_sparse_sixcut_order_seven_theta_singleton_completion_second_cold_audit.md
```

## 1. Reduction to the six-vertex core

Use the perfect matching to pair every `w in W` with a distinct root `s_w`.
If four connected bags give a nonspanning `K_4^-` model in `W`, choose one
vertex in each bag and adjoin its matched root.  For any vertex `w` outside
their union, the fifth bag

```text
{s_w,w,u}
```

is connected, disjoint from the first four, and adjacent to each of them
through the universal vertex `u`.  The five bags therefore retain at most
the one missing contact of the original four-bag model.  Their five roots
are distinct because `w` was not in any old bag.

Likewise, if `W` has a `K_5^-` minor, selecting one vertex in each of its
five branch bags and adjoining the five corresponding matched roots roots
that model directly.  Thus failure of the desired rooted conclusion leaves
exactly the graph-theoretic residue used in Lemma 2.1: a spanning
`K_4^-` model, no nonspanning one, and no `K_5^-` minor.

The last condition is in fact redundant after the second: deleting any one
bag of a `K_5^-` model leaves a `K_4^-` model whose support omits the deleted
nonempty bag.  Its explicit inclusion in the theorem and verifier is
harmless and supplies a useful consistency check.

## 2. Finite classification and independent falsification

The verifier's search space is exact.  On six labelled vertices there are
`2^15=32768` simple graphs.  The four-bag partitions number

```text
S(6,4)=65                                      (spanning),
C(6,4)S(4,4)+C(6,5)S(5,4)=15+60=75           (nonspanning),
```

and the five-bag partitions number

```text
C(6,5)S(5,5)+S(6,5)=6+15=21.
```

For each partition the code correctly tests connectivity of every nonempty
bag and all six or ten quotient contacts, accepting precisely when at most
one is missing.  It visits every fifteen-bit graph mask, tests the three
partition families in the stated order, and canonicalises each survivor
under all `6!` permutations.

I separately enumerated the same graph class with independently written
standard-library code.  It generated all connected branch-set partitions
rather than importing any table or function from the supplied verifier.  It
gave the following exact counts:

```text
labelled six-vertex graphs                         32768
graphs with a K_4^- minor                         23434
graphs whose every K_4^- model is spanning          720
among those, graphs with a K_5^- minor                 0
survivors with seven edges                           720
```

A methodologically separate deletion-and-edge-contraction search reproduced
`23434`, `720`, `0`, and the seven-edge concentration.  Hence neither the
partition encoding nor the supplied model predicate is the sole basis for
the classification.

Finally, direct permutation orbits of the three canonical theta graphs have
sizes

```text
Theta(2,2,3): 180,
Theta(1,2,4): 360,
Theta(1,3,3): 180.
```

The three orbits are disjoint and their union is exactly the set of 720
survivors.  Thus there is no additional isomorphism class and no strict
supergraph survivor.  Running the pinned verifier reproduced

```text
Theta(2,2,3): labelled_survivors=180
Theta(1,2,4): labelled_survivors=360
Theta(1,3,3): labelled_survivors=180
total_labelled_survivors=720 all_have_7_edges
order-seven i=1 core classification: PASS
```

The verifier uses assertions and should be run with the recorded ordinary
Python command, not with `python -O`.

## 3. Theta completion and excess arithmetic

For each surviving graph, `e(W)=7`.  Since `u` has exactly its six neighbours
in `W` and no boundary neighbour,

```text
e(C)=6+7=13,               e(C,S)=e(W,S),
eta_S(C)=13+e(W,S)-4*7=e(W,S)-15.
```

Therefore `eta_S(C)>=6` is exactly the incidence threshold
`e(W,S)>=21`.  The pinned theta theorem has precisely the remaining
hypotheses: stable six-root boundary, universal root-invisible `u`, a
perfect matching from `W` to the roots, and one of the three classified
theta cores.  Its two cold audits and its 34,560-case verifier certify that
this threshold gives a punctured rooted `K_5^-` model.  No hypothesis is
lost in the composition.

## 4. Hall return and host lift

At the pinned Hall-profile revision, an inclusion-minimal deficient family
of order one is a singleton model bag `{u}` with

```text
N_S(u)=empty,              N_C(u)=C-{u},
```

and the other six shore vertices have a perfect matching to `S`.  In a
spanning ordinary five-bag model, the other four bags partition `W`.  Since
the original five-bag quotient has at most one missing contact, those four
bags give the spanning `K_4^-` model required by Theorem 1.1.  The theorem
therefore applies to the high-excess row `eta_S(C)>=6` without an unproved
individual-universality inference for any `i>1` family.

For the host lift, let the punctured five-bag model omit `s_o`, and let
`A,D` be two other full components of `G-S`.  Add the bags

```text
A union {s_o},             D.
```

They are connected and disjoint from the five shore bags.  Fullness gives
each new bag a contact to every rooted bag, and an edge from `s_o` to `D`
gives their mutual contact.  Hence only the possible missing pair already
present in the rooted `K_5^-` model remains, producing a `K_7^-` minor.

## 5. Scope verdict

No reduction, enumeration, arithmetic, dependency, or lifting gap was
found.  The terminal statement is the exact order-seven `i=1` row with
`eta_S(C)>=6` in the three-full-component setting.  It does not resolve the
order-seven families with `i>1`, prove the packet-weighted excess theorem,
close the entire sparse three-component case, or by itself meet the
Norin--Totschnig significance benchmark.
