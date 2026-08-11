# Internal audit: singleton-contact shift to an exact six-cut

Audited file:
`active/hc7_k7minus_five_centre_singleton_shift.md`

Audited SHA-256:

```text
6398ef32f17ba1174031b2c99fd5985b60a61b7ffcd48ccc5b2b00686fcff5c1
```

**Verdict:** **GREEN** for Theorem 1.1, Lemmas 2.1--6.2, the exact
identities (4.4)--(4.16), and the explicitly nonterminal scope of this
revision.

This is a hash-pinned internal mathematical audit, not external peer
review.  Relative to the theorem revision originally checked, the source
changes only its audit-status metadata; no theorem or proof text changed,
so the GREEN verdict is retained.  The theorem derives a normal form and a
sharp obstruction rather than eliminating the singleton-contact case.

## 1. Exact six-cut and chromatic shift

The edge `zx` is the only edge from `z` to `C`.  After deleting it,
`C` and `E=D\cup\{z\}` are therefore precisely the components of `H-B`.
The latter is connected because

\[
                         d_z=7-\rho_z\ge5.
\]

Both components are full at the six-set `B`, inherited from fullness of
`C,D` at `S`.

The six-connectivity argument is valid.  A separator `Q` of `H` of order
at most five could be repaired in `G-Q` only by the edge `zx`; hence
`H-Q` would have exactly two components containing its ends.  The
`z`-component has a vertex besides `z`, since `d_H(z)=7>|Q|`.  Deleting
`Q\cup\{z\}` would then separate two nonempty sets in `G`, contrary to
seven-connectivity.  Thus `B` is an exact order-six cut.  A proper
six-colouring of `H` exists by minor-minimality, and its ends `x,z` must
have the same colour, or it would colour `G`.

## 2. Minimal shifted four-root circuit

If `Y=Z-\{z\}` were feasible on `C`, the separately audited equal-response
transfer supplies a `D`-side colouring with `Y` monochromatic, `p,q`
monochromatic in a second colour, and `z` avoiding that pole colour.  The
equal-response `C`-colouring, restricted after deleting `z`, has the same
two boundary blocks.  Their only uncoloured cross-edge is `zx`.  Its
`C`-end avoids the root colour, and the four remaining colour names on the
other side can be permuted to make `zx` proper.  This would six-colour
`G`, so `Y` is infeasible.

For a minimal infeasible proper subset `T` of `Y`, every member of the
Du--Li--Xie--Yu terminal-avoiding collection would acquire at most the
`5-|T|` omitted centres when lifted to `G`.  Its whole-graph neighbourhood
would consequently have order at most six and separate it from `D`.
Seven-connectivity makes the collection empty.  The restricted identities
are then exact.  For `|T|=2`, the omitted centre `z` contributes six to
the displayed defect sum and makes the right side of (3.1) negative.  For
`|T|=3`, the same contribution makes the right side of (3.2) at most two.
Fullness gives lower bounds two and three, respectively.  Singletons are
feasible directly through connected `C`, so `Y` is inclusion-minimal.

## 3. Scalar bookkeeping

The order-six excess calculation is exact:

\[
 q_H=e(H)-(4|V(H)|-2)=\eta+1,
 \qquad
 \delta_C+\delta_E=q_H+22-e(H[B])=23+\eta-b.
\]

On `C`, the two input equations are

\[
 m_C+e_H(C,B)=5c+1-\sigma,
 \qquad
 8c+g_C=2m_C+e_H(C,B)+1,
\]

where the final one is the deleted edge `zx`.  Solving them gives all
three identities in (4.5); subtracting the pole incidences gives (4.6).
The four root contacts then give (4.7).

On `D`, the five-root bound and its degree sum give (4.8).  The equality
`d_z=7-\rho_z` and four further positive root contacts give (4.8a).
Adjoining `z` to `D` and accounting for its deleted `C`-edge gives (4.9).
Equivalently, the excess of `z` inside `H` is minus one, so

\[
             2\delta_E=e_H(E,B)+g_D-1,
\]

which proves (4.10).  The lower bound uses six distinct `D`--`B`
incidences plus the `\rho_z` edges from `z` to `B`.

The global degree identities

\[
 2\eta=g_C+g_D+\lambda,
 \qquad
 h_C+h_D+b+\rho_z=16+\lambda
\]

give (4.11) and (4.11a).  Substitution in the exact six-cut equation gives
(4.12)--(4.13).  Jakobsen's bound becomes
`2\eta\le c+d-18`, exactly (4.15).  The arithmetic witness in Section 7
satisfies every displayed equality and inequality.

## 4. Density and local neighbourhood conclusions

The four critical-edge paths give `h_C\ge8`; the distinct-side
bichromatic path gives `h_D\ge2`.  Hence both `xi_C,xi_D` are nonnegative.
The source's proof that the full five-root instance on `D` is infeasible
uses only the two opposite responses and seven-connectivity; it does not
use the no-singleton hypothesis appearing later in the cited note.

The unique vertex `x` is anticomplete to `N_D(z)`.  Thus an independent
triple there, together with `x`, would contradict the audited equality
`\alpha(G[N(z)])=3`.  The set has at least five vertices and is `K_4`-free,
so it is not complete and has independence number exactly two.  This
checks (4.16).

Equation (4.5) gives `m_C\ge3c-2`; the standard extremal bound
`e(F)\le3|V(F)|-6` for `K_5`-minor-free graphs therefore supplies an
unrooted `K_5` minor in `C`.  The audited order-six and order-seven
equality-shore eliminations give `c\ge8`.  The proof of the hash-pinned
GREEN four-root atom identity applies to the shifted circuit: its omitted
centre is used only as one possible extra neighbour when terminal-avoiding
sets are lifted.  It does not require that omitted centre to have two
`C`-contacts.  Thus (4.17) and its singleton consequence are valid.

## 5. Boundary matching and fan model

For a boundary edge `up`, failure of a disjoint `wq` makes
`I=S-\{u,p\}` independent.  The exact reflection lemma applies to
`I\mid\{u\}\mid\{p\}` on either full component.  The two resulting
closed-shore colourings have the same exact boundary partition and glue,
a contradiction.  Every boundary edge therefore extends to a matching of
order two.  Since the two poles cover all boundary edges, the matching
number is exactly two.

In a six-colouring of `H`, a Kempe swap shows that `x,z` lie in the same
two-colour component for each non-root colour.  The five resulting first
edges at `x` are distinct.  The audited prescribed-spoke theorem applies
to those edges together with `xz` and the literal six-set `B`.  Truncation
at first boundary hits preserves disjointness and uses every member of
`B`.  The `xz` arm stays in `E`, while the other arms stay in `C`, until
their first hits.

After absorption, `{x}` and `R_0` are universal adjacent bags over the
five limb bags.  Nine limb adjacencies would therefore give seven disjoint
connected branch sets with at most one absent pair, an explicit `K_7^-`
model.  Hence `e(J)\le8`.

## 6. Sharp witness and unresolved assumptions

The tables (7.1)--(7.5) are correctly labelled as arithmetic and local
incidence data, not as existence of a global critical host.  The displayed
`K_8` minus a perfect matching has 24 edges, chromatic number four, no
literal `K_5`, and gives every `C` vertex degree eight after (7.5).  The
five limb sets in (7.6) have exactly eight mutual adjacencies: four from
the `p`-limb and four among the remaining limbs.  Thus the fan bound is
sharp for all explicitly retained data.

The audit leaves the following gaps exactly as the source states:

- the unrooted `K_5` minor has no prescribed boundary contacts;
- the spoke theorem does not prescribe the endpoint of the `xz` arm;
- the opposite bichromatic path intersects the two limbs containing its
  literal pole ends if absorbed whole; and
- the four equality-side paths have neither simultaneous disjointness nor
  allocation to the five limb labels.

No six-colouring, terminal `K_7^-` model, or strict separator descent is
deduced from these data.  The source does not claim otherwise.
