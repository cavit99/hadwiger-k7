# Internal audit: two protected exceptional centres and the order-eleven kernel

## Verdict and revision

**GREEN for the stated order-eleven exclusion.**  I checked the theorem
revision

```text
0cc512a6f8a686db7c0568e1b183912ea8e5395ec2cde7e83e6abd57e41e948b
```

of
[`hc7_k7minus_dominated_two_protected_centres_kernel.md`](hc7_k7minus_dominated_two_protected_centres_kernel.md).
The seven finite materials checked were

```text
c762891e8ce35617f20e7be840f2f5ca0ac697bcca7c1893dd0fa662611d48eb  active/experiments/dominated_singleton_nine_terminal_kernel/probe.py
cc12279f1f8ec4a83e0e3bb34e74741dd1ca4b292bd6e76c483314ecc3fb454a  active/experiments/dominated_singleton_nine_terminal_kernel/verify_order_eleven.py
2b4e458a659741cda7c9aa947decc83477f3e48f0fd3e271fca3e0187dc6c533  active/experiments/dominated_singleton_nine_terminal_kernel/verify_order_nine.py
334e55c0f04a36d7478dd60bd9008a87c950211b5fb0618e5481aadaa06a0ef4  active/experiments/dominated_singleton_nine_terminal_kernel/order_ten_catalogue.py
3fae483e31202b7c7e3e9a29277205c2af28588a8d0b8794e9dd1584e0719f32  active/experiments/dominated_singleton_nine_terminal_kernel/screen_order_ten.py
65fe509ddfa260dd33f6c36bc60e5fe8cad547bfbd56b7c590e20bc1752640dc  active/experiments/dominated_singleton_nine_terminal_kernel/screen_swallowed_suffix.py
1cb7484e461495bfa2426adb181d189bcafcfc4f71509d21280dbe74ae780ee3  active/experiments/dominated_singleton_nine_terminal_kernel/audit_order_ten.py
```

This is an internal mathematical and implementation audit, not external
peer review.  It is not an independent reimplementation of the finite
minor search.

## 1. Host hypotheses and terminal count

The two additional centres really are available as distinct terminals of
`H-Q`.  They are distinct from `u` and mutually nonadjacent because they
belong to the fixed independent five-set.  In particular they are not in
`N(u)={v}\cup Q`, while deleting `u,v` leaves them in `H`.

The proved dominated-centre reduction gives that `H` is five-connected,
so the three-connected terminal-kernel theorem applies to
`T=Q\cup{w,w'}`.  With nine terminals its bound is

```text
|V(K)-T| <= floor(9/4)=2,
```

which gives exactly the range 9--11 used in the theorem.  Terminal-legal
contractions preserve all nine labels and lift to a spanning partition of
`H` into connected branch sets.

## 2. Wu-charge dichotomy

For each nonterminal `s`, terminal irreducibility means that no edge at `s`
is contractible.  Wu therefore gives at least four degree-three neighbours,
each incident with two contractible edges.  Those contractible edges must
have both ends in `T`, because every contractible edge with a nonterminal
end would be terminal-legal.  Thus the charged neighbours lie in `T` and
have terminal degree two.

Charge sets at the two nonterminals are disjoint.  A common charged vertex
would have its two terminal contractible edges and an edge to each
nonterminal, contradicting degree three.  Since `|T|=9`, the union has order
eight or nine.  Taking each charge set to contain all neighbours with the
stated Wu property makes the phrase “uncharged terminal” unambiguous.

If all terminals are charged, deleting the two nonterminals leaves a
connected two-regular graph, hence `C9`.  The nonterminal edge is
contractible if present, because deleting its ends leaves `C9`, so it is
absent.  Applying the exact edge-contraction criterion to a spoke shows
that every charge-class vertex has a same-class cyclic neighbour.  The run
argument leaves the `2,3,2,2` pattern; the one-run alternative has the
displayed two-cut.  Lemma 2.1 is sound.

If one terminal `z` is uncharged, the other eight have terminal degree two.
Deleting the nonterminals still leaves a connected graph.  Handshaking
makes `d_{K[T]}(z)` positive and even.  Every component after deleting `z`
is a path whose two ends meet `z`; a cycle component would be disconnected
from `z`, and a one-vertex path would require parallel edges.  This gives
exactly the bouquet parameterisation with one to four paths of order at
least two.  Charged degree-three vertices also justify that only `xz,yz,xy`
can occur in addition to the two charge stars.  Lemma 2.2 is exhaustive.

## 3. Charge-complete finite check

The cycle generator fixes terminal label zero and rejects one of the two
orientations.  It therefore generates

```text
8!/2 = 20,160
```

labelled undirected nine-cycles.  Direct generation of binary cyclic words
with four `A` entries, four runs and minimum run length two gives exactly
nine words.  A cycle and its `A` subset determine the ordered
four-charge/five-charge kernel uniquely, so there is no missing terminal
labelling.

For every legal owner of each nonterminal, the verifier adds precisely the
quotient star produced by absorbing that nonterminal.  It then checks all
49 assignments of the two protected centres to `Q` roots and retains an
assignment exactly when each resulting rooted bag is connected.  This is
enough even if a target model would not use one of the nonterminals or
centres: absorbing an unused connected bag at an adjacent rooted bag can
only add quotient edges.

The three live labelled `Q` graphs are checked separately.  The rerun
reported 544,320 high-level cycle/pattern/`Q` instances and zero failures.

## 4. One-uncharged finite check

The ordered compositions of eight into one to four parts of order at least
two number thirteen.  For each, the script chooses the four neighbours of
the first nonterminal and all eight subsets of `xz,yz,xy`, giving

```text
13 * binom(8,4) * 8 = 7,280
```

parameters.  Every bouquet can be ordered and each path oriented, so these
parameters cover the structural form in Lemma 2.2.  The implementation then
tests all vertex cuts of order at most two and applies the contraction
criterion to every edge incident with either nonterminal.  It additionally
excludes the ten cycle parameters in which `z` is itself Wu-special; those
belong to the charge-complete branch.  The 34 survivors have exactly the
asserted terminal profiles: two cycles and thirty-two pairs of five-cycles
sharing `z`.

For each survivor, all 36 choices of the two centre positions are checked.
The remaining seven positions receive every labelled copy of the fixed
`Q`: the independently asserted copy counts are 252, 2,520 and 360.  The
script assigns all four non-root vertices to the seven rooted groups in all
`7^4` ways and keeps exactly the assignments with connected groups.
Consequently it does not assume independent or predetermined owners.

The rerun reproduced

```text
FCQ`_   308,448 tests
FCQb_ 3,084,480 tests
FCp`_   440,640 tests
```

with no failure.

The imported minor routine is exact.  When the current graph has more than
five vertices it exhausts deletion of an unused vertex and contraction of
an edge inside a non-singleton branch set.  At order five, at least nine
edges is exactly a `K5^-` subgraph.  Thus a positive answer is equivalent to
the required minor, not merely a density heuristic.

## 5. Lift and scope

Every final quotient vertex represents a connected union containing one
distinct member of `Q`.  A `K5^-` minor in that seven-vertex quotient
therefore lifts to five connected branch sets in `H`, each meeting `Q`.
The two singletons `u,v` are adjacent to one another and to all five sets,
so they give `K2` joined to that model, namely a `K7^-` model.  This proves
the contradiction in Theorem 4.1.

The proof establishes only

```text
|V(K)| in {9,10}.
```

It does not eliminate either remaining order.  In particular, the retained
order-nine diagnostic has genuine static quotient survivors.  Its further
two-contact check eliminates every survivor only after granting each centre
an arbitrary adaptive contact with a distinct rooted quotient bag.  The
audit agrees that the actual matching representative need not survive as
such a contact: its endpoint can be absorbed into the centre-rooted bag.
No original degree-eight condition is transferred to a contracted kernel
vertex, and no colouring-response compatibility is inferred from the finite
carrier calculation.

The adjacent order-ten catalogue is structurally exhaustive for its stated
rooted occurrences.  If `x` is the unique nonterminal, then `J=K-x` is
two-connected by three-connectivity of `K`.  Every degree-two vertex of `J`
must be adjacent to `x`, since it has degree at least three in `K`; such a
vertex is then degree three in `K` and both its `J` edges are contractible
terminal edges, so it belongs to Wu's charged set.  Wu gives at least four
of them.  Conversely, after selecting any subset of higher-degree vertices
as additional neighbours of `x`, exact tests of three-connectivity and
noncontractibility of every edge at `x` are precisely the remaining kernel
conditions.  The generator's 1,153 occurrences and displayed root-degree
profile therefore do not rely on transferring the original degree eight
of a centre to a contracted kernel bag.

The order-ten composition screen checks all positions of the two protected
centres and all labelled copies of `Q` on the other terminals.  It ranges
over every connected absorption of both centre vertices and the unique
nonterminal.  Its contact augmentation is explicitly conditional: it adds
one edge from one selected centre vertex to a chosen `Q` root before the
absorptions.  Zero one-contact failures proves the finite implication, not
the existence of that contact in the host.

The independent order-ten checker does not import the discovery generator,
composition screen or minor routine.  It regenerates the 1,153 occurrences
from `geng`, reproduces occurrence digest
`b4b188d11db1d2c7047e8d92e479e0f8c0e937a48e7c47caf1b88a2ed4975702`,
and checks the conclusion through connected five-bag partitions.  Its replay
reported no one-contact failure for any of the three `Q` types.

The generous swallowed-suffix diagnostic is likewise correctly scoped.  It
applies only to the 2,252 static order-nine survivors and permits any contact
set of order at least two while retaining every old source-bag adjacency.
Its zero-survivor output is a positive quotient implication under stronger
data than a literal split may retain.  The separate exact transfer screen
deletes source adjacencies owned only by the suffix and leaves
`256,1022,256` placements.  Accordingly the theorem records static suffix
transfer as a route nonclosure rather than inferring a host split.

## 6. Unresolved trust boundary

The finite scripts import the previously retained exact minor routine and
the audited list of three live `Q` codes.  This audit checked their use and
replayed both scripts, but did not implement an independent connected-
partition minor detector.  Promotion beyond the active frontier should
therefore obtain a cold independent replay of the finite calculations.
