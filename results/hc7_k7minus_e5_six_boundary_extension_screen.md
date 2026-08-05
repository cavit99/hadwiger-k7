# Exact extension screens for the labelled six-boundary kernels

**Status:** computer-assisted finite result with a separately implemented
exhaustive checker; separate internal audit GREEN for the pinned revision in
the [adjacent audit](hc7_k7minus_e5_six_boundary_extension_screen_audit.md).
This theorem concerns only the finite labelled hosts defined below.  It does
not prove an unbounded reduction or `(E5)`.

Write `K_7^-` for `K_7` with one edge deleted.  Let

```text
P={0,1,2,3,4,5}
```

and let `B` be a graph on `P`.  Unless a case explicitly says otherwise,
`01` is an edge.  Add one of the following low kernels, with no unlisted
edges.

1. The `K_2` kernel has adjacent vertices `d,w` with

   ```text
   N_P(d)={0,1,2,3},              N_P(w)={0,1,4,5}.
   ```

2. The `P_3` kernel has path `f_1-d-f_2` with

   ```text
   N_P(d)={0,1,2},
   N_P(f_1)=N_P(f_2)={0,3,4,5}.
   ```

3. The `K_3` kernel is obtained from the preceding kernel by adding
   `f_1f_2`.

A **six-full representative** is adjacent to every vertex of `P` and to no
low-kernel vertex or other representative.  A **singleton missing `r`** is
adjacent exactly to `P-{r}`.  A **full edge missing `r`** has two adjacent
ends, each adjacent exactly to `P-{r}`.

## 1. Ordinary extension screens

### Theorem 1.1

The following exhaustive statements hold.

#### Favourable `P_3,K_3` orientation

Put `u=0` and assume `d_B(0)=1`, so `01` is the only boundary edge at `u`.

1. With one six-full representative and one singleton missing `0`, the
   `P_3` host contains `K_7^-` whenever `|E(B)|>=5`, and the `K_3` host does
   so whenever `|E(B)|>=4`.  The maximum target-free masks are respectively

   ```text
   P_3:  01,12 and one of {15+34,14+35,13+45};
   K_3:  01,12 and one of {34,35,45}.
   ```

2. With one six-full representative and two singleton components missing
   `0`, suppose the five vertices `P-{0}` induce `P_3` disjoint union `K_2`.
   Every such host contains `K_7^-`.
3. With one six-full representative and one full edge missing `0`, every
   such host contains `K_7^-`.

#### Other `P_3,K_3` orientation

Put `u=1`.  With one six-full representative and two singleton components
missing the same root `r`, every host contains `K_7^-` under the exact
degree-compatible conditions

```text
r=1:       d_B(1)<=3;
r!=1:      d_B(1)=1.
```

The same conclusion holds with the two singleton vertices joined by an
edge.

#### `K_2` extensions

Put `u=0`.

1. With one six-full representative and two singleton components missing
   `0`, assume `d_B(0)<=2` and that `P-{0}` induces `P_3` disjoint union
   `K_2`.  Every such host contains `K_7^-`.
2. With one six-full representative and one full edge missing `0`, assume
   `d_B(0)<=2`.  The target-free boundary graphs are exactly

   \[
      E(B)=\{01\}\mathbin\cup X,
      \qquad X\subseteq\{23,45\}.                    \tag{1.1}
   \]

3. With exactly two six-full representatives and `d_B(0)=1`, every
   target-free boundary has at most seven edges.  At seven edges the unique
   target-free boundary is

   ```text
   01,12,13,14,15,23,45.                             (1.2)
   ```

4. Adding a singleton missing `0` to the preceding two-six-full host always
   gives `K_7^-`.

#### Multiple six-full `P_3,K_3` extensions

1. Three six-full representatives force `K_7^-` for every graph `B`, even
   without requiring `01`.
2. With two six-full representatives, `01 in E(B)` and `d_B(1)<=2`, the
   target-free boundaries are exactly the sixteen graphs

   \[
   E(B)=\{01\}\mathbin\cup X\mathbin\cup Y,          \tag{1.3}
   \]

   where

   ```text
   X is a subset of {02,12},
   Y is empty or consists of one of {34,35,45}.
   ```

   In particular they have at most four edges.
3. Adding one singleton missing `1` forces the target when `d_B(1)<=2`.
   Adding one singleton missing any other root forces the target when
   `d_B(1)=1`.

## 2. Split-contact screens

Contracting two adjacent connected parts of one unbounded component gives
two adjacent representatives.  A root has contact type `L`, `R` or `LR`
according as it has a neighbour in the first part, the second part, or both.
The following statements enumerate all contact types compatible with the
displayed hypotheses.

### Theorem 2.1

1. Take either the `P_3` or `K_3` kernel, one other six-full
   representative, and one split six-full component.  Suppose both split
   parts meet root `1`, every other root meets at least one part, and

   \[
     E(B)=\{01\}\mathbin\cup X\mathbin\cup Y,
   \]

   where `X` is empty or `{02}` and `Y` is empty or one of `{34},{35},{45}`.
   Among all `3^5=243` contact patterns, the host is target-free exactly
   when roots `3,4,5` all have the same exclusive contact type `L` or all
   have the same exclusive contact type `R`.

2. Take the `K_3` kernel, another six-full representative, and a split
   six-full component in which root `1` has exactly one neighbour.  If
   `B` is the triangle on `{0,1,2}` and root `0` or root `2` is adjacent to
   every vertex of the split component, the host is target-free exactly
   when roots `3,4,5` have one common exclusive contact type.

3. Let `E(B)={01,12,34}` and suppose root `1` has exactly one neighbour in
   the split component.  If root `3` or root `4` is adjacent to every vertex
   of the split component, the host is target-free exactly when roots
   `0,1,2,5` have one common exclusive contact type.

The second and third screens each test every compatible contact pattern:
there are `162` patterns for each choice of universal root.

## 3. Exhaustive verification

The retained
[screen implementation](../active/experiments/e5_six_boundary_localisation_advance/e5_six_boundary_extension_screen.cpp)
constructs every host above.  For a host of order `n in {10,11,12}`, it
enumerates every used vertex subset and every partition of that subset into
seven nonempty bags.  It checks bag connectivity and accepts precisely when
the branch-set quotient has at most one missing adjacency.  The complete
partition counts are

| host order | partitions |
|---:|---:|
| 10 | 11,880 |
| 11 | 159,027 |
| 12 | 1,899,612 |

The [recorded run](../active/experiments/e5_six_boundary_localisation_advance/e5_six_boundary_extension_screen_output.txt)
lists every catalogue size and negative distribution.  The
[independent checker](../active/experiments/e5_six_boundary_localisation_advance/e5_six_boundary_extension_screen_check.cpp)
reconstructs all 145,034 hosts and uses a different complete model-universe
generator.  Its deterministic
[driver](../active/experiments/e5_six_boundary_localisation_advance/e5_six_boundary_extension_screen_check.py)
pins the checker source, compiles it strictly as C++20 and verifies its exact
output.  The checker covers 140,498 ordinary hosts and 4,536 split-contact
hosts and includes positive `K_7^-` and negative `K_7^vee` and
complement-of-`P_8` sanity cases.

## 4. Scope

The ordinary screens concern only graphs obtained by contracting each
displayed opposite component to one representative.  The split screens are
valid unbounded inputs only when the two representatives are the contractions
of two adjacent connected parts with the encoded root contacts.  A positive
minor model then lifts through those contractions.

No negative finite host is asserted to lift to an `E5` enemy.  The theorem
does not localise density inside an uncontracted six-full component, prove
that every live configuration reaches one of these hosts, justify repeated
singleton deletion, or prove `(E5)`.
