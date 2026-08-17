# Codegree two need not occur at a degree-eight vertex

**Status:** explicit `K_7^-`-minor-free counterexample, with a deterministic
exhaustive verifier.  It shows that the six-connected degree-eight
low-codegree theorem is sharp.

The verifier is
[`hc7_k7minus_sixconnected_degree_eight_codegree_two_barrier_verify.py`](hc7_k7minus_sixconnected_degree_eight_codegree_two_barrier_verify.py).
Its SHA-256 is

```text
8f6ce5fe0d32ef3e8fcdd15d82e9c6444483a4360dfae4a59ae59499c48142a2.
```

## The false assertion

The following proposed strengthening is false.

> If `G` is six-connected and has no `K_7^-` minor, and `v` has degree
> eight, then some edge incident with `v` has codegree at most two.

There is such a graph in which the seven non-apex edges at `v` all have
codegree exactly three.

## Construction

Start with an icosahedron.  Subdivide each edge once and, in every original
face, join its three subdivision vertices.  This is the frequency-two
icosahedral triangulation `P_0`, with

```text
|V(P_0)|=42,       |E(P_0)|=120.
```

Choose an original face with vertices `0,1,5`, and write `s_ij` for the
subdivision vertex on edge `ij`.  In the quadrilateral formed by the two
triangles

```text
{5,s_05,s_15},       {s_01,s_05,s_15},
```

replace the diagonal `s_05 s_15` by `5 s_01`.  Call the resulting planar
triangulation `P`.  Finally, let

```text
                         G = K_1 join P,
```

and denote the cone apex by `a`.  In the verifier, `s_01` is vertex `12`
and `a` is vertex `42`.

The flip changes the degree profile of `P` to

```text
degree 5: 13 vertices,   degree 6: 28 vertices,   degree 7: s_01.
```

The verifier exhausts all `124,314` vertex sets of order at most four and
finds that their deletion leaves `P` connected.  A degree-five vertex
supplies a five-cut, so `P` is exactly five-connected.  It follows directly
that `G` is exactly six-connected: if the apex survives it joins all
remaining vertices, whilst after deleting it at most four further vertices
have been deleted from `P`.  Conversely, deleting the apex together with
the neighbours of a degree-five vertex disconnects `G`.

## Target exclusion

The graph `G` has no `K_7^-` minor.  Indeed, a model avoiding the apex would
lie in the planar graph `P`.  If a branch set contains the apex, delete that
branch set from the model.  The other six branch sets would give a `K_6` or
`K_6^-` minor in `P`, according as the deleted target vertex is or is not an
end of the missing edge.  Both alternatives are non-planar.

## The incident codegrees

Put `v=s_01`.  The graph induced by its seven neighbours in `P` is the
cycle

```text
0 - s_05 - 5 - s_15 - 1 - s_18 - s_08 - 0.
```

Thus each edge from `v` to a neighbour in `P` has two common neighbours in
`P`, and gains the apex as a third common neighbour in `G`.  The edge `va`
has all seven planar neighbours of `v` as common neighbours.  Consequently

```text
degree_G(v)=8,       {c_G(vx): x in N_G(v)}={3,3,3,3,3,3,3,7}.
```

The proposed bound of two therefore fails, whilst the proved bound of three
is attained.

## Scope

The counterexample has

```text
|V(G)|=43,       |E(G)|=162=4|V(G)|-10.
```

It does not refute a version assuming seven-connectivity, density at least
`4|V(G)|`, or the additional hypotheses of the critical host.  Those are
the remaining plausible settings for a codegree-two conclusion.

## Reproduction

From the repository root run

```text
python3 -B barriers/hc7_k7minus_sixconnected_degree_eight_codegree_two_barrier_verify.py
```

The checker uses only the Python standard library.  It reconstructs the
triangulation and its spherical face certificate, exhausts every deletion
of at most four planar vertices, verifies the displayed five-cut, and
checks the cone parameters, degree profile and all eight incident
codegrees.  It prints the SHA-256 digest of the complete cone edge set.
