# Internal audit: a clean fan from a paired boundary trace

**Verdict:** **GREEN**.

**Audited source:**
[`hc7_k7minus_four_centre_paired_trace_fan.md`](hc7_k7minus_four_centre_paired_trace_fan.md)

**Audited mathematical revision SHA-256:**

```text
80662a131588db4fe69168bef1d88432922ca8697c1266b6c1ed0ea42f004eb0
```

**Promoted source SHA-256:**

```text
ad8a30f5e316fccdbc9319aa8788a00096c599656310ab10498246cdb2c0043c
```

The promoted source differs from the audited mathematical revision only by
replacing the opening `pending` status with a link to this audit.  No
hypothesis, conclusion or proof step changed.

This is a separate internal mathematical audit, not external peer review.
The proof was reconstructed independently against the pinned inputs below.
No unresolved assumption or gap was found within its stated scope.

## Fan and separator check

The first internal vertices of the three Kempe paths lie in `C`, are
adjacent to `p`, and are distinct because they have the three distinct
secondary colours.  Duplicating `q` therefore gives the correct target set
`{p',q_1,q_2}` for the fan form of Menger's theorem.

If a three-fan is absent, Menger gives a set `W` of at most two vertices
which prevents `p` from reaching every target outside `W`.  With

```text
Z=W cap C,
epsilon=1 when p' is in W,
rho=|W cap {q_1,q_2}|,
```

one of the three first Kempe vertices avoids `Z`.  Its component `A` in
`G[C-Z]` is reachable from `p`.  This proves each term in the displayed
neighbourhood bound: outside `C`, the component can meet `U` and `p`; it
can meet `p'` only when `epsilon=1`, and it can meet `q` only when both
copies of `q` lie in `W`.

Seven-connectivity then gives

\[
 7\le |N_G(A)|\le
 5+|Z|+\epsilon+\boldsymbol 1_{\{\rho=2\}},
 \qquad |Z|+\epsilon+\rho\le2.
\]

The cases `rho=1,2` have upper bound six.  Hence `rho=0`,
`|Z|+epsilon=2`, and equality forces exactly one of the two boundaries in
(2.8).  In both cases this is an exact cut of the form `U dotcup T^*`.

The opposite old component `D` survives outside the new boundary.  The
two-component theorem therefore makes `A` one full connected component of
the new cut and places `D` in the other.  The new selected closed shore is
contained in the old one, so the fixed trace colouring restricts, the four
nominated roots avoid `A`, and the fixed opposite root remains in `D`.
Because `Z` is a nonempty subset of `C`, the new selected component is a
proper subset of `C`.  This is the required contradiction to trace
minimality.

Finally, identifying the two copies of `q` turns the three-fan into one
`p`--`p'` path and two `p`--`q` paths with exactly the stated intersections.

## Pinned dependencies

```text
exact-boundary bridge reduction
eca904897e1d32126be1399034966d3304d724ae746fcb83a7b1c56e1b561b0a

trace-preserving descent
04d4585b25ce9fbd8f3392b715eb28caa7e4b008e45072ede2b08cbbf0bfecff

two-component normal form for seven-vertex cuts
1041988a33b749bef5802dd21d3cd9419b5afc754735a20174bf5a13c0a56c96
```

The theorem does not produce a boundary-full connector disjoint from the
fan, a rooted `K_6^-` model, or a proof of the `K_7^-` six-colour conjecture.
