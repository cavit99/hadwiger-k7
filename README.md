# Towards Hadwiger's conjecture

Research on graph colouring and graph minors, focused on the first open
case of Hadwiger's conjecture.

**[Read the main paper (PDF)](paper/k7minus-six-colour/main.pdf)** ·
[LaTeX source](paper/k7minus-six-colour/main.tex) ·
[All manuscripts](paper/README.md)

## The problem

A proper vertex colouring assigns colours so that adjacent vertices have
different colours. A **graph minor** is obtained by deleting vertices or
edges and contracting edges. The **complete graph** $K_t$ has $t$ vertices,
with an edge between every pair.

Hadwiger's conjecture says that every finite simple graph with no $K_t$
minor can be coloured with at most $t-1$ colours. The case studied here is:

> Can every graph with no $K_7$ minor be coloured with at most six colours?

The seven refers to the excluded complete graph; the graphs being coloured
may have any number of vertices. This case, abbreviated `HC7` or `HC_7`,
is not proved.

## Main result

Let $K_7^-$ be the complete graph on seven vertices with one edge deleted.
The principal manuscript, by Cavit Erginsoy, gives a proof of the following:

> Every finite simple graph with no $K_7^-$ minor is six-colourable.

This covers fewer graphs than the full conjecture: a graph may contain a
$K_7^-$ minor without containing a $K_7$ minor.

The proof uses rooted-minor and separation tools of
[Dvořák, Norin and Rahman](https://arxiv.org/abs/2609.17760v1).
It develops new minor constructions and an edge-count theorem, applying to
graphs of arbitrary size. The proof does not require a computer check.

The manuscript has separate internal proof reviews; external mathematical
review remains outstanding. See its [proof reviews and verification instructions](paper/k7minus-six-colour/README.md)
and the [research ledger](RESEARCH_LEDGER.md) for the exact status.

## Two further papers

- **[A matroid proof of bipartite contractibility](paper/bipartite-contractibility/main.pdf).**
  Shows how suitable systems of overlapping paths yield bipartite minors
  while retaining prescribed vertices. Gives an independent proof of an
  earlier assertion by Biswal, Lee and Rao, and a sharp distance bound for
  short paths.
- **[Paired clique minors from connected regions](paper/paired-clique-regions/main.pdf).**
  Gives sharp conditions for constructing a complete-graph minor whose
  connected parts each contain one vertex from each of two specified
  terminal sets.

These are independent specialist papers. The structural, even-subdivision
and complete-bipartite precursor drafts are preserved in the
[manuscript collection](paper/README.md).

## Finding your way around

| Resource | What to find there |
|---|---|
| [Research ledger](RESEARCH_LEDGER.md) | Authoritative current status, exact claims and review records |
| [Current research](active/INDEX.md) | Open questions and active proof work |
| [Supporting results](results/README.md) | Theorem statements, proofs and their internal audits |
| [Counterexamples](barriers/) | Constructions refuting proposed intermediate claims |
| [Archive](archive/) | Superseded drafts, failed approaches and research history |

## Working with the repository

Read [AGENTS.md](AGENTS.md) before contributing. Python experiments use
[uv](https://docs.astral.sh/uv/). To install the locked dependencies and
check the research records:

```sh
uv sync --locked
uv run python3 tools/research_index.py check
uv run python3 tools/research_index.py report
```

[Tool documentation](tools/README.md) covers searching the proof library,
checking dependencies and reproducing computations. Internal audits and
finite checks record their scope and the exact revisions they cover.

## Licence

[MIT](LICENSE).
