# Three-component rooted-model overlap

**Status:** recorded negative finding / route nonclosure.  This is not a
counterexample to `(E5)` and proves no new boundary case.

Let `S=Z union {x}` be a five-cut of a minimum `(E5)` enemy, with three
components `A,B,C` of `G-S`.  A tempting coupling is:

1. obtain a `Z`-rooted `K^*_{4,2}` model in `G[S union A]`;
2. use fifth-root augmentation to put `x` in one helper bag;
3. obtain a `Z`-rooted `K_4` model in `G[S union B]`;
4. unite corresponding root bags and retain `C` as the seventh bag.

The inference is valid only when the rooted `K_4` model in the second
shore avoids `x`.  If its bag rooted at `z in Z` also contains `x`, that
bag overlaps the first shore's helper.  Merging the two overlapping bags
reduces the construction to six bags; no seventh disjoint branch set has
been produced.

This matters already for the natural quotient constructions.  When
`G[S]` is `K_{2,3}` or a four-cycle with one pendant edge, contracting a
full component `B` to one vertex does give a `Z`-rooted `K_4` after a
suitable choice of `x`, but every such elementary model uses `x`.  It
therefore does not couple with fifth-root augmentation.

The smallest repair lemma is one of the following.

- produce a `Z`-rooted `K_4` model in `G[(S-{x}) union B]`; or
- prove that an `x`-using rooted model leaves a connected residual set
  which supplies the lost seventh branch set.

Pointwise fullness of `B`, the contracted universal-vertex quotient, and
the existing rooted `K^*_{4,2}` theorem do not establish either repair.
Accordingly, the triangle-free three-component cases remain open unless
one of these stronger conclusions is proved.

## Critical-cycle descent does not preserve high excess

There is a second tempting continuation in a high-excess lobe `A`.  Put

```text
H*=G[S union A]+E(complement(G[S])).
```

Thus `S` is a clique in `H*`.  In rows where deleting every edge of a
cycle of added boundary edges leaves a virtual-edge graph with a
two-vertex cover, the two opposite components realise each deletion as a
proper minor of `G`.  If `delta(A)>=4`, minimum-enemy density makes every
edge of that cycle critical for five-connectivity in `H*`.  Mader's
critical-cycle theorem then gives `x in S` with

```text
d_{H*}(x)=5,
```

so `x` has exactly one neighbour `a` in `A`.

Let `Z=S-{x}` and complete `G[Z]` through the two opposite components.
The resulting proper target-free minor

```text
H_0=H*-x
```

has

```text
|E(H_0)|=4|A|+delta(A)+5.
```

It is four-connected.  If it were five-connected, `delta(A)>=4` would
make it a smaller E5 enemy, so it has a four-cut `T`.  Since `Z` is a
clique and `H*` is five-connected, `H_0-T` has exactly two components:
one contains `Z-T`, and the other, say `W`, contains `a`.  Consequently

```text
T union {x}
```

is an actual five-cut of `G`, `W` is one of its components, and
`W` is a proper subset of `A`.

This is not yet a well-founded high-excess descent.  Define

```text
eta(W)=|E(G[W])|+|E_G(W,T)|-4|W|
```

and define `eta(R)` analogously for the other component of `H_0-T`.
Exact accounting gives only

```text
eta(W)+eta(R)+|E(H_0[T])|=delta(A)+5,
delta_{T union {x}}(W)=eta(W)+1.
```

The large excess of `A` can lie entirely in `R`; neither
five-connectivity nor fullness supplies a lower bound on `eta(W)` strong
enough to retain `delta(W)>=q+4`.  Choosing `A` minimum only among lobes
with that high-excess property therefore does not contradict the strict
inclusion `W proper subset A`.

Nor does this automatically reach the audited eight-edge residue.  The
new boundary is `H_0[T]` together with `x`, and `x` has at most two
neighbours in `T`.  If it had eight boundary edges, then `T` would be a
clique and the two missing edges would share the end `x`, a case already
eliminated by the adjacent-miss theorem.  Hence every surviving returned
two-component cut has at most seven boundary edges.

The smallest repair is an excess-localisation lemma forcing the component
containing `a` to inherit the required excess, or a terminal theorem for
the resulting two-component boundary with at most seven edges.  The
critical-cycle argument alone proves neither.
