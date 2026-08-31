#!/usr/bin/env python3
"""Regenerate and independently validate the double-cone certificates."""

from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile


HASHES = {
    "hc7_k44_fourconnected_seven_boundary_double_cone_census.py":
        "64371b10f7ea9cfe6fe2d01ffa166d0cd9e5d2b176a9b8cf1488972310171b4e",
    "hc7_k44_fourconnected_seven_boundary_double_cone_certificates_verify.py":
        "3ab82219ec67e75e9caf2d7533033bb972c32b1bfb05e8a5eeedc2b9f8c2725a",
    "hc7_k44_fourconnected_seven_boundary_double_cone_certificates.tsv":
        "32229e0699a892778cf3911b21332c2341eadb33eed1f99652634a79adffa168",
    "hc7_k44_fourconnected_seven_boundary_double_cone_census.txt":
        "7af251c769557f2ae2f38821525c5bb9dc44a6b446be5cedf73367c2b45c4672",
}
EXPECTED_CERTIFICATE_STDOUT = (
    "DOUBLE_CONE_CERTIFICATES_VALID 29 digest "
    "d862876512b71717e4122aa9081b88b6731e21f59eb9eab0817f08f7215dd487\n"
)


def main() -> None:
    directory = Path(__file__).parent
    paths = {name: directory / name for name in HASHES}
    for name, expected in HASHES.items():
        actual = hashlib.sha256(paths[name].read_bytes()).hexdigest()
        if actual != expected:
            raise SystemExit(f"{name} hash mismatch: {actual}")

    census_source = paths[
        "hc7_k44_fourconnected_seven_boundary_double_cone_census.py"
    ]
    certificate_source = paths[
        "hc7_k44_fourconnected_seven_boundary_double_cone_certificates_verify.py"
    ]
    retained_certificates = paths[
        "hc7_k44_fourconnected_seven_boundary_double_cone_certificates.tsv"
    ]
    retained_census = paths[
        "hc7_k44_fourconnected_seven_boundary_double_cone_census.txt"
    ]

    with tempfile.TemporaryDirectory(prefix="k44-double-cone-") as temporary:
        generated_certificates = Path(temporary) / "certificates.tsv"
        generated_census = Path(temporary) / "census.txt"
        census = subprocess.run(
            [
                sys.executable,
                str(census_source),
                str(generated_certificates),
                str(generated_census),
            ],
            check=False,
            capture_output=True,
            text=True,
            timeout=60,
        )
        if census.returncode:
            raise SystemExit(census.stderr or census.stdout)
        if census.stderr:
            raise SystemExit(f"census wrote to stderr: {census.stderr}")
        if generated_certificates.read_bytes() != retained_certificates.read_bytes():
            raise SystemExit("regenerated certificate corpus differs from retained TSV")
        if generated_census.read_bytes() != retained_census.read_bytes():
            raise SystemExit("regenerated census differs from retained output")
        expected_census = retained_census.read_text(encoding="ascii")
        if census.stdout != expected_census:
            raise SystemExit("census stdout differs from retained output")

        certificate = subprocess.run(
            [sys.executable, str(certificate_source), str(generated_certificates)],
            check=False,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if certificate.returncode:
            raise SystemExit(certificate.stderr or certificate.stdout)
        if certificate.stderr:
            raise SystemExit(f"certificate checker wrote to stderr: {certificate.stderr}")
        if certificate.stdout != EXPECTED_CERTIFICATE_STDOUT:
            raise SystemExit("certificate checker output mismatch")

    print(expected_census, end="")
    print(EXPECTED_CERTIFICATE_STDOUT, end="")


if __name__ == "__main__":
    main()
