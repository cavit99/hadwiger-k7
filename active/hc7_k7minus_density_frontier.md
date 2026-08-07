# Closed density frontier for the `K_7^-` six-colour route

**Status:** closed by a written proof with a separate internal **GREEN**
audit.  Internal audit is not external peer review.  `HC_7` remains open.

The former detailed frontier remains available in the immutable pre-closure
revision
[`93079280`](https://github.com/cavit99/hadwiger-k7/blob/93079280ceedd5754105446e27bb76985ad8ffc0/active/hc7_k7minus_density_frontier.md).

## 1. Closed extremal target

The former sole active target was

\[
 \kappa(G)\ge7,
 \qquad |E(G)|\ge4|V(G)|-2
 \quad\Longrightarrow\quad K_7^-\preccurlyeq G.
\]

It is now proved in
[`../results/hc7_k7minus_exact_six_connectivity_closure.md`](../results/hc7_k7minus_exact_six_connectivity_closure.md),
with the adjacent audit
[`../results/hc7_k7minus_exact_six_connectivity_closure_audit.md`](../results/hc7_k7minus_exact_six_connectivity_closure_audit.md).

## 2. Exact proof spine

The decisive intermediate theorem is:

> Every graph `H` with
> \[
>                         \kappa(H)=6,
> \qquad |E(H)|\ge4|V(H)|-2
> \]
> contains `K_7^-` as a minor.

For a six-cut, target exclusion reduces the number of full complementary
components to two or three.

- The two-component boundary is forced to be `K_6-3K_2`; the three
  complementary rooted-four inequalities force total shore excess at most
  four, while density requires at least ten.
- The three-component boundary is forced to be cubic; summing over its
  twelve ordered nonedges forces total shore excess at most nine, while
  density requires at least thirteen.

The seven-connected result follows by contracting the audited density-safe
edge at a degree-seven vertex.  The quotient has connectivity at least six;
minimum order excludes connectivity at least seven, and the exact-six theorem
excludes connectivity six.

## 3. Consequence and scope

Together with the audited critical-host entrance, the theorem proves that
every `K_7^-`-minor-free graph is six-colourable.

It does not prove `HC_7`.  The remaining open upgrade is from the guaranteed
near-clique minor `K_7^-` to a complete `K_7` minor in a hypothetical
seven-contraction-critical host.  That is now the sole active target in the
[labelled missing-edge upgrade frontier](hc7_k7minus_to_k7_upgrade_frontier.md).

## 4. Verification

Run:

```bash
python3 results/hc7_k7minus_exact_six_connectivity_verify.py
```

The deterministic verifier exhausts all labelled six-vertex boundary graphs
and checks the finite classification and ordered-nonedge incidence sums.
