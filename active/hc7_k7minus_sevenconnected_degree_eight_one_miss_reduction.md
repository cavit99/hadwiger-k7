# Four residues for a connected one-miss exterior

**Status:** computer-assisted unbounded reduction, pending independent
audit.  It treats the connected exterior which misses one local vertex; it
does not treat a full exterior or eliminate the four displayed residues.

## Theorem

Let `G` be seven-connected and have no `K_7^-` minor.  Let `v` have degree
eight, put `J=G[N(v)]`, and suppose

\[
 \delta(J)\ge3,\qquad K_4\not\subseteq J,\qquad \alpha(J)=3.
\]

Suppose `G-N[v]` is a connected nonempty graph `C` and

\[
                         N_G(C)=V(J)-\{r\}.           \tag{1}
\]

Then, up to isomorphism of the pair `(J,r)`, one of the following holds:

```text
(GhCKN{,7), (GhEJE{,7), (GjSKN[,7), (GhEMNw,7).
```

## Proof

Contract `C` to one vertex.  The resulting quotient is among the exact
one-component profiles in the degree-eight census.  Since `r` has no
exterior neighbour,

\[
                 7\le d_G(r)=1+d_J(r),
\]

and hence `d_J(r)\ge6`.  Exactly thirteen target-free quotient profiles
meet this necessary condition.

In every one of the thirteen profiles, some vertex of `N_G(C)` has local
degree three.  Minimum degree seven makes it adjacent to at least three
distinct vertices of `C`, so `|C|\ge3`.

Put `S=N_G(C)`, which has order seven.  For every four-set `Z\subseteq S`,
the closed-shore rooted-connectivity lemma makes `(G[C\cup Z],Z)` internally
four-connected.  Jorgensen's theorem therefore gives a `Z`-rooted
`K_4^-` model.  Its possible missing adjacency is one of the nonedges of
`J[Z]`, since a literal root edge joins the corresponding bags.

For nine of the thirteen profiles, the verifier supplies a four-set `Z`
such that completing `J[Z]` except for any one of its nonedges gives a
`K_7^-` model together with the centre.  Replacing each completed root by
its rooted branch set lifts that model to `G`, a contradiction.  Canonical
choices of `Z` are

| profile | `Z` |
|---|---|
| `(G_{PNk,7)` | `0,1,2,5` |
| `(Gh_gns,7)` | `0,1,3,6` |
| `(Gh_gn{,7)` | `0,1,3,6` |
| ``(GMo`M{,7)`` | `0,3,5,6` |
| `(GhEKf[,7)` | `1,2,4,5` |
| `(GhEKf{,7)` | `1,2,4,5` |
| `(GGEF~w,6)` | `0,1,2,3` |
| `(GGEF~w,7)` | `0,1,2,3` |
| `(GBZENw,7)` | `0,2,3,5` |

The four pairs in the statement are exactly those left. `\square`

## Reproduction and scope

Run

```text
UV_CACHE_DIR=/tmp/uv-cache uv run python \
  active/experiments/sevenconnected_connected_exterior_profiles/verify.py
```

The verifier uses exact connected-bag minor testing.  It also checks that
none of the four residues is eliminated by any four-root completion of
this form.  That negative statement marks the limit of this reduction; it
is not evidence that the four profiles occur in a seven-connected
target-free host.
