# Boundary-only barriers to exceptional shore allocation

**Status:** barriers/counterexamples to intermediate claims; computer-assisted
finite verification; separate internal audit GREEN for this revision.  The
deterministic verifier is
[`hc7_k7minus_shore_allocation_barrier_verify.py`](hc7_k7minus_shore_allocation_barrier_verify.py).
Neither barrier is a counterexample to the critical-host shore-allocation
target, the `K_7^-` six-colour conjecture, or `HC_7`.

## 1. Refuted boundary-counting inference

Let `H` be one of the 15 order-eight graphs in the
[both-full boundary reduction](../results/hc7_k7minus_both_full_shore_reduction.md),
and label every nonedge of `H` abstractly by one of two shores `E,F`.  For
an independent triple `I`, put `R=V(H)-I` and let `D_I` be the nonedges of
`H[R]`.

The tempting inference is:

> after choosing or rotating `I`, one shore must label all but at most one
> pair of `D_I`.

This is false as a boundary statement.

### Theorem 1 (balanced labels survive every rotation)

For every one of the 15 graphs `H`, there is a single map

\[
                      \sigma:E(\overline H)\longrightarrow\{E,F\}       \tag{1}
\]

such that, for every independent triple `I`,

\[
 \bigl|D_I\cap\sigma^{-1}(E)\bigr|\ge2,
 \qquad
 \bigl|D_I\cap\sigma^{-1}(F)\bigr|\ge2.                 \tag{2}
\]

Thus neither abstract shore ever carries `|D_I|-1` demands, even after all
independent-triple rotations.

### Verification

The verifier records one explicit 28-bit label mask for each canonical
graph6 code.  Bit positions use lexicographic pairs from
`combinations(range(8),2)`.  It checks that only nonedges are labelled `E`
and verifies (2) for every independent triple; the other nonedges carry
label `F`.  The sorted witness digest is

```text
325a008189de182c099d60990d72c94f02fe78709e4858bc5aa48ec8eba59367
```

These labels are abstract.  The theorem does not assert that one fixed
critical colouring realizes exactly these Kempe-path availabilities, or
that the labels persist across different proper-minor colourings.  Its
precise conclusion is that the boundary graph and independent-triple
rotation alone cannot force demand concentration.

## 2. Fullness and minor exclusion alone do not force allocation

Let

\[
             X=A_1\mathbin{\dot\cup}A_2\mathbin{\dot\cup}A_3,
             \qquad (|A_1|,|A_2|,|A_3|)=(3,3,2),       \tag{3}
\]

and let

\[
                         H=K[A_1]\mathbin{\dot\cup}
                           K[A_2]\mathbin{\dot\cup}K[A_3].       \tag{4}
\]

Add three pairwise nonadjacent vertices `u,e,f`, each adjacent to every
vertex of `X`, and add no other edges.  Call the resulting graph `G_0`.

### Theorem 2 (two-full-shore mechanism barrier)

The graph `G_0` has all of the following properties.

1. `d(u)=8`, `G_0[N(u)]=H` is `K_4`-free, and `\alpha(H)=3`.
2. `G_0-N[u]` has the two singleton `X`-full components `\{e\},\{f\}`.
3. `G_0` has no `K_7^-` minor.
4. For every independent triple `I\subseteq X`, neither closed singleton
   shore `H[X-I]+e` nor `H[X-I]+f` contains an `(X-I)`-rooted `K_5^-`
   model.
5. `\kappa(G_0)=3` and `\chi(G_0)=4`.

#### Explanation

Every independent triple contains one vertex of each clique in (4).  Its
five-vertex reserve therefore induces

\[
                         2K_2\mathbin{\dot\cup}K_1.     \tag{5}
\]

A singleton shore contributes only one nonroot to five rooted bags, so at
least four bags are singleton roots.  Those four roots span at most two
edges.  A rooted `K_5^-` would require at least five of their six mutual
contacts, which is impossible.

For minor exclusion, adding the three edges on `\{u,e,f\}` produces a
clique-sum over that triangle of two copies of `K_6` and one copy of `K_5`.
The five-connected graph `K_7^-` cannot have a minor model straddling this
order-three clique-sum, and no summand has seven vertices.  The verifier
also checks the claim independently: because `G_0` is connected, any minor
model can be enlarged to a spanning model; it exhausts every partition of
the eleven vertices into seven nonempty connected bags and finds none with
20 of the 21 pairwise contacts.

Deleting `\{u,e,f\}` disconnects `H`, while deletion of at most two
vertices leaves one apex joining all surviving boundary vertices.  Hence
the connectivity is three.  The boundary needs three colours and the
independent apex set needs one new colour, giving chromatic number four.

## 3. Reproduction and scope

Run

```text
.venv/bin/python barriers/hc7_k7minus_shore_allocation_barrier_verify.py
```

The wrapper `G_0` lacks exactly the hypotheses that must now do substantive
work: it is neither seven-connected nor proper-minor six-colour-critical.
Accordingly, Theorem 2 does not refute allocation under `(H)`.  It rules
out an argument using only exceptional boundary structure, two full
components, and `K_7^-` exclusion.

Together, the two barriers show what a valid continuation must add.  It
must use compatibility among changing critical colourings, or prove a
topological residual-contact statement inside a packet-one shore.  Static
nonedge counts, whole-component contractions, and independent-triple
rotation are insufficient.
