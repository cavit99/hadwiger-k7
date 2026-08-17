# The packet-free side of a two-root exact-six return is oriented

**Status:** proved unbounded structural reduction; independently cold-audited.
In the exceptional `(2,0,1)` packet-transfer row, deleting the
derived fragment and the two exchanged portals leaves only one-portal
components.  Every such component sees all four common roots and exactly
one of the two missing roots.  Components meeting both portals are already
terminal.

Write `K_7^-` for `K_7` with one edge deleted.  Let `G` be a
six-connected graph with no `K_7^-` minor, let `S` be a six-cut, and suppose
that `G-S` has at least three connected `S`-full components.  Fix one of
them, `C`, and choose two others, `A,D`.

Complete `S` to a clique in the closed `C`-shore.  Let `T` be an order-six
cut in the completed shore, and let `L` be a component behind `T`, remote
from `S-T`.  Assume

```text
Z=S intersect T={z_1,z_2,z_3,z_4},
R=T-S={r_1,r_2},
Q=S-T={q_1,q_2}.                                    (1)
```

Thus `N_G(L)=T`.  Suppose that `L` contains two disjoint connected
`T`-full packets `P_1,P_2`, and that `C-L` contains no connected
`S`-full packet.  Assume also that `mu_S(C)=1`.  These are precisely the
local hypotheses supplied by the exceptional `(2,0,1)` row of the audited
two-packet transfer theorem.

Put

```text
W=C-(L union R).                                    (2)
```

Call the components of `G[W]` **cells**.

## Lemma 1 (a portal and two common contacts are terminal)

Let `E` be a connected subgraph of `G[C-L]`.  If

```text
E intersect R is nonempty,
Q subseteq N_G(E),
|N_G(E) intersect Z|>=2,                            (3)
```

then `G` contains a `K_7^-` minor.

### Proof

Choose distinct `z_3,z_4 in N_G(E) intersect Z`, and let `z_1,z_2` be the
other two vertices of `Z`.  The seven bags

```text
P_1 union {z_1},    P_2 union {z_2},
{z_3},              {z_4},
A union {q_1},      D union {q_2},
E                                                     (4)
```

are pairwise disjoint and connected.  The first four are pairwise
adjacent except possibly for `{z_3}{z_4}`.  The two outer bags are adjacent
to every one of the first four by fullness, and they are adjacent to one
another through either literal vertex of `Q`.  The bag `E` meets both
outer bags through its two `Q`-contacts.  It meets the two singleton bags
through `z_3,z_4`.  Finally, a vertex of `E intersect R` is adjacent to
both `P_1` and `P_2`, because both packets are `T`-full.  Thus (4) misses
at most the pair `{z_3}{z_4}` and is a `K_7^-` model.  \(\square\)

## Lemma 2 (cell contacts)

Every cell `X` meets at least one portal.  More precisely:

1. if `|N_G(X) intersect R|=1`, then

   ```text
   N_G(X) intersect S=Z union {q}
   ```

   for exactly one `q in Q`;
2. if `N_G(X)` meets both portals, then it meets at most one vertex of
   `Q` and at least three vertices of `Z`.

### Proof

There is no edge from `X` to `L`: every neighbour of `L` in `C` belongs
to `R`.  Distinct cells have no edge between them, and no component of
`G-S` has an edge to another.  Hence

```text
N_G(X) subseteq S union R.                           (5)
```

The set `N_G(X)` separates `X` from `A`, so six-connectivity gives
`|N_G(X)|>=6`.  On the other hand, `X` itself is a connected subgraph of
`C-L`; the packet-free hypothesis therefore gives

```text
|N_G(X) intersect S|<=5.                            (6)
```

Equations (5)--(6) force a portal contact.

If there is exactly one portal contact, then equality holds throughout:
`|N_G(X) intersect S|=5`.  If both vertices of `Q` were present, the
connected set consisting of `X` and its portal would satisfy Lemma 1,
because it would also see three vertices of `Z`.  Thus exactly one vertex
of `Q` is present and all four vertices of `Z` are present.

If both portals are present, (5) gives at least four contacts in `S`.  Both
vertices of `Q` together with those contacts would leave at least two
contacts in `Z`, again contradicting Lemma 1 after adjoining either
portal.  Hence at most one vertex of `Q` is present, and at least three
vertices of `Z` are present.  \(\square\)

## Lemma 3 (two-portal cells are impossible)

No cell meets both vertices of `R`.

### Proof

The saturated opposite-side linkage supplies two disjoint paths from `R`
to `Q` in

```text
G[(C-L) union Q]-Z,                                 (7)
```

saturating both endpoint sets.  Relabel so that the path beginning at
`r_i` ends at `q_i`.  A trimmed path avoids the other portal.  It is
therefore either the edge `r_iq_i`, or its internal vertices lie in one
cell adjacent to both `r_i` and `q_i`.

Suppose a cell `X` meets both portals.  Lemma 2 says that it sees at least
three vertices of `Z` and at most one vertex of `Q`.

If `X` sees `q_1`, take the `r_2`--`q_2` linkage path and let `Y` be its
internal cell, if it has one.  The connected set

```text
X union {r_2} union Y                               (8)
```

(with `Y` omitted for a one-edge path) meets both vertices of `Q`, a
portal, and at least three vertices of `Z`.  Lemma 1 is a contradiction.
The case in which `X` sees `q_2` is symmetric.

If `X` sees neither vertex of `Q`, join it to both linkage paths.  The
union of `X`, both portals, and the two internal path cells is connected,
meets both vertices of `Q`, and sees at least three vertices of `Z`.
Lemma 1 is again a contradiction.  \(\square\)

## Theorem 4 (oriented packet-free complement)

Every cell meets exactly one portal and has the form

```text
N_G(X) intersect (S union R)
   ={r_i} union Z union {q_j}                       (9)
```

for some `i,j in {1,2}`.  For a fixed portal `r_i`, all cells incident
with `r_i` use the same vertex of `Q`.  If such a cell exists, every direct
edge from `r_i` to `Q` uses that same vertex.

After relabelling the saturated linkage, the following sharper statement
holds:

* every cell at `r_i` has boundary `{r_i} union Z union {q_i}`;
* if `r_i` has a cell, then `N_G(r_i) intersect Q subseteq {q_i}`;
* a portal with no cell is adjacent to its matched `q_i`, and it is the
  only kind of portal that can have an additional direct edge to the other
  vertex of `Q`; at most one portal has such an additional edge.

In particular, if both portals have cells, `C-L` has exactly two connected
components, one on each portal, and their original-boundary neighbourhoods
are

```text
Z union {q_1}     and     Z union {q_2}.             (10)
```

### Proof

Lemmas 2--3 give (9).  Suppose two cells incident with the same portal use
different vertices of `Q`.  Their union with the portal is connected,
meets both vertices of `Q`, and sees all of `Z`, contrary to Lemma 1.  The
same argument, using one cell and a direct edge from the portal to the
other vertex of `Q`, proves the assertion about direct edges.

The saturated linkage gives each portal a contact with a distinct vertex
of `Q`, either directly or through an incident cell.  Thus a portal which
has a cell must use the matched vertex throughout, giving the first two
bullets.  A portal without a cell can support its linkage path only by a
direct edge.  If both portals had direct edges to both vertices of `Q`,
then `P_1 union {r_1}` and `P_2 union {r_2}` would be two disjoint
`S`-packets in `C`, contrary to `mu_S(C)=1`.  This gives the third bullet.

Finally assume both portals have cells.  Their forced `Q`-contacts are
distinct.  By Lemma 3 no cell joins the two portals.  Also `r_1r_2` is not
an edge: if it were, take one incident cell at each portal; their union
with `r_1,r_2` would satisfy Lemma 1.  Hence the two portal stars are the
two components of `C-L`, and (10) follows from (9).  \(\square\)

## Exact remaining geometry

The theorem converts the exceptional packet vector `(2,0,1)` into an
oriented interface.  Away from a possible cell-free portal, every piece
behind the exchange has an exact order-six boundary obtained from `S` by
replacing one vertex of `Q` by its portal.  The two orientations are
opposite because the saturated linkage uses distinct ends.

Thus the remaining unbounded obstruction is no longer arbitrary failure
of a two-copy linkage.  It consists of two five-root-full portal shores,
each missing the root supplied by the other shore, together with the
possible degenerate case of a portal whose entire return is by literal
edges to `Q`.  Eliminating this oriented interface, or showing that its
exact-six subfragments strictly decrease the coefficient-four potential,
is the next transfer target.

## Pinned dependencies

* two-packet transfer obstruction, final source SHA-256
  `99b59c50f39b43653348997e137d799ff47d8c9e7f402b8dc330e481fd424416`,
  independent GREEN audit SHA-256
  `fd9bb404244c0dc247a9d30480e83bfec356ca2d686a64f23e91cfa5164cfc46`;
* saturated opposite-side linkage, source SHA-256
  `53c91cee74ae8b1f5251e13c14095f8abc65f05625eedb401d3d53173996da15`,
  independent GREEN audit SHA-256
  `c30aa69b6919edd2cfba80d6df1f02e2c75d38d9544bd87e4332ba4d823526a3`.
