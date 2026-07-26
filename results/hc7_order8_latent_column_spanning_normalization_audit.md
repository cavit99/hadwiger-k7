# Independent audit of the eight-latent-column spanning normalization

## Verdict

**GREEN** at the exact mathematical source revision

```text
507c3a11309cf7ce50db05dd9e42e011604323ab658a18a04594a5461cdf3c2a  results/hc7_order8_latent_column_spanning_normalization.md
bb78ac1cc61c501a5f871ab9b69a402f765ee333dabe0c9deeff5805bc94a323  results/hc7_order8_dual_free_root_response_star.md
```

The final source hash is

```text
da16de3ea6868291038f14b83f4cf75b2d783ebfbd5de2240ded7864286760a5  results/hc7_order8_latent_column_spanning_normalization.md
```

The only subsequent source change was replacing the pending-audit status
with the link to this audit; no theorem or proof content changed.  This is a
separate internal audit, not external peer review.

## 1. Seed preservation and minor lifting

For a consumed label `r`, the original roots lie inside
`{v,w} union K_r` and are therefore disjoint from every enlarged surviving
column.  Their original first-edge contacts to all seven surviving labels
remain.  Thus a `K_5` model in `Khat-r` lifts with those two roots exactly as
claimed; extra vertices of the consumed enlarged column may remain unused.

## 2. Spanning proof

For an outside component `Z`, absence of every column attachment would give
`N(Z) subseteq {v,w}`, contradicting seven-connectivity.  If its attachment
labels are not a clique, an internal `Z`-path between two noncontacting
columns adds a contact without a loss.  If they form a clique, absorbing all
of `Z` into any attached column adds coverage without changing the contact
set.  These are exhaustive and prove coverage of `G-{v,w}`.

## 3. Free-root conversion

In the original core system,

\[
 (R_C^r\cup R_D^r)-\{v,w\}=K_r.
\]

Both relevant endpoint labels are response labels rather than the two free
labels, and every selected bypass avoids `v`.  Changing the consumed free
label therefore turns a first root hit away from `w` into a hit on the
restored latent column.  The enlargement qualification is necessary and is
stated correctly: a newly added vertex of that restored column may occur
earlier, so the conclusion becomes “at or before,” not preservation of the
same first vertex.

The result does not preserve low contact degree under the free-root switch,
move an original fan-tail vertex, or prove a dirty-path exchange.  Its trust
boundary is accurate.
