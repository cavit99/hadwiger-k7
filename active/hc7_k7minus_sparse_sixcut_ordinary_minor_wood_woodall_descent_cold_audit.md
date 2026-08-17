# Cold audit: ordinary near-five minors and the Wood--Woodall descent

**Audit status:** GREEN.

**Source audited:**
[`hc7_k7minus_sparse_sixcut_ordinary_minor_wood_woodall_descent.md`](hc7_k7minus_sparse_sixcut_ordinary_minor_wood_woodall_descent.md),
SHA-256

```text
41c72e882b24cb2d560e8006a44e2d63e5ee9e7f672d0011720b993d9f5a1ba2
```

This revision differs from the initially audited mathematical text only by
marking the audit status and replacing “Equivalently” by “Consequently”
before the incidence sum.  The latter is the logically precise direction;
all proofs and numerical claims are unchanged.

The audit reconstructed the two-pole composition, all separator and excess
identities, the small-separator carrier count, the Wood--Woodall cases, and
the strict-drop guardrail.  It certifies the structural reductions, not the
still-open sharp bound `eta<=5`.

## 1. Ordinary-model fork

Every component outside an ordinary model meets its union in connected `C`,
so absorbing it into a bag it meets preserves connectedness, disjointness,
and all old quotient contacts.  The spanning normalisation is valid.

The pinned balanced two-pole theorem says that five spanning branch bags,
each seeing at least three roots, admit a balanced three--three root partition
and complete with the other two full components to `K_7^-`.  Thus a bag `B`
with root visibility `r<=2` exists.  Its full neighbourhood is exactly

```text
P union (N_G(B) intersect S).
```

The four other nonempty bags give a proper side, so six-connectivity forces
`|P|+r>=6`.  Equality is an exact six-cut; strictness gives the stated one-unit
portal surplus.  Since the model spans `C`, every internal portal belongs to
one of the other four bags.

In the equality row, completing `S` adds no edge at `B`.  At least four old
roots remain outside the derived boundary, so the pinned exact-fragment
rerooting and coefficient-four additivity apply exactly.  The complementary
branch-bag contraction paragraph agrees with its independently audited
source and does not claim packet transfer.

## 2. Small internal separators

For every connected proper `X`, its displayed internal and root neighbour
sets form its entire external neighbourhood.  A component of `G-S` other
than `C` is a far-side witness, so a neighbourhood of order below six would
contradict six-connectivity.  Equality is exact and strictness is integral,
giving `r(X)>=7-t(X)`.

For disjoint strict shores with `t<=2`, every shore sees at least five roots.
For each four-set `Z`, at most two shores can be disjoint `Z`-carriers.
Double-counting the fifteen choices gives

```text
sum_i binom(r(X_i),4)<=30,
```

and each summand is at least five, so there are at most six shores.  The same
calculation on the singleton shores gives the vertex-incidence bound used
later.  Strictly speaking, that singleton inequality is a consequence, not a
logical equivalent, of the full carrier theorem; this wording does not affect
any proof step.

The block--cutvertex argument is sound.  Two leaf-block interiors are
disjoint connected shores with one internal neighbour.  If neither is exact,
each sees all six roots and the two interiors are disjoint full packets.

## 3. Primary structural source and arithmetic

Wood and Woodall, *Defective Choosability of Graphs without Small Minors*,
EJC **16** (2009), R92, Lemma 4.2.1, was checked directly in the published
paper.  It states exactly that a three-connected `(K_5-e)`-minor-free graph is
a wheel, the triangular prism, or `K_{3,3}`.

For a wheel with rim length `m`, each rim vertex has three internal
neighbours.  In the non-exact row it therefore has at least four root
neighbours and contributes at least one to the incidence sum, giving `m<=30`.
The identity

```text
eta_S(C)=a(h)+sum_rim(a(v)-2)-4
```

is exact.  The inequality `a-2<=2 binom(a,4)` for `a=4,5,6`, together with
`a(h)<=6`, gives `eta<=62`.

The prism and `K_{3,3}` each have six vertices, nine edges, and degree three.
In the non-exact row all six boundary degrees are at least four.  Summing

```text
a-4 <= (binom(a,4)-1)/4
```

gives total boundary incidence at most thirty and hence `eta<=15`.  All
displayed order and excess constants check.

## 4. Two-shore torso

Two-connectivity forces every component of `C-{u,v}` to meet both adhesion
vertices.  A far-side `u`--`v` path contracts to the possibly added edge
`uv`, so the three-connected torso `J` is genuinely a minor of `C` and remains
ordinary-`K_5^-`-minor-free.

For a wheel torso, a rim vertex in the open shore `X` has no neighbour in `C`
outside `X union {u,v}`.  Its three torso neighbours are therefore exactly
its three internal neighbours in `C`; unless exact, it contributes to the
same incidence bound.  At most thirty such rim vertices and at most one hub
lie in `X`.  The prism and `K_{3,3}` torsos leave at most four open vertices.
This verifies the terminal two-shore bound.

## 5. Strict-drop guardrail

For the `K_6` example, every subset contained in the four- or two-vertex part
has relative boundary at least six, while a subset meeting both parts sees all
six roots.  The exact boundary of the four-set is the displayed two internal
vertices plus four roots.  Direct counts give

```text
eta_S(C)=11,   eta_U(L)=14,   eta_S(C-L)=-3.
```

The proposed global completion is six-connected.  After at most five
deletions, a root and a vertex of the complete second lobe survive.  Some
first-lobe/root attachment edge also survives because the disjoint
`K_{4,4}` and `K_{2,2}` attachment graph has vertex-cover number six.  The
remaining vertices therefore lie in one component.  This validates the
strict-descent counterexample while leaving target-sensitive induction open.

## 6. Verdict

No separator, minor-containment, carrier-counting, or arithmetic defect was
found.  The source correctly isolates three unresolved mechanisms: surplus
portals in a low-visibility ordinary branch bag, nested strict two-separation
chains, and bounded exceptional incidence instances.  It does not represent
the bounds `62` or `15` as the desired sharp terminal.
