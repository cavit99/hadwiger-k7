#!/usr/bin/env python3
"""Verify a palette-pinned all-lock response-square proof gate.

This is a finite falsification diagnostic.  The construction asks whether
the response, lock and common-model data can coexist with seven-connectivity
before K7-minus-edge-minor exclusion is imposed.
"""

from __future__ import annotations

from itertools import combinations, product

import networkx as nx


PALETTE = tuple(range(6))
U, V, X, Y = 6, 7, 8, 9
A2, A3, A4, A5 = 10, 11, 12, 13
FIXED = {A2: 2, A3: 3, A4: 4, A5: 5}
ORDER = 14
E = (0, U)
F = (1, V)


def base_host() -> nx.Graph:
    """Return H=G-{e,f} for the palette-pinned implication gadget."""

    graph = nx.Graph()
    graph.add_nodes_from(range(ORDER))
    graph.add_edges_from(combinations(PALETTE, 2))

    domains = {
        U: {0, 1},
        V: {0, 1},
        X: {0, 2},
        Y: {1, 2},
    }
    for vertex, domain in domains.items():
        graph.add_edges_from((vertex, colour) for colour in set(PALETTE) - domain)

    # This list-colouring gadget realizes the implication U <= V on {0,1}:
    # the sole forbidden assignment is (U,V)=(1,0).
    graph.add_edges_from(((U, Y), (V, X), (X, Y)))

    # Four fixed-colour vertices raise connectivity without changing the
    # response relation.  A2 and A3 form two foreign model bags and are kept
    # anticomplete to the implication gadget.  A4 and A5 lie in the two
    # palette bags already seen from both selected endpoints.
    for vertex, colour in FIXED.items():
        graph.add_edges_from(
            (vertex, palette_vertex)
            for palette_vertex in PALETTE
            if palette_vertex != colour
        )
    graph.add_edges_from(combinations(FIXED, 2))
    graph.add_edges_from(
        (gadget_vertex, fixed_vertex)
        for gadget_vertex in (U, V, X, Y)
        for fixed_vertex in (A4, A5)
    )
    return graph


def colourings(host: nx.Graph) -> tuple[tuple[int, ...], ...]:
    """Enumerate colourings modulo the forced K6 palette permutation."""

    answer = []
    fixed_tail = tuple(FIXED[vertex] for vertex in sorted(FIXED))
    for tail in product(PALETTE, repeat=4):
        colouring = PALETTE + tail + fixed_tail
        if all(colouring[left] != colouring[right] for left, right in host.edges()):
            answer.append(colouring)
    return tuple(answer)


def signature(colouring: tuple[int, ...]) -> str:
    return (
        ("E" if colouring[U] == colouring[0] else "P")
        + ("E" if colouring[V] == colouring[1] else "P")
    )


def pair_locked(
    host: nx.Graph,
    colouring: tuple[int, ...],
    ends: tuple[int, int],
) -> bool:
    alpha = colouring[ends[0]]
    if colouring[ends[1]] != alpha:
        return False
    for beta in set(PALETTE) - {alpha}:
        vertices = [
            vertex for vertex in host if colouring[vertex] in {alpha, beta}
        ]
        component = nx.node_connected_component(host.subgraph(vertices), ends[0])
        if ends[1] not in component:
            return False
    return True


def full_palettes(
    host: nx.Graph,
    colouring: tuple[int, ...],
    ends: tuple[int, int],
) -> tuple[int, ...]:
    alpha = colouring[ends[0]]
    answer = []
    for beta in set(PALETTE) - {alpha}:
        vertices = {
            vertex for vertex in host if colouring[vertex] in {alpha, beta}
        }
        component = nx.node_connected_component(host.subgraph(vertices), ends[0])
        if component == vertices:
            complement = host.subgraph(set(host) - vertices)
            if k_colourable(complement, 4) and not k_colourable(complement, 3):
                answer.append(beta)
    return tuple(sorted(answer))


def k_colourable(graph: nx.Graph, colour_count: int) -> bool:
    colours: dict[int, int] = {}

    def extend() -> bool:
        if len(colours) == len(graph):
            return True
        uncoloured = set(graph) - set(colours)
        vertex = max(
            uncoloured,
            key=lambda item: (
                len({colours[nbr] for nbr in graph[item] if nbr in colours}),
                graph.degree(item),
            ),
        )
        forbidden = {colours[nbr] for nbr in graph[vertex] if nbr in colours}
        for colour in range(colour_count):
            if colour in forbidden:
                continue
            colours[vertex] = colour
            if extend():
                return True
            del colours[vertex]
        return False

    return extend()


def contracted(graph: nx.Graph, edges: tuple[tuple[int, int], ...]) -> nx.Graph:
    answer = graph.copy()
    for left, right in edges:
        answer = nx.contracted_nodes(answer, left, right, self_loops=False)
    return nx.Graph(answer)


def target_subgraph(graph: nx.Graph) -> tuple[int, ...] | None:
    """Return the displayed K7-minus-edge subgraph, if it is present."""

    vertices = PALETTE + (U,)
    missing = {
        frozenset({left, right})
        for left, right in combinations(vertices, 2)
        if not graph.has_edge(left, right)
    }
    if missing == {frozenset({1, U})}:
        return vertices
    return None


def common_model_split_score(graph: nx.Graph) -> tuple[int, int]:
    """Check the natural spanning K6 model and both coordinate splits."""

    bags = (
        frozenset({0, U, Y}),
        frozenset({1, V, X}),
        frozenset({2, 3, A4}),
        frozenset({4, 5, A5}),
        frozenset({A2}),
        frozenset({A3}),
    )
    host = graph.copy()
    host.remove_edges_from((E, F))
    assert set().union(*bags) == set(host)
    assert all(nx.is_connected(host.subgraph(bag)) for bag in bags)
    assert all(
        any(host.has_edge(a, b) for a in bags[left] for b in bags[right])
        for left, right in combinations(range(6), 2)
    )

    scores = []
    for bag_index, ends in ((0, E), (1, F)):
        own = bags[bag_index]
        foreign = tuple(bags[index] for index in range(6) if index != bag_index)
        best = 0
        middle = tuple(own - set(ends))
        for mask in range(1 << len(middle)):
            left = {ends[0]}
            left.update(
                vertex for bit, vertex in enumerate(middle) if mask & (1 << bit)
            )
            right = set(own) - left
            if ends[1] not in right:
                continue
            if not nx.is_connected(graph.subgraph(left)) or not nx.is_connected(
                graph.subgraph(right)
            ):
                continue
            score = sum(
                any(graph.has_edge(a, b) for a in left for b in bag)
                and any(graph.has_edge(a, b) for a in right for b in bag)
                for bag in foreign
            )
            best = max(best, score)
        scores.append(best)
    assert len(scores) == 2
    return scores[0], scores[1]


def screen(host: nx.Graph) -> dict[str, object] | None:
    colour_set = colourings(host)
    signatures = {signature(colouring) for colouring in colour_set}
    if signatures != {"EP", "PE", "EE"}:
        return None

    ep = next(
        (c for c in colour_set if signature(c) == "EP" and pair_locked(host, c, E)),
        None,
    )
    pe = next(
        (c for c in colour_set if signature(c) == "PE" and pair_locked(host, c, F)),
        None,
    )
    if ep is None or pe is None:
        return None

    graph = host.copy()
    graph.add_edges_from((E, F))
    if nx.node_connectivity(graph) < 7:
        return None
    if k_colourable(graph, 6) or not k_colourable(graph, 7):
        return None
    for deleted_edges in ((E,), (F,), (E, F)):
        deletion = graph.copy()
        deletion.remove_edges_from(deleted_edges)
        if not k_colourable(deletion, 6) or k_colourable(deletion, 5):
            return None
    if not all(
        k_colourable(contracted(graph, edges), 6)
        and not k_colourable(contracted(graph, edges), 5)
        for edges in ((E,), (F,), (E, F))
    ):
        return None

    try:
        split_scores = common_model_split_score(graph)
    except AssertionError:
        return None
    if max(split_scores) >= 4:
        return None
    full_ep = full_palettes(host, ep, E)
    full_pe = full_palettes(host, pe, F)
    if min(len(full_ep), len(full_pe)) < 4:
        return None
    return {
        "graph": graph,
        "host": host,
        "EP": ep,
        "PE": pe,
        "full_EP": full_ep,
        "full_PE": full_pe,
        "split_scores": split_scores,
        "target": target_subgraph(graph),
    }


def main() -> None:
    base = base_host()
    result = screen(base)
    if result is None:
        print("NO_SURVIVOR")
        return
    graph = result["graph"]
    assert isinstance(graph, nx.Graph)
    assert result["target"] is not None
    signature_counts = {
        label: sum(signature(colouring) == label for colouring in colourings(base))
        for label in ("EP", "EE", "PE")
    }
    assert signature_counts == {"EP": 1, "EE": 3, "PE": 1}
    print("SCOPED_SURVIVOR_VERIFIED")
    print(f"connectivity={nx.node_connectivity(graph)}")
    print(f"degrees={sorted(dict(graph.degree()).values())}")
    print(f"signature_counts={signature_counts}")
    print(f"EP={result['EP']}")
    print(f"PE={result['PE']}")
    print(f"full_palettes_EP={result['full_EP']}")
    print(f"full_palettes_PE={result['full_PE']}")
    print(f"split_scores={result['split_scores']}")
    print(f"K7_minus_subgraph={result['target']}")
    print("target_exclusion=false")


if __name__ == "__main__":
    main()
