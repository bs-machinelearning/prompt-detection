# Contributing

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and run
`uv sync`. Before submitting changes, run:

```sh
uv run ruff check .
uv run ruff format --check .
```

Run tests relevant to your changes. Follow the data, evaluation, security, and
Git guidance in `AGENTS.md`.
