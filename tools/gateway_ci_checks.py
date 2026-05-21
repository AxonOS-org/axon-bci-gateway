#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

CHECKS = [
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

EXPECTED_JOBS = CHECKS

def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)

def read(rel: str) -> str:
    p = ROOT / rel
    if not p.exists():
        fail(f"missing required file: {rel}")
    return p.read_text(encoding="utf-8", errors="replace")

def normalized(rel: str) -> str:
    return re.sub(r"\s+", " ", read(rel)).strip()

def require_file(rel: str) -> None:
    if not (ROOT / rel).is_file():
        fail(f"missing required file: {rel}")

def require_dir(rel: str) -> None:
    if not (ROOT / rel).is_dir():
        fail(f"missing required directory: {rel}")

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
    for rel in ["OpenBCI_GUI", "GuiUnitTests", "Networking-Test-Kit", "tools"]:
        require_dir(rel)
    require_file("OpenBCI_GUI/OpenBCI_GUI.pde")
    print("required structure: PASS")

def check_readme_surface() -> None:
    text = normalized("README.md")
    for token in [
        "integration fork",
        "acquisition boundary",
        "not a rewrite of OpenBCI GUI",
        "not a certified medical-device component",
        "not a hard real-time kernel",
        "This repository does not claim",
    ]:
        if token not in text:
            fail(f"README missing required surface phrase: {token}")
    print("readme surface: PASS")

def check_attribution_notice() -> None:
    text = read("NOTICE")
    for token in [
        "OpenBCI_GUI",
        "MIT",
        "Joel Murphy",
        "OpenBCI contributors",
        "does not claim affiliation",
        "connect@axonos.org",
        "security@axonos.org",
    ]:
        if token not in text:
            fail(f"NOTICE missing attribution token: {token}")
    print("attribution notice: PASS")

def check_license_policy() -> None:
    text = normalized("LICENSE")
    for token in ["MIT License", "Permission is hereby granted", "THE SOFTWARE IS PROVIDED"]:
        if token not in text:
            fail(f"LICENSE missing MIT token: {token}")
    print("license policy: PASS")

def check_changelog_release() -> None:
    text = read("CHANGELOG.md")
    for token in ["Unreleased", "v1.0.0-axonos", "Versioning policy", "OpenBCI_GUI"]:
        if token not in text:
            fail(f"CHANGELOG missing token: {token}")
    print("changelog release: PASS")

def check_contact_policy() -> None:
    for rel in ["README.md", "CHANGELOG.md", "CONTRIBUTING.md", "NOTICE", "SECURITY.md"]:
        text = read(rel)
        if "info@axonos.org" in text or "denis@axonos.org" in text:
            fail(f"{rel} contains stale email address")
    if "connect@axonos.org" not in read("README.md"):
        fail("README missing connect@axonos.org")
    if "security@axonos.org" not in read("README.md"):
        fail("README missing security@axonos.org")
    print("contact policy: PASS")

def check_overclaim_guard() -> None:
    forbidden = [
        "FDA 510(k)",
        "clinical engagement",
        "clinical pilot",
        "certified kernel",
        "medical device approval",
    ]
    for rel in ["README.md", "CHANGELOG.md", "CONTRIBUTING.md", "NOTICE", "SECURITY.md"]:
        text = read(rel)
        for token in forbidden:
            if token in text:
                fail(f"{rel} contains overclaim-prone token: {token}")
    print("overclaim guard: PASS")

def check_workflow_integrity() -> None:
    text = read(".github/workflows/ci.yml")
    if len(text.splitlines()) < 150:
        fail("ci.yml appears collapsed or too short")
    for token in ["name: ci", "workflow_dispatch", "cancel-in-progress", "tools/gateway_ci_checks.py"]:
        if token not in text:
            fail(f"ci.yml missing token: {token}")
    print("workflow integrity: PASS")

def check_ci_job_count() -> None:
    text = read(".github/workflows/ci.yml")
    missing = []
    for job in EXPECTED_JOBS:
        if re.search(rf"^\s{{2}}{re.escape(job)}:\s*$", text, flags=re.MULTILINE) is None:
            missing.append(job)
    if missing:
        fail(f"ci.yml missing jobs: {', '.join(missing)}")
    print("ci job count: PASS")

def check_markdown_quality() -> None:
    for rel in ["README.md", "CHANGELOG.md", "CONTRIBUTING.md", "NOTICE", "SECURITY.md"]:
        text = read(rel)
        lines = text.splitlines()
        if len(lines) < 12:
            fail(f"{rel} appears collapsed or too short")
        too_long = [i for i, line in enumerate(lines, 1) if len(line) > 220]
        if too_long:
            fail(f"{rel} has overlong line(s): {too_long[:5]}")
    print("markdown quality: PASS")

def check_upstream_boundary() -> None:
    for rel in ["README.md", "NOTICE", "CONTRIBUTING.md"]:
        text = read(rel)
        for token in ["OpenBCI", "upstream", "MIT"]:
            if token not in text:
                fail(f"{rel} missing upstream boundary token: {token}")
    if "If a change improves OpenBCI GUI generally, it belongs upstream first." not in read("README.md"):
        fail("README missing upstream-first rule")
    print("upstream boundary: PASS")

def check_gateway_identifiers() -> None:
    for rel in ["README.md", "CHANGELOG.md", "NOTICE"]:
        text = read(rel)
        for token in ["axonos-gateway", "/axonos"]:
            if token not in text:
                fail(f"{rel} missing gateway identifier: {token}")
    print("gateway identifiers: PASS")

def check_reference_hardware() -> None:
    text = read("README.md")
    for token in ["ADS1299", "STM32F407", "Cortex-A53", "nRF52840", "ATECC608B", "ISO7741"]:
        if token not in text:
            fail(f"README missing reference hardware token: {token}")
    print("reference hardware: PASS")

def check_standard_mapping() -> None:
    text = read("README.md")
    for token in ["AOS-0001", "AOS-0003", "AOS-0008", "AOS-0010", "AOS-0012"]:
        if token not in text:
            fail(f"README missing AxonOS Standard mapping: {token}")
    print("standard mapping: PASS")

def check_path_hygiene() -> None:
    suspicious = []
    for p in ROOT.iterdir():
        name = p.name
        if name.startswith("=") or '"' in name or "'" in name or name.endswith(".tar"):
            suspicious.append(name)
    if suspicious:
        fail(f"suspicious root files: {suspicious}")
    print("path hygiene: PASS")

def check_security_policy() -> None:
    text = read("SECURITY.md")
    for token in ["security@axonos.org", "raw neural data", "upstream OpenBCI GUI"]:
        if token not in text:
            fail(f"SECURITY.md missing token: {token}")
    print("security policy: PASS")

CHECK_MAP = {
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
    if len(sys.argv) != 2 or sys.argv[1] not in CHECK_MAP:
        print("Usage: gateway_ci_checks.py <check>")
        print("Available checks:")
        for check in CHECKS:
            print(f"  - {check}")
        sys.exit(2)
    CHECK_MAP[sys.argv[1]]()

if __name__ == "__main__":
    main()
