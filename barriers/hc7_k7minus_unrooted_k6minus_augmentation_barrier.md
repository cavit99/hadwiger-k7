# An unrooted `K_6^-` minor does not augment in a six-connected graph

**Status:** explicit barrier to an intermediate assertion; written proof and
deterministic checker audited GREEN in the adjacent Lo-robustness audit.
This is not a counterexample to the six-connected `4n` target: it falls
short of that density by ten edges.

## Assertion refuted

The following implication is false.

> If a six-connected graph contains a `K_6^-` minor, then it contains a
> `K_7^-` minor.

## Construction

Let `I` be the icosahedron and form

\[
                         Q=K_1\vee I,
\]

with universal vertex `a`.  The icosahedron is five-connected, so `Q` is
six-connected.  It has thirteen vertices and forty-two edges.

The graph `Q` contains a `K_6^-` minor.  This follows at once from Lo's
Theorem 1.3, because `Q` is four-connected, non-planar and has minimum
degree six.  It can also be checked directly.  In the standard NetworkX
labelling of the icosahedron, the five branch sets

\[
 \{7\},\quad \{0,1,2,3,4,5,6,8\},\quad
 \{9\},\quad\{10\},\quad\{11\}
\]

form a `K_5^-` model, whose only missing pair is `\{9\},\{11\}`.  Adding
the singleton branch set `\{a\}` gives a `K_6^-` model in `Q`.

## Exclusion of `K_7^-`

Suppose that `Q` has a `K_7^-` model.  At most one branch set contains `a`.
If no branch set contains `a`, the model lies in the planar graph `I`,
which is impossible.

Otherwise remove the branch set containing `a`.  The remaining six branch
sets lie in `I`.  If the one permitted missing adjacency of the original
model is incident with the removed branch set, the remaining branch sets
form a `K_6` model.  Otherwise they form a `K_6^-` model.  Both graphs are
non-planar, whereas every minor of `I` is planar.  This contradiction shows
that `Q` has no `K_7^-` minor.

## Scope and density gap

Since the icosahedron has twelve vertices and thirty edges,

\[
                    |E(Q)|=42=4|V(Q)|-10.
\]

Thus the construction does not refute any density-assisted augmentation at
`4n`.  It identifies the first unsupported inference in a direct use of
Lo's theorem: six-connectivity and an unrooted `K_6^-` model do not control
which branch sets meet the prospective seventh branch set.  A successful
argument must use the nine-edge surplus above the sharp `4n-9` elementary-
minor entrance, or establish a genuinely rooted model theorem.

The deterministic checker is
[`hc7_k7minus_unrooted_k6minus_augmentation_barrier_verify.py`](hc7_k7minus_unrooted_k6minus_augmentation_barrier_verify.py).

## Primary source

- O.-H. S. Lo,
  [*A characterization of graphs with no `K_{3,4}` minor*](https://arxiv.org/abs/2603.27973v1),
  Theorem 1.3.
