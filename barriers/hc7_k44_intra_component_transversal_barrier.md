# Barriers to component-local and boundary-resource-redundant repairs

**Status.**  Two explicit abstract incidence counterexamples to the
profile-level intermediate lemmas stated below, with an adjacent deterministic
verifier and an independent internal audit.  Neither is asserted to occur as
a blocker in a seven-connected host, and neither is a graph counterexample to
the full boundary-bisection lemma, the weighted splitter theorem, the literal
case of T44, or T44.

## 1. First refuted statement

The first exact three-cut profile in the audited
[minimum-blocker theorem](../results/hc7_k44_tight_boundary_and_minimum_blocker.md)
has a three-cut `Q`, components `W_1,W_2,W_3`, two resources `c_1,c_2`
meeting every component, and one resource `e_i` supported wholly in each
`W_i`.  The following proposed repair is false even under every audited local
minimum-blocker conclusion.

> **Component-local nonseparating-transversal claim (refuted).**  For some
> distinct `i,j,k`, there is a nonempty connected set `V subseteq W_i` such
> that `X-V` is connected, `V` sees `b,c_1,c_2,e_i`, and `X-V` sees
> `a,c_1,c_2,e_i,e_j`.

If true, this claim would satisfy the two-helper criterion with `U=X-V` and
`h_0=e_k`.  The counterexample shows that the bisection cannot in general be
found inside one three-cut component.

## 2. Exact order-nine profile

Let

```text
Q={t0,t1,t2},                 X[Q]=K3,
W_i={l_i,r_i},                X[W_i]=K2  (i=1,2,3),
X = K3[Q] join (K2[W_1] dotcup K2[W_2] dotcup K2[W_3]).
```

There are no edges between distinct `W_i`.  Let the seven boundary resources
be

```text
D={a,b,c1,c2,e1,e2,e3},       K={c1,c2,e1,e2,e3}.
```

Give them the following exact supports in `X`:

```text
N_X(a)  = {t0,r1,r2,r3};
N_X(b)  = N_X(c1) = {l1,l2,l3};
N_X(c2) = {r1,r2,r3};
N_X(e_i)= {l_i,r_i}.
```

Retain the crossing edge `ab` on the boundary and take no other boundary
edge.  This boundary graph has a proper bipartition with class orders three
and four, as required by the reduced local profile.

Then `X` is three-connected and has minimum degree four.  Every nonempty
`Y subseteq X` satisfies

```text
|N_X(Y)|+|N_D(Y)| >= 7,
```

and every proper connected `Y` seeing both `a,b` satisfies the strict bound
at least eight.  Every resource in `K` is multiply attached.  The vertex
`p=t0` sees `a`, sees no member of `K`, and `X-p` is full to
`H=D-{a}`.  Deleting `Q` leaves exactly the three components `W_i`; the
resources `c_1,c_2` meet all three, and `e_i` has all its neighbours in
`W_i`.  Thus the profile satisfies every local hypothesis and consequence
available before the open boundary-bisection lemma.  This is a complete
counterexample to an inference from those reduced local data; it is not a
realization theorem for an ambient seven-connected graph.

For fixed `i`, a subset of `W_i` seeing `b,c_1,c_2,e_i` must contain both
`l_i` and `r_i`, hence must equal `W_i`.  Its complement then misses `e_i`.
There is no component-local transversal witness.

The order is minimal for this first-profile obstruction.  The cut has three
vertices and three nonempty components.  Multiple attachment of each
component-exclusive resource `e_i` forces `|W_i|>=2`, so `|X|>=9`.

## 3. Exact scope and surviving bisection

This is not a counterexample to the full two-helper bisection.  Put

```text
U={t0,l1,l2},       V=X-U,       h0=c2.
```

Both `U,V` are connected and adjacent.  The set `U` sees `a,b` and the
`K`-resources `c_1,e_1,e_2`, while `V` is full to `H`.  In the criterion

```text
|H-(N_D(U) union {b,h0})|
  + |H-(N_D(V) union {h0})|,
```

the two defect terms are respectively `{e_3}` and the empty set.  The total
defect is one, so the audited two-helper construction still produces the
target.  Exhaustion finds 231 spanning two-helper witnesses in this profile.

The next sufficient target must therefore allow cross-component bisections.
The condition that `U` see `b`, however, is extraneous: the two-helper
criterion already gives the first helper its `b`-contact through the crossing
edge `ab`.  The next profile makes this failure exact.

## 4. A second order-nine profile

On the same graph and boundary resources, use instead

```text
N_X(a)  = {l1,r1,l2,r2,l3,r3};
N_X(b)  = {t2};
N_X(c1) = {l1,l2,l3};
N_X(c2) = {r1,r2,r3};
N_X(e_i)= {l_i,r_i}.
```

Again retain only `ab` on the boundary.  This profile satisfies every
relative inequality, every strict proper connected `a,b`-seeing inequality,
multiple attachment, and the first exact three-cut profile.  The special
vertex can be `p=l_1`: it sees `a`, has `d_K(p)=2`, and `X-p` is `H`-full.

There is no component-local witness because no `W_i` sees `b`.  There is
also no connected bisection in which the first side sees `a,b` and at least
three `K`-resources while its complement is `H`-full: every first side seeing
`b` contains `t_2`, so its complement misses `b`.

Nevertheless the full two-helper criterion again closes.  Take

```text
U={t0,l1,l2},       V=X-U,       h0=c2.
```

The set `U` sees `a` and exactly the three `K`-resources `c_1,e_1,e_2`;
it need not see `b`.  The complement `V` is `H`-full, and the two defects are
again `{e_3}` and the empty set.

This refutes the proposed two-mode statement which required the
cross-component side to see `b`.  The corrected exact sufficient alternative
is:

> `U` and `X-U` are nonempty and connected, `U` sees `a` and at least three
> resources in `K`, and `X-U` is `H`-full.

This is precisely the `H`-full-complement subcase of the two-helper
criterion.  If the complement is `H`-full, its defect is zero and the first
defect is at most one exactly when `h_0` can excuse one of at most two missed
`K`-resources.  The remaining nonsingleton difficulty is therefore the
**support-transfer case** in which the complement is not `H`-full and the
one or two resources supported wholly on the first side must be coordinated
with the single choice of `h_0`.  No unbounded claim is made that the corrected
`H`-full-complement alternative always occurs.

## 5. Verification

Run

```text
python3 barriers/hc7_k44_intra_component_transversal_barrier_verify.py
```

The verifier exhausts all 511 nonempty vertex sets for each profile, every
proper connected set seeing `a,b`, every component-local candidate, and every
relevant spanning two-helper bisection.  Its pinned output is in
[`hc7_k44_intra_component_transversal_barrier_output.txt`](hc7_k44_intra_component_transversal_barrier_output.txt).
