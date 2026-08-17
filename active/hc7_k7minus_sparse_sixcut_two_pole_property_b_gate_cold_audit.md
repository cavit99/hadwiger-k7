# Cold audit: two-pole property-B gate

**Audit status:** GREEN.

**Source audited:**
[`hc7_k7minus_sparse_sixcut_two_pole_property_b_gate.md`](hc7_k7minus_sparse_sixcut_two_pole_property_b_gate.md),
SHA-256

```text
9a7a6923764094b588319ed9e683091ce3a6b27fe0cd32b4f871d4a4a83d098d
```

This audit checks the balanced-partition count, all branch-bag contacts in
the seven-bag composition, both Hall arguments, and the precise scope of the
low-visibility conclusion.  It does not certify a split or descent of the
low-visibility bag.

## 1. Balanced property B

There are exactly twenty labelled choices of a three-set `X` in a six-set,
with `Y=S-X`.  If `H` has order three, it is monochromatic only for `X=H`
or `X=S-H`; if `|H|>=4`, it cannot be monochromatic.  Thus each of the five
sets contributes bad probability at most `2/20`, and the union bound leaves a
positive probability of a partition meeting every `H_i` on both sides.

The sharpening is also correct.  A fixed two-set is contained in `X` for
four choices and in `Y` for four choices, hence is monochromatic in eight of
the twenty choices.  One two-set and four sets of order at least three have
total bad probability at most

```text
8/20+4(2/20)=4/5<1.
```

Consequently, if there is no bag seeing at most one root and at most one bag
seeing at most two roots, the same balanced composition succeeds.  This is
equivalent to the stated alternative.

## 2. Seven-bag composition

The seven displayed bags are disjoint.  Each of `A union X` and `D union Y`
is connected because its component is connected and, by fullness, every
adjoined boundary vertex has a neighbour in that component.  The original
five bags retain all adjacencies of the spanning `K_5^-` model.  Since both
parts of the balanced partition meet every `H_i`, each pole bag is adjacent
to every original branch bag.

The two pole bags are adjacent as well: any vertex of the nonempty set `X`
has a neighbour in the full component `D`, giving an edge from `A union X`
to `D union Y`.  Thus at most the one nonedge of the near-five quotient
remains.  No edge inside `S`, no virtual torso edge, and no unrecorded
branch-bag contact is used.

## 3. Hall saturation when `|C|>=6`

If Hall fails for a nonempty `X subseteq S`, then

```text
|N_C(X) union (S-X)| <= (|X|-1)+(6-|X|)=5.
```

Moreover `C-N_C(X)` is nonempty because `|C|>=6`.  It has no edge to the
surviving set `X`, while every route from it to either other component of
`G-S` must use a deleted vertex of `S-X` or a vertex of `N_C(X)`.  The
displayed set is therefore a genuine cut of order at most five.  This
contradicts six-connectivity and establishes a matching saturating `S`.

## 4. Literal five-vertex row

For every nonempty `U subseteq C`, the full external neighbourhood of `U`
has order at least six.  It is the disjoint union of `N_S(U)` and
`N_C(U)-U`, so

```text
|N_S(U)| >= 6-|N_C(U)-U|.
```

The corrected bound

```text
|N_C(U)-U| <= 5-|U|
```

therefore gives `|N_S(U)|>=|U|+1`, which is stronger than Hall's condition
for matching all five vertices of `C` into distinct roots.  Adjoining each
matched root to its singleton vertex gives five disjoint connected rooted
bags.  Their quotient contains the literal spanning `K_5^-`, and the sixth
root is unused, so the model is genuinely confined to a punctured shore.

## 5. Scope verdict

The source proves exactly the advertised composition gate.  It forces a
branch bag with at most two boundary neighbours (and proves the stated
two-bag sharpening), but it does not distribute the at least four remaining
external-neighbour vertices among distinct model bags.  The final paragraph
records that obstruction accurately and makes no unsupported safe-split or
exact-six claim.
