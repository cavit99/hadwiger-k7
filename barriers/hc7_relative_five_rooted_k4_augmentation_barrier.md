# Relative five-connectivity does not augment a rooted `K_4` to a rooted `K_5^-`

**Status:** exact counterexample with an elementary proof and deterministic
verifier.  It blocks a four-root augmentation shortcut, but its density is
below the live coefficient-four threshold.

The verifier
[`hc7_relative_five_rooted_k4_augmentation_barrier_verify.py`](hc7_relative_five_rooted_k4_augmentation_barrier_verify.py)
has SHA-256

```text
e49e6fd6bb86e7e241c37dfd44a9ffc83d66517eeadeae25fc8015939b19241b
```

## 1. The false assertion

The following statement is false, even when the five roots are independent
and the four-rooted model avoids the omitted root.

> Let `R` be five independent roots in a graph `H`, let
> `C=V(H)-R` be nonempty, and suppose that every nonempty `X subseteq C`
> satisfies `|N_H(X)|>=5`.  If `H-r` contains an `(R-{r})`-rooted `K_4`
> model for some `r in R`, then `H` contains an `R`-rooted `K_5^-` model.

## 2. Counterexample

Let `R={0,1,2,3,4}` be independent.  Add three vertices `u,v,w`, with

```text
E(H[C])={uv,uw},
N_R(u)=012,
N_R(v)=0124,
N_R(w)=0123.
```

In the order

```text
{u},{v},{w},{u,v},{u,w},{v,w},{u,v,w},
```

the external-neighbourhood orders are

```text
5,5,5,5,5,6,5.                                      (1)
```

Thus the exact relative five-connectivity hypothesis holds.

After omitting root `4`, the four bags

```text
{0},  {1,v},  {2,u},  {3,w}                         (2)
```

form a rooted `K_4`.  The singleton bag meets the other three because every
internal vertex sees `0`; the remaining contacts are `vu`, `uw`, and `1w`.

There is no five-rooted `K_5^-` model.  Since the roots are independent and
there are only three internal vertices, such a model would need exactly two
singleton root bags, whose mutual nonedge would be the sole missing
adjacency.  Each of `u,v,w` would therefore belong to a different remaining
bag and see both singleton roots.  Hence the singleton pair would lie in

```text
N_R(u) intersect N_R(v) intersect N_R(w)={0,1,2}.    (3)
```

The bags rooted at `3` and `4` would then necessarily contain `w` and `v`,
respectively, since these are their only internal neighbours.  But
`{3,w}` and `{4,v}` are nonadjacent: `wv`, `3v`, `4w`, and `34` are all
absent.  This gives a second missing adjacency, a contradiction.

## 3. Exact scope

The five-root density surrogate is only

```text
|E(H[C])|+|E_H(C,R)|-3|C|=2+11-9=4.                 (4)
```

Adding a sixth independent root adjacent to all of `u,v,w` gives the
corresponding relative-six shore, still with coefficient-four excess four.
Thus the example does not refute the live density-sensitive implication at
excess six.  It shows that the rooted `K_4` outcome must be combined with
density or more detailed attachment information; relative connectivity and
root independence alone do not augment it.

## 4. Reproduction

Run

```text
python3 -B barriers/hc7_relative_five_rooted_k4_augmentation_barrier_verify.py
```

The standard-library verifier checks (1), the model (2), all `6^3=216`
allocations for a rooted `K_5^-`, and the density calculation (4).
