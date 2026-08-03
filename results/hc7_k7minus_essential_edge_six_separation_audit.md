# Internal audit: essential-edge six-separations at the `4n-2` threshold

**Audited source:**
[`hc7_k7minus_essential_edge_six_separation.md`](hc7_k7minus_essential_edge_six_separation.md)

**Audited source SHA-256:**
`0a652b431e9e0bd92fcc0aa76fa120c4ffcbc7c61a0d0198b2cc475a3ce79b92`

**Verdict:** **GREEN.**  The theorem and both exact counting identities are
correct.  The proof is computation-free.  This is a separate internal
mathematical audit, not external peer review.

## Audit

Let `H=G-xy`.  Edge-minimality gives `kappa(H)<=6`.  If a set `Z` of at
most five vertices disconnected `H`, neither endpoint of `xy` could belong
to `Z`, since then `G-Z=H-Z`.  As adding the single edge `xy` reconnects
`H-Z`, that graph has exactly two components, with `x` and `y` in different
components.  The `x`-component is not a singleton: otherwise

\[
                         N_G(x)\subseteq Z\cup\{y\}
\]

would contradict `d_G(x)>=7`.  Deleting `Z union {x}` would therefore leave
nonempty vertices on both sides and disconnect `G` with at most six deleted
vertices.  This proves `kappa(H)>=6`, and hence equality.

For an order-six cut `S` of `H`, neither endpoint of `xy` is in `S`, since
otherwise `G-S=H-S`.  One added edge can join all components of `H-S` only
when there are exactly two, with its endpoints on opposite shores.  Thus
the shores `A,B` and the assertion that `xy` is their unique edge in `G`
are exact.  Six-connectivity of `H` also makes each shore adjacent to every
vertex of `S`: omitting one boundary vertex would leave a cut of order at
most five.  If both shores were singletons, seven-connectivity on the
resulting eight vertices would force `G=K_8`, contrary to target exclusion.

Simultaneously contracting the two connected shores produces two adjacent
vertices, each complete to `S`.  A `K_5^-` model in `G[S]` would consequently
extend to a `K_7^-` model.  The boundary exclusion is therefore valid.

For the rooted assertion, suppose `(U,W)` is a forbidden separation of
`H[X union Q]` and put

\[
                         Z=(U\cap W)\cup(S-Q).
\]

Because `Q subseteq U`, every vertex of `W-U` lies in `X`.  It has no edge
to the opposite shore, no edge to `U-W` inside the closed shore, and all
remaining possible boundary neighbours lie in `Z`.  The opposite shore
survives, while

\[
 |Z|\le(|Q|-1)+(6-|Q|)=5.
\]

This contradicts six-connectivity of `H`.  The conclusion is valid for
every nonempty `Q subseteq S`, including the endpoint cases.  For four
roots and a nonsingleton shore, the graph has at least six vertices, so the
stated later use of Jørgensen's rooted-diamond theorem has the required
size and rooted-connectivity hypotheses.

For the surplus identities, write `a=|A|`, `b=|B|` and
`e_S=|E(G[S])|`.  The edge partition is

\[
 |E(G)|=(4a+\delta_A)+(4b+\delta_B)+e_S+1,
 \qquad |V(G)|=a+b+6,
\]

where the final edge is `xy`.  Subtracting `4|V(G)|-2` gives

\[
                    \delta_A+\delta_B=21+q(G)-e_S.
\]

When a shore `X` is contracted, all of its internal and boundary edges,
together with `xy`, are replaced by exactly six simple edges to `S` and
one edge to the opposite shore.  Hence

\[
 |E(G/X)|=|E(G)|-4|X|-\delta_X+6,
 \qquad |V(G/X)|=|V(G)|-|X|+1,
\]

and therefore `q(G/X)=q(G)+2-delta_X`.  This also checks that parallel-edge
simplification has been accounted for rather than silently ignored.

Finally, the scope records a genuine nonclosure.  Four rooted bags in one
shore, the opposite shore enlarged by the sole unused boundary vertex, and
the singleton boundary vertex with four named neighbours give only six
branch sets.  The remaining boundary vertex cannot in general be split off
as a seventh bag with all required adjacencies.  Thus the argument does not
prove that `G[S]` is subcubic, and the source correctly makes no such claim.

## Unresolved assumptions

None within the stated theorem.  The theorem does not assert that a shore
contraction preserves seven-connectivity or that the six-separation alone
completes the `4n-2` extremal theorem.
