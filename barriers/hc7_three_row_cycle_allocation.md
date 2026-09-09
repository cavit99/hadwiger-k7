# Three path rows with distinct contacts need not give Q

**Status:** explicit counterexample with a written proof and a separate
internal audit. Here `Q=K7-2K2`, with independent deleted edges.

The three common rows in the
[Q-free transfer theorem](../results/hc7_q_free_rotation_separator.md)
may all be paths, each contacting the four outside vertices at four
distinct vertices, without a Q minor. Thus distinct contacts and a joint
choice across three path rows do not alone close that theorem's residue.
The example is three-connected and three-chromatic, not an actual
seven-connected critical host.

## Construction

Take a cycle `z0,...,z11,z0` and five further vertices `x0,x1,x2,x3,p`.
Join zi to x_s(i), where the cyclic word s is

`0123 | 1023 | 3012`.

Add `x0x2`, `x1x3` and all four edges from p to the x vertices. There
are no other edges. The three consecutive four-vertex cycle paths are
pairwise adjacent and each contacts all four x vertices at distinct
vertices. With centres x0,x2, missing rows x1,x3 and gate {p}, these
paths are exactly the three common rows of an equal-pair transfer.

## Every possible Q model has a restricted form

Suppose a Q model exists. Since the host is connected, extend it to a
spanning model by absorbing unused components into adjacent bags. Each
bag must contact at least five other bags.

The bag containing p must contain an x vertex: p has only four neighbours,
and every path from p to the cycle passes through an x vertex. A bag
containing no x vertex is therefore a cycle interval. It is proper,
since a bag containing the entire cycle would leave at most five more
bags. An interval of length l has at most l+2 neighbours outside itself,
so every such bag has length at least three.

There are at most four bags containing x vertices. If there were at most
three, the length bound would force exactly four cycle-only bags,
consuming the whole cycle as four triples. Their contact graph is a four-cycle, already accounting
for both missing edges of Q. All remaining bags would have to contact
all four triples. But some bag would contain just one x vertex, possibly
with p, and only its three cycle neighbours would be available. This is
impossible. Thus there are exactly four x-containing bags, one per x
vertex, and three cycle-only bags.

The three cycle-only bags must have at least two mutual contacts: two
missing edges on three vertices cannot be independent. Their complement
on the cycle is consequently one consecutive block, called the head.
Its length h is at most three. For h=0 the four x-containing bags have
only four mutual edges, with the two holes sharing an end. For h=1 its
vertex must join its own x bag and supplies no new such edge. Both fail.

For h=2, at most one new edge between x-containing bags can be supplied:
either the two head vertices have different owners and their cycle edge
is new, or they share one owner and only the other vertex's spoke is new.
The two holes must therefore be precisely the remaining hole
between x bags and the hole between the end cycle bags. Every cycle bag
must contact all four x bags. The middle cycle bag has no edge to the
head, so needs four vertices. The three interval lengths are thus 3,4,3.

For h=3 the three interval lengths are 3,3,3. The middle interval has at
most three x contacts. Together with the missing contact between the
end intervals, this uses both holes; the four x bags must form a clique.
Each end interval must contact all four x bags.

## The remaining positions fail

Number head starts from 0 to 11, modulo 12. A cycle vertex owned by the
bag of xj is denoted by j, whether or not that bag also contains p.
An end interval's three spoke labels, together with the owner of the
adjacent head vertex, must contain all four labels. The middle interval
needs four distinct labels when h=2 and three when h=3.

Reading the displayed word gives exactly the following positions meeting
these necessary interval conditions. All other positions have a repeated
label in an interval that requires distinct labels.

| h | Head start | Head labels | Forced end owners | Possible connected owner strings |
|---|---:|---|---|---|
| 2 | 3 | 31 | 3,1 | 31 |
| 2 | 7 | 33 | 3,3 | 33 |
| 2 | 11 | 20 | 2,0 | 20 |
| 3 | 2 | 231 | 3,1 | 331 |
| 3 | 5 | 023 | 0,2 | 022 |
| 3 | 6 | 233 | 2,3 | 223 or 233 |
| 3 | 7 | 330 | 3,3 | 333 |
| 3 | 8 | 301 | 1,3 | none |
| 3 | 11 | 201 | 2,0 | 200 |

The owner strings follow directly from connectedness. Each head portion
assigned to a bag must reach a head vertex with that bag's own spoke
label. For instance, in head 231 with end owners 3,1, the middle vertex
must belong to 3, giving 331. In head 301 with end owners 1,3, the first
owner could reach its spoke only through the entire head, contradicting
the last owner.

For h=2, strings 31 and 20 use an existing paired edge and string 33
supplies no new edge. Thus the x bags still have only four mutual edges,
where five are required. For h=3, each listed owner string supplies at
most one new edge: respectively 23, 23, 23, 03 and 01. The x bags then
have at most five mutual edges, where six are required. This holds for
every choice of the x vertex sharing p. Every possible model has failed,
so the graph is Q-minor-free. No computation is a premise.

## Unaffected scope

The graph has minimum degree three and is three-connected. After deleting
two cycle vertices, every remaining cycle component attaches to the
connected outside star. After deleting one cycle vertex and one outside
vertex, the surviving cycle path joins every surviving x vertex. After
deleting two outside vertices, the intact cycle does the same. In each
case a surviving p still has a surviving x neighbour.

It is exactly three-chromatic. Give p colour 3, give x0,x1 colour 1 and
x2,x3 colour 2. Give even-indexed cycle vertices colour 3 and each
odd-indexed vertex the colour in {1,2} opposite its x neighbour. A
triangle through p supplies the lower bound.

The first false inference is that spreading the four contacts along each
of the three common rows forces a joint Q construction. The actual-host
attack may still use seven-connectivity, minimum degree eight and the
critical colouring constraints. None of those is supplied by this example.
