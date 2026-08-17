# A three-connected ordinary-minor-free lobe has an exact singleton

**Status:** complete unbounded theorem with an exact finite certificate,
independently cold-audited twice.  In a returned three-component six-cut, a
three-connected lobe with no ordinary `K_5^-` minor has a vertex of total
degree six.  Its neighbourhood is an exact six-cut and the singleton
fragment has coefficient-four excess `2`.  This eliminates the entire
no-exact-fragment subcase of the three-connected ordinary-minor-free case;
the returned exact fragment is not itself terminal for the weighted local
theorem.  Ordinary near-five models and nested two-separations also remain.

## 1. Setup and the four-root packing bound

Let `G` be a six-connected graph with no `K_7^-` minor.  Let `S` be a cut of
order six such that `G-S` has at least three components, and fix a component
`C`.  Every component of `G-S` is adjacent to every vertex of `S`.

For `v in C`, write

```text
A(v)=N_G(v) intersect S,        a(v)=|A(v)|.          (1)
```

The audited four-root connected-subgraph theorem gives the following bound:

```text
for every four-set Z subseteq S,
at most two vertices v in C satisfy Z subseteq A(v). (2)
```

Indeed, three such vertices would be three disjoint connected singleton
subgraphs, each adjacent to every vertex of `Z`.

A model on five distinct roots of `S`, confined to the graph obtained by
omitting the sixth root, is terminal.  Two other full components complete its
five branch bags to a `K_7^-` model.  We shall therefore derive a contradiction
whenever such a punctured rooted `K_5^-` model is constructed.

## 2. The six-root mask lemma

Let `A_0,...,A_{k-1}` be subsets of a six-set.  Call the tuple
**four-set admissible** if no four-set is contained in three of the `A_i`.
For distinct assigned roots `r_i in A_i`, say that a pair `ij` is **covered**
if

```text
r_i in A_j       or       r_j in A_i.                (3)
```

Thus, when bag `i` contains a core vertex seeing `A_i` and its assigned root
`r_i`, a covered pair is an actual contact between bags `i` and `j`.

### Lemma 2.1 (five exceptional-core root assignments)

Every four-set-admissible tuple has the indicated assignment.

1. **`W_3` case.**  If `A_0,...,A_3` all have order at least four, there are
   five distinct roots `r_0,...,r_3,t` such that `r_i in A_i` and `t` belongs
   to at least three of the four sets.
2. **`W_4` case.**  If `|A_0|>=3` and `|A_i|>=4` for `1<=i<=4`, there are five
   distinct roots `r_i in A_i` which cover at least one of

   ```text
   13, 24.                                             (4)
   ```

3. **Long-wheel case.**  If all five sets have order at least four, there are
   five distinct roots `r_i in A_i` which cover at least two of

   ```text
   13, 14, 24.                                         (5)
   ```

4. **Prism case.**  Under the same lower bound, five distinct assigned roots
   cover at least three edges of the path

   ```text
   01, 12, 23, 34.                                     (6)
   ```

5. **`K_{3,3}` case.**  Under the same lower bound, five distinct assigned
   roots cover at least three of

   ```text
   01, 02, 12, 34.                                     (7)
   ```

### Exact finite verification

The standard-C verifier
[`verify.c`](experiments/sparse_sixcut_wood_woodall_rooting/verify.c)
enumerates all `64` masks of a six-set, retaining the `22` masks of order at
least four and, for the `W_4` hub, the `42` masks of order at least three.  It
then tests every injection of the bag roots into the six-set and directly
counts the covered pairs in (4)--(7).  The `W_3` case separately tests the
fifth singleton root.

The exact census is

```text
case         tuples tested   assignment failures   admissible failures
W3                234,256                    15                     0
W4              9,838,752                    75                     0
long wheel       5,153,632                    15                     0
prism            5,153,632                    15                     0
K33              5,153,632                    15                     0
```

Here `22^4=234,256`, `42*22^4=9,838,752`, and
`22^5=5,153,632`, so every eligible tuple is generated.  For every raw tuple
on which the displayed assignment fails, the verifier finds a four-set
contained in at least three masks, which violates four-set admissibility.
Assertions pin all five censuses and the zero residual; no random search or external
solver is used.  This proves the lemma within the displayed finite trust
boundary.
`\square`

The exact build command and transcript are recorded in
[`README.md`](experiments/sparse_sixcut_wood_woodall_rooting/README.md).

## 3. Exact-singleton theorem

### Theorem 3.1

If `G[C]` is three-connected and has no ordinary `K_5^-` minor, then some
vertex `v in C` satisfies

```text
d_G(v)=6.                                             (8)
```

Consequently, `N_G(v)` is an exact six-separator with open singleton side
`{v}`.

### Proof

Suppose, for a contradiction, that every vertex of `C` has total degree at
least seven.  Wood and Woodall's Lemma 4.2.1 says that a three-connected
`K_5^-`-minor-free graph is a wheel, the triangular prism, or `K_{3,3}`.
We decode all three possibilities.

#### Wheels

Write the wheel as a hub `h` and a cyclic rim

```text
v_0 v_1 ... v_(m-1) v_0,       m>=3.                 (9)
```

Every rim vertex has three neighbours in `C`, so the supposition gives
`a(v_i)>=4`.  The tuples of masks used below are four-set admissible by (2).

If `m=3`, the wheel is `K_4`, and the hub also has internal degree three.
Label its four vertices `x_0,...,x_3` and apply Lemma 2.1(1).  The bags

```text
{x_i,r_i}   (0<=i<=3),                         {t}    (10)
```

are connected and rooted at five distinct boundary vertices.  The first
four bags form a clique, and `{t}` meets at least three of them.  Thus (10)
is a punctured rooted `K_5^-` model, a contradiction.

If `m=4`, the hub has internal degree four, so `a(h)>=3`.  Index the hub by
`0` and the four rim vertices cyclically by `1,2,3,4`.  Lemma 2.1(2) assigns
five distinct roots.  The five two-vertex bags

```text
{h,r_0},       {v_i,r_i}  (1<=i<=4)                  (11)
```

inherit the eight edges of `W_4`.  The only two missing rim pairs are
`13,24`; (4) supplies at least one of them.  Hence (11) has at least nine of
the ten bag contacts and is again a punctured rooted `K_5^-` model.

It remains that `m>=5`.  Apply Lemma 2.1(3) to the five consecutive rim
vertices `v_0,...,v_4`, and define

```text
B_0={r_0,h,v_0},
B_i={r_i,v_i}                         (1<=i<=3),
B_4={r_4,v_4,v_5,...,v_(m-1)}.                       (12)
```

These five bags are disjoint and connected.  The hub makes `B_0` adjacent
to every other bag.  The other four bags inherit the path contacts
`12,23,34`; their three remaining possible pairs are exactly (5).  At least
two are covered, so the four bags have at least five contacts.  Together
with the four hub contacts, (12) is a punctured rooted `K_5^-` model.  This
contradiction eliminates every wheel.

#### The triangular prism

Let the two triangles be `a_0a_1a_2a_0` and `b_0b_1b_2b_0`, with matching
edges `a_i b_i`.  Omit `a_2` and order the other five vertices as

```text
b_0, a_1, b_2, a_0, b_1.                            (13)
```

All have internal degree three and hence at least four boundary neighbours.
The four nonedges in the graph induced by (13) are precisely the path (6).
Lemma 2.1(4) assigns distinct roots so that at least three of these nonedges
become bag contacts.  The five two-vertex rooted bags inherit the six prism
edges and at least three additional contacts, giving a punctured rooted
`K_5^-` model.  This is impossible.

#### `K_{3,3}`

Let its bipartition be `{a_0,a_1,a_2}` and `{b_0,b_1,b_2}`.  Omit `a_2` and
order the remaining vertices as

```text
b_0,b_1,b_2,a_0,a_1.                                 (14)
```

Again all five masks have order at least four.  The six cross-part pairs are
edges, and the four nonedges are exactly (7): the triangle on indices
`0,1,2` and the pair `34`.  Lemma 2.1(5) covers at least three of them.  The
resulting five two-vertex rooted bags have at least nine contacts, another
forbidden punctured rooted `K_5^-` model.

Every Wood--Woodall case contradicts target exclusion.  Hence the
supposition was false.  Six-connectivity gives minimum degree at least six,
so a vertex of degree exactly six exists.  Its full external neighbourhood
has order six.  Deleting it isolates the vertex and leaves the other full
components as a nonempty far side, so it is an exact six-separator.
`\square`

## 4. The returned fragment has excess two

### Corollary 4.1

For the vertex `v` in Theorem 3.1, put `U=N_G(v)`.  In the completed closed
shore, `{v}` is a component behind the exact six-cut `U`, remote from
`S-U`.  Moreover,

```text
eta_U({v})=2,
eta_S(C)=2+eta_S(C-{v}).                              (15)
```

Punctured-rooted-model exclusion is hereditary on the derived pair
`(G[{v} union U],U)`.

### Proof

Three-connectivity gives `d_C(v)>=3`, so (8) implies `a(v)<=3`; hence
`S-U` is nonempty.  Completing `S` to a clique adds no edge incident with
`v`, and therefore does not change its exact neighbourhood or the orientation
of the fragment.  The singleton has no internal edge and has exactly six
boundary incidences, giving

```text
eta_U({v})=0+6-4=2.
```

Partitioning the internal, boundary, and vertex terms at the exact fragment
gives (15).  The hereditary claim is Corollary 3 of the audited exact-six
rerooting theorem. `\square`

Thus the ordinary-minor-free three-connected branch returns not merely a
bounded exceptional core but an exact singleton fragment with `eta=2`,
together with a strict two-unit decrement in the complementary bookkeeping
term.  Further descent must still transfer the rooted or packing information
across the derived boundary.

## 5. Scope

The theorem eliminates the no-exact-fragment subcase for every
three-connected ordinary-`K_5^-`-minor-free lobe.  It is unbounded in the
wheel order and uses only the target-sensitive four-root packing bound plus
the published three-connected classification.  It does not make the returned
exact fragment terminal.

It does **not** prove the full local excess-five dichotomy.  Two branches
remain outside its hypotheses:

* a lobe containing an ordinary `K_5^-` minor, where low-visibility branch
  bags and transfer of two boundary-full connected subgraphs remain; and
* a two-connected but non-three-connected lobe, where nested strict
  two-separations may persist.

The finite mask lemma is not asserted for arbitrary rooted graphs without
the four-root packing bound (2); its raw assignment-failure cases show that
condition is essential for these constructions.

## 6. Pinned dependencies and primary source

* four-root connected-subgraph packing: source SHA-256
  `adfcc70aca8543e15bcf7e94e1fb310492535f8155f02cb5a5430adba4ce8372`,
  GREEN audit SHA-256
  `4a185697d20ed73c358703eb7d433c3555bca6474497a011630d3805dc493e97`;
* punctured five-root terminal reduction: source SHA-256
  `32c45ee41ee349e2499c82c49bd7a0af7cfd636620bbc7873edea4ca061e1100`,
  GREEN audit SHA-256
  `b89582b3c4c4dfe0c03980c45c93b7fcad250241e6ef356273fd9f3fa2db7a89`;
* exact-six rerooting and additivity: source SHA-256
  `53c91cee74ae8b1f5251e13c14095f8abc65f05625eedb401d3d53173996da15`,
  GREEN audit SHA-256
  `c30aa69b6919edd2cfba80d6df1f02e2c75d38d9544bd87e4332ba4d823526a3`;
* finite verifier SHA-256
  `37584ca0a390c9d556fdfe7cdfc83d24afd7f5fe39987209693f0512c83d60ca`,
  transcript README SHA-256
  `e63be6b2758356e8f141b14cb688e66cc84cd433181c7518d796a17d7b76f40f`.

The external structural input is R. G. Wood and D. R. Woodall,
*Defective Choosability of Graphs without Small Minors*, Electronic Journal
of Combinatorics **16** (2009), R92, Lemma 4.2.1,
[DOI 10.37236/181](https://doi.org/10.37236/181).  The published statement
was checked directly: the only three-connected `(K_5-e)`-minor-free graphs
are wheels, the triangular prism, and `K_{3,3}`.
