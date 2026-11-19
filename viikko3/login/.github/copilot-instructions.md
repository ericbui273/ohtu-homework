# Project Guidelines

## Architecture

- This is a small Flask login application.
- `src/app.py` contains routes and HTTP/UI behavior; `src/index.py` is the development server entry point.
- Keep application logic in `src/services/`, persistence in `src/repositories/`, domain models in `src/entities/`, and Jinja pages in `src/templates/`.
- `UserRepository` currently uses in-memory storage, so data is reset when the server process restarts.
- Robot Framework and Playwright tests live in `src/tests/`; `src/AppLibrary.py` provides HTTP helpers for test setup.

## Build and Test

- Use `uv` for dependency and command management from the repository root.
- Commands are run in the form `uv run ...`
- Python 3.14 is required: run `uv sync` to prepare the environment.
- Start the app with `uv run python src/index.py`; it listens on `http://localhost:5001`.
- Run acceptance tests with `uv run robot src/tests` while the app is running.
- Initialize the Chromium browser if needed with `uv run rfbrowser init chromium`.

## Conventions

- Preserve the existing small, layered structure; routes should delegate validation and authentication to `UserService`.
- Acceptance tests commonly call `/tests/reset` to isolate application state.
- Keep test-generated `log.html`, `output.xml`, `report.html`, `browser/`, and `playwright-log.txt` out of source edits; they are ignored by Git.
- Treat development-only settings in `src/app.py` and `src/index.py` as such: debug mode, host `0.0.0.0`, the reset route, and the hard-coded secret key are not production configuration.
