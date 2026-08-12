# Nine-terminal protected-centre kernel screen

This discovery screen protects the seven common neighbours `Q` and both
ends `w,y` of one further exceptional-centre matching edge in the
five-connected graph `H=G-{u,v}`.
The terminal-legal kernel theorem leaves at most two nonterminal vertices.

The first screen treats the order-nine base: every edge-minimal
three-connected graph on the nine terminals, every placement of the seven
labelled vertices of each surviving graph `Q`, and the two remaining
protected roots.  It adds the literal edges of `Q` and the protected edge
`wy`, and asks for a
`K5-minus` model every branch set of which meets `Q`.  The test is an exact
root-sensitive deletion/contraction recursion; the two protected-centre
bags may be deleted or absorbed, but no `Q`-root can disappear.

This is a finite discovery diagnostic until its generator and composition
receive an independent audit and an unbounded kernel lift is written.

Run:

```text
python3 active/experiments/dominated_singleton_nine_terminal_exact_kernel/screen_order9.py
```
