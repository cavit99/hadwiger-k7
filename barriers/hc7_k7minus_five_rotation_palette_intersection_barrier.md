# Five singleton saturation rows do not force a common missing colour

**Status:** barrier/counterexample to the palette-only intermediate claim
below; separate internal audit GREEN in
[`hc7_k7minus_five_rotation_palette_intersection_barrier_audit.md`](hc7_k7minus_five_rotation_palette_intersection_barrier_audit.md).
This is not a graph counterexample and does not satisfy the full
critical-host hypotheses.

## 1. The false local principle

Let `Z` be a set of five centres.  For each `r in Z`, suppose one has a
six-colour row with the following data.

1. The eight neighbour slots of `r` use all six colours and at least four
   colours occur once.
2. Every `z in Z-\{r\}` has a colour missing from its own eight neighbour
   slots, so the row saturates exactly `r`.
3. Write `L_z` for the set of colours missing at `z`.

The tempting inference was that some row and some pair `\{a,b\}` of
singleton colours at its root satisfy at least one of

\[
 \{a,b\}\cap\bigcap_{z\ne r}L_z\ne\varnothing,       \tag{1.1}
\]

or

\[
 \{a,b\}\cap\{\text{colours on }Z-\{r\}\}
                         =\varnothing.                \tag{1.2}
\]

Condition (1.1) is the common-missing-colour normalization in the global
rotation theorem.  Condition (1.2) is its common-partition fallback.  The
three local assumptions do not imply either condition.

## 2. Counterexample

Use the colour set `\{0,1,2,3,4,5\}` and the five neighbour-slot rows

\[
\begin{aligned}
 R   &=(0,1,2,3,4,4,5,5),\\
 P_0 &=(1,1,2,2,3,4,5,5),\\
 P_1 &=(0,0,2,2,3,4,5,5),\\
 P_2 &=(0,0,1,1,3,4,5,5),\\
 P_3 &=(0,0,1,1,2,4,5,5).
\end{aligned}                                      \tag{2.1}
\]

For each root `r`, assign the other four centres bijectively to
`0,1,2,3`.  Give a centre assigned `c` the colour `c` and use `P_c` on its
neighbour slots.  Use `R` on the neighbour slots of `r`.

The row `R` uses all six colours and has singleton colours
`0,1,2,3`.  The row `P_c` omits exactly `c`, so the displayed colour of
every non-root centre is absent from its neighbourhood.  Thus the row
saturates exactly its root, as required.

On every root row,

\[
 \{L_z:z\ne r\}=\{\{0\},\{1\},\{2\},\{3\}\},
 \qquad
 \bigcap_{z\ne r}L_z=\varnothing.                   \tag{2.2}
\]

Hence (1.1) fails for every pair.  The colours on the four other centres
are exactly `\{0,1,2,3\}`.  Every pair of singleton root colours is a
subset of that set, so (1.2) also fails.

## 3. Exact scope

The construction refutes only an inference from the five local colour
palettes.  It does not encode one graph, adjacency consistency between
overlapping neighbourhoods, contraction-criticality, seven-connectivity or
`K_7^-`-minor exclusion.  Those additional hypotheses may still force a
normalization.

The common-matching theorem avoids the false inference: instead of seeking
one common missing colour among five unrelated rows, it deletes five
vertex-disjoint centre edges and realizes all nonempty equality signatures
on one literal six-chromatic graph.
