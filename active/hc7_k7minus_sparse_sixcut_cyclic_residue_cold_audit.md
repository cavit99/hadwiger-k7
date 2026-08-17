# Independent cold audit: cyclic residue of a sparse returned six-cut

**Verdict:** **GREEN** at the frozen mathematical revision

```text
1161d75f085b91d4f6a8fd8ec0b238858200b49da3146455c2ba4d78dcedbd29
  active/hc7_k7minus_sparse_sixcut_cyclic_residue.md
```

The current source SHA-256 is
`19daca46ffa9e7e9f265560c2e71c2dd8be4c3ef11782c8b3bd8caa918857291`.
The only later change records this GREEN audit in the status line; no
statement, proof, constant, dependency, or scope claim changed.  This is
an independent internal mathematical audit, not external peer review.

## 1. Imported incidence bounds

The sole non-elementary input was checked at its cited frozen revisions:

```text
adfcc70aca8543e15bcf7e94e1fb310492535f8155f02cb5a5430adba4ce8372
  active/hc7_k7minus_sparse_sixcut_four_root_carrier_packing.md
4a185697d20ed73c358703eb7d433c3555bca6474497a011630d3805dc493e97
  active/hc7_k7minus_sparse_sixcut_four_root_carrier_packing_cold_audit.md
```

It gives

```text
sum_{v in C} binom(a(v),4) <= B,
```

where `B=30` in general and `B=27` if `G[S]` has a three-set
spanning at least two edges.  The hypothesis `Delta(G[S])>=2` supplies
such a set by taking a vertex of boundary degree at least two and two of
its neighbours.

## 2. Low internal degrees

For a component `C` of `G-S`, every edge incident with a vertex of `C`
has its other end in `C union S`.  Six-connectivity gives minimum degree
at least six, so

```text
d_C(v)+a(v)=d_G(v)>=6.
```

When `c>=2`, connectedness excludes internal degree zero.  Hence every
internal-degree-one vertex has `a(v)>=5` and contributes at least
`binom(5,4)=5` to the incidence sum, while every
internal-degree-two vertex has `a(v)>=4` and contributes at least one.
Writing their numbers as `n_1,n_2` gives the simultaneous inequality

```text
5n_1+n_2<=B.                                         (A)
```

No contribution from a higher-degree vertex is needed for this bound.

## 3. Cycle-rank arithmetic

For the connected graph `G[C]`, with
`beta=|E(G[C])|-|C|+1`, the degree sum gives

```text
sum_{v in C}(d_C(v)-2)=2 beta-2.
```

If `h` is the number of internal-degree-at-least-three vertices, the
left side is at least `-n_1+h`.  Therefore

```text
h<=2 beta-2+n_1.                                    (B)
```

Combining (A) and (B), without assuming any independence between the
two estimates, yields

```text
c=n_1+n_2+h
 <=2n_1+n_2+2 beta-2
 <=B-3n_1+2 beta-2
 <=B+2 beta-2.
```

Thus `B=30` gives `c<=28+2 beta`, and `B=27` gives
`c<=25+2 beta`.  The isolated component case `c=1` has `beta=0` and
satisfies both bounds directly.

## 4. Nontrivial trees and the residue

For a nontrivial tree, `beta=0` and `n_1>=2`.  Retaining the term
`-3n_1` in the preceding calculation gives

```text
c<=B-3n_1-2<=B-8,
```

which is exactly `22` for `B=30` and `19` for `B=27`.  Conversely,
rearranging the two general bounds and using integrality gives the stated
lower bounds

```text
beta(C)>=ceil((c-28)/2)
```

and, under the boundary-degree hypothesis,

```text
beta(C)>=ceil((c-25)/2).
```

The proof therefore rules out unbounded order at bounded cycle rank but
does not bound the cycle rank or the excess of a cyclic component.  The
source states this nonclosure accurately.  No hidden connectivity,
degree-sum, rounding, or endpoint case was found.
