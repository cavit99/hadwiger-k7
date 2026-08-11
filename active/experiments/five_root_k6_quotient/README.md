# Five independent roots over a `K_6` quotient

**Status:** written elementary theorem with a dependency-free exhaustive
checker. This is a quotient-level negative finding, not a theorem about the
uncontracted branch sets and not a proof of the `K_7^-` six-colour
conjecture.

## Theorem

Let `C` be a six-vertex clique, let `R` be an independent set, and let `H`
be a graph on `C union R` whose only unspecified edges are those between
`C` and `R`. Then

\[
 K_7^-\preccurlyeq H
 \quad\Longleftrightarrow\quad
 d_C(r)\ge5\text{ for some }r\in R.                 \tag{1}
\]

### Proof

If `r` has at least five neighbours in `C`, the singleton branch sets on
`C union {r}` give a `K_7^-` model (and give a `K_7` model when `r` has six
neighbours).

Conversely, suppose that `B_1,...,B_7` form a `K_7^-` model. Since `C` has
only six vertices, some branch set, say `B_1`, contains no vertex of `C`.
The graph `H[R]` is edgeless, so connectedness makes `B_1={r}` for one
root `r`.

Let `s` of the other six branch sets also contain no clique vertex. Each
of those sets is a singleton root and is nonadjacent to `B_1`. Each of the
remaining `6-s` branch sets contains a distinct vertex of `C`, and it can
be adjacent to `B_1` only if it contains a neighbour of `r`. Consequently
`B_1` is nonadjacent to at least

\[
 s+\max\{0,6-s-d_C(r)\}\ge 6-d_C(r)                 \tag{2}
\]

other branch sets. A `K_7^-` model permits at most one such nonadjacency,
so `d_C(r)>=5`. This proves (1). \(\square\)

## Five-root consequence

For a spanning `K_6` model in the graph obtained after deleting five
independent centres, contract the six branch sets. Target exclusion already
gives at most four contacted branch sets per centre. Theorem (1) shows that
the resulting `5 x 6` contact matrix has no further restriction: **every**
matrix with row sums at most four avoids a `K_7^-` minor in the quotient,
even when arbitrary contractions and absorptions are allowed in that
quotient.

The edge-maximal avoiding matrices have all row sums equal to four. Record
each row by its missing pair. Up to permutations of the five roots and six
clique labels, their normal forms are therefore the loopless multigraphs
with five edges on six vertices, allowing parallel edges and isolated
vertices. There are `52` such forms. Their edge-multiplicity profiles are:

| multiplicities | forms |
|---|---:|
| `(5)` | 1 |
| `(4,1)` | 2 |
| `(3,2)` | 2 |
| `(3,1,1)` | 7 |
| `(2,2,1)` | 7 |
| `(2,1,1,1)` | 18 |
| `(1,1,1,1,1)` | 15 |

Thus a successful continuation must split or otherwise use vertices inside
an actual branch set. Reselecting or contracting only the six quotient
vertices and the five independent roots cannot produce the forbidden minor.

## Verification

The accompanying `seven_terminal_kernel_probe.py` is exploratory and does
not support any additional recorded claim.

Run

```text
python3 active/experiments/five_root_k6_quotient/five_root_k6_quotient_verify.py --normal-forms
```

The checker exhausts the `15^5=759,375` labelled edge-maximal matrices and
the `52` normal forms. Expected final output:

```text
GREEN: exact quotient criterion verified
```
