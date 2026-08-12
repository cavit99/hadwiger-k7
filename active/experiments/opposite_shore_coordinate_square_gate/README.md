# Opposite-shore coordinate-square proof gate

**Status:** bounded hostile diagnostic with an explicit deterministic
survivor; [verification audit GREEN](verification_audit.md).  This is not a theorem about the critical host and not a
counterexample to the `K_7^-` six-colour conjecture or `HC_7`.

## Question tested

The final order-eight or order-nine six-cut residue has two selected forest
coordinates entering opposite full components.  The proposed positive
argument uses the three nonempty signatures

\[
             EP,\qquad PE,\qquad EE,
\]

where `E` means that a selected edge has equal-coloured ends and `P` means
that its ends have different colours.  The critical host forbids the fourth
signature `PP`, since it would be a proper six-colouring after both edges
were restored.

The first proof gate asks whether the following weaker collection of data
already forces a boundary-partition collision or a `K_7^-` minor:

1. an order-eight boundary with two anticomplete boundary-full components;
2. one selected coordinate entering each component;
3. all three nonempty signatures;
4. a coloured six-fan on each selected shore;
5. exact six-chromaticity after contracting either coordinate or both;
6. one common spanning `K_6` model co-bagging both coordinate pairs; and
7. no connected proper subset of either component with neighbourhood order
   seven.

The answer is no if the empty signature is not explicitly forbidden.

## Fixed survivor

Use the boundary

```text
T = t0 t1 p x b c u3 u4
```

and the two open components `c0-c1` and `d0-d1`.  There are no edges
between the two components.  Inside `T`, take the edges

```text
p-x p-u3 p-u4
b-c b-u3 b-u4
c-u3 c-u4
u3-u4
```

The boundary contacts are

```text
c0: t0 t1 x b c u3 u4
c1: t0 p
d0: t0 t1 x b c u3 u4
d1: t1 p
```

and the selected coordinates are

```text
e = c0-t0,    f = d0-t1.
```

Each open component is adjacent to every member of `T`.  The only proper
connected subsets of either component are its singleton vertices; their
neighbourhood orders are `8,3` on each shore, so none gives the strict
order-seven outcome.

After deleting `e,f`, the following seven branch sets form a spanning exact
`K_7`-with-two-adjacent-edges-missing model:

```text
P  = {p,x}              U1 = {c0,c1,t0}
B  = {b}                U2 = {d0,d1,t1}
C  = {c}                U3 = {u3}
U4 = {u4}
```

Only `PB` and `PC` are absent.  More importantly for the strengthened proof
gate, the six branch sets

```text
{c0,c1,t0}, {d0,d1,t1}, {b}, {c}, {u3,p,x}, {u4}
```

form one spanning `K_6` model in the same double-deletion graph.  They
co-bag both `e` and `f`; this is not merely a pair of unrelated rooted
models.

For either coordinate bag, every connected split separating the selected
ends has at most two of the five foreign bags adjacent to both sides.  Thus
the usual four-foreign-bag split certificate is genuinely blocked on both
shores, even though the two coordinates share one model.

The exact finite checks give

\[
 \chi(G/e)=\chi(G/f)=\chi(G/\{e,f\})=6,
 \qquad K_7^-\npreccurlyeq G.
\]

All four endpoint signatures occur.  Enumerating the proper equality
partitions of `T` gives the following language sizes:

```text
PP 361
EP  56
PE  56
EE  14
```

The `EP` and `PE` boundary-partition languages are disjoint.  Nevertheless
each has a colouring whose selected equal edge is accompanied by a
shore-confined six-fan with six distinct boundary ends.

## Meaning of the survivor

The survivor does **not** refute the intended host-level disjunction.  It
has the forbidden `PP` signature, is five-colourable, has connectivity
three and has vertices of degree three.  A `PP` colouring itself gives a
partition extending through both shores, so the broad common-partition
outcome is already present.

It does prove a narrower and useful negative finding:

> The three positive vertices of the response square, exact contraction
> chromaticity, two coloured singleton fans and a common co-bagged spanning
> `K_6` model do not force the `EP` and `PE` boundary-partition languages to
> meet, even when the quotient is `K_7^-`-minor-free and has no strict
> order-seven component subset.

Thus a positive opposite-shore theorem must spend the **absence of the
empty signature**, or an equivalent universal nonextendability statement,
at the actual blocked exchange.  Treating the three selected colourings as
if they already encoded that universal condition is unsupported.

Seven-connectivity remains a second genuine missing input: it must either
convert the low-degree side of this finite architecture into a strict
response separator or supply the additional contacts used in the model
exchange.

## Reproduction

Run the fixed verifier from the repository root:

```text
python3 active/experiments/opposite_shore_coordinate_square_gate/verify_survivor.py
```

It independently checks the two full components, the exact and common
models, all 408 proper boundary partitions, the four signature languages,
both coloured six-fans, the contraction chromatic numbers, connectivity,
and exact `K_7^-`-minor exclusion by contraction search.

The exploratory search which found the contact allocation is retained as
[`search_quotient.py`](search_quotient.py).  For the strongest gate used
here, run

```text
python3 active/experiments/opposite_shore_coordinate_square_gate/search_quotient.py \
  --samples 5000 \
  --require-square-fans \
  --require-disjoint-singletons \
  --require-exact-contractions
```

The random stream is seeded, so this invocation is deterministic.  The
search is only a discovery aid; the displayed survivor and its verification
do not depend on extrapolating from the sample.
