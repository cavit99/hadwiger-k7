# A two-component quotient does not by itself complete the literal core

**Status.** Barrier/counterexample to the quotient-only completion claim
stated below; exact finite verification by the adjacent dependency-free
script.  This graph is not a counterexample to the audited two-component
support normal form, its open completion lemma, the literal `K_{4,4}` case
of T44, T44, Conjecture 21, or `HC_7`.

## 1. The refuted claim

The following natural local claim is false.

> **Quotient-only completion claim.**  Let seven vertices
> `a,b,k_0,k_1,k_2,k_3,k_4` occupy distinct vertices of a literal
> `K_{4,4}`, with `a,b` on opposite shores, and let `f` be its unused
> vertex.  Add vertices `P,Q,t_0,t_1,t_2` so that
> `{P,Q}` and `{t_0,t_1,t_2}` induce a `K_{2,3}`.  Suppose `k_0,k_1`
> are adjacent to both `P,Q`, `k_2` is adjacent to `P`, and `k_3,k_4`
> are adjacent to `Q`.  Suppose also that each of `a,b` has a neighbour
> among these five new vertices and that `P` is adjacent to at least one
> of `a,b`.  Then the resulting forced quotient contacts contain a
> `K_7^-` minor.

These are the mandatory contacts obtained by contracting the two components
of a surviving three-cut to `P,Q`: two of the five supports meet both
components, and the other three are contained in the components with a
`1+2` distribution.  The last condition is the distinguished-support
incidence forced on the component meeting only three of the five supports.

## 2. Counterexample

Let `H` have vertex set

```text
{a,b,k0,k1,k2,k3,k4,f,P,Q,t0,t1,t2}.
```

Its edges are exactly the following:

1. all sixteen edges of the literal `K_{4,4}` with shores

   ```text
   {a,k0,k1,f} and {b,k2,k3,k4};
   ```
2. the six edges from each of `P,Q` to each of `t0,t1,t2`;
3. the five edges from `P` to `a,b,k0,k1,k2`; and
4. the four edges from `Q` to `k0,k1,k3,k4`.

Thus `H` has thirteen vertices and thirty-one edges.  It satisfies every
incidence in the quotient-only claim: `k0,k1` are the two supports meeting
both components, `k2` is the component-contained support on the `P` side,
`k3,k4` are the two on the `Q` side, and both distinguished roots `a,b`
meet `P`.  Nevertheless the maximum number of contacts among seven
disjoint connected branch sets in `H` is nineteen.  Hence `H` has no
`K_7^-` minor.

At the five-vertex quotient level, put

```text
R_k0=R_k1={P,Q},  R_k2={P},  R_k3=R_k4={Q}.
```

Every one of the eleven bonds of `K_{2,3}` splits at most the two supports
`R_k0,R_k1`.  Thus changing only the allocation of the three cut vertices
between the two component bags cannot repair the missing twentieth contact.

## 3. Exact verification and trust boundary

Run

```text
python3 barriers/hc7_k44_two_component_quotient_completion_barrier_verify.py
```

The expected output is

```text
PASS vertices=13 edges=31 exact_minor_optimum=19
PASS canonical_states=1586222
PASS skeleton_bonds=11 maximum_split_supports=2
NOTE local contracted quotient only; q>=6 and support multiplicity fail
```

The verifier starts with the thirteen singleton parts.  At every step it
either deletes a current part or contracts two parts joined by an edge, and
it exhausts all canonical states until seven parts remain.  Every part is
therefore connected.  Conversely, every seven-branch-set minor model is
reached by first deleting its unused vertices and then contracting a
spanning tree in each connected branch set.  Counting quotient contacts at
the leaves therefore computes the exact optimum, rather than a heuristic
or a lower bound.  The only computational trust assumptions are the Python
interpreter and the short explicit enumeration.  No SMT solver or external
package is used.

## 4. Exact scope and the missing global information

The counterexample is deliberately only a contracted quotient.  It fails
three hypotheses retained by the live unbounded problem.

1. The component-contained quotient supports `R_k2,R_k3,R_k4` have order
   one, rather than order at least two.
2. Each `t_i` has

   ```text
   |N(t_i)| + |{k:R_k meets {t_i}}| = 2,
   ```
   so the six-boundary inequality `q(W)>=6` fails sharply.
3. It has no proper support-full induced-path bond side.  Any induced path
   meeting all five quotient supports must contain `P,Q`.  If it contains
   one cut vertex it is `P-t_i-Q`, whose complementary two cut vertices are
   disconnected; if it contains at least two cut vertices, its induced
   subgraph is not a path.

Consequently this barrier rules out only an argument which contracts each
component immediately and then uses the mandatory root incidences.  A valid
completion must exploit uncontracted structure forced by `q>=6` and support
multiplicity, or the sequential minimum support-full path and its attachment
bounds.  The obstruction identifies the sharp local incidence to overcome:
the component meeting three `K`-supports contains both distinguished
supports, the component meeting four contains neither, and no boundary
support meets the three-cut.
