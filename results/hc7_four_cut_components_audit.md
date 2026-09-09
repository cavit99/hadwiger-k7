# Audit of the four-cut component theorem

**Verdict: GREEN.** Separate cold whole-source internal audit of
[the theorem](hc7_four_cut_components.md), reviewed on 9 September 2026 at
SHA-256 `2986fb1f55c2cbaa4572b7c88e287ed5aa4230f34ab3b63dabe4d840e247e03f`.
No unresolved gap was found in its three conclusions. This is internal
review, not external peer review or completion of C19 or HC7.

## Exact inputs and provenance

The complete draft was reviewed at SHA-256
`93eb01e57c8b00121c0d7d05907724197ecce3925df47bca1941470572cb2c82`.
Promotion changed only the source status and four relative input links;
reversing those substitutions exactly recovers the reviewed draft bytes.
The mathematical text is unchanged.

Literature-repair supplied an earlier independent-cut colouring proof;
route-assessment independently supplied the current colour-collision and
reverse-contraction simplification and authored the consolidated source.
This reviewer did not develop these proofs and read the complete frozen
source and both invoked statements with their audits. All four input
hashes match:

- [Complement four-connectivity](hc7_two_triangle_complement_four_connectivity.md):
  `0a75273d2270d5a675e3aa565610d47e375fa89e982b565fbd0ad4f4e5fd3b69`;
  [audit](hc7_two_triangle_complement_four_connectivity_audit.md):
  `d074cc7eb384222f1b68ed53728fd721c7a6e7edbf266c55cec313a5c73b2014`.
- [Five-root degree-six theorem](hc7_five_root_degree_six.md):
  `289c5ad015b6c392ea69e8e26e15eba54b4eba7cb155789edd76b3dbb5c9f9a4`;
  [audit](hc7_five_root_degree_six_audit.md):
  `6f13ffd37126c78a697b5752574fe06b6fd13b68dabb0d63e4e39d76a8f1d065`.

Their recorded literature inspections are inherited; no fresh primary
inspection, finite computation or additional reviewer verdict is claimed.

## Strongest inference checks

**The packet is an actual side model.** Every cut component is full to S
by four-connectivity and contacts at least three R vertices by
seven-connectivity. If C misses r, every C vertex loses at most the two
discarded S vertices in the displayed induced side. For every nonempty
X contained in C, r survives outside its neighbourhood, so its original
boundary has at least seven vertices and the retained boundary at least
five. The degree-six packet therefore applies with all five distinct
roots retained and all other components, r and two S vertices unused.

**Three or more components are exhausted.** At least one component meets
N_F(v), because it has five vertices while S has four; at most two do,
because the surviving A vertices and the surviving x,y each form a
connected group. With two v-free components, the second component plus
s3 and a v-touching component plus v are disjoint adjacent full bags over
one packet. With exactly one v-free component, both remaining components
meet v. The intersection of two subsets of size at least two in B chooses
an admissible packet endpoint contacted by the unexpanded component.
Its possible missing B contact consequently has a different B end from
the packet's hole. No models from different endpoint choices are combined.

**The colourings agree on their entire common boundary.** Contracting
D union S is valid since D is full to S. Expanding only S, an independent
set, gives a proper colouring on the untouched C side. Two responses
whose S colour is outside the four distinct R colours align by a palette
permutation. Otherwise equality with r proves r is anticomplete to D
union S. Its at least five F-neighbours supply an actual neighbour in C.
Thus C union S union {r} is connected, and the reverse proper-minor
colouring expands the independent set S union {r} on the untouched D
side. The two responses have exactly the same boundary partition. Aligning
the four R colours aligns S as well; every edge lies in a closed side.
No colouring is expanded through its consumed component.

**The missed-root conclusion preserves both possible holes.** Five
F-neighbours of r ensure a contacted component distinct from C, since S
has only four vertices. That component contacts the two chosen S roots
and at least two of R-{r}. Choose the admissible endpoint in this latter
set. The singleton r is full to the packet and adjacent to the component;
any two absent contacts have disjoint ends, giving Q.

Parts (1) and (3) need only the structural hypotheses; part (2) also uses
seven-chromaticity and proper-minor six-colourability. Extra neighbourhood
edges are allowed throughout. The binary cases with non-independent S
remain open, as do an iterable reduction, C19, HC7 and the full objective.
