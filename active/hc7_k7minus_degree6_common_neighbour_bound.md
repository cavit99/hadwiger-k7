# A degree-six common-neighbour bound

**Status:** written proof; separate internal audit.

This note isolates the degree-six part of Norin and Totschnig's extremal
argument and records that it needs only exclusion of a `K_7^-` minor.  It
does not use edge-maximality or a global density hypothesis.

## Theorem 1 (degree-six disk bound)

Let `H` be a five-connected graph with at least nine vertices.  Suppose that

1. `H` has no `K_7^-` minor;
2. every edge of `H` has at least four common neighbours; and
3. `H` has a vertex `v` of degree six.

Then

```text
|E(H)| <= 4|V(H)| - 9.
```

### Proof

Put `T=N_H(v)`.  For each `z in T`, the four common neighbours of `v,z`
belong to `T`, so `z` has at most one non-neighbour in `T`.  We may therefore
write

```text
T={u_1,w_1,u_2,w_2,u_3,w_3},
```

where the only possible non-edges of `H[T]` are `u_iw_i`, `i=1,2,3`.

We use the following immediate observation.

> (**Two-pair observation.**) There are no two vertex-disjoint paths, with
> open interiors outside `N_H[v]`, joining `u_i` to `w_i` and `u_j` to
> `w_j` for distinct `i,j`.

Indeed, contracting the two paths fills two of the at most three missing
matching edges in `H[T]`.  Together with the singleton bag `{v}`, the six
vertices of `T` then give a `K_7^-` minor.

All three pairs `u_iw_i` are non-edges.  Otherwise choose a component `C` of
`H-N_H[v]`, which exists because `|V(H)|>=9`.  Five-connectivity implies
that at least five vertices of `T` have neighbours in `C`.  Hence both ends
of one of the other two pairs have neighbours in `C`.  A path through `C`
joining that pair, together with the assumed edge `u_iw_i`, contradicts the
two-pair observation.

For some `i`, the vertices `u_i,w_i` have no common neighbour outside
`N_H[v]`.  If not, choose a common neighbour `x_i` outside `N_H[v]` for
each `i`.  If two of the `x_i` are distinct, the corresponding length-two
paths contradict the two-pair observation.  Thus all three may be taken to
be one vertex `x`.  The graph

```text
H-(N_H[v] union {x})
```

is nonempty.  If `C` is one of its components, then `|N_H(C)|>=5`.  Since
`v` has no neighbour in `C`, at least four vertices of `T` have neighbours
in `C`; consequently both ends of some pair have neighbours in `C`.  A path
through `C` joining that pair and a length-two path through `x` joining a
different pair are disjoint, again a contradiction.  Relabel so that
`u_1,w_1` have no common neighbour outside `N_H[v]`.

We next show that there is no nontrivial separation `(A,B)` of order five
with `N_H[v] subseteq A`.  Suppose otherwise and put `S=A intersect B`.
By the standard set-to-set form of Menger's theorem, there are five disjoint
paths in `H[A]`, internally disjoint from `N_H[v]`, joining

```text
u_1,w_1,u_2,w_2,w_3
```

to the five distinct vertices of `S`.  Denote their ends in `S`, in the
same order, by `s_1,t_1,s_2,t_2,x`.

Apply the Robertson--Seymour--Thomas two-paths theorem to `H[B]-x`, with
the cyclically ordered terminals `s_1,s_2,t_1,t_2`.  Its crossing-path
outcome, extended by the five paths above, contradicts the two-pair
observation.  Its separation outcome lifts, after restoring `x`, to a
separation of `H` of order at most four, contrary to five-connectivity.

It remains to consider the disk outcome.  Thus `H[B]-x` has a drawing in a
disc with `s_1,s_2,t_1,t_2` on its boundary in this order.  Every edge with
an end in `B-A` has at most two common neighbours in `H[B]-x`: three such
neighbours in a plane drawing put one behind a triangle containing the
edge, and that triangle, together with `x` if necessary, gives a separator
of `H` of order at most four.  Restoring `x` therefore gives an edge of `H`
with at most three common neighbours, contrary to hypothesis 2.  This proves
the asserted absence of a five-separation.

Finally apply the same two-paths theorem to

```text
H' = H-{v,u_1,w_1}
```

with terminals `u_2,u_3,w_2,w_3` in this order.  Crossing paths contradict
the two-pair observation.  A separation outcome lifts to a nontrivial
separation of `H` of order at most five whose first side contains `N_H[v]`,
contrary to the preceding paragraph.  Hence the disk outcome holds: `H'`
has a plane drawing with the four displayed terminals on the outer face.
Consequently

```text
|E(H')| <= 3|V(H')| - 7.
```

Every vertex outside `N_H[v]` has at most one neighbour in
`{v,u_1,w_1}`, by the choice of `u_1,w_1`.  Each of
`u_2,u_3,w_2,w_3` has exactly three neighbours in that triple, and the
triple itself induces two edges.  Writing `n'=|V(H')|`, we obtain

```text
|E(H)|
 <= (3n'-7) + (n'-4) + 4*3 + 2
  = 4n' + 3
  = 4|V(H)| - 9.
```

This proves the theorem.  \(\square\)

## Scope

The proof uses the forbidden-minor hypothesis only in the two-pair
observation, where the displayed construction is a `K_7^-` model, not
merely a `K_7^vee` model.  It uses the four-common-neighbour assumption in
exactly two places: to make the complement of `H[T]` a matching, and to
exclude the disk outcome inside a five-separation.  No minimal-enemy or
edge-maximality assumption is present.

## Source

The proof is an explicit hypothesis audit of the degree-six part of Sergey
Norin and Agnes Totschnig,
[*Every graph with no `K_7^vee`-minor is 6-colorable*](https://arxiv.org/abs/2507.03244),
Claims 3.12--3.15 and the final calculation in the proof of Theorem 6.
