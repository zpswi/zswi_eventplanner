FROM python:3.12-alpine

WORKDIR /app

RUN apk --no-cache --update add pipx
RUN apk add --virtual build-deps gcc python3-dev musl-dev
RUN apk add --no-cache mariadb-dev
RUN pipx install poetry

ENV PATH="/root/.local/bin:$PATH"

ENTRYPOINT ["docker/entrypoint.sh"]