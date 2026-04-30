# Contributing to AxonOS BCI Gateway

Thank you for considering a contribution.

## What kind of contributions are welcome

This repository is a thin integration fork of OpenBCI_GUI. Contributions
that make sense here:

- Bug fixes specific to the AxonOS integration (networking identifiers, LSL
  stream naming, OSC routing)
- Documentation updates
- CI improvements

Contributions that belong upstream:

- Changes to signal processing, hardware communication, or core GUI logic —
  please open these against [OpenBCI/OpenBCI_GUI](https://github.com/OpenBCI/OpenBCI_GUI)
  directly.

## Workflow

1. Fork the repository.
2. Create a branch from `master`:

   ```bash
   git checkout -b fix/describe-your-change
   ```

3. Make your changes.
4. Verify the branding consistency checks pass locally:

   ```bash
   grep -q "axonos-gateway" OpenBCI_GUI/NetworkStreamOut.pde
   grep -q "/axonos"         OpenBCI_GUI/W_Networking.pde
   grep -q "AxonOS-org"      LICENSE
   ```

5. Commit with a descriptive message and push.
6. Open a Pull Request against `master` with a clear description of what
   changed and why.

## Reporting issues

Please use [GitHub Issues](../../issues). Include:

- OS and Processing version
- Board type (Cyton / Ganglion / Synthetic)
- Steps to reproduce
- Relevant console output

## Code of conduct

Be direct and professional. No harassment, no spam.

## Contact

- Main project: [axonos.org](https://axonos.org)
- Email: [info@axonos.org](mailto:info@axonos.org)
