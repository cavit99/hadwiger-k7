# Internal audit: induced-path owner-circuit compression

**Verdict:** GREEN.  This is a separate internal mathematical audit, not
external peer review.

## 1. Exact revision and scope

The audited source is
[`hc7_k7minus_p3_owner_circuit_compression.md`](hc7_k7minus_p3_owner_circuit_compression.md),
with SHA-256

```text
0d1b0a8246ee87487de82e2350bedb13eb3a643c8aa4fee046c98bb180b7c41c
```

The audit covers the spanning-model transfers, the Rado--Menger owner
circuit, elimination of the five-owner/order-nine case, the exact boundary
counts and inheritance of the original path-operation colourings.  It does
not audit a terminal proof of the `K_7^-` six-colour conjecture, which the
source does not claim.

## 2. Minimum spanning path bag

For a component `A` of `R-V(P)`, connectedness of `R` gives an `A`--`P`
edge, so `R_0=R-A` is connected.  If `A` has no owner, seven-connectivity
and spanningness force an `A`--`D_i` edge: otherwise its whole neighbourhood
would lie in the three-vertex path.  Moving `A` into such a met bag preserves
connectivity of that bag, and every root contact has a representative in
`R_0`.  If `A` has the sole owner `i`, moving it into `D_i` is connected,
an `A`--`R_0` edge restores the root--`D_i` adjacency, and every nonowner
again has a surviving root contact.  Both moves strictly shrink `R` while
retaining a spanning co-bagged model.

Every `T_i=N(D_i)\cap R` is nonempty because the original six branch sets
are pairwise adjacent.  Hence distinct components cannot both own one label.
Every component owns at least two of five labels, so there are at most two
components.  This argument is not invalidated by the earlier spanning
minimal-deficient-tree barrier: its zero-owner filler has no foreign
contact and adhesion one, while seven-connectivity here forces the foreign
contact used by the transfer.

## 3. Labelled linkage and owner circuit

A family of vertex-disjoint labelled paths, including trivial paths,
extends to a partition of connected `A` into connected parts rooted at those
paths.  Each part attaches to its owner `D_i` through `A_i` and to `R_0`
through its distinct `B` end.  Nonowner contacts survive in `R_0`, so
absorbing all parts gives a valid smaller spanning model.  Therefore the
full linkage cannot exist.

The strict gammoid in `A` rooted at `B` correctly handles overlapping
target sets and trivial paths.  For a minimal deficient label family `I`,
linkability of `I-\{i\}` gives

\[
 |I|-1\le r(A_{I-\{i\}})\le r(A_I)<|I|,
\]

so `r(A_I)=|I|-1`.  Endpoint-inclusive vertex Menger supplies the stated
separator `S`.  Singleton target families are linkable because `A` is
connected and both source and target sets are nonempty, giving `|I|\ge2`.

If `|I|=5`, every foreign root-contact set lies in `A`, so `R_0` has no
edge to the connected union `D_1\cup\cdots\cup D_5`.  Every path from
`R_0` to that union contains an in-`A` segment from `B` to `A_I`, and hence
meets the four-set `S`.  This separates two nonempty sets, contradicting
seven-connectivity.  Thus `|I|\le4`.

## 4. Boundary conclusions

If all target portals lie in `S`, pigeonhole places two differently labelled
portal sets at one literal vertex.  Otherwise the selected component `C`
of `A-S` contains no `B` vertex, is anticomplete to `R_0`, and satisfies
`N(C)\cap R\subseteq S`.  Spanningness leaves only the five foreign bags.
Without a repeated boundary contact in one bag,

\[
                 7\le |N(C)|\le |S|+5=|I|+4\le8.
\]

The lower bound is a proper application of seven-connectivity because
`R_0` remains outside `C\cup N(C)`.  Equality gives exactly the claimed
`2+5` order-seven and `3+5` order-eight forms.  With two appendages, their
disjoint owner sets each have order at most three, so every nonrepeated
bounded output is exactly order seven.

## 5. Response inheritance

The path `P` lies in `R_0`, while `C` is anticomplete to `R_0`.  Therefore
no path vertex belongs to `C\cup N(C)`.  The three original nonempty path
signatures restrict properly to the closed `C`-shore and are rejected by
the opposite intact shore through colour-name alignment and gluing.

Every crossing edge `g` is vertex-disjoint from the induced path, so the
three edges form a componentwise-induced `P_3\dot\cup K_2`.  Contracting
any nonempty subset gives the seven exact signatures.  The `g`-only
colouring is proper after `C` is deleted; the path-only colourings are
proper on `C\cup N(C)`.  The two response orientations and all rejection
claims are therefore valid without changing either the original model or
the original path colourings.

## 6. Duplication, dependencies and trust boundary

The older model-anchored owner-circuit theorem permits unused vertices and
six foreign labels; its bound of nine plus unused-neighbour contributions
does not duplicate the present spanning `K_6`, five-label elimination.  All
links in the source resolve.  The cited exact-seven restart, three-piece
composition, full order-eight closure, operation-coupled order-eight theorem
and two barrier notes have adjacent GREEN audits.

The proof eliminates only the nonrepeated order-nine owner-circuit branch.
A shared labelled contact, repeated foreign-bag contact, the literal
`R=V(P)` deficiency, and the later exact-seven/eight alternatives remain
genuine residues.  The scope section records them accurately and makes no
unsupported static-ownership or branch-set/colouring identification.
