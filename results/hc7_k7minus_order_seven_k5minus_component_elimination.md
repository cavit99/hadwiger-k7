# A five-vertex `K_5^-` component behind an order-seven cut is terminal

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_order_seven_k5minus_component_elimination_audit.md`](hc7_k7minus_order_seven_k5minus_component_elimination_audit.md).

This result treats the sharp five-vertex component that can arise from a
two-cut after five independent degree-eight vertices are deleted.  Its
conclusion is an explicit `K_7^-` minor; no colouring synchronization or
finite enumeration is used.

## 1. The component theorem

### Theorem 1.1

Let `G` be a seven-connected graph with minimum degree at least eight and
with no `K_5` subgraph.  Let `S` be a vertex cut of order seven, and let
`C,D` be distinct components of `G-S`.  If

\[
                         |C|=5
       \qquad\hbox{and}\qquad G[C]\cong K_5^-,          \tag{1.1}
\]

then `G` contains `K_7^-` as a minor.

#### Proof

Write `a,b` for the unique nonadjacent pair of `G[C]`.  Thus `a,b` have
degree three in `G[C]`, while the other three vertices of `C` have degree
four there.

For `v in C`, put

\[
                         P(v)=N_G(v)\cap S.              \tag{1.2}
\]

Since `C` is a component of `G-S`, every neighbour of `v` outside `C`
lies in `S`.  Minimum degree therefore gives

\[
                 |P(a)|,|P(b)|\ge5,
       \qquad |P(v)|\ge4\quad(v\in C-\{a,b\}).          \tag{1.3}
\]

Consequently,

\[
                         |E_G(C,S)|\ge22.                \tag{1.4}
\]

No vertex of `S` has five neighbours in `C`: such a vertex together with
either of the two literal `K_4` subgraphs of `G[C]` would form a literal
`K_5` in `G`.  Hence

\[
                         |N_C(x)|\le4\qquad(x\in S).     \tag{1.5}
\]

Equations (1.4)-(1.5) and `|S|=7` yield a vertex `t in S` with

\[
                         |N_C(t)|=4.                    \tag{1.6}
\]

Let `w` be the unique vertex of `C` not adjacent to `t`.

The two sets `P(a),P(b)` have order at least five inside the seven-set
`S`, so their intersection has order at least three.  Choose

\[
                         s\in P(a)\cap P(b)-\{t\}.       \tag{1.7}
\]

We next match the four vertices of `C-{a}` into `S-{s,t}` using actual
edges of `G`.  Let `X` be a nonempty subset of `C-{a}`.  The open
neighbourhood of `X` is the disjoint union

\[
                         N_G(X)=N_C(X)\mathbin{\dot\cup}N_S(X). \tag{1.8}
\]

It separates `X` from the nonempty component `D`; seven-connectivity gives
`|N_G(X)|>=7`.  Since

\[
                         |N_C(X)|\le5-|X|,               \tag{1.9}
\]

we obtain

\[
                         |N_S(X)|\ge|X|+2.               \tag{1.10}
\]

Deleting `s,t` from this neighbourhood leaves at least `|X|` vertices.
Hall's theorem therefore gives an injection

\[
 f:C-\{a\}\longrightarrow S-\{s,t\}
       \qquad\hbox{such that}\qquad vf(v)\in E(G)       \tag{1.11}
\]

for every `v in C-{a}`.  Extend it by setting

\[
                         f(a)=s.                         \tag{1.12}
\]

This remains injective, and `af(a)` is an edge by (1.7).

For every `v in C`, define

\[
                         B_v=\{v,f(v)\},                 \tag{1.13}
\]

and define `B_t={t}`.  These six branch sets are nonempty, connected, and
pairwise disjoint.  The five sets `B_v`, `v in C`, are pairwise adjacent.
Every adjacency except possibly `B_aB_b` follows from the corresponding
edge of `G[C]`; the remaining adjacency is supplied by the edge

\[
                         f(a)b=sb,                       \tag{1.14}
\]

again using (1.7).  The singleton `B_t` is adjacent to `B_v` for every
`v\ne w` through the edge `tv`.  Thus

\[
                         B_t,\quad (B_v:v\in C)          \tag{1.15}
\]

form a `K_6^-` minor model, with only `B_tB_w` possibly nonadjacent.

Finally, seven-connectivity gives

\[
                         N_G(D)=S.                       \tag{1.16}
\]

Indeed, a proper subset of `S` containing `N_G(D)` would be a cut of order
at most six separating `D` from `C`.  Since `f(C)` has order five and is
disjoint from `{t}`, let \(u\) be the unique vertex of
\(S-(f(C)\cup\{t\})\).  The branch set

\[
                         B_D=V(D)\cup\{u\}              \tag{1.17}
\]

is connected because `D` has a neighbour at `u`.  It is disjoint from the
six earlier bags.  It is adjacent to `B_t` through an edge from `D` to `t`
and to every `B_v` through an edge from `D` to the distinct boundary
vertex `f(v)`.  The seven branch sets

\[
                         B_D,B_t,(B_v:v\in C)            \tag{1.18}
\]

are pairwise disjoint and have every pairwise adjacency except possibly
`B_tB_w`.  They form an explicit `K_7^-` minor model.  \(\square\)

## 2. Application to the five-centre two-cut

Let `Z` be an independent set of five vertices, put `F=G-Z`, and suppose
that `{p,q}` is a two-cut of `F` with two complementary components.  Then

\[
                         S=Z\cup\{p,q\}                  \tag{2.1}
\]

is an order-seven cut of `G`.

In the live minor-minimal seven-chromatic host, the audited
[critical seven-cut capacity theorem](hc7_k7minus_critical_seven_cut_capacity.md),
Theorem 3(2), says that `G[S]` has an edge.  If `pq` is absent, independence
of `Z` therefore forces at least one centre-pole edge.  In particular, the
earlier conditional setup in which `pq` and every centre-pole edge were all
absent cannot occur in that host.

If one component of `G-S` has order five and induces `K_5^-`, Theorem 1.1
is already terminal.  In the sharp equality case, the boundary-degree
sequence `5,5,4,4,4` is exactly the lower-bound sequence in (1.3).  The
proof above uses the full live boundary and the opposite component
directly; it does not need to prescribe which centre-pole edge exists.

## 3. Scope

The theorem eliminates the five-vertex `K_5^-` component, not the entire
two-cut branch.  It does not prove that an arbitrary component behind the
two-cut has order five or induces `K_5^-`, and it makes no assertion about
larger strict-inequality components.  Those are separate cases of the
five-centre two-cut reduction.
