<div align="center">

<img src="https://upload.wikimedia.org/wikipedia/commons/d/dd/Processing_2021_logo.svg" width="100" alt="Processing" />

# AxonOS BCI Gateway

### Neural signal acquisition layer for AxonOS — fork of OpenBCI_GUI v6.0.0-beta.1

> Processing-based GUI bridge between OpenBCI Cyton/Ganglion hardware and the AxonOS real-time neural kernel. Maintained as an integration fork with minimal divergence from upstream.

[![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](#license)
[![Upstream](https://img.shields.io/badge/upstream-OpenBCI__GUI-blue?style=for-the-badge&logo=github&logoColor=white)](https://github.com/OpenBCI/OpenBCI_GUI)
[![AxonOS Project](https://img.shields.io/badge/AxonOS--org-0E2A47?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AxonOS-org)

[![Processing](https://img.shields.io/badge/Processing-4.x-006699?style=flat-square)](https://processing.org/download)
[![BrainFlow](https://img.shields.io/badge/BrainFlow-supported-success?style=flat-square)](https://brainflow.org)
[![SDK](https://img.shields.io/badge/axonos--sdk-0.1.6-orange?style=flat-square)](https://github.com/AxonOS-org/AxonOS-sdk)
[![Status](https://img.shields.io/badge/status-integration--fork-yellow?style=flat-square)](#about)

[**About**](#about) · [**Quick start**](#quick-start) · [**Reference hardware**](#axonos-reference-target) · [**Changes**](./CHANGELOG.md) · [**Contributing**](./CONTRIBUTING.md) · [**License**](#license)

</div>

---

## About

This gateway is an **integration fork** of [OpenBCI_GUI v6.0.0-beta.1](https://github.com/OpenBCI/OpenBCI_GUI),
maintained by [AxonOS-org](https://axonos.org) for hardware-in-the-loop testing
with the AxonOS real-time neural kernel.

It is **intentionally kept close to upstream** to minimise maintenance burden. AxonOS-specific changes are limited to:

- Networking identifiers (`LSL stream id = axonos-gateway`, `OSC base = /axonos`)
- Branding in window titles and About dialog
- Documentation pointers to AxonOS resources
- AxonOS reference hardware compatibility notes

For the complete diff against upstream, see [CHANGELOG.md](./CHANGELOG.md).

This repository is **not** a reimplementation. All signal acquisition,
hardware communication, and GUI logic is OpenBCI's work, licensed under MIT
(see [LICENSE](./LICENSE)).

> **Looking for the main AxonOS project?** → [axonos.org](https://axonos.org) · [github.com/AxonOS-org](https://github.com/AxonOS-org)

## Quick start

**Requirements:**

- [Processing 4](https://processing.org/download)
- Processing libraries (install via **Tools → Manage Libraries**): `ControlP5`, `G4P`, `gwoptics`, `BrainFlow`

```sh
# 1. Clone
git clone https://github.com/AxonOS-org/axon-bci-gateway.git
cd axon-bci-gateway

# 2. Open in Processing
# File → Open → OpenBCI_GUI/OpenBCI_GUI.pde

# 3. Run (⌘R / Ctrl+R)
```

When running, the LSL stream identifier is `axonos-gateway` and the OSC
base address is `/axonos`. Configure your AxonOS pipeline consumer accordingly.

## Version

| Field | Value |
|:---|:---|
| Gateway version | `v1.0.0-axonos` |
| Based on upstream | OpenBCI_GUI `v6.0.0-beta.1` |
| AxonOS SDK compatibility | [axonos-sdk v0.1.6](https://github.com/AxonOS-org/AxonOS-sdk) |
| AxonOS Kernel compatibility | [AxonOS-kernel v0.1.9](https://github.com/AxonOS-org/AxonOS-kernel) |

## AxonOS reference target

The gateway is tested against the AxonOS reference hardware platform:

| Component | Part |
|:---|:---|
| ADC | ADS1299 · 8-channel · 24-bit · 250 SPS |
| DSP core | STM32F407 · Cortex-M4F · 168 MHz |
| App core | Cortex-A53 · 1.2 GHz |
| Wireless | nRF52840 · BLE 5.3 |
| Secure element | ATECC608B |
| Isolation | ISO7741 · 5 kV galvanic |

For pipeline timing specifications (WCET, WCRT, validation evidence levels),
see [RFC-0004](https://github.com/AxonOS-org/axonos-rfcs/blob/main/rfcs/0004-dual-core-real-time-contract.md)
and the [AxonOS validation framework (RFC-0003)](https://github.com/AxonOS-org/axonos-rfcs/blob/main/rfcs/0003-validation-status-framework.md).
Performance numbers are tagged by evidence level (L1/L2/L3) — not standalone marketing claims.

## Repository structure

```
axon-bci-gateway/
├── README.md                       ← this file
├── CHANGELOG.md                    ← AxonOS-specific changes vs upstream
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE                         ← MIT (preserved from upstream)
├── NOTICE                          ← attribution + AxonOS modifications
├── .github/workflows/ci.yml        ← link check + actionlint
├── OpenBCI_GUI/                    ← Processing source (unchanged structure)
├── GuiUnitTests/                   ← upstream test suite
├── Networking-Test-Kit/            ← upstream networking tests
├── images/                         ← UI assets
├── release/                        ← release artifacts
└── tools/                          ← upstream tooling
```

## Changes from upstream

See [CHANGELOG.md](./CHANGELOG.md) for the complete list of modifications.
The diff is intentionally small and limited to integration touchpoints.

## Contributing

This fork accepts contributions that align with the AxonOS integration
scope. For changes to OpenBCI core GUI behaviour, please contribute
upstream to [OpenBCI/OpenBCI_GUI](https://github.com/OpenBCI/OpenBCI_GUI) first.

See [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

This fork preserves the upstream **MIT License** in full.

- Copyright © 2018 [Joel Murphy / OpenBCI](https://openbci.com) — original work
- Copyright © 2024–2026 Denis Yermakou / AxonOS-org — modifications listed in CHANGELOG.md

See [LICENSE](./LICENSE) for the complete text and [NOTICE](./NOTICE) for
detailed attribution and the AxonOS trademark policy.

## Related

- **[AxonOS-kernel](https://github.com/AxonOS-org/AxonOS-kernel)** — the verifiable kernel substrate
- **[AxonOS-sdk](https://github.com/AxonOS-org/AxonOS-sdk)** — application-side SDK
- **[axonos-rfcs](https://github.com/AxonOS-org/axonos-rfcs)** — engineering specifications
- **Project website:** [axonos.org](https://axonos.org)
- **Long-form essays:** [medium.com/@AxonOS](https://medium.com/@AxonOS)

## Contact

- **General correspondence:** [info@axonos.org](mailto:info@axonos.org)
- **Partnership and clinical engagement:** [connect@axonos.org](mailto:connect@axonos.org)
- **Security disclosures:** [security@axonos.org](mailto:security@axonos.org)
- **Bugs and pull requests:** [GitHub Issues](https://github.com/AxonOS-org/axon-bci-gateway/issues)

---

<div align="center">

**Author and maintainer (AxonOS-side):** Denis Yermakou · [denis@axonos.org](mailto:denis@axonos.org)

[axonos.org](https://axonos.org) · [medium.com/@AxonOS](https://medium.com/@AxonOS) · [github.com/AxonOS-org](https://github.com/AxonOS-org)

Zurich · Berlin · Milano · San Mateo · Singapore

<sub>The gateway is how the kernel earns the right to see real brain signals.</sub>

</div>
