# Independent internal audit: two-component shore-split elimination

**Verdict: GREEN.**  The theorem gives valid explicit `K_7^-` minor models
in every unbalanced and balanced two-component literal-shore split.  The
argument is unbounded and computation-free.  This is a separate internal
audit, not external peer review.

**Audited source:**
[`hc7_k44_two_component_shore_split_elimination.md`](hc7_k44_two_component_shore_split_elimination.md)

**Audited source SHA-256:**
`bebf46848e162a037361f74e2da5b02c2cb484789c83b9fe91db4e6e0a69145d`

**Presentation-only recheck (1 September 2026).**  Relative to audited
revision `672d929dfe7df82cbd70d9105f46fec4eed2583e3d8d88c9106e7a490a0c9bdf`,
the theorem now defines vertex-minimality explicitly and names the already
used two-set `H` as `\{d_1,d_2\}`.  An independent recheck found no changed
hypothesis, conclusion, branch-set construction, inference, or contact count.
The GREEN verdict and frozen inputs are unchanged.

**Frozen inputs:**

- adjacent-singleton contraction trace:
  `174baaa7a01d75048575760387f568bbf2ace15cef61e10a2dd5ed35372ca2ef`;
- exact shore-split profiles:
  `9234ff2c545608e7dcb3572dff3875137cbd2978a209826196dc111153d555ae`;
- balanced one-sidedness:
  `5d89f80b93bb185fc7176cf5098a96b506fd8e518c5b7bbc9718867a4d0db664`.

## 1. Unbalanced split

The audit reconstructed the trimmed `b`--`U` path inside the connected
component `D`.  It contains exactly one vertex `u` of `U`.  The sets

```text
{epsilon,s},    (R-s) union {eta},    B_b
```

are disjoint and connected.  Their three mutual contacts are supplied by
`epsilon eta`, `epsilon b`, and `eta b`.  They are universal to the four
`S_0`-rooted sets through `s`, the exact boundary of `R-s`, and `u`,
respectively.

When `x` is exterior, the two unused opposite-shore vertices are exactly
the members of `U-{u}`.  When `x in S_1`, they are the sole member of
`U-{u}` and `x`.  Attaching them to distinct roots produces a `K_4^-`
core.  No branch set overlaps another, and the contact count is
`3+12+5=20` in both the `1+3` and `1+2` cases.

## 2. Balanced split with `R-F` nonempty

After applying the independently audited one-sidedness theorem, every
component of `R-F` misses `a`, either alone or together with `p`.
Fullness and label disjointness therefore give distinct endpoint neighbours
`f_a,f_p in F`.

If an `a`-component `W` exists, its only possible second missed resource is
`u in T`.  The audit checked that

```text
{a,f_a},    W union {p},    B_b
```

form a triangle.  The `b`--`H` path bag contains exactly one member of
`H`; the other member of `H` and `f_p` complete the core.  If `u in S_0`,
the inequality `|N_F(W)|>=|M_W|=2` makes `f_p` available in the
`u`-rooted set and repairs the unique missing contact.  Otherwise `W`
already sees every core root.  Thus all three outside sets are universal
to a `K_4^-` core.

If there is no `a`-component, every component has missed set `{a,p}` and
sees both vertices of `F`.  For any such component `W_0`, the sets

```text
W_0 union {x},    {a,f_a},    {p,f_p}
```

form a triangle universal to the core.  The two vertices of `H` complete
the core to `K_4^-`.  This again gives exactly the required 20 contacts.

## 3. The residue `R=F`

The audit independently derived the exact neighbourhoods

```text
N(f)=S_0 union {g,x,a},    N(g)=S_0 union {f,x,p}.
```

They follow from connectedness of `R`, fullness, minimum degree seven, and
the disjoint endpoint label sets.  Hence `{a,f}` and `{p,g}` are adjacent
connected sets universal to the four core roots.

For a component `C` of `D-H` seen by `x`, the inequality

```text
|N_{S_0}(C)|+|N_H(C)| >= 4
```

is exact enough to assign the two vertices of `H` to distinct roots and
repair every missed root.  The same allocation works with the singleton
`{x}` whenever `|N_{S_0}(x)|+|N_H(x)|>=4`.

Otherwise minimum degree forces `x=b`, adjacency from `x` to both
endpoints, and exactly three incidences from `x` into `S_0 union H`.
The audit checked the two-resource allocation in all three cases
`|N_H(x)|=0,1,2`.  Its only exceptional pattern is that `x` sees both
vertices of `H` and one root `q`, while `C` sees precisely
`S_0-{q}`.  Outside that pattern, adjoining `C` to a pure root makes the
core a `K_4`, while `x` contacts three core sets; the count is
`6+11+3=20`.  In the exceptional pattern, the seven-boundary inequality
forces `C` to see both vertices of `H` and both endpoints, so `C` itself
is the third universal member of the outside triangle over a `K_4^-`
core.

Finally, when `D=H`, fullness and label disjointness give each endpoint
exactly one neighbour in `H` and one in `F`.  With the other endpoint and
`x=b`, each has four fixed neighbours.  Minimum degree forces at least
three disjoint `S_0` labels for each endpoint, impossible in a four-set.

## 4. Scope

Every displayed branch set was checked for connectivity, pairwise
disjointness, and the stated contacts.  There are no unresolved assumptions
inside the theorem's hypotheses.  The result eliminates exactly the
two-component literal-shore-split alternative.  It does not eliminate the
core-concentrated or three-component contraction responses, a nonsingleton
blocker, the literal `K_{4,4}` case, T44, Conjecture 21, or `HC_7`.
