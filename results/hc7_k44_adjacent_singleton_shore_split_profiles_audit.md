# Independent internal audit: adjacent-singleton shore-split profiles

**Verdict: GREEN.** The exact source revision identified below is a valid
written unbounded reduction. This is a separate internal mathematical audit,
not external peer review.

**Audited source:**
[`hc7_k44_adjacent_singleton_shore_split_profiles.md`](hc7_k44_adjacent_singleton_shore_split_profiles.md)

**Audited source SHA-256:**
`9234ff2c545608e7dcb3572dff3875137cbd2978a209826196dc111153d555ae`

## 1. Scope of the audit

The proof was reconstructed from the exact adjacent-singleton neighbourhood
identities, the assumed two-component exact cut
`E={a,p} dotcup T`, the audited contraction-trace,
closed-shore rooted-connectivity and seven-cut theorems, and standard
set-Menger. The audit checked every rooted path family, every reassignment of
an unused literal-core vertex, all branch-set disjointness, and every quotient
contact count. No finite computation is added by this proof.

The result is a profile theorem only. It does not eliminate either remaining
two-component split and does not prove the adjacent-singleton case, literal
T44, T44, Conjecture 21, or `HC_7`.

## 2. Unbalanced split and the common missed endpoint

When `R cap (S-T)={s}`, closed-shore rooted connectivity on `D` gives seven
disjoint `E`-rooted bags with representatives exactly `S-{s}`. After deleting
the `x`-rooted bag, the retained representatives are all four vertices of
`S_0` and the two `a,p` representatives in `S_1`. The unused vertices are `s`
and the discarded bag's representative. Assigning these to two distinct
`S_0`-rooted bags gives a `K_6` quotient minus the pure `S_0` and pure `S_1`
pairs; the edge `ap` repairs the pure `S_1` pair, so there are at least
fourteen contacts.

For a component `W` of `R-s`, seven-connectivity and
`N(W) subseteq E union {s}` imply that `W` misses at most one member of `E`.
If it misses no member or only `x`, it sees all six retained roots. If it
misses `m in S_0`, it must see `s`, and assigning `s` to the `m`-rooted bag
repairs the only missing helper contact. In each case `W` would be a universal
seventh bag, giving `14+6=20` contacts. Hence every such component misses
exactly one of `a,p`.

If two components miss different endpoints, the proof constructs a valid
`T`-rooted `K_5^-` in `D union T`. For exterior `x`, its rooted bag is an
`x`-to-`S_1` path in `D`; for core `x`, it is the singleton root. The two
remaining `D`-side `S_1` vertices enlarge two different `S_0` bags. The bags
`W_a union {p}` and `W_p union {a}` are connected, disjoint, universal to the
five rooted bags, and adjacent through `ap`. Thus the quotient has
`9+5+5+1=20` contacts. All components of `R-s` therefore miss one common
endpoint `epsilon`, and fullness of `R` forces `epsilon s`.

The proof that `R-s` is nonempty is exact: otherwise fullness of `R={s}` gives
both `as` and `ps`, contradicting `L(a) cap L(p)=emptyset`. If `R-s` had `k`
components, deleting the exact boundary `(E-{epsilon}) union {s}` of any one
leaves the `k` components plus the connected side containing `D` and
`epsilon`. The seven-cut theorem gives `k<=2`. Equality would make that
boundary a three-component seven-cut, hence subcubic, while `s` has its four
literal neighbours in `S_0` inside the boundary. Therefore `R-s` is connected.

## 3. Boundary colouring, nonedges, and the location of `b`

The connected exterior set `R-s` has tight boundary
`(E-{epsilon}) union {s}`. The audited tight-boundary theorem gives a proper
`3`-by-`4` bipartition extending the literal shores. The four vertices of
`S_0` fill the order-four class, so `eta,x,s` form the other class.
Consequently `eta s`, `eta x`, and `xs` are nonedges. Since `eta b` is an
edge, `x ne b`.

The common neighbour `b` is exterior, distinct from `s`, and lies outside `E`
because it is distinct from `a,p`, from `S_0`, and from `x`. It cannot lie in
`R`, since `epsilon b` would be a second `epsilon`-neighbour there besides
`s`. Hence `b in D`.

## 4. Rooted-support obstruction

For a forbidden connected set `B_x`, the definition guarantees that it
contains the root `x`, meets `N_D(epsilon)`, and uses exactly one vertex of the
three-set `U` when `x` is exterior, or avoids the two-set `U` when `x in S_1`.
In either case, assigning two untouched vertices of `U` to two distinct
singleton `S_0` bags gives an `x`-rooted `K_5^-` with nine contacts.

The bags `(R-s) union {eta}` and `{epsilon,s}` are connected, disjoint from
this model and from one another, and adjacent through `ap`. The first sees all
five rooted bags through `T`. The second sees the four `S_0` bags through `s`
and the `x` bag through the chosen `epsilon`-neighbour in `D`. The contact count
is at least `9+5+5+1=20`, so no forbidden `B_x` exists.

If `epsilon x` were an edge, the same model works with an exterior
`x`--`U` path trimmed at first contact, or with `{x}` when `x` is core;
`epsilon x` supplies the last helper contact. Thus `epsilon x` is a nonedge.

For exterior `x`, put `A=N_D(x)` and `B=N_D(epsilon)`. An `A`--`B` path using
one member of `U`, together with `x`, is forbidden. A path avoiding `U` can be
extended from its vertex set to the first vertex of `U`; this again yields a
forbidden connected set. Therefore every `A`--`B` path uses at least two of
the three vertices of `U`, so two vertex-disjoint such paths cannot exist.
Both neighbour sets are nonempty by fullness of `D`. Set-Menger, with
separators allowed to meet either endpoint set as stated in the theorem, gives
a separator of order at most one; connectedness excludes order zero. The
separator therefore has order exactly one.

When `x in S_1`, any path in `D-U` from `N_D(x)` to `N_D(epsilon)`, together
with `x`, is a forbidden set avoiding `U`. Hence deleting `U` separates the two
neighbour sets.

## 5. Balanced split

For a component `W` of `R-F`, all neighbours lie in `E union F`.
Seven-connectivity gives

`|N(W) cap F| >= |E-N_E(W)|=|M_W|`,

so `|M_W|<=2` and a double miss forces adjacency to both vertices of `F`.

Closed-shore rooted connectivity in `D` gives six disjoint bags rooted at
`S_0 union {a,p}`, with the `a,p` bags represented by the two `D`-side
vertices of `S_1`. Assigning the two vertices of `F` to distinct `S_0` bags
gives `K_6` minus the two pure same-shore pairs; `ap` repairs the pure `S_1`
pair, leaving fourteen contacts. If `W` saw both `a,p`, the inequality above
permits distinct seen vertices of `F` to be assigned to every missed selected
`S_0` root. Thus `W` would be universal to all six bags and give twenty
contacts. Hence every component misses `a` or `p`.

If both one-endpoint miss types occur, linking exterior `x` through `D` to one
`D`-side `S_1` vertex and assigning the other such vertex and both members of
`F` to three distinct `S_0` bags gives an actual `T`-rooted `K_5`. The helpers
`W_a union {p}` and `W_p union {a}` are connected, disjoint and adjacent
through `ap`; each has effective defect at most one. A total defect at most
one would give `10+5+5+1-1=20` contacts. Target-freeness therefore forces both
defects to equal one, which implies the exact miss sets `{a,u}`, `{p,v}` with
`u,v in T` and the nonedges `pu,av`.

## 6. Inputs and exact scope

The adjacent audited inputs used are:

| input | source SHA-256 | audit SHA-256 |
|---|---|---|
| singleton-atom reduction (for provenance of the explicit hypotheses) | `775a4f5a6cf2f455a2ca54a232146fd2f4b22a1c88e7e38770b26bfb83df8e07` | `616278d73a0c978a98f972de6efe17786132d91198bceedf8b806dbf50824d88` |
| adjacent-singleton contraction trace | `174baaa7a01d75048575760387f568bbf2ace15cef61e10a2dd5ed35372ca2ef` | `db6e39bf079b9637725c6929f0a38b6cde13a2a96f102b0f6919908e3f6bfd5f` |
| tight-boundary theorem | `384150b962a3e86848622e78cd711fac3d27b1bfcedbc22a1ce8adb2d7127b90` | `f0f5ab26c066e7641059e6aa5f5961b0a8b437afb034675c5119e242c26d2faa` |
| seven-cut component theorem | `cbd3ecb73bea0530797ad58080ae6db6052bfbf69f90af558283e3f250772ef8` | `8cd2f3adb52c8cfedd8fc3a11d47c67444dc9df62d6b5e79a78bfe914e533294` |
| closed-shore rooted connectivity | `ba6dbfe1ca9e89041b1a77174844c24598984cbe76349a55c41f15b2e997cc03` | `03738f53f8892c786dadd236c529c59b7045b3dc8371de22f0836f3721e5e43a` |

The remaining input is standard vertex-Menger. No bounded enumeration enters
this proof; any computational trust is inherited only through the audited
singleton-atom input.
