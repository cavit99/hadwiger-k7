# Closing the triangle boundary of a three-component six-cut

**Status:** written proof with a separate hash-pinned internal audit.
This closes one complete separator case for arbitrary component orders.
The other sparse boundaries, the six-connected density theorem, Conjecture
21 and HC7 remain open. No novelty or NT-equivalence claim is made.

## 1. Hypotheses and inputs

Let `G` be a finite simple six-connected graph, let
`e(G)>=4|V(G)|`, and suppose that a six-set `S` separates exactly three
components `A,C,D`. Put

```text
B=G[S],
eta(L)=e(G[L])+e_G(L,S)-4|L|,
a_L(s)=|N_G(s) intersect L|.
```

Assume for contradiction that `G` has no `K7^-` minor. Every component
is adjacent to every vertex of `S`. More generally every nonempty
`W subseteq L`, for any component `L`, has at least six external neighbours
in `G`, all belonging to `(L-W) union S`.

The [audited five-root density application](../results/hc7_five_root_density_sixcut.md)
gives `eta(L)<=7` when `e(B)=3`. Since

```text
sum_L eta(L)=24+(e(G)-4|V(G)|)-3>=21,
```

we have `e(G)=4|V(G)|` and `eta(A)=eta(C)=eta(D)=7` in this case.

We use two rooted inputs with their exact statements:

1. Dvořák--Norin--Rahman, [Theorem 2.6](https://arxiv.org/html/2609.17760v1#S2),
   states five-root universality by density. The row needed in Section 2
   supplies every labelled graph with at most six edges when density is
   at least four. Internal five-connectivity implies its 4-lightness
   hypothesis.
2. The [audited four-root helper input](../results/hc7_k7minus_degree7_rooted_helper_closure.md)
   records Norin--Totschnig, Lemma 12: an internally four-connected graph
   rooted at a four-set `Z` with `e(H)>=4|V(H)|-9` has four root bags
   and two adjacent helper bags, each adjacent to all four root bags.
   The [fifth-root augmentation lemma](../active/hc7_k7minus_e5_k5minus_cut_elimination.md#lemma-1-fifth-root-augmentation)
   places an additional specified vertex `x` in a helper whenever
   `(H,Z union {x})` is internally five-connected.

These are external or previously audited inputs, not new proofs here.

## 2. Puncturing an isolated boundary vertex

**Lemma.** Under the hypotheses above, suppose that `B` consists of a
triangle on `T` and three isolated vertices. For each component `L` and
each `s in S-T`, we have `a_L(s)>=4`.

**Proof.** Suppose instead that `a_L(s)<=3`, and root
`F=G[L union (S-{s})]` at `Z_s=S-{s}`. Every nonempty root-free subset
of `F` has at least five external neighbours: in the original graph it
has at least six, and deleting `s` removes at most one. Consequently
`F` is internally five-connected and therefore 4-light. Its density is

```text
rho4(F)=eta(L)-a_L(s)>=7-3=4.
```

The graph induced by its five roots has exactly the three triangle edges.
Choose any one of the seven missing root pairs, and let `J` consist of
the other six missing pairs. Five-root universality gives an
identity-rooted model of `J`. The three literal triangle edges supply
the corresponding additional contacts, producing a `Z_s`-rooted
`K5^-` model avoiding `s`.

The two other components, say `M,N`, give additional branch sets
`M union {s}` and `N`. They are adjacent through `s`, connected and
disjoint, and each meets every root bag through its prescribed boundary
root. Together these seven bags form `K7^-`. This contradicts the
assumption on `G`. QED

## 3. Complete closure of the triangle boundary

**Theorem.** If `G` is six-connected, `e(G)>=4|V(G)|`, and a six-set
`S` separates exactly three components such that `G[S]` consists of a
triangle and three isolated vertices, then `G` has a `K7^-` minor.
There is no bound on the orders of the components.

**Proof.** Retain the contradiction assumptions of Section 1. Write
`S=T union {r,x,y}`, where `T` is the triangle. Choose any one component
as `C` and denote the others by `A,D`. Construct the auxiliary graph

```text
H=G[C union S]+{rs:s in S-{r}},
Z=T union {r}.
```

All five added star edges are new. They are realisable simultaneously in
the original graph by absorbing `A` into the branch set containing `r`:
the component `A` is connected and has a neighbour at every vertex of
`S`. This will be the only use of `A`.

The density is exact:

```text
e(H)=4|C|+eta(C)+e(B)+5
    =4|C|+7+3+5
    =4(|C|+6)-9
    =4|V(H)|-9.                                      (1)
```

We next check both connectivity requirements before applying the rooted
inputs. Let `Y` be a nonempty subset of `V(H)-Z=C union {x,y}` and
suppose `|N_H(Y)|<=3`. If `W=Y intersect C` were nonempty, then

```text
N_G(W) subseteq N_H(Y) union {x,y},
```

giving at most five external neighbours in `G`, a contradiction. Thus
`Y` is one of `{x}`, `{y}`, `{x,y}`. By Section 2, both `x` and `y`
have at least four neighbours in `C`; these neighbours lie outside
every such `Y`. None of these three sets has boundary of order at most
three. Hence `(H,Z)` is internally four-connected.

Similarly let `Y subseteq V(H)-(Z union {x})=C union {y}` have
boundary of order at most four. A nonempty intersection `W=Y intersect C`
would satisfy

```text
N_G(W) subseteq N_H(Y) union {y},
```

again contradicting six-connectivity. The only other possibility is
`Y={y}`. But `y` has its at least four neighbours in `C` and also its
new neighbour `r`, so `d_H(y)>=5`. Thus `(H,Z union {x})` is internally
five-connected as well.

By (1) and the four-root helper input, `H` has a `Z`-rooted two-helper
model. Fifth-root augmentation lets us choose it with `x` in one helper
`U`; call the other helper `V`. The four root bags form a clique, since
`H[Z]` is the literal `K4` consisting of the triangle `T` and the three
star edges from `r` to `T`. Thus the six model bags form a `K6` model.

Lift it to `G` by enlarging only the root bag containing `r` by the
whole component `A`. This bag is connected through an edge from `r` to
`A`, and every used added star edge `rs` is replaced by an edge from
`A` to its endpoint `s`. If both endpoints belong to one model bag,
the same replacement preserves its connectivity. The other five bags
are unchanged, and all six lifted bags remain disjoint.

Use `D` as the seventh bag. It meets all four root bags through their
prescribed vertices in `Z`, and meets `U` through its neighbour at `x`.
The only possibly missing contact is between `D` and `V`. The seven
bags therefore give `K7^-` in the original graph. QED

No proper minor is asserted to be contraction-critical or six-connected.
The auxiliary graph is used only with the two rooted connectivity
conditions proved explicitly above; its virtual edges have disjoint
original-host ownership through the one reserved component `A`.
