# Three-arm screen for the order-nine protected-centre residue

This is a hostile finite diagnostic, not a theorem about the critical host.
It starts with the exact all-terminal order-nine compositions which survive
every faithful one-suffix transfer.  Their counts are

```text
C5 disjoint union K2       256
C5 with a pendant P2      1022
C7                         256
```

## Explicit arm model

For one protected centre `w`, let `x` be its swallowed matching mate.  The
screen chooses three distinct `Q` roots `q_0,q_1,q_2` and expands the
`w`-rooted branch bag by three vertices `a_0,a_1,a_2`.  It retains the
original edge `wx` and puts in the literal paths

```text
x-a_i-q_i,  i=0,1,2.
```

They are internally disjoint and have distinct ends.  Inside the source
bag, both `x-a_i` and `w-a_i` are present.  Thus

```text
P_i={x,a_i}
```

is connected, the rooted complement of `P_i` is connected, and the
original edge `wx` crosses the split.  The arm edge `a_iq_i` forces `q_i`
to be owned by `P_i` alone.

Every other old foreign contact is assigned an actual endpoint in the
expanded source bag.  A contact placed at `x` is owned by all three
candidate pieces, one placed at `a_i` is owned only by `P_i`, and one placed
at `w` is owned by none.  Hence its ownership incidence across the three
pieces must be one of

```text
000, 100, 010, 001, 111.
```

This is stricter than choosing three independent quotient contact masks.
The three arm contacts are added simultaneously before any transfer.  If
they already give a `Q`-rooted `K_5^-` minor, the placement is terminal.  If
not, the verifier performs each faithful transfer separately: it removes
precisely the source adjacencies owned by `P_i`, absorbs `P_i` into `q_i`,
and restores the original edge as the new source-to-`q_i` adjacency.

The other protected centre remains literal and retains a distinct original
centre edge to its own swallowed mate.  Any quotient adjacency between the
two protected bags is realised away from the two centre vertices, so the
centres themselves remain independent.  Whenever both centres separately
have a surviving three-arm expansion, the screen also tests their first
canonical choices together on one common augmented quotient.  This last
count is a reproducible symmetric diagnostic, not an exhaustive search over
all pairs of three-arm choices.

For every surviving quotient placement, the program builds the expanded
graph just described and applies an exact root-sensitive
deletion/contraction test for a `K_5^-` minor.  All five bags must meet the
seven literal vertices of `Q`.  This prevents a
false survivor caused by splitting one contracted centre bag into several
usable minor branch sets.

Run from the repository root:

```text
python3 active/experiments/dominated_singleton_order9_three_fan_gate/verify.py
python3 active/experiments/dominated_singleton_order9_three_fan_gate/marked_edge_absorption.py
python3 active/experiments/dominated_singleton_order9_three_fan_gate/corrected_one_contact.py
```

The second command is a separate, stronger exact operation screen.  It
orders the two non-`Q` terminals as the protected centre `w` and its mate
`x`, retains `wx`, and contracts each existing carrier edge `xq` into its
literal `Q` root.  The subsequent root-sensitive minor search exhausts all
ways of deleting or absorbing the remaining unmarked centre bag.  It
reports both the existential conclusion needed when one may choose among
the existing `xq` edges and the stronger per-edge conclusion.

The third command repairs a historical diagnostic bug: the former
one-contact helper added a second, fixed contact at the other protected
centre.  It recomputes every static survivor with exactly one added edge.

## Current verdict

The earlier `2,177`/`75` one-contact split is invalid.  Its helper encoded
`(contact,0)` or `(0,contact)` through a routine which adds both entries,
so every alleged single-contact test contained a hidden contact from the
other centre to `Q` root zero.  The canonical helper now accepts `None` and
adds exactly one edge.  The corrected replay finds that every static
failure still has a closing genuine contact at at least one centre, but
only `325,1242,334` placements close at both centres.  The remaining
one-sided counts are `102,204,45`, respectively.  Thus 1,901 of the 2,252
placements are two-sided and 351 are one-sided; the old 2,177/75 split and
its degree-profile conclusions must not be used.

The marked-edge absorption screen is complete and negative.  For the three
graphs on `Q`, respectively, it starts from `249,740,209` root-sensitive
baseline failures and tests `1,533,4,194,1,161` existing carrier edges
`xq`, over `498,1,480,418` orientations of `(w,x)`.  Contracting `x` into
`q` fails in every case.  This is structurally expected: the baseline
root-sensitive search already permits the unmarked vertex `x` to be
absorbed into any adjacent `Q`-rooted branch set.  Even after adding an
arbitrary edge `xq`, `142,320,102` orientations have no usable choice of
`q`.  Thus marked-edge parity alone does not terminalise the static model.

The explicit three-arm screen is also negative for the local inference.
Among the faithful suffix survivors, the numbers admitting a literal
three-arm survivor at some protected centre are `82,326,82`; the same
numbers admit one at both centres separately.  Testing the first canonical
choices simultaneously at both centres leaves `54,226,56`.  The latter is
not exhaustive over all pairs, but already supplies explicit survivors to
the local three-arm transfer claim.  None of these finite witnesses is a
critical-host counterexample, and the screen does not encode boundary
extension languages or an actual labelled separation.

The deterministic digests are:

```text
marked-edge absorption
FCQ`_  129d5e1c419912ab3479e25acc6f3bd6370ed830e9f825ba327ed7e2640407a6
FCQb_  0b07870fb91f4ee5a8a473844a0177f331753afafc45fe4959c646b8a00ccfad
FCp`_  5186acee6062ba35005e82be535257a2d05bb776496006e2d4a833df0af424c4

explicit three-arm screen
FCQ`_  00b0f69a153120e54fb8b43f63b1c8911932885cc5e35b9f80498004d2d3274b
FCQb_  188a8f46f1ac80c2d32f2eece6e5ed8728966be1b5e9de87260dfb2b09d197ad
FCp`_  fe5707d1d4c7ee065efef1dd3ed5fca3137778f3403a643c7c478ad8e02db359

corrected one-contact replay, first family
FCQ`_  bb79dc947187e7ba30145ee4fc06b7e0a3a1f65d372821264f2af55315204560
```

The last two corrected one-contact digests were not independently captured
in this run; the displayed complete counts are therefore not digest-pinned
by this README.

The checked script revisions are:

```text
51f096626f8c49715e0b2086c03213f00f2502620bad48665b10e5c425f530b5  ../dominated_singleton_nine_terminal_kernel/verify_order_nine.py
d4e76e39e0ede578582be8e5e8cac29e0712a73515425dee305826d176a0fd97  verify.py
acf57329066a57fd7634f0a3d5c21c14f39f641df4415a2629fa394e699c9222  marked_edge_absorption.py
f257802715a1102ce20f66068d12cc3034137f47091f2fbe3c94a788b9ee4b1d  corrected_one_contact.py
```

## Trust boundary

The computation can refute a proposed inference which uses only these
three local arms and their exact ownership transfers.  It cannot verify or
refute the operation-labelled host theorem.  In particular, an actual
labelled separation depends on the ambient graph and on which boundary
partition extends through each shore.  Neither datum survives contraction
to the nine-terminal kernel.  The source branch bag and its fan arms are
also unbounded before contraction, and no bounded compression theorem for
their colouring languages is known.  Consequently an exhaustive negative
result here would remain finite evidence, while a survivor only records a
route nonclosure for this explicit local mechanism.
