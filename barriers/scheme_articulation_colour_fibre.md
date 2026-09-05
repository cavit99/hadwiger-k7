# Two barriers to transporting schemes through target separations

**Status:** written proof of a barrier/counterexample to an intermediate
claim, with a separate internal audit at the exact hash recorded beside
this file. This is not a counterexample to
contractibility or to the current triangle-free classification candidate.

## Absorbing an attachment colour

**Refuted statement.** Given a properly coloured scheme of a bipartite
target block `B` with a distinguished prescribed root `v`, there is always
a fully rooted `B`-minor whose `v` branch set contains every host vertex
of colour `v`.

This extra requirement was proposed to glue a block to the rest of a
target at `v`: absorbing the shared colour into the `v` bag would let
the rest of the scheme continue through a single identified vertex.
Ordinary full rooted contractibility has no such colour-class containment
conclusion.

## Explicit scheme

Take target cycle `v,a,b,c,v`. Its four named vertices are the prescribed
roots. Add nonroots `v_1,v_2,a_1,b_1,c_1`, coloured by their letter, and
take precisely the edges of these four paths:

```text
P_va = v,a_1,v_1,a
P_ab = a,b_1,a_1,b
P_bc = b,c_1,b_1,c
P_cv = c,v_2,c_1,v.
```

Each path is simple and contains no other prescribed root internally.
Its colours alternate between its target endpoints. Every host vertex
belongs only to paths incident with its colour, so the path-intersection
condition holds for every collection of paths. This is a properly
coloured scheme. No minimum nonroot degree is assumed in the refuted
statement: `v_1,v_2` each lie on one path in this block, as can happen
when other paths using their colour belong to another target block.

## Contradiction to colour-class containment

Suppose four disjoint connected branch sets form the prescribed rooted
cycle and that `C_v` contains `v_1,v_2`. The only neighbours of `v_1`
are `a_1,a`. Since `a` belongs to its own prescribed branch set,
connectivity of `C_v` forces `a_1 in C_v`. Similarly the two neighbours
of `v_2` are `c_1,c`, forcing `c_1 in C_v`.

The only neighbours of root `b` are `a_1,c_1`. They both belong to
`C_v`, so the disjoint connected set `C_b` is necessarily `{b}` and
has no contact with `C_a` or `C_c`. Both contacts are required by the
target cycle. This proves the refutation for arbitrary connected
branch sets.

An ordinary fully rooted model exists:

```text
C_v={v},   C_a={a,v_1,a_1},
C_b={b},   C_c={c,v_2,c_1}.
```

The four contacts are witnessed respectively by `v a_1`, `a_1 b`,
`b c_1`, and `c_1 v`. Each displayed set is connected, they are
disjoint and contain their prescribed roots. Vertex `b_1` is unused.

## Exact failure and remaining possibility

The first unsupported inference in the proposed local gluing proof
was strengthening a fully rooted block model to one containing the
whole attachment colour class in a single bag. The explicit scheme
excludes that strengthening even though the block is bipartite and
the ordinary rooted conclusion holds.

This example does not disprove contractibility of a graph formed by
attaching bipartite blocks, nor the candidate classification by exclusion
of skewed thetas and one odd-cycle-cover edge per component. It does
not itself supply a scheme for any larger target. A valid gluing proof
can still coordinate ownership of shared-colour vertices across the
blocks or replace local gluing by a global root-preserving reduction.
No computer enumeration is a premise of this nine-vertex construction.

## A Whitney switch cannot just relabel one side's path incidences

**Barrier/counterexample to an intermediate transport rule.** Suppose a
target is the union of two edge-disjoint subgraphs meeting in two
vertices `u,v`. A Whitney switch interchanges `u,v` in the endpoints of
every edge on one side. The following proposed rule is false: transport
an arbitrary scheme by relabelling the demands on that side while
retaining each path's nonroot vertices. The failure occurs in the
intersection axiom, independently of the separate task of reconnecting
the paths to the newly demanded prescribed roots.

Take the target cycle

```text
H = u,a,b,v,c,d,u,
E_1 = {ua,ab,bv},   E_2 = {vc,cd,du}.
```

Switching `u,v` on `E_2` gives

```text
H' = u,a,b,v,d,c,u,
E'_2 = {uc,cd,dv}.
```

For each target vertex `x`, let `x_0` be its prescribed root and `x_1`
a nonroot of colour `x`. In the canonical two-copy scheme, the path
for edge `xy` is `x_0,y_1,x_1,y_0`. Each path is simple and properly
coloured; a nonroot of colour `x` occurs precisely on paths for edges
incident with `x`. In particular,

```text
P_ua = u_0,a_1,u_1,a_0,
P_du = d_0,u_1,d_1,u_0.
```

They share the nonroot `u_1`. After the proposed one-sided switch,
their demands would be `ua` and `dv`. Those two edges of `H'` have no
common endpoint. Thus any two paths retaining that shared nonroot
violate the scheme intersection axiom, even if their endpoints could
otherwise be reconnected to the desired roots. Recolouring `u_1`
cannot repair an empty intersection of target endpoint sets.

This example refutes the stated incidence-preserving transport rule.
It does not refute preservation of contractibility under Whitney
switches: both displayed targets are cycles and are contractible by
Kündgen--Pelsmajer--Ramamurthi,
[Theorem 4.2](https://arxiv.org/html/1207.6141).
Splitting a shared nonroot into separate copies changes the host and
requires a new lift argument: a returned model must be chosen so that
distinct branch sets do not use copies of the same original vertex.
Neither a target cycle-matroid equivalence nor ordinary rooted
contractibility supplies that compatibility. The smallest missing
repair is a simultaneous allocation of the two separator colour
classes, or another scheme transformation with an explicit valid lift.
