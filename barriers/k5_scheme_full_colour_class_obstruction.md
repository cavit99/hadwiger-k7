# A rooted K5 scheme with no full colour-class bag

**Status:** explicit counterexample to a prescribed normal form, with a
written proof and a separate internal audit recorded beside this source.
It is not a counterexample to K5 contractibility or to Hadwiger's conjecture.

## Construction and exact claim

Let the five roots be `a,b,c,d,e`, and let the other vertices be
`u,B,C,D,E`, of colours `a,b,c,d,e`, respectively. Each root has its own
colour. Take precisely the edges in these ten paths:

```
a-B-u-b    a-C-u-c    a-D-u-d    a-E-u-e
b-C-B-c    d-E-D-e
b-d        b-e        c-d        c-e
```

These are a properly coloured K5 scheme: each path uses just its two
endpoint colours, contains no foreign root, and every common path
vertex has its colour as a common target endpoint. The host has ten
vertices and twenty-two edges.

**Proposition.** This scheme has a rooted K5 minor, but in every rooted
K5 model each bag omits the nonroot of its own root's colour. In
particular, no full colour class can be prescribed as part of its own
root bag, even while the other bags are allowed arbitrary expansion.

**Proof.** A positive model, in root order `a,b,c,d,e`, is

`{a}, {b,C}, {c,B}, {d,E}, {e,D}`.

Each pair bag is connected. The a bag meets the other four through
`C,B,E,D`; the b--c and d--e contacts use `CB` and `ED`, while the
remaining four contacts are literal root edges.

We exclude the proposed full-colour-class bags for arbitrary models,
allowing unused vertices. Write `R_t` for the bag of root t. The
permutations interchanging `b,c` or `d,e`, or exchanging these two
pairs, together with their corresponding capital vertices, are host
automorphisms. It suffices to consider `u in R_a` and `B in R_b`.

Suppose `u in R_a`. Since a and u are nonadjacent, connectivity forces
some capital vertex into `R_a`; by symmetry choose B. The only nonroot
neighbours of c are u and B. Both are already in `R_a`, and every other
neighbour of c is another prescribed root. Thus `R_c={c}`, which has no
contact with `R_b`. This is impossible.

Now suppose `B in R_b`. If u were also in `R_b`, the same neighbourhood
argument would make c singleton, this time missing `R_a`. Hence
`u notin R_b`. Connectivity of `R_b` forces C into it: the only possible
neighbours of B inside this bag are u and C, since a and c are other
roots. The a bag cannot be singleton, because its four neighbours
`B,C,D,E` would then meet at most three other bags. By the first case
it does not contain u, and B,C are already owned by b. It must therefore
contain D or E; interchange d,e if necessary so that `D in R_a`.

The c bag must contain u. Otherwise it is singleton, because its only
nonroot neighbours are u and B, and it has no contact with `R_a`.
Consequently the only two nonroot neighbours of e, namely u and D,
belong to `R_c` and `R_a`. This forces `R_e={e}`, which misses `R_d`.
The contradiction completes the proof. QED

## Exact finite cross-check and scope

The [standard-library verifier](k5_scheme_full_colour_class_obstruction_verify.py)
enumerates all `6^5=7,776` allocations: each nonroot is either unused or
belongs to one of the five named bags. It tests connectivity and all ten
required contacts. It finds exactly 21 rooted K5 models and none containing
an own-colour pair. Calibration includes a literal K5, a rooted C5
negative, and the canonical two-copy K5 with a positive own-colour-pair
model. Run:

```sh
uv run python3 barriers/k5_scheme_full_colour_class_obstruction_verify.py
```

Expected output begins `PASS: proper K5 scheme; 7,776 allocations; 21
rooted models; no own-colour pair in any bag`. The written proof above
does not depend on enumeration. The obstruction concerns compulsory
full-colour-class allocation; partial allocations and the displayed
rooted K5 remain valid. It supplies no counterexample to the actual
seven-connected, degree-eight critical-host construction.

## Four marked vertices: avoidance or separation also fails

Let K have roots `0,1,2,3` and nonroots `4,5,6,7`, with the latter
having colours `0,1,2,3`, respectively. Its edges are precisely the union
of these six properly coloured K4-scheme paths:

```
0-1    0-2    1-3
0-7-4-3    1-6-5-2    2-7-6-3
```

Mark all four nonroots. This refutes the following proposed alternative:
a rooted K4 model either omits a marked vertex or puts the four marked
vertices in four different bags. A rooted K4 model does exist, for example
`{0,4,7}, {1}, {2,5,6}, {3}`.

**Proof of the obstruction.** Deleting 7 leaves root 0 with only roots
1,2 as neighbours. Its bag must be singleton and cannot meet three other
bags. Deleting 6 gives the same obstruction at root 1, whose remaining
neighbours are roots 0,3. Thus every model uses 7 and 6.

After deleting 4, root 3 has only neighbours 1,6. Its bag cannot be
singleton, so it must contain 6. Root 1 then has no available nonroot
neighbour and is singleton; its neighbours 0,3,6 belong to only two
other bags. This is impossible. After deleting 5, root 2 similarly must
own 7, leaving root 0 singleton with contacts to only the 1 and 2 bags.
Consequently every rooted K4 model uses all four marked vertices.

If the markers were in four different bags, each bag would consist of
its root and exactly one marker. Connectivity forces, successively,
`{0,7}, {1,6}, {2,5}, {3,4}`. The last two bags are nonadjacent.
This proves the obstruction for arbitrary rooted models, including
models initially allowed to leave vertices unused. QED

There is nevertheless a positive K5 extension with different ownership.
Add a new root a and a nonroot u of a fifth colour, and add the four
paths `a-(i+4)-u-i`, for `i=0,1,2,3`. Together with the six paths above
these form a proper K5-scheme. In root order `a,0,1,2,3`, it has the model

`{a,7}, {0}, {1,6}, {2,5}, {3,u}`.

All pair bags are connected. The a bag meets the other four through
`7-0,7-6,7-2,7-u`. The middle three bags meet through `0-1,0-2,6-5`,
and the last bag meets those three through `u-0,u-1,u-2`. Vertex 4 is
unused. Thus a may take a marker while u belongs to a different root's
bag. The failed alternative restricted a method of first extracting a
K4 model in K; it does not exhaust allocations in the augmented host.
This additional obstruction and its positive extension are established
by the displayed proofs, independently of the verifier for the earlier
ten-vertex example. Neither is a counterexample to rooted K5 extraction.
