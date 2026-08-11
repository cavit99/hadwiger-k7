# Internal audit: pairwise contact of common-hole Kempe components

**Verdict:** **GREEN** for Theorem 2.1, Corollary 2.2, and the stated
scope.  This is a separate internal mathematical audit, not external peer
review.

## 1. Exact revision checked

The audited source
`hc7_k7minus_five_centre_b2_pairwise_kempe_touch.md` has SHA-256

```text
8c0c6fb2e39478b336aa28cbde2963a6a8e61bfff2447dee69e4982ca2432cce
```

The direct audited inputs were checked at these source revisions:

- common-hole transition:
  `8dd19d32589ec2a42b4525d445bdcb55e443150dae4a08133f6c30ff1c03bbee`;
- `b=2` rectangle theorem:
  `8843b2c86dbf6ccc6555fd198246c5c9f8a85ffa9ffc69b67f6e40a58d0e3674`.

## 2. Simultaneous Kempe switch

If `K_s` and `K_t` are disjoint and anticomplete, performing the two
switches simultaneously preserves properness.  Each switch is proper on
its own two-colour component; disjointness removes overlap, and
anticompleteness removes every possible new conflict between the two
switched sets.  The boundary colour `gamma` is outside both switched
colour pairs, so the common boundary remains fixed.

Each four-contact set initially uses `Omega-{r}` once each.  Its unique
`s`- and `t`-contacts lie in `K_s` and `K_t`, respectively.  Both become
colour `r`, while the other two contacts retain the two colours in
`Omega-{r,s,t}`.  Thus both contact supports are exactly contained in

\[
                         \{r\}\cup(\Omega-\{r,s,t\}),
\]

a three-set.

## 3. Hall obstruction check

The two opposite-shore availability lists are nonempty and disjoint, so
the erased centres can be assigned two distinct colours.  The resulting
forbidden relation occupies two rows and at most three columns, hence has
at most six positions.  It cannot contain a full row or column, a
`2 by 4` rectangle, or a `4 by 2` rectangle.  The exact Hall criterion
therefore gives an avoiding permutation.  The shore colourings glue,
contradicting non-six-colourability.  Every pair `K_s,K_t` must touch.

## 4. Scope

The proof establishes pairwise contact only.  It does not infer disjoint
paired branch sets, a rooted minor, or a strict separation.  The linked
barrier addresses precisely that stronger local inference.  No unresolved
assumption or gap remains in the theorem as stated.
