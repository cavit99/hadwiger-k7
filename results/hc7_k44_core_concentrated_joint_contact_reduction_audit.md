# Independent audit: core-concentrated joint-contact reduction

## Verdict

**GREEN** at the exact source revision

```text
b2a50744b39e4e2e77e8f6de54976074a9757a42415b9468e24d46417ed104da  results/hc7_k44_core_concentrated_joint_contact_reduction.md
```

Relative to audited revision
`b364d3adb0574a98afa8a8c975b47bca694137dc7348ac1559df433a5ad4937a`,
this revision only replaces the undefined symbol `t_h` with the already named
root `h` of `B_h` in the tree-partition argument.  An independent recheck
confirmed that the rooted bag, tree split, branch sets, inferences, and
contacts are unchanged; the GREEN verdict is unchanged.

The three conclusions are proved under the displayed hypotheses.  In
particular, the proof correctly strengthens the two separate rooted-contact
bounds to a joint three-bag bound and returns an actual full-neighbourhood
separator in every target-free core-concentrated profile.  The separator is
only lower-bounded by seven; the source does not claim equality.

The added finiteness and simplicity hypotheses are exactly those used by
the spanning-tree, degree-counting, and finite branch-set arguments.  The
set returned in Section 4 is one nonempty side of a two-part partition of
`R`, and the set returned in Section 5 is one nonempty side of a two-part
partition of `B_h`.  It is therefore proper in the ambient component or
branch set, as asserted; conclusion 3 is not witnessed trivially by all of
`R`.

## 1. Rooted model and spanning normalization

The five branch sets of a `T`-rooted `K_5` model are pairwise disjoint and
each contains its named root.  Since there are exactly five roots and five
bags, each bag contains exactly one vertex of `T`.  This justifies every
later use of the fact that an `R`-to-branch-set edge must end at that bag's
root: distinct components `D,R` of `G-E` are anticomplete.

The spanning normalization in Section 4 is valid.  The graph
`G[D union T]` is connected because `D` is connected and is adjacent to
every member of `T`.  Every component outside the current model union has
an edge to some current branch set.  Absorbing that entire component into
one contacted bag preserves connectedness, disjointness, all five roots,
and every old clique contact.  Repetition terminates with a spanning rooted
model.

## 2. Joint contact and containment counts

For the joint bound, the seven sets

```text
(B_t:t in T), R, {a,p}
```

are pairwise disjoint and connected.  The five rooted bags contribute ten
contacts, `R` contributes five contacts to them through their roots and one
contact to `{a,p}` by fullness, and `{a,p}` contributes at least four
further rooted-bag contacts.  Thus the count `10+5+1+4=20` is correct and
gives a `K_7^-` model.

For the containment implication, choosing
`h in C_a-C_p` makes `B_h union {a}` connected and leaves the five model
bags pairwise adjacent.  The singleton `{p}` contacts its three old bags
and the enlarged `h`-bag through `ap`; `R` contacts all five bags and
`{p}`.  The same twenty-contact count is therefore valid.  Interchanging
`a,p` proves the symmetric statement.  Finally, the unique common
neighbour lies outside `T`, so `N(a) cap T` and `N(p) cap T` are disjoint;
their roots occur in the corresponding contact sets, proving the boundary
sum bound.

## 3. Remote-component split

For disjoint connected `U,V subseteq R`, the bags `U union {a}` and
`V union {p}` are connected and adjacent through `ap`.  A rooted bag
`B_t` is contacted by the first new bag exactly when
`t in C_a union N_T(U)`: an edge from `U subseteq R` cannot end in the
`D`-part of `B_t`, and `t` is its only boundary root.  The symmetric
identity holds for the other bag.  Hence condition (13) gives ten clique
contacts, the one contact between the new bags, and at least nine of the
ten possible new-bag-to-rooted-bag contacts.  The count in (15) is correct.

When distinct endpoint neighbours `x,y` occur in `R`, deleting an edge of
their path in a spanning tree partitions all of `R` into nonempty connected
sets `X_a,X_p` containing the prescribed vertices.  The seven displayed
bags are disjoint.  Their guaranteed contact count is exactly `21-d` in
the stated bookkeeping; the surviving tree edge between the two parts is
an additional witness for the same pair already joined through `ap`, not
an additional pairwise contact.  Target-freeness forces `d>=2`.

Every term counted by `d` is a genuine anticompleteness between one split
part together with its endpoint and a nonempty rooted bag.  The split part
itself is therefore anticomplete to that bag.  Removing its full
neighbourhood leaves the connected split part on one open side and the
rooted bag on another, so the returned full neighbourhood is an actual
separator.  If `b in D`, fullness gives endpoint neighbours in `R` and
uniqueness of `b` makes them distinct.  If `b in R`, a distinct choice
exists unless both endpoint neighbourhoods in `R` equal `{b}`.  These
cases are exhaustive.

## 4. Branch-set split in the final common-neighbour location

Under `N(a) cap R=N(p) cap R={b}`, degree seven leaves exactly five
neighbours of `a` in `D union T`.  A spanning rooted model contains all
five, while the joint contact bound puts them in at most three bags, so
one bag contains at least two distinct neighbours.

The tree partition in Section 5 is correct.  In the minimal subtree
containing `h` and all `a`-neighbours in `B_h`, there is a leaf different
from `h` which is an `a`-neighbour.  Removing its incident minimal-subtree
edge from the full spanning tree puts that leaf alone among the specified
terminals on one side.  Thus both resulting connected parts contain an
`a`-neighbour, the other part contains `h`, and the two parts are
adjacent by the removed tree edge.

For the seven bags in (21), the first three form a triangle: the split
edge, `ap`, and an `R-h` edge supply its three contacts.  The four foreign
bags supply six contacts, `R union {p}` supplies four more to them, and the
two split parts with the attached `a` supply `8-d'`.  Therefore
`3+6+4+8-d'=21-d'` is correct.  If `d'<=1` this is a `K_7^-` model; otherwise
a deficient connected part is anticomplete to a foreign bag and its full
neighbourhood is an actual separator.  This proves conclusion 3 without
assuming an upper bound on that separator.

The common-branch-set refinement uses the same disjointness and count.
If a common bag has distinct endpoint-contact vertices, its tree split
returns the target or a separator.  Avoiding both outcomes forces both
endpoint contacts in a common bag to be the unique common neighbour `b`;
disjointness of branch sets permits at most one such bag, and none when
`b in R`.

## 5. Separator order

Seven-connectivity gives `|N_G(Y)|>=7` for every returned actual
separator.  At equality, a component of the deletion which missed one
boundary vertex would have all its neighbours among the other six
boundary vertices.  Those vertices would disconnect the graph, so every
component is boundary-full.  No converse or equality assertion is used.

## 6. Abstract eight-vertex route nonclosure

The graph in Section 7 has exactly 21 edges.  Its vertex degrees are

```text
deg(r)=7, deg(q1)=deg(q2)=deg(q3)=6,
deg(q4)=deg(q5)=5, deg(p)=4, deg(a)=3.
```

Thus deleting one vertex leaves at most 18 edges.  Every edge lies in a
triangle, so contracting any edge deletes that edge and identifies at
least one further pair of parallel edges; the resulting simple graph has
at most 19 edges.  A seven-branch model in an eight-vertex graph either
uses seven singleton bags or uses all eight vertices with exactly one
two-vertex connected bag.  These are precisely a vertex deletion and an
edge contraction.  Neither can yield the 20 edges required by `K_7^-`.

This verifies the finite example as an abstract obstruction to contact
counting only.  It does not satisfy, and is not presented as satisfying,
the ambient seven-connectivity, literal-core, or degree-seven hypotheses.

## Trust boundary and scope

This audit is a direct finite-graph and branch-set check; it invokes no
computer-assisted unbounded inference.  It confirms an unbounded separator
reduction, not closure of the adjacent-singleton case.  The exact remaining
target is to eliminate the whole core-concentrated profile.  Neither of the
two evident mechanisms is proved: an exact-seven marked-certificate theorem
producing the target or a safe contraction, or a descent/rerouting theorem
for larger boundaries with a strictly decreasing complexity.  The theorem
does not prove the literal `K_{4,4}` case, T44, Conjecture 21, or `HC_7`.
