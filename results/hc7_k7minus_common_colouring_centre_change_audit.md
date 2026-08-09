# Internal audit: common colouring and the opposite-side cut family

**Verdict:** **GREEN**.

**Audited source:**
[`hc7_k7minus_common_colouring_centre_change.md`](hc7_k7minus_common_colouring_centre_change.md)

**Audited source SHA-256:**

```text
8c1c27b99edbd5b73ccc6254eafb10dfddeed62d3b271e4e8ba527783a08412a
```

This pin includes Corollary 4.3 and the final terminology edit.  Separate
auditors reconstructed the common-colouring theorem, the cut-family bound,
all simultaneous replacements, and the Boolean separation identities.  No
hypothesis, conclusion, citation or proof step remains unaudited.

This is a separate internal mathematical and citation audit, not external
peer review.  The proof was reconstructed against the exact external
theorems and the pinned local inputs.  No unresolved assumption or gap was
found within its stated scope.

## Common colouring and change of deleted vertex

The four selected old colour classes induce a four-chromatic graph `J`: a
three-colouring of `J`, together with the two untouched classes, would
five-colour `H`.  Martinsson--Steiner, Theorem 1.3, applies by
contrapositive and gives a four-colouring of `J` using at most three colours
on the nominated roots.  Splicing the palettes is proper.

The old deleted vertex is not saturated in the resulting colouring
`theta`.  If no centre were saturated, independent missing-colour choices
on the independent set `U` would six-colour `G`.  Thus another centre is
saturated.  Six positive colour multiplicities among eight neighbours have
total excess two, so at least four colour classes are singletons.

If there is one saturated centre `s`, `theta` extends to `G-s`, with its
restriction to `H` unchanged.  The audited four-centre theorem therefore
returns the stated rooted `K_5` model or a traced exact cut.  With several
saturated centres, the source does not claim such an extension; it applies
Fabila-Monroy--Wood directly in `H` and asserts no colouring trace.  This
distinction is correct.

## Exact-cut comparison

Every component behind an exact four-centre cut has at least three vertices.
A singleton contradicts minimum degree eight; a two-vertex component puts
the four independent centres in a degree-eight neighbourhood.

If a new cut splits `C`, or meets `C` while leaving `C` on one open side,
fixed-anchor exact uncrossing gives a nonempty proper selected component
inside `C`.  Its closed side lies in the old selected closed side, so the
fixed colouring and named roots restrict.  This contradicts trace
minimality.  Hence every distinct cut is oriented with

\[
 C\subseteq A,
 \qquad
 \varnothing\ne B\subsetneq D,
 \qquad
 N_D(B)=T'\cap D.
\]

The removed old boundary vertices are anticomplete to `B`.  No old trace is
asserted on `B`.

## Minimal cut family

Two intersecting inclusion-minimal far-side components have an exact
fixed-anchor join whose right open side is their intersection.  The
two-component theorem makes it connected, contradicting minimality.  Thus
the minimal members are disjoint.

Every neighbour of a member in the interaction graph consumes a distinct
vertex of its three-vertex boundary, so the maximum degree is at most three.
Three independent members, together with `C`, would give four independent
neighbours of every centre, so the independence number is at most two.

If the interaction graph contains a triangle and a fourth vertex, the seven
branch sets in (4.3) form a `K_7^-` model; only the last two singleton
centres may be nonadjacent.  If five vertices survive, triangle-freeness and
independence number two force a five-cycle.  The branch sets in (4.4) then
form a `K_7^-` model; only `B_1,B_3` may be nonadjacent.  Hence the family
has at most four members.  With four, both the graph and its complement are
triangle-free, leaving exactly `2K_2`, `P_4`, and `C_4`.

## Simultaneous centre replacement

In the equality case there are five pairwise disjoint full connected pieces.
For each centre `u`, their positive neighbour multiplicities satisfy

\[
 \sum_P(m_{uP}-1)+r_u=3.
\]

At least two pieces therefore contain a unique neighbour of `u`, and the
total number of unique-neighbour incidences is at least eight.  Distinct
centres cannot have the same unique neighbour in one piece: deleting that
vertex would leave a nonempty set separated from the old opposite component
by at most six vertices.

For every nonempty `W subseteq W_P`, the induction in Corollary 4.2 keeps
`P-X(P,W)` nonempty.  After deleting

\[
 Z(P,W)=(U-W)\cup T_P\cup X(P,W),
\]

the other side is exactly `O_P union W` and is connected.  Every component
of the first side has neighbourhood contained in the seven-set `Z(P,W)`.
Seven-connectivity forces equality; the two-component theorem then makes
the first side connected and full.  A singleton would have degree seven,
so the remainder has at least two vertices.

The replacement cuts are all distinct.  Their intersections with `U`
recover `W`.  For a fixed nonempty `W`, equal cuts from different pieces
would leave two distinct component remainders while any member of `W`
survives and is anticomplete to both, producing a third component.

If `k_P=|W_P|`, the number of replacement cuts is

\[
 \sum_P(2^{k_P}-1).
\]

For five nonnegative integers of sum at least eight, discrete convexity
minimizes this at `2,2,2,1,1`, giving eleven.  The five original
four-centre cuts are distinct and contain all four centres; the replacement
cuts omit a nonempty set of centres.  The claimed total of at least sixteen
distinct exact order-seven cuts follows.

## Boolean separation sublattices

For a fixed component `P`, the closed sides in Corollary 4.3 satisfy

\[
 A_W=P\cup T_P\cup(U-W),
 \qquad
 B_W=O_P\cup T_P\cup U\cup X(P,W).
\]

Their intersection is exactly the seven-vertex cut `Z(P,W)`, and their
open sides are `P-X(P,W)` and `O_P union W`.  Injectivity of
`u mapsto x_{uP}` gives

```text
X(P,W_1) cap X(P,W_2)=X(P,W_1 cap W_2).
```

Direct set algebra therefore makes meet correspond to `W_1 union W_2` and
join to `W_1 cap W_2`.  The family is a Boolean sublattice with the subset
order reversed.  Since the five values `|W_P|` have sum at least eight,
one has order at least two and supplies a four-element square.

The old opposite component is nonempty, so `G[A_emptyset]` is a proper
minor and has a six-colouring.  Every other `A_W` is a subset of
`A_emptyset`; restriction therefore gives the stated coherent boundary
partition at every cut.  This does not compare the opposite-side colouring
responses.

## External sources and pinned local dependencies

- A. Martinsson and R. Steiner, *Strengthening Hadwiger's conjecture for
  4- and 5-chromatic graphs*, J. Combin. Theory Ser. B **164** (2024),
  1--16, <https://doi.org/10.1016/j.jctb.2023.08.009>, Theorem 1.3.
- R. Fabila-Monroy and D. R. Wood, *Rooted `K_4`-Minors*, Electron. J.
  Combin. **20**(2) (2013), Paper P64,
  <https://doi.org/10.37236/3476>, Theorem 8.

```text
four-centre rooted-web theorem and exact-cut lattice
e7fcf00c9bdbd2fcbab78bb13d4244a659f4f7db0ae45a97cfbd9a8d599a0ee3

trace-preserving minimum four-centre cut
04d4585b25ce9fbd8f3392b715eb28caa7e4b008e45072ede2b08cbbf0bfecff

two-component normal form for seven-vertex cuts
1041988a33b749bef5802dd21d3cd9419b5afc754735a20174bf5a13c0a56c96

degree-eight neighbourhood structure
fc1e88c28b1f4d0dc7a1cbdeefa19fecfd5e969b986c64e11eb1990615f5dfbd
```

The theorem does not compare the simultaneous-replacement cuts by
fixed-anchor uncrossing, turn the rooted `K_5` into a `K_7^-` model, or
prove the `K_7^-` six-colour conjecture.
