#!/usr/bin/env python3
"""Compile and summarize the hash-pinned adjacent-portal C census."""

from __future__ import annotations

import hashlib
from pathlib import Path
import shutil
import subprocess
import tempfile


SOURCE_SHA256 = "c77769fe640a75289106b1854cca35eeaa4ac379aec62cab95eb30a4f826365d"
EXPECTED_STDERR = """\
partitions=11880
total=26569 negative=5428
hist 4 4 4900
hist 4 5 240
hist 5 4 240
hist 5 5 48
special_five=48 crossing_edge_positive=192
"""


def main() -> None:
    source = Path(__file__).with_name(
        "hc7_literal_k44_adjacent_portal_census_verify.c"
    )
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    if digest != SOURCE_SHA256:
        raise SystemExit(f"C verifier source hash mismatch: {digest}")

    compiler = shutil.which("cc") or shutil.which("clang") or shutil.which("gcc")
    if compiler is None:
        raise SystemExit("no C compiler found")

    with tempfile.TemporaryDirectory(prefix="k44-adjacent-portal-") as temporary:
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
        if run.stderr != EXPECTED_STDERR:
            raise SystemExit(
                "C verifier summary mismatch:\n"
                f"expected:\n{EXPECTED_STDERR}\nactual:\n{run.stderr}"
            )
        profiles = run.stdout.splitlines()
        if len(profiles) != 5428 or any(
            not profile.startswith("NEG ") for profile in profiles
        ):
            raise SystemExit("unexpected adjacent-portal negative-profile corpus")
        profile_digest = hashlib.sha256(run.stdout.encode()).hexdigest()

    print("GREEN literal K4,4 adjacent-portal census")
    print(EXPECTED_STDERR, end="")
    print(f"profile_rows={len(profiles)}")
    print(f"profile_sha256={profile_digest}")


if __name__ == "__main__":
    main()
