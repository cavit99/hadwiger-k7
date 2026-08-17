#!/usr/bin/env python3
"""Verify the finite boundary certificates in the returned-six-cut theorem.

The script uses only the Python standard library.  It enumerates graphs on
six labelled vertices, quotients by all relabellings, and checks the weighted
rooted inequalities using exact rational arithmetic.
"""

from fractions import Fraction
from itertools import combinations, combinations_with_replacement, permutations


VERTICES = tuple(range(6))
PAIRS = tuple(combinations(VERTICES, 2))
FOUR_SETS = tuple(map(frozenset, combinations(VERTICES, 4)))
PERMUTATIONS = tuple(permutations(VERTICES))


def parse_edges(spec: str) -> frozenset[tuple[int, int]]:
    edges = []
    for token in spec.split(","):
        x, y = map(int, token)
        edges.append(tuple(sorted((x, y))))
    return frozenset(edges)


def degrees(edges: frozenset[tuple[int, int]]) -> tuple[int, ...]:
    return tuple(sum(v in edge for edge in edges) for v in VERTICES)


def induced_size(
    edges: frozenset[tuple[int, int]], vertices: frozenset[int]
) -> int:
    return sum(x in vertices and y in vertices for x, y in edges)


def contains_four_cycle(
    edges: frozenset[tuple[int, int]], vertices: frozenset[int]
) -> bool:
    if len(vertices) != 4:
        raise RuntimeError("four-cycle check requires four vertices")
    first = min(vertices)
    others = sorted(vertices - {first})
    for ordering in permutations(others):
        cycle = (first,) + ordering
        cycle_edges = {
            tuple(sorted((cycle[index], cycle[(index + 1) % 4])))
            for index in range(4)
        }
        if cycle_edges <= edges:
            return True
    return False


def canonical(edges: frozenset[tuple[int, int]]) -> tuple[tuple[int, int], ...]:
    images = []
    for permutation in PERMUTATIONS:
        image = tuple(
            sorted(tuple(sorted((permutation[x], permutation[y]))) for x, y in edges)
        )
        images.append(image)
    return min(images)


def boundary_classes(size: int, minimum_cubic_vertices: int = 0):
    labelled = 0
    classes: dict[tuple[tuple[int, int], ...], int] = {}
    for chosen in combinations(PAIRS, size):
        edges = frozenset(chosen)
        degree = degrees(edges)
        if max(degree) > 3:
            continue
        if sum(value == 3 for value in degree) < minimum_cubic_vertices:
            continue
        if any(induced_size(edges, four_set) > 4 for four_set in FOUR_SETS):
            continue
        labelled += 1
        key = canonical(edges)
        classes[key] = classes.get(key, 0) + 1
    return labelled, classes


CERTIFICATES = {
    "8-I": (
        parse_edges("03,04,05,13,14,15,24,25"),
        ("01", "02", "12", "34", "35", "45"),
        Fraction(1, 4),
        "connectedness",
        Fraction(5, 2),
    ),
    "8-II": (
        parse_edges("02,04,05,13,14,15,24,35"),
        ("01", "34", "25"),
        Fraction(1, 2),
        "connectedness",
        Fraction(5, 2),
    ),
    "8-III": (
        parse_edges("02,03,05,13,14,15,24,25"),
        ("01", "23", "45"),
        Fraction(1, 2),
        "connectedness",
        Fraction(5, 2),
    ),
    "7-I": (
        parse_edges("01,02,03,12,14,25,34"),
        ("04", "15", "23"),
        Fraction(1, 2),
        "connectedness",
        Fraction(3),
    ),
    "7-II": (
        parse_edges("01,02,03,12,14,34,35"),
        ("04", "15", "32"),
        Fraction(1, 2),
        "connectedness",
        Fraction(3),
    ),
    "7-III": (
        parse_edges("01,02,03,14,15,24,25"),
        ("04", "05", "13", "23"),
        Fraction(1, 2),
        "degree03",
        Fraction(3),
    ),
    "7-IV": (
        parse_edges("01,02,03,12,34,35,45"),
        ("04", "05", "13", "23"),
        Fraction(1, 2),
        "degree03",
        Fraction(4),
    ),
    "7-V": (
        parse_edges("01,02,03,14,15,24,35"),
        ("04", "05", "12", "13"),
        Fraction(1, 2),
        "degree01",
        Fraction(4),
    ),
}


REMAINING_SEVEN = {
    "7-VI": parse_edges("01,02,03,12,14,35,45"),
    "7-VII": parse_edges("01,02,03,14,24,35,45"),
}


LINEAR_WITNESSES = {
    "7-IV": (5, 6, (5, 2, 2, 5, 2, 2), 4),
    "7-V": (5, 6, (5, 5, 2, 2, 2, 2), 4),
    "7-VI": (10, 15, (10, 10, 1, 3, 3, 3), 5),
    "7-VII": (10, 9, (10, 1, 2, 10, 10, 10), 12),
}


COMPATIBLE_PAIR_PAIRS = {
    "7-VI": (
        "01/23",
        "01/24",
        "02/13",
        "04/12",
        "04/13",
        "04/15",
        "05/13",
        "05/23",
        "05/34",
        "15/24",
        "15/34",
    ),
    "7-VII": (
        "04/12",
        "04/13",
        "04/15",
        "04/23",
        "04/25",
        "05/13",
        "05/23",
        "05/34",
        "15/34",
        "25/34",
    ),
}


def parse_pair(spec: str) -> tuple[int, int]:
    return tuple(sorted(map(int, spec)))


def completed_boundary(
    edges: frozenset[tuple[int, int]], omitted: tuple[int, int]
) -> frozenset[tuple[int, int]]:
    roots = sorted(set(VERTICES) - set(omitted))
    return edges | frozenset(combinations(roots, 2))


def compatible_pair_pairs(edges: frozenset[tuple[int, int]]):
    compatible = set()
    for first, second in combinations_with_replacement(PAIRS, 2):
        completion = completed_boundary(edges, first) | completed_boundary(
            edges, second
        )
        if len(completion) >= 14:
            compatible.add((first, second))
    return compatible


def rooted_triggers(edges: frozenset[tuple[int, int]]):
    """Return every pair to which one of the two branches of (3) applies."""
    degree = degrees(edges)
    triggers = []
    for p, q in PAIRS:
        pair = (p, q)
        root_set = frozenset(VERTICES) - frozenset(pair)
        nonedge_cubic = pair not in edges and (degree[p] == 3 or degree[q] == 3)
        adjacent_cover = pair in edges and all(
            tuple(sorted((p, z))) in edges or tuple(sorted((q, z))) in edges
            for z in root_set
        )
        if nonedge_cubic or adjacent_cover:
            kind = "nonedge-cubic" if nonedge_cubic else "adjacent-cover"
            triggers.append((pair, root_set, kind))
    return tuple(triggers)


def verify_linear_witness(
    name: str,
    edges: frozenset[tuple[int, int]],
    witness: tuple[int, int, tuple[int, ...], int],
) -> None:
    """Check a numerical witness against every linear inequality in the note."""
    c, internal_edges, attachments, claimed_eta = witness
    if len(attachments) != 6:
        raise RuntimeError(f"{name}: malformed attachment vector")
    if not c - 1 <= internal_edges <= c * (c - 1) // 2:
        raise RuntimeError(f"{name}: internal-edge count violates elementary bounds")
    if any(not 1 <= value <= c for value in attachments):
        raise RuntimeError(f"{name}: attachment vector violates fullness or simplicity")
    if 2 * internal_edges + sum(attachments) < 6 * c:
        raise RuntimeError(f"{name}: degree inequality fails")
    eta = internal_edges + sum(attachments) - 4 * c
    if eta != claimed_eta:
        raise RuntimeError(f"{name}: eta {eta}, expected {claimed_eta}")

    for pair, root_set, kind in rooted_triggers(edges):
        if contains_four_cycle(edges, root_set):
            raise RuntimeError(f"{name}: {kind} trigger {pair} has a root four-cycle")
        left = (
            internal_edges
            + sum(attachments[z] for z in root_set)
            + induced_size(edges, root_set)
        )
        if left > 3 * c + 4:
            raise RuntimeError(
                f"{name}: {kind} trigger {pair} fails: {left}>{3*c+4}"
            )


def verify_type_vi_dual() -> None:
    """Verify the exact eta <= 5 certificate for type VI."""
    edges = REMAINING_SEVEN["7-VI"]
    terms = []
    for pair_spec in ("04", "13", "15"):
        pair = parse_pair(pair_spec)
        roots = frozenset(VERTICES) - frozenset(pair)
        vector = [1] + [int(vertex in roots) for vertex in VERTICES] + [-3]
        terms.append((vector, 4 - induced_size(edges, roots)))

    # -2e-P+6c <= 0, a_1-c <= 0, and -a_2 <= -1.
    terms.append(([-2] + [-1] * 6 + [6], 0))
    upper_one = [0] * 8
    upper_one[2] = 1
    upper_one[7] = -1
    terms.append((upper_one, 0))
    lower_two = [0] * 8
    lower_two[3] = -1
    terms.append((lower_two, -1))

    coefficient_sum = [
        sum(vector[index] for vector, _ in terms) for index in range(8)
    ]
    objective = [1] + [1] * 6 + [-4]
    constant_sum = sum(constant for _, constant in terms)
    if coefficient_sum != objective or constant_sum != 5:
        raise RuntimeError(
            f"7-VI: dual gives {coefficient_sum} <= {constant_sum}"
        )

    for pair_spec in ("04", "05", "13", "15"):
        pair = parse_pair(pair_spec)
        roots = frozenset(VERTICES) - frozenset(pair)
        if induced_size(edges, roots) != 2 or contains_four_cycle(edges, roots):
            raise RuntimeError(f"7-VI: strict root check fails at {pair_spec}")


def verify_certificate(name: str, certificate) -> None:
    edges, pair_specs, weight, completion, claimed_bound = certificate
    degree = degrees(edges)
    incidence = [Fraction(0) for _ in VERTICES]
    total_weight = Fraction(0)
    constant = Fraction(0)
    root_edge_counts = []

    for pair_spec in pair_specs:
        q, p = map(int, pair_spec)
        edge = tuple(sorted((q, p)))
        if edge in edges:
            raise RuntimeError(f"{name}: {pair_spec} is not a boundary nonedge")
        if degree[q] != 3 and degree[p] != 3:
            raise RuntimeError(f"{name}: {pair_spec} has no cubic end")
        omitted = frozenset((q, p))
        root_set = frozenset(VERTICES) - omitted
        root_edge_count = induced_size(edges, root_set)
        if contains_four_cycle(edges, root_set):
            raise RuntimeError(f"{name}: {pair_spec} has a root four-cycle")
        root_edge_counts.append(root_edge_count)
        total_weight += weight
        incidence[q] += weight
        incidence[p] += weight
        constant += weight * (4 - root_edge_count)

    if name in {"7-IV", "7-V"} and set(root_edge_counts) != {2}:
        raise RuntimeError(f"{name}: strict root counts {root_edge_counts}")

    # Weighted (3): lambda*e + sum(lambda-incidence[v])*a_v
    # <= 3*lambda*c + constant.
    e_coefficient = total_weight
    attachment_coefficients = [total_weight - value for value in incidence]
    c_coefficient = 3 * total_weight

    if completion == "connectedness":
        # Add (c-e)/2 <= 1/2.
        e_coefficient -= Fraction(1, 2)
        c_coefficient -= Fraction(1, 2)
        constant += Fraction(1, 2)
    elif completion.startswith("degree"):
        exceptional_vertices = tuple(map(int, completion.removeprefix("degree")))
        if len(exceptional_vertices) != 2:
            raise RuntimeError(f"{name}: malformed degree completion {completion}")
        for vertex in exceptional_vertices:
            attachment_coefficients[vertex] += Fraction(1, 2)
            c_coefficient += Fraction(1, 2)
        # Add -e-P/2 <= -3c, equivalent to half the degree inequality.
        e_coefficient -= 1
        attachment_coefficients = [value - Fraction(1, 2) for value in attachment_coefficients]
        c_coefficient -= 3
    else:
        raise RuntimeError(f"{name}: unknown completion {completion}")

    if e_coefficient != 1:
        raise RuntimeError(f"{name}: final internal-edge coefficient {e_coefficient}")
    if attachment_coefficients != [Fraction(1)] * 6:
        raise RuntimeError(
            f"{name}: final attachment coefficients {attachment_coefficients}"
        )
    if c_coefficient != 4:
        raise RuntimeError(f"{name}: final order coefficient {c_coefficient}")
    if constant != claimed_bound:
        raise RuntimeError(f"{name}: bound {constant}, expected {claimed_bound}")


def main() -> None:
    labelled_eight, classes_eight = boundary_classes(8)
    labelled_seven_dense, classes_seven_dense = boundary_classes(7, 3)
    labelled_seven_all, classes_seven_all = boundary_classes(7)

    named_eight = {canonical(value[0]) for key, value in CERTIFICATES.items() if key[0] == "8"}
    named_seven = {
        canonical(CERTIFICATES[key][0]) for key in ("7-I", "7-II", "7-III")
    }
    named_further = {
        canonical(CERTIFICATES[key][0]) for key in ("7-IV", "7-V")
    }
    named_remaining = {canonical(edges) for edges in REMAINING_SEVEN.values()}

    if set(classes_eight) != named_eight:
        raise RuntimeError("the named eight-edge boundaries are not exhaustive")
    if set(classes_seven_dense) != named_seven:
        raise RuntimeError("the named dense seven-edge boundaries are not exhaustive")
    if len(classes_seven_all) != 7:
        raise RuntimeError(f"expected seven total seven-edge classes, got {len(classes_seven_all)}")
    if len(classes_seven_all) - len(classes_seven_dense) != 4:
        raise RuntimeError("expected four remaining seven-edge classes")
    if not named_further <= set(classes_seven_all) - set(classes_seven_dense):
        raise RuntimeError("types IV and V are not two distinct remaining classes")
    actual_remaining = (
        set(classes_seven_all) - set(classes_seven_dense) - named_further
    )
    if actual_remaining != named_remaining:
        raise RuntimeError("the two stated remaining seven-edge types are not exact")

    for name, certificate in CERTIFICATES.items():
        verify_certificate(name, certificate)
    witness_boundaries = {
        "7-IV": CERTIFICATES["7-IV"][0],
        "7-V": CERTIFICATES["7-V"][0],
        **REMAINING_SEVEN,
    }
    for name, witness in LINEAR_WITNESSES.items():
        verify_linear_witness(name, witness_boundaries[name], witness)
    verify_type_vi_dual()

    for c in (4, 10, 100):
        verify_linear_witness(
            "7-VI-family",
            REMAINING_SEVEN["7-VI"],
            (c, 2 * c - 5, (c, c, 1, 3, 3, 3), 5),
        )
    for c in (2, 10, 100):
        verify_linear_witness(
            "7-VII-ray",
            REMAINING_SEVEN["7-VII"],
            (c, c - 1, (c, 1, 2, c, c, c), c + 2),
        )

    for name, specifications in COMPATIBLE_PAIR_PAIRS.items():
        expected = set()
        for specification in specifications:
            first_spec, second_spec = specification.split("/")
            pair_pair = tuple(sorted((parse_pair(first_spec), parse_pair(second_spec))))
            expected.add(pair_pair)
        actual = compatible_pair_pairs(REMAINING_SEVEN[name])
        if actual != expected:
            raise RuntimeError(
                f"{name}: compatible pair-pairs differ: "
                f"missing={expected-actual}, extra={actual-expected}"
            )

    adjacent_cover_pairs = {}
    for name, expected_pair in (("7-IV", (0, 3)), ("7-V", (0, 1))):
        triggers = rooted_triggers(CERTIFICATES[name][0])
        actual_pairs = {
            pair for pair, _, kind in triggers if kind == "adjacent-cover"
        }
        if actual_pairs != {expected_pair}:
            raise RuntimeError(f"{name}: adjacent-cover pairs {actual_pairs}")
        adjacent_cover_pairs[name] = expected_pair

    print("GREEN returned three-component dense-boundary certificates")
    print(f"eight_edge_labelled={labelled_eight}")
    print(f"eight_edge_isomorphism_classes={len(classes_eight)}")
    print(f"seven_edge_three_cubic_labelled={labelled_seven_dense}")
    print(f"seven_edge_three_cubic_isomorphism_classes={len(classes_seven_dense)}")
    print(f"seven_edge_remaining_isomorphism_classes={len(classes_seven_all)-len(classes_seven_dense)}")
    print("seven_edge_further_eliminated_isomorphism_classes=3")
    print("seven_edge_unhandled_isomorphism_classes=1")
    print("adjacent_cover_triggers=7-IV:03;7-V:01")
    print("strict_rooted_counts=7-IV:2,2,2,2;7-V:2,2,2,2")
    print("linear_witness_eta=7-IV:4,7-V:4,7-VI:5,7-VII:12@c10")
    print("type_VI_dual=R04+R13+R15+degree+upper1+lower2:5")
    print("type_VI_bound=5")
    print("remaining_type_VII_recession_eta=c+2")
    print("cross_lobe_compatible_pair_pairs=7-VI:11;7-VII:10")
    print(
        "weighted_bounds=8-I:5/2,8-II:5/2,8-III:5/2,"
        "7-I:3,7-II:3,7-III:3,7-IV:4,7-V:4"
    )


if __name__ == "__main__":
    main()
