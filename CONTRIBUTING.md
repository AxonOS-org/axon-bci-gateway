# Contributing to axon-bci-gateway

Thank you for your interest in the AxonOS BCI Gateway. This repository is
an **integration fork** of [OpenBCI_GUI](https://github.com/OpenBCI/OpenBCI_GUI),
so the contribution model is a little different from a typical project.

## Before you open a pull request — read this

The single most important question to answer first:

> **Does this change belong in OpenBCI_GUI upstream, or only in the AxonOS fork?**

### Belongs upstream (→ OpenBCI/OpenBCI_GUI)

- New GUI widgets, signal-processing improvements, hardware drivers
- Bug fixes in signal acquisition, board communication, recording
- New board support, BrainFlow integration improvements
- Performance improvements, refactoring
- Anything that benefits the wider OpenBCI community

Please contribute these to [OpenBCI/OpenBCI_GUI](https://github.com/OpenBCI/OpenBCI_GUI)
first. Once merged upstream, they will be pulled into this fork during
the next rebase.

### Belongs in this fork (→ AxonOS-org/axon-bci-gateway)

- AxonOS-specific networking identifiers (LSL stream id, OSC addresses)
- AxonOS branding in titles and About dialogs
- AxonOS hardware-platform compatibility notes
- AxonOS RFC link updates in documentation
- This repository's CI, NOTICE, CHANGELOG

## Local development

You will need:

- [Processing 4](https://processing.org/download)
- Libraries via **Processing → Tools → Manage Libraries**:
  - ControlP5
  - G4P
  - gwoptics
  - BrainFlow

```sh
git clone https://github.com/AxonOS-org/axon-bci-gateway.git
cd axon-bci-gateway
# File → Open → OpenBCI_GUI/OpenBCI_GUI.pde
# Run with ⌘R / Ctrl+R
```

## Pull-request checklist

- [ ] The change belongs in this fork (see above)
- [ ] [CHANGELOG.md](./CHANGELOG.md) updated with an entry under
      *Unreleased* listing your AxonOS-specific change
- [ ] If touching files originally authored by OpenBCI, the upstream
      copyright header is preserved
- [ ] No new external dependencies without prior discussion
- [ ] Any new external link in markdown is reachable (the CI link-check
      will fail otherwise)

## Code style

This fork follows OpenBCI_GUI upstream coding conventions. Do **not**
reformat large blocks of upstream code in your pull request — it
makes future rebases against upstream painful.

For new files authored by you under the AxonOS fork:

```java
/*
 * SPDX-License-Identifier: MIT
 * Copyright (c) 2024–2026 Denis Yermakou / AxonOS-org
 * Part of the AxonOS BCI Gateway — https://github.com/AxonOS-org/axon-bci-gateway
 *
 * Based on OpenBCI_GUI by Joel Murphy and the OpenBCI contributors.
 * Original MIT licence preserved — see LICENSE and NOTICE.
 */
```

## Reporting bugs

Open an [issue](https://github.com/AxonOS-org/axon-bci-gateway/issues)
with:

- Processing version
- BrainFlow library version
- OpenBCI hardware (Cyton / Ganglion / WiFi shield / etc.)
- AxonOS kernel and SDK version
- Minimal steps to reproduce
- Expected vs actual behaviour

If the bug also reproduces in upstream OpenBCI_GUI (without AxonOS
networking enabled), please report it upstream at
[OpenBCI/OpenBCI_GUI/issues](https://github.com/OpenBCI/OpenBCI_GUI/issues)
**in addition to here** so that the wider OpenBCI community benefits
from the fix.

## Security disclosures

Do **not** open a public issue for security-sensitive matters.
Email `security@axonos.org` directly. PGP key available on request.

## Code of conduct

See [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md). In short: be kind,
be specific, and assume good faith. This is a small project with
a single maintainer — your time and bandwidth is appreciated.

## License of your contribution

By submitting a pull request to this repository, you agree that your
contribution is licensed under the **MIT License** (same as the
upstream OpenBCI_GUI work and this fork). No separate Contributor
License Agreement is required (inbound = outbound model).

If your contribution is substantial, you may add yourself to the
list of contributors in NOTICE.

---

**Maintainer:** Denis Yermakou · [denis@axonos.org](mailto:denis@axonos.org)

[axonos.org](https://axonos.org) · [github.com/AxonOS-org](https://github.com/AxonOS-org)
