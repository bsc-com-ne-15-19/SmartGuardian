#!/bin/ash

echo "Apply database migrations"
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

exec "$@"
