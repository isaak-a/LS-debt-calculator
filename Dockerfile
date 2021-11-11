FROM python:3.9-slim-buster

WORKDIR /lsdebt

RUN apt-get update && apt-get install -y netcat
COPY --chown=root wait-for-postgres.sh .

COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir

COPY lsdebt/ .

CMD ["./wait-for-postgres.sh", "gunicorn", "--workers=5", "--threads=1", "--log-level=DEBUG", "-b 0.0.0.0:8050", "index:server"]
