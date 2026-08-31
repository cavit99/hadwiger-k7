#!/usr/bin/env python3
"""Compile and run the hash-pinned rooted-``K_4^-`` C verifier."""

from __future__ import annotations

import hashlib
from pathlib import Path
import shutil
import subprocess
import tempfile


SOURCE_SHA256 = "15ff05aec0d17184a9a50b3fe62e6097b27bfe10eafb5fda2e77dd4316a1f18b"
EXPECTED_STDOUT = """\
n=4 three_connected_labelled=1 assignment_upper_bound=1 all_green
n=5 three_connected_labelled=26 assignment_upper_bound=130 all_green
n=6 three_connected_labelled=1768 assignment_upper_bound=44200 all_green
n=7 three_connected_labelled=225096 assignment_upper_bound=28137000 all_green
"""


def main() -> None:
    source = Path(__file__).with_name("rooted_k4minus_four_roots_verify.c")
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    if digest != SOURCE_SHA256:
        raise SystemExit(f"C verifier source hash mismatch: {digest}")

    compiler = shutil.which("cc") or shutil.which("clang") or shutil.which("gcc")
    if compiler is None:
        raise SystemExit("no C compiler found")

    with tempfile.TemporaryDirectory(prefix="rooted-k4minus-") as temporary:
        binary = Path(temporary) / "verify"
        compilation = subprocess.run(
            [compiler, "-O3", str(source), "-o", str(binary)],
            check=False,
            capture_output=True,
            text=True,
        )
        if compilation.returncode:
            raise SystemExit(compilation.stderr or compilation.stdout)
        run = subprocess.run(
            [str(binary)],
            check=False,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if run.returncode:
            raise SystemExit(run.stderr or run.stdout)
        if run.stderr:
            raise SystemExit(f"C verifier wrote to stderr: {run.stderr}")
        if run.stdout != EXPECTED_STDOUT:
            raise SystemExit(
                "C verifier output mismatch:\n"
                f"expected:\n{EXPECTED_STDOUT}\nactual:\n{run.stdout}"
            )

    print(EXPECTED_STDOUT, end="")


if __name__ == "__main__":
    main()
