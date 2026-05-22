#!/usr/bin/env python3
"""Repository contract checks for axon-bci-gateway.

This checker is intentionally lightweight. The gateway is a Processing/OpenBCI
integration fork, not a Rust kernel crate. These checks verify repository
surface, fork attribution, workflow hygiene, and claim discipline.

Each GitHub Actions job calls this script with one check name. The workflow has
17 independent jobs so failures are easy to read in the Actions UI.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]


EXPECTED_JOBS = [
    "repository-contract",
    "required-structure",
    "readme-surface",
    "attribution-notice",
    "license-policy",
    "changelog-release",
    "contact-policy",
    "overclaim-guard",
    "workflow-integrity",
    "ci-job-count",
    "markdown-quality",
    "upstream-boundary",
    "gateway-identifiers",
    "reference-hardware",
    "standard-mapping",
    "path-hygiene",
    "security-policy",
]


TEXT_FILES = [
    "README.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "NOTICE",
    "SECURITY.md",
    ".github/workflows/ci.yml",
    "tools/gateway_ci_checks.py",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        fail(f"missing required file: {rel}")
    return path.read_text(encoding="utf-8", errors="replace")


def require_file(rel: str) -> None:
    if not (ROOT / rel).is_file():
        fail(f"missing required file: {rel}")


def require_dir(rel: str) -> None:
    if not (ROOT / rel).is_dir():
        fail(f"missing required directory: {rel}")


def require_contains(rel: str, token: str) -> None:
    text = read(rel)
    if token not in text:
        fail(f"{rel} must contain: {token!r}")


def require_not_contains(rel: str, token: str) -> None:
    text = read(rel)
    if token in text:
        fail(f"{rel} must not contain: {token!r}")


def line_count(rel: str) -> int:
    return len(read(rel).splitlines())


def check_repository_contract() -> None:
    for rel in [
        "README.md",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "CODE_OF_CONDUCT.md",
        "LICENSE",
        "NOTICE",
        "SECURITY.md",
        ".github/workflows/ci.yml",
        "tools/gateway_ci_checks.py",
    ]:
        require_file(rel)

    print("repository contract: PASS")


def check_required_structure() -> None:
    for rel in [
        "OpenBCI_GUI",
        "GuiUnitTests",
        "Networking-Test-Kit",
        "tools",
    ]:
        require_dir(rel)

    require_file("OpenBCI_GUI/OpenBCI_GUI.pde")

    print("required structure: PASS")


def check_readme_surface() -> None:
    text = read("README.md")

    required = [
        "integration fork",
        "acquisition boundary",
        "not a rewrite of OpenBCI GUI",
        "It is not a hard real-time kernel.",
        "This repository does not claim",
        "OpenBCI endorsement",
    ]

    for token in required:
        if token not in text:
            fail(f"README missing required surface phrase: {token}")

    if line_count("README.md") < 140:
        fail("README.md appears collapsed; expected at least 140 lines")

    print("readme surface: PASS")


def check_attribution_notice() -> None:
    text = read("NOTICE")

    required = [
        "OpenBCI_GUI",
        "MIT",
        "Joel Murphy",
        "OpenBCI contributors",
        "does not claim affiliation",
        "connect@axonos.org",
        "security@axonos.org",
    ]

    for token in required:
        if token not in text:
            fail(f"NOTICE missing attribution token: {token}")

    print("attribution notice: PASS")


def check_license_policy() -> None:
    text = read("LICENSE")

    required = [
        "MIT License",
        "Permission is hereby granted",
        "THE SOFTWARE IS PROVIDED",
    ]

    for token in required:
        if token not in text:
            fail(f"LICENSE missing MIT token: {token}")

    print("license policy: PASS")


def check_changelog_release() -> None:
    text = read("CHANGELOG.md")

    required = [
        "Unreleased",
        "v1.0.0-axonos",
        "Versioning policy",
        "OpenBCI_GUI",
    ]

    for token in required:
        if token not in text:
            fail(f"CHANGELOG missing token: {token}")

    print("changelog release: PASS")


def check_contact_policy() -> None:
    stale = [
        "info" + "@axonos.org",
        "denis" + "@axonos.org",
        "axonosorg" + "@gmail.com",
    ]

    for rel in TEXT_FILES:
        text = read(rel)
        for token in stale:
            if token in text:
                fail(f"{rel} contains stale email address: {token}")

    require_contains("README.md", "connect@axonos.org")
    require_contains("README.md", "security@axonos.org")
    require_contains("SECURITY.md", "security@axonos.org")

    print("contact policy: PASS")


def check_overclaim_guard() -> None:
    forbidden = [
        "FDA " + "510(k)",
        "clinical " + "engagement",
        "clinical " + "pilot",
        "certified kernel",
        "medical device approval",
        "measured " + "WCRT",
        "measured " + "WCET",
    ]

    for rel in [
        "README.md",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "NOTICE",
        "SECURITY.md",
    ]:
        text = read(rel)
        for token in forbidden:
            if token in text:
                fail(f"{rel} contains overclaim-prone token: {token}")

    print("overclaim guard: PASS")


def check_workflow_integrity() -> None:
    text = read(".github/workflows/ci.yml")

    if line_count(".github/workflows/ci.yml") < 200:
        fail("ci.yml appears collapsed or too short; expected at least 200 lines")

    required = [
        "name: ci",
        "workflow_dispatch",
        "cancel-in-progress",
        "tools/gateway_ci_checks.py",
    ]

    for token in required:
        if token not in text:
            fail(f"ci.yml missing token: {token}")

    print("workflow integrity: PASS")


def check_ci_job_count() -> None:
    text = read(".github/workflows/ci.yml")
    missing: list[str] = []

    for job in EXPECTED_JOBS:
        pattern = rf"^\s+{re.escape(job)}:\s*$"
        if re.search(pattern, text, flags=re.MULTILINE) is None:
            missing.append(job)

    if missing:
        fail(f"ci.yml missing jobs: {', '.join(missing)}")

    print("ci job count: PASS")


def check_markdown_quality() -> None:
    thresholds = {
        "README.md": 140,
        "CHANGELOG.md": 45,
        "CONTRIBUTING.md": 35,
        "NOTICE": 35,
        "SECURITY.md": 15,
    }

    for rel, minimum in thresholds.items():
        lines = read(rel).splitlines()
        if len(lines) < minimum:
            fail(f"{rel} appears collapsed; expected at least {minimum} lines")

        too_long = [
            i
            for i, line in enumerate(lines, 1)
            if len(line) > 220
        ]
        if too_long:
            fail(f"{rel} has overlong line(s): {too_long[:5]}")

    print("markdown quality: PASS")


def check_upstream_boundary() -> None:
    for rel in [
        "README.md",
        "NOTICE",
        "CONTRIBUTING.md",
    ]:
        text = read(rel)
        for token in [
            "OpenBCI",
            "upstream",
            "MIT",
        ]:
            if token not in text:
                fail(f"{rel} missing upstream boundary token: {token}")

    require_contains(
        "README.md",
        "If a change improves OpenBCI GUI generally, it belongs upstream first.",
    )

    print("upstream boundary: PASS")


def check_gateway_identifiers() -> None:
    for rel in [
        "README.md",
        "CHANGELOG.md",
        "NOTICE",
    ]:
        text = read(rel)
        for token in [
            "axonos-gateway",
            "/axonos",
        ]:
            if token not in text:
                fail(f"{rel} missing gateway identifier: {token}")

    print("gateway identifiers: PASS")


def check_reference_hardware() -> None:
    text = read("README.md")

    required = [
        "ADS1299",
        "STM32F407",
        "Cortex-A53",
        "nRF52840",
        "ATECC608B",
        "ISO7741",
    ]

    for token in required:
        if token not in text:
            fail(f"README missing reference hardware token: {token}")

    print("reference hardware: PASS")


def check_standard_mapping() -> None:
    text = read("README.md")

    required = [
        "AOS-0001",
        "AOS-0003",
        "AOS-0008",
        "AOS-0010",
        "AOS-0012",
    ]

    for token in required:
        if token not in text:
            fail(f"README missing AxonOS Standard mapping: {token}")

    print("standard mapping: PASS")


def check_path_hygiene() -> None:
    suspicious: list[str] = []

    ignored_roots = {".git"}

    for path in ROOT.rglob("*"):
        if any(part in ignored_roots for part in path.parts):
            continue

        name = path.name
        if name.startswith("="):
            suspicious.append(str(path.relative_to(ROOT)))
        if '"' in name or "'" in name:
            suspicious.append(str(path.relative_to(ROOT)))
        if name.endswith(".tar"):
            suspicious.append(str(path.relative_to(ROOT)))

    if suspicious:
        fail(f"suspicious root files: {suspicious}")

    print("path hygiene: PASS")


def check_security_policy() -> None:
    text = read("SECURITY.md")

    required = [
        "security@axonos.org",
        "raw neural data",
        "upstream OpenBCI GUI",
    ]

    for token in required:
        if token not in text:
            fail(f"SECURITY.md missing token: {token}")

    print("security policy: PASS")


CHECKS: dict[str, Callable[[], None]] = {
    "repository-contract": check_repository_contract,
    "required-structure": check_required_structure,
    "readme-surface": check_readme_surface,
    "attribution-notice": check_attribution_notice,
    "license-policy": check_license_policy,
    "changelog-release": check_changelog_release,
    "contact-policy": check_contact_policy,
    "overclaim-guard": check_overclaim_guard,
    "workflow-integrity": check_workflow_integrity,
    "ci-job-count": check_ci_job_count,
    "markdown-quality": check_markdown_quality,
    "upstream-boundary": check_upstream_boundary,
    "gateway-identifiers": check_gateway_identifiers,
    "reference-hardware": check_reference_hardware,
    "standard-mapping": check_standard_mapping,
    "path-hygiene": check_path_hygiene,
    "security-policy": check_security_policy,
}


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: gateway_ci_checks.py <check>")
        print("")
        print("Available checks:")
        for check in EXPECTED_JOBS:
            print(f"  - {check}")
        sys.exit(2)

    check_name = sys.argv[1]
    if check_name not in CHECKS:
        fail(f"unknown check: {check_name}")

    CHECKS[check_name]()


if __name__ == "__main__":
    main()
