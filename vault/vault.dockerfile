FROM python:3.10-slim AS builder

RUN mkdir -p /home/vault
WORKDIR /home/vault

COPY vault /home/vault/vault
COPY readme.md /home/vault/readme.md
COPY pyproject.toml /home/vault/pyproject.toml

RUN pip install poetry && poetry config virtualenvs.in-project true --local && poetry install


FROM builder AS final
ENV PATH="/home/vault/.venv/bin:$PATH"
COPY --from=builder /home/vault/.venv /home/vault/.venv

RUN apt-get update && apt-get -q install -y git zsh vim curl
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

RUN mkdir -p /home/vault
WORKDIR /home/vault

COPY vault /home/vault/vault
CMD ["gunicorn", "-c", "vault/config/gunicorn.conf.py", "vault:app"]
