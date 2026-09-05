# Expanding separator roots in the singleton completion

**Status:** written proof and barrier/counterexample to an intermediate
claim, with a [separate internal audit](hc7_k44_expanding_separator_roots_audit.md).
The positive
statement below closes one case of the singleton residue. The explicit
planar construction refutes a broader local inference even when all
separator-root branch sets may expand. Neither result proves the full
singleton completion, T44, Conjecture 21 or `HC_7`. This note belongs to the
[designated T44 frontier](../active/hc7_k44_closure_frontier.md#42-singleton-blocker-and-its-contraction-trace).

## 1. The full target being attacked

Use the hypotheses of the
[core-concentrated joint-contact theorem](../results/hc7_k44_core_concentrated_joint_contact_reduction.md).
Thus `G` is seven-connected, `E={a,p} dotunion T` is an exact seven-cut,
`|T|=5`, its two open components `D,R` are full to `E`, the adjacent
vertices `a,p` have degree seven and unique common neighbour `b` outside
`T`, and `G[D union T]` has a `T`-rooted `K_5` model. The target is to
prove that every such host contains `K_7^-`.

For a fixed rooted model `(B_t:t in T)`, let `C_a,C_p` be the sets of
rooted bags contacted by `a,p`. Target-freeness would give
`|C_a union C_p|<=3` for every choice of the rooted model. The full target
remains open here; Sections 2 and 3 delimit a possible use of the new
universal rooted bipartite theorem.

## 2. Equal three-contact sets do close when the remote side is nontrivial

**Theorem (written proof).** Suppose `G,E,D,R,T,a,p` have the hypotheses
above, except that target-freeness is not assumed. If one `T`-rooted `K_5`
model in `G[D union T]` satisfies

```
C_a=C_p=C,     |C|=3,     |R|>=2,
```

then `G` contains a `K_7^-` minor.

### Proof

Write `T-C={x,y}` and put

```
F=G[R union {a,p,x,y}],     Z={a,p,x,y}.
```

The pair `(F,Z)` is internally four-connected: if a separation of `F`
has every vertex of `Z` on one closed side and a nonempty other open side
`W`, then `W subseteq R`. Its external neighbourhood in `G` is contained
in its separator in `F`, together with `C`. A separator of order at most
three in `F` would therefore give a separator of order at most six in
`G`. At least one of the four roots in `Z` lies outside that separator
and outside `W`, so this contradicts
seven-connectivity. Also `|F|>=6`.

Norin--Totschnig, Lemma 10 (the stated reformulation of Jørgensen,
Lemma 16(2)), therefore supplies a `Z`-rooted `K_4^-` model in `F`.
Denote its four branch sets by `A,P,X,Y`, with the correspondingly named
roots. At least three of the four cross contacts

```
A--X, A--Y, P--X, P--Y
```

are present, irrespective of which edge the rooted `K_4^-` omits.

Replace `B_x,B_y` by `B_x union X,B_y union Y`, keep the other three
`B_t`, and take `A,P` as the two remaining bags. These seven sets are
connected and pairwise disjoint: the two models share only the named
roots `x,y`, and their open sides lie in the distinct components `D,R`.
The five `T` bags retain all ten clique contacts. The root edge `ap`
gives the `A--P` contact, the six original contacts from `a,p` to the
three bags indexed by `C` survive, and at least three cross contacts
come from the rooted `K_4^-`. There are at least `10+1+6+3=20` contacts,
as required. No induction or decrease claim is used. Square.

This proof allows the `x,y` bags to expand into `R`; requiring all five
`T` bags to remain disjoint from `R` would lose precisely this option.
The conclusion uses an existing four-root theorem, not the new general
matroid argument. When `|R|=1`, Lemma 10's order hypothesis fails, and
that case has not been closed by this argument.

## 3. A planar obstruction even when separator roots may expand

**Refuted local inference.** Let `R` be connected with seven distinct
boundary roots `E={a,p} dotunion T`, `|T|=5`. Assume fullness to `E`,

```
|N_R(W)|+|N_E(W)|>=7  for every nonempty W subseteq R,
```

the root edge `ap`, a unique common `a,p` neighbour in `R`, and recorded
contact sets `C_a,C_p subseteq T` of union order at most three. Even with
incidences compatible with endpoint degree seven and a unique common
neighbour in the whole host, these data do **not** force seven disjoint
connected branch sets containing the seven roots and satisfying all but
at most one of the ten `a,p`-to-`T` contacts, where the recorded contacts
may be counted as already supplied by a fixed model outside `R`.

In particular, the inference remains false when the `T` branch sets may
use arbitrary vertices of `R`.

### Construction

Let `R` be a wheel with hub `h` and rim `r_0,...,r_4` in cyclic order.
Add five roots

```
q_0=a, q_1=p, q_2=t_0, q_3=t_1, q_4=t_2,
```

where `q_i` has the two neighbours `r_i,r_(i+1)` in `R` (indices modulo
five). Add the root edges

```
q_0q_1, q_2q_3, q_3q_4, q_4q_0.
```

Call this graph `F`. In its plane drawing all five roots lie on one face
in the order `a,p,t_0,t_1,t_2`; between `p,t_0` the facial walk passes
through `r_2`. Finally add two further boundary roots `c,d`, each adjacent
to every vertex of `R`, and let

```
T={t_0,t_1,t_2,c,d},
C_a={t_2,c,d},       C_p={c,d}.
```

No other edges involving `c,d` are needed in the local graph.

### Verification of the hypotheses

Each root has a neighbour in `R`, and `r_1` is the unique common `a,p`
neighbour there. For every nonempty `W subseteq R`, its boundary in `F`
has order at least five. To see this, first suppose `h in W`, and put
`s=|W-{h}|`. All `5-s` other rim vertices are boundary vertices. If
`1<=s<=4`, at least `s+1` roots touch `W`; the cases `s=0,5` each give
five boundary vertices directly. If `h notin W`, then `W` is a nonempty
rim set. A singleton has three neighbours in `R-W` and two root
neighbours; a two-set has at least two neighbours in `R-W` and three
root neighbours; a set of at least three rim vertices has the hub and
at least four root neighbours in its boundary. Adding `c,d` therefore
raises every such boundary to at least seven.

The local degrees of `a,p` are four and three. Three further neighbours
of `a` can be placed in the externally supplied `c,d` bags, and four
further neighbours of `p` can be placed in those same two bags, using
seven distinct vertices. Both endpoints then have degree seven; their
recorded contact sets are exactly the ones displayed, and no additional
common neighbour is introduced. This is a compatibility construction;
it is not a seven-connected target-free realization of `D`.

### Why allowing root expansion still fails

The plane graph `F` has no fully rooted `K_{2,3}` with at most one edge
deleted, with parts `{a,p}` and `{t_0,t_1,t_2}`. Every such target contains
a four-cycle in which `a,p` are opposite. For the other two roots
`t_i,t_j` on that cycle, the facial order in `F` is `a,p,t_i,t_j` after
possibly interchanging `i,j`. The cycle model would give vertex-disjoint
`a`--`t_i` and `p`--`t_j` paths with alternating endpoints on one face,
contrary to planarity.

Suppose the refuted local inference held for the constructed instance.
Discard the branch sets containing `c,d`. The remaining five connected
sets all lie in `F`, since no other root branch set can contain either
of those two roots. They must retain at least five of the six cross
contacts between `{a,p}` and `{t_0,t_1,t_2}`. The only recorded contact
among these is `a--t_2`, and its literal root edge already belongs to
`F`. The five sets would therefore be the forbidden rooted
`K_{2,3}` with at most one edge deleted. This contradiction proves the
negative finding. It permits unrestricted expansion of every root bag.

### Scope and smallest repair

The first unsupported inference is that the local boundary data supply
the required bipartite scheme, or its fully rooted minor. Simultaneous
matroid contractions cannot produce a model which this facial-order
obstruction excludes. A different selection of a matroid minimizer
does not repair the missing premise.

The example does not encode the actual other component `D`, global
seven-connectivity or target-freeness. It does not refute the full
singleton target, T44 or the universal bipartite theorem. A completion
must use additional global information, in particular a change of the
`T`-rooted `K_5` allocation in `D`, or a minor construction that does not
preserve the prescribed seven final bags. Those are the remaining
theorem obligations; the local rooted-allocation statement above is
false.

## Primary input

Norin--Totschnig, [*Every graph with no `K_7^vee`-minor is
6-colorable*, Lemma 10](https://arxiv.org/html/2507.03244v1), with its
exact hypotheses `|V(F)|>=6`, four prescribed roots and internal
four-connectivity. The new universal bipartite theorem is assessed here
at its [audited statement](../results/bipartite_contractibility_via_matroid_reduction.md);
it is not invoked to infer missing scheme paths from connectivity alone.
