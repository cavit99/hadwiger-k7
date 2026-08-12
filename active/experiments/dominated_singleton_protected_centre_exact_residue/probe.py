#!/usr/bin/env python3
"""Profile the nonterminal protected-centre exact-kernel residue.

This is a discovery diagnostic.  It uses the current deterministic exact
eight-terminal order-eight/order-nine catalogue, whose finite census is not
yet independently audited.  No output of this script is a promoted theorem.
"""

from __future__ import annotations

import collections
import importlib.util
from pathlib import Path
import sys


ACTIVE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ACTIVE))
import hc7_eight_terminal_exact_bundle_catalogue as exact  # noqa: E402


def load_probe():
    path = (
        ACTIVE
        / "experiments"
        / "dominated_singleton_exact_eight_kernel_absorption"
        / "probe.py"
    )
    spec = importlib.util.spec_from_file_location("exact_absorption", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


probe = load_probe()


def degree(mask: int, vertex: int) -> int:
    return sum(
        bool(mask >> exact.PAIR_INDEX[tuple(sorted((vertex, other)))] & 1)
        for other in exact.TERMINALS
        if other != vertex
    )


def profile_order_eight() -> None:
    _unlabelled, masks = exact.order_eight_catalogue()
    profile = collections.Counter()
    for code in probe.LIVE_CODES:
        fixed = probe.q_mask(code)
        for mask in masks:
            if probe.closes(fixed, mask):
                continue
            degrees = tuple(sorted(degree(mask, vertex) for vertex in range(8)))
            profile[(code, mask.bit_count(), degree(mask, 7), degrees)] += 1
    print("order8_residue_profile")
    for key, count in sorted(profile.items()):
        print(key, count)


def profile_order_nine() -> None:
    _rooted, _edges, _degrees, _templates, families = exact.order_nine_catalogue()
    profile = collections.Counter()
    for code in probe.LIVE_CODES:
        fixed = probe.q_mask(code)
        for family in families:
            if any(probe.closes(fixed, carrier) for carrier in family):
                continue
            centre_degrees = tuple(sorted({degree(mask, 7) for mask in family}))
            edge_counts = tuple(sorted({mask.bit_count() for mask in family}))
            profile[(code, len(family), centre_degrees, edge_counts)] += 1
    print("order9_residue_profile")
    for key, count in sorted(profile.items()):
        print(key, count)


if __name__ == "__main__":
    profile_order_eight()
    if "--order9" in sys.argv:
        profile_order_nine()
