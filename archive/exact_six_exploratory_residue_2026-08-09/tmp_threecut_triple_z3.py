from itertools import combinations
from z3 import And, Bool, If, Not, Or, Solver, Sum, sat

HN = 9
S = range(3)
C = range(3, 6)
D = range(6, 9)
W = set(C)

hedges = set()
for block in (S, C, D):
    for a, b in combinations(block, 2):
        hedges.add((a, b))
for s in S:
    for x in tuple(C) + tuple(D):
        hedges.add(tuple(sorted((s, x))))

hadj = [0] * HN
for a, b in hedges:
    hadj[a] |= 1 << b
    hadj[b] |= 1 << a


def connected(mask):
    if not mask:
        return False
    seen = mask & -mask
    todo = seen
    while todo:
        bit = todo & -todo
        todo ^= bit
        v = bit.bit_length() - 1
        add = hadj[v] & mask & ~seen
        seen |= add
        todo |= add
    return seen == mask


all_h = (1 << HN) - 1
partitions = []
split_partitions = []
for left in range(1, all_h):
    right = all_h ^ left
    if left > right or not connected(left) or not connected(right):
        continue
    partitions.append((left, right))
    wc = sum(bool(left & (1 << w)) for w in W)
    if 0 < wc < 3:
        split_partitions.append((left, right))

edge = [[Bool(f"e_{r}_{h}") for h in range(HN)] for r in range(4)]
solver = Solver()

# Minimum degree in the prospective six-connected graph.
for h in range(HN):
    solver.add(Sum([If(edge[r][h], 1, 0) for r in range(4)]) >= 6 - len([x for x in range(HN) if hadj[h] >> x & 1]))
for r in range(4):
    solver.add(Sum([If(edge[r][h], 1, 0) for h in range(HN)]) >= (4 if r < 2 else 3))

def root_crosses(r, left, right):
    return And(Or([edge[r][h] for h in range(HN) if left >> h & 1]),
               Or([edge[r][h] for h in range(HN) if right >> h & 1]))

# Some unmarked rooted model exists, but none splits the three marks.
solver.add(Or([And([root_crosses(r, a, b) for r in range(4)]) for a, b in partitions]))
for a, b in split_partitions:
    solver.add(Not(And([root_crosses(r, a, b) for r in range(4)])))

print("partitions", len(partitions), "split", len(split_partitions))
if solver.check() != sat:
    print("UNSAT")
else:
    model = solver.model()
    masks = []
    for r in range(4):
        mask = sum(1 << h for h in range(HN) if model.eval(edge[r][h], model_completion=True))
        masks.append(mask)
    print("SAT", masks)
