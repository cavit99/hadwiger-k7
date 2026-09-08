# Audit of the colour-class and marked-vertex allocation obstructions

**Verdict: GREEN.** Separate internal audit, 8 September 2026; not external
peer review. The claim concerns a compulsory branch-set normal form, not
K5 contractibility or Hadwiger's conjecture.

**Exact source:** [the barrier](k5_scheme_full_colour_class_obstruction.md),
SHA256 `6da997fff17f9d1e4756bdd284f4a814c0c3734b5dfb873661d072201dbdd528`.
Removing only the final marked-vertex section exactly recovers the
previously audited source at
`b84803400210782665b3a7b61f554b5a92b0aaae83e0b76fe7619248e35c3c8b`.
Its complete mathematical draft was read at
`76d135d523b664f460ee245bdc594bf37fa7d68bc69851f7651ec8cc3b1f6aa3`;
reversing the final status-only edit recovers that hash exactly.

The ten paths have the claimed distinct root pairs, proper endpoint
colours and intersection condition. Their union has ten vertices and
22 edges. The displayed model retains every root, has connected disjoint
bags, and supplies all ten required contacts.

The analytical exclusion covers every rooted model, including unused
vertices. If a owns u, any connecting capital vertex forces the paired
lower-case root to be singleton and miss the other root's bag. If b owns
B, either owning u already forces a missing contact, or connectivity forces
C into b's bag. Then a must own D or E, and c must own u. The remaining
paired root becomes singleton and misses its partner's bag. The stated
automorphisms cover the other three root colours. These arguments use
actual neighbour sets and fixed ownership, not an edge-count heuristic.

The [verifier](k5_scheme_full_colour_class_obstruction_verify.py), SHA256
`c1d4cc5dbac17f97d1edf218d1d96e763070ebd03f81ef8833fc5239811860bf`,
was independently read and run with `uv run python3`. Assigning each of
five nonroots to one of five root bags or to unused enumerates all 7,776
possibilities. Connectivity and all ten contacts are checked directly;
the run found 21 models and no own-colour pair. The literal K5, rooted C5
and canonical two-copy calibrations passed. This is a finite cross-check;
the arbitrary-model proof above is independent of computation.

The original auditor had previously discussed the a/u ownership case, then read
the entire frozen proof independently of the enumeration. No unresolved
assumption or gap was found in the stated barrier.

## Appended marked-K4 obstruction and positive extension

A separate reviewer read the complete revised source and independently
checked the appended eight-vertex proof. Deleting 7 or 6 leaves root
0 or 1 singleton with only two possible other bags. Deleting 4 forces
6 into the 3 bag and then leaves root 1 with only two bag contacts;
deleting 5 gives the corresponding 2/7/0 argument. Thus every rooted
K4 model uses all four markers, including models originally allowed
unused vertices.

Separating the four markers would force one into each root bag.
Actual root neighbourhoods then force exactly {0,7}, {1,6}, {2,5},
{3,4}; the last two sets have no edge between them. The displayed
positive K4 model has all six contacts. The augmented ten-vertex host
is a proper K5-scheme, and its displayed model {a,7}, {0}, {1,6},
{2,5}, {3,u} has all ten contacts with fixed disjoint connected bags,
leaving 4 unused.

The appended proof is independent of enumeration. The original verifier
and its hash are unchanged, and its recorded counts concern only the
first example. The new reviewer authored the original full-colour-class
source and had discussed the proposed marked-vertex alternative; the
original source's separate audit above remains that of its original
auditor. The new independent proof review concerns the appended
construction and its exact scope. Neither construction refutes rooted
K5 extraction, and no general allocation theorem is asserted.
