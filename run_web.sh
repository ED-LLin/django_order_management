#!/bin/sh

# Wait for PostgreSQL to start
sh wait-for-postgres.sh db
# Execute database migrations
python manage.py migrate
# Start Django
python manage.py runserver 0.0.0.0:8008