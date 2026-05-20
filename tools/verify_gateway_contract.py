#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)

def read(path: str) -> str:
    p = ROOT / path
    if not p.exists():
        fail(f"missing required file: {path}")
    return p.read_text(encoding="utf-8", errors="replace")

def require_file(path: str) -> None:
    if not (ROOT / path).is_file():
        fail(f"missing required file: {path}")
    print(f"ok file: {path}")

def require_dir(path: str) -> None:
    if not (ROOT / path).is_dir():
        fail(f"missing required directory: {path}")
    print(f"ok dir: {path}")

def require_contains(path: str, needle: str) -> None:
    text = read(path)
    if needle not in text:
        fail(f"{path} must contain: {needle!r}")
    print(f"ok text: {path} contains {needle!r}")

def require_not_contains(path: str, needle: str) -> None:
    text = read(path)
    if needle in text:
        fail(f"{path} must not contain stale text: {needle!r}")
    print(f"ok text: {path} does not contain {needle!r}")

def main() -> None:
    for path in [
        "README.md",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "LICENSE",
        "NOTICE",
        ".github/workflows/ci.yml",
    ]:
        require_file(path)

    for path in [
        "OpenBCI_GUI",
        "GuiUnitTests",
        "Networking-Test-Kit",
    ]:
        require_dir(path)

    require_file("OpenBCI_GUI/OpenBCI_GUI.pde")

    require_contains("README.md", "integration fork")
    require_contains("README.md", "OpenBCI")
    require_contains("README.md", "AxonOS")
    require_contains("README.md", "connect@axonos.org")
    require_contains("NOTICE", "OpenBCI")
    require_contains("NOTICE", "MIT")

    require_not_contains("README.md", "info@axonos.org")
    require_not_contains("README.md", "AxonOS-sdk")
    require_not_contains("README.md", "AxonOS-kernel")

    print("\nAxonOS BCI Gateway contract: PASS")

if __name__ == "__main__":
    main()
