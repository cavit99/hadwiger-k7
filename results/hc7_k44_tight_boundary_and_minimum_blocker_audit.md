# Independent internal audit: tight boundaries and minimum blockers

**Verdict: GREEN.**  The exact source revision identified below is a valid
written unbounded reduction.  This is a separate internal mathematical
audit, not external peer review.

**Audited source:**
[`hc7_k44_tight_boundary_and_minimum_blocker.md`](hc7_k44_tight_boundary_and_minimum_blocker.md)

**Audited source SHA-256:**
`384150b962a3e86848622e78cd711fac3d27b1bfcedbc22a1ce8adb2d7127b90`

## 1. Tight boundaries and prescribed core vertices

For a connected tight set `Y`, the set `D=partial Y` is an actual
seven-cut and every complementary component is full to `D`.  The audited
three-component bound and closed-shore lemma give seven disjoint
`D`-rooted paths with distinct literal-core representatives, using the
exact capacity identity `|S-D|=|D-S|+1`.  A same-shore edge in `G[D]`
would give the displayed rooted `K_5^-` together with two universal bags;
the contact count is exactly `9+5+6=20`.  Thus the `3`-by-`4` proper
boundary colouring is valid.

The prescribed-core-vertex Menger dichotomy is exact.  A deficient
separator together with `Q union {s}` separates nonempty `Y` from a
surviving target, so seven-connectivity forces an exact seven-cut.  In the
linkage branch, the two omitted-shore colourings differ in class size by
one and agree on components meeting `Q`; hence a flipped `Q`-free component
has nonzero odd imbalance.  The exterior-edge corollary correctly excludes
an entire literal shore in `Q`.

## 2. Two-helper construction and small separations

Lemma 4.1 is correct.  Five selected core vertices root a genuine `K_5`
using the other three core vertices.  The bags `U union {a}` and `V` are
adjacent connected helpers, and the two defect terms count exactly their
missing contacts, including the automatic `ab` contact.  Condition (13)
therefore gives at least `10+5+5+1-1=20` contacts.  Equation (16) is exact
resource accounting; equality with `a,b` represented creates precisely a
smaller blocker.

The order-two, cutvertex, triangle and two-cut eliminations are complete.
In the two-cut case,

```text
E_i=(intersection_{j != i} Delta_j)-N_D({x,y}),
```

both defects have order at most two, equality meets `{a,b}`, and the two
defects are disjoint by boundary fullness.  The sole initially failing
both-`a` pattern is repaired by reversing the helper orientation and
choosing `h_0`.  Thus every target-free nonsingleton minimum blocker is
three-connected.

## 3. Attachment and minimum degree

A `K`-resource with a unique neighbour would make `X-z` a smaller blocker.
The chosen `p in N_X(a)` preserves `b`; the one-vertex defect inequality
then shows that `X-p` represents all of `H`.  Lemma 4.1 forces `p` to see
at most two `K`-resources.

For an internal degree-three vertex, the singleton and complement
inequalities give `alpha+beta+k>=4` and `e<=1`.  Equations (25) and (26)
are exactly the negations of the two helper orientations.  The three
exhaustive `(alpha,beta)` cases each produce a smaller blocker or contradict
the other orientation.  Hence the asserted minimum degree four is valid.

## 4. Three-cut profiles

Every component behind a three-cut has all three cut contacts and at least
three `K` contacts.  For `W_i,X-W_i`, the pre-omission defect sum is
`5-c_i` plus the indicator that all `b`-neighbours lie on the atom-helper
side.  When both sides see `a`, one may orient the split so that the
indicator is zero.  The indicator is unavoidable exactly when only one side
sees `a` and every `b`-neighbour lies there.  Thus `e_i=0` is possible only
when every neighbour of both `a` and `b` lies in `W_i` and `|K_i|=3`; this
exceptional component is unique.

Here `e_i` counts resources whose entire `X`-neighbourhood lies inside
`W_i`.  Consequently `5-sum_i e_i` counts resources not supported wholly
inside a single component; it does not assert that such a resource meets
multiple components, because it may also meet the three-cut.  With this
interpretation, the capacity count excludes four components.  At three
components it gives exactly the two profiles stated in the theorem.  No
stronger intercomponent-sharing claim is used.

## 5. Inputs, trust boundary and scope

The audit accepts these adjacent GREEN inputs at their source revisions:

| input | source SHA-256 |
|---|---|
| singleton-atom reduction | `775a4f5a6cf2f455a2ca54a232146fd2f4b22a1c88e7e38770b26bfb83df8e07` |
| seven-cut component theorem | `cbd3ecb73bea0530797ad58080ae6db6052bfbf69f90af558283e3f250772ef8` |
| closed-shore rooted connectivity | `ba6dbfe1ca9e89041b1a77174844c24598984cbe76349a55c41f15b2e997cc03` |

Standard set-Menger is used only in the reconstructed form above.  The
bounded search in Section 8 is evidence only, is outside this verdict, and
supports no unbounded inference.

The theorem does not prove the boundary-bisection lemma, eliminate every
minimum nonsingleton blocker, close the adjacent-singleton case, prove the
weighted splitter theorem, or close literal T44.  The precise nonsingleton
residue is the minimum-degree-four boundary-bisection lemma in Section 8.
