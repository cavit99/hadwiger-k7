# Five-connectivity suffices for the rooted-helper closure

**Status:** written proof. The adjacent audit records its separate internal
verdict at an exact source hash. The global six-colouring conjectures remain
open; no external peer review or novelty claim is asserted here.

All graphs are finite and simple. Write `K_t^-` for `K_t` with one edge
deleted, and `K_7^=` for `K_7` with two independent edges deleted. A
`Z`-rooted two-helper model consists of four connected disjoint root bags,
one containing each member of `Z`, and two further connected disjoint bags
`U,V`. Each helper contacts every root bag, and `U,V` contact each other.
Root-root contacts are not required in this definition.

## 1. Exact input

We use Norin--Totschnig, Lemma 12, in the form recorded in the
[audited rooted-helper source](../results/hc7_k7minus_degree7_rooted_helper_closure.md)
at SHA-256
`6ffee04cf9ff66275f9674c24bc2b9c669b1e108b76e5b1d2a18ec7d0106fe67`:
if `(F,Z)` is internally four-connected, `|Z|=4`, and
`e(F)>=4|V(F)|-9`, then a `Z`-rooted two-helper model exists.
Its [adjacent audit](../results/hc7_k7minus_degree7_rooted_helper_closure_audit.md)
records the primary statement and hypotheses. We do not use its separate
fifth-root augmentation lemma.

## 2. Contact with a deleted vertex

**Lemma 1.** Let `G` be five-connected, let `v` be a vertex, and let
`Z` be a four-set in `V(G)-{v}`. If `F=G-v` has a `Z`-rooted two-helper
model, then it has such a model with a helper adjacent to `v` in `G`.

**Proof.** Among these models in the fixed finite graph `F`, maximize
`|U union V|`; subject to this, minimize the total order of the four root
bags. For a root bag `R_i` with prescribed root `z_i`, let `P_i` be the
set of its vertices adjacent to `U union V`.

Each `P_i` is a singleton. It is nonempty because both helpers contact
`R_i`. If it contained two vertices, we could choose distinct `a,b` in
`R_i` adjacent to `U,V`, respectively: failure to choose such a pair
would make both contact sets the same singleton. A minimal tree in
`F[R_i]` containing `z_i,a,b` spans `R_i`, by the secondary minimum.
One of `a,b` is a leaf different from `z_i`; suppose it is `a`. Move
`a` into `U`. Both altered bags remain connected, the old tree edge at
`a` preserves the contact from `U` to `R_i-{a}`, and `b` preserves the
other helper contact. The root stays in its own bag and all bags remain
disjoint. The helper union has strictly increased, a contradiction.

No component of `F` outside all six bags contacts a helper, since it
could be absorbed into that helper, again increasing their union.
Therefore the entire external neighbourhood in `F` of `U union V` is
contained in `P=union_i P_i`, which has four actual vertices.

If `v` contacted neither helper, this would also be their entire external
neighbourhood in `G`. Deleting `P` would separate the nonempty helper union
from `v`, which lies outside `P` and outside the model. This contradicts
five-connectivity. Hence a helper contacts `v`. QED

The argument is a finite optimization in the original host, not an
induction on quotients. Its improving moves strictly increase the helper
union; its only tie-breaking operation decreases root-bag order. It
retains every prescribed root and never assigns a vertex to two bags.

## 3. The closure theorem

**Theorem 2.** Let `G` be five-connected of order `n`, let
`d_G(v)=d`, and suppose

`e(G)>=4n+d-13`.

1. If `G[N(v)]` contains a `K_4^-` subgraph, then `G` contains a
   `K_7^=` minor.
2. If `G[N(v)]` contains a `K_4` subgraph, then `G` contains a
   `K_7^-` minor.

**Proof.** Choose the corresponding four vertices `Z subseteq N(v)`.
The graph `F=G-v` is four-connected, so `(F,Z)` is internally
four-connected. Moreover

`e(F)=e(G)-d>=4n-13=4|V(F)|-9`.

The exact input supplies a `Z`-rooted two-helper model in `F`.
Lemma 1 supplies such a model with at least one helper adjacent to `v`.
Add the singleton bag `{v}`. It contacts all four root bags through
their prescribed roots, and contacts at least one helper. The helpers
contact one another and all four root bags. Every literal edge on `Z`
survives because its ends are retained in their prescribed bags.

For the first conclusion, the only possible missing contacts are the
missing edge of the root `K_4^-` and the contact from `{v}` to the other
helper. These pairs have disjoint ends. For the second conclusion all
root-root contacts exist, leaving at most one missing contact. In either
case the seven displayed bags give the required minor. QED

This strengthens the connectivity hypothesis of the earlier closure and
uses the same density threshold. It does not assert that a subsequent
quotient remains five-connected, preserve contraction-criticality in that
quotient, or close the remaining global constructions.
