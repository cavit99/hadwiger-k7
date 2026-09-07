# Independent audit of marked bipartite scheme completion

**Verdict: GREEN.** Separate internal mathematical audit of the complete
[source](hc7_marked_k33_scheme_completion.md), at whole-source SHA-256
`fb55cc00b52e0f3fb6f6e547f08b29ed6aae37cb25c4176a7c7fb96ada05dc2f`.
Restoring the previous opening and Section 3 scope, then removing appended
Sections 4–5, exactly recovers the audited three-path source SHA-256
`804ae8ffa01c70d37db8af27ceb0c7f0edbc8819c65d685a6fe3610a8149bec4`.
For that earlier revision, reversing only the status, input wording and
two promotion links recovered the cold-read draft SHA-256
`0d36f44a48399a1edc1611cf83db22e3a281728f4bdf2e65be356fce66dc00a7`.
This is not external peer review or proof of the full critical case.

The universal bipartite input was read at its source-pinned SHA-256
`3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`,
checked against both adjacent GREEN audits. No new literature theorem or
finite verification is used here.

## Strongest inference checks

- **Terminal models.** An unused marker or a marker in any `B` bag supplies
  a second `B`-shore edge beyond `34`. If both markers occupy one `A` bag,
  a pendant marked segment transfers to its indicated cycle-root bag; the
  retained marked tree restores the three cross-contacts and retains its
  prescribed triangle root. For the separate `K_{2,3}` plus `D` case,
  a single marker in `D` makes the two possible omissions independent.
  With both markers, the same tree transfer restores all three contacts
  from the retained `a0` tree. Every resulting bag remains connected,
  disjoint and adjacent to `v` through a retained named neighbour.
- **No hidden normalization.** The initial proper endpoint-colouring is
  a hypothesis. Projections are connected because projected incident paths
  cover their colour classes and begin at their prescribed roots. A label
  on only one path still gives a nonloop. No minimum degree or multiple
  membership is assumed, and a marker outside the path union is terminal.
- **Collisions and ownership.** In the `A` orientation, a component merging
  `a0` with a marker is disjoint from the lifted `K_{2,3}` obtained by
  excluding every `a0`-coloured quotient vertex. Allocated labels cannot
  re-enter another component's preimage. A component merging both markers
  is indivisible in any lifted model, so they are either both unused or
  in one bag. These cases terminate before any recursive root assertion.
- **Restricted rank case.** For `N_A>N_B` and `R<N_B`, deleting the two
  marked labels gives `|E'|=N_A-2>=N_B-1>=R>=R'`. If `R'<|E'|`, a
  nonempty restricted minimizer spans exactly the full projections'
  components on that set, even if the restricted projections disconnect.
  The component contraction therefore applies while both markers remain
  untouched. If `R'=|E'|`, the inequalities force `N_A=N_B+1` and
  `R'=R=N_B-1`. An allocation of all `E'` is also a full-ground maximum.
  Equality with a full minimizer forces every label outside it to be
  allocated, so both unallocated markers lie inside it. Its component
  forests span every marked traversal without using either marker.
  Deleting those two labels is thus a valid scheme reduction, and the
  lifted rooted model avoids both original markers.
- **Induction and literal edges.** Every recursive set is nonempty and
  strictly decreases the scheme-union order. All nine named vertices stay
  distinct in precisely those cases where recursion is used. The triangle,
  five-cycle and `v` edges can consequently be retained as auxiliary edges;
  none is silently required to be a projection edge. If path cleanup drops
  a marked image, the lifted model leaves its whole preimage unused and
  is terminal. Disjoint connected preimages compose all remaining lifts.

**Original three-path scope.** That critical application is conditional on all
three extra `a0`-to-cycle bichromatic connections in the same colouring.
They then form a genuine scheme with the existing six paths, since every
shared vertex has a common endpoint colour. Their existence is not proved.
The theorem chooses a model jointly with its reductions; it gives no
ownership guarantee for an arbitrary returned model. No substantive gap
was found in its stated conclusion, but Conjectures 19/21 and HC7 remain open.

## Two-path extension: separate cold check

**Verdict: GREEN.** The appended proof needs `a0–1` and either `a0–3`
or `a0–4`; it does not prove the version omitting `a0–1`.

The auxiliary hypotheses now explicitly exclude `v` from every marked
and scheme preimage and retain it as its original singleton. This was
required during the audit: allowing the auxiliary L marker to equal `v`
would admit `K_7` minus the adjacent pairs `a0–3,1–3`, which has no `Q`
minor. The actual constructions always preserved this separation.

In L, the extra `14` edge and an unused marker supply the full `B`
triangle; a root-marker collision instead supplies a connected helper
whose possible omission is independent of the core omission. In C,
the entire original two-marker preimage stays indivisible. A forward
root-marker collision is terminal by the original tree transfer; a
reverse packing is accepted only when it excludes that marked object.
Otherwise `R'<N_B<=N_A-1=|E'|` gives a nonempty minimizing set avoiding
it. No arbitrary reverse owner of the marked object is deemed terminal.

For P, the reverse restriction protects marker `2`. Label `0` occurs
only in the `1,4` projections because the target edge `a0–3` is absent.
An allocated `0` therefore merges into its same-colour prescribed root
along `01` or `04`, gaining `14` without meeting another root or `2`.
Path images remain endpoint-coloured walks and simplify validly. If `0`
was deleted, its disjoint preimage can instead join the root-`4` preimage;
the allocated component trees already bypass it. Both transitions give L.
The root-free merger of `0,2` gives precisely C, retaining both original
markers and all relevant original cycle contacts in its connected preimage.

L and C are proved independently at every order before P. Thus P's
initial off-scheme-`0` transition to L needs no strict decrease. Every
invocation of an induction hypothesis does follow a nonempty component
reduction and strictly reduces scheme order. All six prescribed roots,
the literal triangle, the required cycle contacts and singleton `v`
remain correctly owned. The previous three-connection scope is therefore
strengthened, but forcing the stated two-connection conjunction in a
critical colouring, or completing its failures, remains a global gap.
