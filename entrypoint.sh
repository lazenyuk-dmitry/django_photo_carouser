#!/bin/bash

until printf "" 2>>/dev/null >>/dev/tcp/db/3306; do
    echo "Waiting for MySQL..."
    sleep 1
done

echo "Applying migrations..."
python manage.py migrate --noinput
python manage.py createsuperuser --noinput || echo "Superuser already exists"

echo "Collecting static files..."
python manage.py compilescss
python manage.py collectstatic --noinput --ignore=*.scss

echo "Starting Gunicorn..."
exec gunicorn app.wsgi:application --bind 0.0.0.0:8000 --workers 3
