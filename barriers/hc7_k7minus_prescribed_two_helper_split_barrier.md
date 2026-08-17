# Universal four-root factorisation does not prescribe the two helpers

**Status:** explicit finite barriers with a deterministic exhaustive
verifier.  These examples refute only the strengthening without target
exclusion: both contain `K_7^-`.  They therefore leave open a
split-or-`K_7^-` theorem
and any theorem using the minimum-degree-seven or seven-connected
augmentation available in the critical host.

The verifier is
[`hc7_k7minus_prescribed_two_helper_split_barrier_verify.py`](hc7_k7minus_prescribed_two_helper_split_barrier_verify.py),
at SHA-256

```text
a7d7ef75d7cd45d94fb46a6203661428de60435d6ada4ac6104d5d5606be2199.
```

## 1. The false assertion

The following strengthening of the universal four-root/two-helper
factorisation is false.

> Let `H` be six-connected with
> `|E(H)|>=4|V(H)|-6`.  For every four-set `Z` and distinct
> `x,y in V(H)-Z`, there is a partition
>
> ```text
> V(H)=Z dot_union U dot_union V
> ```
>
> such that `H[U]` and `H[V]` are connected, `U,V` are adjacent, each
> vertex of `Z` has a neighbour in both helpers, and `x in U,y in V`.

Both graphs below satisfy the unprescribed conclusion for **every**
four-set.  Each nevertheless has one displayed pair which cannot be put
in distinct helpers.

## 2. A ten-vertex barrier

Let `H_1` have vertex set `{0,...,9}` and let its complement have edge set

```text
25 26 28 34 37 38 46 49 57 59 67.
```

Then

```text
|V(H_1)|=10,       |E(H_1)|=34=4|V(H_1)|-6,
kappa(H_1)=6,      delta(H_1)=6.
```

Take

```text
Z={0,1,2,3},       x=4,       y=5.
```

The verifier checks all `2^4` assignments of the other vertices and finds
no connected `Z`-full helper partition with `4` and `5` on opposite sides.
It separately checks every four-set.  The number of unprescribed
factorisations ranges from 7 to 23; the deterministic first-certificate
stream has SHA-256

```text
a9fab0a4dd0237470f3cfbfcee5980545ed2bf92a148d114358a602c137154fb.
```

This obstruction is not target-free.  The seven bags

```text
{0}, {1}, {2,3,6}, {4}, {5}, {7}, {8}
```

are connected and pairwise adjacent except for `{5}` and `{7}`.  They form
an explicit `K_7^-` model.

## 3. A diamond-rooted barrier

The second example shows that prescribing the helpers can fail even when
the four roots induce the exact diamond used at an exceptional centre.

Start with the icosahedron on `{0,...,11}` with edges

```text
01 03 05 09 0-11
12 15 16 19
26 28 29 2-10
34 38 39 3-11
47 48 4-10 4-11
56 57 5-11
67 6-10
7-10 7-11
89 8-10.
```

Add a universal apex `12` and the four chords

```text
13 14 17 18.
```

Call the resulting graph `H_2`.  Direct exhaustive deletion gives

```text
|V(H_2)|=13,       |E(H_2)|=46=4|V(H_2)|-6,
kappa(H_2)=6,      delta(H_2)=6.
```

Put

```text
Z={0,1,2,12},      x=5,       y=6.
```

The root graph is a diamond whose missing edge is `02`.  Exhausting all
`2^7` assignments gives no connected `Z`-full factorisation separating
`5` from `6`.  Again the verifier checks the unprescribed conclusion for
every four-set.  The factorisation count ranges from 25 to 160, and the
first-certificate stream has SHA-256

```text
226af415944de47bd7466186befd88d940b6fd56c47841ac07ec6a02be35eb55.
```

This graph also contains the target.  The seven bags

```text
{3}, {7}, {2,5,6,8}, {1,9}, {4,10}, {0,11}, {12}
```

are connected and pairwise adjacent except for `{3}` and `{7}`.

## 4. Exact consequence

Six-connectivity, the sharp `4n-6` density and universal spanning
four-root/two-helper factorisation do not prescribe even one nominated
helper pair.  The diamond hypothesis does not repair the statement.

Both examples identify the same viable escape.  They have minimum degree
six and contain explicit `K_7^-` models.  Thus they do **not** refute any of
the following possible repairs:

1. prescribed helper separation or a `K_7^-` minor;
2. prescribed helper separation in a target-free graph of minimum degree
   at least seven; or
3. prescribed helper separation when adjoining the deleted exceptional
   centre gives the special seven-connected augmentation from the critical
   host.

The first graph also uses a literal `K_4` as its root set.  The second is
the relevant sharp warning: it retains diamond roots but fails both the
target exclusion and the minimum-degree/seven-connected-augmentation
conditions.

## 5. Reproduction

From the repository root run

```text
python3 -B barriers/hc7_k7minus_prescribed_two_helper_split_barrier_verify.py
```

The checker uses only the Python standard library.  It verifies both edge
sets, density equalities, exact six-connectivity, all unprescribed
four-root factorisations, the two prescribed failures and every adjacency
of the displayed `K_7^-` models.
