# Nine-terminal protected-centre kernel experiment

This directory certifies the two-nonterminal branch obtained by protecting
the seven vertices of `Q` and two exterior exceptional centres in
`H=G-{u,v}`.

Run from the repository root:

```text
python3 active/experiments/dominated_singleton_nine_terminal_kernel/probe.py
python3 active/experiments/dominated_singleton_nine_terminal_kernel/verify_order_eleven.py
```

The first command checks the charge-complete order-eleven normal form.  Its
expected terminal output is:

```text
patterns 9 tests 544320
failures {'FCQ`_': 0, 'FCQb_': 0, 'FCp`_': 0}
first {}
```

The second command checks the one-uncharged-terminal normal form.  Its
structural generator starts with all `13*70*8=7,280` ordered bouquet,
charge and optional-edge parameters.  Exact three-connectivity and
terminal-irreducibility tests and the exact uncharged condition leave 34
canonical parameter instances: 2 with one terminal cycle and 32 with two
five-cycles sharing the
uncharged terminal.  It then checks all 1,584 placements of the protected
centres and every labelled copy of each live `Q` type.  The expected
summary is:

```text
canonical_skeletons 34
protected_centre_placements 1224
q_copy_counts {'FCQ`_': 252, 'FCQb_': 2520, 'FCp`_': 360}
tests {'FCQ`_': 308448, 'FCQb_': 3084480, 'FCp`_': 440640}
failures {}
first_failure {}
```

For each exact kernel parameter, the verifier enumerates every connected
assignment of the two protected-centre vertices and the two nonterminals to
the seven `Q`-rooted quotient bags.  Every final quotient is tested for a
`K_5^-` minor by exact deletion-and-contraction recursion.

`verify_order_nine.py` is a retained diagnostic for the all-terminal
order-nine residue.  Static composition leaves respectively 427, 1,446 and
379 labelled placements for the three `Q` types.  If the two protected
centre bags are each allowed one additional contact to an adaptively chosen
`Q`-rooted bag, no placement survives.  This does not prove that the host
supplies such quotient contacts: a matching-representative edge may have
its other endpoint inside the same contracted centre bag.  The diagnostic
is not used in the order-eleven theorem.

One adaptive contact already closes 2,177 of the 2,252 static survivors.
In the remaining 75 placements, the usable-contact centre always has
kernel degree three and the other centre has degree four through eight.
Only two of those 75 placements have nonadjacent centre vertices, so
adjacency is not the correct host discriminator.

The order-ten row is generated and checked by:

```text
python3 active/experiments/dominated_singleton_nine_terminal_kernel/order_ten_catalogue.py
python3 active/experiments/dominated_singleton_nine_terminal_kernel/screen_order_ten.py
```

The first command derives all 1,153 unlabelled rooted occurrences from the
Wu degree-two condition, exact three-connectivity and exact
noncontractibility at the unique nonterminal.  The second checks
130,003,056 labelled `Q`/centre placements.  Static composition leaves
840, 1,811 and 598 placements; one arbitrary adaptive protected-centre to
`Q`-bag contact eliminates every survivor.  This is again a conditional
quotient theorem, because the host must still supply a matching-coordinate
edge leaving a centre-rooted bag.

The additional diagnostic
`screen_swallowed_suffix.py` tests the quotient shadow of the proposed
internal path split.  On every all-terminal order-nine static survivor,
grant a swallowed suffix contacts with any two or more rooted bags, retain
all old source-bag adjacencies, and absorb the suffix into one contacted
bag.  No quotient survives.  This is deliberately more generous than a
literal host split: it does not delete source adjacencies owned only by the
suffix.  The host still has to prove that a minimal centre-rooted bag has a
suffix with two useful foreign rooted-bag contacts and that the source bag
retains the required carrier adjacencies.

The finite checks do not prove the terminal-kernel reduction.  The host
theorem and the Wu-charge derivation are written in the adjacent active
theorem note.
