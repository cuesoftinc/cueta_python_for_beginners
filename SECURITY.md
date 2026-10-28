# Security Policy

## Supported Versions

The repository holds course material only and has no deployed service. Fixes are applied to `main`.

## Reporting a Vulnerability

Do not use the regular issue tracker. Report vulnerabilities through the repository's **Security > Report a vulnerability** flow. If that option is unavailable, email `security@cuesoft.io` with the subject `Security vulnerability: cueta_python_for_beginners`.

Include the impact, the affected file or component, reproduction steps and any suggested mitigation. Do not include credentials or confidential material. We aim to acknowledge reports within three business days.

## Secret and Data Handling

- Never commit `.env` files, keys, student data or unpublished client material.
- Use synthetic data in examples and screenshots.
- Rotate a credential immediately if exposure is suspected.
