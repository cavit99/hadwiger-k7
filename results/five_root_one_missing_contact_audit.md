# Independent audit: two helpers with one missing contact

**Verdict:** GREEN for the stated five-rooted helper theorem, using the
expressly cited and separately audited minimal-counterexample reductions.
This is an internal proof audit, not external peer review. It establishes
neither Conjecture 21 nor HC7, and makes no claim that this rooted theorem
meets the user's requested comparison in significance with Norin–Totschnig.

**Audited source:** [two helpers with at most one missing contact](five_root_one_missing_contact.md),
SHA256 `078ba860d4cdde187cdc6e618a4e1842dd623523dbefbe3ead06544c7d8afa18`.
The independently audited development draft had SHA256
`44cbb5f1e37a99d2b8ea520a447077f814d0db62d54306f4948ff16e0074f946`.
The promoted source was reread in full; its mathematical argument is
unchanged. Promotion changed the title, status and audit link, relative
dependency links, and the external PDF link's explicit version.

## Dependencies and exact scope

The proof's two direct written inputs were checked at these source hashes:

- [Degree and connectivity restrictions](hc7_c21_rooted_density_low_degree_reduction.md):
  `431bd7d7d2b5bcb59e385781234c6d7ed6824f62ee50eb8ddf49e69da792cef2`.
- [Degree-five elimination](hc7_c21_helper_degree_six.md):
  `85927a0f7d1af6229930fd67f7144eac35b934c54ad504539a34d39e209020ee`.

Its transitive [rooted dart input](rooted_dart_nonroot_degree_five.md) has
SHA256 `37dcf256f64fca7c49a1bd4ec66021371fba9a7863bf9523597ba4b898ecfad2`.
The corresponding adjacent audits cover their induction, rooted lifts,
internal connectivity and degree restrictions. The helper theorem is not
assumed in those reductions: its hypothetical lexicographically minimum
counterexample is restricted until the present proof contradicts it.

The external atom theorem was inspected both in the
[primary HTML](https://arxiv.org/html/1610.09093v1#S2) and in the rendered
[primary PDF, printed page 5](https://arxiv.org/pdf/1610.09093v1).
Theorem 5 requires a member `S` of the chosen family contained in
`T-barA`, together with `T intersect A` nonempty. The overbar is essential.
It assumes neither global contraction-criticality nor an edge family
coming from a spanning tree. Its fragment and atom definitions match
the definitions in the audited proof.

## Strongest inference: the padded atom

The auxiliary graph has ordinary connectivity exactly five: internal
five-connectivity of the original rooted graph excludes smaller cuts,
and the original root set separates the new clique from the nonempty
original nonroot set. Thus its five-separators are minimum separators
in the precise sense required by the atom theorem.

Every low-triangle edge has an original proper blocker by the audited
contraction-obstruction input. Padding changes neither its neighbourhood
nor incident edges, so it remains an eligible fragment. A minimum atom
therefore has order at most the number of original nonroots. If it met
the root/padding clique, it would contain that clique minus at most five
vertices, contradicting this order bound. The atom lies entirely among
the original nonroots.

Its original closed side is proper: otherwise its five-neighbour
boundary would equal the five roots and could not contain the endpoints
of any member of the edge family. Its density is consequently at most
one. Nonroot minimum degree six excludes atom orders one and two. The
exact incident-edge count then yields an atom vertex of weighted degree
at most eight, and hence a low-triangle incident edge. Both endpoints
lie in the atom or its boundary, while the blocker cut contains both
and meets the atom. These are exactly the two hypotheses of Theorem 5.
Its order bound gives at most two atom vertices, the contradiction.

The atom minimizes over all eligible fragments. The argument does not
assume that intersections preserve positive density, or that all
eligible fragments are the previously chosen blockers.

## Remaining constructions and counts

- The low-triangle family is nonempty. Minimum degree six and at most
  three root neighbours imply at least four nonroots; their average
  weighted degree is `8+4/m<=9`.
- If every edge at a vertex of weight at most nine has at least four
  completed-root triangles, its actual neighbourhood meets every
  hypothesis of the rooted-star lemma. Five disjoint paths are taken
  in the original graph, truncated at their first neighbourhood entry.
  All original roots in that neighbourhood have trivial paths.
- The star centre is a nonroot, and its bag avoids all five linkage
  endpoints except that centre. Removing the centre from its linkage
  path leaves a nonempty prescribed-root bag. The star bag has five
  root contacts, the singleton helper has four, and they are adjacent.
  All seven bags are disjoint and use only original edges.
- For an edge with one root end, the completed triangle count includes
  the other root neighbours of its nonroot end. The stated quotient
  density identity therefore correctly removes the newly root–root
  edges. No original roots are identified, and the fixed connected
  preimage belongs to only the appropriate prescribed-root bag.

No model is constructed in the padded graph and then lifted. Padding is
used solely to select an ordinary atom; it is not asserted to retain
rooted density, colourability, or criticality. No finite search or census
is used. No unresolved gap was found in this proof with the pinned
dependencies above; global composition and comparative significance
remain separate obligations.
