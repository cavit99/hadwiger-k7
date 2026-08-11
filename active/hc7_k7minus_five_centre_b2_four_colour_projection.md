# Four-colour projections of the `b=2` common-hole orbit

**Status:** written proof; separate internal audit GREEN at the revision
recorded in the adjacent audit.
Deleting the hole colour from the exact five-chromatic core gives an exact
four-chromatic graph.  For a hole in one centre's availability list, the
other centre's neighbourhood is colourful in every four-colouring.  The
three-contact bound on the `D`-shore then forces that colourful set, and
the Martinsson--Steiner rooted `K_4`, entirely into `C`.  This gives a
shore-confined single-centre-rooted `K_5` model.  The argument does not make the first
centre's neighbourhood colourful in every four-colouring and does not
synchronize two rooted models.  It therefore does not close the `b=2`
branch.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting

Use the notation and conclusions of the common-hole transition theorem in
[`hc7_k7minus_five_centre_b2_common_hole_transition.md`](hc7_k7minus_five_centre_b2_common_hole_transition.md).
Thus

\[
 H=G-\{z_p,z_q\},\qquad X=H-\Gamma,                 \tag{1.1}
\]

where `Gamma` is one fixed independent colour class, `chi(X)=5`, and

\[
 S_x=N_X(z_x)\qquad(x\in\{p,q\}).                  \tag{1.2}
\]

Every proper five-colouring of `X` makes at least one of `S_p,S_q`
colourful.  For every `r` in the five-colour palette `Omega`, the
common-hole orbit supplies a five-colouring `c_r|X`, and

\[
 S_x\text{ is colourful in }c_r|X
       \quad\Longleftrightarrow\quad r\notin L_x,   \tag{1.3}
\]

where the nonempty lists `L_p,L_q` are disjoint.

For `r\in\Omega`, put

\[
 V_r=\{v\in V(X):c_r(v)=r\},\qquad Y_r=X-V_r.      \tag{1.4}
\]

## 2. The forced colourful projection

### Theorem 2.1 (one-sided four-colour projection)

For every `r\in L_p`, all of the following hold.

1. `chi(Y_r)=4`.
2. The set `S_q\cap V(Y_r)` is colourful in every proper
   four-colouring of `Y_r`.
3. The graph `G[C\cap V(Y_r)]` is four-chromatic, and `N_C(z_q)` is
   colourful in every proper four-colouring of it.
4. The graph `G[C\cap V(Y_r)]` contains a `K_4`-minor model rooted at the
   four literal vertices of `N_C(z_q)`.
5. Adjoining the singleton branch set `\{z_q\}` gives a `K_5`-minor
   model confined to `G[(C\cap V(Y_r))\cup\{z_q\}]`.

Symmetrically, for every `r\in L_q`, the same conclusions hold with
`p,q` interchanged.

#### Proof

The colouring `c_r|Y_r` uses at most four colours, so `chi(Y_r)\le4`.
If `Y_r` were three-colourable, colour its vertices with three colours and
give the independent set `V_r` one fresh colour.  This would four-colour
`X`, contrary to `chi(X)=5`.  Hence `chi(Y_r)=4`.

Now fix an arbitrary proper four-colouring `psi` of `Y_r` and extend it to
a proper five-colouring of `X` by giving all of `V_r` one fresh fifth
colour.  Since `r\in L_p`, the exact support formula

\[
 \{c_r(v):v\in S_p\}=(\Omega-\{r\})\cup(\Omega-L_p)
\]

from Theorem 3.1 of the common-hole transition theorem, together with the
definition of `V_r`, gives

\[
                         S_p\cap V_r=\varnothing.    \tag{2.1}
\]

Thus `S_p` cannot be colourful in the extended five-colouring: it has no
neighbour in the fresh colour class.  The universal two-root colouring
cover therefore forces `S_q` to be colourful.  Its vertices in `V_r`
account only for the fresh fifth colour, so `S_q\cap V(Y_r)` must use all
four colours of `psi`.  Since `psi` was arbitrary, this proves item 2.

Put

\[
 Y_C=G[C\cap V(Y_r)],\qquad Y_D=G[D\cap V(Y_r)].    \tag{2.2}
\]

These graphs are anticomplete and their union is `Y_r`: all five vertices
of the independent boundary set `T` belong to `Gamma` and have been
deleted.  Write

\[
 U_C=S_q\cap V(Y_C),\qquad U_D=S_q\cap V(Y_D).
\]

At least one of `U_C,U_D` is colourful in every proper four-colouring of
its corresponding graph.  Otherwise choose a four-colouring on each side
which misses a colour on the displayed set.  Permute the colour names on
one side so that the two missing colours agree.  Their union would be a
four-colouring of `Y_r` in which `S_q` misses that colour, contradicting
item 2.

The set `U_D` has order at most three, because `z_q` has exactly three
neighbours in `D`.  It cannot use all four colours in any colouring.
Consequently `U_C` is colourful in every proper four-colouring of `Y_C`.
In particular `chi(Y_C)=4`; a colouring with at most three colours would
contradict colourfulness.  The common-hole property gives

\[
                         U_C=N_C(z_q),               \tag{2.3}
\]

because the four `C`-contacts use the four colours in `Omega-\{r\}` and
therefore none lies in `V_r` or `Gamma`.

Martinsson and Steiner, Theorem 1.3 in
[*Strengthening Hadwiger's conjecture for 4- and 5-chromatic graphs*](https://arxiv.org/abs/2209.00594),
says that a colourful set in a four-chromatic graph roots a `K_4` minor.
It gives item 4.  Since `|N_C(z_q)|=4`, disjointness makes the four
contacts occur one per branch set.  Every branch set is adjacent to
`z_q`, so adding `\{z_q\}` gives item 5.  The proof for a hole in `L_q`
is symmetric. \(\square\)

### Corollary 2.2 (models in both orientations)

The common-hole orbit supplies a `z_q`-rooted `K_5` model in `C\cup\{z_q\}`
for every hole in `L_p` and a `z_p`-rooted `K_5` model in
`C\cup\{z_p\}` for every hole in `L_q`.  In each case the four non-centre
bags are rooted at all four `C`-contacts of the displayed centre.  The
models are obtained in different four-chromatic vertex-deleted graphs;
no common branch-set model is asserted.

## 3. The first unsupported inference

For `r\in L_p`, the same argument does **not** prove that
`S_p\cap V(Y_r)` is colourful in every four-colouring of `Y_r`.  If a
four-colouring misses a colour on that set, the resulting five-colouring
of `X` still has `S_q` colourful, exactly as the universal cover permits.
There is no contradiction.

Even an additional proof that both `S_p\cap V(Y_r)` and
`S_q\cap V(Y_r)` are colourful would not, by itself, produce one `K_4`
model whose every branch set meets both sets.  The explicit separately
audited
[paired-colourful planar-core barrier](../barriers/hc7_paired_colourful_planar_core_barrier.md)
has a four-connected planar four-chromatic graph with two sets colourful
in every four-colouring but no `K_4` model rooted at both sets.  That
barrier is not a critical host and does not refute a host-assisted
synchronization theorem; it does refute the static paired inference.

Consequently Theorem 2.1 yields one shore-confined rooted `K_5`, not the
two additional branch sets required for a `K_7^-` model.  A terminal
composition must use the deleted colour class `V_r`, the fixed class
`Gamma`, the literal orientation-changing component, or the retained
centres on the opposite shore to synchronize the second centre with the
same four bags.  Martinsson--Steiner applied separately to different
members of the common-hole orbit does not provide that synchronization.

## Dependencies and claim status

- exact five-chromaticity, the universal two-root colouring cover, and
  the common-hole orbit are the written conclusions of the active
  common-hole transition theorem, which is awaiting separate audit;
- the rooted `K_4` conclusion is the established external theorem of
  Martinsson--Steiner cited above; and
- the failure of static paired synchronization is witnessed by the
  separately audited repository barrier cited in Section 3.

All new deductions are proved here.  No paired-rooted `K_4`, `K_7^-`
minor, or closure of the `b=2` row is claimed.
