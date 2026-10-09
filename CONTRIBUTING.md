# Contributing to Sash

Thanks for contributing! This document outlines how to run, test, and submit changes.

## Quick start

```bash
# Clone and enter the repo
git clone https://github.com/FriesRdBest/Sash.git && cd Sash

# Create a virtual environment
python -m venv .venv && source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the UI (demo mode)
streamlit run app.py

# Run tests
python -m pytest tests/ -q

# Lint
ruff check .
```

## Pull requests

Open a PR against `main`. In your PR description, include:
- Purpose and scope.
- Design changes (if any).
- Evidence (tests, logs, screenshots).
- Failure behavior and security/privacy considerations.
- Documentation updates (README, docs/).

## Coding standards

- Format with `ruff` (imports) and keep code simple.
- Add tests for new logic, especially reliability and security paths.
- Do not commit secrets; use environment variables and `.env.example`.

## Questions?

Open an issue or discuss in the PR. We prefer small, iterative changes with clear evidence.
