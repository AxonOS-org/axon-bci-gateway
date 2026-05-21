# AxonOS BCI Gateway

[![CI](https://github.com/AxonOS-org/axon-bci-gateway/actions/workflows/ci.yml/badge.svg)](https://github.com/AxonOS-org/axon-bci-gateway/actions/workflows/ci.yml)
![License](https://img.shields.io/badge/license-MIT-blue)
![Status](https://img.shields.io/badge/status-integration--fork-lightgrey)
![Runtime](https://img.shields.io/badge/runtime-Processing%20%2F%20Java-006699)

**OpenBCI GUI integration fork for AxonOS hardware-in-the-loop EEG acquisition and pipeline testing.**

`axon-bci-gateway` sits at the acquisition boundary of the AxonOS stack. It
preserves the upstream OpenBCI GUI structure and limits AxonOS-specific changes
to integration touchpoints: stream naming, OSC namespace, documentation,
attribution, reference-hardware notes, and fork-integrity CI.

This repository is not a rewrite of OpenBCI GUI. Signal acquisition, hardware
communication, GUI behavior, and BrainFlow integration remain upstream OpenBCI
work under the MIT License.

## Position in the AxonOS stack

AxonOS is the deterministic operating layer between neural hardware and
intelligent applications.

| Layer | Repository | Role |
|---|---|---|
| Standard | `axonos-standard` | draft standard, evidence vocabulary, validation discipline |
| Kernel substrate | `axonos-kernel` | real-time scheduling, bounded IPC, monotonic time |
| RFCs | `axonos-rfcs` | engineering contracts and design records |
| SDK boundary | `axonos-sdk` | typed intent and capability boundary |
| Consent layer | `axonos-consent` | runtime consent and safety-state semantics |
| Acquisition gateway | `axon-bci-gateway` | OpenBCI GUI integration fork for EEG input |

The gateway lets AxonOS interact with real acquisition tools without pretending
that the gateway itself is the safety-critical kernel.

## Scope

AxonOS-specific scope is limited to:

- LSL stream identifier convention: `axonos-gateway`;
- OSC namespace convention: `/axonos`;
- AxonOS documentation pointers;
- reference-hardware compatibility notes;
- attribution and fork-maintenance metadata;
- CI checks that verify the fork contract.

Out of scope:

- changing OpenBCI acquisition behavior;
- modifying board communication logic;
- changing GUI widgets unrelated to AxonOS integration;
- claiming regulatory or clinical readiness;
- claiming kernel timing performance;
- claiming that this fork is endorsed by OpenBCI, Inc.

If a change improves OpenBCI GUI generally, it belongs upstream first.

## Gateway contract

| Contract item | Meaning |
|---|---|
| Acquisition boundary | the fork preserves upstream OpenBCI GUI acquisition paths |
| AxonOS identity | integration uses explicit stream and OSC naming conventions |
| Attribution | upstream OpenBCI authorship and MIT licensing remain visible |
| No safety overclaim | timing, clinical, and regulatory claims are not made here |
| Fork hygiene | CI verifies structure, attribution, docs, and AxonOS scope |

This is an integration gateway, not a certified medical-device component and not a hard real-time kernel.

## Quick start

Requirements:

- Processing 4;
- Processing libraries installed through **Tools → Manage Libraries**:
  - `ControlP5`;
  - `G4P`;
  - `gwoptics`;
  - `BrainFlow`.

Clone and open:

```bash
git clone https://github.com/AxonOS-org/axon-bci-gateway.git
cd axon-bci-gateway
```

Then open in Processing:

```text
OpenBCI_GUI/OpenBCI_GUI.pde
```

Run with `Ctrl+R` / `Cmd+R`.

When running with AxonOS integration configuration, downstream consumers should
expect:

| Channel | Value |
|---|---|
| LSL stream identifier | `axonos-gateway` |
| OSC base namespace | `/axonos` |

## Version and compatibility

| Field | Value |
|---|---|
| Gateway status | integration fork |
| Base upstream | OpenBCI_GUI `v6.0.0-beta.1` |
| Language/runtime | Processing / Java |
| License | MIT |
| AxonOS contact | `connect@axonos.org` |

Compatibility notes:

- AxonOS kernel and SDK integration is evolving.
- This repository does not define the AxonOS ABI.
- Timing and safety claims belong in `axonos-kernel`, `axonos-rfcs`, and
  hardware validation artifacts, not in this GUI fork.

## AxonOS Standard mapping

| Standard artifact | Relevance |
|---|---|
| AOS-0001 System Boundary | defines the gateway as an acquisition boundary |
| AOS-0003 Evidence Levels and Claims | prevents timing and clinical overclaim |
| AOS-0008 IPC and Timing Contract | applies only to downstream real-time integration claims |
| AOS-0010 Reference Implementation Mapping | maps gateway status as integration fork |
| AOS-0012 Hardware Validation Protocol | governs future L3 hardware timing claims, not this GUI fork |

## Reference hardware context

The gateway is intended for hardware-in-the-loop testing around the AxonOS
reference platform.

| Component | Reference part |
|---|---|
| EEG ADC | ADS1299 · 8-channel · 24-bit · 250 SPS |
| DSP / real-time core | STM32F407 · Cortex-M4F · 168 MHz |
| Application core | Cortex-A53 |
| Wireless | nRF52840 · BLE |
| Secure element | ATECC608B |
| Isolation | ISO7741 · galvanic isolation |

## Repository structure

```text
axon-bci-gateway/
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── NOTICE
├── SECURITY.md
├── .github/workflows/ci.yml
├── tools/gateway_ci_checks.py
├── OpenBCI_GUI/
├── GuiUnitTests/
├── Networking-Test-Kit/
├── images/
└── release/
```

The upstream source tree is deliberately preserved to keep future rebases
tractable.

## CI philosophy

This is a Processing GUI fork, not a Cargo, Maven, Gradle, or Rust kernel
project.

The CI therefore checks the fork contract:

1. required repository structure exists;
2. attribution to OpenBCI is preserved;
3. AxonOS scope is described accurately;
4. README, NOTICE, CHANGELOG, and SECURITY stay consistent;
5. no clinical, regulatory, or kernel-performance overclaim is introduced;
6. workflow and repository metadata remain readable.

The CI does not attempt to compile the full Processing GUI, because that requires
the Processing runtime and GUI libraries that are not part of a normal headless
GitHub Actions environment.

## What this repository does not claim

This repository does not claim:

- certified medical-device readiness;
- OpenBCI endorsement;
- safety-critical kernel behavior;
- kernel timing performance claims;
- regulatory compliance;
- replacement of OpenBCI GUI;
- ownership of upstream OpenBCI acquisition code.

The intended claim is narrower:

> This repository is an AxonOS-maintained integration fork of OpenBCI_GUI for
> hardware-in-the-loop EEG acquisition and AxonOS pipeline integration.

## Contributing

Use this rule first:

> Does the change belong upstream in OpenBCI_GUI, or only in the AxonOS fork?

Belongs upstream:

- board support;
- GUI widget behavior;
- acquisition bug fixes;
- BrainFlow improvements;
- general OpenBCI usability improvements.

Belongs here:

- AxonOS stream/OSC naming;
- AxonOS documentation;
- AxonOS reference-hardware notes;
- CI and fork-contract checks;
- attribution and NOTICE maintenance.

See `CONTRIBUTING.md`.

## License and attribution

This fork preserves the upstream MIT License.

- Original work: OpenBCI GUI by Joel Murphy and OpenBCI contributors.
- AxonOS fork maintenance: Denis Yermakou / AxonOS-org.
- AxonOS modifications are listed in `CHANGELOG.md`.
- Attribution and trademark scope are documented in `NOTICE`.

This fork does not claim affiliation with, endorsement by, or sponsorship from
OpenBCI, Inc.

## Contact

General: connect@axonos.org  
Security disclosures: security@axonos.org  
Project: https://axonos.org
