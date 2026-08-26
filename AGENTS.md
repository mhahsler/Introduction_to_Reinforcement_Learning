# Repository guidance

## Purpose and layout

- This repository contains teaching material for an introductory reinforcement
  learning course. Prefer clear, textbook-oriented implementations over clever
  abstractions or premature optimization.
- Topic directories such as `DP/`, `MC/`, `TD/`, `DRL/`, and
  `Policy_Gradient/` contain notebooks and a local README. Read the relevant
  README before changing material in that directory.
- Shared course utilities and installation notes live in `common/`.
- `common/gym-classics2/`, when present, is a standalone Python package and may
  be a nested Git checkout. Treat it as a separate project and modify it only
  when the task includes that package.

## Working conventions

- Preserve the pedagogical progression, terminology, and mathematical notation
  used by Sutton and Barto and by nearby course material.
- Keep examples readable for students. Prefer explicit intermediate steps and
  descriptive names when they make an algorithm easier to understand.
- Keep things short so students will not gloss over it.
- Follow the existing style in the file being changed; the repository does not
  enforce a single formatter across all historical teaching examples.
- Use the current Gymnasium API: `reset()` returns `(observation, info)`, and
  `step()` returns `(observation, reward, terminated, truncated, info)`.
- Make stochastic examples reproducible when practical. Prefer an explicit seed
  and `numpy.random.default_rng` for newly written code.
- Do not add assignment solutions or artifacts matching the solution patterns
  in `.gitignore`.
- Do not modify or regenerate binary slides, trained-model archives, images, or
  recorded videos unless the task explicitly requires those artifacts.

## Notebooks

- Keep notebook changes narrowly scoped. Do not reformat the entire notebook
  JSON, reorder unrelated cells, or clear all outputs unless requested.
- Preserve explanatory Markdown and ensure code remains consistent with the
  narrative immediately around it.
- Avoid executing long training runs merely to validate a small edit. Use a
  reduced episode count or a focused smoke test when that adequately exercises
  the changed logic, and state any validation limitation in the handoff.
- Never commit transient notebook output such as new videos, logs, checkpoints,
  caches, or virtual environments.

## Setup and validation

- Use `common/README.md` for the course environment and optional visualization
  dependencies. Do not commit a local virtual environment.
- Keep the stablebasline3 dependency separate from the regular environment in environment.yml.
- Validate in proportion to the change. For a standalone Python file, at least
  run `python -m py_compile <changed-file>` when imports are not needed.
- For an executable notebook, use a temporary output rather than overwriting the
  source during validation, for example:

  ```bash
  jupyter nbconvert --to notebook --execute path/to/notebook.ipynb \
    --output-dir=/tmp
  ```

- For changes inside `common/gym-classics2/`, install its test dependencies in
  an isolated environment and run:

  ```bash
  cd common/gym-classics2
  python -m pytest
  ```

- Report which checks were run and call out tests skipped because they require
  long training, rendering, unavailable system packages, or external services.
