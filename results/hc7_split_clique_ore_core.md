# Excluding the Ore core in the split-clique frame

**Status:** written proof with a [separate internal audit](hc7_split_clique_ore_core_audit.md). This closes one
explicit core configuration inside the original seven-connected host. It
does not classify all list-critical cores or close the split-clique case.
The current target remains the
[degree-seven construction](../active/hc7_c21_rooted_density_construction.md#4-what-remains-towards-hc7).

## Structural statement

Let `G` be a finite seven-connected graph. Suppose the following distinct
vertices and disjoint sets occur:

- `R=A union E` induces a five-clique, with `|A|=2` and `|E|=3`;
- `D` induces a four-clique and is disjoint from `R`;
- `u,b,y` lie outside `R union D`;
- `N_G(u)=A union D union {b}`, and `b` is adjacent to both vertices of `A`;
- `y` is adjacent to every vertex of `E union D`.

Then `G` contains a `K7` minor. No absence of additional edges is assumed,
except for the stated exact neighbourhood of `u`.

In the split-clique application, `P=A union {b}` is the triangle,
`N_G(u)=P dotunion D`, `R` meets `P` exactly in `A`, and the three
vertices of `E` lie in the exterior. The vertex `y` also lies in the
exterior and outside `R`. These hypotheses describe the literal Ore
core arising in the current list-colouring probe. The structural
statement allows arbitrarily many further vertices in the original
graph and does not require a two-exception colouring response.

## Proof

Put `H=R union D union {u,y}`. Let `C0` be the vertex set of the component
of `G-H` containing `b`. It is connected and has neighbours at `u` and
both vertices of `A`.

Every component `C` of `G-H` has at least seven neighbours in `H`.
Indeed, all its neighbours outside `C` lie in `H`; if fewer than seven
were present, deleting them would separate `C` from a vertex of `H`
outside this neighbourhood. Such a vertex exists because `|H|=11`.
Moreover, every component other than `C0` has no neighbour at `u`, by
the exact description of `N_G(u)`. Consequently every such component
has a neighbour in `D`: otherwise its neighbourhood would be contained
in `R union {y}`, a set of order six.

Let `F` be the set of vertices of `E` having no neighbour in `C0`, and
put `m=|F|`. If `m=0`, then `C0` is already adjacent to all of `R`.
The sets `C0` and `{u,d,y}`, for any `d in D`, are disjoint connected
sets, adjacent through the edge `bu`, and both meet every vertex of
`R` by an edge. Together with the five singleton vertices of `R` they
give `K7`.

Assume therefore that `1<=m<=3`. The neighbourhood of `C0` outside `D`
is contained in

`{u,y} union A union (E-F)`,

which has order `7-m`. Its total boundary has order at least seven, so

`|N_G(C0) intersection D| >= m`.                         (1)

For each `r in F`, choose a contact as follows. The only possible
neighbours of `r` inside `H-D` are the four other vertices of `R` and
`y`; it cannot see `u`. Since seven-connectivity implies minimum degree
at least seven, `r` has a neighbour either in `D` or outside `H`.

- If `r` has a neighbour `d_r in D`, choose this vertex directly.
- Otherwise choose a component `C_r` of `G-H` adjacent to `r`, and
  choose `d_r in D` adjacent to `C_r`. Such a component differs from
  `C0` because `r in F`, and its contact with `D` was proved above.

Let `D0={d_r:r in F}`. Thus `1<=|D0|<=m`. We can enlarge `D0` to a
set `D1 subseteq D` which meets `N_G(C0)` and has order at most three:

- If `D0` already meets `N_G(C0)`, take `D1=D0`.
- If `m<=2`, add one vertex of `N_G(C0) intersection D` to `D0`.
- If `m=3` and the first case does not hold, (1) implies that at most
  one vertex of `D` lies outside `N_G(C0)`. Hence `D0` is a singleton;
  adding one neighbour of `C0` gives `|D1|=2`.

Now set

`W=C0 union D1 union (union of all components C_r selected above)`.

The four-clique edges connect `D1`; it has an edge to `C0`, and each
selected component has an edge to its chosen vertex `d_r in D1`.
Thus `W` is connected. It is adjacent to every vertex of `R`: `C0`
supplies both `A` contacts and all `E-F` contacts, while each `r in F`
has its chosen direct or component contact in `W`.

Choose `d* in D-D1`, possible because `|D1|<=3`, and put

`T={u,d*,y}`.

The edges `ud*` and `d*y` make `T` connected. It is adjacent to both
vertices of `A` through `u` and to all three vertices of `E` through
`y`. Its vertices lie in `H`, whereas every component used in `W` lies
outside `H`; moreover `d*` is outside `D1`. Hence `T` and `W` are
disjoint and both avoid `R`. They are adjacent through `ub`, because
`b in C0 subseteq W`. The five singleton bags at `R`, together with
`T` and `W`, therefore form a `K7` minor. QED.

## Exact scope

This is a construction in the original host. It uses neither a
contraction-critical quotient nor a colouring extension, and the seven
bags above need no further lift. Independent domination by the sixth
colour class motivated the investigation but is not a hypothesis of
the final statement.

The preceding list-critical example shows that a minimal noncolourable
list instance can contain the displayed Ore core without itself
supplying two four-clique-full bags. The proof above explains precisely
how the original seven-connectivity excludes that example after it is
placed in the full split-clique frame. It does not show that a general
minimal list-critical instance must contain this literal five-clique
and the vertex `y` with the stated contacts. That classification or a
different construction remains necessary for the whole case.
