#!/usr/bin/env python3
"""Exploratory LP upper bounds for the remaining seven-edge boundaries."""

from importlib.util import module_from_spec, spec_from_file_location
from fractions import Fraction
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VERIFY = ROOT / "active" / "hc7_k7minus_returned_three_component_dense_boundary_elimination_verify.py"
SPEC = spec_from_file_location("boundary_verify", VERIFY)
assert SPEC and SPEC.loader
TOOLS = module_from_spec(SPEC)
SPEC.loader.exec_module(TOOLS)


def allowed_pairs(edges):
    degree = TOOLS.degrees(edges)
    answer = set()
    for p, q in TOOLS.PAIRS:
        edge = (p, q)
        roots = set(TOOLS.VERTICES) - {p, q}
        if edge not in edges and max(degree[p], degree[q]) == 3:
            answer.add(edge)
        if edge in edges and all(
            tuple(sorted((p, z))) in edges or tuple(sorted((q, z))) in edges
            for z in roots
        ):
            answer.add(edge)
    return sorted(answer)


def lp_bound(edges, c):
    # Variables are e,a_0,...,a_5.  Constraints are A x <= b.
    constraints = []
    row = [Fraction(0)] * 7; row[0] = -1
    constraints.append((row, -(c - 1), "connected"))
    row = [Fraction(0)] * 7; row[0] = 1
    constraints.append((row, Fraction(c * (c - 1), 2), "simple"))
    row = [Fraction(0)] * 7; row[0] = -2; row[1:] = [-1] * 6
    constraints.append((row, -6 * c, "degree"))
    for i in range(6):
        row = [Fraction(0)] * 7; row[1 + i] = -1
        constraints.append((row, -1, f"full-{i}"))
        row = [Fraction(0)] * 7; row[1 + i] = 1
        constraints.append((row, c, f"simple-attachment-{i}"))
    for p, q in allowed_pairs(edges):
        roots = frozenset(TOOLS.VERTICES) - frozenset((p, q))
        row = [Fraction(1)] * 7; row[1 + p] = 0; row[1 + q] = 0
        constant = 3 * c + 5 - TOOLS.induced_size(edges, roots)
        constraints.append((row, constant, f"root-{p}{q}"))

    objective = [Fraction(1)] * 7

    def solve(matrix, vector):
        augmented = [list(row) + [value] for row, value in zip(matrix, vector)]
        for column in range(7):
            pivot = next((r for r in range(column, 7) if augmented[r][column]), None)
            if pivot is None:
                return None
            augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
            scale = augmented[column][column]
            augmented[column] = [value / scale for value in augmented[column]]
            for r in range(7):
                if r == column or not augmented[r][column]:
                    continue
                scale = augmented[r][column]
                augmented[r] = [
                    left - scale * right
                    for left, right in zip(augmented[r], augmented[column])
                ]
        return [augmented[r][-1] for r in range(7)]

    def dot(left, right):
        return sum((x * y for x, y in zip(left, right)), Fraction(0))
    best = None
    witness = None
    for chosen in combinations(range(len(constraints)), 7):
        matrix = [constraints[i][0] for i in chosen]
        vector = [constraints[i][1] for i in chosen]
        point = solve(matrix, vector)
        if point is None:
            continue
        if any(dot(row, point) > bound for row, bound, _ in constraints):
            continue
        value = dot(objective, point) - 4 * c
        if best is None or value > best:
            best = value
            witness = (point, [constraints[i][2] for i in chosen])
    return best, witness


def main():
    _, all_classes = TOOLS.boundary_classes(7)
    _, dense_classes = TOOLS.boundary_classes(7, 3)
    remaining = [frozenset(key) for key in all_classes if key not in dense_classes]
    for index, edges in enumerate(remaining):
        print(f"class={index} edges={sorted(edges)} pairs={allowed_pairs(edges)}")
        for c in (1, 2, 3, 4, 5, 8, 12, 20):
            best, witness = lp_bound(edges, c)
            print(f"  c={c} eta_lp={best} active={witness[1] if witness else None}")


if __name__ == "__main__":
    main()
