# Independent audit: operation-coupled four-centre web-cut reduction

**Verdict:** GREEN.

**Audited source:**
[`hc7_k7minus_four_centre_operation_cut_reduction.md`](hc7_k7minus_four_centre_operation_cut_reduction.md)

**Mathematical revision SHA-256:**

```text
eb98dcc7703f4e067855977af97617ef8734ec3a35d498cff6725d53ca603aaf
```

After the verdict, only the opening status was changed to link this audit.
The promoted source hash is

```text
4d4ca474cb9d9f28632077f0a89d79c0fc36840f3eb2600c745e0ea2150f2f98
```

This is a separate internal mathematical audit, not external peer review.
No unresolved mathematical gap was found.  The theorem does not eliminate
the web outcome or prove the `K_7^-` six-colour conjecture.

## 1. Hypotheses and dependencies

The audit checked the following pinned inputs:

```text
four-centre rooted-web theorem
b9c6fb2efffc8ebfce641d78c422754e07b0e7375f3a1d3e534c12d881968ade

critical-edge fan descent
d359b4a14520fc4d558ebc600c4e64b7f6bf65ef9fa425b107effa498afc3bfa

critical seven-cut capacity
d4d650fee168fc2ff0e00a3b7b0faed6ff674ba8cd3c06c263f63c4170656f34

adaptive exact-seven (1,2) closure
df8d47261337659ade312bf8a6dfab22453c92bae5841bbb6b6fd303eadf6533
```

The Fabila-Monroy--Wood uses were checked against Lemma 2 and Theorems 6
and 8 of the cited primary paper.  The setting explicitly imports the
nonplanarity of `H` needed in Proposition 5.1.

## 2. Cross-edge colouring and fan descent

The uniqueness of the `gamma`-coloured neighbour makes `rx` the sole
monochromatic edge after restoring `r`.  If an alternate-colour component
failed to join `x` to `r`, its interchange would repair `rx` without
creating another conflict at `r`, six-colouring the host.  The five
first-hit neighbours have the five distinct alternate colours.

When `|T_0|<=5`, every literal parameter maps exactly to the audited
fan-descent theorem: boundary `S`, component `D`, boundary endpoint `r`,
internal endpoint `x`, operated edge `rx`, and the fixed edge-deletion
colouring.  Its strict separator outcome retains the claimed proper shore
trace and common exact colour block.

When `|T_0|=6`, retaining `q` direct spokes leaves `5-q` sources.  Failed
capacitated routing gives `|Z|<=4-q`.  The selected component then has
neighbourhood of order at most

\[
                         1+1+(4-q)\le6,
\]

contrary to seven-connectivity.  The other old component makes this a
genuine separation.  The theorem correctly says that at least one outcome
is guaranteed; it does not claim exclusivity over different target sets.

## 3. Five-limb contact bound

The audited fan theorem supplies six distinct boundary ends and preserves
the five first edges.  The proposed seven bags

```text
{x},  C union {r},  and the five limbs
```

are pairwise disjoint and connected.  The first bag contacts every limb,
the second contacts the first bag through `rx` and every limb through its
literal boundary end, and fullness connects `r` to `C`.  Nine of the ten
limb contacts therefore leave at most one missing adjacency among all
seven bags, producing a forbidden `K_7^-` model.  The asserted upper bound
of eight is exact for this argument.

## 4. Packet-rich boundary

The critical seven-cut capacity theorem gives precisely `(1,1)` or `(1,2)`
up to orientation.  In the second case, adaptive reflection with the
independent block `U` closes whenever `G[T]` has an edge.  Applying the same
audited closure to larger independent sets and to arbitrary independent
four-sets proves both `alpha(G[S])=4` and the complement assertion.

For Theorem 4.2, a thin full packet joined to `U` is connected, and its
contraction makes `U` one exact boundary block.  The `3` and `2,1`
partitions of the independent set `T` have packet demand two, so the two
rich packets would reflect them and six-colour `G`.  Thus all three
vertices of `T` are singleton blocks.  A failed two-colour connection lets
one interchange merge a selected pair, again reducing demand to two.  The
remaining five boundary vertices avoid those two colours, so a simple
connecting path is internally contained in `D`.  The three paths concern
one fixed colouring but are not claimed mutually disjoint.

## 5. One-centre crossing repair

Deleting the three centres other than `s` leaves the four-connected graph
`H+s`.  It contains the nonplanar subgraph `H`, so the planar alternative
in the four-connected rooted-`K_4` theorem is impossible.  A rooted model
exists and must use `s`, since `H` itself has none.  The corresponding
alternating linkage cannot avoid `s`, while its two paths are disjoint and
hence cannot both use `s`.  Exactly one path uses the named centre.

## 6. Scope

The audited result proves:

- a strict response-carrying exact-seven shore descent or a clean
  colour-indexed packing;
- a two-edge deficit in the five-limb contact graph;
- the independent-boundary and fixed-colouring Kempe normal form in the
  packet-rich case; and
- an uncoloured one-centre repair of every rooted-web obstruction.

It does not show that the strict cut retains all four centres, allocate the
fan limbs to rooted model bags, eliminate the `(1,1)` case, eliminate the
independent-`T` `(1,2)` case, or prove the target conjecture.
