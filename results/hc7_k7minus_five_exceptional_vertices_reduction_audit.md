# Internal audit: five exceptional degree-eight vertices

**Verdict:** GREEN.

**Audited theorem SHA-256:**
`3ebcbaf595b16d616dcd01efdc2e8dd23f0ed6079a3294e8299f7b365787483b`.

This is a separate internal mathematical audit, not external peer review.

## Extremal input

Jakobsen's theorem, quoted as Theorem 2 in Albar,
*Coloration of `K_7^-`-minor free graphs* (arXiv:1402.2806), says that an
`n`-vertex graph with at least `(9/2)n-12` edges contains a `K_7^-` minor or
is a `(K_{2,2,2,2},K_6,4)`-cockade.  A nontrivial cockade has a four-cut;
the base graphs are at most six-chromatic.  Thus the present host is not an
exception and

\[
                              2m\le9n-25.
\]

With minimum degree seven,

\[
 9n-2m=2n_7+n_8-\sum_{i\ge10}(i-9)n_i,
\]

so `2n_7+n_8>=25` is correct.

## Count and exceptional set

The audited input revisions are:

| result | SHA-256 |
|---|---|
| degree-seven clique incidence | `8378b1920987284abf3ff33d476d28efee5c9a13659afe7a192febaacb3d501f` |
| at most two literal `K_5` subgraphs | `5b5e399122b996186e861f5075e7808c8e6fe4353082256ee12d5074499d2574` |

Seven-chromaticity makes the graph non-two-apex.  Hence all degree-seven
vertices and all nonbad degree-eight vertices lie in the union of at most
two five-cliques, a set of order at most ten.  If `b` is the bad count,

\[
 n_7+n_8-b\le10,
 \qquad
 b\ge n_7+n_8-10\ge15-n_7\ge5.
\]

The last inequality uses `n_7<=10`.  Five bad vertices cannot form a clique,
because each would then lie in that literal `K_5`; therefore two are
nonadjacent.

## Finishing theorem and trust boundary

The exact sufficient finishing statement is that at most four exceptional
degree-eight vertices occur.  This is contradicted directly by the proved
lower bound `b>=5`.  Excluding every nonadjacent exceptional pair is
stronger, and producing five pairwise adjacent bags meeting both root
neighbourhoods is stronger again.  The theorem does not assert either pair
statement.  The adjacent barrier explicitly rules out deriving the paired
model from ordinary seven-path linkage alone.
