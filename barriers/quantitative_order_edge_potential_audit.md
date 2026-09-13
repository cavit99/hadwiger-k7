# Independent audit: order and edge potential obstruction

**Status:** separate internal mathematical audit, 13 September 2026.
This is not external peer review or a claim of comparative significance.

**Verdict: GREEN** for the stated integer scalar construction and both
failures of numerical inference. No unresolved gap was found within that
scope. No graph realisation, failure of reduction R, or improved colouring
theorem follows. The HC7 or independently substantiated NT-comparable
completion criterion remains unmet.

## Exact source and scope

- [Audited source](quantitative_order_edge_potential.md).
- Whole-file SHA-256:
  `c975fa3900f8350518baf957304467282525cf2e23cb8c531102e72810fd016b`.
- Checked independently: the integer recurrence; uniform positivity and
  order and edge capacities; density and loss inequalities; failure of
  both the fixed-constant cubic bound and the first-step order reduction.

The transition inequalities are checked for `p=q,...,2r+1`; the terminal
order and edge counts are at level `2r`. All asymptotic assertions concern
sufficiently large integer r, as stipulated in the source.

## Rounding and the uniform lower bound

The recurrence preserves even integer orders, and therefore
`m_p=n_p(p-r+1/2)` is an integer. Writing the rounding error at a step as
`epsilon_p` gives

`n_(p-1)=n_p(1-p/r^2)-epsilon_p`, with `0<=epsilon_p<2`.

All multipliers lie in `(0,1]`. On expanding the recurrence, every error
is multiplied by a product at most one; replacing their sum by `2(q-p)`
therefore gives the stated lower bound. This does not assume that the
intermediate orders are positive.

For sufficiently large r all `j/r^2<=1/2`, and summing
`log(1-j/r^2)>=-2j/r^2` proves the product estimate uniformly in p.
Since `q(q+1)/r^2=(log r)/4+o(1)`, its use as the lower bound
`r^(-1/4-o(1))` is valid. The resulting positive term is
`r^(5/4-o(1))`, while `2q=O(r sqrt(log r))` is smaller by a factor
tending to zero. Hence every order is positive and much larger than
`2q`. Positivity then makes the recurrence decreasing, proving the upper
order bound as well. The capacity condition reduces exactly to
`n_p>=2p-2r+2`, which this same lower bound supplies. The edge counts are
positive and meet the required density bound at equality.

## Loss inequalities and asymptotic separation

The first loss follows directly from
`D_p>=n_p p/r^2>=n_p(p-r+1/2)/r^2`. For the second, independent expansion
gives `m_p-m_(p-1)=n_p+D_p(p-r-1/2)`. The coefficient is positive.
Substitution and subtraction of `m_p/r` produce exactly the source's
bracket `p^2-2pr+2r^2-(p+r)/2`. Its derivative in p is positive on
`p>=2r`; its value at `2r` is `2r^2-3r/2>0`.

Finally, `q/r~sqrt(log r)/2` and `n_q~r^(3/2)`. The cubic expression has
order `(log r)^(3/2)`, exceeding every fixed affine function of
`log(n_q/r)~(log r)/2`. In the first-step ratio the rounding contribution
is asymptotic to `8/(sqrt(r) log r)`, while `r/q~2/sqrt(log r)`; both
vanish. Integer rounding therefore cannot restore either proposed bound.

## Limits of the verdict

The sequences certify integer scalar inequalities only. In particular,
the audit does not infer independent star packings, compatible minor
models, chromatic criticality, or the all-minor independence hypothesis
from them. Those additional graph constraints may exclude the sequences.
The [quantitative frontier](../active/quantitative_star_contraction_frontier.md)
correctly retains R and its colouring consequence as unproved.
The checks above are written arguments; no finite computation is a premise.
