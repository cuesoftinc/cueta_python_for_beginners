# Contributing

This repository is maintained by the Cuesoft team and open to outside contributions. The course is four weeks, each with a `student/` exercise file, a `solutions/` reference and a `tests/` folder.

## Getting started

1. Fork the repository, or clone it if you are a member of the organization.
2. Install Python 3. The course uses the standard library only, so there is nothing else to install.
3. Create a focused branch named `<feature|bugfix>/<short-description>`.

## Before opening a pull request

Run the reference solutions against the tests of each week you changed, from that week's folder:

```bash
python run_solution_tests.py
```

The student tests (`python run_tests.py`) are expected to fail until the exercises are completed, so a change to student files is checked by the solution run. Remove `.DS_Store` and `__pycache__` files before committing.

Use Conventional Commits (`feat:`, `fix:`, `chore:`, `docs:`), keep changes focused, and never commit credentials, personal data or `.env` files.

## Code review

At least one approving review from a maintainer is required before merge. Be responsive to review feedback.

## Code of Conduct

Participation is governed by our [Code of Conduct](CODE_OF_CONDUCT.md).
