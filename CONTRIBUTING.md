# Contributing to axon-bci-gateway

`axon-bci-gateway` is an AxonOS integration fork of OpenBCI GUI.

The first question for every change is:

> Does this belong upstream in OpenBCI GUI, or only in the AxonOS fork?

## Belongs upstream

Contribute these changes to OpenBCI GUI first:

- board support;
- signal acquisition fixes;
- GUI widget behavior;
- BrainFlow improvements;
- general OpenBCI usability improvements.

## Belongs in this fork

Contribute these changes here:

- AxonOS stream and OSC naming;
- AxonOS documentation;
- AxonOS reference-hardware notes;
- fork-contract CI;
- attribution and NOTICE maintenance.

## Pull-request checklist

- The change belongs in this fork.
- Upstream copyright notices are preserved.
- `CHANGELOG.md` is updated for AxonOS-specific changes.
- README does not introduce timing, clinical, regulatory, or kernel-performance
  claims.
- Security-sensitive issues are reported privately to `security@axonos.org`.

## License

Contributions are licensed under the MIT License, matching the upstream OpenBCI
GUI license and this fork.
