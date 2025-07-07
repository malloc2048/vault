FROM python:3.13-slim AS builder

RUN mkdir -p /app
WORKDIR /app

COPY ./vault /app/vault
COPY readme.md /app/readme.md
COPY pyproject.toml /app/pyproject.toml

RUN pip install poetry && poetry config virtualenvs.in-project true --local && poetry install

ENV PATH="/app/vault/.venv/bin:$PATH"

RUN apt-get update && apt-get -q install -y git zsh vim curl
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

CMD ["poetry", "run", "gunicorn", "-c", "vault/config/gunicorn.conf.py", "vault:app"]
