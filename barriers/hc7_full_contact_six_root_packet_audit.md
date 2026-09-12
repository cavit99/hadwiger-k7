# Audit of the full-contact six-root packet barrier

**Verdict: GREEN.**

Date: 12 September 2026. Source:
`barriers/hc7_full_contact_six_root_packet.md`, SHA-256
`8c350bb8d9e537b74a719f931953a7d090c9938a9a8c320e0934a46fae184fae`.

The graph has seventeen vertices. Its stated degrees, singleton R-contact
sets and full six-root neighbourhood of C follow directly from the edge
list. The boundary calculation exhausts all nonempty C-subsets according
to membership of w and the two clique counts. The bound on distinct
B-to-R labels is valid for every selected subset; the repeated label r0
is the only possible duplication. In particular `N(B)={w} union R`
has size five. No relative-six claim is accepted.

The rooted obstruction allows arbitrary connected branch sets. Between
the two root pairs `{p,q}` and `{r2,r3}`, every Q6 retains a perfect
matching. Its two contacts expand to vertex-disjoint paths in four
distinct owning bags, avoiding the other roots r0,r1. After those two
vertices are deleted, every such path must pass through w. This is a
contradiction independent of unused vertices or root-bag expansion.

The construction contains the literal K7 on `A union {p,q}`, so it is
neither Q7-free nor free of literal K5-minus. Moreover B has only the
single non-R packet neighbour w; restoring two omitted cut vertices
gives at most three neighbours in the actual complement F. It therefore
cannot occur as that side of a four-connected F. The barrier refutes
exactly the stated full-contact/proper-five intermediate assertion, not
the relative-six packet target or the actual critical-host construction.

This is separate internal review of Franklin's construction. The reviewer
participated in the surrounding packet investigation but did not author
this example. No finite computation or external peer review is a premise;
no C19, HC7 or NT-comparable conclusion follows.
