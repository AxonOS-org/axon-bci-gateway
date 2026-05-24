# axon-bci-gateway — AxonOS context

This repository is a **fork of the OpenBCI GUI project**. Its upstream
`README.md` is the OpenBCI project's own documentation and is retained
unchanged so that the fork stays mergeable with upstream.

This file explains why the fork exists within the AxonOS organisation.

## Role within AxonOS

`axon-bci-gateway` is the **acquisition-boundary gateway** of the AxonOS
stack. It is used for hardware-in-the-loop EEG acquisition and for
pipeline testing against real OpenBCI hardware. It sits *below* the
AxonOS real-time kernel, on the hardware side of the acquisition
boundary.

It is **not** a safety-relevant AxonOS component. The real-time
guarantees, the neural-permission model, and the consent enforcement of
AxonOS live in the dedicated repositories — not here. This fork is an
acquisition and test harness.

## Where the AxonOS project actually is

| Repository | Role |
| --- | --- |
| [`axonos-standard`](https://github.com/AxonOS-org/axonos-standard) | Canonical technical standard |
| [`axonos-kernel`](https://github.com/AxonOS-org/axonos-kernel) | Real-time kernel substrate |
| [`axonos-consent`](https://github.com/AxonOS-org/axonos-consent) | Consent finite-state machine |
| [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) | Typed-intent application SDK |
| [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) | Engineering RFCs |
| [`axonos-swarm`](https://github.com/AxonOS-org/axonos-swarm) | Distributed coordination research |

Start at [`AxonOS-org/AxonOS`](https://github.com/AxonOS-org/AxonOS) —
the project entry point — or at <https://axonos.org>.

## Licensing

The forked OpenBCI GUI code retains its upstream licence. AxonOS-specific
additions, where present, follow the AxonOS dual Apache-2.0 / MIT policy.

---

The AxonOS Project · <https://axonos.org> · connect@axonos.org
