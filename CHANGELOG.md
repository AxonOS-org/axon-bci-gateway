# Changelog

All notable AxonOS-fork-specific changes to this repository are documented here.

Upstream OpenBCI GUI changes are not duplicated in this file. For upstream history, see the original OpenBCI GUI repository:

<https://github.com/OpenBCI/OpenBCI_GUI>

This fork uses AxonOS-specific version suffixes such as `-axonos` to separate fork metadata from upstream OpenBCI releases.

---

## [Unreleased]

### Added

- Repository contract verifier: `tools/verify_gateway_contract.py`.
- CI workflow for fork-integrity, attribution, documentation, and AxonOS scope.
- README structure aligned with the AxonOS repository family.

### Changed

- Repository positioning clarified as an integration fork, not a reimplementation.
- Contact address standardised to `connect@axonos.org`.
- Repository claims narrowed to hardware-in-the-loop gateway integration.

---

## [v1.0.0-axonos] — 2024-Q1

Initial AxonOS integration fork based on OpenBCI_GUI `v6.0.0-beta.1`.

### Added

- AxonOS fork metadata.
- `NOTICE` file preserving upstream attribution.
- AxonOS reference-hardware notes.
- AxonOS documentation pointers.
- CI scaffolding for documentation and fork-integrity checks.

### Changed

- Integration naming conventions:
  - LSL stream identifier: `axonos-gateway`
  - OSC base namespace: `/axonos`
- Documentation and About text updated to reference AxonOS integration scope.

### Preserved

- OpenBCI signal acquisition logic.
- OpenBCI hardware communication logic.
- OpenBCI GUI structure.
- BrainFlow integration.
- Upstream MIT License.
- Upstream copyright notices.
