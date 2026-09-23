# Two complete path systems in one disagreement region do not force K7

**Status:** explicit counterexample with a written exclusion proof and a
deterministic certificate check; no separate audit. It refutes an intermediate
construction, not the original critical-host case or HC7.

## Statement refuted

Let `N(u)=P dotunion D`, with `P={p,a,b}` a triangle and
`D={d1,d2,d3,d4}` a four-clique, anticomplete to P. Suppose G-u has proper
six-colourings phi and psi which fix `di=i`, have the same entire sixth
class B, and satisfy

    phi(p,a,b) = (6,5,4),    psi(p,a,b) = (6,3,5).

Suppose every p/a-to-`{d1,d2,d3}` demand has a path using its endpoint
colours under phi, and every p/b-to-`{d1,d2,d4}` demand has such a path
under psi. Suppose also that the colourings agree outside one strongly
connected component of the transition digraph: orient xy from x to y
when `psi(x)=phi(y)`.

These conditions do **not** imply a K7 minor. In particular, making the
two full systems agree outside one region does not justify their simultaneous
branch-set allocation.

## Construction

Take the seventeen vertices

    u,p,a,b,d1,d2,d3,d4,x,t,s,v1,v2,e1,e2,f,q.

Include the edges of the cliques P, D and `{a,x,b}`, every edge from u
to `P union D`, and exactly the following additional edges:

    px;
    av_i, bv_i, tv_i, td_i, pe_i, e_i f, fd_i   (i=1,2);
    xs, sd3, sd4, xq, qd3, qd4.

There are 39 edges. The vertices `p,f,q` have colour six, `t,s` have
colour five, and `di,vi,ei` have colour i whenever those vertices exist.
The two colourings differ only on the triangle:

| Vertex | a | x | b |
| --- | --- | --- | --- |
| phi | 5 | 3 | 4 |
| psi | 3 | 4 | 5 |

Both are proper. Their whole transition digraph has just the three arcs
`a -> x -> b -> a`; agreement vertices have no transition arcs.

For i=1,2, use `p-e_i-f-d_i` in both systems, `a-v_i-t-d_i` under phi,
and `b-v_i-t-d_i` under psi. The four remaining paths are

    phi: p-x-q-d3, a-x-s-d3;
    psi: p-x-q-d4, b-x-s-d4.

Thus all twelve demands hold. Each individual six-path family is a valid
bipartite scheme. The two different gates t and s prevent the proposed
unqualified combination.

## Excluding K7

Eliminate vertices in the following order, completing the remaining
neighbourhood to a clique before each deletion:

    e1,e2,f,q,s,d3,d4,d1,d2,p,u,v1,v2,a,b,t,x.

The respective remaining neighbourhoods are

    {f,p}, {f,p}, {d1,d2,p}, {d3,d4,x}, {d3,d4,x},
    {d1,d2,d4,u,x}, {d1,d2,u,x}, {d2,p,t,u,x}, {p,t,u,x},
    {a,b,t,u,x}, {a,b,t,x}, {a,b,t}, {a,b,t},
    {b,t,x}, {t,x}, {x}, {}.

All have order at most five, so this is a width-five tree-decomposition
certificate. Treewidth does not increase under taking minors, whereas K7
has treewidth six. Hence G has no K7 minor. This uses a displayed
certificate, not failure of a minor search.

## Unaffected scope and required repair

The graph is six-colourable, even with the same B and fixed D. Set

    u=x=5; p=f=q=6; a=1, b=2, t=3, s=1;
    v1=v2=4; e_i=d_i=i.

Consequently `G-({u} union B)` has a five-colouring avoiding five on
`{a,b}`. That is forbidden in the original critical host. The graph is
also has the four-vertex separator `{u,p,x,t}`, and B is not dominating.
The displayed pair is not asserted to minimise disagreement among all
opposite-owner pairs.

The first false inference is that the selected paths and their strongly
connected disagreement region suffice to construct the minor. A repair
must use further hypotheses, such as the whole fixed-B colouring relation
or the original host's connectivity and proper-minor colourings; their
sufficiency remains unproved. The
[technical frontier](../active/hc7_c21_rooted_density_construction.md#next-attack-the-split-clique-neighbourhood)
retains the full-host construction obligation.

Run the dependency-free certificate checker with

    uv run python3 active/hc7_two_colouring_region_verify.py

It checks the exact graph, both colourings, twelve paths, transition arcs,
elimination trace and displayed six-colouring. The finite conclusion is
only this explicit seventeen-vertex counterexample.
