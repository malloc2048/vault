FROM ghcr.io/astral-sh/uv:debian-slim

RUN mkdir -p /app
WORKDIR /app

COPY ./vault /app/vault
COPY readme.md /app/readme.md
COPY pyproject.toml /app/pyproject.toml

RUN uv sync

CMD ["uv", "run", "gunicorn", "-c", "vault/config/gunicorn.conf.py", "vault:app"]
