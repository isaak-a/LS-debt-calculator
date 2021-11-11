FROM postgres:14.0-bullseye
COPY sql/* /docker-entrypoint-initdb.d/
