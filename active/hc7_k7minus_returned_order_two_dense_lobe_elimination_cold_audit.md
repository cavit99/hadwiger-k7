# Independent cold audit: returned order-two dense-lobe elimination

**Verdict:** **GREEN** at the frozen theorem and verifier revisions

```text
b5ddf0129e96588e38997c7669f7f55b926836ed9ad912d1ae056a22e14f9a83
  active/hc7_k7minus_returned_order_two_dense_lobe_elimination.md
929ca03af1c5404b659b0391b9fe089acd414dfebe8f93117fe3ac02d1c682df
  active/experiments/returned_order_two_dense_lobe_elimination/recursive_verify.py
1c44627c6ec673efefd38d9b31584b68f8e36defb3b77530c58761ab4337407c
  active/experiments/returned_order_two_dense_lobe_elimination/partition_verify.cpp
```

This is an independent internal mathematical and computational audit, not
external peer review.  The current theorem SHA-256 is
`c7973ede760cb62ece475b5a2c2a67e9f5f46bc45b80275963ed14346f82d69a`;
the only later change records this GREEN audit in its status line.  No
statement, proof, computation, dependency, or scope claim changed.

## 1. Nine-vertex quotient

Contracting the connected opposite component `B` produces one vertex `b`.
Fullness gives all six `b-S` edges, while the fact that `A` and `B` are
distinct components of `G-S` excludes `bx` and `by`.  The retained edge
`xy`, the arbitrary boundary graph, and the two labelled attachment sets
therefore give exactly the quotient encoded by both verifiers.  A target
minor in this quotient lifts through the contraction, so the order of `B`
is genuinely unrestricted.

## 2. Equality reduction and profile count

Let `d` be the number of boundary vertices adjacent to both `x` and `y`.
Fullness gives exactly one attachment at each of the other boundary
vertices, and hence

```text
p=6+d.
```

Thus `p>=21-e_S` is equivalent to `d>=15-e_S`.  Retain both attachment
edges at exactly `15-e_S` double vertices and delete one attachment edge
at every other double vertex.  This preserves fullness and produces a
spanning subgraph at equality.  Since adding edges cannot destroy a minor,
verification of every equality profile proves the inequality case; no
minimality or induced-subgraph assumption is being used.

At equality the number of singly attached boundary vertices is

```text
6-(15-e_S)=e_S-9.
```

Choosing the boundary graph, the singly attached vertices and their
endpoint independently gives

```text
e_S=9:  binom(15,9)  binom(6,0) 2^0 =  5,005
e_S=10: binom(15,10) binom(6,1) 2^1 = 36,036
e_S=11: binom(15,11) binom(6,2) 2^2 = 81,900
total:                                      122,941.
```

The base-three status loops in both implementations realise exactly these
labelled choices: status zero is left-only, one is right-only, and two is
double.  The fifteen-bit masks independently enumerate every boundary
graph with the nominated edge count.

## 3. Recursive verifier

The Python search begins with all nine singleton bags.  A merger is allowed
exactly when two bags touch, so every generated bag remains connected;
deletion makes vertices unused.  Conversely, for any seven-branch-set
minor model, delete every unused singleton and merge each desired branch
set along a spanning tree.  This gives a search path to the model before
the bag count reaches seven.  At seven bags, at most one missing pair is
equivalent to a `K_7^-` model, with a `K_7` model correctly accepted as
well.

A clean rerun produced

```text
eS=9 checked=5005 positive=5005
eS=10 checked=36036 positive=36036
eS=11 checked=81900 positive=81900
controls=PASS
total=122941
certificate_digest=c90f0ffb52a2ee94b30d0d249e048b5501f97d4f34fdf291874780fab968370c
```

The digest agrees exactly with the frozen theorem and experiment notes.
The positive control is a `K_7^-` plus two unused vertices; the negative
control is a `K_6` plus three isolated vertices.  Both have the asserted
status.

## 4. Direct partition verifier

The C++ verifier generates a set partition by processing the used vertices
in increasing order, adding the next vertex to any existing block or
creating one new final block.  Ordering blocks by their first-created
vertex makes this a duplicate-free and exhaustive restricted-growth
generation.  Over used subsets of orders seven, eight and nine, the count
is

```text
binom(9,7) S(7,7) + binom(9,8) S(8,7) + S(9,7)
= 36 + 252 + 462 = 750,
```

where `S(n,k)` is a Stirling number of the second kind.  These are exactly
all possible unions of seven nonempty branch sets in a nine-vertex graph.
The subsequent tests are literal breadth-first connectedness tests and
all twenty-one interbag adjacency tests.

The documented optimized build reproduced

```text
eS=9 checked=5005 positive=5005
eS=10 checked=36036 positive=36036
eS=11 checked=81900 positive=81900
partitions=750
controls=PASS
total=122941
```

An additional build with libstdc++ debug iterators and AddressSanitizer plus
UndefinedBehaviorSanitizer completed the same census with exit status zero.
The two verifiers share only the transparent quotient/profile definition;
their minor searches are independently implemented as recursive minor
operations and direct branch-set partitions.

## 5. Corollary and scope

At source revision

```text
87fdc55007f32622a11f5050d6f0e9719e45af95c1e7e2d86f480a4a3a1338e3
  active/hc7_k7minus_returned_two_component_contraction_descent.md
```

outcome 1 of Theorem 6 supplies precisely a full order-two edge component,
`9<=e_S<=11`, and at least `21-e_S` attachment edges.  Its elimination is
therefore a direct application of the audited finite theorem.  This audit
checks that handoff, not the full proof of the separate descent theorem.

No equality, monotonicity, enumeration, branch-set completeness, control,
or scope defect was found.  The result eliminates only the dense returned
order-two component; the boundary-atom, nested-separator and sparse rows
remain open exactly as stated.
