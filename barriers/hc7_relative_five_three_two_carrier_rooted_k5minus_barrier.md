# Relative five-connectivity and all three--two carriers do not force a rooted `K_5^-`

**Status:** exact local barrier to a carrier-synchronisation lemma; elementary
proof and deterministic exhaustive verifier.  The example has low excess and
does not refute the density-sensitive sparse-six-cut target.

The verifier is
[`hc7_relative_five_three_two_carrier_rooted_k5minus_barrier_verify.py`](hc7_relative_five_three_two_carrier_rooted_k5minus_barrier_verify.py),
at SHA-256

```text
a47d10dee89cdb735b8e2d513ceeda9e19783f9d665015cd737e324e60c00032.
```

## 1. The false assertion

The following proposed local lemma is false.

> Let `R` be five independent terminals in a graph `H`.  Suppose every
> nonempty terminal-avoiding set `X` satisfies `|N_H(X)|>=5`.  If every
> partition of `R` into a three-set and a two-set has two disjoint connected
> carriers, then `H` has an `R`-rooted `K_5^-` model.

The connectivity condition is precisely the relative condition inherited by
a five-root puncture of an internally six-connected six-boundary shore.  Thus
adding it does not repair the carrier-only assertion.

## 2. Counterexample

Let

```text
R={0,1,2,3,4}
```

be independent.  Add adjacent nonterminals `u,v`; join `u` to all five
terminals and join `v` to `0,1,2,3`.

The only nonempty terminal-avoiding sets are `{u}`, `{v}` and `{u,v}`.  Their
external neighbourhoods have orders `6`, `5` and `5`, respectively.

Every three--two partition has disjoint connected carriers.  Let `P` be its
two-set.

- If `4 in P`, use `P union {u}` and `(R-P) union {v}`.
- If `4 notin P`, use `P union {v}` and `(R-P) union {u}`.

Both displayed sets are connected in each case and they are disjoint.

There is nevertheless no `R`-rooted `K_5^-` model.  Only two vertices lie
outside `R`, so at least three of the five rooted branch bags are singleton
terminals.  Those three bags are pairwise nonadjacent because `R` is
independent.  Hence every rooted model has at least three missing branch-bag
adjacencies, whereas `K_5^-` permits only one.

## 3. Six-root shore form and exact scope

Add a sixth independent root `x`, adjacent only to `v`.  With

```text
C={u,v},                 S=R union {x},
```

every nonempty `X subseteq C` has `|N(X)|>=6`: the three neighbourhood orders
are `6,6,6`.  The component is `S`-full.  Its coefficient-four excess is

```text
eta(C)=e(C)+e(C,S)-4|C|=1+10-8=3.
```

After puncturing `x`, the five-root excess is `1+9-8=2`.  Consequently this
example rules out only a purely topological synchronisation of the ten
three--two carrier outcomes.  It does **not** refute either live
density-sensitive target

```text
eta(C)>=6  =>  a punctured five-rooted K_5^- model,
```

or

```text
eta(C)<=5 mu_S(C).
```

Any successful use of the Du--Li--Xie--Yu carrier alternatives must therefore
exploit excess, exact-cut descent, or additional compatibility between the
ten separately chosen carrier pairs.

## 4. Reproduction

From the repository root run

```text
python3 -B barriers/hc7_relative_five_three_two_carrier_rooted_k5minus_barrier_verify.py
```

The standard-library checker verifies the six-root neighbourhood condition,
all ten carrier instances, the excess calculation, and all `6^2=36`
allocations of `u,v` to rooted branch bags.
