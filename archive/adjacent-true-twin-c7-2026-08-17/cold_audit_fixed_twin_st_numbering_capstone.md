# Cold audit: the fixed true-twin `C_5+K_2` seam

**Verdict: GREEN.**  I independently checked
`draft_fixed_twin_seam_st_numbering_capstone.md` at SHA-256
`0a6a7748d490d9b29811458d975aedeb63ce55e02bba0cf88d738ced965416bb`.
The stronger theorem stated there is valid: it requires no connectedness,
packet, or relative-connectivity hypothesis on the vertices outside the
seven-vertex common neighbourhood.  Seven-connectivity supplies exactly
the missing global input.

This is an internal cold audit, not external peer review.

## 1. Hypotheses checked

The theorem assumes a simple graph `G` with `kappa(G)>=7` and
`delta(G)>=8`, and adjacent true twins `a,b`.  Their full common external
neighbourhood is

```text
T = V(C) disjoint-union {e1,e2},
```

where `C` is an induced five-cycle, `e1e2` is an edge, and in total at most
one edge joins a pole to `C`.  Thus:

* each twin is adjacent to the other twin and every vertex of `T`;
* neither twin has a neighbour outside `T union {a,b}`;
* a cycle vertex has, outside the graph `H` defined below, exactly the two
  twins and its two cycle neighbours; and
* each pole has at most one cycle neighbour, with at most one such edge in
  total across both poles.

No assumption about components of `G-(T union {a,b})` is used or silently
introduced.

## 2. The complement of the cycle and twins is two-connected

Put

```text
H = G-(V(C) union {a,b}).
```

Both poles lie in `H`, and their edge puts them in one component.  If `H`
were disconnected, any other component `X` would contain neither pole.
Because components of `H` do not contact one another and vertices outside
`T union {a,b}` do not see the twins,

```text
N_G(X) subseteq V(C).
```

Deleting this set of five vertices separates nonempty `X` from (at least)
`a,b,e1,e2`, contradicting seven-connectivity.

Now suppose `z` is a cut vertex of `H`.  If `z` is not a pole, the pole edge
puts both poles in one component of `H-z`; choose a different component
`X`.  If `z` is a pole, choose a component different from the component
containing the other pole.  In both cases `X` contains no pole and

```text
N_G(X) subseteq V(C) union {z}.
```

The right side has order at most six and its deletion leaves `X` and the
twins on different sides, again contradicting seven-connectivity.

For every `c in V(C)`, interpreting `d_H(c)` as the number of neighbours of
`c` in `V(H)`, inducedness of `C` gives

```text
d_H(c) = d_G(c)-4 >= 4.
```

The optional pole--cycle edge is counted in `H`, not among the four removed
neighbours.  In particular `H` has at least four vertices.  Hence the
draft's conclusion that `H` is two-connected is valid in every pole and
non-pole cut-vertex case.

The only suggested editorial change is to define the external notation
`d_H(c):=|N_G(c) intersect V(H)|`, since `c` is not itself a vertex of `H`.

## 3. The `st` ordering is self-contained

The draft does not need to import the classical `st`-numbering theorem.  Its
ear proof is complete:

1. the prescribed edge `e1e2` lies on a cycle because `H-e1e2` has an
   `e1`--`e2` path;
2. every component outside the current subgraph has two distinct
   attachments, or one attachment would be a cut vertex;
3. a path through such a component is an open ear; and
4. inserting each ear's internal vertices, in path order, immediately
   after its earlier endpoint preserves lower- and higher-neighbour
   witnesses for old vertices and supplies them for new vertices.

Thus there is an order

```text
v1=e1, v2, ..., vn=e2
```

in which every internal vertex has an earlier and a later neighbour.  By
repeatedly following an earlier (respectively later) neighbour, every
prefix (respectively suffix) induces a connected graph.

For provenance, the standard prescribed-edge result was introduced by
A. Lempel, S. Even and I. Cederbaum, *An algorithm for planarity testing of
graphs*, in *Theory of Graphs*, 1967/68.  S. Even and R. E. Tarjan,
*Computing an st-numbering*, **Theoretical Computer Science 2** (1976),
339--344, gives the linear-time algorithm.  The application to this twin
seam is not part of those classical results.

## 4. The first-index support argument

For a cut after `v_k`, let `L_k` be the prefix, `R_k` the suffix, and let
`U_k,V_k` be their supports on the cycle.  The following points were checked
independently.

* `L_k` and `R_k` are connected.
* They are adjacent for every `1<=k<n`, because `e1` is always in `L_k`,
  `e2` is always in `R_k`, and `e1e2` is an edge.
* Every cycle vertex has an `H`-neighbour, so
  `U_k union V_k=V(C)`.
* The sole optional pole--cycle edge gives
  `|U_1|<=1` and `|V_{n-1}|<=1`.
* Consequently `|U_{n-1}|>=4`.

Let `j` be the first index with `|U_j|>=2`.  The endpoint bounds and
`|U_{n-1}|>=4` show that `2<=j<=n-1`, and minimality gives
`|U_{j-1}|<=1`.  If `|V_j|<=1`, at least three cycle vertices lie outside
`U_{j-1} union V_j`.  Since

```text
V(H) = L_{j-1} disjoint-union {v_j} disjoint-union R_j,
```

every one of those cycle vertices has all its `H`-neighbours contained in
the singleton `{v_j}`.  This contradicts `d_H(c)>=4`.  Therefore
`|U_j|,|V_j|>=2`.  All indices are valid even in the endpoint case
`j=n-1`.

At a resulting good cut both supports have order at least two and cover a
five-set, so one has order at least three.

## 5. Five-cycle arc lemma and final quotient

The draft's marker-gap proof of the arc lemma is complete.  An alternative
two-case proof is as follows.  Shrink the two supports to a disjoint
red/blue partition of the five cycle vertices of sizes two and three.  This
is possible directly when one support has order two; when both have order
at least three, assign their intersection so that two vertices go to the
first support and three to the second.  If the red vertices are adjacent,
write the cyclic order as

```text
r1,r2,b1,b2,b3
```

and take arcs `{b3,r1}`, `{r2,b1}`, `{b2}`.  If they are nonadjacent, write

```text
r1,b1,r2,b2,b3
```

and use the same three displayed arcs.  Every arc meets blue and exactly
two meet red.  Passing back to the original larger supports can only add
incidences.

For the final seven bags:

* the twins see each other, both pole-containing bags, and all three cycle
  arcs;
* the prefix and suffix see one another through `e1e2`;
* the three nonempty cyclic arcs are pairwise adjacent through the three
  cut edges of `C`; and
* among the six prefix/suffix--arc pairs, the arc lemma leaves at most one
  nonedge.

Therefore the quotient has at least 20 of the 21 edges of `K_7`, exactly as
claimed.

## 6. Independent finite falsification

`verify_fixed_twin_st_support.py` is independent of the prose proof.  It
exhausts all 576 ordered support pairs satisfying the interval lemma on a
labelled five-cycle (without assuming that the supports cover the cycle)
and all ten three-arc partitions.  It also exhausts every abstract
cycle-to-`st`-order
neighbour profile of orders five through seven in which every cycle vertex
has at least three neighbours and the two endpoint positions occur at most
once in total.  Its output is

```text
arc_support_pairs 576 best_missing_distribution {0: 216, 1: 360} GREEN
st_profile_counts {5: 11, 6: 34375, 7: 11534336} GREEN
```

The verifier SHA-256 is
`c69ddb49814be127bd3f87f1917e3eed02eb6e9a0b30d52e8a1276f3478c1efe`.
The computation deliberately checks the weaker degree-three threshold:
that is already enough for the support contradiction, so it includes every
canonical degree-four profile.  It is only a bounded falsification audit;
the theorem is unbounded because of the preceding proof.

## 7. Novelty and priority check

I searched combinations of the exact structural terms

```text
adjacent true twins / coduplicate vertices
C5 + K2 common neighbourhood
K7-minus minor
Hadwiger / complete minor
degree-eight true twins
```

and checked the currently available Norin--Totschnig paper and the local
campaign corpus.  I found no published statement matching this seam
theorem or this support-cut application.  The `st`-numbering itself is
classical, as cited above.  The use of its connected prefix/suffix cuts,
the last-support transition, and the `(2,3)` cycle-arc completion appear to
be the new part.

This is a serious but necessarily non-exhaustive priority search, not a
claim of definitive novelty.  The theorem's significance is conditional on
the audited upstream reductions that produce the literal seam; by itself it
does not prove Conjecture 21 or `(HC_7)`.
