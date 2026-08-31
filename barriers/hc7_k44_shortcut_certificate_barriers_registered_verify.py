#!/usr/bin/env python3
"""Compile and validate the two hash-pinned K4,4 shortcut barriers."""

from __future__ import annotations

import hashlib
import itertools
from pathlib import Path
import re
import shutil
import subprocess
import tempfile


SOURCES = {
    "hc7_k44_fat_triangle_certificate_barrier_verify.c":
        "14aae8c4fa35859a336573d41e69981234e7a121ed18027239572ad12423eb55",
    "hc7_k44_one_split_theta_certificate_barrier_verify.c":
        "7804e3af454721a792652c58ac8cd9b2f84b0ad9bf5087812f409c3aef78f2b5",
}


def run_red(binary: Path, arguments: tuple[int, ...], prefix: str) -> int:
    run = subprocess.run(
        [str(binary), *map(str, arguments)],
        check=False,
        capture_output=True,
        text=True,
        timeout=30,
    )
    if run.returncode != 1:
        raise SystemExit(
            f"{binary.name} {arguments} returned {run.returncode}, expected RED exit 1"
        )
    if run.stderr:
        raise SystemExit(f"{binary.name} {arguments} wrote to stderr: {run.stderr}")
    lines = run.stdout.splitlines()
    if not lines or not lines[0].startswith(prefix):
        raise SystemExit(f"{binary.name} {arguments} has an invalid screen header")
    match = re.fullmatch(r"NO_TARGET checked=(\d+) best=(\d+)", lines[1])
    if match is None or int(match.group(1)) <= 0:
        raise SystemExit(f"{binary.name} {arguments} has an invalid RED summary")
    return int(match.group(2))


def main() -> None:
    compiler = shutil.which("cc") or shutil.which("clang") or shutil.which("gcc")
    if compiler is None:
        raise SystemExit("no C compiler found")
    directory = Path(__file__).parent

    with tempfile.TemporaryDirectory(prefix="k44-shortcut-barriers-") as temporary:
        binaries = {}
        for index, (name, expected_hash) in enumerate(SOURCES.items()):
            source = directory / name
            digest = hashlib.sha256(source.read_bytes()).hexdigest()
            if digest != expected_hash:
                raise SystemExit(f"{name} source hash mismatch: {digest}")
            binary = Path(temporary) / f"verify-{index}"
            compilation = subprocess.run(
                [compiler, "-O3", str(source), "-o", str(binary)],
                check=False,
                capture_output=True,
                text=True,
            )
            if compilation.returncode:
                raise SystemExit(compilation.stderr or compilation.stdout)
            binaries[name] = binary

        fat_profiles = tuple(
            (left, middle, 7 - left - middle)
            for left, middle in itertools.product(range(1, 6), repeat=2)
            if 7 - left - middle > 0
        )
        split_profiles = tuple(
            (left, paths)
            for left, paths in itertools.product(range(1, 4), range(1, 7))
        )
        fat_best = max(
            run_red(
                binaries["hc7_k44_fat_triangle_certificate_barrier_verify.c"],
                profile,
                "SCREEN profile=",
            )
            for profile in fat_profiles
        )
        split_best = max(
            run_red(
                binaries["hc7_k44_one_split_theta_certificate_barrier_verify.c"],
                profile,
                "SCREEN split=",
            )
            for profile in split_profiles
        )

    if len(fat_profiles) != 15 or fat_best != 18:
        raise SystemExit("fat-triangle aggregate mismatch")
    if len(split_profiles) != 18 or split_best != 15:
        raise SystemExit("split-theta aggregate mismatch")
    print("fat_profiles=15 unexpected_status=0 max_quotient_edges=18")
    print("split_profiles=18 unexpected_status=0 max_quotient_edges=15")
    print("PASS K4,4 shortcut-certificate barriers")


if __name__ == "__main__":
    main()
