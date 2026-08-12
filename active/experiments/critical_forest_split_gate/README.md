# Seven-connected all-lock split diagnostic

**Status:** explicit finite construction with a deterministic verifier.  It
is a scoped negative diagnostic, not a theorem about the critical host and
not a counterexample to the `K_7^-` six-colour conjecture or `HC_7`.

## Question tested

Let `e` and `f` be two independent edges and put

```text
H = G - {e,f}.
```

The current two-coordinate argument has much more information than the
earlier finite diagnostic retained.  In particular, the all-proper
signature is absent, singleton equalities may lock in every alternate
palette, four of those palettes may fill their whole bichromatic induced
graphs, and the ambient graph is seven-connected.

This construction tests whether the following data alone force a split of
one co-bagged branch set which meets four foreign bags on both sides:

1. `G` is seven-connected;
2. the six-colour signatures of `H` are exactly `EP, PE, EE`;
3. `chi(G)=7`, while all three nonempty edge deletions and all three
   nonempty edge contractions are exactly six-chromatic;
4. the equal pair in each singleton response is locked in every one of the
   five alternate colours;
5. in four alternate colours, the lock component is the full bichromatic
   induced graph and its complement has chromatic number exactly four;
6. one spanning `K_6`-minor model in `H` co-bags both endpoint pairs; and
7. each of the two indicated splits of that model has at most three foreign
   bags adjacent to both sides.

These seven conditions coexist.  Target exclusion does not: the construction
contains a displayed `K_7^-` subgraph.

Here `E` means equal-coloured ends and `P` means different-coloured ends.

## Construction

Take a clique

```text
c0 c1 c2 c3 c4 c5
```

which fixes the six colour names.  Add four vertices `u,v,x,y`.  Adjacency
to the palette restricts their available colours to

```text
u,v : {0,1}
x   : {0,2}
y   : {1,2},
```

and add `uy`, `vx`, and `xy`.  Thus the possible ordered pairs of colours on
`u,v` are exactly

```text
(0,0), (0,1), (1,1).
```

Add four further vertices `a2,a3,a4,a5`.  Vertex `ai` is adjacent to every
palette vertex except `ci`, so it is forced to colour `i`; the four new
vertices form a clique.  Finally, join each of `u,v,x,y` to `a4` and `a5`.
These last edges increase connectivity without changing the displayed list
colouring relation.

Let

```text
e = c0-u,    f = c1-v.
```

The graph just described is `H`; restoring `e,f` gives `G`.  A proper
six-colouring of `H` has signature

```text
EP  when (u,v)=(0,0),
EE  when (u,v)=(0,1),
PE  when (u,v)=(1,1).
```

The fourth possibility `(1,0)`, which would be `PP`, is forbidden by the
three-vertex implication gadget.

## Verified properties

The verifier enumerates all colourings after normalising the palette.  It
finds one `EP` colouring, three `EE` colourings and one `PE` colouring.  It
then checks

```text
kappa(G) = 8,
chi(G) = 7,
chi(G-J) = chi(G/J) = 6 for every nonempty J subset {e,f}.
```

In the `EP` colouring the pair `c0,u` is joined in every `0`--`beta`
bichromatic graph; in the `PE` colouring the analogous statement holds for
`c1,v`.  For `beta=2,3,4,5`, the relevant component is the full
bichromatic induced graph.  In each case the complementary induced graph
contains the other four palette vertices as a `K_4`, while the inherited
colouring uses four colours, so its chromatic number is exactly four.

The following branch sets form one spanning `K_6`-minor model in `H`:

```text
{c0,u,y}       {c1,v,x}
{c2,c3,a4}     {c4,c5,a5}
{a2}           {a3}.
```

The first set co-bags `e` and the second co-bags `f`.  Among all connected
bipartitions of the first bag separating `c0` from `u`, at most three of the
five foreign bags are adjacent to both sides.  The same maximum, three,
holds for the second bag with `c1` and `v`.  Hence the four-foreign-bag split
criterion is blocked in this displayed common model.

The target check is equally explicit.  The seven vertices

```text
c0 c1 c2 c3 c4 c5 u
```

induce `K_7^-`, with `c1-u` as their sole missing edge.  Thus the construction
fails target exclusion in the strongest possible way.

## Scope of the conclusion

This construction disproves only the intermediate inference that the
response square, seven-connectivity, all five locks, the four full-palette
components and one common model must by themselves force the desired
four-bag split.  A valid theorem may instead use the displayed
`K_7^-` outcome, as it should here.

The palette is a `K_6`, so the construction also deliberately omits the
critical host's proved exclusion of a `K_5` subgraph.  Nor does the verifier
claim full contraction-criticality: it checks exactly the six selected
deletion and contraction states stated above.  These omissions are part of
the scope, not hidden approximations to the live hypotheses.

There is no faithful benign version of the same graph-level search with
target exclusion added.  For literal graphs, absence of `PP` says precisely
that restoring `e,f` leaves no proper six-colouring of `G`.  The other
colourings show that `chi(G)=7`.  Requiring at the same time that
`K_7^-` is not a minor of `G` would therefore ask the search to find an
actual counterexample to the conjecture.  A finite failure would establish
only the chosen order bound.  If the colouring relation is instead imposed
externally on a quotient, minor exclusion no longer refers to the same
graph and the experiment is not a faithful test of the host theorem.

The useful conclusion is consequently narrow but firm: the target-free
proof must spend `K_7^-`-minor exclusion at the model-allocation step.  The
full-palette normal form and connectivity do not replace that input.

## Reproduction

From the repository root, run

```text
uv run python active/experiments/critical_forest_split_gate/verify_gate.py
```

The script constructs the graph, enumerates the normalised six-colourings,
checks exact deletion and contraction chromaticity, computes vertex
connectivity, verifies the displayed spanning model and both split maxima,
checks the all-lock and full-palette assertions, and prints the explicit
`K_7^-` subgraph.
