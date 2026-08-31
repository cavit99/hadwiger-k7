#!/usr/bin/env python3
"""Run the pinned low-codegree verifier without NetworkX's known hash warning."""

from __future__ import annotations

import hashlib
from pathlib import Path
import runpy
import sys
import warnings


SOURCE_SHA256 = "d721c181a8388feb7901e8ab04f704c19679cfb56551752756a45733f28d6fdc"


def main() -> None:
    if sys.flags.optimize:
        raise SystemExit(
            "the pinned low-codegree verifier requires assertions; rerun without -O"
        )
    source = Path(__file__).with_name(
        "hc7_k7minus_sixconnected_degree_eight_low_codegree_verify.py"
    )
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    if digest != SOURCE_SHA256:
        raise SystemExit(f"low-codegree verifier source hash mismatch: {digest}")
    warnings.filterwarnings(
        "ignore",
        message=(
            "The hashes produced for graphs without node or edge attributes changed "
            "in v3.5 due to a bugfix \\(see documentation\\)\\."
        ),
        category=UserWarning,
    )
    runpy.run_path(str(source), run_name="__main__")


if __name__ == "__main__":
    main()
