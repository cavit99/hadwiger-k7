# Simultaneous transfers in a near-clique model

**Status:** written proof; separate internal audit at the source hash recorded
in the adjacent audit.

## Global target and notation

**Conjectural target.** Every seven-connected graph containing a
`K_7^vee` minor contains a `K_7^=` minor. Here `K_7^vee` deletes two
incident edges of `K_7`, whereas `K_7^=` deletes two independent edges.
The statements below give sufficient constructions, not this theorem.

**Written conditional implication.** The structural target would prove
Norin--Totschnig Conjecture 19: every `K_7^=`-minor-free graph is
six-colourable. Indeed, choose a minor-minimal non-six-colourable
`K_7^=`-minor-free graph `G`. Every proper minor is six-colourable, and
deleting one vertex and restoring it with one new colour gives `chi(G)=7`.
The graph is noncomplete, since `K_7` contains `K_7^=`. Mader's
seven-connectivity theorem for this contraction-critical case, as used in
the [audited critical reduction](hc7_k7minus_critical_to_sixconnected_4n_reduction.md),
gives `kappa(G)>=7`.
[Norin--Totschnig, Theorem 4](https://arxiv.org/abs/2507.03244)
states that every `K_7^vee`-minor-free graph is six-colourable, so `G`
contains a `K_7^vee` minor. The proposed structural target would supply
the forbidden `K_7^=` minor in `G`. This implication uses neither a
density bound nor a quotient lift; its structural premise remains open.

Fix disjoint connected bags `D={v}, T_1,...,T_4,B,C`. The six bags other
than `D` are pairwise adjacent; `v` meets each `T_i` and misses `B,C`.
Adjacency always means an actual host edge between the stated sets.
Extra host vertices and edges are allowed. No prescribed root inside a
donor is retained by the constructions below.

## 1. A simultaneous transfer criterion

**Theorem 1 (written proof).** Choose any nonempty subset of the four
donors `T_i`, and partition each chosen donor as `T_i=X_i dot-union Y_i`, where
both parts are nonempty and connected. Suppose
`W={v} union (union_i X_i)` is connected. Keep the untouched core bags
and replace each donor by `Y_i`. Let `L` be the graph whose vertices are
these six resulting core bags, with an edge exactly when the corresponding
bags are nonadjacent. Let `g` count the bags among `B,C` adjacent to `W`.
Either of the following conditions gives a `K_7^=` minor:

1. `g=1` and `L` has at most one edge;
2. `g=2` and `L` is a matching of size at most two.

**Proof.** A connected graph partitioned into two nonempty parts has an
edge between them, so `X_i` is adjacent to `Y_i`. Thus `W` meets every
donor remainder. It also meets every untouched `T_j` using the original
edge from `v`. The seven proposed bags are nonempty, connected and
pairwise disjoint. Their only possible missing contacts are those of `L`
and the `2-g` contacts from `W` to `B,C`.

If `g=1`, write `H` for the still-missed bag. No missing core contact is
incident with `H`: every original donor--`H` edge either remains incident
with `Y_i`, or has its donor endpoint in `X_i` and would make `W` meet
`H`. Untouched core contacts survive. Consequently the at most two missing
contacts form a matching. This is also immediate under condition 2.
A matching of size at most two extends to a matching of size two on seven
vertices; discard any unnecessary model contacts. These seven explicit
bags therefore give the required minor in the original host. QED

In particular, contacts between two donor remainders must be checked
between those remainders. An old edge between whole donors is insufficient.
There is no quotient, induction or decreasing parameter in this theorem.

## 2. When a simultaneous move reduces to one donor

**Theorem 2 (written proof).** Under either terminal condition of Theorem 1,
if some `X_i` is adjacent to `v` and to at least one of `B,C`, then moving
only `X_i` into `{v}` already gives a `K_7^=` minor.

**Proof.** Restore every other donor whole. Every lost core contact in
this one-donor move is incident with `Y_i` and is also a lost contact in
the simultaneous move. Hence there is at most one such loss, because
the terminal conditions make `L` a matching. The new deficient bag
`{v} union X_i` is connected and gains at least one of `B,C`. It meets
`Y_i` through an `X_i`--`Y_i` edge and meets the other original `T_j`
through `v`. If one hole remains, the proof of Theorem 1 shows that any
core loss is independent of it; if neither remains, there is at most one
missing contact. The explicit seven bags again give `K_7^=`. QED

Thus a simultaneous construction which cannot be reduced to one donor
must obtain its new hole contact through a transferred piece not directly
adjacent to `v`. A connected chain of transferred pieces can do this.

## 3. A strict two-donor example

**Proposition 3 (written proof).** A two-donor move can be terminal although
no permitted one-donor move is terminal in the displayed model.

**Proof.** Take vertices `v,x_1,y_1,x_2,y_2,u_3,u_4,b,c`.
The six vertices `y_1,y_2,u_3,u_4,b,c` induce `K_6-y_1u_3`.
Add exactly the edges

```text
x_1y_1, x_1u_3, x_2y_2, x_1x_2, x_2b,
vx_1, vy_2, vu_3, vu_4.
```

The initial model has deficient bag `{v}`, donors
`T_1={x_1,y_1}`, `T_2={x_2,y_2}` and singleton bags
`{u_3},{u_4},{b},{c}`. It is a `K_7^vee` model spanning the host.

There are only two connected one-donor donations adjacent to `v`.
Donating `{x_1}` gains neither hole and loses the core contact `y_1u_3`.
Donating `{y_2}` gains both holes, but its remainder `{x_2}` loses contacts
to `{u_3},{u_4},{c}`. Neither returned seven-bag model contains the target.
The opposite singleton halves are not adjacent to `v`; the other donors
are singletons. There are no unowned vertices supplying an additional
path. This exhausts the permitted one-donor constructions in this model,
not all possible minor models of the host.

Instead donate `{x_1}` and `{x_2}` together. Their union with `{v}` is
connected along `v x_1 x_2`. The new six core bags are the original six
named `y_1,y_2,u_3,u_4,b,c`; their sole missing contact is `y_1u_3`.
The new bag meets all except `{c}`. The two missing contacts are independent,
giving `K_7^=`. After donating only `{x_1}`, three contacts are missing,
so requiring every intermediate model to remain `K_7^vee` rejects this
valid construction. QED

## 4. Exact remaining inference

**Recorded route nonclosure.** Seven-connectivity is not used in Theorems
1--2. What remains unproved is that, allowing all core bags and the two
missing labels to change, a seven-connected host with the initial minor
has a terminal simultaneous allocation, or a reduction with a valid lift
and a strictly decreasing parameter. The displayed finite example proves
only that chains enlarge the permitted constructions.

A proposed chain must retain actual remainder--remainder contacts and
connected donor remainders. Distinct fan endpoints in a donor tree do not
establish either condition. A failed chain search has not been shown to
produce a separator of at most six actual vertices: counting the six core
bag labels is not such a certificate. Temporary losses are allowed by the
construction, but no well-founded rule through those losses is proved.
