#!/bin/bash

set -eu

while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
done

>&2 echo "Postgres is up - executing command"
exec "$@"
