# Changelog

All notable changes to the AxonOS BCI Gateway fork relative to upstream
[OpenBCI_GUI](https://github.com/OpenBCI/OpenBCI_GUI).

Upstream base: **OpenBCI_GUI v6.0.0-beta.1**

---

## [1.0.0-axonos] — 2026-04-30

### Added
- `Copyright (c) 2024–2026 AxonOS-org` line to LICENSE (alongside original
  OpenBCI copyright — both preserved as required by MIT).
- `.gitignore` covering Processing/Java build artifacts, IDE files, OS files,
  and session data.
- This CHANGELOG.
- `.github/workflows/ci.yml` — branding consistency checks on push and PR.

### Changed
- **Application version string:** `v6.0.0-beta.1` → `v1.0.0-axonos`
  (`OpenBCI_GUI/OpenBCI_GUI.pde`)
- **Version date:** `September 2023` → `April 2026`
  (`OpenBCI_GUI/OpenBCI_GUI.pde`)
- **Startup message:** `Welcome to the Processing-based OpenBCI GUI!` →
  `Welcome to the AxonOS BCI Gateway!`
  (`OpenBCI_GUI/OpenBCI_GUI.pde`)
- **Documentation URL:** `docs.openbci.com/Software/OpenBCISoftware/GUIDocs/` →
  `axonos.org/docs`
  (`OpenBCI_GUI/OpenBCI_GUI.pde`)
- **Release API URL:** `api.github.com/repos/OpenBCI/OpenBCI_GUI/releases/latest` →
  `api.github.com/repos/AxonOS-org/axon-bci-gateway/releases/latest`
  (`OpenBCI_GUI/OpenBCI_GUI.pde`)
- **GitHub release URL:** `github.com/OpenBCI/OpenBCI_GUI/releases/latest` →
  `github.com/AxonOS-org/axon-bci-gateway/releases/latest`
  (`OpenBCI_GUI/OpenBCI_GUI.pde`)
- **LSL stream identifier:** `openbcigui` → `axonos-gateway`
  (`OpenBCI_GUI/NetworkStreamOut.pde`)
- **OSC base address:** `/openbci` → `/axonos`
  (`OpenBCI_GUI/W_Networking.pde`)
- **LSL default stream names:** `obci_eeg1/2/3` → `axon_eeg1/2/3`
  (`OpenBCI_GUI/W_Networking.pde`)
- **Networking guide URL:** `docs.openbci.com/...GUIWidgets/#networking` →
  `axonos.org/docs/networking`
  (`OpenBCI_GUI/W_Networking.pde`)
- **Data outputs URL:** Google Docs link → `axonos.org/docs/data-outputs`
  (`OpenBCI_GUI/W_Networking.pde`)
- **README.md** rewritten: AxonOS context, RFC links, clean attribution.
- **CONTRIBUTING.md** rewritten: AxonOS-org workflow (`master` branch),
  removed all references to `support@openbci.com` and `OpenBCI Forum`.

### Known limitations
- Upstream OpenBCI_GUI `v6.0.0-beta.1` bugs are inherited. Substantive fixes
  should be contributed to [OpenBCI/OpenBCI_GUI](https://github.com/OpenBCI/OpenBCI_GUI)
  upstream.
- No Processing build verification in CI (Processing headless builds are
  non-trivial; CI currently checks branding consistency only).
