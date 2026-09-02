# Spanning and split-count normal forms for the literal `K_{4,4}` two-helper criterion

**Status.** Written unbounded corollary; the adjacent audit identifies the
exact checked revision.  This note exactly reformulates the existing
two-helper inequality.  It does not prove that a required partition exists
and does not prove the weighted splitter theorem, the literal case of T44,
T44, Conjecture 21, or `HC_7`.

## 1. Setting

Use the boundary normal form from the audited
[minimum-blocker theorem](hc7_k44_tight_boundary_and_minimum_blocker.md):

\[
 D=\{a,b\}\mathbin{\dot\cup}K,
 \qquad |K|=5,
 \qquad H=\{b\}\mathbin{\dot\cup}K.                \tag{1}
\]

Let `X` be the connected blocker.  Every member of `D` has a neighbour in
`X`.  For `R subseteq X`, let

\[
                 N_D(R)=\{d\in D:N_X(d)\cap R\ne\varnothing\}.  \tag{2}
\]

For disjoint sets `U,V subseteq X`, the two-helper defect at `h_0 in H` is

\[
 \begin{split}
 \delta_{h_0}(U,V)
  ={}&|H-(N_D(U)\cup\{b,h_0\})|\\
    &+|H-(N_D(V)\cup\{h_0\})|.                     \tag{3}
 \end{split}
\]

When `U,V` are nonempty and connected, an edge joins them, and
`a in N_D(U)`, the promoted two-helper lemma says that
`delta_{h_0}(U,V)<=1` produces an explicit `K_7^-` minor.

## 2. Unused vertices can be absorbed

### Lemma 2.1 (spanning extension)

Let `X` be connected, and let `U_0,V_0 subseteq X` be disjoint nonempty
connected sets with an edge between them.  There is a partition

\[
                         X=U\mathbin{\dot\cup}V      \tag{4}
\]

into connected sets such that `U_0 subseteq U` and `V_0 subseteq V`.
Moreover, for every `h_0 in H`,

\[
                    \delta_{h_0}(U,V)
                       \le \delta_{h_0}(U_0,V_0).    \tag{5}
\]

#### Proof

Every component of `X-(U_0 union V_0)` has an edge to `U_0 union V_0`:
different components of that deletion have no edge between them, and `X` is
connected.  Assign each component whole to a side that it meets.  Each
enlarged side remains connected, the original edge keeps the sides adjacent,
and together they partition `X`.  Enlarging a helper can only enlarge its
set of represented boundary resources, which proves (5).  \(\square\)

Thus there is no loss of generality in seeking a spanning connected
partition for the two-helper criterion, even though its original statement
does not require one.

## 3. Exact split count

For an ordered partition (4), define

\[
 s(U,V)=\left|\left\{k\in K:
       N_X(k)\cap U\ne\varnothing\ne N_X(k)\cap V
                         \right\}\right|            \tag{6}
\]

and

\[
 \varepsilon_b(U,V)=
 \begin{cases}
  1,&N_X(b)\cap V=\varnothing,\\
  0,&N_X(b)\cap V\ne\varnothing.
 \end{cases}                                         \tag{7}
\]

### Theorem 3.1 (split-count identity)

For every ordered spanning partition (4),

\[
 \min_{h_0\in H}\delta_{h_0}(U,V)
    =\max\{0,\,4-s(U,V)+\varepsilon_b(U,V)\}.        \tag{8}
\]

Consequently, if `U,V` are connected, adjacent, and `a in N_D(U)`, then the
numerical hypothesis of the two-helper lemma holds for some `h_0 in H` if
and only if

\[
                    s(U,V)\ge3+\varepsilon_b(U,V).   \tag{9}
\]

Equivalently:

1. if `V` sees `b`, at least three of the five `K`-supports must split; and
2. if `V` misses `b`, at least four of the five `K`-supports must split.

#### Proof

Put

\[
 F_U=K-N_D(U),
 \qquad
 F_V=(K-N_D(V))\cup
 \begin{cases}
  \{b\},&\varepsilon_b(U,V)=1,\\
  \varnothing,&\varepsilon_b(U,V)=0.
 \end{cases}                                         \tag{10}
\]

Every `K`-resource has a neighbour in `X=U dotcup V`.  It therefore lies in
both represented sets, contributing nothing to `F_U union F_V`, exactly
when its support splits.  Otherwise it lies in exactly one of `F_U,F_V`.
Thus these two sets are disjoint and

\[
                         |F_U|+|F_V|
                            =5-s(U,V)+\varepsilon_b(U,V). \tag{11}
\]

The expression in (3) is

\[
                         |F_U-\{h_0\}|+|F_V-\{h_0\}|. \tag{12}
\]

If (11) is positive, choose `h_0` to be a resource counted there; since the
sets are disjoint, this deletes exactly one contribution.  If it is zero,
the minimum is already zero.  This proves (8), and (9) follows by asking
when its right side is at most one.  \(\square\)

The equivalence in Theorem 3.1 is with the numerical hypothesis of the
two-helper lemma, not with the existence of a `K_7^-` minor.  That lemma
remains a sufficient minor construction.

## 4. The anchored three-support condition

Suppose the distinguished vertex `p` supplied by the minimum-blocker theorem
is placed in `U`, some vertex of `N_X(b)-\{p\}` is placed in `V`, and at least
three `K`-supports split.  Then `U` sees `a`, `V` sees `b`, and (9) holds.
This is a useful sufficient subcase.

It is not equivalent to the full two-helper criterion.  It prescribes the
particular vertex `p` and omits the second exact mode in which `V` misses
`b` but four `K`-supports split.
