#!/usr/bin/env python3
"""Compile and run the independent E5 extension-screen checker."""

from __future__ import annotations

import hashlib
from pathlib import Path
import shutil
import subprocess
import tempfile


SOURCE_SHA256 = "bc59c072510ad5e5fb684c8a63b68abbac31e68dd59f7172b850b5cb984dfd49"
EXPECTED_STDOUT = (
    "PASS independent E5 six-boundary extension check\n"
    "ordinary hosts checked: 140498\n"
    "portal hosts checked: 4536\n"
    "total finite hosts checked: 145034\n"
    "model universes: n=10 11880; n=11 159027; n=12 1899612\n"
)


def main() -> None:
    source = Path(__file__).with_suffix(".cpp")
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    if digest != SOURCE_SHA256:
        raise SystemExit(f"checker source hash mismatch: {digest}")

    compiler = shutil.which("c++") or shutil.which("clang++") or shutil.which("g++")
    if compiler is None:
        raise SystemExit("no C++20 compiler found")

    with tempfile.TemporaryDirectory(prefix="e5-extension-check-") as temporary:
        binary = Path(temporary) / "checker"
        compilation = subprocess.run(
            [
                compiler,
                "-std=c++20",
                "-O3",
                "-Wall",
                "-Wextra",
                "-Wpedantic",
                str(source),
                "-o",
                str(binary),
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        if compilation.returncode != 0:
            raise SystemExit(compilation.stderr or compilation.stdout)

        run = subprocess.run(
            [str(binary)],
            check=False,
            capture_output=True,
            text=True,
            timeout=180,
        )
        if run.returncode != 0:
            raise SystemExit(run.stderr or run.stdout)
        if run.stdout != EXPECTED_STDOUT:
            raise SystemExit(
                "independent checker output mismatch:\n"
                f"expected:\n{EXPECTED_STDOUT}\nactual:\n{run.stdout}"
            )

    print(EXPECTED_STDOUT, end="")


if __name__ == "__main__":
    main()
