# Changelog

All notable AxonOS-fork-specific changes to this project are documented
in this file. Upstream OpenBCI_GUI changes are NOT duplicated here —
see the [upstream CHANGELOG](https://github.com/OpenBCI/OpenBCI_GUI/blob/master/CHANGELOG.md).

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this fork adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
with the suffix `-axonos` to distinguish from upstream releases.

---

## [Unreleased]

### Added
- This CHANGELOG file (was previously implicit via git history).

### Changed
- README rewritten with AxonOS unified visual standard (badges, footer,
  attribution to Denis Yermakou as fork maintainer).
- CONTRIBUTING.md rewritten to clarify upstream-vs-fork contribution paths.

---

## [v1.0.0-axonos] — 2024-Q1

Initial AxonOS fork from [OpenBCI_GUI v6.0.0-beta.1](https://github.com/OpenBCI/OpenBCI_GUI/releases/tag/v6.0.0-beta.1).

### AxonOS-specific changes vs upstream

#### Added
- `NOTICE` file with full attribution to OpenBCI upstream and AxonOS-side
  modifications (Denis Yermakou).
- `CHANGELOG.md` (this file) tracking AxonOS-specific diff.
- `.github/workflows/ci.yml` with link-check, markdownlint, actionlint,
  yamllint, java-syntax-check, and license-header job.
- `.github/markdown-link-check.json` configuration for link verification.
- AxonOS reference-hardware compatibility table in README.

#### Changed
- **Networking identifiers** to integrate with the AxonOS pipeline:
  - LSL stream identifier: `OpenBCI_EEG` → `axonos-gateway`
  - OSC base address: `/openbci` → `/axonos`
- **Branding** in window titles, splash screen, and About dialog:
  - "OpenBCI GUI" → "AxonOS BCI Gateway (based on OpenBCI_GUI)"
  - Where appropriate, attribution to both OpenBCI and AxonOS-org.
- **README.md** updated:
  - AxonOS branding header
  - Pointers to axonos.org, axonos-rfcs, AxonOS-kernel, AxonOS-sdk
  - Compatibility section for AxonOS reference hardware
- **CONTRIBUTING.md** updated to direct upstream-relevant changes to
  OpenBCI_GUI and fork-relevant changes here.

#### Preserved (unchanged from upstream)
- All signal acquisition logic
- All hardware communication code
- All GUI widget code
- All BrainFlow integration
- The upstream MIT licence in full
- Original copyright notices in source files

#### Maintainer note

The fork is **intentionally minimal**. Any change touching upstream OpenBCI
source must justify itself as integration-only — if it improves OpenBCI
behaviour generally, it belongs upstream first. This keeps rebasing against
future OpenBCI_GUI releases tractable.

---

## Versioning policy

| Tag             | Meaning |
|:----------------|:--------|
| `vX.Y.Z`        | upstream OpenBCI_GUI release (preserved verbatim) |
| `vX.Y.Z-axonos` | AxonOS fork release based on upstream `vX.Y.Z` |
| `vX.Y.Z-axonos.N` | Nth AxonOS-side patch on top of upstream `vX.Y.Z` |

Examples:
- `v6.0.0-beta.1` — base upstream release this fork started from
- `v1.0.0-axonos` — initial AxonOS fork release
- `v1.0.0-axonos.1` — first AxonOS patch on top of the initial fork
- `v6.1.0-axonos` — fork rebased against future upstream `v6.1.0`

---

**Maintainer:** Denis Yermakou · [denis@axonos.org](mailto:denis@axonos.org)
[github.com/AxonOS-org](https://github.com/AxonOS-org) · [axonos.org](https://axonos.org)
