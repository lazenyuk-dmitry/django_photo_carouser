#!/bin/bash

DB_HOST_NAME=${DB_HOST:-db}
DB_PORT_NUM=${DB_PORT:-3306}

# Проверка готовности
until printf "" 2>>/dev/null >>/dev/tcp/$DB_HOST_NAME/$DB_PORT_NUM; do
    echo "Waiting for database on ($DB_HOST_NAME)..."
    sleep 1
done

echo "Applying migrations..."
python manage.py migrate --noinput
python manage.py createsuperuser --noinput || echo "Superuser already exists"

echo "Collecting static files..."
python manage.py compilescss
python manage.py collectstatic --noinput --ignore=*.scss

echo "Starting Gunicorn..."
exec gunicorn app.wsgi:application --bind 0.0.0.0:8000 --workers ${GUNICORN_WORKERS:-2}
