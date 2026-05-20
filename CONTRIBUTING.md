# Contributing to axon-bci-gateway

Thank you for your interest in the AxonOS BCI Gateway.

This repository is an integration fork of OpenBCI_GUI. The first question for any contribution is:

> Does this change belong upstream in OpenBCI_GUI, or only in the AxonOS fork?

## Changes that belong upstream

Please contribute these to OpenBCI first:

- hardware drivers;
- GUI widget behavior;
- acquisition bugs;
- BrainFlow integration improvements;
- board communication changes;
- general Processing GUI improvements.

Upstream repository:

<https://github.com/OpenBCI/OpenBCI_GUI>

## Changes that belong in this fork

Open a pull request here for:

- AxonOS integration identifiers;
- AxonOS documentation links;
- AxonOS reference-hardware notes;
- fork metadata;
- `NOTICE`, `CHANGELOG`, and README corrections;
- CI checks for fork integrity.

## Local development

Install:

- Processing 4;
- `ControlP5`;
- `G4P`;
- `gwoptics`;
- `BrainFlow`.

Then open:

```text
OpenBCI_GUI/OpenBCI_GUI.pde
```

in Processing and run with `Ctrl+R` / `Cmd+R`.

## Pull request checklist

- The change belongs in this fork.
- Upstream OpenBCI copyright notices are preserved.
- `CHANGELOG.md` is updated if the change affects fork behavior.
- No broad reformatting of upstream source files.
- No clinical, regulatory, or kernel-performance claim is added to this GUI fork.
- `python3 tools/verify_gateway_contract.py` passes locally.

## Security disclosures

Do not open a public issue for security-sensitive matters.

Email:

```text
security@axonos.org
```

## License

By contributing to this repository, you agree that your contribution is licensed under the MIT License, matching the upstream OpenBCI GUI license.
