# Barrier: one internal vertex per rooted bag is too restrictive

**Status:** exact unbounded counterfamily to the incidence-only strengthening.
It is not a counterexample to the sparse six-cut dichotomy: every member has
a punctured rooted `K_5`, using one gate and one clique carrier in each bag.

## Construction

Let `S={s_1,...,s_6}` be stable.  For an integer `m>=6`, let the shore `C`
consist of six independent **gates** `g_1,...,g_6` and a clique `W` of order
`m`.  Add every gate--clique edge, and give `g_i` the sole boundary neighbour
`s_i`.  No vertex of `W` has a boundary neighbour.

The example is realised inside a genuinely six-connected graph by adding a
second component `D=K_6` of `G-S` and every edge between `D` and `S`.

## Exact checks

For nonempty `X subseteq C`, put

```text
a=|X intersect {g_1,...,g_6}|,   b=|X intersect W|.
```

If `b=0`, the boundary of `X` contains all `m` clique vertices outside the
set and its `a` distinct boundary roots, so has order `m+a>=6`.  If `a=0`,
it has the six gates and the `m-b` unused clique vertices, so has order at
least six.  If both parts are nonempty, its internal boundary has order

```text
(6-a)+(m-b)
```

and it sees `a` roots, for total `m+6-b>=6`.  Thus the shore satisfies the
exact relative-six condition.  The second-lobe completion described above is
six-connected: after fewer than six deletions, a root, its gate, and a clique
vertex survive on the first side, whilst a root and a vertex of `D` survive on
the second; these vertices join every remaining vertex to a common surviving
root.

Every connected `S`-full packet contains every gate, because `g_i` is the
unique shore neighbour of `s_i`.  Hence two such packets cannot be disjoint
and `mu_S(C)=1`.

The excess is

```text
eta_S(C) = binom(m,2)+6m+6-4(m+6)
         = (m^2+3m-36)/2.
```

It is `9` at `m=6` and is unbounded.

## Failure of the proposed certificate

Consider a rooted model in which every non-singleton bag has the form

```text
{s_i,v},   v in C.
```

Connectivity forces `v=g_i`, because `g_i` is the only shore neighbour of
`s_i`.  Distinct gates are nonadjacent, and stability supplies no root--root
or cross-root contact.  Consequently no two of these one-vertex-augmented
bags touch.  Singleton root bags do not repair this, so five such bags cannot
have a `K_5^-` quotient.

The desired unrestricted conclusion nevertheless holds.  For any five
indices choose distinct `w_i in W`; then

```text
B_i={s_i,g_i,w_i}
```

are five disjoint connected rooted bags.  They are pairwise adjacent through
the clique edges `w_iw_j`, so they form a punctured rooted `K_5` model.  The
ordinary clique on any five vertices of `W` also shows that the shore contains
an ordinary `K_5^-` minor.

Thus an unbounded certificate theorem must allow at least a gate plus a core
carrier in one rooted bag.  The singleton-or-one-internal-vertex formulation
cannot be the terminal combinatorial lemma.

## Reproduction

Run

```text
python barriers/hc7_incidence_only_rooted_k5minus_gate_clique_barrier_verify.py
```

The verifier checks the local inequalities and packet number by exhaustive
subset enumeration, rejects all incidence-only five-bag allocations, checks
the explicit rooted `K_5`, and exhausts every deletion of at most five
vertices in the completed host.
