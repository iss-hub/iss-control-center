FROM python:3.10-alpine

WORKDIR /app

RUN apk add --no-cache --virtual .build-deps \
  gcc \
  musl-dev

RUN pip install poetry
RUN poetry config --local virtualenvs.create false

COPY ./pyproject.toml ./
COPY ./poetry.lock ./
RUN poetry install --no-root

RUN apk del .build-deps

COPY ./ ./

# CMD ["uvicorn", "--help"]
CMD ["uvicorn", "iss-control-center.main:app", "--host", "0.0.0.0", "--port", "3000"]
