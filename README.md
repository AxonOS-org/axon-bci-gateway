# AxonOS BCI Gateway

> Integration fork of [OpenBCI_GUI v6.0.0-beta.1](https://github.com/OpenBCI/OpenBCI_GUI),
> maintained by [AxonOS-org](https://axonos.org) for hardware-in-the-loop testing
> with the AxonOS real-time neural kernel.

**Looking for the main AxonOS project?** → [axonos.org](https://axonos.org)  
**Engineering RFCs and architecture?** → [github.com/AxonOS-org/axonos-rfcs](https://github.com/AxonOS-org/axonos-rfcs)

---

## What this is

This gateway provides a Processing-based GUI for streaming EEG data from
OpenBCI Cyton / Ganglion hardware into the AxonOS signal pipeline. It is
intentionally kept close to upstream OpenBCI_GUI to minimise maintenance
burden. AxonOS-specific changes are limited to networking identifiers, branding,
and documentation pointers — see [CHANGELOG.md](CHANGELOG.md) for the full diff.

This repository is **not** a reimplementation of OpenBCI_GUI. All signal
acquisition, hardware communication, and GUI logic is OpenBCI's work,
licensed under MIT (see [LICENSE](LICENSE)).

---

## Quick start

**Requirements:** [Processing 4](https://processing.org/download) with the
following libraries (install via Processing → Tools → Manage Libraries):
`ControlP5`, `G4P`, `gwoptics`, `BrainFlow`.

```bash
# 1. Clone
git clone https://github.com/AxonOS-org/axon-bci-gateway.git
cd axon-bci-gateway

# 2. Open in Processing
# File → Open → OpenBCI_GUI/OpenBCI_GUI.pde

# 3. Run (⌘R / Ctrl+R)
```

When running, the LSL stream identifier is `axonos-gateway` and the OSC
base address is `/axonos`. Configure your AxonOS pipeline consumer accordingly.

---

## Version

| Field | Value |
|---|---|
| Gateway version | `v1.0.0-axonos` |
| Based on upstream | OpenBCI_GUI `v6.0.0-beta.1` |
| AxonOS SDK | [axonos-sdk v0.1.1](https://github.com/AxonOS-org/axonos-sdk) |

---

## AxonOS reference target

The gateway is tested against the AxonOS reference hardware:

| Component | Part |
|---|---|
| ADC | ADS1299 · 8-channel · 24-bit · 250 SPS |
| DSP core | STM32F407 Cortex-M4F · 168 MHz |
| Wireless | nRF52840 · BLE 5.3 |

For pipeline timing specifications (WCET, WCRT, validation evidence levels),
see [RFC-0004](https://github.com/AxonOS-org/axonos-rfcs/blob/main/rfcs/0004-dual-core-real-time-contract.md)
and the [AxonOS validation framework (RFC-0003)](https://github.com/AxonOS-org/axonos-rfcs/blob/main/rfcs/0003-validation-status-framework.md).
Performance numbers are tagged by evidence level (L1/L2/L3) — not standalone
marketing claims.

---

## Changes from upstream

See [CHANGELOG.md](CHANGELOG.md) for a complete list of modifications.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

This fork preserves the upstream MIT license in full.  
Copyright (c) 2018 OpenBCI — original work.  
Copyright (c) 2024–2026 AxonOS-org — modifications listed in CHANGELOG.md.

See [LICENSE](LICENSE) for the complete text.

---

## Contact

- Website: [axonos.org](https://axonos.org)
- General: [info@axonos.org](mailto:info@axonos.org)
- Bugs and PRs: [GitHub Issues](../../issues)
