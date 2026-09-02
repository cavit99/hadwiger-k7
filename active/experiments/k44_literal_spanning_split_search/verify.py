#!/usr/bin/env python3
"""Reproduce the bounded spanning-split hostile screen."""

from __future__ import annotations

import shutil

import z3

from search import nx, search

if not __debug__:
    raise SystemExit("verification requires assertions; do not use Python -O")


def required_tool(name: str) -> str:
    path = shutil.which(name)
    if path is None:
        raise RuntimeError(f"required nauty tool not found: {name}")
    return path


def main():
    geng = required_tool("geng")
    planarg = required_tool("planarg")
    labelg = required_tool("labelg")
    print(
        f"z3_version={z3.get_version_string()} networkx_version={nx.__version__} "
        "nauty_tools=available"
    )
    cases = (
        (8, "anchored", None, "all", 3, 424,
         "79043a58646d5fc086e54b33c75f77e9935221dcf00245e2781ad234eb288ad5", 422),
        (8, "full", None, "all", 3, 424,
         "79043a58646d5fc086e54b33c75f77e9935221dcf00245e2781ad234eb288ad5", 422),
        (9, "anchored", 4, "all", 3, 16,
         "9e851692305a2c9b565cdb6e4ff4644c34b02c796dbc7b53db416a2afb2260bd", 16),
        (9, "full", 4, "all", 3, 16,
         "9e851692305a2c9b565cdb6e4ff4644c34b02c796dbc7b53db416a2afb2260bd", 16),
        (9, "anchored", None, "planar", 4, 14,
         "08048d0e52435765946d241d35ddf08617b4b35f3c8c4aca2bedbff69dc32f9c", 10),
        (9, "full", None, "planar", 4, 14,
         "08048d0e52435765946d241d35ddf08617b4b35f3c8c4aca2bedbff69dc32f9c", 10),
        (9, "anchored", None, "join-perturbations", 3, 6,
         "ae62a05e285f00fafebda2b36776d8074136d419a8e679eec67caf2949964821", 6),
        (9, "full", None, "join-perturbations", 3, 6,
         "ae62a05e285f00fafebda2b36776d8074136d419a8e679eec67caf2949964821", 6),
    )
    for (order, mode, max_degree, family, connectivity, generated,
         digest, eligible) in cases:
        status = search(
            order,
            mode,
            geng,
            None,
            max_degree,
            family,
            connectivity,
            planarg,
            labelg,
            False,
            (generated, digest, eligible),
        )
        assert status == 0
    print("GREEN bounded literal-K44 spanning split hostile screen")


if __name__ == "__main__":
    main()
