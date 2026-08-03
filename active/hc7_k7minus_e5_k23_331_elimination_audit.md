# Audit: elimination of the `K_{2,3}` `(3,3,1)` row

**Verdict:** GREEN.

**Audited source:**
`active/hc7_k7minus_e5_k23_331_elimination.md`

**SHA-256:**
`33ff2125cafdfdc75b28e3a4ae7d24e4299e6e77cec946d674b7f2875a6e15c1`

This is an internal mathematical audit, not external peer review.

## 1. Setting and scope

The theorem assumes exactly the equality row

```text
q=0,  r=3,  G[S]=K_{2,3},  {delta(A),delta(B),delta(C)}={3,3,1}
```

in a minimum `E5` enemy.  It does not claim that every
three-component boundary, `(E5)`, or the seven-connected `4n-2` theorem is
settled.

The standard closed-shore facts used are valid: every component is full to
the order-five cut, and `(G[S union L],S)` is internally
five-connected.

## 2. Root-avoiding `K_4` in an excess-three lobe

Label the parts of `K_{2,3}` by `X={u,v}` and `Y={a,b,c}`.  For
`x in Y`, the graph `J-x` is `K_{2,2}=C_4`, so it has four edges.
Writing `p(x)=|E_G({x},B)|` gives the exact identity

```text
|E(G[(S-{x}) union B])|
 =|E(G[B])|+|E_G(B,S)|-p(x)+4
 =4|B|+delta(B)-p(x)+4.
```

If the graph has no rooted `K_4`, Fabila-Monroy--Wood Theorem 15 supplies
a spanning obstruction with four nominated vertices in its planar
skeleton.  A nonempty set of lobe vertices in one added clique has all its
external neighbours in the facial triangle, with only the deleted boundary
vertex `x` possible in addition.  Its external neighbourhood therefore has
order at most four, contrary to five-connectivity.  Since distinct
components of `G-S` have no edges between them, no omitted external
neighbour has been overlooked.  All vertices of the rooted graph are thus
in the planar skeleton, so the ordinary planar bound applies.

The resulting lower bound

```text
p(x)>=|B|+delta(B)-2
```

is correct.  Summing it over the three vertices of `Y` and adding the two
fullness contacts at `u,v` gives

```text
|E_G(B,S)|>=3|B|+3delta(B)-4.
```

Connectedness gives the independent upper bound

```text
|E_G(B,S)|
 =4|B|+delta(B)-|E(G[B])|
 <=3|B|+delta(B)+1.
```

At `delta(B)=3` these bounds differ by one.  Therefore some `x in Y`
does yield a rooted `K_4` in `G[(S-{x}) union B]`.  In particular, the
model avoids `x`; the earlier root--helper overlap is not being repeated.

## 3. `K^*_{4,2}` threshold in the other high lobe

For the chosen `x`, the two nonedges completing `J[Z]=C_4` to `K_4`
join pairs of distinct roots.

If `p_A(x)=1`, deleting `x` and adding those two edges gives

```text
|V|=|A|+4,
|E|=4|A|+delta(A)+5=4|A|+8,
```

which is one edge above `4|V|-9`.  A separation of the rooted pair of
order at most three becomes an internal separation of
`(G[S union A],S)` of order at most four after `x` is put in the
separator.

If `p_A(x)>=2`, retaining `x` and adding the same two edges gives

```text
|V|=|A|+5,
|E|=4|A|+delta(A)+8=4|A|+11=4|V|-9.
```

Here `x` has its two neighbours in `J` and at least two in `A`.  The
standard rooted-connectivity transfer therefore excludes the only
singleton-`x` exception and makes the pair internally four-connected.

Norin--Totschnig Lemma 12 applies in both cases.  The added edges cannot
be internal to a branch set because their ends are distinct nominated
roots, and root--root adjacency is not required in `K^*_{4,2}`.  Removing
the virtual edges consequently leaves an actual rooted model in the
original closed shore.  The pinned fifth-root augmentation lemma then
puts `x` in one helper.

The fifth-root input was checked at source revision
`81306114489449f1bd2d8521c4aefc216411f81bf6721c7763412d4a7a87c6c0`.

## 4. Seven branch sets

Let `R_z` and `Q_z` be the root bags in the `A`-shore
`K^*_{4,2}` model and the `B`-shore rooted `K_4` model.  Their union
`M_z=R_z union Q_z` is connected through the common root `z`.

The seven proposed bags are

```text
M_z (z in Z), U, V, C.
```

They are disjoint.  The two shores intersect only in `S`; distinct
nominated roots lie in distinct root bags; the second model avoids `x`;
and every member of `S` already belongs to its specified root bag or to
the helper containing `x`.

All adjacencies are accounted for:

- the four `M_z` are pairwise adjacent through the rooted `K_4`;
- both helpers meet every `M_z`, and the helpers meet each other, by the
  definition of `K^*_{4,2}`;
- fullness of `C` makes it adjacent to each `M_z` through `z` and to `U`
  through `x`.

Only `CV` may be absent.  These are therefore branch sets of a
`K_7^-` minor, giving the required contradiction.

## 5. External inputs

The external statements are used at their stated scope:

- Norin--Totschnig, Lemma 12: absence of a `Z`-rooted
  `K^*_{4,2}` model in an internally four-connected pair with four roots
  implies `|E(H)|<=4|V(H)|-10`.
- Fabila-Monroy--Wood, Theorem 15: a graph with four nominated vertices
  and no rooted `K_4` is a spanning subgraph of one of the six stated
  planar-skeleton obstruction classes.

No finite enumeration or unaudited computational result enters the proof.
