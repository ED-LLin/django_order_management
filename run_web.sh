#!/bin/sh

# Wait for PostgreSQL to start
while ! nc -z db 7432; do
  echo "Waiting for PostgreSQL to start..."
  sleep 1
done

# Start Django
python manage.py runserver 0.0.0.0:8008