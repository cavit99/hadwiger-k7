#!/usr/bin/env python3
"""Classify the protected-centre order-eight/order-nine quotient residue.

This is a discovery diagnostic.  It imports the exact catalogue generator,
whose order-eight and order-nine branches have not yet received an
independent audit, and the composition probe in this directory.  It records
fixed-Q automorphism orbits and tests the deliberately stronger quotient
hypothesis that one further edge from the protected root to an arbitrary
Q-rooted bag is available.
"""

from __future__ import annotations

import collections
import hashlib
import importlib.util
import itertools
from pathlib import Path
import sys


if not __debug__:
    raise SystemExit("classification requires assertions; do not run with -O")


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("absorption_probe", HERE / "probe.py")
assert SPEC is not None and SPEC.loader is not None
probe = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(probe)
exact = probe.exact
base = probe.base

EXPECTED_SUMMARY = {
    ("order8", "FCQ`_"): (210, 15, 30, 3),
    ("order8", "FCQb_"): (74, 37, 6, 3),
    ("order8", "FCp`_"): (141, 14, 15, 3),
    ("order9", "FCQ`_"): (430, 23, 0, 0),
    ("order9", "FCQb_"): (86, 43, 0, 0),
    ("order9", "FCp`_"): (287, 22, 0, 0),
}


def automorphisms(code: str) -> tuple[tuple[int, ...], ...]:
    graph = base.decode_graph6(code)
    answer = []
    for image in itertools.permutations(range(7)):
        if all(
            base.adjacent(graph, left, right)
            == base.adjacent(graph, image[left], image[right])
            for left, right in itertools.combinations(range(7), 2)
        ):
            answer.append(image + (7,))
    return tuple(answer)


def relabel_mask(mask: int, image: tuple[int, ...]) -> int:
    answer = 0
    for index, (left, right) in enumerate(exact.PAIRS):
        if mask >> index & 1:
            pair = tuple(sorted((image[left], image[right])))
            answer |= 1 << exact.PAIR_INDEX[pair]
    return answer


def relabel_family(
    family: tuple[int, ...], image: tuple[int, ...]
) -> tuple[int, ...]:
    return tuple(sorted(relabel_mask(mask, image) for mask in family))


def canonical_family(
    family: tuple[int, ...], group: tuple[tuple[int, ...], ...]
) -> tuple[int, ...]:
    return min(relabel_family(family, image) for image in group)


def degree_profile(mask: int) -> tuple[int, ...]:
    degrees = [0] * 8
    for index, (left, right) in enumerate(exact.PAIRS):
        if mask >> index & 1:
            degrees[left] += 1
            degrees[right] += 1
    return tuple(sorted(degrees))


def root_degree(mask: int) -> int:
    return sum(
        bool(mask >> exact.PAIR_INDEX[(vertex, 7)] & 1)
        for vertex in range(7)
    )


def root_neighbour_mask(mask: int) -> int:
    return sum(
        1 << vertex
        for vertex in range(7)
        if mask >> exact.PAIR_INDEX[(vertex, 7)] & 1
    )


def add_root_edge(mask: int, vertex: int) -> int:
    return mask | (1 << exact.PAIR_INDEX[(vertex, 7)])


def closes_with_some_root_edge(code_mask: int, family: tuple[int, ...]) -> bool:
    return any(
        probe.closes(code_mask, add_root_edge(carrier, vertex))
        for carrier in family
        for vertex in range(7)
    )


def forcing_root_set(code_mask: int, family: tuple[int, ...]) -> int:
    """Roots at which one added protected-root contact permits closure.

    The legal owner of the unique nonterminal may be chosen after the exact
    kernel is known.  Accordingly a root belongs to this set when at least
    one member of the owner family closes after the same rooted contact is
    added.
    """

    return sum(
        1 << vertex
        for vertex in range(7)
        if any(
            probe.closes(code_mask, add_root_edge(carrier, vertex))
            for carrier in family
        )
    )


def q_edge_mask(mask: int) -> int:
    return sum(
        1 << probe.INDEX7[edge]
        for edge in probe.PAIRS7
        if mask >> exact.PAIR_INDEX[edge] & 1
    )


def family_profile(code_mask: int, family: tuple[int, ...]) -> tuple:
    root_masks = tuple(root_neighbour_mask(mask) for mask in family)
    common_root = 0x7F
    possible_root = 0
    possible_q_edges = code_mask
    for root_mask, carrier in zip(root_masks, family):
        common_root &= root_mask
        possible_root |= root_mask
        possible_q_edges |= q_edge_mask(carrier)

    forcing = forcing_root_set(code_mask, family)
    degree_profiles = tuple(sorted({degree_profile(mask) for mask in family}))
    edge_counts = tuple(sorted({mask.bit_count() for mask in family}))
    root_degrees = tuple(sorted({mask.bit_count() for mask in root_masks}))
    return (
        len(family),
        edge_counts,
        root_degrees,
        degree_profiles,
        common_root.bit_count(),
        possible_root.bit_count(),
        (0x7F ^ possible_root).bit_count(),
        (0x1F_FFFF ^ possible_q_edges).bit_count(),
        forcing.bit_count(),
    )


def format_vertices(mask: int) -> str:
    return "".join(str(vertex) for vertex in range(7) if mask >> vertex & 1) or "-"


def digest_records(records: tuple[bytes, ...]) -> str:
    digest = hashlib.sha256()
    for record in records:
        digest.update(len(record).to_bytes(2, "big"))
        digest.update(record)
    return digest.hexdigest()


def canonical_vertex_mask(mask: int, group: tuple[tuple[int, ...], ...]) -> int:
    return min(
        sum(1 << image[vertex] for vertex in range(7) if mask >> vertex & 1)
        for image in group
    )


def neighbours(mask: int, vertex: int, vertices=range(8)) -> tuple[int, ...]:
    return tuple(
        other
        for other in vertices
        if other != vertex
        and mask >> exact.PAIR_INDEX[tuple(sorted((vertex, other)))] & 1
    )


def robust_order_eight_shape(mask: int) -> str:
    """Recognise the four unlabelled shapes in the robust order-eight core."""

    q_degrees = tuple(len(neighbours(mask, vertex, range(7))) for vertex in range(7))
    if root_degree(mask) == 7:
        assert q_degrees == (2,) * 7
        return "wheel(C7)"

    assert root_degree(mask) == 5
    assert q_degrees == tuple(
        2 if mask >> exact.PAIR_INDEX[(vertex, 7)] & 1 else 3
        for vertex in range(7)
    )
    branch = tuple(vertex for vertex in range(7) if q_degrees[vertex] == 3)
    assert len(branch) == 2
    start, finish = branch
    lengths = []
    for following in neighbours(mask, start, range(7)):
        previous, current, length = start, following, 1
        while current != finish:
            choices = tuple(
                vertex
                for vertex in neighbours(mask, current, range(7))
                if vertex != previous
            )
            assert len(choices) == 1
            previous, current = current, choices[0]
            length += 1
        lengths.append(length)
    assert len(lengths) == 3 and sum(lengths) == 8
    return "theta" + "".join(str(length) for length in sorted(lengths))


def extra_q_contact_profile(code_mask: int, carrier: int) -> tuple[int, int, bool]:
    """Count forcing and nonforcing new contacts between Q-rooted bags."""

    forcing = []
    nonforcing = []
    for edge in probe.PAIRS7:
        carrier_bit = 1 << exact.PAIR_INDEX[edge]
        q_bit = 1 << probe.INDEX7[edge]
        if carrier & carrier_bit or code_mask & q_bit:
            continue
        if probe.closes(code_mask, carrier | carrier_bit):
            forcing.append(carrier_bit)
        else:
            nonforcing.append(carrier_bit)
    every_nonforcing_pair_closes = len(nonforcing) >= 2 and all(
        probe.closes(code_mask, carrier | first | second)
        for first, second in itertools.combinations(nonforcing, 2)
    )
    return len(forcing), len(nonforcing), every_nonforcing_pair_closes


def classify(
    name: str,
    families: tuple[tuple[int, ...], ...],
) -> dict[str, tuple[tuple[int, ...], ...]]:
    total_failures = 0
    total_orbits = 0
    total_edge_robust = 0
    failures_by_code = {}
    for code in probe.LIVE_CODES:
        fixed = probe.q_mask(code)
        failed = tuple(
            family
            for family in families
            if not any(probe.closes(fixed, carrier) for carrier in family)
        )
        group = automorphisms(code)
        orbits = {canonical_family(family, group) for family in failed}
        robust = tuple(
            family
            for family in failed
            if not closes_with_some_root_edge(fixed, family)
        )
        robust_orbits = {canonical_family(family, group) for family in robust}
        failures_by_code[code] = failed
        family_sizes = collections.Counter(len(family) for family in failed)
        all_profiles = tuple(family_profile(fixed, family) for family in failed)
        forcing_sizes = collections.Counter(profile[8] for profile in all_profiles)
        root_contact_ranges = collections.Counter(
            (profile[4], profile[5]) for profile in all_profiles
        )
        edge_count_ranges = collections.Counter(
            (
                min(mask.bit_count() for mask in family),
                max(mask.bit_count() for mask in family),
            )
            for family in failed
        )
        universal_missing_counts = collections.Counter(
            (profile[6], profile[7]) for profile in all_profiles
        )
        profiles = collections.Counter(
            family_profile(fixed, family) for family in robust
        )
        total_failures += len(failed)
        total_orbits += len(orbits)
        total_edge_robust += len(robust)
        assert (
            len(failed),
            len(orbits),
            len(robust),
            len(robust_orbits),
        ) == EXPECTED_SUMMARY[(name, code)]
        print(
            code,
            name,
            f"failures={len(failed)}",
            f"orbits={len(orbits)}",
            f"survive_every_added_root_edge={len(robust)}",
            f"robust_orbits={len(robust_orbits)}",
            flush=True,
        )
        print(
            code,
            name,
            "failure_digest",
            exact.sha256_families(failed),
            "orbit_digest",
            exact.sha256_families(tuple(sorted(orbits))),
            "robust_digest",
            exact.sha256_families(robust),
            flush=True,
        )
        print(code, name, "robust_profiles", sorted(profiles.items()), flush=True)
        if name == "order8":
            shapes = collections.Counter(
                robust_order_eight_shape(family[0]) for family in robust
            )
            contact_profiles = collections.Counter(
                (
                    robust_order_eight_shape(family[0]),
                    *extra_q_contact_profile(fixed, family[0]),
                )
                for family in robust
            )
            print(code, name, "robust_shapes", sorted(shapes.items()), flush=True)
            print(
                code,
                name,
                "robust_extra_Q_contact_profiles",
                sorted(contact_profiles.items()),
                flush=True,
            )
        print(
            code, name, "owner_family_sizes", sorted(family_sizes.items()), flush=True
        )
        print(
            code,
            name,
            "forcing_root_set_sizes",
            sorted(forcing_sizes.items()),
            flush=True,
        )
        print(
            code,
            name,
            "common_possible_root_contacts",
            sorted(root_contact_ranges.items()),
            flush=True,
        )
        print(
            code,
            name,
            "carrier_edge_count_ranges",
            sorted(edge_count_ranges.items()),
            flush=True,
        )
        print(
            code,
            name,
            "universal_missing_root_q_edges",
            sorted(universal_missing_counts.items()),
            flush=True,
        )
        if robust_orbits:
            print(code, name, "first_robust_orbit", min(robust_orbits), flush=True)
        if "--orbits" in sys.argv:
            orbit_multiplicity = collections.Counter(
                canonical_family(family, group) for family in failed
            )
            for orbit_index, (representative, multiplicity) in enumerate(
                sorted(orbit_multiplicity.items()), 1
            ):
                root_masks = tuple(root_neighbour_mask(mask) for mask in representative)
                common_root = 0x7F
                possible_root = 0
                possible_q_edges = fixed
                for root_mask, carrier in zip(root_masks, representative):
                    common_root &= root_mask
                    possible_root |= root_mask
                    possible_q_edges |= q_edge_mask(carrier)
                forcing = forcing_root_set(fixed, representative)
                missing_q_pairs = tuple(
                    edge
                    for edge in probe.PAIRS7
                    if not (possible_q_edges >> probe.INDEX7[edge] & 1)
                )
                print(
                    "orbit",
                    code,
                    name,
                    orbit_index,
                    f"multiplicity={multiplicity}",
                    f"family_size={len(representative)}",
                    f"edge_counts={sorted({mask.bit_count() for mask in representative})}",
                    f"root_degrees={sorted({root_degree(mask) for mask in representative})}",
                    f"common_Nw={format_vertices(common_root)}",
                    f"possible_Nw={format_vertices(possible_root)}",
                    f"universally_missing_w={format_vertices(0x7F ^ possible_root)}",
                    f"forcing_w={format_vertices(forcing)}",
                    f"universally_missing_Q={missing_q_pairs}",
                    f"masks={representative}",
                    flush=True,
                )
    print(
        name,
        f"total_failures={total_failures}",
        f"total_orbits={total_orbits}",
        f"survive_every_added_root_edge={total_edge_robust}",
        flush=True,
    )
    return failures_by_code


def template_degree_sequence(template: int) -> tuple[int, ...]:
    terminal_mask, extra_neighbours = template >> 8, template & 0xFF
    degrees = []
    for vertex in range(8):
        degrees.append(
            len(neighbours(terminal_mask, vertex, range(8)))
            + bool(extra_neighbours >> vertex & 1)
        )
    degrees.append(extra_neighbours.bit_count())
    return tuple(sorted(degrees))


def classify_order_nine_templates(
    templates: tuple[int, ...],
    failures_by_code: dict[str, tuple[tuple[int, ...], ...]],
) -> None:
    targets = {
        family
        for families in failures_by_code.values()
        for family in families
    }
    template_for_family = {}
    for template in templates:
        family = exact.owner_family_one_extra(template)
        if family in targets:
            template_for_family[family] = template
    assert template_for_family.keys() == targets

    for code, failed in failures_by_code.items():
        fixed = probe.q_mask(code)
        group = automorphisms(code)
        edge_counts = collections.Counter()
        x_degrees = collections.Counter()
        degree_sequences = collections.Counter()
        protected_contacts = collections.Counter()
        forcing_orbits = collections.Counter()
        missing_orbits = collections.Counter()
        forcing_records = []
        residual_templates = []
        for family in failed:
            template = template_for_family[family]
            terminal_mask, extra_neighbours = template >> 8, template & 0xFF
            x_degree = extra_neighbours.bit_count()
            base_root_neighbours = root_neighbour_mask(terminal_mask)
            x_root = bool(extra_neighbours >> 7 & 1)
            possible_root = base_root_neighbours
            if x_root:
                possible_root |= extra_neighbours & 0x7F
            forcing = forcing_root_set(fixed, family)
            residual_templates.append(template)
            forcing_records.append(template.to_bytes(8, "big") + bytes([forcing]))

            edge_counts[terminal_mask.bit_count() + x_degree] += 1
            x_degrees[x_degree] += 1
            degree_sequences[template_degree_sequence(template)] += 1
            protected_contacts[
                (
                    base_root_neighbours.bit_count() + x_root,
                    base_root_neighbours.bit_count(),
                    x_root,
                    (0x7F ^ possible_root).bit_count(),
                )
            ] += 1
            forcing_orbits[canonical_vertex_mask(forcing, group)] += 1
            missing_orbits[
                canonical_vertex_mask(0x7F ^ possible_root, group)
            ] += 1

        assert all(
            degree == 3 and terminal_degree == 2 and x_root
            for degree, terminal_degree, x_root, _missing in protected_contacts
        )
        assert set(degree_sequences) == {
            (3, 3, 3, 3, 3, 3, 3, 3, 6),
            (3, 3, 3, 3, 3, 3, 3, 4, 7),
            (3, 3, 3, 3, 3, 3, 3, 3, 8),
            (3, 3, 3, 3, 3, 3, 4, 4, 8),
        }
        print(
            code, "order9_kernel_edge_counts", sorted(edge_counts.items()), flush=True
        )
        print(code, "order9_x_degrees", sorted(x_degrees.items()), flush=True)
        print(
            code,
            "order9_kernel_degree_sequences",
            sorted(degree_sequences.items()),
            flush=True,
        )
        print(
            code,
            "order9_residual_template_digest",
            exact.sha256_fixed_width(sorted(residual_templates), 8),
            "forcing_record_digest",
            digest_records(tuple(sorted(forcing_records))),
            flush=True,
        )
        print(
            code,
            "order9_protected_contacts_dK_dT_xw_missing",
            sorted(protected_contacts.items()),
            flush=True,
        )
        print(
            code,
            "order9_forcing_set_orbits",
            [
                (format_vertices(mask), count)
                for mask, count in sorted(forcing_orbits.items())
            ],
            flush=True,
        )
        print(
            code,
            "order9_universally_missing_root_set_orbits",
            [(format_vertices(mask), count) for mask, count in sorted(missing_orbits.items())],
            flush=True,
        )


def main() -> None:
    _unlabelled8, masks8 = exact.order_eight_catalogue()
    classify("order8", tuple((mask,) for mask in masks8))
    if "--all" in sys.argv:
        _rooted, _edges, _degrees, templates, families9 = exact.order_nine_catalogue()
        failures = classify("order9", families9)
        classify_order_nine_templates(templates, failures)


if __name__ == "__main__":
    main()
