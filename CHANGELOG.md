# Changelog

All notable AxonOS-fork-specific changes to this project are documented here.

Upstream OpenBCI GUI changes are not duplicated here. See the upstream
OpenBCI_GUI project for upstream history.

## [Unreleased]

### Added

- Seventeen-job repository contract CI.
- `tools/gateway_ci_checks.py` verifier.
- `SECURITY.md` with AxonOS security disclosure contact.
- AxonOS Standard mapping for the gateway boundary.
- Line-count guards for README, workflow, and checker integrity.

### Changed

- Rewrote README as multiline, audit-friendly Markdown.
- Clarified that the gateway is an integration fork.
- Standardized public contact address to `connect@axonos.org`.
- Replaced collapsed one-line workflow with readable GitHub Actions YAML.

### Fixed

- Removed stale uppercase repository links and old personal maintainer addresses.
- Removed overclaim-prone wording around public safety and timing claims.
- Reduced risk that public gateway docs imply kernel-level safety status.

## [v1.0.0-axonos] — 2024-Q1

Initial AxonOS fork from OpenBCI_GUI `v6.0.0-beta.1`.

### Added

- `NOTICE` file with attribution to OpenBCI upstream and AxonOS-side
  modifications.
- `CHANGELOG.md` tracking AxonOS-specific diff.
- AxonOS reference-hardware compatibility table in README.
- AxonOS stream and OSC naming conventions.

### Changed

- LSL stream identifier convention: `OpenBCI_EEG` to `axonos-gateway`.
- OSC base namespace convention: `/openbci` to `/axonos`.
- Documentation updated to describe the gateway as an AxonOS acquisition
  boundary.

### Preserved

- Signal acquisition logic.
- Hardware communication code.
- GUI widget behavior.
- BrainFlow integration.
- Upstream MIT license.
- Upstream OpenBCI attribution.

## Versioning policy

| Tag | Meaning |
|---|---|
| `vX.Y.Z` | upstream OpenBCI_GUI release where preserved verbatim |
| `vX.Y.Z-axonos` | AxonOS fork release based on upstream version |
| `vX.Y.Z-axonos.N` | Nth AxonOS-side patch on top of the fork release |

Maintainer: Denis Yermakou / AxonOS-org.
