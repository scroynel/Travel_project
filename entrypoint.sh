#!/bin/sh

# Stop on any error
set -e

# A function to wait for the database (so that Django doesn't crash on startup)
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting PostgreSQL..."
    # Check the availability of the database port (usually 5432)
    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done
    echo "PostgreSQL запущен!"
fi

echo "--> Applying migrations..."
python manage.py migrate --noinput

echo "--> Setting up initial data..."
python manage.py shell <<EOF
from django.contrib.auth.models import User

# 1. Superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@gmail.com', 'admin')
    print('✅ Superuser created')
EOF
# hand over control to the main (runserver)
exec "$@"