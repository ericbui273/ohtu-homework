# Project Guidelines

## Architecture

- `src/tuote.py` defines the `Tuote` product model.
- `src/ostos.py` defines a product-line purchase that tracks quantity and line price.
- `src/ostoskori.py` contains the basket implementation; currently many basket methods are placeholders and should be implemented only as tests require them.
- `src/index.py` is currently a placeholder for optional application code.

## Code Style

- Keep the existing Finnish domain vocabulary and method names, such as `Tuote`, `Ostos`, `Ostoskori`, `hinta`, `lisaa_tuote`, and `poista_tuote`.
- Follow the existing small, direct Python class style and expose state through methods instead of introducing a different API style.
- Keep internal fields underscore-prefixed and use direct sibling imports (for example, `from tuote import Tuote`).
- Maintain the currently minimal type annotations; add annotations consistently to public method signatures when extending the API.

## Build and Test

- Use Python 3.14 or newer.
- Install dependencies with `uv sync`.
- Run the test suite from the repository root with `uv run pytest`.
- For TDD work, always implement absolutely minimal code that makes the tests pass.

## Conventions

- Code of `ostos.py` and `tuote.py` should not be changed.
- Place tests in `src/tests/` and use `unittest.TestCase`/`setUp` consistently with the existing test style.
- Preserve `Ostos.muuta_lukumaaraa`: quantity changes below zero clamp the line quantity to zero.
- Do not assume an item can be negative in quantity or that an unimplemented basket method has a specified collection/return format; derive behavior from tests or explicit requirements.
- Tests should not be edited unless explicitly asked.