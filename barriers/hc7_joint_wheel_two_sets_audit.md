# Independent audit: the two-set wheel barrier

**Audited source:** [hc7_joint_wheel_two_sets.md](hc7_joint_wheel_two_sets.md),
SHA-256 `c6f017fac7dc200bd0718e2fed656ce60e9cdb4d1a0e81fc871db43db68027a7`.
**Reviewer:** separate internal audit by `exterior_joint_model`, 12 September 2026.
**Verdict: GREEN.** The family refutes the stated two-set wheel assertion
for every integer `m>=14`, including arbitrary minor models.

The listed annular faces are consistent with every prescribed edge and
give a planar embedding with outer facial cycle A. The degrees are exactly
as stated: five on A, even B, and C; six on odd B; and `2m` at h.
All neighbours used in the deletion argument are distinct for `m>=14`.
If h survives, C joins h; either every surviving B retains a C neighbour
or at most one B is deleted and its surviving cycle or path joins C.
Each surviving A retains a B neighbour unless all three deletions are in B,
when the intact A cycle joins surviving B. If h is deleted, the two remaining
deletions give exactly the two C cases stated. Thus P is four-connected.
Adding the apex gives five-connectivity and minimum degree six; Euler
excludes planarity. The two seven-element sets are distinct contiguous arcs
also when `m=14`, where together they exhaust the outer cycle.

The two exterior fans and their joining edge admit a planar drawing.
A cycle in the contact graph of arbitrary disjoint connected paired bags
can be divided into three nonempty consecutive groups. Their connected
unions remain disjoint and paired, and are pairwise adjacent. With the two
fan centres they form a K5 minor, contradicting planarity. Extra vertices,
extra contacts, and arbitrary choices of S and T contacts cause no problem.
Deleting the sole possible apex-owning bag from a wheel model leaves a
cycle: a C4 for a hub bag or a triangle for a rim bag. Its other bags lie
in P. This covers an apex bag of any size, as well as models avoiding it.

The same ownership argument verifies Q7 exclusion: removing its apex bag
would leave a six-vertex minor with thirteen or fourteen edges in P.
Direct counting gives `|P|=5m+1`, `e(P)=14m`, `|M|=5m+2`, and `e(M)=19m+1`;
the stated `m=14` values and exactly `4m` degree-six vertices follow.
No finite search is used. The stronger residual degree condition fails,
and deleting z is planar. This is not a barrier to the actual retained
critical-host hypotheses and does not resolve C19 or HC7.
