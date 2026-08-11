# Internal audit of the five-centre critical-completion elimination

Audited file:
`active/hc7_k7minus_five_centre_critical_completion_nested_cut.md`

Audited SHA-256:

```text
61ca52fbb1b51fba01af195a2c0b1d3a631542f3a78e0fba166c6c042474dfbd
```

**Verdict:** **GREEN** for Lemmas 2.1, 3.1, 3.2, Theorem 4.1,
Lemma 4.2, Corollary 4.3, Lemma 7.1, Theorem 7.2, and the global
consequence (8.1).

This is a hash-pinned internal mathematical audit, not external peer review.
Relative to the theorem revision originally checked, the source changes
only its audit-status metadata; no theorem or proof text changed, so the
GREEN verdict is retained.
The revision gives an unbounded terminal elimination of both nonrainbow
critical-completion rows in the minimally infeasible five-root setting.  It
does not eliminate the surviving all-rainbow row or prove the full
five-centre two-cut theorem.

## 1. Dependencies and standing witnesses

The exact local dependency revisions checked are:

| input | source SHA-256 | audit SHA-256 |
|---|---|---|
| five-centre two-cut reduction | `1917b5e3d183d44a2d905d2628272d10e4bc6f7ae0768b43cab0e9462b83332a` | `d01183c936d79ea2e07f956c2e89f7291df9cc28a5dab3dda6b093c8a69c4ea3` |
| four-root palette transfer | `1f91f4396e090497a576fd63c1462762b5ab5f95151a06632a8f63584caee1a9` | `b366bbd22bd3b37db844db80d14c80b909a49e4ee2c3681767ac0b1c916ce668` |
| exact boundary incidence | `e8c53c8255f7e6fe62b014e6909f4d12501e7994691d99e6b749ad9b2b9a3fd6` | `bb913b8a6af2aa830567c87d6350246885743195514fb6fcc1db4af49025d3ee` |
| global five-root palette alternative | `b26f9f0d12822f93af55e3aa566fc75b985dcb5a17daa4ea2b329c8efea274c3` | `765df0db1168001a212c77e5f871abe4725d4c92cc4e11ae8d887ff808f92e6a` |

For either nonrainbow row, the feasible four-root witness lies in
`G[D union A union {p,q}]`, where `A=Z-{z}`.  The omitted centre `z` is
therefore neither on the witness path nor in a complementary component.
Full five-root infeasibility correctly implies that `z` is anticomplete to
the component `K` containing `A`: one such edge would put all five roots in
one component after deletion of the unchanged pole path.

The fixed `D`-shore colouring gives `alpha` on `Z`, distinct colours
`beta,delta` on the poles, and the remaining three-colour set `Gamma`.
Every vertex of `N_D(z)` avoids `alpha`.  In the nonrainbow case at least
one colour of `Gamma` is absent from `N_D(z)`; for three contacts this uses
the proved fact that `N_D(z)` is a clique, and for two contacts it is
immediate.

## 2. Recheck of the pole-incident row

Sections 1--6 were rechecked in full.  The earlier one-edge argument remains
GREEN.

For an admissible split, contracting `K` and the two pole subpaths gives
three pairwise adjacent connected sets.  Absorbing a `z`-adjacent off-path
component into the opposite pole subpath preserves connectivity and
disjointness.  The literal pole edge at `z` and the assumed opposite-side
contact make `z` adjacent to both pole bags.  The contraction/gluing
argument then excludes the split exactly as stated in Lemma 2.1.

Prefix minimization is valid.  Rerouting through a component or chord that
crosses the first `K`-contact preserves four-root feasibility and makes the
new retained-root component contact the new path earlier.  This proves the
noncrossing statement.  The prefix component is nonempty in both cases:
either the open prefix contains a vertex, or the lower bound on
`|N_D(z)|` supplies a confined off-path component when the prefix is one
edge.  The retained `D`-component has a later path contact, so the prefix is
a strict subset of `D`.

The proof that `A` is anticomplete to the nested component is also sound.
In the open-prefix case, an `A`-edge would put a vertex in `K` and yield an
earlier path contact.  In the one-edge case, the nested component is exactly
the selected off-path component and is anticomplete to `K`.  This contradicts
the exact neighbourhood `Z dotunion {p,w}` and proves Corollary 4.3.  No
minor-lifting or colouring-synchronization assumption is used.

## 3. Pole-freeness makes every path split admissible

In Section 7, the boundary-incidence theorem supplies at least one centre
adjacent to each pole.  Because `z` is pole-free, both such centres belong
to `A subseteq K`.  The literal edges from those roots to `p,q` make `K`
adjacent to both end vertices of `P`.  Consequently every edge of `P`
separates two subpaths each adjacent to `K`, exactly as required in
Theorem 7.2.

The contact set

```text
T=N_D(z)
```

has order two or three and is a clique.  Since `z` is anticomplete to `K`,
no member of `T` lies in `K`.

## 4. Audit of Lemma 7.1

The three cases in Lemma 7.1 are exhaustive.

If two contacts lie on `P`, their trivial paths are disjoint and have
distinct ends.  If exactly one contact `r_1` lies on `P`, clique adjacency
puts every other contact in one component `B` of the rooted graph minus
`P`, and makes `r_1` an attachment of `B`.  The component `B` is distinct
from `K`, anticomplete to `A`, and contained in `D`.  Its only possible
external neighbours are `z` and vertices of `P`.  If `r_1` were its sole
path attachment, `{z,r_1}` would separate `B` from the nonempty shore `C`.
Thus a second attachment exists, and a route through `B`, stopped at its
first path vertex, is disjoint from the trivial path.

If no contact lies on `P`, clique adjacency puts all of `T` in one
component `B` of the rooted graph minus `P`.  The set-Menger argument is
correct.  Failure of two vertex-disjoint `T`--`P` paths gives a hitting set
`X` of order at most one.  Since `|T|>=2`, the clique `T-X` is nonempty and
connected.  Its component `W` in `B-X` has no neighbour on `P-X`; it also
has no neighbour in `A`, `K`, another off-path component, or `C`.  Hence

```text
N_G(W) subseteq {z} union X,
```

an order-at-most-two separator between `W` and `C`.  Seven-connectivity
rules this out.  Vertex-disjoint set paths necessarily use distinct starts
and distinct ends, and stopping them at their first vertices of `P`
establishes (7.5).

No hidden two-linkage hypothesis is present: ordinary set Menger plus the
clique structure of `T` is sufficient.

## 5. Audit of Theorem 7.2

Order the distinct path ends as `r_1,r_2` and split `P` at an edge between
them.  Equation (7.5) and vertex-disjointness imply that

```text
K,  P_p union Q_1,  P_q union Q_2
```

are pairwise disjoint connected sets.  The split edge joins the last two;
the retained pole contacts join `K` to both.  Their contraction images
therefore form a triangle.  The distinct initial vertices `t_1,t_2` make
`z` adjacent to the two path images through literal edges.  Contracting
`K` is nontrivial because it contains the four distinct roots in `A`, so
the resulting graph is a proper minor and is six-colourable.

After naming the triangle colours `alpha,beta,delta`, adjacency to the two
path images excludes `beta,delta` at `z`.  Expanding `A,p,q` gives a proper
colouring of the closed `C`-side: `A` is independent, `z` is independent
of `A` and pole-free, and every edge from `C` to an expanded boundary
vertex was represented at the corresponding contraction image.  Thus the
only untested edges after taking `phi_D` on `D` are exactly the edges from
`z` to `D`.

If `z` has colour `alpha`, those edges are proper because `phi_D` originally
colours `z` with `alpha`.  Otherwise `z` has a colour in `Gamma`.
Nonrainbowness supplies an absent `Gamma`-colour, and a permutation of the
three `Gamma` names on the minor side fixes all boundary colours while
sending `z` to that absent colour.  The two partial colourings then glue.
Both cases contradict `chi(G)=7`, proving Theorem 7.2.

## 6. Global consequence and scope

Every centre has zero or one pole edge.  Corollary 4.3 excludes a
nonrainbow centre with one pole edge, and Theorem 7.2 excludes a nonrainbow
centre with none.  Therefore every `N_D(z)` is a three-vertex clique using
exactly the three colours in `Gamma`, which is precisely (8.1).  The prior
global-palette lemma then places all thirty pole--triangle Kempe connections
in the one fixed colouring.

No unresolved assumption or proof gap remains in the critical-completion
elimination claimed by this revision.  The all-rainbow branch remains open.
