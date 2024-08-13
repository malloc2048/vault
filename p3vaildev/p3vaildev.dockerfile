FROM python:3.10-slim AS builder

RUN mkdir -p /home/p3vaildev
WORKDIR /home/p3vaildev

COPY p3vaildev /home/p3vaildev/p3vaildev
COPY readme.md /home/p3vaildev/readme.md
COPY pyproject.toml /home/p3vaildev/pyproject.toml

RUN pip install poetry && poetry config virtualenvs.in-project true --local && poetry install

FROM builder AS final
ENV PATH="/home/p3vaildev/.venv/bin:$PATH"
COPY --from=builder /home/p3vaildev/.venv /home/p3vaildev/.venv

RUN apt-get update && apt-get -q install -y git zsh vim curl iputils-ping
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

RUN mkdir -p /home/p3vaildev
WORKDIR /home/p3vaildev

COPY data /home/p3vaildev/data
COPY p3vaildev /home/p3vaildev/p3vaildev
CMD ["gunicorn", "-c", "p3vaildev/config/gunicorn.conf.py", "p3vaildev:app"]
