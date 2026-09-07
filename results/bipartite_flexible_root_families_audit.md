# Independent audit of flexible bipartite endpoints

**Verdict: GREEN.**

**Date:** 7 September 2026. This is a separate internal mathematical audit,
not external peer review or a significance assessment.

The exact source reviewed is
[the complete proof](bipartite_flexible_root_families.md), SHA-256
`5435c44801978073092cfaef1b685e8b5b52723a52ea28a87e3089d44127ec44`.
Promotion changed only the source status paragraph from the independently
reviewed active draft at SHA-256
`a6f03b752648c8bef5b15a6c2994bc40401dd106e357608905f5ef0423389a69`;
reversing that edit reproduces the reviewed source exactly.
The pinned matroid-union input was checked against disk at SHA-256
`3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`.
No finite computation or new literature assertion is a premise.

## Exact conclusion and the main reduction

Theorem 1 permits a nonempty prescribed root set at every vertex of a
finite simple bipartite target, on both shores. It returns one disjoint
connected bag for **each individual root**. A required target edge needs
one contact between its two root families; the contacting members may
change. It does not return one connected bag containing an entire family,
and it does not preserve every initially selected endpoint pair.

The strongest inference is the reduction through a component containing
the auxiliary identified root. A spanning independent forest there lifts
to exactly one actual tree per prescribed root: a root-to-root path would
become a cycle after identification, and the edge count excludes an
additional root-free component. All other auxiliary components lift to
single actual trees. Their label sets are disjoint across colours, so the
lifted connected pieces are disjoint and contain at most one root each.

An arbitrary traversal between two lifted root pieces could not be lifted
through the virtual identification. The proof avoids precisely that
inference. Read a demand from its opposite-shore root, and stop at its
first actual piece containing a root of the required destination colour.
Every earlier projected traversal through a deleted label lies in a
root-free auxiliary component, whose endpoints have one genuine connected
preimage. An edge crossing two destination-root pieces is never needed:
its first endpoint already terminates the path. This remains valid when
the old label belongs to another colour's allocated tree; that foreign
label is not reused. Flexible endpoint choice is essential here.

The quotient keeps all roots separate. Its selected paths have the same
two endpoint colours and no other root internally. Proper colouring is
required only on the selected path union; arbitrary auxiliary host edges
are retained without an invalid monochromatic contraction. In particular,
the literal decorated root edges survive as contacts throughout.

## Rank, termination and lift

Simplicity of the target and one path per target edge give at most one
edge for a label in each projection. Each ground label is a nonloop in
some modified projection: its two path neighbours are distinct and cannot
both be prescribed roots. The modified full rank is the number of
nonroots on the projected shore, including unused roots as isolated
vertices before their auxiliary identification.

Choosing the smaller nonroot shore makes a deficient union rank strictly
less than the ground-set size. Thus a minimizing set is nonempty, and
equality in the union formula supplies simultaneous spanning forests on
all its components. A nonempty such set contains a nonloop, so at least
one allocated edge has a connected three-vertex preimage and an actual
contraction occurs. The number of vertices in the selected union plus
all prescribed roots strictly decreases. Subsequent cleanup cannot
increase it. A smaller instance satisfies the same hypotheses, and
composing its disjoint connected preimages preserves every root and each
required contact. There is no circular induction or unsupported virtual
minor operation.

## Cycle terminal and critical application

Theorem 2 uses all eight distinct root bags. Each triangle-root bag has a
contact to root 4 and to a member of each repeated cycle-colour pair.
Choosing one such contact gives exactly the four stated types. The three
cuts of the rooted path `0-1-2-3` exhaust the needed alternatives: if the
middle split fails, at least two bags have type L or at least two have
type R, and the corresponding end split has at most one missing contact.
In a valid middle split the two possible missing contacts have different
triangle ends and different cycle ends. The three cycle unions are
connected, form a triangle and retain neighbours of the separate vertex
`v`. Hence the seven bags give exactly the asserted `Q` minor.

In the critical application, each triangle root has a neighbourhood
colour used there nowhere else. If its bichromatic component misses the
relevant cycle-colour family, swapping that component eliminates its old
colour from `N(v)` and allows `v` to be coloured. The first-root path
choice is root-clean, and all nine paths use one original proper
colouring. No old model is asserted to survive a later recolouring.

The full proof was independently read before this audit was written. A
standalone definition of `Q` was added after the first complete-file
review; no mathematical correction was needed. No unresolved gap was
found in the two stated theorems. Forcing the excluded three-colour-cycle
state from the canonical two-pair state remains unproved. This audit does
not certify Conjecture 19, Conjecture 21, `HC_7`, or the user's alternative
significance criterion. Research-index integration and checks are recorded separately.
