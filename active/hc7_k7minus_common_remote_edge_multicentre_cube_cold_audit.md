# Cold audit of the common-edge multicentre manuscript

**Verdict:** **GREEN after two incorporated precision repairs.**  The global
incidence, mixed-operation, connectivity, exact-model and bounded
original-coordinate conclusions are mathematically valid.  Corollary 2.6
now restricts its intermediate quantifier to a proper vertex subset, and
Theorem 6.1 cites the required actual-boundary descent theorem by name.  The
manuscript is a strong structural side theorem, but it is not a terminal
theorem and does not meet the Norin--Totschnig benchmark.

## 1. Audited revision

The audited source is
[`hc7_k7minus_common_remote_edge_multicentre_cube.md`](hc7_k7minus_common_remote_edge_multicentre_cube.md)
at SHA-256

```text
bb7357e7797c8caf5c72a118036c90e63c23661e581d63e24b0878796de29f3d
```

The repaired and subsequently strengthened current source SHA-256 is
`950c9408b093e3f21e88a8ab99f362d15b63dd5327ab76b6d9c0bd0cf1f46b9c`.
Relative to the originally audited version, it incorporates the two repairs
prescribed in Sections 2 and 4 of this audit.  It also imports the independently
audited critical-host defect ladder `D\geq27` and propagates that stronger
input through every incidence estimate.  The arithmetic of that propagation
is checked below.

The two most important exact dependencies are:

```text
d95c459737f7d94e8c212e8f3d90e2b5fbf762f46567d70e6e6d9dfb386dd244  results/hc7_k7minus_matching_lock_boundary_reduction.md
4845f5375581971aca7397bbac0e3eb930dd2943c9dca71f6264a24e2fa31c6e  results/hc7_k7minus_exact_k7vee_separator_dichotomy.md
```

## 2. Incidence and Ramsey checks

For an edge `e=uv`, contraction removes `1+c(e)` edges.  Jakobsen's strict
bound on the six-connected contraction gives

\[
                              D+2c(e)\geq32.
\]

The exceptional vertices not remote from `e` are contained in
`B\cap(N(u)\cup N(v))`; the endpoint correction in (2.9)--(2.10) is
correct.  Minimising

\[
                 D+\left\lceil\frac{32-D}{2}\right\rceil
\]

over the strengthened range `D\geq27` gives `D+c(e)\geq30`, so every edge is
remote from at least `14+\tau-s(u)-s(v)\geq14` exceptional centres.  For
`D=27,\ldots,31`, the five lower bounds in (2.15) are respectively
`16,14,17,15,18`; for `D\geq32` the lower bound is at least sixteen.  Thus the
matching double count remains strict.  Lemma 2.3 then correctly extracts an
independent triple.

The application in Corollary 2.6 is valid, but the sentence beginning
"More generally" is too broad.  At equality, connectedness gives a
contradiction only when `A` is a proper subset of `V(G)`.  Replace it by:

> More generally, let `A\subsetneq V(G)` be a subset of `B` with no
> independent set of order `r+1`.  Then (2.17), degree eight and
> connectedness show that `|A|\geq R(r,5)+8` is impossible.  Apply this to
> the proper set `A=\mathcal R(f)`, which omits both ends of `f`.

The source incorporates this repair.  With the strengthened remote-centre
bound, the Ramsey staircase now starts at `\tau=9` for four independent
centres and at `\tau=23` for five: respectively
`14+9-\lfloor9/5\rfloor=22=R(3,5)+8` and
`14+23-\lfloor23/5\rfloor=33=R(4,5)+8`.  The exact Ramsey values should be
sourced to Greenwood--Gleason for `R(3,5)=14` and McKay--Radziszowski for
`R(4,5)=25`.

## 3. Operation cubes and exact models

The recolouring proof works for every mixed keep/delete/contract pattern.
Each selected component is induced on its own vertex set, expansion creates
only the selected conflicts, and the repair vertices are independent.  The
proper-minor upper bound and the repair lower bound therefore give exact
six-chromaticity in Theorems 3.1, 4.1 and 5.2.

The connectivity restorations in Theorems 3.2, 4.1 and 5.2 are sound.  In
each case every old component survives deletion of the crossing centres,
because a retained centre has degree six in the deletion graph, exceeding
the alleged cut order.  The exact five-, four- and six-cut conclusions
follow with the stated orders.  Lemma 5.1's cyclic separator argument is
valid, as is the palette law in Corollary 5.3.

The density thresholds meet Norin--Totschnig Theorem 6, and the order-25
host excludes its eight-vertex exception.  Absorbing unused vertices makes
the models spanning.  Target exclusion then makes both nominally missing
bag pairs anticomplete in the restored graph, so the claimed exactness is
valid.  The `HC_6` uses in the all-contraction quotients are also legitimate.

## 4. Theorem 6.1 and label re-entry

The label-preserving conclusion is correct, but its dependency must be
identified precisely.  The needed result is Corollary 2.2 of
[`hc7_k7minus_matching_lock_boundary_reduction.md`](../results/hc7_k7minus_matching_lock_boundary_reduction.md),
which descends an arbitrary actual boundary of order at least ten.  The
older large-boundary theorem with a `K_5`-minor-free boundary hypothesis is
not enough.

The descent may use fresh operation edges, but that does not damage the
proof.  Once the final actual boundary `R` has order at most nine, it cannot
contain all eleven vertices of `F_7`.  An original selected edge `q` is
therefore not wholly in `R`; its singleton-signature colouring is proper on
one closed side, and gluing proves rejection by the intact opposite side.
The multiplicity counts in Corollary 6.2 are correct.  The unique order-nine
one-coordinate residue is exactly the row in (6.3).

The final dependency list should therefore replace its last two bullets by
one unambiguous pair:

> - the audited exact-`K_7^\vee` model-separator dichotomy and established
>   case `HC_6`; and
> - Corollary 2.2 of the audited matching-lock actual-boundary reduction.

## 5. Barriers and significance

The manuscript does not cross any recorded barrier.  In particular, the
anchored-coordinate compression barrier shows that a fixed labelled
response alone need not have a small boundary.  Theorem 6.1 legitimately
uses an unlabelled fresh descent only to obtain the small geometry, then
re-enters through an original coordinate by the eleven-versus-nine endpoint
count.

What remains is terminal.  The theorem gives neither a boundary partition
accepted by both shores nor compatibility between the exact
`K_7^\vee` model and the all-contraction `K_6` model.  The connected-full
bridge quotient barrier shows that static fullness and exceptional-boundary
topology do not supply that compatibility.  Thus the exact significance is:

- a universal global edge--centre incidence theorem;
- common independent remote centres and common matching concentration;
- large exact mixed-operation languages on fixed hosts; and
- bounded re-entry of an original operation coordinate.

These are substantial structural advances, not another purely local
normal form.  They do not eliminate a critical-host degree layer, prove a
colouring theorem, or close Conjecture 21.  They therefore fall short of
the requested Norin--Totschnig-level benchmark.
