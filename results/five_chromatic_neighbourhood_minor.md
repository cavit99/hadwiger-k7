# Five-chromatic neighbourhoods and joins force a seven-vertex minor

**Status:** written proof; separate internal audit recorded
[beside this file](five_chromatic_neighbourhood_minor_audit.md).
These are sufficient cases of the augmentation target, not its general
solution or a proof of Conjecture 19, Conjecture 21 or HC7. Novelty and
NT-comparable significance are not asserted.

All graphs are finite and simple. Let `Q7=K7-2K2`, with independent
deleted edges, and let W4 be a four-cycle with a universal hub. Thus
`Q7=K2 join W4=K3 join C4`. Extra contacts in a minor model are harmless.

## A five-chromatic neighbourhood

**Theorem 1.** Every five-connected graph H of order at least seven
with `chi(H[N_H(z)])>=5` for some vertex z contains Q7.

**Inputs.** Brooks' theorem implies that a connected five-chromatic
graph other than K5 has a vertex of degree at least five.
[Martinsson–Steiner, Theorem 1.3](https://arxiv.org/html/2209.00594v1#S1),
gives a set-rooted K4 in any four-chromatic graph whose marked set meets
every class in every four-colouring. The representatives are selected
by the theorem. The [five-root wheel theorem](hc7_rooted_wheel_extension.md)
extends a K4 rooted at four members of a five-set to a W4 rooted at all
five in a three-connected ambient graph; the fifth root may already
belong to the K4 model. These are the same inputs used in the
[four-connected five-chromatic theorem](four_connected_five_chromatic_minor.md).

**Proof.** Choose an induced vertex-minimal non-four-colourable graph
J inside `H[N_H(z)]`. Then J is connected, `chi(J)=5`, and every J-a
is four-chromatic.

If J is K5, it and z form a literal K6. Any component D outside that
clique has at least five neighbours in it: a smaller boundary would
separate D from a surviving clique vertex. The six singleton clique bags
and D have at most one missing contact and therefore contain Q7.

Otherwise choose a in J with at least five J-neighbours, using Brooks.
The set `N_J(a)` meets every class in every four-colouring of J-a,
since a missed colour would extend to J. Martinsson–Steiner supplies
four disjoint K4 bags in J-a, each containing a different J-neighbour
of a. Choose a fifth such neighbour.

The unchanged ambient graph `H-{z,a}` is three-connected. The wheel
theorem gives five disjoint connected W4 bags there, retaining the five
chosen neighbours. Those roots also neighbour z, since J lies in N_H(z).
Thus the five bags contact both singleton bags `{a}` and `{z}`, which
are adjacent to each other. They form `K2 join W4=Q7`. No contraction
of the critical core is used, and no connectivity of J-a is assumed.
QED

## Joins

**Theorem 2.** Every five-connected graph H of order at least seven
with `chi(H)>=6` and disconnected complement contains Q7.

**Proof.** Write `H=H1 join H2` with both factors nonempty, and put
`a=chi(H1)<=b=chi(H2)`. Then a+b>=6.

If a=1, any H1 vertex has a neighbourhood of chromatic number at least
b>=5. If a=2, choose an edge in H1; an endpoint's neighbourhood contains
the other endpoint joined to H2, so has chromatic number at least
b+1>=5. Theorem 1 applies in both cases.

Suppose a>=3. If either factor contains a triangle, a triangle vertex's
neighbourhood contains an edge joined to the other factor and is again
at least five-chromatic. Otherwise both factors are triangle-free and
nonbipartite. Each contains an odd cycle of length at least five. Contract
one cycle to K3 and the other to C4. These contractions occur in disjoint
factors; all cross contacts survive the join. Their seven branch sets
give `K3 join C4=Q7`. QED

Neither theorem requires a minimum-degree bound. Consequently a
counterexample to the selected augmentation target must have connected
complement and four-colourable neighbourhoods. This is a necessary
restriction, not a sufficient description of counterexamples.
