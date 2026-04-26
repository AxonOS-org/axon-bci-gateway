# AxonOS — OpenBCI_GUI Integration Fork

> This is an integration fork of [OpenBCI_GUI](https://github.com/OpenBCI/OpenBCI_GUI), maintained for compatibility testing between AxonOS and OpenBCI Cyton / Ganglion hardware.
>
> **Looking for the main AxonOS project?** → [axonos.org](https://axonos.org)

## About AxonOS

AxonOS is an open-source real-time neural operating system for brain–computer interfaces — built in Rust `#![no_std]` on ARMv8-M, with sub-millisecond hard real-time guarantees for closed-loop BCI signal processing. Often described as *"Linux for the brain,"* AxonOS provides the foundational platform layer that clinical and research BCI applications run on top of.

### Core technical specifications

- **Compute:** Dual-core — STM32F407 M4F @ 168 MHz (DSP) + Cortex-A53 @ 1.2 GHz (App), shared-SRAM IPC ≤ 0.2 µs
- **Front-end:** ADS1299 8-channel 24-bit @ 250 SPS, ISO7741 5 kV medical isolation
- **Real-time:** WCRT 972 µs measured over 12 h / 10.8 M epochs, zero deadline misses; jitter 2.1 µs σ, 6.5 µs P99.9
- **Classification:** 82.4 % 4-class (full calibration), 91.7 % 2-class (ZeroCalib, ~70 s warmup)
- **Security:** ATECC608B secure element, NIST SP 800-90B RNG, Cognitive Hypervisor on TrustZone-S
- **Power:** 300–500 mW; ~4 h autonomy on 800 mAh LiPo
- **Wireless:** nRF52840 BLE 5.3, Neural PTP clock sync (±18 µs over BLE mesh)

### Why this fork

We use this fork to validate AxonOS's intent-classification and ZeroCalib pipelines against live OpenBCI Cyton / Ganglion data streams during hardware-in-the-loop testing. Modifications are intentionally minimal — see commits ahead of `OpenBCI/OpenBCI_GUI:master`. Full credit for OpenBCI_GUI belongs to the OpenBCI team; this is not redistributed as a product.

## Links

- Project: [axonos.org](https://axonos.org)
- Technical writing (38+ articles): [medium.com/@AxonOS](https://medium.com/@AxonOS)
- Contact: **axonosorg@gmail.com**

## License

This fork preserves the upstream OpenBCI_GUI license. AxonOS's own crates (`axonos-consent`, `axonos-intent`, etc.) live in separate repositories and are dual-licensed Apache-2.0 / MIT unless noted otherwise.
