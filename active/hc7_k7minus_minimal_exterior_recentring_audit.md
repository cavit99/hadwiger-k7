# Internal audit: minimum exceptional exterior and recentering

**Audited source:** `hc7_k7minus_minimal_exterior_recentring.md`

**SHA-256:**
`5c4e98bd1ea25a22d2c96b1e8a2abcce39759191006fe250f5bbaf971f933e7a`

**Verdict:** **GREEN.**  The minimum-component and colouring deductions are
written and unbounded.  The added terminal corollary correctly invokes the
separately audited full-side vertex exclusion and eliminates the former
recentring alternative.  The result inherits computer-assisted trust
boundaries from cited inputs; no new finite computation is used here.
This is a separate internal mathematical audit, not external peer review.

## Dependencies checked

| Input | SHA-256 |
|---|---|
| Two-component literal-clique exclusion and density jump | `e1b54acdd971831786c0d8912d5e4189aaeedd84184540ed438e594aadb9b2e4` |
| Degree-eight exterior-component bound | `4ee48c6d71c994b166b29dcd969d64c3526e6b6b75fa8a849fae834cf95eea29` |
| Same-miss exclusion | `2b269e7ecea09f695991689e2a6db64d928aedb141ea8cfbf85d14f84fc70617` |
| Critical seven-cut capacity | `d4d650fee168fc2ff0e00a3b7b0faed6ff674ba8cd3c06c263f63c4170656f34` |
| Two-singleton common-host theorem | `4abda28600ee5acb22bf56f1946e0ea2499d2bc5b2d90f65ad2ba1dd10b40c75` |
| Common-host double-contraction and lock allocation | `753dbf0fc251584dac8a67d907988737ac8dda30daa3dcc24b6fbabd949cf467` |
| Operation-coupled order-eight response | `be8fc118ab832ff9a24057873c815805539c0ab7cb1e4996c4d81202cf72b268` |
| One-nonfull full-side vertex exclusion | `c13889297cbfafabc4056532ee86d49793cae2aa98e0c0c19b3f8759da4019bc` |

Each dependency has an adjacent GREEN internal audit.  The exterior-component
bound is the only computer-assisted input essential to the minimum-component
proof.  The standard Ramsey equality `R(5,3)=14` is also used.

## Mathematical check

The two-component theorem first removes every literal `K_5`, raises minimum
degree to eight, and supplies at least `25+tau` degree-eight vertices.  A
singleton exterior component would be a false twin of the centre and would
allow a six-colouring, so both components are nontrivial.

For a degree-eight vertex `v` in a minimum component `E`, at least one
neighbour lies in `E`, leaving at most seven boundary neighbours.  If the
opposite component meets a missed boundary vertex, any additional component
of `G-N[v]` lies strictly inside `E`, contradicting minimality.  Otherwise
seven-connectivity forces one missed boundary vertex, seven common boundary
contacts, and exactly one neighbour of `v` in `E`.  The degree-eight
component bound then gives precisely the two equal-order components stated
in the source.

The same-miss exclusion supplies the attachment at the omitted vertex.
Critical seven-cut capacity makes the resulting packing vector exactly
`(1,2)` and forbids two different recentering vertices in `E`.  Relative to
the new centre, the component containing `u` contacts all seven common
boundary vertices through `u`; same-miss exclusion supplies its remaining
contact, so the claimed one-nonfull orientation is exact.

For the nonadjacent recentered pair, the universal alternative in the
two-singleton theorem applies to every vertex-deletion colouring.  Properness
at the retained vertex forces the two opposite equality patterns on the
common seven-set.

For Lemma 6, the private edges `uy,vw` are disjoint and their deletion
leaves `N_H(u)=N_H(v)=S`.  A five-colouring of that common host would extend
after giving the nonadjacent vertices `u,v` one fresh colour.  The audited
two-edge theorem supplies all three permitted equality patterns.  In a
double-contraction response, distinct colours on the two contracted pairs
can be exchanged at `u,v`; this makes both deleted edges proper and hence
would six-colour `G`.  All four endpoints therefore have one colour, every
other colour occurs on `S`, and properness forces `yw` to be absent.  The
same-colour lock theorem gives one lock for each alternate colour and a
three-lock majority for one fixed pair.  Since `H-S` has precisely the
components `F,{u},{v},C`, the last-boundary tails of all these lock paths
are correctly localized in the one connected middle subgraph `C`.
The one-restoration part of the same theorem separately leaves at least four
locks on each private pair after passage to `H`; the source correctly warns
that the two resulting colourings need not agree.

For Corollary 7, the five differently coloured last-`S` vertices give at
least five neighbours of `C` in `S`.  Equality with all seven vertices of
`S` would contradict critical capacity using `F,{u},{v},C`, so the contact
set has order five or six.  Direct edge bookkeeping gives the exact
neighbourhood `T union {u,v}`, the connected complementary component
`F union (S-T)`, and fullness of both sides.

The maximum-degree conclusion is also valid.  If `a-b-c` is a path in
`G[T]`, the seven displayed branch sets are connected and disjoint.  The
first four form a clique, are each complete to the three path singletons,
and only the `a-c` adjacency may be absent.  This is an explicit `K_7^-`
model.  When `|T|=5`, every full connected subgraph in `C` must contain the
unique `C`-neighbours `y,w` of `u,v`, so that side has packing number one.
Two full subgraphs on the other side would give total capacity three, whose
nine-edge boundary bound contradicts the ten edges from `u,v` to `T`.
Thus the order-seven packing vector is exactly `(1,1)`.

Finally, the count outside the nine-vertex closed neighbourhood and
`R(5,3)=14` correctly yield an independent four-set of degree-eight
exceptional vertices.

The new terminal step is immediate and correctly oriented.  In the former
recentring outcome, old `F` misses `y`, while old `E` is full to `X`: `v`
sees `S=X-\{y\}` and the same-miss exclusion supplies an `E`--`y`
attachment.  Thus `{v}` is an `S`-full singleton in the full component of
a one-nonfull configuration.  The audited full-side vertex theorem excludes
exactly this configuration through a six-colouring.  No matching-core path
or boundary classification is needed.

## Exact limitations

The former recentering vertex and its exact order-seven/eight matching-core
interfaces are now excluded.  The result still does not exclude the
original disconnected centre `u`: its selected minimum component may
contain no degree-eight vertex, or only degree-eight vertices with connected
anti-neighbourhoods.  The general one-nonfull, adjacent-miss and both-full
configurations remain open.  No global exceptional-centre connectivity
theorem or `K_7^-` six-colour theorem follows.
