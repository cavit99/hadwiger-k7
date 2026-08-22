#!/usr/bin/env python3
"""Independent exhaustive check of the C5 (2,3)-support arc lemma."""

from itertools import combinations


def cyclic_three_interval_partitions():
    out = set()
    for cuts in combinations(range(5), 3):
        adjacency = {v: {(v - 1) % 5, (v + 1) % 5} for v in range(5)}
        for v in cuts:
            w = (v + 1) % 5
            adjacency[v].remove(w)
            adjacency[w].remove(v)
        seen = set()
        parts = []
        for start in range(5):
            if start in seen:
                continue
            todo = [start]
            seen.add(start)
            mask = 0
            while todo:
                v = todo.pop()
                mask |= 1 << v
                for w in adjacency[v]:
                    if w not in seen:
                        seen.add(w)
                        todo.append(w)
            parts.append(mask)
        assert len(parts) == 3
        out.add(tuple(sorted(parts)))
    return tuple(sorted(out))


def main():
    partitions = cyclic_three_interval_partitions()
    assert len(partitions) == 10
    eligible = 0
    zero_defect = 0
    one_defect = 0
    failures = []
    for a in range(1 << 5):
        for b in range(1 << 5):
            if a.bit_count() < 2 or b.bit_count() < 2:
                continue
            if max(a.bit_count(), b.bit_count()) < 3:
                continue
            eligible += 1
            defect = min(
                sum(not (a & part) for part in partition)
                + sum(not (b & part) for part in partition)
                for partition in partitions
            )
            if defect == 0:
                zero_defect += 1
            elif defect == 1:
                one_defect += 1
            else:
                failures.append((a, b, defect))
    assert eligible == 576
    assert not failures
    assert zero_defect + one_defect == eligible
    print("cyclic_partitions", len(partitions))
    print("eligible_ordered_pairs", eligible)
    print("zero_defect", zero_defect)
    print("one_defect", one_defect)
    print("failures", len(failures))
    print("GREEN")


if __name__ == "__main__":
    main()
