FROM python:3.9-slim-buster

WORKDIR /lsdebt
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY lsdebt/ .

CMD ["gunicorn", "--workers=5", "--threads=1", "-b 0.0.0.0:8050", "index:server"]
