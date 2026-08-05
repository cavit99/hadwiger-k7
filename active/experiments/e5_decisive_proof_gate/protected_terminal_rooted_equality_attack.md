# Protected terminal rooted-equality attack

**Status:** unaudited working note. The results below are not promoted theorems and do not alter the authoritative research frontier. This note records the mathematical progress, failed mechanisms, and exact remaining obligation from the protected rooted-equality attack following the decisive E5 proof gate.

**Branch baseline before this note:** `12302ce93e9f024eae9b319acc89b61dd78e9c22`.

Throughout, `K_7^-` denotes `K_7` with one edge deleted. A `Z`-rooted `K_{4,2}` model has four pairwise disjoint connected root bags, one containing each member of `Z`, and two further connected helper bags; each helper is adjacent to all four root bags. The two helpers need not be adjacent. A `Z`-rooted `K^*_{4,2}` additionally requires the helpers to be adjacent.

This attack did not prove `(E5)`. It produced three useful reductions and isolated one exact unbounded placement theorem whose proof would complete the proposed terminal classification.

## 1. Helper localisation across a full opposite shore

### Working Lemma 1

Let `G` be five-connected and `K_7^-`-minor-free. Let

```text
P=Z disjoint union {r,s},             |Z|=4,
G[Z]=K_4,
```

and suppose `G-P` has two connected components `C,D`, both adjacent to every member of `P`.

If `G[C union P]` contains a `Z`-rooted `K_{4,2}` model, then `G` contains a `K_7^-` minor.

### Proof sketch requiring hostile audit

Normalize the rooted model by minimizing the root bags and maximizing the two helper bags.

If the helpers are adjacent, their union has at most four external attachment vertices, one in each root bag, by the standard maximal-helper argument. Since `(G[C union P],P)` is internally five-connected, at least one of `r,s` must lie in a helper bag. The four root bags are pairwise adjacent through the literal `K_4=G[Z]`. Thus the six model bags form a `K_6` model, and the full opposite component `D` is adjacent to all four root bags and to the helper containing that boundary vertex. It may miss only the other helper, giving `K_7^-`.

If the helpers are nonadjacent, apply the same maximality argument to each helper separately. Each has an external neighbourhood of order four. Internal five-connectivity forces one of `r,s` into each helper. The full component `D` is then adjacent to all six model bags; the only possibly absent adjacency is between the two helpers. Again the seven bags give `K_7^-`.

The proof obligation requiring audit is the precise maximal-helper statement in the nonadjacent-helper case: every external neighbour of each helper lies among four single root portals after the chosen normalization.

### Density consequence

Let

```text
J=G[C union Z].
```

If `(J,Z)` is internally four-connected, then a target-free host has no `Z`-rooted `K_{4,2}` model. Hence the sharp rooted density theorem gives

\[
 |E(J)|\le 4|V(J)|-10.                              \tag{1.1}
\]

There is a strict form when the roots do not span a clique:

\[
 G[Z]\ne K_4 \quad\Longrightarrow\quad
 |E(J)|\le4|V(J)|-11.                               \tag{1.2}
\]

Indeed, add one missing root-root edge. Such an edge cannot create a rooted `K_{4,2}` model because the model requires root-helper contacts, not root-root contacts. Apply (1.1) to the augmented graph.

Thus a closed shore at density at least `4|V|-10` either has the literal four-root clique required by the host composition or returns an order-at-most-three rooted separation.

## 2. The `K_2` one-six-full/full-edge equality returns a rooted separation

Use the promoted `K_2` kernel labels

```text
P={0,1,2,3,4,5},                    0=u,
T={d,w},                            dw in E(G),
N_P(d)={0,1,2,3},
N_P(w)={0,1,4,5}.
```

Suppose the opposite shore consists of one `P`-six-full component `C` and one full edge `F={f,g}` missing `u`. Thus both `f,g` are complete to

```text
Q=P-{u}={1,2,3,4,5}.
```

The promoted equality is

\[
 |E(G[C\cup Q])|=4|C\cup Q|-10.                    \tag{2.1}
\]

Put

```text
Z={2,3,4,5}.
```

Exact contact accounting gives

\[
 |E(G[C\cup Z])|=4|C|+10-p_C(1),                    \tag{2.2}
\]

where `p_C(1)=|E_G({1},C)|<=|C|`. Therefore

\[
 |E(G[C\cup Z])|
 \ge3|C|+10
 >3(|C|+4)-7.                                       \tag{2.3}
\]

### Working Lemma 2

The rooted pair `(G[C union Z],Z)` is not internally four-connected.

### Proof

If it were internally four-connected, the rooted `K_4` density theorem applied to (2.3) would give four pairwise adjacent bags rooted at `2,3,4,5`.

Together with

```text
{f},     {g},     {1,d,w},
```

these form seven pairwise disjoint connected branch sets of a `K_7` minor:

- `f,g` are adjacent and complete to `Q`;
- `{1,d,w}` is connected;
- `d` meets roots `2,3`;
- `w` meets roots `4,5`;
- the boundary vertex `1` joins the last bag to both `f,g`.

This contradicts target-freeness.

### Host lift

Choose a rooted separation of order at most three whose non-root side lies in `C`. Adding `u,1` to its separator gives an exact five-cut of `G`.

The universal five-cut theorem supplies a component of excess at least four and hence order at least the selected lobe order `a`. Since exactly `a+2` vertices lie outside a five-cut, every far component returned inside `C` has aggregate order at most two unless it itself gives strict high-excess descent.

Therefore the formerly unbounded equality component returns one of:

1. strict high-excess descent below `a`;
2. one or two singleton components; or
3. one two-vertex edge component.

This is an unbounded reduction; the bounded atoms are outputs of five-connectivity and exact order accounting, not an assumed finite search bound.

## 3. A returned full edge forces a matching boundary

### Working Lemma 3

Let `Q` be a five-cut in a minimum E5 enemy. Suppose `G-Q` has a high component `H` and a component

```text
X={x,y},            xy in E(G),
```

where both `x,y` are complete to `Q`. If `G[Q]` contains two adjacent edges, then `G` contains a `K_7^-` minor.

Consequently, in a target-free host,

\[
 G[Q]\text{ is a matching together with isolated vertices}. \tag{3.1}
\]

### Proof sketch

Choose `t,z in Q` such that the remaining three vertices

```text
Q-{t,z}
```

span at least two edges. Assign the high shore and distinguished root `t` so that the existing rooted six-bag supply applies. It gives a `(Q-{t})`-rooted `K^*_{4,2}` model in the high shore with `t` in one helper `U`; denote the other helper by `V` and the root bag containing `z` by `R_z`.

Merge `V` and `R_z`. The seven branch sets are

```text
U,
V union R_z,
(R_q : q in Q-{t,z}),
{x},
{y}.
```

The two full edge vertices are adjacent to every root/helper bag through their complete contacts with `Q`. The three remaining rooted bags have at least two of their three mutual adjacencies from the literal boundary edges. Thus at most one pair of branch sets is nonadjacent, giving `K_7^-`.

The points requiring audit are:

- verifying the density hypothesis for the chosen root `t` in every adjacent-edge boundary pattern; and
- checking the displayed model adjacencies after merging `V` with `R_z`.

## 4. Resulting exact equality residue

Combining Sections 2 and 3, the `K_2` one-six-full/full-edge equality reduces to:

1. a singleton recurrence; or
2. an exact five-root `4|V|-10` equality pair whose five-root boundary is a matching.

This is a materially sharper residue than one arbitrary six-full component. It is not eliminated.

## 5. Terminal equality classification: conditional structural picture

The attack suggests the following classification for a terminal pair:

```text
(J,Z) internally four-connected,
|Z|=4,
J[Z]=K_4,
|E(J)|=4|V(J)|-10,
no Z-rooted K_{4,2} model.
```

Conditional on a suitable exact equality decomposition theorem for `K_6`-minor-free graphs, repeated exact-equality clique-sum peeling should reduce every `K_6`-minor-free terminal pair to one of:

1. `K_5`, with `Z` any four vertices;
2. a cone over a four-connected maximal planar graph, with `Z` equal to the apex and a facial triangle.

Both proposed atoms have no rooted `K_{4,2}`:

- `K_5` has only one non-root vertex;
- in the cone case, two disjoint connected helper subgraphs adjacent to all four roots would project to two disjoint connected subgraphs in the planar base, both meeting all three vertices of one facial triangle, which should contradict planarity.

This classification was not promoted because the exact primary-source equality theorem and all root-preservation details were not pinned and audited.

## 6. Exact missing theorem

The classification would be completed by the following unbounded placement statement.

> **Four-root `K_6`-placement theorem.**
> Let `J` be four-connected and let `Z` induce `K_4`. If `J` has a `K_6` minor, then `J` has a `Z`-rooted `K_{4,2}` model.

No counterexample appeared in small-order and random probes, but no unbounded proof was obtained.

### Proposed proof architecture

Choose a spanning `K_6` model maximizing the number of bags containing distinct roots of `Z`.

- If four different bags contain the four roots, the other two bags are the helpers.
- Otherwise some donor bag contains at least two roots and at least three model bags are root-free.
- Split a connected root-containing part from the donor and transfer it into a root-free bag while preserving the labelled `K_6` model.
- The repository's transfer-or-separator machinery shows that failure of a transfer forces a literal residual separator or a portal monopoly inside the donor.
- The remaining task is to prove that three root-free targets and four-connectivity make every such monopoly impossible, or yield an order-three separator.

This is the current first unsupported inference.

## 7. Failed mechanisms and nonclosures

The following approaches were tested and should not be repeated without an additional invariant.

1. **Boundary contacts alone.** The decisive proof-gate split screens already exhibit many target-free contact quotients. Internal density is indispensable.
2. **Unlabelled `K_6` or `K_7^vee` models.** They do not place the four roots in distinct bags or preserve the protected endpoint contacts.
3. **Arbitrary equality contraction.** Internal four-connectivity of the rooted pair does not by itself imply that reinserting the contracted pair preserves five-connectivity of the host.
4. **Assuming terminal pairs are automatically `K_6`-minor-free.** This is equivalent to the open four-root placement theorem and may not be assumed.
5. **Promoting the cone/clique-sum picture without source pinning.** The structural equality input must be identified precisely and the rooted labels checked through every decomposition step.

## 8. Recommended next attack

The next campaign should focus exclusively on the four-root `K_6`-placement theorem.

A useful minimum-counterexample setup is:

```text
J four-connected,
Z induces K_4,
J has a K_6 minor,
J has no Z-rooted K_{4,2},
|V(J)| minimum.
```

Choose a spanning `K_6` model lexicographically:

1. maximize the number of root-separated bags;
2. minimize the order of a donor containing multiple roots;
3. minimize the total number of donor portals to root-free target bags.

Then prove a transfer-or-three-separator lemma for a connected donor with at least two roots and at least three root-free targets. A successful transfer contradicts model optimality. A failed transfer must return a literal separator of order at most three, contradicting four-connectivity.

Success would:

- classify the terminal rooted equality pairs;
- finish the protected ranked-peel mechanism at its terminal class;
- close the exact `K_2` equality family after the matching-boundary reduction; and
- supply the same rooted placement needed in the six-connected `4n-2` essential-edge shore analysis.

## 9. Claim status summary

**Working proof, requiring audit:**

- Helper localisation across a full opposite shore.
- The `K_2` one-full/full-edge equality returns a rooted separation.
- A returned full edge forces a matching boundary.

**Conjectural target:**

- Four-root `K_6`-placement theorem.

**Conditional structural picture, not established:**

- Recursive reduction of every `K_6`-minor-free terminal equality pair to `K_5` or a cone over a four-connected maximal planar graph with the stated root placement.

**Not proved:**

- `(E5)`;
- the primary `4n-2` theorem;
- elimination of the matching-boundary equality pair;
- preservation of full host five-connectivity under every protected equality peel.
