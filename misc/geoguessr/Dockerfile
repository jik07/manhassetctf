FROM python:slim AS app
RUN pip install --no-cache-dir progress

FROM pwn.red/jail
COPY --from=app / /srv
COPY main.py /srv/app/run
COPY location.txt /srv/app
COPY flag.txt /srv/app

ENV JAIL_MEM=20M JAIL_POW=5000 JAIL_ENV_NUM=5