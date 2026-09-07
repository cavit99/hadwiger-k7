# Connectivity does not place prescribed vertices in distinct clique bags

**Status:** barrier/counterexample to an intermediate claim; written proof.
The adjacent audit records its checked revision. This does not refute the
five-root `K_6` proposal, Conjecture 21 or `HC_7`.

## Refuted assertion

> For every `t`, every `(t+1)`-connected graph containing a `K_t` minor
> has a `K_t` model placing any `t-1` prescribed vertices in distinct bags.

The assertion also fails with the weaker connectivity assumption `t`.
An unprescribed extra bag does not justify a general rooting argument.

## Counterexample family

**Theorem.** For every integer `m>=3`, let `F_m` be the complete
multipartite graph with `2m` parts, each of order two. Then `F_m` is
`(4m-2)`-connected and contains a `K_{3m}` minor. There is a set of
`3m-1` prescribed vertices which cannot occupy distinct bags in any
`K_{3m}` model.

**Proof.** Deleting fewer than `4m-2` vertices leaves at least three
vertices, hence vertices from at least two parts; the remaining complete
multipartite graph is connected. Deleting all vertices outside one part
disconnects that part's two vertices. Thus connectivity is exactly `4m-2`.

To construct the clique minor, retain one vertex from each part as a
singleton bag. Pair the remaining `2m` vertices arbitrarily into `m`
two-vertex bags. Each pair uses distinct parts and is connected. The
singleton bags are pairwise adjacent, and a bag using two parts is
adjacent to every other nonempty bag. These are `3m` clique bags.

Now consider any `K_{3m}` model and let `q` count its nonsingleton bags.
Its disjoint bags use at least `3m+q` vertices, so `q<=m`. Its singleton
bags lie in distinct parts and therefore number at most `2m`; hence
`3m-q<=2m`, giving `q>=m`. Equality forces every vertex to be used, with
exactly one singleton per part and exactly `m` two-vertex bags.

Put `r=3m-1`, and choose the prescribed set `S` of order `r` inside
`ceil(r/2)` parts. At most `ceil(r/2)` singleton bags contain prescribed
vertices. Therefore at least

```text
r - ceil(r/2) = floor((3m-1)/2) > m
```

prescribed vertices must lie in the `m` two-vertex bags. Some such bag
contains two prescribed vertices, so their placement cannot be distinct.
Finally `4m-2 >= 3m+1` for `m>=3`, proving the claimed failure even at
connectivity at least `t+1`, with `t=3m`. QED

For `m=3`, the graph has twelve vertices, connectivity ten and a `K_9`
minor; prescribe all eight vertices in any four of its six parts.

## Scope of the failure

Menger's theorem can give disjoint paths to distinct artificial selectors
attached to the bags of a clique model. Their first entries into the
original model need not belong to distinct bags. Assigning an entire path
to its terminal bag can remove vertices needed to connect another bag or
to retain its clique contacts. The theorem above rules out a universal
repair based solely on connectivity and one unprescribed bag.

The specific proposal for a six-connected graph with a `K_6` minor and
five prescribed vertices is not refuted here. Nor is an existential
construction choosing five suitable neighbours of a critical vertex.
Those require their own simultaneous construction or valid reduction;
neither Menger's theorem nor positive finite probes provides it.
