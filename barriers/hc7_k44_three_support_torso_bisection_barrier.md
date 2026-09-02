# Four-connectivity and the local torso inequality do not force the required bisection

**Status.** Barrier/counterexample to the stripped three-support torso claim
stated below; direct finite verification by the adjacent dependency-free
script.  This is not a counterexample to the global triangle-boundary torso
bisection lemma, the nonsingleton literal-core completion, the literal
`K_{4,4}` case of T44, T44, Conjecture 21, or `HC_7`.

## 1. Claim refuted

The following local statement is false.

> **Stripped torso-bisection claim.**  Let `H` be four-connected, let `T`
> induce a triangle, and let `P=V(H)-T` be connected.  Let `E,F_1,F_2` be
> supports of order at least two such that `E subseteq P`, while each `F_i`
> meets both `P` and `V(H)-P`.  Suppose that, for every nonempty connected
> `W subseteq P`,
> \[
>  |N_H(W)|+|\{R\in\{E,F_1,F_2\}:R\cap W\ne\varnothing\}|\ge6.
> \]
> Then there is a nonempty connected `A subset P` such that `H-A` is
> connected, `A` meets `F_1,F_2`, and `A` splits `E`.

## 2. Counterexample

Take `H=K_5` on

```text
P={u,v},  T={t0,t1,t2},
```

and put

```text
E={u,v},  F1={u,t1},  F2={v,t2}.
```

The graph `H` is four-connected, `T` is a triangle, `P` is connected, and
all three supports have order two.  The only nonempty connected subsets of
`P` are `{u}`, `{v}`, and `P`.  Their boundary-plus-support scores are
respectively six, six, and six:

```text
W={u}:  |N_H(W)|=4 and W meets E,F1;
W={v}:  |N_H(W)|=4 and W meets E,F2;
W=P:    |N_H(W)|=3 and W meets E,F1,F2.
```

Any set `A subseteq P` meeting both `F1` and `F2` must contain both `u` and
`v`, so `A=P`.  It therefore does not split `E`.  This disproves the claim.

## 3. Exact scope

The example has no complementary component and no two additional supports.
Moreover, both external supports leave `P` through `T`; the global
two-component support normal form does not permit that incidence on a
one-whole-support side without additional bridge information.  The example
also does not carry the global minimum support-full path or the distinguished
`a,b` incidences.

Accordingly, the live triangle-boundary torso bisection lemma must use the
provenance of the external supports in the complementary component, the two
supports not meeting `P`, or the global minimum-path data.  Four-connectivity
of the torso and its three-support inequality alone are insufficient.

## 4. Verification

Run

```text
python3 barriers/hc7_k44_three_support_torso_bisection_barrier_verify.py
```

Expected output:

```text
PASS order=5 connectivity=4 local_scores=6,6,6
PASS candidate_bisections=0
NOTE stripped local torso claim only; global support provenance is absent
```
