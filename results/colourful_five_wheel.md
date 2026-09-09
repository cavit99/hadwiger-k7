# Colourful sets: a three-connected minor and a rooted wheel

**Status:** written deductions, with a [separate internal audit](colourful_five_wheel_audit.md).
The separator reduction below is a uniform formulation of
Martinsson–Steiner, [Claims 3.8–3.10](https://arxiv.org/html/2209.00594v1#S3),
whose proof treats four colours. We adapt their argument to k>=4 and
state the marked-minor conclusion explicitly. No new separator method,
priority for the wheel corollary or NT-level significance is claimed.

All graphs are finite and simple. A set C is *colourful in every
k-colouring* if it meets every colour class of every proper k-colouring.
A C-rooted model has pairwise disjoint connected bags, each containing a
member of C; its representatives are not prescribed.

## A three-connected marked minor

**Theorem.** Let k>=4. Every k-colourable pair (F,C) with C colourful in
every k-colouring has a three-connected minor F' and a set C' colourful
in every k-colouring of F', with chi(F')=k. Each member of C' has a fixed
connected contraction preimage containing an original member of C.
Consequently every C'-rooted minor model lifts to a C-rooted model in F.

Use colours {0,...,k-1}, calling 0 special and the others old. A
*permitted colouring* is a proper k-colouring giving every member of C
an old colour. The hypothesis is precisely that F is k-colourable but
has no permitted colouring. Such a pair has chi(F)=k, since a
(k-1)-colouring would be permitted.

Induct on |V(F)|. If F is three-connected, retain F and C. Otherwise
we construct a smaller pair in the same class. A marked minor has fixed
disjoint connected preimages, with an original mark in each marked
preimage. These preimages compose through successive reductions and
lift every returned model. Each reduction below separately retains
ordinary k-colourability and absence of a permitted colouring.

### Marked lifts through a two-cut

Let (A,B) be a separation of a two-connected F, with A intersect B={u,v}
and both interiors nonempty. Write A,B also for their induced graphs.
Every component of F-{u,v} meets both ports, so B is connected.
A+uv is a minor through a u-v path in B; A/(u=v) is a minor through
contraction of all of B. These operations leave A-{u,v} unchanged.

If B-{u,v} contains a mark c, a u-c path in B-v and the singleton v
are disjoint connected seeds. Extend them to a connected partition of B
and contract its two parts to u,v. The parts are adjacent, so this
simultaneously realises the virtual edge uv and a new mark at u. The
symmetric construction marks v. An unwanted added edge may be deleted.

If the interior of B contains at least two marks, two disjoint paths
join u,v to distinct interior marks. Otherwise vertex Menger gives a
one-vertex separator p between the two ports and those marks in B. A
mark surviving deletion of p then has no path to a surviving port,
contradicting connectedness of F-p. Extend these paths to a connected
partition of B to realise A+uv with both ports marked. Contracting all
of B instead gives a marked merged port whenever B contains a mark.
All these preimages avoid the retained interior of A.

### Cuts of order at most one

If F is disconnected, some component has no permitted colouring;
otherwise its components' permitted colourings combine. Retain that
component and apply induction.

For a cutvertex w, take proper sides A,B meeting in w. If one side
contains no mark, every permitted colouring of the other extends over
it by permuting an ordinary k-colouring to agree at w. Thus the marked
side has no permitted colouring, and we retain it.

Otherwise mark w in both sides. Each side is still k-colourable and
lifts as a marked minor through a path to a mark in the other side.
If both permit colourings, w is old in each, and permuting the old
colours lets them agree at w. They then give a permitted colouring of F.
Hence one marked side has no permitted colouring; apply induction there.

### Cuts of order two

We may now assume F is two-connected. Choose a two-cut {u,v}, proper
sides A,B, and fix an ordinary k-colouring f of F.

**At least two internal marks on each side.** If f(u) differs from f(v),
add uv in each side and mark both ports. If they are equal, identify
u,v in each side and mark the merged vertex. Both resulting graphs
are k-colourable by f, and both are marked minors by the preceding lifts.
If both have permitted colourings, their ports are old and have the
same equality relation. Permuting old colours therefore glues them to
a permitted colouring of F. At least one smaller marked pair has no
permitted colouring; apply induction to it.

**At most one internal mark on one side.** Orient the separation so
B-{u,v} has no mark or has a sole mark c. Retain all marks in A.

If f(u)=f(v), identify the ports in A and additionally mark the merged
vertex if c exists. The restriction of f k-colours this graph. A
permitted colouring there would extend over B by permuting f: match
its equal port colour, and, if c exists, also make c old. This is
possible because the merged port is old when c exists and there is
another old colour available. Thus this smaller marked pair has no
permitted colouring. Contract B to realise its marked lift.

If f(u) differs from f(v), add uv in A. If c exists and shares f(u),
add a mark at u; if it shares f(v), mark v; otherwise add no mark.
The resulting graph is k-colourable by f. In a permitted colouring,
match the two port colours by a permutation of f on B. If c shares a
port colour, its chosen marked port ensures that c becomes old. If it
shares neither, send its colour to an unused old colour: k>=4 leaves
one after at most two old port colours. With no c there is no extra
condition. Original marks at the ports already belong to A and are old.
This would give a permitted colouring of F, a contradiction. The virtual
edge and any new mark have the simultaneous lift proved above, so
induction applies.

Every replacement strictly lowers the number of vertices. The final
pair remains k-colourable with no permitted colouring, so has chromatic
number k. Since k>=4, it has at least four vertices; absence of cuts of
order at most two therefore makes it three-connected. Composing the
fixed marked preimages proves the theorem. QED

## Five colours: a rooted wheel

**Corollary.** If F is five-chromatic and C is colourful in every
five-colouring, F has a W4 minor with five distinct bags each meeting C.
The hub and rim order are not prescribed.

**Proof.** Apply the theorem with k=5, then the
[colourful-set corollary, Section 7](hc7_rooted_wheel_extension.md#7-colourful-sets-and-the-double-critical-branch),
source SHA-256 `f72e0b3d4254724a58f55b9445c0c173ea6c96e535416da47b1efc7fd5eb43b3`,
with [two internal audits](hc7_rooted_wheel_extension_audit.md).
That corollary deletes one whole colour class, applies Martinsson–Steiner,
Theorem 1.3, to the remaining four colours, and uses the five-root wheel
extension in the three-connected graph. Lift its model through the
fixed marked preimages. QED

## Six colours: reserve any whole class

**Corollary.** Let F be six-chromatic and C colourful in every six-colouring.
For every whole class I of any six-colouring, F-I has a wheel whose five
bags each meet C-I. There is a member of C in I, outside all five bags.

**Proof.** The inherited colouring gives chi(F-I)<=5. Four colours there
and a fifth on I would colour F, so chi(F-I)=5. Every five-colouring of
F-I makes C-I colourful: otherwise restoring I in a sixth colour would
leave a colour missing from C. Apply the preceding corollary. Colourfulness in the
original six-colouring gives C intersect I nonempty. QED

In a minor-minimal seven-chromatic graph G, F=G-v is six-chromatic and
C=N_G(v) is colourful in every six-colouring, since a missing colour
would extend to v. Thus this corollary reserves any chosen whole class
while extracting five distinct neighbour-containing bags. It does not
make the reserved neighbour adjacent to those bags.

A wheel extracted from a colourful six-set may also contain the sixth
mark in one of its bags. Only marks in the deleted class I are guaranteed
unused. Neither a sixth compatible bag nor Conjecture 19 is proved here.
