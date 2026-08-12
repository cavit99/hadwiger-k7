# Internal audit: portal-edge threshold reduction

**Verdict:** GREEN for Theorem 2.1, Lemma 3.1, and the stated route
nonclosure.  This is a separate internal mathematical audit, not external
peer review.

## 1. Exact revision and scope

The audited source is
[`hc7_k7minus_portal_edge_cycle_threshold.md`](hc7_k7minus_portal_edge_cycle_threshold.md),
with SHA-256

```text
0a4c9046015984e9701c1c8911d2552ad669fbc6f792b309a679973d09808a54
```

The source was promoted from `active/` after the audit; only its status and
audit link changed.  Its mathematical content is unchanged.

The source assumes the seven-connected row of the six-coordinate forest
reduction: both `G` and `X=G-F` are seven-connected, `delta(G)>=8`, and
`F` is either a matching of order six or `4K_2` together with an induced
path `s-r-t`.  The selected portal edge `e` is required to be disjoint
from `V(F)`.  The note makes no claim about a portal edge incident with a
forest vertex.

## 2. External theorem statements

The four external inputs were checked at the quantifiers actually used.

1. Haggkvist--Thomassen: `k` independent edges in a
   `(k+1)`-connected graph lie on one cycle.  The source applies this only
   with six independent edges in the seven-connected graph `G`.
2. Denley--Wu: if independent nontrivial paths have total length `s`, and
   `T` consists of `t>=1` further prescribed vertices, then an
   `(s+t)`-connected graph has a cycle containing all those paths and
   vertices.  This is Corollary 3.4 of the original paper (also quoted as
   Theorem 6(1) in Gould's cycle survey).  The source uses `s=6,t=1`, with
   the prescribed vertex disjoint from all six one-edge paths.
3. Kawarabayashi, Theorem 2: if `L` is a set of `k` independent edges in
   a `k`-connected graph and either `k` is even or `G-L` is connected,
   then `L` is contained in one cycle or in the union of two
   vertex-disjoint cycles.  This exact statement is reproduced as
   Theorem 1.3 by Knappe--Pitz.
4. Knappe--Pitz, Theorem 1.4: a connected graph contains a closed trail
   through every prescribed set of `k` edges if and only if it has no odd
   cut of order at most `k`.  This is a global characterisation.  The
   source uses it correctly as the dichotomy: either there is such a small
   odd cut, or every chosen seven-edge set lies on a closed trail.

In particular, none of these results asserts that seven independent edges
in a seven-connected graph lie on one cycle.  The Haggkvist--Thomassen
theorem would require eight-connectivity, while the Denley--Wu theorem at
connectivity seven requires at least one prescribed vertex and hence
allows total prescribed path length at most six.

## 3. Matching case of Theorem 2.1

When `F` is a matching and `e` is disjoint from it,

```text
L = F union {e}
```

is a set of seven independent edges.  The identity `G-L=X-e` is exact.
Since `X` is seven-connected, it has no bridge, so `X-e` is connected.
Kawarabayashi therefore supplies the claimed one-cycle or two
vertex-disjoint-cycle cover.

For an omitted edge `f=uw`, the set `(F-{f}) union {e}` consists of six
independent one-edge paths.  Either chosen end of `f` is outside all those
paths.  Denley--Wu with `s=6,t=1` gives the displayed omitted-coordinate
cycle.  No step infers that the other end of `f`, or `f` itself, belongs
to that cycle.

## 4. Induced-path case of Theorem 2.1

Write `F=M_0 union {rs,rt}`.  Componentwise inducedness gives
`st notin E(G)`, so the edge `st` introduced in

```text
G' = (G-r)+st
```

is genuinely artificial.  Removing one vertex from the seven-connected
graph `G` leaves `G-r` six-connected, and adding an edge cannot reduce
connectivity.  Because `e` is disjoint from `V(F)`, the set

```text
L' = M_0 union {st,e}
```

consists of six independent edges in the six-connected graph `G'`.
Evenness of six alone satisfies Kawarabayashi's hypothesis.  The additional
identity

```text
G'-L' = X-r-e
```

is also correct; its right-hand side is connected because `X-r` is
six-connected and hence has no bridge.

Every cycle cover of `L'` contains the artificial edge `st` on exactly
one of its cycles.  Replacing that occurrence by `s-r-t` produces a
simple cycle: `r` was deleted from `G'` and is therefore new to the cycle.
If Kawarabayashi returned two vertex-disjoint cycles, the second avoids
`s,t`, and also avoids the new vertex `r`; vertex-disjointness is therefore
preserved after lifting.  The lifted cycle or pair of cycles contains all
of `F union {e}`.

Finally, `M_0 union {rs,e}` and `M_0 union {rt,e}` are each sets of six
independent edges.  The two Haggkvist--Thomassen applications are valid
and make no compatibility claim between their resulting cycles.

## 5. Seven-edge-cut lemma

Whitney's inequalities give edge-connectivity at least seven from
seven-vertex-connectivity.  Hence a nonempty cut of order at most seven
has order exactly seven.

For one shore `A`, let `S_A` be the ends in `A` of its seven cut edges.
If `A=S_A` and `m=|A|<=7`, minimum degree eight gives

```text
7 = |delta(A)| >= m(9-m) > 7,
```

a contradiction.  Thus `A-S_A` is nonempty, and the symmetric statement
holds on the other shore.  Removing `S_A` is now a proper vertex cut, so
seven-connectivity forces `|S_A|>=7`.  Since there are only seven cut
edges, equality holds.  Repeating the argument on the other shore shows
that all seven cut edges have distinct ends on both sides and that either
endpoint set is the separator of a proper order-seven separation.

The separator furnished by this lemma need not retain one of the selected
forest coordinates or the selected portal edge.  The source does not
claim that stronger labelled conclusion; it is explicitly left for the
proposed two-cycle composition theorem.

## 6. Route boundary

In the matching case, upgrading Kawarabayashi's cover from at most two
cycles to one cycle using only the displayed connectivity hypotheses is
exactly the parameter-seven Lovasz--Woodall assertion.  In the induced-path
case, suppressing the internal path vertex produces the corresponding
parameter-six assertion.  The conjecture is known through parameter five,
but no published general parameter-six or parameter-seven theorem was
identified.  The source therefore correctly labels the one-cycle inference
as unsupported rather than treating Kawarabayashi's outline of a full proof
as a published theorem.

The proved output is a two-cycle reduction, not a `K_7^-` model and not a
six-colouring of `G`.  Merging the cycles still has to use information
specific to this host, such as the exact near-clique branch bags, the
punctured signature cube, or a response-bearing separation.  The proposed
two-cycle portal-composition statement remains a conjectural next target.
