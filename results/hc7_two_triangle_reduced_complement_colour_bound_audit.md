# Internal audit: the reduced-complement colour bound

**Verdict: GREEN.**

**Audited source:** [the reduced-complement theorem](hc7_two_triangle_reduced_complement_colour_bound.md).

**Whole-source SHA-256:**
`22e6d77e3400e929131d72b8bded414483a7d6331b864cb253a91fd8e8f26a11`.

This is a separate internal mathematical audit, not external peer review.
The reviewer supplied the connected-three-set observation controlling the
B labels near x and y and checked the proposed palette cases in discussion.
The source was written by another agent; this audit includes a separate
complete read of its exact frozen text. The parent reported an additional
whole-source review and contributed earlier palette arguments.

## Revision and dependency checks

The complete draft was checked at
`60cfd023852276f073a800060fd8afbfc8bdb68ea4eb38d718b26f3f06764930`.
Reversing only the final status and two relocation links recovers those
bytes exactly. No mathematical change occurred during promotion.

The sole direct input and its audit match their printed hashes:
`ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4` and
`26b2f5ad7226c7bb3f194cac8523f043d7ae6ca955036249f04ddc9fb6d94394`.
The edge, connected-three-set and four-clique conclusions were reread.
No fresh primary-source inspection or finite computation is a premise.

## Strongest inference checks

For any reserved vertex z, two distinct B labels in S_z are witnessed
by z and at most two of its M neighbours. This connected set has order
at most three, avoids the four-clique v+B, and contacts v through z.
Its contraction would therefore supply three distinct clique contacts.
All four clique roots remain singleton and distinct. The same edge
argument on xy limits their collective A neighbourhood to one vertex,
so at least two choices of a are eligible. The proof covers every such a.

The selected colour class avoids both surviving A roots, and hence
contains no neighbour of v. Its two-B-neighbour vertices cannot contact
a,x,y by the original four-clique restriction. Its zero-B-neighbour
vertices retain a colour whenever the three reserved vertices use at
most two B colours.

Since S_x and S_y each have size at most one, the omitted Bi exists.
In the ordinary palette case, a one-B-neighbour class vertex can lose
both available colours only if its list equals the chosen palette and
it contacts x or y. Its label would then be Bi, contradicting the
choice. The list for a always meets that palette.

Failure to colour x,y distinctly in the two-colour palette means they
both have the same literal B neighbour Bk. Then v,Bk,x,y really form
an alternative four-clique. A class vertex labelled Bk cannot meet
both x,y. If it meets a and x, its exact alternative-clique neighbours
are Bk,x, whereas its neighbour a sees v; Corollary 3 excludes this.
The a,y case is symmetric. Thus such a vertex sees at most one reserved
vertex. Every differently labelled class vertex misses x,y by the
already proved S_x,S_y restriction. All list cases are exhausted.

Finally the recolouring gives six colours on G-v, with B,a,x,y in one
three-colour palette and the remaining M classes in the disjoint palette.
One of the latter colours is absent from the two surviving A roots and
therefore from all of N(v). Assigning it to v is valid. No maximal helper
bag or colouring of a contracted model is used.

## Scope

The theorem proves the chromatic lower bound before any reserved-core
normalisation. It uses chi(G)>=7, not proper-minor colourability, and
does not supply a rooted K5 model, preserved deletion connectivity, or
a Q construction. No gap was found in the stated deduction; the global
two-triangle allocation remains unresolved.
