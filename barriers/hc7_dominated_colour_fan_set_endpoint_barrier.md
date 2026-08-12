# Set-rooted Kempe components do not complete a colour-rooted five-fan

**Status:** barrier/counterexample to an intermediate claim;
computer-assisted finite result; internal self-audit adjacent.  This is not
a counterexample to the dominated-centre theorem, Conjecture 21, or `HC_7`.

The deterministic verifier is
[`hc7_dominated_colour_fan_set_endpoint_barrier_verify.py`](hc7_dominated_colour_fan_set_endpoint_barrier_verify.py).

## 1. Refuted inference

The following local implication is false.

> Let a seven-set `Q` be partitioned into five nonempty independent colour
> blocks.  Choose one root from each block and a rooted
> `F_5=K_1\vee P_4` model on those roots.  For the two disjoint missing
> pairs `ac,bd` of the path roles, suppose there are two vertex-disjoint
> connected subgraphs meeting the corresponding pairs of colour blocks.
> Then the union contains a `K_5^-` minor whose five branch sets meet `Q`.

The construction below has no `K_5^-` minor at all.

## 2. Construction

On `Q={0,1,2,3,4,5,6}`, take

```text
0-3-6-2-5-0    and    1-4.
```

Thus `G[Q]=C_5\mathbin{\dot\cup}K_2`, one of the three surviving
dominated-centre common-neighbour graphs.  Partition `Q` into the five
independent blocks

```text
A={0,1,2},  B={3},  C={4},  D={5},  E={6}.
```

Use the rainbow roots `0,3,4,5,6`.  On them add the rooted five-fan with
hub `3` and path

```text
0-5-4-6,
```

so the two disjoint missing path pairs are `A-C` and `D-E`.

Add two new vertices `x,y` and precisely the four connector edges

```text
1-x, x-4, 5-y, y-6.
```

The paths `1-x-4` and `5-y-6` are vertex-disjoint.  The first meets the
colour blocks `A,C`, and the second meets `D,E`, exactly as supplied by the
set-valued bichromatic-component lemma.  The first path nevertheless meets
`A` at vertex `1`, not at the selected `A`-root `0`.

## 3. Exact verification

The verifier enumerates every choice of five nonempty branch sets on every
subset of the nine vertices.  It tests connectivity and all ten pairwise
branch-set adjacencies directly.  There are 22,827 set partitions to test,
of which 3,058 have five connected bags.  None has nine adjacencies, so the
graph has no `K_5^-` minor.

Run from the repository root:

```text
python3 barriers/hc7_dominated_colour_fan_set_endpoint_barrier_verify.py
```

The expected output is

```text
set_endpoint_barrier partitions_tested=22827 connected_five_bag_models=3058 K5_minus_minor=False
```

## 4. Scope

This barrier isolates the first quantifier loss in the colour-guided fan
proposal.  A bichromatic component meeting `Q_A` and `Q_C` need not meet
the chosen `A`- and `C`-rooted bags.  The failure remains even when the
second connector has the exact selected roots and both connectors are
clean outside the singleton fan bags.

The nine-vertex graph is not claimed to be five-connected,
seven-chromatic, contraction-critical, or compatible with the full
two-shore response.  It therefore does not refute a protected fan-exchange
theorem using those host hypotheses.  It shows only that set-valued Kempe
completeness cannot by itself be composed with an arbitrarily labelled
rooted-five-fan model.
