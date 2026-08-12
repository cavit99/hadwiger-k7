# A five-chromatic boundary need not contain a two-set-transversal rooted `K_5` model

**Status:** explicit barrier/counterexample to the intermediate claim stated
below.  It is not a counterexample to the `K_7^-` six-colour conjecture,
the bounded-feedback alternative, or any host-level composition theorem.

## Refuted claim

The following boundary-only assertion is false.

> **Proposed two-set-transversal claim.**  Let `Q` be a `K_5`-subgraph-free
> graph with `|V(Q)|<=14` and `chi(Q)>=5`.  If
> `A,B subseteq V(Q)` satisfy `|A|,|B|>=7`, then `Q` has a `K_5`-minor
> model every branch set of which meets both `A` and `B`.

This is the direct boundary assertion one might try to apply to two leaf
pieces of the forest in the bounded-feedback outcome, since
seven-connectivity gives each leaf piece at least seven neighbours in the
feedback set.

## Construction

Let

\[
                    Q=(K_2\vee C_5)\mathbin{\dot\cup}K_1.       \tag{1}
\]

Write `p,q` for the vertices of `K_2`, write
`c_0,c_1,c_2,c_3,c_4` cyclically for the vertices of `C_5`, and let `t` be
the isolated vertex.  Put

\[
                       A=V(Q)-\{p\},\qquad
                       B=V(Q)-\{q\}.                 \tag{2}
\]

Then `|V(Q)|=8` and `|A|=|B|=7`.  Also

\[
                       \chi(Q)=2+\chi(C_5)=5,        \tag{3}
\]

while `Q` has no `K_5` subgraph because

\[
                       \omega(Q)=2+\omega(C_5)=4.   \tag{4}
\]

## Every `K_5` model has two forced singleton bags

The isolated vertex `t` cannot occur in a `K_5`-minor model.  Consider any
such model in `K_2 vee C_5`.

Both `p` and `q` must occur.  Indeed, if `p` were absent, removing the one
possible branch set containing `q` would leave four pairwise adjacent
connected branch sets in `C_5`, a `K_4` minor of a cycle.  This is
impossible.  The same argument applies with `p,q` interchanged.

The vertices `p,q` cannot lie in the same branch set, since the remaining
four branch sets would again form a `K_4` minor in `C_5`.  Let `P_p,P_q`
be their two distinct branch sets.  The other three branch sets form a
`K_3` minor in the unused part of `C_5`.  If either `P_p` or `P_q` contained
a cycle vertex, that unused part would be a proper subgraph of `C_5`, hence
a forest, which has no `K_3` minor.  Therefore

\[
                              P_p=\{p\},\qquad
                              P_q=\{q\}.              \tag{5}
\]

The bag `P_p` misses `A`, and the bag `P_q` misses `B`.  Thus no `K_5`
model in `Q` has every branch set meeting both sets in (2), refuting the
proposed claim.

## Exact scope

The construction refutes only the inference from

\[
 |V(Q)|\leq14,\quad \chi(Q)\geq5,\quad K_5\nsubseteq Q,
 \quad |A|,|B|\geq7                               \tag{6}
\]

to a `K_5` model contained entirely in `Q` and transversal to both named
sets.  It does not use, and therefore does not refute a theorem using, the
full forest of `S`-bridges and the inequalities

\[
 |N_S(Y)|+|E_{G-S}(Y,(G-S)-Y)|\geq7                \tag{7}
\]

for every connected forest piece `Y` with a nonempty far side.

Indeed, the most natural two-exterior augmentation of this example already
contains the target.  Add vertices `x,y`, make `x` adjacent to every vertex
of `A`, make `y` adjacent to every vertex of `B`, and do not add `xy`.
Then

\[
 \{p\},\ \{q\},\ \{c_0\},\ \{c_1\},\ \{c_2\},
 \ \{x,c_4\},\ \{y,c_3\}                           \tag{8}
\]

are seven connected branch sets with only the pair
`{c_0},{c_2}` nonadjacent.  They form an explicit `K_7^-` model.  Thus the
failure of the boundary-only rooted model does not prevent a successful
host-level composition in which exterior forest pieces enter the branch
sets.

The smallest plausible repair is consequently a finite
**forest-bridge composition theorem**: retain the boundary graph together
with its connected forest pieces and all their boundary neighbourhoods,
rather than replacing those pieces by two cardinality-seven subsets of the
boundary.
