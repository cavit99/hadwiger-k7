# Second audit of the five-root wheel extension

**Verdict: GREEN.** This is a separate whole-source internal proof review of
[the theorem and both colouring corollaries](hc7_rooted_wheel_extension.md),
reviewed on 9 September 2026 at SHA-256
`f72e0b3d4254724a58f55b9445c0c173ea6c96e535416da47b1efc7fd5eb43b3`.
No unresolved mathematical gap was found at this revision.

## Scope and provenance

The reviewer, route-assessment, participated in the preceding contraction
and root-incident-edge discussions and checked several proposed reductions.
The parent assembled the source; universal-proof developed the one-root-side
argument and separately reviewed the complete text. This audit is a fresh
complete reading of the written proof, not a claim of independent discovery
or external peer review. No finite enumeration is a proof premise.

The initial draft was read at
`93f80a565d6307608f31a632032cf2364c91b513a52d21da9fda13e9e7c01356`.
The final revision includes genuine proof clarifications and ownership
corrections, not merely a status change. In particular, it explicitly
excludes used nonterminal neighbours in the essentiality argument; handles
the selected separator root in either the same or a different bag; restricts
the mandatory-path edge to internal vertices; permits the omitted terminal
to be the path endpoint w; and replaces the overlapping proposed bag A+r
by (A-X)+r in the root switch. Universal-proof identified the two ownership
omissions during its separate read. All these corrections were checked in
the final file. The verdict above applies to the final revision.

## Strongest proof checks

1. **Induction class and lift.** Minimum order is taken over all
   three-connected five-terminal counterexamples having a K4 rooted at
   *some* four terminals. The omitted terminal may lie in a bag. Every
   reduction retains all five labels, strictly lowers the host order and
   preserves such a K4. Changing the selected four roots is therefore
   legitimate. Expanding the fixed connected contraction preimages lifts
   every resulting wheel with disjoint bags and all contacts intact.

2. **Elementary contractions and Wu.** The clique-neighbour argument
   excludes every possible cut of order at most two in the quotient.
   Boundary contraction uses a genuine three-cut; a deleted merged vertex
   is handled by the actual edge uv. The terminal kernel has at most one
   nonterminal. Its non-cycle alternative has a two-cut, so a literal
   terminal triangle is terminal. The essentiality proof correctly leaves
   at most two possible Wu neighbours after excluding nonterminals,
   contradicting the required four.

3. **Root-free component.** All outside bag pieces reconnect through their
   owned boundary vertices. The exceptional case includes w in A as well
   as w in a different bag. Essentiality makes each nonterminal mandatory
   on every w-to-U path. Its remaining w-component would otherwise have
   actual boundary within {p,w}. In the final two-vertex component, every
   p-edge has an explicit legal internal allocation, including the separate
   pw allocation. The second noncontractible edge at each possible u/v
   neighbour then prevents the claimed Wu neighbourhood.

4. **Other-root component.** The crucial bound is on the actual boundary
   of X union Y, within {w,z}, rather than on a model quotient. It forces
   all surviving selected roots into Y. The omitted terminal cannot be a
   deleted singleton obstruction, and its position when two consecutive
   nonterminals occur is checked against all three original boundary ports.
   The one-vertex and two-vertex path cases are exhaustive. In the final
   incomparable case, (A-X)+r and (B-X)+{t,p} are disjoint, connected,
   retain their outside clique contacts and meet through rt. One of the
   two proposed contraction edges is necessarily terminal-safe.

5. **Root-incident closure.** A cut containing the selected root leaves
   only root-free or other-root small components; no unproved component
   containing two selected roots is invoked. Every two-terminal component
   has a legal contraction in the listed port cases. The singleton cases
   first exclude a K4 witness avoiding the omitted terminal. In the
   remaining double-terminal bag, two outside nonsingleton bags would
   leave a missing clique contact. With one such bag, switching the
   selected root makes the final internal edge admit no singleton or
   two-terminal obstruction. The two neighbours a,p cannot both be removed
   by the one remaining cut vertex. This supplies the final contradiction.

## External inputs and colouring consequences

The reviewer independently checked the exact contractible-edge statement
in [Wu's publisher abstract](https://doi.org/10.1017/S0963548302005497),
including simplicity, three-connectivity and order at least five. Only
that published theorem is imported; its proof was not re-audited here.
The reviewer also checked [Martinsson–Steiner, Theorem 1.3 and the preceding
definition of set-rooting](https://arxiv.org/html/2209.00594v1).
It supplies one vertex of the colourful set in each K4 bag, with no fixed
representatives or connectivity assumption on the four-chromatic host.

Deleting the entire independent colour class I gives exactly four colours
and universal colourfulness on the same graph H-I. The four resulting
representatives and a member of C intersect I are distinct terminals in H.
For the last corollary, five-connectivity of G gives three-connectivity
after deleting x,y. The moved vertices in a class missing the common
neighbourhood are independent and all miss y, so the stated recolouring
really would use six colours. Finally, the five wheel bags and singleton
x,y have exactly the required K2 join W4 contacts.

The proof closes the stated double-critical branch. It does not settle
the six-chromatic deletion branch, Conjecture 19, Conjecture 21 or HC7.
No priority or comparison with Norin–Totschnig is established by this audit.
